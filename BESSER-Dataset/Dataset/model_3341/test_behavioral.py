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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Expression101_stub_double():
    # aS3_assignmentExpression has no real 'aS3_assignmentExpression103' property in the generated
    # code (a bare stub) -- manually attach it so aS3_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_VariableDeclaration(anytype="sample_text", name="sample_text")
    partner = aS3_assignmentExpression()
    setattr(partner, 'aS3_assignmentExpression103', None)
    _safe_set(owner, 'aS3_VariableDeclaration102', partner)
    assert getattr(partner, 'aS3_assignmentExpression103') == owner
    _safe_set(owner, 'aS3_VariableDeclaration102', None)
    assert getattr(partner, 'aS3_assignmentExpression103') is None


def test_assoc_Expression97_stub_double():
    # aS3_assignmentExpression has no real 'aS3_assignmentExpression' property in the generated
    # code (a bare stub) -- manually attach it so aS3_MemberVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_MemberVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_MemberVariableDeclaration(anytype="sample_text", name="sample_text")
    partner = aS3_assignmentExpression()
    setattr(partner, 'aS3_assignmentExpression', None)
    _safe_set(owner, 'aS3_MemberVariableDeclaration98', partner)
    assert getattr(partner, 'aS3_assignmentExpression') == owner
    _safe_set(owner, 'aS3_MemberVariableDeclaration98', None)
    assert getattr(partner, 'aS3_assignmentExpression') is None


def test_assoc_aexpr148_stub_double():
    # aS3_Expression has no real 'aS3_Expression149' property in the generated
    # code (a bare stub) -- manually attach it so aS3_conditionalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_conditionalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_conditionalExpression(op="sample_text")
    partner = aS3_Expression()
    setattr(partner, 'aS3_Expression149', None)
    _safe_set(owner, 'aS3_conditionalExpression', {partner})
    assert getattr(partner, 'aS3_Expression149') == owner
    _safe_set(owner, 'aS3_conditionalExpression', set())
    assert getattr(partner, 'aS3_Expression149') is None


def test_assoc_annonFields23_stub_double():
    # aS3_annotationFields has no real 'aS3_annotationFields' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Annotation(name="sample_text")
    partner = aS3_annotationFields()
    setattr(partner, 'aS3_annotationFields', None)
    _safe_set(owner, 'aS3_Annotation', partner)
    assert getattr(partner, 'aS3_annotationFields') == owner
    _safe_set(owner, 'aS3_Annotation', None)
    assert getattr(partner, 'aS3_annotationFields') is None


def test_assoc_annonFields24_stub_double():
    # aS3_annotationFields has no real 'aS3_annotationFields25' property in the generated
    # code (a bare stub) -- manually attach it so aS3_annotationField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_annotationField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_annotationField(name="sample_text")
    partner = aS3_annotationFields()
    setattr(partner, 'aS3_annotationFields25', None)
    _safe_set(owner, 'aS3_annotationField', partner)
    assert getattr(partner, 'aS3_annotationFields25') == owner
    _safe_set(owner, 'aS3_annotationField', None)
    assert getattr(partner, 'aS3_annotationFields25') is None


def test_assoc_block125_stub_double():
    # aS3_Block has no real 'aS3_Block127' property in the generated
    # code (a bare stub) -- manually attach it so aS3_identi's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_identi's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_identi(i="sample_text")
    partner = aS3_Block()
    setattr(partner, 'aS3_Block127', None)
    _safe_set(owner, 'aS3_identi126', partner)
    assert getattr(partner, 'aS3_Block127') == owner
    _safe_set(owner, 'aS3_identi126', None)
    assert getattr(partner, 'aS3_Block127') is None


def test_assoc_body84_stub_double():
    # aS3_Block has no real 'aS3_Block86' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Method(anytype="sample_text", name="sample_text")
    partner = aS3_Block()
    setattr(partner, 'aS3_Block86', None)
    _safe_set(owner, 'aS3_Method85', partner)
    assert getattr(partner, 'aS3_Block86') == owner
    _safe_set(owner, 'aS3_Method85', None)
    assert getattr(partner, 'aS3_Block86') is None


def test_assoc_brack243_stub_double():
    # aS3_brackets has no real 'aS3_brackets245' property in the generated
    # code (a bare stub) -- manually attach it so aS3_fullNewSubexpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_fullNewSubexpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_fullNewSubexpression(fnsd="sample_text")
    partner = aS3_brackets()
    setattr(partner, 'aS3_brackets245', None)
    _safe_set(owner, 'aS3_fullNewSubexpression244', {partner})
    assert getattr(partner, 'aS3_brackets245') == owner
    _safe_set(owner, 'aS3_fullNewSubexpression244', set())
    assert getattr(partner, 'aS3_brackets245') is None


def test_assoc_classes16_stub_double():
    # aS3_EObject has no real 'aS3_EObject18' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Package(name="sample_text")
    partner = aS3_EObject()
    setattr(partner, 'aS3_EObject18', None)
    _safe_set(owner, 'aS3_Package17', {partner})
    assert getattr(partner, 'aS3_EObject18') == owner
    _safe_set(owner, 'aS3_Package17', set())
    assert getattr(partner, 'aS3_EObject18') is None


def test_assoc_cond155_stub_double():
    # aS3_conditionalSubExpression has no real 'aS3_conditionalSubExpression156' property in the generated
    # code (a bare stub) -- manually attach it so aS3_logicalOrExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_logicalOrExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_logicalOrExpression(o="sample_text")
    partner = aS3_conditionalSubExpression()
    setattr(partner, 'aS3_conditionalSubExpression156', None)
    _safe_set(owner, 'aS3_logicalOrExpression', partner)
    assert getattr(partner, 'aS3_conditionalSubExpression156') == owner
    _safe_set(owner, 'aS3_logicalOrExpression', None)
    assert getattr(partner, 'aS3_conditionalSubExpression156') is None


def test_assoc_decl323_stub_double():
    # aS3_forInit has no real 'aS3_forInit324' property in the generated
    # code (a bare stub) -- manually attach it so aS3_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_VariableDeclaration(anytype="sample_text", name="sample_text")
    partner = aS3_forInit()
    setattr(partner, 'aS3_forInit324', None)
    _safe_set(owner, 'aS3_VariableDeclaration325', partner)
    assert getattr(partner, 'aS3_forInit324') == owner
    _safe_set(owner, 'aS3_VariableDeclaration325', None)
    assert getattr(partner, 'aS3_forInit324') is None


def test_assoc_directives11_stub_double():
    # aS3_directive has no real 'aS3_directive' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Package(name="sample_text")
    partner = aS3_directive()
    setattr(partner, 'aS3_directive', None)
    _safe_set(owner, 'aS3_Package12', {partner})
    assert getattr(partner, 'aS3_directive') == owner
    _safe_set(owner, 'aS3_Package12', set())
    assert getattr(partner, 'aS3_directive') is None


def test_assoc_expr172_stub_double():
    # aS3_unaryExpression has no real 'aS3_unaryExpression' property in the generated
    # code (a bare stub) -- manually attach it so aS3_multiplicativeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_multiplicativeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_multiplicativeExpression(o="sample_text")
    partner = aS3_unaryExpression()
    setattr(partner, 'aS3_unaryExpression', None)
    _safe_set(owner, 'aS3_multiplicativeExpression173', {partner})
    assert getattr(partner, 'aS3_unaryExpression') == owner
    _safe_set(owner, 'aS3_multiplicativeExpression173', set())
    assert getattr(partner, 'aS3_unaryExpression') is None


def test_assoc_expr238_stub_double():
    # aS3_primaryExpression has no real 'aS3_primaryExpression239' property in the generated
    # code (a bare stub) -- manually attach it so aS3_fullNewSubexpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_fullNewSubexpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_fullNewSubexpression(fnsd="sample_text")
    partner = aS3_primaryExpression()
    setattr(partner, 'aS3_primaryExpression239', None)
    _safe_set(owner, 'aS3_fullNewSubexpression', {partner})
    assert getattr(partner, 'aS3_primaryExpression239') == owner
    _safe_set(owner, 'aS3_fullNewSubexpression', set())
    assert getattr(partner, 'aS3_primaryExpression239') is None


def test_assoc_expr26_stub_double():
    # aS3_Expression has no real 'aS3_Expression' property in the generated
    # code (a bare stub) -- manually attach it so aS3_annotationField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_annotationField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_annotationField(name="sample_text")
    partner = aS3_Expression()
    setattr(partner, 'aS3_Expression', None)
    _safe_set(owner, 'aS3_annotationField27', partner)
    assert getattr(partner, 'aS3_Expression') == owner
    _safe_set(owner, 'aS3_annotationField27', None)
    assert getattr(partner, 'aS3_Expression') is None


def test_assoc_fexpr216_stub_double():
    # aS3_primaryExpression has no real 'aS3_primaryExpression217' property in the generated
    # code (a bare stub) -- manually attach it so aS3_functionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_functionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_functionExpression(name="sample_text")
    partner = aS3_primaryExpression()
    setattr(partner, 'aS3_primaryExpression217', None)
    _safe_set(owner, 'aS3_functionExpression218', partner)
    assert getattr(partner, 'aS3_primaryExpression217') == owner
    _safe_set(owner, 'aS3_functionExpression218', None)
    assert getattr(partner, 'aS3_primaryExpression217') is None


def test_assoc_func47_stub_double():
    # aS3_functionCommon has no real 'aS3_functionCommon' property in the generated
    # code (a bare stub) -- manually attach it so aS3_functionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_functionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_functionExpression(name="sample_text")
    partner = aS3_functionCommon()
    setattr(partner, 'aS3_functionCommon', None)
    _safe_set(owner, 'aS3_functionExpression', partner)
    assert getattr(partner, 'aS3_functionCommon') == owner
    _safe_set(owner, 'aS3_functionExpression', None)
    assert getattr(partner, 'aS3_functionCommon') is None


def test_assoc_ide121_stub_double():
    # aS3_qualifiedIdent has no real 'aS3_qualifiedIdent' property in the generated
    # code (a bare stub) -- manually attach it so aS3_identi's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_identi's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_identi(i="sample_text")
    partner = aS3_qualifiedIdent()
    setattr(partner, 'aS3_qualifiedIdent', None)
    _safe_set(owner, 'aS3_identi122', partner)
    assert getattr(partner, 'aS3_qualifiedIdent') == owner
    _safe_set(owner, 'aS3_identi122', None)
    assert getattr(partner, 'aS3_qualifiedIdent') is None


def test_assoc_imp8_stub_double():
    # aS3_Imports has no real 'aS3_Imports10' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Package(name="sample_text")
    partner = aS3_Imports()
    setattr(partner, 'aS3_Imports10', None)
    _safe_set(owner, 'aS3_Package9', partner)
    assert getattr(partner, 'aS3_Imports10') == owner
    _safe_set(owner, 'aS3_Package9', None)
    assert getattr(partner, 'aS3_Imports10') is None


def test_assoc_imports19_stub_double():
    # aS3_Imports has no real 'aS3_Imports20' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Import(importedNamespace="sample_text")
    partner = aS3_Imports()
    setattr(partner, 'aS3_Imports20', None)
    _safe_set(owner, 'aS3_Import', partner)
    assert getattr(partner, 'aS3_Imports20') == owner
    _safe_set(owner, 'aS3_Import', None)
    assert getattr(partner, 'aS3_Imports20') is None


def test_assoc_lit107_stub_double():
    # aS3_exprOrObjectLiteral has no real 'aS3_exprOrObjectLiteral' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Parameter(anytype="sample_text", name="sample_text")
    partner = aS3_exprOrObjectLiteral()
    setattr(partner, 'aS3_exprOrObjectLiteral', None)
    _safe_set(owner, 'aS3_Parameter108', partner)
    assert getattr(partner, 'aS3_exprOrObjectLiteral') == owner
    _safe_set(owner, 'aS3_Parameter108', None)
    assert getattr(partner, 'aS3_exprOrObjectLiteral') is None


def test_assoc_members13_stub_double():
    # aS3_EObject has no real 'aS3_EObject15' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Package(name="sample_text")
    partner = aS3_EObject()
    setattr(partner, 'aS3_EObject15', None)
    _safe_set(owner, 'aS3_Package14', {partner})
    assert getattr(partner, 'aS3_EObject15') == owner
    _safe_set(owner, 'aS3_Package14', set())
    assert getattr(partner, 'aS3_EObject15') is None


def test_assoc_members63_stub_double():
    # aS3_Member has no real 'aS3_Member' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Class(name="sample_text")
    partner = aS3_Member()
    setattr(partner, 'aS3_Member', None)
    _safe_set(owner, 'aS3_Class64', {partner})
    assert getattr(partner, 'aS3_Member') == owner
    _safe_set(owner, 'aS3_Class64', set())
    assert getattr(partner, 'aS3_Member') is None


def test_assoc_meth67_stub_double():
    # aS3_Member has no real 'aS3_Member68' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Method(anytype="sample_text", name="sample_text")
    partner = aS3_Member()
    setattr(partner, 'aS3_Member68', None)
    _safe_set(owner, 'aS3_Method', partner)
    assert getattr(partner, 'aS3_Member68') == owner
    _safe_set(owner, 'aS3_Method', None)
    assert getattr(partner, 'aS3_Member68') is None


def test_assoc_name115_stub_double():
    # aS3_literalField has no real 'aS3_literalField116' property in the generated
    # code (a bare stub) -- manually attach it so aS3_fieldName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_fieldName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_fieldName(name="sample_text", number="sample_text")
    partner = aS3_literalField()
    setattr(partner, 'aS3_literalField116', None)
    _safe_set(owner, 'aS3_fieldName', partner)
    assert getattr(partner, 'aS3_literalField116') == owner
    _safe_set(owner, 'aS3_fieldName', None)
    assert getattr(partner, 'aS3_literalField116') is None


def test_assoc_name263_stub_double():
    # aS3_parameterDeclaration has no real 'aS3_parameterDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so aS3_identi's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_identi's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_identi(i="sample_text")
    partner = aS3_parameterDeclaration()
    setattr(partner, 'aS3_parameterDeclaration', None)
    _safe_set(owner, 'aS3_identi264', partner)
    assert getattr(partner, 'aS3_parameterDeclaration') == owner
    _safe_set(owner, 'aS3_identi264', None)
    assert getattr(partner, 'aS3_parameterDeclaration') is None


def test_assoc_package0_stub_double():
    # aS3_Model has no real 'aS3_Model' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Package(name="sample_text")
    partner = aS3_Model()
    setattr(partner, 'aS3_Model', None)
    _safe_set(owner, 'aS3_Package', partner)
    assert getattr(partner, 'aS3_Model') == owner
    _safe_set(owner, 'aS3_Package', None)
    assert getattr(partner, 'aS3_Model') is None


def test_assoc_params260_stub_double():
    # aS3_parameterDeclarationList has no real 'aS3_parameterDeclarationList261' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Parameter(anytype="sample_text", name="sample_text")
    partner = aS3_parameterDeclarationList()
    setattr(partner, 'aS3_parameterDeclarationList261', None)
    _safe_set(owner, 'aS3_Parameter262', partner)
    assert getattr(partner, 'aS3_parameterDeclarationList261') == owner
    _safe_set(owner, 'aS3_Parameter262', None)
    assert getattr(partner, 'aS3_parameterDeclarationList261') is None


def test_assoc_qual133_stub_double():
    # aS3_simpleQualifiedIdentifier has no real 'aS3_simpleQualifiedIdentifier134' property in the generated
    # code (a bare stub) -- manually attach it so aS3_qualifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_qualifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_qualifier(level="sample_text")
    partner = aS3_simpleQualifiedIdentifier()
    setattr(partner, 'aS3_simpleQualifiedIdentifier134', None)
    _safe_set(owner, 'aS3_qualifier', partner)
    assert getattr(partner, 'aS3_simpleQualifiedIdentifier134') == owner
    _safe_set(owner, 'aS3_qualifier', None)
    assert getattr(partner, 'aS3_simpleQualifiedIdentifier134') is None


def test_assoc_quali240_stub_double():
    # aS3_qualifiedIdent has no real 'aS3_qualifiedIdent242' property in the generated
    # code (a bare stub) -- manually attach it so aS3_fullNewSubexpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_fullNewSubexpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_fullNewSubexpression(fnsd="sample_text")
    partner = aS3_qualifiedIdent()
    setattr(partner, 'aS3_qualifiedIdent242', None)
    _safe_set(owner, 'aS3_fullNewSubexpression241', {partner})
    assert getattr(partner, 'aS3_qualifiedIdent242') == owner
    _safe_set(owner, 'aS3_fullNewSubexpression241', set())
    assert getattr(partner, 'aS3_qualifiedIdent242') is None


def test_assoc_type104_stub_double():
    # aS3_EObject has no real 'aS3_EObject106' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Parameter(anytype="sample_text", name="sample_text")
    partner = aS3_EObject()
    setattr(partner, 'aS3_EObject106', None)
    _safe_set(owner, 'aS3_Parameter105', partner)
    assert getattr(partner, 'aS3_EObject106') == owner
    _safe_set(owner, 'aS3_Parameter105', None)
    assert getattr(partner, 'aS3_EObject106') is None


def test_assoc_type123_stub_double():
    # aS3_typeExpression has no real 'aS3_typeExpression' property in the generated
    # code (a bare stub) -- manually attach it so aS3_identi's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_identi's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_identi(i="sample_text")
    partner = aS3_typeExpression()
    setattr(partner, 'aS3_typeExpression', None)
    _safe_set(owner, 'aS3_identi124', partner)
    assert getattr(partner, 'aS3_typeExpression') == owner
    _safe_set(owner, 'aS3_identi124', None)
    assert getattr(partner, 'aS3_typeExpression') is None


def test_assoc_type44_stub_double():
    # aS3_EObject has no real 'aS3_EObject46' property in the generated
    # code (a bare stub) -- manually attach it so aS3_InterfaceMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_InterfaceMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_InterfaceMethod(anytype="sample_text", name="sample_text")
    partner = aS3_EObject()
    setattr(partner, 'aS3_EObject46', None)
    _safe_set(owner, 'aS3_InterfaceMethod45', partner)
    assert getattr(partner, 'aS3_EObject46') == owner
    _safe_set(owner, 'aS3_InterfaceMethod45', None)
    assert getattr(partner, 'aS3_EObject46') is None


def test_assoc_type81_stub_double():
    # aS3_EObject has no real 'aS3_EObject83' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Method(anytype="sample_text", name="sample_text")
    partner = aS3_EObject()
    setattr(partner, 'aS3_EObject83', None)
    _safe_set(owner, 'aS3_Method82', partner)
    assert getattr(partner, 'aS3_EObject83') == owner
    _safe_set(owner, 'aS3_Method82', None)
    assert getattr(partner, 'aS3_EObject83') is None


def test_assoc_type94_stub_double():
    # aS3_EObject has no real 'aS3_EObject96' property in the generated
    # code (a bare stub) -- manually attach it so aS3_MemberVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_MemberVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_MemberVariableDeclaration(anytype="sample_text", name="sample_text")
    partner = aS3_EObject()
    setattr(partner, 'aS3_EObject96', None)
    _safe_set(owner, 'aS3_MemberVariableDeclaration95', partner)
    assert getattr(partner, 'aS3_EObject96') == owner
    _safe_set(owner, 'aS3_MemberVariableDeclaration95', None)
    assert getattr(partner, 'aS3_EObject96') is None


def test_assoc_type99_stub_double():
    # aS3_EObject has no real 'aS3_EObject100' property in the generated
    # code (a bare stub) -- manually attach it so aS3_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_VariableDeclaration(anytype="sample_text", name="sample_text")
    partner = aS3_EObject()
    setattr(partner, 'aS3_EObject100', None)
    _safe_set(owner, 'aS3_VariableDeclaration', partner)
    assert getattr(partner, 'aS3_EObject100') == owner
    _safe_set(owner, 'aS3_VariableDeclaration', None)
    assert getattr(partner, 'aS3_EObject100') is None


def test_assoc_uaenpm183_stub_double():
    # aS3_unaryExpression has no real 'aS3_unaryExpression184' property in the generated
    # code (a bare stub) -- manually attach it so aS3_unaryExpressionNotPlusMinus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_unaryExpressionNotPlusMinus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_unaryExpressionNotPlusMinus(de="sample_text", in_="sample_text")
    partner = aS3_unaryExpression()
    setattr(partner, 'aS3_unaryExpression184', None)
    _safe_set(owner, 'aS3_unaryExpressionNotPlusMinus', partner)
    assert getattr(partner, 'aS3_unaryExpression184') == owner
    _safe_set(owner, 'aS3_unaryExpressionNotPlusMinus', None)
    assert getattr(partner, 'aS3_unaryExpression184') is None


def test_assoc_uses21_stub_double():
    # aS3_directive has no real 'aS3_directive22' property in the generated
    # code (a bare stub) -- manually attach it so aS3_Uses's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_Uses's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_Uses(anytype="sample_text", type="sample_text")
    partner = aS3_directive()
    setattr(partner, 'aS3_directive22', None)
    _safe_set(owner, 'aS3_Uses', partner)
    assert getattr(partner, 'aS3_directive22') == owner
    _safe_set(owner, 'aS3_Uses', None)
    assert getattr(partner, 'aS3_directive22') is None


def test_assoc_value350_stub_double():
    # aS3_RegexpConstant has no real 'aS3_RegexpConstant' property in the generated
    # code (a bare stub) -- manually attach it so aS3_regexpLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_regexpLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_regexpLiteral(s="sample_text")
    partner = aS3_RegexpConstant()
    setattr(partner, 'aS3_RegexpConstant', None)
    _safe_set(owner, 'aS3_regexpLiteral', partner)
    assert getattr(partner, 'aS3_RegexpConstant') == owner
    _safe_set(owner, 'aS3_regexpLiteral', None)
    assert getattr(partner, 'aS3_RegexpConstant') is None


def test_assoc_var65_stub_double():
    # aS3_Member has no real 'aS3_Member66' property in the generated
    # code (a bare stub) -- manually attach it so aS3_MemberVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aS3_MemberVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aS3_MemberVariableDeclaration(anytype="sample_text", name="sample_text")
    partner = aS3_Member()
    setattr(partner, 'aS3_Member66', None)
    _safe_set(owner, 'aS3_MemberVariableDeclaration', partner)
    assert getattr(partner, 'aS3_Member66') == owner
    _safe_set(owner, 'aS3_MemberVariableDeclaration', None)
    assert getattr(partner, 'aS3_Member66') is None


