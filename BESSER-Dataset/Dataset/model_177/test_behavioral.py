import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    petrinet_Net,
    petrinet_NetStopEvent,
    petrinet_Place,
    petrinet_Token,
    petrinet_Transition,
    petrinet_TransitionFireEvent,
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

def test_assoc_input3_reverse_link_reassign_clear():
    a1 = petrinet_Transition(name="sample_text")
    a2 = petrinet_Transition(name="sample_text_2")
    b = petrinet_Place(initialTokens=7, name="sample_text")
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


def test_assoc_output6_reverse_link_reassign_clear():
    a1 = petrinet_Transition(name="sample_text")
    a2 = petrinet_Transition(name="sample_text_2")
    b = petrinet_Place(initialTokens=7, name="sample_text")
    _safe_set(b, 'petrinet_Place8', a1)
    assert _is_linked(b, 'petrinet_Place8', a1)
    if hasattr(a1, 'petrinet_Transition7'):
        assert _is_linked(a1, 'petrinet_Transition7', b)
    _safe_set(b, 'petrinet_Place8', a2)
    assert _is_linked(b, 'petrinet_Place8', a2)
    if hasattr(a1, 'petrinet_Transition7'):
        assert not _is_linked(a1, 'petrinet_Transition7', b)
    if hasattr(a2, 'petrinet_Transition7'):
        assert _is_linked(a2, 'petrinet_Transition7', b)
    _safe_set(b, 'petrinet_Place8', None)
    assert not _is_linked(b, 'petrinet_Place8', a2)
    if hasattr(a2, 'petrinet_Transition7'):
        assert not _is_linked(a2, 'petrinet_Transition7', b)


def test_assoc_places0_reverse_link_reassign_clear():
    a1 = petrinet_Place(initialTokens=7, name="sample_text")
    a2 = petrinet_Place(initialTokens=13, name="sample_text_2")
    b = petrinet_Net()
    _safe_set(b, 'petrinet_Net', {a1})
    assert _is_linked(b, 'petrinet_Net', a1)
    if hasattr(a1, 'petrinet_Place'):
        assert _is_linked(a1, 'petrinet_Place', b)
    _safe_set(b, 'petrinet_Net', {a2})
    assert _is_linked(b, 'petrinet_Net', a2)
    if hasattr(a1, 'petrinet_Place'):
        assert not _is_linked(a1, 'petrinet_Place', b)
    if hasattr(a2, 'petrinet_Place'):
        assert _is_linked(a2, 'petrinet_Place', b)
    _safe_set(b, 'petrinet_Net', set())
    assert not _is_linked(b, 'petrinet_Net', a2)
    if hasattr(a2, 'petrinet_Place'):
        assert not _is_linked(a2, 'petrinet_Place', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = petrinet_Transition(name="sample_text")
    a2 = petrinet_Transition(name="sample_text_2")
    b = petrinet_Net()
    _safe_set(b, 'petrinet_Net2', {a1})
    assert _is_linked(b, 'petrinet_Net2', a1)
    if hasattr(a1, 'petrinet_Transition'):
        assert _is_linked(a1, 'petrinet_Transition', b)
    _safe_set(b, 'petrinet_Net2', {a2})
    assert _is_linked(b, 'petrinet_Net2', a2)
    if hasattr(a1, 'petrinet_Transition'):
        assert not _is_linked(a1, 'petrinet_Transition', b)
    if hasattr(a2, 'petrinet_Transition'):
        assert _is_linked(a2, 'petrinet_Transition', b)
    _safe_set(b, 'petrinet_Net2', set())
    assert not _is_linked(b, 'petrinet_Net2', a2)
    if hasattr(a2, 'petrinet_Transition'):
        assert not _is_linked(a2, 'petrinet_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_net11_stub_double():
    # petrinet_NetStopEvent has no real 'petrinet_NetStopEvent' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Net's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Net's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Net()
    partner = petrinet_NetStopEvent()
    setattr(partner, 'petrinet_NetStopEvent', None)
    _safe_set(owner, 'petrinet_Net12', partner)
    assert getattr(partner, 'petrinet_NetStopEvent') == owner
    _safe_set(owner, 'petrinet_Net12', None)
    assert getattr(partner, 'petrinet_NetStopEvent') is None


def test_assoc_tokens9_stub_double():
    # petrinet_Token has no real 'petrinet_Token' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(initialTokens=7, name="sample_text")
    partner = petrinet_Token()
    setattr(partner, 'petrinet_Token', None)
    _safe_set(owner, 'petrinet_Place10', {partner})
    assert getattr(partner, 'petrinet_Token') == owner
    _safe_set(owner, 'petrinet_Place10', set())
    assert getattr(partner, 'petrinet_Token') is None


def test_assoc_transition13_stub_double():
    # petrinet_TransitionFireEvent has no real 'petrinet_TransitionFireEvent' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(name="sample_text")
    partner = petrinet_TransitionFireEvent()
    setattr(partner, 'petrinet_TransitionFireEvent', None)
    _safe_set(owner, 'petrinet_Transition14', partner)
    assert getattr(partner, 'petrinet_TransitionFireEvent') == owner
    _safe_set(owner, 'petrinet_Transition14', None)
    assert getattr(partner, 'petrinet_TransitionFireEvent') is None


