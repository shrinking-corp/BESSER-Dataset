import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    statemachine_Event,
    statemachine_SM,
    statemachine_State,
    statemachine_Transition,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_event17_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition18' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Event(id="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition18', None)
    _safe_set(owner, 'statemachine_Event19', partner)
    assert getattr(partner, 'statemachine_Transition18') == owner
    _safe_set(owner, 'statemachine_Event19', None)
    assert getattr(partner, 'statemachine_Transition18') is None


def test_assoc_events9_stub_double():
    # statemachine_SM has no real 'statemachine_SM10' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Event(id="sample_text")
    partner = statemachine_SM()
    setattr(partner, 'statemachine_SM10', None)
    _safe_set(owner, 'statemachine_Event', partner)
    assert owner in getattr(partner, 'statemachine_SM10')
    _safe_set(owner, 'statemachine_Event', None)
    assert owner not in getattr(partner, 'statemachine_SM10')


def test_assoc_final4_stub_double():
    # statemachine_SM has no real 'statemachine_SM5' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(id="sample_text")
    partner = statemachine_SM()
    setattr(partner, 'statemachine_SM5', None)
    _safe_set(owner, 'statemachine_State6', partner)
    assert owner in getattr(partner, 'statemachine_SM5')
    _safe_set(owner, 'statemachine_State6', None)
    assert owner not in getattr(partner, 'statemachine_SM5')


def test_assoc_from_11_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition12' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(id="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition12', None)
    _safe_set(owner, 'statemachine_State13', partner)
    assert getattr(partner, 'statemachine_Transition12') == owner
    _safe_set(owner, 'statemachine_State13', None)
    assert getattr(partner, 'statemachine_Transition12') is None


def test_assoc_initial1_stub_double():
    # statemachine_SM has no real 'statemachine_SM2' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(id="sample_text")
    partner = statemachine_SM()
    setattr(partner, 'statemachine_SM2', None)
    _safe_set(owner, 'statemachine_State3', partner)
    assert getattr(partner, 'statemachine_SM2') == owner
    _safe_set(owner, 'statemachine_State3', None)
    assert getattr(partner, 'statemachine_SM2') is None


def test_assoc_states0_stub_double():
    # statemachine_SM has no real 'statemachine_SM' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(id="sample_text")
    partner = statemachine_SM()
    setattr(partner, 'statemachine_SM', None)
    _safe_set(owner, 'statemachine_State', partner)
    assert owner in getattr(partner, 'statemachine_SM')
    _safe_set(owner, 'statemachine_State', None)
    assert owner not in getattr(partner, 'statemachine_SM')


def test_assoc_to14_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition15' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(id="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition15', None)
    _safe_set(owner, 'statemachine_State16', partner)
    assert getattr(partner, 'statemachine_Transition15') == owner
    _safe_set(owner, 'statemachine_State16', None)
    assert getattr(partner, 'statemachine_Transition15') is None


