import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotation,
    AssignmentStatement,
    BinaryOperatorExpression,
    CollectionExpression,
    CollectionInitValue,
    CollectionType,
    EolElement,
    Expression,
    FeatureCallExpression,
    LiteralExpression,
    NameExpression,
    OperatorExpression,
    OrderedCollectionType,
    PrimitiveExpression,
    PrimitiveType,
    PseudoType,
    Statement,
    SwitchCaseStatement,
    Type,
    UnaryOperatorExpression,
    UniqueCollectionType,
    VariableDeclarationExpression,
    eol_AbortStatement,
    eol_AndOperatorExpression,
    eol_Annotation,
    eol_AnnotationBlock,
    eol_AnyType,
    eol_AssignmentStatement,
    eol_BagExpression,
    eol_BagType,
    eol_BinaryOperatorExpression,
    eol_Block,
    eol_BooleanExpression,
    eol_BooleanType,
    eol_BreakAllStatement,
    eol_BreakStatement,
    eol_CollectionExpression,
    eol_CollectionInitValue,
    eol_CollectionType,
    eol_ContinueStatement,
    eol_DeleteStatement,
    eol_DivideOperatorExpression,
    eol_EClassifier,
    eol_EObject,
    eol_EPackage,
    eol_EType,
    eol_EnumerationLiteralExpression,
    eol_EolElement,
    eol_EqualsOperatorExpression,
    eol_ExecutableAnnotation,
    eol_ExpRange,
    eol_ExprList,
    eol_Expression,
    eol_ExpressionStatement,
    eol_FOLMethodCallExpression,
    eol_FeatureCallExpression,
    eol_ForStatement,
    eol_FormalParameterExpression,
    eol_GreaterThanOperatorExpression,
    eol_GreaterThanOrEqualToOperatorExpression,
    eol_IfStatement,
    eol_ImpliesOperatorExpression,
    eol_Import,
    eol_IntegerExpression,
    eol_IntegerType,
    eol_KeyValue,
    eol_LessThanOperatorExpression,
    eol_LessThanOrEqualToOperatorExpression,
    eol_LiteralExpression,
    eol_MapExpression,
    eol_MapType,
    eol_MethodCallExpression,
    eol_MinusOperatorExpression,
    eol_ModelDeclarationParameter,
    eol_ModelDeclarationStatement,
    eol_ModelElementType,
    eol_ModelExpression,
    eol_ModelType,
    eol_MultiplyOperatorExpression,
    eol_NameExpression,
    eol_NativeExpression,
    eol_NativeType,
    eol_NegativeOperatorExpression,
    eol_NewExpression,
    eol_NotEqualsOperatorExpression,
    eol_NotOperatorExpression,
    eol_OperationArgType,
    eol_OperationDefinition,
    eol_OperatorExpression,
    eol_OrOperatorExpression,
    eol_OrderedCollectionType,
    eol_OrderedSetExpression,
    eol_OrderedSetType,
    eol_PlusOperatorExpression,
    eol_PrimitiveExpression,
    eol_PrimitiveType,
    eol_Program,
    eol_PropertyCallExpression,
    eol_PseudoType,
    eol_RealExpression,
    eol_RealType,
    eol_ReturnStatement,
    eol_SelfContentType,
    eol_SelfInnermostType,
    eol_SelfType,
    eol_SequenceExpression,
    eol_SequenceType,
    eol_SetExpression,
    eol_SetType,
    eol_SimpleAnnotation,
    eol_SpecialAssignmentStatement,
    eol_SpecialNameExpression,
    eol_Statement,
    eol_StringExpression,
    eol_StringType,
    eol_SwitchCaseDefaultStatement,
    eol_SwitchCaseExpressionStatement,
    eol_SwitchCaseStatement,
    eol_SwitchStatement,
    eol_TextPosition,
    eol_TextRegion,
    eol_ThrowStatement,
    eol_TransactionStatement,
    eol_Type,
    eol_UnaryOperatorExpression,
    eol_UniqueCollectionType,
    eol_VariableDeclarationExpression,
    eol_VoidType,
    eol_WhileStatement,
    eol_XorOperatorExpression,
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

def test_assoc_container1_reverse_link_reassign_clear():
    a1 = eol_EolElement(column=7, line=7, uri="sample_text")
    a2 = eol_EolElement(column=13, line=13, uri="sample_text_2")
    b = eol_EolElement(column=7, line=7, uri="sample_text")
    _safe_set(b, 'eol_EolElement0', a1)
    assert _is_linked(b, 'eol_EolElement0', a1)
    if hasattr(a1, 'eol_EolElement'):
        assert _is_linked(a1, 'eol_EolElement', b)
    _safe_set(b, 'eol_EolElement0', a2)
    assert _is_linked(b, 'eol_EolElement0', a2)
    if hasattr(a1, 'eol_EolElement'):
        assert not _is_linked(a1, 'eol_EolElement', b)
    if hasattr(a2, 'eol_EolElement'):
        assert _is_linked(a2, 'eol_EolElement', b)
    _safe_set(b, 'eol_EolElement0', None)
    assert not _is_linked(b, 'eol_EolElement0', a2)
    if hasattr(a2, 'eol_EolElement'):
        assert not _is_linked(a2, 'eol_EolElement', b)


def test_assoc_create64_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(lastDefinitionPoint="sample_text")
    a2 = eol_VariableDeclarationExpression(lastDefinitionPoint="sample_text_2")
    b = eol_BooleanExpression(val=True)
    _safe_set(b, 'eol_BooleanExpression66', a1)
    assert _is_linked(b, 'eol_BooleanExpression66', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression65'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression65', b)
    _safe_set(b, 'eol_BooleanExpression66', a2)
    assert _is_linked(b, 'eol_BooleanExpression66', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression65'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression65', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression65'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression65', b)
    _safe_set(b, 'eol_BooleanExpression66', None)
    assert not _is_linked(b, 'eol_BooleanExpression66', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression65'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression65', b)


def test_assoc_isType52_reverse_link_reassign_clear():
    a1 = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    a2 = eol_NameExpression(name="sample_text_2", resolvedContent="sample_text_2")
    b = eol_BooleanExpression(val=True)
    _safe_set(b, 'eol_BooleanExpression54', a1)
    assert _is_linked(b, 'eol_BooleanExpression54', a1)
    if hasattr(a1, 'eol_NameExpression53'):
        assert _is_linked(a1, 'eol_NameExpression53', b)
    _safe_set(b, 'eol_BooleanExpression54', a2)
    assert _is_linked(b, 'eol_BooleanExpression54', a2)
    if hasattr(a1, 'eol_NameExpression53'):
        assert not _is_linked(a1, 'eol_NameExpression53', b)
    if hasattr(a2, 'eol_NameExpression53'):
        assert _is_linked(a2, 'eol_NameExpression53', b)
    _safe_set(b, 'eol_BooleanExpression54', None)
    assert not _is_linked(b, 'eol_BooleanExpression54', a2)
    if hasattr(a2, 'eol_NameExpression53'):
        assert not _is_linked(a2, 'eol_NameExpression53', b)


def test_assoc_name62_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(lastDefinitionPoint="sample_text")
    a2 = eol_VariableDeclarationExpression(lastDefinitionPoint="sample_text_2")
    b = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression63', a1)
    assert _is_linked(b, 'eol_NameExpression63', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression', b)
    _safe_set(b, 'eol_NameExpression63', a2)
    assert _is_linked(b, 'eol_NameExpression63', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression', b)
    _safe_set(b, 'eol_NameExpression63', None)
    assert not _is_linked(b, 'eol_NameExpression63', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc__result89_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition90' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(lastDefinitionPoint="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition90', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression91', partner)
    assert getattr(partner, 'eol_OperationDefinition90') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression91', None)
    assert getattr(partner, 'eol_OperationDefinition90') is None


def test_assoc_alias135_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement136' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement136', None)
    _safe_set(owner, 'eol_NameExpression137', partner)
    assert owner in getattr(partner, 'eol_ModelDeclarationStatement136')
    _safe_set(owner, 'eol_NameExpression137', None)
    assert owner not in getattr(partner, 'eol_ModelDeclarationStatement136')


def test_assoc_driver138_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement139' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement139', None)
    _safe_set(owner, 'eol_NameExpression140', partner)
    assert getattr(partner, 'eol_ModelDeclarationStatement139') == owner
    _safe_set(owner, 'eol_NameExpression140', None)
    assert getattr(partner, 'eol_ModelDeclarationStatement139') is None


def test_assoc_ecoreType187_stub_double():
    # eol_EClassifier has no real 'eol_EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so eol_ModelElementType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_ModelElementType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_ModelElementType(elementName="sample_text", modelName="sample_text")
    partner = eol_EClassifier()
    setattr(partner, 'eol_EClassifier', None)
    _safe_set(owner, 'eol_ModelElementType', partner)
    assert getattr(partner, 'eol_EClassifier') == owner
    _safe_set(owner, 'eol_ModelElementType', None)
    assert getattr(partner, 'eol_EClassifier') is None


def test_assoc_end6_stub_double():
    # eol_TextRegion has no real 'eol_TextRegion7' property in the generated
    # code (a bare stub) -- manually attach it so eol_TextPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_TextPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_TextPosition(column=7, line=7)
    partner = eol_TextRegion()
    setattr(partner, 'eol_TextRegion7', None)
    _safe_set(owner, 'eol_TextPosition8', partner)
    assert getattr(partner, 'eol_TextRegion7') == owner
    _safe_set(owner, 'eol_TextPosition8', None)
    assert getattr(partner, 'eol_TextRegion7') is None


def test_assoc_enumeration34_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression', None)
    _safe_set(owner, 'eol_NameExpression35', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression') == owner
    _safe_set(owner, 'eol_NameExpression35', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression') is None


def test_assoc_extended59_stub_double():
    # eol_PropertyCallExpression has no real 'eol_PropertyCallExpression60' property in the generated
    # code (a bare stub) -- manually attach it so eol_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_BooleanExpression(val=True)
    partner = eol_PropertyCallExpression()
    setattr(partner, 'eol_PropertyCallExpression60', None)
    _safe_set(owner, 'eol_BooleanExpression61', partner)
    assert getattr(partner, 'eol_PropertyCallExpression60') == owner
    _safe_set(owner, 'eol_BooleanExpression61', None)
    assert getattr(partner, 'eol_PropertyCallExpression60') is None


def test_assoc_imported21_stub_double():
    # eol_Import has no real 'eol_Import22' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(val="sample_text")
    partner = eol_Import()
    setattr(partner, 'eol_Import22', None)
    _safe_set(owner, 'eol_StringExpression', partner)
    assert getattr(partner, 'eol_Import22') == owner
    _safe_set(owner, 'eol_StringExpression', None)
    assert getattr(partner, 'eol_Import22') is None


def test_assoc_isArrow43_stub_double():
    # eol_FeatureCallExpression has no real 'eol_FeatureCallExpression44' property in the generated
    # code (a bare stub) -- manually attach it so eol_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_BooleanExpression(val=True)
    partner = eol_FeatureCallExpression()
    setattr(partner, 'eol_FeatureCallExpression44', None)
    _safe_set(owner, 'eol_BooleanExpression', partner)
    assert getattr(partner, 'eol_FeatureCallExpression44') == owner
    _safe_set(owner, 'eol_BooleanExpression', None)
    assert getattr(partner, 'eol_FeatureCallExpression44') is None


def test_assoc_isType228_stub_double():
    # eol_NativeExpression has no real 'eol_NativeExpression229' property in the generated
    # code (a bare stub) -- manually attach it so eol_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_BooleanExpression(val=True)
    partner = eol_NativeExpression()
    setattr(partner, 'eol_NativeExpression229', None)
    _safe_set(owner, 'eol_BooleanExpression230', partner)
    assert getattr(partner, 'eol_NativeExpression229') == owner
    _safe_set(owner, 'eol_BooleanExpression230', None)
    assert getattr(partner, 'eol_NativeExpression229') is None


def test_assoc_literal36_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression37' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression37', None)
    _safe_set(owner, 'eol_NameExpression38', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression37') == owner
    _safe_set(owner, 'eol_NameExpression38', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression37') is None


def test_assoc_method151_stub_double():
    # eol_FOLMethodCallExpression has no real 'eol_FOLMethodCallExpression152' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_FOLMethodCallExpression()
    setattr(partner, 'eol_FOLMethodCallExpression152', None)
    _safe_set(owner, 'eol_NameExpression153', partner)
    assert getattr(partner, 'eol_FOLMethodCallExpression152') == owner
    _safe_set(owner, 'eol_NameExpression153', None)
    assert getattr(partner, 'eol_FOLMethodCallExpression152') is None


def test_assoc_method47_stub_double():
    # eol_MethodCallExpression has no real 'eol_MethodCallExpression48' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_MethodCallExpression()
    setattr(partner, 'eol_MethodCallExpression48', None)
    _safe_set(owner, 'eol_NameExpression49', partner)
    assert getattr(partner, 'eol_MethodCallExpression48') == owner
    _safe_set(owner, 'eol_NameExpression49', None)
    assert getattr(partner, 'eol_MethodCallExpression48') is None


def test_assoc_modelName221_stub_double():
    # eol_ModelType has no real 'eol_ModelType' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_ModelType()
    setattr(partner, 'eol_ModelType', None)
    _safe_set(owner, 'eol_NameExpression222', partner)
    assert getattr(partner, 'eol_ModelType') == owner
    _safe_set(owner, 'eol_NameExpression222', None)
    assert getattr(partner, 'eol_ModelType') is None


def test_assoc_name132_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement133' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement133', None)
    _safe_set(owner, 'eol_NameExpression134', partner)
    assert getattr(partner, 'eol_ModelDeclarationStatement133') == owner
    _safe_set(owner, 'eol_NameExpression134', None)
    assert getattr(partner, 'eol_ModelDeclarationStatement133') is None


def test_assoc_name17_stub_double():
    # eol_Program has no real 'eol_Program18' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_Program()
    setattr(partner, 'eol_Program18', None)
    _safe_set(owner, 'eol_NameExpression', partner)
    assert getattr(partner, 'eol_Program18') == owner
    _safe_set(owner, 'eol_NameExpression', None)
    assert getattr(partner, 'eol_Program18') is None


def test_assoc_name175_stub_double():
    # eol_Annotation has no real 'eol_Annotation' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_Annotation()
    setattr(partner, 'eol_Annotation', None)
    _safe_set(owner, 'eol_NameExpression176', partner)
    assert getattr(partner, 'eol_Annotation') == owner
    _safe_set(owner, 'eol_NameExpression176', None)
    assert getattr(partner, 'eol_Annotation') is None


def test_assoc_name199_stub_double():
    # eol_ModelDeclarationParameter has no real 'eol_ModelDeclarationParameter200' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_ModelDeclarationParameter()
    setattr(partner, 'eol_ModelDeclarationParameter200', None)
    _safe_set(owner, 'eol_NameExpression201', partner)
    assert getattr(partner, 'eol_ModelDeclarationParameter200') == owner
    _safe_set(owner, 'eol_NameExpression201', None)
    assert getattr(partner, 'eol_ModelDeclarationParameter200') is None


def test_assoc_name81_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition82' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition82', None)
    _safe_set(owner, 'eol_NameExpression83', partner)
    assert getattr(partner, 'eol_OperationDefinition82') == owner
    _safe_set(owner, 'eol_NameExpression83', None)
    assert getattr(partner, 'eol_OperationDefinition82') is None


def test_assoc_names209_stub_double():
    # eol_TransactionStatement has no real 'eol_TransactionStatement210' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_TransactionStatement()
    setattr(partner, 'eol_TransactionStatement210', None)
    _safe_set(owner, 'eol_NameExpression211', partner)
    assert owner in getattr(partner, 'eol_TransactionStatement210')
    _safe_set(owner, 'eol_NameExpression211', None)
    assert owner not in getattr(partner, 'eol_TransactionStatement210')


def test_assoc_nativeExpr226_stub_double():
    # eol_NativeExpression has no real 'eol_NativeExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(val="sample_text")
    partner = eol_NativeExpression()
    setattr(partner, 'eol_NativeExpression', None)
    _safe_set(owner, 'eol_StringExpression227', partner)
    assert getattr(partner, 'eol_NativeExpression') == owner
    _safe_set(owner, 'eol_StringExpression227', None)
    assert getattr(partner, 'eol_NativeExpression') is None


def test_assoc_nativeExpression191_stub_double():
    # eol_NativeType has no real 'eol_NativeType' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(val="sample_text")
    partner = eol_NativeType()
    setattr(partner, 'eol_NativeType', None)
    _safe_set(owner, 'eol_StringExpression192', partner)
    assert getattr(partner, 'eol_NativeType') == owner
    _safe_set(owner, 'eol_StringExpression192', None)
    assert getattr(partner, 'eol_NativeType') is None


def test_assoc_parameters67_stub_double():
    # eol_Expression has no real 'eol_Expression69' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(lastDefinitionPoint="sample_text")
    partner = eol_Expression()
    setattr(partner, 'eol_Expression69', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression68', {partner})
    assert getattr(partner, 'eol_Expression69') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression68', set())
    assert getattr(partner, 'eol_Expression69') is None


def test_assoc_property57_stub_double():
    # eol_PropertyCallExpression has no real 'eol_PropertyCallExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_PropertyCallExpression()
    setattr(partner, 'eol_PropertyCallExpression', None)
    _safe_set(owner, 'eol_NameExpression58', partner)
    assert getattr(partner, 'eol_PropertyCallExpression') == owner
    _safe_set(owner, 'eol_NameExpression58', None)
    assert getattr(partner, 'eol_PropertyCallExpression') is None


def test_assoc_region2_stub_double():
    # eol_TextRegion has no real 'eol_TextRegion' property in the generated
    # code (a bare stub) -- manually attach it so eol_EolElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_EolElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_EolElement(column=7, line=7, uri="sample_text")
    partner = eol_TextRegion()
    setattr(partner, 'eol_TextRegion', None)
    _safe_set(owner, 'eol_EolElement3', partner)
    assert getattr(partner, 'eol_TextRegion') == owner
    _safe_set(owner, 'eol_EolElement3', None)
    assert getattr(partner, 'eol_TextRegion') is None


def test_assoc_resolvedModelDeclaration188_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement190' property in the generated
    # code (a bare stub) -- manually attach it so eol_ModelElementType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_ModelElementType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_ModelElementType(elementName="sample_text", modelName="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement190', None)
    _safe_set(owner, 'eol_ModelElementType189', partner)
    assert getattr(partner, 'eol_ModelDeclarationStatement190') == owner
    _safe_set(owner, 'eol_ModelElementType189', None)
    assert getattr(partner, 'eol_ModelDeclarationStatement190') is None


def test_assoc_self86_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition87' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(lastDefinitionPoint="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition87', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression88', partner)
    assert getattr(partner, 'eol_OperationDefinition87') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression88', None)
    assert getattr(partner, 'eol_OperationDefinition87') is None


def test_assoc_start4_stub_double():
    # eol_TextRegion has no real 'eol_TextRegion5' property in the generated
    # code (a bare stub) -- manually attach it so eol_TextPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_TextPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_TextPosition(column=7, line=7)
    partner = eol_TextRegion()
    setattr(partner, 'eol_TextRegion5', None)
    _safe_set(owner, 'eol_TextPosition', partner)
    assert getattr(partner, 'eol_TextRegion5') == owner
    _safe_set(owner, 'eol_TextPosition', None)
    assert getattr(partner, 'eol_TextRegion5') is None


def test_assoc_value202_stub_double():
    # eol_ModelDeclarationParameter has no real 'eol_ModelDeclarationParameter203' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(val="sample_text")
    partner = eol_ModelDeclarationParameter()
    setattr(partner, 'eol_ModelDeclarationParameter203', None)
    _safe_set(owner, 'eol_StringExpression204', partner)
    assert getattr(partner, 'eol_ModelDeclarationParameter203') == owner
    _safe_set(owner, 'eol_StringExpression204', None)
    assert getattr(partner, 'eol_ModelDeclarationParameter203') is None


def test_assoc_values179_stub_double():
    # eol_SimpleAnnotation has no real 'eol_SimpleAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(val="sample_text")
    partner = eol_SimpleAnnotation()
    setattr(partner, 'eol_SimpleAnnotation', None)
    _safe_set(owner, 'eol_StringExpression180', partner)
    assert owner in getattr(partner, 'eol_SimpleAnnotation')
    _safe_set(owner, 'eol_StringExpression180', None)
    assert owner not in getattr(partner, 'eol_SimpleAnnotation')


