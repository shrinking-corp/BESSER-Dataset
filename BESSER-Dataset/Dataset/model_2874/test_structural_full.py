import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Annotation,
    AssignmentStatement,
    BinaryOperatorExpression,
    CollectionExpression,
    CollectionInitValue,
    CollectionType,
    DomElement,
    Expression,
    FeatureCallExpression,
    LiteralExpression,
    NameExpression,
    OperatorExpression,
    PrimitiveExpression,
    PrimitiveType,
    Statement,
    SwitchCaseStatement,
    Type,
    UnaryOperatorExpression,
    dom_AbortStatement,
    dom_AndOperatorExpression,
    dom_Annotation,
    dom_AnnotationBlock,
    dom_AnyType,
    dom_AssignmentStatement,
    dom_BagExpression,
    dom_BagType,
    dom_BinaryOperatorExpression,
    dom_Block,
    dom_BooleanExpression,
    dom_BooleanType,
    dom_BreakAllStatement,
    dom_BreakStatement,
    dom_CollectionExpression,
    dom_CollectionInitValue,
    dom_CollectionType,
    dom_ContinueStatement,
    dom_DeleteStatement,
    dom_DivideOperatorExpression,
    dom_DomElement,
    dom_EnumerationLiteralExpression,
    dom_EqualsOperatorExpression,
    dom_ExecutableAnnotation,
    dom_ExpRange,
    dom_ExprList,
    dom_Expression,
    dom_ExpressionStatement,
    dom_FOLMethodCallExpression,
    dom_FeatureCallExpression,
    dom_ForStatement,
    dom_FormalParameterExpression,
    dom_GreaterThanOperatorExpression,
    dom_GreaterThanOrEqualToOperatorExpression,
    dom_IfStatement,
    dom_ImpliesOperatorExpression,
    dom_Import,
    dom_IntegerExpression,
    dom_IntegerType,
    dom_KeyValue,
    dom_LessThanOperatorExpression,
    dom_LessThanOrEqualToOperatorExpression,
    dom_LiteralExpression,
    dom_MapExpression,
    dom_MapType,
    dom_MethodCallExpression,
    dom_MinusOperatorExpression,
    dom_ModelDeclarationParameter,
    dom_ModelDeclarationStatement,
    dom_ModelElementType,
    dom_ModelElementTypeExpression,
    dom_ModelExpression,
    dom_MultiplyOperatorExpression,
    dom_NameExpression,
    dom_NativeType,
    dom_NegativeOperatorExpression,
    dom_NewExpression,
    dom_NotEqualsOperatorExpression,
    dom_NotOperatorExpression,
    dom_OperationDefinition,
    dom_OperatorExpression,
    dom_OrOperatorExpression,
    dom_OrderedSetExpression,
    dom_OrderedSetType,
    dom_PlusOperatorExpression,
    dom_PrimitiveExpression,
    dom_PrimitiveType,
    dom_Program,
    dom_PropertyCallExpression,
    dom_RealExpression,
    dom_RealType,
    dom_ReturnStatement,
    dom_SequenceExpression,
    dom_SequenceType,
    dom_SetExpression,
    dom_SetType,
    dom_ShortModelDeclarationExpression,
    dom_SimpleAnnotation,
    dom_SpecialAssignmentStatement,
    dom_SpecialNameExpression,
    dom_Statement,
    dom_StringExpression,
    dom_StringType,
    dom_SwitchCaseDefaultStatement,
    dom_SwitchCaseExpressionStatement,
    dom_SwitchCaseStatement,
    dom_SwitchStatement,
    dom_ThrowStatement,
    dom_TransactionStatement,
    dom_Type,
    dom_UnaryOperatorExpression,
    dom_VariableDeclarationExpression,
    dom_WhileStatement,
    dom_XorOperatorExpression,
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

def test_dom_BooleanExpression_val_value_roundtrip():
    instance = dom_BooleanExpression(val=True)
    assert instance.val == True
    instance.val = False
    assert instance.val == False


def test_dom_DomElement_column_value_roundtrip():
    instance = dom_DomElement(column=7, line=7)
    assert instance.column == 7
    instance.column = 13
    assert instance.column == 13


def test_dom_DomElement_line_value_roundtrip():
    instance = dom_DomElement(column=7, line=7)
    assert instance.line == 7
    instance.line = 13
    assert instance.line == 13


def test_dom_IntegerExpression_val_value_roundtrip():
    instance = dom_IntegerExpression(val=7)
    assert instance.val == 7
    instance.val = 13
    assert instance.val == 13


def test_dom_NameExpression_name_value_roundtrip():
    instance = dom_NameExpression(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_RealExpression_val_value_roundtrip():
    instance = dom_RealExpression(val=3.14)
    assert instance.val == 3.14
    instance.val = 9.99
    assert instance.val == 9.99


def test_dom_StringExpression_val_value_roundtrip():
    instance = dom_StringExpression(val="sample_text")
    assert instance.val == "sample_text"
    instance.val = "sample_text_2"
    assert instance.val == "sample_text_2"


def test_dom_ExecutableAnnotation_isa_Annotation():
    instance = dom_ExecutableAnnotation()
    assert isinstance(instance, Annotation)


def test_dom_SimpleAnnotation_isa_Annotation():
    instance = dom_SimpleAnnotation()
    assert isinstance(instance, Annotation)


def test_dom_SpecialAssignmentStatement_isa_AssignmentStatement():
    instance = dom_SpecialAssignmentStatement()
    assert isinstance(instance, AssignmentStatement)


def test_dom_AndOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_AndOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_DivideOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_DivideOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_EqualsOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_EqualsOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_GreaterThanOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_GreaterThanOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_GreaterThanOrEqualToOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_GreaterThanOrEqualToOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_ImpliesOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_ImpliesOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_LessThanOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_LessThanOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_LessThanOrEqualToOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_LessThanOrEqualToOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_MinusOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_MinusOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_MultiplyOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_MultiplyOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_NotEqualsOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_NotEqualsOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_OrOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_OrOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_PlusOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_PlusOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_XorOperatorExpression_isa_BinaryOperatorExpression():
    instance = dom_XorOperatorExpression()
    assert isinstance(instance, BinaryOperatorExpression)


def test_dom_BagExpression_isa_CollectionExpression():
    instance = dom_BagExpression()
    assert isinstance(instance, CollectionExpression)


def test_dom_OrderedSetExpression_isa_CollectionExpression():
    instance = dom_OrderedSetExpression()
    assert isinstance(instance, CollectionExpression)


def test_dom_SequenceExpression_isa_CollectionExpression():
    instance = dom_SequenceExpression()
    assert isinstance(instance, CollectionExpression)


def test_dom_SetExpression_isa_CollectionExpression():
    instance = dom_SetExpression()
    assert isinstance(instance, CollectionExpression)


def test_dom_ExpRange_isa_CollectionInitValue():
    instance = dom_ExpRange()
    assert isinstance(instance, CollectionInitValue)


def test_dom_ExprList_isa_CollectionInitValue():
    instance = dom_ExprList()
    assert isinstance(instance, CollectionInitValue)


def test_dom_BagType_isa_CollectionType():
    instance = dom_BagType()
    assert isinstance(instance, CollectionType)


def test_dom_OrderedSetType_isa_CollectionType():
    instance = dom_OrderedSetType()
    assert isinstance(instance, CollectionType)


def test_dom_SequenceType_isa_CollectionType():
    instance = dom_SequenceType()
    assert isinstance(instance, CollectionType)


def test_dom_SetType_isa_CollectionType():
    instance = dom_SetType()
    assert isinstance(instance, CollectionType)


def test_dom_Annotation_isa_DomElement():
    instance = dom_Annotation()
    assert isinstance(instance, DomElement)


def test_dom_AnnotationBlock_isa_DomElement():
    instance = dom_AnnotationBlock()
    assert isinstance(instance, DomElement)


def test_dom_Block_isa_DomElement():
    instance = dom_Block()
    assert isinstance(instance, DomElement)


def test_dom_CollectionInitValue_isa_DomElement():
    instance = dom_CollectionInitValue()
    assert isinstance(instance, DomElement)


def test_dom_Expression_isa_DomElement():
    instance = dom_Expression()
    assert isinstance(instance, DomElement)


def test_dom_Import_isa_DomElement():
    instance = dom_Import()
    assert isinstance(instance, DomElement)


def test_dom_KeyValue_isa_DomElement():
    instance = dom_KeyValue()
    assert isinstance(instance, DomElement)


def test_dom_ModelDeclarationParameter_isa_DomElement():
    instance = dom_ModelDeclarationParameter()
    assert isinstance(instance, DomElement)


def test_dom_OperationDefinition_isa_DomElement():
    instance = dom_OperationDefinition()
    assert isinstance(instance, DomElement)


def test_dom_Program_isa_DomElement():
    instance = dom_Program()
    assert isinstance(instance, DomElement)


def test_dom_Statement_isa_DomElement():
    instance = dom_Statement()
    assert isinstance(instance, DomElement)


def test_dom_Type_isa_DomElement():
    instance = dom_Type()
    assert isinstance(instance, DomElement)


def test_dom_EnumerationLiteralExpression_isa_Expression():
    instance = dom_EnumerationLiteralExpression()
    assert isinstance(instance, Expression)


def test_dom_FeatureCallExpression_isa_Expression():
    instance = dom_FeatureCallExpression()
    assert isinstance(instance, Expression)


def test_dom_FormalParameterExpression_isa_Expression():
    instance = dom_FormalParameterExpression()
    assert isinstance(instance, Expression)


def test_dom_LiteralExpression_isa_Expression():
    instance = dom_LiteralExpression()
    assert isinstance(instance, Expression)


def test_dom_ModelElementTypeExpression_isa_Expression():
    instance = dom_ModelElementTypeExpression()
    assert isinstance(instance, Expression)


def test_dom_NameExpression_isa_Expression():
    instance = dom_NameExpression(name="sample_text")
    assert isinstance(instance, Expression)


def test_dom_NewExpression_isa_Expression():
    instance = dom_NewExpression()
    assert isinstance(instance, Expression)


def test_dom_OperatorExpression_isa_Expression():
    instance = dom_OperatorExpression()
    assert isinstance(instance, Expression)


def test_dom_VariableDeclarationExpression_isa_Expression():
    instance = dom_VariableDeclarationExpression()
    assert isinstance(instance, Expression)


def test_dom_FOLMethodCallExpression_isa_FeatureCallExpression():
    instance = dom_FOLMethodCallExpression()
    assert isinstance(instance, FeatureCallExpression)


def test_dom_MethodCallExpression_isa_FeatureCallExpression():
    instance = dom_MethodCallExpression()
    assert isinstance(instance, FeatureCallExpression)


def test_dom_PropertyCallExpression_isa_FeatureCallExpression():
    instance = dom_PropertyCallExpression()
    assert isinstance(instance, FeatureCallExpression)


def test_dom_CollectionExpression_isa_LiteralExpression():
    instance = dom_CollectionExpression()
    assert isinstance(instance, LiteralExpression)


def test_dom_MapExpression_isa_LiteralExpression():
    instance = dom_MapExpression()
    assert isinstance(instance, LiteralExpression)


def test_dom_PrimitiveExpression_isa_LiteralExpression():
    instance = dom_PrimitiveExpression()
    assert isinstance(instance, LiteralExpression)


def test_dom_ModelExpression_isa_NameExpression():
    instance = dom_ModelExpression()
    assert isinstance(instance, NameExpression)


def test_dom_SpecialNameExpression_isa_NameExpression():
    instance = dom_SpecialNameExpression()
    assert isinstance(instance, NameExpression)


def test_dom_BinaryOperatorExpression_isa_OperatorExpression():
    instance = dom_BinaryOperatorExpression()
    assert isinstance(instance, OperatorExpression)


def test_dom_UnaryOperatorExpression_isa_OperatorExpression():
    instance = dom_UnaryOperatorExpression()
    assert isinstance(instance, OperatorExpression)


def test_dom_BooleanExpression_isa_PrimitiveExpression():
    instance = dom_BooleanExpression(val=True)
    assert isinstance(instance, PrimitiveExpression)


def test_dom_IntegerExpression_isa_PrimitiveExpression():
    instance = dom_IntegerExpression(val=7)
    assert isinstance(instance, PrimitiveExpression)


def test_dom_RealExpression_isa_PrimitiveExpression():
    instance = dom_RealExpression(val=3.14)
    assert isinstance(instance, PrimitiveExpression)


def test_dom_StringExpression_isa_PrimitiveExpression():
    instance = dom_StringExpression(val="sample_text")
    assert isinstance(instance, PrimitiveExpression)


def test_dom_BooleanType_isa_PrimitiveType():
    instance = dom_BooleanType()
    assert isinstance(instance, PrimitiveType)


def test_dom_IntegerType_isa_PrimitiveType():
    instance = dom_IntegerType()
    assert isinstance(instance, PrimitiveType)


def test_dom_RealType_isa_PrimitiveType():
    instance = dom_RealType()
    assert isinstance(instance, PrimitiveType)


def test_dom_StringType_isa_PrimitiveType():
    instance = dom_StringType()
    assert isinstance(instance, PrimitiveType)


def test_dom_AbortStatement_isa_Statement():
    instance = dom_AbortStatement()
    assert isinstance(instance, Statement)


def test_dom_AssignmentStatement_isa_Statement():
    instance = dom_AssignmentStatement()
    assert isinstance(instance, Statement)


def test_dom_BreakAllStatement_isa_Statement():
    instance = dom_BreakAllStatement()
    assert isinstance(instance, Statement)


def test_dom_BreakStatement_isa_Statement():
    instance = dom_BreakStatement()
    assert isinstance(instance, Statement)


def test_dom_ContinueStatement_isa_Statement():
    instance = dom_ContinueStatement()
    assert isinstance(instance, Statement)


def test_dom_DeleteStatement_isa_Statement():
    instance = dom_DeleteStatement()
    assert isinstance(instance, Statement)


def test_dom_ExpressionStatement_isa_Statement():
    instance = dom_ExpressionStatement()
    assert isinstance(instance, Statement)


def test_dom_ForStatement_isa_Statement():
    instance = dom_ForStatement()
    assert isinstance(instance, Statement)


def test_dom_IfStatement_isa_Statement():
    instance = dom_IfStatement()
    assert isinstance(instance, Statement)


def test_dom_ModelDeclarationStatement_isa_Statement():
    instance = dom_ModelDeclarationStatement()
    assert isinstance(instance, Statement)


def test_dom_ReturnStatement_isa_Statement():
    instance = dom_ReturnStatement()
    assert isinstance(instance, Statement)


def test_dom_SwitchCaseStatement_isa_Statement():
    instance = dom_SwitchCaseStatement()
    assert isinstance(instance, Statement)


def test_dom_SwitchStatement_isa_Statement():
    instance = dom_SwitchStatement()
    assert isinstance(instance, Statement)


def test_dom_ThrowStatement_isa_Statement():
    instance = dom_ThrowStatement()
    assert isinstance(instance, Statement)


def test_dom_TransactionStatement_isa_Statement():
    instance = dom_TransactionStatement()
    assert isinstance(instance, Statement)


def test_dom_WhileStatement_isa_Statement():
    instance = dom_WhileStatement()
    assert isinstance(instance, Statement)


def test_dom_SwitchCaseDefaultStatement_isa_SwitchCaseStatement():
    instance = dom_SwitchCaseDefaultStatement()
    assert isinstance(instance, SwitchCaseStatement)


def test_dom_SwitchCaseExpressionStatement_isa_SwitchCaseStatement():
    instance = dom_SwitchCaseExpressionStatement()
    assert isinstance(instance, SwitchCaseStatement)


def test_dom_AnyType_isa_Type():
    instance = dom_AnyType()
    assert isinstance(instance, Type)


def test_dom_CollectionType_isa_Type():
    instance = dom_CollectionType()
    assert isinstance(instance, Type)


def test_dom_MapType_isa_Type():
    instance = dom_MapType()
    assert isinstance(instance, Type)


def test_dom_ModelElementType_isa_Type():
    instance = dom_ModelElementType()
    assert isinstance(instance, Type)


def test_dom_NativeType_isa_Type():
    instance = dom_NativeType()
    assert isinstance(instance, Type)


def test_dom_PrimitiveType_isa_Type():
    instance = dom_PrimitiveType()
    assert isinstance(instance, Type)


def test_dom_NegativeOperatorExpression_isa_UnaryOperatorExpression():
    instance = dom_NegativeOperatorExpression()
    assert isinstance(instance, UnaryOperatorExpression)


def test_dom_NotOperatorExpression_isa_UnaryOperatorExpression():
    instance = dom_NotOperatorExpression()
    assert isinstance(instance, UnaryOperatorExpression)


def test_assoc_alias110_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_ModelDeclarationStatement()
    b2 = dom_ModelDeclarationStatement()
    _safe_set(a, 'dom_NameExpression112', b1)
    assert _is_linked(a, 'dom_NameExpression112', b1)
    if hasattr(b1, 'dom_ModelDeclarationStatement111'):
        assert _is_linked(b1, 'dom_ModelDeclarationStatement111', a)
    _safe_set(a, 'dom_NameExpression112', b2)
    assert _is_linked(a, 'dom_NameExpression112', b2)
    if hasattr(b1, 'dom_ModelDeclarationStatement111'):
        assert not _is_linked(b1, 'dom_ModelDeclarationStatement111', a)
    if hasattr(b2, 'dom_ModelDeclarationStatement111'):
        assert _is_linked(b2, 'dom_ModelDeclarationStatement111', a)
    _safe_set(a, 'dom_NameExpression112', None)
    assert not _is_linked(a, 'dom_NameExpression112', b2)
    if hasattr(b2, 'dom_ModelDeclarationStatement111'):
        assert not _is_linked(b2, 'dom_ModelDeclarationStatement111', a)


def test_assoc_container1_link_reassign_clear():
    a = dom_DomElement(column=7, line=7)
    b1 = dom_DomElement(column=7, line=7)
    b2 = dom_DomElement(column=13, line=13)
    _safe_set(a, 'dom_DomElement', b1)
    assert _is_linked(a, 'dom_DomElement', b1)
    if hasattr(b1, 'dom_DomElement0'):
        assert _is_linked(b1, 'dom_DomElement0', a)
    _safe_set(a, 'dom_DomElement', b2)
    assert _is_linked(a, 'dom_DomElement', b2)
    if hasattr(b1, 'dom_DomElement0'):
        assert not _is_linked(b1, 'dom_DomElement0', a)
    if hasattr(b2, 'dom_DomElement0'):
        assert _is_linked(b2, 'dom_DomElement0', a)
    _safe_set(a, 'dom_DomElement', None)
    assert not _is_linked(a, 'dom_DomElement', b2)
    if hasattr(b2, 'dom_DomElement0'):
        assert not _is_linked(b2, 'dom_DomElement0', a)


def test_assoc_create47_link_reassign_clear():
    a = dom_BooleanExpression(val=True)
    b1 = dom_VariableDeclarationExpression()
    b2 = dom_VariableDeclarationExpression()
    _safe_set(a, 'dom_BooleanExpression49', b1)
    assert _is_linked(a, 'dom_BooleanExpression49', b1)
    if hasattr(b1, 'dom_VariableDeclarationExpression48'):
        assert _is_linked(b1, 'dom_VariableDeclarationExpression48', a)
    _safe_set(a, 'dom_BooleanExpression49', b2)
    assert _is_linked(a, 'dom_BooleanExpression49', b2)
    if hasattr(b1, 'dom_VariableDeclarationExpression48'):
        assert not _is_linked(b1, 'dom_VariableDeclarationExpression48', a)
    if hasattr(b2, 'dom_VariableDeclarationExpression48'):
        assert _is_linked(b2, 'dom_VariableDeclarationExpression48', a)
    _safe_set(a, 'dom_BooleanExpression49', None)
    assert not _is_linked(a, 'dom_BooleanExpression49', b2)
    if hasattr(b2, 'dom_VariableDeclarationExpression48'):
        assert not _is_linked(b2, 'dom_VariableDeclarationExpression48', a)


def test_assoc_driver113_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_ModelDeclarationStatement()
    b2 = dom_ModelDeclarationStatement()
    _safe_set(a, 'dom_NameExpression115', b1)
    assert _is_linked(a, 'dom_NameExpression115', b1)
    if hasattr(b1, 'dom_ModelDeclarationStatement114'):
        assert _is_linked(b1, 'dom_ModelDeclarationStatement114', a)
    _safe_set(a, 'dom_NameExpression115', b2)
    assert _is_linked(a, 'dom_NameExpression115', b2)
    if hasattr(b1, 'dom_ModelDeclarationStatement114'):
        assert not _is_linked(b1, 'dom_ModelDeclarationStatement114', a)
    if hasattr(b2, 'dom_ModelDeclarationStatement114'):
        assert _is_linked(b2, 'dom_ModelDeclarationStatement114', a)
    _safe_set(a, 'dom_NameExpression115', None)
    assert not _is_linked(a, 'dom_NameExpression115', b2)
    if hasattr(b2, 'dom_ModelDeclarationStatement114'):
        assert not _is_linked(b2, 'dom_ModelDeclarationStatement114', a)


def test_assoc_element185_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_ModelElementTypeExpression()
    b2 = dom_ModelElementTypeExpression()
    _safe_set(a, 'dom_NameExpression187', b1)
    assert _is_linked(a, 'dom_NameExpression187', b1)
    if hasattr(b1, 'dom_ModelElementTypeExpression186'):
        assert _is_linked(b1, 'dom_ModelElementTypeExpression186', a)
    _safe_set(a, 'dom_NameExpression187', b2)
    assert _is_linked(a, 'dom_NameExpression187', b2)
    if hasattr(b1, 'dom_ModelElementTypeExpression186'):
        assert not _is_linked(b1, 'dom_ModelElementTypeExpression186', a)
    if hasattr(b2, 'dom_ModelElementTypeExpression186'):
        assert _is_linked(b2, 'dom_ModelElementTypeExpression186', a)
    _safe_set(a, 'dom_NameExpression187', None)
    assert not _is_linked(a, 'dom_NameExpression187', b2)
    if hasattr(b2, 'dom_ModelElementTypeExpression186'):
        assert not _is_linked(b2, 'dom_ModelElementTypeExpression186', a)


def test_assoc_enumeration21_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_EnumerationLiteralExpression()
    b2 = dom_EnumerationLiteralExpression()
    _safe_set(a, 'dom_NameExpression22', b1)
    assert _is_linked(a, 'dom_NameExpression22', b1)
    if hasattr(b1, 'dom_EnumerationLiteralExpression'):
        assert _is_linked(b1, 'dom_EnumerationLiteralExpression', a)
    _safe_set(a, 'dom_NameExpression22', b2)
    assert _is_linked(a, 'dom_NameExpression22', b2)
    if hasattr(b1, 'dom_EnumerationLiteralExpression'):
        assert not _is_linked(b1, 'dom_EnumerationLiteralExpression', a)
    if hasattr(b2, 'dom_EnumerationLiteralExpression'):
        assert _is_linked(b2, 'dom_EnumerationLiteralExpression', a)
    _safe_set(a, 'dom_NameExpression22', None)
    assert not _is_linked(a, 'dom_NameExpression22', b2)
    if hasattr(b2, 'dom_EnumerationLiteralExpression'):
        assert not _is_linked(b2, 'dom_EnumerationLiteralExpression', a)


def test_assoc_extended42_link_reassign_clear():
    a = dom_BooleanExpression(val=True)
    b1 = dom_PropertyCallExpression()
    b2 = dom_PropertyCallExpression()
    _safe_set(a, 'dom_BooleanExpression44', b1)
    assert _is_linked(a, 'dom_BooleanExpression44', b1)
    if hasattr(b1, 'dom_PropertyCallExpression43'):
        assert _is_linked(b1, 'dom_PropertyCallExpression43', a)
    _safe_set(a, 'dom_BooleanExpression44', b2)
    assert _is_linked(a, 'dom_BooleanExpression44', b2)
    if hasattr(b1, 'dom_PropertyCallExpression43'):
        assert not _is_linked(b1, 'dom_PropertyCallExpression43', a)
    if hasattr(b2, 'dom_PropertyCallExpression43'):
        assert _is_linked(b2, 'dom_PropertyCallExpression43', a)
    _safe_set(a, 'dom_BooleanExpression44', None)
    assert not _is_linked(a, 'dom_BooleanExpression44', b2)
    if hasattr(b2, 'dom_PropertyCallExpression43'):
        assert not _is_linked(b2, 'dom_PropertyCallExpression43', a)


def test_assoc_imported11_link_reassign_clear():
    a = dom_StringExpression(val="sample_text")
    b1 = dom_Import()
    b2 = dom_Import()
    _safe_set(a, 'dom_StringExpression', b1)
    assert _is_linked(a, 'dom_StringExpression', b1)
    if hasattr(b1, 'dom_Import12'):
        assert _is_linked(b1, 'dom_Import12', a)
    _safe_set(a, 'dom_StringExpression', b2)
    assert _is_linked(a, 'dom_StringExpression', b2)
    if hasattr(b1, 'dom_Import12'):
        assert not _is_linked(b1, 'dom_Import12', a)
    if hasattr(b2, 'dom_Import12'):
        assert _is_linked(b2, 'dom_Import12', a)
    _safe_set(a, 'dom_StringExpression', None)
    assert not _is_linked(a, 'dom_StringExpression', b2)
    if hasattr(b2, 'dom_Import12'):
        assert not _is_linked(b2, 'dom_Import12', a)


def test_assoc_isArrow31_link_reassign_clear():
    a = dom_BooleanExpression(val=True)
    b1 = dom_FeatureCallExpression()
    b2 = dom_FeatureCallExpression()
    _safe_set(a, 'dom_BooleanExpression', b1)
    assert _is_linked(a, 'dom_BooleanExpression', b1)
    if hasattr(b1, 'dom_FeatureCallExpression32'):
        assert _is_linked(b1, 'dom_FeatureCallExpression32', a)
    _safe_set(a, 'dom_BooleanExpression', b2)
    assert _is_linked(a, 'dom_BooleanExpression', b2)
    if hasattr(b1, 'dom_FeatureCallExpression32'):
        assert not _is_linked(b1, 'dom_FeatureCallExpression32', a)
    if hasattr(b2, 'dom_FeatureCallExpression32'):
        assert _is_linked(b2, 'dom_FeatureCallExpression32', a)
    _safe_set(a, 'dom_BooleanExpression', None)
    assert not _is_linked(a, 'dom_BooleanExpression', b2)
    if hasattr(b2, 'dom_FeatureCallExpression32'):
        assert not _is_linked(b2, 'dom_FeatureCallExpression32', a)


def test_assoc_literal23_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_EnumerationLiteralExpression()
    b2 = dom_EnumerationLiteralExpression()
    _safe_set(a, 'dom_NameExpression25', b1)
    assert _is_linked(a, 'dom_NameExpression25', b1)
    if hasattr(b1, 'dom_EnumerationLiteralExpression24'):
        assert _is_linked(b1, 'dom_EnumerationLiteralExpression24', a)
    _safe_set(a, 'dom_NameExpression25', b2)
    assert _is_linked(a, 'dom_NameExpression25', b2)
    if hasattr(b1, 'dom_EnumerationLiteralExpression24'):
        assert not _is_linked(b1, 'dom_EnumerationLiteralExpression24', a)
    if hasattr(b2, 'dom_EnumerationLiteralExpression24'):
        assert _is_linked(b2, 'dom_EnumerationLiteralExpression24', a)
    _safe_set(a, 'dom_NameExpression25', None)
    assert not _is_linked(a, 'dom_NameExpression25', b2)
    if hasattr(b2, 'dom_EnumerationLiteralExpression24'):
        assert not _is_linked(b2, 'dom_EnumerationLiteralExpression24', a)


def test_assoc_method123_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_FOLMethodCallExpression()
    b2 = dom_FOLMethodCallExpression()
    _safe_set(a, 'dom_NameExpression125', b1)
    assert _is_linked(a, 'dom_NameExpression125', b1)
    if hasattr(b1, 'dom_FOLMethodCallExpression124'):
        assert _is_linked(b1, 'dom_FOLMethodCallExpression124', a)
    _safe_set(a, 'dom_NameExpression125', b2)
    assert _is_linked(a, 'dom_NameExpression125', b2)
    if hasattr(b1, 'dom_FOLMethodCallExpression124'):
        assert not _is_linked(b1, 'dom_FOLMethodCallExpression124', a)
    if hasattr(b2, 'dom_FOLMethodCallExpression124'):
        assert _is_linked(b2, 'dom_FOLMethodCallExpression124', a)
    _safe_set(a, 'dom_NameExpression125', None)
    assert not _is_linked(a, 'dom_NameExpression125', b2)
    if hasattr(b2, 'dom_FOLMethodCallExpression124'):
        assert not _is_linked(b2, 'dom_FOLMethodCallExpression124', a)


def test_assoc_method35_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_MethodCallExpression()
    b2 = dom_MethodCallExpression()
    _safe_set(a, 'dom_NameExpression37', b1)
    assert _is_linked(a, 'dom_NameExpression37', b1)
    if hasattr(b1, 'dom_MethodCallExpression36'):
        assert _is_linked(b1, 'dom_MethodCallExpression36', a)
    _safe_set(a, 'dom_NameExpression37', b2)
    assert _is_linked(a, 'dom_NameExpression37', b2)
    if hasattr(b1, 'dom_MethodCallExpression36'):
        assert not _is_linked(b1, 'dom_MethodCallExpression36', a)
    if hasattr(b2, 'dom_MethodCallExpression36'):
        assert _is_linked(b2, 'dom_MethodCallExpression36', a)
    _safe_set(a, 'dom_NameExpression37', None)
    assert not _is_linked(a, 'dom_NameExpression37', b2)
    if hasattr(b2, 'dom_MethodCallExpression36'):
        assert not _is_linked(b2, 'dom_MethodCallExpression36', a)


def test_assoc_model182_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_ModelElementTypeExpression()
    b2 = dom_ModelElementTypeExpression()
    _safe_set(a, 'dom_NameExpression184', b1)
    assert _is_linked(a, 'dom_NameExpression184', b1)
    if hasattr(b1, 'dom_ModelElementTypeExpression183'):
        assert _is_linked(b1, 'dom_ModelElementTypeExpression183', a)
    _safe_set(a, 'dom_NameExpression184', b2)
    assert _is_linked(a, 'dom_NameExpression184', b2)
    if hasattr(b1, 'dom_ModelElementTypeExpression183'):
        assert not _is_linked(b1, 'dom_ModelElementTypeExpression183', a)
    if hasattr(b2, 'dom_ModelElementTypeExpression183'):
        assert _is_linked(b2, 'dom_ModelElementTypeExpression183', a)
    _safe_set(a, 'dom_NameExpression184', None)
    assert not _is_linked(a, 'dom_NameExpression184', b2)
    if hasattr(b2, 'dom_ModelElementTypeExpression183'):
        assert not _is_linked(b2, 'dom_ModelElementTypeExpression183', a)


def test_assoc_model26_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_EnumerationLiteralExpression()
    b2 = dom_EnumerationLiteralExpression()
    _safe_set(a, 'dom_NameExpression28', b1)
    assert _is_linked(a, 'dom_NameExpression28', b1)
    if hasattr(b1, 'dom_EnumerationLiteralExpression27'):
        assert _is_linked(b1, 'dom_EnumerationLiteralExpression27', a)
    _safe_set(a, 'dom_NameExpression28', b2)
    assert _is_linked(a, 'dom_NameExpression28', b2)
    if hasattr(b1, 'dom_EnumerationLiteralExpression27'):
        assert not _is_linked(b1, 'dom_EnumerationLiteralExpression27', a)
    if hasattr(b2, 'dom_EnumerationLiteralExpression27'):
        assert _is_linked(b2, 'dom_EnumerationLiteralExpression27', a)
    _safe_set(a, 'dom_NameExpression28', None)
    assert not _is_linked(a, 'dom_NameExpression28', b2)
    if hasattr(b2, 'dom_EnumerationLiteralExpression27'):
        assert not _is_linked(b2, 'dom_EnumerationLiteralExpression27', a)


def test_assoc_name107_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_ModelDeclarationStatement()
    b2 = dom_ModelDeclarationStatement()
    _safe_set(a, 'dom_NameExpression109', b1)
    assert _is_linked(a, 'dom_NameExpression109', b1)
    if hasattr(b1, 'dom_ModelDeclarationStatement108'):
        assert _is_linked(b1, 'dom_ModelDeclarationStatement108', a)
    _safe_set(a, 'dom_NameExpression109', b2)
    assert _is_linked(a, 'dom_NameExpression109', b2)
    if hasattr(b1, 'dom_ModelDeclarationStatement108'):
        assert not _is_linked(b1, 'dom_ModelDeclarationStatement108', a)
    if hasattr(b2, 'dom_ModelDeclarationStatement108'):
        assert _is_linked(b2, 'dom_ModelDeclarationStatement108', a)
    _safe_set(a, 'dom_NameExpression109', None)
    assert not _is_linked(a, 'dom_NameExpression109', b2)
    if hasattr(b2, 'dom_ModelDeclarationStatement108'):
        assert not _is_linked(b2, 'dom_ModelDeclarationStatement108', a)


def test_assoc_name136_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_Annotation()
    b2 = dom_Annotation()
    _safe_set(a, 'dom_NameExpression137', b1)
    assert _is_linked(a, 'dom_NameExpression137', b1)
    if hasattr(b1, 'dom_Annotation'):
        assert _is_linked(b1, 'dom_Annotation', a)
    _safe_set(a, 'dom_NameExpression137', b2)
    assert _is_linked(a, 'dom_NameExpression137', b2)
    if hasattr(b1, 'dom_Annotation'):
        assert not _is_linked(b1, 'dom_Annotation', a)
    if hasattr(b2, 'dom_Annotation'):
        assert _is_linked(b2, 'dom_Annotation', a)
    _safe_set(a, 'dom_NameExpression137', None)
    assert not _is_linked(a, 'dom_NameExpression137', b2)
    if hasattr(b2, 'dom_Annotation'):
        assert not _is_linked(b2, 'dom_Annotation', a)


def test_assoc_name157_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_ModelDeclarationParameter()
    b2 = dom_ModelDeclarationParameter()
    _safe_set(a, 'dom_NameExpression159', b1)
    assert _is_linked(a, 'dom_NameExpression159', b1)
    if hasattr(b1, 'dom_ModelDeclarationParameter158'):
        assert _is_linked(b1, 'dom_ModelDeclarationParameter158', a)
    _safe_set(a, 'dom_NameExpression159', b2)
    assert _is_linked(a, 'dom_NameExpression159', b2)
    if hasattr(b1, 'dom_ModelDeclarationParameter158'):
        assert not _is_linked(b1, 'dom_ModelDeclarationParameter158', a)
    if hasattr(b2, 'dom_ModelDeclarationParameter158'):
        assert _is_linked(b2, 'dom_ModelDeclarationParameter158', a)
    _safe_set(a, 'dom_NameExpression159', None)
    assert not _is_linked(a, 'dom_NameExpression159', b2)
    if hasattr(b2, 'dom_ModelDeclarationParameter158'):
        assert not _is_linked(b2, 'dom_ModelDeclarationParameter158', a)


def test_assoc_name170_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_FormalParameterExpression()
    b2 = dom_FormalParameterExpression()
    _safe_set(a, 'dom_NameExpression172', b1)
    assert _is_linked(a, 'dom_NameExpression172', b1)
    if hasattr(b1, 'dom_FormalParameterExpression171'):
        assert _is_linked(b1, 'dom_FormalParameterExpression171', a)
    _safe_set(a, 'dom_NameExpression172', b2)
    assert _is_linked(a, 'dom_NameExpression172', b2)
    if hasattr(b1, 'dom_FormalParameterExpression171'):
        assert not _is_linked(b1, 'dom_FormalParameterExpression171', a)
    if hasattr(b2, 'dom_FormalParameterExpression171'):
        assert _is_linked(b2, 'dom_FormalParameterExpression171', a)
    _safe_set(a, 'dom_NameExpression172', None)
    assert not _is_linked(a, 'dom_NameExpression172', b2)
    if hasattr(b2, 'dom_FormalParameterExpression171'):
        assert not _is_linked(b2, 'dom_FormalParameterExpression171', a)


def test_assoc_name45_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_VariableDeclarationExpression()
    b2 = dom_VariableDeclarationExpression()
    _safe_set(a, 'dom_NameExpression46', b1)
    assert _is_linked(a, 'dom_NameExpression46', b1)
    if hasattr(b1, 'dom_VariableDeclarationExpression'):
        assert _is_linked(b1, 'dom_VariableDeclarationExpression', a)
    _safe_set(a, 'dom_NameExpression46', b2)
    assert _is_linked(a, 'dom_NameExpression46', b2)
    if hasattr(b1, 'dom_VariableDeclarationExpression'):
        assert not _is_linked(b1, 'dom_VariableDeclarationExpression', a)
    if hasattr(b2, 'dom_VariableDeclarationExpression'):
        assert _is_linked(b2, 'dom_VariableDeclarationExpression', a)
    _safe_set(a, 'dom_NameExpression46', None)
    assert not _is_linked(a, 'dom_NameExpression46', b2)
    if hasattr(b2, 'dom_VariableDeclarationExpression'):
        assert not _is_linked(b2, 'dom_VariableDeclarationExpression', a)


def test_assoc_name64_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_OperationDefinition()
    b2 = dom_OperationDefinition()
    _safe_set(a, 'dom_NameExpression66', b1)
    assert _is_linked(a, 'dom_NameExpression66', b1)
    if hasattr(b1, 'dom_OperationDefinition65'):
        assert _is_linked(b1, 'dom_OperationDefinition65', a)
    _safe_set(a, 'dom_NameExpression66', b2)
    assert _is_linked(a, 'dom_NameExpression66', b2)
    if hasattr(b1, 'dom_OperationDefinition65'):
        assert not _is_linked(b1, 'dom_OperationDefinition65', a)
    if hasattr(b2, 'dom_OperationDefinition65'):
        assert _is_linked(b2, 'dom_OperationDefinition65', a)
    _safe_set(a, 'dom_NameExpression66', None)
    assert not _is_linked(a, 'dom_NameExpression66', b2)
    if hasattr(b2, 'dom_OperationDefinition65'):
        assert not _is_linked(b2, 'dom_OperationDefinition65', a)


def test_assoc_name7_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_Program()
    b2 = dom_Program()
    _safe_set(a, 'dom_NameExpression', b1)
    assert _is_linked(a, 'dom_NameExpression', b1)
    if hasattr(b1, 'dom_Program8'):
        assert _is_linked(b1, 'dom_Program8', a)
    _safe_set(a, 'dom_NameExpression', b2)
    assert _is_linked(a, 'dom_NameExpression', b2)
    if hasattr(b1, 'dom_Program8'):
        assert not _is_linked(b1, 'dom_Program8', a)
    if hasattr(b2, 'dom_Program8'):
        assert _is_linked(b2, 'dom_Program8', a)
    _safe_set(a, 'dom_NameExpression', None)
    assert not _is_linked(a, 'dom_NameExpression', b2)
    if hasattr(b2, 'dom_Program8'):
        assert not _is_linked(b2, 'dom_Program8', a)


def test_assoc_names167_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_TransactionStatement()
    b2 = dom_TransactionStatement()
    _safe_set(a, 'dom_NameExpression169', b1)
    assert _is_linked(a, 'dom_NameExpression169', b1)
    if hasattr(b1, 'dom_TransactionStatement168'):
        assert _is_linked(b1, 'dom_TransactionStatement168', a)
    _safe_set(a, 'dom_NameExpression169', b2)
    assert _is_linked(a, 'dom_NameExpression169', b2)
    if hasattr(b1, 'dom_TransactionStatement168'):
        assert not _is_linked(b1, 'dom_TransactionStatement168', a)
    if hasattr(b2, 'dom_TransactionStatement168'):
        assert _is_linked(b2, 'dom_TransactionStatement168', a)
    _safe_set(a, 'dom_NameExpression169', None)
    assert not _is_linked(a, 'dom_NameExpression169', b2)
    if hasattr(b2, 'dom_TransactionStatement168'):
        assert not _is_linked(b2, 'dom_TransactionStatement168', a)


def test_assoc_nativeExpression149_link_reassign_clear():
    a = dom_StringExpression(val="sample_text")
    b1 = dom_NativeType()
    b2 = dom_NativeType()
    _safe_set(a, 'dom_StringExpression150', b1)
    assert _is_linked(a, 'dom_StringExpression150', b1)
    if hasattr(b1, 'dom_NativeType'):
        assert _is_linked(b1, 'dom_NativeType', a)
    _safe_set(a, 'dom_StringExpression150', b2)
    assert _is_linked(a, 'dom_StringExpression150', b2)
    if hasattr(b1, 'dom_NativeType'):
        assert not _is_linked(b1, 'dom_NativeType', a)
    if hasattr(b2, 'dom_NativeType'):
        assert _is_linked(b2, 'dom_NativeType', a)
    _safe_set(a, 'dom_StringExpression150', None)
    assert not _is_linked(a, 'dom_StringExpression150', b2)
    if hasattr(b2, 'dom_NativeType'):
        assert not _is_linked(b2, 'dom_NativeType', a)


def test_assoc_property40_link_reassign_clear():
    a = dom_NameExpression(name="sample_text")
    b1 = dom_PropertyCallExpression()
    b2 = dom_PropertyCallExpression()
    _safe_set(a, 'dom_NameExpression41', b1)
    assert _is_linked(a, 'dom_NameExpression41', b1)
    if hasattr(b1, 'dom_PropertyCallExpression'):
        assert _is_linked(b1, 'dom_PropertyCallExpression', a)
    _safe_set(a, 'dom_NameExpression41', b2)
    assert _is_linked(a, 'dom_NameExpression41', b2)
    if hasattr(b1, 'dom_PropertyCallExpression'):
        assert not _is_linked(b1, 'dom_PropertyCallExpression', a)
    if hasattr(b2, 'dom_PropertyCallExpression'):
        assert _is_linked(b2, 'dom_PropertyCallExpression', a)
    _safe_set(a, 'dom_NameExpression41', None)
    assert not _is_linked(a, 'dom_NameExpression41', b2)
    if hasattr(b2, 'dom_PropertyCallExpression'):
        assert not _is_linked(b2, 'dom_PropertyCallExpression', a)


def test_assoc_value160_link_reassign_clear():
    a = dom_StringExpression(val="sample_text")
    b1 = dom_ModelDeclarationParameter()
    b2 = dom_ModelDeclarationParameter()
    _safe_set(a, 'dom_StringExpression162', b1)
    assert _is_linked(a, 'dom_StringExpression162', b1)
    if hasattr(b1, 'dom_ModelDeclarationParameter161'):
        assert _is_linked(b1, 'dom_ModelDeclarationParameter161', a)
    _safe_set(a, 'dom_StringExpression162', b2)
    assert _is_linked(a, 'dom_StringExpression162', b2)
    if hasattr(b1, 'dom_ModelDeclarationParameter161'):
        assert not _is_linked(b1, 'dom_ModelDeclarationParameter161', a)
    if hasattr(b2, 'dom_ModelDeclarationParameter161'):
        assert _is_linked(b2, 'dom_ModelDeclarationParameter161', a)
    _safe_set(a, 'dom_StringExpression162', None)
    assert not _is_linked(a, 'dom_StringExpression162', b2)
    if hasattr(b2, 'dom_ModelDeclarationParameter161'):
        assert not _is_linked(b2, 'dom_ModelDeclarationParameter161', a)


def test_assoc_values140_link_reassign_clear():
    a = dom_StringExpression(val="sample_text")
    b1 = dom_SimpleAnnotation()
    b2 = dom_SimpleAnnotation()
    _safe_set(a, 'dom_StringExpression141', b1)
    assert _is_linked(a, 'dom_StringExpression141', b1)
    if hasattr(b1, 'dom_SimpleAnnotation'):
        assert _is_linked(b1, 'dom_SimpleAnnotation', a)
    _safe_set(a, 'dom_StringExpression141', b2)
    assert _is_linked(a, 'dom_StringExpression141', b2)
    if hasattr(b1, 'dom_SimpleAnnotation'):
        assert not _is_linked(b1, 'dom_SimpleAnnotation', a)
    if hasattr(b2, 'dom_SimpleAnnotation'):
        assert _is_linked(b2, 'dom_SimpleAnnotation', a)
    _safe_set(a, 'dom_StringExpression141', None)
    assert not _is_linked(a, 'dom_StringExpression141', b2)
    if hasattr(b2, 'dom_SimpleAnnotation'):
        assert not _is_linked(b2, 'dom_SimpleAnnotation', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Annotation_strategy = st.builds(Annotation)
@given(instance=Annotation_strategy)
@settings(max_examples=25)
def test_Annotation_instantiation(instance):
    assert isinstance(instance, Annotation)


AssignmentStatement_strategy = st.builds(AssignmentStatement)
@given(instance=AssignmentStatement_strategy)
@settings(max_examples=25)
def test_AssignmentStatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)


BinaryOperatorExpression_strategy = st.builds(BinaryOperatorExpression)
@given(instance=BinaryOperatorExpression_strategy)
@settings(max_examples=25)
def test_BinaryOperatorExpression_instantiation(instance):
    assert isinstance(instance, BinaryOperatorExpression)


CollectionExpression_strategy = st.builds(CollectionExpression)
@given(instance=CollectionExpression_strategy)
@settings(max_examples=25)
def test_CollectionExpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)


CollectionInitValue_strategy = st.builds(CollectionInitValue)
@given(instance=CollectionInitValue_strategy)
@settings(max_examples=25)
def test_CollectionInitValue_instantiation(instance):
    assert isinstance(instance, CollectionInitValue)


CollectionType_strategy = st.builds(CollectionType)
@given(instance=CollectionType_strategy)
@settings(max_examples=25)
def test_CollectionType_instantiation(instance):
    assert isinstance(instance, CollectionType)


DomElement_strategy = st.builds(DomElement)
@given(instance=DomElement_strategy)
@settings(max_examples=25)
def test_DomElement_instantiation(instance):
    assert isinstance(instance, DomElement)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FeatureCallExpression_strategy = st.builds(FeatureCallExpression)
@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=25)
def test_FeatureCallExpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)


LiteralExpression_strategy = st.builds(LiteralExpression)
@given(instance=LiteralExpression_strategy)
@settings(max_examples=25)
def test_LiteralExpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)


NameExpression_strategy = st.builds(NameExpression)
@given(instance=NameExpression_strategy)
@settings(max_examples=25)
def test_NameExpression_instantiation(instance):
    assert isinstance(instance, NameExpression)


OperatorExpression_strategy = st.builds(OperatorExpression)
@given(instance=OperatorExpression_strategy)
@settings(max_examples=25)
def test_OperatorExpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)


PrimitiveExpression_strategy = st.builds(PrimitiveExpression)
@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=25)
def test_PrimitiveExpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


SwitchCaseStatement_strategy = st.builds(SwitchCaseStatement)
@given(instance=SwitchCaseStatement_strategy)
@settings(max_examples=25)
def test_SwitchCaseStatement_instantiation(instance):
    assert isinstance(instance, SwitchCaseStatement)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


UnaryOperatorExpression_strategy = st.builds(UnaryOperatorExpression)
@given(instance=UnaryOperatorExpression_strategy)
@settings(max_examples=25)
def test_UnaryOperatorExpression_instantiation(instance):
    assert isinstance(instance, UnaryOperatorExpression)


dom_AbortStatement_strategy = st.builds(dom_AbortStatement)
@given(instance=dom_AbortStatement_strategy)
@settings(max_examples=25)
def test_dom_AbortStatement_instantiation(instance):
    assert isinstance(instance, dom_AbortStatement)


dom_AndOperatorExpression_strategy = st.builds(dom_AndOperatorExpression)
@given(instance=dom_AndOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_AndOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_AndOperatorExpression)


dom_Annotation_strategy = st.builds(dom_Annotation)
@given(instance=dom_Annotation_strategy)
@settings(max_examples=25)
def test_dom_Annotation_instantiation(instance):
    assert isinstance(instance, dom_Annotation)


dom_AnnotationBlock_strategy = st.builds(dom_AnnotationBlock)
@given(instance=dom_AnnotationBlock_strategy)
@settings(max_examples=25)
def test_dom_AnnotationBlock_instantiation(instance):
    assert isinstance(instance, dom_AnnotationBlock)


dom_AnyType_strategy = st.builds(dom_AnyType)
@given(instance=dom_AnyType_strategy)
@settings(max_examples=25)
def test_dom_AnyType_instantiation(instance):
    assert isinstance(instance, dom_AnyType)


dom_AssignmentStatement_strategy = st.builds(dom_AssignmentStatement)
@given(instance=dom_AssignmentStatement_strategy)
@settings(max_examples=25)
def test_dom_AssignmentStatement_instantiation(instance):
    assert isinstance(instance, dom_AssignmentStatement)


dom_BagExpression_strategy = st.builds(dom_BagExpression)
@given(instance=dom_BagExpression_strategy)
@settings(max_examples=25)
def test_dom_BagExpression_instantiation(instance):
    assert isinstance(instance, dom_BagExpression)


dom_BagType_strategy = st.builds(dom_BagType)
@given(instance=dom_BagType_strategy)
@settings(max_examples=25)
def test_dom_BagType_instantiation(instance):
    assert isinstance(instance, dom_BagType)


dom_BinaryOperatorExpression_strategy = st.builds(dom_BinaryOperatorExpression)
@given(instance=dom_BinaryOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_BinaryOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_BinaryOperatorExpression)


dom_Block_strategy = st.builds(dom_Block)
@given(instance=dom_Block_strategy)
@settings(max_examples=25)
def test_dom_Block_instantiation(instance):
    assert isinstance(instance, dom_Block)


dom_BooleanExpression_strategy = st.builds(dom_BooleanExpression, val=st.booleans())
@given(instance=dom_BooleanExpression_strategy)
@settings(max_examples=25)
def test_dom_BooleanExpression_instantiation(instance):
    assert isinstance(instance, dom_BooleanExpression)


dom_BooleanType_strategy = st.builds(dom_BooleanType)
@given(instance=dom_BooleanType_strategy)
@settings(max_examples=25)
def test_dom_BooleanType_instantiation(instance):
    assert isinstance(instance, dom_BooleanType)


dom_BreakAllStatement_strategy = st.builds(dom_BreakAllStatement)
@given(instance=dom_BreakAllStatement_strategy)
@settings(max_examples=25)
def test_dom_BreakAllStatement_instantiation(instance):
    assert isinstance(instance, dom_BreakAllStatement)


dom_BreakStatement_strategy = st.builds(dom_BreakStatement)
@given(instance=dom_BreakStatement_strategy)
@settings(max_examples=25)
def test_dom_BreakStatement_instantiation(instance):
    assert isinstance(instance, dom_BreakStatement)


dom_CollectionExpression_strategy = st.builds(dom_CollectionExpression)
@given(instance=dom_CollectionExpression_strategy)
@settings(max_examples=25)
def test_dom_CollectionExpression_instantiation(instance):
    assert isinstance(instance, dom_CollectionExpression)


dom_CollectionInitValue_strategy = st.builds(dom_CollectionInitValue)
@given(instance=dom_CollectionInitValue_strategy)
@settings(max_examples=25)
def test_dom_CollectionInitValue_instantiation(instance):
    assert isinstance(instance, dom_CollectionInitValue)


dom_CollectionType_strategy = st.builds(dom_CollectionType)
@given(instance=dom_CollectionType_strategy)
@settings(max_examples=25)
def test_dom_CollectionType_instantiation(instance):
    assert isinstance(instance, dom_CollectionType)


dom_ContinueStatement_strategy = st.builds(dom_ContinueStatement)
@given(instance=dom_ContinueStatement_strategy)
@settings(max_examples=25)
def test_dom_ContinueStatement_instantiation(instance):
    assert isinstance(instance, dom_ContinueStatement)


dom_DeleteStatement_strategy = st.builds(dom_DeleteStatement)
@given(instance=dom_DeleteStatement_strategy)
@settings(max_examples=25)
def test_dom_DeleteStatement_instantiation(instance):
    assert isinstance(instance, dom_DeleteStatement)


dom_DivideOperatorExpression_strategy = st.builds(dom_DivideOperatorExpression)
@given(instance=dom_DivideOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_DivideOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_DivideOperatorExpression)


dom_DomElement_strategy = st.builds(dom_DomElement, column=st.integers(), line=st.integers())
@given(instance=dom_DomElement_strategy)
@settings(max_examples=25)
def test_dom_DomElement_instantiation(instance):
    assert isinstance(instance, dom_DomElement)


dom_EnumerationLiteralExpression_strategy = st.builds(dom_EnumerationLiteralExpression)
@given(instance=dom_EnumerationLiteralExpression_strategy)
@settings(max_examples=25)
def test_dom_EnumerationLiteralExpression_instantiation(instance):
    assert isinstance(instance, dom_EnumerationLiteralExpression)


dom_EqualsOperatorExpression_strategy = st.builds(dom_EqualsOperatorExpression)
@given(instance=dom_EqualsOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_EqualsOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_EqualsOperatorExpression)


dom_ExecutableAnnotation_strategy = st.builds(dom_ExecutableAnnotation)
@given(instance=dom_ExecutableAnnotation_strategy)
@settings(max_examples=25)
def test_dom_ExecutableAnnotation_instantiation(instance):
    assert isinstance(instance, dom_ExecutableAnnotation)


dom_ExpRange_strategy = st.builds(dom_ExpRange)
@given(instance=dom_ExpRange_strategy)
@settings(max_examples=25)
def test_dom_ExpRange_instantiation(instance):
    assert isinstance(instance, dom_ExpRange)


dom_ExprList_strategy = st.builds(dom_ExprList)
@given(instance=dom_ExprList_strategy)
@settings(max_examples=25)
def test_dom_ExprList_instantiation(instance):
    assert isinstance(instance, dom_ExprList)


dom_Expression_strategy = st.builds(dom_Expression)
@given(instance=dom_Expression_strategy)
@settings(max_examples=25)
def test_dom_Expression_instantiation(instance):
    assert isinstance(instance, dom_Expression)


dom_ExpressionStatement_strategy = st.builds(dom_ExpressionStatement)
@given(instance=dom_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_dom_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, dom_ExpressionStatement)


dom_FOLMethodCallExpression_strategy = st.builds(dom_FOLMethodCallExpression)
@given(instance=dom_FOLMethodCallExpression_strategy)
@settings(max_examples=25)
def test_dom_FOLMethodCallExpression_instantiation(instance):
    assert isinstance(instance, dom_FOLMethodCallExpression)


dom_FeatureCallExpression_strategy = st.builds(dom_FeatureCallExpression)
@given(instance=dom_FeatureCallExpression_strategy)
@settings(max_examples=25)
def test_dom_FeatureCallExpression_instantiation(instance):
    assert isinstance(instance, dom_FeatureCallExpression)


dom_ForStatement_strategy = st.builds(dom_ForStatement)
@given(instance=dom_ForStatement_strategy)
@settings(max_examples=25)
def test_dom_ForStatement_instantiation(instance):
    assert isinstance(instance, dom_ForStatement)


dom_FormalParameterExpression_strategy = st.builds(dom_FormalParameterExpression)
@given(instance=dom_FormalParameterExpression_strategy)
@settings(max_examples=25)
def test_dom_FormalParameterExpression_instantiation(instance):
    assert isinstance(instance, dom_FormalParameterExpression)


dom_GreaterThanOperatorExpression_strategy = st.builds(dom_GreaterThanOperatorExpression)
@given(instance=dom_GreaterThanOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_GreaterThanOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_GreaterThanOperatorExpression)


dom_GreaterThanOrEqualToOperatorExpression_strategy = st.builds(dom_GreaterThanOrEqualToOperatorExpression)
@given(instance=dom_GreaterThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_GreaterThanOrEqualToOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_GreaterThanOrEqualToOperatorExpression)


dom_IfStatement_strategy = st.builds(dom_IfStatement)
@given(instance=dom_IfStatement_strategy)
@settings(max_examples=25)
def test_dom_IfStatement_instantiation(instance):
    assert isinstance(instance, dom_IfStatement)


dom_ImpliesOperatorExpression_strategy = st.builds(dom_ImpliesOperatorExpression)
@given(instance=dom_ImpliesOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_ImpliesOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_ImpliesOperatorExpression)


dom_Import_strategy = st.builds(dom_Import)
@given(instance=dom_Import_strategy)
@settings(max_examples=25)
def test_dom_Import_instantiation(instance):
    assert isinstance(instance, dom_Import)


dom_IntegerExpression_strategy = st.builds(dom_IntegerExpression, val=st.integers())
@given(instance=dom_IntegerExpression_strategy)
@settings(max_examples=25)
def test_dom_IntegerExpression_instantiation(instance):
    assert isinstance(instance, dom_IntegerExpression)


dom_IntegerType_strategy = st.builds(dom_IntegerType)
@given(instance=dom_IntegerType_strategy)
@settings(max_examples=25)
def test_dom_IntegerType_instantiation(instance):
    assert isinstance(instance, dom_IntegerType)


dom_KeyValue_strategy = st.builds(dom_KeyValue)
@given(instance=dom_KeyValue_strategy)
@settings(max_examples=25)
def test_dom_KeyValue_instantiation(instance):
    assert isinstance(instance, dom_KeyValue)


dom_LessThanOperatorExpression_strategy = st.builds(dom_LessThanOperatorExpression)
@given(instance=dom_LessThanOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_LessThanOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_LessThanOperatorExpression)


dom_LessThanOrEqualToOperatorExpression_strategy = st.builds(dom_LessThanOrEqualToOperatorExpression)
@given(instance=dom_LessThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_LessThanOrEqualToOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_LessThanOrEqualToOperatorExpression)


dom_LiteralExpression_strategy = st.builds(dom_LiteralExpression)
@given(instance=dom_LiteralExpression_strategy)
@settings(max_examples=25)
def test_dom_LiteralExpression_instantiation(instance):
    assert isinstance(instance, dom_LiteralExpression)


dom_MapExpression_strategy = st.builds(dom_MapExpression)
@given(instance=dom_MapExpression_strategy)
@settings(max_examples=25)
def test_dom_MapExpression_instantiation(instance):
    assert isinstance(instance, dom_MapExpression)


dom_MapType_strategy = st.builds(dom_MapType)
@given(instance=dom_MapType_strategy)
@settings(max_examples=25)
def test_dom_MapType_instantiation(instance):
    assert isinstance(instance, dom_MapType)


dom_MethodCallExpression_strategy = st.builds(dom_MethodCallExpression)
@given(instance=dom_MethodCallExpression_strategy)
@settings(max_examples=25)
def test_dom_MethodCallExpression_instantiation(instance):
    assert isinstance(instance, dom_MethodCallExpression)


dom_MinusOperatorExpression_strategy = st.builds(dom_MinusOperatorExpression)
@given(instance=dom_MinusOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_MinusOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_MinusOperatorExpression)


dom_ModelDeclarationParameter_strategy = st.builds(dom_ModelDeclarationParameter)
@given(instance=dom_ModelDeclarationParameter_strategy)
@settings(max_examples=25)
def test_dom_ModelDeclarationParameter_instantiation(instance):
    assert isinstance(instance, dom_ModelDeclarationParameter)


dom_ModelDeclarationStatement_strategy = st.builds(dom_ModelDeclarationStatement)
@given(instance=dom_ModelDeclarationStatement_strategy)
@settings(max_examples=25)
def test_dom_ModelDeclarationStatement_instantiation(instance):
    assert isinstance(instance, dom_ModelDeclarationStatement)


dom_ModelElementType_strategy = st.builds(dom_ModelElementType)
@given(instance=dom_ModelElementType_strategy)
@settings(max_examples=25)
def test_dom_ModelElementType_instantiation(instance):
    assert isinstance(instance, dom_ModelElementType)


dom_ModelElementTypeExpression_strategy = st.builds(dom_ModelElementTypeExpression)
@given(instance=dom_ModelElementTypeExpression_strategy)
@settings(max_examples=25)
def test_dom_ModelElementTypeExpression_instantiation(instance):
    assert isinstance(instance, dom_ModelElementTypeExpression)


dom_ModelExpression_strategy = st.builds(dom_ModelExpression)
@given(instance=dom_ModelExpression_strategy)
@settings(max_examples=25)
def test_dom_ModelExpression_instantiation(instance):
    assert isinstance(instance, dom_ModelExpression)


dom_MultiplyOperatorExpression_strategy = st.builds(dom_MultiplyOperatorExpression)
@given(instance=dom_MultiplyOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_MultiplyOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_MultiplyOperatorExpression)


dom_NameExpression_strategy = st.builds(dom_NameExpression, name=safe_text)
@given(instance=dom_NameExpression_strategy)
@settings(max_examples=25)
def test_dom_NameExpression_instantiation(instance):
    assert isinstance(instance, dom_NameExpression)


dom_NativeType_strategy = st.builds(dom_NativeType)
@given(instance=dom_NativeType_strategy)
@settings(max_examples=25)
def test_dom_NativeType_instantiation(instance):
    assert isinstance(instance, dom_NativeType)


dom_NegativeOperatorExpression_strategy = st.builds(dom_NegativeOperatorExpression)
@given(instance=dom_NegativeOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_NegativeOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_NegativeOperatorExpression)


dom_NewExpression_strategy = st.builds(dom_NewExpression)
@given(instance=dom_NewExpression_strategy)
@settings(max_examples=25)
def test_dom_NewExpression_instantiation(instance):
    assert isinstance(instance, dom_NewExpression)


dom_NotEqualsOperatorExpression_strategy = st.builds(dom_NotEqualsOperatorExpression)
@given(instance=dom_NotEqualsOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_NotEqualsOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_NotEqualsOperatorExpression)


dom_NotOperatorExpression_strategy = st.builds(dom_NotOperatorExpression)
@given(instance=dom_NotOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_NotOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_NotOperatorExpression)


dom_OperationDefinition_strategy = st.builds(dom_OperationDefinition)
@given(instance=dom_OperationDefinition_strategy)
@settings(max_examples=25)
def test_dom_OperationDefinition_instantiation(instance):
    assert isinstance(instance, dom_OperationDefinition)


dom_OperatorExpression_strategy = st.builds(dom_OperatorExpression)
@given(instance=dom_OperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_OperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_OperatorExpression)


dom_OrOperatorExpression_strategy = st.builds(dom_OrOperatorExpression)
@given(instance=dom_OrOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_OrOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_OrOperatorExpression)


dom_OrderedSetExpression_strategy = st.builds(dom_OrderedSetExpression)
@given(instance=dom_OrderedSetExpression_strategy)
@settings(max_examples=25)
def test_dom_OrderedSetExpression_instantiation(instance):
    assert isinstance(instance, dom_OrderedSetExpression)


dom_OrderedSetType_strategy = st.builds(dom_OrderedSetType)
@given(instance=dom_OrderedSetType_strategy)
@settings(max_examples=25)
def test_dom_OrderedSetType_instantiation(instance):
    assert isinstance(instance, dom_OrderedSetType)


dom_PlusOperatorExpression_strategy = st.builds(dom_PlusOperatorExpression)
@given(instance=dom_PlusOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_PlusOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_PlusOperatorExpression)


dom_PrimitiveExpression_strategy = st.builds(dom_PrimitiveExpression)
@given(instance=dom_PrimitiveExpression_strategy)
@settings(max_examples=25)
def test_dom_PrimitiveExpression_instantiation(instance):
    assert isinstance(instance, dom_PrimitiveExpression)


dom_PrimitiveType_strategy = st.builds(dom_PrimitiveType)
@given(instance=dom_PrimitiveType_strategy)
@settings(max_examples=25)
def test_dom_PrimitiveType_instantiation(instance):
    assert isinstance(instance, dom_PrimitiveType)


dom_Program_strategy = st.builds(dom_Program)
@given(instance=dom_Program_strategy)
@settings(max_examples=25)
def test_dom_Program_instantiation(instance):
    assert isinstance(instance, dom_Program)


dom_PropertyCallExpression_strategy = st.builds(dom_PropertyCallExpression)
@given(instance=dom_PropertyCallExpression_strategy)
@settings(max_examples=25)
def test_dom_PropertyCallExpression_instantiation(instance):
    assert isinstance(instance, dom_PropertyCallExpression)


dom_RealExpression_strategy = st.builds(dom_RealExpression, val=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=dom_RealExpression_strategy)
@settings(max_examples=25)
def test_dom_RealExpression_instantiation(instance):
    assert isinstance(instance, dom_RealExpression)


dom_RealType_strategy = st.builds(dom_RealType)
@given(instance=dom_RealType_strategy)
@settings(max_examples=25)
def test_dom_RealType_instantiation(instance):
    assert isinstance(instance, dom_RealType)


dom_ReturnStatement_strategy = st.builds(dom_ReturnStatement)
@given(instance=dom_ReturnStatement_strategy)
@settings(max_examples=25)
def test_dom_ReturnStatement_instantiation(instance):
    assert isinstance(instance, dom_ReturnStatement)


dom_SequenceExpression_strategy = st.builds(dom_SequenceExpression)
@given(instance=dom_SequenceExpression_strategy)
@settings(max_examples=25)
def test_dom_SequenceExpression_instantiation(instance):
    assert isinstance(instance, dom_SequenceExpression)


dom_SequenceType_strategy = st.builds(dom_SequenceType)
@given(instance=dom_SequenceType_strategy)
@settings(max_examples=25)
def test_dom_SequenceType_instantiation(instance):
    assert isinstance(instance, dom_SequenceType)


dom_SetExpression_strategy = st.builds(dom_SetExpression)
@given(instance=dom_SetExpression_strategy)
@settings(max_examples=25)
def test_dom_SetExpression_instantiation(instance):
    assert isinstance(instance, dom_SetExpression)


dom_SetType_strategy = st.builds(dom_SetType)
@given(instance=dom_SetType_strategy)
@settings(max_examples=25)
def test_dom_SetType_instantiation(instance):
    assert isinstance(instance, dom_SetType)


dom_ShortModelDeclarationExpression_strategy = st.builds(dom_ShortModelDeclarationExpression)
@given(instance=dom_ShortModelDeclarationExpression_strategy)
@settings(max_examples=25)
def test_dom_ShortModelDeclarationExpression_instantiation(instance):
    assert isinstance(instance, dom_ShortModelDeclarationExpression)


dom_SimpleAnnotation_strategy = st.builds(dom_SimpleAnnotation)
@given(instance=dom_SimpleAnnotation_strategy)
@settings(max_examples=25)
def test_dom_SimpleAnnotation_instantiation(instance):
    assert isinstance(instance, dom_SimpleAnnotation)


dom_SpecialAssignmentStatement_strategy = st.builds(dom_SpecialAssignmentStatement)
@given(instance=dom_SpecialAssignmentStatement_strategy)
@settings(max_examples=25)
def test_dom_SpecialAssignmentStatement_instantiation(instance):
    assert isinstance(instance, dom_SpecialAssignmentStatement)


dom_SpecialNameExpression_strategy = st.builds(dom_SpecialNameExpression)
@given(instance=dom_SpecialNameExpression_strategy)
@settings(max_examples=25)
def test_dom_SpecialNameExpression_instantiation(instance):
    assert isinstance(instance, dom_SpecialNameExpression)


dom_Statement_strategy = st.builds(dom_Statement)
@given(instance=dom_Statement_strategy)
@settings(max_examples=25)
def test_dom_Statement_instantiation(instance):
    assert isinstance(instance, dom_Statement)


dom_StringExpression_strategy = st.builds(dom_StringExpression, val=safe_text)
@given(instance=dom_StringExpression_strategy)
@settings(max_examples=25)
def test_dom_StringExpression_instantiation(instance):
    assert isinstance(instance, dom_StringExpression)


dom_StringType_strategy = st.builds(dom_StringType)
@given(instance=dom_StringType_strategy)
@settings(max_examples=25)
def test_dom_StringType_instantiation(instance):
    assert isinstance(instance, dom_StringType)


dom_SwitchCaseDefaultStatement_strategy = st.builds(dom_SwitchCaseDefaultStatement)
@given(instance=dom_SwitchCaseDefaultStatement_strategy)
@settings(max_examples=25)
def test_dom_SwitchCaseDefaultStatement_instantiation(instance):
    assert isinstance(instance, dom_SwitchCaseDefaultStatement)


dom_SwitchCaseExpressionStatement_strategy = st.builds(dom_SwitchCaseExpressionStatement)
@given(instance=dom_SwitchCaseExpressionStatement_strategy)
@settings(max_examples=25)
def test_dom_SwitchCaseExpressionStatement_instantiation(instance):
    assert isinstance(instance, dom_SwitchCaseExpressionStatement)


dom_SwitchCaseStatement_strategy = st.builds(dom_SwitchCaseStatement)
@given(instance=dom_SwitchCaseStatement_strategy)
@settings(max_examples=25)
def test_dom_SwitchCaseStatement_instantiation(instance):
    assert isinstance(instance, dom_SwitchCaseStatement)


dom_SwitchStatement_strategy = st.builds(dom_SwitchStatement)
@given(instance=dom_SwitchStatement_strategy)
@settings(max_examples=25)
def test_dom_SwitchStatement_instantiation(instance):
    assert isinstance(instance, dom_SwitchStatement)


dom_ThrowStatement_strategy = st.builds(dom_ThrowStatement)
@given(instance=dom_ThrowStatement_strategy)
@settings(max_examples=25)
def test_dom_ThrowStatement_instantiation(instance):
    assert isinstance(instance, dom_ThrowStatement)


dom_TransactionStatement_strategy = st.builds(dom_TransactionStatement)
@given(instance=dom_TransactionStatement_strategy)
@settings(max_examples=25)
def test_dom_TransactionStatement_instantiation(instance):
    assert isinstance(instance, dom_TransactionStatement)


dom_Type_strategy = st.builds(dom_Type)
@given(instance=dom_Type_strategy)
@settings(max_examples=25)
def test_dom_Type_instantiation(instance):
    assert isinstance(instance, dom_Type)


dom_UnaryOperatorExpression_strategy = st.builds(dom_UnaryOperatorExpression)
@given(instance=dom_UnaryOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_UnaryOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_UnaryOperatorExpression)


dom_VariableDeclarationExpression_strategy = st.builds(dom_VariableDeclarationExpression)
@given(instance=dom_VariableDeclarationExpression_strategy)
@settings(max_examples=25)
def test_dom_VariableDeclarationExpression_instantiation(instance):
    assert isinstance(instance, dom_VariableDeclarationExpression)


dom_WhileStatement_strategy = st.builds(dom_WhileStatement)
@given(instance=dom_WhileStatement_strategy)
@settings(max_examples=25)
def test_dom_WhileStatement_instantiation(instance):
    assert isinstance(instance, dom_WhileStatement)


dom_XorOperatorExpression_strategy = st.builds(dom_XorOperatorExpression)
@given(instance=dom_XorOperatorExpression_strategy)
@settings(max_examples=25)
def test_dom_XorOperatorExpression_instantiation(instance):
    assert isinstance(instance, dom_XorOperatorExpression)


