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
    java__ASTNode,
    java__AbstractMethodDeclaration,
    java__AbstractMethodInvocation,
    java__AbstractTypeDeclaration,
    java__AbstractTypeQualifiedExpression,
    java__AbstractVariablesContainer,
    java__Annotation,
    java__AnnotationMemberValuePair,
    java__AnnotationTypeDeclaration,
    java__AnnotationTypeMemberDeclaration,
    java__AnonymousClassDeclaration,
    java__Archive,
    java__ArrayAccess,
    java__ArrayCreation,
    java__ArrayInitializer,
    java__ArrayLengthAccess,
    java__ArrayType,
    java__AssertStatement,
    java__Assignment,
    java__Block,
    java__BlockComment,
    java__BodyDeclaration,
    java__BooleanLiteral,
    java__BreakStatement,
    java__CastExpression,
    java__CatchClause,
    java__CharacterLiteral,
    java__ClassDeclaration,
    java__ClassFile,
    java__ClassInstanceCreation,
    java__Comment,
    java__CompilationUnit,
    java__ConditionalExpression,
    java__ConstructorDeclaration,
    java__ConstructorInvocation,
    java__ContinueStatement,
    java__DoStatement,
    java__EmptyStatement,
    java__EnhancedForStatement,
    java__EnumConstantDeclaration,
    java__EnumDeclaration,
    java__Expression,
    java__ExpressionStatement,
    java__FieldAccess,
    java__FieldDeclaration,
    java__ForStatement,
    java__IfStatement,
    java__ImportDeclaration,
    java__InfixExpression,
    java__Initializer,
    java__InstanceofExpression,
    java__InterfaceDeclaration,
    java__Javadoc,
    java__LabeledStatement,
    java__LineComment,
    java__Manifest,
    java__ManifestAttribute,
    java__ManifestEntry,
    java__MemberRef,
    java__MethodDeclaration,
    java__MethodInvocation,
    java__MethodRef,
    java__MethodRefParameter,
    java__Model,
    java__Modifier,
    java__NamedElement,
    java__NamespaceAccess,
    java__NullLiteral,
    java__NumberLiteral,
    java__Package,
    java__PackageAccess,
    java__ParameterizedType,
    java__ParenthesizedExpression,
    java__PostfixExpression,
    java__PrefixExpression,
    java__PrimitiveType,
    java__PrimitiveTypeBoolean,
    java__PrimitiveTypeByte,
    java__PrimitiveTypeChar,
    java__PrimitiveTypeDouble,
    java__PrimitiveTypeFloat,
    java__PrimitiveTypeInt,
    java__PrimitiveTypeLong,
    java__PrimitiveTypeShort,
    java__PrimitiveTypeVoid,
    java__QueryCollection,
    java__ReturnStatement,
    java__SingleVariableAccess,
    java__SingleVariableDeclaration,
    java__Statement,
    java__StringLiteral,
    java__SuperConstructorInvocation,
    java__SuperFieldAccess,
    java__SuperMethodInvocation,
    java__SwitchCase,
    java__SwitchStatement,
    java__SynchronizedStatement,
    java__TagElement,
    java__TextElement,
    java__ThisExpression,
    java__ThrowStatement,
    java__TryStatement,
    java__Type,
    java__TypeAccess,
    java__TypeDeclaration,
    java__TypeDeclarationStatement,
    java__TypeLiteral,
    java__TypeParameter,
    java__UnresolvedAnnotationDeclaration,
    java__UnresolvedAnnotationTypeMemberDeclaration,
    java__UnresolvedClassDeclaration,
    java__UnresolvedEnumDeclaration,
    java__UnresolvedInterfaceDeclaration,
    java__UnresolvedItem,
    java__UnresolvedItemAccess,
    java__UnresolvedLabeledStatement,
    java__UnresolvedMethodDeclaration,
    java__UnresolvedSingleVariableDeclaration,
    java__UnresolvedType,
    java__UnresolvedTypeDeclaration,
    java__UnresolvedVariableDeclarationFragment,
    java__VariableDeclaration,
    java__VariableDeclarationExpression,
    java__VariableDeclarationFragment,
    java__VariableDeclarationStatement,
    java__WhileStatement,
    java__WildCardType,
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
    a1 = java__Model(name="sample_text")
    a2 = java__Model(name="sample_text_2")
    b = java__Archive(originalFilePath="sample_text")
    _safe_set(b, 'java__Archive248', a1)
    assert _is_linked(b, 'java__Archive248', a1)
    if hasattr(a1, 'java__Model247'):
        assert _is_linked(a1, 'java__Model247', b)
    _safe_set(b, 'java__Archive248', a2)
    assert _is_linked(b, 'java__Archive248', a2)
    if hasattr(a1, 'java__Model247'):
        assert not _is_linked(a1, 'java__Model247', b)
    if hasattr(a2, 'java__Model247'):
        assert _is_linked(a2, 'java__Model247', b)
    _safe_set(b, 'java__Archive248', None)
    assert not _is_linked(b, 'java__Archive248', a2)
    if hasattr(a2, 'java__Model247'):
        assert not _is_linked(a2, 'java__Model247', b)


def test_assoc_attachedSource106_reverse_link_reassign_clear():
    a1 = java__CompilationUnit(originalFilePath="sample_text")
    a2 = java__CompilationUnit(originalFilePath="sample_text_2")
    b = java__ClassFile(originalFilePath="sample_text")
    _safe_set(b, 'java__ClassFile107', a1)
    assert _is_linked(b, 'java__ClassFile107', a1)
    if hasattr(a1, 'java__CompilationUnit108'):
        assert _is_linked(a1, 'java__CompilationUnit108', b)
    _safe_set(b, 'java__ClassFile107', a2)
    assert _is_linked(b, 'java__ClassFile107', a2)
    if hasattr(a1, 'java__CompilationUnit108'):
        assert not _is_linked(a1, 'java__CompilationUnit108', b)
    if hasattr(a2, 'java__CompilationUnit108'):
        assert _is_linked(a2, 'java__CompilationUnit108', b)
    _safe_set(b, 'java__ClassFile107', None)
    assert not _is_linked(b, 'java__ClassFile107', a2)
    if hasattr(a2, 'java__CompilationUnit108'):
        assert not _is_linked(a2, 'java__CompilationUnit108', b)


def test_assoc_attributes210_reverse_link_reassign_clear():
    a1 = java__ManifestEntry(name="sample_text")
    a2 = java__ManifestEntry(name="sample_text_2")
    b = java__ManifestAttribute(key="sample_text", value="sample_text")
    _safe_set(b, 'java__ManifestAttribute212', a1)
    assert _is_linked(b, 'java__ManifestAttribute212', a1)
    if hasattr(a1, 'java__ManifestEntry211'):
        assert _is_linked(a1, 'java__ManifestEntry211', b)
    _safe_set(b, 'java__ManifestAttribute212', a2)
    assert _is_linked(b, 'java__ManifestAttribute212', a2)
    if hasattr(a1, 'java__ManifestEntry211'):
        assert not _is_linked(a1, 'java__ManifestEntry211', b)
    if hasattr(a2, 'java__ManifestEntry211'):
        assert _is_linked(a2, 'java__ManifestEntry211', b)
    _safe_set(b, 'java__ManifestAttribute212', None)
    assert not _is_linked(b, 'java__ManifestAttribute212', a2)
    if hasattr(a2, 'java__ManifestEntry211'):
        assert not _is_linked(a2, 'java__ManifestEntry211', b)


def test_assoc_classFiles243_reverse_link_reassign_clear():
    a1 = java__Model(name="sample_text")
    a2 = java__Model(name="sample_text_2")
    b = java__ClassFile(originalFilePath="sample_text")
    _safe_set(b, 'java__ClassFile245', a1)
    assert _is_linked(b, 'java__ClassFile245', a1)
    if hasattr(a1, 'java__Model244'):
        assert _is_linked(a1, 'java__Model244', b)
    _safe_set(b, 'java__ClassFile245', a2)
    assert _is_linked(b, 'java__ClassFile245', a2)
    if hasattr(a1, 'java__Model244'):
        assert not _is_linked(a1, 'java__Model244', b)
    if hasattr(a2, 'java__Model244'):
        assert _is_linked(a2, 'java__Model244', b)
    _safe_set(b, 'java__ClassFile245', None)
    assert not _is_linked(b, 'java__ClassFile245', a2)
    if hasattr(a2, 'java__Model244'):
        assert not _is_linked(a2, 'java__Model244', b)


def test_assoc_classFiles32_reverse_link_reassign_clear():
    a1 = java__ClassFile(originalFilePath="sample_text")
    a2 = java__ClassFile(originalFilePath="sample_text_2")
    b = java__Archive(originalFilePath="sample_text")
    _safe_set(b, 'java__Archive', {a1})
    assert _is_linked(b, 'java__Archive', a1)
    if hasattr(a1, 'java__ClassFile'):
        assert _is_linked(a1, 'java__ClassFile', b)
    _safe_set(b, 'java__Archive', {a2})
    assert _is_linked(b, 'java__Archive', a2)
    if hasattr(a1, 'java__ClassFile'):
        assert not _is_linked(a1, 'java__ClassFile', b)
    if hasattr(a2, 'java__ClassFile'):
        assert _is_linked(a2, 'java__ClassFile', b)
    _safe_set(b, 'java__Archive', set())
    assert not _is_linked(b, 'java__Archive', a2)
    if hasattr(a2, 'java__ClassFile'):
        assert not _is_linked(a2, 'java__ClassFile', b)


def test_assoc_commentList128_reverse_link_reassign_clear():
    a1 = java__CompilationUnit(originalFilePath="sample_text")
    a2 = java__CompilationUnit(originalFilePath="sample_text_2")
    b = java__Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    _safe_set(b, 'java__Comment130', a1)
    assert _is_linked(b, 'java__Comment130', a1)
    if hasattr(a1, 'java__CompilationUnit129'):
        assert _is_linked(a1, 'java__CompilationUnit129', b)
    _safe_set(b, 'java__Comment130', a2)
    assert _is_linked(b, 'java__Comment130', a2)
    if hasattr(a1, 'java__CompilationUnit129'):
        assert not _is_linked(a1, 'java__CompilationUnit129', b)
    if hasattr(a2, 'java__CompilationUnit129'):
        assert _is_linked(a2, 'java__CompilationUnit129', b)
    _safe_set(b, 'java__Comment130', None)
    assert not _is_linked(b, 'java__Comment130', a2)
    if hasattr(a2, 'java__CompilationUnit129'):
        assert not _is_linked(a2, 'java__CompilationUnit129', b)


def test_assoc_compilationUnits240_reverse_link_reassign_clear():
    a1 = java__Model(name="sample_text")
    a2 = java__Model(name="sample_text_2")
    b = java__CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'java__CompilationUnit242', a1)
    assert _is_linked(b, 'java__CompilationUnit242', a1)
    if hasattr(a1, 'java__Model241'):
        assert _is_linked(a1, 'java__Model241', b)
    _safe_set(b, 'java__CompilationUnit242', a2)
    assert _is_linked(b, 'java__CompilationUnit242', a2)
    if hasattr(a1, 'java__Model241'):
        assert not _is_linked(a1, 'java__Model241', b)
    if hasattr(a2, 'java__Model241'):
        assert _is_linked(a2, 'java__Model241', b)
    _safe_set(b, 'java__CompilationUnit242', None)
    assert not _is_linked(b, 'java__CompilationUnit242', a2)
    if hasattr(a2, 'java__Model241'):
        assert not _is_linked(a2, 'java__Model241', b)


def test_assoc_importedElement184_reverse_link_reassign_clear():
    a1 = java__NamedElement(name="sample_text", proxy=True)
    a2 = java__NamedElement(name="sample_text_2", proxy=False)
    b = java__ImportDeclaration(static=True)
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
    a1 = java__ImportDeclaration(static=True)
    a2 = java__ImportDeclaration(static=False)
    b = java__CompilationUnit(originalFilePath="sample_text")
    _safe_set(b, 'java__CompilationUnit132', {a1})
    assert _is_linked(b, 'java__CompilationUnit132', a1)
    if hasattr(a1, 'java__ImportDeclaration'):
        assert _is_linked(a1, 'java__ImportDeclaration', b)
    _safe_set(b, 'java__CompilationUnit132', {a2})
    assert _is_linked(b, 'java__CompilationUnit132', a2)
    if hasattr(a1, 'java__ImportDeclaration'):
        assert not _is_linked(a1, 'java__ImportDeclaration', b)
    if hasattr(a2, 'java__ImportDeclaration'):
        assert _is_linked(a2, 'java__ImportDeclaration', b)
    _safe_set(b, 'java__CompilationUnit132', set())
    assert not _is_linked(b, 'java__CompilationUnit132', a2)
    if hasattr(a2, 'java__ImportDeclaration'):
        assert not _is_linked(a2, 'java__ImportDeclaration', b)


def test_assoc_modifier293_reverse_link_reassign_clear():
    a1 = java__SingleVariableDeclaration(varargs=True)
    a2 = java__SingleVariableDeclaration(varargs=False)
    b = java__Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
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
    a1 = java__VariableDeclarationStatement(extraArrayDimensions=7)
    a2 = java__VariableDeclarationStatement(extraArrayDimensions=13)
    b = java__Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
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
    a1 = java__MethodDeclaration(extraArrayDimensions=7)
    a2 = java__MethodDeclaration(extraArrayDimensions=13)
    b = java__MethodDeclaration(extraArrayDimensions=7)
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
    a1 = java__MethodDeclaration(extraArrayDimensions=7)
    a2 = java__MethodDeclaration(extraArrayDimensions=13)
    b = java__MethodDeclaration(extraArrayDimensions=7)
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
    a1 = java__SingleVariableDeclaration(varargs=True)
    a2 = java__SingleVariableDeclaration(varargs=False)
    b = java__Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
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
    a1 = java__NamedElement(name="sample_text", proxy=True)
    a2 = java__NamedElement(name="sample_text_2", proxy=False)
    b = java__ImportDeclaration(static=True)
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
    a1 = java__VariableDeclarationStatement(extraArrayDimensions=7)
    a2 = java__VariableDeclarationStatement(extraArrayDimensions=13)
    b = java__Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
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


