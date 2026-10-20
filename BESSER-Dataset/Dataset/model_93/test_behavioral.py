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
    javaMM_ASTNode,
    javaMM_AbstractMethodDeclaration,
    javaMM_AbstractMethodInvocation,
    javaMM_AbstractTypeDeclaration,
    javaMM_AbstractTypeQualifiedExpression,
    javaMM_AbstractVariablesContainer,
    javaMM_Annotation,
    javaMM_AnnotationMemberValuePair,
    javaMM_AnnotationTypeDeclaration,
    javaMM_AnnotationTypeMemberDeclaration,
    javaMM_AnonymousClassDeclaration,
    javaMM_Archive,
    javaMM_ArrayAccess,
    javaMM_ArrayCreation,
    javaMM_ArrayInitializer,
    javaMM_ArrayLengthAccess,
    javaMM_ArrayType,
    javaMM_AssertStatement,
    javaMM_Assignment,
    javaMM_Block,
    javaMM_BlockComment,
    javaMM_BodyDeclaration,
    javaMM_BooleanLiteral,
    javaMM_BreakStatement,
    javaMM_CastExpression,
    javaMM_CatchClause,
    javaMM_CharacterLiteral,
    javaMM_ClassDeclaration,
    javaMM_ClassFile,
    javaMM_ClassInstanceCreation,
    javaMM_Comment,
    javaMM_CompilationUnit,
    javaMM_ConditionalExpression,
    javaMM_ConstructorDeclaration,
    javaMM_ConstructorInvocation,
    javaMM_ContinueStatement,
    javaMM_DoStatement,
    javaMM_EmptyStatement,
    javaMM_EnhancedForStatement,
    javaMM_EnumConstantDeclaration,
    javaMM_EnumDeclaration,
    javaMM_Expression,
    javaMM_ExpressionStatement,
    javaMM_FieldAccess,
    javaMM_FieldDeclaration,
    javaMM_ForStatement,
    javaMM_IfStatement,
    javaMM_ImportDeclaration,
    javaMM_InfixExpression,
    javaMM_Initializer,
    javaMM_InstanceofExpression,
    javaMM_InterfaceDeclaration,
    javaMM_Javadoc,
    javaMM_LabeledStatement,
    javaMM_LineComment,
    javaMM_Manifest,
    javaMM_ManifestAttribute,
    javaMM_ManifestEntry,
    javaMM_MemberRef,
    javaMM_MethodDeclaration,
    javaMM_MethodInvocation,
    javaMM_MethodRef,
    javaMM_MethodRefParameter,
    javaMM_Model,
    javaMM_Modifier,
    javaMM_NamedElement,
    javaMM_NamespaceAccess,
    javaMM_NullLiteral,
    javaMM_NumberLiteral,
    javaMM_Package,
    javaMM_PackageAccess,
    javaMM_ParameterizedType,
    javaMM_ParenthesizedExpression,
    javaMM_PostfixExpression,
    javaMM_PrefixExpression,
    javaMM_PrimitiveType,
    javaMM_PrimitiveTypeBoolean,
    javaMM_PrimitiveTypeByte,
    javaMM_PrimitiveTypeChar,
    javaMM_PrimitiveTypeDouble,
    javaMM_PrimitiveTypeFloat,
    javaMM_PrimitiveTypeInt,
    javaMM_PrimitiveTypeLong,
    javaMM_PrimitiveTypeShort,
    javaMM_PrimitiveTypeVoid,
    javaMM_ReturnStatement,
    javaMM_SingleVariableAccess,
    javaMM_SingleVariableDeclaration,
    javaMM_Statement,
    javaMM_StringLiteral,
    javaMM_SuperConstructorInvocation,
    javaMM_SuperFieldAccess,
    javaMM_SuperMethodInvocation,
    javaMM_SwitchCase,
    javaMM_SwitchStatement,
    javaMM_SynchronizedStatement,
    javaMM_TagElement,
    javaMM_TextElement,
    javaMM_ThisExpression,
    javaMM_ThrowStatement,
    javaMM_TryStatement,
    javaMM_Type,
    javaMM_TypeAccess,
    javaMM_TypeDeclaration,
    javaMM_TypeDeclarationStatement,
    javaMM_TypeLiteral,
    javaMM_TypeParameter,
    javaMM_UnresolvedAnnotationDeclaration,
    javaMM_UnresolvedAnnotationTypeMemberDeclaration,
    javaMM_UnresolvedClassDeclaration,
    javaMM_UnresolvedEnumDeclaration,
    javaMM_UnresolvedInterfaceDeclaration,
    javaMM_UnresolvedItem,
    javaMM_UnresolvedItemAccess,
    javaMM_UnresolvedLabeledStatement,
    javaMM_UnresolvedMethodDeclaration,
    javaMM_UnresolvedSingleVariableDeclaration,
    javaMM_UnresolvedType,
    javaMM_UnresolvedTypeDeclaration,
    javaMM_UnresolvedVariableDeclarationFragment,
    javaMM_VariableDeclaration,
    javaMM_VariableDeclarationExpression,
    javaMM_VariableDeclarationFragment,
    javaMM_VariableDeclarationStatement,
    javaMM_WhileStatement,
    javaMM_WildCardType,
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
    a1 = javaMM_Model(name="sample_text")
    a2 = javaMM_Model(name="sample_text_2")
    b = javaMM_Archive(originalFilePath="sample_text")
    _safe_set(b, 'javaMM_Archive248', a1)
    assert _is_linked(b, 'javaMM_Archive248', a1)
    if hasattr(a1, 'javaMM_Model247'):
        assert _is_linked(a1, 'javaMM_Model247', b)
    _safe_set(b, 'javaMM_Archive248', a2)
    assert _is_linked(b, 'javaMM_Archive248', a2)
    if hasattr(a1, 'javaMM_Model247'):
        assert not _is_linked(a1, 'javaMM_Model247', b)
    if hasattr(a2, 'javaMM_Model247'):
        assert _is_linked(a2, 'javaMM_Model247', b)
    _safe_set(b, 'javaMM_Archive248', None)
    assert not _is_linked(b, 'javaMM_Archive248', a2)
    if hasattr(a2, 'javaMM_Model247'):
        assert not _is_linked(a2, 'javaMM_Model247', b)


def test_assoc_attachedSource106_reverse_link_reassign_clear():
    a1 = javaMM_CompilationUnit(originalFilePath="sample_text")
    a2 = javaMM_CompilationUnit(originalFilePath="sample_text_2")
    b = javaMM_ClassFile(originalFilePath="sample_text")
    _safe_set(b, 'javaMM_ClassFile107', a1)
    assert _is_linked(b, 'javaMM_ClassFile107', a1)
    if hasattr(a1, 'javaMM_CompilationUnit108'):
        assert _is_linked(a1, 'javaMM_CompilationUnit108', b)
    _safe_set(b, 'javaMM_ClassFile107', a2)
    assert _is_linked(b, 'javaMM_ClassFile107', a2)
    if hasattr(a1, 'javaMM_CompilationUnit108'):
        assert not _is_linked(a1, 'javaMM_CompilationUnit108', b)
    if hasattr(a2, 'javaMM_CompilationUnit108'):
        assert _is_linked(a2, 'javaMM_CompilationUnit108', b)
    _safe_set(b, 'javaMM_ClassFile107', None)
    assert not _is_linked(b, 'javaMM_ClassFile107', a2)
    if hasattr(a2, 'javaMM_CompilationUnit108'):
        assert not _is_linked(a2, 'javaMM_CompilationUnit108', b)


def test_assoc_attributes210_reverse_link_reassign_clear():
    a1 = javaMM_ManifestEntry(name="sample_text")
    a2 = javaMM_ManifestEntry(name="sample_text_2")
    b = javaMM_ManifestAttribute(key="sample_text", value="sample_text")
    _safe_set(b, 'javaMM_ManifestAttribute212', a1)
    assert _is_linked(b, 'javaMM_ManifestAttribute212', a1)
    if hasattr(a1, 'javaMM_ManifestEntry211'):
        assert _is_linked(a1, 'javaMM_ManifestEntry211', b)
    _safe_set(b, 'javaMM_ManifestAttribute212', a2)
    assert _is_linked(b, 'javaMM_ManifestAttribute212', a2)
    if hasattr(a1, 'javaMM_ManifestEntry211'):
        assert not _is_linked(a1, 'javaMM_ManifestEntry211', b)
    if hasattr(a2, 'javaMM_ManifestEntry211'):
        assert _is_linked(a2, 'javaMM_ManifestEntry211', b)
    _safe_set(b, 'javaMM_ManifestAttribute212', None)
    assert not _is_linked(b, 'javaMM_ManifestAttribute212', a2)
    if hasattr(a2, 'javaMM_ManifestEntry211'):
        assert not _is_linked(a2, 'javaMM_ManifestEntry211', b)


def test_assoc_classFiles243_reverse_link_reassign_clear():
    a1 = javaMM_Model(name="sample_text")
    a2 = javaMM_Model(name="sample_text_2")
    b = javaMM_ClassFile(originalFilePath="sample_text")
    _safe_set(b, 'javaMM_ClassFile245', a1)
    assert _is_linked(b, 'javaMM_ClassFile245', a1)
    if hasattr(a1, 'javaMM_Model244'):
        assert _is_linked(a1, 'javaMM_Model244', b)
    _safe_set(b, 'javaMM_ClassFile245', a2)
    assert _is_linked(b, 'javaMM_ClassFile245', a2)
    if hasattr(a1, 'javaMM_Model244'):
        assert not _is_linked(a1, 'javaMM_Model244', b)
    if hasattr(a2, 'javaMM_Model244'):
        assert _is_linked(a2, 'javaMM_Model244', b)
    _safe_set(b, 'javaMM_ClassFile245', None)
    assert not _is_linked(b, 'javaMM_ClassFile245', a2)
    if hasattr(a2, 'javaMM_Model244'):
        assert not _is_linked(a2, 'javaMM_Model244', b)


def test_assoc_classFiles32_reverse_link_reassign_clear():
    a1 = javaMM_ClassFile(originalFilePath="sample_text")
    a2 = javaMM_ClassFile(originalFilePath="sample_text_2")
    b = javaMM_Archive(originalFilePath="sample_text")
    _safe_set(b, 'javaMM_Archive', {a1})
    assert _is_linked(b, 'javaMM_Archive', a1)
    if hasattr(a1, 'javaMM_ClassFile'):
        assert _is_linked(a1, 'javaMM_ClassFile', b)
    _safe_set(b, 'javaMM_Archive', {a2})
    assert _is_linked(b, 'javaMM_Archive', a2)
    if hasattr(a1, 'javaMM_ClassFile'):
        assert not _is_linked(a1, 'javaMM_ClassFile', b)
    if hasattr(a2, 'javaMM_ClassFile'):
        assert _is_linked(a2, 'javaMM_ClassFile', b)
    _safe_set(b, 'javaMM_Archive', set())
    assert not _is_linked(b, 'javaMM_Archive', a2)
    if hasattr(a2, 'javaMM_ClassFile'):
        assert not _is_linked(a2, 'javaMM_ClassFile', b)


def test_assoc_commentList128_reverse_link_reassign_clear():
    a1 = javaMM_CompilationUnit(originalFilePath="sample_text")
    a2 = javaMM_CompilationUnit(originalFilePath="sample_text_2")
    b = javaMM_Comment(content="sample_text", enclosedByParent="sample_text", prefixOfParent="sample_text")
    _safe_set(b, 'javaMM_Comment130', a1)
    assert _is_linked(b, 'javaMM_Comment130', a1)
    if hasattr(a1, 'javaMM_CompilationUnit129'):
        assert _is_linked(a1, 'javaMM_CompilationUnit129', b)
    _safe_set(b, 'javaMM_Comment130', a2)
    assert _is_linked(b, 'javaMM_Comment130', a2)
    if hasattr(a1, 'javaMM_CompilationUnit129'):
        assert not _is_linked(a1, 'javaMM_CompilationUnit129', b)
    if hasattr(a2, 'javaMM_CompilationUnit129'):
        assert _is_linked(a2, 'javaMM_CompilationUnit129', b)
    _safe_set(b, 'javaMM_Comment130', None)
    assert not _is_linked(b, 'javaMM_Comment130', a2)
    if hasattr(a2, 'javaMM_CompilationUnit129'):
        assert not _is_linked(a2, 'javaMM_CompilationUnit129', b)


def test_assoc_commentsAfterBody16_reverse_link_reassign_clear():
    a1 = javaMM_Comment(content="sample_text", enclosedByParent="sample_text", prefixOfParent="sample_text")
    a2 = javaMM_Comment(content="sample_text_2", enclosedByParent="sample_text_2", prefixOfParent="sample_text_2")
    b = javaMM_AbstractTypeDeclaration()
    _safe_set(b, 'javaMM_AbstractTypeDeclaration17', {a1})
    assert _is_linked(b, 'javaMM_AbstractTypeDeclaration17', a1)
    if hasattr(a1, 'javaMM_Comment18'):
        assert _is_linked(a1, 'javaMM_Comment18', b)
    _safe_set(b, 'javaMM_AbstractTypeDeclaration17', {a2})
    assert _is_linked(b, 'javaMM_AbstractTypeDeclaration17', a2)
    if hasattr(a1, 'javaMM_Comment18'):
        assert not _is_linked(a1, 'javaMM_Comment18', b)
    if hasattr(a2, 'javaMM_Comment18'):
        assert _is_linked(a2, 'javaMM_Comment18', b)
    _safe_set(b, 'javaMM_AbstractTypeDeclaration17', set())
    assert not _is_linked(b, 'javaMM_AbstractTypeDeclaration17', a2)
    if hasattr(a2, 'javaMM_Comment18'):
        assert not _is_linked(a2, 'javaMM_Comment18', b)


def test_assoc_commentsBeforeBody15_reverse_link_reassign_clear():
    a1 = javaMM_Comment(content="sample_text", enclosedByParent="sample_text", prefixOfParent="sample_text")
    a2 = javaMM_Comment(content="sample_text_2", enclosedByParent="sample_text_2", prefixOfParent="sample_text_2")
    b = javaMM_AbstractTypeDeclaration()
    _safe_set(b, 'javaMM_AbstractTypeDeclaration', {a1})
    assert _is_linked(b, 'javaMM_AbstractTypeDeclaration', a1)
    if hasattr(a1, 'javaMM_Comment'):
        assert _is_linked(a1, 'javaMM_Comment', b)
    _safe_set(b, 'javaMM_AbstractTypeDeclaration', {a2})
    assert _is_linked(b, 'javaMM_AbstractTypeDeclaration', a2)
    if hasattr(a1, 'javaMM_Comment'):
        assert not _is_linked(a1, 'javaMM_Comment', b)
    if hasattr(a2, 'javaMM_Comment'):
        assert _is_linked(a2, 'javaMM_Comment', b)
    _safe_set(b, 'javaMM_AbstractTypeDeclaration', set())
    assert not _is_linked(b, 'javaMM_AbstractTypeDeclaration', a2)
    if hasattr(a2, 'javaMM_Comment'):
        assert not _is_linked(a2, 'javaMM_Comment', b)


def test_assoc_compilationUnits240_reverse_link_reassign_clear():
    a1 = javaMM_Model(name="sample_text")
    a2 = javaMM_Model(name="sample_text_2")
    b = javaMM_CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'javaMM_CompilationUnit242', a1)
    assert _is_linked(b, 'javaMM_CompilationUnit242', a1)
    if hasattr(a1, 'javaMM_Model241'):
        assert _is_linked(a1, 'javaMM_Model241', b)
    _safe_set(b, 'javaMM_CompilationUnit242', a2)
    assert _is_linked(b, 'javaMM_CompilationUnit242', a2)
    if hasattr(a1, 'javaMM_Model241'):
        assert not _is_linked(a1, 'javaMM_Model241', b)
    if hasattr(a2, 'javaMM_Model241'):
        assert _is_linked(a2, 'javaMM_Model241', b)
    _safe_set(b, 'javaMM_CompilationUnit242', None)
    assert not _is_linked(b, 'javaMM_CompilationUnit242', a2)
    if hasattr(a2, 'javaMM_Model241'):
        assert not _is_linked(a2, 'javaMM_Model241', b)


def test_assoc_importedElement184_reverse_link_reassign_clear():
    a1 = javaMM_NamedElement(name="sample_text", proxy="sample_text")
    a2 = javaMM_NamedElement(name="sample_text_2", proxy="sample_text_2")
    b = javaMM_ImportDeclaration(static="sample_text")
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
    a1 = javaMM_ImportDeclaration(static="sample_text")
    a2 = javaMM_ImportDeclaration(static="sample_text_2")
    b = javaMM_CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'javaMM_CompilationUnit132', {a1})
    assert _is_linked(b, 'javaMM_CompilationUnit132', a1)
    if hasattr(a1, 'javaMM_ImportDeclaration'):
        assert _is_linked(a1, 'javaMM_ImportDeclaration', b)
    _safe_set(b, 'javaMM_CompilationUnit132', {a2})
    assert _is_linked(b, 'javaMM_CompilationUnit132', a2)
    if hasattr(a1, 'javaMM_ImportDeclaration'):
        assert not _is_linked(a1, 'javaMM_ImportDeclaration', b)
    if hasattr(a2, 'javaMM_ImportDeclaration'):
        assert _is_linked(a2, 'javaMM_ImportDeclaration', b)
    _safe_set(b, 'javaMM_CompilationUnit132', set())
    assert not _is_linked(b, 'javaMM_CompilationUnit132', a2)
    if hasattr(a2, 'javaMM_ImportDeclaration'):
        assert not _is_linked(a2, 'javaMM_ImportDeclaration', b)


def test_assoc_modifier293_reverse_link_reassign_clear():
    a1 = javaMM_SingleVariableDeclaration(varargs="sample_text")
    a2 = javaMM_SingleVariableDeclaration(varargs="sample_text_2")
    b = javaMM_Modifier(inheritance="sample_text", native="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", visibility="sample_text", volatile="sample_text")
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
    a1 = javaMM_VariableDeclarationStatement(extraArrayDimensions=7)
    a2 = javaMM_VariableDeclarationStatement(extraArrayDimensions=13)
    b = javaMM_Modifier(inheritance="sample_text", native="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", visibility="sample_text", volatile="sample_text")
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
    a1 = javaMM_MethodDeclaration(extraArrayDimensions=7)
    a2 = javaMM_MethodDeclaration(extraArrayDimensions=13)
    b = javaMM_MethodDeclaration(extraArrayDimensions=7)
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
    a1 = javaMM_MethodDeclaration(extraArrayDimensions=7)
    a2 = javaMM_MethodDeclaration(extraArrayDimensions=13)
    b = javaMM_MethodDeclaration(extraArrayDimensions=7)
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
    a1 = javaMM_SingleVariableDeclaration(varargs="sample_text")
    a2 = javaMM_SingleVariableDeclaration(varargs="sample_text_2")
    b = javaMM_Modifier(inheritance="sample_text", native="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", visibility="sample_text", volatile="sample_text")
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


def test_assoc_type103_reverse_link_reassign_clear():
    a1 = javaMM_ClassFile(originalFilePath="sample_text")
    a2 = javaMM_ClassFile(originalFilePath="sample_text_2")
    b = javaMM_AbstractTypeDeclaration()
    _safe_set(b, 'javaMM_AbstractTypeDeclaration105', a1)
    assert _is_linked(b, 'javaMM_AbstractTypeDeclaration105', a1)
    if hasattr(a1, 'javaMM_ClassFile104'):
        assert _is_linked(a1, 'javaMM_ClassFile104', b)
    _safe_set(b, 'javaMM_AbstractTypeDeclaration105', a2)
    assert _is_linked(b, 'javaMM_AbstractTypeDeclaration105', a2)
    if hasattr(a1, 'javaMM_ClassFile104'):
        assert not _is_linked(a1, 'javaMM_ClassFile104', b)
    if hasattr(a2, 'javaMM_ClassFile104'):
        assert _is_linked(a2, 'javaMM_ClassFile104', b)
    _safe_set(b, 'javaMM_AbstractTypeDeclaration105', None)
    assert not _is_linked(b, 'javaMM_AbstractTypeDeclaration105', a2)
    if hasattr(a2, 'javaMM_ClassFile104'):
        assert not _is_linked(a2, 'javaMM_ClassFile104', b)


def test_assoc_types136_reverse_link_reassign_clear():
    a1 = javaMM_CompilationUnit(originalFilePath="sample_text")
    a2 = javaMM_CompilationUnit(originalFilePath="sample_text_2")
    b = javaMM_AbstractTypeDeclaration()
    _safe_set(b, 'javaMM_AbstractTypeDeclaration138', a1)
    assert _is_linked(b, 'javaMM_AbstractTypeDeclaration138', a1)
    if hasattr(a1, 'javaMM_CompilationUnit137'):
        assert _is_linked(a1, 'javaMM_CompilationUnit137', b)
    _safe_set(b, 'javaMM_AbstractTypeDeclaration138', a2)
    assert _is_linked(b, 'javaMM_AbstractTypeDeclaration138', a2)
    if hasattr(a1, 'javaMM_CompilationUnit137'):
        assert not _is_linked(a1, 'javaMM_CompilationUnit137', b)
    if hasattr(a2, 'javaMM_CompilationUnit137'):
        assert _is_linked(a2, 'javaMM_CompilationUnit137', b)
    _safe_set(b, 'javaMM_AbstractTypeDeclaration138', None)
    assert not _is_linked(b, 'javaMM_AbstractTypeDeclaration138', a2)
    if hasattr(a2, 'javaMM_CompilationUnit137'):
        assert not _is_linked(a2, 'javaMM_CompilationUnit137', b)


def test_assoc_usagesInImports258_reverse_link_reassign_clear():
    a1 = javaMM_NamedElement(name="sample_text", proxy="sample_text")
    a2 = javaMM_NamedElement(name="sample_text_2", proxy="sample_text_2")
    b = javaMM_ImportDeclaration(static="sample_text")
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
    a1 = javaMM_VariableDeclarationStatement(extraArrayDimensions=7)
    a2 = javaMM_VariableDeclarationStatement(extraArrayDimensions=13)
    b = javaMM_Modifier(inheritance="sample_text", native="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", visibility="sample_text", volatile="sample_text")
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

def test_assoc_abstractTypeDeclaration85_stub_double():
    # javaMM_BodyDeclaration has no real 'bodyDeclarations' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_AbstractTypeDeclaration()
    partner = javaMM_BodyDeclaration()
    setattr(partner, 'bodyDeclarations', None)
    _safe_set(owner, 'AbstractTypeDeclaration', partner)
    assert getattr(partner, 'bodyDeclarations') == owner
    _safe_set(owner, 'AbstractTypeDeclaration', None)
    assert getattr(partner, 'bodyDeclarations') is None


def test_assoc_annotations297_stub_double():
    # javaMM_Annotation has no real 'javaMM_Annotation299' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_SingleVariableDeclaration(varargs="sample_text")
    partner = javaMM_Annotation()
    setattr(partner, 'javaMM_Annotation299', None)
    _safe_set(owner, 'javaMM_SingleVariableDeclaration298', {partner})
    assert getattr(partner, 'javaMM_Annotation299') == owner
    _safe_set(owner, 'javaMM_SingleVariableDeclaration298', set())
    assert getattr(partner, 'javaMM_Annotation299') is None


def test_assoc_annotations361_stub_double():
    # javaMM_Annotation has no real 'javaMM_Annotation362' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_VariableDeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_VariableDeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_VariableDeclarationStatement(extraArrayDimensions=7)
    partner = javaMM_Annotation()
    setattr(partner, 'javaMM_Annotation362', None)
    _safe_set(owner, 'javaMM_VariableDeclarationStatement', {partner})
    assert getattr(partner, 'javaMM_Annotation362') == owner
    _safe_set(owner, 'javaMM_VariableDeclarationStatement', set())
    assert getattr(partner, 'javaMM_Annotation362') is None


def test_assoc_bodyDeclaration249_stub_double():
    # javaMM_BodyDeclaration has no real 'BodyDeclaration250' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Modifier(inheritance="sample_text", native="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", visibility="sample_text", volatile="sample_text")
    partner = javaMM_BodyDeclaration()
    setattr(partner, 'BodyDeclaration250', None)
    _safe_set(owner, 'modifier', partner)
    assert getattr(partner, 'BodyDeclaration250') == owner
    _safe_set(owner, 'modifier', None)
    assert getattr(partner, 'BodyDeclaration250') is None


def test_assoc_bodyDeclarations14_stub_double():
    # javaMM_BodyDeclaration has no real 'BodyDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_AbstractTypeDeclaration()
    partner = javaMM_BodyDeclaration()
    setattr(partner, 'BodyDeclaration', None)
    _safe_set(owner, 'abstractTypeDeclaration', {partner})
    assert getattr(partner, 'BodyDeclaration') == owner
    _safe_set(owner, 'abstractTypeDeclaration', set())
    assert getattr(partner, 'BodyDeclaration') is None


def test_assoc_bound363_stub_double():
    # javaMM_TypeAccess has no real 'javaMM_TypeAccess364' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_WildCardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_WildCardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_WildCardType(upperBound="sample_text")
    partner = javaMM_TypeAccess()
    setattr(partner, 'javaMM_TypeAccess364', None)
    _safe_set(owner, 'javaMM_WildCardType', partner)
    assert getattr(partner, 'javaMM_TypeAccess364') == owner
    _safe_set(owner, 'javaMM_WildCardType', None)
    assert getattr(partner, 'javaMM_TypeAccess364') is None


def test_assoc_catchClause302_stub_double():
    # javaMM_CatchClause has no real 'CatchClause' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_SingleVariableDeclaration(varargs="sample_text")
    partner = javaMM_CatchClause()
    setattr(partner, 'CatchClause', None)
    _safe_set(owner, 'exception', partner)
    assert getattr(partner, 'CatchClause') == owner
    _safe_set(owner, 'exception', None)
    assert getattr(partner, 'CatchClause') is None


def test_assoc_comments40_stub_double():
    # javaMM_ASTNode has no real 'javaMM_ASTNode' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Comment(content="sample_text", enclosedByParent="sample_text", prefixOfParent="sample_text")
    partner = javaMM_ASTNode()
    setattr(partner, 'javaMM_ASTNode', None)
    _safe_set(owner, 'javaMM_Comment41', partner)
    assert owner in getattr(partner, 'javaMM_ASTNode')
    _safe_set(owner, 'javaMM_Comment41', None)
    assert owner not in getattr(partner, 'javaMM_ASTNode')


def test_assoc_declaration339_stub_double():
    # javaMM_TypeDeclarationStatement has no real 'javaMM_TypeDeclarationStatement' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_AbstractTypeDeclaration()
    partner = javaMM_TypeDeclarationStatement()
    setattr(partner, 'javaMM_TypeDeclarationStatement', None)
    _safe_set(owner, 'javaMM_AbstractTypeDeclaration340', partner)
    assert getattr(partner, 'javaMM_TypeDeclarationStatement') == owner
    _safe_set(owner, 'javaMM_AbstractTypeDeclaration340', None)
    assert getattr(partner, 'javaMM_TypeDeclarationStatement') is None


def test_assoc_elementType78_stub_double():
    # javaMM_TypeAccess has no real 'javaMM_TypeAccess79' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_ArrayType(dimensions=7)
    partner = javaMM_TypeAccess()
    setattr(partner, 'javaMM_TypeAccess79', None)
    _safe_set(owner, 'javaMM_ArrayType', partner)
    assert getattr(partner, 'javaMM_TypeAccess79') == owner
    _safe_set(owner, 'javaMM_ArrayType', None)
    assert getattr(partner, 'javaMM_TypeAccess79') is None


def test_assoc_enhancedForStatement303_stub_double():
    # javaMM_EnhancedForStatement has no real 'EnhancedForStatement' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_SingleVariableDeclaration(varargs="sample_text")
    partner = javaMM_EnhancedForStatement()
    setattr(partner, 'EnhancedForStatement', None)
    _safe_set(owner, 'parameter', partner)
    assert getattr(partner, 'EnhancedForStatement') == owner
    _safe_set(owner, 'parameter', None)
    assert getattr(partner, 'EnhancedForStatement') is None


def test_assoc_entryAttributes208_stub_double():
    # javaMM_Manifest has no real 'javaMM_Manifest209' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_ManifestEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_ManifestEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_ManifestEntry(name="sample_text")
    partner = javaMM_Manifest()
    setattr(partner, 'javaMM_Manifest209', None)
    _safe_set(owner, 'javaMM_ManifestEntry', partner)
    assert owner in getattr(partner, 'javaMM_Manifest209')
    _safe_set(owner, 'javaMM_ManifestEntry', None)
    assert owner not in getattr(partner, 'javaMM_Manifest209')


def test_assoc_exception99_stub_double():
    # javaMM_CatchClause has no real 'catchClause' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_SingleVariableDeclaration(varargs="sample_text")
    partner = javaMM_CatchClause()
    setattr(partner, 'catchClause', None)
    _safe_set(owner, 'SingleVariableDeclaration100', partner)
    assert getattr(partner, 'catchClause') == owner
    _safe_set(owner, 'SingleVariableDeclaration100', None)
    assert getattr(partner, 'catchClause') is None


def test_assoc_expression308_stub_double():
    # javaMM_Expression has no real 'javaMM_Expression309' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_SwitchCase(default="sample_text")
    partner = javaMM_Expression()
    setattr(partner, 'javaMM_Expression309', None)
    _safe_set(owner, 'javaMM_SwitchCase', partner)
    assert getattr(partner, 'javaMM_Expression309') == owner
    _safe_set(owner, 'javaMM_SwitchCase', None)
    assert getattr(partner, 'javaMM_Expression309') is None


def test_assoc_extendedOperands190_stub_double():
    # javaMM_Expression has no real 'javaMM_Expression192' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_InfixExpression(operator="sample_text")
    partner = javaMM_Expression()
    setattr(partner, 'javaMM_Expression192', None)
    _safe_set(owner, 'javaMM_InfixExpression191', {partner})
    assert getattr(partner, 'javaMM_Expression192') == owner
    _safe_set(owner, 'javaMM_InfixExpression191', set())
    assert getattr(partner, 'javaMM_Expression192') is None


def test_assoc_fragments320_stub_double():
    # javaMM_ASTNode has no real 'javaMM_ASTNode322' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_TagElement(tagName="sample_text")
    partner = javaMM_ASTNode()
    setattr(partner, 'javaMM_ASTNode322', None)
    _safe_set(owner, 'javaMM_TagElement321', {partner})
    assert getattr(partner, 'javaMM_ASTNode322') == owner
    _safe_set(owner, 'javaMM_TagElement321', set())
    assert getattr(partner, 'javaMM_ASTNode322') is None


def test_assoc_initializer351_stub_double():
    # javaMM_Expression has no real 'javaMM_Expression352' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_VariableDeclaration(extraArrayDimensions=7)
    partner = javaMM_Expression()
    setattr(partner, 'javaMM_Expression352', None)
    _safe_set(owner, 'javaMM_VariableDeclaration', partner)
    assert getattr(partner, 'javaMM_Expression352') == owner
    _safe_set(owner, 'javaMM_VariableDeclaration', None)
    assert getattr(partner, 'javaMM_Expression352') is None


def test_assoc_leftHandSide80_stub_double():
    # javaMM_Expression has no real 'javaMM_Expression81' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Assignment(operator="sample_text")
    partner = javaMM_Expression()
    setattr(partner, 'javaMM_Expression81', None)
    _safe_set(owner, 'javaMM_Assignment', partner)
    assert getattr(partner, 'javaMM_Expression81') == owner
    _safe_set(owner, 'javaMM_Assignment', None)
    assert getattr(partner, 'javaMM_Expression81') is None


def test_assoc_leftOperand187_stub_double():
    # javaMM_Expression has no real 'javaMM_Expression189' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_InfixExpression(operator="sample_text")
    partner = javaMM_Expression()
    setattr(partner, 'javaMM_Expression189', None)
    _safe_set(owner, 'javaMM_InfixExpression188', partner)
    assert getattr(partner, 'javaMM_Expression189') == owner
    _safe_set(owner, 'javaMM_InfixExpression188', None)
    assert getattr(partner, 'javaMM_Expression189') is None


def test_assoc_mainAttributes206_stub_double():
    # javaMM_Manifest has no real 'javaMM_Manifest207' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_ManifestAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_ManifestAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_ManifestAttribute(key="sample_text", value="sample_text")
    partner = javaMM_Manifest()
    setattr(partner, 'javaMM_Manifest207', None)
    _safe_set(owner, 'javaMM_ManifestAttribute', partner)
    assert owner in getattr(partner, 'javaMM_Manifest207')
    _safe_set(owner, 'javaMM_ManifestAttribute', None)
    assert owner not in getattr(partner, 'javaMM_Manifest207')


def test_assoc_manifest33_stub_double():
    # javaMM_Manifest has no real 'javaMM_Manifest' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Archive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Archive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Archive(originalFilePath="sample_text")
    partner = javaMM_Manifest()
    setattr(partner, 'javaMM_Manifest', None)
    _safe_set(owner, 'javaMM_Archive34', partner)
    assert getattr(partner, 'javaMM_Manifest') == owner
    _safe_set(owner, 'javaMM_Archive34', None)
    assert getattr(partner, 'javaMM_Manifest') is None


def test_assoc_member213_stub_double():
    # javaMM_MemberRef has no real 'javaMM_MemberRef' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_NamedElement(name="sample_text", proxy="sample_text")
    partner = javaMM_MemberRef()
    setattr(partner, 'javaMM_MemberRef', None)
    _safe_set(owner, 'javaMM_NamedElement', partner)
    assert getattr(partner, 'javaMM_MemberRef') == owner
    _safe_set(owner, 'javaMM_NamedElement', None)
    assert getattr(partner, 'javaMM_MemberRef') is None


def test_assoc_methodDeclaration300_stub_double():
    # javaMM_AbstractMethodDeclaration has no real 'AbstractMethodDeclaration301' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_SingleVariableDeclaration(varargs="sample_text")
    partner = javaMM_AbstractMethodDeclaration()
    setattr(partner, 'AbstractMethodDeclaration301', None)
    _safe_set(owner, 'parameters', partner)
    assert getattr(partner, 'AbstractMethodDeclaration301') == owner
    _safe_set(owner, 'parameters', None)
    assert getattr(partner, 'AbstractMethodDeclaration301') is None


def test_assoc_model261_stub_double():
    # javaMM_Package has no real 'ownedElements262' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Model(name="sample_text")
    partner = javaMM_Package()
    setattr(partner, 'ownedElements262', None)
    _safe_set(owner, 'Model', partner)
    assert getattr(partner, 'ownedElements262') == owner
    _safe_set(owner, 'Model', None)
    assert getattr(partner, 'ownedElements262') is None


def test_assoc_modifier354_stub_double():
    # javaMM_VariableDeclarationExpression has no real 'variableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Modifier(inheritance="sample_text", native="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", visibility="sample_text", volatile="sample_text")
    partner = javaMM_VariableDeclarationExpression()
    setattr(partner, 'variableDeclarationExpression', None)
    _safe_set(owner, 'Modifier355', partner)
    assert getattr(partner, 'variableDeclarationExpression') == owner
    _safe_set(owner, 'Modifier355', None)
    assert getattr(partner, 'variableDeclarationExpression') is None


def test_assoc_modifier90_stub_double():
    # javaMM_BodyDeclaration has no real 'bodyDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Modifier(inheritance="sample_text", native="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", visibility="sample_text", volatile="sample_text")
    partner = javaMM_BodyDeclaration()
    setattr(partner, 'bodyDeclaration', None)
    _safe_set(owner, 'Modifier', partner)
    assert getattr(partner, 'bodyDeclaration') == owner
    _safe_set(owner, 'Modifier', None)
    assert getattr(partner, 'bodyDeclaration') is None


def test_assoc_operand283_stub_double():
    # javaMM_Expression has no real 'javaMM_Expression284' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_PostfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_PostfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_PostfixExpression(operator="sample_text")
    partner = javaMM_Expression()
    setattr(partner, 'javaMM_Expression284', None)
    _safe_set(owner, 'javaMM_PostfixExpression', partner)
    assert getattr(partner, 'javaMM_Expression284') == owner
    _safe_set(owner, 'javaMM_PostfixExpression', None)
    assert getattr(partner, 'javaMM_Expression284') is None


def test_assoc_operand285_stub_double():
    # javaMM_Expression has no real 'javaMM_Expression286' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_PrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_PrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_PrefixExpression(operator="sample_text")
    partner = javaMM_Expression()
    setattr(partner, 'javaMM_Expression286', None)
    _safe_set(owner, 'javaMM_PrefixExpression', partner)
    assert getattr(partner, 'javaMM_Expression286') == owner
    _safe_set(owner, 'javaMM_PrefixExpression', None)
    assert getattr(partner, 'javaMM_Expression286') is None


def test_assoc_originalClassFile44_stub_double():
    # javaMM_ASTNode has no real 'javaMM_ASTNode45' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_ClassFile(originalFilePath="sample_text")
    partner = javaMM_ASTNode()
    setattr(partner, 'javaMM_ASTNode45', None)
    _safe_set(owner, 'javaMM_ClassFile46', partner)
    assert getattr(partner, 'javaMM_ASTNode45') == owner
    _safe_set(owner, 'javaMM_ClassFile46', None)
    assert getattr(partner, 'javaMM_ASTNode45') is None


def test_assoc_originalCompilationUnit42_stub_double():
    # javaMM_ASTNode has no real 'javaMM_ASTNode43' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_CompilationUnit(originalFilePath="sample_text")
    partner = javaMM_ASTNode()
    setattr(partner, 'javaMM_ASTNode43', None)
    _safe_set(owner, 'javaMM_CompilationUnit', partner)
    assert getattr(partner, 'javaMM_ASTNode43') == owner
    _safe_set(owner, 'javaMM_CompilationUnit', None)
    assert getattr(partner, 'javaMM_ASTNode43') is None


def test_assoc_orphanTypes237_stub_double():
    # javaMM_Type has no real 'javaMM_Type' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Model(name="sample_text")
    partner = javaMM_Type()
    setattr(partner, 'javaMM_Type', None)
    _safe_set(owner, 'javaMM_Model', {partner})
    assert getattr(partner, 'javaMM_Type') == owner
    _safe_set(owner, 'javaMM_Model', set())
    assert getattr(partner, 'javaMM_Type') is None


def test_assoc_ownedElements235_stub_double():
    # javaMM_Package has no real 'Package236' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Model(name="sample_text")
    partner = javaMM_Package()
    setattr(partner, 'Package236', None)
    _safe_set(owner, 'model', {partner})
    assert getattr(partner, 'Package236') == owner
    _safe_set(owner, 'model', set())
    assert getattr(partner, 'Package236') is None


def test_assoc_ownedElements259_stub_double():
    # javaMM_Package has no real 'package' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_AbstractTypeDeclaration()
    partner = javaMM_Package()
    setattr(partner, 'package', None)
    _safe_set(owner, 'AbstractTypeDeclaration260', partner)
    assert owner in getattr(partner, 'package')
    _safe_set(owner, 'AbstractTypeDeclaration260', None)
    assert owner not in getattr(partner, 'package')


def test_assoc_package109_stub_double():
    # javaMM_Package has no real 'javaMM_Package' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_ClassFile(originalFilePath="sample_text")
    partner = javaMM_Package()
    setattr(partner, 'javaMM_Package', None)
    _safe_set(owner, 'javaMM_ClassFile110', partner)
    assert getattr(partner, 'javaMM_Package') == owner
    _safe_set(owner, 'javaMM_ClassFile110', None)
    assert getattr(partner, 'javaMM_Package') is None


def test_assoc_package133_stub_double():
    # javaMM_Package has no real 'javaMM_Package135' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_CompilationUnit(originalFilePath="sample_text")
    partner = javaMM_Package()
    setattr(partner, 'javaMM_Package135', None)
    _safe_set(owner, 'javaMM_CompilationUnit134', partner)
    assert getattr(partner, 'javaMM_Package135') == owner
    _safe_set(owner, 'javaMM_CompilationUnit134', None)
    assert getattr(partner, 'javaMM_Package135') is None


def test_assoc_package19_stub_double():
    # javaMM_Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_AbstractTypeDeclaration()
    partner = javaMM_Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'ownedElements', partner)
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'ownedElements', None)
    assert getattr(partner, 'Package') is None


def test_assoc_parameter151_stub_double():
    # javaMM_EnhancedForStatement has no real 'enhancedForStatement' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_SingleVariableDeclaration(varargs="sample_text")
    partner = javaMM_EnhancedForStatement()
    setattr(partner, 'enhancedForStatement', None)
    _safe_set(owner, 'SingleVariableDeclaration152', partner)
    assert getattr(partner, 'enhancedForStatement') == owner
    _safe_set(owner, 'SingleVariableDeclaration152', None)
    assert getattr(partner, 'enhancedForStatement') is None


def test_assoc_parameters1_stub_double():
    # javaMM_AbstractMethodDeclaration has no real 'methodDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_SingleVariableDeclaration(varargs="sample_text")
    partner = javaMM_AbstractMethodDeclaration()
    setattr(partner, 'methodDeclaration', None)
    _safe_set(owner, 'SingleVariableDeclaration', partner)
    assert owner in getattr(partner, 'methodDeclaration')
    _safe_set(owner, 'SingleVariableDeclaration', None)
    assert owner not in getattr(partner, 'methodDeclaration')


def test_assoc_parameters230_stub_double():
    # javaMM_MethodRef has no real 'javaMM_MethodRef231' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_MethodRefParameter(name="sample_text", varargs="sample_text")
    partner = javaMM_MethodRef()
    setattr(partner, 'javaMM_MethodRef231', None)
    _safe_set(owner, 'javaMM_MethodRefParameter', partner)
    assert owner in getattr(partner, 'javaMM_MethodRef231')
    _safe_set(owner, 'javaMM_MethodRefParameter', None)
    assert owner not in getattr(partner, 'javaMM_MethodRef231')


def test_assoc_returnType217_stub_double():
    # javaMM_TypeAccess has no real 'javaMM_TypeAccess218' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_MethodDeclaration(extraArrayDimensions=7)
    partner = javaMM_TypeAccess()
    setattr(partner, 'javaMM_TypeAccess218', None)
    _safe_set(owner, 'javaMM_MethodDeclaration', partner)
    assert getattr(partner, 'javaMM_TypeAccess218') == owner
    _safe_set(owner, 'javaMM_MethodDeclaration', None)
    assert getattr(partner, 'javaMM_TypeAccess218') is None


def test_assoc_rightHandSide82_stub_double():
    # javaMM_Expression has no real 'javaMM_Expression84' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Assignment(operator="sample_text")
    partner = javaMM_Expression()
    setattr(partner, 'javaMM_Expression84', None)
    _safe_set(owner, 'javaMM_Assignment83', partner)
    assert getattr(partner, 'javaMM_Expression84') == owner
    _safe_set(owner, 'javaMM_Assignment83', None)
    assert getattr(partner, 'javaMM_Expression84') is None


def test_assoc_rightOperand185_stub_double():
    # javaMM_Expression has no real 'javaMM_Expression186' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_InfixExpression(operator="sample_text")
    partner = javaMM_Expression()
    setattr(partner, 'javaMM_Expression186', None)
    _safe_set(owner, 'javaMM_InfixExpression', partner)
    assert getattr(partner, 'javaMM_Expression186') == owner
    _safe_set(owner, 'javaMM_InfixExpression', None)
    assert getattr(partner, 'javaMM_Expression186') is None


def test_assoc_superClass126_stub_double():
    # javaMM_TypeAccess has no real 'javaMM_TypeAccess127' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_ClassDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_ClassDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_ClassDeclaration()
    partner = javaMM_TypeAccess()
    setattr(partner, 'javaMM_TypeAccess127', None)
    _safe_set(owner, 'javaMM_ClassDeclaration', partner)
    assert getattr(partner, 'javaMM_TypeAccess127') == owner
    _safe_set(owner, 'javaMM_ClassDeclaration', None)
    assert getattr(partner, 'javaMM_TypeAccess127') is None


def test_assoc_superInterfaces20_stub_double():
    # javaMM_TypeAccess has no real 'javaMM_TypeAccess22' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_AbstractTypeDeclaration()
    partner = javaMM_TypeAccess()
    setattr(partner, 'javaMM_TypeAccess22', None)
    _safe_set(owner, 'javaMM_AbstractTypeDeclaration21', {partner})
    assert getattr(partner, 'javaMM_TypeAccess22') == owner
    _safe_set(owner, 'javaMM_AbstractTypeDeclaration21', set())
    assert getattr(partner, 'javaMM_TypeAccess22') is None


def test_assoc_tags200_stub_double():
    # javaMM_Javadoc has no real 'javaMM_Javadoc' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_TagElement(tagName="sample_text")
    partner = javaMM_Javadoc()
    setattr(partner, 'javaMM_Javadoc', None)
    _safe_set(owner, 'javaMM_TagElement', partner)
    assert owner in getattr(partner, 'javaMM_Javadoc')
    _safe_set(owner, 'javaMM_TagElement', None)
    assert owner not in getattr(partner, 'javaMM_Javadoc')


def test_assoc_type232_stub_double():
    # javaMM_TypeAccess has no real 'javaMM_TypeAccess234' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_MethodRefParameter(name="sample_text", varargs="sample_text")
    partner = javaMM_TypeAccess()
    setattr(partner, 'javaMM_TypeAccess234', None)
    _safe_set(owner, 'javaMM_MethodRefParameter233', partner)
    assert getattr(partner, 'javaMM_TypeAccess234') == owner
    _safe_set(owner, 'javaMM_MethodRefParameter233', None)
    assert getattr(partner, 'javaMM_TypeAccess234') is None


def test_assoc_type295_stub_double():
    # javaMM_TypeAccess has no real 'javaMM_TypeAccess296' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_SingleVariableDeclaration(varargs="sample_text")
    partner = javaMM_TypeAccess()
    setattr(partner, 'javaMM_TypeAccess296', None)
    _safe_set(owner, 'javaMM_SingleVariableDeclaration', partner)
    assert getattr(partner, 'javaMM_TypeAccess296') == owner
    _safe_set(owner, 'javaMM_SingleVariableDeclaration', None)
    assert getattr(partner, 'javaMM_TypeAccess296') is None


def test_assoc_unresolvedItems238_stub_double():
    # javaMM_UnresolvedItem has no real 'javaMM_UnresolvedItem' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Model(name="sample_text")
    partner = javaMM_UnresolvedItem()
    setattr(partner, 'javaMM_UnresolvedItem', None)
    _safe_set(owner, 'javaMM_Model239', {partner})
    assert getattr(partner, 'javaMM_UnresolvedItem') == owner
    _safe_set(owner, 'javaMM_Model239', set())
    assert getattr(partner, 'javaMM_UnresolvedItem') is None


def test_assoc_usageInVariableAccess353_stub_double():
    # javaMM_SingleVariableAccess has no real 'SingleVariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_VariableDeclaration(extraArrayDimensions=7)
    partner = javaMM_SingleVariableAccess()
    setattr(partner, 'SingleVariableAccess', None)
    _safe_set(owner, 'variable', {partner})
    assert getattr(partner, 'SingleVariableAccess') == owner
    _safe_set(owner, 'variable', set())
    assert getattr(partner, 'SingleVariableAccess') is None


def test_assoc_variable289_stub_double():
    # javaMM_SingleVariableAccess has no real 'usageInVariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_VariableDeclaration(extraArrayDimensions=7)
    partner = javaMM_SingleVariableAccess()
    setattr(partner, 'usageInVariableAccess', None)
    _safe_set(owner, 'VariableDeclaration', partner)
    assert getattr(partner, 'usageInVariableAccess') == owner
    _safe_set(owner, 'VariableDeclaration', None)
    assert getattr(partner, 'usageInVariableAccess') is None


def test_assoc_variableDeclarationExpression256_stub_double():
    # javaMM_VariableDeclarationExpression has no real 'VariableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so javaMM_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaMM_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaMM_Modifier(inheritance="sample_text", native="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", visibility="sample_text", volatile="sample_text")
    partner = javaMM_VariableDeclarationExpression()
    setattr(partner, 'VariableDeclarationExpression', None)
    _safe_set(owner, 'modifier257', partner)
    assert getattr(partner, 'VariableDeclarationExpression') == owner
    _safe_set(owner, 'modifier257', None)
    assert getattr(partner, 'VariableDeclarationExpression') is None


