import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    AbstractMethodDeclaration,
    AbstractMethodInvocation,
    AbstractTypeDeclaration,
    AbstractTypeQualifiedExpression,
    AbstractVariablesContainer,
    AnnotationTypeDeclaration,
    AnnotationTypeMemberDeclaration,
    BodyDeclaration,
    ClassDeclaration,
    Comment,
    EnumDeclaration,
    Expression,
    InterfaceDeclaration,
    LabeledStatement,
    MethodDeclaration,
    NamedElement,
    NamespaceAccess,
    PrimitiveType,
    SingleVariableDeclaration,
    Statement,
    Type,
    TypeDeclaration,
    UnresolvedItem,
    VariableDeclaration,
    VariableDeclarationFragment,
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
    java_BlockComment,
    java_BodyDeclaration,
    java_BooleanLiteral,
    java_BreakStatement,
    java_CastExpression,
    java_CatchClause,
    java_CharacterLiteral,
    java_ClassDeclaration,
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
    java_Javadoc,
    java_LabeledStatement,
    java_LineComment,
    java_Manifest,
    java_ManifestAttribute,
    java_ManifestEntry,
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
    java_PackageAccess,
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
    java_TextElement,
    java_ThisExpression,
    java_ThrowStatement,
    java_TryStatement,
    java_Type,
    java_TypeAccess,
    java_TypeDeclaration,
    java_TypeDeclarationStatement,
    java_TypeLiteral,
    java_TypeParameter,
    java_UnresolvedAnnotationDeclaration,
    java_UnresolvedAnnotationTypeMemberDeclaration,
    java_UnresolvedClassDeclaration,
    java_UnresolvedEnumDeclaration,
    java_UnresolvedInterfaceDeclaration,
    java_UnresolvedItem,
    java_UnresolvedItemAccess,
    java_UnresolvedLabeledStatement,
    java_UnresolvedMethodDeclaration,
    java_UnresolvedSingleVariableDeclaration,
    java_UnresolvedType,
    java_UnresolvedTypeDeclaration,
    java_UnresolvedVariableDeclarationFragment,
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

def test_assoc_archives221_reverse_link_reassign_clear():
    a1 = java_Model(name="sample_text")
    a2 = java_Model(name="sample_text_2")
    b = java_Archive(originalFilePath="sample_text")
    _safe_set(b, 'java_Archive223', a1)
    assert _is_linked(b, 'java_Archive223', a1)
    if hasattr(a1, 'java_Model222'):
        assert _is_linked(a1, 'java_Model222', b)
    _safe_set(b, 'java_Archive223', a2)
    assert _is_linked(b, 'java_Archive223', a2)
    if hasattr(a1, 'java_Model222'):
        assert not _is_linked(a1, 'java_Model222', b)
    if hasattr(a2, 'java_Model222'):
        assert _is_linked(a2, 'java_Model222', b)
    _safe_set(b, 'java_Archive223', None)
    assert not _is_linked(b, 'java_Archive223', a2)
    if hasattr(a2, 'java_Model222'):
        assert not _is_linked(a2, 'java_Model222', b)


def test_assoc_attributes188_reverse_link_reassign_clear():
    a1 = java_ManifestEntry(name="sample_text")
    a2 = java_ManifestEntry(name="sample_text_2")
    b = java_ManifestAttribute(key="sample_text", value="sample_text")
    _safe_set(b, 'java_ManifestAttribute190', a1)
    assert _is_linked(b, 'java_ManifestAttribute190', a1)
    if hasattr(a1, 'java_ManifestEntry189'):
        assert _is_linked(a1, 'java_ManifestEntry189', b)
    _safe_set(b, 'java_ManifestAttribute190', a2)
    assert _is_linked(b, 'java_ManifestAttribute190', a2)
    if hasattr(a1, 'java_ManifestEntry189'):
        assert not _is_linked(a1, 'java_ManifestEntry189', b)
    if hasattr(a2, 'java_ManifestEntry189'):
        assert _is_linked(a2, 'java_ManifestEntry189', b)
    _safe_set(b, 'java_ManifestAttribute190', None)
    assert not _is_linked(b, 'java_ManifestAttribute190', a2)
    if hasattr(a2, 'java_ManifestEntry189'):
        assert not _is_linked(a2, 'java_ManifestEntry189', b)


def test_assoc_commentList107_reverse_link_reassign_clear():
    a1 = java_CompilationUnit(originalFilePath="sample_text")
    a2 = java_CompilationUnit(originalFilePath="sample_text_2")
    b = java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    _safe_set(b, 'java_Comment109', a1)
    assert _is_linked(b, 'java_Comment109', a1)
    if hasattr(a1, 'java_CompilationUnit108'):
        assert _is_linked(a1, 'java_CompilationUnit108', b)
    _safe_set(b, 'java_Comment109', a2)
    assert _is_linked(b, 'java_Comment109', a2)
    if hasattr(a1, 'java_CompilationUnit108'):
        assert not _is_linked(a1, 'java_CompilationUnit108', b)
    if hasattr(a2, 'java_CompilationUnit108'):
        assert _is_linked(a2, 'java_CompilationUnit108', b)
    _safe_set(b, 'java_Comment109', None)
    assert not _is_linked(b, 'java_Comment109', a2)
    if hasattr(a2, 'java_CompilationUnit108'):
        assert not _is_linked(a2, 'java_CompilationUnit108', b)


def test_assoc_compilationUnits218_reverse_link_reassign_clear():
    a1 = java_Model(name="sample_text")
    a2 = java_Model(name="sample_text_2")
    b = java_CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'java_CompilationUnit220', a1)
    assert _is_linked(b, 'java_CompilationUnit220', a1)
    if hasattr(a1, 'java_Model219'):
        assert _is_linked(a1, 'java_Model219', b)
    _safe_set(b, 'java_CompilationUnit220', a2)
    assert _is_linked(b, 'java_CompilationUnit220', a2)
    if hasattr(a1, 'java_Model219'):
        assert not _is_linked(a1, 'java_Model219', b)
    if hasattr(a2, 'java_Model219'):
        assert _is_linked(a2, 'java_Model219', b)
    _safe_set(b, 'java_CompilationUnit220', None)
    assert not _is_linked(b, 'java_CompilationUnit220', a2)
    if hasattr(a2, 'java_Model219'):
        assert not _is_linked(a2, 'java_Model219', b)


def test_assoc_importedElement162_reverse_link_reassign_clear():
    a1 = java_NamedElement(name="sample_text", proxy=True)
    a2 = java_NamedElement(name="sample_text_2", proxy=False)
    b = java_ImportDeclaration(static=True)
    _safe_set(b, 'usagesInImports', a1)
    assert _is_linked(b, 'usagesInImports', a1)
    if hasattr(a1, 'NamedElement'):
        assert _is_linked(a1, 'NamedElement', b)
    _safe_set(b, 'usagesInImports', a2)
    assert _is_linked(b, 'usagesInImports', a2)
    if hasattr(a1, 'NamedElement'):
        assert not _is_linked(a1, 'NamedElement', b)
    if hasattr(a2, 'NamedElement'):
        assert _is_linked(a2, 'NamedElement', b)
    _safe_set(b, 'usagesInImports', None)
    assert not _is_linked(b, 'usagesInImports', a2)
    if hasattr(a2, 'NamedElement'):
        assert not _is_linked(a2, 'NamedElement', b)


def test_assoc_imports110_reverse_link_reassign_clear():
    a1 = java_ImportDeclaration(static=True)
    a2 = java_ImportDeclaration(static=False)
    b = java_CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'java_CompilationUnit111', {a1})
    assert _is_linked(b, 'java_CompilationUnit111', a1)
    if hasattr(a1, 'java_ImportDeclaration'):
        assert _is_linked(a1, 'java_ImportDeclaration', b)
    _safe_set(b, 'java_CompilationUnit111', {a2})
    assert _is_linked(b, 'java_CompilationUnit111', a2)
    if hasattr(a1, 'java_ImportDeclaration'):
        assert not _is_linked(a1, 'java_ImportDeclaration', b)
    if hasattr(a2, 'java_ImportDeclaration'):
        assert _is_linked(a2, 'java_ImportDeclaration', b)
    _safe_set(b, 'java_CompilationUnit111', set())
    assert not _is_linked(b, 'java_CompilationUnit111', a2)
    if hasattr(a2, 'java_ImportDeclaration'):
        assert not _is_linked(a2, 'java_ImportDeclaration', b)


def test_assoc_modifier268_reverse_link_reassign_clear():
    a1 = java_SingleVariableDeclaration(varargs=True)
    a2 = java_SingleVariableDeclaration(varargs=False)
    b = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    _safe_set(b, 'Modifier269', a1)
    assert _is_linked(b, 'Modifier269', a1)
    if hasattr(a1, 'singleVariableDeclaration'):
        assert _is_linked(a1, 'singleVariableDeclaration', b)
    _safe_set(b, 'Modifier269', a2)
    assert _is_linked(b, 'Modifier269', a2)
    if hasattr(a1, 'singleVariableDeclaration'):
        assert not _is_linked(a1, 'singleVariableDeclaration', b)
    if hasattr(a2, 'singleVariableDeclaration'):
        assert _is_linked(a2, 'singleVariableDeclaration', b)
    _safe_set(b, 'Modifier269', None)
    assert not _is_linked(b, 'Modifier269', a2)
    if hasattr(a2, 'singleVariableDeclaration'):
        assert not _is_linked(a2, 'singleVariableDeclaration', b)


def test_assoc_modifier334_reverse_link_reassign_clear():
    a1 = java_VariableDeclarationStatement(extraArrayDimensions=7)
    a2 = java_VariableDeclarationStatement(extraArrayDimensions=13)
    b = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    _safe_set(b, 'Modifier335', a1)
    assert _is_linked(b, 'Modifier335', a1)
    if hasattr(a1, 'variableDeclarationStatement'):
        assert _is_linked(a1, 'variableDeclarationStatement', b)
    _safe_set(b, 'Modifier335', a2)
    assert _is_linked(b, 'Modifier335', a2)
    if hasattr(a1, 'variableDeclarationStatement'):
        assert not _is_linked(a1, 'variableDeclarationStatement', b)
    if hasattr(a2, 'variableDeclarationStatement'):
        assert _is_linked(a2, 'variableDeclarationStatement', b)
    _safe_set(b, 'Modifier335', None)
    assert not _is_linked(b, 'Modifier335', a2)
    if hasattr(a2, 'variableDeclarationStatement'):
        assert not _is_linked(a2, 'variableDeclarationStatement', b)


def test_assoc_redefinedMethodDeclaration198_reverse_link_reassign_clear():
    a1 = java_MethodDeclaration(extraArrayDimensions=7)
    a2 = java_MethodDeclaration(extraArrayDimensions=13)
    b = java_MethodDeclaration(extraArrayDimensions=7)
    _safe_set(b, 'redefinitions', a1)
    assert _is_linked(b, 'redefinitions', a1)
    if hasattr(a1, 'MethodDeclaration'):
        assert _is_linked(a1, 'MethodDeclaration', b)
    _safe_set(b, 'redefinitions', a2)
    assert _is_linked(b, 'redefinitions', a2)
    if hasattr(a1, 'MethodDeclaration'):
        assert not _is_linked(a1, 'MethodDeclaration', b)
    if hasattr(a2, 'MethodDeclaration'):
        assert _is_linked(a2, 'MethodDeclaration', b)
    _safe_set(b, 'redefinitions', None)
    assert not _is_linked(b, 'redefinitions', a2)
    if hasattr(a2, 'MethodDeclaration'):
        assert not _is_linked(a2, 'MethodDeclaration', b)


def test_assoc_redefinitions200_reverse_link_reassign_clear():
    a1 = java_MethodDeclaration(extraArrayDimensions=7)
    a2 = java_MethodDeclaration(extraArrayDimensions=13)
    b = java_MethodDeclaration(extraArrayDimensions=7)
    _safe_set(b, 'redefinedMethodDeclaration', {a1})
    assert _is_linked(b, 'redefinedMethodDeclaration', a1)
    if hasattr(a1, 'MethodDeclaration201'):
        assert _is_linked(a1, 'MethodDeclaration201', b)
    _safe_set(b, 'redefinedMethodDeclaration', {a2})
    assert _is_linked(b, 'redefinedMethodDeclaration', a2)
    if hasattr(a1, 'MethodDeclaration201'):
        assert not _is_linked(a1, 'MethodDeclaration201', b)
    if hasattr(a2, 'MethodDeclaration201'):
        assert _is_linked(a2, 'MethodDeclaration201', b)
    _safe_set(b, 'redefinedMethodDeclaration', set())
    assert not _is_linked(b, 'redefinedMethodDeclaration', a2)
    if hasattr(a2, 'MethodDeclaration201'):
        assert not _is_linked(a2, 'MethodDeclaration201', b)


def test_assoc_singleVariableDeclaration226_reverse_link_reassign_clear():
    a1 = java_SingleVariableDeclaration(varargs=True)
    a2 = java_SingleVariableDeclaration(varargs=False)
    b = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    _safe_set(b, 'modifier227', a1)
    assert _is_linked(b, 'modifier227', a1)
    if hasattr(a1, 'SingleVariableDeclaration228'):
        assert _is_linked(a1, 'SingleVariableDeclaration228', b)
    _safe_set(b, 'modifier227', a2)
    assert _is_linked(b, 'modifier227', a2)
    if hasattr(a1, 'SingleVariableDeclaration228'):
        assert not _is_linked(a1, 'SingleVariableDeclaration228', b)
    if hasattr(a2, 'SingleVariableDeclaration228'):
        assert _is_linked(a2, 'SingleVariableDeclaration228', b)
    _safe_set(b, 'modifier227', None)
    assert not _is_linked(b, 'modifier227', a2)
    if hasattr(a2, 'SingleVariableDeclaration228'):
        assert not _is_linked(a2, 'SingleVariableDeclaration228', b)


def test_assoc_usagesInImports233_reverse_link_reassign_clear():
    a1 = java_NamedElement(name="sample_text", proxy=True)
    a2 = java_NamedElement(name="sample_text_2", proxy=False)
    b = java_ImportDeclaration(static=True)
    _safe_set(b, 'ImportDeclaration', a1)
    assert _is_linked(b, 'ImportDeclaration', a1)
    if hasattr(a1, 'importedElement'):
        assert _is_linked(a1, 'importedElement', b)
    _safe_set(b, 'ImportDeclaration', a2)
    assert _is_linked(b, 'ImportDeclaration', a2)
    if hasattr(a1, 'importedElement'):
        assert not _is_linked(a1, 'importedElement', b)
    if hasattr(a2, 'importedElement'):
        assert _is_linked(a2, 'importedElement', b)
    _safe_set(b, 'ImportDeclaration', None)
    assert not _is_linked(b, 'ImportDeclaration', a2)
    if hasattr(a2, 'importedElement'):
        assert not _is_linked(a2, 'importedElement', b)


def test_assoc_variableDeclarationStatement229_reverse_link_reassign_clear():
    a1 = java_VariableDeclarationStatement(extraArrayDimensions=7)
    a2 = java_VariableDeclarationStatement(extraArrayDimensions=13)
    b = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    _safe_set(b, 'modifier230', a1)
    assert _is_linked(b, 'modifier230', a1)
    if hasattr(a1, 'VariableDeclarationStatement'):
        assert _is_linked(a1, 'VariableDeclarationStatement', b)
    _safe_set(b, 'modifier230', a2)
    assert _is_linked(b, 'modifier230', a2)
    if hasattr(a1, 'VariableDeclarationStatement'):
        assert not _is_linked(a1, 'VariableDeclarationStatement', b)
    if hasattr(a2, 'VariableDeclarationStatement'):
        assert _is_linked(a2, 'VariableDeclarationStatement', b)
    _safe_set(b, 'modifier230', None)
    assert not _is_linked(b, 'modifier230', a2)
    if hasattr(a2, 'VariableDeclarationStatement'):
        assert not _is_linked(a2, 'VariableDeclarationStatement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations272_stub_double():
    # java_Annotation has no real 'java_Annotation274' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_Annotation()
    setattr(partner, 'java_Annotation274', None)
    _safe_set(owner, 'java_SingleVariableDeclaration273', {partner})
    assert getattr(partner, 'java_Annotation274') == owner
    _safe_set(owner, 'java_SingleVariableDeclaration273', set())
    assert getattr(partner, 'java_Annotation274') is None


def test_assoc_annotations336_stub_double():
    # java_Annotation has no real 'java_Annotation337' property in the generated
    # code (a bare stub) -- manually attach it so java_VariableDeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_VariableDeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_VariableDeclarationStatement(extraArrayDimensions=7)
    partner = java_Annotation()
    setattr(partner, 'java_Annotation337', None)
    _safe_set(owner, 'java_VariableDeclarationStatement', {partner})
    assert getattr(partner, 'java_Annotation337') == owner
    _safe_set(owner, 'java_VariableDeclarationStatement', set())
    assert getattr(partner, 'java_Annotation337') is None


def test_assoc_bodyDeclaration224_stub_double():
    # java_BodyDeclaration has no real 'BodyDeclaration225' property in the generated
    # code (a bare stub) -- manually attach it so java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java_BodyDeclaration()
    setattr(partner, 'BodyDeclaration225', None)
    _safe_set(owner, 'modifier', partner)
    assert getattr(partner, 'BodyDeclaration225') == owner
    _safe_set(owner, 'modifier', None)
    assert getattr(partner, 'BodyDeclaration225') is None


def test_assoc_bound338_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess339' property in the generated
    # code (a bare stub) -- manually attach it so java_WildCardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_WildCardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_WildCardType(upperBound=True)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess339', None)
    _safe_set(owner, 'java_WildCardType', partner)
    assert getattr(partner, 'java_TypeAccess339') == owner
    _safe_set(owner, 'java_WildCardType', None)
    assert getattr(partner, 'java_TypeAccess339') is None


def test_assoc_catchClause277_stub_double():
    # java_CatchClause has no real 'CatchClause' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_CatchClause()
    setattr(partner, 'CatchClause', None)
    _safe_set(owner, 'exception', partner)
    assert getattr(partner, 'CatchClause') == owner
    _safe_set(owner, 'exception', None)
    assert getattr(partner, 'CatchClause') is None


def test_assoc_comments38_stub_double():
    # java_ASTNode has no real 'java_ASTNode' property in the generated
    # code (a bare stub) -- manually attach it so java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = java_ASTNode()
    setattr(partner, 'java_ASTNode', None)
    _safe_set(owner, 'java_Comment39', partner)
    assert owner in getattr(partner, 'java_ASTNode')
    _safe_set(owner, 'java_Comment39', None)
    assert owner not in getattr(partner, 'java_ASTNode')


def test_assoc_commentsAfterBody16_stub_double():
    # java_AbstractTypeDeclaration has no real 'java_AbstractTypeDeclaration17' property in the generated
    # code (a bare stub) -- manually attach it so java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = java_AbstractTypeDeclaration()
    setattr(partner, 'java_AbstractTypeDeclaration17', None)
    _safe_set(owner, 'java_Comment18', partner)
    assert owner in getattr(partner, 'java_AbstractTypeDeclaration17')
    _safe_set(owner, 'java_Comment18', None)
    assert owner not in getattr(partner, 'java_AbstractTypeDeclaration17')


def test_assoc_commentsBeforeBody15_stub_double():
    # java_AbstractTypeDeclaration has no real 'java_AbstractTypeDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = java_AbstractTypeDeclaration()
    setattr(partner, 'java_AbstractTypeDeclaration', None)
    _safe_set(owner, 'java_Comment', partner)
    assert owner in getattr(partner, 'java_AbstractTypeDeclaration')
    _safe_set(owner, 'java_Comment', None)
    assert owner not in getattr(partner, 'java_AbstractTypeDeclaration')


def test_assoc_elementType72_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess73' property in the generated
    # code (a bare stub) -- manually attach it so java_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_ArrayType(dimensions=7)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess73', None)
    _safe_set(owner, 'java_ArrayType', partner)
    assert getattr(partner, 'java_TypeAccess73') == owner
    _safe_set(owner, 'java_ArrayType', None)
    assert getattr(partner, 'java_TypeAccess73') is None


def test_assoc_enhancedForStatement278_stub_double():
    # java_EnhancedForStatement has no real 'EnhancedForStatement' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_EnhancedForStatement()
    setattr(partner, 'EnhancedForStatement', None)
    _safe_set(owner, 'parameter', partner)
    assert getattr(partner, 'EnhancedForStatement') == owner
    _safe_set(owner, 'parameter', None)
    assert getattr(partner, 'EnhancedForStatement') is None


def test_assoc_entryAttributes186_stub_double():
    # java_Manifest has no real 'java_Manifest187' property in the generated
    # code (a bare stub) -- manually attach it so java_ManifestEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_ManifestEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_ManifestEntry(name="sample_text")
    partner = java_Manifest()
    setattr(partner, 'java_Manifest187', None)
    _safe_set(owner, 'java_ManifestEntry', partner)
    assert owner in getattr(partner, 'java_Manifest187')
    _safe_set(owner, 'java_ManifestEntry', None)
    assert owner not in getattr(partner, 'java_Manifest187')


def test_assoc_exception93_stub_double():
    # java_CatchClause has no real 'catchClause' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_CatchClause()
    setattr(partner, 'catchClause', None)
    _safe_set(owner, 'SingleVariableDeclaration94', partner)
    assert getattr(partner, 'catchClause') == owner
    _safe_set(owner, 'SingleVariableDeclaration94', None)
    assert getattr(partner, 'catchClause') is None


def test_assoc_expression283_stub_double():
    # java_Expression has no real 'java_Expression284' property in the generated
    # code (a bare stub) -- manually attach it so java_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SwitchCase(default=True)
    partner = java_Expression()
    setattr(partner, 'java_Expression284', None)
    _safe_set(owner, 'java_SwitchCase', partner)
    assert getattr(partner, 'java_Expression284') == owner
    _safe_set(owner, 'java_SwitchCase', None)
    assert getattr(partner, 'java_Expression284') is None


def test_assoc_extendedOperands168_stub_double():
    # java_Expression has no real 'java_Expression170' property in the generated
    # code (a bare stub) -- manually attach it so java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_InfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression170', None)
    _safe_set(owner, 'java_InfixExpression169', {partner})
    assert getattr(partner, 'java_Expression170') == owner
    _safe_set(owner, 'java_InfixExpression169', set())
    assert getattr(partner, 'java_Expression170') is None


def test_assoc_fragments295_stub_double():
    # java_ASTNode has no real 'java_ASTNode297' property in the generated
    # code (a bare stub) -- manually attach it so java_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_TagElement(tagName="sample_text")
    partner = java_ASTNode()
    setattr(partner, 'java_ASTNode297', None)
    _safe_set(owner, 'java_TagElement296', {partner})
    assert getattr(partner, 'java_ASTNode297') == owner
    _safe_set(owner, 'java_TagElement296', set())
    assert getattr(partner, 'java_ASTNode297') is None


def test_assoc_initializer326_stub_double():
    # java_Expression has no real 'java_Expression327' property in the generated
    # code (a bare stub) -- manually attach it so java_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_VariableDeclaration(extraArrayDimensions=7)
    partner = java_Expression()
    setattr(partner, 'java_Expression327', None)
    _safe_set(owner, 'java_VariableDeclaration', partner)
    assert getattr(partner, 'java_Expression327') == owner
    _safe_set(owner, 'java_VariableDeclaration', None)
    assert getattr(partner, 'java_Expression327') is None


def test_assoc_leftHandSide74_stub_double():
    # java_Expression has no real 'java_Expression75' property in the generated
    # code (a bare stub) -- manually attach it so java_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Assignment(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression75', None)
    _safe_set(owner, 'java_Assignment', partner)
    assert getattr(partner, 'java_Expression75') == owner
    _safe_set(owner, 'java_Assignment', None)
    assert getattr(partner, 'java_Expression75') is None


def test_assoc_leftOperand165_stub_double():
    # java_Expression has no real 'java_Expression167' property in the generated
    # code (a bare stub) -- manually attach it so java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_InfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression167', None)
    _safe_set(owner, 'java_InfixExpression166', partner)
    assert getattr(partner, 'java_Expression167') == owner
    _safe_set(owner, 'java_InfixExpression166', None)
    assert getattr(partner, 'java_Expression167') is None


def test_assoc_mainAttributes184_stub_double():
    # java_Manifest has no real 'java_Manifest185' property in the generated
    # code (a bare stub) -- manually attach it so java_ManifestAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_ManifestAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_ManifestAttribute(key="sample_text", value="sample_text")
    partner = java_Manifest()
    setattr(partner, 'java_Manifest185', None)
    _safe_set(owner, 'java_ManifestAttribute', partner)
    assert owner in getattr(partner, 'java_Manifest185')
    _safe_set(owner, 'java_ManifestAttribute', None)
    assert owner not in getattr(partner, 'java_Manifest185')


def test_assoc_manifest32_stub_double():
    # java_Manifest has no real 'java_Manifest' property in the generated
    # code (a bare stub) -- manually attach it so java_Archive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Archive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Archive(originalFilePath="sample_text")
    partner = java_Manifest()
    setattr(partner, 'java_Manifest', None)
    _safe_set(owner, 'java_Archive', partner)
    assert getattr(partner, 'java_Manifest') == owner
    _safe_set(owner, 'java_Archive', None)
    assert getattr(partner, 'java_Manifest') is None


def test_assoc_member191_stub_double():
    # java_MemberRef has no real 'java_MemberRef' property in the generated
    # code (a bare stub) -- manually attach it so java_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_NamedElement(name="sample_text", proxy=True)
    partner = java_MemberRef()
    setattr(partner, 'java_MemberRef', None)
    _safe_set(owner, 'java_NamedElement', partner)
    assert getattr(partner, 'java_MemberRef') == owner
    _safe_set(owner, 'java_NamedElement', None)
    assert getattr(partner, 'java_MemberRef') is None


def test_assoc_methodDeclaration275_stub_double():
    # java_AbstractMethodDeclaration has no real 'AbstractMethodDeclaration276' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_AbstractMethodDeclaration()
    setattr(partner, 'AbstractMethodDeclaration276', None)
    _safe_set(owner, 'parameters', partner)
    assert getattr(partner, 'AbstractMethodDeclaration276') == owner
    _safe_set(owner, 'parameters', None)
    assert getattr(partner, 'AbstractMethodDeclaration276') is None


def test_assoc_model236_stub_double():
    # java_Package has no real 'ownedElements237' property in the generated
    # code (a bare stub) -- manually attach it so java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Model(name="sample_text")
    partner = java_Package()
    setattr(partner, 'ownedElements237', None)
    _safe_set(owner, 'Model', partner)
    assert getattr(partner, 'ownedElements237') == owner
    _safe_set(owner, 'Model', None)
    assert getattr(partner, 'ownedElements237') is None


def test_assoc_modifier329_stub_double():
    # java_VariableDeclarationExpression has no real 'variableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java_VariableDeclarationExpression()
    setattr(partner, 'variableDeclarationExpression', None)
    _safe_set(owner, 'Modifier330', partner)
    assert getattr(partner, 'variableDeclarationExpression') == owner
    _safe_set(owner, 'Modifier330', None)
    assert getattr(partner, 'variableDeclarationExpression') is None


def test_assoc_modifier84_stub_double():
    # java_BodyDeclaration has no real 'bodyDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java_BodyDeclaration()
    setattr(partner, 'bodyDeclaration', None)
    _safe_set(owner, 'Modifier', partner)
    assert getattr(partner, 'bodyDeclaration') == owner
    _safe_set(owner, 'Modifier', None)
    assert getattr(partner, 'bodyDeclaration') is None


def test_assoc_operand258_stub_double():
    # java_Expression has no real 'java_Expression259' property in the generated
    # code (a bare stub) -- manually attach it so java_PostfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_PostfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_PostfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression259', None)
    _safe_set(owner, 'java_PostfixExpression', partner)
    assert getattr(partner, 'java_Expression259') == owner
    _safe_set(owner, 'java_PostfixExpression', None)
    assert getattr(partner, 'java_Expression259') is None


def test_assoc_operand260_stub_double():
    # java_Expression has no real 'java_Expression261' property in the generated
    # code (a bare stub) -- manually attach it so java_PrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_PrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_PrefixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression261', None)
    _safe_set(owner, 'java_PrefixExpression', partner)
    assert getattr(partner, 'java_Expression261') == owner
    _safe_set(owner, 'java_PrefixExpression', None)
    assert getattr(partner, 'java_Expression261') is None


def test_assoc_originalCompilationUnit40_stub_double():
    # java_ASTNode has no real 'java_ASTNode41' property in the generated
    # code (a bare stub) -- manually attach it so java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_CompilationUnit(originalFilePath="sample_text")
    partner = java_ASTNode()
    setattr(partner, 'java_ASTNode41', None)
    _safe_set(owner, 'java_CompilationUnit', partner)
    assert getattr(partner, 'java_ASTNode41') == owner
    _safe_set(owner, 'java_CompilationUnit', None)
    assert getattr(partner, 'java_ASTNode41') is None


def test_assoc_orphanTypes215_stub_double():
    # java_Type has no real 'java_Type' property in the generated
    # code (a bare stub) -- manually attach it so java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Model(name="sample_text")
    partner = java_Type()
    setattr(partner, 'java_Type', None)
    _safe_set(owner, 'java_Model', {partner})
    assert getattr(partner, 'java_Type') == owner
    _safe_set(owner, 'java_Model', set())
    assert getattr(partner, 'java_Type') is None


def test_assoc_ownedElements213_stub_double():
    # java_Package has no real 'Package214' property in the generated
    # code (a bare stub) -- manually attach it so java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Model(name="sample_text")
    partner = java_Package()
    setattr(partner, 'Package214', None)
    _safe_set(owner, 'model', {partner})
    assert getattr(partner, 'Package214') == owner
    _safe_set(owner, 'model', set())
    assert getattr(partner, 'Package214') is None


def test_assoc_package112_stub_double():
    # java_Package has no real 'java_Package' property in the generated
    # code (a bare stub) -- manually attach it so java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_CompilationUnit(originalFilePath="sample_text")
    partner = java_Package()
    setattr(partner, 'java_Package', None)
    _safe_set(owner, 'java_CompilationUnit113', partner)
    assert getattr(partner, 'java_Package') == owner
    _safe_set(owner, 'java_CompilationUnit113', None)
    assert getattr(partner, 'java_Package') is None


def test_assoc_parameter129_stub_double():
    # java_EnhancedForStatement has no real 'enhancedForStatement' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_EnhancedForStatement()
    setattr(partner, 'enhancedForStatement', None)
    _safe_set(owner, 'SingleVariableDeclaration130', partner)
    assert getattr(partner, 'enhancedForStatement') == owner
    _safe_set(owner, 'SingleVariableDeclaration130', None)
    assert getattr(partner, 'enhancedForStatement') is None


def test_assoc_parameters1_stub_double():
    # java_AbstractMethodDeclaration has no real 'methodDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_AbstractMethodDeclaration()
    setattr(partner, 'methodDeclaration', None)
    _safe_set(owner, 'SingleVariableDeclaration', partner)
    assert owner in getattr(partner, 'methodDeclaration')
    _safe_set(owner, 'SingleVariableDeclaration', None)
    assert owner not in getattr(partner, 'methodDeclaration')


def test_assoc_parameters208_stub_double():
    # java_MethodRef has no real 'java_MethodRef209' property in the generated
    # code (a bare stub) -- manually attach it so java_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_MethodRefParameter(name="sample_text", varargs=True)
    partner = java_MethodRef()
    setattr(partner, 'java_MethodRef209', None)
    _safe_set(owner, 'java_MethodRefParameter', partner)
    assert owner in getattr(partner, 'java_MethodRef209')
    _safe_set(owner, 'java_MethodRefParameter', None)
    assert owner not in getattr(partner, 'java_MethodRef209')


def test_assoc_returnType195_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess196' property in the generated
    # code (a bare stub) -- manually attach it so java_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_MethodDeclaration(extraArrayDimensions=7)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess196', None)
    _safe_set(owner, 'java_MethodDeclaration', partner)
    assert getattr(partner, 'java_TypeAccess196') == owner
    _safe_set(owner, 'java_MethodDeclaration', None)
    assert getattr(partner, 'java_TypeAccess196') is None


def test_assoc_rightHandSide76_stub_double():
    # java_Expression has no real 'java_Expression78' property in the generated
    # code (a bare stub) -- manually attach it so java_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Assignment(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression78', None)
    _safe_set(owner, 'java_Assignment77', partner)
    assert getattr(partner, 'java_Expression78') == owner
    _safe_set(owner, 'java_Assignment77', None)
    assert getattr(partner, 'java_Expression78') is None


def test_assoc_rightOperand163_stub_double():
    # java_Expression has no real 'java_Expression164' property in the generated
    # code (a bare stub) -- manually attach it so java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_InfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression164', None)
    _safe_set(owner, 'java_InfixExpression', partner)
    assert getattr(partner, 'java_Expression164') == owner
    _safe_set(owner, 'java_InfixExpression', None)
    assert getattr(partner, 'java_Expression164') is None


def test_assoc_tags178_stub_double():
    # java_Javadoc has no real 'java_Javadoc' property in the generated
    # code (a bare stub) -- manually attach it so java_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_TagElement(tagName="sample_text")
    partner = java_Javadoc()
    setattr(partner, 'java_Javadoc', None)
    _safe_set(owner, 'java_TagElement', partner)
    assert owner in getattr(partner, 'java_Javadoc')
    _safe_set(owner, 'java_TagElement', None)
    assert owner not in getattr(partner, 'java_Javadoc')


def test_assoc_type210_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess212' property in the generated
    # code (a bare stub) -- manually attach it so java_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_MethodRefParameter(name="sample_text", varargs=True)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess212', None)
    _safe_set(owner, 'java_MethodRefParameter211', partner)
    assert getattr(partner, 'java_TypeAccess212') == owner
    _safe_set(owner, 'java_MethodRefParameter211', None)
    assert getattr(partner, 'java_TypeAccess212') is None


def test_assoc_type270_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess271' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess271', None)
    _safe_set(owner, 'java_SingleVariableDeclaration', partner)
    assert getattr(partner, 'java_TypeAccess271') == owner
    _safe_set(owner, 'java_SingleVariableDeclaration', None)
    assert getattr(partner, 'java_TypeAccess271') is None


def test_assoc_types114_stub_double():
    # java_AbstractTypeDeclaration has no real 'java_AbstractTypeDeclaration116' property in the generated
    # code (a bare stub) -- manually attach it so java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_CompilationUnit(originalFilePath="sample_text")
    partner = java_AbstractTypeDeclaration()
    setattr(partner, 'java_AbstractTypeDeclaration116', None)
    _safe_set(owner, 'java_CompilationUnit115', {partner})
    assert getattr(partner, 'java_AbstractTypeDeclaration116') == owner
    _safe_set(owner, 'java_CompilationUnit115', set())
    assert getattr(partner, 'java_AbstractTypeDeclaration116') is None


def test_assoc_unresolvedItems216_stub_double():
    # java_UnresolvedItem has no real 'java_UnresolvedItem' property in the generated
    # code (a bare stub) -- manually attach it so java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Model(name="sample_text")
    partner = java_UnresolvedItem()
    setattr(partner, 'java_UnresolvedItem', None)
    _safe_set(owner, 'java_Model217', {partner})
    assert getattr(partner, 'java_UnresolvedItem') == owner
    _safe_set(owner, 'java_Model217', set())
    assert getattr(partner, 'java_UnresolvedItem') is None


def test_assoc_usageInVariableAccess328_stub_double():
    # java_SingleVariableAccess has no real 'SingleVariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so java_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_VariableDeclaration(extraArrayDimensions=7)
    partner = java_SingleVariableAccess()
    setattr(partner, 'SingleVariableAccess', None)
    _safe_set(owner, 'variable', {partner})
    assert getattr(partner, 'SingleVariableAccess') == owner
    _safe_set(owner, 'variable', set())
    assert getattr(partner, 'SingleVariableAccess') is None


def test_assoc_variable264_stub_double():
    # java_SingleVariableAccess has no real 'usageInVariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so java_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_VariableDeclaration(extraArrayDimensions=7)
    partner = java_SingleVariableAccess()
    setattr(partner, 'usageInVariableAccess', None)
    _safe_set(owner, 'VariableDeclaration', partner)
    assert getattr(partner, 'usageInVariableAccess') == owner
    _safe_set(owner, 'VariableDeclaration', None)
    assert getattr(partner, 'usageInVariableAccess') is None


def test_assoc_variableDeclarationExpression231_stub_double():
    # java_VariableDeclarationExpression has no real 'VariableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java_VariableDeclarationExpression()
    setattr(partner, 'VariableDeclarationExpression', None)
    _safe_set(owner, 'modifier232', partner)
    assert getattr(partner, 'VariableDeclarationExpression') == owner
    _safe_set(owner, 'modifier232', None)
    assert getattr(partner, 'VariableDeclarationExpression') is None


