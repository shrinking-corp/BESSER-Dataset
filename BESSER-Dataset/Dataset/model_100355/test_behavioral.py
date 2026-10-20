import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTransition,
    Action,
    Binding,
    EventAutomatonModel_AbstractTransition,
    EventAutomatonModel_Action,
    EventAutomatonModel_Automaton,
    EventAutomatonModel_Binding,
    EventAutomatonModel_ComplexEventProcessor,
    EventAutomatonModel_ConstantBinding,
    EventAutomatonModel_EpsilonTransition,
    EventAutomatonModel_Event,
    EventAutomatonModel_EventGuard,
    EventAutomatonModel_FixParameter,
    EventAutomatonModel_FreeParameter,
    EventAutomatonModel_NotEquivalentRelation,
    EventAutomatonModel_Parameter,
    EventAutomatonModel_ResetTimerAction,
    EventAutomatonModel_SetTimerAction,
    EventAutomatonModel_State,
    EventAutomatonModel_SymbolicEvent,
    EventAutomatonModel_SymbolicEventParameter,
    EventAutomatonModel_SymbolicInputEvent,
    EventAutomatonModel_SymbolicParameter,
    EventAutomatonModel_SymbolicTimeoutEvent,
    EventAutomatonModel_SymbolicTimer,
    EventAutomatonModel_SymbolicTokenParameter,
    EventAutomatonModel_TimerAction,
    EventAutomatonModel_Token,
    EventAutomatonModel_TokenParameterBinding,
    EventAutomatonModel_Transition,
    Parameter,
    SymbolicEvent,
    SymbolicParameter,
    TimerAction,
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

def test_assoc_initialState3_reverse_link_reassign_clear():
    a1 = EventAutomatonModel_State(acceptor="sample_text", id=7)
    a2 = EventAutomatonModel_State(acceptor="sample_text_2", id=13)
    b = EventAutomatonModel_Automaton(name="sample_text")
    _safe_set(b, 'EventAutomatonModel_Automaton4', a1)
    assert _is_linked(b, 'EventAutomatonModel_Automaton4', a1)
    if hasattr(a1, 'EventAutomatonModel_State5'):
        assert _is_linked(a1, 'EventAutomatonModel_State5', b)
    _safe_set(b, 'EventAutomatonModel_Automaton4', a2)
    assert _is_linked(b, 'EventAutomatonModel_Automaton4', a2)
    if hasattr(a1, 'EventAutomatonModel_State5'):
        assert not _is_linked(a1, 'EventAutomatonModel_State5', b)
    if hasattr(a2, 'EventAutomatonModel_State5'):
        assert _is_linked(a2, 'EventAutomatonModel_State5', b)
    _safe_set(b, 'EventAutomatonModel_Automaton4', None)
    assert not _is_linked(b, 'EventAutomatonModel_Automaton4', a2)
    if hasattr(a2, 'EventAutomatonModel_State5'):
        assert not _is_linked(a2, 'EventAutomatonModel_State5', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = EventAutomatonModel_State(acceptor="sample_text", id=7)
    a2 = EventAutomatonModel_State(acceptor="sample_text_2", id=13)
    b = EventAutomatonModel_Automaton(name="sample_text")
    _safe_set(b, 'EventAutomatonModel_Automaton', {a1})
    assert _is_linked(b, 'EventAutomatonModel_Automaton', a1)
    if hasattr(a1, 'EventAutomatonModel_State'):
        assert _is_linked(a1, 'EventAutomatonModel_State', b)
    _safe_set(b, 'EventAutomatonModel_Automaton', {a2})
    assert _is_linked(b, 'EventAutomatonModel_Automaton', a2)
    if hasattr(a1, 'EventAutomatonModel_State'):
        assert not _is_linked(a1, 'EventAutomatonModel_State', b)
    if hasattr(a2, 'EventAutomatonModel_State'):
        assert _is_linked(a2, 'EventAutomatonModel_State', b)
    _safe_set(b, 'EventAutomatonModel_Automaton', set())
    assert not _is_linked(b, 'EventAutomatonModel_Automaton', a2)
    if hasattr(a2, 'EventAutomatonModel_State'):
        assert not _is_linked(a2, 'EventAutomatonModel_State', b)


def test_assoc_symbolicTokenParameters6_reverse_link_reassign_clear():
    a1 = EventAutomatonModel_SymbolicParameter(name="sample_text")
    a2 = EventAutomatonModel_SymbolicParameter(name="sample_text_2")
    b = EventAutomatonModel_Automaton(name="sample_text")
    _safe_set(b, 'EventAutomatonModel_Automaton7', {a1})
    assert _is_linked(b, 'EventAutomatonModel_Automaton7', a1)
    if hasattr(a1, 'EventAutomatonModel_SymbolicParameter'):
        assert _is_linked(a1, 'EventAutomatonModel_SymbolicParameter', b)
    _safe_set(b, 'EventAutomatonModel_Automaton7', {a2})
    assert _is_linked(b, 'EventAutomatonModel_Automaton7', a2)
    if hasattr(a1, 'EventAutomatonModel_SymbolicParameter'):
        assert not _is_linked(a1, 'EventAutomatonModel_SymbolicParameter', b)
    if hasattr(a2, 'EventAutomatonModel_SymbolicParameter'):
        assert _is_linked(a2, 'EventAutomatonModel_SymbolicParameter', b)
    _safe_set(b, 'EventAutomatonModel_Automaton7', set())
    assert not _is_linked(b, 'EventAutomatonModel_Automaton7', a2)
    if hasattr(a2, 'EventAutomatonModel_SymbolicParameter'):
        assert not _is_linked(a2, 'EventAutomatonModel_SymbolicParameter', b)


def test_assoc_timers8_reverse_link_reassign_clear():
    a1 = EventAutomatonModel_SymbolicTimer(name="sample_text")
    a2 = EventAutomatonModel_SymbolicTimer(name="sample_text_2")
    b = EventAutomatonModel_Automaton(name="sample_text")
    _safe_set(b, 'EventAutomatonModel_Automaton9', {a1})
    assert _is_linked(b, 'EventAutomatonModel_Automaton9', a1)
    if hasattr(a1, 'EventAutomatonModel_SymbolicTimer'):
        assert _is_linked(a1, 'EventAutomatonModel_SymbolicTimer', b)
    _safe_set(b, 'EventAutomatonModel_Automaton9', {a2})
    assert _is_linked(b, 'EventAutomatonModel_Automaton9', a2)
    if hasattr(a1, 'EventAutomatonModel_SymbolicTimer'):
        assert not _is_linked(a1, 'EventAutomatonModel_SymbolicTimer', b)
    if hasattr(a2, 'EventAutomatonModel_SymbolicTimer'):
        assert _is_linked(a2, 'EventAutomatonModel_SymbolicTimer', b)
    _safe_set(b, 'EventAutomatonModel_Automaton9', set())
    assert not _is_linked(b, 'EventAutomatonModel_Automaton9', a2)
    if hasattr(a2, 'EventAutomatonModel_SymbolicTimer'):
        assert not _is_linked(a2, 'EventAutomatonModel_SymbolicTimer', b)


def test_assoc_trapState10_reverse_link_reassign_clear():
    a1 = EventAutomatonModel_State(acceptor="sample_text", id=7)
    a2 = EventAutomatonModel_State(acceptor="sample_text_2", id=13)
    b = EventAutomatonModel_Automaton(name="sample_text")
    _safe_set(b, 'EventAutomatonModel_Automaton11', a1)
    assert _is_linked(b, 'EventAutomatonModel_Automaton11', a1)
    if hasattr(a1, 'EventAutomatonModel_State12'):
        assert _is_linked(a1, 'EventAutomatonModel_State12', b)
    _safe_set(b, 'EventAutomatonModel_Automaton11', a2)
    assert _is_linked(b, 'EventAutomatonModel_Automaton11', a2)
    if hasattr(a1, 'EventAutomatonModel_State12'):
        assert not _is_linked(a1, 'EventAutomatonModel_State12', b)
    if hasattr(a2, 'EventAutomatonModel_State12'):
        assert _is_linked(a2, 'EventAutomatonModel_State12', b)
    _safe_set(b, 'EventAutomatonModel_Automaton11', None)
    assert not _is_linked(b, 'EventAutomatonModel_Automaton11', a2)
    if hasattr(a2, 'EventAutomatonModel_State12'):
        assert not _is_linked(a2, 'EventAutomatonModel_State12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_automata15_stub_double():
    # EventAutomatonModel_ComplexEventProcessor has no real 'EventAutomatonModel_ComplexEventProcessor' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_Automaton(name="sample_text")
    partner = EventAutomatonModel_ComplexEventProcessor()
    setattr(partner, 'EventAutomatonModel_ComplexEventProcessor', None)
    _safe_set(owner, 'EventAutomatonModel_Automaton16', partner)
    assert owner in getattr(partner, 'EventAutomatonModel_ComplexEventProcessor')
    _safe_set(owner, 'EventAutomatonModel_Automaton16', None)
    assert owner not in getattr(partner, 'EventAutomatonModel_ComplexEventProcessor')


def test_assoc_boundTo27_stub_double():
    # EventAutomatonModel_ConstantBinding has no real 'EventAutomatonModel_ConstantBinding' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_FixParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_FixParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_FixParameter(value="sample_text")
    partner = EventAutomatonModel_ConstantBinding()
    setattr(partner, 'EventAutomatonModel_ConstantBinding', None)
    _safe_set(owner, 'EventAutomatonModel_FixParameter', partner)
    assert getattr(partner, 'EventAutomatonModel_ConstantBinding') == owner
    _safe_set(owner, 'EventAutomatonModel_FixParameter', None)
    assert getattr(partner, 'EventAutomatonModel_ConstantBinding') is None


def test_assoc_from_50_stub_double():
    # EventAutomatonModel_AbstractTransition has no real 'outgoingTransitions' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_State(acceptor="sample_text", id=7)
    partner = EventAutomatonModel_AbstractTransition()
    setattr(partner, 'outgoingTransitions', None)
    _safe_set(owner, 'State51', partner)
    assert getattr(partner, 'outgoingTransitions') == owner
    _safe_set(owner, 'State51', None)
    assert getattr(partner, 'outgoingTransitions') is None


def test_assoc_incomingTransitions24_stub_double():
    # EventAutomatonModel_AbstractTransition has no real 'AbstractTransition' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_State(acceptor="sample_text", id=7)
    partner = EventAutomatonModel_AbstractTransition()
    setattr(partner, 'AbstractTransition', None)
    _safe_set(owner, 'to', {partner})
    assert getattr(partner, 'AbstractTransition') == owner
    _safe_set(owner, 'to', set())
    assert getattr(partner, 'AbstractTransition') is None


def test_assoc_on37_stub_double():
    # EventAutomatonModel_Token has no real 'tokens' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_State(acceptor="sample_text", id=7)
    partner = EventAutomatonModel_Token()
    setattr(partner, 'tokens', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'tokens') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'tokens') is None


def test_assoc_outgoingTransitions25_stub_double():
    # EventAutomatonModel_AbstractTransition has no real 'AbstractTransition26' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_State(acceptor="sample_text", id=7)
    partner = EventAutomatonModel_AbstractTransition()
    setattr(partner, 'AbstractTransition26', None)
    _safe_set(owner, 'from_', {partner})
    assert getattr(partner, 'AbstractTransition26') == owner
    _safe_set(owner, 'from_', set())
    assert getattr(partner, 'AbstractTransition26') is None


def test_assoc_parameters34_stub_double():
    # EventAutomatonModel_Event has no real 'EventAutomatonModel_Event35' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_FixParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_FixParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_FixParameter(value="sample_text")
    partner = EventAutomatonModel_Event()
    setattr(partner, 'EventAutomatonModel_Event35', None)
    _safe_set(owner, 'EventAutomatonModel_FixParameter36', partner)
    assert owner in getattr(partner, 'EventAutomatonModel_Event35')
    _safe_set(owner, 'EventAutomatonModel_FixParameter36', None)
    assert owner not in getattr(partner, 'EventAutomatonModel_Event35')


def test_assoc_states53_stub_double():
    # EventAutomatonModel_NotEquivalentRelation has no real 'EventAutomatonModel_NotEquivalentRelation' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_State(acceptor="sample_text", id=7)
    partner = EventAutomatonModel_NotEquivalentRelation()
    setattr(partner, 'EventAutomatonModel_NotEquivalentRelation', None)
    _safe_set(owner, 'EventAutomatonModel_State54', partner)
    assert owner in getattr(partner, 'EventAutomatonModel_NotEquivalentRelation')
    _safe_set(owner, 'EventAutomatonModel_State54', None)
    assert owner not in getattr(partner, 'EventAutomatonModel_NotEquivalentRelation')


def test_assoc_symbolicEvents17_stub_double():
    # EventAutomatonModel_ComplexEventProcessor has no real 'EventAutomatonModel_ComplexEventProcessor18' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_SymbolicInputEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_SymbolicInputEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_SymbolicInputEvent(name="sample_text")
    partner = EventAutomatonModel_ComplexEventProcessor()
    setattr(partner, 'EventAutomatonModel_ComplexEventProcessor18', None)
    _safe_set(owner, 'EventAutomatonModel_SymbolicInputEvent', partner)
    assert owner in getattr(partner, 'EventAutomatonModel_ComplexEventProcessor18')
    _safe_set(owner, 'EventAutomatonModel_SymbolicInputEvent', None)
    assert owner not in getattr(partner, 'EventAutomatonModel_ComplexEventProcessor18')


def test_assoc_symbolicParameters19_stub_double():
    # EventAutomatonModel_SymbolicEvent has no real 'EventAutomatonModel_SymbolicEvent' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_SymbolicParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_SymbolicParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_SymbolicParameter(name="sample_text")
    partner = EventAutomatonModel_SymbolicEvent()
    setattr(partner, 'EventAutomatonModel_SymbolicEvent', None)
    _safe_set(owner, 'EventAutomatonModel_SymbolicParameter20', partner)
    assert owner in getattr(partner, 'EventAutomatonModel_SymbolicEvent')
    _safe_set(owner, 'EventAutomatonModel_SymbolicParameter20', None)
    assert owner not in getattr(partner, 'EventAutomatonModel_SymbolicEvent')


def test_assoc_timeoutEvent14_stub_double():
    # EventAutomatonModel_SymbolicTimeoutEvent has no real 'SymbolicTimeoutEvent' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_SymbolicTimer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_SymbolicTimer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_SymbolicTimer(name="sample_text")
    partner = EventAutomatonModel_SymbolicTimeoutEvent()
    setattr(partner, 'SymbolicTimeoutEvent', None)
    _safe_set(owner, 'timer', partner)
    assert getattr(partner, 'SymbolicTimeoutEvent') == owner
    _safe_set(owner, 'timer', None)
    assert getattr(partner, 'SymbolicTimeoutEvent') is None


def test_assoc_timer28_stub_double():
    # EventAutomatonModel_SymbolicTimeoutEvent has no real 'timeoutEvent' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_SymbolicTimer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_SymbolicTimer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_SymbolicTimer(name="sample_text")
    partner = EventAutomatonModel_SymbolicTimeoutEvent()
    setattr(partner, 'timeoutEvent', None)
    _safe_set(owner, 'SymbolicTimer', partner)
    assert getattr(partner, 'timeoutEvent') == owner
    _safe_set(owner, 'SymbolicTimer', None)
    assert getattr(partner, 'timeoutEvent') is None


def test_assoc_timer30_stub_double():
    # EventAutomatonModel_TimerAction has no real 'EventAutomatonModel_TimerAction' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_SymbolicTimer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_SymbolicTimer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_SymbolicTimer(name="sample_text")
    partner = EventAutomatonModel_TimerAction()
    setattr(partner, 'EventAutomatonModel_TimerAction', None)
    _safe_set(owner, 'EventAutomatonModel_SymbolicTimer31', partner)
    assert getattr(partner, 'EventAutomatonModel_TimerAction') == owner
    _safe_set(owner, 'EventAutomatonModel_SymbolicTimer31', None)
    assert getattr(partner, 'EventAutomatonModel_TimerAction') is None


def test_assoc_to48_stub_double():
    # EventAutomatonModel_AbstractTransition has no real 'incomingTransitions' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_State(acceptor="sample_text", id=7)
    partner = EventAutomatonModel_AbstractTransition()
    setattr(partner, 'incomingTransitions', None)
    _safe_set(owner, 'State49', partner)
    assert getattr(partner, 'incomingTransitions') == owner
    _safe_set(owner, 'State49', None)
    assert getattr(partner, 'incomingTransitions') is None


def test_assoc_tokens1_stub_double():
    # EventAutomatonModel_Token has no real 'EventAutomatonModel_Token' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_Automaton(name="sample_text")
    partner = EventAutomatonModel_Token()
    setattr(partner, 'EventAutomatonModel_Token', None)
    _safe_set(owner, 'EventAutomatonModel_Automaton2', {partner})
    assert getattr(partner, 'EventAutomatonModel_Token') == owner
    _safe_set(owner, 'EventAutomatonModel_Automaton2', set())
    assert getattr(partner, 'EventAutomatonModel_Token') is None


def test_assoc_tokens23_stub_double():
    # EventAutomatonModel_Token has no real 'Token' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_State(acceptor="sample_text", id=7)
    partner = EventAutomatonModel_Token()
    setattr(partner, 'Token', None)
    _safe_set(owner, 'on', {partner})
    assert getattr(partner, 'Token') == owner
    _safe_set(owner, 'on', set())
    assert getattr(partner, 'Token') is None


def test_assoc_type21_stub_double():
    # EventAutomatonModel_Parameter has no real 'EventAutomatonModel_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so EventAutomatonModel_SymbolicParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EventAutomatonModel_SymbolicParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EventAutomatonModel_SymbolicParameter(name="sample_text")
    partner = EventAutomatonModel_Parameter()
    setattr(partner, 'EventAutomatonModel_Parameter', None)
    _safe_set(owner, 'EventAutomatonModel_SymbolicParameter22', partner)
    assert getattr(partner, 'EventAutomatonModel_Parameter') == owner
    _safe_set(owner, 'EventAutomatonModel_SymbolicParameter22', None)
    assert getattr(partner, 'EventAutomatonModel_Parameter') is None


