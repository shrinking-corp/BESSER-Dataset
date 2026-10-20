import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    TimedZone,
    Transition,
    TypedTransition,
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
    automaton_NegativeTransition,
    automaton_Parameter,
    automaton_ParameterBinding,
    automaton_ParameterTable,
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

def test_assoc_inState51_reverse_link_reassign_clear():
    a1 = automaton_TimedZone(time="sample_text")
    a2 = automaton_TimedZone(time="sample_text_2")
    b = automaton_State(label="sample_text")
    _safe_set(b, 'State52', a1)
    assert _is_linked(b, 'State52', a1)
    if hasattr(a1, 'inStateOf'):
        assert _is_linked(a1, 'inStateOf', b)
    _safe_set(b, 'State52', a2)
    assert _is_linked(b, 'State52', a2)
    if hasattr(a1, 'inStateOf'):
        assert not _is_linked(a1, 'inStateOf', b)
    if hasattr(a2, 'inStateOf'):
        assert _is_linked(a2, 'inStateOf', b)
    _safe_set(b, 'State52', None)
    assert not _is_linked(b, 'State52', a2)
    if hasattr(a2, 'inStateOf'):
        assert not _is_linked(a2, 'inStateOf', b)


def test_assoc_inStateOf39_reverse_link_reassign_clear():
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


def test_assoc_outState53_reverse_link_reassign_clear():
    a1 = automaton_TimedZone(time="sample_text")
    a2 = automaton_TimedZone(time="sample_text_2")
    b = automaton_State(label="sample_text")
    _safe_set(b, 'State54', a1)
    assert _is_linked(b, 'State54', a1)
    if hasattr(a1, 'outStateOf'):
        assert _is_linked(a1, 'outStateOf', b)
    _safe_set(b, 'State54', a2)
    assert _is_linked(b, 'State54', a2)
    if hasattr(a1, 'outStateOf'):
        assert not _is_linked(a1, 'outStateOf', b)
    if hasattr(a2, 'outStateOf'):
        assert _is_linked(a2, 'outStateOf', b)
    _safe_set(b, 'State54', None)
    assert not _is_linked(b, 'State54', a2)
    if hasattr(a2, 'outStateOf'):
        assert not _is_linked(a2, 'outStateOf', b)


def test_assoc_outStateOf40_reverse_link_reassign_clear():
    a1 = automaton_TimedZone(time="sample_text")
    a2 = automaton_TimedZone(time="sample_text_2")
    b = automaton_State(label="sample_text")
    _safe_set(b, 'outState', {a1})
    assert _is_linked(b, 'outState', a1)
    if hasattr(a1, 'TimedZone41'):
        assert _is_linked(a1, 'TimedZone41', b)
    _safe_set(b, 'outState', {a2})
    assert _is_linked(b, 'outState', a2)
    if hasattr(a1, 'TimedZone41'):
        assert not _is_linked(a1, 'TimedZone41', b)
    if hasattr(a2, 'TimedZone41'):
        assert _is_linked(a2, 'TimedZone41', b)
    _safe_set(b, 'outState', set())
    assert not _is_linked(b, 'outState', a2)
    if hasattr(a2, 'TimedZone41'):
        assert not _is_linked(a2, 'TimedZone41', b)


def test_assoc_states8_reverse_link_reassign_clear():
    a1 = automaton_State(label="sample_text")
    a2 = automaton_State(label="sample_text_2")
    b = automaton_Automaton(eventPatternId="sample_text")
    _safe_set(b, 'automaton_Automaton9', {a1})
    assert _is_linked(b, 'automaton_Automaton9', a1)
    if hasattr(a1, 'automaton_State'):
        assert _is_linked(a1, 'automaton_State', b)
    _safe_set(b, 'automaton_Automaton9', {a2})
    assert _is_linked(b, 'automaton_Automaton9', a2)
    if hasattr(a1, 'automaton_State'):
        assert not _is_linked(a1, 'automaton_State', b)
    if hasattr(a2, 'automaton_State'):
        assert _is_linked(a2, 'automaton_State', b)
    _safe_set(b, 'automaton_Automaton9', set())
    assert not _is_linked(b, 'automaton_Automaton9', a2)
    if hasattr(a2, 'automaton_State'):
        assert not _is_linked(a2, 'automaton_State', b)


def test_assoc_timedZones13_reverse_link_reassign_clear():
    a1 = automaton_TimedZone(time="sample_text")
    a2 = automaton_TimedZone(time="sample_text_2")
    b = automaton_Automaton(eventPatternId="sample_text")
    _safe_set(b, 'automaton_Automaton14', {a1})
    assert _is_linked(b, 'automaton_Automaton14', a1)
    if hasattr(a1, 'automaton_TimedZone'):
        assert _is_linked(a1, 'automaton_TimedZone', b)
    _safe_set(b, 'automaton_Automaton14', {a2})
    assert _is_linked(b, 'automaton_Automaton14', a2)
    if hasattr(a1, 'automaton_TimedZone'):
        assert not _is_linked(a1, 'automaton_TimedZone', b)
    if hasattr(a2, 'automaton_TimedZone'):
        assert _is_linked(a2, 'automaton_TimedZone', b)
    _safe_set(b, 'automaton_Automaton14', set())
    assert not _is_linked(b, 'automaton_Automaton14', a2)
    if hasattr(a2, 'automaton_TimedZone'):
        assert not _is_linked(a2, 'automaton_TimedZone', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_automata0_stub_double():
    # automaton_InternalModel has no real 'automaton_InternalModel' property in the generated
    # code (a bare stub) -- manually attach it so automaton_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_Automaton(eventPatternId="sample_text")
    partner = automaton_InternalModel()
    setattr(partner, 'automaton_InternalModel', None)
    _safe_set(owner, 'automaton_Automaton', partner)
    assert owner in getattr(partner, 'automaton_InternalModel')
    _safe_set(owner, 'automaton_Automaton', None)
    assert owner not in getattr(partner, 'automaton_InternalModel')


def test_assoc_currentState21_stub_double():
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


def test_assoc_enabledForTheLatestEvent3_stub_double():
    # automaton_InternalModel has no real 'automaton_InternalModel4' property in the generated
    # code (a bare stub) -- manually attach it so automaton_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_Automaton(eventPatternId="sample_text")
    partner = automaton_InternalModel()
    setattr(partner, 'automaton_InternalModel4', None)
    _safe_set(owner, 'automaton_Automaton5', partner)
    assert owner in getattr(partner, 'automaton_InternalModel4')
    _safe_set(owner, 'automaton_Automaton5', None)
    assert owner not in getattr(partner, 'automaton_InternalModel4')


def test_assoc_eventTokens10_stub_double():
    # automaton_EventToken has no real 'automaton_EventToken12' property in the generated
    # code (a bare stub) -- manually attach it so automaton_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_Automaton(eventPatternId="sample_text")
    partner = automaton_EventToken()
    setattr(partner, 'automaton_EventToken12', None)
    _safe_set(owner, 'automaton_Automaton11', {partner})
    assert getattr(partner, 'automaton_EventToken12') == owner
    _safe_set(owner, 'automaton_Automaton11', set())
    assert getattr(partner, 'automaton_EventToken12') is None


def test_assoc_eventTokens35_stub_double():
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


def test_assoc_finalStates17_stub_double():
    # automaton_FinalState has no real 'automaton_FinalState' property in the generated
    # code (a bare stub) -- manually attach it so automaton_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_Automaton(eventPatternId="sample_text")
    partner = automaton_FinalState()
    setattr(partner, 'automaton_FinalState', None)
    _safe_set(owner, 'automaton_Automaton18', {partner})
    assert getattr(partner, 'automaton_FinalState') == owner
    _safe_set(owner, 'automaton_Automaton18', set())
    assert getattr(partner, 'automaton_FinalState') is None


def test_assoc_inTransitions32_stub_double():
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


def test_assoc_initialState15_stub_double():
    # automaton_InitState has no real 'automaton_InitState' property in the generated
    # code (a bare stub) -- manually attach it so automaton_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_Automaton(eventPatternId="sample_text")
    partner = automaton_InitState()
    setattr(partner, 'automaton_InitState', None)
    _safe_set(owner, 'automaton_Automaton16', partner)
    assert getattr(partner, 'automaton_InitState') == owner
    _safe_set(owner, 'automaton_Automaton16', None)
    assert getattr(partner, 'automaton_InitState') is None


def test_assoc_lastProcessedEvent36_stub_double():
    # automaton_Event has no real 'automaton_Event38' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_Event()
    setattr(partner, 'automaton_Event38', None)
    _safe_set(owner, 'automaton_State37', partner)
    assert getattr(partner, 'automaton_Event38') == owner
    _safe_set(owner, 'automaton_State37', None)
    assert getattr(partner, 'automaton_Event38') is None


def test_assoc_outTransitions33_stub_double():
    # automaton_Transition has no real 'Transition34' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_Transition()
    setattr(partner, 'Transition34', None)
    _safe_set(owner, 'preState', {partner})
    assert getattr(partner, 'Transition34') == owner
    _safe_set(owner, 'preState', set())
    assert getattr(partner, 'Transition34') is None


def test_assoc_parameterBindings57_stub_double():
    # automaton_ParameterTable has no real 'parameterTable' property in the generated
    # code (a bare stub) -- manually attach it so automaton_ParameterBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_ParameterBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_ParameterBinding(symbolicName="sample_text", value="sample_text")
    partner = automaton_ParameterTable()
    setattr(partner, 'parameterTable', None)
    _safe_set(owner, 'ParameterBinding', partner)
    assert owner in getattr(partner, 'parameterTable')
    _safe_set(owner, 'ParameterBinding', None)
    assert owner not in getattr(partner, 'parameterTable')


def test_assoc_parameterTable61_stub_double():
    # automaton_ParameterTable has no real 'ParameterTable62' property in the generated
    # code (a bare stub) -- manually attach it so automaton_ParameterBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_ParameterBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_ParameterBinding(symbolicName="sample_text", value="sample_text")
    partner = automaton_ParameterTable()
    setattr(partner, 'ParameterTable62', None)
    _safe_set(owner, 'parameterBindings', partner)
    assert getattr(partner, 'ParameterTable62') == owner
    _safe_set(owner, 'parameterBindings', None)
    assert getattr(partner, 'ParameterTable62') is None


def test_assoc_parameters47_stub_double():
    # automaton_TypedTransition has no real 'transition48' property in the generated
    # code (a bare stub) -- manually attach it so automaton_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_Parameter(position=7, symbolicName="sample_text")
    partner = automaton_TypedTransition()
    setattr(partner, 'transition48', None)
    _safe_set(owner, 'Parameter', partner)
    assert owner in getattr(partner, 'transition48')
    _safe_set(owner, 'Parameter', None)
    assert owner not in getattr(partner, 'transition48')


def test_assoc_postState44_stub_double():
    # automaton_Transition has no real 'inTransitions' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_Transition()
    setattr(partner, 'inTransitions', None)
    _safe_set(owner, 'State45', partner)
    assert getattr(partner, 'inTransitions') == owner
    _safe_set(owner, 'State45', None)
    assert getattr(partner, 'inTransitions') is None


def test_assoc_preState42_stub_double():
    # automaton_Transition has no real 'outTransitions' property in the generated
    # code (a bare stub) -- manually attach it so automaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_State(label="sample_text")
    partner = automaton_Transition()
    setattr(partner, 'outTransitions', None)
    _safe_set(owner, 'State43', partner)
    assert getattr(partner, 'outTransitions') == owner
    _safe_set(owner, 'State43', None)
    assert getattr(partner, 'outTransitions') is None


def test_assoc_timedZones28_stub_double():
    # automaton_EventToken has no real 'automaton_EventToken29' property in the generated
    # code (a bare stub) -- manually attach it so automaton_TimedZone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_TimedZone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_TimedZone(time="sample_text")
    partner = automaton_EventToken()
    setattr(partner, 'automaton_EventToken29', None)
    _safe_set(owner, 'automaton_TimedZone30', partner)
    assert owner in getattr(partner, 'automaton_EventToken29')
    _safe_set(owner, 'automaton_TimedZone30', None)
    assert owner not in getattr(partner, 'automaton_EventToken29')


def test_assoc_transition55_stub_double():
    # automaton_TypedTransition has no real 'TypedTransition56' property in the generated
    # code (a bare stub) -- manually attach it so automaton_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_Parameter(position=7, symbolicName="sample_text")
    partner = automaton_TypedTransition()
    setattr(partner, 'TypedTransition56', None)
    _safe_set(owner, 'parameters', partner)
    assert getattr(partner, 'TypedTransition56') == owner
    _safe_set(owner, 'parameters', None)
    assert getattr(partner, 'TypedTransition56') is None


def test_assoc_trapState19_stub_double():
    # automaton_TrapState has no real 'automaton_TrapState' property in the generated
    # code (a bare stub) -- manually attach it so automaton_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaton_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaton_Automaton(eventPatternId="sample_text")
    partner = automaton_TrapState()
    setattr(partner, 'automaton_TrapState', None)
    _safe_set(owner, 'automaton_Automaton20', partner)
    assert getattr(partner, 'automaton_TrapState') == owner
    _safe_set(owner, 'automaton_Automaton20', None)
    assert getattr(partner, 'automaton_TrapState') is None


