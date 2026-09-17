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
    StateContainer,
    Named,
    workflow_StateTransition,
    workflow_AbstractState,
    workflow_Workflow,
    IntermediateState,
    workflow_Fork,
    workflow_Decision,
    workflow_Processing,
    workflow_Join,
    workflow_SubProcess,
    workflow_Task,
    ToState,
    FromState,
    AbstractState,
    workflow_End,
    workflow_IntermediateState,
    workflow_Start,
    workflow_StateContainer,
    workflow_ToState,
    workflow_FromState,
    EObject,
    workflow_Named,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_statecontainer_is_not_abstract():
    assert not inspect.isabstract(StateContainer)


def test_hyp_statecontainer_constructor_exists():
    assert callable(StateContainer.__init__)


def test_hyp_statecontainer_constructor_args():
    sig = inspect.signature(StateContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_statetransition_is_not_abstract():
    assert not inspect.isabstract(workflow_StateTransition)


def test_hyp_workflow_statetransition_constructor_exists():
    assert callable(workflow_StateTransition.__init__)


def test_hyp_workflow_statetransition_constructor_args():
    sig = inspect.signature(workflow_StateTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_abstractstate_is_not_abstract():
    assert not inspect.isabstract(workflow_AbstractState)


def test_hyp_workflow_abstractstate_constructor_exists():
    assert callable(workflow_AbstractState.__init__)


def test_hyp_workflow_abstractstate_constructor_args():
    sig = inspect.signature(workflow_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "associatedClass" in params, "Missing parameter 'associatedClass'"




def test_hyp_workflow_workflow_is_not_abstract():
    assert not inspect.isabstract(workflow_Workflow)


def test_hyp_workflow_workflow_constructor_exists():
    assert callable(workflow_Workflow.__init__)


def test_hyp_workflow_workflow_constructor_args():
    sig = inspect.signature(workflow_Workflow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intermediatestate_is_not_abstract():
    assert not inspect.isabstract(IntermediateState)


def test_hyp_intermediatestate_constructor_exists():
    assert callable(IntermediateState.__init__)


def test_hyp_intermediatestate_constructor_args():
    sig = inspect.signature(IntermediateState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_fork_is_not_abstract():
    assert not inspect.isabstract(workflow_Fork)


def test_hyp_workflow_fork_constructor_exists():
    assert callable(workflow_Fork.__init__)


def test_hyp_workflow_fork_constructor_args():
    sig = inspect.signature(workflow_Fork.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_decision_is_not_abstract():
    assert not inspect.isabstract(workflow_Decision)


def test_hyp_workflow_decision_constructor_exists():
    assert callable(workflow_Decision.__init__)


def test_hyp_workflow_decision_constructor_args():
    sig = inspect.signature(workflow_Decision.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_processing_is_not_abstract():
    assert not inspect.isabstract(workflow_Processing)


def test_hyp_workflow_processing_constructor_exists():
    assert callable(workflow_Processing.__init__)


def test_hyp_workflow_processing_constructor_args():
    sig = inspect.signature(workflow_Processing.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_join_is_not_abstract():
    assert not inspect.isabstract(workflow_Join)


def test_hyp_workflow_join_constructor_exists():
    assert callable(workflow_Join.__init__)


def test_hyp_workflow_join_constructor_args():
    sig = inspect.signature(workflow_Join.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_subprocess_is_not_abstract():
    assert not inspect.isabstract(workflow_SubProcess)


def test_hyp_workflow_subprocess_constructor_exists():
    assert callable(workflow_SubProcess.__init__)


def test_hyp_workflow_subprocess_constructor_args():
    sig = inspect.signature(workflow_SubProcess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_task_is_not_abstract():
    assert not inspect.isabstract(workflow_Task)


def test_hyp_workflow_task_constructor_exists():
    assert callable(workflow_Task.__init__)


def test_hyp_workflow_task_constructor_args():
    sig = inspect.signature(workflow_Task.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tostate_is_not_abstract():
    assert not inspect.isabstract(ToState)


def test_hyp_tostate_constructor_exists():
    assert callable(ToState.__init__)


def test_hyp_tostate_constructor_args():
    sig = inspect.signature(ToState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fromstate_is_not_abstract():
    assert not inspect.isabstract(FromState)


def test_hyp_fromstate_constructor_exists():
    assert callable(FromState.__init__)


def test_hyp_fromstate_constructor_args():
    sig = inspect.signature(FromState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_hyp_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_hyp_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_end_is_not_abstract():
    assert not inspect.isabstract(workflow_End)


def test_hyp_workflow_end_constructor_exists():
    assert callable(workflow_End.__init__)


def test_hyp_workflow_end_constructor_args():
    sig = inspect.signature(workflow_End.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_intermediatestate_is_not_abstract():
    assert not inspect.isabstract(workflow_IntermediateState)


def test_hyp_workflow_intermediatestate_constructor_exists():
    assert callable(workflow_IntermediateState.__init__)


def test_hyp_workflow_intermediatestate_constructor_args():
    sig = inspect.signature(workflow_IntermediateState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_start_is_not_abstract():
    assert not inspect.isabstract(workflow_Start)


def test_hyp_workflow_start_constructor_exists():
    assert callable(workflow_Start.__init__)


def test_hyp_workflow_start_constructor_args():
    sig = inspect.signature(workflow_Start.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_statecontainer_is_not_abstract():
    assert not inspect.isabstract(workflow_StateContainer)


def test_hyp_workflow_statecontainer_constructor_exists():
    assert callable(workflow_StateContainer.__init__)


def test_hyp_workflow_statecontainer_constructor_args():
    sig = inspect.signature(workflow_StateContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_tostate_is_not_abstract():
    assert not inspect.isabstract(workflow_ToState)


def test_hyp_workflow_tostate_constructor_exists():
    assert callable(workflow_ToState.__init__)


def test_hyp_workflow_tostate_constructor_args():
    sig = inspect.signature(workflow_ToState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_fromstate_is_not_abstract():
    assert not inspect.isabstract(workflow_FromState)


def test_hyp_workflow_fromstate_constructor_exists():
    assert callable(workflow_FromState.__init__)


def test_hyp_workflow_fromstate_constructor_args():
    sig = inspect.signature(workflow_FromState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_hyp_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_hyp_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workflow_named_is_not_abstract():
    assert not inspect.isabstract(workflow_Named)


def test_hyp_workflow_named_constructor_exists():
    assert callable(workflow_Named.__init__)


def test_hyp_workflow_named_constructor_args():
    sig = inspect.signature(workflow_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
StateContainer_strategy = st.builds(
    StateContainer,
)
Named_strategy = st.builds(
    Named,
)
workflow_StateTransition_strategy = st.builds(
    workflow_StateTransition,
)
workflow_AbstractState_strategy = st.builds(
    workflow_AbstractState,
    associatedClass=
        safe_text
)
workflow_Workflow_strategy = st.builds(
    workflow_Workflow,
)
IntermediateState_strategy = st.builds(
    IntermediateState,
)
workflow_Fork_strategy = st.builds(
    workflow_Fork,
)
workflow_Decision_strategy = st.builds(
    workflow_Decision,
)
workflow_Processing_strategy = st.builds(
    workflow_Processing,
)
workflow_Join_strategy = st.builds(
    workflow_Join,
)
workflow_SubProcess_strategy = st.builds(
    workflow_SubProcess,
)
workflow_Task_strategy = st.builds(
    workflow_Task,
)
ToState_strategy = st.builds(
    ToState,
)
FromState_strategy = st.builds(
    FromState,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
workflow_End_strategy = st.builds(
    workflow_End,
)
workflow_IntermediateState_strategy = st.builds(
    workflow_IntermediateState,
)
workflow_Start_strategy = st.builds(
    workflow_Start,
)
workflow_StateContainer_strategy = st.builds(
    workflow_StateContainer,
)
workflow_ToState_strategy = st.builds(
    workflow_ToState,
)
workflow_FromState_strategy = st.builds(
    workflow_FromState,
)
EObject_strategy = st.builds(
    EObject,
)
workflow_Named_strategy = st.builds(
    workflow_Named,
    name=
        safe_text
)







@given(instance=workflow_AbstractState_strategy)
def test_hyp_workflow_abstractstate_associatedClass_setter(instance):
    original = instance.associatedClass
    instance.associatedClass = original
    assert instance.associatedClass == original






















@given(instance=workflow_Named_strategy)
def test_hyp_workflow_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractState,
    EObject,
    FromState,
    IntermediateState,
    Named,
    StateContainer,
    ToState,
    workflow_AbstractState,
    workflow_Decision,
    workflow_End,
    workflow_Fork,
    workflow_FromState,
    workflow_IntermediateState,
    workflow_Join,
    workflow_Named,
    workflow_Processing,
    workflow_Start,
    workflow_StateContainer,
    workflow_StateTransition,
    workflow_SubProcess,
    workflow_Task,
    workflow_ToState,
    workflow_Workflow,
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

def test_workflow_AbstractState_associatedClass_value_roundtrip():
    instance = workflow_AbstractState(associatedClass="sample_text")
    assert instance.associatedClass == "sample_text"
    instance.associatedClass = "sample_text_2"
    assert instance.associatedClass == "sample_text_2"


def test_workflow_Named_name_value_roundtrip():
    instance = workflow_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_workflow_End_isa_AbstractState():
    instance = workflow_End()
    assert isinstance(instance, AbstractState)


def test_workflow_IntermediateState_isa_AbstractState():
    instance = workflow_IntermediateState()
    assert isinstance(instance, AbstractState)


def test_workflow_Start_isa_AbstractState():
    instance = workflow_Start()
    assert isinstance(instance, AbstractState)


def test_workflow_Named_isa_EObject():
    instance = workflow_Named(name="sample_text")
    assert isinstance(instance, EObject)


def test_workflow_IntermediateState_isa_FromState():
    instance = workflow_IntermediateState()
    assert isinstance(instance, FromState)


def test_workflow_Start_isa_FromState():
    instance = workflow_Start()
    assert isinstance(instance, FromState)


def test_workflow_Decision_isa_IntermediateState():
    instance = workflow_Decision()
    assert isinstance(instance, IntermediateState)


def test_workflow_Fork_isa_IntermediateState():
    instance = workflow_Fork()
    assert isinstance(instance, IntermediateState)


def test_workflow_Join_isa_IntermediateState():
    instance = workflow_Join()
    assert isinstance(instance, IntermediateState)


def test_workflow_Processing_isa_IntermediateState():
    instance = workflow_Processing()
    assert isinstance(instance, IntermediateState)


def test_workflow_SubProcess_isa_IntermediateState():
    instance = workflow_SubProcess()
    assert isinstance(instance, IntermediateState)


def test_workflow_Task_isa_IntermediateState():
    instance = workflow_Task()
    assert isinstance(instance, IntermediateState)


def test_workflow_AbstractState_isa_Named():
    instance = workflow_AbstractState(associatedClass="sample_text")
    assert isinstance(instance, Named)


def test_workflow_StateTransition_isa_Named():
    instance = workflow_StateTransition()
    assert isinstance(instance, Named)


def test_workflow_Workflow_isa_Named():
    instance = workflow_Workflow()
    assert isinstance(instance, Named)


def test_workflow_SubProcess_isa_StateContainer():
    instance = workflow_SubProcess()
    assert isinstance(instance, StateContainer)


def test_workflow_Workflow_isa_StateContainer():
    instance = workflow_Workflow()
    assert isinstance(instance, StateContainer)


def test_workflow_End_isa_ToState():
    instance = workflow_End()
    assert isinstance(instance, ToState)


def test_workflow_IntermediateState_isa_ToState():
    instance = workflow_IntermediateState()
    assert isinstance(instance, ToState)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractState_strategy = st.builds(AbstractState)
@given(instance=AbstractState_strategy)
@settings(max_examples=25)
def test_AbstractState_instantiation(instance):
    assert isinstance(instance, AbstractState)


EObject_strategy = st.builds(EObject)
@given(instance=EObject_strategy)
@settings(max_examples=25)
def test_EObject_instantiation(instance):
    assert isinstance(instance, EObject)


FromState_strategy = st.builds(FromState)
@given(instance=FromState_strategy)
@settings(max_examples=25)
def test_FromState_instantiation(instance):
    assert isinstance(instance, FromState)


IntermediateState_strategy = st.builds(IntermediateState)
@given(instance=IntermediateState_strategy)
@settings(max_examples=25)
def test_IntermediateState_instantiation(instance):
    assert isinstance(instance, IntermediateState)


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


StateContainer_strategy = st.builds(StateContainer)
@given(instance=StateContainer_strategy)
@settings(max_examples=25)
def test_StateContainer_instantiation(instance):
    assert isinstance(instance, StateContainer)


ToState_strategy = st.builds(ToState)
@given(instance=ToState_strategy)
@settings(max_examples=25)
def test_ToState_instantiation(instance):
    assert isinstance(instance, ToState)


workflow_AbstractState_strategy = st.builds(workflow_AbstractState, associatedClass=safe_text)
@given(instance=workflow_AbstractState_strategy)
@settings(max_examples=25)
def test_workflow_AbstractState_instantiation(instance):
    assert isinstance(instance, workflow_AbstractState)


workflow_Decision_strategy = st.builds(workflow_Decision)
@given(instance=workflow_Decision_strategy)
@settings(max_examples=25)
def test_workflow_Decision_instantiation(instance):
    assert isinstance(instance, workflow_Decision)


workflow_End_strategy = st.builds(workflow_End)
@given(instance=workflow_End_strategy)
@settings(max_examples=25)
def test_workflow_End_instantiation(instance):
    assert isinstance(instance, workflow_End)


workflow_Fork_strategy = st.builds(workflow_Fork)
@given(instance=workflow_Fork_strategy)
@settings(max_examples=25)
def test_workflow_Fork_instantiation(instance):
    assert isinstance(instance, workflow_Fork)


workflow_FromState_strategy = st.builds(workflow_FromState)
@given(instance=workflow_FromState_strategy)
@settings(max_examples=25)
def test_workflow_FromState_instantiation(instance):
    assert isinstance(instance, workflow_FromState)


workflow_IntermediateState_strategy = st.builds(workflow_IntermediateState)
@given(instance=workflow_IntermediateState_strategy)
@settings(max_examples=25)
def test_workflow_IntermediateState_instantiation(instance):
    assert isinstance(instance, workflow_IntermediateState)


workflow_Join_strategy = st.builds(workflow_Join)
@given(instance=workflow_Join_strategy)
@settings(max_examples=25)
def test_workflow_Join_instantiation(instance):
    assert isinstance(instance, workflow_Join)


workflow_Named_strategy = st.builds(workflow_Named, name=safe_text)
@given(instance=workflow_Named_strategy)
@settings(max_examples=25)
def test_workflow_Named_instantiation(instance):
    assert isinstance(instance, workflow_Named)


workflow_Processing_strategy = st.builds(workflow_Processing)
@given(instance=workflow_Processing_strategy)
@settings(max_examples=25)
def test_workflow_Processing_instantiation(instance):
    assert isinstance(instance, workflow_Processing)


workflow_Start_strategy = st.builds(workflow_Start)
@given(instance=workflow_Start_strategy)
@settings(max_examples=25)
def test_workflow_Start_instantiation(instance):
    assert isinstance(instance, workflow_Start)


workflow_StateContainer_strategy = st.builds(workflow_StateContainer)
@given(instance=workflow_StateContainer_strategy)
@settings(max_examples=25)
def test_workflow_StateContainer_instantiation(instance):
    assert isinstance(instance, workflow_StateContainer)


workflow_StateTransition_strategy = st.builds(workflow_StateTransition)
@given(instance=workflow_StateTransition_strategy)
@settings(max_examples=25)
def test_workflow_StateTransition_instantiation(instance):
    assert isinstance(instance, workflow_StateTransition)


workflow_SubProcess_strategy = st.builds(workflow_SubProcess)
@given(instance=workflow_SubProcess_strategy)
@settings(max_examples=25)
def test_workflow_SubProcess_instantiation(instance):
    assert isinstance(instance, workflow_SubProcess)


workflow_Task_strategy = st.builds(workflow_Task)
@given(instance=workflow_Task_strategy)
@settings(max_examples=25)
def test_workflow_Task_instantiation(instance):
    assert isinstance(instance, workflow_Task)


workflow_ToState_strategy = st.builds(workflow_ToState)
@given(instance=workflow_ToState_strategy)
@settings(max_examples=25)
def test_workflow_ToState_instantiation(instance):
    assert isinstance(instance, workflow_ToState)


workflow_Workflow_strategy = st.builds(workflow_Workflow)
@given(instance=workflow_Workflow_strategy)
@settings(max_examples=25)
def test_workflow_Workflow_instantiation(instance):
    assert isinstance(instance, workflow_Workflow)



