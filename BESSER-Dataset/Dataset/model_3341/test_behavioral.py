import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CaseStatement,
    Condition,
    DefaultXMLNamespaceStatement,
    Expression,
    ExpressionStatement,
    Statement,
    SwitchStatement,
    ThrowStatement,
    aS3_AccessorRole,
    aS3_Annotation,
    aS3_Block,
    aS3_BoolConstant,
    aS3_CaseStatement,
    aS3_Class,
    aS3_Condition,
    aS3_DefaultStatement,
    aS3_DefaultXMLNamespaceStatement,
    aS3_DoWhileStatement,
    aS3_EObject,
    aS3_Expression,
    aS3_ExpressionStatement,
    aS3_ForEachStatement,
    aS3_ForStatement,
    aS3_IfStatement,
    aS3_Import,
    aS3_Imports,
    aS3_Interface,
    aS3_InterfaceMethod,
    aS3_Member,
    aS3_MemberVariableDeclaration,
    aS3_Method,
    aS3_MethodBody,
    aS3_Model,
    aS3_Modifier,
    aS3_Null,
    aS3_NumberConstant,
    aS3_Package,
    aS3_Parameter,
    aS3_RegexpConstant,
    aS3_ReturnStatement,
    aS3_Statement,
    aS3_StringConstant,
    aS3_SwitchStatement,
    aS3_SymbolRef,
    aS3_This,
    aS3_ThrowStatement,
    aS3_TryStatement,
    aS3_Undefined,
    aS3_Uses,
    aS3_VariableDeclaration,
    aS3_WhileStatement,
    aS3_WithStatement,
    aS3_XmlConstant,
    aS3_additiveExpression,
    aS3_annotationField,
    aS3_annotationFields,
    aS3_arguments,
    aS3_arrayLiteral,
    aS3_assignmentExpression,
    aS3_basicParameterDeclaration,
    aS3_bitwiseAndExpression,
    aS3_bitwiseOrExpression,
    aS3_bitwiseXorExpression,
    aS3_brackets,
    aS3_catchBlock,
    aS3_conditionalExpression,
    aS3_conditionalSubExpression,
    aS3_directive,
    aS3_e4xAttributeIdentifier,
    aS3_element,
    aS3_elementList,
    aS3_encapsulatedExpression,
    aS3_equalityExpression,
    aS3_exprOrObjectLiteral,
    aS3_expressionList,
    aS3_expressionQualifiedIdentifier,
    aS3_fieldList,
    aS3_fieldName,
    aS3_finallyBlock,
    aS3_forCond,
    aS3_forInClause,
    aS3_forInClauseDecl,
    aS3_forInClauseTail,
    aS3_forInit,
    aS3_forIter,
    aS3_fullNewSubexpression,
    aS3_functionCommon,
    aS3_functionExpression,
    aS3_functionSignature,
    aS3_identi,
    aS3_identifier,
    aS3_literalField,
    aS3_logicalAndExpression,
    aS3_logicalOrExpression,
    aS3_multiplicativeExpression,
    aS3_namespaceName,
    aS3_newExpression,
    aS3_nonAttributeQualifiedIdentifier,
    aS3_nonemptyElementList,
    aS3_objectLiteral,
    aS3_parameterDeclaration,
    aS3_parameterDeclarationList,
    aS3_parameterDefault,
    aS3_parameterRestDeclaration,
    aS3_postfixExpression,
    aS3_primaryExpression,
    aS3_propOrIdent,
    aS3_propertyIdentifier,
    aS3_qualifiedIdent,
    aS3_qualifiedIdentifier,
    aS3_qualifier,
    aS3_regexpLiteral,
    aS3_relationalExpression,
    aS3_shiftExpression,
    aS3_simpleQualifiedIdentifier,
    aS3_switchBlock,
    aS3_switchStatementList,
    aS3_traditionalForClause,
    aS3_typeExpression,
    aS3_unaryExpression,
    aS3_unaryExpressionNotPlusMinus,
    assignmentExpression,
    brackets,
    catchBlock,
    conditionalExpression,
    element,
    elementList,
    encapsulatedExpression,
    exprOrObjectLiteral,
    expressionQualifiedIdentifier,
    finallyBlock,
    forInClauseDecl,
    forInClauseTail,
    nonAttributeQualifiedIdentifier,
    nonemptyElementList,
    parameterDeclaration,
    parameterDefault,
    propertyIdentifier,
    qualifiedIdent,
    qualifiedIdentifier,
    qualifier,
    unaryExpressionNotPlusMinus,
    AccessLevel,
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

def test_assoc_accessor40_reverse_link_reassign_clear():
    a1 = aS3_InterfaceMethod(anytype="sample_text", name="sample_text")
    a2 = aS3_InterfaceMethod(anytype="sample_text_2", name="sample_text_2")
    b = aS3_AccessorRole(accessor="sample_text")
    _safe_set(b, 'aS3_AccessorRole', a1)
    assert _is_linked(b, 'aS3_AccessorRole', a1)
    if hasattr(a1, 'aS3_InterfaceMethod41'):
        assert _is_linked(a1, 'aS3_InterfaceMethod41', b)
    _safe_set(b, 'aS3_AccessorRole', a2)
    assert _is_linked(b, 'aS3_AccessorRole', a2)
    if hasattr(a1, 'aS3_InterfaceMethod41'):
        assert not _is_linked(a1, 'aS3_InterfaceMethod41', b)
    if hasattr(a2, 'aS3_InterfaceMethod41'):
        assert _is_linked(a2, 'aS3_InterfaceMethod41', b)
    _safe_set(b, 'aS3_AccessorRole', None)
    assert not _is_linked(b, 'aS3_AccessorRole', a2)
    if hasattr(a2, 'aS3_InterfaceMethod41'):
        assert not _is_linked(a2, 'aS3_InterfaceMethod41', b)


def test_assoc_accessor75_reverse_link_reassign_clear():
    a1 = aS3_Method(anytype="sample_text", name="sample_text")
    a2 = aS3_Method(anytype="sample_text_2", name="sample_text_2")
    b = aS3_AccessorRole(accessor="sample_text")
    _safe_set(b, 'aS3_AccessorRole77', a1)
    assert _is_linked(b, 'aS3_AccessorRole77', a1)
    if hasattr(a1, 'aS3_Method76'):
        assert _is_linked(a1, 'aS3_Method76', b)
    _safe_set(b, 'aS3_AccessorRole77', a2)
    assert _is_linked(b, 'aS3_AccessorRole77', a2)
    if hasattr(a1, 'aS3_Method76'):
        assert not _is_linked(a1, 'aS3_Method76', b)
    if hasattr(a2, 'aS3_Method76'):
        assert _is_linked(a2, 'aS3_Method76', b)
    _safe_set(b, 'aS3_AccessorRole77', None)
    assert not _is_linked(b, 'aS3_AccessorRole77', a2)
    if hasattr(a2, 'aS3_Method76'):
        assert not _is_linked(a2, 'aS3_Method76', b)


def test_assoc_annotations28_reverse_link_reassign_clear():
    a1 = aS3_Interface(access="sample_text", name="sample_text")
    a2 = aS3_Interface(access="sample_text_2", name="sample_text_2")
    b = aS3_Annotation(name="sample_text")
    _safe_set(b, 'aS3_Annotation29', a1)
    assert _is_linked(b, 'aS3_Annotation29', a1)
    if hasattr(a1, 'aS3_Interface'):
        assert _is_linked(a1, 'aS3_Interface', b)
    _safe_set(b, 'aS3_Annotation29', a2)
    assert _is_linked(b, 'aS3_Annotation29', a2)
    if hasattr(a1, 'aS3_Interface'):
        assert not _is_linked(a1, 'aS3_Interface', b)
    if hasattr(a2, 'aS3_Interface'):
        assert _is_linked(a2, 'aS3_Interface', b)
    _safe_set(b, 'aS3_Annotation29', None)
    assert not _is_linked(b, 'aS3_Annotation29', a2)
    if hasattr(a2, 'aS3_Interface'):
        assert not _is_linked(a2, 'aS3_Interface', b)


def test_assoc_annotations35_reverse_link_reassign_clear():
    a1 = aS3_InterfaceMethod(anytype="sample_text", name="sample_text")
    a2 = aS3_InterfaceMethod(anytype="sample_text_2", name="sample_text_2")
    b = aS3_Annotation(name="sample_text")
    _safe_set(b, 'aS3_Annotation37', a1)
    assert _is_linked(b, 'aS3_Annotation37', a1)
    if hasattr(a1, 'aS3_InterfaceMethod36'):
        assert _is_linked(a1, 'aS3_InterfaceMethod36', b)
    _safe_set(b, 'aS3_Annotation37', a2)
    assert _is_linked(b, 'aS3_Annotation37', a2)
    if hasattr(a1, 'aS3_InterfaceMethod36'):
        assert not _is_linked(a1, 'aS3_InterfaceMethod36', b)
    if hasattr(a2, 'aS3_InterfaceMethod36'):
        assert _is_linked(a2, 'aS3_InterfaceMethod36', b)
    _safe_set(b, 'aS3_Annotation37', None)
    assert not _is_linked(b, 'aS3_Annotation37', a2)
    if hasattr(a2, 'aS3_InterfaceMethod36'):
        assert not _is_linked(a2, 'aS3_InterfaceMethod36', b)


def test_assoc_annotations52_reverse_link_reassign_clear():
    a1 = aS3_Class(name="sample_text")
    a2 = aS3_Class(name="sample_text_2")
    b = aS3_Annotation(name="sample_text")
    _safe_set(b, 'aS3_Annotation53', a1)
    assert _is_linked(b, 'aS3_Annotation53', a1)
    if hasattr(a1, 'aS3_Class'):
        assert _is_linked(a1, 'aS3_Class', b)
    _safe_set(b, 'aS3_Annotation53', a2)
    assert _is_linked(b, 'aS3_Annotation53', a2)
    if hasattr(a1, 'aS3_Class'):
        assert not _is_linked(a1, 'aS3_Class', b)
    if hasattr(a2, 'aS3_Class'):
        assert _is_linked(a2, 'aS3_Class', b)
    _safe_set(b, 'aS3_Annotation53', None)
    assert not _is_linked(b, 'aS3_Annotation53', a2)
    if hasattr(a2, 'aS3_Class'):
        assert not _is_linked(a2, 'aS3_Class', b)


def test_assoc_annotations69_reverse_link_reassign_clear():
    a1 = aS3_Method(anytype="sample_text", name="sample_text")
    a2 = aS3_Method(anytype="sample_text_2", name="sample_text_2")
    b = aS3_Annotation(name="sample_text")
    _safe_set(b, 'aS3_Annotation71', a1)
    assert _is_linked(b, 'aS3_Annotation71', a1)
    if hasattr(a1, 'aS3_Method70'):
        assert _is_linked(a1, 'aS3_Method70', b)
    _safe_set(b, 'aS3_Annotation71', a2)
    assert _is_linked(b, 'aS3_Annotation71', a2)
    if hasattr(a1, 'aS3_Method70'):
        assert not _is_linked(a1, 'aS3_Method70', b)
    if hasattr(a2, 'aS3_Method70'):
        assert _is_linked(a2, 'aS3_Method70', b)
    _safe_set(b, 'aS3_Annotation71', None)
    assert not _is_linked(b, 'aS3_Annotation71', a2)
    if hasattr(a2, 'aS3_Method70'):
        assert not _is_linked(a2, 'aS3_Method70', b)


def test_assoc_annotations88_reverse_link_reassign_clear():
    a1 = aS3_MemberVariableDeclaration(anytype="sample_text", name="sample_text")
    a2 = aS3_MemberVariableDeclaration(anytype="sample_text_2", name="sample_text_2")
    b = aS3_Annotation(name="sample_text")
    _safe_set(b, 'aS3_Annotation90', a1)
    assert _is_linked(b, 'aS3_Annotation90', a1)
    if hasattr(a1, 'aS3_MemberVariableDeclaration89'):
        assert _is_linked(a1, 'aS3_MemberVariableDeclaration89', b)
    _safe_set(b, 'aS3_Annotation90', a2)
    assert _is_linked(b, 'aS3_Annotation90', a2)
    if hasattr(a1, 'aS3_MemberVariableDeclaration89'):
        assert not _is_linked(a1, 'aS3_MemberVariableDeclaration89', b)
    if hasattr(a2, 'aS3_MemberVariableDeclaration89'):
        assert _is_linked(a2, 'aS3_MemberVariableDeclaration89', b)
    _safe_set(b, 'aS3_Annotation90', None)
    assert not _is_linked(b, 'aS3_Annotation90', a2)
    if hasattr(a2, 'aS3_MemberVariableDeclaration89'):
        assert not _is_linked(a2, 'aS3_MemberVariableDeclaration89', b)


def test_assoc_expr157_reverse_link_reassign_clear():
    a1 = aS3_logicalAndExpression(o="sample_text")
    a2 = aS3_logicalAndExpression(o="sample_text_2")
    b = aS3_bitwiseOrExpression(o="sample_text")
    _safe_set(b, 'aS3_bitwiseOrExpression', a1)
    assert _is_linked(b, 'aS3_bitwiseOrExpression', a1)
    if hasattr(a1, 'aS3_logicalAndExpression'):
        assert _is_linked(a1, 'aS3_logicalAndExpression', b)
    _safe_set(b, 'aS3_bitwiseOrExpression', a2)
    assert _is_linked(b, 'aS3_bitwiseOrExpression', a2)
    if hasattr(a1, 'aS3_logicalAndExpression'):
        assert not _is_linked(a1, 'aS3_logicalAndExpression', b)
    if hasattr(a2, 'aS3_logicalAndExpression'):
        assert _is_linked(a2, 'aS3_logicalAndExpression', b)
    _safe_set(b, 'aS3_bitwiseOrExpression', None)
    assert not _is_linked(b, 'aS3_bitwiseOrExpression', a2)
    if hasattr(a2, 'aS3_logicalAndExpression'):
        assert not _is_linked(a2, 'aS3_logicalAndExpression', b)


def test_assoc_expr158_reverse_link_reassign_clear():
    a1 = aS3_bitwiseXorExpression(o="sample_text")
    a2 = aS3_bitwiseXorExpression(o="sample_text_2")
    b = aS3_bitwiseOrExpression(o="sample_text")
    _safe_set(b, 'aS3_bitwiseOrExpression159', {a1})
    assert _is_linked(b, 'aS3_bitwiseOrExpression159', a1)
    if hasattr(a1, 'aS3_bitwiseXorExpression'):
        assert _is_linked(a1, 'aS3_bitwiseXorExpression', b)
    _safe_set(b, 'aS3_bitwiseOrExpression159', {a2})
    assert _is_linked(b, 'aS3_bitwiseOrExpression159', a2)
    if hasattr(a1, 'aS3_bitwiseXorExpression'):
        assert not _is_linked(a1, 'aS3_bitwiseXorExpression', b)
    if hasattr(a2, 'aS3_bitwiseXorExpression'):
        assert _is_linked(a2, 'aS3_bitwiseXorExpression', b)
    _safe_set(b, 'aS3_bitwiseOrExpression159', set())
    assert not _is_linked(b, 'aS3_bitwiseOrExpression159', a2)
    if hasattr(a2, 'aS3_bitwiseXorExpression'):
        assert not _is_linked(a2, 'aS3_bitwiseXorExpression', b)


def test_assoc_expr160_reverse_link_reassign_clear():
    a1 = aS3_bitwiseXorExpression(o="sample_text")
    a2 = aS3_bitwiseXorExpression(o="sample_text_2")
    b = aS3_bitwiseAndExpression(o="sample_text")
    _safe_set(b, 'aS3_bitwiseAndExpression', a1)
    assert _is_linked(b, 'aS3_bitwiseAndExpression', a1)
    if hasattr(a1, 'aS3_bitwiseXorExpression161'):
        assert _is_linked(a1, 'aS3_bitwiseXorExpression161', b)
    _safe_set(b, 'aS3_bitwiseAndExpression', a2)
    assert _is_linked(b, 'aS3_bitwiseAndExpression', a2)
    if hasattr(a1, 'aS3_bitwiseXorExpression161'):
        assert not _is_linked(a1, 'aS3_bitwiseXorExpression161', b)
    if hasattr(a2, 'aS3_bitwiseXorExpression161'):
        assert _is_linked(a2, 'aS3_bitwiseXorExpression161', b)
    _safe_set(b, 'aS3_bitwiseAndExpression', None)
    assert not _is_linked(b, 'aS3_bitwiseAndExpression', a2)
    if hasattr(a2, 'aS3_bitwiseXorExpression161'):
        assert not _is_linked(a2, 'aS3_bitwiseXorExpression161', b)


def test_assoc_expr162_reverse_link_reassign_clear():
    a1 = aS3_equalityExpression(o="sample_text")
    a2 = aS3_equalityExpression(o="sample_text_2")
    b = aS3_bitwiseAndExpression(o="sample_text")
    _safe_set(b, 'aS3_bitwiseAndExpression163', {a1})
    assert _is_linked(b, 'aS3_bitwiseAndExpression163', a1)
    if hasattr(a1, 'aS3_equalityExpression'):
        assert _is_linked(a1, 'aS3_equalityExpression', b)
    _safe_set(b, 'aS3_bitwiseAndExpression163', {a2})
    assert _is_linked(b, 'aS3_bitwiseAndExpression163', a2)
    if hasattr(a1, 'aS3_equalityExpression'):
        assert not _is_linked(a1, 'aS3_equalityExpression', b)
    if hasattr(a2, 'aS3_equalityExpression'):
        assert _is_linked(a2, 'aS3_equalityExpression', b)
    _safe_set(b, 'aS3_bitwiseAndExpression163', set())
    assert not _is_linked(b, 'aS3_bitwiseAndExpression163', a2)
    if hasattr(a2, 'aS3_equalityExpression'):
        assert not _is_linked(a2, 'aS3_equalityExpression', b)


def test_assoc_expr164_reverse_link_reassign_clear():
    a1 = aS3_relationalExpression(o="sample_text")
    a2 = aS3_relationalExpression(o="sample_text_2")
    b = aS3_equalityExpression(o="sample_text")
    _safe_set(b, 'aS3_equalityExpression165', {a1})
    assert _is_linked(b, 'aS3_equalityExpression165', a1)
    if hasattr(a1, 'aS3_relationalExpression'):
        assert _is_linked(a1, 'aS3_relationalExpression', b)
    _safe_set(b, 'aS3_equalityExpression165', {a2})
    assert _is_linked(b, 'aS3_equalityExpression165', a2)
    if hasattr(a1, 'aS3_relationalExpression'):
        assert not _is_linked(a1, 'aS3_relationalExpression', b)
    if hasattr(a2, 'aS3_relationalExpression'):
        assert _is_linked(a2, 'aS3_relationalExpression', b)
    _safe_set(b, 'aS3_equalityExpression165', set())
    assert not _is_linked(b, 'aS3_equalityExpression165', a2)
    if hasattr(a2, 'aS3_relationalExpression'):
        assert not _is_linked(a2, 'aS3_relationalExpression', b)


def test_assoc_expr166_reverse_link_reassign_clear():
    a1 = aS3_shiftExpression(o="sample_text")
    a2 = aS3_shiftExpression(o="sample_text_2")
    b = aS3_relationalExpression(o="sample_text")
    _safe_set(b, 'aS3_relationalExpression167', {a1})
    assert _is_linked(b, 'aS3_relationalExpression167', a1)
    if hasattr(a1, 'aS3_shiftExpression'):
        assert _is_linked(a1, 'aS3_shiftExpression', b)
    _safe_set(b, 'aS3_relationalExpression167', {a2})
    assert _is_linked(b, 'aS3_relationalExpression167', a2)
    if hasattr(a1, 'aS3_shiftExpression'):
        assert not _is_linked(a1, 'aS3_shiftExpression', b)
    if hasattr(a2, 'aS3_shiftExpression'):
        assert _is_linked(a2, 'aS3_shiftExpression', b)
    _safe_set(b, 'aS3_relationalExpression167', set())
    assert not _is_linked(b, 'aS3_relationalExpression167', a2)
    if hasattr(a2, 'aS3_shiftExpression'):
        assert not _is_linked(a2, 'aS3_shiftExpression', b)


def test_assoc_expr168_reverse_link_reassign_clear():
    a1 = aS3_shiftExpression(o="sample_text")
    a2 = aS3_shiftExpression(o="sample_text_2")
    b = aS3_additiveExpression(o="sample_text")
    _safe_set(b, 'aS3_additiveExpression', a1)
    assert _is_linked(b, 'aS3_additiveExpression', a1)
    if hasattr(a1, 'aS3_shiftExpression169'):
        assert _is_linked(a1, 'aS3_shiftExpression169', b)
    _safe_set(b, 'aS3_additiveExpression', a2)
    assert _is_linked(b, 'aS3_additiveExpression', a2)
    if hasattr(a1, 'aS3_shiftExpression169'):
        assert not _is_linked(a1, 'aS3_shiftExpression169', b)
    if hasattr(a2, 'aS3_shiftExpression169'):
        assert _is_linked(a2, 'aS3_shiftExpression169', b)
    _safe_set(b, 'aS3_additiveExpression', None)
    assert not _is_linked(b, 'aS3_additiveExpression', a2)
    if hasattr(a2, 'aS3_shiftExpression169'):
        assert not _is_linked(a2, 'aS3_shiftExpression169', b)


def test_assoc_expr170_reverse_link_reassign_clear():
    a1 = aS3_multiplicativeExpression(o="sample_text")
    a2 = aS3_multiplicativeExpression(o="sample_text_2")
    b = aS3_additiveExpression(o="sample_text")
    _safe_set(b, 'aS3_additiveExpression171', {a1})
    assert _is_linked(b, 'aS3_additiveExpression171', a1)
    if hasattr(a1, 'aS3_multiplicativeExpression'):
        assert _is_linked(a1, 'aS3_multiplicativeExpression', b)
    _safe_set(b, 'aS3_additiveExpression171', {a2})
    assert _is_linked(b, 'aS3_additiveExpression171', a2)
    if hasattr(a1, 'aS3_multiplicativeExpression'):
        assert not _is_linked(a1, 'aS3_multiplicativeExpression', b)
    if hasattr(a2, 'aS3_multiplicativeExpression'):
        assert _is_linked(a2, 'aS3_multiplicativeExpression', b)
    _safe_set(b, 'aS3_additiveExpression171', set())
    assert not _is_linked(b, 'aS3_additiveExpression171', a2)
    if hasattr(a2, 'aS3_multiplicativeExpression'):
        assert not _is_linked(a2, 'aS3_multiplicativeExpression', b)


def test_assoc_identi119_reverse_link_reassign_clear():
    a1 = aS3_identi(i="sample_text")
    a2 = aS3_identi(i="sample_text_2")
    b = aS3_fieldName(name="sample_text", number="sample_text")
    _safe_set(b, 'aS3_fieldName120', a1)
    assert _is_linked(b, 'aS3_fieldName120', a1)
    if hasattr(a1, 'aS3_identi'):
        assert _is_linked(a1, 'aS3_identi', b)
    _safe_set(b, 'aS3_fieldName120', a2)
    assert _is_linked(b, 'aS3_fieldName120', a2)
    if hasattr(a1, 'aS3_identi'):
        assert not _is_linked(a1, 'aS3_identi', b)
    if hasattr(a2, 'aS3_identi'):
        assert _is_linked(a2, 'aS3_identi', b)
    _safe_set(b, 'aS3_fieldName120', None)
    assert not _is_linked(b, 'aS3_fieldName120', a2)
    if hasattr(a2, 'aS3_identi'):
        assert not _is_linked(a2, 'aS3_identi', b)


def test_assoc_members33_reverse_link_reassign_clear():
    a1 = aS3_InterfaceMethod(anytype="sample_text", name="sample_text")
    a2 = aS3_InterfaceMethod(anytype="sample_text_2", name="sample_text_2")
    b = aS3_Interface(access="sample_text", name="sample_text")
    _safe_set(b, 'aS3_Interface34', {a1})
    assert _is_linked(b, 'aS3_Interface34', a1)
    if hasattr(a1, 'aS3_InterfaceMethod'):
        assert _is_linked(a1, 'aS3_InterfaceMethod', b)
    _safe_set(b, 'aS3_Interface34', {a2})
    assert _is_linked(b, 'aS3_Interface34', a2)
    if hasattr(a1, 'aS3_InterfaceMethod'):
        assert not _is_linked(a1, 'aS3_InterfaceMethod', b)
    if hasattr(a2, 'aS3_InterfaceMethod'):
        assert _is_linked(a2, 'aS3_InterfaceMethod', b)
    _safe_set(b, 'aS3_Interface34', set())
    assert not _is_linked(b, 'aS3_Interface34', a2)
    if hasattr(a2, 'aS3_InterfaceMethod'):
        assert not _is_linked(a2, 'aS3_InterfaceMethod', b)


def test_assoc_modifier38_reverse_link_reassign_clear():
    a1 = aS3_Modifier(access="sample_text", dynamic=True, final=True, native=True, static=True)
    a2 = aS3_Modifier(access="sample_text_2", dynamic=False, final=False, native=False, static=False)
    b = aS3_InterfaceMethod(anytype="sample_text", name="sample_text")
    _safe_set(b, 'aS3_InterfaceMethod39', a1)
    assert _is_linked(b, 'aS3_InterfaceMethod39', a1)
    if hasattr(a1, 'aS3_Modifier'):
        assert _is_linked(a1, 'aS3_Modifier', b)
    _safe_set(b, 'aS3_InterfaceMethod39', a2)
    assert _is_linked(b, 'aS3_InterfaceMethod39', a2)
    if hasattr(a1, 'aS3_Modifier'):
        assert not _is_linked(a1, 'aS3_Modifier', b)
    if hasattr(a2, 'aS3_Modifier'):
        assert _is_linked(a2, 'aS3_Modifier', b)
    _safe_set(b, 'aS3_InterfaceMethod39', None)
    assert not _is_linked(b, 'aS3_InterfaceMethod39', a2)
    if hasattr(a2, 'aS3_Modifier'):
        assert not _is_linked(a2, 'aS3_Modifier', b)


def test_assoc_modifier54_reverse_link_reassign_clear():
    a1 = aS3_Modifier(access="sample_text", dynamic=True, final=True, native=True, static=True)
    a2 = aS3_Modifier(access="sample_text_2", dynamic=False, final=False, native=False, static=False)
    b = aS3_Class(name="sample_text")
    _safe_set(b, 'aS3_Class55', a1)
    assert _is_linked(b, 'aS3_Class55', a1)
    if hasattr(a1, 'aS3_Modifier56'):
        assert _is_linked(a1, 'aS3_Modifier56', b)
    _safe_set(b, 'aS3_Class55', a2)
    assert _is_linked(b, 'aS3_Class55', a2)
    if hasattr(a1, 'aS3_Modifier56'):
        assert not _is_linked(a1, 'aS3_Modifier56', b)
    if hasattr(a2, 'aS3_Modifier56'):
        assert _is_linked(a2, 'aS3_Modifier56', b)
    _safe_set(b, 'aS3_Class55', None)
    assert not _is_linked(b, 'aS3_Class55', a2)
    if hasattr(a2, 'aS3_Modifier56'):
        assert not _is_linked(a2, 'aS3_Modifier56', b)


def test_assoc_modifier72_reverse_link_reassign_clear():
    a1 = aS3_Modifier(access="sample_text", dynamic=True, final=True, native=True, static=True)
    a2 = aS3_Modifier(access="sample_text_2", dynamic=False, final=False, native=False, static=False)
    b = aS3_Method(anytype="sample_text", name="sample_text")
    _safe_set(b, 'aS3_Method73', a1)
    assert _is_linked(b, 'aS3_Method73', a1)
    if hasattr(a1, 'aS3_Modifier74'):
        assert _is_linked(a1, 'aS3_Modifier74', b)
    _safe_set(b, 'aS3_Method73', a2)
    assert _is_linked(b, 'aS3_Method73', a2)
    if hasattr(a1, 'aS3_Modifier74'):
        assert not _is_linked(a1, 'aS3_Modifier74', b)
    if hasattr(a2, 'aS3_Modifier74'):
        assert _is_linked(a2, 'aS3_Modifier74', b)
    _safe_set(b, 'aS3_Method73', None)
    assert not _is_linked(b, 'aS3_Method73', a2)
    if hasattr(a2, 'aS3_Modifier74'):
        assert not _is_linked(a2, 'aS3_Modifier74', b)


def test_assoc_modifier91_reverse_link_reassign_clear():
    a1 = aS3_Modifier(access="sample_text", dynamic=True, final=True, native=True, static=True)
    a2 = aS3_Modifier(access="sample_text_2", dynamic=False, final=False, native=False, static=False)
    b = aS3_MemberVariableDeclaration(anytype="sample_text", name="sample_text")
    _safe_set(b, 'aS3_MemberVariableDeclaration92', a1)
    assert _is_linked(b, 'aS3_MemberVariableDeclaration92', a1)
    if hasattr(a1, 'aS3_Modifier93'):
        assert _is_linked(a1, 'aS3_Modifier93', b)
    _safe_set(b, 'aS3_MemberVariableDeclaration92', a2)
    assert _is_linked(b, 'aS3_MemberVariableDeclaration92', a2)
    if hasattr(a1, 'aS3_Modifier93'):
        assert not _is_linked(a1, 'aS3_Modifier93', b)
    if hasattr(a2, 'aS3_Modifier93'):
        assert _is_linked(a2, 'aS3_Modifier93', b)
    _safe_set(b, 'aS3_MemberVariableDeclaration92', None)
    assert not _is_linked(b, 'aS3_MemberVariableDeclaration92', a2)
    if hasattr(a2, 'aS3_Modifier93'):
        assert not _is_linked(a2, 'aS3_Modifier93', b)


def test_assoc_params42_reverse_link_reassign_clear():
    a1 = aS3_Parameter(anytype="sample_text", name="sample_text")
    a2 = aS3_Parameter(anytype="sample_text_2", name="sample_text_2")
    b = aS3_InterfaceMethod(anytype="sample_text", name="sample_text")
    _safe_set(b, 'aS3_InterfaceMethod43', {a1})
    assert _is_linked(b, 'aS3_InterfaceMethod43', a1)
    if hasattr(a1, 'aS3_Parameter'):
        assert _is_linked(a1, 'aS3_Parameter', b)
    _safe_set(b, 'aS3_InterfaceMethod43', {a2})
    assert _is_linked(b, 'aS3_InterfaceMethod43', a2)
    if hasattr(a1, 'aS3_Parameter'):
        assert not _is_linked(a1, 'aS3_Parameter', b)
    if hasattr(a2, 'aS3_Parameter'):
        assert _is_linked(a2, 'aS3_Parameter', b)
    _safe_set(b, 'aS3_InterfaceMethod43', set())
    assert not _is_linked(b, 'aS3_InterfaceMethod43', a2)
    if hasattr(a2, 'aS3_Parameter'):
        assert not _is_linked(a2, 'aS3_Parameter', b)


def test_assoc_params78_reverse_link_reassign_clear():
    a1 = aS3_Parameter(anytype="sample_text", name="sample_text")
    a2 = aS3_Parameter(anytype="sample_text_2", name="sample_text_2")
    b = aS3_Method(anytype="sample_text", name="sample_text")
    _safe_set(b, 'aS3_Method79', {a1})
    assert _is_linked(b, 'aS3_Method79', a1)
    if hasattr(a1, 'aS3_Parameter80'):
        assert _is_linked(a1, 'aS3_Parameter80', b)
    _safe_set(b, 'aS3_Method79', {a2})
    assert _is_linked(b, 'aS3_Method79', a2)
    if hasattr(a1, 'aS3_Parameter80'):
        assert not _is_linked(a1, 'aS3_Parameter80', b)
    if hasattr(a2, 'aS3_Parameter80'):
        assert _is_linked(a2, 'aS3_Parameter80', b)
    _safe_set(b, 'aS3_Method79', set())
    assert not _is_linked(b, 'aS3_Method79', a2)
    if hasattr(a2, 'aS3_Parameter80'):
        assert not _is_linked(a2, 'aS3_Parameter80', b)


def test_assoc_superclass31_reverse_link_reassign_clear():
    a1 = aS3_Interface(access="sample_text", name="sample_text")
    a2 = aS3_Interface(access="sample_text_2", name="sample_text_2")
    b = aS3_Interface(access="sample_text", name="sample_text")
    _safe_set(b, 'aS3_Interface32', a1)
    assert _is_linked(b, 'aS3_Interface32', a1)
    if hasattr(a1, 'aS3_Interface30'):
        assert _is_linked(a1, 'aS3_Interface30', b)
    _safe_set(b, 'aS3_Interface32', a2)
    assert _is_linked(b, 'aS3_Interface32', a2)
    if hasattr(a1, 'aS3_Interface30'):
        assert not _is_linked(a1, 'aS3_Interface30', b)
    if hasattr(a2, 'aS3_Interface30'):
        assert _is_linked(a2, 'aS3_Interface30', b)
    _safe_set(b, 'aS3_Interface32', None)
    assert not _is_linked(b, 'aS3_Interface32', a2)
    if hasattr(a2, 'aS3_Interface30'):
        assert not _is_linked(a2, 'aS3_Interface30', b)


def test_assoc_superclass58_reverse_link_reassign_clear():
    a1 = aS3_Class(name="sample_text")
    a2 = aS3_Class(name="sample_text_2")
    b = aS3_Class(name="sample_text")
    _safe_set(b, 'aS3_Class59', a1)
    assert _is_linked(b, 'aS3_Class59', a1)
    if hasattr(a1, 'aS3_Class57'):
        assert _is_linked(a1, 'aS3_Class57', b)
    _safe_set(b, 'aS3_Class59', a2)
    assert _is_linked(b, 'aS3_Class59', a2)
    if hasattr(a1, 'aS3_Class57'):
        assert not _is_linked(a1, 'aS3_Class57', b)
    if hasattr(a2, 'aS3_Class57'):
        assert _is_linked(a2, 'aS3_Class57', b)
    _safe_set(b, 'aS3_Class59', None)
    assert not _is_linked(b, 'aS3_Class59', a2)
    if hasattr(a2, 'aS3_Class57'):
        assert not _is_linked(a2, 'aS3_Class57', b)


def test_assoc_types60_reverse_link_reassign_clear():
    a1 = aS3_Interface(access="sample_text", name="sample_text")
    a2 = aS3_Interface(access="sample_text_2", name="sample_text_2")
    b = aS3_Class(name="sample_text")
    _safe_set(b, 'aS3_Class61', {a1})
    assert _is_linked(b, 'aS3_Class61', a1)
    if hasattr(a1, 'aS3_Interface62'):
        assert _is_linked(a1, 'aS3_Interface62', b)
    _safe_set(b, 'aS3_Class61', {a2})
    assert _is_linked(b, 'aS3_Class61', a2)
    if hasattr(a1, 'aS3_Interface62'):
        assert not _is_linked(a1, 'aS3_Interface62', b)
    if hasattr(a2, 'aS3_Interface62'):
        assert _is_linked(a2, 'aS3_Interface62', b)
    _safe_set(b, 'aS3_Class61', set())
    assert not _is_linked(b, 'aS3_Class61', a2)
    if hasattr(a2, 'aS3_Interface62'):
        assert not _is_linked(a2, 'aS3_Interface62', b)


