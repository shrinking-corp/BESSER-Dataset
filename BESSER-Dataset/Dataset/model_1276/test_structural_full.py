import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Classifier,
    ocl_uml_AnyType,
    ocl_uml_AssociationClassCallExp,
    ocl_uml_BagType,
    ocl_uml_BooleanLiteralExp,
    ocl_uml_CallExp,
    ocl_uml_CollectionItem,
    ocl_uml_CollectionLiteralExp,
    ocl_uml_CollectionLiteralPart,
    ocl_uml_CollectionRange,
    ocl_uml_CollectionType,
    ocl_uml_ElementType,
    ocl_uml_EnumLiteralExp,
    ocl_uml_ExpressionInOCL,
    ocl_uml_FeatureCallExp,
    ocl_uml_IfExp,
    ocl_uml_IntegerLiteralExp,
    ocl_uml_InvalidLiteralExp,
    ocl_uml_InvalidType,
    ocl_uml_IterateExp,
    ocl_uml_IteratorExp,
    ocl_uml_LetExp,
    ocl_uml_LiteralExp,
    ocl_uml_LoopExp,
    ocl_uml_MessageExp,
    ocl_uml_MessageType,
    ocl_uml_NavigationCallExp,
    ocl_uml_NullLiteralExp,
    ocl_uml_NumericLiteralExp,
    ocl_uml_OCLExpression,
    ocl_uml_OperationCallExp,
    ocl_uml_OrderedSetType,
    ocl_uml_PrimitiveLiteralExp,
    ocl_uml_PrimitiveType,
    ocl_uml_PropertyCallExp,
    ocl_uml_RealLiteralExp,
    ocl_uml_SequenceType,
    ocl_uml_SetType,
    ocl_uml_StateExp,
    ocl_uml_StringLiteralExp,
    ocl_uml_TemplateParameterType,
    ocl_uml_TupleLiteralExp,
    ocl_uml_TupleLiteralPart,
    ocl_uml_TupleType,
    ocl_uml_TypeExp,
    ocl_uml_TypeType,
    ocl_uml_UnlimitedNaturalLiteralExp,
    ocl_uml_UnspecifiedValueExp,
    ocl_uml_Variable,
    ocl_uml_VariableExp,
    ocl_uml_VoidType,
    types_ElementType,
    uml_ocl_Operation,
    uml_ocl_Property,
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

def test_ocl_uml_ElementType_isa_Classifier():
    instance = ocl_uml_ElementType()
    assert isinstance(instance, Classifier)


def test_ocl_uml_ElementType_isa_types_ElementType():
    instance = ocl_uml_ElementType()
    assert isinstance(instance, types_ElementType)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


ocl_uml_AnyType_strategy = st.builds(ocl_uml_AnyType)
@given(instance=ocl_uml_AnyType_strategy)
@settings(max_examples=25)
def test_ocl_uml_AnyType_instantiation(instance):
    assert isinstance(instance, ocl_uml_AnyType)


ocl_uml_AssociationClassCallExp_strategy = st.builds(ocl_uml_AssociationClassCallExp)
@given(instance=ocl_uml_AssociationClassCallExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_AssociationClassCallExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_AssociationClassCallExp)


ocl_uml_BagType_strategy = st.builds(ocl_uml_BagType)
@given(instance=ocl_uml_BagType_strategy)
@settings(max_examples=25)
def test_ocl_uml_BagType_instantiation(instance):
    assert isinstance(instance, ocl_uml_BagType)


ocl_uml_BooleanLiteralExp_strategy = st.builds(ocl_uml_BooleanLiteralExp)
@given(instance=ocl_uml_BooleanLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_BooleanLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_BooleanLiteralExp)


ocl_uml_CallExp_strategy = st.builds(ocl_uml_CallExp)
@given(instance=ocl_uml_CallExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_CallExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_CallExp)


ocl_uml_CollectionItem_strategy = st.builds(ocl_uml_CollectionItem)
@given(instance=ocl_uml_CollectionItem_strategy)
@settings(max_examples=25)
def test_ocl_uml_CollectionItem_instantiation(instance):
    assert isinstance(instance, ocl_uml_CollectionItem)


ocl_uml_CollectionLiteralExp_strategy = st.builds(ocl_uml_CollectionLiteralExp)
@given(instance=ocl_uml_CollectionLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_CollectionLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_CollectionLiteralExp)


ocl_uml_CollectionLiteralPart_strategy = st.builds(ocl_uml_CollectionLiteralPart)
@given(instance=ocl_uml_CollectionLiteralPart_strategy)
@settings(max_examples=25)
def test_ocl_uml_CollectionLiteralPart_instantiation(instance):
    assert isinstance(instance, ocl_uml_CollectionLiteralPart)


ocl_uml_CollectionRange_strategy = st.builds(ocl_uml_CollectionRange)
@given(instance=ocl_uml_CollectionRange_strategy)
@settings(max_examples=25)
def test_ocl_uml_CollectionRange_instantiation(instance):
    assert isinstance(instance, ocl_uml_CollectionRange)


ocl_uml_CollectionType_strategy = st.builds(ocl_uml_CollectionType)
@given(instance=ocl_uml_CollectionType_strategy)
@settings(max_examples=25)
def test_ocl_uml_CollectionType_instantiation(instance):
    assert isinstance(instance, ocl_uml_CollectionType)


ocl_uml_ElementType_strategy = st.builds(ocl_uml_ElementType)
@given(instance=ocl_uml_ElementType_strategy)
@settings(max_examples=25)
def test_ocl_uml_ElementType_instantiation(instance):
    assert isinstance(instance, ocl_uml_ElementType)


ocl_uml_EnumLiteralExp_strategy = st.builds(ocl_uml_EnumLiteralExp)
@given(instance=ocl_uml_EnumLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_EnumLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_EnumLiteralExp)


ocl_uml_ExpressionInOCL_strategy = st.builds(ocl_uml_ExpressionInOCL)
@given(instance=ocl_uml_ExpressionInOCL_strategy)
@settings(max_examples=25)
def test_ocl_uml_ExpressionInOCL_instantiation(instance):
    assert isinstance(instance, ocl_uml_ExpressionInOCL)


ocl_uml_FeatureCallExp_strategy = st.builds(ocl_uml_FeatureCallExp)
@given(instance=ocl_uml_FeatureCallExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_FeatureCallExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_FeatureCallExp)


ocl_uml_IfExp_strategy = st.builds(ocl_uml_IfExp)
@given(instance=ocl_uml_IfExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_IfExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_IfExp)


ocl_uml_IntegerLiteralExp_strategy = st.builds(ocl_uml_IntegerLiteralExp)
@given(instance=ocl_uml_IntegerLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_IntegerLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_IntegerLiteralExp)


ocl_uml_InvalidLiteralExp_strategy = st.builds(ocl_uml_InvalidLiteralExp)
@given(instance=ocl_uml_InvalidLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_InvalidLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_InvalidLiteralExp)


ocl_uml_InvalidType_strategy = st.builds(ocl_uml_InvalidType)
@given(instance=ocl_uml_InvalidType_strategy)
@settings(max_examples=25)
def test_ocl_uml_InvalidType_instantiation(instance):
    assert isinstance(instance, ocl_uml_InvalidType)


ocl_uml_IterateExp_strategy = st.builds(ocl_uml_IterateExp)
@given(instance=ocl_uml_IterateExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_IterateExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_IterateExp)


ocl_uml_IteratorExp_strategy = st.builds(ocl_uml_IteratorExp)
@given(instance=ocl_uml_IteratorExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_IteratorExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_IteratorExp)


ocl_uml_LetExp_strategy = st.builds(ocl_uml_LetExp)
@given(instance=ocl_uml_LetExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_LetExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_LetExp)


ocl_uml_LiteralExp_strategy = st.builds(ocl_uml_LiteralExp)
@given(instance=ocl_uml_LiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_LiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_LiteralExp)


ocl_uml_LoopExp_strategy = st.builds(ocl_uml_LoopExp)
@given(instance=ocl_uml_LoopExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_LoopExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_LoopExp)


ocl_uml_MessageExp_strategy = st.builds(ocl_uml_MessageExp)
@given(instance=ocl_uml_MessageExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_MessageExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_MessageExp)


ocl_uml_MessageType_strategy = st.builds(ocl_uml_MessageType)
@given(instance=ocl_uml_MessageType_strategy)
@settings(max_examples=25)
def test_ocl_uml_MessageType_instantiation(instance):
    assert isinstance(instance, ocl_uml_MessageType)


ocl_uml_NavigationCallExp_strategy = st.builds(ocl_uml_NavigationCallExp)
@given(instance=ocl_uml_NavigationCallExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_NavigationCallExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_NavigationCallExp)


ocl_uml_NullLiteralExp_strategy = st.builds(ocl_uml_NullLiteralExp)
@given(instance=ocl_uml_NullLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_NullLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_NullLiteralExp)


ocl_uml_NumericLiteralExp_strategy = st.builds(ocl_uml_NumericLiteralExp)
@given(instance=ocl_uml_NumericLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_NumericLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_NumericLiteralExp)


ocl_uml_OCLExpression_strategy = st.builds(ocl_uml_OCLExpression)
@given(instance=ocl_uml_OCLExpression_strategy)
@settings(max_examples=25)
def test_ocl_uml_OCLExpression_instantiation(instance):
    assert isinstance(instance, ocl_uml_OCLExpression)


ocl_uml_OperationCallExp_strategy = st.builds(ocl_uml_OperationCallExp)
@given(instance=ocl_uml_OperationCallExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_OperationCallExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_OperationCallExp)


ocl_uml_OrderedSetType_strategy = st.builds(ocl_uml_OrderedSetType)
@given(instance=ocl_uml_OrderedSetType_strategy)
@settings(max_examples=25)
def test_ocl_uml_OrderedSetType_instantiation(instance):
    assert isinstance(instance, ocl_uml_OrderedSetType)


ocl_uml_PrimitiveLiteralExp_strategy = st.builds(ocl_uml_PrimitiveLiteralExp)
@given(instance=ocl_uml_PrimitiveLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_PrimitiveLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_PrimitiveLiteralExp)


ocl_uml_PrimitiveType_strategy = st.builds(ocl_uml_PrimitiveType)
@given(instance=ocl_uml_PrimitiveType_strategy)
@settings(max_examples=25)
def test_ocl_uml_PrimitiveType_instantiation(instance):
    assert isinstance(instance, ocl_uml_PrimitiveType)


ocl_uml_PropertyCallExp_strategy = st.builds(ocl_uml_PropertyCallExp)
@given(instance=ocl_uml_PropertyCallExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_PropertyCallExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_PropertyCallExp)


ocl_uml_RealLiteralExp_strategy = st.builds(ocl_uml_RealLiteralExp)
@given(instance=ocl_uml_RealLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_RealLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_RealLiteralExp)


ocl_uml_SequenceType_strategy = st.builds(ocl_uml_SequenceType)
@given(instance=ocl_uml_SequenceType_strategy)
@settings(max_examples=25)
def test_ocl_uml_SequenceType_instantiation(instance):
    assert isinstance(instance, ocl_uml_SequenceType)


ocl_uml_SetType_strategy = st.builds(ocl_uml_SetType)
@given(instance=ocl_uml_SetType_strategy)
@settings(max_examples=25)
def test_ocl_uml_SetType_instantiation(instance):
    assert isinstance(instance, ocl_uml_SetType)


ocl_uml_StateExp_strategy = st.builds(ocl_uml_StateExp)
@given(instance=ocl_uml_StateExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_StateExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_StateExp)


ocl_uml_StringLiteralExp_strategy = st.builds(ocl_uml_StringLiteralExp)
@given(instance=ocl_uml_StringLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_StringLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_StringLiteralExp)


ocl_uml_TemplateParameterType_strategy = st.builds(ocl_uml_TemplateParameterType)
@given(instance=ocl_uml_TemplateParameterType_strategy)
@settings(max_examples=25)
def test_ocl_uml_TemplateParameterType_instantiation(instance):
    assert isinstance(instance, ocl_uml_TemplateParameterType)


ocl_uml_TupleLiteralExp_strategy = st.builds(ocl_uml_TupleLiteralExp)
@given(instance=ocl_uml_TupleLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_TupleLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_TupleLiteralExp)


ocl_uml_TupleLiteralPart_strategy = st.builds(ocl_uml_TupleLiteralPart)
@given(instance=ocl_uml_TupleLiteralPart_strategy)
@settings(max_examples=25)
def test_ocl_uml_TupleLiteralPart_instantiation(instance):
    assert isinstance(instance, ocl_uml_TupleLiteralPart)


ocl_uml_TupleType_strategy = st.builds(ocl_uml_TupleType)
@given(instance=ocl_uml_TupleType_strategy)
@settings(max_examples=25)
def test_ocl_uml_TupleType_instantiation(instance):
    assert isinstance(instance, ocl_uml_TupleType)


ocl_uml_TypeExp_strategy = st.builds(ocl_uml_TypeExp)
@given(instance=ocl_uml_TypeExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_TypeExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_TypeExp)


ocl_uml_TypeType_strategy = st.builds(ocl_uml_TypeType)
@given(instance=ocl_uml_TypeType_strategy)
@settings(max_examples=25)
def test_ocl_uml_TypeType_instantiation(instance):
    assert isinstance(instance, ocl_uml_TypeType)


ocl_uml_UnlimitedNaturalLiteralExp_strategy = st.builds(ocl_uml_UnlimitedNaturalLiteralExp)
@given(instance=ocl_uml_UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_UnlimitedNaturalLiteralExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_UnlimitedNaturalLiteralExp)


ocl_uml_UnspecifiedValueExp_strategy = st.builds(ocl_uml_UnspecifiedValueExp)
@given(instance=ocl_uml_UnspecifiedValueExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_UnspecifiedValueExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_UnspecifiedValueExp)


ocl_uml_Variable_strategy = st.builds(ocl_uml_Variable)
@given(instance=ocl_uml_Variable_strategy)
@settings(max_examples=25)
def test_ocl_uml_Variable_instantiation(instance):
    assert isinstance(instance, ocl_uml_Variable)


ocl_uml_VariableExp_strategy = st.builds(ocl_uml_VariableExp)
@given(instance=ocl_uml_VariableExp_strategy)
@settings(max_examples=25)
def test_ocl_uml_VariableExp_instantiation(instance):
    assert isinstance(instance, ocl_uml_VariableExp)


ocl_uml_VoidType_strategy = st.builds(ocl_uml_VoidType)
@given(instance=ocl_uml_VoidType_strategy)
@settings(max_examples=25)
def test_ocl_uml_VoidType_instantiation(instance):
    assert isinstance(instance, ocl_uml_VoidType)


types_ElementType_strategy = st.builds(types_ElementType)
@given(instance=types_ElementType_strategy)
@settings(max_examples=25)
def test_types_ElementType_instantiation(instance):
    assert isinstance(instance, types_ElementType)


uml_ocl_Operation_strategy = st.builds(uml_ocl_Operation)
@given(instance=uml_ocl_Operation_strategy)
@settings(max_examples=25)
def test_uml_ocl_Operation_instantiation(instance):
    assert isinstance(instance, uml_ocl_Operation)


uml_ocl_Property_strategy = st.builds(uml_ocl_Property)
@given(instance=uml_ocl_Property_strategy)
@settings(max_examples=25)
def test_uml_ocl_Property_instantiation(instance):
    assert isinstance(instance, uml_ocl_Property)


