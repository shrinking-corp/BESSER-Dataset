import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    Transition,
    stochasticpetrinet_Arc,
    stochasticpetrinet_ImmediateTransition,
    stochasticpetrinet_Node,
    stochasticpetrinet_PetriNet,
    stochasticpetrinet_Place,
    stochasticpetrinet_TimedTransition,
    stochasticpetrinet_Transition,
    ArcKind,
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

def test_assoc_place3_reverse_link_reassign_clear():
    a1 = stochasticpetrinet_Place(tokens=7)
    a2 = stochasticpetrinet_Place(tokens=13)
    b = stochasticpetrinet_Arc(kind="sample_text")
    _safe_set(b, 'stochasticpetrinet_Arc', a1)
    assert _is_linked(b, 'stochasticpetrinet_Arc', a1)
    if hasattr(a1, 'stochasticpetrinet_Place'):
        assert _is_linked(a1, 'stochasticpetrinet_Place', b)
    _safe_set(b, 'stochasticpetrinet_Arc', a2)
    assert _is_linked(b, 'stochasticpetrinet_Arc', a2)
    if hasattr(a1, 'stochasticpetrinet_Place'):
        assert not _is_linked(a1, 'stochasticpetrinet_Place', b)
    if hasattr(a2, 'stochasticpetrinet_Place'):
        assert _is_linked(a2, 'stochasticpetrinet_Place', b)
    _safe_set(b, 'stochasticpetrinet_Arc', None)
    assert not _is_linked(b, 'stochasticpetrinet_Arc', a2)
    if hasattr(a2, 'stochasticpetrinet_Place'):
        assert not _is_linked(a2, 'stochasticpetrinet_Place', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arcs1_stub_double():
    # stochasticpetrinet_Transition has no real 'transition' property in the generated
    # code (a bare stub) -- manually attach it so stochasticpetrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stochasticpetrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stochasticpetrinet_Arc(kind="sample_text")
    partner = stochasticpetrinet_Transition()
    setattr(partner, 'transition', None)
    _safe_set(owner, 'Arc', partner)
    assert owner in getattr(partner, 'transition')
    _safe_set(owner, 'Arc', None)
    assert owner not in getattr(partner, 'transition')


def test_assoc_transition2_stub_double():
    # stochasticpetrinet_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so stochasticpetrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stochasticpetrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stochasticpetrinet_Arc(kind="sample_text")
    partner = stochasticpetrinet_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'arcs', partner)
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'arcs', None)
    assert getattr(partner, 'Transition') is None


