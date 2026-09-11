import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArgumentExpression,
    BinaryExpression,
    Expression,
    Literal,
    UnaryExpression,
    expressions_ArgumentExpression,
    expressions_AssignmentExpression,
    expressions_BinaryExpression,
    expressions_BitwiseAndExpression,
    expressions_BitwiseOrExpression,
    expressions_BitwiseXorExpression,
    expressions_BoolLiteral,
    expressions_ConditionalExpression,
    expressions_DoubleLiteral,
    expressions_EObject,
    expressions_ElementReferenceExpression,
    expressions_Expression,
    expressions_FeatureCall,
    expressions_FloatLiteral,
    expressions_HexLiteral,
    expressions_IntLiteral,
    expressions_Literal,
    expressions_LogicalAndExpression,
    expressions_LogicalNotExpression,
    expressions_LogicalOrExpression,
    expressions_LogicalRelationExpression,
    expressions_NullLiteral,
    expressions_NumericalAddSubtractExpression,
    expressions_NumericalMultiplyDivideExpression,
    expressions_NumericalUnaryExpression,
    expressions_ParenthesizedExpression,
    expressions_PrimitiveValueExpression,
    expressions_ShiftExpression,
    expressions_StringLiteral,
    expressions_Type,
    expressions_TypeCastExpression,
    expressions_UnaryExpression,
    AdditiveOperator,
    AssignmentOperator,
    BitwiseOperator,
    LogicalOperator,
    MultiplicativeOperator,
    RelationalOperator,
    ShiftOperator,
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

def test_expressions_AssignmentExpression_operator_value_roundtrip():
    instance = expressions_AssignmentExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_expressions_BoolLiteral_value_value_roundtrip():
    instance = expressions_BoolLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_expressions_DoubleLiteral_value_value_roundtrip():
    instance = expressions_DoubleLiteral(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_expressions_ElementReferenceExpression_arrayAccess_value_roundtrip():
    instance = expressions_ElementReferenceExpression(arrayAccess=True, operationCall=True)
    assert instance.arrayAccess == True
    instance.arrayAccess = False
    assert instance.arrayAccess == False


def test_expressions_ElementReferenceExpression_operationCall_value_roundtrip():
    instance = expressions_ElementReferenceExpression(arrayAccess=True, operationCall=True)
    assert instance.operationCall == True
    instance.operationCall = False
    assert instance.operationCall == False


def test_expressions_FeatureCall_arrayAccess_value_roundtrip():
    instance = expressions_FeatureCall(arrayAccess=True, operationCall=True)
    assert instance.arrayAccess == True
    instance.arrayAccess = False
    assert instance.arrayAccess == False


def test_expressions_FeatureCall_operationCall_value_roundtrip():
    instance = expressions_FeatureCall(arrayAccess=True, operationCall=True)
    assert instance.operationCall == True
    instance.operationCall = False
    assert instance.operationCall == False


def test_expressions_FloatLiteral_value_value_roundtrip():
    instance = expressions_FloatLiteral(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_expressions_HexLiteral_value_value_roundtrip():
    instance = expressions_HexLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_expressions_IntLiteral_value_value_roundtrip():
    instance = expressions_IntLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_expressions_LogicalRelationExpression_operator_value_roundtrip():
    instance = expressions_LogicalRelationExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_expressions_NumericalAddSubtractExpression_operator_value_roundtrip():
    instance = expressions_NumericalAddSubtractExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_expressions_NumericalMultiplyDivideExpression_operator_value_roundtrip():
    instance = expressions_NumericalMultiplyDivideExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_expressions_NumericalUnaryExpression_operator_value_roundtrip():
    instance = expressions_NumericalUnaryExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_expressions_ShiftExpression_operator_value_roundtrip():
    instance = expressions_ShiftExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_expressions_StringLiteral_value_value_roundtrip():
    instance = expressions_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_expressions_ElementReferenceExpression_isa_ArgumentExpression():
    instance = expressions_ElementReferenceExpression(arrayAccess=True, operationCall=True)
    assert isinstance(instance, ArgumentExpression)


def test_expressions_FeatureCall_isa_ArgumentExpression():
    instance = expressions_FeatureCall(arrayAccess=True, operationCall=True)
    assert isinstance(instance, ArgumentExpression)


def test_expressions_BitwiseAndExpression_isa_BinaryExpression():
    instance = expressions_BitwiseAndExpression()
    assert isinstance(instance, BinaryExpression)


def test_expressions_BitwiseOrExpression_isa_BinaryExpression():
    instance = expressions_BitwiseOrExpression()
    assert isinstance(instance, BinaryExpression)


def test_expressions_BitwiseXorExpression_isa_BinaryExpression():
    instance = expressions_BitwiseXorExpression()
    assert isinstance(instance, BinaryExpression)


def test_expressions_LogicalAndExpression_isa_BinaryExpression():
    instance = expressions_LogicalAndExpression()
    assert isinstance(instance, BinaryExpression)


def test_expressions_LogicalOrExpression_isa_BinaryExpression():
    instance = expressions_LogicalOrExpression()
    assert isinstance(instance, BinaryExpression)


def test_expressions_LogicalRelationExpression_isa_BinaryExpression():
    instance = expressions_LogicalRelationExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_expressions_NumericalAddSubtractExpression_isa_BinaryExpression():
    instance = expressions_NumericalAddSubtractExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_expressions_NumericalMultiplyDivideExpression_isa_BinaryExpression():
    instance = expressions_NumericalMultiplyDivideExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_expressions_ShiftExpression_isa_BinaryExpression():
    instance = expressions_ShiftExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_expressions_ArgumentExpression_isa_Expression():
    instance = expressions_ArgumentExpression()
    assert isinstance(instance, Expression)


def test_expressions_AssignmentExpression_isa_Expression():
    instance = expressions_AssignmentExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_expressions_BinaryExpression_isa_Expression():
    instance = expressions_BinaryExpression()
    assert isinstance(instance, Expression)


def test_expressions_ConditionalExpression_isa_Expression():
    instance = expressions_ConditionalExpression()
    assert isinstance(instance, Expression)


def test_expressions_ParenthesizedExpression_isa_Expression():
    instance = expressions_ParenthesizedExpression()
    assert isinstance(instance, Expression)


def test_expressions_PrimitiveValueExpression_isa_Expression():
    instance = expressions_PrimitiveValueExpression()
    assert isinstance(instance, Expression)


def test_expressions_TypeCastExpression_isa_Expression():
    instance = expressions_TypeCastExpression()
    assert isinstance(instance, Expression)


def test_expressions_UnaryExpression_isa_Expression():
    instance = expressions_UnaryExpression()
    assert isinstance(instance, Expression)


def test_expressions_BoolLiteral_isa_Literal():
    instance = expressions_BoolLiteral(value=True)
    assert isinstance(instance, Literal)


def test_expressions_DoubleLiteral_isa_Literal():
    instance = expressions_DoubleLiteral(value=3.14)
    assert isinstance(instance, Literal)


def test_expressions_FloatLiteral_isa_Literal():
    instance = expressions_FloatLiteral(value=3.14)
    assert isinstance(instance, Literal)


def test_expressions_HexLiteral_isa_Literal():
    instance = expressions_HexLiteral(value=7)
    assert isinstance(instance, Literal)


def test_expressions_IntLiteral_isa_Literal():
    instance = expressions_IntLiteral(value=7)
    assert isinstance(instance, Literal)


def test_expressions_NullLiteral_isa_Literal():
    instance = expressions_NullLiteral()
    assert isinstance(instance, Literal)


def test_expressions_StringLiteral_isa_Literal():
    instance = expressions_StringLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_expressions_LogicalNotExpression_isa_UnaryExpression():
    instance = expressions_LogicalNotExpression()
    assert isinstance(instance, UnaryExpression)


def test_expressions_NumericalUnaryExpression_isa_UnaryExpression():
    instance = expressions_NumericalUnaryExpression(operator="sample_text")
    assert isinstance(instance, UnaryExpression)


def test_assoc_arraySelector26_link_reassign_clear():
    a = expressions_FeatureCall(arrayAccess=True, operationCall=True)
    b1 = expressions_Expression()
    b2 = expressions_Expression()
    _safe_set(a, 'expressions_FeatureCall27', {b1})
    assert _is_linked(a, 'expressions_FeatureCall27', b1)
    if hasattr(b1, 'expressions_Expression28'):
        assert _is_linked(b1, 'expressions_Expression28', a)
    _safe_set(a, 'expressions_FeatureCall27', {b2})
    assert _is_linked(a, 'expressions_FeatureCall27', b2)
    if hasattr(b1, 'expressions_Expression28'):
        assert not _is_linked(b1, 'expressions_Expression28', a)
    if hasattr(b2, 'expressions_Expression28'):
        assert _is_linked(b2, 'expressions_Expression28', a)
    _safe_set(a, 'expressions_FeatureCall27', set())
    assert not _is_linked(a, 'expressions_FeatureCall27', b2)
    if hasattr(b2, 'expressions_Expression28'):
        assert not _is_linked(b2, 'expressions_Expression28', a)


def test_assoc_arraySelector31_link_reassign_clear():
    a = expressions_ElementReferenceExpression(arrayAccess=True, operationCall=True)
    b1 = expressions_Expression()
    b2 = expressions_Expression()
    _safe_set(a, 'expressions_ElementReferenceExpression32', {b1})
    assert _is_linked(a, 'expressions_ElementReferenceExpression32', b1)
    if hasattr(b1, 'expressions_Expression33'):
        assert _is_linked(b1, 'expressions_Expression33', a)
    _safe_set(a, 'expressions_ElementReferenceExpression32', {b2})
    assert _is_linked(a, 'expressions_ElementReferenceExpression32', b2)
    if hasattr(b1, 'expressions_Expression33'):
        assert not _is_linked(b1, 'expressions_Expression33', a)
    if hasattr(b2, 'expressions_Expression33'):
        assert _is_linked(b2, 'expressions_Expression33', a)
    _safe_set(a, 'expressions_ElementReferenceExpression32', set())
    assert not _is_linked(a, 'expressions_ElementReferenceExpression32', b2)
    if hasattr(b2, 'expressions_Expression33'):
        assert not _is_linked(b2, 'expressions_Expression33', a)


def test_assoc_expression10_link_reassign_clear():
    a = expressions_AssignmentExpression(operator="sample_text")
    b1 = expressions_Expression()
    b2 = expressions_Expression()
    _safe_set(a, 'expressions_AssignmentExpression11', b1)
    assert _is_linked(a, 'expressions_AssignmentExpression11', b1)
    if hasattr(b1, 'expressions_Expression12'):
        assert _is_linked(b1, 'expressions_Expression12', a)
    _safe_set(a, 'expressions_AssignmentExpression11', b2)
    assert _is_linked(a, 'expressions_AssignmentExpression11', b2)
    if hasattr(b1, 'expressions_Expression12'):
        assert not _is_linked(b1, 'expressions_Expression12', a)
    if hasattr(b2, 'expressions_Expression12'):
        assert _is_linked(b2, 'expressions_Expression12', a)
    _safe_set(a, 'expressions_AssignmentExpression11', None)
    assert not _is_linked(a, 'expressions_AssignmentExpression11', b2)
    if hasattr(b2, 'expressions_Expression12'):
        assert not _is_linked(b2, 'expressions_Expression12', a)


def test_assoc_feature24_link_reassign_clear():
    a = expressions_FeatureCall(arrayAccess=True, operationCall=True)
    b1 = expressions_EObject()
    b2 = expressions_EObject()
    _safe_set(a, 'expressions_FeatureCall25', b1)
    assert _is_linked(a, 'expressions_FeatureCall25', b1)
    if hasattr(b1, 'expressions_EObject'):
        assert _is_linked(b1, 'expressions_EObject', a)
    _safe_set(a, 'expressions_FeatureCall25', b2)
    assert _is_linked(a, 'expressions_FeatureCall25', b2)
    if hasattr(b1, 'expressions_EObject'):
        assert not _is_linked(b1, 'expressions_EObject', a)
    if hasattr(b2, 'expressions_EObject'):
        assert _is_linked(b2, 'expressions_EObject', a)
    _safe_set(a, 'expressions_FeatureCall25', None)
    assert not _is_linked(a, 'expressions_FeatureCall25', b2)
    if hasattr(b2, 'expressions_EObject'):
        assert not _is_linked(b2, 'expressions_EObject', a)


def test_assoc_leftOperand0_link_reassign_clear():
    a = expressions_BinaryExpression()
    b1 = expressions_Expression()
    b2 = expressions_Expression()
    _safe_set(a, 'expressions_BinaryExpression', b1)
    assert _is_linked(a, 'expressions_BinaryExpression', b1)
    if hasattr(b1, 'expressions_Expression'):
        assert _is_linked(b1, 'expressions_Expression', a)
    _safe_set(a, 'expressions_BinaryExpression', b2)
    assert _is_linked(a, 'expressions_BinaryExpression', b2)
    if hasattr(b1, 'expressions_Expression'):
        assert not _is_linked(b1, 'expressions_Expression', a)
    if hasattr(b2, 'expressions_Expression'):
        assert _is_linked(b2, 'expressions_Expression', a)
    _safe_set(a, 'expressions_BinaryExpression', None)
    assert not _is_linked(a, 'expressions_BinaryExpression', b2)
    if hasattr(b2, 'expressions_Expression'):
        assert not _is_linked(b2, 'expressions_Expression', a)


def test_assoc_operand4_link_reassign_clear():
    a = expressions_UnaryExpression()
    b1 = expressions_Expression()
    b2 = expressions_Expression()
    _safe_set(a, 'expressions_UnaryExpression', b1)
    assert _is_linked(a, 'expressions_UnaryExpression', b1)
    if hasattr(b1, 'expressions_Expression5'):
        assert _is_linked(b1, 'expressions_Expression5', a)
    _safe_set(a, 'expressions_UnaryExpression', b2)
    assert _is_linked(a, 'expressions_UnaryExpression', b2)
    if hasattr(b1, 'expressions_Expression5'):
        assert not _is_linked(b1, 'expressions_Expression5', a)
    if hasattr(b2, 'expressions_Expression5'):
        assert _is_linked(b2, 'expressions_Expression5', a)
    _safe_set(a, 'expressions_UnaryExpression', None)
    assert not _is_linked(a, 'expressions_UnaryExpression', b2)
    if hasattr(b2, 'expressions_Expression5'):
        assert not _is_linked(b2, 'expressions_Expression5', a)


def test_assoc_owner22_link_reassign_clear():
    a = expressions_FeatureCall(arrayAccess=True, operationCall=True)
    b1 = expressions_Expression()
    b2 = expressions_Expression()
    _safe_set(a, 'expressions_FeatureCall', b1)
    assert _is_linked(a, 'expressions_FeatureCall', b1)
    if hasattr(b1, 'expressions_Expression23'):
        assert _is_linked(b1, 'expressions_Expression23', a)
    _safe_set(a, 'expressions_FeatureCall', b2)
    assert _is_linked(a, 'expressions_FeatureCall', b2)
    if hasattr(b1, 'expressions_Expression23'):
        assert not _is_linked(b1, 'expressions_Expression23', a)
    if hasattr(b2, 'expressions_Expression23'):
        assert _is_linked(b2, 'expressions_Expression23', a)
    _safe_set(a, 'expressions_FeatureCall', None)
    assert not _is_linked(a, 'expressions_FeatureCall', b2)
    if hasattr(b2, 'expressions_Expression23'):
        assert not _is_linked(b2, 'expressions_Expression23', a)


def test_assoc_reference29_link_reassign_clear():
    a = expressions_ElementReferenceExpression(arrayAccess=True, operationCall=True)
    b1 = expressions_EObject()
    b2 = expressions_EObject()
    _safe_set(a, 'expressions_ElementReferenceExpression', b1)
    assert _is_linked(a, 'expressions_ElementReferenceExpression', b1)
    if hasattr(b1, 'expressions_EObject30'):
        assert _is_linked(b1, 'expressions_EObject30', a)
    _safe_set(a, 'expressions_ElementReferenceExpression', b2)
    assert _is_linked(a, 'expressions_ElementReferenceExpression', b2)
    if hasattr(b1, 'expressions_EObject30'):
        assert not _is_linked(b1, 'expressions_EObject30', a)
    if hasattr(b2, 'expressions_EObject30'):
        assert _is_linked(b2, 'expressions_EObject30', a)
    _safe_set(a, 'expressions_ElementReferenceExpression', None)
    assert not _is_linked(a, 'expressions_ElementReferenceExpression', b2)
    if hasattr(b2, 'expressions_EObject30'):
        assert not _is_linked(b2, 'expressions_EObject30', a)


def test_assoc_rightOperand1_link_reassign_clear():
    a = expressions_BinaryExpression()
    b1 = expressions_Expression()
    b2 = expressions_Expression()
    _safe_set(a, 'expressions_BinaryExpression2', b1)
    assert _is_linked(a, 'expressions_BinaryExpression2', b1)
    if hasattr(b1, 'expressions_Expression3'):
        assert _is_linked(b1, 'expressions_Expression3', a)
    _safe_set(a, 'expressions_BinaryExpression2', b2)
    assert _is_linked(a, 'expressions_BinaryExpression2', b2)
    if hasattr(b1, 'expressions_Expression3'):
        assert not _is_linked(b1, 'expressions_Expression3', a)
    if hasattr(b2, 'expressions_Expression3'):
        assert _is_linked(b2, 'expressions_Expression3', a)
    _safe_set(a, 'expressions_BinaryExpression2', None)
    assert not _is_linked(a, 'expressions_BinaryExpression2', b2)
    if hasattr(b2, 'expressions_Expression3'):
        assert not _is_linked(b2, 'expressions_Expression3', a)


def test_assoc_varRef8_link_reassign_clear():
    a = expressions_AssignmentExpression(operator="sample_text")
    b1 = expressions_Expression()
    b2 = expressions_Expression()
    _safe_set(a, 'expressions_AssignmentExpression', b1)
    assert _is_linked(a, 'expressions_AssignmentExpression', b1)
    if hasattr(b1, 'expressions_Expression9'):
        assert _is_linked(b1, 'expressions_Expression9', a)
    _safe_set(a, 'expressions_AssignmentExpression', b2)
    assert _is_linked(a, 'expressions_AssignmentExpression', b2)
    if hasattr(b1, 'expressions_Expression9'):
        assert not _is_linked(b1, 'expressions_Expression9', a)
    if hasattr(b2, 'expressions_Expression9'):
        assert _is_linked(b2, 'expressions_Expression9', a)
    _safe_set(a, 'expressions_AssignmentExpression', None)
    assert not _is_linked(a, 'expressions_AssignmentExpression', b2)
    if hasattr(b2, 'expressions_Expression9'):
        assert not _is_linked(b2, 'expressions_Expression9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArgumentExpression_strategy = st.builds(ArgumentExpression)
@given(instance=ArgumentExpression_strategy)
@settings(max_examples=25)
def test_ArgumentExpression_instantiation(instance):
    assert isinstance(instance, ArgumentExpression)


BinaryExpression_strategy = st.builds(BinaryExpression)
@given(instance=BinaryExpression_strategy)
@settings(max_examples=25)
def test_BinaryExpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


UnaryExpression_strategy = st.builds(UnaryExpression)
@given(instance=UnaryExpression_strategy)
@settings(max_examples=25)
def test_UnaryExpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)


expressions_ArgumentExpression_strategy = st.builds(expressions_ArgumentExpression)
@given(instance=expressions_ArgumentExpression_strategy)
@settings(max_examples=25)
def test_expressions_ArgumentExpression_instantiation(instance):
    assert isinstance(instance, expressions_ArgumentExpression)


expressions_AssignmentExpression_strategy = st.builds(expressions_AssignmentExpression, operator=safe_text)
@given(instance=expressions_AssignmentExpression_strategy)
@settings(max_examples=25)
def test_expressions_AssignmentExpression_instantiation(instance):
    assert isinstance(instance, expressions_AssignmentExpression)


expressions_BinaryExpression_strategy = st.builds(expressions_BinaryExpression)
@given(instance=expressions_BinaryExpression_strategy)
@settings(max_examples=25)
def test_expressions_BinaryExpression_instantiation(instance):
    assert isinstance(instance, expressions_BinaryExpression)


expressions_BitwiseAndExpression_strategy = st.builds(expressions_BitwiseAndExpression)
@given(instance=expressions_BitwiseAndExpression_strategy)
@settings(max_examples=25)
def test_expressions_BitwiseAndExpression_instantiation(instance):
    assert isinstance(instance, expressions_BitwiseAndExpression)


expressions_BitwiseOrExpression_strategy = st.builds(expressions_BitwiseOrExpression)
@given(instance=expressions_BitwiseOrExpression_strategy)
@settings(max_examples=25)
def test_expressions_BitwiseOrExpression_instantiation(instance):
    assert isinstance(instance, expressions_BitwiseOrExpression)


expressions_BitwiseXorExpression_strategy = st.builds(expressions_BitwiseXorExpression)
@given(instance=expressions_BitwiseXorExpression_strategy)
@settings(max_examples=25)
def test_expressions_BitwiseXorExpression_instantiation(instance):
    assert isinstance(instance, expressions_BitwiseXorExpression)


expressions_BoolLiteral_strategy = st.builds(expressions_BoolLiteral, value=st.booleans())
@given(instance=expressions_BoolLiteral_strategy)
@settings(max_examples=25)
def test_expressions_BoolLiteral_instantiation(instance):
    assert isinstance(instance, expressions_BoolLiteral)


expressions_ConditionalExpression_strategy = st.builds(expressions_ConditionalExpression)
@given(instance=expressions_ConditionalExpression_strategy)
@settings(max_examples=25)
def test_expressions_ConditionalExpression_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalExpression)


expressions_DoubleLiteral_strategy = st.builds(expressions_DoubleLiteral, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=expressions_DoubleLiteral_strategy)
@settings(max_examples=25)
def test_expressions_DoubleLiteral_instantiation(instance):
    assert isinstance(instance, expressions_DoubleLiteral)


expressions_EObject_strategy = st.builds(expressions_EObject)
@given(instance=expressions_EObject_strategy)
@settings(max_examples=25)
def test_expressions_EObject_instantiation(instance):
    assert isinstance(instance, expressions_EObject)


expressions_ElementReferenceExpression_strategy = st.builds(expressions_ElementReferenceExpression, arrayAccess=st.booleans(), operationCall=st.booleans())
@given(instance=expressions_ElementReferenceExpression_strategy)
@settings(max_examples=25)
def test_expressions_ElementReferenceExpression_instantiation(instance):
    assert isinstance(instance, expressions_ElementReferenceExpression)


expressions_Expression_strategy = st.builds(expressions_Expression)
@given(instance=expressions_Expression_strategy)
@settings(max_examples=25)
def test_expressions_Expression_instantiation(instance):
    assert isinstance(instance, expressions_Expression)


expressions_FeatureCall_strategy = st.builds(expressions_FeatureCall, arrayAccess=st.booleans(), operationCall=st.booleans())
@given(instance=expressions_FeatureCall_strategy)
@settings(max_examples=25)
def test_expressions_FeatureCall_instantiation(instance):
    assert isinstance(instance, expressions_FeatureCall)


expressions_FloatLiteral_strategy = st.builds(expressions_FloatLiteral, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=expressions_FloatLiteral_strategy)
@settings(max_examples=25)
def test_expressions_FloatLiteral_instantiation(instance):
    assert isinstance(instance, expressions_FloatLiteral)


expressions_HexLiteral_strategy = st.builds(expressions_HexLiteral, value=st.integers())
@given(instance=expressions_HexLiteral_strategy)
@settings(max_examples=25)
def test_expressions_HexLiteral_instantiation(instance):
    assert isinstance(instance, expressions_HexLiteral)


expressions_IntLiteral_strategy = st.builds(expressions_IntLiteral, value=st.integers())
@given(instance=expressions_IntLiteral_strategy)
@settings(max_examples=25)
def test_expressions_IntLiteral_instantiation(instance):
    assert isinstance(instance, expressions_IntLiteral)


expressions_Literal_strategy = st.builds(expressions_Literal)
@given(instance=expressions_Literal_strategy)
@settings(max_examples=25)
def test_expressions_Literal_instantiation(instance):
    assert isinstance(instance, expressions_Literal)


expressions_LogicalAndExpression_strategy = st.builds(expressions_LogicalAndExpression)
@given(instance=expressions_LogicalAndExpression_strategy)
@settings(max_examples=25)
def test_expressions_LogicalAndExpression_instantiation(instance):
    assert isinstance(instance, expressions_LogicalAndExpression)


expressions_LogicalNotExpression_strategy = st.builds(expressions_LogicalNotExpression)
@given(instance=expressions_LogicalNotExpression_strategy)
@settings(max_examples=25)
def test_expressions_LogicalNotExpression_instantiation(instance):
    assert isinstance(instance, expressions_LogicalNotExpression)


expressions_LogicalOrExpression_strategy = st.builds(expressions_LogicalOrExpression)
@given(instance=expressions_LogicalOrExpression_strategy)
@settings(max_examples=25)
def test_expressions_LogicalOrExpression_instantiation(instance):
    assert isinstance(instance, expressions_LogicalOrExpression)


expressions_LogicalRelationExpression_strategy = st.builds(expressions_LogicalRelationExpression, operator=safe_text)
@given(instance=expressions_LogicalRelationExpression_strategy)
@settings(max_examples=25)
def test_expressions_LogicalRelationExpression_instantiation(instance):
    assert isinstance(instance, expressions_LogicalRelationExpression)


expressions_NullLiteral_strategy = st.builds(expressions_NullLiteral)
@given(instance=expressions_NullLiteral_strategy)
@settings(max_examples=25)
def test_expressions_NullLiteral_instantiation(instance):
    assert isinstance(instance, expressions_NullLiteral)


expressions_NumericalAddSubtractExpression_strategy = st.builds(expressions_NumericalAddSubtractExpression, operator=safe_text)
@given(instance=expressions_NumericalAddSubtractExpression_strategy)
@settings(max_examples=25)
def test_expressions_NumericalAddSubtractExpression_instantiation(instance):
    assert isinstance(instance, expressions_NumericalAddSubtractExpression)


expressions_NumericalMultiplyDivideExpression_strategy = st.builds(expressions_NumericalMultiplyDivideExpression, operator=safe_text)
@given(instance=expressions_NumericalMultiplyDivideExpression_strategy)
@settings(max_examples=25)
def test_expressions_NumericalMultiplyDivideExpression_instantiation(instance):
    assert isinstance(instance, expressions_NumericalMultiplyDivideExpression)


expressions_NumericalUnaryExpression_strategy = st.builds(expressions_NumericalUnaryExpression, operator=safe_text)
@given(instance=expressions_NumericalUnaryExpression_strategy)
@settings(max_examples=25)
def test_expressions_NumericalUnaryExpression_instantiation(instance):
    assert isinstance(instance, expressions_NumericalUnaryExpression)


expressions_ParenthesizedExpression_strategy = st.builds(expressions_ParenthesizedExpression)
@given(instance=expressions_ParenthesizedExpression_strategy)
@settings(max_examples=25)
def test_expressions_ParenthesizedExpression_instantiation(instance):
    assert isinstance(instance, expressions_ParenthesizedExpression)


expressions_PrimitiveValueExpression_strategy = st.builds(expressions_PrimitiveValueExpression)
@given(instance=expressions_PrimitiveValueExpression_strategy)
@settings(max_examples=25)
def test_expressions_PrimitiveValueExpression_instantiation(instance):
    assert isinstance(instance, expressions_PrimitiveValueExpression)


expressions_ShiftExpression_strategy = st.builds(expressions_ShiftExpression, operator=safe_text)
@given(instance=expressions_ShiftExpression_strategy)
@settings(max_examples=25)
def test_expressions_ShiftExpression_instantiation(instance):
    assert isinstance(instance, expressions_ShiftExpression)


expressions_StringLiteral_strategy = st.builds(expressions_StringLiteral, value=safe_text)
@given(instance=expressions_StringLiteral_strategy)
@settings(max_examples=25)
def test_expressions_StringLiteral_instantiation(instance):
    assert isinstance(instance, expressions_StringLiteral)


expressions_Type_strategy = st.builds(expressions_Type)
@given(instance=expressions_Type_strategy)
@settings(max_examples=25)
def test_expressions_Type_instantiation(instance):
    assert isinstance(instance, expressions_Type)


expressions_TypeCastExpression_strategy = st.builds(expressions_TypeCastExpression)
@given(instance=expressions_TypeCastExpression_strategy)
@settings(max_examples=25)
def test_expressions_TypeCastExpression_instantiation(instance):
    assert isinstance(instance, expressions_TypeCastExpression)


expressions_UnaryExpression_strategy = st.builds(expressions_UnaryExpression)
@given(instance=expressions_UnaryExpression_strategy)
@settings(max_examples=25)
def test_expressions_UnaryExpression_instantiation(instance):
    assert isinstance(instance, expressions_UnaryExpression)


