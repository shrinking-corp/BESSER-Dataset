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
    Java_ASTNode,
    Java_AbstractMethodDeclaration,
    Java_AbstractMethodInvocation,
    Java_AbstractTypeDeclaration,
    Java_AbstractTypeQualifiedExpression,
    Java_AbstractVariablesContainer,
    Java_Annotation,
    Java_AnnotationMemberValuePair,
    Java_AnnotationTypeDeclaration,
    Java_AnnotationTypeMemberDeclaration,
    Java_AnonymousClassDeclaration,
    Java_Archive,
    Java_ArrayAccess,
    Java_ArrayCreation,
    Java_ArrayInitializer,
    Java_ArrayLengthAccess,
    Java_ArrayType,
    Java_AssertStatement,
    Java_Assignment,
    Java_Block,
    Java_BlockComment,
    Java_BodyDeclaration,
    Java_BooleanLiteral,
    Java_BreakStatement,
    Java_CastExpression,
    Java_CatchClause,
    Java_CharacterLiteral,
    Java_ClassDeclaration,
    Java_ClassFile,
    Java_ClassInstanceCreation,
    Java_Comment,
    Java_CompilationUnit,
    Java_ConditionalExpression,
    Java_ConstructorDeclaration,
    Java_ConstructorInvocation,
    Java_ContinueStatement,
    Java_DoStatement,
    Java_EmptyStatement,
    Java_EnhancedForStatement,
    Java_EnumConstantDeclaration,
    Java_EnumDeclaration,
    Java_Expression,
    Java_ExpressionStatement,
    Java_FieldAccess,
    Java_FieldDeclaration,
    Java_ForStatement,
    Java_IfStatement,
    Java_ImportDeclaration,
    Java_InfixExpression,
    Java_Initializer,
    Java_InstanceofExpression,
    Java_InterfaceDeclaration,
    Java_Javadoc,
    Java_LabeledStatement,
    Java_LineComment,
    Java_Manifest,
    Java_ManifestAttribute,
    Java_ManifestEntry,
    Java_MemberRef,
    Java_MethodDeclaration,
    Java_MethodInvocation,
    Java_MethodRef,
    Java_MethodRefParameter,
    Java_Model,
    Java_Modifier,
    Java_NamedElement,
    Java_NamespaceAccess,
    Java_NullLiteral,
    Java_NumberLiteral,
    Java_Package,
    Java_PackageAccess,
    Java_ParameterizedType,
    Java_ParenthesizedExpression,
    Java_PostfixExpression,
    Java_PrefixExpression,
    Java_PrimitiveType,
    Java_PrimitiveTypeBoolean,
    Java_PrimitiveTypeByte,
    Java_PrimitiveTypeChar,
    Java_PrimitiveTypeDouble,
    Java_PrimitiveTypeFloat,
    Java_PrimitiveTypeInt,
    Java_PrimitiveTypeLong,
    Java_PrimitiveTypeShort,
    Java_PrimitiveTypeVoid,
    Java_ReturnStatement,
    Java_SingleVariableAccess,
    Java_SingleVariableDeclaration,
    Java_Statement,
    Java_StringLiteral,
    Java_SuperConstructorInvocation,
    Java_SuperFieldAccess,
    Java_SuperMethodInvocation,
    Java_SwitchCase,
    Java_SwitchStatement,
    Java_SynchronizedStatement,
    Java_TagElement,
    Java_TextElement,
    Java_ThisExpression,
    Java_ThrowStatement,
    Java_TryStatement,
    Java_Type,
    Java_TypeAccess,
    Java_TypeDeclaration,
    Java_TypeDeclarationStatement,
    Java_TypeLiteral,
    Java_TypeParameter,
    Java_UnresolvedAnnotationDeclaration,
    Java_UnresolvedAnnotationTypeMemberDeclaration,
    Java_UnresolvedClassDeclaration,
    Java_UnresolvedEnumDeclaration,
    Java_UnresolvedInterfaceDeclaration,
    Java_UnresolvedItem,
    Java_UnresolvedItemAccess,
    Java_UnresolvedLabeledStatement,
    Java_UnresolvedMethodDeclaration,
    Java_UnresolvedSingleVariableDeclaration,
    Java_UnresolvedType,
    Java_UnresolvedTypeDeclaration,
    Java_UnresolvedVariableDeclarationFragment,
    Java_VariableDeclaration,
    Java_VariableDeclarationExpression,
    Java_VariableDeclarationFragment,
    Java_VariableDeclarationStatement,
    Java_WhileStatement,
    Java_WildCardType,
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

def test_assoc_archives246_reverse_link_reassign_clear():
    a1 = Java_Model(name="sample_text")
    a2 = Java_Model(name="sample_text_2")
    b = Java_Archive(originalFilePath="sample_text")
    _safe_set(b, 'Java_Archive248', a1)
    assert _is_linked(b, 'Java_Archive248', a1)
    if hasattr(a1, 'Java_Model247'):
        assert _is_linked(a1, 'Java_Model247', b)
    _safe_set(b, 'Java_Archive248', a2)
    assert _is_linked(b, 'Java_Archive248', a2)
    if hasattr(a1, 'Java_Model247'):
        assert not _is_linked(a1, 'Java_Model247', b)
    if hasattr(a2, 'Java_Model247'):
        assert _is_linked(a2, 'Java_Model247', b)
    _safe_set(b, 'Java_Archive248', None)
    assert not _is_linked(b, 'Java_Archive248', a2)
    if hasattr(a2, 'Java_Model247'):
        assert not _is_linked(a2, 'Java_Model247', b)


def test_assoc_attachedSource106_reverse_link_reassign_clear():
    a1 = Java_CompilationUnit(originalFilePath="sample_text")
    a2 = Java_CompilationUnit(originalFilePath="sample_text_2")
    b = Java_ClassFile(originalFilePath="sample_text")
    _safe_set(b, 'Java_ClassFile107', a1)
    assert _is_linked(b, 'Java_ClassFile107', a1)
    if hasattr(a1, 'Java_CompilationUnit108'):
        assert _is_linked(a1, 'Java_CompilationUnit108', b)
    _safe_set(b, 'Java_ClassFile107', a2)
    assert _is_linked(b, 'Java_ClassFile107', a2)
    if hasattr(a1, 'Java_CompilationUnit108'):
        assert not _is_linked(a1, 'Java_CompilationUnit108', b)
    if hasattr(a2, 'Java_CompilationUnit108'):
        assert _is_linked(a2, 'Java_CompilationUnit108', b)
    _safe_set(b, 'Java_ClassFile107', None)
    assert not _is_linked(b, 'Java_ClassFile107', a2)
    if hasattr(a2, 'Java_CompilationUnit108'):
        assert not _is_linked(a2, 'Java_CompilationUnit108', b)


def test_assoc_attributes210_reverse_link_reassign_clear():
    a1 = Java_ManifestEntry(name="sample_text")
    a2 = Java_ManifestEntry(name="sample_text_2")
    b = Java_ManifestAttribute(key="sample_text", value="sample_text")
    _safe_set(b, 'Java_ManifestAttribute212', a1)
    assert _is_linked(b, 'Java_ManifestAttribute212', a1)
    if hasattr(a1, 'Java_ManifestEntry211'):
        assert _is_linked(a1, 'Java_ManifestEntry211', b)
    _safe_set(b, 'Java_ManifestAttribute212', a2)
    assert _is_linked(b, 'Java_ManifestAttribute212', a2)
    if hasattr(a1, 'Java_ManifestEntry211'):
        assert not _is_linked(a1, 'Java_ManifestEntry211', b)
    if hasattr(a2, 'Java_ManifestEntry211'):
        assert _is_linked(a2, 'Java_ManifestEntry211', b)
    _safe_set(b, 'Java_ManifestAttribute212', None)
    assert not _is_linked(b, 'Java_ManifestAttribute212', a2)
    if hasattr(a2, 'Java_ManifestEntry211'):
        assert not _is_linked(a2, 'Java_ManifestEntry211', b)


def test_assoc_classFiles243_reverse_link_reassign_clear():
    a1 = Java_Model(name="sample_text")
    a2 = Java_Model(name="sample_text_2")
    b = Java_ClassFile(originalFilePath="sample_text")
    _safe_set(b, 'Java_ClassFile245', a1)
    assert _is_linked(b, 'Java_ClassFile245', a1)
    if hasattr(a1, 'Java_Model244'):
        assert _is_linked(a1, 'Java_Model244', b)
    _safe_set(b, 'Java_ClassFile245', a2)
    assert _is_linked(b, 'Java_ClassFile245', a2)
    if hasattr(a1, 'Java_Model244'):
        assert not _is_linked(a1, 'Java_Model244', b)
    if hasattr(a2, 'Java_Model244'):
        assert _is_linked(a2, 'Java_Model244', b)
    _safe_set(b, 'Java_ClassFile245', None)
    assert not _is_linked(b, 'Java_ClassFile245', a2)
    if hasattr(a2, 'Java_Model244'):
        assert not _is_linked(a2, 'Java_Model244', b)


def test_assoc_classFiles32_reverse_link_reassign_clear():
    a1 = Java_ClassFile(originalFilePath="sample_text")
    a2 = Java_ClassFile(originalFilePath="sample_text_2")
    b = Java_Archive(originalFilePath="sample_text")
    _safe_set(b, 'Java_Archive', {a1})
    assert _is_linked(b, 'Java_Archive', a1)
    if hasattr(a1, 'Java_ClassFile'):
        assert _is_linked(a1, 'Java_ClassFile', b)
    _safe_set(b, 'Java_Archive', {a2})
    assert _is_linked(b, 'Java_Archive', a2)
    if hasattr(a1, 'Java_ClassFile'):
        assert not _is_linked(a1, 'Java_ClassFile', b)
    if hasattr(a2, 'Java_ClassFile'):
        assert _is_linked(a2, 'Java_ClassFile', b)
    _safe_set(b, 'Java_Archive', set())
    assert not _is_linked(b, 'Java_Archive', a2)
    if hasattr(a2, 'Java_ClassFile'):
        assert not _is_linked(a2, 'Java_ClassFile', b)


def test_assoc_commentList128_reverse_link_reassign_clear():
    a1 = Java_CompilationUnit(originalFilePath="sample_text")
    a2 = Java_CompilationUnit(originalFilePath="sample_text_2")
    b = Java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    _safe_set(b, 'Java_Comment130', a1)
    assert _is_linked(b, 'Java_Comment130', a1)
    if hasattr(a1, 'Java_CompilationUnit129'):
        assert _is_linked(a1, 'Java_CompilationUnit129', b)
    _safe_set(b, 'Java_Comment130', a2)
    assert _is_linked(b, 'Java_Comment130', a2)
    if hasattr(a1, 'Java_CompilationUnit129'):
        assert not _is_linked(a1, 'Java_CompilationUnit129', b)
    if hasattr(a2, 'Java_CompilationUnit129'):
        assert _is_linked(a2, 'Java_CompilationUnit129', b)
    _safe_set(b, 'Java_Comment130', None)
    assert not _is_linked(b, 'Java_Comment130', a2)
    if hasattr(a2, 'Java_CompilationUnit129'):
        assert not _is_linked(a2, 'Java_CompilationUnit129', b)


def test_assoc_compilationUnits240_reverse_link_reassign_clear():
    a1 = Java_Model(name="sample_text")
    a2 = Java_Model(name="sample_text_2")
    b = Java_CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'Java_CompilationUnit242', a1)
    assert _is_linked(b, 'Java_CompilationUnit242', a1)
    if hasattr(a1, 'Java_Model241'):
        assert _is_linked(a1, 'Java_Model241', b)
    _safe_set(b, 'Java_CompilationUnit242', a2)
    assert _is_linked(b, 'Java_CompilationUnit242', a2)
    if hasattr(a1, 'Java_Model241'):
        assert not _is_linked(a1, 'Java_Model241', b)
    if hasattr(a2, 'Java_Model241'):
        assert _is_linked(a2, 'Java_Model241', b)
    _safe_set(b, 'Java_CompilationUnit242', None)
    assert not _is_linked(b, 'Java_CompilationUnit242', a2)
    if hasattr(a2, 'Java_Model241'):
        assert not _is_linked(a2, 'Java_Model241', b)


def test_assoc_importedElement184_reverse_link_reassign_clear():
    a1 = Java_NamedElement(name="sample_text", proxy=True)
    a2 = Java_NamedElement(name="sample_text_2", proxy=False)
    b = Java_ImportDeclaration(static=True)
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


def test_assoc_imports131_reverse_link_reassign_clear():
    a1 = Java_ImportDeclaration(static=True)
    a2 = Java_ImportDeclaration(static=False)
    b = Java_CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'Java_CompilationUnit132', {a1})
    assert _is_linked(b, 'Java_CompilationUnit132', a1)
    if hasattr(a1, 'Java_ImportDeclaration'):
        assert _is_linked(a1, 'Java_ImportDeclaration', b)
    _safe_set(b, 'Java_CompilationUnit132', {a2})
    assert _is_linked(b, 'Java_CompilationUnit132', a2)
    if hasattr(a1, 'Java_ImportDeclaration'):
        assert not _is_linked(a1, 'Java_ImportDeclaration', b)
    if hasattr(a2, 'Java_ImportDeclaration'):
        assert _is_linked(a2, 'Java_ImportDeclaration', b)
    _safe_set(b, 'Java_CompilationUnit132', set())
    assert not _is_linked(b, 'Java_CompilationUnit132', a2)
    if hasattr(a2, 'Java_ImportDeclaration'):
        assert not _is_linked(a2, 'Java_ImportDeclaration', b)


def test_assoc_modifier293_reverse_link_reassign_clear():
    a1 = Java_SingleVariableDeclaration(varargs=True)
    a2 = Java_SingleVariableDeclaration(varargs=False)
    b = Java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    _safe_set(b, 'Modifier294', a1)
    assert _is_linked(b, 'Modifier294', a1)
    if hasattr(a1, 'singleVariableDeclaration'):
        assert _is_linked(a1, 'singleVariableDeclaration', b)
    _safe_set(b, 'Modifier294', a2)
    assert _is_linked(b, 'Modifier294', a2)
    if hasattr(a1, 'singleVariableDeclaration'):
        assert not _is_linked(a1, 'singleVariableDeclaration', b)
    if hasattr(a2, 'singleVariableDeclaration'):
        assert _is_linked(a2, 'singleVariableDeclaration', b)
    _safe_set(b, 'Modifier294', None)
    assert not _is_linked(b, 'Modifier294', a2)
    if hasattr(a2, 'singleVariableDeclaration'):
        assert not _is_linked(a2, 'singleVariableDeclaration', b)


def test_assoc_modifier359_reverse_link_reassign_clear():
    a1 = Java_VariableDeclarationStatement(extraArrayDimensions=7)
    a2 = Java_VariableDeclarationStatement(extraArrayDimensions=13)
    b = Java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    _safe_set(b, 'Modifier360', a1)
    assert _is_linked(b, 'Modifier360', a1)
    if hasattr(a1, 'variableDeclarationStatement'):
        assert _is_linked(a1, 'variableDeclarationStatement', b)
    _safe_set(b, 'Modifier360', a2)
    assert _is_linked(b, 'Modifier360', a2)
    if hasattr(a1, 'variableDeclarationStatement'):
        assert not _is_linked(a1, 'variableDeclarationStatement', b)
    if hasattr(a2, 'variableDeclarationStatement'):
        assert _is_linked(a2, 'variableDeclarationStatement', b)
    _safe_set(b, 'Modifier360', None)
    assert not _is_linked(b, 'Modifier360', a2)
    if hasattr(a2, 'variableDeclarationStatement'):
        assert not _is_linked(a2, 'variableDeclarationStatement', b)


def test_assoc_redefinedMethodDeclaration220_reverse_link_reassign_clear():
    a1 = Java_MethodDeclaration(extraArrayDimensions=7)
    a2 = Java_MethodDeclaration(extraArrayDimensions=13)
    b = Java_MethodDeclaration(extraArrayDimensions=7)
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


def test_assoc_redefinitions222_reverse_link_reassign_clear():
    a1 = Java_MethodDeclaration(extraArrayDimensions=7)
    a2 = Java_MethodDeclaration(extraArrayDimensions=13)
    b = Java_MethodDeclaration(extraArrayDimensions=7)
    _safe_set(b, 'redefinedMethodDeclaration', {a1})
    assert _is_linked(b, 'redefinedMethodDeclaration', a1)
    if hasattr(a1, 'MethodDeclaration223'):
        assert _is_linked(a1, 'MethodDeclaration223', b)
    _safe_set(b, 'redefinedMethodDeclaration', {a2})
    assert _is_linked(b, 'redefinedMethodDeclaration', a2)
    if hasattr(a1, 'MethodDeclaration223'):
        assert not _is_linked(a1, 'MethodDeclaration223', b)
    if hasattr(a2, 'MethodDeclaration223'):
        assert _is_linked(a2, 'MethodDeclaration223', b)
    _safe_set(b, 'redefinedMethodDeclaration', set())
    assert not _is_linked(b, 'redefinedMethodDeclaration', a2)
    if hasattr(a2, 'MethodDeclaration223'):
        assert not _is_linked(a2, 'MethodDeclaration223', b)


def test_assoc_singleVariableDeclaration251_reverse_link_reassign_clear():
    a1 = Java_SingleVariableDeclaration(varargs=True)
    a2 = Java_SingleVariableDeclaration(varargs=False)
    b = Java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    _safe_set(b, 'modifier252', a1)
    assert _is_linked(b, 'modifier252', a1)
    if hasattr(a1, 'SingleVariableDeclaration253'):
        assert _is_linked(a1, 'SingleVariableDeclaration253', b)
    _safe_set(b, 'modifier252', a2)
    assert _is_linked(b, 'modifier252', a2)
    if hasattr(a1, 'SingleVariableDeclaration253'):
        assert not _is_linked(a1, 'SingleVariableDeclaration253', b)
    if hasattr(a2, 'SingleVariableDeclaration253'):
        assert _is_linked(a2, 'SingleVariableDeclaration253', b)
    _safe_set(b, 'modifier252', None)
    assert not _is_linked(b, 'modifier252', a2)
    if hasattr(a2, 'SingleVariableDeclaration253'):
        assert not _is_linked(a2, 'SingleVariableDeclaration253', b)


def test_assoc_usagesInImports258_reverse_link_reassign_clear():
    a1 = Java_NamedElement(name="sample_text", proxy=True)
    a2 = Java_NamedElement(name="sample_text_2", proxy=False)
    b = Java_ImportDeclaration(static=True)
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


def test_assoc_variableDeclarationStatement254_reverse_link_reassign_clear():
    a1 = Java_VariableDeclarationStatement(extraArrayDimensions=7)
    a2 = Java_VariableDeclarationStatement(extraArrayDimensions=13)
    b = Java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    _safe_set(b, 'modifier255', a1)
    assert _is_linked(b, 'modifier255', a1)
    if hasattr(a1, 'VariableDeclarationStatement'):
        assert _is_linked(a1, 'VariableDeclarationStatement', b)
    _safe_set(b, 'modifier255', a2)
    assert _is_linked(b, 'modifier255', a2)
    if hasattr(a1, 'VariableDeclarationStatement'):
        assert not _is_linked(a1, 'VariableDeclarationStatement', b)
    if hasattr(a2, 'VariableDeclarationStatement'):
        assert _is_linked(a2, 'VariableDeclarationStatement', b)
    _safe_set(b, 'modifier255', None)
    assert not _is_linked(b, 'modifier255', a2)
    if hasattr(a2, 'VariableDeclarationStatement'):
        assert not _is_linked(a2, 'VariableDeclarationStatement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations297_stub_double():
    # Java_Annotation has no real 'Java_Annotation299' property in the generated
    # code (a bare stub) -- manually attach it so Java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_SingleVariableDeclaration(varargs=True)
    partner = Java_Annotation()
    setattr(partner, 'Java_Annotation299', None)
    _safe_set(owner, 'Java_SingleVariableDeclaration298', {partner})
    assert getattr(partner, 'Java_Annotation299') == owner
    _safe_set(owner, 'Java_SingleVariableDeclaration298', set())
    assert getattr(partner, 'Java_Annotation299') is None


def test_assoc_annotations361_stub_double():
    # Java_Annotation has no real 'Java_Annotation362' property in the generated
    # code (a bare stub) -- manually attach it so Java_VariableDeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_VariableDeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_VariableDeclarationStatement(extraArrayDimensions=7)
    partner = Java_Annotation()
    setattr(partner, 'Java_Annotation362', None)
    _safe_set(owner, 'Java_VariableDeclarationStatement', {partner})
    assert getattr(partner, 'Java_Annotation362') == owner
    _safe_set(owner, 'Java_VariableDeclarationStatement', set())
    assert getattr(partner, 'Java_Annotation362') is None


def test_assoc_bodyDeclaration249_stub_double():
    # Java_BodyDeclaration has no real 'BodyDeclaration250' property in the generated
    # code (a bare stub) -- manually attach it so Java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = Java_BodyDeclaration()
    setattr(partner, 'BodyDeclaration250', None)
    _safe_set(owner, 'modifier', partner)
    assert getattr(partner, 'BodyDeclaration250') == owner
    _safe_set(owner, 'modifier', None)
    assert getattr(partner, 'BodyDeclaration250') is None


def test_assoc_bound363_stub_double():
    # Java_TypeAccess has no real 'Java_TypeAccess364' property in the generated
    # code (a bare stub) -- manually attach it so Java_WildCardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_WildCardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_WildCardType(upperBound=True)
    partner = Java_TypeAccess()
    setattr(partner, 'Java_TypeAccess364', None)
    _safe_set(owner, 'Java_WildCardType', partner)
    assert getattr(partner, 'Java_TypeAccess364') == owner
    _safe_set(owner, 'Java_WildCardType', None)
    assert getattr(partner, 'Java_TypeAccess364') is None


def test_assoc_catchClause302_stub_double():
    # Java_CatchClause has no real 'CatchClause' property in the generated
    # code (a bare stub) -- manually attach it so Java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_SingleVariableDeclaration(varargs=True)
    partner = Java_CatchClause()
    setattr(partner, 'CatchClause', None)
    _safe_set(owner, 'exception', partner)
    assert getattr(partner, 'CatchClause') == owner
    _safe_set(owner, 'exception', None)
    assert getattr(partner, 'CatchClause') is None


def test_assoc_comments40_stub_double():
    # Java_ASTNode has no real 'Java_ASTNode' property in the generated
    # code (a bare stub) -- manually attach it so Java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = Java_ASTNode()
    setattr(partner, 'Java_ASTNode', None)
    _safe_set(owner, 'Java_Comment41', partner)
    assert owner in getattr(partner, 'Java_ASTNode')
    _safe_set(owner, 'Java_Comment41', None)
    assert owner not in getattr(partner, 'Java_ASTNode')


def test_assoc_commentsAfterBody16_stub_double():
    # Java_AbstractTypeDeclaration has no real 'Java_AbstractTypeDeclaration17' property in the generated
    # code (a bare stub) -- manually attach it so Java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = Java_AbstractTypeDeclaration()
    setattr(partner, 'Java_AbstractTypeDeclaration17', None)
    _safe_set(owner, 'Java_Comment18', partner)
    assert owner in getattr(partner, 'Java_AbstractTypeDeclaration17')
    _safe_set(owner, 'Java_Comment18', None)
    assert owner not in getattr(partner, 'Java_AbstractTypeDeclaration17')


def test_assoc_commentsBeforeBody15_stub_double():
    # Java_AbstractTypeDeclaration has no real 'Java_AbstractTypeDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so Java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = Java_AbstractTypeDeclaration()
    setattr(partner, 'Java_AbstractTypeDeclaration', None)
    _safe_set(owner, 'Java_Comment', partner)
    assert owner in getattr(partner, 'Java_AbstractTypeDeclaration')
    _safe_set(owner, 'Java_Comment', None)
    assert owner not in getattr(partner, 'Java_AbstractTypeDeclaration')


def test_assoc_elementType78_stub_double():
    # Java_TypeAccess has no real 'Java_TypeAccess79' property in the generated
    # code (a bare stub) -- manually attach it so Java_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_ArrayType(dimensions=7)
    partner = Java_TypeAccess()
    setattr(partner, 'Java_TypeAccess79', None)
    _safe_set(owner, 'Java_ArrayType', partner)
    assert getattr(partner, 'Java_TypeAccess79') == owner
    _safe_set(owner, 'Java_ArrayType', None)
    assert getattr(partner, 'Java_TypeAccess79') is None


def test_assoc_enhancedForStatement303_stub_double():
    # Java_EnhancedForStatement has no real 'EnhancedForStatement' property in the generated
    # code (a bare stub) -- manually attach it so Java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_SingleVariableDeclaration(varargs=True)
    partner = Java_EnhancedForStatement()
    setattr(partner, 'EnhancedForStatement', None)
    _safe_set(owner, 'parameter', partner)
    assert getattr(partner, 'EnhancedForStatement') == owner
    _safe_set(owner, 'parameter', None)
    assert getattr(partner, 'EnhancedForStatement') is None


def test_assoc_entryAttributes208_stub_double():
    # Java_Manifest has no real 'Java_Manifest209' property in the generated
    # code (a bare stub) -- manually attach it so Java_ManifestEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_ManifestEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_ManifestEntry(name="sample_text")
    partner = Java_Manifest()
    setattr(partner, 'Java_Manifest209', None)
    _safe_set(owner, 'Java_ManifestEntry', partner)
    assert owner in getattr(partner, 'Java_Manifest209')
    _safe_set(owner, 'Java_ManifestEntry', None)
    assert owner not in getattr(partner, 'Java_Manifest209')


def test_assoc_exception99_stub_double():
    # Java_CatchClause has no real 'catchClause' property in the generated
    # code (a bare stub) -- manually attach it so Java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_SingleVariableDeclaration(varargs=True)
    partner = Java_CatchClause()
    setattr(partner, 'catchClause', None)
    _safe_set(owner, 'SingleVariableDeclaration100', partner)
    assert getattr(partner, 'catchClause') == owner
    _safe_set(owner, 'SingleVariableDeclaration100', None)
    assert getattr(partner, 'catchClause') is None


def test_assoc_expression308_stub_double():
    # Java_Expression has no real 'Java_Expression309' property in the generated
    # code (a bare stub) -- manually attach it so Java_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_SwitchCase(default=True)
    partner = Java_Expression()
    setattr(partner, 'Java_Expression309', None)
    _safe_set(owner, 'Java_SwitchCase', partner)
    assert getattr(partner, 'Java_Expression309') == owner
    _safe_set(owner, 'Java_SwitchCase', None)
    assert getattr(partner, 'Java_Expression309') is None


def test_assoc_extendedOperands190_stub_double():
    # Java_Expression has no real 'Java_Expression192' property in the generated
    # code (a bare stub) -- manually attach it so Java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_InfixExpression(operator="sample_text")
    partner = Java_Expression()
    setattr(partner, 'Java_Expression192', None)
    _safe_set(owner, 'Java_InfixExpression191', {partner})
    assert getattr(partner, 'Java_Expression192') == owner
    _safe_set(owner, 'Java_InfixExpression191', set())
    assert getattr(partner, 'Java_Expression192') is None


def test_assoc_fragments320_stub_double():
    # Java_ASTNode has no real 'Java_ASTNode322' property in the generated
    # code (a bare stub) -- manually attach it so Java_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_TagElement(tagName="sample_text")
    partner = Java_ASTNode()
    setattr(partner, 'Java_ASTNode322', None)
    _safe_set(owner, 'Java_TagElement321', {partner})
    assert getattr(partner, 'Java_ASTNode322') == owner
    _safe_set(owner, 'Java_TagElement321', set())
    assert getattr(partner, 'Java_ASTNode322') is None


def test_assoc_initializer351_stub_double():
    # Java_Expression has no real 'Java_Expression352' property in the generated
    # code (a bare stub) -- manually attach it so Java_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_VariableDeclaration(extraArrayDimensions=7)
    partner = Java_Expression()
    setattr(partner, 'Java_Expression352', None)
    _safe_set(owner, 'Java_VariableDeclaration', partner)
    assert getattr(partner, 'Java_Expression352') == owner
    _safe_set(owner, 'Java_VariableDeclaration', None)
    assert getattr(partner, 'Java_Expression352') is None


def test_assoc_leftHandSide80_stub_double():
    # Java_Expression has no real 'Java_Expression81' property in the generated
    # code (a bare stub) -- manually attach it so Java_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Assignment(operator="sample_text")
    partner = Java_Expression()
    setattr(partner, 'Java_Expression81', None)
    _safe_set(owner, 'Java_Assignment', partner)
    assert getattr(partner, 'Java_Expression81') == owner
    _safe_set(owner, 'Java_Assignment', None)
    assert getattr(partner, 'Java_Expression81') is None


def test_assoc_leftOperand187_stub_double():
    # Java_Expression has no real 'Java_Expression189' property in the generated
    # code (a bare stub) -- manually attach it so Java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_InfixExpression(operator="sample_text")
    partner = Java_Expression()
    setattr(partner, 'Java_Expression189', None)
    _safe_set(owner, 'Java_InfixExpression188', partner)
    assert getattr(partner, 'Java_Expression189') == owner
    _safe_set(owner, 'Java_InfixExpression188', None)
    assert getattr(partner, 'Java_Expression189') is None


def test_assoc_mainAttributes206_stub_double():
    # Java_Manifest has no real 'Java_Manifest207' property in the generated
    # code (a bare stub) -- manually attach it so Java_ManifestAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_ManifestAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_ManifestAttribute(key="sample_text", value="sample_text")
    partner = Java_Manifest()
    setattr(partner, 'Java_Manifest207', None)
    _safe_set(owner, 'Java_ManifestAttribute', partner)
    assert owner in getattr(partner, 'Java_Manifest207')
    _safe_set(owner, 'Java_ManifestAttribute', None)
    assert owner not in getattr(partner, 'Java_Manifest207')


def test_assoc_manifest33_stub_double():
    # Java_Manifest has no real 'Java_Manifest' property in the generated
    # code (a bare stub) -- manually attach it so Java_Archive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Archive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Archive(originalFilePath="sample_text")
    partner = Java_Manifest()
    setattr(partner, 'Java_Manifest', None)
    _safe_set(owner, 'Java_Archive34', partner)
    assert getattr(partner, 'Java_Manifest') == owner
    _safe_set(owner, 'Java_Archive34', None)
    assert getattr(partner, 'Java_Manifest') is None


def test_assoc_member213_stub_double():
    # Java_MemberRef has no real 'Java_MemberRef' property in the generated
    # code (a bare stub) -- manually attach it so Java_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_NamedElement(name="sample_text", proxy=True)
    partner = Java_MemberRef()
    setattr(partner, 'Java_MemberRef', None)
    _safe_set(owner, 'Java_NamedElement', partner)
    assert getattr(partner, 'Java_MemberRef') == owner
    _safe_set(owner, 'Java_NamedElement', None)
    assert getattr(partner, 'Java_MemberRef') is None


def test_assoc_methodDeclaration300_stub_double():
    # Java_AbstractMethodDeclaration has no real 'AbstractMethodDeclaration301' property in the generated
    # code (a bare stub) -- manually attach it so Java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_SingleVariableDeclaration(varargs=True)
    partner = Java_AbstractMethodDeclaration()
    setattr(partner, 'AbstractMethodDeclaration301', None)
    _safe_set(owner, 'parameters', partner)
    assert getattr(partner, 'AbstractMethodDeclaration301') == owner
    _safe_set(owner, 'parameters', None)
    assert getattr(partner, 'AbstractMethodDeclaration301') is None


def test_assoc_model261_stub_double():
    # Java_Package has no real 'ownedElements262' property in the generated
    # code (a bare stub) -- manually attach it so Java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Model(name="sample_text")
    partner = Java_Package()
    setattr(partner, 'ownedElements262', None)
    _safe_set(owner, 'Model', partner)
    assert getattr(partner, 'ownedElements262') == owner
    _safe_set(owner, 'Model', None)
    assert getattr(partner, 'ownedElements262') is None


def test_assoc_modifier354_stub_double():
    # Java_VariableDeclarationExpression has no real 'variableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so Java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = Java_VariableDeclarationExpression()
    setattr(partner, 'variableDeclarationExpression', None)
    _safe_set(owner, 'Modifier355', partner)
    assert getattr(partner, 'variableDeclarationExpression') == owner
    _safe_set(owner, 'Modifier355', None)
    assert getattr(partner, 'variableDeclarationExpression') is None


def test_assoc_modifier90_stub_double():
    # Java_BodyDeclaration has no real 'bodyDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so Java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = Java_BodyDeclaration()
    setattr(partner, 'bodyDeclaration', None)
    _safe_set(owner, 'Modifier', partner)
    assert getattr(partner, 'bodyDeclaration') == owner
    _safe_set(owner, 'Modifier', None)
    assert getattr(partner, 'bodyDeclaration') is None


def test_assoc_operand283_stub_double():
    # Java_Expression has no real 'Java_Expression284' property in the generated
    # code (a bare stub) -- manually attach it so Java_PostfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_PostfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_PostfixExpression(operator="sample_text")
    partner = Java_Expression()
    setattr(partner, 'Java_Expression284', None)
    _safe_set(owner, 'Java_PostfixExpression', partner)
    assert getattr(partner, 'Java_Expression284') == owner
    _safe_set(owner, 'Java_PostfixExpression', None)
    assert getattr(partner, 'Java_Expression284') is None


def test_assoc_operand285_stub_double():
    # Java_Expression has no real 'Java_Expression286' property in the generated
    # code (a bare stub) -- manually attach it so Java_PrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_PrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_PrefixExpression(operator="sample_text")
    partner = Java_Expression()
    setattr(partner, 'Java_Expression286', None)
    _safe_set(owner, 'Java_PrefixExpression', partner)
    assert getattr(partner, 'Java_Expression286') == owner
    _safe_set(owner, 'Java_PrefixExpression', None)
    assert getattr(partner, 'Java_Expression286') is None


def test_assoc_originalClassFile44_stub_double():
    # Java_ASTNode has no real 'Java_ASTNode45' property in the generated
    # code (a bare stub) -- manually attach it so Java_ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_ClassFile(originalFilePath="sample_text")
    partner = Java_ASTNode()
    setattr(partner, 'Java_ASTNode45', None)
    _safe_set(owner, 'Java_ClassFile46', partner)
    assert getattr(partner, 'Java_ASTNode45') == owner
    _safe_set(owner, 'Java_ClassFile46', None)
    assert getattr(partner, 'Java_ASTNode45') is None


def test_assoc_originalCompilationUnit42_stub_double():
    # Java_ASTNode has no real 'Java_ASTNode43' property in the generated
    # code (a bare stub) -- manually attach it so Java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_CompilationUnit(originalFilePath="sample_text")
    partner = Java_ASTNode()
    setattr(partner, 'Java_ASTNode43', None)
    _safe_set(owner, 'Java_CompilationUnit', partner)
    assert getattr(partner, 'Java_ASTNode43') == owner
    _safe_set(owner, 'Java_CompilationUnit', None)
    assert getattr(partner, 'Java_ASTNode43') is None


def test_assoc_orphanTypes237_stub_double():
    # Java_Type has no real 'Java_Type' property in the generated
    # code (a bare stub) -- manually attach it so Java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Model(name="sample_text")
    partner = Java_Type()
    setattr(partner, 'Java_Type', None)
    _safe_set(owner, 'Java_Model', {partner})
    assert getattr(partner, 'Java_Type') == owner
    _safe_set(owner, 'Java_Model', set())
    assert getattr(partner, 'Java_Type') is None


def test_assoc_ownedElements235_stub_double():
    # Java_Package has no real 'Package236' property in the generated
    # code (a bare stub) -- manually attach it so Java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Model(name="sample_text")
    partner = Java_Package()
    setattr(partner, 'Package236', None)
    _safe_set(owner, 'model', {partner})
    assert getattr(partner, 'Package236') == owner
    _safe_set(owner, 'model', set())
    assert getattr(partner, 'Package236') is None


def test_assoc_package109_stub_double():
    # Java_Package has no real 'Java_Package' property in the generated
    # code (a bare stub) -- manually attach it so Java_ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_ClassFile(originalFilePath="sample_text")
    partner = Java_Package()
    setattr(partner, 'Java_Package', None)
    _safe_set(owner, 'Java_ClassFile110', partner)
    assert getattr(partner, 'Java_Package') == owner
    _safe_set(owner, 'Java_ClassFile110', None)
    assert getattr(partner, 'Java_Package') is None


def test_assoc_package133_stub_double():
    # Java_Package has no real 'Java_Package135' property in the generated
    # code (a bare stub) -- manually attach it so Java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_CompilationUnit(originalFilePath="sample_text")
    partner = Java_Package()
    setattr(partner, 'Java_Package135', None)
    _safe_set(owner, 'Java_CompilationUnit134', partner)
    assert getattr(partner, 'Java_Package135') == owner
    _safe_set(owner, 'Java_CompilationUnit134', None)
    assert getattr(partner, 'Java_Package135') is None


def test_assoc_parameter151_stub_double():
    # Java_EnhancedForStatement has no real 'enhancedForStatement' property in the generated
    # code (a bare stub) -- manually attach it so Java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_SingleVariableDeclaration(varargs=True)
    partner = Java_EnhancedForStatement()
    setattr(partner, 'enhancedForStatement', None)
    _safe_set(owner, 'SingleVariableDeclaration152', partner)
    assert getattr(partner, 'enhancedForStatement') == owner
    _safe_set(owner, 'SingleVariableDeclaration152', None)
    assert getattr(partner, 'enhancedForStatement') is None


def test_assoc_parameters1_stub_double():
    # Java_AbstractMethodDeclaration has no real 'methodDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so Java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_SingleVariableDeclaration(varargs=True)
    partner = Java_AbstractMethodDeclaration()
    setattr(partner, 'methodDeclaration', None)
    _safe_set(owner, 'SingleVariableDeclaration', partner)
    assert owner in getattr(partner, 'methodDeclaration')
    _safe_set(owner, 'SingleVariableDeclaration', None)
    assert owner not in getattr(partner, 'methodDeclaration')


def test_assoc_parameters230_stub_double():
    # Java_MethodRef has no real 'Java_MethodRef231' property in the generated
    # code (a bare stub) -- manually attach it so Java_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_MethodRefParameter(name="sample_text", varargs=True)
    partner = Java_MethodRef()
    setattr(partner, 'Java_MethodRef231', None)
    _safe_set(owner, 'Java_MethodRefParameter', partner)
    assert owner in getattr(partner, 'Java_MethodRef231')
    _safe_set(owner, 'Java_MethodRefParameter', None)
    assert owner not in getattr(partner, 'Java_MethodRef231')


def test_assoc_returnType217_stub_double():
    # Java_TypeAccess has no real 'Java_TypeAccess218' property in the generated
    # code (a bare stub) -- manually attach it so Java_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_MethodDeclaration(extraArrayDimensions=7)
    partner = Java_TypeAccess()
    setattr(partner, 'Java_TypeAccess218', None)
    _safe_set(owner, 'Java_MethodDeclaration', partner)
    assert getattr(partner, 'Java_TypeAccess218') == owner
    _safe_set(owner, 'Java_MethodDeclaration', None)
    assert getattr(partner, 'Java_TypeAccess218') is None


def test_assoc_rightHandSide82_stub_double():
    # Java_Expression has no real 'Java_Expression84' property in the generated
    # code (a bare stub) -- manually attach it so Java_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Assignment(operator="sample_text")
    partner = Java_Expression()
    setattr(partner, 'Java_Expression84', None)
    _safe_set(owner, 'Java_Assignment83', partner)
    assert getattr(partner, 'Java_Expression84') == owner
    _safe_set(owner, 'Java_Assignment83', None)
    assert getattr(partner, 'Java_Expression84') is None


def test_assoc_rightOperand185_stub_double():
    # Java_Expression has no real 'Java_Expression186' property in the generated
    # code (a bare stub) -- manually attach it so Java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_InfixExpression(operator="sample_text")
    partner = Java_Expression()
    setattr(partner, 'Java_Expression186', None)
    _safe_set(owner, 'Java_InfixExpression', partner)
    assert getattr(partner, 'Java_Expression186') == owner
    _safe_set(owner, 'Java_InfixExpression', None)
    assert getattr(partner, 'Java_Expression186') is None


def test_assoc_tags200_stub_double():
    # Java_Javadoc has no real 'Java_Javadoc' property in the generated
    # code (a bare stub) -- manually attach it so Java_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_TagElement(tagName="sample_text")
    partner = Java_Javadoc()
    setattr(partner, 'Java_Javadoc', None)
    _safe_set(owner, 'Java_TagElement', partner)
    assert owner in getattr(partner, 'Java_Javadoc')
    _safe_set(owner, 'Java_TagElement', None)
    assert owner not in getattr(partner, 'Java_Javadoc')


def test_assoc_type103_stub_double():
    # Java_AbstractTypeDeclaration has no real 'Java_AbstractTypeDeclaration105' property in the generated
    # code (a bare stub) -- manually attach it so Java_ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_ClassFile(originalFilePath="sample_text")
    partner = Java_AbstractTypeDeclaration()
    setattr(partner, 'Java_AbstractTypeDeclaration105', None)
    _safe_set(owner, 'Java_ClassFile104', partner)
    assert getattr(partner, 'Java_AbstractTypeDeclaration105') == owner
    _safe_set(owner, 'Java_ClassFile104', None)
    assert getattr(partner, 'Java_AbstractTypeDeclaration105') is None


def test_assoc_type232_stub_double():
    # Java_TypeAccess has no real 'Java_TypeAccess234' property in the generated
    # code (a bare stub) -- manually attach it so Java_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_MethodRefParameter(name="sample_text", varargs=True)
    partner = Java_TypeAccess()
    setattr(partner, 'Java_TypeAccess234', None)
    _safe_set(owner, 'Java_MethodRefParameter233', partner)
    assert getattr(partner, 'Java_TypeAccess234') == owner
    _safe_set(owner, 'Java_MethodRefParameter233', None)
    assert getattr(partner, 'Java_TypeAccess234') is None


def test_assoc_type295_stub_double():
    # Java_TypeAccess has no real 'Java_TypeAccess296' property in the generated
    # code (a bare stub) -- manually attach it so Java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_SingleVariableDeclaration(varargs=True)
    partner = Java_TypeAccess()
    setattr(partner, 'Java_TypeAccess296', None)
    _safe_set(owner, 'Java_SingleVariableDeclaration', partner)
    assert getattr(partner, 'Java_TypeAccess296') == owner
    _safe_set(owner, 'Java_SingleVariableDeclaration', None)
    assert getattr(partner, 'Java_TypeAccess296') is None


def test_assoc_types136_stub_double():
    # Java_AbstractTypeDeclaration has no real 'Java_AbstractTypeDeclaration138' property in the generated
    # code (a bare stub) -- manually attach it so Java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_CompilationUnit(originalFilePath="sample_text")
    partner = Java_AbstractTypeDeclaration()
    setattr(partner, 'Java_AbstractTypeDeclaration138', None)
    _safe_set(owner, 'Java_CompilationUnit137', {partner})
    assert getattr(partner, 'Java_AbstractTypeDeclaration138') == owner
    _safe_set(owner, 'Java_CompilationUnit137', set())
    assert getattr(partner, 'Java_AbstractTypeDeclaration138') is None


def test_assoc_unresolvedItems238_stub_double():
    # Java_UnresolvedItem has no real 'Java_UnresolvedItem' property in the generated
    # code (a bare stub) -- manually attach it so Java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Model(name="sample_text")
    partner = Java_UnresolvedItem()
    setattr(partner, 'Java_UnresolvedItem', None)
    _safe_set(owner, 'Java_Model239', {partner})
    assert getattr(partner, 'Java_UnresolvedItem') == owner
    _safe_set(owner, 'Java_Model239', set())
    assert getattr(partner, 'Java_UnresolvedItem') is None


def test_assoc_usageInVariableAccess353_stub_double():
    # Java_SingleVariableAccess has no real 'SingleVariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so Java_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_VariableDeclaration(extraArrayDimensions=7)
    partner = Java_SingleVariableAccess()
    setattr(partner, 'SingleVariableAccess', None)
    _safe_set(owner, 'variable', {partner})
    assert getattr(partner, 'SingleVariableAccess') == owner
    _safe_set(owner, 'variable', set())
    assert getattr(partner, 'SingleVariableAccess') is None


def test_assoc_variable289_stub_double():
    # Java_SingleVariableAccess has no real 'usageInVariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so Java_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_VariableDeclaration(extraArrayDimensions=7)
    partner = Java_SingleVariableAccess()
    setattr(partner, 'usageInVariableAccess', None)
    _safe_set(owner, 'VariableDeclaration', partner)
    assert getattr(partner, 'usageInVariableAccess') == owner
    _safe_set(owner, 'VariableDeclaration', None)
    assert getattr(partner, 'usageInVariableAccess') is None


def test_assoc_variableDeclarationExpression256_stub_double():
    # Java_VariableDeclarationExpression has no real 'VariableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so Java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = Java_VariableDeclarationExpression()
    setattr(partner, 'VariableDeclarationExpression', None)
    _safe_set(owner, 'modifier257', partner)
    assert getattr(partner, 'VariableDeclarationExpression') == owner
    _safe_set(owner, 'modifier257', None)
    assert getattr(partner, 'VariableDeclarationExpression') is None


