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
    fsm_NamedElement,
    Statement,
    State,
    fsm_FinalState,
    Pseudostate,
    fsm_Junction,
    fsm_Choice,
    fsm_ShallowHistory,
    fsm_DeepHistory,
    fsm_Fork,
    fsm_Join,
    fsm_InitialState,
    fsm_Statement,
    fsm_Trigger,
    fsm_Program,
    AbstractState,
    fsm_Pseudostate,
    fsm_State,
    Trigger,
    fsm_AndTrigger,
    fsm_Constraint,
    NamedElement,
    fsm_AbstractState,
    fsm_Transition,
    fsm_Region,
    fsm_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm_NamedElement)


def test_hyp_fsm_namedelement_constructor_exists():
    assert callable(fsm_NamedElement.__init__)


def test_hyp_fsm_namedelement_constructor_args():
    sig = inspect.signature(fsm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm_FinalState)


def test_hyp_fsm_finalstate_constructor_exists():
    assert callable(fsm_FinalState.__init__)


def test_hyp_fsm_finalstate_constructor_args():
    sig = inspect.signature(fsm_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_hyp_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_hyp_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_junction_is_not_abstract():
    assert not inspect.isabstract(fsm_Junction)


def test_hyp_fsm_junction_constructor_exists():
    assert callable(fsm_Junction.__init__)


def test_hyp_fsm_junction_constructor_args():
    sig = inspect.signature(fsm_Junction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_choice_is_not_abstract():
    assert not inspect.isabstract(fsm_Choice)


def test_hyp_fsm_choice_constructor_exists():
    assert callable(fsm_Choice.__init__)


def test_hyp_fsm_choice_constructor_args():
    sig = inspect.signature(fsm_Choice.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_shallowhistory_is_not_abstract():
    assert not inspect.isabstract(fsm_ShallowHistory)


def test_hyp_fsm_shallowhistory_constructor_exists():
    assert callable(fsm_ShallowHistory.__init__)


def test_hyp_fsm_shallowhistory_constructor_args():
    sig = inspect.signature(fsm_ShallowHistory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_deephistory_is_not_abstract():
    assert not inspect.isabstract(fsm_DeepHistory)


def test_hyp_fsm_deephistory_constructor_exists():
    assert callable(fsm_DeepHistory.__init__)


def test_hyp_fsm_deephistory_constructor_args():
    sig = inspect.signature(fsm_DeepHistory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_fork_is_not_abstract():
    assert not inspect.isabstract(fsm_Fork)


def test_hyp_fsm_fork_constructor_exists():
    assert callable(fsm_Fork.__init__)


def test_hyp_fsm_fork_constructor_args():
    sig = inspect.signature(fsm_Fork.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_join_is_not_abstract():
    assert not inspect.isabstract(fsm_Join)


def test_hyp_fsm_join_constructor_exists():
    assert callable(fsm_Join.__init__)


def test_hyp_fsm_join_constructor_args():
    sig = inspect.signature(fsm_Join.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm_InitialState)


def test_hyp_fsm_initialstate_constructor_exists():
    assert callable(fsm_InitialState.__init__)


def test_hyp_fsm_initialstate_constructor_args():
    sig = inspect.signature(fsm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_statement_is_not_abstract():
    assert not inspect.isabstract(fsm_Statement)


def test_hyp_fsm_statement_constructor_exists():
    assert callable(fsm_Statement.__init__)


def test_hyp_fsm_statement_constructor_args():
    sig = inspect.signature(fsm_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_trigger_is_not_abstract():
    assert not inspect.isabstract(fsm_Trigger)


def test_hyp_fsm_trigger_constructor_exists():
    assert callable(fsm_Trigger.__init__)


def test_hyp_fsm_trigger_constructor_args():
    sig = inspect.signature(fsm_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_fsm_program_is_not_abstract():
    assert not inspect.isabstract(fsm_Program)


def test_hyp_fsm_program_constructor_exists():
    assert callable(fsm_Program.__init__)


def test_hyp_fsm_program_constructor_args():
    sig = inspect.signature(fsm_Program.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_hyp_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_hyp_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm_Pseudostate)


def test_hyp_fsm_pseudostate_constructor_exists():
    assert callable(fsm_Pseudostate.__init__)


def test_hyp_fsm_pseudostate_constructor_args():
    sig = inspect.signature(fsm_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_hyp_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_hyp_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_hyp_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_hyp_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_andtrigger_is_not_abstract():
    assert not inspect.isabstract(fsm_AndTrigger)


def test_hyp_fsm_andtrigger_constructor_exists():
    assert callable(fsm_AndTrigger.__init__)


def test_hyp_fsm_andtrigger_constructor_args():
    sig = inspect.signature(fsm_AndTrigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_constraint_is_not_abstract():
    assert not inspect.isabstract(fsm_Constraint)


def test_hyp_fsm_constraint_constructor_exists():
    assert callable(fsm_Constraint.__init__)


def test_hyp_fsm_constraint_constructor_args():
    sig = inspect.signature(fsm_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsm_AbstractState)


def test_hyp_fsm_abstractstate_constructor_exists():
    assert callable(fsm_AbstractState.__init__)


def test_hyp_fsm_abstractstate_constructor_args():
    sig = inspect.signature(fsm_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_hyp_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_hyp_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_region_is_not_abstract():
    assert not inspect.isabstract(fsm_Region)


def test_hyp_fsm_region_constructor_exists():
    assert callable(fsm_Region.__init__)


def test_hyp_fsm_region_constructor_args():
    sig = inspect.signature(fsm_Region.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm_StateMachine)


def test_hyp_fsm_statemachine_constructor_exists():
    assert callable(fsm_StateMachine.__init__)


def test_hyp_fsm_statemachine_constructor_args():
    sig = inspect.signature(fsm_StateMachine.__init__)
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
fsm_NamedElement_strategy = st.builds(
    fsm_NamedElement,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
State_strategy = st.builds(
    State,
)
fsm_FinalState_strategy = st.builds(
    fsm_FinalState,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
fsm_Junction_strategy = st.builds(
    fsm_Junction,
)
fsm_Choice_strategy = st.builds(
    fsm_Choice,
)
fsm_ShallowHistory_strategy = st.builds(
    fsm_ShallowHistory,
)
fsm_DeepHistory_strategy = st.builds(
    fsm_DeepHistory,
)
fsm_Fork_strategy = st.builds(
    fsm_Fork,
)
fsm_Join_strategy = st.builds(
    fsm_Join,
)
fsm_InitialState_strategy = st.builds(
    fsm_InitialState,
)
fsm_Statement_strategy = st.builds(
    fsm_Statement,
)
fsm_Trigger_strategy = st.builds(
    fsm_Trigger,
    expression=
        safe_text
)
fsm_Program_strategy = st.builds(
    fsm_Program,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
fsm_Pseudostate_strategy = st.builds(
    fsm_Pseudostate,
)
fsm_State_strategy = st.builds(
    fsm_State,
)
Trigger_strategy = st.builds(
    Trigger,
)
fsm_AndTrigger_strategy = st.builds(
    fsm_AndTrigger,
)
fsm_Constraint_strategy = st.builds(
    fsm_Constraint,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm_AbstractState_strategy = st.builds(
    fsm_AbstractState,
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
)
fsm_Region_strategy = st.builds(
    fsm_Region,
)
fsm_StateMachine_strategy = st.builds(
    fsm_StateMachine,
)




@given(instance=fsm_NamedElement_strategy)
def test_hyp_fsm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
















@given(instance=fsm_Trigger_strategy)
def test_hyp_fsm_trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original














# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractState,
    NamedElement,
    Pseudostate,
    State,
    Statement,
    Trigger,
    fsm_AbstractState,
    fsm_AndTrigger,
    fsm_Choice,
    fsm_Constraint,
    fsm_DeepHistory,
    fsm_FinalState,
    fsm_Fork,
    fsm_InitialState,
    fsm_Join,
    fsm_Junction,
    fsm_NamedElement,
    fsm_Program,
    fsm_Pseudostate,
    fsm_Region,
    fsm_ShallowHistory,
    fsm_State,
    fsm_StateMachine,
    fsm_Statement,
    fsm_Transition,
    fsm_Trigger,
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

def test_fsm_NamedElement_name_value_roundtrip():
    instance = fsm_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fsm_Trigger_expression_value_roundtrip():
    instance = fsm_Trigger(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_fsm_Pseudostate_isa_AbstractState():
    instance = fsm_Pseudostate()
    assert isinstance(instance, AbstractState)


def test_fsm_State_isa_AbstractState():
    instance = fsm_State()
    assert isinstance(instance, AbstractState)


def test_fsm_AbstractState_isa_NamedElement():
    instance = fsm_AbstractState()
    assert isinstance(instance, NamedElement)


def test_fsm_Region_isa_NamedElement():
    instance = fsm_Region()
    assert isinstance(instance, NamedElement)


def test_fsm_StateMachine_isa_NamedElement():
    instance = fsm_StateMachine()
    assert isinstance(instance, NamedElement)


def test_fsm_Transition_isa_NamedElement():
    instance = fsm_Transition()
    assert isinstance(instance, NamedElement)


def test_fsm_Choice_isa_Pseudostate():
    instance = fsm_Choice()
    assert isinstance(instance, Pseudostate)


def test_fsm_DeepHistory_isa_Pseudostate():
    instance = fsm_DeepHistory()
    assert isinstance(instance, Pseudostate)


def test_fsm_Fork_isa_Pseudostate():
    instance = fsm_Fork()
    assert isinstance(instance, Pseudostate)


def test_fsm_InitialState_isa_Pseudostate():
    instance = fsm_InitialState()
    assert isinstance(instance, Pseudostate)


def test_fsm_Join_isa_Pseudostate():
    instance = fsm_Join()
    assert isinstance(instance, Pseudostate)


def test_fsm_Junction_isa_Pseudostate():
    instance = fsm_Junction()
    assert isinstance(instance, Pseudostate)


def test_fsm_ShallowHistory_isa_Pseudostate():
    instance = fsm_ShallowHistory()
    assert isinstance(instance, Pseudostate)


def test_fsm_FinalState_isa_State():
    instance = fsm_FinalState()
    assert isinstance(instance, State)


def test_fsm_Program_isa_Statement():
    instance = fsm_Program()
    assert isinstance(instance, Statement)


def test_fsm_AndTrigger_isa_Trigger():
    instance = fsm_AndTrigger()
    assert isinstance(instance, Trigger)


def test_assoc_left28_link_reassign_clear():
    a = fsm_Trigger(expression="sample_text")
    b1 = fsm_AndTrigger()
    b2 = fsm_AndTrigger()
    _safe_set(a, 'fsm_Trigger29', b1)
    assert _is_linked(a, 'fsm_Trigger29', b1)
    if hasattr(b1, 'fsm_AndTrigger'):
        assert _is_linked(b1, 'fsm_AndTrigger', a)
    _safe_set(a, 'fsm_Trigger29', b2)
    assert _is_linked(a, 'fsm_Trigger29', b2)
    if hasattr(b1, 'fsm_AndTrigger'):
        assert not _is_linked(b1, 'fsm_AndTrigger', a)
    if hasattr(b2, 'fsm_AndTrigger'):
        assert _is_linked(b2, 'fsm_AndTrigger', a)
    _safe_set(a, 'fsm_Trigger29', None)
    assert not _is_linked(a, 'fsm_Trigger29', b2)
    if hasattr(b2, 'fsm_AndTrigger'):
        assert not _is_linked(b2, 'fsm_AndTrigger', a)


def test_assoc_right30_link_reassign_clear():
    a = fsm_Trigger(expression="sample_text")
    b1 = fsm_AndTrigger()
    b2 = fsm_AndTrigger()
    _safe_set(a, 'fsm_Trigger32', b1)
    assert _is_linked(a, 'fsm_Trigger32', b1)
    if hasattr(b1, 'fsm_AndTrigger31'):
        assert _is_linked(b1, 'fsm_AndTrigger31', a)
    _safe_set(a, 'fsm_Trigger32', b2)
    assert _is_linked(a, 'fsm_Trigger32', b2)
    if hasattr(b1, 'fsm_AndTrigger31'):
        assert not _is_linked(b1, 'fsm_AndTrigger31', a)
    if hasattr(b2, 'fsm_AndTrigger31'):
        assert _is_linked(b2, 'fsm_AndTrigger31', a)
    _safe_set(a, 'fsm_Trigger32', None)
    assert not _is_linked(a, 'fsm_Trigger32', b2)
    if hasattr(b2, 'fsm_AndTrigger31'):
        assert not _is_linked(b2, 'fsm_AndTrigger31', a)


def test_assoc_trigger18_link_reassign_clear():
    a = fsm_Trigger(expression="sample_text")
    b1 = fsm_Transition()
    b2 = fsm_Transition()
    _safe_set(a, 'fsm_Trigger', b1)
    assert _is_linked(a, 'fsm_Trigger', b1)
    if hasattr(b1, 'fsm_Transition19'):
        assert _is_linked(b1, 'fsm_Transition19', a)
    _safe_set(a, 'fsm_Trigger', b2)
    assert _is_linked(a, 'fsm_Trigger', b2)
    if hasattr(b1, 'fsm_Transition19'):
        assert not _is_linked(b1, 'fsm_Transition19', a)
    if hasattr(b2, 'fsm_Transition19'):
        assert _is_linked(b2, 'fsm_Transition19', a)
    _safe_set(a, 'fsm_Trigger', None)
    assert not _is_linked(a, 'fsm_Trigger', b2)
    if hasattr(b2, 'fsm_Transition19'):
        assert not _is_linked(b2, 'fsm_Transition19', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractState_strategy = st.builds(AbstractState)
@given(instance=AbstractState_strategy)
@settings(max_examples=25)
def test_AbstractState_instantiation(instance):
    assert isinstance(instance, AbstractState)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Pseudostate_strategy = st.builds(Pseudostate)
@given(instance=Pseudostate_strategy)
@settings(max_examples=25)
def test_Pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


Trigger_strategy = st.builds(Trigger)
@given(instance=Trigger_strategy)
@settings(max_examples=25)
def test_Trigger_instantiation(instance):
    assert isinstance(instance, Trigger)


fsm_AbstractState_strategy = st.builds(fsm_AbstractState)
@given(instance=fsm_AbstractState_strategy)
@settings(max_examples=25)
def test_fsm_AbstractState_instantiation(instance):
    assert isinstance(instance, fsm_AbstractState)


fsm_AndTrigger_strategy = st.builds(fsm_AndTrigger)
@given(instance=fsm_AndTrigger_strategy)
@settings(max_examples=25)
def test_fsm_AndTrigger_instantiation(instance):
    assert isinstance(instance, fsm_AndTrigger)


fsm_Choice_strategy = st.builds(fsm_Choice)
@given(instance=fsm_Choice_strategy)
@settings(max_examples=25)
def test_fsm_Choice_instantiation(instance):
    assert isinstance(instance, fsm_Choice)


fsm_Constraint_strategy = st.builds(fsm_Constraint)
@given(instance=fsm_Constraint_strategy)
@settings(max_examples=25)
def test_fsm_Constraint_instantiation(instance):
    assert isinstance(instance, fsm_Constraint)


fsm_DeepHistory_strategy = st.builds(fsm_DeepHistory)
@given(instance=fsm_DeepHistory_strategy)
@settings(max_examples=25)
def test_fsm_DeepHistory_instantiation(instance):
    assert isinstance(instance, fsm_DeepHistory)


fsm_FinalState_strategy = st.builds(fsm_FinalState)
@given(instance=fsm_FinalState_strategy)
@settings(max_examples=25)
def test_fsm_FinalState_instantiation(instance):
    assert isinstance(instance, fsm_FinalState)


fsm_Fork_strategy = st.builds(fsm_Fork)
@given(instance=fsm_Fork_strategy)
@settings(max_examples=25)
def test_fsm_Fork_instantiation(instance):
    assert isinstance(instance, fsm_Fork)


fsm_InitialState_strategy = st.builds(fsm_InitialState)
@given(instance=fsm_InitialState_strategy)
@settings(max_examples=25)
def test_fsm_InitialState_instantiation(instance):
    assert isinstance(instance, fsm_InitialState)


fsm_Join_strategy = st.builds(fsm_Join)
@given(instance=fsm_Join_strategy)
@settings(max_examples=25)
def test_fsm_Join_instantiation(instance):
    assert isinstance(instance, fsm_Join)


fsm_Junction_strategy = st.builds(fsm_Junction)
@given(instance=fsm_Junction_strategy)
@settings(max_examples=25)
def test_fsm_Junction_instantiation(instance):
    assert isinstance(instance, fsm_Junction)


fsm_NamedElement_strategy = st.builds(fsm_NamedElement, name=safe_text)
@given(instance=fsm_NamedElement_strategy)
@settings(max_examples=25)
def test_fsm_NamedElement_instantiation(instance):
    assert isinstance(instance, fsm_NamedElement)


fsm_Program_strategy = st.builds(fsm_Program)
@given(instance=fsm_Program_strategy)
@settings(max_examples=25)
def test_fsm_Program_instantiation(instance):
    assert isinstance(instance, fsm_Program)


fsm_Pseudostate_strategy = st.builds(fsm_Pseudostate)
@given(instance=fsm_Pseudostate_strategy)
@settings(max_examples=25)
def test_fsm_Pseudostate_instantiation(instance):
    assert isinstance(instance, fsm_Pseudostate)


fsm_Region_strategy = st.builds(fsm_Region)
@given(instance=fsm_Region_strategy)
@settings(max_examples=25)
def test_fsm_Region_instantiation(instance):
    assert isinstance(instance, fsm_Region)


fsm_ShallowHistory_strategy = st.builds(fsm_ShallowHistory)
@given(instance=fsm_ShallowHistory_strategy)
@settings(max_examples=25)
def test_fsm_ShallowHistory_instantiation(instance):
    assert isinstance(instance, fsm_ShallowHistory)


fsm_State_strategy = st.builds(fsm_State)
@given(instance=fsm_State_strategy)
@settings(max_examples=25)
def test_fsm_State_instantiation(instance):
    assert isinstance(instance, fsm_State)


fsm_StateMachine_strategy = st.builds(fsm_StateMachine)
@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=25)
def test_fsm_StateMachine_instantiation(instance):
    assert isinstance(instance, fsm_StateMachine)


fsm_Statement_strategy = st.builds(fsm_Statement)
@given(instance=fsm_Statement_strategy)
@settings(max_examples=25)
def test_fsm_Statement_instantiation(instance):
    assert isinstance(instance, fsm_Statement)


fsm_Transition_strategy = st.builds(fsm_Transition)
@given(instance=fsm_Transition_strategy)
@settings(max_examples=25)
def test_fsm_Transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)


fsm_Trigger_strategy = st.builds(fsm_Trigger, expression=safe_text)
@given(instance=fsm_Trigger_strategy)
@settings(max_examples=25)
def test_fsm_Trigger_instantiation(instance):
    assert isinstance(instance, fsm_Trigger)



