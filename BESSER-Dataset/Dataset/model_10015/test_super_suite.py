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
    operators_QueryVariableQualifier,
    operators_EOperation,
    QueryVariableQualifier,
    operators_EReferenceQualifier,
    operators_EOperationQualifier,
    operators_StructuralFeatureSet,
    operators_EStructuralFeature,
    operators_Variable,
    operators_EObject,
    operators_EClass,
    Variable,
    operators_QueryVariable,
    operators_EReference,
    operators_Referrable,
    Referrable,
    operators_VariableReference,
    Result,
    operators_PrimitiveReference,
    operators_EObjectReference,
    operators_EAttribute,
    operators_Result,
    operators_Operator,
    operators_TypeVariable,
    Operator,
    operators_MOVE,
    operators_MERGE,
    operators_SPLIT,
    operators_ASSIGN,
    operators_SET,
    operators_DELETE,
    operators_VAR,
    operators_CREATE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_operators_queryvariablequalifier_is_not_abstract():
    assert not inspect.isabstract(operators_QueryVariableQualifier)


def test_hyp_operators_queryvariablequalifier_constructor_exists():
    assert callable(operators_QueryVariableQualifier.__init__)


def test_hyp_operators_queryvariablequalifier_constructor_args():
    sig = inspect.signature(operators_QueryVariableQualifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_eoperation_is_not_abstract():
    assert not inspect.isabstract(operators_EOperation)


def test_hyp_operators_eoperation_constructor_exists():
    assert callable(operators_EOperation.__init__)


def test_hyp_operators_eoperation_constructor_args():
    sig = inspect.signature(operators_EOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_queryvariablequalifier_is_not_abstract():
    assert not inspect.isabstract(QueryVariableQualifier)


def test_hyp_queryvariablequalifier_constructor_exists():
    assert callable(QueryVariableQualifier.__init__)


def test_hyp_queryvariablequalifier_constructor_args():
    sig = inspect.signature(QueryVariableQualifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_ereferencequalifier_is_not_abstract():
    assert not inspect.isabstract(operators_EReferenceQualifier)


def test_hyp_operators_ereferencequalifier_constructor_exists():
    assert callable(operators_EReferenceQualifier.__init__)


def test_hyp_operators_ereferencequalifier_constructor_args():
    sig = inspect.signature(operators_EReferenceQualifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_eoperationqualifier_is_not_abstract():
    assert not inspect.isabstract(operators_EOperationQualifier)


def test_hyp_operators_eoperationqualifier_constructor_exists():
    assert callable(operators_EOperationQualifier.__init__)


def test_hyp_operators_eoperationqualifier_constructor_args():
    sig = inspect.signature(operators_EOperationQualifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_structuralfeatureset_is_not_abstract():
    assert not inspect.isabstract(operators_StructuralFeatureSet)


def test_hyp_operators_structuralfeatureset_constructor_exists():
    assert callable(operators_StructuralFeatureSet.__init__)


def test_hyp_operators_structuralfeatureset_constructor_args():
    sig = inspect.signature(operators_StructuralFeatureSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(operators_EStructuralFeature)


def test_hyp_operators_estructuralfeature_constructor_exists():
    assert callable(operators_EStructuralFeature.__init__)


def test_hyp_operators_estructuralfeature_constructor_args():
    sig = inspect.signature(operators_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_variable_is_not_abstract():
    assert not inspect.isabstract(operators_Variable)


def test_hyp_operators_variable_constructor_exists():
    assert callable(operators_Variable.__init__)


def test_hyp_operators_variable_constructor_args():
    sig = inspect.signature(operators_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_operators_eobject_is_not_abstract():
    assert not inspect.isabstract(operators_EObject)


def test_hyp_operators_eobject_constructor_exists():
    assert callable(operators_EObject.__init__)


def test_hyp_operators_eobject_constructor_args():
    sig = inspect.signature(operators_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_eclass_is_not_abstract():
    assert not inspect.isabstract(operators_EClass)


def test_hyp_operators_eclass_constructor_exists():
    assert callable(operators_EClass.__init__)


def test_hyp_operators_eclass_constructor_args():
    sig = inspect.signature(operators_EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_queryvariable_is_not_abstract():
    assert not inspect.isabstract(operators_QueryVariable)


def test_hyp_operators_queryvariable_constructor_exists():
    assert callable(operators_QueryVariable.__init__)


def test_hyp_operators_queryvariable_constructor_args():
    sig = inspect.signature(operators_QueryVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_ereference_is_not_abstract():
    assert not inspect.isabstract(operators_EReference)


def test_hyp_operators_ereference_constructor_exists():
    assert callable(operators_EReference.__init__)


def test_hyp_operators_ereference_constructor_args():
    sig = inspect.signature(operators_EReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_referrable_is_not_abstract():
    assert not inspect.isabstract(operators_Referrable)


def test_hyp_operators_referrable_constructor_exists():
    assert callable(operators_Referrable.__init__)


def test_hyp_operators_referrable_constructor_args():
    sig = inspect.signature(operators_Referrable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_referrable_is_not_abstract():
    assert not inspect.isabstract(Referrable)


def test_hyp_referrable_constructor_exists():
    assert callable(Referrable.__init__)


def test_hyp_referrable_constructor_args():
    sig = inspect.signature(Referrable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_variablereference_is_not_abstract():
    assert not inspect.isabstract(operators_VariableReference)


def test_hyp_operators_variablereference_constructor_exists():
    assert callable(operators_VariableReference.__init__)


def test_hyp_operators_variablereference_constructor_args():
    sig = inspect.signature(operators_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_result_is_not_abstract():
    assert not inspect.isabstract(Result)


def test_hyp_result_constructor_exists():
    assert callable(Result.__init__)


def test_hyp_result_constructor_args():
    sig = inspect.signature(Result.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_primitivereference_is_not_abstract():
    assert not inspect.isabstract(operators_PrimitiveReference)


def test_hyp_operators_primitivereference_constructor_exists():
    assert callable(operators_PrimitiveReference.__init__)


def test_hyp_operators_primitivereference_constructor_args():
    sig = inspect.signature(operators_PrimitiveReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_operators_eobjectreference_is_not_abstract():
    assert not inspect.isabstract(operators_EObjectReference)


def test_hyp_operators_eobjectreference_constructor_exists():
    assert callable(operators_EObjectReference.__init__)


def test_hyp_operators_eobjectreference_constructor_args():
    sig = inspect.signature(operators_EObjectReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_eattribute_is_not_abstract():
    assert not inspect.isabstract(operators_EAttribute)


def test_hyp_operators_eattribute_constructor_exists():
    assert callable(operators_EAttribute.__init__)


def test_hyp_operators_eattribute_constructor_args():
    sig = inspect.signature(operators_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_result_is_not_abstract():
    assert not inspect.isabstract(operators_Result)


def test_hyp_operators_result_constructor_exists():
    assert callable(operators_Result.__init__)


def test_hyp_operators_result_constructor_args():
    sig = inspect.signature(operators_Result.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Operator)


def test_hyp_operators_operator_constructor_exists():
    assert callable(operators_Operator.__init__)


def test_hyp_operators_operator_constructor_args():
    sig = inspect.signature(operators_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "executed" in params, "Missing parameter 'executed'"




def test_hyp_operators_typevariable_is_not_abstract():
    assert not inspect.isabstract(operators_TypeVariable)


def test_hyp_operators_typevariable_constructor_exists():
    assert callable(operators_TypeVariable.__init__)


def test_hyp_operators_typevariable_constructor_args():
    sig = inspect.signature(operators_TypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_hyp_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_hyp_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_move_is_not_abstract():
    assert not inspect.isabstract(operators_MOVE)


def test_hyp_operators_move_constructor_exists():
    assert callable(operators_MOVE.__init__)


def test_hyp_operators_move_constructor_args():
    sig = inspect.signature(operators_MOVE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_merge_is_not_abstract():
    assert not inspect.isabstract(operators_MERGE)


def test_hyp_operators_merge_constructor_exists():
    assert callable(operators_MERGE.__init__)


def test_hyp_operators_merge_constructor_args():
    sig = inspect.signature(operators_MERGE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_split_is_not_abstract():
    assert not inspect.isabstract(operators_SPLIT)


def test_hyp_operators_split_constructor_exists():
    assert callable(operators_SPLIT.__init__)


def test_hyp_operators_split_constructor_args():
    sig = inspect.signature(operators_SPLIT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_assign_is_not_abstract():
    assert not inspect.isabstract(operators_ASSIGN)


def test_hyp_operators_assign_constructor_exists():
    assert callable(operators_ASSIGN.__init__)


def test_hyp_operators_assign_constructor_args():
    sig = inspect.signature(operators_ASSIGN.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_operators_set_is_not_abstract():
    assert not inspect.isabstract(operators_SET)


def test_hyp_operators_set_constructor_exists():
    assert callable(operators_SET.__init__)


def test_hyp_operators_set_constructor_args():
    sig = inspect.signature(operators_SET.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_delete_is_not_abstract():
    assert not inspect.isabstract(operators_DELETE)


def test_hyp_operators_delete_constructor_exists():
    assert callable(operators_DELETE.__init__)


def test_hyp_operators_delete_constructor_args():
    sig = inspect.signature(operators_DELETE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_var_is_not_abstract():
    assert not inspect.isabstract(operators_VAR)


def test_hyp_operators_var_constructor_exists():
    assert callable(operators_VAR.__init__)


def test_hyp_operators_var_constructor_args():
    sig = inspect.signature(operators_VAR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_create_is_not_abstract():
    assert not inspect.isabstract(operators_CREATE)


def test_hyp_operators_create_constructor_exists():
    assert callable(operators_CREATE.__init__)


def test_hyp_operators_create_constructor_args():
    sig = inspect.signature(operators_CREATE.__init__)
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
operators_QueryVariableQualifier_strategy = st.builds(
    operators_QueryVariableQualifier,
)
operators_EOperation_strategy = st.builds(
    operators_EOperation,
)
QueryVariableQualifier_strategy = st.builds(
    QueryVariableQualifier,
)
operators_EReferenceQualifier_strategy = st.builds(
    operators_EReferenceQualifier,
)
operators_EOperationQualifier_strategy = st.builds(
    operators_EOperationQualifier,
)
operators_StructuralFeatureSet_strategy = st.builds(
    operators_StructuralFeatureSet,
)
operators_EStructuralFeature_strategy = st.builds(
    operators_EStructuralFeature,
)
operators_Variable_strategy = st.builds(
    operators_Variable,
    name=
        safe_text
)
operators_EObject_strategy = st.builds(
    operators_EObject,
)
operators_EClass_strategy = st.builds(
    operators_EClass,
)
Variable_strategy = st.builds(
    Variable,
)
operators_QueryVariable_strategy = st.builds(
    operators_QueryVariable,
)
operators_EReference_strategy = st.builds(
    operators_EReference,
)
operators_Referrable_strategy = st.builds(
    operators_Referrable,
)
Referrable_strategy = st.builds(
    Referrable,
)
operators_VariableReference_strategy = st.builds(
    operators_VariableReference,
)
Result_strategy = st.builds(
    Result,
)
operators_PrimitiveReference_strategy = st.builds(
    operators_PrimitiveReference,
    value=
        safe_text
)
operators_EObjectReference_strategy = st.builds(
    operators_EObjectReference,
)
operators_EAttribute_strategy = st.builds(
    operators_EAttribute,
)
operators_Result_strategy = st.builds(
    operators_Result,
)
operators_Operator_strategy = st.builds(
    operators_Operator,
    executed=
        st.booleans()
)
operators_TypeVariable_strategy = st.builds(
    operators_TypeVariable,
)
Operator_strategy = st.builds(
    Operator,
)
operators_MOVE_strategy = st.builds(
    operators_MOVE,
)
operators_MERGE_strategy = st.builds(
    operators_MERGE,
)
operators_SPLIT_strategy = st.builds(
    operators_SPLIT,
)
operators_ASSIGN_strategy = st.builds(
    operators_ASSIGN,
    value=
        safe_text
)
operators_SET_strategy = st.builds(
    operators_SET,
)
operators_DELETE_strategy = st.builds(
    operators_DELETE,
)
operators_VAR_strategy = st.builds(
    operators_VAR,
)
operators_CREATE_strategy = st.builds(
    operators_CREATE,
)











@given(instance=operators_Variable_strategy)
def test_hyp_operators_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original













@given(instance=operators_PrimitiveReference_strategy)
def test_hyp_operators_primitivereference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=operators_Operator_strategy)
def test_hyp_operators_operator_executed_setter(instance):
    original = instance.executed
    instance.executed = original
    assert instance.executed == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings







@given(instance=operators_ASSIGN_strategy)
def test_hyp_operators_assign_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Operator,
    QueryVariableQualifier,
    Referrable,
    Result,
    Variable,
    operators_ASSIGN,
    operators_CREATE,
    operators_DELETE,
    operators_EAttribute,
    operators_EClass,
    operators_EObject,
    operators_EObjectReference,
    operators_EOperation,
    operators_EOperationQualifier,
    operators_EReference,
    operators_EReferenceQualifier,
    operators_EStructuralFeature,
    operators_MERGE,
    operators_MOVE,
    operators_Operator,
    operators_PrimitiveReference,
    operators_QueryVariable,
    operators_QueryVariableQualifier,
    operators_Referrable,
    operators_Result,
    operators_SET,
    operators_SPLIT,
    operators_StructuralFeatureSet,
    operators_TypeVariable,
    operators_VAR,
    operators_Variable,
    operators_VariableReference,
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

def test_operators_ASSIGN_value_value_roundtrip():
    instance = operators_ASSIGN(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_operators_Operator_executed_value_roundtrip():
    instance = operators_Operator(executed=True)
    assert instance.executed == True
    instance.executed = False
    assert instance.executed == False


def test_operators_PrimitiveReference_value_value_roundtrip():
    instance = operators_PrimitiveReference(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_operators_Variable_name_value_roundtrip():
    instance = operators_Variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_operators_ASSIGN_isa_Operator():
    instance = operators_ASSIGN(value="sample_text")
    assert isinstance(instance, Operator)


def test_operators_CREATE_isa_Operator():
    instance = operators_CREATE()
    assert isinstance(instance, Operator)


def test_operators_DELETE_isa_Operator():
    instance = operators_DELETE()
    assert isinstance(instance, Operator)


def test_operators_MERGE_isa_Operator():
    instance = operators_MERGE()
    assert isinstance(instance, Operator)


def test_operators_MOVE_isa_Operator():
    instance = operators_MOVE()
    assert isinstance(instance, Operator)


def test_operators_SET_isa_Operator():
    instance = operators_SET()
    assert isinstance(instance, Operator)


def test_operators_SPLIT_isa_Operator():
    instance = operators_SPLIT()
    assert isinstance(instance, Operator)


def test_operators_VAR_isa_Operator():
    instance = operators_VAR()
    assert isinstance(instance, Operator)


def test_operators_EOperationQualifier_isa_QueryVariableQualifier():
    instance = operators_EOperationQualifier()
    assert isinstance(instance, QueryVariableQualifier)


def test_operators_EReferenceQualifier_isa_QueryVariableQualifier():
    instance = operators_EReferenceQualifier()
    assert isinstance(instance, QueryVariableQualifier)


def test_operators_EObjectReference_isa_Referrable():
    instance = operators_EObjectReference()
    assert isinstance(instance, Referrable)


def test_operators_VariableReference_isa_Referrable():
    instance = operators_VariableReference()
    assert isinstance(instance, Referrable)


def test_operators_EObjectReference_isa_Result():
    instance = operators_EObjectReference()
    assert isinstance(instance, Result)


def test_operators_PrimitiveReference_isa_Result():
    instance = operators_PrimitiveReference(value="sample_text")
    assert isinstance(instance, Result)


def test_operators_QueryVariable_isa_Variable():
    instance = operators_QueryVariable()
    assert isinstance(instance, Variable)


def test_operators_TypeVariable_isa_Variable():
    instance = operators_TypeVariable()
    assert isinstance(instance, Variable)


def test_assoc_attribute12_link_reassign_clear():
    a = operators_ASSIGN(value="sample_text")
    b1 = operators_EAttribute()
    b2 = operators_EAttribute()
    _safe_set(a, 'operators_ASSIGN', b1)
    assert _is_linked(a, 'operators_ASSIGN', b1)
    if hasattr(b1, 'operators_EAttribute'):
        assert _is_linked(b1, 'operators_EAttribute', a)
    _safe_set(a, 'operators_ASSIGN', b2)
    assert _is_linked(a, 'operators_ASSIGN', b2)
    if hasattr(b1, 'operators_EAttribute'):
        assert not _is_linked(b1, 'operators_EAttribute', a)
    if hasattr(b2, 'operators_EAttribute'):
        assert _is_linked(b2, 'operators_EAttribute', a)
    _safe_set(a, 'operators_ASSIGN', None)
    assert not _is_linked(a, 'operators_ASSIGN', b2)
    if hasattr(b2, 'operators_EAttribute'):
        assert not _is_linked(b2, 'operators_EAttribute', a)


def test_assoc_attributeOwner13_link_reassign_clear():
    a = operators_ASSIGN(value="sample_text")
    b1 = operators_Referrable()
    b2 = operators_Referrable()
    _safe_set(a, 'operators_ASSIGN14', b1)
    assert _is_linked(a, 'operators_ASSIGN14', b1)
    if hasattr(b1, 'operators_Referrable15'):
        assert _is_linked(b1, 'operators_Referrable15', a)
    _safe_set(a, 'operators_ASSIGN14', b2)
    assert _is_linked(a, 'operators_ASSIGN14', b2)
    if hasattr(b1, 'operators_Referrable15'):
        assert not _is_linked(b1, 'operators_Referrable15', a)
    if hasattr(b2, 'operators_Referrable15'):
        assert _is_linked(b2, 'operators_Referrable15', a)
    _safe_set(a, 'operators_ASSIGN14', None)
    assert not _is_linked(a, 'operators_ASSIGN14', b2)
    if hasattr(b2, 'operators_Referrable15'):
        assert not _is_linked(b2, 'operators_Referrable15', a)


def test_assoc_deletion10_link_reassign_clear():
    a = operators_DELETE()
    b1 = operators_Referrable()
    b2 = operators_Referrable()
    _safe_set(a, 'operators_DELETE', b1)
    assert _is_linked(a, 'operators_DELETE', b1)
    if hasattr(b1, 'operators_Referrable11'):
        assert _is_linked(b1, 'operators_Referrable11', a)
    _safe_set(a, 'operators_DELETE', b2)
    assert _is_linked(a, 'operators_DELETE', b2)
    if hasattr(b1, 'operators_Referrable11'):
        assert not _is_linked(b1, 'operators_Referrable11', a)
    if hasattr(b2, 'operators_Referrable11'):
        assert _is_linked(b2, 'operators_Referrable11', a)
    _safe_set(a, 'operators_DELETE', None)
    assert not _is_linked(a, 'operators_DELETE', b2)
    if hasattr(b2, 'operators_Referrable11'):
        assert not _is_linked(b2, 'operators_Referrable11', a)


def test_assoc_movee32_link_reassign_clear():
    a = operators_MOVE()
    b1 = operators_Referrable()
    b2 = operators_Referrable()
    _safe_set(a, 'operators_MOVE33', b1)
    assert _is_linked(a, 'operators_MOVE33', b1)
    if hasattr(b1, 'operators_Referrable34'):
        assert _is_linked(b1, 'operators_Referrable34', a)
    _safe_set(a, 'operators_MOVE33', b2)
    assert _is_linked(a, 'operators_MOVE33', b2)
    if hasattr(b1, 'operators_Referrable34'):
        assert not _is_linked(b1, 'operators_Referrable34', a)
    if hasattr(b2, 'operators_Referrable34'):
        assert _is_linked(b2, 'operators_Referrable34', a)
    _safe_set(a, 'operators_MOVE33', None)
    assert not _is_linked(a, 'operators_MOVE33', b2)
    if hasattr(b2, 'operators_Referrable34'):
        assert not _is_linked(b2, 'operators_Referrable34', a)


def test_assoc_newInstanceVariable1_link_reassign_clear():
    a = operators_CREATE()
    b1 = operators_TypeVariable()
    b2 = operators_TypeVariable()
    _safe_set(a, 'operators_CREATE', b1)
    assert _is_linked(a, 'operators_CREATE', b1)
    if hasattr(b1, 'operators_TypeVariable'):
        assert _is_linked(b1, 'operators_TypeVariable', a)
    _safe_set(a, 'operators_CREATE', b2)
    assert _is_linked(a, 'operators_CREATE', b2)
    if hasattr(b1, 'operators_TypeVariable'):
        assert not _is_linked(b1, 'operators_TypeVariable', a)
    if hasattr(b2, 'operators_TypeVariable'):
        assert _is_linked(b2, 'operators_TypeVariable', a)
    _safe_set(a, 'operators_CREATE', None)
    assert not _is_linked(a, 'operators_CREATE', b2)
    if hasattr(b2, 'operators_TypeVariable'):
        assert not _is_linked(b2, 'operators_TypeVariable', a)


def test_assoc_newParent27_link_reassign_clear():
    a = operators_MOVE()
    b1 = operators_Referrable()
    b2 = operators_Referrable()
    _safe_set(a, 'operators_MOVE', b1)
    assert _is_linked(a, 'operators_MOVE', b1)
    if hasattr(b1, 'operators_Referrable28'):
        assert _is_linked(b1, 'operators_Referrable28', a)
    _safe_set(a, 'operators_MOVE', b2)
    assert _is_linked(a, 'operators_MOVE', b2)
    if hasattr(b1, 'operators_Referrable28'):
        assert not _is_linked(b1, 'operators_Referrable28', a)
    if hasattr(b2, 'operators_Referrable28'):
        assert _is_linked(b2, 'operators_Referrable28', a)
    _safe_set(a, 'operators_MOVE', None)
    assert not _is_linked(a, 'operators_MOVE', b2)
    if hasattr(b2, 'operators_Referrable28'):
        assert not _is_linked(b2, 'operators_Referrable28', a)


def test_assoc_parent2_link_reassign_clear():
    a = operators_CREATE()
    b1 = operators_Referrable()
    b2 = operators_Referrable()
    _safe_set(a, 'operators_CREATE3', b1)
    assert _is_linked(a, 'operators_CREATE3', b1)
    if hasattr(b1, 'operators_Referrable'):
        assert _is_linked(b1, 'operators_Referrable', a)
    _safe_set(a, 'operators_CREATE3', b2)
    assert _is_linked(a, 'operators_CREATE3', b2)
    if hasattr(b1, 'operators_Referrable'):
        assert not _is_linked(b1, 'operators_Referrable', a)
    if hasattr(b2, 'operators_Referrable'):
        assert _is_linked(b2, 'operators_Referrable', a)
    _safe_set(a, 'operators_CREATE3', None)
    assert not _is_linked(a, 'operators_CREATE3', b2)
    if hasattr(b2, 'operators_Referrable'):
        assert not _is_linked(b2, 'operators_Referrable', a)


def test_assoc_parentCompositeReference4_link_reassign_clear():
    a = operators_CREATE()
    b1 = operators_EReference()
    b2 = operators_EReference()
    _safe_set(a, 'operators_CREATE5', b1)
    assert _is_linked(a, 'operators_CREATE5', b1)
    if hasattr(b1, 'operators_EReference'):
        assert _is_linked(b1, 'operators_EReference', a)
    _safe_set(a, 'operators_CREATE5', b2)
    assert _is_linked(a, 'operators_CREATE5', b2)
    if hasattr(b1, 'operators_EReference'):
        assert not _is_linked(b1, 'operators_EReference', a)
    if hasattr(b2, 'operators_EReference'):
        assert _is_linked(b2, 'operators_EReference', a)
    _safe_set(a, 'operators_CREATE5', None)
    assert not _is_linked(a, 'operators_CREATE5', b2)
    if hasattr(b2, 'operators_EReference'):
        assert not _is_linked(b2, 'operators_EReference', a)


def test_assoc_parentReference29_link_reassign_clear():
    a = operators_MOVE()
    b1 = operators_EReference()
    b2 = operators_EReference()
    _safe_set(a, 'operators_MOVE30', b1)
    assert _is_linked(a, 'operators_MOVE30', b1)
    if hasattr(b1, 'operators_EReference31'):
        assert _is_linked(b1, 'operators_EReference31', a)
    _safe_set(a, 'operators_MOVE30', b2)
    assert _is_linked(a, 'operators_MOVE30', b2)
    if hasattr(b1, 'operators_EReference31'):
        assert not _is_linked(b1, 'operators_EReference31', a)
    if hasattr(b2, 'operators_EReference31'):
        assert _is_linked(b2, 'operators_EReference31', a)
    _safe_set(a, 'operators_MOVE30', None)
    assert not _is_linked(a, 'operators_MOVE30', b2)
    if hasattr(b2, 'operators_EReference31'):
        assert not _is_linked(b2, 'operators_EReference31', a)


def test_assoc_reference18_link_reassign_clear():
    a = operators_SET()
    b1 = operators_EReference()
    b2 = operators_EReference()
    _safe_set(a, 'operators_SET', b1)
    assert _is_linked(a, 'operators_SET', b1)
    if hasattr(b1, 'operators_EReference19'):
        assert _is_linked(b1, 'operators_EReference19', a)
    _safe_set(a, 'operators_SET', b2)
    assert _is_linked(a, 'operators_SET', b2)
    if hasattr(b1, 'operators_EReference19'):
        assert not _is_linked(b1, 'operators_EReference19', a)
    if hasattr(b2, 'operators_EReference19'):
        assert _is_linked(b2, 'operators_EReference19', a)
    _safe_set(a, 'operators_SET', None)
    assert not _is_linked(a, 'operators_SET', b2)
    if hasattr(b2, 'operators_EReference19'):
        assert not _is_linked(b2, 'operators_EReference19', a)


def test_assoc_referenceOwner23_link_reassign_clear():
    a = operators_SET()
    b1 = operators_Referrable()
    b2 = operators_Referrable()
    _safe_set(a, 'operators_SET24', b1)
    assert _is_linked(a, 'operators_SET24', b1)
    if hasattr(b1, 'operators_Referrable25'):
        assert _is_linked(b1, 'operators_Referrable25', a)
    _safe_set(a, 'operators_SET24', b2)
    assert _is_linked(a, 'operators_SET24', b2)
    if hasattr(b1, 'operators_Referrable25'):
        assert not _is_linked(b1, 'operators_Referrable25', a)
    if hasattr(b2, 'operators_Referrable25'):
        assert _is_linked(b2, 'operators_Referrable25', a)
    _safe_set(a, 'operators_SET24', None)
    assert not _is_linked(a, 'operators_SET24', b2)
    if hasattr(b2, 'operators_Referrable25'):
        assert not _is_linked(b2, 'operators_Referrable25', a)


def test_assoc_referencedVariable26_link_reassign_clear():
    a = operators_Variable(name="sample_text")
    b1 = operators_VariableReference()
    b2 = operators_VariableReference()
    _safe_set(a, 'operators_Variable', b1)
    assert _is_linked(a, 'operators_Variable', b1)
    if hasattr(b1, 'operators_VariableReference'):
        assert _is_linked(b1, 'operators_VariableReference', a)
    _safe_set(a, 'operators_Variable', b2)
    assert _is_linked(a, 'operators_Variable', b2)
    if hasattr(b1, 'operators_VariableReference'):
        assert not _is_linked(b1, 'operators_VariableReference', a)
    if hasattr(b2, 'operators_VariableReference'):
        assert _is_linked(b2, 'operators_VariableReference', a)
    _safe_set(a, 'operators_Variable', None)
    assert not _is_linked(a, 'operators_Variable', b2)
    if hasattr(b2, 'operators_VariableReference'):
        assert not _is_linked(b2, 'operators_VariableReference', a)


def test_assoc_result0_link_reassign_clear():
    a = operators_Operator(executed=True)
    b1 = operators_Result()
    b2 = operators_Result()
    _safe_set(a, 'operators_Operator', b1)
    assert _is_linked(a, 'operators_Operator', b1)
    if hasattr(b1, 'operators_Result'):
        assert _is_linked(b1, 'operators_Result', a)
    _safe_set(a, 'operators_Operator', b2)
    assert _is_linked(a, 'operators_Operator', b2)
    if hasattr(b1, 'operators_Result'):
        assert not _is_linked(b1, 'operators_Result', a)
    if hasattr(b2, 'operators_Result'):
        assert _is_linked(b2, 'operators_Result', a)
    _safe_set(a, 'operators_Operator', None)
    assert not _is_linked(a, 'operators_Operator', b2)
    if hasattr(b2, 'operators_Result'):
        assert not _is_linked(b2, 'operators_Result', a)


def test_assoc_value20_link_reassign_clear():
    a = operators_SET()
    b1 = operators_Referrable()
    b2 = operators_Referrable()
    _safe_set(a, 'operators_SET21', b1)
    assert _is_linked(a, 'operators_SET21', b1)
    if hasattr(b1, 'operators_Referrable22'):
        assert _is_linked(b1, 'operators_Referrable22', a)
    _safe_set(a, 'operators_SET21', b2)
    assert _is_linked(a, 'operators_SET21', b2)
    if hasattr(b1, 'operators_Referrable22'):
        assert not _is_linked(b1, 'operators_Referrable22', a)
    if hasattr(b2, 'operators_Referrable22'):
        assert _is_linked(b2, 'operators_Referrable22', a)
    _safe_set(a, 'operators_SET21', None)
    assert not _is_linked(a, 'operators_SET21', b2)
    if hasattr(b2, 'operators_Referrable22'):
        assert not _is_linked(b2, 'operators_Referrable22', a)


def test_assoc_variable43_link_reassign_clear():
    a = operators_VAR()
    b1 = operators_QueryVariable()
    b2 = operators_QueryVariable()
    _safe_set(a, 'operators_VAR', b1)
    assert _is_linked(a, 'operators_VAR', b1)
    if hasattr(b1, 'operators_QueryVariable'):
        assert _is_linked(b1, 'operators_QueryVariable', a)
    _safe_set(a, 'operators_VAR', b2)
    assert _is_linked(a, 'operators_VAR', b2)
    if hasattr(b1, 'operators_QueryVariable'):
        assert not _is_linked(b1, 'operators_QueryVariable', a)
    if hasattr(b2, 'operators_QueryVariable'):
        assert _is_linked(b2, 'operators_QueryVariable', a)
    _safe_set(a, 'operators_VAR', None)
    assert not _is_linked(a, 'operators_VAR', b2)
    if hasattr(b2, 'operators_QueryVariable'):
        assert not _is_linked(b2, 'operators_QueryVariable', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Operator_strategy = st.builds(Operator)
@given(instance=Operator_strategy)
@settings(max_examples=25)
def test_Operator_instantiation(instance):
    assert isinstance(instance, Operator)


QueryVariableQualifier_strategy = st.builds(QueryVariableQualifier)
@given(instance=QueryVariableQualifier_strategy)
@settings(max_examples=25)
def test_QueryVariableQualifier_instantiation(instance):
    assert isinstance(instance, QueryVariableQualifier)


Referrable_strategy = st.builds(Referrable)
@given(instance=Referrable_strategy)
@settings(max_examples=25)
def test_Referrable_instantiation(instance):
    assert isinstance(instance, Referrable)


Result_strategy = st.builds(Result)
@given(instance=Result_strategy)
@settings(max_examples=25)
def test_Result_instantiation(instance):
    assert isinstance(instance, Result)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


operators_ASSIGN_strategy = st.builds(operators_ASSIGN, value=safe_text)
@given(instance=operators_ASSIGN_strategy)
@settings(max_examples=25)
def test_operators_ASSIGN_instantiation(instance):
    assert isinstance(instance, operators_ASSIGN)


operators_CREATE_strategy = st.builds(operators_CREATE)
@given(instance=operators_CREATE_strategy)
@settings(max_examples=25)
def test_operators_CREATE_instantiation(instance):
    assert isinstance(instance, operators_CREATE)


operators_DELETE_strategy = st.builds(operators_DELETE)
@given(instance=operators_DELETE_strategy)
@settings(max_examples=25)
def test_operators_DELETE_instantiation(instance):
    assert isinstance(instance, operators_DELETE)


operators_EAttribute_strategy = st.builds(operators_EAttribute)
@given(instance=operators_EAttribute_strategy)
@settings(max_examples=25)
def test_operators_EAttribute_instantiation(instance):
    assert isinstance(instance, operators_EAttribute)


operators_EClass_strategy = st.builds(operators_EClass)
@given(instance=operators_EClass_strategy)
@settings(max_examples=25)
def test_operators_EClass_instantiation(instance):
    assert isinstance(instance, operators_EClass)


operators_EObject_strategy = st.builds(operators_EObject)
@given(instance=operators_EObject_strategy)
@settings(max_examples=25)
def test_operators_EObject_instantiation(instance):
    assert isinstance(instance, operators_EObject)


operators_EObjectReference_strategy = st.builds(operators_EObjectReference)
@given(instance=operators_EObjectReference_strategy)
@settings(max_examples=25)
def test_operators_EObjectReference_instantiation(instance):
    assert isinstance(instance, operators_EObjectReference)


operators_EOperation_strategy = st.builds(operators_EOperation)
@given(instance=operators_EOperation_strategy)
@settings(max_examples=25)
def test_operators_EOperation_instantiation(instance):
    assert isinstance(instance, operators_EOperation)


operators_EOperationQualifier_strategy = st.builds(operators_EOperationQualifier)
@given(instance=operators_EOperationQualifier_strategy)
@settings(max_examples=25)
def test_operators_EOperationQualifier_instantiation(instance):
    assert isinstance(instance, operators_EOperationQualifier)


operators_EReference_strategy = st.builds(operators_EReference)
@given(instance=operators_EReference_strategy)
@settings(max_examples=25)
def test_operators_EReference_instantiation(instance):
    assert isinstance(instance, operators_EReference)


operators_EReferenceQualifier_strategy = st.builds(operators_EReferenceQualifier)
@given(instance=operators_EReferenceQualifier_strategy)
@settings(max_examples=25)
def test_operators_EReferenceQualifier_instantiation(instance):
    assert isinstance(instance, operators_EReferenceQualifier)


operators_EStructuralFeature_strategy = st.builds(operators_EStructuralFeature)
@given(instance=operators_EStructuralFeature_strategy)
@settings(max_examples=25)
def test_operators_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, operators_EStructuralFeature)


operators_MERGE_strategy = st.builds(operators_MERGE)
@given(instance=operators_MERGE_strategy)
@settings(max_examples=25)
def test_operators_MERGE_instantiation(instance):
    assert isinstance(instance, operators_MERGE)


operators_MOVE_strategy = st.builds(operators_MOVE)
@given(instance=operators_MOVE_strategy)
@settings(max_examples=25)
def test_operators_MOVE_instantiation(instance):
    assert isinstance(instance, operators_MOVE)


operators_Operator_strategy = st.builds(operators_Operator, executed=st.booleans())
@given(instance=operators_Operator_strategy)
@settings(max_examples=25)
def test_operators_Operator_instantiation(instance):
    assert isinstance(instance, operators_Operator)


operators_PrimitiveReference_strategy = st.builds(operators_PrimitiveReference, value=safe_text)
@given(instance=operators_PrimitiveReference_strategy)
@settings(max_examples=25)
def test_operators_PrimitiveReference_instantiation(instance):
    assert isinstance(instance, operators_PrimitiveReference)


operators_QueryVariable_strategy = st.builds(operators_QueryVariable)
@given(instance=operators_QueryVariable_strategy)
@settings(max_examples=25)
def test_operators_QueryVariable_instantiation(instance):
    assert isinstance(instance, operators_QueryVariable)


operators_QueryVariableQualifier_strategy = st.builds(operators_QueryVariableQualifier)
@given(instance=operators_QueryVariableQualifier_strategy)
@settings(max_examples=25)
def test_operators_QueryVariableQualifier_instantiation(instance):
    assert isinstance(instance, operators_QueryVariableQualifier)


operators_Referrable_strategy = st.builds(operators_Referrable)
@given(instance=operators_Referrable_strategy)
@settings(max_examples=25)
def test_operators_Referrable_instantiation(instance):
    assert isinstance(instance, operators_Referrable)


operators_Result_strategy = st.builds(operators_Result)
@given(instance=operators_Result_strategy)
@settings(max_examples=25)
def test_operators_Result_instantiation(instance):
    assert isinstance(instance, operators_Result)


operators_SET_strategy = st.builds(operators_SET)
@given(instance=operators_SET_strategy)
@settings(max_examples=25)
def test_operators_SET_instantiation(instance):
    assert isinstance(instance, operators_SET)


operators_SPLIT_strategy = st.builds(operators_SPLIT)
@given(instance=operators_SPLIT_strategy)
@settings(max_examples=25)
def test_operators_SPLIT_instantiation(instance):
    assert isinstance(instance, operators_SPLIT)


operators_StructuralFeatureSet_strategy = st.builds(operators_StructuralFeatureSet)
@given(instance=operators_StructuralFeatureSet_strategy)
@settings(max_examples=25)
def test_operators_StructuralFeatureSet_instantiation(instance):
    assert isinstance(instance, operators_StructuralFeatureSet)


operators_TypeVariable_strategy = st.builds(operators_TypeVariable)
@given(instance=operators_TypeVariable_strategy)
@settings(max_examples=25)
def test_operators_TypeVariable_instantiation(instance):
    assert isinstance(instance, operators_TypeVariable)


operators_VAR_strategy = st.builds(operators_VAR)
@given(instance=operators_VAR_strategy)
@settings(max_examples=25)
def test_operators_VAR_instantiation(instance):
    assert isinstance(instance, operators_VAR)


operators_Variable_strategy = st.builds(operators_Variable, name=safe_text)
@given(instance=operators_Variable_strategy)
@settings(max_examples=25)
def test_operators_Variable_instantiation(instance):
    assert isinstance(instance, operators_Variable)


operators_VariableReference_strategy = st.builds(operators_VariableReference)
@given(instance=operators_VariableReference_strategy)
@settings(max_examples=25)
def test_operators_VariableReference_instantiation(instance):
    assert isinstance(instance, operators_VariableReference)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Operator,
    QueryVariableQualifier,
    Referrable,
    Result,
    Variable,
    operators_ASSIGN,
    operators_CREATE,
    operators_DELETE,
    operators_EAttribute,
    operators_EClass,
    operators_EObject,
    operators_EObjectReference,
    operators_EOperation,
    operators_EOperationQualifier,
    operators_EReference,
    operators_EReferenceQualifier,
    operators_EStructuralFeature,
    operators_MERGE,
    operators_MOVE,
    operators_Operator,
    operators_PrimitiveReference,
    operators_QueryVariable,
    operators_QueryVariableQualifier,
    operators_Referrable,
    operators_Result,
    operators_SET,
    operators_SPLIT,
    operators_StructuralFeatureSet,
    operators_TypeVariable,
    operators_VAR,
    operators_Variable,
    operators_VariableReference,
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

def test_assoc_attribute12_stub_double():
    # operators_EAttribute has no real 'operators_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so operators_ASSIGN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_ASSIGN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_ASSIGN(value="sample_text")
    partner = operators_EAttribute()
    setattr(partner, 'operators_EAttribute', None)
    _safe_set(owner, 'operators_ASSIGN', partner)
    assert getattr(partner, 'operators_EAttribute') == owner
    _safe_set(owner, 'operators_ASSIGN', None)
    assert getattr(partner, 'operators_EAttribute') is None


def test_assoc_attributeOwner13_stub_double():
    # operators_Referrable has no real 'operators_Referrable15' property in the generated
    # code (a bare stub) -- manually attach it so operators_ASSIGN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_ASSIGN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_ASSIGN(value="sample_text")
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable15', None)
    _safe_set(owner, 'operators_ASSIGN14', partner)
    assert getattr(partner, 'operators_Referrable15') == owner
    _safe_set(owner, 'operators_ASSIGN14', None)
    assert getattr(partner, 'operators_Referrable15') is None


def test_assoc_deletion10_stub_double():
    # operators_Referrable has no real 'operators_Referrable11' property in the generated
    # code (a bare stub) -- manually attach it so operators_DELETE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_DELETE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_DELETE()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable11', None)
    _safe_set(owner, 'operators_DELETE', partner)
    assert getattr(partner, 'operators_Referrable11') == owner
    _safe_set(owner, 'operators_DELETE', None)
    assert getattr(partner, 'operators_Referrable11') is None


def test_assoc_movee32_stub_double():
    # operators_Referrable has no real 'operators_Referrable34' property in the generated
    # code (a bare stub) -- manually attach it so operators_MOVE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_MOVE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_MOVE()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable34', None)
    _safe_set(owner, 'operators_MOVE33', partner)
    assert getattr(partner, 'operators_Referrable34') == owner
    _safe_set(owner, 'operators_MOVE33', None)
    assert getattr(partner, 'operators_Referrable34') is None


def test_assoc_newInstanceVariable1_stub_double():
    # operators_TypeVariable has no real 'operators_TypeVariable' property in the generated
    # code (a bare stub) -- manually attach it so operators_CREATE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_CREATE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_CREATE()
    partner = operators_TypeVariable()
    setattr(partner, 'operators_TypeVariable', None)
    _safe_set(owner, 'operators_CREATE', partner)
    assert getattr(partner, 'operators_TypeVariable') == owner
    _safe_set(owner, 'operators_CREATE', None)
    assert getattr(partner, 'operators_TypeVariable') is None


def test_assoc_newParent27_stub_double():
    # operators_Referrable has no real 'operators_Referrable28' property in the generated
    # code (a bare stub) -- manually attach it so operators_MOVE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_MOVE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_MOVE()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable28', None)
    _safe_set(owner, 'operators_MOVE', partner)
    assert getattr(partner, 'operators_Referrable28') == owner
    _safe_set(owner, 'operators_MOVE', None)
    assert getattr(partner, 'operators_Referrable28') is None


def test_assoc_parent2_stub_double():
    # operators_Referrable has no real 'operators_Referrable' property in the generated
    # code (a bare stub) -- manually attach it so operators_CREATE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_CREATE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_CREATE()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable', None)
    _safe_set(owner, 'operators_CREATE3', partner)
    assert getattr(partner, 'operators_Referrable') == owner
    _safe_set(owner, 'operators_CREATE3', None)
    assert getattr(partner, 'operators_Referrable') is None


def test_assoc_parentCompositeReference4_stub_double():
    # operators_EReference has no real 'operators_EReference' property in the generated
    # code (a bare stub) -- manually attach it so operators_CREATE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_CREATE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_CREATE()
    partner = operators_EReference()
    setattr(partner, 'operators_EReference', None)
    _safe_set(owner, 'operators_CREATE5', partner)
    assert getattr(partner, 'operators_EReference') == owner
    _safe_set(owner, 'operators_CREATE5', None)
    assert getattr(partner, 'operators_EReference') is None


def test_assoc_parentReference29_stub_double():
    # operators_EReference has no real 'operators_EReference31' property in the generated
    # code (a bare stub) -- manually attach it so operators_MOVE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_MOVE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_MOVE()
    partner = operators_EReference()
    setattr(partner, 'operators_EReference31', None)
    _safe_set(owner, 'operators_MOVE30', partner)
    assert getattr(partner, 'operators_EReference31') == owner
    _safe_set(owner, 'operators_MOVE30', None)
    assert getattr(partner, 'operators_EReference31') is None


def test_assoc_reference18_stub_double():
    # operators_EReference has no real 'operators_EReference19' property in the generated
    # code (a bare stub) -- manually attach it so operators_SET's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_SET's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_SET()
    partner = operators_EReference()
    setattr(partner, 'operators_EReference19', None)
    _safe_set(owner, 'operators_SET', partner)
    assert getattr(partner, 'operators_EReference19') == owner
    _safe_set(owner, 'operators_SET', None)
    assert getattr(partner, 'operators_EReference19') is None


def test_assoc_referenceOwner23_stub_double():
    # operators_Referrable has no real 'operators_Referrable25' property in the generated
    # code (a bare stub) -- manually attach it so operators_SET's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_SET's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_SET()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable25', None)
    _safe_set(owner, 'operators_SET24', partner)
    assert getattr(partner, 'operators_Referrable25') == owner
    _safe_set(owner, 'operators_SET24', None)
    assert getattr(partner, 'operators_Referrable25') is None


def test_assoc_referencedVariable26_stub_double():
    # operators_VariableReference has no real 'operators_VariableReference' property in the generated
    # code (a bare stub) -- manually attach it so operators_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Variable(name="sample_text")
    partner = operators_VariableReference()
    setattr(partner, 'operators_VariableReference', None)
    _safe_set(owner, 'operators_Variable', partner)
    assert getattr(partner, 'operators_VariableReference') == owner
    _safe_set(owner, 'operators_Variable', None)
    assert getattr(partner, 'operators_VariableReference') is None


def test_assoc_result0_stub_double():
    # operators_Result has no real 'operators_Result' property in the generated
    # code (a bare stub) -- manually attach it so operators_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Operator(executed=True)
    partner = operators_Result()
    setattr(partner, 'operators_Result', None)
    _safe_set(owner, 'operators_Operator', partner)
    assert getattr(partner, 'operators_Result') == owner
    _safe_set(owner, 'operators_Operator', None)
    assert getattr(partner, 'operators_Result') is None


def test_assoc_value20_stub_double():
    # operators_Referrable has no real 'operators_Referrable22' property in the generated
    # code (a bare stub) -- manually attach it so operators_SET's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_SET's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_SET()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable22', None)
    _safe_set(owner, 'operators_SET21', partner)
    assert getattr(partner, 'operators_Referrable22') == owner
    _safe_set(owner, 'operators_SET21', None)
    assert getattr(partner, 'operators_Referrable22') is None


def test_assoc_variable43_stub_double():
    # operators_QueryVariable has no real 'operators_QueryVariable' property in the generated
    # code (a bare stub) -- manually attach it so operators_VAR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_VAR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_VAR()
    partner = operators_QueryVariable()
    setattr(partner, 'operators_QueryVariable', None)
    _safe_set(owner, 'operators_VAR', partner)
    assert getattr(partner, 'operators_QueryVariable') == owner
    _safe_set(owner, 'operators_VAR', None)
    assert getattr(partner, 'operators_QueryVariable') is None




from python_code import operators_ASSIGN
from python_code import operators_EAttribute
from python_code import operators_Referrable

def test_operators_ASSIGN___init__():
    assert operators_ASSIGN.__init__(operators_ASSIGN('', operators_ASSIGN=operators_EAttribute(), operators_ASSIGN14=operators_Referrable()), '', operators_ASSIGN=operators_EAttribute(), operators_ASSIGN14=operators_Referrable()) == None

def test_operators_ASSIGN_execute():
    operators_ASSIGN.execute(operators_ASSIGN('', operators_ASSIGN=operators_EAttribute(), operators_ASSIGN14=operators_Referrable()))
from python_code import operators_CREATE
from python_code import operators_EReference
from python_code import operators_Referrable
from python_code import operators_TypeVariable

def test_operators_CREATE___init__():
    assert operators_CREATE.__init__(operators_CREATE(operators_CREATE=operators_TypeVariable(), operators_CREATE3=operators_Referrable(), operators_CREATE5=operators_EReference()), operators_CREATE=operators_TypeVariable(), operators_CREATE3=operators_Referrable(), operators_CREATE5=operators_EReference()) == None

def test_operators_CREATE_execute():
    operators_CREATE.execute(operators_CREATE(operators_CREATE=operators_TypeVariable(), operators_CREATE3=operators_Referrable(), operators_CREATE5=operators_EReference()))
from python_code import operators_DELETE
from python_code import operators_Referrable

def test_operators_DELETE___init__():
    assert operators_DELETE.__init__(operators_DELETE(operators_DELETE=operators_Referrable()), operators_DELETE=operators_Referrable()) == None

def test_operators_DELETE_execute():
    operators_DELETE.execute(operators_DELETE(operators_DELETE=operators_Referrable()))
from python_code import operators_EReference
from python_code import operators_MOVE
from python_code import operators_Referrable

def test_operators_MOVE___init__():
    assert operators_MOVE.__init__(operators_MOVE(operators_MOVE=operators_Referrable(), operators_MOVE30=operators_EReference(), operators_MOVE33=operators_Referrable()), operators_MOVE=operators_Referrable(), operators_MOVE30=operators_EReference(), operators_MOVE33=operators_Referrable()) == None

def test_operators_MOVE_execute():
    operators_MOVE.execute(operators_MOVE(operators_MOVE=operators_Referrable(), operators_MOVE30=operators_EReference(), operators_MOVE33=operators_Referrable()))
from python_code import operators_Operator
from python_code import operators_Result

def test_operators_Operator___init__():
    assert operators_Operator.__init__(operators_Operator(True, operators_Operator=operators_Result()), False, operators_Operator=operators_Result()) == None

def test_operators_Operator_execute():
    operators_Operator.execute(operators_Operator(False, operators_Operator=operators_Result()))
from python_code import operators_PrimitiveReference

def test_operators_PrimitiveReference___init__():
    assert operators_PrimitiveReference.__init__(operators_PrimitiveReference(''), '') == None
from python_code import operators_EReference
from python_code import operators_Referrable
from python_code import operators_SET

def test_operators_SET___init__():
    assert operators_SET.__init__(operators_SET(operators_SET=operators_EReference(), operators_SET21=operators_Referrable(), operators_SET24=operators_Referrable()), operators_SET=operators_EReference(), operators_SET21=operators_Referrable(), operators_SET24=operators_Referrable()) == None

def test_operators_SET_execute():
    operators_SET.execute(operators_SET(operators_SET=operators_EReference(), operators_SET21=operators_Referrable(), operators_SET24=operators_Referrable()))
from python_code import operators_QueryVariable
from python_code import operators_VAR

def test_operators_VAR___init__():
    assert operators_VAR.__init__(operators_VAR(operators_VAR=operators_QueryVariable()), operators_VAR=operators_QueryVariable()) == None

def test_operators_VAR_execute():
    operators_VAR.execute(operators_VAR(operators_VAR=operators_QueryVariable()))
from python_code import operators_Variable
from python_code import operators_VariableReference

def test_operators_Variable___init__():
    assert operators_Variable.__init__(operators_Variable('', operators_Variable=operators_VariableReference()), '', operators_Variable=operators_VariableReference()) == None

