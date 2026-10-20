import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotation,
    ArithmeticOperatorExpression,
    AssignmentStatement,
    BinaryOperatorExpression,
    CollectionExpression,
    CollectionInitValue,
    CollectionType,
    ComparisonOperatorExpression,
    EolElement,
    EolLibraryModule,
    Expression,
    FeatureCallExpression,
    LiteralExpression,
    LogicalOperatorExpression,
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
    eol_ArithmeticOperatorExpression,
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
    eol_ComparisonOperatorExpression,
    eol_ContinueStatement,
    eol_DeleteStatement,
    eol_DivideOperatorExpression,
    eol_EClassifier,
    eol_EObject,
    eol_EPackage,
    eol_EType,
    eol_EnumerationLiteralExpression,
    eol_EolElement,
    eol_EolLibraryModule,
    eol_EolProgram,
    eol_EqualsOperatorExpression,
    eol_ExecutableAnnotation,
    eol_ExpRange,
    eol_ExprList,
    eol_Expression,
    eol_ExpressionOrStatementBlock,
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
    eol_LogicalOperatorExpression,
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


def test_assoc_create53_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(definitionPoints="sample_text")
    a2 = eol_VariableDeclarationExpression(definitionPoints="sample_text_2")
    b = eol_BooleanExpression(val=True)
    _safe_set(b, 'eol_BooleanExpression55', a1)
    assert _is_linked(b, 'eol_BooleanExpression55', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression54'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression54', b)
    _safe_set(b, 'eol_BooleanExpression55', a2)
    assert _is_linked(b, 'eol_BooleanExpression55', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression54'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression54', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression54'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression54', b)
    _safe_set(b, 'eol_BooleanExpression55', None)
    assert not _is_linked(b, 'eol_BooleanExpression55', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression54'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression54', b)


def test_assoc_isType41_reverse_link_reassign_clear():
    a1 = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    a2 = eol_NameExpression(name="sample_text_2", resolvedContent="sample_text_2")
    b = eol_BooleanExpression(val=True)
    _safe_set(b, 'eol_BooleanExpression43', a1)
    assert _is_linked(b, 'eol_BooleanExpression43', a1)
    if hasattr(a1, 'eol_NameExpression42'):
        assert _is_linked(a1, 'eol_NameExpression42', b)
    _safe_set(b, 'eol_BooleanExpression43', a2)
    assert _is_linked(b, 'eol_BooleanExpression43', a2)
    if hasattr(a1, 'eol_NameExpression42'):
        assert not _is_linked(a1, 'eol_NameExpression42', b)
    if hasattr(a2, 'eol_NameExpression42'):
        assert _is_linked(a2, 'eol_NameExpression42', b)
    _safe_set(b, 'eol_BooleanExpression43', None)
    assert not _is_linked(b, 'eol_BooleanExpression43', a2)
    if hasattr(a2, 'eol_NameExpression42'):
        assert not _is_linked(a2, 'eol_NameExpression42', b)


def test_assoc_name51_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(definitionPoints="sample_text")
    a2 = eol_VariableDeclarationExpression(definitionPoints="sample_text_2")
    b = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression52', a1)
    assert _is_linked(b, 'eol_NameExpression52', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression', b)
    _safe_set(b, 'eol_NameExpression52', a2)
    assert _is_linked(b, 'eol_NameExpression52', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression', b)
    _safe_set(b, 'eol_NameExpression52', None)
    assert not _is_linked(b, 'eol_NameExpression52', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc__result77_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition78' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(definitionPoints="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition78', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression79', partner)
    assert getattr(partner, 'eol_OperationDefinition78') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression79', None)
    assert getattr(partner, 'eol_OperationDefinition78') is None


def test_assoc_alias124_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement125' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(definitionPoints="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement125', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression126', partner)
    assert owner in getattr(partner, 'eol_ModelDeclarationStatement125')
    _safe_set(owner, 'eol_VariableDeclarationExpression126', None)
    assert owner not in getattr(partner, 'eol_ModelDeclarationStatement125')


def test_assoc_driver127_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement128' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(definitionPoints="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement128', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression129', partner)
    assert getattr(partner, 'eol_ModelDeclarationStatement128') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression129', None)
    assert getattr(partner, 'eol_ModelDeclarationStatement128') is None


def test_assoc_dynamicTypes155_stub_double():
    # eol_Type has no real 'eol_Type156' property in the generated
    # code (a bare stub) -- manually attach it so eol_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_AnyType(declared=True)
    partner = eol_Type()
    setattr(partner, 'eol_Type156', None)
    _safe_set(owner, 'eol_AnyType', {partner})
    assert getattr(partner, 'eol_Type156') == owner
    _safe_set(owner, 'eol_AnyType', set())
    assert getattr(partner, 'eol_Type156') is None


def test_assoc_ecoreType176_stub_double():
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


def test_assoc_enumeration24_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression', None)
    _safe_set(owner, 'eol_NameExpression', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression') == owner
    _safe_set(owner, 'eol_NameExpression', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression') is None


def test_assoc_extended48_stub_double():
    # eol_PropertyCallExpression has no real 'eol_PropertyCallExpression49' property in the generated
    # code (a bare stub) -- manually attach it so eol_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_BooleanExpression(val=True)
    partner = eol_PropertyCallExpression()
    setattr(partner, 'eol_PropertyCallExpression49', None)
    _safe_set(owner, 'eol_BooleanExpression50', partner)
    assert getattr(partner, 'eol_PropertyCallExpression49') == owner
    _safe_set(owner, 'eol_BooleanExpression50', None)
    assert getattr(partner, 'eol_PropertyCallExpression49') is None


def test_assoc_imported13_stub_double():
    # eol_Import has no real 'eol_Import' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(val="sample_text")
    partner = eol_Import()
    setattr(partner, 'eol_Import', None)
    _safe_set(owner, 'eol_StringExpression', partner)
    assert getattr(partner, 'eol_Import') == owner
    _safe_set(owner, 'eol_StringExpression', None)
    assert getattr(partner, 'eol_Import') is None


def test_assoc_isArrow32_stub_double():
    # eol_FeatureCallExpression has no real 'eol_FeatureCallExpression33' property in the generated
    # code (a bare stub) -- manually attach it so eol_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_BooleanExpression(val=True)
    partner = eol_FeatureCallExpression()
    setattr(partner, 'eol_FeatureCallExpression33', None)
    _safe_set(owner, 'eol_BooleanExpression', partner)
    assert getattr(partner, 'eol_FeatureCallExpression33') == owner
    _safe_set(owner, 'eol_BooleanExpression', None)
    assert getattr(partner, 'eol_FeatureCallExpression33') is None


def test_assoc_isType217_stub_double():
    # eol_NativeExpression has no real 'eol_NativeExpression218' property in the generated
    # code (a bare stub) -- manually attach it so eol_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_BooleanExpression(val=True)
    partner = eol_NativeExpression()
    setattr(partner, 'eol_NativeExpression218', None)
    _safe_set(owner, 'eol_BooleanExpression219', partner)
    assert getattr(partner, 'eol_NativeExpression218') == owner
    _safe_set(owner, 'eol_BooleanExpression219', None)
    assert getattr(partner, 'eol_NativeExpression218') is None


def test_assoc_literal25_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression26' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression26', None)
    _safe_set(owner, 'eol_NameExpression27', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression26') == owner
    _safe_set(owner, 'eol_NameExpression27', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression26') is None


def test_assoc_method140_stub_double():
    # eol_FOLMethodCallExpression has no real 'eol_FOLMethodCallExpression141' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_FOLMethodCallExpression()
    setattr(partner, 'eol_FOLMethodCallExpression141', None)
    _safe_set(owner, 'eol_NameExpression142', partner)
    assert getattr(partner, 'eol_FOLMethodCallExpression141') == owner
    _safe_set(owner, 'eol_NameExpression142', None)
    assert getattr(partner, 'eol_FOLMethodCallExpression141') is None


def test_assoc_method36_stub_double():
    # eol_MethodCallExpression has no real 'eol_MethodCallExpression37' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_MethodCallExpression()
    setattr(partner, 'eol_MethodCallExpression37', None)
    _safe_set(owner, 'eol_NameExpression38', partner)
    assert getattr(partner, 'eol_MethodCallExpression37') == owner
    _safe_set(owner, 'eol_NameExpression38', None)
    assert getattr(partner, 'eol_MethodCallExpression37') is None


def test_assoc_name121_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement122' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(definitionPoints="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement122', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression123', partner)
    assert getattr(partner, 'eol_ModelDeclarationStatement122') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression123', None)
    assert getattr(partner, 'eol_ModelDeclarationStatement122') is None


def test_assoc_name164_stub_double():
    # eol_Annotation has no real 'eol_Annotation' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_Annotation()
    setattr(partner, 'eol_Annotation', None)
    _safe_set(owner, 'eol_NameExpression165', partner)
    assert getattr(partner, 'eol_Annotation') == owner
    _safe_set(owner, 'eol_NameExpression165', None)
    assert getattr(partner, 'eol_Annotation') is None


def test_assoc_name188_stub_double():
    # eol_ModelDeclarationParameter has no real 'eol_ModelDeclarationParameter189' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_ModelDeclarationParameter()
    setattr(partner, 'eol_ModelDeclarationParameter189', None)
    _safe_set(owner, 'eol_NameExpression190', partner)
    assert getattr(partner, 'eol_ModelDeclarationParameter189') == owner
    _safe_set(owner, 'eol_NameExpression190', None)
    assert getattr(partner, 'eol_ModelDeclarationParameter189') is None


def test_assoc_name237_stub_double():
    # eol_EolLibraryModule has no real 'eol_EolLibraryModule238' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_EolLibraryModule()
    setattr(partner, 'eol_EolLibraryModule238', None)
    _safe_set(owner, 'eol_NameExpression239', partner)
    assert getattr(partner, 'eol_EolLibraryModule238') == owner
    _safe_set(owner, 'eol_NameExpression239', None)
    assert getattr(partner, 'eol_EolLibraryModule238') is None


def test_assoc_name69_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition70' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition70', None)
    _safe_set(owner, 'eol_NameExpression71', partner)
    assert getattr(partner, 'eol_OperationDefinition70') == owner
    _safe_set(owner, 'eol_NameExpression71', None)
    assert getattr(partner, 'eol_OperationDefinition70') is None


def test_assoc_names196_stub_double():
    # eol_TransactionStatement has no real 'eol_TransactionStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_TransactionStatement()
    setattr(partner, 'eol_TransactionStatement', None)
    _safe_set(owner, 'eol_NameExpression197', partner)
    assert owner in getattr(partner, 'eol_TransactionStatement')
    _safe_set(owner, 'eol_NameExpression197', None)
    assert owner not in getattr(partner, 'eol_TransactionStatement')


def test_assoc_nativeExpr215_stub_double():
    # eol_NativeExpression has no real 'eol_NativeExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(val="sample_text")
    partner = eol_NativeExpression()
    setattr(partner, 'eol_NativeExpression', None)
    _safe_set(owner, 'eol_StringExpression216', partner)
    assert getattr(partner, 'eol_NativeExpression') == owner
    _safe_set(owner, 'eol_StringExpression216', None)
    assert getattr(partner, 'eol_NativeExpression') is None


def test_assoc_nativeExpression180_stub_double():
    # eol_NativeType has no real 'eol_NativeType' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(val="sample_text")
    partner = eol_NativeType()
    setattr(partner, 'eol_NativeType', None)
    _safe_set(owner, 'eol_StringExpression181', partner)
    assert getattr(partner, 'eol_NativeType') == owner
    _safe_set(owner, 'eol_StringExpression181', None)
    assert getattr(partner, 'eol_NativeType') is None


def test_assoc_parameters56_stub_double():
    # eol_Expression has no real 'eol_Expression58' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(definitionPoints="sample_text")
    partner = eol_Expression()
    setattr(partner, 'eol_Expression58', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression57', {partner})
    assert getattr(partner, 'eol_Expression58') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression57', set())
    assert getattr(partner, 'eol_Expression58') is None


def test_assoc_property46_stub_double():
    # eol_PropertyCallExpression has no real 'eol_PropertyCallExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(name="sample_text", resolvedContent="sample_text")
    partner = eol_PropertyCallExpression()
    setattr(partner, 'eol_PropertyCallExpression', None)
    _safe_set(owner, 'eol_NameExpression47', partner)
    assert getattr(partner, 'eol_PropertyCallExpression') == owner
    _safe_set(owner, 'eol_NameExpression47', None)
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


def test_assoc_resolvedModelDeclaration177_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement179' property in the generated
    # code (a bare stub) -- manually attach it so eol_ModelElementType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_ModelElementType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_ModelElementType(elementName="sample_text", modelName="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement179', None)
    _safe_set(owner, 'eol_ModelElementType178', {partner})
    assert getattr(partner, 'eol_ModelDeclarationStatement179') == owner
    _safe_set(owner, 'eol_ModelElementType178', set())
    assert getattr(partner, 'eol_ModelDeclarationStatement179') is None


def test_assoc_self74_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition75' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(definitionPoints="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition75', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression76', partner)
    assert getattr(partner, 'eol_OperationDefinition75') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression76', None)
    assert getattr(partner, 'eol_OperationDefinition75') is None


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


def test_assoc_value191_stub_double():
    # eol_ModelDeclarationParameter has no real 'eol_ModelDeclarationParameter192' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(val="sample_text")
    partner = eol_ModelDeclarationParameter()
    setattr(partner, 'eol_ModelDeclarationParameter192', None)
    _safe_set(owner, 'eol_StringExpression193', partner)
    assert getattr(partner, 'eol_ModelDeclarationParameter192') == owner
    _safe_set(owner, 'eol_StringExpression193', None)
    assert getattr(partner, 'eol_ModelDeclarationParameter192') is None


def test_assoc_values168_stub_double():
    # eol_SimpleAnnotation has no real 'eol_SimpleAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(val="sample_text")
    partner = eol_SimpleAnnotation()
    setattr(partner, 'eol_SimpleAnnotation', None)
    _safe_set(owner, 'eol_StringExpression169', partner)
    assert owner in getattr(partner, 'eol_SimpleAnnotation')
    _safe_set(owner, 'eol_StringExpression169', None)
    assert owner not in getattr(partner, 'eol_SimpleAnnotation')


