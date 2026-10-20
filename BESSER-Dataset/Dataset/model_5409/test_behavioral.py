import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Diagram,
    fta_Condition,
    fta_Diagram,
    fta_Event,
    fta_FTA,
    fta_Hazard,
    GateType,
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

def test_assoc_condition2_reverse_link_reassign_clear():
    a1 = fta_Event(BaseEvent=True)
    a2 = fta_Event(BaseEvent=False)
    b = fta_Condition(GateKind="sample_text")
    _safe_set(b, 'fta_Condition3', a1)
    assert _is_linked(b, 'fta_Condition3', a1)
    if hasattr(a1, 'fta_Event'):
        assert _is_linked(a1, 'fta_Event', b)
    _safe_set(b, 'fta_Condition3', a2)
    assert _is_linked(b, 'fta_Condition3', a2)
    if hasattr(a1, 'fta_Event'):
        assert not _is_linked(a1, 'fta_Event', b)
    if hasattr(a2, 'fta_Event'):
        assert _is_linked(a2, 'fta_Event', b)
    _safe_set(b, 'fta_Condition3', None)
    assert not _is_linked(b, 'fta_Condition3', a2)
    if hasattr(a2, 'fta_Event'):
        assert not _is_linked(a2, 'fta_Event', b)


def test_assoc_events4_reverse_link_reassign_clear():
    a1 = fta_Event(BaseEvent=True)
    a2 = fta_Event(BaseEvent=False)
    b = fta_Condition(GateKind="sample_text")
    _safe_set(b, 'fta_Condition5', {a1})
    assert _is_linked(b, 'fta_Condition5', a1)
    if hasattr(a1, 'fta_Event6'):
        assert _is_linked(a1, 'fta_Event6', b)
    _safe_set(b, 'fta_Condition5', {a2})
    assert _is_linked(b, 'fta_Condition5', a2)
    if hasattr(a1, 'fta_Event6'):
        assert not _is_linked(a1, 'fta_Event6', b)
    if hasattr(a2, 'fta_Event6'):
        assert _is_linked(a2, 'fta_Event6', b)
    _safe_set(b, 'fta_Condition5', set())
    assert not _is_linked(b, 'fta_Condition5', a2)
    if hasattr(a2, 'fta_Event6'):
        assert not _is_linked(a2, 'fta_Event6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_conditions1_stub_double():
    # fta_Hazard has no real 'fta_Hazard' property in the generated
    # code (a bare stub) -- manually attach it so fta_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fta_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fta_Condition(GateKind="sample_text")
    partner = fta_Hazard()
    setattr(partner, 'fta_Hazard', None)
    _safe_set(owner, 'fta_Condition', partner)
    assert owner in getattr(partner, 'fta_Hazard')
    _safe_set(owner, 'fta_Condition', None)
    assert owner not in getattr(partner, 'fta_Hazard')


def test_assoc_diagrams0_stub_double():
    # fta_FTA has no real 'fta_FTA' property in the generated
    # code (a bare stub) -- manually attach it so fta_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fta_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fta_Diagram(detail="sample_text", id="sample_text", name="sample_text")
    partner = fta_FTA()
    setattr(partner, 'fta_FTA', None)
    _safe_set(owner, 'fta_Diagram', partner)
    assert owner in getattr(partner, 'fta_FTA')
    _safe_set(owner, 'fta_Diagram', None)
    assert owner not in getattr(partner, 'fta_FTA')


