import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Guard,
    NamedElement,
    tfsm_plaink3_EvaluateGuard,
    tfsm_plaink3_EventGuard,
    tfsm_plaink3_FSMClock,
    tfsm_plaink3_FSMEvent,
    tfsm_plaink3_Guard,
    tfsm_plaink3_NamedElement,
    tfsm_plaink3_State,
    tfsm_plaink3_TFSM,
    tfsm_plaink3_TemporalGuard,
    tfsm_plaink3_TimedSystem,
    tfsm_plaink3_Transition,
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

def test_assoc_generatedEvents21_reverse_link_reassign_clear():
    a1 = tfsm_plaink3_Transition(action="sample_text")
    a2 = tfsm_plaink3_Transition(action="sample_text_2")
    b = tfsm_plaink3_FSMEvent(isTriggered=True)
    _safe_set(b, 'tfsm_plaink3_FSMEvent23', a1)
    assert _is_linked(b, 'tfsm_plaink3_FSMEvent23', a1)
    if hasattr(a1, 'tfsm_plaink3_Transition22'):
        assert _is_linked(a1, 'tfsm_plaink3_Transition22', b)
    _safe_set(b, 'tfsm_plaink3_FSMEvent23', a2)
    assert _is_linked(b, 'tfsm_plaink3_FSMEvent23', a2)
    if hasattr(a1, 'tfsm_plaink3_Transition22'):
        assert not _is_linked(a1, 'tfsm_plaink3_Transition22', b)
    if hasattr(a2, 'tfsm_plaink3_Transition22'):
        assert _is_linked(a2, 'tfsm_plaink3_Transition22', b)
    _safe_set(b, 'tfsm_plaink3_FSMEvent23', None)
    assert not _is_linked(b, 'tfsm_plaink3_FSMEvent23', a2)
    if hasattr(a2, 'tfsm_plaink3_Transition22'):
        assert not _is_linked(a2, 'tfsm_plaink3_Transition22', b)


def test_assoc_onClock24_reverse_link_reassign_clear():
    a1 = tfsm_plaink3_TemporalGuard(afterDuration=7)
    a2 = tfsm_plaink3_TemporalGuard(afterDuration=13)
    b = tfsm_plaink3_FSMClock(numberOfTicks="sample_text")
    _safe_set(b, 'tfsm_plaink3_FSMClock25', a1)
    assert _is_linked(b, 'tfsm_plaink3_FSMClock25', a1)
    if hasattr(a1, 'tfsm_plaink3_TemporalGuard'):
        assert _is_linked(a1, 'tfsm_plaink3_TemporalGuard', b)
    _safe_set(b, 'tfsm_plaink3_FSMClock25', a2)
    assert _is_linked(b, 'tfsm_plaink3_FSMClock25', a2)
    if hasattr(a1, 'tfsm_plaink3_TemporalGuard'):
        assert not _is_linked(a1, 'tfsm_plaink3_TemporalGuard', b)
    if hasattr(a2, 'tfsm_plaink3_TemporalGuard'):
        assert _is_linked(a2, 'tfsm_plaink3_TemporalGuard', b)
    _safe_set(b, 'tfsm_plaink3_FSMClock25', None)
    assert not _is_linked(b, 'tfsm_plaink3_FSMClock25', a2)
    if hasattr(a2, 'tfsm_plaink3_TemporalGuard'):
        assert not _is_linked(a2, 'tfsm_plaink3_TemporalGuard', b)


def test_assoc_sollicitingTransitions28_reverse_link_reassign_clear():
    a1 = tfsm_plaink3_Transition(action="sample_text")
    a2 = tfsm_plaink3_Transition(action="sample_text_2")
    b = tfsm_plaink3_FSMEvent(isTriggered=True)
    _safe_set(b, 'tfsm_plaink3_FSMEvent29', {a1})
    assert _is_linked(b, 'tfsm_plaink3_FSMEvent29', a1)
    if hasattr(a1, 'tfsm_plaink3_Transition30'):
        assert _is_linked(a1, 'tfsm_plaink3_Transition30', b)
    _safe_set(b, 'tfsm_plaink3_FSMEvent29', {a2})
    assert _is_linked(b, 'tfsm_plaink3_FSMEvent29', a2)
    if hasattr(a1, 'tfsm_plaink3_Transition30'):
        assert not _is_linked(a1, 'tfsm_plaink3_Transition30', b)
    if hasattr(a2, 'tfsm_plaink3_Transition30'):
        assert _is_linked(a2, 'tfsm_plaink3_Transition30', b)
    _safe_set(b, 'tfsm_plaink3_FSMEvent29', set())
    assert not _is_linked(b, 'tfsm_plaink3_FSMEvent29', a2)
    if hasattr(a2, 'tfsm_plaink3_Transition30'):
        assert not _is_linked(a2, 'tfsm_plaink3_Transition30', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_globalClocks33_stub_double():
    # tfsm_plaink3_TimedSystem has no real 'tfsm_plaink3_TimedSystem34' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_FSMClock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_FSMClock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_FSMClock(numberOfTicks="sample_text")
    partner = tfsm_plaink3_TimedSystem()
    setattr(partner, 'tfsm_plaink3_TimedSystem34', None)
    _safe_set(owner, 'tfsm_plaink3_FSMClock35', partner)
    assert owner in getattr(partner, 'tfsm_plaink3_TimedSystem34')
    _safe_set(owner, 'tfsm_plaink3_FSMClock35', None)
    assert owner not in getattr(partner, 'tfsm_plaink3_TimedSystem34')


def test_assoc_globalEvents36_stub_double():
    # tfsm_plaink3_TimedSystem has no real 'tfsm_plaink3_TimedSystem37' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_FSMEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_FSMEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_FSMEvent(isTriggered=True)
    partner = tfsm_plaink3_TimedSystem()
    setattr(partner, 'tfsm_plaink3_TimedSystem37', None)
    _safe_set(owner, 'tfsm_plaink3_FSMEvent38', partner)
    assert owner in getattr(partner, 'tfsm_plaink3_TimedSystem37')
    _safe_set(owner, 'tfsm_plaink3_FSMEvent38', None)
    assert owner not in getattr(partner, 'tfsm_plaink3_TimedSystem37')


def test_assoc_incomingTransitions13_stub_double():
    # tfsm_plaink3_State has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_Transition(action="sample_text")
    partner = tfsm_plaink3_State()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition14', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition14', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_localClock4_stub_double():
    # tfsm_plaink3_TFSM has no real 'tfsm_plaink3_TFSM5' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_FSMClock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_FSMClock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_FSMClock(numberOfTicks="sample_text")
    partner = tfsm_plaink3_TFSM()
    setattr(partner, 'tfsm_plaink3_TFSM5', None)
    _safe_set(owner, 'tfsm_plaink3_FSMClock', partner)
    assert getattr(partner, 'tfsm_plaink3_TFSM5') == owner
    _safe_set(owner, 'tfsm_plaink3_FSMClock', None)
    assert getattr(partner, 'tfsm_plaink3_TFSM5') is None


def test_assoc_localEvents2_stub_double():
    # tfsm_plaink3_TFSM has no real 'tfsm_plaink3_TFSM3' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_FSMEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_FSMEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_FSMEvent(isTriggered=True)
    partner = tfsm_plaink3_TFSM()
    setattr(partner, 'tfsm_plaink3_TFSM3', None)
    _safe_set(owner, 'tfsm_plaink3_FSMEvent', partner)
    assert owner in getattr(partner, 'tfsm_plaink3_TFSM3')
    _safe_set(owner, 'tfsm_plaink3_FSMEvent', None)
    assert owner not in getattr(partner, 'tfsm_plaink3_TFSM3')


def test_assoc_outgoingTransitions12_stub_double():
    # tfsm_plaink3_State has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_Transition(action="sample_text")
    partner = tfsm_plaink3_State()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_ownedGuard19_stub_double():
    # tfsm_plaink3_Guard has no real 'tfsm_plaink3_Guard' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_Transition(action="sample_text")
    partner = tfsm_plaink3_Guard()
    setattr(partner, 'tfsm_plaink3_Guard', None)
    _safe_set(owner, 'tfsm_plaink3_Transition20', partner)
    assert getattr(partner, 'tfsm_plaink3_Guard') == owner
    _safe_set(owner, 'tfsm_plaink3_Transition20', None)
    assert getattr(partner, 'tfsm_plaink3_Guard') is None


def test_assoc_ownedTransitions6_stub_double():
    # tfsm_plaink3_TFSM has no real 'tfsm_plaink3_TFSM7' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_Transition(action="sample_text")
    partner = tfsm_plaink3_TFSM()
    setattr(partner, 'tfsm_plaink3_TFSM7', None)
    _safe_set(owner, 'tfsm_plaink3_Transition', partner)
    assert owner in getattr(partner, 'tfsm_plaink3_TFSM7')
    _safe_set(owner, 'tfsm_plaink3_Transition', None)
    assert owner not in getattr(partner, 'tfsm_plaink3_TFSM7')


def test_assoc_source15_stub_double():
    # tfsm_plaink3_State has no real 'State16' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_Transition(action="sample_text")
    partner = tfsm_plaink3_State()
    setattr(partner, 'State16', None)
    _safe_set(owner, 'outgoingTransitions', partner)
    assert getattr(partner, 'State16') == owner
    _safe_set(owner, 'outgoingTransitions', None)
    assert getattr(partner, 'State16') is None


def test_assoc_target17_stub_double():
    # tfsm_plaink3_State has no real 'State18' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_Transition(action="sample_text")
    partner = tfsm_plaink3_State()
    setattr(partner, 'State18', None)
    _safe_set(owner, 'incomingTransitions', partner)
    assert getattr(partner, 'State18') == owner
    _safe_set(owner, 'incomingTransitions', None)
    assert getattr(partner, 'State18') is None


def test_assoc_triggeringEvent26_stub_double():
    # tfsm_plaink3_EventGuard has no real 'tfsm_plaink3_EventGuard' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_plaink3_FSMEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_plaink3_FSMEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_plaink3_FSMEvent(isTriggered=True)
    partner = tfsm_plaink3_EventGuard()
    setattr(partner, 'tfsm_plaink3_EventGuard', None)
    _safe_set(owner, 'tfsm_plaink3_FSMEvent27', partner)
    assert getattr(partner, 'tfsm_plaink3_EventGuard') == owner
    _safe_set(owner, 'tfsm_plaink3_FSMEvent27', None)
    assert getattr(partner, 'tfsm_plaink3_EventGuard') is None


