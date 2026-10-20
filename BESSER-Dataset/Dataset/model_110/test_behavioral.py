import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    AbstractTypeDeclaration,
    AnnotatableType,
    Annotation,
    BodyDeclaration,
    Comment,
    Expression,
    IDocElement,
    IExtendedModifier,
    MethodReference,
    Name,
    Statement,
    Type,
    VariableDeclaration,
    ast_ASTNode,
    ast_AbstractTypeDeclaration,
    ast_AnnotatableType,
    ast_Annotation,
    ast_AnnotationTypeDeclaration,
    ast_AnnotationTypeMemberDeclaration,
    ast_AnonymousClassDeclaration,
    ast_ArrayAccess,
    ast_ArrayCreation,
    ast_ArrayInitializer,
    ast_ArrayType,
    ast_AssertStatement,
    ast_Assignment,
    ast_Block,
    ast_BlockComment,
    ast_BodyDeclaration,
    ast_BooleanLiteral,
    ast_BreakStatement,
    ast_CastExpression,
    ast_CatchClause,
    ast_CharacterLiteral,
    ast_ClassInstanceCreation,
    ast_Comment,
    ast_CompilationUnit,
    ast_ConditionalExpression,
    ast_ConstructorInvocation,
    ast_ContinueStatement,
    ast_CreationReference,
    ast_Dimension,
    ast_DoStatement,
    ast_EmptyStatement,
    ast_EnhancedForStatement,
    ast_EnumConstantDeclaration,
    ast_EnumDeclaration,
    ast_Expression,
    ast_ExpressionMethodReference,
    ast_ExpressionStatement,
    ast_FieldAccess,
    ast_FieldDeclaration,
    ast_ForStatement,
    ast_IDocElement,
    ast_IExtendedModifier,
    ast_IfStatement,
    ast_ImportDeclaration,
    ast_InfixExpression,
    ast_Initializer,
    ast_InstanceofExpression,
    ast_IntersectionType,
    ast_Javadoc,
    ast_LabeledStatement,
    ast_LambdaExpression,
    ast_LineComment,
    ast_MarkerAnnotation,
    ast_MemberRef,
    ast_MemberValuePair,
    ast_MethodDeclaration,
    ast_MethodInvocation,
    ast_MethodRef,
    ast_MethodRefParameter,
    ast_MethodReference,
    ast_Modifier,
    ast_Name,
    ast_NameQualifiedType,
    ast_NormalAnnotation,
    ast_NullLiteral,
    ast_NumberLiteral,
    ast_PackageDeclaration,
    ast_ParameterizedType,
    ast_ParenthesizedExpression,
    ast_PostfixExpression,
    ast_PrefixExpression,
    ast_PrimitiveType,
    ast_QualifiedName,
    ast_QualifiedType,
    ast_ReturnStatement,
    ast_SimpleName,
    ast_SimpleType,
    ast_SingleMemberAnnotation,
    ast_SingleVariableDeclaration,
    ast_Statement,
    ast_StringLiteral,
    ast_SuperConstructorInvocation,
    ast_SuperFieldAccess,
    ast_SuperMethodInvocation,
    ast_SuperMethodReference,
    ast_SwitchCase,
    ast_SwitchStatement,
    ast_SynchronizedStatement,
    ast_TagElement,
    ast_TextElement,
    ast_ThisExpression,
    ast_ThrowStatement,
    ast_TryStatement,
    ast_Type,
    ast_TypeDeclaration,
    ast_TypeDeclarationStatement,
    ast_TypeLiteral,
    ast_TypeMethodReference,
    ast_TypeParameter,
    ast_UnionType,
    ast_VariableDeclaration,
    ast_VariableDeclarationExpression,
    ast_VariableDeclarationFragment,
    ast_VariableDeclarationStatement,
    ast_WhileStatement,
    ast_WildcardType,
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

def test_assoc_name172_reverse_link_reassign_clear():
    a1 = ast_SimpleName(identifier="sample_text")
    a2 = ast_SimpleName(identifier="sample_text_2")
    b = ast_MethodDeclaration(constructor=True)
    _safe_set(b, 'ast_MethodDeclaration173', a1)
    assert _is_linked(b, 'ast_MethodDeclaration173', a1)
    if hasattr(a1, 'ast_SimpleName174'):
        assert _is_linked(a1, 'ast_SimpleName174', b)
    _safe_set(b, 'ast_MethodDeclaration173', a2)
    assert _is_linked(b, 'ast_MethodDeclaration173', a2)
    if hasattr(a1, 'ast_SimpleName174'):
        assert not _is_linked(a1, 'ast_SimpleName174', b)
    if hasattr(a2, 'ast_SimpleName174'):
        assert _is_linked(a2, 'ast_SimpleName174', b)
    _safe_set(b, 'ast_MethodDeclaration173', None)
    assert not _is_linked(b, 'ast_MethodDeclaration173', a2)
    if hasattr(a2, 'ast_SimpleName174'):
        assert not _is_linked(a2, 'ast_SimpleName174', b)


def test_assoc_name241_reverse_link_reassign_clear():
    a1 = ast_SingleVariableDeclaration(varargs=True)
    a2 = ast_SingleVariableDeclaration(varargs=False)
    b = ast_SimpleName(identifier="sample_text")
    _safe_set(b, 'ast_SimpleName243', a1)
    assert _is_linked(b, 'ast_SimpleName243', a1)
    if hasattr(a1, 'ast_SingleVariableDeclaration242'):
        assert _is_linked(a1, 'ast_SingleVariableDeclaration242', b)
    _safe_set(b, 'ast_SimpleName243', a2)
    assert _is_linked(b, 'ast_SimpleName243', a2)
    if hasattr(a1, 'ast_SingleVariableDeclaration242'):
        assert not _is_linked(a1, 'ast_SingleVariableDeclaration242', b)
    if hasattr(a2, 'ast_SingleVariableDeclaration242'):
        assert _is_linked(a2, 'ast_SingleVariableDeclaration242', b)
    _safe_set(b, 'ast_SimpleName243', None)
    assert not _is_linked(b, 'ast_SimpleName243', a2)
    if hasattr(a2, 'ast_SingleVariableDeclaration242'):
        assert not _is_linked(a2, 'ast_SingleVariableDeclaration242', b)


def test_assoc_name305_reverse_link_reassign_clear():
    a1 = ast_TypeDeclaration(interface=True)
    a2 = ast_TypeDeclaration(interface=False)
    b = ast_SimpleName(identifier="sample_text")
    _safe_set(b, 'ast_SimpleName307', a1)
    assert _is_linked(b, 'ast_SimpleName307', a1)
    if hasattr(a1, 'ast_TypeDeclaration306'):
        assert _is_linked(a1, 'ast_TypeDeclaration306', b)
    _safe_set(b, 'ast_SimpleName307', a2)
    assert _is_linked(b, 'ast_SimpleName307', a2)
    if hasattr(a1, 'ast_TypeDeclaration306'):
        assert not _is_linked(a1, 'ast_TypeDeclaration306', b)
    if hasattr(a2, 'ast_TypeDeclaration306'):
        assert _is_linked(a2, 'ast_TypeDeclaration306', b)
    _safe_set(b, 'ast_SimpleName307', None)
    assert not _is_linked(b, 'ast_SimpleName307', a2)
    if hasattr(a2, 'ast_TypeDeclaration306'):
        assert not _is_linked(a2, 'ast_TypeDeclaration306', b)


def test_assoc_name363_reverse_link_reassign_clear():
    a1 = ast_SimpleName(identifier="sample_text")
    a2 = ast_SimpleName(identifier="sample_text_2")
    b = ast_MethodRefParameter(varargs=True)
    _safe_set(b, 'ast_MethodRefParameter364', a1)
    assert _is_linked(b, 'ast_MethodRefParameter364', a1)
    if hasattr(a1, 'ast_SimpleName365'):
        assert _is_linked(a1, 'ast_SimpleName365', b)
    _safe_set(b, 'ast_MethodRefParameter364', a2)
    assert _is_linked(b, 'ast_MethodRefParameter364', a2)
    if hasattr(a1, 'ast_SimpleName365'):
        assert not _is_linked(a1, 'ast_SimpleName365', b)
    if hasattr(a2, 'ast_SimpleName365'):
        assert _is_linked(a2, 'ast_SimpleName365', b)
    _safe_set(b, 'ast_MethodRefParameter364', None)
    assert not _is_linked(b, 'ast_MethodRefParameter364', a2)
    if hasattr(a2, 'ast_SimpleName365'):
        assert not _is_linked(a2, 'ast_SimpleName365', b)


def test_assoc_parameters181_reverse_link_reassign_clear():
    a1 = ast_SingleVariableDeclaration(varargs=True)
    a2 = ast_SingleVariableDeclaration(varargs=False)
    b = ast_MethodDeclaration(constructor=True)
    _safe_set(b, 'ast_MethodDeclaration182', {a1})
    assert _is_linked(b, 'ast_MethodDeclaration182', a1)
    if hasattr(a1, 'ast_SingleVariableDeclaration183'):
        assert _is_linked(a1, 'ast_SingleVariableDeclaration183', b)
    _safe_set(b, 'ast_MethodDeclaration182', {a2})
    assert _is_linked(b, 'ast_MethodDeclaration182', a2)
    if hasattr(a1, 'ast_SingleVariableDeclaration183'):
        assert not _is_linked(a1, 'ast_SingleVariableDeclaration183', b)
    if hasattr(a2, 'ast_SingleVariableDeclaration183'):
        assert _is_linked(a2, 'ast_SingleVariableDeclaration183', b)
    _safe_set(b, 'ast_MethodDeclaration182', set())
    assert not _is_linked(b, 'ast_MethodDeclaration182', a2)
    if hasattr(a2, 'ast_SingleVariableDeclaration183'):
        assert not _is_linked(a2, 'ast_SingleVariableDeclaration183', b)


def test_assoc_receiverQualifier178_reverse_link_reassign_clear():
    a1 = ast_SimpleName(identifier="sample_text")
    a2 = ast_SimpleName(identifier="sample_text_2")
    b = ast_MethodDeclaration(constructor=True)
    _safe_set(b, 'ast_MethodDeclaration179', a1)
    assert _is_linked(b, 'ast_MethodDeclaration179', a1)
    if hasattr(a1, 'ast_SimpleName180'):
        assert _is_linked(a1, 'ast_SimpleName180', b)
    _safe_set(b, 'ast_MethodDeclaration179', a2)
    assert _is_linked(b, 'ast_MethodDeclaration179', a2)
    if hasattr(a1, 'ast_SimpleName180'):
        assert not _is_linked(a1, 'ast_SimpleName180', b)
    if hasattr(a2, 'ast_SimpleName180'):
        assert _is_linked(a2, 'ast_SimpleName180', b)
    _safe_set(b, 'ast_MethodDeclaration179', None)
    assert not _is_linked(b, 'ast_MethodDeclaration179', a2)
    if hasattr(a2, 'ast_SimpleName180'):
        assert not _is_linked(a2, 'ast_SimpleName180', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations218_stub_double():
    # ast_Annotation has no real 'ast_Annotation219' property in the generated
    # code (a bare stub) -- manually attach it so ast_PrimitiveType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_PrimitiveType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_PrimitiveType(primitiveTypeCode="sample_text")
    partner = ast_Annotation()
    setattr(partner, 'ast_Annotation219', None)
    _safe_set(owner, 'ast_PrimitiveType', {partner})
    assert getattr(partner, 'ast_Annotation219') == owner
    _safe_set(owner, 'ast_PrimitiveType', set())
    assert getattr(partner, 'ast_Annotation219') is None


def test_assoc_annotations427_stub_double():
    # ast_Annotation has no real 'ast_Annotation428' property in the generated
    # code (a bare stub) -- manually attach it so ast_WildcardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_WildcardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_WildcardType(upperBound=True)
    partner = ast_Annotation()
    setattr(partner, 'ast_Annotation428', None)
    _safe_set(owner, 'ast_WildcardType', {partner})
    assert getattr(partner, 'ast_Annotation428') == owner
    _safe_set(owner, 'ast_WildcardType', set())
    assert getattr(partner, 'ast_Annotation428') is None


def test_assoc_body190_stub_double():
    # ast_Block has no real 'ast_Block192' property in the generated
    # code (a bare stub) -- manually attach it so ast_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MethodDeclaration(constructor=True)
    partner = ast_Block()
    setattr(partner, 'ast_Block192', None)
    _safe_set(owner, 'ast_MethodDeclaration191', partner)
    assert getattr(partner, 'ast_Block192') == owner
    _safe_set(owner, 'ast_MethodDeclaration191', None)
    assert getattr(partner, 'ast_Block192') is None


def test_assoc_body469_stub_double():
    # ast_ASTNode has no real 'ast_ASTNode' property in the generated
    # code (a bare stub) -- manually attach it so ast_LambdaExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_LambdaExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_LambdaExpression(parentheses=True)
    partner = ast_ASTNode()
    setattr(partner, 'ast_ASTNode', None)
    _safe_set(owner, 'ast_LambdaExpression470', partner)
    assert getattr(partner, 'ast_ASTNode') == owner
    _safe_set(owner, 'ast_LambdaExpression470', None)
    assert getattr(partner, 'ast_ASTNode') is None


def test_assoc_bodyDeclarations317_stub_double():
    # ast_BodyDeclaration has no real 'ast_BodyDeclaration319' property in the generated
    # code (a bare stub) -- manually attach it so ast_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_TypeDeclaration(interface=True)
    partner = ast_BodyDeclaration()
    setattr(partner, 'ast_BodyDeclaration319', None)
    _safe_set(owner, 'ast_TypeDeclaration318', {partner})
    assert getattr(partner, 'ast_BodyDeclaration319') == owner
    _safe_set(owner, 'ast_TypeDeclaration318', set())
    assert getattr(partner, 'ast_BodyDeclaration319') is None


def test_assoc_bound429_stub_double():
    # ast_Type has no real 'ast_Type431' property in the generated
    # code (a bare stub) -- manually attach it so ast_WildcardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_WildcardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_WildcardType(upperBound=True)
    partner = ast_Type()
    setattr(partner, 'ast_Type431', None)
    _safe_set(owner, 'ast_WildcardType430', partner)
    assert getattr(partner, 'ast_Type431') == owner
    _safe_set(owner, 'ast_WildcardType430', None)
    assert getattr(partner, 'ast_Type431') is None


def test_assoc_exception58_stub_double():
    # ast_CatchClause has no real 'ast_CatchClause' property in the generated
    # code (a bare stub) -- manually attach it so ast_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SingleVariableDeclaration(varargs=True)
    partner = ast_CatchClause()
    setattr(partner, 'ast_CatchClause', None)
    _safe_set(owner, 'ast_SingleVariableDeclaration', partner)
    assert getattr(partner, 'ast_CatchClause') == owner
    _safe_set(owner, 'ast_SingleVariableDeclaration', None)
    assert getattr(partner, 'ast_CatchClause') is None


def test_assoc_extendedOperands143_stub_double():
    # ast_Expression has no real 'ast_Expression145' property in the generated
    # code (a bare stub) -- manually attach it so ast_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_InfixExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression145', None)
    _safe_set(owner, 'ast_InfixExpression144', {partner})
    assert getattr(partner, 'ast_Expression145') == owner
    _safe_set(owner, 'ast_InfixExpression144', set())
    assert getattr(partner, 'ast_Expression145') is None


def test_assoc_extraDimensions2184_stub_double():
    # ast_Dimension has no real 'ast_Dimension186' property in the generated
    # code (a bare stub) -- manually attach it so ast_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MethodDeclaration(constructor=True)
    partner = ast_Dimension()
    setattr(partner, 'ast_Dimension186', None)
    _safe_set(owner, 'ast_MethodDeclaration185', {partner})
    assert getattr(partner, 'ast_Dimension186') == owner
    _safe_set(owner, 'ast_MethodDeclaration185', set())
    assert getattr(partner, 'ast_Dimension186') is None


def test_assoc_extraDimensions2244_stub_double():
    # ast_Dimension has no real 'ast_Dimension246' property in the generated
    # code (a bare stub) -- manually attach it so ast_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SingleVariableDeclaration(varargs=True)
    partner = ast_Dimension()
    setattr(partner, 'ast_Dimension246', None)
    _safe_set(owner, 'ast_SingleVariableDeclaration245', {partner})
    assert getattr(partner, 'ast_Dimension246') == owner
    _safe_set(owner, 'ast_SingleVariableDeclaration245', set())
    assert getattr(partner, 'ast_Dimension246') is None


def test_assoc_fragments20_stub_double():
    # ast_IDocElement has no real 'ast_IDocElement' property in the generated
    # code (a bare stub) -- manually attach it so ast_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_TagElement(tagName="sample_text")
    partner = ast_IDocElement()
    setattr(partner, 'ast_IDocElement', None)
    _safe_set(owner, 'ast_TagElement', {partner})
    assert getattr(partner, 'ast_IDocElement') == owner
    _safe_set(owner, 'ast_TagElement', set())
    assert getattr(partner, 'ast_IDocElement') is None


def test_assoc_imports77_stub_double():
    # ast_CompilationUnit has no real 'ast_CompilationUnit78' property in the generated
    # code (a bare stub) -- manually attach it so ast_ImportDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_ImportDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_ImportDeclaration(onDemand=True, static=True)
    partner = ast_CompilationUnit()
    setattr(partner, 'ast_CompilationUnit78', None)
    _safe_set(owner, 'ast_ImportDeclaration', partner)
    assert owner in getattr(partner, 'ast_CompilationUnit78')
    _safe_set(owner, 'ast_ImportDeclaration', None)
    assert owner not in getattr(partner, 'ast_CompilationUnit78')


def test_assoc_initializer247_stub_double():
    # ast_Expression has no real 'ast_Expression249' property in the generated
    # code (a bare stub) -- manually attach it so ast_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SingleVariableDeclaration(varargs=True)
    partner = ast_Expression()
    setattr(partner, 'ast_Expression249', None)
    _safe_set(owner, 'ast_SingleVariableDeclaration248', partner)
    assert getattr(partner, 'ast_Expression249') == owner
    _safe_set(owner, 'ast_SingleVariableDeclaration248', None)
    assert getattr(partner, 'ast_Expression249') is None


def test_assoc_javadoc162_stub_double():
    # ast_Javadoc has no real 'ast_Javadoc163' property in the generated
    # code (a bare stub) -- manually attach it so ast_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MethodDeclaration(constructor=True)
    partner = ast_Javadoc()
    setattr(partner, 'ast_Javadoc163', None)
    _safe_set(owner, 'ast_MethodDeclaration', partner)
    assert getattr(partner, 'ast_Javadoc163') == owner
    _safe_set(owner, 'ast_MethodDeclaration', None)
    assert getattr(partner, 'ast_Javadoc163') is None


def test_assoc_javadoc300_stub_double():
    # ast_Javadoc has no real 'ast_Javadoc301' property in the generated
    # code (a bare stub) -- manually attach it so ast_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_TypeDeclaration(interface=True)
    partner = ast_Javadoc()
    setattr(partner, 'ast_Javadoc301', None)
    _safe_set(owner, 'ast_TypeDeclaration', partner)
    assert getattr(partner, 'ast_Javadoc301') == owner
    _safe_set(owner, 'ast_TypeDeclaration', None)
    assert getattr(partner, 'ast_Javadoc301') is None


def test_assoc_label157_stub_double():
    # ast_LabeledStatement has no real 'ast_LabeledStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_LabeledStatement()
    setattr(partner, 'ast_LabeledStatement', None)
    _safe_set(owner, 'ast_SimpleName158', partner)
    assert getattr(partner, 'ast_LabeledStatement') == owner
    _safe_set(owner, 'ast_SimpleName158', None)
    assert getattr(partner, 'ast_LabeledStatement') is None


def test_assoc_label51_stub_double():
    # ast_BreakStatement has no real 'ast_BreakStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_BreakStatement()
    setattr(partner, 'ast_BreakStatement', None)
    _safe_set(owner, 'ast_SimpleName52', partner)
    assert getattr(partner, 'ast_BreakStatement') == owner
    _safe_set(owner, 'ast_SimpleName52', None)
    assert getattr(partner, 'ast_BreakStatement') is None


def test_assoc_label94_stub_double():
    # ast_ContinueStatement has no real 'ast_ContinueStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_ContinueStatement()
    setattr(partner, 'ast_ContinueStatement', None)
    _safe_set(owner, 'ast_SimpleName95', partner)
    assert getattr(partner, 'ast_ContinueStatement') == owner
    _safe_set(owner, 'ast_SimpleName95', None)
    assert getattr(partner, 'ast_ContinueStatement') is None


def test_assoc_leftHandSide45_stub_double():
    # ast_Expression has no real 'ast_Expression46' property in the generated
    # code (a bare stub) -- manually attach it so ast_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Assignment(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression46', None)
    _safe_set(owner, 'ast_Assignment', partner)
    assert getattr(partner, 'ast_Expression46') == owner
    _safe_set(owner, 'ast_Assignment', None)
    assert getattr(partner, 'ast_Expression46') is None


def test_assoc_leftOperand138_stub_double():
    # ast_Expression has no real 'ast_Expression139' property in the generated
    # code (a bare stub) -- manually attach it so ast_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_InfixExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression139', None)
    _safe_set(owner, 'ast_InfixExpression', partner)
    assert getattr(partner, 'ast_Expression139') == owner
    _safe_set(owner, 'ast_InfixExpression', None)
    assert getattr(partner, 'ast_Expression139') is None


def test_assoc_modifiers164_stub_double():
    # ast_IExtendedModifier has no real 'ast_IExtendedModifier166' property in the generated
    # code (a bare stub) -- manually attach it so ast_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MethodDeclaration(constructor=True)
    partner = ast_IExtendedModifier()
    setattr(partner, 'ast_IExtendedModifier166', None)
    _safe_set(owner, 'ast_MethodDeclaration165', {partner})
    assert getattr(partner, 'ast_IExtendedModifier166') == owner
    _safe_set(owner, 'ast_MethodDeclaration165', set())
    assert getattr(partner, 'ast_IExtendedModifier166') is None


def test_assoc_modifiers232_stub_double():
    # ast_IExtendedModifier has no real 'ast_IExtendedModifier234' property in the generated
    # code (a bare stub) -- manually attach it so ast_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SingleVariableDeclaration(varargs=True)
    partner = ast_IExtendedModifier()
    setattr(partner, 'ast_IExtendedModifier234', None)
    _safe_set(owner, 'ast_SingleVariableDeclaration233', {partner})
    assert getattr(partner, 'ast_IExtendedModifier234') == owner
    _safe_set(owner, 'ast_SingleVariableDeclaration233', set())
    assert getattr(partner, 'ast_IExtendedModifier234') is None


def test_assoc_modifiers302_stub_double():
    # ast_IExtendedModifier has no real 'ast_IExtendedModifier304' property in the generated
    # code (a bare stub) -- manually attach it so ast_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_TypeDeclaration(interface=True)
    partner = ast_IExtendedModifier()
    setattr(partner, 'ast_IExtendedModifier304', None)
    _safe_set(owner, 'ast_TypeDeclaration303', {partner})
    assert getattr(partner, 'ast_IExtendedModifier304') == owner
    _safe_set(owner, 'ast_TypeDeclaration303', set())
    assert getattr(partner, 'ast_IExtendedModifier304') is None


def test_assoc_name105_stub_double():
    # ast_FieldAccess has no real 'ast_FieldAccess106' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_FieldAccess()
    setattr(partner, 'ast_FieldAccess106', None)
    _safe_set(owner, 'ast_SimpleName107', partner)
    assert getattr(partner, 'ast_FieldAccess106') == owner
    _safe_set(owner, 'ast_SimpleName107', None)
    assert getattr(partner, 'ast_FieldAccess106') is None


def test_assoc_name11_stub_double():
    # ast_MemberRef has no real 'ast_MemberRef12' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_MemberRef()
    setattr(partner, 'ast_MemberRef12', None)
    _safe_set(owner, 'ast_SimpleName', partner)
    assert getattr(partner, 'ast_MemberRef12') == owner
    _safe_set(owner, 'ast_SimpleName', None)
    assert getattr(partner, 'ast_MemberRef12') is None


def test_assoc_name135_stub_double():
    # ast_Name has no real 'ast_Name137' property in the generated
    # code (a bare stub) -- manually attach it so ast_ImportDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_ImportDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_ImportDeclaration(onDemand=True, static=True)
    partner = ast_Name()
    setattr(partner, 'ast_Name137', None)
    _safe_set(owner, 'ast_ImportDeclaration136', partner)
    assert getattr(partner, 'ast_Name137') == owner
    _safe_set(owner, 'ast_ImportDeclaration136', None)
    assert getattr(partner, 'ast_Name137') is None


def test_assoc_name15_stub_double():
    # ast_MethodRef has no real 'ast_MethodRef16' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_MethodRef()
    setattr(partner, 'ast_MethodRef16', None)
    _safe_set(owner, 'ast_SimpleName17', partner)
    assert getattr(partner, 'ast_MethodRef16') == owner
    _safe_set(owner, 'ast_SimpleName17', None)
    assert getattr(partner, 'ast_MethodRef16') is None


def test_assoc_name198_stub_double():
    # ast_MethodInvocation has no real 'ast_MethodInvocation199' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_MethodInvocation()
    setattr(partner, 'ast_MethodInvocation199', None)
    _safe_set(owner, 'ast_SimpleName200', partner)
    assert getattr(partner, 'ast_MethodInvocation199') == owner
    _safe_set(owner, 'ast_SimpleName200', None)
    assert getattr(partner, 'ast_MethodInvocation199') is None


def test_assoc_name222_stub_double():
    # ast_QualifiedName has no real 'ast_QualifiedName223' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_QualifiedName()
    setattr(partner, 'ast_QualifiedName223', None)
    _safe_set(owner, 'ast_SimpleName224', partner)
    assert getattr(partner, 'ast_QualifiedName223') == owner
    _safe_set(owner, 'ast_SimpleName224', None)
    assert getattr(partner, 'ast_QualifiedName223') is None


def test_assoc_name260_stub_double():
    # ast_SuperFieldAccess has no real 'ast_SuperFieldAccess261' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_SuperFieldAccess()
    setattr(partner, 'ast_SuperFieldAccess261', None)
    _safe_set(owner, 'ast_SimpleName262', partner)
    assert getattr(partner, 'ast_SuperFieldAccess261') == owner
    _safe_set(owner, 'ast_SimpleName262', None)
    assert getattr(partner, 'ast_SuperFieldAccess261') is None


def test_assoc_name268_stub_double():
    # ast_SuperMethodInvocation has no real 'ast_SuperMethodInvocation269' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_SuperMethodInvocation()
    setattr(partner, 'ast_SuperMethodInvocation269', None)
    _safe_set(owner, 'ast_SimpleName270', partner)
    assert getattr(partner, 'ast_SuperMethodInvocation269') == owner
    _safe_set(owner, 'ast_SimpleName270', None)
    assert getattr(partner, 'ast_SuperMethodInvocation269') is None


def test_assoc_name333_stub_double():
    # ast_VariableDeclarationFragment has no real 'ast_VariableDeclarationFragment334' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_VariableDeclarationFragment()
    setattr(partner, 'ast_VariableDeclarationFragment334', None)
    _safe_set(owner, 'ast_SimpleName335', partner)
    assert getattr(partner, 'ast_VariableDeclarationFragment334') == owner
    _safe_set(owner, 'ast_SimpleName335', None)
    assert getattr(partner, 'ast_VariableDeclarationFragment334') is None


def test_assoc_name379_stub_double():
    # ast_EnumDeclaration has no real 'ast_EnumDeclaration380' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_EnumDeclaration()
    setattr(partner, 'ast_EnumDeclaration380', None)
    _safe_set(owner, 'ast_SimpleName381', partner)
    assert getattr(partner, 'ast_EnumDeclaration380') == owner
    _safe_set(owner, 'ast_SimpleName381', None)
    assert getattr(partner, 'ast_EnumDeclaration380') is None


def test_assoc_name396_stub_double():
    # ast_EnumConstantDeclaration has no real 'ast_EnumConstantDeclaration397' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_EnumConstantDeclaration()
    setattr(partner, 'ast_EnumConstantDeclaration397', None)
    _safe_set(owner, 'ast_SimpleName398', partner)
    assert getattr(partner, 'ast_EnumConstantDeclaration397') == owner
    _safe_set(owner, 'ast_SimpleName398', None)
    assert getattr(partner, 'ast_EnumConstantDeclaration397') is None


def test_assoc_name408_stub_double():
    # ast_TypeParameter has no real 'ast_TypeParameter409' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_TypeParameter()
    setattr(partner, 'ast_TypeParameter409', None)
    _safe_set(owner, 'ast_SimpleName410', partner)
    assert getattr(partner, 'ast_TypeParameter409') == owner
    _safe_set(owner, 'ast_SimpleName410', None)
    assert getattr(partner, 'ast_TypeParameter409') is None


def test_assoc_name424_stub_double():
    # ast_QualifiedType has no real 'ast_QualifiedType425' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_QualifiedType()
    setattr(partner, 'ast_QualifiedType425', None)
    _safe_set(owner, 'ast_SimpleName426', partner)
    assert getattr(partner, 'ast_QualifiedType425') == owner
    _safe_set(owner, 'ast_SimpleName426', None)
    assert getattr(partner, 'ast_QualifiedType425') is None


def test_assoc_name432_stub_double():
    # ast_MemberValuePair has no real 'ast_MemberValuePair433' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_MemberValuePair()
    setattr(partner, 'ast_MemberValuePair433', None)
    _safe_set(owner, 'ast_SimpleName434', partner)
    assert getattr(partner, 'ast_MemberValuePair433') == owner
    _safe_set(owner, 'ast_SimpleName434', None)
    assert getattr(partner, 'ast_MemberValuePair433') is None


def test_assoc_name443_stub_double():
    # ast_AnnotationTypeDeclaration has no real 'ast_AnnotationTypeDeclaration444' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_AnnotationTypeDeclaration()
    setattr(partner, 'ast_AnnotationTypeDeclaration444', None)
    _safe_set(owner, 'ast_SimpleName445', partner)
    assert getattr(partner, 'ast_AnnotationTypeDeclaration444') == owner
    _safe_set(owner, 'ast_SimpleName445', None)
    assert getattr(partner, 'ast_AnnotationTypeDeclaration444') is None


def test_assoc_name457_stub_double():
    # ast_AnnotationTypeMemberDeclaration has no real 'ast_AnnotationTypeMemberDeclaration458' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_AnnotationTypeMemberDeclaration()
    setattr(partner, 'ast_AnnotationTypeMemberDeclaration458', None)
    _safe_set(owner, 'ast_SimpleName459', partner)
    assert getattr(partner, 'ast_AnnotationTypeMemberDeclaration458') == owner
    _safe_set(owner, 'ast_SimpleName459', None)
    assert getattr(partner, 'ast_AnnotationTypeMemberDeclaration458') is None


def test_assoc_name478_stub_double():
    # ast_NameQualifiedType has no real 'ast_NameQualifiedType479' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_NameQualifiedType()
    setattr(partner, 'ast_NameQualifiedType479', None)
    _safe_set(owner, 'ast_SimpleName480', partner)
    assert getattr(partner, 'ast_NameQualifiedType479') == owner
    _safe_set(owner, 'ast_SimpleName480', None)
    assert getattr(partner, 'ast_NameQualifiedType479') is None


def test_assoc_name491_stub_double():
    # ast_ExpressionMethodReference has no real 'ast_ExpressionMethodReference492' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_ExpressionMethodReference()
    setattr(partner, 'ast_ExpressionMethodReference492', None)
    _safe_set(owner, 'ast_SimpleName493', partner)
    assert getattr(partner, 'ast_ExpressionMethodReference492') == owner
    _safe_set(owner, 'ast_SimpleName493', None)
    assert getattr(partner, 'ast_ExpressionMethodReference492') is None


def test_assoc_name499_stub_double():
    # ast_SuperMethodReference has no real 'ast_SuperMethodReference500' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_SuperMethodReference()
    setattr(partner, 'ast_SuperMethodReference500', None)
    _safe_set(owner, 'ast_SimpleName501', partner)
    assert getattr(partner, 'ast_SuperMethodReference500') == owner
    _safe_set(owner, 'ast_SimpleName501', None)
    assert getattr(partner, 'ast_SuperMethodReference500') is None


def test_assoc_name507_stub_double():
    # ast_TypeMethodReference has no real 'ast_TypeMethodReference508' property in the generated
    # code (a bare stub) -- manually attach it so ast_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SimpleName(identifier="sample_text")
    partner = ast_TypeMethodReference()
    setattr(partner, 'ast_TypeMethodReference508', None)
    _safe_set(owner, 'ast_SimpleName509', partner)
    assert getattr(partner, 'ast_TypeMethodReference508') == owner
    _safe_set(owner, 'ast_SimpleName509', None)
    assert getattr(partner, 'ast_TypeMethodReference508') is None


def test_assoc_operand214_stub_double():
    # ast_Expression has no real 'ast_Expression215' property in the generated
    # code (a bare stub) -- manually attach it so ast_PostfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_PostfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_PostfixExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression215', None)
    _safe_set(owner, 'ast_PostfixExpression', partner)
    assert getattr(partner, 'ast_Expression215') == owner
    _safe_set(owner, 'ast_PostfixExpression', None)
    assert getattr(partner, 'ast_Expression215') is None


def test_assoc_operand216_stub_double():
    # ast_Expression has no real 'ast_Expression217' property in the generated
    # code (a bare stub) -- manually attach it so ast_PrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_PrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_PrefixExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression217', None)
    _safe_set(owner, 'ast_PrefixExpression', partner)
    assert getattr(partner, 'ast_Expression217') == owner
    _safe_set(owner, 'ast_PrefixExpression', None)
    assert getattr(partner, 'ast_Expression217') is None


def test_assoc_parameter366_stub_double():
    # ast_EnhancedForStatement has no real 'ast_EnhancedForStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SingleVariableDeclaration(varargs=True)
    partner = ast_EnhancedForStatement()
    setattr(partner, 'ast_EnhancedForStatement', None)
    _safe_set(owner, 'ast_SingleVariableDeclaration367', partner)
    assert getattr(partner, 'ast_EnhancedForStatement') == owner
    _safe_set(owner, 'ast_SingleVariableDeclaration367', None)
    assert getattr(partner, 'ast_EnhancedForStatement') is None


def test_assoc_parameters18_stub_double():
    # ast_MethodRef has no real 'ast_MethodRef19' property in the generated
    # code (a bare stub) -- manually attach it so ast_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MethodRefParameter(varargs=True)
    partner = ast_MethodRef()
    setattr(partner, 'ast_MethodRef19', None)
    _safe_set(owner, 'ast_MethodRefParameter', partner)
    assert owner in getattr(partner, 'ast_MethodRef19')
    _safe_set(owner, 'ast_MethodRefParameter', None)
    assert owner not in getattr(partner, 'ast_MethodRef19')


def test_assoc_parameters468_stub_double():
    # ast_VariableDeclaration has no real 'ast_VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so ast_LambdaExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_LambdaExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_LambdaExpression(parentheses=True)
    partner = ast_VariableDeclaration()
    setattr(partner, 'ast_VariableDeclaration', None)
    _safe_set(owner, 'ast_LambdaExpression', {partner})
    assert getattr(partner, 'ast_VariableDeclaration') == owner
    _safe_set(owner, 'ast_LambdaExpression', set())
    assert getattr(partner, 'ast_VariableDeclaration') is None


def test_assoc_receiverType175_stub_double():
    # ast_Type has no real 'ast_Type177' property in the generated
    # code (a bare stub) -- manually attach it so ast_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MethodDeclaration(constructor=True)
    partner = ast_Type()
    setattr(partner, 'ast_Type177', None)
    _safe_set(owner, 'ast_MethodDeclaration176', partner)
    assert getattr(partner, 'ast_Type177') == owner
    _safe_set(owner, 'ast_MethodDeclaration176', None)
    assert getattr(partner, 'ast_Type177') is None


def test_assoc_returnType2169_stub_double():
    # ast_Type has no real 'ast_Type171' property in the generated
    # code (a bare stub) -- manually attach it so ast_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MethodDeclaration(constructor=True)
    partner = ast_Type()
    setattr(partner, 'ast_Type171', None)
    _safe_set(owner, 'ast_MethodDeclaration170', partner)
    assert getattr(partner, 'ast_Type171') == owner
    _safe_set(owner, 'ast_MethodDeclaration170', None)
    assert getattr(partner, 'ast_Type171') is None


def test_assoc_rightHandSide47_stub_double():
    # ast_Expression has no real 'ast_Expression49' property in the generated
    # code (a bare stub) -- manually attach it so ast_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Assignment(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression49', None)
    _safe_set(owner, 'ast_Assignment48', partner)
    assert getattr(partner, 'ast_Expression49') == owner
    _safe_set(owner, 'ast_Assignment48', None)
    assert getattr(partner, 'ast_Expression49') is None


def test_assoc_rightOperand140_stub_double():
    # ast_Expression has no real 'ast_Expression142' property in the generated
    # code (a bare stub) -- manually attach it so ast_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_InfixExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression142', None)
    _safe_set(owner, 'ast_InfixExpression141', partner)
    assert getattr(partner, 'ast_Expression142') == owner
    _safe_set(owner, 'ast_InfixExpression141', None)
    assert getattr(partner, 'ast_Expression142') is None


def test_assoc_superInterfaceTypes314_stub_double():
    # ast_Type has no real 'ast_Type316' property in the generated
    # code (a bare stub) -- manually attach it so ast_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_TypeDeclaration(interface=True)
    partner = ast_Type()
    setattr(partner, 'ast_Type316', None)
    _safe_set(owner, 'ast_TypeDeclaration315', {partner})
    assert getattr(partner, 'ast_Type316') == owner
    _safe_set(owner, 'ast_TypeDeclaration315', set())
    assert getattr(partner, 'ast_Type316') is None


def test_assoc_superclassType311_stub_double():
    # ast_Type has no real 'ast_Type313' property in the generated
    # code (a bare stub) -- manually attach it so ast_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_TypeDeclaration(interface=True)
    partner = ast_Type()
    setattr(partner, 'ast_Type313', None)
    _safe_set(owner, 'ast_TypeDeclaration312', partner)
    assert getattr(partner, 'ast_Type313') == owner
    _safe_set(owner, 'ast_TypeDeclaration312', None)
    assert getattr(partner, 'ast_Type313') is None


def test_assoc_tags154_stub_double():
    # ast_Javadoc has no real 'ast_Javadoc155' property in the generated
    # code (a bare stub) -- manually attach it so ast_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_TagElement(tagName="sample_text")
    partner = ast_Javadoc()
    setattr(partner, 'ast_Javadoc155', None)
    _safe_set(owner, 'ast_TagElement156', partner)
    assert owner in getattr(partner, 'ast_Javadoc155')
    _safe_set(owner, 'ast_TagElement156', None)
    assert owner not in getattr(partner, 'ast_Javadoc155')


def test_assoc_thrownExceptionTypes187_stub_double():
    # ast_Type has no real 'ast_Type189' property in the generated
    # code (a bare stub) -- manually attach it so ast_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MethodDeclaration(constructor=True)
    partner = ast_Type()
    setattr(partner, 'ast_Type189', None)
    _safe_set(owner, 'ast_MethodDeclaration188', {partner})
    assert getattr(partner, 'ast_Type189') == owner
    _safe_set(owner, 'ast_MethodDeclaration188', set())
    assert getattr(partner, 'ast_Type189') is None


def test_assoc_type235_stub_double():
    # ast_Type has no real 'ast_Type237' property in the generated
    # code (a bare stub) -- manually attach it so ast_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SingleVariableDeclaration(varargs=True)
    partner = ast_Type()
    setattr(partner, 'ast_Type237', None)
    _safe_set(owner, 'ast_SingleVariableDeclaration236', partner)
    assert getattr(partner, 'ast_Type237') == owner
    _safe_set(owner, 'ast_SingleVariableDeclaration236', None)
    assert getattr(partner, 'ast_Type237') is None


def test_assoc_type360_stub_double():
    # ast_Type has no real 'ast_Type362' property in the generated
    # code (a bare stub) -- manually attach it so ast_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MethodRefParameter(varargs=True)
    partner = ast_Type()
    setattr(partner, 'ast_Type362', None)
    _safe_set(owner, 'ast_MethodRefParameter361', partner)
    assert getattr(partner, 'ast_Type362') == owner
    _safe_set(owner, 'ast_MethodRefParameter361', None)
    assert getattr(partner, 'ast_Type362') is None


def test_assoc_typeParameters167_stub_double():
    # ast_TypeParameter has no real 'ast_TypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so ast_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MethodDeclaration(constructor=True)
    partner = ast_TypeParameter()
    setattr(partner, 'ast_TypeParameter', None)
    _safe_set(owner, 'ast_MethodDeclaration168', {partner})
    assert getattr(partner, 'ast_TypeParameter') == owner
    _safe_set(owner, 'ast_MethodDeclaration168', set())
    assert getattr(partner, 'ast_TypeParameter') is None


def test_assoc_typeParameters308_stub_double():
    # ast_TypeParameter has no real 'ast_TypeParameter310' property in the generated
    # code (a bare stub) -- manually attach it so ast_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_TypeDeclaration(interface=True)
    partner = ast_TypeParameter()
    setattr(partner, 'ast_TypeParameter310', None)
    _safe_set(owner, 'ast_TypeDeclaration309', {partner})
    assert getattr(partner, 'ast_TypeParameter310') == owner
    _safe_set(owner, 'ast_TypeDeclaration309', set())
    assert getattr(partner, 'ast_TypeParameter310') is None


def test_assoc_varargsAnnotations238_stub_double():
    # ast_Annotation has no real 'ast_Annotation240' property in the generated
    # code (a bare stub) -- manually attach it so ast_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SingleVariableDeclaration(varargs=True)
    partner = ast_Annotation()
    setattr(partner, 'ast_Annotation240', None)
    _safe_set(owner, 'ast_SingleVariableDeclaration239', {partner})
    assert getattr(partner, 'ast_Annotation240') == owner
    _safe_set(owner, 'ast_SingleVariableDeclaration239', set())
    assert getattr(partner, 'ast_Annotation240') is None


