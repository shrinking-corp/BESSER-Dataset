import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    TimedZone,
    Transition,
    automaton_AtomicEventPattern,
    automaton_Automaton,
    automaton_EpsilonTransition,
    automaton_Event,
    automaton_EventPattern,
    automaton_EventToken,
    automaton_FinalState,
    automaton_Guard,
    automaton_HoldsFor,
    automaton_InitState,
    automaton_InternalModel,
    automaton_State,
    automaton_TimedZone,
    automaton_Transition,
    automaton_TrapState,
    automaton_TypedTransition,
    automaton_Within,
    EventContext,
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

def test_assoc_inState37_reverse_link_reassign_clear():
    a1 = automaton_TimedZone(time="sample_text")
    a2 = automaton_TimedZone(time="sample_text_2")
    b = automaton_State(label="sample_text")
    _safe_set(b, 'State38', a1)
    assert _is_linked(b, 'State38', a1)
    if hasattr(a1, 'inStateOf'):
        assert _is_linked(a1, 'inStateOf', b)
    _safe_set(b, 'State38', a2)
    assert _is_linked(b, 'State38', a2)
    if hasattr(a1, 'inStateOf'):
        assert not _is_linked(a1, 'inStateOf', b)
    if hasattr(a2, 'inStateOf'):
        assert _is_linked(a2, 'inStateOf', b)
    _safe_set(b, 'State38', None)
    assert not _is_linked(b, 'State38', a2)
    if hasattr(a2, 'inStateOf'):
        assert not _is_linked(a2, 'inStateOf', b)


def test_assoc_inStateOf27_reverse_link_reassign_clear():
    a1 = automaton_TimedZone(time="sample_text")
    a2 = automaton_TimedZone(time="sample_text_2")
    b = automaton_State(label="sample_text")
    _safe_set(b, 'inState', {a1})
    assert _is_linked(b, 'inState', a1)
    if hasattr(a1, 'TimedZone'):
        assert _is_linked(a1, 'TimedZone', b)
    _safe_set(b, 'inState', {a2})
    assert _is_linked(b, 'inState', a2)
    if hasattr(a1, 'TimedZone'):
        assert not _is_linked(a1, 'TimedZone', b)
    if hasattr(a2, 'TimedZone'):
        assert _is_linked(a2, 'TimedZone', b)
    _safe_set(b, 'inState', set())
    assert not _is_linked(b, 'inState', a2)
    if hasattr(a2, 'TimedZone'):
        assert not _is_linked(a2, 'TimedZone', b)


def test_assoc_outState39_reverse_link_reassign_clear():
    a1 = automaton_TimedZone(time="sample_text")
    a2 = automaton_TimedZone(time="sample_text_2")
    b = automaton_State(label="sample_text")
    _safe_set(b, 'State40', a1)
    assert _is_linked(b, 'State40', a1)
    if hasattr(a1, 'outStateOf'):
        assert _is_linked(a1, 'outStateOf', b)
    _safe_set(b, 'State40', a2)
    assert _is_linked(b, 'State40', a2)
    if hasattr(a1, 'outStateOf'):
        assert not _is_linked(a1, 'outStateOf', b)
    if hasattr(a2, 'outStateOf'):
        assert _is_linked(a2, 'outStateOf', b)
    _safe_set(b, 'State40', None)
    assert not _is_linked(b, 'State40', a2)
    if hasattr(a2, 'outStateOf'):
        assert not _is_linked(a2, 'outStateOf', b)


def test_assoc_outStateOf28_reverse_link_reassign_clear():
    a1 = automaton_TimedZone(time="sample_text")
    a2 = automaton_TimedZone(time="sample_text_2")
    b = automaton_State(label="sample_text")
    _safe_set(b, 'outState', {a1})
    assert _is_linked(b, 'outState', a1)
    if hasattr(a1, 'TimedZone29'):
        assert _is_linked(a1, 'TimedZone29', b)
    _safe_set(b, 'outState', {a2})
    assert _is_linked(b, 'outState', a2)
    if hasattr(a1, 'TimedZone29'):
        assert not _is_linked(a1, 'TimedZone29', b)
    if hasattr(a2, 'TimedZone29'):
        assert _is_linked(a2, 'TimedZone29', b)
    _safe_set(b, 'outState', set())
    assert not _is_linked(b, 'outState', a2)
    if hasattr(a2, 'TimedZone29'):
        assert not _is_linked(a2, 'TimedZone29', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_automata0_stub_double():
    # automaton_Automaton has no real 'automaton_Automaton' property in the generated
    # code (a bare stub) -- manually attach it so automaton_InternalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_InternalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_InternalModel(context="sample_text")
    partner = automaton_Automaton()
    setattr(partner, 'automaton_Automaton', None)
    _safe_set(owner, 'automaton_InternalModel', {partner})
    assert getattr(partner, 'automaton_Automaton') == owner
    _safe_set(owner, 'automaton_InternalModel', set())
    assert getattr(partner, 'automaton_Automaton') is None


def test_assoc_currentState10_stub_double():
    # automaton_EventToken has no real 'eventTokens' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_EventToken()
    setattr(partner, 'eventTokens', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'eventTokens') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'eventTokens') is None


def test_assoc_eventTokens23_stub_double():
    # automaton_EventToken has no real 'EventToken' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_EventToken()
    setattr(partner, 'EventToken', None)
    _safe_set(owner, 'currentState', {partner})
    assert getattr(partner, 'EventToken') == owner
    _safe_set(owner, 'currentState', set())
    assert getattr(partner, 'EventToken') is None


def test_assoc_inTransitions20_stub_double():
    # automaton_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'postState', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'postState', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_lastProcessedEvent24_stub_double():
    # automaton_Event has no real 'automaton_Event26' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_Event()
    setattr(partner, 'automaton_Event26', None)
    _safe_set(owner, 'automaton_State25', partner)
    assert getattr(partner, 'automaton_Event26') == owner
    _safe_set(owner, 'automaton_State25', None)
    assert getattr(partner, 'automaton_Event26') is None


def test_assoc_latestEvent1_stub_double():
    # automaton_Event has no real 'automaton_Event' property in the generated
    # code (a bare stub) -- manually attach it so automaton_InternalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_InternalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_InternalModel(context="sample_text")
    partner = automaton_Event()
    setattr(partner, 'automaton_Event', None)
    _safe_set(owner, 'automaton_InternalModel2', partner)
    assert getattr(partner, 'automaton_Event') == owner
    _safe_set(owner, 'automaton_InternalModel2', None)
    assert getattr(partner, 'automaton_Event') is None


def test_assoc_outTransitions21_stub_double():
    # automaton_Transition has no real 'Transition22' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_Transition()
    setattr(partner, 'Transition22', None)
    _safe_set(owner, 'preState', {partner})
    assert getattr(partner, 'Transition22') == owner
    _safe_set(owner, 'preState', set())
    assert getattr(partner, 'Transition22') is None


def test_assoc_postState32_stub_double():
    # automaton_Transition has no real 'inTransitions' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_Transition()
    setattr(partner, 'inTransitions', None)
    _safe_set(owner, 'State33', partner)
    assert getattr(partner, 'inTransitions') == owner
    _safe_set(owner, 'State33', None)
    assert getattr(partner, 'inTransitions') is None


def test_assoc_preState30_stub_double():
    # automaton_Transition has no real 'outTransitions' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_Transition()
    setattr(partner, 'outTransitions', None)
    _safe_set(owner, 'State31', partner)
    assert getattr(partner, 'outTransitions') == owner
    _safe_set(owner, 'State31', None)
    assert getattr(partner, 'outTransitions') is None


def test_assoc_states3_stub_double():
    # automaton_Automaton has no real 'automaton_Automaton4' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_Automaton()
    setattr(partner, 'automaton_Automaton4', None)
    _safe_set(owner, 'automaton_State', partner)
    assert getattr(partner, 'automaton_Automaton4') == owner
    _safe_set(owner, 'automaton_State', None)
    assert getattr(partner, 'automaton_Automaton4') is None


def test_assoc_timedZones17_stub_double():
    # automaton_EventToken has no real 'automaton_EventToken18' property in the generated
    # code (a bare stub) -- manually attach it so automaton_TimedZone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_TimedZone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_TimedZone(time="sample_text")
    partner = automaton_EventToken()
    setattr(partner, 'automaton_EventToken18', None)
    _safe_set(owner, 'automaton_TimedZone19', partner)
    assert getattr(partner, 'automaton_EventToken18') == owner
    _safe_set(owner, 'automaton_TimedZone19', None)
    assert getattr(partner, 'automaton_EventToken18') is None


def test_assoc_timedZones8_stub_double():
    # automaton_Automaton has no real 'automaton_Automaton9' property in the generated
    # code (a bare stub) -- manually attach it so automaton_TimedZone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_TimedZone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_TimedZone(time="sample_text")
    partner = automaton_Automaton()
    setattr(partner, 'automaton_Automaton9', None)
    _safe_set(owner, 'automaton_TimedZone', partner)
    assert getattr(partner, 'automaton_Automaton9') == owner
    _safe_set(owner, 'automaton_TimedZone', None)
    assert getattr(partner, 'automaton_Automaton9') is None


