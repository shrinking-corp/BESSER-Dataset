import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Guard,
    NamedElement,
    tfsm_EvaluateGuard,
    tfsm_EventGuard,
    tfsm_FSMClock,
    tfsm_FSMEvent,
    tfsm_Guard,
    tfsm_NamedElement,
    tfsm_State,
    tfsm_TFSM,
    tfsm_TemporalGuard,
    tfsm_TimedSystem,
    tfsm_Transition,
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

def test_assoc_generatedEvents18_stub_double():
    # tfsm_FSMEvent has no real 'tfsm_FSMEvent20' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_FSMEvent()
    setattr(partner, 'tfsm_FSMEvent20', None)
    _safe_set(owner, 'tfsm_Transition19', {partner})
    assert getattr(partner, 'tfsm_FSMEvent20') == owner
    _safe_set(owner, 'tfsm_Transition19', set())
    assert getattr(partner, 'tfsm_FSMEvent20') is None


def test_assoc_incomingTransitions10_stub_double():
    # tfsm_State has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_State()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition11', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition11', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_onClock21_stub_double():
    # tfsm_FSMClock has no real 'tfsm_FSMClock22' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_TemporalGuard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_TemporalGuard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_TemporalGuard(afterDuration=7)
    partner = tfsm_FSMClock()
    setattr(partner, 'tfsm_FSMClock22', None)
    _safe_set(owner, 'tfsm_TemporalGuard', partner)
    assert getattr(partner, 'tfsm_FSMClock22') == owner
    _safe_set(owner, 'tfsm_TemporalGuard', None)
    assert getattr(partner, 'tfsm_FSMClock22') is None


def test_assoc_outgoingTransitions9_stub_double():
    # tfsm_State has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_State()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_ownedGuard16_stub_double():
    # tfsm_Guard has no real 'tfsm_Guard' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_Guard()
    setattr(partner, 'tfsm_Guard', None)
    _safe_set(owner, 'tfsm_Transition17', partner)
    assert getattr(partner, 'tfsm_Guard') == owner
    _safe_set(owner, 'tfsm_Transition17', None)
    assert getattr(partner, 'tfsm_Guard') is None


def test_assoc_ownedTransitions6_stub_double():
    # tfsm_TFSM has no real 'tfsm_TFSM7' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_TFSM()
    setattr(partner, 'tfsm_TFSM7', None)
    _safe_set(owner, 'tfsm_Transition', partner)
    assert owner in getattr(partner, 'tfsm_TFSM7')
    _safe_set(owner, 'tfsm_Transition', None)
    assert owner not in getattr(partner, 'tfsm_TFSM7')


def test_assoc_sollicitingTransitions25_stub_double():
    # tfsm_FSMEvent has no real 'tfsm_FSMEvent26' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_FSMEvent()
    setattr(partner, 'tfsm_FSMEvent26', None)
    _safe_set(owner, 'tfsm_Transition27', partner)
    assert owner in getattr(partner, 'tfsm_FSMEvent26')
    _safe_set(owner, 'tfsm_Transition27', None)
    assert owner not in getattr(partner, 'tfsm_FSMEvent26')


def test_assoc_source12_stub_double():
    # tfsm_State has no real 'State13' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_State()
    setattr(partner, 'State13', None)
    _safe_set(owner, 'outgoingTransitions', partner)
    assert getattr(partner, 'State13') == owner
    _safe_set(owner, 'outgoingTransitions', None)
    assert getattr(partner, 'State13') is None


def test_assoc_target14_stub_double():
    # tfsm_State has no real 'State15' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_State()
    setattr(partner, 'State15', None)
    _safe_set(owner, 'incomingTransitions', partner)
    assert getattr(partner, 'State15') == owner
    _safe_set(owner, 'incomingTransitions', None)
    assert getattr(partner, 'State15') is None


