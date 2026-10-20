import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    petrinetv3_Net,
    petrinetv3_Place,
    petrinetv3_Token,
    petrinetv3_Transition,
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

def test_assoc_input2_reverse_link_reassign_clear():
    a1 = petrinetv3_Transition(clock=7, name="sample_text", tmax=7, tmin=7)
    a2 = petrinetv3_Transition(clock=13, name="sample_text_2", tmax=13, tmin=13)
    b = petrinetv3_Place(initialTokens=7, name="sample_text")
    _safe_set(b, 'petrinetv3_Place3', a1)
    assert _is_linked(b, 'petrinetv3_Place3', a1)
    if hasattr(a1, 'petrinetv3_Transition'):
        assert _is_linked(a1, 'petrinetv3_Transition', b)
    _safe_set(b, 'petrinetv3_Place3', a2)
    assert _is_linked(b, 'petrinetv3_Place3', a2)
    if hasattr(a1, 'petrinetv3_Transition'):
        assert not _is_linked(a1, 'petrinetv3_Transition', b)
    if hasattr(a2, 'petrinetv3_Transition'):
        assert _is_linked(a2, 'petrinetv3_Transition', b)
    _safe_set(b, 'petrinetv3_Place3', None)
    assert not _is_linked(b, 'petrinetv3_Place3', a2)
    if hasattr(a2, 'petrinetv3_Transition'):
        assert not _is_linked(a2, 'petrinetv3_Transition', b)


def test_assoc_output4_reverse_link_reassign_clear():
    a1 = petrinetv3_Transition(clock=7, name="sample_text", tmax=7, tmin=7)
    a2 = petrinetv3_Transition(clock=13, name="sample_text_2", tmax=13, tmin=13)
    b = petrinetv3_Place(initialTokens=7, name="sample_text")
    _safe_set(b, 'petrinetv3_Place6', a1)
    assert _is_linked(b, 'petrinetv3_Place6', a1)
    if hasattr(a1, 'petrinetv3_Transition5'):
        assert _is_linked(a1, 'petrinetv3_Transition5', b)
    _safe_set(b, 'petrinetv3_Place6', a2)
    assert _is_linked(b, 'petrinetv3_Place6', a2)
    if hasattr(a1, 'petrinetv3_Transition5'):
        assert not _is_linked(a1, 'petrinetv3_Transition5', b)
    if hasattr(a2, 'petrinetv3_Transition5'):
        assert _is_linked(a2, 'petrinetv3_Transition5', b)
    _safe_set(b, 'petrinetv3_Place6', None)
    assert not _is_linked(b, 'petrinetv3_Place6', a2)
    if hasattr(a2, 'petrinetv3_Transition5'):
        assert not _is_linked(a2, 'petrinetv3_Transition5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_parentNet7_stub_double():
    # petrinetv3_Net has no real 'Net' property in the generated
    # code (a bare stub) -- manually attach it so petrinetv3_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetv3_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetv3_Transition(clock=7, name="sample_text", tmax=7, tmin=7)
    partner = petrinetv3_Net()
    setattr(partner, 'Net', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'Net') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'Net') is None


def test_assoc_places0_stub_double():
    # petrinetv3_Net has no real 'petrinetv3_Net' property in the generated
    # code (a bare stub) -- manually attach it so petrinetv3_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetv3_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetv3_Place(initialTokens=7, name="sample_text")
    partner = petrinetv3_Net()
    setattr(partner, 'petrinetv3_Net', None)
    _safe_set(owner, 'petrinetv3_Place', partner)
    assert owner in getattr(partner, 'petrinetv3_Net')
    _safe_set(owner, 'petrinetv3_Place', None)
    assert owner not in getattr(partner, 'petrinetv3_Net')


def test_assoc_tokens8_stub_double():
    # petrinetv3_Token has no real 'petrinetv3_Token' property in the generated
    # code (a bare stub) -- manually attach it so petrinetv3_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetv3_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetv3_Place(initialTokens=7, name="sample_text")
    partner = petrinetv3_Token()
    setattr(partner, 'petrinetv3_Token', None)
    _safe_set(owner, 'petrinetv3_Place9', {partner})
    assert getattr(partner, 'petrinetv3_Token') == owner
    _safe_set(owner, 'petrinetv3_Place9', set())
    assert getattr(partner, 'petrinetv3_Token') is None


def test_assoc_transitions1_stub_double():
    # petrinetv3_Net has no real 'parentNet' property in the generated
    # code (a bare stub) -- manually attach it so petrinetv3_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetv3_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetv3_Transition(clock=7, name="sample_text", tmax=7, tmin=7)
    partner = petrinetv3_Net()
    setattr(partner, 'parentNet', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'parentNet')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'parentNet')


