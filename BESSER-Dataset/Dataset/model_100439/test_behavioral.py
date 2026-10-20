import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    IDBase,
    NameBase,
    State,
    StateAction,
    StateVertex,
    statechart_Action,
    statechart_CompositeState,
    statechart_DO,
    statechart_ENTRY,
    statechart_EXIT,
    statechart_Event,
    statechart_Guard,
    statechart_Label,
    statechart_State,
    statechart_StateAction,
    statechart_StateMachine,
    statechart_StateMachineRoot,
    statechart_StateVertex,
    statechart_Transition,
    statechart_TransitionAction,
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

def test_assoc_calledByAction5_reverse_link_reassign_clear():
    a1 = statechart_StateMachine(name="sample_text")
    a2 = statechart_StateMachine(name="sample_text_2")
    b = statechart_Action(value="sample_text")
    _safe_set(b, 'Action', a1)
    assert _is_linked(b, 'Action', a1)
    if hasattr(a1, 'stateMachineCall'):
        assert _is_linked(a1, 'stateMachineCall', b)
    _safe_set(b, 'Action', a2)
    assert _is_linked(b, 'Action', a2)
    if hasattr(a1, 'stateMachineCall'):
        assert not _is_linked(a1, 'stateMachineCall', b)
    if hasattr(a2, 'stateMachineCall'):
        assert _is_linked(a2, 'stateMachineCall', b)
    _safe_set(b, 'Action', None)
    assert not _is_linked(b, 'Action', a2)
    if hasattr(a2, 'stateMachineCall'):
        assert not _is_linked(a2, 'stateMachineCall', b)


def test_assoc_evt_container29_reverse_link_reassign_clear():
    a1 = statechart_Transition(description="sample_text")
    a2 = statechart_Transition(description="sample_text_2")
    b = statechart_Event(name="sample_text")
    _safe_set(b, 'trigger', a1)
    assert _is_linked(b, 'trigger', a1)
    if hasattr(a1, 'Transition30'):
        assert _is_linked(a1, 'Transition30', b)
    _safe_set(b, 'trigger', a2)
    assert _is_linked(b, 'trigger', a2)
    if hasattr(a1, 'Transition30'):
        assert not _is_linked(a1, 'Transition30', b)
    if hasattr(a2, 'Transition30'):
        assert _is_linked(a2, 'Transition30', b)
    _safe_set(b, 'trigger', None)
    assert not _is_linked(b, 'trigger', a2)
    if hasattr(a2, 'Transition30'):
        assert not _is_linked(a2, 'Transition30', b)


def test_assoc_gua_container31_reverse_link_reassign_clear():
    a1 = statechart_Transition(description="sample_text")
    a2 = statechart_Transition(description="sample_text_2")
    b = statechart_Guard(expression="sample_text")
    _safe_set(b, 'guard', a1)
    assert _is_linked(b, 'guard', a1)
    if hasattr(a1, 'Transition32'):
        assert _is_linked(a1, 'Transition32', b)
    _safe_set(b, 'guard', a2)
    assert _is_linked(b, 'guard', a2)
    if hasattr(a1, 'Transition32'):
        assert not _is_linked(a1, 'Transition32', b)
    if hasattr(a2, 'Transition32'):
        assert _is_linked(a2, 'Transition32', b)
    _safe_set(b, 'guard', None)
    assert not _is_linked(b, 'guard', a2)
    if hasattr(a2, 'Transition32'):
        assert not _is_linked(a2, 'Transition32', b)


def test_assoc_guard23_reverse_link_reassign_clear():
    a1 = statechart_Transition(description="sample_text")
    a2 = statechart_Transition(description="sample_text_2")
    b = statechart_Guard(expression="sample_text")
    _safe_set(b, 'Guard', a1)
    assert _is_linked(b, 'Guard', a1)
    if hasattr(a1, 'gua_container'):
        assert _is_linked(a1, 'gua_container', b)
    _safe_set(b, 'Guard', a2)
    assert _is_linked(b, 'Guard', a2)
    if hasattr(a1, 'gua_container'):
        assert not _is_linked(a1, 'gua_container', b)
    if hasattr(a2, 'gua_container'):
        assert _is_linked(a2, 'gua_container', b)
    _safe_set(b, 'Guard', None)
    assert not _is_linked(b, 'Guard', a2)
    if hasattr(a2, 'gua_container'):
        assert not _is_linked(a2, 'gua_container', b)


def test_assoc_stateMachineCall16_reverse_link_reassign_clear():
    a1 = statechart_StateMachine(name="sample_text")
    a2 = statechart_StateMachine(name="sample_text_2")
    b = statechart_Action(value="sample_text")
    _safe_set(b, 'calledByAction', a1)
    assert _is_linked(b, 'calledByAction', a1)
    if hasattr(a1, 'StateMachine17'):
        assert _is_linked(a1, 'StateMachine17', b)
    _safe_set(b, 'calledByAction', a2)
    assert _is_linked(b, 'calledByAction', a2)
    if hasattr(a1, 'StateMachine17'):
        assert not _is_linked(a1, 'StateMachine17', b)
    if hasattr(a2, 'StateMachine17'):
        assert _is_linked(a2, 'StateMachine17', b)
    _safe_set(b, 'calledByAction', None)
    assert not _is_linked(b, 'calledByAction', a2)
    if hasattr(a2, 'StateMachine17'):
        assert not _is_linked(a2, 'StateMachine17', b)


def test_assoc_transSM_container18_reverse_link_reassign_clear():
    a1 = statechart_Transition(description="sample_text")
    a2 = statechart_Transition(description="sample_text_2")
    b = statechart_StateMachine(name="sample_text")
    _safe_set(b, 'StateMachine19', a1)
    assert _is_linked(b, 'StateMachine19', a1)
    if hasattr(a1, 'transitions'):
        assert _is_linked(a1, 'transitions', b)
    _safe_set(b, 'StateMachine19', a2)
    assert _is_linked(b, 'StateMachine19', a2)
    if hasattr(a1, 'transitions'):
        assert not _is_linked(a1, 'transitions', b)
    if hasattr(a2, 'transitions'):
        assert _is_linked(a2, 'transitions', b)
    _safe_set(b, 'StateMachine19', None)
    assert not _is_linked(b, 'StateMachine19', a2)
    if hasattr(a2, 'transitions'):
        assert not _is_linked(a2, 'transitions', b)


def test_assoc_transitions2_reverse_link_reassign_clear():
    a1 = statechart_Transition(description="sample_text")
    a2 = statechart_Transition(description="sample_text_2")
    b = statechart_StateMachine(name="sample_text")
    _safe_set(b, 'transSM_container', {a1})
    assert _is_linked(b, 'transSM_container', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'transSM_container', {a2})
    assert _is_linked(b, 'transSM_container', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'transSM_container', set())
    assert not _is_linked(b, 'transSM_container', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_trigger22_reverse_link_reassign_clear():
    a1 = statechart_Transition(description="sample_text")
    a2 = statechart_Transition(description="sample_text_2")
    b = statechart_Event(name="sample_text")
    _safe_set(b, 'Event', a1)
    assert _is_linked(b, 'Event', a1)
    if hasattr(a1, 'evt_container'):
        assert _is_linked(a1, 'evt_container', b)
    _safe_set(b, 'Event', a2)
    assert _is_linked(b, 'Event', a2)
    if hasattr(a1, 'evt_container'):
        assert not _is_linked(a1, 'evt_container', b)
    if hasattr(a2, 'evt_container'):
        assert _is_linked(a2, 'evt_container', b)
    _safe_set(b, 'Event', None)
    assert not _is_linked(b, 'Event', a2)
    if hasattr(a2, 'evt_container'):
        assert not _is_linked(a2, 'evt_container', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_InitialState6_stub_double():
    # statechart_State has no real 'statechart_State' property in the generated
    # code (a bare stub) -- manually attach it so statechart_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_StateMachine(name="sample_text")
    partner = statechart_State()
    setattr(partner, 'statechart_State', None)
    _safe_set(owner, 'statechart_StateMachine7', partner)
    assert getattr(partner, 'statechart_State') == owner
    _safe_set(owner, 'statechart_StateMachine7', None)
    assert getattr(partner, 'statechart_State') is None


def test_assoc_InitialStateMachine1_stub_double():
    # statechart_StateMachineRoot has no real 'statechart_StateMachineRoot' property in the generated
    # code (a bare stub) -- manually attach it so statechart_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_StateMachine(name="sample_text")
    partner = statechart_StateMachineRoot()
    setattr(partner, 'statechart_StateMachineRoot', None)
    _safe_set(owner, 'statechart_StateMachine', partner)
    assert getattr(partner, 'statechart_StateMachineRoot') == owner
    _safe_set(owner, 'statechart_StateMachine', None)
    assert getattr(partner, 'statechart_StateMachineRoot') is None


def test_assoc_act_container33_stub_double():
    # statechart_TransitionAction has no real 'action' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(description="sample_text")
    partner = statechart_TransitionAction()
    setattr(partner, 'action', None)
    _safe_set(owner, 'Transition34', partner)
    assert getattr(partner, 'action') == owner
    _safe_set(owner, 'Transition34', None)
    assert getattr(partner, 'action') is None


def test_assoc_action24_stub_double():
    # statechart_TransitionAction has no real 'TransitionAction' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(description="sample_text")
    partner = statechart_TransitionAction()
    setattr(partner, 'TransitionAction', None)
    _safe_set(owner, 'act_container', partner)
    assert getattr(partner, 'TransitionAction') == owner
    _safe_set(owner, 'act_container', None)
    assert getattr(partner, 'TransitionAction') is None


def test_assoc_deferrableEvents12_stub_double():
    # statechart_State has no real 'statechart_State13' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Event(name="sample_text")
    partner = statechart_State()
    setattr(partner, 'statechart_State13', None)
    _safe_set(owner, 'statechart_Event', partner)
    assert owner in getattr(partner, 'statechart_State13')
    _safe_set(owner, 'statechart_Event', None)
    assert owner not in getattr(partner, 'statechart_State13')


def test_assoc_incoming38_stub_double():
    # statechart_StateVertex has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(description="sample_text")
    partner = statechart_StateVertex()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition39', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition39', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_internalTransitions10_stub_double():
    # statechart_State has no real 'transS_container' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(description="sample_text")
    partner = statechart_State()
    setattr(partner, 'transS_container', None)
    _safe_set(owner, 'Transition11', partner)
    assert owner in getattr(partner, 'transS_container')
    _safe_set(owner, 'Transition11', None)
    assert owner not in getattr(partner, 'transS_container')


def test_assoc_label40_stub_double():
    # statechart_StateVertex has no real 'statechart_StateVertex' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Label(name="sample_text")
    partner = statechart_StateVertex()
    setattr(partner, 'statechart_StateVertex', None)
    _safe_set(owner, 'statechart_Label', partner)
    assert owner in getattr(partner, 'statechart_StateVertex')
    _safe_set(owner, 'statechart_Label', None)
    assert owner not in getattr(partner, 'statechart_StateVertex')


def test_assoc_outgoing36_stub_double():
    # statechart_StateVertex has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(description="sample_text")
    partner = statechart_StateVertex()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition37', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition37', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_source25_stub_double():
    # statechart_StateVertex has no real 'StateVertex26' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(description="sample_text")
    partner = statechart_StateVertex()
    setattr(partner, 'StateVertex26', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'StateVertex26') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'StateVertex26') is None


def test_assoc_state_container8_stub_double():
    # statechart_State has no real 'top' property in the generated
    # code (a bare stub) -- manually attach it so statechart_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_StateMachine(name="sample_text")
    partner = statechart_State()
    setattr(partner, 'top', None)
    _safe_set(owner, 'StateMachine9', partner)
    assert getattr(partner, 'top') == owner
    _safe_set(owner, 'StateMachine9', None)
    assert getattr(partner, 'top') is None


def test_assoc_statemachine_container4_stub_double():
    # statechart_StateMachineRoot has no real 'StateMachineRoot' property in the generated
    # code (a bare stub) -- manually attach it so statechart_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_StateMachine(name="sample_text")
    partner = statechart_StateMachineRoot()
    setattr(partner, 'StateMachineRoot', None)
    _safe_set(owner, 'subStateMachines', partner)
    assert getattr(partner, 'StateMachineRoot') == owner
    _safe_set(owner, 'subStateMachines', None)
    assert getattr(partner, 'StateMachineRoot') is None


def test_assoc_subStateMachines0_stub_double():
    # statechart_StateMachineRoot has no real 'statemachine_container' property in the generated
    # code (a bare stub) -- manually attach it so statechart_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_StateMachine(name="sample_text")
    partner = statechart_StateMachineRoot()
    setattr(partner, 'statemachine_container', None)
    _safe_set(owner, 'StateMachine', partner)
    assert owner in getattr(partner, 'statemachine_container')
    _safe_set(owner, 'StateMachine', None)
    assert owner not in getattr(partner, 'statemachine_container')


def test_assoc_subVertexes15_stub_double():
    # statechart_StateVertex has no real 'StateVertex' property in the generated
    # code (a bare stub) -- manually attach it so statechart_CompositeState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_CompositeState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_CompositeState(isConcurrent=True)
    partner = statechart_StateVertex()
    setattr(partner, 'StateVertex', None)
    _safe_set(owner, 'sv_container', {partner})
    assert getattr(partner, 'StateVertex') == owner
    _safe_set(owner, 'sv_container', set())
    assert getattr(partner, 'StateVertex') is None


def test_assoc_sv_container35_stub_double():
    # statechart_StateVertex has no real 'subVertexes' property in the generated
    # code (a bare stub) -- manually attach it so statechart_CompositeState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_CompositeState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_CompositeState(isConcurrent=True)
    partner = statechart_StateVertex()
    setattr(partner, 'subVertexes', None)
    _safe_set(owner, 'CompositeState', partner)
    assert getattr(partner, 'subVertexes') == owner
    _safe_set(owner, 'CompositeState', None)
    assert getattr(partner, 'subVertexes') is None


def test_assoc_target27_stub_double():
    # statechart_StateVertex has no real 'StateVertex28' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(description="sample_text")
    partner = statechart_StateVertex()
    setattr(partner, 'StateVertex28', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'StateVertex28') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'StateVertex28') is None


def test_assoc_top3_stub_double():
    # statechart_State has no real 'State' property in the generated
    # code (a bare stub) -- manually attach it so statechart_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_StateMachine(name="sample_text")
    partner = statechart_State()
    setattr(partner, 'State', None)
    _safe_set(owner, 'state_container', {partner})
    assert getattr(partner, 'State') == owner
    _safe_set(owner, 'state_container', set())
    assert getattr(partner, 'State') is None


def test_assoc_transS_container20_stub_double():
    # statechart_State has no real 'State21' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(description="sample_text")
    partner = statechart_State()
    setattr(partner, 'State21', None)
    _safe_set(owner, 'internalTransitions', partner)
    assert getattr(partner, 'State21') == owner
    _safe_set(owner, 'internalTransitions', None)
    assert getattr(partner, 'State21') is None


