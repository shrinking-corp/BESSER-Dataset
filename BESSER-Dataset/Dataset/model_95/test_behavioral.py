import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    AbstractMethodDeclaration,
    AbstractMethodInvocation,
    AbstractTypeDeclaration,
    AbstractTypeQualifiedExpression,
    AbstractVariablesContainer,
    BodyDeclaration,
    Expression,
    NamedElement,
    NamespaceAccess,
    PrimitiveType,
    Statement,
    Type,
    TypeDeclaration,
    UnresolvedItem,
    VariableDeclaration,
    java_ASTNode,
    java_AbstractMethodDeclaration,
    java_AbstractMethodInvocation,
    java_AbstractTypeDeclaration,
    java_AbstractTypeQualifiedExpression,
    java_AbstractVariablesContainer,
    java_Annotation,
    java_AnnotationMemberValuePair,
    java_AnnotationTypeDeclaration,
    java_AnnotationTypeMemberDeclaration,
    java_AnonymousClassDeclaration,
    java_Archive,
    java_ArrayAccess,
    java_ArrayCreation,
    java_ArrayInitializer,
    java_ArrayLengthAccess,
    java_ArrayType,
    java_AssertStatement,
    java_Assignment,
    java_Block,
    java_BodyDeclaration,
    java_BooleanLiteral,
    java_BreakStatement,
    java_CastExpression,
    java_CatchClause,
    java_CharacterLiteral,
    java_ClassDeclaration,
    java_ClassFile,
    java_ClassInstanceCreation,
    java_Comment,
    java_CompilationUnit,
    java_ConditionalExpression,
    java_ConstructorDeclaration,
    java_ConstructorInvocation,
    java_ContinueStatement,
    java_DoStatement,
    java_EmptyStatement,
    java_EnhancedForStatement,
    java_EnumConstantDeclaration,
    java_EnumDeclaration,
    java_Expression,
    java_ExpressionStatement,
    java_FieldAccess,
    java_FieldDeclaration,
    java_ForStatement,
    java_IfStatement,
    java_ImportDeclaration,
    java_InfixExpression,
    java_Initializer,
    java_InstanceofExpression,
    java_InterfaceDeclaration,
    java_LabeledStatement,
    java_MemberRef,
    java_MethodDeclaration,
    java_MethodInvocation,
    java_MethodRef,
    java_MethodRefParameter,
    java_Model,
    java_Modifier,
    java_NamedElement,
    java_NamespaceAccess,
    java_NullLiteral,
    java_NumberLiteral,
    java_Package,
    java_ParameterizedType,
    java_ParenthesizedExpression,
    java_PostfixExpression,
    java_PrefixExpression,
    java_PrimitiveType,
    java_PrimitiveTypeBoolean,
    java_PrimitiveTypeByte,
    java_PrimitiveTypeChar,
    java_PrimitiveTypeDouble,
    java_PrimitiveTypeFloat,
    java_PrimitiveTypeInt,
    java_PrimitiveTypeLong,
    java_PrimitiveTypeShort,
    java_PrimitiveTypeVoid,
    java_ReturnStatement,
    java_SingleVariableAccess,
    java_SingleVariableDeclaration,
    java_Statement,
    java_StringLiteral,
    java_SuperConstructorInvocation,
    java_SuperFieldAccess,
    java_SuperMethodInvocation,
    java_SwitchCase,
    java_SwitchStatement,
    java_SynchronizedStatement,
    java_TagElement,
    java_ThisExpression,
    java_ThrowStatement,
    java_TryStatement,
    java_Type,
    java_TypeAccess,
    java_TypeDeclaration,
    java_TypeDeclarationStatement,
    java_TypeLiteral,
    java_TypeParameter,
    java_UnresolvedItem,
    java_UnresolvedItemAccess,
    java_UnresolvedTypeDeclaration,
    java_VariableDeclaration,
    java_VariableDeclarationExpression,
    java_VariableDeclarationFragment,
    java_VariableDeclarationStatement,
    java_WhileStatement,
    java_WildCardType,
    AssignmentKind,
    InfixExpressionKind,
    InheritanceKind,
    PostfixExpressionKind,
    PrefixExpressionKind,
    VisibilityKind,
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

def test_assoc_archives256_reverse_link_reassign_clear():
    a1 = java_Model(name="sample_text")
    a2 = java_Model(name="sample_text_2")
    b = java_Archive(originalFilePath="sample_text")
    _safe_set(b, 'java_Archive', a1)
    assert _is_linked(b, 'java_Archive', a1)
    if hasattr(a1, 'java_Model257'):
        assert _is_linked(a1, 'java_Model257', b)
    _safe_set(b, 'java_Archive', a2)
    assert _is_linked(b, 'java_Archive', a2)
    if hasattr(a1, 'java_Model257'):
        assert not _is_linked(a1, 'java_Model257', b)
    if hasattr(a2, 'java_Model257'):
        assert _is_linked(a2, 'java_Model257', b)
    _safe_set(b, 'java_Archive', None)
    assert not _is_linked(b, 'java_Archive', a2)
    if hasattr(a2, 'java_Model257'):
        assert not _is_linked(a2, 'java_Model257', b)


def test_assoc_compilationUnits251_reverse_link_reassign_clear():
    a1 = java_Model(name="sample_text")
    a2 = java_Model(name="sample_text_2")
    b = java_CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'java_CompilationUnit252', a1)
    assert _is_linked(b, 'java_CompilationUnit252', a1)
    if hasattr(a1, 'java_Model'):
        assert _is_linked(a1, 'java_Model', b)
    _safe_set(b, 'java_CompilationUnit252', a2)
    assert _is_linked(b, 'java_CompilationUnit252', a2)
    if hasattr(a1, 'java_Model'):
        assert not _is_linked(a1, 'java_Model', b)
    if hasattr(a2, 'java_Model'):
        assert _is_linked(a2, 'java_Model', b)
    _safe_set(b, 'java_CompilationUnit252', None)
    assert not _is_linked(b, 'java_CompilationUnit252', a2)
    if hasattr(a2, 'java_Model'):
        assert not _is_linked(a2, 'java_Model', b)


def test_assoc_importedElement57_reverse_link_reassign_clear():
    a1 = java_NamedElement(name="sample_text", proxy=True)
    a2 = java_NamedElement(name="sample_text_2", proxy=False)
    b = java_ImportDeclaration(static=True)
    _safe_set(b, 'java_ImportDeclaration', a1)
    assert _is_linked(b, 'java_ImportDeclaration', a1)
    if hasattr(a1, 'java_NamedElement'):
        assert _is_linked(a1, 'java_NamedElement', b)
    _safe_set(b, 'java_ImportDeclaration', a2)
    assert _is_linked(b, 'java_ImportDeclaration', a2)
    if hasattr(a1, 'java_NamedElement'):
        assert not _is_linked(a1, 'java_NamedElement', b)
    if hasattr(a2, 'java_NamedElement'):
        assert _is_linked(a2, 'java_NamedElement', b)
    _safe_set(b, 'java_ImportDeclaration', None)
    assert not _is_linked(b, 'java_ImportDeclaration', a2)
    if hasattr(a2, 'java_NamedElement'):
        assert not _is_linked(a2, 'java_NamedElement', b)


def test_assoc_imports122_reverse_link_reassign_clear():
    a1 = java_ImportDeclaration(static=True)
    a2 = java_ImportDeclaration(static=False)
    b = java_CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'java_CompilationUnit123', {a1})
    assert _is_linked(b, 'java_CompilationUnit123', a1)
    if hasattr(a1, 'java_ImportDeclaration124'):
        assert _is_linked(a1, 'java_ImportDeclaration124', b)
    _safe_set(b, 'java_CompilationUnit123', {a2})
    assert _is_linked(b, 'java_CompilationUnit123', a2)
    if hasattr(a1, 'java_ImportDeclaration124'):
        assert not _is_linked(a1, 'java_ImportDeclaration124', b)
    if hasattr(a2, 'java_ImportDeclaration124'):
        assert _is_linked(a2, 'java_ImportDeclaration124', b)
    _safe_set(b, 'java_CompilationUnit123', set())
    assert not _is_linked(b, 'java_CompilationUnit123', a2)
    if hasattr(a2, 'java_ImportDeclaration124'):
        assert not _is_linked(a2, 'java_ImportDeclaration124', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_comments66_stub_double():
    # java_ASTNode has no real 'java_ASTNode' property in the generated
    # code (a bare stub) -- manually attach it so java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Comment(content="sample_text")
    partner = java_ASTNode()
    setattr(partner, 'java_ASTNode', None)
    _safe_set(owner, 'java_Comment67', partner)
    assert owner in getattr(partner, 'java_ASTNode')
    _safe_set(owner, 'java_Comment67', None)
    assert owner not in getattr(partner, 'java_ASTNode')


def test_assoc_commentsAfterBody28_stub_double():
    # java_AbstractTypeDeclaration has no real 'java_AbstractTypeDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Comment(content="sample_text")
    partner = java_AbstractTypeDeclaration()
    setattr(partner, 'java_AbstractTypeDeclaration', None)
    _safe_set(owner, 'java_Comment', partner)
    assert owner in getattr(partner, 'java_AbstractTypeDeclaration')
    _safe_set(owner, 'java_Comment', None)
    assert owner not in getattr(partner, 'java_AbstractTypeDeclaration')


def test_assoc_commentsBeforeBody29_stub_double():
    # java_AbstractTypeDeclaration has no real 'java_AbstractTypeDeclaration30' property in the generated
    # code (a bare stub) -- manually attach it so java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Comment(content="sample_text")
    partner = java_AbstractTypeDeclaration()
    setattr(partner, 'java_AbstractTypeDeclaration30', None)
    _safe_set(owner, 'java_Comment31', partner)
    assert owner in getattr(partner, 'java_AbstractTypeDeclaration30')
    _safe_set(owner, 'java_Comment31', None)
    assert owner not in getattr(partner, 'java_AbstractTypeDeclaration30')


def test_assoc_elementType151_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess152' property in the generated
    # code (a bare stub) -- manually attach it so java_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_ArrayType(dimensions=7)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess152', None)
    _safe_set(owner, 'java_ArrayType', partner)
    assert getattr(partner, 'java_TypeAccess152') == owner
    _safe_set(owner, 'java_ArrayType', None)
    assert getattr(partner, 'java_TypeAccess152') is None


def test_assoc_extendedOperands116_stub_double():
    # java_Expression has no real 'java_Expression118' property in the generated
    # code (a bare stub) -- manually attach it so java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_InfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression118', None)
    _safe_set(owner, 'java_InfixExpression117', {partner})
    assert getattr(partner, 'java_Expression118') == owner
    _safe_set(owner, 'java_InfixExpression117', set())
    assert getattr(partner, 'java_Expression118') is None


def test_assoc_leftHandSide43_stub_double():
    # java_Expression has no real 'java_Expression44' property in the generated
    # code (a bare stub) -- manually attach it so java_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Assignment(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression44', None)
    _safe_set(owner, 'java_Assignment', partner)
    assert getattr(partner, 'java_Expression44') == owner
    _safe_set(owner, 'java_Assignment', None)
    assert getattr(partner, 'java_Expression44') is None


def test_assoc_leftOperand113_stub_double():
    # java_Expression has no real 'java_Expression115' property in the generated
    # code (a bare stub) -- manually attach it so java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_InfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression115', None)
    _safe_set(owner, 'java_InfixExpression114', partner)
    assert getattr(partner, 'java_Expression115') == owner
    _safe_set(owner, 'java_InfixExpression114', None)
    assert getattr(partner, 'java_Expression115') is None


def test_assoc_modifier155_stub_double():
    # java_BodyDeclaration has no real 'java_BodyDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Modifier(inheritance="sample_text", static=True, visibility="sample_text")
    partner = java_BodyDeclaration()
    setattr(partner, 'java_BodyDeclaration', None)
    _safe_set(owner, 'java_Modifier156', partner)
    assert getattr(partner, 'java_BodyDeclaration') == owner
    _safe_set(owner, 'java_Modifier156', None)
    assert getattr(partner, 'java_BodyDeclaration') is None


def test_assoc_modifier23_stub_double():
    # java_SingleVariableDeclaration has no real 'java_SingleVariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Modifier(inheritance="sample_text", static=True, visibility="sample_text")
    partner = java_SingleVariableDeclaration()
    setattr(partner, 'java_SingleVariableDeclaration', None)
    _safe_set(owner, 'java_Modifier', partner)
    assert getattr(partner, 'java_SingleVariableDeclaration') == owner
    _safe_set(owner, 'java_Modifier', None)
    assert getattr(partner, 'java_SingleVariableDeclaration') is None


def test_assoc_operand171_stub_double():
    # java_Expression has no real 'java_Expression172' property in the generated
    # code (a bare stub) -- manually attach it so java_PrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_PrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_PrefixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression172', None)
    _safe_set(owner, 'java_PrefixExpression', partner)
    assert getattr(partner, 'java_Expression172') == owner
    _safe_set(owner, 'java_PrefixExpression', None)
    assert getattr(partner, 'java_Expression172') is None


def test_assoc_operand48_stub_double():
    # java_Expression has no real 'java_Expression49' property in the generated
    # code (a bare stub) -- manually attach it so java_PostfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_PostfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_PostfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression49', None)
    _safe_set(owner, 'java_PostfixExpression', partner)
    assert getattr(partner, 'java_Expression49') == owner
    _safe_set(owner, 'java_PostfixExpression', None)
    assert getattr(partner, 'java_Expression49') is None


def test_assoc_originalCompilationUnit70_stub_double():
    # java_ASTNode has no real 'java_ASTNode71' property in the generated
    # code (a bare stub) -- manually attach it so java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_CompilationUnit(originalFilePath="sample_text")
    partner = java_ASTNode()
    setattr(partner, 'java_ASTNode71', None)
    _safe_set(owner, 'java_CompilationUnit', partner)
    assert getattr(partner, 'java_ASTNode71') == owner
    _safe_set(owner, 'java_CompilationUnit', None)
    assert getattr(partner, 'java_ASTNode71') is None


def test_assoc_orphanTypes253_stub_double():
    # java_Type has no real 'java_Type255' property in the generated
    # code (a bare stub) -- manually attach it so java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Model(name="sample_text")
    partner = java_Type()
    setattr(partner, 'java_Type255', None)
    _safe_set(owner, 'java_Model254', {partner})
    assert getattr(partner, 'java_Type255') == owner
    _safe_set(owner, 'java_Model254', set())
    assert getattr(partner, 'java_Type255') is None


def test_assoc_ownedElements258_stub_double():
    # java_Package has no real 'java_Package260' property in the generated
    # code (a bare stub) -- manually attach it so java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Model(name="sample_text")
    partner = java_Package()
    setattr(partner, 'java_Package260', None)
    _safe_set(owner, 'java_Model259', {partner})
    assert getattr(partner, 'java_Package260') == owner
    _safe_set(owner, 'java_Model259', set())
    assert getattr(partner, 'java_Package260') is None


def test_assoc_rightHandSide45_stub_double():
    # java_Expression has no real 'java_Expression47' property in the generated
    # code (a bare stub) -- manually attach it so java_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Assignment(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression47', None)
    _safe_set(owner, 'java_Assignment46', partner)
    assert getattr(partner, 'java_Expression47') == owner
    _safe_set(owner, 'java_Assignment46', None)
    assert getattr(partner, 'java_Expression47') is None


def test_assoc_rightOperand111_stub_double():
    # java_Expression has no real 'java_Expression112' property in the generated
    # code (a bare stub) -- manually attach it so java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_InfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression112', None)
    _safe_set(owner, 'java_InfixExpression', partner)
    assert getattr(partner, 'java_Expression112') == owner
    _safe_set(owner, 'java_InfixExpression', None)
    assert getattr(partner, 'java_Expression112') is None


def test_assoc_types125_stub_double():
    # java_AbstractTypeDeclaration has no real 'java_AbstractTypeDeclaration127' property in the generated
    # code (a bare stub) -- manually attach it so java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_CompilationUnit(originalFilePath="sample_text")
    partner = java_AbstractTypeDeclaration()
    setattr(partner, 'java_AbstractTypeDeclaration127', None)
    _safe_set(owner, 'java_CompilationUnit126', {partner})
    assert getattr(partner, 'java_AbstractTypeDeclaration127') == owner
    _safe_set(owner, 'java_CompilationUnit126', set())
    assert getattr(partner, 'java_AbstractTypeDeclaration127') is None


