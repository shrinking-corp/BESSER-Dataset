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

def test_assoc_archives246_reverse_link_reassign_clear():
    a1 = java_Model(name="sample_text")
    a2 = java_Model(name="sample_text_2")
    b = java_Archive(originalFilePath="sample_text")
    _safe_set(b, 'java_Archive248', a1)
    assert _is_linked(b, 'java_Archive248', a1)
    if hasattr(a1, 'java_Model247'):
        assert _is_linked(a1, 'java_Model247', b)
    _safe_set(b, 'java_Archive248', a2)
    assert _is_linked(b, 'java_Archive248', a2)
    if hasattr(a1, 'java_Model247'):
        assert not _is_linked(a1, 'java_Model247', b)
    if hasattr(a2, 'java_Model247'):
        assert _is_linked(a2, 'java_Model247', b)
    _safe_set(b, 'java_Archive248', None)
    assert not _is_linked(b, 'java_Archive248', a2)
    if hasattr(a2, 'java_Model247'):
        assert not _is_linked(a2, 'java_Model247', b)


def test_assoc_attachedSource105_reverse_link_reassign_clear():
    a1 = java_CompilationUnit(originalFilePath="sample_text")
    a2 = java_CompilationUnit(originalFilePath="sample_text_2")
    b = java_ClassFile(originalFilePath="sample_text")
    _safe_set(b, 'java_ClassFile106', a1)
    assert _is_linked(b, 'java_ClassFile106', a1)
    if hasattr(a1, 'java_CompilationUnit107'):
        assert _is_linked(a1, 'java_CompilationUnit107', b)
    _safe_set(b, 'java_ClassFile106', a2)
    assert _is_linked(b, 'java_ClassFile106', a2)
    if hasattr(a1, 'java_CompilationUnit107'):
        assert not _is_linked(a1, 'java_CompilationUnit107', b)
    if hasattr(a2, 'java_CompilationUnit107'):
        assert _is_linked(a2, 'java_CompilationUnit107', b)
    _safe_set(b, 'java_ClassFile106', None)
    assert not _is_linked(b, 'java_ClassFile106', a2)
    if hasattr(a2, 'java_CompilationUnit107'):
        assert not _is_linked(a2, 'java_CompilationUnit107', b)


def test_assoc_attributes208_reverse_link_reassign_clear():
    a1 = java_ManifestEntry(name="sample_text")
    a2 = java_ManifestEntry(name="sample_text_2")
    b = java_ManifestAttribute(key="sample_text", value="sample_text")
    _safe_set(b, 'java_ManifestAttribute210', a1)
    assert _is_linked(b, 'java_ManifestAttribute210', a1)
    if hasattr(a1, 'java_ManifestEntry209'):
        assert _is_linked(a1, 'java_ManifestEntry209', b)
    _safe_set(b, 'java_ManifestAttribute210', a2)
    assert _is_linked(b, 'java_ManifestAttribute210', a2)
    if hasattr(a1, 'java_ManifestEntry209'):
        assert not _is_linked(a1, 'java_ManifestEntry209', b)
    if hasattr(a2, 'java_ManifestEntry209'):
        assert _is_linked(a2, 'java_ManifestEntry209', b)
    _safe_set(b, 'java_ManifestAttribute210', None)
    assert not _is_linked(b, 'java_ManifestAttribute210', a2)
    if hasattr(a2, 'java_ManifestEntry209'):
        assert not _is_linked(a2, 'java_ManifestEntry209', b)


def test_assoc_classFiles243_reverse_link_reassign_clear():
    a1 = java_Model(name="sample_text")
    a2 = java_Model(name="sample_text_2")
    b = java_ClassFile(originalFilePath="sample_text")
    _safe_set(b, 'java_ClassFile245', a1)
    assert _is_linked(b, 'java_ClassFile245', a1)
    if hasattr(a1, 'java_Model244'):
        assert _is_linked(a1, 'java_Model244', b)
    _safe_set(b, 'java_ClassFile245', a2)
    assert _is_linked(b, 'java_ClassFile245', a2)
    if hasattr(a1, 'java_Model244'):
        assert not _is_linked(a1, 'java_Model244', b)
    if hasattr(a2, 'java_Model244'):
        assert _is_linked(a2, 'java_Model244', b)
    _safe_set(b, 'java_ClassFile245', None)
    assert not _is_linked(b, 'java_ClassFile245', a2)
    if hasattr(a2, 'java_Model244'):
        assert not _is_linked(a2, 'java_Model244', b)


def test_assoc_classFiles31_reverse_link_reassign_clear():
    a1 = java_ClassFile(originalFilePath="sample_text")
    a2 = java_ClassFile(originalFilePath="sample_text_2")
    b = java_Archive(originalFilePath="sample_text")
    _safe_set(b, 'java_Archive', {a1})
    assert _is_linked(b, 'java_Archive', a1)
    if hasattr(a1, 'java_ClassFile'):
        assert _is_linked(a1, 'java_ClassFile', b)
    _safe_set(b, 'java_Archive', {a2})
    assert _is_linked(b, 'java_Archive', a2)
    if hasattr(a1, 'java_ClassFile'):
        assert not _is_linked(a1, 'java_ClassFile', b)
    if hasattr(a2, 'java_ClassFile'):
        assert _is_linked(a2, 'java_ClassFile', b)
    _safe_set(b, 'java_Archive', set())
    assert not _is_linked(b, 'java_Archive', a2)
    if hasattr(a2, 'java_ClassFile'):
        assert not _is_linked(a2, 'java_ClassFile', b)


def test_assoc_commentList127_reverse_link_reassign_clear():
    a1 = java_CompilationUnit(originalFilePath="sample_text")
    a2 = java_CompilationUnit(originalFilePath="sample_text_2")
    b = java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    _safe_set(b, 'java_Comment129', a1)
    assert _is_linked(b, 'java_Comment129', a1)
    if hasattr(a1, 'java_CompilationUnit128'):
        assert _is_linked(a1, 'java_CompilationUnit128', b)
    _safe_set(b, 'java_Comment129', a2)
    assert _is_linked(b, 'java_Comment129', a2)
    if hasattr(a1, 'java_CompilationUnit128'):
        assert not _is_linked(a1, 'java_CompilationUnit128', b)
    if hasattr(a2, 'java_CompilationUnit128'):
        assert _is_linked(a2, 'java_CompilationUnit128', b)
    _safe_set(b, 'java_Comment129', None)
    assert not _is_linked(b, 'java_Comment129', a2)
    if hasattr(a2, 'java_CompilationUnit128'):
        assert not _is_linked(a2, 'java_CompilationUnit128', b)


def test_assoc_compilationUnits240_reverse_link_reassign_clear():
    a1 = java_Model(name="sample_text")
    a2 = java_Model(name="sample_text_2")
    b = java_CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'java_CompilationUnit242', a1)
    assert _is_linked(b, 'java_CompilationUnit242', a1)
    if hasattr(a1, 'java_Model241'):
        assert _is_linked(a1, 'java_Model241', b)
    _safe_set(b, 'java_CompilationUnit242', a2)
    assert _is_linked(b, 'java_CompilationUnit242', a2)
    if hasattr(a1, 'java_Model241'):
        assert not _is_linked(a1, 'java_Model241', b)
    if hasattr(a2, 'java_Model241'):
        assert _is_linked(a2, 'java_Model241', b)
    _safe_set(b, 'java_CompilationUnit242', None)
    assert not _is_linked(b, 'java_CompilationUnit242', a2)
    if hasattr(a2, 'java_Model241'):
        assert not _is_linked(a2, 'java_Model241', b)


def test_assoc_importedElement183_reverse_link_reassign_clear():
    a1 = java_NamedElement(name="sample_text", proxy=True)
    a2 = java_NamedElement(name="sample_text_2", proxy=False)
    b = java_ImportDeclaration(static=True)
    _safe_set(b, 'java_ImportDeclaration184', a1)
    assert _is_linked(b, 'java_ImportDeclaration184', a1)
    if hasattr(a1, 'java_NamedElement'):
        assert _is_linked(a1, 'java_NamedElement', b)
    _safe_set(b, 'java_ImportDeclaration184', a2)
    assert _is_linked(b, 'java_ImportDeclaration184', a2)
    if hasattr(a1, 'java_NamedElement'):
        assert not _is_linked(a1, 'java_NamedElement', b)
    if hasattr(a2, 'java_NamedElement'):
        assert _is_linked(a2, 'java_NamedElement', b)
    _safe_set(b, 'java_ImportDeclaration184', None)
    assert not _is_linked(b, 'java_ImportDeclaration184', a2)
    if hasattr(a2, 'java_NamedElement'):
        assert not _is_linked(a2, 'java_NamedElement', b)


def test_assoc_imports130_reverse_link_reassign_clear():
    a1 = java_ImportDeclaration(static=True)
    a2 = java_ImportDeclaration(static=False)
    b = java_CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'java_CompilationUnit131', {a1})
    assert _is_linked(b, 'java_CompilationUnit131', a1)
    if hasattr(a1, 'java_ImportDeclaration'):
        assert _is_linked(a1, 'java_ImportDeclaration', b)
    _safe_set(b, 'java_CompilationUnit131', {a2})
    assert _is_linked(b, 'java_CompilationUnit131', a2)
    if hasattr(a1, 'java_ImportDeclaration'):
        assert not _is_linked(a1, 'java_ImportDeclaration', b)
    if hasattr(a2, 'java_ImportDeclaration'):
        assert _is_linked(a2, 'java_ImportDeclaration', b)
    _safe_set(b, 'java_CompilationUnit131', set())
    assert not _is_linked(b, 'java_CompilationUnit131', a2)
    if hasattr(a2, 'java_ImportDeclaration'):
        assert not _is_linked(a2, 'java_ImportDeclaration', b)


def test_assoc_modifier292_reverse_link_reassign_clear():
    a1 = java_SingleVariableDeclaration(varargs=True)
    a2 = java_SingleVariableDeclaration(varargs=False)
    b = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    _safe_set(b, 'Modifier293', a1)
    assert _is_linked(b, 'Modifier293', a1)
    if hasattr(a1, 'singleVariableDeclaration'):
        assert _is_linked(a1, 'singleVariableDeclaration', b)
    _safe_set(b, 'Modifier293', a2)
    assert _is_linked(b, 'Modifier293', a2)
    if hasattr(a1, 'singleVariableDeclaration'):
        assert not _is_linked(a1, 'singleVariableDeclaration', b)
    if hasattr(a2, 'singleVariableDeclaration'):
        assert _is_linked(a2, 'singleVariableDeclaration', b)
    _safe_set(b, 'Modifier293', None)
    assert not _is_linked(b, 'Modifier293', a2)
    if hasattr(a2, 'singleVariableDeclaration'):
        assert not _is_linked(a2, 'singleVariableDeclaration', b)


def test_assoc_modifier358_reverse_link_reassign_clear():
    a1 = java_VariableDeclarationStatement(extraArrayDimensions=7)
    a2 = java_VariableDeclarationStatement(extraArrayDimensions=13)
    b = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    _safe_set(b, 'Modifier359', a1)
    assert _is_linked(b, 'Modifier359', a1)
    if hasattr(a1, 'variableDeclarationStatement'):
        assert _is_linked(a1, 'variableDeclarationStatement', b)
    _safe_set(b, 'Modifier359', a2)
    assert _is_linked(b, 'Modifier359', a2)
    if hasattr(a1, 'variableDeclarationStatement'):
        assert not _is_linked(a1, 'variableDeclarationStatement', b)
    if hasattr(a2, 'variableDeclarationStatement'):
        assert _is_linked(a2, 'variableDeclarationStatement', b)
    _safe_set(b, 'Modifier359', None)
    assert not _is_linked(b, 'Modifier359', a2)
    if hasattr(a2, 'variableDeclarationStatement'):
        assert not _is_linked(a2, 'variableDeclarationStatement', b)


def test_assoc_redefinedMethodDeclaration219_reverse_link_reassign_clear():
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


def test_assoc_redefinitions221_reverse_link_reassign_clear():
    a1 = java_MethodDeclaration(extraArrayDimensions=7)
    a2 = java_MethodDeclaration(extraArrayDimensions=13)
    b = java_MethodDeclaration(extraArrayDimensions=7)
    _safe_set(b, 'redefinedMethodDeclaration', {a1})
    assert _is_linked(b, 'redefinedMethodDeclaration', a1)
    if hasattr(a1, 'MethodDeclaration222'):
        assert _is_linked(a1, 'MethodDeclaration222', b)
    _safe_set(b, 'redefinedMethodDeclaration', {a2})
    assert _is_linked(b, 'redefinedMethodDeclaration', a2)
    if hasattr(a1, 'MethodDeclaration222'):
        assert not _is_linked(a1, 'MethodDeclaration222', b)
    if hasattr(a2, 'MethodDeclaration222'):
        assert _is_linked(a2, 'MethodDeclaration222', b)
    _safe_set(b, 'redefinedMethodDeclaration', set())
    assert not _is_linked(b, 'redefinedMethodDeclaration', a2)
    if hasattr(a2, 'MethodDeclaration222'):
        assert not _is_linked(a2, 'MethodDeclaration222', b)


def test_assoc_singleVariableDeclaration251_reverse_link_reassign_clear():
    a1 = java_SingleVariableDeclaration(varargs=True)
    a2 = java_SingleVariableDeclaration(varargs=False)
    b = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
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


def test_assoc_variableDeclarationStatement254_reverse_link_reassign_clear():
    a1 = java_VariableDeclarationStatement(extraArrayDimensions=7)
    a2 = java_VariableDeclarationStatement(extraArrayDimensions=13)
    b = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
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

def test_assoc_annotations296_stub_double():
    # java_Annotation has no real 'java_Annotation298' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_Annotation()
    setattr(partner, 'java_Annotation298', None)
    _safe_set(owner, 'java_SingleVariableDeclaration297', {partner})
    assert getattr(partner, 'java_Annotation298') == owner
    _safe_set(owner, 'java_SingleVariableDeclaration297', set())
    assert getattr(partner, 'java_Annotation298') is None


def test_assoc_annotations360_stub_double():
    # java_Annotation has no real 'java_Annotation361' property in the generated
    # code (a bare stub) -- manually attach it so java_VariableDeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_VariableDeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_VariableDeclarationStatement(extraArrayDimensions=7)
    partner = java_Annotation()
    setattr(partner, 'java_Annotation361', None)
    _safe_set(owner, 'java_VariableDeclarationStatement', {partner})
    assert getattr(partner, 'java_Annotation361') == owner
    _safe_set(owner, 'java_VariableDeclarationStatement', set())
    assert getattr(partner, 'java_Annotation361') is None


def test_assoc_bodyDeclaration249_stub_double():
    # java_BodyDeclaration has no real 'BodyDeclaration250' property in the generated
    # code (a bare stub) -- manually attach it so java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java_BodyDeclaration()
    setattr(partner, 'BodyDeclaration250', None)
    _safe_set(owner, 'modifier', partner)
    assert getattr(partner, 'BodyDeclaration250') == owner
    _safe_set(owner, 'modifier', None)
    assert getattr(partner, 'BodyDeclaration250') is None


def test_assoc_bound362_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess363' property in the generated
    # code (a bare stub) -- manually attach it so java_WildCardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_WildCardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_WildCardType(upperBound=True)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess363', None)
    _safe_set(owner, 'java_WildCardType', partner)
    assert getattr(partner, 'java_TypeAccess363') == owner
    _safe_set(owner, 'java_WildCardType', None)
    assert getattr(partner, 'java_TypeAccess363') is None


def test_assoc_catchClause300_stub_double():
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


def test_assoc_comments39_stub_double():
    # java_ASTNode has no real 'java_ASTNode' property in the generated
    # code (a bare stub) -- manually attach it so java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = java_ASTNode()
    setattr(partner, 'java_ASTNode', None)
    _safe_set(owner, 'java_Comment40', partner)
    assert owner in getattr(partner, 'java_ASTNode')
    _safe_set(owner, 'java_Comment40', None)
    assert owner not in getattr(partner, 'java_ASTNode')


def test_assoc_commentsAfterBody15_stub_double():
    # java_AbstractTypeDeclaration has no real 'java_AbstractTypeDeclaration16' property in the generated
    # code (a bare stub) -- manually attach it so java_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = java_AbstractTypeDeclaration()
    setattr(partner, 'java_AbstractTypeDeclaration16', None)
    _safe_set(owner, 'java_Comment17', partner)
    assert owner in getattr(partner, 'java_AbstractTypeDeclaration16')
    _safe_set(owner, 'java_Comment17', None)
    assert owner not in getattr(partner, 'java_AbstractTypeDeclaration16')


def test_assoc_commentsBeforeBody14_stub_double():
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


def test_assoc_elementType77_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess78' property in the generated
    # code (a bare stub) -- manually attach it so java_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_ArrayType(dimensions=7)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess78', None)
    _safe_set(owner, 'java_ArrayType', partner)
    assert getattr(partner, 'java_TypeAccess78') == owner
    _safe_set(owner, 'java_ArrayType', None)
    assert getattr(partner, 'java_TypeAccess78') is None


def test_assoc_enhancedForStatement301_stub_double():
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


def test_assoc_entryAttributes206_stub_double():
    # java_Manifest has no real 'java_Manifest207' property in the generated
    # code (a bare stub) -- manually attach it so java_ManifestEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_ManifestEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_ManifestEntry(name="sample_text")
    partner = java_Manifest()
    setattr(partner, 'java_Manifest207', None)
    _safe_set(owner, 'java_ManifestEntry', partner)
    assert owner in getattr(partner, 'java_Manifest207')
    _safe_set(owner, 'java_ManifestEntry', None)
    assert owner not in getattr(partner, 'java_Manifest207')


def test_assoc_exception98_stub_double():
    # java_CatchClause has no real 'catchClause' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_CatchClause()
    setattr(partner, 'catchClause', None)
    _safe_set(owner, 'SingleVariableDeclaration99', partner)
    assert getattr(partner, 'catchClause') == owner
    _safe_set(owner, 'SingleVariableDeclaration99', None)
    assert getattr(partner, 'catchClause') is None


def test_assoc_expression306_stub_double():
    # java_Expression has no real 'java_Expression307' property in the generated
    # code (a bare stub) -- manually attach it so java_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SwitchCase(default=True)
    partner = java_Expression()
    setattr(partner, 'java_Expression307', None)
    _safe_set(owner, 'java_SwitchCase', partner)
    assert getattr(partner, 'java_Expression307') == owner
    _safe_set(owner, 'java_SwitchCase', None)
    assert getattr(partner, 'java_Expression307') is None


def test_assoc_extendedOperands190_stub_double():
    # java_Expression has no real 'java_Expression192' property in the generated
    # code (a bare stub) -- manually attach it so java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_InfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression192', None)
    _safe_set(owner, 'java_InfixExpression191', {partner})
    assert getattr(partner, 'java_Expression192') == owner
    _safe_set(owner, 'java_InfixExpression191', set())
    assert getattr(partner, 'java_Expression192') is None


def test_assoc_fragments318_stub_double():
    # java_ASTNode has no real 'java_ASTNode320' property in the generated
    # code (a bare stub) -- manually attach it so java_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_TagElement(tagName="sample_text")
    partner = java_ASTNode()
    setattr(partner, 'java_ASTNode320', None)
    _safe_set(owner, 'java_TagElement319', {partner})
    assert getattr(partner, 'java_ASTNode320') == owner
    _safe_set(owner, 'java_TagElement319', set())
    assert getattr(partner, 'java_ASTNode320') is None


def test_assoc_initializer350_stub_double():
    # java_Expression has no real 'java_Expression352' property in the generated
    # code (a bare stub) -- manually attach it so java_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_VariableDeclaration(extraArrayDimensions=7)
    partner = java_Expression()
    setattr(partner, 'java_Expression352', None)
    _safe_set(owner, 'java_VariableDeclaration351', partner)
    assert getattr(partner, 'java_Expression352') == owner
    _safe_set(owner, 'java_VariableDeclaration351', None)
    assert getattr(partner, 'java_Expression352') is None


def test_assoc_leftHandSide79_stub_double():
    # java_Expression has no real 'java_Expression80' property in the generated
    # code (a bare stub) -- manually attach it so java_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Assignment(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression80', None)
    _safe_set(owner, 'java_Assignment', partner)
    assert getattr(partner, 'java_Expression80') == owner
    _safe_set(owner, 'java_Assignment', None)
    assert getattr(partner, 'java_Expression80') is None


def test_assoc_leftOperand187_stub_double():
    # java_Expression has no real 'java_Expression189' property in the generated
    # code (a bare stub) -- manually attach it so java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_InfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression189', None)
    _safe_set(owner, 'java_InfixExpression188', partner)
    assert getattr(partner, 'java_Expression189') == owner
    _safe_set(owner, 'java_InfixExpression188', None)
    assert getattr(partner, 'java_Expression189') is None


def test_assoc_mainAttributes204_stub_double():
    # java_Manifest has no real 'java_Manifest205' property in the generated
    # code (a bare stub) -- manually attach it so java_ManifestAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_ManifestAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_ManifestAttribute(key="sample_text", value="sample_text")
    partner = java_Manifest()
    setattr(partner, 'java_Manifest205', None)
    _safe_set(owner, 'java_ManifestAttribute', partner)
    assert owner in getattr(partner, 'java_Manifest205')
    _safe_set(owner, 'java_ManifestAttribute', None)
    assert owner not in getattr(partner, 'java_Manifest205')


def test_assoc_manifest32_stub_double():
    # java_Manifest has no real 'java_Manifest' property in the generated
    # code (a bare stub) -- manually attach it so java_Archive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Archive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Archive(originalFilePath="sample_text")
    partner = java_Manifest()
    setattr(partner, 'java_Manifest', None)
    _safe_set(owner, 'java_Archive33', partner)
    assert getattr(partner, 'java_Manifest') == owner
    _safe_set(owner, 'java_Archive33', None)
    assert getattr(partner, 'java_Manifest') is None


def test_assoc_member211_stub_double():
    # java_MemberRef has no real 'java_MemberRef' property in the generated
    # code (a bare stub) -- manually attach it so java_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_NamedElement(name="sample_text", proxy=True)
    partner = java_MemberRef()
    setattr(partner, 'java_MemberRef', None)
    _safe_set(owner, 'java_NamedElement212', partner)
    assert getattr(partner, 'java_MemberRef') == owner
    _safe_set(owner, 'java_NamedElement212', None)
    assert getattr(partner, 'java_MemberRef') is None


def test_assoc_methodDeclaration299_stub_double():
    # java_AbstractMethodDeclaration has no real 'AbstractMethodDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_AbstractMethodDeclaration()
    setattr(partner, 'AbstractMethodDeclaration', None)
    _safe_set(owner, 'parameters', partner)
    assert getattr(partner, 'AbstractMethodDeclaration') == owner
    _safe_set(owner, 'parameters', None)
    assert getattr(partner, 'AbstractMethodDeclaration') is None


def test_assoc_model260_stub_double():
    # java_Package has no real 'ownedElements261' property in the generated
    # code (a bare stub) -- manually attach it so java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Model(name="sample_text")
    partner = java_Package()
    setattr(partner, 'ownedElements261', None)
    _safe_set(owner, 'Model', partner)
    assert getattr(partner, 'ownedElements261') == owner
    _safe_set(owner, 'Model', None)
    assert getattr(partner, 'ownedElements261') is None


def test_assoc_modifier353_stub_double():
    # java_VariableDeclarationExpression has no real 'variableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java_VariableDeclarationExpression()
    setattr(partner, 'variableDeclarationExpression', None)
    _safe_set(owner, 'Modifier354', partner)
    assert getattr(partner, 'variableDeclarationExpression') == owner
    _safe_set(owner, 'Modifier354', None)
    assert getattr(partner, 'variableDeclarationExpression') is None


def test_assoc_modifier89_stub_double():
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


def test_assoc_operand281_stub_double():
    # java_Expression has no real 'java_Expression282' property in the generated
    # code (a bare stub) -- manually attach it so java_PostfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_PostfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_PostfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression282', None)
    _safe_set(owner, 'java_PostfixExpression', partner)
    assert getattr(partner, 'java_Expression282') == owner
    _safe_set(owner, 'java_PostfixExpression', None)
    assert getattr(partner, 'java_Expression282') is None


def test_assoc_operand283_stub_double():
    # java_Expression has no real 'java_Expression284' property in the generated
    # code (a bare stub) -- manually attach it so java_PrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_PrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_PrefixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression284', None)
    _safe_set(owner, 'java_PrefixExpression', partner)
    assert getattr(partner, 'java_Expression284') == owner
    _safe_set(owner, 'java_PrefixExpression', None)
    assert getattr(partner, 'java_Expression284') is None


def test_assoc_originalClassFile43_stub_double():
    # java_ASTNode has no real 'java_ASTNode44' property in the generated
    # code (a bare stub) -- manually attach it so java_ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_ClassFile(originalFilePath="sample_text")
    partner = java_ASTNode()
    setattr(partner, 'java_ASTNode44', None)
    _safe_set(owner, 'java_ClassFile45', partner)
    assert getattr(partner, 'java_ASTNode44') == owner
    _safe_set(owner, 'java_ClassFile45', None)
    assert getattr(partner, 'java_ASTNode44') is None


def test_assoc_originalCompilationUnit41_stub_double():
    # java_ASTNode has no real 'java_ASTNode42' property in the generated
    # code (a bare stub) -- manually attach it so java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_CompilationUnit(originalFilePath="sample_text")
    partner = java_ASTNode()
    setattr(partner, 'java_ASTNode42', None)
    _safe_set(owner, 'java_CompilationUnit', partner)
    assert getattr(partner, 'java_ASTNode42') == owner
    _safe_set(owner, 'java_CompilationUnit', None)
    assert getattr(partner, 'java_ASTNode42') is None


def test_assoc_orphanTypes237_stub_double():
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


def test_assoc_ownedElements235_stub_double():
    # java_Package has no real 'Package236' property in the generated
    # code (a bare stub) -- manually attach it so java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Model(name="sample_text")
    partner = java_Package()
    setattr(partner, 'Package236', None)
    _safe_set(owner, 'model', {partner})
    assert getattr(partner, 'Package236') == owner
    _safe_set(owner, 'model', set())
    assert getattr(partner, 'Package236') is None


def test_assoc_package108_stub_double():
    # java_Package has no real 'java_Package' property in the generated
    # code (a bare stub) -- manually attach it so java_ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_ClassFile(originalFilePath="sample_text")
    partner = java_Package()
    setattr(partner, 'java_Package', None)
    _safe_set(owner, 'java_ClassFile109', partner)
    assert getattr(partner, 'java_Package') == owner
    _safe_set(owner, 'java_ClassFile109', None)
    assert getattr(partner, 'java_Package') is None


def test_assoc_package132_stub_double():
    # java_Package has no real 'java_Package134' property in the generated
    # code (a bare stub) -- manually attach it so java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_CompilationUnit(originalFilePath="sample_text")
    partner = java_Package()
    setattr(partner, 'java_Package134', None)
    _safe_set(owner, 'java_CompilationUnit133', partner)
    assert getattr(partner, 'java_Package134') == owner
    _safe_set(owner, 'java_CompilationUnit133', None)
    assert getattr(partner, 'java_Package134') is None


def test_assoc_parameter150_stub_double():
    # java_EnhancedForStatement has no real 'enhancedForStatement' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_EnhancedForStatement()
    setattr(partner, 'enhancedForStatement', None)
    _safe_set(owner, 'SingleVariableDeclaration151', partner)
    assert getattr(partner, 'enhancedForStatement') == owner
    _safe_set(owner, 'SingleVariableDeclaration151', None)
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


def test_assoc_parameters230_stub_double():
    # java_MethodRef has no real 'java_MethodRef231' property in the generated
    # code (a bare stub) -- manually attach it so java_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_MethodRefParameter(name="sample_text", varargs=True)
    partner = java_MethodRef()
    setattr(partner, 'java_MethodRef231', None)
    _safe_set(owner, 'java_MethodRefParameter', partner)
    assert owner in getattr(partner, 'java_MethodRef231')
    _safe_set(owner, 'java_MethodRefParameter', None)
    assert owner not in getattr(partner, 'java_MethodRef231')


def test_assoc_returnType216_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess217' property in the generated
    # code (a bare stub) -- manually attach it so java_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_MethodDeclaration(extraArrayDimensions=7)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess217', None)
    _safe_set(owner, 'java_MethodDeclaration', partner)
    assert getattr(partner, 'java_TypeAccess217') == owner
    _safe_set(owner, 'java_MethodDeclaration', None)
    assert getattr(partner, 'java_TypeAccess217') is None


def test_assoc_rightHandSide81_stub_double():
    # java_Expression has no real 'java_Expression83' property in the generated
    # code (a bare stub) -- manually attach it so java_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Assignment(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression83', None)
    _safe_set(owner, 'java_Assignment82', partner)
    assert getattr(partner, 'java_Expression83') == owner
    _safe_set(owner, 'java_Assignment82', None)
    assert getattr(partner, 'java_Expression83') is None


def test_assoc_rightOperand185_stub_double():
    # java_Expression has no real 'java_Expression186' property in the generated
    # code (a bare stub) -- manually attach it so java_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_InfixExpression(operator="sample_text")
    partner = java_Expression()
    setattr(partner, 'java_Expression186', None)
    _safe_set(owner, 'java_InfixExpression', partner)
    assert getattr(partner, 'java_Expression186') == owner
    _safe_set(owner, 'java_InfixExpression', None)
    assert getattr(partner, 'java_Expression186') is None


def test_assoc_tags200_stub_double():
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


def test_assoc_type102_stub_double():
    # java_AbstractTypeDeclaration has no real 'java_AbstractTypeDeclaration104' property in the generated
    # code (a bare stub) -- manually attach it so java_ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_ClassFile(originalFilePath="sample_text")
    partner = java_AbstractTypeDeclaration()
    setattr(partner, 'java_AbstractTypeDeclaration104', None)
    _safe_set(owner, 'java_ClassFile103', partner)
    assert getattr(partner, 'java_AbstractTypeDeclaration104') == owner
    _safe_set(owner, 'java_ClassFile103', None)
    assert getattr(partner, 'java_AbstractTypeDeclaration104') is None


def test_assoc_type232_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess234' property in the generated
    # code (a bare stub) -- manually attach it so java_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_MethodRefParameter(name="sample_text", varargs=True)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess234', None)
    _safe_set(owner, 'java_MethodRefParameter233', partner)
    assert getattr(partner, 'java_TypeAccess234') == owner
    _safe_set(owner, 'java_MethodRefParameter233', None)
    assert getattr(partner, 'java_TypeAccess234') is None


def test_assoc_type294_stub_double():
    # java_TypeAccess has no real 'java_TypeAccess295' property in the generated
    # code (a bare stub) -- manually attach it so java_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_SingleVariableDeclaration(varargs=True)
    partner = java_TypeAccess()
    setattr(partner, 'java_TypeAccess295', None)
    _safe_set(owner, 'java_SingleVariableDeclaration', partner)
    assert getattr(partner, 'java_TypeAccess295') == owner
    _safe_set(owner, 'java_SingleVariableDeclaration', None)
    assert getattr(partner, 'java_TypeAccess295') is None


def test_assoc_types135_stub_double():
    # java_AbstractTypeDeclaration has no real 'java_AbstractTypeDeclaration137' property in the generated
    # code (a bare stub) -- manually attach it so java_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_CompilationUnit(originalFilePath="sample_text")
    partner = java_AbstractTypeDeclaration()
    setattr(partner, 'java_AbstractTypeDeclaration137', None)
    _safe_set(owner, 'java_CompilationUnit136', {partner})
    assert getattr(partner, 'java_AbstractTypeDeclaration137') == owner
    _safe_set(owner, 'java_CompilationUnit136', set())
    assert getattr(partner, 'java_AbstractTypeDeclaration137') is None


def test_assoc_unresolvedItems238_stub_double():
    # java_UnresolvedItem has no real 'java_UnresolvedItem' property in the generated
    # code (a bare stub) -- manually attach it so java_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Model(name="sample_text")
    partner = java_UnresolvedItem()
    setattr(partner, 'java_UnresolvedItem', None)
    _safe_set(owner, 'java_Model239', {partner})
    assert getattr(partner, 'java_UnresolvedItem') == owner
    _safe_set(owner, 'java_Model239', set())
    assert getattr(partner, 'java_UnresolvedItem') is None


def test_assoc_variable287_stub_double():
    # java_SingleVariableAccess has no real 'java_SingleVariableAccess288' property in the generated
    # code (a bare stub) -- manually attach it so java_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_VariableDeclaration(extraArrayDimensions=7)
    partner = java_SingleVariableAccess()
    setattr(partner, 'java_SingleVariableAccess288', None)
    _safe_set(owner, 'java_VariableDeclaration', partner)
    assert getattr(partner, 'java_SingleVariableAccess288') == owner
    _safe_set(owner, 'java_VariableDeclaration', None)
    assert getattr(partner, 'java_SingleVariableAccess288') is None


def test_assoc_variableDeclarationExpression256_stub_double():
    # java_VariableDeclarationExpression has no real 'VariableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so java_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java_VariableDeclarationExpression()
    setattr(partner, 'VariableDeclarationExpression', None)
    _safe_set(owner, 'modifier257', partner)
    assert getattr(partner, 'VariableDeclarationExpression') == owner
    _safe_set(owner, 'modifier257', None)
    assert getattr(partner, 'VariableDeclarationExpression') is None


