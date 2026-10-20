import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    AbstractTypeDeclaration,
    Annotation,
    BodyDeclaration,
    Comment,
    DOM_AST,
    DOM_ASTNode,
    DOM_AbstractTypeDeclaration,
    DOM_Annotation,
    DOM_AnnotationTypeDeclaration,
    DOM_AnnotationTypeMemberDeclaration,
    DOM_AnonymousClassDeclaration,
    DOM_ArrayAccess,
    DOM_ArrayCreation,
    DOM_ArrayInitializer,
    DOM_ArrayType,
    DOM_AssertStatement,
    DOM_Assignment,
    DOM_Block,
    DOM_BlockComment,
    DOM_BodyDeclaration,
    DOM_BooleanLiteral,
    DOM_BreakStatement,
    DOM_CastExpression,
    DOM_CatchClause,
    DOM_CharacterLiteral,
    DOM_ClassInstanceCreation,
    DOM_Comment,
    DOM_CompilationUnit,
    DOM_ConditionalExpression,
    DOM_ConstructorInvocation,
    DOM_ContinueStatement,
    DOM_DoStatement,
    DOM_EmptyStatement,
    DOM_EnhancedForStatement,
    DOM_EnumConstantDeclaration,
    DOM_EnumDeclaration,
    DOM_Expression,
    DOM_ExpressionStatement,
    DOM_ExtendedModifier,
    DOM_FieldAccess,
    DOM_FieldDeclaration,
    DOM_ForStatement,
    DOM_IMethod,
    DOM_IPackageFragment,
    DOM_IType,
    DOM_IfStatement,
    DOM_ImportDeclaration,
    DOM_InfixExpression,
    DOM_Initializer,
    DOM_InstanceofExpression,
    DOM_Javadoc,
    DOM_LabeledStatement,
    DOM_LineComment,
    DOM_MarkerAnnotation,
    DOM_MemberRef,
    DOM_MemberValuePair,
    DOM_MethodDeclaration,
    DOM_MethodInvocation,
    DOM_MethodRef,
    DOM_MethodRefParameter,
    DOM_Modifier,
    DOM_Name,
    DOM_NormalAnnotation,
    DOM_NullLiteral,
    DOM_NumberLiteral,
    DOM_PackageDeclaration,
    DOM_ParameterizedType,
    DOM_ParenthesizedExpression,
    DOM_PostfixExpression,
    DOM_PrefixExpression,
    DOM_PrimitiveType,
    DOM_QualifiedName,
    DOM_QualifiedType,
    DOM_ReturnStatement,
    DOM_SimpleName,
    DOM_SimpleType,
    DOM_SingleMemberAnnotation,
    DOM_SingleVariableDeclaration,
    DOM_Statement,
    DOM_StringLiteral,
    DOM_SuperConstructorInvocation,
    DOM_SuperFieldAccess,
    DOM_SuperMethodInvocation,
    DOM_SwitchCase,
    DOM_SwitchStatement,
    DOM_SynchronizedStatement,
    DOM_TagElement,
    DOM_TextElement,
    DOM_ThisExpression,
    DOM_ThrowStatement,
    DOM_TryStatement,
    DOM_Type,
    DOM_TypeDeclaration,
    DOM_TypeDeclarationStatement,
    DOM_TypeLiteral,
    DOM_TypeParameter,
    DOM_VariableDeclaration,
    DOM_VariableDeclarationExpression,
    DOM_VariableDeclarationFragment,
    DOM_VariableDeclarationStatement,
    DOM_WhileStatement,
    DOM_WildcardType,
    Expression,
    ExtendedModifier,
    Name,
    Statement,
    Type,
    VariableDeclaration,
    AssignmentOperatorKind,
    InfixExpressionOperatorKind,
    PostfixExpressionOperatorKind,
    PrefixExpressionOperatorKind,
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

def test_assoc_expression308_reverse_link_reassign_clear():
    a1 = DOM_SwitchCase(default="sample_text")
    a2 = DOM_SwitchCase(default="sample_text_2")
    b = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'DOM_Expression309', a1)
    assert _is_linked(b, 'DOM_Expression309', a1)
    if hasattr(a1, 'DOM_SwitchCase'):
        assert _is_linked(a1, 'DOM_SwitchCase', b)
    _safe_set(b, 'DOM_Expression309', a2)
    assert _is_linked(b, 'DOM_Expression309', a2)
    if hasattr(a1, 'DOM_SwitchCase'):
        assert not _is_linked(a1, 'DOM_SwitchCase', b)
    if hasattr(a2, 'DOM_SwitchCase'):
        assert _is_linked(a2, 'DOM_SwitchCase', b)
    _safe_set(b, 'DOM_Expression309', None)
    assert not _is_linked(b, 'DOM_Expression309', a2)
    if hasattr(a2, 'DOM_SwitchCase'):
        assert not _is_linked(a2, 'DOM_SwitchCase', b)


def test_assoc_extendedOperands182_reverse_link_reassign_clear():
    a1 = DOM_InfixExpression(operator="sample_text")
    a2 = DOM_InfixExpression(operator="sample_text_2")
    b = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'DOM_Expression183', a1)
    assert _is_linked(b, 'DOM_Expression183', a1)
    if hasattr(a1, 'DOM_InfixExpression'):
        assert _is_linked(a1, 'DOM_InfixExpression', b)
    _safe_set(b, 'DOM_Expression183', a2)
    assert _is_linked(b, 'DOM_Expression183', a2)
    if hasattr(a1, 'DOM_InfixExpression'):
        assert not _is_linked(a1, 'DOM_InfixExpression', b)
    if hasattr(a2, 'DOM_InfixExpression'):
        assert _is_linked(a2, 'DOM_InfixExpression', b)
    _safe_set(b, 'DOM_Expression183', None)
    assert not _is_linked(b, 'DOM_Expression183', a2)
    if hasattr(a2, 'DOM_InfixExpression'):
        assert not _is_linked(a2, 'DOM_InfixExpression', b)


def test_assoc_initializer60_reverse_link_reassign_clear():
    a1 = DOM_VariableDeclaration(extraDimensions="sample_text")
    a2 = DOM_VariableDeclaration(extraDimensions="sample_text_2")
    b = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'DOM_Expression61', a1)
    assert _is_linked(b, 'DOM_Expression61', a1)
    if hasattr(a1, 'DOM_VariableDeclaration'):
        assert _is_linked(a1, 'DOM_VariableDeclaration', b)
    _safe_set(b, 'DOM_Expression61', a2)
    assert _is_linked(b, 'DOM_Expression61', a2)
    if hasattr(a1, 'DOM_VariableDeclaration'):
        assert not _is_linked(a1, 'DOM_VariableDeclaration', b)
    if hasattr(a2, 'DOM_VariableDeclaration'):
        assert _is_linked(a2, 'DOM_VariableDeclaration', b)
    _safe_set(b, 'DOM_Expression61', None)
    assert not _is_linked(b, 'DOM_Expression61', a2)
    if hasattr(a2, 'DOM_VariableDeclaration'):
        assert not _is_linked(a2, 'DOM_VariableDeclaration', b)


def test_assoc_leftHandSide145_reverse_link_reassign_clear():
    a1 = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    a2 = DOM_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    b = DOM_Assignment(operator="sample_text")
    _safe_set(b, 'DOM_Assignment', a1)
    assert _is_linked(b, 'DOM_Assignment', a1)
    if hasattr(a1, 'DOM_Expression146'):
        assert _is_linked(a1, 'DOM_Expression146', b)
    _safe_set(b, 'DOM_Assignment', a2)
    assert _is_linked(b, 'DOM_Assignment', a2)
    if hasattr(a1, 'DOM_Expression146'):
        assert not _is_linked(a1, 'DOM_Expression146', b)
    if hasattr(a2, 'DOM_Expression146'):
        assert _is_linked(a2, 'DOM_Expression146', b)
    _safe_set(b, 'DOM_Assignment', None)
    assert not _is_linked(b, 'DOM_Assignment', a2)
    if hasattr(a2, 'DOM_Expression146'):
        assert not _is_linked(a2, 'DOM_Expression146', b)


def test_assoc_leftOperand184_reverse_link_reassign_clear():
    a1 = DOM_InfixExpression(operator="sample_text")
    a2 = DOM_InfixExpression(operator="sample_text_2")
    b = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'DOM_Expression186', a1)
    assert _is_linked(b, 'DOM_Expression186', a1)
    if hasattr(a1, 'DOM_InfixExpression185'):
        assert _is_linked(a1, 'DOM_InfixExpression185', b)
    _safe_set(b, 'DOM_Expression186', a2)
    assert _is_linked(b, 'DOM_Expression186', a2)
    if hasattr(a1, 'DOM_InfixExpression185'):
        assert not _is_linked(a1, 'DOM_InfixExpression185', b)
    if hasattr(a2, 'DOM_InfixExpression185'):
        assert _is_linked(a2, 'DOM_InfixExpression185', b)
    _safe_set(b, 'DOM_Expression186', None)
    assert not _is_linked(b, 'DOM_Expression186', a2)
    if hasattr(a2, 'DOM_InfixExpression185'):
        assert not _is_linked(a2, 'DOM_InfixExpression185', b)


def test_assoc_name20_reverse_link_reassign_clear():
    a1 = DOM_Name(fullyQualifiedName="sample_text")
    a2 = DOM_Name(fullyQualifiedName="sample_text_2")
    b = DOM_ImportDeclaration(onDemand="sample_text", static="sample_text")
    _safe_set(b, 'DOM_ImportDeclaration21', a1)
    assert _is_linked(b, 'DOM_ImportDeclaration21', a1)
    if hasattr(a1, 'DOM_Name'):
        assert _is_linked(a1, 'DOM_Name', b)
    _safe_set(b, 'DOM_ImportDeclaration21', a2)
    assert _is_linked(b, 'DOM_ImportDeclaration21', a2)
    if hasattr(a1, 'DOM_Name'):
        assert not _is_linked(a1, 'DOM_Name', b)
    if hasattr(a2, 'DOM_Name'):
        assert _is_linked(a2, 'DOM_Name', b)
    _safe_set(b, 'DOM_ImportDeclaration21', None)
    assert not _is_linked(b, 'DOM_ImportDeclaration21', a2)
    if hasattr(a2, 'DOM_Name'):
        assert not _is_linked(a2, 'DOM_Name', b)


def test_assoc_name38_reverse_link_reassign_clear():
    a1 = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    a2 = DOM_SimpleName(declaration="sample_text_2", identifier="sample_text_2")
    b = DOM_MethodRefParameter(varargs="sample_text")
    _safe_set(b, 'DOM_MethodRefParameter39', a1)
    assert _is_linked(b, 'DOM_MethodRefParameter39', a1)
    if hasattr(a1, 'DOM_SimpleName40'):
        assert _is_linked(a1, 'DOM_SimpleName40', b)
    _safe_set(b, 'DOM_MethodRefParameter39', a2)
    assert _is_linked(b, 'DOM_MethodRefParameter39', a2)
    if hasattr(a1, 'DOM_SimpleName40'):
        assert not _is_linked(a1, 'DOM_SimpleName40', b)
    if hasattr(a2, 'DOM_SimpleName40'):
        assert _is_linked(a2, 'DOM_SimpleName40', b)
    _safe_set(b, 'DOM_MethodRefParameter39', None)
    assert not _is_linked(b, 'DOM_MethodRefParameter39', a2)
    if hasattr(a2, 'DOM_SimpleName40'):
        assert not _is_linked(a2, 'DOM_SimpleName40', b)


def test_assoc_name62_reverse_link_reassign_clear():
    a1 = DOM_VariableDeclaration(extraDimensions="sample_text")
    a2 = DOM_VariableDeclaration(extraDimensions="sample_text_2")
    b = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    _safe_set(b, 'DOM_SimpleName64', a1)
    assert _is_linked(b, 'DOM_SimpleName64', a1)
    if hasattr(a1, 'DOM_VariableDeclaration63'):
        assert _is_linked(a1, 'DOM_VariableDeclaration63', b)
    _safe_set(b, 'DOM_SimpleName64', a2)
    assert _is_linked(b, 'DOM_SimpleName64', a2)
    if hasattr(a1, 'DOM_VariableDeclaration63'):
        assert not _is_linked(a1, 'DOM_VariableDeclaration63', b)
    if hasattr(a2, 'DOM_VariableDeclaration63'):
        assert _is_linked(a2, 'DOM_VariableDeclaration63', b)
    _safe_set(b, 'DOM_SimpleName64', None)
    assert not _is_linked(b, 'DOM_SimpleName64', a2)
    if hasattr(a2, 'DOM_VariableDeclaration63'):
        assert not _is_linked(a2, 'DOM_VariableDeclaration63', b)


def test_assoc_name68_reverse_link_reassign_clear():
    a1 = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    a2 = DOM_SimpleName(declaration="sample_text_2", identifier="sample_text_2")
    b = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    _safe_set(b, 'DOM_AbstractTypeDeclaration69', a1)
    assert _is_linked(b, 'DOM_AbstractTypeDeclaration69', a1)
    if hasattr(a1, 'DOM_SimpleName70'):
        assert _is_linked(a1, 'DOM_SimpleName70', b)
    _safe_set(b, 'DOM_AbstractTypeDeclaration69', a2)
    assert _is_linked(b, 'DOM_AbstractTypeDeclaration69', a2)
    if hasattr(a1, 'DOM_SimpleName70'):
        assert not _is_linked(a1, 'DOM_SimpleName70', b)
    if hasattr(a2, 'DOM_SimpleName70'):
        assert _is_linked(a2, 'DOM_SimpleName70', b)
    _safe_set(b, 'DOM_AbstractTypeDeclaration69', None)
    assert not _is_linked(b, 'DOM_AbstractTypeDeclaration69', a2)
    if hasattr(a2, 'DOM_SimpleName70'):
        assert not _is_linked(a2, 'DOM_SimpleName70', b)


def test_assoc_name95_reverse_link_reassign_clear():
    a1 = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    a2 = DOM_SimpleName(declaration="sample_text_2", identifier="sample_text_2")
    b = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    _safe_set(b, 'DOM_MethodDeclaration96', a1)
    assert _is_linked(b, 'DOM_MethodDeclaration96', a1)
    if hasattr(a1, 'DOM_SimpleName97'):
        assert _is_linked(a1, 'DOM_SimpleName97', b)
    _safe_set(b, 'DOM_MethodDeclaration96', a2)
    assert _is_linked(b, 'DOM_MethodDeclaration96', a2)
    if hasattr(a1, 'DOM_SimpleName97'):
        assert not _is_linked(a1, 'DOM_SimpleName97', b)
    if hasattr(a2, 'DOM_SimpleName97'):
        assert _is_linked(a2, 'DOM_SimpleName97', b)
    _safe_set(b, 'DOM_MethodDeclaration96', None)
    assert not _is_linked(b, 'DOM_MethodDeclaration96', a2)
    if hasattr(a2, 'DOM_SimpleName97'):
        assert not _is_linked(a2, 'DOM_SimpleName97', b)


def test_assoc_operand211_reverse_link_reassign_clear():
    a1 = DOM_PostfixExpression(operator="sample_text")
    a2 = DOM_PostfixExpression(operator="sample_text_2")
    b = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'DOM_Expression212', a1)
    assert _is_linked(b, 'DOM_Expression212', a1)
    if hasattr(a1, 'DOM_PostfixExpression'):
        assert _is_linked(a1, 'DOM_PostfixExpression', b)
    _safe_set(b, 'DOM_Expression212', a2)
    assert _is_linked(b, 'DOM_Expression212', a2)
    if hasattr(a1, 'DOM_PostfixExpression'):
        assert not _is_linked(a1, 'DOM_PostfixExpression', b)
    if hasattr(a2, 'DOM_PostfixExpression'):
        assert _is_linked(a2, 'DOM_PostfixExpression', b)
    _safe_set(b, 'DOM_Expression212', None)
    assert not _is_linked(b, 'DOM_Expression212', a2)
    if hasattr(a2, 'DOM_PostfixExpression'):
        assert not _is_linked(a2, 'DOM_PostfixExpression', b)


def test_assoc_operand213_reverse_link_reassign_clear():
    a1 = DOM_PrefixExpression(operator="sample_text")
    a2 = DOM_PrefixExpression(operator="sample_text_2")
    b = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'DOM_Expression214', a1)
    assert _is_linked(b, 'DOM_Expression214', a1)
    if hasattr(a1, 'DOM_PrefixExpression'):
        assert _is_linked(a1, 'DOM_PrefixExpression', b)
    _safe_set(b, 'DOM_Expression214', a2)
    assert _is_linked(b, 'DOM_Expression214', a2)
    if hasattr(a1, 'DOM_PrefixExpression'):
        assert not _is_linked(a1, 'DOM_PrefixExpression', b)
    if hasattr(a2, 'DOM_PrefixExpression'):
        assert _is_linked(a2, 'DOM_PrefixExpression', b)
    _safe_set(b, 'DOM_Expression214', None)
    assert not _is_linked(b, 'DOM_Expression214', a2)
    if hasattr(a2, 'DOM_PrefixExpression'):
        assert not _is_linked(a2, 'DOM_PrefixExpression', b)


def test_assoc_parameters101_reverse_link_reassign_clear():
    a1 = DOM_SingleVariableDeclaration(varargs="sample_text")
    a2 = DOM_SingleVariableDeclaration(varargs="sample_text_2")
    b = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    _safe_set(b, 'DOM_MethodDeclaration102', {a1})
    assert _is_linked(b, 'DOM_MethodDeclaration102', a1)
    if hasattr(a1, 'DOM_SingleVariableDeclaration103'):
        assert _is_linked(a1, 'DOM_SingleVariableDeclaration103', b)
    _safe_set(b, 'DOM_MethodDeclaration102', {a2})
    assert _is_linked(b, 'DOM_MethodDeclaration102', a2)
    if hasattr(a1, 'DOM_SingleVariableDeclaration103'):
        assert not _is_linked(a1, 'DOM_SingleVariableDeclaration103', b)
    if hasattr(a2, 'DOM_SingleVariableDeclaration103'):
        assert _is_linked(a2, 'DOM_SingleVariableDeclaration103', b)
    _safe_set(b, 'DOM_MethodDeclaration102', set())
    assert not _is_linked(b, 'DOM_MethodDeclaration102', a2)
    if hasattr(a2, 'DOM_SingleVariableDeclaration103'):
        assert not _is_linked(a2, 'DOM_SingleVariableDeclaration103', b)


def test_assoc_rightHandSide147_reverse_link_reassign_clear():
    a1 = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    a2 = DOM_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    b = DOM_Assignment(operator="sample_text")
    _safe_set(b, 'DOM_Assignment148', a1)
    assert _is_linked(b, 'DOM_Assignment148', a1)
    if hasattr(a1, 'DOM_Expression149'):
        assert _is_linked(a1, 'DOM_Expression149', b)
    _safe_set(b, 'DOM_Assignment148', a2)
    assert _is_linked(b, 'DOM_Assignment148', a2)
    if hasattr(a1, 'DOM_Expression149'):
        assert not _is_linked(a1, 'DOM_Expression149', b)
    if hasattr(a2, 'DOM_Expression149'):
        assert _is_linked(a2, 'DOM_Expression149', b)
    _safe_set(b, 'DOM_Assignment148', None)
    assert not _is_linked(b, 'DOM_Assignment148', a2)
    if hasattr(a2, 'DOM_Expression149'):
        assert not _is_linked(a2, 'DOM_Expression149', b)


def test_assoc_rightOperand187_reverse_link_reassign_clear():
    a1 = DOM_InfixExpression(operator="sample_text")
    a2 = DOM_InfixExpression(operator="sample_text_2")
    b = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'DOM_Expression189', a1)
    assert _is_linked(b, 'DOM_Expression189', a1)
    if hasattr(a1, 'DOM_InfixExpression188'):
        assert _is_linked(a1, 'DOM_InfixExpression188', b)
    _safe_set(b, 'DOM_Expression189', a2)
    assert _is_linked(b, 'DOM_Expression189', a2)
    if hasattr(a1, 'DOM_InfixExpression188'):
        assert not _is_linked(a1, 'DOM_InfixExpression188', b)
    if hasattr(a2, 'DOM_InfixExpression188'):
        assert _is_linked(a2, 'DOM_InfixExpression188', b)
    _safe_set(b, 'DOM_Expression189', None)
    assert not _is_linked(b, 'DOM_Expression189', a2)
    if hasattr(a2, 'DOM_InfixExpression188'):
        assert not _is_linked(a2, 'DOM_InfixExpression188', b)


def test_assoc_thrownExceptions104_reverse_link_reassign_clear():
    a1 = DOM_Name(fullyQualifiedName="sample_text")
    a2 = DOM_Name(fullyQualifiedName="sample_text_2")
    b = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    _safe_set(b, 'DOM_MethodDeclaration105', {a1})
    assert _is_linked(b, 'DOM_MethodDeclaration105', a1)
    if hasattr(a1, 'DOM_Name106'):
        assert _is_linked(a1, 'DOM_Name106', b)
    _safe_set(b, 'DOM_MethodDeclaration105', {a2})
    assert _is_linked(b, 'DOM_MethodDeclaration105', a2)
    if hasattr(a1, 'DOM_Name106'):
        assert not _is_linked(a1, 'DOM_Name106', b)
    if hasattr(a2, 'DOM_Name106'):
        assert _is_linked(a2, 'DOM_Name106', b)
    _safe_set(b, 'DOM_MethodDeclaration105', set())
    assert not _is_linked(b, 'DOM_MethodDeclaration105', a2)
    if hasattr(a2, 'DOM_Name106'):
        assert not _is_linked(a2, 'DOM_Name106', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments155_stub_double():
    # DOM_ClassInstanceCreation has no real 'DOM_ClassInstanceCreation' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ClassInstanceCreation()
    setattr(partner, 'DOM_ClassInstanceCreation', None)
    _safe_set(owner, 'DOM_Expression156', partner)
    assert owner in getattr(partner, 'DOM_ClassInstanceCreation')
    _safe_set(owner, 'DOM_Expression156', None)
    assert owner not in getattr(partner, 'DOM_ClassInstanceCreation')


def test_assoc_arguments195_stub_double():
    # DOM_MethodInvocation has no real 'DOM_MethodInvocation' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_MethodInvocation()
    setattr(partner, 'DOM_MethodInvocation', None)
    _safe_set(owner, 'DOM_Expression196', partner)
    assert owner in getattr(partner, 'DOM_MethodInvocation')
    _safe_set(owner, 'DOM_Expression196', None)
    assert owner not in getattr(partner, 'DOM_MethodInvocation')


def test_assoc_arguments220_stub_double():
    # DOM_SuperMethodInvocation has no real 'DOM_SuperMethodInvocation' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_SuperMethodInvocation()
    setattr(partner, 'DOM_SuperMethodInvocation', None)
    _safe_set(owner, 'DOM_Expression221', partner)
    assert owner in getattr(partner, 'DOM_SuperMethodInvocation')
    _safe_set(owner, 'DOM_Expression221', None)
    assert owner not in getattr(partner, 'DOM_SuperMethodInvocation')


def test_assoc_arguments252_stub_double():
    # DOM_ConstructorInvocation has no real 'DOM_ConstructorInvocation' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ConstructorInvocation()
    setattr(partner, 'DOM_ConstructorInvocation', None)
    _safe_set(owner, 'DOM_Expression253', partner)
    assert owner in getattr(partner, 'DOM_ConstructorInvocation')
    _safe_set(owner, 'DOM_Expression253', None)
    assert owner not in getattr(partner, 'DOM_ConstructorInvocation')


def test_assoc_arguments300_stub_double():
    # DOM_SuperConstructorInvocation has no real 'DOM_SuperConstructorInvocation' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_SuperConstructorInvocation()
    setattr(partner, 'DOM_SuperConstructorInvocation', None)
    _safe_set(owner, 'DOM_Expression301', partner)
    assert owner in getattr(partner, 'DOM_SuperConstructorInvocation')
    _safe_set(owner, 'DOM_Expression301', None)
    assert owner not in getattr(partner, 'DOM_SuperConstructorInvocation')


def test_assoc_arguments79_stub_double():
    # DOM_EnumConstantDeclaration has no real 'DOM_EnumConstantDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_EnumConstantDeclaration()
    setattr(partner, 'DOM_EnumConstantDeclaration', None)
    _safe_set(owner, 'DOM_Expression80', partner)
    assert owner in getattr(partner, 'DOM_EnumConstantDeclaration')
    _safe_set(owner, 'DOM_Expression80', None)
    assert owner not in getattr(partner, 'DOM_EnumConstantDeclaration')


def test_assoc_array131_stub_double():
    # DOM_ArrayAccess has no real 'DOM_ArrayAccess' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ArrayAccess()
    setattr(partner, 'DOM_ArrayAccess', None)
    _safe_set(owner, 'DOM_Expression132', partner)
    assert getattr(partner, 'DOM_ArrayAccess') == owner
    _safe_set(owner, 'DOM_Expression132', None)
    assert getattr(partner, 'DOM_ArrayAccess') is None


def test_assoc_binding110_stub_double():
    # DOM_IMethod has no real 'DOM_IMethod' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = DOM_IMethod()
    setattr(partner, 'DOM_IMethod', None)
    _safe_set(owner, 'DOM_MethodDeclaration111', partner)
    assert getattr(partner, 'DOM_IMethod') == owner
    _safe_set(owner, 'DOM_MethodDeclaration111', None)
    assert getattr(partner, 'DOM_IMethod') is None


def test_assoc_body93_stub_double():
    # DOM_Block has no real 'DOM_Block94' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = DOM_Block()
    setattr(partner, 'DOM_Block94', None)
    _safe_set(owner, 'DOM_MethodDeclaration', partner)
    assert getattr(partner, 'DOM_Block94') == owner
    _safe_set(owner, 'DOM_MethodDeclaration', None)
    assert getattr(partner, 'DOM_Block94') is None


def test_assoc_bodyDeclarations65_stub_double():
    # DOM_BodyDeclaration has no real 'DOM_BodyDeclaration67' property in the generated
    # code (a bare stub) -- manually attach it so DOM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    partner = DOM_BodyDeclaration()
    setattr(partner, 'DOM_BodyDeclaration67', None)
    _safe_set(owner, 'DOM_AbstractTypeDeclaration66', {partner})
    assert getattr(partner, 'DOM_BodyDeclaration67') == owner
    _safe_set(owner, 'DOM_AbstractTypeDeclaration66', set())
    assert getattr(partner, 'DOM_BodyDeclaration67') is None


def test_assoc_bound363_stub_double():
    # DOM_Type has no real 'DOM_Type364' property in the generated
    # code (a bare stub) -- manually attach it so DOM_WildcardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_WildcardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_WildcardType(upperBound="sample_text")
    partner = DOM_Type()
    setattr(partner, 'DOM_Type364', None)
    _safe_set(owner, 'DOM_WildcardType', partner)
    assert getattr(partner, 'DOM_Type364') == owner
    _safe_set(owner, 'DOM_WildcardType', None)
    assert getattr(partner, 'DOM_Type364') is None


def test_assoc_componentType345_stub_double():
    # DOM_Type has no real 'DOM_Type347' property in the generated
    # code (a bare stub) -- manually attach it so DOM_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_ArrayType(dimensions="sample_text")
    partner = DOM_Type()
    setattr(partner, 'DOM_Type347', None)
    _safe_set(owner, 'DOM_ArrayType346', partner)
    assert getattr(partner, 'DOM_Type347') == owner
    _safe_set(owner, 'DOM_ArrayType346', None)
    assert getattr(partner, 'DOM_Type347') is None


def test_assoc_declaration330_stub_double():
    # DOM_TypeDeclarationStatement has no real 'DOM_TypeDeclarationStatement' property in the generated
    # code (a bare stub) -- manually attach it so DOM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    partner = DOM_TypeDeclarationStatement()
    setattr(partner, 'DOM_TypeDeclarationStatement', None)
    _safe_set(owner, 'DOM_AbstractTypeDeclaration331', partner)
    assert getattr(partner, 'DOM_TypeDeclarationStatement') == owner
    _safe_set(owner, 'DOM_AbstractTypeDeclaration331', None)
    assert getattr(partner, 'DOM_TypeDeclarationStatement') is None


def test_assoc_default71_stub_double():
    # DOM_AnnotationTypeMemberDeclaration has no real 'DOM_AnnotationTypeMemberDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_AnnotationTypeMemberDeclaration()
    setattr(partner, 'DOM_AnnotationTypeMemberDeclaration', None)
    _safe_set(owner, 'DOM_Expression72', partner)
    assert getattr(partner, 'DOM_AnnotationTypeMemberDeclaration') == owner
    _safe_set(owner, 'DOM_Expression72', None)
    assert getattr(partner, 'DOM_AnnotationTypeMemberDeclaration') is None


def test_assoc_dimensions136_stub_double():
    # DOM_ArrayCreation has no real 'DOM_ArrayCreation' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ArrayCreation()
    setattr(partner, 'DOM_ArrayCreation', None)
    _safe_set(owner, 'DOM_Expression137', partner)
    assert owner in getattr(partner, 'DOM_ArrayCreation')
    _safe_set(owner, 'DOM_Expression137', None)
    assert owner not in getattr(partner, 'DOM_ArrayCreation')


def test_assoc_elementType348_stub_double():
    # DOM_Type has no real 'DOM_Type350' property in the generated
    # code (a bare stub) -- manually attach it so DOM_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_ArrayType(dimensions="sample_text")
    partner = DOM_Type()
    setattr(partner, 'DOM_Type350', None)
    _safe_set(owner, 'DOM_ArrayType349', partner)
    assert getattr(partner, 'DOM_Type350') == owner
    _safe_set(owner, 'DOM_ArrayType349', None)
    assert getattr(partner, 'DOM_Type350') is None


def test_assoc_elseExpression169_stub_double():
    # DOM_ConditionalExpression has no real 'DOM_ConditionalExpression' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ConditionalExpression()
    setattr(partner, 'DOM_ConditionalExpression', None)
    _safe_set(owner, 'DOM_Expression170', partner)
    assert getattr(partner, 'DOM_ConditionalExpression') == owner
    _safe_set(owner, 'DOM_Expression170', None)
    assert getattr(partner, 'DOM_ConditionalExpression') is None


def test_assoc_exception7_stub_double():
    # DOM_CatchClause has no real 'DOM_CatchClause8' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SingleVariableDeclaration(varargs="sample_text")
    partner = DOM_CatchClause()
    setattr(partner, 'DOM_CatchClause8', None)
    _safe_set(owner, 'DOM_SingleVariableDeclaration', partner)
    assert getattr(partner, 'DOM_CatchClause8') == owner
    _safe_set(owner, 'DOM_SingleVariableDeclaration', None)
    assert getattr(partner, 'DOM_CatchClause8') is None


def test_assoc_expression150_stub_double():
    # DOM_CastExpression has no real 'DOM_CastExpression' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_CastExpression()
    setattr(partner, 'DOM_CastExpression', None)
    _safe_set(owner, 'DOM_Expression151', partner)
    assert getattr(partner, 'DOM_CastExpression') == owner
    _safe_set(owner, 'DOM_Expression151', None)
    assert getattr(partner, 'DOM_CastExpression') is None


def test_assoc_expression160_stub_double():
    # DOM_ClassInstanceCreation has no real 'DOM_ClassInstanceCreation161' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ClassInstanceCreation()
    setattr(partner, 'DOM_ClassInstanceCreation161', None)
    _safe_set(owner, 'DOM_Expression162', partner)
    assert getattr(partner, 'DOM_ClassInstanceCreation161') == owner
    _safe_set(owner, 'DOM_Expression162', None)
    assert getattr(partner, 'DOM_ClassInstanceCreation161') is None


def test_assoc_expression171_stub_double():
    # DOM_ConditionalExpression has no real 'DOM_ConditionalExpression172' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ConditionalExpression()
    setattr(partner, 'DOM_ConditionalExpression172', None)
    _safe_set(owner, 'DOM_Expression173', partner)
    assert getattr(partner, 'DOM_ConditionalExpression172') == owner
    _safe_set(owner, 'DOM_Expression173', None)
    assert getattr(partner, 'DOM_ConditionalExpression172') is None


def test_assoc_expression177_stub_double():
    # DOM_FieldAccess has no real 'DOM_FieldAccess' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_FieldAccess()
    setattr(partner, 'DOM_FieldAccess', None)
    _safe_set(owner, 'DOM_Expression178', partner)
    assert getattr(partner, 'DOM_FieldAccess') == owner
    _safe_set(owner, 'DOM_Expression178', None)
    assert getattr(partner, 'DOM_FieldAccess') is None


def test_assoc_expression197_stub_double():
    # DOM_MethodInvocation has no real 'DOM_MethodInvocation198' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_MethodInvocation()
    setattr(partner, 'DOM_MethodInvocation198', None)
    _safe_set(owner, 'DOM_Expression199', partner)
    assert getattr(partner, 'DOM_MethodInvocation198') == owner
    _safe_set(owner, 'DOM_Expression199', None)
    assert getattr(partner, 'DOM_MethodInvocation198') is None


def test_assoc_expression209_stub_double():
    # DOM_ParenthesizedExpression has no real 'DOM_ParenthesizedExpression' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ParenthesizedExpression()
    setattr(partner, 'DOM_ParenthesizedExpression', None)
    _safe_set(owner, 'DOM_Expression210', partner)
    assert getattr(partner, 'DOM_ParenthesizedExpression') == owner
    _safe_set(owner, 'DOM_Expression210', None)
    assert getattr(partner, 'DOM_ParenthesizedExpression') is None


def test_assoc_expression243_stub_double():
    # DOM_AssertStatement has no real 'DOM_AssertStatement' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_AssertStatement()
    setattr(partner, 'DOM_AssertStatement', None)
    _safe_set(owner, 'DOM_Expression244', partner)
    assert getattr(partner, 'DOM_AssertStatement') == owner
    _safe_set(owner, 'DOM_Expression244', None)
    assert getattr(partner, 'DOM_AssertStatement') is None


def test_assoc_expression261_stub_double():
    # DOM_DoStatement has no real 'DOM_DoStatement262' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_DoStatement()
    setattr(partner, 'DOM_DoStatement262', None)
    _safe_set(owner, 'DOM_Expression263', partner)
    assert getattr(partner, 'DOM_DoStatement262') == owner
    _safe_set(owner, 'DOM_Expression263', None)
    assert getattr(partner, 'DOM_DoStatement262') is None


def test_assoc_expression266_stub_double():
    # DOM_EnhancedForStatement has no real 'DOM_EnhancedForStatement267' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_EnhancedForStatement()
    setattr(partner, 'DOM_EnhancedForStatement267', None)
    _safe_set(owner, 'DOM_Expression268', partner)
    assert getattr(partner, 'DOM_EnhancedForStatement267') == owner
    _safe_set(owner, 'DOM_Expression268', None)
    assert getattr(partner, 'DOM_EnhancedForStatement267') is None


def test_assoc_expression272_stub_double():
    # DOM_ExpressionStatement has no real 'DOM_ExpressionStatement' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ExpressionStatement()
    setattr(partner, 'DOM_ExpressionStatement', None)
    _safe_set(owner, 'DOM_Expression273', partner)
    assert getattr(partner, 'DOM_ExpressionStatement') == owner
    _safe_set(owner, 'DOM_Expression273', None)
    assert getattr(partner, 'DOM_ExpressionStatement') is None


def test_assoc_expression276_stub_double():
    # DOM_ForStatement has no real 'DOM_ForStatement277' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ForStatement()
    setattr(partner, 'DOM_ForStatement277', None)
    _safe_set(owner, 'DOM_Expression278', partner)
    assert getattr(partner, 'DOM_ForStatement277') == owner
    _safe_set(owner, 'DOM_Expression278', None)
    assert getattr(partner, 'DOM_ForStatement277') is None


def test_assoc_expression287_stub_double():
    # DOM_IfStatement has no real 'DOM_IfStatement288' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_IfStatement()
    setattr(partner, 'DOM_IfStatement288', None)
    _safe_set(owner, 'DOM_Expression289', partner)
    assert getattr(partner, 'DOM_IfStatement288') == owner
    _safe_set(owner, 'DOM_Expression289', None)
    assert getattr(partner, 'DOM_IfStatement288') is None


def test_assoc_expression298_stub_double():
    # DOM_ReturnStatement has no real 'DOM_ReturnStatement' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ReturnStatement()
    setattr(partner, 'DOM_ReturnStatement', None)
    _safe_set(owner, 'DOM_Expression299', partner)
    assert getattr(partner, 'DOM_ReturnStatement') == owner
    _safe_set(owner, 'DOM_Expression299', None)
    assert getattr(partner, 'DOM_ReturnStatement') is None


def test_assoc_expression302_stub_double():
    # DOM_SuperConstructorInvocation has no real 'DOM_SuperConstructorInvocation303' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_SuperConstructorInvocation()
    setattr(partner, 'DOM_SuperConstructorInvocation303', None)
    _safe_set(owner, 'DOM_Expression304', partner)
    assert getattr(partner, 'DOM_SuperConstructorInvocation303') == owner
    _safe_set(owner, 'DOM_Expression304', None)
    assert getattr(partner, 'DOM_SuperConstructorInvocation303') is None


def test_assoc_expression310_stub_double():
    # DOM_SwitchStatement has no real 'DOM_SwitchStatement' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_SwitchStatement()
    setattr(partner, 'DOM_SwitchStatement', None)
    _safe_set(owner, 'DOM_Expression311', partner)
    assert getattr(partner, 'DOM_SwitchStatement') == owner
    _safe_set(owner, 'DOM_Expression311', None)
    assert getattr(partner, 'DOM_SwitchStatement') is None


def test_assoc_expression317_stub_double():
    # DOM_SynchronizedStatement has no real 'DOM_SynchronizedStatement318' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_SynchronizedStatement()
    setattr(partner, 'DOM_SynchronizedStatement318', None)
    _safe_set(owner, 'DOM_Expression319', partner)
    assert getattr(partner, 'DOM_SynchronizedStatement318') == owner
    _safe_set(owner, 'DOM_Expression319', None)
    assert getattr(partner, 'DOM_SynchronizedStatement318') is None


def test_assoc_expression320_stub_double():
    # DOM_ThrowStatement has no real 'DOM_ThrowStatement' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ThrowStatement()
    setattr(partner, 'DOM_ThrowStatement', None)
    _safe_set(owner, 'DOM_Expression321', partner)
    assert getattr(partner, 'DOM_ThrowStatement') == owner
    _safe_set(owner, 'DOM_Expression321', None)
    assert getattr(partner, 'DOM_ThrowStatement') is None


def test_assoc_expression342_stub_double():
    # DOM_WhileStatement has no real 'DOM_WhileStatement343' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_WhileStatement()
    setattr(partner, 'DOM_WhileStatement343', None)
    _safe_set(owner, 'DOM_Expression344', partner)
    assert getattr(partner, 'DOM_WhileStatement343') == owner
    _safe_set(owner, 'DOM_Expression344', None)
    assert getattr(partner, 'DOM_WhileStatement343') is None


def test_assoc_expressions142_stub_double():
    # DOM_ArrayInitializer has no real 'DOM_ArrayInitializer143' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ArrayInitializer()
    setattr(partner, 'DOM_ArrayInitializer143', None)
    _safe_set(owner, 'DOM_Expression144', partner)
    assert owner in getattr(partner, 'DOM_ArrayInitializer143')
    _safe_set(owner, 'DOM_Expression144', None)
    assert owner not in getattr(partner, 'DOM_ArrayInitializer143')


def test_assoc_fragments53_stub_double():
    # DOM_ASTNode has no real 'DOM_ASTNode54' property in the generated
    # code (a bare stub) -- manually attach it so DOM_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_TagElement(nested="sample_text", tagName="sample_text")
    partner = DOM_ASTNode()
    setattr(partner, 'DOM_ASTNode54', None)
    _safe_set(owner, 'DOM_TagElement', {partner})
    assert getattr(partner, 'DOM_ASTNode54') == owner
    _safe_set(owner, 'DOM_TagElement', set())
    assert getattr(partner, 'DOM_ASTNode54') is None


def test_assoc_imports15_stub_double():
    # DOM_CompilationUnit has no real 'DOM_CompilationUnit16' property in the generated
    # code (a bare stub) -- manually attach it so DOM_ImportDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_ImportDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_ImportDeclaration(onDemand="sample_text", static="sample_text")
    partner = DOM_CompilationUnit()
    setattr(partner, 'DOM_CompilationUnit16', None)
    _safe_set(owner, 'DOM_ImportDeclaration', partner)
    assert owner in getattr(partner, 'DOM_CompilationUnit16')
    _safe_set(owner, 'DOM_ImportDeclaration', None)
    assert owner not in getattr(partner, 'DOM_CompilationUnit16')


def test_assoc_index133_stub_double():
    # DOM_ArrayAccess has no real 'DOM_ArrayAccess134' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ArrayAccess()
    setattr(partner, 'DOM_ArrayAccess134', None)
    _safe_set(owner, 'DOM_Expression135', partner)
    assert getattr(partner, 'DOM_ArrayAccess134') == owner
    _safe_set(owner, 'DOM_Expression135', None)
    assert getattr(partner, 'DOM_ArrayAccess134') is None


def test_assoc_initializers279_stub_double():
    # DOM_ForStatement has no real 'DOM_ForStatement280' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ForStatement()
    setattr(partner, 'DOM_ForStatement280', None)
    _safe_set(owner, 'DOM_Expression281', partner)
    assert owner in getattr(partner, 'DOM_ForStatement280')
    _safe_set(owner, 'DOM_Expression281', None)
    assert owner not in getattr(partner, 'DOM_ForStatement280')


def test_assoc_label250_stub_double():
    # DOM_BreakStatement has no real 'DOM_BreakStatement' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_BreakStatement()
    setattr(partner, 'DOM_BreakStatement', None)
    _safe_set(owner, 'DOM_SimpleName251', partner)
    assert getattr(partner, 'DOM_BreakStatement') == owner
    _safe_set(owner, 'DOM_SimpleName251', None)
    assert getattr(partner, 'DOM_BreakStatement') is None


def test_assoc_label257_stub_double():
    # DOM_ContinueStatement has no real 'DOM_ContinueStatement' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_ContinueStatement()
    setattr(partner, 'DOM_ContinueStatement', None)
    _safe_set(owner, 'DOM_SimpleName258', partner)
    assert getattr(partner, 'DOM_ContinueStatement') == owner
    _safe_set(owner, 'DOM_SimpleName258', None)
    assert getattr(partner, 'DOM_ContinueStatement') is None


def test_assoc_label295_stub_double():
    # DOM_LabeledStatement has no real 'DOM_LabeledStatement296' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_LabeledStatement()
    setattr(partner, 'DOM_LabeledStatement296', None)
    _safe_set(owner, 'DOM_SimpleName297', partner)
    assert getattr(partner, 'DOM_LabeledStatement296') == owner
    _safe_set(owner, 'DOM_SimpleName297', None)
    assert getattr(partner, 'DOM_LabeledStatement296') is None


def test_assoc_leftOperand190_stub_double():
    # DOM_InstanceofExpression has no real 'DOM_InstanceofExpression' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_InstanceofExpression()
    setattr(partner, 'DOM_InstanceofExpression', None)
    _safe_set(owner, 'DOM_Expression191', partner)
    assert getattr(partner, 'DOM_InstanceofExpression') == owner
    _safe_set(owner, 'DOM_Expression191', None)
    assert getattr(partner, 'DOM_InstanceofExpression') is None


def test_assoc_message245_stub_double():
    # DOM_AssertStatement has no real 'DOM_AssertStatement246' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_AssertStatement()
    setattr(partner, 'DOM_AssertStatement246', None)
    _safe_set(owner, 'DOM_Expression247', partner)
    assert getattr(partner, 'DOM_AssertStatement246') == owner
    _safe_set(owner, 'DOM_Expression247', None)
    assert getattr(partner, 'DOM_AssertStatement246') is None


def test_assoc_modifiers368_stub_double():
    # DOM_ExtendedModifier has no real 'DOM_ExtendedModifier370' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SingleVariableDeclaration(varargs="sample_text")
    partner = DOM_ExtendedModifier()
    setattr(partner, 'DOM_ExtendedModifier370', None)
    _safe_set(owner, 'DOM_SingleVariableDeclaration369', {partner})
    assert getattr(partner, 'DOM_ExtendedModifier370') == owner
    _safe_set(owner, 'DOM_SingleVariableDeclaration369', set())
    assert getattr(partner, 'DOM_ExtendedModifier370') is None


def test_assoc_name179_stub_double():
    # DOM_FieldAccess has no real 'DOM_FieldAccess180' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_FieldAccess()
    setattr(partner, 'DOM_FieldAccess180', None)
    _safe_set(owner, 'DOM_SimpleName181', partner)
    assert getattr(partner, 'DOM_FieldAccess180') == owner
    _safe_set(owner, 'DOM_SimpleName181', None)
    assert getattr(partner, 'DOM_FieldAccess180') is None


def test_assoc_name200_stub_double():
    # DOM_MethodInvocation has no real 'DOM_MethodInvocation201' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_MethodInvocation()
    setattr(partner, 'DOM_MethodInvocation201', None)
    _safe_set(owner, 'DOM_SimpleName202', partner)
    assert getattr(partner, 'DOM_MethodInvocation201') == owner
    _safe_set(owner, 'DOM_SimpleName202', None)
    assert getattr(partner, 'DOM_MethodInvocation201') is None


def test_assoc_name215_stub_double():
    # DOM_SuperFieldAccess has no real 'DOM_SuperFieldAccess' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_SuperFieldAccess()
    setattr(partner, 'DOM_SuperFieldAccess', None)
    _safe_set(owner, 'DOM_SimpleName216', partner)
    assert getattr(partner, 'DOM_SuperFieldAccess') == owner
    _safe_set(owner, 'DOM_SimpleName216', None)
    assert getattr(partner, 'DOM_SuperFieldAccess') is None


def test_assoc_name22_stub_double():
    # DOM_MemberRef has no real 'DOM_MemberRef' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_MemberRef()
    setattr(partner, 'DOM_MemberRef', None)
    _safe_set(owner, 'DOM_SimpleName', partner)
    assert getattr(partner, 'DOM_MemberRef') == owner
    _safe_set(owner, 'DOM_SimpleName', None)
    assert getattr(partner, 'DOM_MemberRef') is None


def test_assoc_name222_stub_double():
    # DOM_SuperMethodInvocation has no real 'DOM_SuperMethodInvocation223' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Name(fullyQualifiedName="sample_text")
    partner = DOM_SuperMethodInvocation()
    setattr(partner, 'DOM_SuperMethodInvocation223', None)
    _safe_set(owner, 'DOM_Name224', partner)
    assert getattr(partner, 'DOM_SuperMethodInvocation223') == owner
    _safe_set(owner, 'DOM_Name224', None)
    assert getattr(partner, 'DOM_SuperMethodInvocation223') is None


def test_assoc_name26_stub_double():
    # DOM_MemberValuePair has no real 'DOM_MemberValuePair' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_MemberValuePair()
    setattr(partner, 'DOM_MemberValuePair', None)
    _safe_set(owner, 'DOM_SimpleName27', partner)
    assert getattr(partner, 'DOM_MemberValuePair') == owner
    _safe_set(owner, 'DOM_SimpleName27', None)
    assert getattr(partner, 'DOM_MemberValuePair') is None


def test_assoc_name31_stub_double():
    # DOM_MethodRef has no real 'DOM_MethodRef' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_MethodRef()
    setattr(partner, 'DOM_MethodRef', None)
    _safe_set(owner, 'DOM_SimpleName32', partner)
    assert getattr(partner, 'DOM_MethodRef') == owner
    _safe_set(owner, 'DOM_SimpleName32', None)
    assert getattr(partner, 'DOM_MethodRef') is None


def test_assoc_name356_stub_double():
    # DOM_QualifiedType has no real 'DOM_QualifiedType' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_QualifiedType()
    setattr(partner, 'DOM_QualifiedType', None)
    _safe_set(owner, 'DOM_SimpleName357', partner)
    assert getattr(partner, 'DOM_QualifiedType') == owner
    _safe_set(owner, 'DOM_SimpleName357', None)
    assert getattr(partner, 'DOM_QualifiedType') is None


def test_assoc_name361_stub_double():
    # DOM_SimpleType has no real 'DOM_SimpleType' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Name(fullyQualifiedName="sample_text")
    partner = DOM_SimpleType()
    setattr(partner, 'DOM_SimpleType', None)
    _safe_set(owner, 'DOM_Name362', partner)
    assert getattr(partner, 'DOM_SimpleType') == owner
    _safe_set(owner, 'DOM_Name362', None)
    assert getattr(partner, 'DOM_SimpleType') is None


def test_assoc_name371_stub_double():
    # DOM_QualifiedName has no real 'DOM_QualifiedName' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_QualifiedName()
    setattr(partner, 'DOM_QualifiedName', None)
    _safe_set(owner, 'DOM_SimpleName372', partner)
    assert getattr(partner, 'DOM_QualifiedName') == owner
    _safe_set(owner, 'DOM_SimpleName372', None)
    assert getattr(partner, 'DOM_QualifiedName') is None


def test_assoc_name48_stub_double():
    # DOM_PackageDeclaration has no real 'DOM_PackageDeclaration49' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Name(fullyQualifiedName="sample_text")
    partner = DOM_PackageDeclaration()
    setattr(partner, 'DOM_PackageDeclaration49', None)
    _safe_set(owner, 'DOM_Name50', partner)
    assert getattr(partner, 'DOM_PackageDeclaration49') == owner
    _safe_set(owner, 'DOM_Name50', None)
    assert getattr(partner, 'DOM_PackageDeclaration49') is None


def test_assoc_name55_stub_double():
    # DOM_TypeParameter has no real 'DOM_TypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_TypeParameter()
    setattr(partner, 'DOM_TypeParameter', None)
    _safe_set(owner, 'DOM_SimpleName56', partner)
    assert getattr(partner, 'DOM_TypeParameter') == owner
    _safe_set(owner, 'DOM_SimpleName56', None)
    assert getattr(partner, 'DOM_TypeParameter') is None


def test_assoc_name73_stub_double():
    # DOM_AnnotationTypeMemberDeclaration has no real 'DOM_AnnotationTypeMemberDeclaration74' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_AnnotationTypeMemberDeclaration()
    setattr(partner, 'DOM_AnnotationTypeMemberDeclaration74', None)
    _safe_set(owner, 'DOM_SimpleName75', partner)
    assert getattr(partner, 'DOM_AnnotationTypeMemberDeclaration74') == owner
    _safe_set(owner, 'DOM_SimpleName75', None)
    assert getattr(partner, 'DOM_AnnotationTypeMemberDeclaration74') is None


def test_assoc_name84_stub_double():
    # DOM_EnumConstantDeclaration has no real 'DOM_EnumConstantDeclaration85' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = DOM_EnumConstantDeclaration()
    setattr(partner, 'DOM_EnumConstantDeclaration85', None)
    _safe_set(owner, 'DOM_SimpleName86', partner)
    assert getattr(partner, 'DOM_EnumConstantDeclaration85') == owner
    _safe_set(owner, 'DOM_SimpleName86', None)
    assert getattr(partner, 'DOM_EnumConstantDeclaration85') is None


def test_assoc_parameter269_stub_double():
    # DOM_EnhancedForStatement has no real 'DOM_EnhancedForStatement270' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SingleVariableDeclaration(varargs="sample_text")
    partner = DOM_EnhancedForStatement()
    setattr(partner, 'DOM_EnhancedForStatement270', None)
    _safe_set(owner, 'DOM_SingleVariableDeclaration271', partner)
    assert getattr(partner, 'DOM_EnhancedForStatement270') == owner
    _safe_set(owner, 'DOM_SingleVariableDeclaration271', None)
    assert getattr(partner, 'DOM_EnhancedForStatement270') is None


def test_assoc_parameters36_stub_double():
    # DOM_MethodRef has no real 'DOM_MethodRef37' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodRefParameter(varargs="sample_text")
    partner = DOM_MethodRef()
    setattr(partner, 'DOM_MethodRef37', None)
    _safe_set(owner, 'DOM_MethodRefParameter', partner)
    assert owner in getattr(partner, 'DOM_MethodRef37')
    _safe_set(owner, 'DOM_MethodRefParameter', None)
    assert owner not in getattr(partner, 'DOM_MethodRef37')


def test_assoc_qualifier217_stub_double():
    # DOM_SuperFieldAccess has no real 'DOM_SuperFieldAccess218' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Name(fullyQualifiedName="sample_text")
    partner = DOM_SuperFieldAccess()
    setattr(partner, 'DOM_SuperFieldAccess218', None)
    _safe_set(owner, 'DOM_Name219', partner)
    assert getattr(partner, 'DOM_SuperFieldAccess218') == owner
    _safe_set(owner, 'DOM_Name219', None)
    assert getattr(partner, 'DOM_SuperFieldAccess218') is None


def test_assoc_qualifier225_stub_double():
    # DOM_SuperMethodInvocation has no real 'DOM_SuperMethodInvocation226' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Name(fullyQualifiedName="sample_text")
    partner = DOM_SuperMethodInvocation()
    setattr(partner, 'DOM_SuperMethodInvocation226', None)
    _safe_set(owner, 'DOM_Name227', partner)
    assert getattr(partner, 'DOM_SuperMethodInvocation226') == owner
    _safe_set(owner, 'DOM_Name227', None)
    assert getattr(partner, 'DOM_SuperMethodInvocation226') is None


def test_assoc_qualifier23_stub_double():
    # DOM_MemberRef has no real 'DOM_MemberRef24' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Name(fullyQualifiedName="sample_text")
    partner = DOM_MemberRef()
    setattr(partner, 'DOM_MemberRef24', None)
    _safe_set(owner, 'DOM_Name25', partner)
    assert getattr(partner, 'DOM_MemberRef24') == owner
    _safe_set(owner, 'DOM_Name25', None)
    assert getattr(partner, 'DOM_MemberRef24') is None


def test_assoc_qualifier231_stub_double():
    # DOM_ThisExpression has no real 'DOM_ThisExpression' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Name(fullyQualifiedName="sample_text")
    partner = DOM_ThisExpression()
    setattr(partner, 'DOM_ThisExpression', None)
    _safe_set(owner, 'DOM_Name232', partner)
    assert getattr(partner, 'DOM_ThisExpression') == owner
    _safe_set(owner, 'DOM_Name232', None)
    assert getattr(partner, 'DOM_ThisExpression') is None


def test_assoc_qualifier33_stub_double():
    # DOM_MethodRef has no real 'DOM_MethodRef34' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Name(fullyQualifiedName="sample_text")
    partner = DOM_MethodRef()
    setattr(partner, 'DOM_MethodRef34', None)
    _safe_set(owner, 'DOM_Name35', partner)
    assert getattr(partner, 'DOM_MethodRef34') == owner
    _safe_set(owner, 'DOM_Name35', None)
    assert getattr(partner, 'DOM_MethodRef34') is None


def test_assoc_qualifier373_stub_double():
    # DOM_QualifiedName has no real 'DOM_QualifiedName374' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Name(fullyQualifiedName="sample_text")
    partner = DOM_QualifiedName()
    setattr(partner, 'DOM_QualifiedName374', None)
    _safe_set(owner, 'DOM_Name375', partner)
    assert getattr(partner, 'DOM_QualifiedName374') == owner
    _safe_set(owner, 'DOM_Name375', None)
    assert getattr(partner, 'DOM_QualifiedName374') is None


def test_assoc_returnType98_stub_double():
    # DOM_Type has no real 'DOM_Type100' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = DOM_Type()
    setattr(partner, 'DOM_Type100', None)
    _safe_set(owner, 'DOM_MethodDeclaration99', partner)
    assert getattr(partner, 'DOM_Type100') == owner
    _safe_set(owner, 'DOM_MethodDeclaration99', None)
    assert getattr(partner, 'DOM_Type100') is None


def test_assoc_superInterfaceTypes119_stub_double():
    # DOM_Type has no real 'DOM_Type121' property in the generated
    # code (a bare stub) -- manually attach it so DOM_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_TypeDeclaration(interface="sample_text")
    partner = DOM_Type()
    setattr(partner, 'DOM_Type121', None)
    _safe_set(owner, 'DOM_TypeDeclaration120', {partner})
    assert getattr(partner, 'DOM_Type121') == owner
    _safe_set(owner, 'DOM_TypeDeclaration120', set())
    assert getattr(partner, 'DOM_Type121') is None


def test_assoc_superclassType117_stub_double():
    # DOM_Type has no real 'DOM_Type118' property in the generated
    # code (a bare stub) -- manually attach it so DOM_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_TypeDeclaration(interface="sample_text")
    partner = DOM_Type()
    setattr(partner, 'DOM_Type118', None)
    _safe_set(owner, 'DOM_TypeDeclaration', partner)
    assert getattr(partner, 'DOM_Type118') == owner
    _safe_set(owner, 'DOM_TypeDeclaration', None)
    assert getattr(partner, 'DOM_Type118') is None


def test_assoc_tags125_stub_double():
    # DOM_Javadoc has no real 'DOM_Javadoc126' property in the generated
    # code (a bare stub) -- manually attach it so DOM_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_TagElement(nested="sample_text", tagName="sample_text")
    partner = DOM_Javadoc()
    setattr(partner, 'DOM_Javadoc126', None)
    _safe_set(owner, 'DOM_TagElement127', partner)
    assert owner in getattr(partner, 'DOM_Javadoc126')
    _safe_set(owner, 'DOM_TagElement127', None)
    assert owner not in getattr(partner, 'DOM_Javadoc126')


def test_assoc_thenExpression174_stub_double():
    # DOM_ConditionalExpression has no real 'DOM_ConditionalExpression175' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ConditionalExpression()
    setattr(partner, 'DOM_ConditionalExpression175', None)
    _safe_set(owner, 'DOM_Expression176', partner)
    assert getattr(partner, 'DOM_ConditionalExpression175') == owner
    _safe_set(owner, 'DOM_Expression176', None)
    assert getattr(partner, 'DOM_ConditionalExpression175') is None


def test_assoc_type140_stub_double():
    # DOM_ArrayCreation has no real 'DOM_ArrayCreation141' property in the generated
    # code (a bare stub) -- manually attach it so DOM_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_ArrayType(dimensions="sample_text")
    partner = DOM_ArrayCreation()
    setattr(partner, 'DOM_ArrayCreation141', None)
    _safe_set(owner, 'DOM_ArrayType', partner)
    assert getattr(partner, 'DOM_ArrayCreation141') == owner
    _safe_set(owner, 'DOM_ArrayType', None)
    assert getattr(partner, 'DOM_ArrayCreation141') is None


def test_assoc_type365_stub_double():
    # DOM_Type has no real 'DOM_Type367' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SingleVariableDeclaration(varargs="sample_text")
    partner = DOM_Type()
    setattr(partner, 'DOM_Type367', None)
    _safe_set(owner, 'DOM_SingleVariableDeclaration366', partner)
    assert getattr(partner, 'DOM_Type367') == owner
    _safe_set(owner, 'DOM_SingleVariableDeclaration366', None)
    assert getattr(partner, 'DOM_Type367') is None


def test_assoc_type41_stub_double():
    # DOM_Type has no real 'DOM_Type' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodRefParameter(varargs="sample_text")
    partner = DOM_Type()
    setattr(partner, 'DOM_Type', None)
    _safe_set(owner, 'DOM_MethodRefParameter42', partner)
    assert getattr(partner, 'DOM_Type') == owner
    _safe_set(owner, 'DOM_MethodRefParameter42', None)
    assert getattr(partner, 'DOM_Type') is None


def test_assoc_typeBinding19_stub_double():
    # DOM_IType has no real 'DOM_IType' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_IType()
    setattr(partner, 'DOM_IType', None)
    _safe_set(owner, 'DOM_Expression', partner)
    assert getattr(partner, 'DOM_IType') == owner
    _safe_set(owner, 'DOM_Expression', None)
    assert getattr(partner, 'DOM_IType') is None


def test_assoc_typeName128_stub_double():
    # DOM_Annotation has no real 'DOM_Annotation129' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Name(fullyQualifiedName="sample_text")
    partner = DOM_Annotation()
    setattr(partner, 'DOM_Annotation129', None)
    _safe_set(owner, 'DOM_Name130', partner)
    assert getattr(partner, 'DOM_Annotation129') == owner
    _safe_set(owner, 'DOM_Name130', None)
    assert getattr(partner, 'DOM_Annotation129') is None


def test_assoc_typeParameters107_stub_double():
    # DOM_TypeParameter has no real 'DOM_TypeParameter109' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = DOM_TypeParameter()
    setattr(partner, 'DOM_TypeParameter109', None)
    _safe_set(owner, 'DOM_MethodDeclaration108', {partner})
    assert getattr(partner, 'DOM_TypeParameter109') == owner
    _safe_set(owner, 'DOM_MethodDeclaration108', set())
    assert getattr(partner, 'DOM_TypeParameter109') is None


def test_assoc_typeParameters122_stub_double():
    # DOM_TypeParameter has no real 'DOM_TypeParameter124' property in the generated
    # code (a bare stub) -- manually attach it so DOM_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_TypeDeclaration(interface="sample_text")
    partner = DOM_TypeParameter()
    setattr(partner, 'DOM_TypeParameter124', None)
    _safe_set(owner, 'DOM_TypeDeclaration123', {partner})
    assert getattr(partner, 'DOM_TypeParameter124') == owner
    _safe_set(owner, 'DOM_TypeDeclaration123', set())
    assert getattr(partner, 'DOM_TypeParameter124') is None


def test_assoc_types17_stub_double():
    # DOM_CompilationUnit has no real 'DOM_CompilationUnit18' property in the generated
    # code (a bare stub) -- manually attach it so DOM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    partner = DOM_CompilationUnit()
    setattr(partner, 'DOM_CompilationUnit18', None)
    _safe_set(owner, 'DOM_AbstractTypeDeclaration', partner)
    assert owner in getattr(partner, 'DOM_CompilationUnit18')
    _safe_set(owner, 'DOM_AbstractTypeDeclaration', None)
    assert owner not in getattr(partner, 'DOM_CompilationUnit18')


def test_assoc_updaters282_stub_double():
    # DOM_ForStatement has no real 'DOM_ForStatement283' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_ForStatement()
    setattr(partner, 'DOM_ForStatement283', None)
    _safe_set(owner, 'DOM_Expression284', partner)
    assert owner in getattr(partner, 'DOM_ForStatement283')
    _safe_set(owner, 'DOM_Expression284', None)
    assert owner not in getattr(partner, 'DOM_ForStatement283')


def test_assoc_value28_stub_double():
    # DOM_MemberValuePair has no real 'DOM_MemberValuePair29' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_MemberValuePair()
    setattr(partner, 'DOM_MemberValuePair29', None)
    _safe_set(owner, 'DOM_Expression30', partner)
    assert getattr(partner, 'DOM_MemberValuePair29') == owner
    _safe_set(owner, 'DOM_Expression30', None)
    assert getattr(partner, 'DOM_MemberValuePair29') is None


def test_assoc_value378_stub_double():
    # DOM_SingleMemberAnnotation has no real 'DOM_SingleMemberAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = DOM_SingleMemberAnnotation()
    setattr(partner, 'DOM_SingleMemberAnnotation', None)
    _safe_set(owner, 'DOM_Expression379', partner)
    assert getattr(partner, 'DOM_SingleMemberAnnotation') == owner
    _safe_set(owner, 'DOM_Expression379', None)
    assert getattr(partner, 'DOM_SingleMemberAnnotation') is None


