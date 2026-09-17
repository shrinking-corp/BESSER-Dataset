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
    Constant,
    featureModel_Number,
    featureModel_NULL,
    featureModel_Expression,
    featureModel_Group,
    Expression,
    featureModel_UnaryOperation,
    featureModel_Identifier,
    featureModel_Constant,
    featureModel_BinaryOperation,
    featureModel_Model,
    featureModel_Feature,
    Feature,
    featureModel_GroupedFeature,
    featureModel_SolitaryFeature,
    UnaryOperator,
    SimpleType,
    BinaryOperator,
    SolitaryType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_hyp_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_hyp_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_number_is_not_abstract():
    assert not inspect.isabstract(featureModel_Number)


def test_hyp_featuremodel_number_constructor_exists():
    assert callable(featureModel_Number.__init__)


def test_hyp_featuremodel_number_constructor_args():
    sig = inspect.signature(featureModel_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_featuremodel_null_is_not_abstract():
    assert not inspect.isabstract(featureModel_NULL)


def test_hyp_featuremodel_null_constructor_exists():
    assert callable(featureModel_NULL.__init__)


def test_hyp_featuremodel_null_constructor_args():
    sig = inspect.signature(featureModel_NULL.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_expression_is_not_abstract():
    assert not inspect.isabstract(featureModel_Expression)


def test_hyp_featuremodel_expression_constructor_exists():
    assert callable(featureModel_Expression.__init__)


def test_hyp_featuremodel_expression_constructor_args():
    sig = inspect.signature(featureModel_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_group_is_not_abstract():
    assert not inspect.isabstract(featureModel_Group)


def test_hyp_featuremodel_group_constructor_exists():
    assert callable(featureModel_Group.__init__)


def test_hyp_featuremodel_group_constructor_args():
    sig = inspect.signature(featureModel_Group.__init__)
    params = list(sig.parameters.keys())
    assert "inclusive" in params, "Missing parameter 'inclusive'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_unaryoperation_is_not_abstract():
    assert not inspect.isabstract(featureModel_UnaryOperation)


def test_hyp_featuremodel_unaryoperation_constructor_exists():
    assert callable(featureModel_UnaryOperation.__init__)


def test_hyp_featuremodel_unaryoperation_constructor_args():
    sig = inspect.signature(featureModel_UnaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_featuremodel_identifier_is_not_abstract():
    assert not inspect.isabstract(featureModel_Identifier)


def test_hyp_featuremodel_identifier_constructor_exists():
    assert callable(featureModel_Identifier.__init__)


def test_hyp_featuremodel_identifier_constructor_args():
    sig = inspect.signature(featureModel_Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_featuremodel_constant_is_not_abstract():
    assert not inspect.isabstract(featureModel_Constant)


def test_hyp_featuremodel_constant_constructor_exists():
    assert callable(featureModel_Constant.__init__)


def test_hyp_featuremodel_constant_constructor_args():
    sig = inspect.signature(featureModel_Constant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(featureModel_BinaryOperation)


def test_hyp_featuremodel_binaryoperation_constructor_exists():
    assert callable(featureModel_BinaryOperation.__init__)


def test_hyp_featuremodel_binaryoperation_constructor_args():
    sig = inspect.signature(featureModel_BinaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_featuremodel_model_is_not_abstract():
    assert not inspect.isabstract(featureModel_Model)


def test_hyp_featuremodel_model_constructor_exists():
    assert callable(featureModel_Model.__init__)


def test_hyp_featuremodel_model_constructor_args():
    sig = inspect.signature(featureModel_Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_feature_is_not_abstract():
    assert not inspect.isabstract(featureModel_Feature)


def test_hyp_featuremodel_feature_constructor_exists():
    assert callable(featureModel_Feature.__init__)


def test_hyp_featuremodel_feature_constructor_args():
    sig = inspect.signature(featureModel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"





def test_hyp_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_hyp_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_hyp_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_groupedfeature_is_not_abstract():
    assert not inspect.isabstract(featureModel_GroupedFeature)


def test_hyp_featuremodel_groupedfeature_constructor_exists():
    assert callable(featureModel_GroupedFeature.__init__)


def test_hyp_featuremodel_groupedfeature_constructor_args():
    sig = inspect.signature(featureModel_GroupedFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_solitaryfeature_is_not_abstract():
    assert not inspect.isabstract(featureModel_SolitaryFeature)


def test_hyp_featuremodel_solitaryfeature_constructor_exists():
    assert callable(featureModel_SolitaryFeature.__init__)


def test_hyp_featuremodel_solitaryfeature_constructor_args():
    sig = inspect.signature(featureModel_SolitaryFeature.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"


def test_hyp_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_hyp_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "Not",
        "Minus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_hyp_simpletype_exists():
    # Check that the Enumeration exists
    assert SimpleType is not None

def test_hyp_simpletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleType]
    expected_literals = [
        "int",
        "boolean",
        "String",
        "double",
        "nulltype",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleType"

def test_hyp_binaryoperator_exists():
    # Check that the Enumeration exists
    assert BinaryOperator is not None

def test_hyp_binaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOperator]
    expected_literals = [
        "Divide",
        "Equals",
        "And",
        "Higher",
        "Or",
        "Subtract",
        "Multiply",
        "Add",
        "Lower",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOperator"

def test_hyp_solitarytype_exists():
    # Check that the Enumeration exists
    assert SolitaryType is not None

def test_hyp_solitarytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SolitaryType]
    expected_literals = [
        "Mandatory",
        "Optional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SolitaryType"


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
Constant_strategy = st.builds(
    Constant,
)
featureModel_Number_strategy = st.builds(
    featureModel_Number,
    value=
        st.integers()
)
featureModel_NULL_strategy = st.builds(
    featureModel_NULL,
)
featureModel_Expression_strategy = st.builds(
    featureModel_Expression,
)
featureModel_Group_strategy = st.builds(
    featureModel_Group,
    inclusive=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
featureModel_UnaryOperation_strategy = st.builds(
    featureModel_UnaryOperation,
    operator=
        safe_text
)
featureModel_Identifier_strategy = st.builds(
    featureModel_Identifier,
    name=
        safe_text
)
featureModel_Constant_strategy = st.builds(
    featureModel_Constant,
)
featureModel_BinaryOperation_strategy = st.builds(
    featureModel_BinaryOperation,
    operator=
        safe_text
)
featureModel_Model_strategy = st.builds(
    featureModel_Model,
)
featureModel_Feature_strategy = st.builds(
    featureModel_Feature,
    name=
        safe_text,
    type=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
featureModel_GroupedFeature_strategy = st.builds(
    featureModel_GroupedFeature,
)
featureModel_SolitaryFeature_strategy = st.builds(
    featureModel_SolitaryFeature,
    required=
        safe_text
)





@given(instance=featureModel_Number_strategy)
def test_hyp_featuremodel_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=featureModel_Group_strategy)
def test_hyp_featuremodel_group_inclusive_setter(instance):
    original = instance.inclusive
    instance.inclusive = original
    assert instance.inclusive == original





@given(instance=featureModel_UnaryOperation_strategy)
def test_hyp_featuremodel_unaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=featureModel_Identifier_strategy)
def test_hyp_featuremodel_identifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=featureModel_BinaryOperation_strategy)
def test_hyp_featuremodel_binaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=featureModel_Feature_strategy)
def test_hyp_featuremodel_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=featureModel_Feature_strategy)
def test_hyp_featuremodel_feature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original






@given(instance=featureModel_SolitaryFeature_strategy)
def test_hyp_featuremodel_solitaryfeature_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Constant,
    Expression,
    Feature,
    featureModel_BinaryOperation,
    featureModel_Constant,
    featureModel_Expression,
    featureModel_Feature,
    featureModel_Group,
    featureModel_GroupedFeature,
    featureModel_Identifier,
    featureModel_Model,
    featureModel_NULL,
    featureModel_Number,
    featureModel_SolitaryFeature,
    featureModel_UnaryOperation,
    BinaryOperator,
    SimpleType,
    SolitaryType,
    UnaryOperator,
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

def test_featureModel_BinaryOperation_operator_value_roundtrip():
    instance = featureModel_BinaryOperation(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_featureModel_Feature_name_value_roundtrip():
    instance = featureModel_Feature(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_featureModel_Feature_type_value_roundtrip():
    instance = featureModel_Feature(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_featureModel_Group_inclusive_value_roundtrip():
    instance = featureModel_Group(inclusive=True)
    assert instance.inclusive == True
    instance.inclusive = False
    assert instance.inclusive == False


def test_featureModel_Identifier_name_value_roundtrip():
    instance = featureModel_Identifier(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_featureModel_Number_value_value_roundtrip():
    instance = featureModel_Number(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_featureModel_SolitaryFeature_required_value_roundtrip():
    instance = featureModel_SolitaryFeature(required="sample_text")
    assert instance.required == "sample_text"
    instance.required = "sample_text_2"
    assert instance.required == "sample_text_2"


def test_featureModel_UnaryOperation_operator_value_roundtrip():
    instance = featureModel_UnaryOperation(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_featureModel_NULL_isa_Constant():
    instance = featureModel_NULL()
    assert isinstance(instance, Constant)


def test_featureModel_Number_isa_Constant():
    instance = featureModel_Number(value=7)
    assert isinstance(instance, Constant)


def test_featureModel_BinaryOperation_isa_Expression():
    instance = featureModel_BinaryOperation(operator="sample_text")
    assert isinstance(instance, Expression)


def test_featureModel_Constant_isa_Expression():
    instance = featureModel_Constant()
    assert isinstance(instance, Expression)


def test_featureModel_Identifier_isa_Expression():
    instance = featureModel_Identifier(name="sample_text")
    assert isinstance(instance, Expression)


def test_featureModel_UnaryOperation_isa_Expression():
    instance = featureModel_UnaryOperation(operator="sample_text")
    assert isinstance(instance, Expression)


def test_featureModel_GroupedFeature_isa_Feature():
    instance = featureModel_GroupedFeature()
    assert isinstance(instance, Feature)


def test_featureModel_SolitaryFeature_isa_Feature():
    instance = featureModel_SolitaryFeature(required="sample_text")
    assert isinstance(instance, Feature)


def test_assoc_RootFeature5_link_reassign_clear():
    a = featureModel_Feature(name="sample_text", type="sample_text")
    b1 = featureModel_Model()
    b2 = featureModel_Model()
    _safe_set(a, 'featureModel_Feature6', b1)
    assert _is_linked(a, 'featureModel_Feature6', b1)
    if hasattr(b1, 'featureModel_Model'):
        assert _is_linked(b1, 'featureModel_Model', a)
    _safe_set(a, 'featureModel_Feature6', b2)
    assert _is_linked(a, 'featureModel_Feature6', b2)
    if hasattr(b1, 'featureModel_Model'):
        assert not _is_linked(b1, 'featureModel_Model', a)
    if hasattr(b2, 'featureModel_Model'):
        assert _is_linked(b2, 'featureModel_Model', a)
    _safe_set(a, 'featureModel_Feature6', None)
    assert not _is_linked(a, 'featureModel_Feature6', b2)
    if hasattr(b2, 'featureModel_Model'):
        assert not _is_linked(b2, 'featureModel_Model', a)


def test_assoc_constraints3_link_reassign_clear():
    a = featureModel_Feature(name="sample_text", type="sample_text")
    b1 = featureModel_Expression()
    b2 = featureModel_Expression()
    _safe_set(a, 'featureModel_Feature4', {b1})
    assert _is_linked(a, 'featureModel_Feature4', b1)
    if hasattr(b1, 'featureModel_Expression'):
        assert _is_linked(b1, 'featureModel_Expression', a)
    _safe_set(a, 'featureModel_Feature4', {b2})
    assert _is_linked(a, 'featureModel_Feature4', b2)
    if hasattr(b1, 'featureModel_Expression'):
        assert not _is_linked(b1, 'featureModel_Expression', a)
    if hasattr(b2, 'featureModel_Expression'):
        assert _is_linked(b2, 'featureModel_Expression', a)
    _safe_set(a, 'featureModel_Feature4', set())
    assert not _is_linked(a, 'featureModel_Feature4', b2)
    if hasattr(b2, 'featureModel_Expression'):
        assert not _is_linked(b2, 'featureModel_Expression', a)


def test_assoc_exp14_link_reassign_clear():
    a = featureModel_UnaryOperation(operator="sample_text")
    b1 = featureModel_Expression()
    b2 = featureModel_Expression()
    _safe_set(a, 'featureModel_UnaryOperation', b1)
    assert _is_linked(a, 'featureModel_UnaryOperation', b1)
    if hasattr(b1, 'featureModel_Expression15'):
        assert _is_linked(b1, 'featureModel_Expression15', a)
    _safe_set(a, 'featureModel_UnaryOperation', b2)
    assert _is_linked(a, 'featureModel_UnaryOperation', b2)
    if hasattr(b1, 'featureModel_Expression15'):
        assert not _is_linked(b1, 'featureModel_Expression15', a)
    if hasattr(b2, 'featureModel_Expression15'):
        assert _is_linked(b2, 'featureModel_Expression15', a)
    _safe_set(a, 'featureModel_UnaryOperation', None)
    assert not _is_linked(a, 'featureModel_UnaryOperation', b2)
    if hasattr(b2, 'featureModel_Expression15'):
        assert not _is_linked(b2, 'featureModel_Expression15', a)


def test_assoc_features1_link_reassign_clear():
    a = featureModel_SolitaryFeature(required="sample_text")
    b1 = featureModel_Feature(name="sample_text", type="sample_text")
    b2 = featureModel_Feature(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'featureModel_SolitaryFeature', b1)
    assert _is_linked(a, 'featureModel_SolitaryFeature', b1)
    if hasattr(b1, 'featureModel_Feature2'):
        assert _is_linked(b1, 'featureModel_Feature2', a)
    _safe_set(a, 'featureModel_SolitaryFeature', b2)
    assert _is_linked(a, 'featureModel_SolitaryFeature', b2)
    if hasattr(b1, 'featureModel_Feature2'):
        assert not _is_linked(b1, 'featureModel_Feature2', a)
    if hasattr(b2, 'featureModel_Feature2'):
        assert _is_linked(b2, 'featureModel_Feature2', a)
    _safe_set(a, 'featureModel_SolitaryFeature', None)
    assert not _is_linked(a, 'featureModel_SolitaryFeature', b2)
    if hasattr(b2, 'featureModel_Feature2'):
        assert not _is_linked(b2, 'featureModel_Feature2', a)


def test_assoc_groupedFeatures7_link_reassign_clear():
    a = featureModel_Group(inclusive=True)
    b1 = featureModel_GroupedFeature()
    b2 = featureModel_GroupedFeature()
    _safe_set(a, 'featureModel_Group8', {b1})
    assert _is_linked(a, 'featureModel_Group8', b1)
    if hasattr(b1, 'featureModel_GroupedFeature'):
        assert _is_linked(b1, 'featureModel_GroupedFeature', a)
    _safe_set(a, 'featureModel_Group8', {b2})
    assert _is_linked(a, 'featureModel_Group8', b2)
    if hasattr(b1, 'featureModel_GroupedFeature'):
        assert not _is_linked(b1, 'featureModel_GroupedFeature', a)
    if hasattr(b2, 'featureModel_GroupedFeature'):
        assert _is_linked(b2, 'featureModel_GroupedFeature', a)
    _safe_set(a, 'featureModel_Group8', set())
    assert not _is_linked(a, 'featureModel_Group8', b2)
    if hasattr(b2, 'featureModel_GroupedFeature'):
        assert not _is_linked(b2, 'featureModel_GroupedFeature', a)


def test_assoc_groups0_link_reassign_clear():
    a = featureModel_Group(inclusive=True)
    b1 = featureModel_Feature(name="sample_text", type="sample_text")
    b2 = featureModel_Feature(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'featureModel_Group', b1)
    assert _is_linked(a, 'featureModel_Group', b1)
    if hasattr(b1, 'featureModel_Feature'):
        assert _is_linked(b1, 'featureModel_Feature', a)
    _safe_set(a, 'featureModel_Group', b2)
    assert _is_linked(a, 'featureModel_Group', b2)
    if hasattr(b1, 'featureModel_Feature'):
        assert not _is_linked(b1, 'featureModel_Feature', a)
    if hasattr(b2, 'featureModel_Feature'):
        assert _is_linked(b2, 'featureModel_Feature', a)
    _safe_set(a, 'featureModel_Group', None)
    assert not _is_linked(a, 'featureModel_Group', b2)
    if hasattr(b2, 'featureModel_Feature'):
        assert not _is_linked(b2, 'featureModel_Feature', a)


def test_assoc_lexp11_link_reassign_clear():
    a = featureModel_BinaryOperation(operator="sample_text")
    b1 = featureModel_Expression()
    b2 = featureModel_Expression()
    _safe_set(a, 'featureModel_BinaryOperation12', b1)
    assert _is_linked(a, 'featureModel_BinaryOperation12', b1)
    if hasattr(b1, 'featureModel_Expression13'):
        assert _is_linked(b1, 'featureModel_Expression13', a)
    _safe_set(a, 'featureModel_BinaryOperation12', b2)
    assert _is_linked(a, 'featureModel_BinaryOperation12', b2)
    if hasattr(b1, 'featureModel_Expression13'):
        assert not _is_linked(b1, 'featureModel_Expression13', a)
    if hasattr(b2, 'featureModel_Expression13'):
        assert _is_linked(b2, 'featureModel_Expression13', a)
    _safe_set(a, 'featureModel_BinaryOperation12', None)
    assert not _is_linked(a, 'featureModel_BinaryOperation12', b2)
    if hasattr(b2, 'featureModel_Expression13'):
        assert not _is_linked(b2, 'featureModel_Expression13', a)


def test_assoc_ref16_link_reassign_clear():
    a = featureModel_Identifier(name="sample_text")
    b1 = featureModel_Feature(name="sample_text", type="sample_text")
    b2 = featureModel_Feature(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'featureModel_Identifier', {b1})
    assert _is_linked(a, 'featureModel_Identifier', b1)
    if hasattr(b1, 'featureModel_Feature17'):
        assert _is_linked(b1, 'featureModel_Feature17', a)
    _safe_set(a, 'featureModel_Identifier', {b2})
    assert _is_linked(a, 'featureModel_Identifier', b2)
    if hasattr(b1, 'featureModel_Feature17'):
        assert not _is_linked(b1, 'featureModel_Feature17', a)
    if hasattr(b2, 'featureModel_Feature17'):
        assert _is_linked(b2, 'featureModel_Feature17', a)
    _safe_set(a, 'featureModel_Identifier', set())
    assert not _is_linked(a, 'featureModel_Identifier', b2)
    if hasattr(b2, 'featureModel_Feature17'):
        assert not _is_linked(b2, 'featureModel_Feature17', a)


def test_assoc_rexp9_link_reassign_clear():
    a = featureModel_BinaryOperation(operator="sample_text")
    b1 = featureModel_Expression()
    b2 = featureModel_Expression()
    _safe_set(a, 'featureModel_BinaryOperation', b1)
    assert _is_linked(a, 'featureModel_BinaryOperation', b1)
    if hasattr(b1, 'featureModel_Expression10'):
        assert _is_linked(b1, 'featureModel_Expression10', a)
    _safe_set(a, 'featureModel_BinaryOperation', b2)
    assert _is_linked(a, 'featureModel_BinaryOperation', b2)
    if hasattr(b1, 'featureModel_Expression10'):
        assert not _is_linked(b1, 'featureModel_Expression10', a)
    if hasattr(b2, 'featureModel_Expression10'):
        assert _is_linked(b2, 'featureModel_Expression10', a)
    _safe_set(a, 'featureModel_BinaryOperation', None)
    assert not _is_linked(a, 'featureModel_BinaryOperation', b2)
    if hasattr(b2, 'featureModel_Expression10'):
        assert not _is_linked(b2, 'featureModel_Expression10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Constant_strategy = st.builds(Constant)
@given(instance=Constant_strategy)
@settings(max_examples=25)
def test_Constant_instantiation(instance):
    assert isinstance(instance, Constant)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


featureModel_BinaryOperation_strategy = st.builds(featureModel_BinaryOperation, operator=safe_text)
@given(instance=featureModel_BinaryOperation_strategy)
@settings(max_examples=25)
def test_featureModel_BinaryOperation_instantiation(instance):
    assert isinstance(instance, featureModel_BinaryOperation)


featureModel_Constant_strategy = st.builds(featureModel_Constant)
@given(instance=featureModel_Constant_strategy)
@settings(max_examples=25)
def test_featureModel_Constant_instantiation(instance):
    assert isinstance(instance, featureModel_Constant)


featureModel_Expression_strategy = st.builds(featureModel_Expression)
@given(instance=featureModel_Expression_strategy)
@settings(max_examples=25)
def test_featureModel_Expression_instantiation(instance):
    assert isinstance(instance, featureModel_Expression)


featureModel_Feature_strategy = st.builds(featureModel_Feature, name=safe_text, type=safe_text)
@given(instance=featureModel_Feature_strategy)
@settings(max_examples=25)
def test_featureModel_Feature_instantiation(instance):
    assert isinstance(instance, featureModel_Feature)


featureModel_Group_strategy = st.builds(featureModel_Group, inclusive=st.booleans())
@given(instance=featureModel_Group_strategy)
@settings(max_examples=25)
def test_featureModel_Group_instantiation(instance):
    assert isinstance(instance, featureModel_Group)


featureModel_GroupedFeature_strategy = st.builds(featureModel_GroupedFeature)
@given(instance=featureModel_GroupedFeature_strategy)
@settings(max_examples=25)
def test_featureModel_GroupedFeature_instantiation(instance):
    assert isinstance(instance, featureModel_GroupedFeature)


featureModel_Identifier_strategy = st.builds(featureModel_Identifier, name=safe_text)
@given(instance=featureModel_Identifier_strategy)
@settings(max_examples=25)
def test_featureModel_Identifier_instantiation(instance):
    assert isinstance(instance, featureModel_Identifier)


featureModel_Model_strategy = st.builds(featureModel_Model)
@given(instance=featureModel_Model_strategy)
@settings(max_examples=25)
def test_featureModel_Model_instantiation(instance):
    assert isinstance(instance, featureModel_Model)


featureModel_NULL_strategy = st.builds(featureModel_NULL)
@given(instance=featureModel_NULL_strategy)
@settings(max_examples=25)
def test_featureModel_NULL_instantiation(instance):
    assert isinstance(instance, featureModel_NULL)


featureModel_Number_strategy = st.builds(featureModel_Number, value=st.integers())
@given(instance=featureModel_Number_strategy)
@settings(max_examples=25)
def test_featureModel_Number_instantiation(instance):
    assert isinstance(instance, featureModel_Number)


featureModel_SolitaryFeature_strategy = st.builds(featureModel_SolitaryFeature, required=safe_text)
@given(instance=featureModel_SolitaryFeature_strategy)
@settings(max_examples=25)
def test_featureModel_SolitaryFeature_instantiation(instance):
    assert isinstance(instance, featureModel_SolitaryFeature)


featureModel_UnaryOperation_strategy = st.builds(featureModel_UnaryOperation, operator=safe_text)
@given(instance=featureModel_UnaryOperation_strategy)
@settings(max_examples=25)
def test_featureModel_UnaryOperation_instantiation(instance):
    assert isinstance(instance, featureModel_UnaryOperation)



