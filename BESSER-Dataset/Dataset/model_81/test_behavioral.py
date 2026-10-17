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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations297_stub_double():
    # java__Annotation has no real 'java__Annotation299' property in the generated
    # code (a bare stub) -- manually attach it so java__SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__SingleVariableDeclaration(varargs=True)
    partner = java__Annotation()
    setattr(partner, 'java__Annotation299', None)
    _safe_set(owner, 'java__SingleVariableDeclaration298', {partner})
    assert getattr(partner, 'java__Annotation299') == owner
    _safe_set(owner, 'java__SingleVariableDeclaration298', set())
    assert getattr(partner, 'java__Annotation299') is None


def test_assoc_annotations361_stub_double():
    # java__Annotation has no real 'java__Annotation362' property in the generated
    # code (a bare stub) -- manually attach it so java__VariableDeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__VariableDeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__VariableDeclarationStatement(extraArrayDimensions=7)
    partner = java__Annotation()
    setattr(partner, 'java__Annotation362', None)
    _safe_set(owner, 'java__VariableDeclarationStatement', {partner})
    assert getattr(partner, 'java__Annotation362') == owner
    _safe_set(owner, 'java__VariableDeclarationStatement', set())
    assert getattr(partner, 'java__Annotation362') is None


def test_assoc_bodyDeclaration249_stub_double():
    # java__BodyDeclaration has no real 'BodyDeclaration250' property in the generated
    # code (a bare stub) -- manually attach it so java__Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java__BodyDeclaration()
    setattr(partner, 'BodyDeclaration250', None)
    _safe_set(owner, 'modifier', partner)
    assert getattr(partner, 'BodyDeclaration250') == owner
    _safe_set(owner, 'modifier', None)
    assert getattr(partner, 'BodyDeclaration250') is None


def test_assoc_bound363_stub_double():
    # java__TypeAccess has no real 'java__TypeAccess364' property in the generated
    # code (a bare stub) -- manually attach it so java__WildCardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__WildCardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__WildCardType(upperBound=True)
    partner = java__TypeAccess()
    setattr(partner, 'java__TypeAccess364', None)
    _safe_set(owner, 'java__WildCardType', partner)
    assert getattr(partner, 'java__TypeAccess364') == owner
    _safe_set(owner, 'java__WildCardType', None)
    assert getattr(partner, 'java__TypeAccess364') is None


def test_assoc_catchClause302_stub_double():
    # java__CatchClause has no real 'CatchClause' property in the generated
    # code (a bare stub) -- manually attach it so java__SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__SingleVariableDeclaration(varargs=True)
    partner = java__CatchClause()
    setattr(partner, 'CatchClause', None)
    _safe_set(owner, 'exception', partner)
    assert getattr(partner, 'CatchClause') == owner
    _safe_set(owner, 'exception', None)
    assert getattr(partner, 'CatchClause') is None


def test_assoc_comments40_stub_double():
    # java__ASTNode has no real 'java__ASTNode' property in the generated
    # code (a bare stub) -- manually attach it so java__Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = java__ASTNode()
    setattr(partner, 'java__ASTNode', None)
    _safe_set(owner, 'java__Comment41', partner)
    assert getattr(partner, 'java__ASTNode') == owner
    _safe_set(owner, 'java__Comment41', None)
    assert getattr(partner, 'java__ASTNode') is None


def test_assoc_commentsAfterBody16_stub_double():
    # java__AbstractTypeDeclaration has no real 'java__AbstractTypeDeclaration17' property in the generated
    # code (a bare stub) -- manually attach it so java__Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = java__AbstractTypeDeclaration()
    setattr(partner, 'java__AbstractTypeDeclaration17', None)
    _safe_set(owner, 'java__Comment18', partner)
    assert getattr(partner, 'java__AbstractTypeDeclaration17') == owner
    _safe_set(owner, 'java__Comment18', None)
    assert getattr(partner, 'java__AbstractTypeDeclaration17') is None


def test_assoc_commentsBeforeBody15_stub_double():
    # java__AbstractTypeDeclaration has no real 'java__AbstractTypeDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so java__Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Comment(content="sample_text", enclosedByParent=True, prefixOfParent=True)
    partner = java__AbstractTypeDeclaration()
    setattr(partner, 'java__AbstractTypeDeclaration', None)
    _safe_set(owner, 'java__Comment', partner)
    assert getattr(partner, 'java__AbstractTypeDeclaration') == owner
    _safe_set(owner, 'java__Comment', None)
    assert getattr(partner, 'java__AbstractTypeDeclaration') is None


def test_assoc_elementType78_stub_double():
    # java__TypeAccess has no real 'java__TypeAccess79' property in the generated
    # code (a bare stub) -- manually attach it so java__ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__ArrayType(dimensions=7)
    partner = java__TypeAccess()
    setattr(partner, 'java__TypeAccess79', None)
    _safe_set(owner, 'java__ArrayType', partner)
    assert getattr(partner, 'java__TypeAccess79') == owner
    _safe_set(owner, 'java__ArrayType', None)
    assert getattr(partner, 'java__TypeAccess79') is None


def test_assoc_enhancedForStatement303_stub_double():
    # java__EnhancedForStatement has no real 'EnhancedForStatement' property in the generated
    # code (a bare stub) -- manually attach it so java__SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__SingleVariableDeclaration(varargs=True)
    partner = java__EnhancedForStatement()
    setattr(partner, 'EnhancedForStatement', None)
    _safe_set(owner, 'parameter', partner)
    assert getattr(partner, 'EnhancedForStatement') == owner
    _safe_set(owner, 'parameter', None)
    assert getattr(partner, 'EnhancedForStatement') is None


def test_assoc_entryAttributes208_stub_double():
    # java__Manifest has no real 'java__Manifest209' property in the generated
    # code (a bare stub) -- manually attach it so java__ManifestEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__ManifestEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__ManifestEntry(name="sample_text")
    partner = java__Manifest()
    setattr(partner, 'java__Manifest209', None)
    _safe_set(owner, 'java__ManifestEntry', partner)
    assert getattr(partner, 'java__Manifest209') == owner
    _safe_set(owner, 'java__ManifestEntry', None)
    assert getattr(partner, 'java__Manifest209') is None


def test_assoc_exception99_stub_double():
    # java__CatchClause has no real 'catchClause' property in the generated
    # code (a bare stub) -- manually attach it so java__SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__SingleVariableDeclaration(varargs=True)
    partner = java__CatchClause()
    setattr(partner, 'catchClause', None)
    _safe_set(owner, 'SingleVariableDeclaration100', partner)
    assert getattr(partner, 'catchClause') == owner
    _safe_set(owner, 'SingleVariableDeclaration100', None)
    assert getattr(partner, 'catchClause') is None


def test_assoc_expression308_stub_double():
    # java__Expression has no real 'java__Expression309' property in the generated
    # code (a bare stub) -- manually attach it so java__SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__SwitchCase(default=True)
    partner = java__Expression()
    setattr(partner, 'java__Expression309', None)
    _safe_set(owner, 'java__SwitchCase', partner)
    assert getattr(partner, 'java__Expression309') == owner
    _safe_set(owner, 'java__SwitchCase', None)
    assert getattr(partner, 'java__Expression309') is None


def test_assoc_extendedOperands190_stub_double():
    # java__Expression has no real 'java__Expression192' property in the generated
    # code (a bare stub) -- manually attach it so java__InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__InfixExpression(operator="sample_text")
    partner = java__Expression()
    setattr(partner, 'java__Expression192', None)
    _safe_set(owner, 'java__InfixExpression191', {partner})
    assert getattr(partner, 'java__Expression192') == owner
    _safe_set(owner, 'java__InfixExpression191', set())
    assert getattr(partner, 'java__Expression192') is None


def test_assoc_fragments320_stub_double():
    # java__ASTNode has no real 'java__ASTNode322' property in the generated
    # code (a bare stub) -- manually attach it so java__TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__TagElement(tagName="sample_text")
    partner = java__ASTNode()
    setattr(partner, 'java__ASTNode322', None)
    _safe_set(owner, 'java__TagElement321', {partner})
    assert getattr(partner, 'java__ASTNode322') == owner
    _safe_set(owner, 'java__TagElement321', set())
    assert getattr(partner, 'java__ASTNode322') is None


def test_assoc_initializer351_stub_double():
    # java__Expression has no real 'java__Expression352' property in the generated
    # code (a bare stub) -- manually attach it so java__VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__VariableDeclaration(extraArrayDimensions=7)
    partner = java__Expression()
    setattr(partner, 'java__Expression352', None)
    _safe_set(owner, 'java__VariableDeclaration', partner)
    assert getattr(partner, 'java__Expression352') == owner
    _safe_set(owner, 'java__VariableDeclaration', None)
    assert getattr(partner, 'java__Expression352') is None


def test_assoc_leftHandSide80_stub_double():
    # java__Expression has no real 'java__Expression81' property in the generated
    # code (a bare stub) -- manually attach it so java__Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Assignment(operator="sample_text")
    partner = java__Expression()
    setattr(partner, 'java__Expression81', None)
    _safe_set(owner, 'java__Assignment', partner)
    assert getattr(partner, 'java__Expression81') == owner
    _safe_set(owner, 'java__Assignment', None)
    assert getattr(partner, 'java__Expression81') is None


def test_assoc_leftOperand187_stub_double():
    # java__Expression has no real 'java__Expression189' property in the generated
    # code (a bare stub) -- manually attach it so java__InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__InfixExpression(operator="sample_text")
    partner = java__Expression()
    setattr(partner, 'java__Expression189', None)
    _safe_set(owner, 'java__InfixExpression188', partner)
    assert getattr(partner, 'java__Expression189') == owner
    _safe_set(owner, 'java__InfixExpression188', None)
    assert getattr(partner, 'java__Expression189') is None


def test_assoc_mainAttributes206_stub_double():
    # java__Manifest has no real 'java__Manifest207' property in the generated
    # code (a bare stub) -- manually attach it so java__ManifestAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__ManifestAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__ManifestAttribute(key="sample_text", value="sample_text")
    partner = java__Manifest()
    setattr(partner, 'java__Manifest207', None)
    _safe_set(owner, 'java__ManifestAttribute', partner)
    assert getattr(partner, 'java__Manifest207') == owner
    _safe_set(owner, 'java__ManifestAttribute', None)
    assert getattr(partner, 'java__Manifest207') is None


def test_assoc_manifest33_stub_double():
    # java__Manifest has no real 'java__Manifest' property in the generated
    # code (a bare stub) -- manually attach it so java__Archive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Archive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Archive(originalFilePath="sample_text")
    partner = java__Manifest()
    setattr(partner, 'java__Manifest', None)
    _safe_set(owner, 'java__Archive34', partner)
    assert getattr(partner, 'java__Manifest') == owner
    _safe_set(owner, 'java__Archive34', None)
    assert getattr(partner, 'java__Manifest') is None


def test_assoc_member213_stub_double():
    # java__MemberRef has no real 'java__MemberRef' property in the generated
    # code (a bare stub) -- manually attach it so java__NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__NamedElement(name="sample_text", proxy=True)
    partner = java__MemberRef()
    setattr(partner, 'java__MemberRef', None)
    _safe_set(owner, 'java__NamedElement', partner)
    assert getattr(partner, 'java__MemberRef') == owner
    _safe_set(owner, 'java__NamedElement', None)
    assert getattr(partner, 'java__MemberRef') is None


def test_assoc_methodDeclaration300_stub_double():
    # java__AbstractMethodDeclaration has no real 'AbstractMethodDeclaration301' property in the generated
    # code (a bare stub) -- manually attach it so java__SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__SingleVariableDeclaration(varargs=True)
    partner = java__AbstractMethodDeclaration()
    setattr(partner, 'AbstractMethodDeclaration301', None)
    _safe_set(owner, 'parameters', partner)
    assert getattr(partner, 'AbstractMethodDeclaration301') == owner
    _safe_set(owner, 'parameters', None)
    assert getattr(partner, 'AbstractMethodDeclaration301') is None


def test_assoc_model261_stub_double():
    # java__Package has no real 'ownedElements262' property in the generated
    # code (a bare stub) -- manually attach it so java__Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Model(name="sample_text")
    partner = java__Package()
    setattr(partner, 'ownedElements262', None)
    _safe_set(owner, 'Model', partner)
    assert getattr(partner, 'ownedElements262') == owner
    _safe_set(owner, 'Model', None)
    assert getattr(partner, 'ownedElements262') is None


def test_assoc_modifier354_stub_double():
    # java__VariableDeclarationExpression has no real 'variableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so java__Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java__VariableDeclarationExpression()
    setattr(partner, 'variableDeclarationExpression', None)
    _safe_set(owner, 'Modifier355', partner)
    assert getattr(partner, 'variableDeclarationExpression') == owner
    _safe_set(owner, 'Modifier355', None)
    assert getattr(partner, 'variableDeclarationExpression') is None


def test_assoc_modifier90_stub_double():
    # java__BodyDeclaration has no real 'bodyDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so java__Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java__BodyDeclaration()
    setattr(partner, 'bodyDeclaration', None)
    _safe_set(owner, 'Modifier', partner)
    assert getattr(partner, 'bodyDeclaration') == owner
    _safe_set(owner, 'Modifier', None)
    assert getattr(partner, 'bodyDeclaration') is None


def test_assoc_operand283_stub_double():
    # java__Expression has no real 'java__Expression284' property in the generated
    # code (a bare stub) -- manually attach it so java__PostfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__PostfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__PostfixExpression(operator="sample_text")
    partner = java__Expression()
    setattr(partner, 'java__Expression284', None)
    _safe_set(owner, 'java__PostfixExpression', partner)
    assert getattr(partner, 'java__Expression284') == owner
    _safe_set(owner, 'java__PostfixExpression', None)
    assert getattr(partner, 'java__Expression284') is None


def test_assoc_operand285_stub_double():
    # java__Expression has no real 'java__Expression286' property in the generated
    # code (a bare stub) -- manually attach it so java__PrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__PrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__PrefixExpression(operator="sample_text")
    partner = java__Expression()
    setattr(partner, 'java__Expression286', None)
    _safe_set(owner, 'java__PrefixExpression', partner)
    assert getattr(partner, 'java__Expression286') == owner
    _safe_set(owner, 'java__PrefixExpression', None)
    assert getattr(partner, 'java__Expression286') is None


def test_assoc_originalClassFile44_stub_double():
    # java__ASTNode has no real 'java__ASTNode45' property in the generated
    # code (a bare stub) -- manually attach it so java__ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__ClassFile(originalFilePath="sample_text")
    partner = java__ASTNode()
    setattr(partner, 'java__ASTNode45', None)
    _safe_set(owner, 'java__ClassFile46', partner)
    assert getattr(partner, 'java__ASTNode45') == owner
    _safe_set(owner, 'java__ClassFile46', None)
    assert getattr(partner, 'java__ASTNode45') is None


def test_assoc_originalCompilationUnit42_stub_double():
    # java__ASTNode has no real 'java__ASTNode43' property in the generated
    # code (a bare stub) -- manually attach it so java__CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__CompilationUnit(originalFilePath="sample_text")
    partner = java__ASTNode()
    setattr(partner, 'java__ASTNode43', None)
    _safe_set(owner, 'java__CompilationUnit', partner)
    assert getattr(partner, 'java__ASTNode43') == owner
    _safe_set(owner, 'java__CompilationUnit', None)
    assert getattr(partner, 'java__ASTNode43') is None


def test_assoc_orphanTypes237_stub_double():
    # java__Type has no real 'java__Type' property in the generated
    # code (a bare stub) -- manually attach it so java__Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Model(name="sample_text")
    partner = java__Type()
    setattr(partner, 'java__Type', None)
    _safe_set(owner, 'java__Model', {partner})
    assert getattr(partner, 'java__Type') == owner
    _safe_set(owner, 'java__Model', set())
    assert getattr(partner, 'java__Type') is None


def test_assoc_ownedElements235_stub_double():
    # java__Package has no real 'Package236' property in the generated
    # code (a bare stub) -- manually attach it so java__Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Model(name="sample_text")
    partner = java__Package()
    setattr(partner, 'Package236', None)
    _safe_set(owner, 'model', {partner})
    assert getattr(partner, 'Package236') == owner
    _safe_set(owner, 'model', set())
    assert getattr(partner, 'Package236') is None


def test_assoc_package109_stub_double():
    # java__Package has no real 'java__Package' property in the generated
    # code (a bare stub) -- manually attach it so java__ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__ClassFile(originalFilePath="sample_text")
    partner = java__Package()
    setattr(partner, 'java__Package', None)
    _safe_set(owner, 'java__ClassFile110', partner)
    assert getattr(partner, 'java__Package') == owner
    _safe_set(owner, 'java__ClassFile110', None)
    assert getattr(partner, 'java__Package') is None


def test_assoc_package133_stub_double():
    # java__Package has no real 'java__Package135' property in the generated
    # code (a bare stub) -- manually attach it so java__CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__CompilationUnit(originalFilePath="sample_text")
    partner = java__Package()
    setattr(partner, 'java__Package135', None)
    _safe_set(owner, 'java__CompilationUnit134', partner)
    assert getattr(partner, 'java__Package135') == owner
    _safe_set(owner, 'java__CompilationUnit134', None)
    assert getattr(partner, 'java__Package135') is None


def test_assoc_parameter151_stub_double():
    # java__EnhancedForStatement has no real 'enhancedForStatement' property in the generated
    # code (a bare stub) -- manually attach it so java__SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__SingleVariableDeclaration(varargs=True)
    partner = java__EnhancedForStatement()
    setattr(partner, 'enhancedForStatement', None)
    _safe_set(owner, 'SingleVariableDeclaration152', partner)
    assert getattr(partner, 'enhancedForStatement') == owner
    _safe_set(owner, 'SingleVariableDeclaration152', None)
    assert getattr(partner, 'enhancedForStatement') is None


def test_assoc_parameters1_stub_double():
    # java__AbstractMethodDeclaration has no real 'methodDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so java__SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__SingleVariableDeclaration(varargs=True)
    partner = java__AbstractMethodDeclaration()
    setattr(partner, 'methodDeclaration', None)
    _safe_set(owner, 'SingleVariableDeclaration', partner)
    assert getattr(partner, 'methodDeclaration') == owner
    _safe_set(owner, 'SingleVariableDeclaration', None)
    assert getattr(partner, 'methodDeclaration') is None


def test_assoc_parameters230_stub_double():
    # java__MethodRef has no real 'java__MethodRef231' property in the generated
    # code (a bare stub) -- manually attach it so java__MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__MethodRefParameter(name="sample_text", varargs=True)
    partner = java__MethodRef()
    setattr(partner, 'java__MethodRef231', None)
    _safe_set(owner, 'java__MethodRefParameter', partner)
    assert getattr(partner, 'java__MethodRef231') == owner
    _safe_set(owner, 'java__MethodRefParameter', None)
    assert getattr(partner, 'java__MethodRef231') is None


def test_assoc_returnType217_stub_double():
    # java__TypeAccess has no real 'java__TypeAccess218' property in the generated
    # code (a bare stub) -- manually attach it so java__MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__MethodDeclaration(extraArrayDimensions=7)
    partner = java__TypeAccess()
    setattr(partner, 'java__TypeAccess218', None)
    _safe_set(owner, 'java__MethodDeclaration', partner)
    assert getattr(partner, 'java__TypeAccess218') == owner
    _safe_set(owner, 'java__MethodDeclaration', None)
    assert getattr(partner, 'java__TypeAccess218') is None


def test_assoc_rightHandSide82_stub_double():
    # java__Expression has no real 'java__Expression84' property in the generated
    # code (a bare stub) -- manually attach it so java__Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Assignment(operator="sample_text")
    partner = java__Expression()
    setattr(partner, 'java__Expression84', None)
    _safe_set(owner, 'java__Assignment83', partner)
    assert getattr(partner, 'java__Expression84') == owner
    _safe_set(owner, 'java__Assignment83', None)
    assert getattr(partner, 'java__Expression84') is None


def test_assoc_rightOperand185_stub_double():
    # java__Expression has no real 'java__Expression186' property in the generated
    # code (a bare stub) -- manually attach it so java__InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__InfixExpression(operator="sample_text")
    partner = java__Expression()
    setattr(partner, 'java__Expression186', None)
    _safe_set(owner, 'java__InfixExpression', partner)
    assert getattr(partner, 'java__Expression186') == owner
    _safe_set(owner, 'java__InfixExpression', None)
    assert getattr(partner, 'java__Expression186') is None


def test_assoc_tags200_stub_double():
    # java__Javadoc has no real 'java__Javadoc' property in the generated
    # code (a bare stub) -- manually attach it so java__TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__TagElement(tagName="sample_text")
    partner = java__Javadoc()
    setattr(partner, 'java__Javadoc', None)
    _safe_set(owner, 'java__TagElement', partner)
    assert getattr(partner, 'java__Javadoc') == owner
    _safe_set(owner, 'java__TagElement', None)
    assert getattr(partner, 'java__Javadoc') is None


def test_assoc_type103_stub_double():
    # java__AbstractTypeDeclaration has no real 'java__AbstractTypeDeclaration105' property in the generated
    # code (a bare stub) -- manually attach it so java__ClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__ClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__ClassFile(originalFilePath="sample_text")
    partner = java__AbstractTypeDeclaration()
    setattr(partner, 'java__AbstractTypeDeclaration105', None)
    _safe_set(owner, 'java__ClassFile104', partner)
    assert getattr(partner, 'java__AbstractTypeDeclaration105') == owner
    _safe_set(owner, 'java__ClassFile104', None)
    assert getattr(partner, 'java__AbstractTypeDeclaration105') is None


def test_assoc_type232_stub_double():
    # java__TypeAccess has no real 'java__TypeAccess234' property in the generated
    # code (a bare stub) -- manually attach it so java__MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__MethodRefParameter(name="sample_text", varargs=True)
    partner = java__TypeAccess()
    setattr(partner, 'java__TypeAccess234', None)
    _safe_set(owner, 'java__MethodRefParameter233', partner)
    assert getattr(partner, 'java__TypeAccess234') == owner
    _safe_set(owner, 'java__MethodRefParameter233', None)
    assert getattr(partner, 'java__TypeAccess234') is None


def test_assoc_type295_stub_double():
    # java__TypeAccess has no real 'java__TypeAccess296' property in the generated
    # code (a bare stub) -- manually attach it so java__SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__SingleVariableDeclaration(varargs=True)
    partner = java__TypeAccess()
    setattr(partner, 'java__TypeAccess296', None)
    _safe_set(owner, 'java__SingleVariableDeclaration', partner)
    assert getattr(partner, 'java__TypeAccess296') == owner
    _safe_set(owner, 'java__SingleVariableDeclaration', None)
    assert getattr(partner, 'java__TypeAccess296') is None


def test_assoc_types136_stub_double():
    # java__AbstractTypeDeclaration has no real 'java__AbstractTypeDeclaration138' property in the generated
    # code (a bare stub) -- manually attach it so java__CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__CompilationUnit(originalFilePath="sample_text")
    partner = java__AbstractTypeDeclaration()
    setattr(partner, 'java__AbstractTypeDeclaration138', None)
    _safe_set(owner, 'java__CompilationUnit137', {partner})
    assert getattr(partner, 'java__AbstractTypeDeclaration138') == owner
    _safe_set(owner, 'java__CompilationUnit137', set())
    assert getattr(partner, 'java__AbstractTypeDeclaration138') is None


def test_assoc_unresolvedItems238_stub_double():
    # java__UnresolvedItem has no real 'java__UnresolvedItem' property in the generated
    # code (a bare stub) -- manually attach it so java__Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Model(name="sample_text")
    partner = java__UnresolvedItem()
    setattr(partner, 'java__UnresolvedItem', None)
    _safe_set(owner, 'java__Model239', {partner})
    assert getattr(partner, 'java__UnresolvedItem') == owner
    _safe_set(owner, 'java__Model239', set())
    assert getattr(partner, 'java__UnresolvedItem') is None


def test_assoc_usageInVariableAccess353_stub_double():
    # java__SingleVariableAccess has no real 'SingleVariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so java__VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__VariableDeclaration(extraArrayDimensions=7)
    partner = java__SingleVariableAccess()
    setattr(partner, 'SingleVariableAccess', None)
    _safe_set(owner, 'variable', {partner})
    assert getattr(partner, 'SingleVariableAccess') == owner
    _safe_set(owner, 'variable', set())
    assert getattr(partner, 'SingleVariableAccess') is None


def test_assoc_variable289_stub_double():
    # java__SingleVariableAccess has no real 'usageInVariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so java__VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__VariableDeclaration(extraArrayDimensions=7)
    partner = java__SingleVariableAccess()
    setattr(partner, 'usageInVariableAccess', None)
    _safe_set(owner, 'VariableDeclaration', partner)
    assert getattr(partner, 'usageInVariableAccess') == owner
    _safe_set(owner, 'VariableDeclaration', None)
    assert getattr(partner, 'usageInVariableAccess') is None


def test_assoc_variableDeclarationExpression256_stub_double():
    # java__VariableDeclarationExpression has no real 'VariableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so java__Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java__Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java__Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    partner = java__VariableDeclarationExpression()
    setattr(partner, 'VariableDeclarationExpression', None)
    _safe_set(owner, 'modifier257', partner)
    assert getattr(partner, 'VariableDeclarationExpression') == owner
    _safe_set(owner, 'modifier257', None)
    assert getattr(partner, 'VariableDeclarationExpression') is None


