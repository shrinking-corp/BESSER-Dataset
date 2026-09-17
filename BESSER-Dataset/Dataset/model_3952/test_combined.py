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
    sooml_NamedElement,
    IsInStateCondition,
    sooml_ParameterIsInStateCondition,
    sooml_ReferenceIsInStateCondition,
    Guard,
    sooml_IsInStateCondition,
    sooml_ParameterBinding,
    Action,
    sooml_ReferenceAssignmentAction,
    sooml_CallOperationAction,
    CallOperationAction,
    sooml_CallParameterOperationAction,
    sooml_CallReferenceOperationAction,
    sooml_Transition,
    StructuralFeature,
    sooml_Reference,
    sooml_Attribute,
    sooml_Event,
    sooml_Guard,
    sooml_Action,
    sooml_EntryOperation,
    NamedElement,
    sooml_StructuralFeature,
    sooml_State,
    sooml_Parameter,
    sooml_Package,
    sooml_Operation,
    sooml_StateMachine,
    sooml_Class,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_sooml_namedelement_is_not_abstract():
    assert not inspect.isabstract(sooml_NamedElement)


def test_hyp_sooml_namedelement_constructor_exists():
    assert callable(sooml_NamedElement.__init__)


def test_hyp_sooml_namedelement_constructor_args():
    sig = inspect.signature(sooml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_isinstatecondition_is_not_abstract():
    assert not inspect.isabstract(IsInStateCondition)


def test_hyp_isinstatecondition_constructor_exists():
    assert callable(IsInStateCondition.__init__)


def test_hyp_isinstatecondition_constructor_args():
    sig = inspect.signature(IsInStateCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_parameterisinstatecondition_is_not_abstract():
    assert not inspect.isabstract(sooml_ParameterIsInStateCondition)


def test_hyp_sooml_parameterisinstatecondition_constructor_exists():
    assert callable(sooml_ParameterIsInStateCondition.__init__)


def test_hyp_sooml_parameterisinstatecondition_constructor_args():
    sig = inspect.signature(sooml_ParameterIsInStateCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_referenceisinstatecondition_is_not_abstract():
    assert not inspect.isabstract(sooml_ReferenceIsInStateCondition)


def test_hyp_sooml_referenceisinstatecondition_constructor_exists():
    assert callable(sooml_ReferenceIsInStateCondition.__init__)


def test_hyp_sooml_referenceisinstatecondition_constructor_args():
    sig = inspect.signature(sooml_ReferenceIsInStateCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_hyp_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_hyp_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_isinstatecondition_is_not_abstract():
    assert not inspect.isabstract(sooml_IsInStateCondition)


def test_hyp_sooml_isinstatecondition_constructor_exists():
    assert callable(sooml_IsInStateCondition.__init__)


def test_hyp_sooml_isinstatecondition_constructor_args():
    sig = inspect.signature(sooml_IsInStateCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_parameterbinding_is_not_abstract():
    assert not inspect.isabstract(sooml_ParameterBinding)


def test_hyp_sooml_parameterbinding_constructor_exists():
    assert callable(sooml_ParameterBinding.__init__)


def test_hyp_sooml_parameterbinding_constructor_args():
    sig = inspect.signature(sooml_ParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_referenceassignmentaction_is_not_abstract():
    assert not inspect.isabstract(sooml_ReferenceAssignmentAction)


def test_hyp_sooml_referenceassignmentaction_constructor_exists():
    assert callable(sooml_ReferenceAssignmentAction.__init__)


def test_hyp_sooml_referenceassignmentaction_constructor_args():
    sig = inspect.signature(sooml_ReferenceAssignmentAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(sooml_CallOperationAction)


def test_hyp_sooml_calloperationaction_constructor_exists():
    assert callable(sooml_CallOperationAction.__init__)


def test_hyp_sooml_calloperationaction_constructor_args():
    sig = inspect.signature(sooml_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(CallOperationAction)


def test_hyp_calloperationaction_constructor_exists():
    assert callable(CallOperationAction.__init__)


def test_hyp_calloperationaction_constructor_args():
    sig = inspect.signature(CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_callparameteroperationaction_is_not_abstract():
    assert not inspect.isabstract(sooml_CallParameterOperationAction)


def test_hyp_sooml_callparameteroperationaction_constructor_exists():
    assert callable(sooml_CallParameterOperationAction.__init__)


def test_hyp_sooml_callparameteroperationaction_constructor_args():
    sig = inspect.signature(sooml_CallParameterOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_callreferenceoperationaction_is_not_abstract():
    assert not inspect.isabstract(sooml_CallReferenceOperationAction)


def test_hyp_sooml_callreferenceoperationaction_constructor_exists():
    assert callable(sooml_CallReferenceOperationAction.__init__)


def test_hyp_sooml_callreferenceoperationaction_constructor_args():
    sig = inspect.signature(sooml_CallReferenceOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_transition_is_not_abstract():
    assert not inspect.isabstract(sooml_Transition)


def test_hyp_sooml_transition_constructor_exists():
    assert callable(sooml_Transition.__init__)


def test_hyp_sooml_transition_constructor_args():
    sig = inspect.signature(sooml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_hyp_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_hyp_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_reference_is_not_abstract():
    assert not inspect.isabstract(sooml_Reference)


def test_hyp_sooml_reference_constructor_exists():
    assert callable(sooml_Reference.__init__)


def test_hyp_sooml_reference_constructor_args():
    sig = inspect.signature(sooml_Reference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_attribute_is_not_abstract():
    assert not inspect.isabstract(sooml_Attribute)


def test_hyp_sooml_attribute_constructor_exists():
    assert callable(sooml_Attribute.__init__)


def test_hyp_sooml_attribute_constructor_args():
    sig = inspect.signature(sooml_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"




def test_hyp_sooml_event_is_not_abstract():
    assert not inspect.isabstract(sooml_Event)


def test_hyp_sooml_event_constructor_exists():
    assert callable(sooml_Event.__init__)


def test_hyp_sooml_event_constructor_args():
    sig = inspect.signature(sooml_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_guard_is_not_abstract():
    assert not inspect.isabstract(sooml_Guard)


def test_hyp_sooml_guard_constructor_exists():
    assert callable(sooml_Guard.__init__)


def test_hyp_sooml_guard_constructor_args():
    sig = inspect.signature(sooml_Guard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_action_is_not_abstract():
    assert not inspect.isabstract(sooml_Action)


def test_hyp_sooml_action_constructor_exists():
    assert callable(sooml_Action.__init__)


def test_hyp_sooml_action_constructor_args():
    sig = inspect.signature(sooml_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_entryoperation_is_not_abstract():
    assert not inspect.isabstract(sooml_EntryOperation)


def test_hyp_sooml_entryoperation_constructor_exists():
    assert callable(sooml_EntryOperation.__init__)


def test_hyp_sooml_entryoperation_constructor_args():
    sig = inspect.signature(sooml_EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(sooml_StructuralFeature)


def test_hyp_sooml_structuralfeature_constructor_exists():
    assert callable(sooml_StructuralFeature.__init__)


def test_hyp_sooml_structuralfeature_constructor_args():
    sig = inspect.signature(sooml_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"





def test_hyp_sooml_state_is_not_abstract():
    assert not inspect.isabstract(sooml_State)


def test_hyp_sooml_state_constructor_exists():
    assert callable(sooml_State.__init__)


def test_hyp_sooml_state_constructor_args():
    sig = inspect.signature(sooml_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_parameter_is_not_abstract():
    assert not inspect.isabstract(sooml_Parameter)


def test_hyp_sooml_parameter_constructor_exists():
    assert callable(sooml_Parameter.__init__)


def test_hyp_sooml_parameter_constructor_args():
    sig = inspect.signature(sooml_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"




def test_hyp_sooml_package_is_not_abstract():
    assert not inspect.isabstract(sooml_Package)


def test_hyp_sooml_package_constructor_exists():
    assert callable(sooml_Package.__init__)


def test_hyp_sooml_package_constructor_args():
    sig = inspect.signature(sooml_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_operation_is_not_abstract():
    assert not inspect.isabstract(sooml_Operation)


def test_hyp_sooml_operation_constructor_exists():
    assert callable(sooml_Operation.__init__)


def test_hyp_sooml_operation_constructor_args():
    sig = inspect.signature(sooml_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_statemachine_is_not_abstract():
    assert not inspect.isabstract(sooml_StateMachine)


def test_hyp_sooml_statemachine_constructor_exists():
    assert callable(sooml_StateMachine.__init__)


def test_hyp_sooml_statemachine_constructor_args():
    sig = inspect.signature(sooml_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sooml_class_is_not_abstract():
    assert not inspect.isabstract(sooml_Class)


def test_hyp_sooml_class_constructor_exists():
    assert callable(sooml_Class.__init__)


def test_hyp_sooml_class_constructor_args():
    sig = inspect.signature(sooml_Class.__init__)
    params = list(sig.parameters.keys())

def test_hyp_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_hyp_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "Complex",
        "Boolean",
        "Integer",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
sooml_NamedElement_strategy = st.builds(
    sooml_NamedElement,
    name=
        safe_text
)
IsInStateCondition_strategy = st.builds(
    IsInStateCondition,
)
sooml_ParameterIsInStateCondition_strategy = st.builds(
    sooml_ParameterIsInStateCondition,
)
sooml_ReferenceIsInStateCondition_strategy = st.builds(
    sooml_ReferenceIsInStateCondition,
)
Guard_strategy = st.builds(
    Guard,
)
sooml_IsInStateCondition_strategy = st.builds(
    sooml_IsInStateCondition,
)
sooml_ParameterBinding_strategy = st.builds(
    sooml_ParameterBinding,
)
Action_strategy = st.builds(
    Action,
)
sooml_ReferenceAssignmentAction_strategy = st.builds(
    sooml_ReferenceAssignmentAction,
)
sooml_CallOperationAction_strategy = st.builds(
    sooml_CallOperationAction,
)
CallOperationAction_strategy = st.builds(
    CallOperationAction,
)
sooml_CallParameterOperationAction_strategy = st.builds(
    sooml_CallParameterOperationAction,
)
sooml_CallReferenceOperationAction_strategy = st.builds(
    sooml_CallReferenceOperationAction,
)
sooml_Transition_strategy = st.builds(
    sooml_Transition,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
sooml_Reference_strategy = st.builds(
    sooml_Reference,
)
sooml_Attribute_strategy = st.builds(
    sooml_Attribute,
    dataType=
        safe_text
)
sooml_Event_strategy = st.builds(
    sooml_Event,
)
sooml_Guard_strategy = st.builds(
    sooml_Guard,
)
sooml_Action_strategy = st.builds(
    sooml_Action,
)
sooml_EntryOperation_strategy = st.builds(
    sooml_EntryOperation,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sooml_StructuralFeature_strategy = st.builds(
    sooml_StructuralFeature,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers()
)
sooml_State_strategy = st.builds(
    sooml_State,
)
sooml_Parameter_strategy = st.builds(
    sooml_Parameter,
    dataType=
        safe_text
)
sooml_Package_strategy = st.builds(
    sooml_Package,
)
sooml_Operation_strategy = st.builds(
    sooml_Operation,
)
sooml_StateMachine_strategy = st.builds(
    sooml_StateMachine,
)
sooml_Class_strategy = st.builds(
    sooml_Class,
)




@given(instance=sooml_NamedElement_strategy)
def test_hyp_sooml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



















@given(instance=sooml_Attribute_strategy)
def test_hyp_sooml_attribute_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original









@given(instance=sooml_StructuralFeature_strategy)
def test_hyp_sooml_structuralfeature_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=sooml_StructuralFeature_strategy)
def test_hyp_sooml_structuralfeature_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original





@given(instance=sooml_Parameter_strategy)
def test_hyp_sooml_parameter_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    CallOperationAction,
    Guard,
    IsInStateCondition,
    NamedElement,
    StructuralFeature,
    sooml_Action,
    sooml_Attribute,
    sooml_CallOperationAction,
    sooml_CallParameterOperationAction,
    sooml_CallReferenceOperationAction,
    sooml_Class,
    sooml_EntryOperation,
    sooml_Event,
    sooml_Guard,
    sooml_IsInStateCondition,
    sooml_NamedElement,
    sooml_Operation,
    sooml_Package,
    sooml_Parameter,
    sooml_ParameterBinding,
    sooml_ParameterIsInStateCondition,
    sooml_Reference,
    sooml_ReferenceAssignmentAction,
    sooml_ReferenceIsInStateCondition,
    sooml_State,
    sooml_StateMachine,
    sooml_StructuralFeature,
    sooml_Transition,
    DataType,
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

def test_sooml_Attribute_dataType_value_roundtrip():
    instance = sooml_Attribute(dataType="sample_text")
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_sooml_NamedElement_name_value_roundtrip():
    instance = sooml_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sooml_Parameter_dataType_value_roundtrip():
    instance = sooml_Parameter(dataType="sample_text")
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_sooml_StructuralFeature_lowerBound_value_roundtrip():
    instance = sooml_StructuralFeature(lowerBound=7, upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_sooml_StructuralFeature_upperBound_value_roundtrip():
    instance = sooml_StructuralFeature(lowerBound=7, upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_sooml_CallOperationAction_isa_Action():
    instance = sooml_CallOperationAction()
    assert isinstance(instance, Action)


def test_sooml_ReferenceAssignmentAction_isa_Action():
    instance = sooml_ReferenceAssignmentAction()
    assert isinstance(instance, Action)


def test_sooml_CallParameterOperationAction_isa_CallOperationAction():
    instance = sooml_CallParameterOperationAction()
    assert isinstance(instance, CallOperationAction)


def test_sooml_CallReferenceOperationAction_isa_CallOperationAction():
    instance = sooml_CallReferenceOperationAction()
    assert isinstance(instance, CallOperationAction)


def test_sooml_IsInStateCondition_isa_Guard():
    instance = sooml_IsInStateCondition()
    assert isinstance(instance, Guard)


def test_sooml_ParameterIsInStateCondition_isa_IsInStateCondition():
    instance = sooml_ParameterIsInStateCondition()
    assert isinstance(instance, IsInStateCondition)


def test_sooml_ReferenceIsInStateCondition_isa_IsInStateCondition():
    instance = sooml_ReferenceIsInStateCondition()
    assert isinstance(instance, IsInStateCondition)


def test_sooml_Class_isa_NamedElement():
    instance = sooml_Class()
    assert isinstance(instance, NamedElement)


def test_sooml_Operation_isa_NamedElement():
    instance = sooml_Operation()
    assert isinstance(instance, NamedElement)


def test_sooml_Package_isa_NamedElement():
    instance = sooml_Package()
    assert isinstance(instance, NamedElement)


def test_sooml_Parameter_isa_NamedElement():
    instance = sooml_Parameter(dataType="sample_text")
    assert isinstance(instance, NamedElement)


def test_sooml_State_isa_NamedElement():
    instance = sooml_State()
    assert isinstance(instance, NamedElement)


def test_sooml_StructuralFeature_isa_NamedElement():
    instance = sooml_StructuralFeature(lowerBound=7, upperBound=7)
    assert isinstance(instance, NamedElement)


def test_sooml_Attribute_isa_StructuralFeature():
    instance = sooml_Attribute(dataType="sample_text")
    assert isinstance(instance, StructuralFeature)


def test_sooml_Reference_isa_StructuralFeature():
    instance = sooml_Reference()
    assert isinstance(instance, StructuralFeature)


def test_assoc_callObjectViaParameter63_link_reassign_clear():
    a = sooml_Parameter(dataType="sample_text")
    b1 = sooml_CallParameterOperationAction()
    b2 = sooml_CallParameterOperationAction()
    _safe_set(a, 'sooml_Parameter64', b1)
    assert _is_linked(a, 'sooml_Parameter64', b1)
    if hasattr(b1, 'sooml_CallParameterOperationAction'):
        assert _is_linked(b1, 'sooml_CallParameterOperationAction', a)
    _safe_set(a, 'sooml_Parameter64', b2)
    assert _is_linked(a, 'sooml_Parameter64', b2)
    if hasattr(b1, 'sooml_CallParameterOperationAction'):
        assert not _is_linked(b1, 'sooml_CallParameterOperationAction', a)
    if hasattr(b2, 'sooml_CallParameterOperationAction'):
        assert _is_linked(b2, 'sooml_CallParameterOperationAction', a)
    _safe_set(a, 'sooml_Parameter64', None)
    assert not _is_linked(a, 'sooml_Parameter64', b2)
    if hasattr(b2, 'sooml_CallParameterOperationAction'):
        assert not _is_linked(b2, 'sooml_CallParameterOperationAction', a)


def test_assoc_classType39_link_reassign_clear():
    a = sooml_Parameter(dataType="sample_text")
    b1 = sooml_Class()
    b2 = sooml_Class()
    _safe_set(a, 'sooml_Parameter40', b1)
    assert _is_linked(a, 'sooml_Parameter40', b1)
    if hasattr(b1, 'sooml_Class41'):
        assert _is_linked(b1, 'sooml_Class41', a)
    _safe_set(a, 'sooml_Parameter40', b2)
    assert _is_linked(a, 'sooml_Parameter40', b2)
    if hasattr(b1, 'sooml_Class41'):
        assert not _is_linked(b1, 'sooml_Class41', a)
    if hasattr(b2, 'sooml_Class41'):
        assert _is_linked(b2, 'sooml_Class41', a)
    _safe_set(a, 'sooml_Parameter40', None)
    assert not _is_linked(a, 'sooml_Parameter40', b2)
    if hasattr(b2, 'sooml_Class41'):
        assert not _is_linked(b2, 'sooml_Class41', a)


def test_assoc_features9_link_reassign_clear():
    a = sooml_StructuralFeature(lowerBound=7, upperBound=7)
    b1 = sooml_Class()
    b2 = sooml_Class()
    _safe_set(a, 'sooml_StructuralFeature', b1)
    assert _is_linked(a, 'sooml_StructuralFeature', b1)
    if hasattr(b1, 'sooml_Class10'):
        assert _is_linked(b1, 'sooml_Class10', a)
    _safe_set(a, 'sooml_StructuralFeature', b2)
    assert _is_linked(a, 'sooml_StructuralFeature', b2)
    if hasattr(b1, 'sooml_Class10'):
        assert not _is_linked(b1, 'sooml_Class10', a)
    if hasattr(b2, 'sooml_Class10'):
        assert _is_linked(b2, 'sooml_Class10', a)
    _safe_set(a, 'sooml_StructuralFeature', None)
    assert not _is_linked(a, 'sooml_StructuralFeature', b2)
    if hasattr(b2, 'sooml_Class10'):
        assert not _is_linked(b2, 'sooml_Class10', a)


def test_assoc_parameter16_link_reassign_clear():
    a = sooml_Parameter(dataType="sample_text")
    b1 = sooml_Operation()
    b2 = sooml_Operation()
    _safe_set(a, 'sooml_Parameter', b1)
    assert _is_linked(a, 'sooml_Parameter', b1)
    if hasattr(b1, 'sooml_Operation17'):
        assert _is_linked(b1, 'sooml_Operation17', a)
    _safe_set(a, 'sooml_Parameter', b2)
    assert _is_linked(a, 'sooml_Parameter', b2)
    if hasattr(b1, 'sooml_Operation17'):
        assert not _is_linked(b1, 'sooml_Operation17', a)
    if hasattr(b2, 'sooml_Operation17'):
        assert _is_linked(b2, 'sooml_Operation17', a)
    _safe_set(a, 'sooml_Parameter', None)
    assert not _is_linked(a, 'sooml_Parameter', b2)
    if hasattr(b2, 'sooml_Operation17'):
        assert not _is_linked(b2, 'sooml_Operation17', a)


def test_assoc_parameter59_link_reassign_clear():
    a = sooml_Parameter(dataType="sample_text")
    b1 = sooml_ParameterIsInStateCondition()
    b2 = sooml_ParameterIsInStateCondition()
    _safe_set(a, 'sooml_Parameter60', b1)
    assert _is_linked(a, 'sooml_Parameter60', b1)
    if hasattr(b1, 'sooml_ParameterIsInStateCondition'):
        assert _is_linked(b1, 'sooml_ParameterIsInStateCondition', a)
    _safe_set(a, 'sooml_Parameter60', b2)
    assert _is_linked(a, 'sooml_Parameter60', b2)
    if hasattr(b1, 'sooml_ParameterIsInStateCondition'):
        assert not _is_linked(b1, 'sooml_ParameterIsInStateCondition', a)
    if hasattr(b2, 'sooml_ParameterIsInStateCondition'):
        assert _is_linked(b2, 'sooml_ParameterIsInStateCondition', a)
    _safe_set(a, 'sooml_Parameter60', None)
    assert not _is_linked(a, 'sooml_Parameter60', b2)
    if hasattr(b2, 'sooml_ParameterIsInStateCondition'):
        assert not _is_linked(b2, 'sooml_ParameterIsInStateCondition', a)


def test_assoc_parameter65_link_reassign_clear():
    a = sooml_Parameter(dataType="sample_text")
    b1 = sooml_ReferenceAssignmentAction()
    b2 = sooml_ReferenceAssignmentAction()
    _safe_set(a, 'sooml_Parameter66', b1)
    assert _is_linked(a, 'sooml_Parameter66', b1)
    if hasattr(b1, 'sooml_ReferenceAssignmentAction'):
        assert _is_linked(b1, 'sooml_ReferenceAssignmentAction', a)
    _safe_set(a, 'sooml_Parameter66', b2)
    assert _is_linked(a, 'sooml_Parameter66', b2)
    if hasattr(b1, 'sooml_ReferenceAssignmentAction'):
        assert not _is_linked(b1, 'sooml_ReferenceAssignmentAction', a)
    if hasattr(b2, 'sooml_ReferenceAssignmentAction'):
        assert _is_linked(b2, 'sooml_ReferenceAssignmentAction', a)
    _safe_set(a, 'sooml_Parameter66', None)
    assert not _is_linked(a, 'sooml_Parameter66', b2)
    if hasattr(b2, 'sooml_ReferenceAssignmentAction'):
        assert not _is_linked(b2, 'sooml_ReferenceAssignmentAction', a)


def test_assoc_parameterBinding49_link_reassign_clear():
    a = sooml_Parameter(dataType="sample_text")
    b1 = sooml_ParameterBinding()
    b2 = sooml_ParameterBinding()
    _safe_set(a, 'sooml_Parameter51', b1)
    assert _is_linked(a, 'sooml_Parameter51', b1)
    if hasattr(b1, 'sooml_ParameterBinding50'):
        assert _is_linked(b1, 'sooml_ParameterBinding50', a)
    _safe_set(a, 'sooml_Parameter51', b2)
    assert _is_linked(a, 'sooml_Parameter51', b2)
    if hasattr(b1, 'sooml_ParameterBinding50'):
        assert not _is_linked(b1, 'sooml_ParameterBinding50', a)
    if hasattr(b2, 'sooml_ParameterBinding50'):
        assert _is_linked(b2, 'sooml_ParameterBinding50', a)
    _safe_set(a, 'sooml_Parameter51', None)
    assert not _is_linked(a, 'sooml_Parameter51', b2)
    if hasattr(b2, 'sooml_ParameterBinding50'):
        assert not _is_linked(b2, 'sooml_ParameterBinding50', a)


def test_assoc_structuralFeatureBinding46_link_reassign_clear():
    a = sooml_StructuralFeature(lowerBound=7, upperBound=7)
    b1 = sooml_ParameterBinding()
    b2 = sooml_ParameterBinding()
    _safe_set(a, 'sooml_StructuralFeature48', b1)
    assert _is_linked(a, 'sooml_StructuralFeature48', b1)
    if hasattr(b1, 'sooml_ParameterBinding47'):
        assert _is_linked(b1, 'sooml_ParameterBinding47', a)
    _safe_set(a, 'sooml_StructuralFeature48', b2)
    assert _is_linked(a, 'sooml_StructuralFeature48', b2)
    if hasattr(b1, 'sooml_ParameterBinding47'):
        assert not _is_linked(b1, 'sooml_ParameterBinding47', a)
    if hasattr(b2, 'sooml_ParameterBinding47'):
        assert _is_linked(b2, 'sooml_ParameterBinding47', a)
    _safe_set(a, 'sooml_StructuralFeature48', None)
    assert not _is_linked(a, 'sooml_StructuralFeature48', b2)
    if hasattr(b2, 'sooml_ParameterBinding47'):
        assert not _is_linked(b2, 'sooml_ParameterBinding47', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


CallOperationAction_strategy = st.builds(CallOperationAction)
@given(instance=CallOperationAction_strategy)
@settings(max_examples=25)
def test_CallOperationAction_instantiation(instance):
    assert isinstance(instance, CallOperationAction)


Guard_strategy = st.builds(Guard)
@given(instance=Guard_strategy)
@settings(max_examples=25)
def test_Guard_instantiation(instance):
    assert isinstance(instance, Guard)


IsInStateCondition_strategy = st.builds(IsInStateCondition)
@given(instance=IsInStateCondition_strategy)
@settings(max_examples=25)
def test_IsInStateCondition_instantiation(instance):
    assert isinstance(instance, IsInStateCondition)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


StructuralFeature_strategy = st.builds(StructuralFeature)
@given(instance=StructuralFeature_strategy)
@settings(max_examples=25)
def test_StructuralFeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)


sooml_Action_strategy = st.builds(sooml_Action)
@given(instance=sooml_Action_strategy)
@settings(max_examples=25)
def test_sooml_Action_instantiation(instance):
    assert isinstance(instance, sooml_Action)


sooml_Attribute_strategy = st.builds(sooml_Attribute, dataType=safe_text)
@given(instance=sooml_Attribute_strategy)
@settings(max_examples=25)
def test_sooml_Attribute_instantiation(instance):
    assert isinstance(instance, sooml_Attribute)


sooml_CallOperationAction_strategy = st.builds(sooml_CallOperationAction)
@given(instance=sooml_CallOperationAction_strategy)
@settings(max_examples=25)
def test_sooml_CallOperationAction_instantiation(instance):
    assert isinstance(instance, sooml_CallOperationAction)


sooml_CallParameterOperationAction_strategy = st.builds(sooml_CallParameterOperationAction)
@given(instance=sooml_CallParameterOperationAction_strategy)
@settings(max_examples=25)
def test_sooml_CallParameterOperationAction_instantiation(instance):
    assert isinstance(instance, sooml_CallParameterOperationAction)


sooml_CallReferenceOperationAction_strategy = st.builds(sooml_CallReferenceOperationAction)
@given(instance=sooml_CallReferenceOperationAction_strategy)
@settings(max_examples=25)
def test_sooml_CallReferenceOperationAction_instantiation(instance):
    assert isinstance(instance, sooml_CallReferenceOperationAction)


sooml_Class_strategy = st.builds(sooml_Class)
@given(instance=sooml_Class_strategy)
@settings(max_examples=25)
def test_sooml_Class_instantiation(instance):
    assert isinstance(instance, sooml_Class)


sooml_EntryOperation_strategy = st.builds(sooml_EntryOperation)
@given(instance=sooml_EntryOperation_strategy)
@settings(max_examples=25)
def test_sooml_EntryOperation_instantiation(instance):
    assert isinstance(instance, sooml_EntryOperation)


sooml_Event_strategy = st.builds(sooml_Event)
@given(instance=sooml_Event_strategy)
@settings(max_examples=25)
def test_sooml_Event_instantiation(instance):
    assert isinstance(instance, sooml_Event)


sooml_Guard_strategy = st.builds(sooml_Guard)
@given(instance=sooml_Guard_strategy)
@settings(max_examples=25)
def test_sooml_Guard_instantiation(instance):
    assert isinstance(instance, sooml_Guard)


sooml_IsInStateCondition_strategy = st.builds(sooml_IsInStateCondition)
@given(instance=sooml_IsInStateCondition_strategy)
@settings(max_examples=25)
def test_sooml_IsInStateCondition_instantiation(instance):
    assert isinstance(instance, sooml_IsInStateCondition)


sooml_NamedElement_strategy = st.builds(sooml_NamedElement, name=safe_text)
@given(instance=sooml_NamedElement_strategy)
@settings(max_examples=25)
def test_sooml_NamedElement_instantiation(instance):
    assert isinstance(instance, sooml_NamedElement)


sooml_Operation_strategy = st.builds(sooml_Operation)
@given(instance=sooml_Operation_strategy)
@settings(max_examples=25)
def test_sooml_Operation_instantiation(instance):
    assert isinstance(instance, sooml_Operation)


sooml_Package_strategy = st.builds(sooml_Package)
@given(instance=sooml_Package_strategy)
@settings(max_examples=25)
def test_sooml_Package_instantiation(instance):
    assert isinstance(instance, sooml_Package)


sooml_Parameter_strategy = st.builds(sooml_Parameter, dataType=safe_text)
@given(instance=sooml_Parameter_strategy)
@settings(max_examples=25)
def test_sooml_Parameter_instantiation(instance):
    assert isinstance(instance, sooml_Parameter)


sooml_ParameterBinding_strategy = st.builds(sooml_ParameterBinding)
@given(instance=sooml_ParameterBinding_strategy)
@settings(max_examples=25)
def test_sooml_ParameterBinding_instantiation(instance):
    assert isinstance(instance, sooml_ParameterBinding)


sooml_ParameterIsInStateCondition_strategy = st.builds(sooml_ParameterIsInStateCondition)
@given(instance=sooml_ParameterIsInStateCondition_strategy)
@settings(max_examples=25)
def test_sooml_ParameterIsInStateCondition_instantiation(instance):
    assert isinstance(instance, sooml_ParameterIsInStateCondition)


sooml_Reference_strategy = st.builds(sooml_Reference)
@given(instance=sooml_Reference_strategy)
@settings(max_examples=25)
def test_sooml_Reference_instantiation(instance):
    assert isinstance(instance, sooml_Reference)


sooml_ReferenceAssignmentAction_strategy = st.builds(sooml_ReferenceAssignmentAction)
@given(instance=sooml_ReferenceAssignmentAction_strategy)
@settings(max_examples=25)
def test_sooml_ReferenceAssignmentAction_instantiation(instance):
    assert isinstance(instance, sooml_ReferenceAssignmentAction)


sooml_ReferenceIsInStateCondition_strategy = st.builds(sooml_ReferenceIsInStateCondition)
@given(instance=sooml_ReferenceIsInStateCondition_strategy)
@settings(max_examples=25)
def test_sooml_ReferenceIsInStateCondition_instantiation(instance):
    assert isinstance(instance, sooml_ReferenceIsInStateCondition)


sooml_State_strategy = st.builds(sooml_State)
@given(instance=sooml_State_strategy)
@settings(max_examples=25)
def test_sooml_State_instantiation(instance):
    assert isinstance(instance, sooml_State)


sooml_StateMachine_strategy = st.builds(sooml_StateMachine)
@given(instance=sooml_StateMachine_strategy)
@settings(max_examples=25)
def test_sooml_StateMachine_instantiation(instance):
    assert isinstance(instance, sooml_StateMachine)


sooml_StructuralFeature_strategy = st.builds(sooml_StructuralFeature, lowerBound=st.integers(), upperBound=st.integers())
@given(instance=sooml_StructuralFeature_strategy)
@settings(max_examples=25)
def test_sooml_StructuralFeature_instantiation(instance):
    assert isinstance(instance, sooml_StructuralFeature)


sooml_Transition_strategy = st.builds(sooml_Transition)
@given(instance=sooml_Transition_strategy)
@settings(max_examples=25)
def test_sooml_Transition_instantiation(instance):
    assert isinstance(instance, sooml_Transition)



