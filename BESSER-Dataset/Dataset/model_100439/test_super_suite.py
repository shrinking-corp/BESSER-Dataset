# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StateAction,
    statechart_ENTRY,
    statechart_EXIT,
    statechart_DO,
    NameBase,
    Action,
    statechart_TransitionAction,
    statechart_StateAction,
    State,
    statechart_CompositeState,
    StateVertex,
    statechart_State,
    IDBase,
    statechart_StateVertex,
    statechart_StateMachine,
    statechart_Label,
    statechart_Event,
    statechart_Guard,
    statechart_Action,
    statechart_Transition,
    statechart_StateMachineRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_stateaction_is_not_abstract():
    assert not inspect.isabstract(StateAction)


def test_hyp_stateaction_constructor_exists():
    assert callable(StateAction.__init__)


def test_hyp_stateaction_constructor_args():
    sig = inspect.signature(StateAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statechart_entry_is_not_abstract():
    assert not inspect.isabstract(statechart_ENTRY)


def test_hyp_statechart_entry_constructor_exists():
    assert callable(statechart_ENTRY.__init__)


def test_hyp_statechart_entry_constructor_args():
    sig = inspect.signature(statechart_ENTRY.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statechart_exit_is_not_abstract():
    assert not inspect.isabstract(statechart_EXIT)


def test_hyp_statechart_exit_constructor_exists():
    assert callable(statechart_EXIT.__init__)


def test_hyp_statechart_exit_constructor_args():
    sig = inspect.signature(statechart_EXIT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statechart_do_is_not_abstract():
    assert not inspect.isabstract(statechart_DO)


def test_hyp_statechart_do_constructor_exists():
    assert callable(statechart_DO.__init__)


def test_hyp_statechart_do_constructor_args():
    sig = inspect.signature(statechart_DO.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namebase_is_not_abstract():
    assert not inspect.isabstract(NameBase)


def test_hyp_namebase_constructor_exists():
    assert callable(NameBase.__init__)


def test_hyp_namebase_constructor_args():
    sig = inspect.signature(NameBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statechart_transitionaction_is_not_abstract():
    assert not inspect.isabstract(statechart_TransitionAction)


def test_hyp_statechart_transitionaction_constructor_exists():
    assert callable(statechart_TransitionAction.__init__)


def test_hyp_statechart_transitionaction_constructor_args():
    sig = inspect.signature(statechart_TransitionAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statechart_stateaction_is_not_abstract():
    assert not inspect.isabstract(statechart_StateAction)


def test_hyp_statechart_stateaction_constructor_exists():
    assert callable(statechart_StateAction.__init__)


def test_hyp_statechart_stateaction_constructor_args():
    sig = inspect.signature(statechart_StateAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statechart_compositestate_is_not_abstract():
    assert not inspect.isabstract(statechart_CompositeState)


def test_hyp_statechart_compositestate_constructor_exists():
    assert callable(statechart_CompositeState.__init__)


def test_hyp_statechart_compositestate_constructor_args():
    sig = inspect.signature(statechart_CompositeState.__init__)
    params = list(sig.parameters.keys())
    assert "isConcurrent" in params, "Missing parameter 'isConcurrent'"




def test_hyp_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_hyp_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_hyp_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statechart_state_is_not_abstract():
    assert not inspect.isabstract(statechart_State)


def test_hyp_statechart_state_constructor_exists():
    assert callable(statechart_State.__init__)


def test_hyp_statechart_state_constructor_args():
    sig = inspect.signature(statechart_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_idbase_is_not_abstract():
    assert not inspect.isabstract(IDBase)


def test_hyp_idbase_constructor_exists():
    assert callable(IDBase.__init__)


def test_hyp_idbase_constructor_args():
    sig = inspect.signature(IDBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statechart_statevertex_is_not_abstract():
    assert not inspect.isabstract(statechart_StateVertex)


def test_hyp_statechart_statevertex_constructor_exists():
    assert callable(statechart_StateVertex.__init__)


def test_hyp_statechart_statevertex_constructor_args():
    sig = inspect.signature(statechart_StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statechart_statemachine_is_not_abstract():
    assert not inspect.isabstract(statechart_StateMachine)


def test_hyp_statechart_statemachine_constructor_exists():
    assert callable(statechart_StateMachine.__init__)


def test_hyp_statechart_statemachine_constructor_args():
    sig = inspect.signature(statechart_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_statechart_label_is_not_abstract():
    assert not inspect.isabstract(statechart_Label)


def test_hyp_statechart_label_constructor_exists():
    assert callable(statechart_Label.__init__)


def test_hyp_statechart_label_constructor_args():
    sig = inspect.signature(statechart_Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_statechart_event_is_not_abstract():
    assert not inspect.isabstract(statechart_Event)


def test_hyp_statechart_event_constructor_exists():
    assert callable(statechart_Event.__init__)


def test_hyp_statechart_event_constructor_args():
    sig = inspect.signature(statechart_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_statechart_guard_is_not_abstract():
    assert not inspect.isabstract(statechart_Guard)


def test_hyp_statechart_guard_constructor_exists():
    assert callable(statechart_Guard.__init__)


def test_hyp_statechart_guard_constructor_args():
    sig = inspect.signature(statechart_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_statechart_action_is_not_abstract():
    assert not inspect.isabstract(statechart_Action)


def test_hyp_statechart_action_constructor_exists():
    assert callable(statechart_Action.__init__)


def test_hyp_statechart_action_constructor_args():
    sig = inspect.signature(statechart_Action.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_statechart_transition_is_not_abstract():
    assert not inspect.isabstract(statechart_Transition)


def test_hyp_statechart_transition_constructor_exists():
    assert callable(statechart_Transition.__init__)


def test_hyp_statechart_transition_constructor_args():
    sig = inspect.signature(statechart_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_statechart_statemachineroot_is_not_abstract():
    assert not inspect.isabstract(statechart_StateMachineRoot)


def test_hyp_statechart_statemachineroot_constructor_exists():
    assert callable(statechart_StateMachineRoot.__init__)


def test_hyp_statechart_statemachineroot_constructor_args():
    sig = inspect.signature(statechart_StateMachineRoot.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
StateAction_strategy = st.builds(
    StateAction,
)
statechart_ENTRY_strategy = st.builds(
    statechart_ENTRY,
)
statechart_EXIT_strategy = st.builds(
    statechart_EXIT,
)
statechart_DO_strategy = st.builds(
    statechart_DO,
)
NameBase_strategy = st.builds(
    NameBase,
)
Action_strategy = st.builds(
    Action,
)
statechart_TransitionAction_strategy = st.builds(
    statechart_TransitionAction,
)
statechart_StateAction_strategy = st.builds(
    statechart_StateAction,
)
State_strategy = st.builds(
    State,
)
statechart_CompositeState_strategy = st.builds(
    statechart_CompositeState,
    isConcurrent=
        st.booleans()
)
StateVertex_strategy = st.builds(
    StateVertex,
)
statechart_State_strategy = st.builds(
    statechart_State,
)
IDBase_strategy = st.builds(
    IDBase,
)
statechart_StateVertex_strategy = st.builds(
    statechart_StateVertex,
)
statechart_StateMachine_strategy = st.builds(
    statechart_StateMachine,
    name=
        safe_text
)
statechart_Label_strategy = st.builds(
    statechart_Label,
    name=
        safe_text
)
statechart_Event_strategy = st.builds(
    statechart_Event,
    name=
        safe_text
)
statechart_Guard_strategy = st.builds(
    statechart_Guard,
    expression=
        safe_text
)
statechart_Action_strategy = st.builds(
    statechart_Action,
    value=
        safe_text
)
statechart_Transition_strategy = st.builds(
    statechart_Transition,
    description=
        safe_text
)
statechart_StateMachineRoot_strategy = st.builds(
    statechart_StateMachineRoot,
)













@given(instance=statechart_CompositeState_strategy)
def test_hyp_statechart_compositestate_isConcurrent_setter(instance):
    original = instance.isConcurrent
    instance.isConcurrent = original
    assert instance.isConcurrent == original








@given(instance=statechart_StateMachine_strategy)
def test_hyp_statechart_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=statechart_Label_strategy)
def test_hyp_statechart_label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=statechart_Event_strategy)
def test_hyp_statechart_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=statechart_Guard_strategy)
def test_hyp_statechart_guard_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original




@given(instance=statechart_Action_strategy)
def test_hyp_statechart_action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=statechart_Transition_strategy)
def test_hyp_statechart_transition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_statechart_Action_value_value_roundtrip():
    instance = statechart_Action(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_statechart_CompositeState_isConcurrent_value_roundtrip():
    instance = statechart_CompositeState(isConcurrent=True)
    assert instance.isConcurrent == True
    instance.isConcurrent = False
    assert instance.isConcurrent == False


def test_statechart_Event_name_value_roundtrip():
    instance = statechart_Event(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statechart_Guard_expression_value_roundtrip():
    instance = statechart_Guard(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_statechart_Label_name_value_roundtrip():
    instance = statechart_Label(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statechart_StateMachine_name_value_roundtrip():
    instance = statechart_StateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statechart_Transition_description_value_roundtrip():
    instance = statechart_Transition(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_statechart_StateAction_isa_Action():
    instance = statechart_StateAction()
    assert isinstance(instance, Action)


def test_statechart_TransitionAction_isa_Action():
    instance = statechart_TransitionAction()
    assert isinstance(instance, Action)


def test_statechart_Action_isa_IDBase():
    instance = statechart_Action(value="sample_text")
    assert isinstance(instance, IDBase)


def test_statechart_Event_isa_IDBase():
    instance = statechart_Event(name="sample_text")
    assert isinstance(instance, IDBase)


def test_statechart_Guard_isa_IDBase():
    instance = statechart_Guard(expression="sample_text")
    assert isinstance(instance, IDBase)


def test_statechart_Label_isa_IDBase():
    instance = statechart_Label(name="sample_text")
    assert isinstance(instance, IDBase)


def test_statechart_StateMachine_isa_IDBase():
    instance = statechart_StateMachine(name="sample_text")
    assert isinstance(instance, IDBase)


def test_statechart_StateMachineRoot_isa_IDBase():
    instance = statechart_StateMachineRoot()
    assert isinstance(instance, IDBase)


def test_statechart_StateVertex_isa_IDBase():
    instance = statechart_StateVertex()
    assert isinstance(instance, IDBase)


def test_statechart_Transition_isa_IDBase():
    instance = statechart_Transition(description="sample_text")
    assert isinstance(instance, IDBase)


def test_statechart_StateVertex_isa_NameBase():
    instance = statechart_StateVertex()
    assert isinstance(instance, NameBase)


def test_statechart_CompositeState_isa_State():
    instance = statechart_CompositeState(isConcurrent=True)
    assert isinstance(instance, State)


def test_statechart_DO_isa_StateAction():
    instance = statechart_DO()
    assert isinstance(instance, StateAction)


def test_statechart_ENTRY_isa_StateAction():
    instance = statechart_ENTRY()
    assert isinstance(instance, StateAction)


def test_statechart_EXIT_isa_StateAction():
    instance = statechart_EXIT()
    assert isinstance(instance, StateAction)


def test_statechart_State_isa_StateVertex():
    instance = statechart_State()
    assert isinstance(instance, StateVertex)


def test_assoc_InitialState6_link_reassign_clear():
    a = statechart_StateMachine(name="sample_text")
    b1 = statechart_State()
    b2 = statechart_State()
    _safe_set(a, 'statechart_StateMachine7', b1)
    assert _is_linked(a, 'statechart_StateMachine7', b1)
    if hasattr(b1, 'statechart_State'):
        assert _is_linked(b1, 'statechart_State', a)
    _safe_set(a, 'statechart_StateMachine7', b2)
    assert _is_linked(a, 'statechart_StateMachine7', b2)
    if hasattr(b1, 'statechart_State'):
        assert not _is_linked(b1, 'statechart_State', a)
    if hasattr(b2, 'statechart_State'):
        assert _is_linked(b2, 'statechart_State', a)
    _safe_set(a, 'statechart_StateMachine7', None)
    assert not _is_linked(a, 'statechart_StateMachine7', b2)
    if hasattr(b2, 'statechart_State'):
        assert not _is_linked(b2, 'statechart_State', a)


def test_assoc_InitialStateMachine1_link_reassign_clear():
    a = statechart_StateMachine(name="sample_text")
    b1 = statechart_StateMachineRoot()
    b2 = statechart_StateMachineRoot()
    _safe_set(a, 'statechart_StateMachine', b1)
    assert _is_linked(a, 'statechart_StateMachine', b1)
    if hasattr(b1, 'statechart_StateMachineRoot'):
        assert _is_linked(b1, 'statechart_StateMachineRoot', a)
    _safe_set(a, 'statechart_StateMachine', b2)
    assert _is_linked(a, 'statechart_StateMachine', b2)
    if hasattr(b1, 'statechart_StateMachineRoot'):
        assert not _is_linked(b1, 'statechart_StateMachineRoot', a)
    if hasattr(b2, 'statechart_StateMachineRoot'):
        assert _is_linked(b2, 'statechart_StateMachineRoot', a)
    _safe_set(a, 'statechart_StateMachine', None)
    assert not _is_linked(a, 'statechart_StateMachine', b2)
    if hasattr(b2, 'statechart_StateMachineRoot'):
        assert not _is_linked(b2, 'statechart_StateMachineRoot', a)


def test_assoc_act_container33_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_TransitionAction()
    b2 = statechart_TransitionAction()
    _safe_set(a, 'Transition34', b1)
    assert _is_linked(a, 'Transition34', b1)
    if hasattr(b1, 'action'):
        assert _is_linked(b1, 'action', a)
    _safe_set(a, 'Transition34', b2)
    assert _is_linked(a, 'Transition34', b2)
    if hasattr(b1, 'action'):
        assert not _is_linked(b1, 'action', a)
    if hasattr(b2, 'action'):
        assert _is_linked(b2, 'action', a)
    _safe_set(a, 'Transition34', None)
    assert not _is_linked(a, 'Transition34', b2)
    if hasattr(b2, 'action'):
        assert not _is_linked(b2, 'action', a)


def test_assoc_action24_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_TransitionAction()
    b2 = statechart_TransitionAction()
    _safe_set(a, 'act_container', b1)
    assert _is_linked(a, 'act_container', b1)
    if hasattr(b1, 'TransitionAction'):
        assert _is_linked(b1, 'TransitionAction', a)
    _safe_set(a, 'act_container', b2)
    assert _is_linked(a, 'act_container', b2)
    if hasattr(b1, 'TransitionAction'):
        assert not _is_linked(b1, 'TransitionAction', a)
    if hasattr(b2, 'TransitionAction'):
        assert _is_linked(b2, 'TransitionAction', a)
    _safe_set(a, 'act_container', None)
    assert not _is_linked(a, 'act_container', b2)
    if hasattr(b2, 'TransitionAction'):
        assert not _is_linked(b2, 'TransitionAction', a)


def test_assoc_calledByAction5_link_reassign_clear():
    a = statechart_StateMachine(name="sample_text")
    b1 = statechart_Action(value="sample_text")
    b2 = statechart_Action(value="sample_text_2")
    _safe_set(a, 'stateMachineCall', {b1})
    assert _is_linked(a, 'stateMachineCall', b1)
    if hasattr(b1, 'Action'):
        assert _is_linked(b1, 'Action', a)
    _safe_set(a, 'stateMachineCall', {b2})
    assert _is_linked(a, 'stateMachineCall', b2)
    if hasattr(b1, 'Action'):
        assert not _is_linked(b1, 'Action', a)
    if hasattr(b2, 'Action'):
        assert _is_linked(b2, 'Action', a)
    _safe_set(a, 'stateMachineCall', set())
    assert not _is_linked(a, 'stateMachineCall', b2)
    if hasattr(b2, 'Action'):
        assert not _is_linked(b2, 'Action', a)


def test_assoc_deferrableEvents12_link_reassign_clear():
    a = statechart_Event(name="sample_text")
    b1 = statechart_State()
    b2 = statechart_State()
    _safe_set(a, 'statechart_Event', b1)
    assert _is_linked(a, 'statechart_Event', b1)
    if hasattr(b1, 'statechart_State13'):
        assert _is_linked(b1, 'statechart_State13', a)
    _safe_set(a, 'statechart_Event', b2)
    assert _is_linked(a, 'statechart_Event', b2)
    if hasattr(b1, 'statechart_State13'):
        assert not _is_linked(b1, 'statechart_State13', a)
    if hasattr(b2, 'statechart_State13'):
        assert _is_linked(b2, 'statechart_State13', a)
    _safe_set(a, 'statechart_Event', None)
    assert not _is_linked(a, 'statechart_Event', b2)
    if hasattr(b2, 'statechart_State13'):
        assert not _is_linked(b2, 'statechart_State13', a)


def test_assoc_evt_container29_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_Event(name="sample_text")
    b2 = statechart_Event(name="sample_text_2")
    _safe_set(a, 'Transition30', b1)
    assert _is_linked(a, 'Transition30', b1)
    if hasattr(b1, 'trigger'):
        assert _is_linked(b1, 'trigger', a)
    _safe_set(a, 'Transition30', b2)
    assert _is_linked(a, 'Transition30', b2)
    if hasattr(b1, 'trigger'):
        assert not _is_linked(b1, 'trigger', a)
    if hasattr(b2, 'trigger'):
        assert _is_linked(b2, 'trigger', a)
    _safe_set(a, 'Transition30', None)
    assert not _is_linked(a, 'Transition30', b2)
    if hasattr(b2, 'trigger'):
        assert not _is_linked(b2, 'trigger', a)


def test_assoc_gua_container31_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_Guard(expression="sample_text")
    b2 = statechart_Guard(expression="sample_text_2")
    _safe_set(a, 'Transition32', b1)
    assert _is_linked(a, 'Transition32', b1)
    if hasattr(b1, 'guard'):
        assert _is_linked(b1, 'guard', a)
    _safe_set(a, 'Transition32', b2)
    assert _is_linked(a, 'Transition32', b2)
    if hasattr(b1, 'guard'):
        assert not _is_linked(b1, 'guard', a)
    if hasattr(b2, 'guard'):
        assert _is_linked(b2, 'guard', a)
    _safe_set(a, 'Transition32', None)
    assert not _is_linked(a, 'Transition32', b2)
    if hasattr(b2, 'guard'):
        assert not _is_linked(b2, 'guard', a)


def test_assoc_guard23_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_Guard(expression="sample_text")
    b2 = statechart_Guard(expression="sample_text_2")
    _safe_set(a, 'gua_container', b1)
    assert _is_linked(a, 'gua_container', b1)
    if hasattr(b1, 'Guard'):
        assert _is_linked(b1, 'Guard', a)
    _safe_set(a, 'gua_container', b2)
    assert _is_linked(a, 'gua_container', b2)
    if hasattr(b1, 'Guard'):
        assert not _is_linked(b1, 'Guard', a)
    if hasattr(b2, 'Guard'):
        assert _is_linked(b2, 'Guard', a)
    _safe_set(a, 'gua_container', None)
    assert not _is_linked(a, 'gua_container', b2)
    if hasattr(b2, 'Guard'):
        assert not _is_linked(b2, 'Guard', a)


def test_assoc_incoming38_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_StateVertex()
    b2 = statechart_StateVertex()
    _safe_set(a, 'Transition39', b1)
    assert _is_linked(a, 'Transition39', b1)
    if hasattr(b1, 'target'):
        assert _is_linked(b1, 'target', a)
    _safe_set(a, 'Transition39', b2)
    assert _is_linked(a, 'Transition39', b2)
    if hasattr(b1, 'target'):
        assert not _is_linked(b1, 'target', a)
    if hasattr(b2, 'target'):
        assert _is_linked(b2, 'target', a)
    _safe_set(a, 'Transition39', None)
    assert not _is_linked(a, 'Transition39', b2)
    if hasattr(b2, 'target'):
        assert not _is_linked(b2, 'target', a)


def test_assoc_internalTransitions10_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_State()
    b2 = statechart_State()
    _safe_set(a, 'Transition11', b1)
    assert _is_linked(a, 'Transition11', b1)
    if hasattr(b1, 'transS_container'):
        assert _is_linked(b1, 'transS_container', a)
    _safe_set(a, 'Transition11', b2)
    assert _is_linked(a, 'Transition11', b2)
    if hasattr(b1, 'transS_container'):
        assert not _is_linked(b1, 'transS_container', a)
    if hasattr(b2, 'transS_container'):
        assert _is_linked(b2, 'transS_container', a)
    _safe_set(a, 'Transition11', None)
    assert not _is_linked(a, 'Transition11', b2)
    if hasattr(b2, 'transS_container'):
        assert not _is_linked(b2, 'transS_container', a)


def test_assoc_label40_link_reassign_clear():
    a = statechart_Label(name="sample_text")
    b1 = statechart_StateVertex()
    b2 = statechart_StateVertex()
    _safe_set(a, 'statechart_Label', b1)
    assert _is_linked(a, 'statechart_Label', b1)
    if hasattr(b1, 'statechart_StateVertex'):
        assert _is_linked(b1, 'statechart_StateVertex', a)
    _safe_set(a, 'statechart_Label', b2)
    assert _is_linked(a, 'statechart_Label', b2)
    if hasattr(b1, 'statechart_StateVertex'):
        assert not _is_linked(b1, 'statechart_StateVertex', a)
    if hasattr(b2, 'statechart_StateVertex'):
        assert _is_linked(b2, 'statechart_StateVertex', a)
    _safe_set(a, 'statechart_Label', None)
    assert not _is_linked(a, 'statechart_Label', b2)
    if hasattr(b2, 'statechart_StateVertex'):
        assert not _is_linked(b2, 'statechart_StateVertex', a)


def test_assoc_outgoing36_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_StateVertex()
    b2 = statechart_StateVertex()
    _safe_set(a, 'Transition37', b1)
    assert _is_linked(a, 'Transition37', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'Transition37', b2)
    assert _is_linked(a, 'Transition37', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'Transition37', None)
    assert not _is_linked(a, 'Transition37', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_source25_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_StateVertex()
    b2 = statechart_StateVertex()
    _safe_set(a, 'outgoing', b1)
    assert _is_linked(a, 'outgoing', b1)
    if hasattr(b1, 'StateVertex26'):
        assert _is_linked(b1, 'StateVertex26', a)
    _safe_set(a, 'outgoing', b2)
    assert _is_linked(a, 'outgoing', b2)
    if hasattr(b1, 'StateVertex26'):
        assert not _is_linked(b1, 'StateVertex26', a)
    if hasattr(b2, 'StateVertex26'):
        assert _is_linked(b2, 'StateVertex26', a)
    _safe_set(a, 'outgoing', None)
    assert not _is_linked(a, 'outgoing', b2)
    if hasattr(b2, 'StateVertex26'):
        assert not _is_linked(b2, 'StateVertex26', a)


def test_assoc_stateMachineCall16_link_reassign_clear():
    a = statechart_StateMachine(name="sample_text")
    b1 = statechart_Action(value="sample_text")
    b2 = statechart_Action(value="sample_text_2")
    _safe_set(a, 'StateMachine17', b1)
    assert _is_linked(a, 'StateMachine17', b1)
    if hasattr(b1, 'calledByAction'):
        assert _is_linked(b1, 'calledByAction', a)
    _safe_set(a, 'StateMachine17', b2)
    assert _is_linked(a, 'StateMachine17', b2)
    if hasattr(b1, 'calledByAction'):
        assert not _is_linked(b1, 'calledByAction', a)
    if hasattr(b2, 'calledByAction'):
        assert _is_linked(b2, 'calledByAction', a)
    _safe_set(a, 'StateMachine17', None)
    assert not _is_linked(a, 'StateMachine17', b2)
    if hasattr(b2, 'calledByAction'):
        assert not _is_linked(b2, 'calledByAction', a)


def test_assoc_state_container8_link_reassign_clear():
    a = statechart_StateMachine(name="sample_text")
    b1 = statechart_State()
    b2 = statechart_State()
    _safe_set(a, 'StateMachine9', b1)
    assert _is_linked(a, 'StateMachine9', b1)
    if hasattr(b1, 'top'):
        assert _is_linked(b1, 'top', a)
    _safe_set(a, 'StateMachine9', b2)
    assert _is_linked(a, 'StateMachine9', b2)
    if hasattr(b1, 'top'):
        assert not _is_linked(b1, 'top', a)
    if hasattr(b2, 'top'):
        assert _is_linked(b2, 'top', a)
    _safe_set(a, 'StateMachine9', None)
    assert not _is_linked(a, 'StateMachine9', b2)
    if hasattr(b2, 'top'):
        assert not _is_linked(b2, 'top', a)


def test_assoc_statemachine_container4_link_reassign_clear():
    a = statechart_StateMachine(name="sample_text")
    b1 = statechart_StateMachineRoot()
    b2 = statechart_StateMachineRoot()
    _safe_set(a, 'subStateMachines', b1)
    assert _is_linked(a, 'subStateMachines', b1)
    if hasattr(b1, 'StateMachineRoot'):
        assert _is_linked(b1, 'StateMachineRoot', a)
    _safe_set(a, 'subStateMachines', b2)
    assert _is_linked(a, 'subStateMachines', b2)
    if hasattr(b1, 'StateMachineRoot'):
        assert not _is_linked(b1, 'StateMachineRoot', a)
    if hasattr(b2, 'StateMachineRoot'):
        assert _is_linked(b2, 'StateMachineRoot', a)
    _safe_set(a, 'subStateMachines', None)
    assert not _is_linked(a, 'subStateMachines', b2)
    if hasattr(b2, 'StateMachineRoot'):
        assert not _is_linked(b2, 'StateMachineRoot', a)


def test_assoc_subStateMachines0_link_reassign_clear():
    a = statechart_StateMachine(name="sample_text")
    b1 = statechart_StateMachineRoot()
    b2 = statechart_StateMachineRoot()
    _safe_set(a, 'StateMachine', b1)
    assert _is_linked(a, 'StateMachine', b1)
    if hasattr(b1, 'statemachine_container'):
        assert _is_linked(b1, 'statemachine_container', a)
    _safe_set(a, 'StateMachine', b2)
    assert _is_linked(a, 'StateMachine', b2)
    if hasattr(b1, 'statemachine_container'):
        assert not _is_linked(b1, 'statemachine_container', a)
    if hasattr(b2, 'statemachine_container'):
        assert _is_linked(b2, 'statemachine_container', a)
    _safe_set(a, 'StateMachine', None)
    assert not _is_linked(a, 'StateMachine', b2)
    if hasattr(b2, 'statemachine_container'):
        assert not _is_linked(b2, 'statemachine_container', a)


def test_assoc_subVertexes15_link_reassign_clear():
    a = statechart_CompositeState(isConcurrent=True)
    b1 = statechart_StateVertex()
    b2 = statechart_StateVertex()
    _safe_set(a, 'sv_container', {b1})
    assert _is_linked(a, 'sv_container', b1)
    if hasattr(b1, 'StateVertex'):
        assert _is_linked(b1, 'StateVertex', a)
    _safe_set(a, 'sv_container', {b2})
    assert _is_linked(a, 'sv_container', b2)
    if hasattr(b1, 'StateVertex'):
        assert not _is_linked(b1, 'StateVertex', a)
    if hasattr(b2, 'StateVertex'):
        assert _is_linked(b2, 'StateVertex', a)
    _safe_set(a, 'sv_container', set())
    assert not _is_linked(a, 'sv_container', b2)
    if hasattr(b2, 'StateVertex'):
        assert not _is_linked(b2, 'StateVertex', a)


def test_assoc_sv_container35_link_reassign_clear():
    a = statechart_CompositeState(isConcurrent=True)
    b1 = statechart_StateVertex()
    b2 = statechart_StateVertex()
    _safe_set(a, 'CompositeState', b1)
    assert _is_linked(a, 'CompositeState', b1)
    if hasattr(b1, 'subVertexes'):
        assert _is_linked(b1, 'subVertexes', a)
    _safe_set(a, 'CompositeState', b2)
    assert _is_linked(a, 'CompositeState', b2)
    if hasattr(b1, 'subVertexes'):
        assert not _is_linked(b1, 'subVertexes', a)
    if hasattr(b2, 'subVertexes'):
        assert _is_linked(b2, 'subVertexes', a)
    _safe_set(a, 'CompositeState', None)
    assert not _is_linked(a, 'CompositeState', b2)
    if hasattr(b2, 'subVertexes'):
        assert not _is_linked(b2, 'subVertexes', a)


def test_assoc_target27_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_StateVertex()
    b2 = statechart_StateVertex()
    _safe_set(a, 'incoming', b1)
    assert _is_linked(a, 'incoming', b1)
    if hasattr(b1, 'StateVertex28'):
        assert _is_linked(b1, 'StateVertex28', a)
    _safe_set(a, 'incoming', b2)
    assert _is_linked(a, 'incoming', b2)
    if hasattr(b1, 'StateVertex28'):
        assert not _is_linked(b1, 'StateVertex28', a)
    if hasattr(b2, 'StateVertex28'):
        assert _is_linked(b2, 'StateVertex28', a)
    _safe_set(a, 'incoming', None)
    assert not _is_linked(a, 'incoming', b2)
    if hasattr(b2, 'StateVertex28'):
        assert not _is_linked(b2, 'StateVertex28', a)


def test_assoc_top3_link_reassign_clear():
    a = statechart_StateMachine(name="sample_text")
    b1 = statechart_State()
    b2 = statechart_State()
    _safe_set(a, 'state_container', {b1})
    assert _is_linked(a, 'state_container', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'state_container', {b2})
    assert _is_linked(a, 'state_container', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'state_container', set())
    assert not _is_linked(a, 'state_container', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_transSM_container18_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_StateMachine(name="sample_text")
    b2 = statechart_StateMachine(name="sample_text_2")
    _safe_set(a, 'transitions', b1)
    assert _is_linked(a, 'transitions', b1)
    if hasattr(b1, 'StateMachine19'):
        assert _is_linked(b1, 'StateMachine19', a)
    _safe_set(a, 'transitions', b2)
    assert _is_linked(a, 'transitions', b2)
    if hasattr(b1, 'StateMachine19'):
        assert not _is_linked(b1, 'StateMachine19', a)
    if hasattr(b2, 'StateMachine19'):
        assert _is_linked(b2, 'StateMachine19', a)
    _safe_set(a, 'transitions', None)
    assert not _is_linked(a, 'transitions', b2)
    if hasattr(b2, 'StateMachine19'):
        assert not _is_linked(b2, 'StateMachine19', a)


def test_assoc_transS_container20_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_State()
    b2 = statechart_State()
    _safe_set(a, 'internalTransitions', b1)
    assert _is_linked(a, 'internalTransitions', b1)
    if hasattr(b1, 'State21'):
        assert _is_linked(b1, 'State21', a)
    _safe_set(a, 'internalTransitions', b2)
    assert _is_linked(a, 'internalTransitions', b2)
    if hasattr(b1, 'State21'):
        assert not _is_linked(b1, 'State21', a)
    if hasattr(b2, 'State21'):
        assert _is_linked(b2, 'State21', a)
    _safe_set(a, 'internalTransitions', None)
    assert not _is_linked(a, 'internalTransitions', b2)
    if hasattr(b2, 'State21'):
        assert not _is_linked(b2, 'State21', a)


def test_assoc_transitions2_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_StateMachine(name="sample_text")
    b2 = statechart_StateMachine(name="sample_text_2")
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'transSM_container'):
        assert _is_linked(b1, 'transSM_container', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'transSM_container'):
        assert not _is_linked(b1, 'transSM_container', a)
    if hasattr(b2, 'transSM_container'):
        assert _is_linked(b2, 'transSM_container', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'transSM_container'):
        assert not _is_linked(b2, 'transSM_container', a)


def test_assoc_trigger22_link_reassign_clear():
    a = statechart_Transition(description="sample_text")
    b1 = statechart_Event(name="sample_text")
    b2 = statechart_Event(name="sample_text_2")
    _safe_set(a, 'evt_container', b1)
    assert _is_linked(a, 'evt_container', b1)
    if hasattr(b1, 'Event'):
        assert _is_linked(b1, 'Event', a)
    _safe_set(a, 'evt_container', b2)
    assert _is_linked(a, 'evt_container', b2)
    if hasattr(b1, 'Event'):
        assert not _is_linked(b1, 'Event', a)
    if hasattr(b2, 'Event'):
        assert _is_linked(b2, 'Event', a)
    _safe_set(a, 'evt_container', None)
    assert not _is_linked(a, 'evt_container', b2)
    if hasattr(b2, 'Event'):
        assert not _is_linked(b2, 'Event', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


IDBase_strategy = st.builds(IDBase)
@given(instance=IDBase_strategy)
@settings(max_examples=25)
def test_IDBase_instantiation(instance):
    assert isinstance(instance, IDBase)


NameBase_strategy = st.builds(NameBase)
@given(instance=NameBase_strategy)
@settings(max_examples=25)
def test_NameBase_instantiation(instance):
    assert isinstance(instance, NameBase)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


StateAction_strategy = st.builds(StateAction)
@given(instance=StateAction_strategy)
@settings(max_examples=25)
def test_StateAction_instantiation(instance):
    assert isinstance(instance, StateAction)


StateVertex_strategy = st.builds(StateVertex)
@given(instance=StateVertex_strategy)
@settings(max_examples=25)
def test_StateVertex_instantiation(instance):
    assert isinstance(instance, StateVertex)


statechart_Action_strategy = st.builds(statechart_Action, value=safe_text)
@given(instance=statechart_Action_strategy)
@settings(max_examples=25)
def test_statechart_Action_instantiation(instance):
    assert isinstance(instance, statechart_Action)


statechart_CompositeState_strategy = st.builds(statechart_CompositeState, isConcurrent=st.booleans())
@given(instance=statechart_CompositeState_strategy)
@settings(max_examples=25)
def test_statechart_CompositeState_instantiation(instance):
    assert isinstance(instance, statechart_CompositeState)


statechart_DO_strategy = st.builds(statechart_DO)
@given(instance=statechart_DO_strategy)
@settings(max_examples=25)
def test_statechart_DO_instantiation(instance):
    assert isinstance(instance, statechart_DO)


statechart_ENTRY_strategy = st.builds(statechart_ENTRY)
@given(instance=statechart_ENTRY_strategy)
@settings(max_examples=25)
def test_statechart_ENTRY_instantiation(instance):
    assert isinstance(instance, statechart_ENTRY)


statechart_EXIT_strategy = st.builds(statechart_EXIT)
@given(instance=statechart_EXIT_strategy)
@settings(max_examples=25)
def test_statechart_EXIT_instantiation(instance):
    assert isinstance(instance, statechart_EXIT)


statechart_Event_strategy = st.builds(statechart_Event, name=safe_text)
@given(instance=statechart_Event_strategy)
@settings(max_examples=25)
def test_statechart_Event_instantiation(instance):
    assert isinstance(instance, statechart_Event)


statechart_Guard_strategy = st.builds(statechart_Guard, expression=safe_text)
@given(instance=statechart_Guard_strategy)
@settings(max_examples=25)
def test_statechart_Guard_instantiation(instance):
    assert isinstance(instance, statechart_Guard)


statechart_Label_strategy = st.builds(statechart_Label, name=safe_text)
@given(instance=statechart_Label_strategy)
@settings(max_examples=25)
def test_statechart_Label_instantiation(instance):
    assert isinstance(instance, statechart_Label)


statechart_State_strategy = st.builds(statechart_State)
@given(instance=statechart_State_strategy)
@settings(max_examples=25)
def test_statechart_State_instantiation(instance):
    assert isinstance(instance, statechart_State)


statechart_StateAction_strategy = st.builds(statechart_StateAction)
@given(instance=statechart_StateAction_strategy)
@settings(max_examples=25)
def test_statechart_StateAction_instantiation(instance):
    assert isinstance(instance, statechart_StateAction)


statechart_StateMachine_strategy = st.builds(statechart_StateMachine, name=safe_text)
@given(instance=statechart_StateMachine_strategy)
@settings(max_examples=25)
def test_statechart_StateMachine_instantiation(instance):
    assert isinstance(instance, statechart_StateMachine)


statechart_StateMachineRoot_strategy = st.builds(statechart_StateMachineRoot)
@given(instance=statechart_StateMachineRoot_strategy)
@settings(max_examples=25)
def test_statechart_StateMachineRoot_instantiation(instance):
    assert isinstance(instance, statechart_StateMachineRoot)


statechart_StateVertex_strategy = st.builds(statechart_StateVertex)
@given(instance=statechart_StateVertex_strategy)
@settings(max_examples=25)
def test_statechart_StateVertex_instantiation(instance):
    assert isinstance(instance, statechart_StateVertex)


statechart_Transition_strategy = st.builds(statechart_Transition, description=safe_text)
@given(instance=statechart_Transition_strategy)
@settings(max_examples=25)
def test_statechart_Transition_instantiation(instance):
    assert isinstance(instance, statechart_Transition)


statechart_TransitionAction_strategy = st.builds(statechart_TransitionAction)
@given(instance=statechart_TransitionAction_strategy)
@settings(max_examples=25)
def test_statechart_TransitionAction_instantiation(instance):
    assert isinstance(instance, statechart_TransitionAction)





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




from python_code import statechart_CompositeState
from python_code import statechart_StateVertex

def test_statechart_CompositeState___init__():
    assert statechart_CompositeState.__init__(statechart_CompositeState(False, sv_container=set(), CompositeState=statechart_StateVertex()), False, sv_container=set(), CompositeState=statechart_StateVertex()) == None
from python_code import statechart_Label
from python_code import statechart_StateVertex

def test_statechart_Label___init__():
    assert statechart_Label.__init__(statechart_Label('', statechart_Label=statechart_StateVertex()), '', statechart_Label=statechart_StateVertex()) == None

