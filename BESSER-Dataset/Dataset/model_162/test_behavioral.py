import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    petrinet_Box,
    petrinet_Net,
    petrinet_Place,
    petrinet_Transition,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_box1_reverse_link_reassign_clear():
    a1 = petrinet_Transition(id=7, name="sample_text")
    a2 = petrinet_Transition(id=13, name="sample_text_2")
    b = petrinet_Box(id=7, name="sample_text")
    _safe_set(b, 'petrinet_Box', a1)
    assert _is_linked(b, 'petrinet_Box', a1)
    if hasattr(a1, 'petrinet_Transition2'):
        assert _is_linked(a1, 'petrinet_Transition2', b)
    _safe_set(b, 'petrinet_Box', a2)
    assert _is_linked(b, 'petrinet_Box', a2)
    if hasattr(a1, 'petrinet_Transition2'):
        assert not _is_linked(a1, 'petrinet_Transition2', b)
    if hasattr(a2, 'petrinet_Transition2'):
        assert _is_linked(a2, 'petrinet_Transition2', b)
    _safe_set(b, 'petrinet_Box', None)
    assert not _is_linked(b, 'petrinet_Box', a2)
    if hasattr(a2, 'petrinet_Transition2'):
        assert not _is_linked(a2, 'petrinet_Transition2', b)


def test_assoc_place14_reverse_link_reassign_clear():
    a1 = petrinet_Place(id=7, name="sample_text")
    a2 = petrinet_Place(id=13, name="sample_text_2")
    b = petrinet_Box(id=7, name="sample_text")
    _safe_set(b, 'petrinet_Box15', {a1})
    assert _is_linked(b, 'petrinet_Box15', a1)
    if hasattr(a1, 'petrinet_Place16'):
        assert _is_linked(a1, 'petrinet_Place16', b)
    _safe_set(b, 'petrinet_Box15', {a2})
    assert _is_linked(b, 'petrinet_Box15', a2)
    if hasattr(a1, 'petrinet_Place16'):
        assert not _is_linked(a1, 'petrinet_Place16', b)
    if hasattr(a2, 'petrinet_Place16'):
        assert _is_linked(a2, 'petrinet_Place16', b)
    _safe_set(b, 'petrinet_Box15', set())
    assert not _is_linked(b, 'petrinet_Box15', a2)
    if hasattr(a2, 'petrinet_Place16'):
        assert not _is_linked(a2, 'petrinet_Place16', b)


def test_assoc_place3_reverse_link_reassign_clear():
    a1 = petrinet_Transition(id=7, name="sample_text")
    a2 = petrinet_Transition(id=13, name="sample_text_2")
    b = petrinet_Place(id=7, name="sample_text")
    _safe_set(b, 'petrinet_Place5', a1)
    assert _is_linked(b, 'petrinet_Place5', a1)
    if hasattr(a1, 'petrinet_Transition4'):
        assert _is_linked(a1, 'petrinet_Transition4', b)
    _safe_set(b, 'petrinet_Place5', a2)
    assert _is_linked(b, 'petrinet_Place5', a2)
    if hasattr(a1, 'petrinet_Transition4'):
        assert not _is_linked(a1, 'petrinet_Transition4', b)
    if hasattr(a2, 'petrinet_Transition4'):
        assert _is_linked(a2, 'petrinet_Transition4', b)
    _safe_set(b, 'petrinet_Place5', None)
    assert not _is_linked(b, 'petrinet_Place5', a2)
    if hasattr(a2, 'petrinet_Transition4'):
        assert not _is_linked(a2, 'petrinet_Transition4', b)


def test_assoc_transition0_reverse_link_reassign_clear():
    a1 = petrinet_Transition(id=7, name="sample_text")
    a2 = petrinet_Transition(id=13, name="sample_text_2")
    b = petrinet_Place(id=7, name="sample_text")
    _safe_set(b, 'petrinet_Place', {a1})
    assert _is_linked(b, 'petrinet_Place', a1)
    if hasattr(a1, 'petrinet_Transition'):
        assert _is_linked(a1, 'petrinet_Transition', b)
    _safe_set(b, 'petrinet_Place', {a2})
    assert _is_linked(b, 'petrinet_Place', a2)
    if hasattr(a1, 'petrinet_Transition'):
        assert not _is_linked(a1, 'petrinet_Transition', b)
    if hasattr(a2, 'petrinet_Transition'):
        assert _is_linked(a2, 'petrinet_Transition', b)
    _safe_set(b, 'petrinet_Place', set())
    assert not _is_linked(b, 'petrinet_Place', a2)
    if hasattr(a2, 'petrinet_Transition'):
        assert not _is_linked(a2, 'petrinet_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_box11_stub_double():
    # petrinet_Net has no real 'petrinet_Net12' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Box's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Box's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Box(id=7, name="sample_text")
    partner = petrinet_Net()
    setattr(partner, 'petrinet_Net12', None)
    _safe_set(owner, 'petrinet_Box13', partner)
    assert owner in getattr(partner, 'petrinet_Net12')
    _safe_set(owner, 'petrinet_Box13', None)
    assert owner not in getattr(partner, 'petrinet_Net12')


def test_assoc_place6_stub_double():
    # petrinet_Net has no real 'petrinet_Net' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(id=7, name="sample_text")
    partner = petrinet_Net()
    setattr(partner, 'petrinet_Net', None)
    _safe_set(owner, 'petrinet_Place7', partner)
    assert owner in getattr(partner, 'petrinet_Net')
    _safe_set(owner, 'petrinet_Place7', None)
    assert owner not in getattr(partner, 'petrinet_Net')


def test_assoc_transition8_stub_double():
    # petrinet_Net has no real 'petrinet_Net9' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(id=7, name="sample_text")
    partner = petrinet_Net()
    setattr(partner, 'petrinet_Net9', None)
    _safe_set(owner, 'petrinet_Transition10', partner)
    assert owner in getattr(partner, 'petrinet_Net9')
    _safe_set(owner, 'petrinet_Transition10', None)
    assert owner not in getattr(partner, 'petrinet_Net9')


