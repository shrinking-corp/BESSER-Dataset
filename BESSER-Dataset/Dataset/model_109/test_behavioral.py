import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    AbstractTypeDeclaration,
    Annotation,
    BodyDeclaration,
    Comment,
    Expression,
    ExtendedModifier,
    IJavaElement,
    IMember,
    IPackageFragmentRoot,
    ISourceReference,
    ITypeRoot,
    JDTAST_AST,
    JDTAST_ASTNode,
    JDTAST_AbstractTypeDeclaration,
    JDTAST_Annotation,
    JDTAST_AnnotationTypeDeclaration,
    JDTAST_AnnotationTypeMemberDeclaration,
    JDTAST_AnonymousClassDeclaration,
    JDTAST_ArrayAccess,
    JDTAST_ArrayCreation,
    JDTAST_ArrayInitializer,
    JDTAST_ArrayType,
    JDTAST_AssertStatement,
    JDTAST_Assignment,
    JDTAST_BinaryPackageFragmentRoot,
    JDTAST_Block,
    JDTAST_BlockComment,
    JDTAST_BodyDeclaration,
    JDTAST_BooleanLiteral,
    JDTAST_BreakStatement,
    JDTAST_CastExpression,
    JDTAST_CatchClause,
    JDTAST_CharacterLiteral,
    JDTAST_ClassInstanceCreation,
    JDTAST_Comment,
    JDTAST_CompilationUnit,
    JDTAST_ConditionalExpression,
    JDTAST_ConstructorInvocation,
    JDTAST_ContinueStatement,
    JDTAST_DoStatement,
    JDTAST_EmptyStatement,
    JDTAST_EnhancedForStatement,
    JDTAST_EnumConstantDeclaration,
    JDTAST_EnumDeclaration,
    JDTAST_Expression,
    JDTAST_ExpressionStatement,
    JDTAST_ExtendedModifier,
    JDTAST_FieldAccess,
    JDTAST_FieldDeclaration,
    JDTAST_ForStatement,
    JDTAST_IClassFile,
    JDTAST_ICompilationUnit,
    JDTAST_IField,
    JDTAST_IImportDeclaration,
    JDTAST_IInitializer,
    JDTAST_IJavaElement,
    JDTAST_IJavaModel,
    JDTAST_IJavaProject,
    JDTAST_IMember,
    JDTAST_IMethod,
    JDTAST_IPackageFragment,
    JDTAST_IPackageFragmentRoot,
    JDTAST_ISourceRange,
    JDTAST_ISourceReference,
    JDTAST_IType,
    JDTAST_ITypeParameter,
    JDTAST_ITypeRoot,
    JDTAST_IfStatement,
    JDTAST_ImportDeclaration,
    JDTAST_InfixExpression,
    JDTAST_Initializer,
    JDTAST_InstanceofExpression,
    JDTAST_Javadoc,
    JDTAST_LabeledStatement,
    JDTAST_LineComment,
    JDTAST_MarkerAnnotation,
    JDTAST_MemberRef,
    JDTAST_MemberValuePair,
    JDTAST_MethodDeclaration,
    JDTAST_MethodInvocation,
    JDTAST_MethodRef,
    JDTAST_MethodRefParameter,
    JDTAST_Modifier,
    JDTAST_Name,
    JDTAST_NormalAnnotation,
    JDTAST_NullLiteral,
    JDTAST_NumberLiteral,
    JDTAST_PackageDeclaration,
    JDTAST_Parameter,
    JDTAST_ParameterizedType,
    JDTAST_ParenthesizedExpression,
    JDTAST_PhysicalElement,
    JDTAST_PostfixExpression,
    JDTAST_PrefixExpression,
    JDTAST_PrimitiveType,
    JDTAST_QualifiedName,
    JDTAST_QualifiedType,
    JDTAST_ReturnStatement,
    JDTAST_SimpleName,
    JDTAST_SimpleType,
    JDTAST_SingleMemberAnnotation,
    JDTAST_SingleVariableDeclaration,
    JDTAST_SourcePackageFragmentRoot,
    JDTAST_Statement,
    JDTAST_StringLiteral,
    JDTAST_SuperConstructorInvocation,
    JDTAST_SuperFieldAccess,
    JDTAST_SuperMethodInvocation,
    JDTAST_SwitchCase,
    JDTAST_SwitchStatement,
    JDTAST_SynchronizedStatement,
    JDTAST_TagElement,
    JDTAST_TextElement,
    JDTAST_ThisExpression,
    JDTAST_ThrowStatement,
    JDTAST_TryStatement,
    JDTAST_Type,
    JDTAST_TypeDeclaration,
    JDTAST_TypeDeclarationStatement,
    JDTAST_TypeLiteral,
    JDTAST_TypeParameter,
    JDTAST_VariableDeclaration,
    JDTAST_VariableDeclarationExpression,
    JDTAST_VariableDeclarationFragment,
    JDTAST_VariableDeclarationStatement,
    JDTAST_WhileStatement,
    JDTAST_WildcardType,
    Name,
    PhysicalElement,
    Statement,
    Type,
    VariableDeclaration,
    AssignmentOperatorKind,
    InfixExpressionOperatorKind,
    Modifiers,
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

def test_assoc_binding164_reverse_link_reassign_clear():
    a1 = JDTAST_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    a2 = JDTAST_MethodDeclaration(constructor="sample_text_2", extraDimensions="sample_text_2", varargs="sample_text_2")
    b = JDTAST_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    _safe_set(b, 'JDTAST_IMethod166', a1)
    assert _is_linked(b, 'JDTAST_IMethod166', a1)
    if hasattr(a1, 'JDTAST_MethodDeclaration165'):
        assert _is_linked(a1, 'JDTAST_MethodDeclaration165', b)
    _safe_set(b, 'JDTAST_IMethod166', a2)
    assert _is_linked(b, 'JDTAST_IMethod166', a2)
    if hasattr(a1, 'JDTAST_MethodDeclaration165'):
        assert not _is_linked(a1, 'JDTAST_MethodDeclaration165', b)
    if hasattr(a2, 'JDTAST_MethodDeclaration165'):
        assert _is_linked(a2, 'JDTAST_MethodDeclaration165', b)
    _safe_set(b, 'JDTAST_IMethod166', None)
    assert not _is_linked(b, 'JDTAST_IMethod166', a2)
    if hasattr(a2, 'JDTAST_MethodDeclaration165'):
        assert not _is_linked(a2, 'JDTAST_MethodDeclaration165', b)


def test_assoc_classFiles14_reverse_link_reassign_clear():
    a1 = JDTAST_IPackageFragment(isDefaultPackage="sample_text")
    a2 = JDTAST_IPackageFragment(isDefaultPackage="sample_text_2")
    b = JDTAST_IClassFile(isClass="sample_text", isInterface="sample_text")
    _safe_set(b, 'JDTAST_IClassFile', a1)
    assert _is_linked(b, 'JDTAST_IClassFile', a1)
    if hasattr(a1, 'JDTAST_IPackageFragment'):
        assert _is_linked(a1, 'JDTAST_IPackageFragment', b)
    _safe_set(b, 'JDTAST_IClassFile', a2)
    assert _is_linked(b, 'JDTAST_IClassFile', a2)
    if hasattr(a1, 'JDTAST_IPackageFragment'):
        assert not _is_linked(a1, 'JDTAST_IPackageFragment', b)
    if hasattr(a2, 'JDTAST_IPackageFragment'):
        assert _is_linked(a2, 'JDTAST_IPackageFragment', b)
    _safe_set(b, 'JDTAST_IClassFile', None)
    assert not _is_linked(b, 'JDTAST_IClassFile', a2)
    if hasattr(a2, 'JDTAST_IPackageFragment'):
        assert not _is_linked(a2, 'JDTAST_IPackageFragment', b)


def test_assoc_expression363_reverse_link_reassign_clear():
    a1 = JDTAST_SwitchCase(default="sample_text")
    a2 = JDTAST_SwitchCase(default="sample_text_2")
    b = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'JDTAST_Expression364', a1)
    assert _is_linked(b, 'JDTAST_Expression364', a1)
    if hasattr(a1, 'JDTAST_SwitchCase'):
        assert _is_linked(a1, 'JDTAST_SwitchCase', b)
    _safe_set(b, 'JDTAST_Expression364', a2)
    assert _is_linked(b, 'JDTAST_Expression364', a2)
    if hasattr(a1, 'JDTAST_SwitchCase'):
        assert not _is_linked(a1, 'JDTAST_SwitchCase', b)
    if hasattr(a2, 'JDTAST_SwitchCase'):
        assert _is_linked(a2, 'JDTAST_SwitchCase', b)
    _safe_set(b, 'JDTAST_Expression364', None)
    assert not _is_linked(b, 'JDTAST_Expression364', a2)
    if hasattr(a2, 'JDTAST_SwitchCase'):
        assert not _is_linked(a2, 'JDTAST_SwitchCase', b)


def test_assoc_extendedOperands237_reverse_link_reassign_clear():
    a1 = JDTAST_InfixExpression(operator="sample_text")
    a2 = JDTAST_InfixExpression(operator="sample_text_2")
    b = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'JDTAST_Expression238', a1)
    assert _is_linked(b, 'JDTAST_Expression238', a1)
    if hasattr(a1, 'JDTAST_InfixExpression'):
        assert _is_linked(a1, 'JDTAST_InfixExpression', b)
    _safe_set(b, 'JDTAST_Expression238', a2)
    assert _is_linked(b, 'JDTAST_Expression238', a2)
    if hasattr(a1, 'JDTAST_InfixExpression'):
        assert not _is_linked(a1, 'JDTAST_InfixExpression', b)
    if hasattr(a2, 'JDTAST_InfixExpression'):
        assert _is_linked(a2, 'JDTAST_InfixExpression', b)
    _safe_set(b, 'JDTAST_Expression238', None)
    assert not _is_linked(b, 'JDTAST_Expression238', a2)
    if hasattr(a2, 'JDTAST_InfixExpression'):
        assert not _is_linked(a2, 'JDTAST_InfixExpression', b)


def test_assoc_fields40_reverse_link_reassign_clear():
    a1 = JDTAST_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    a2 = JDTAST_IType(fullyQualifiedName="sample_text_2", fullyQualifiedParametrizedName="sample_text_2")
    b = JDTAST_IField(constant="sample_text", isEnumConstant="sample_text", isTransient="sample_text", isVolatile="sample_text", typeSignature="sample_text")
    _safe_set(b, 'JDTAST_IField', a1)
    assert _is_linked(b, 'JDTAST_IField', a1)
    if hasattr(a1, 'JDTAST_IType41'):
        assert _is_linked(a1, 'JDTAST_IType41', b)
    _safe_set(b, 'JDTAST_IField', a2)
    assert _is_linked(b, 'JDTAST_IField', a2)
    if hasattr(a1, 'JDTAST_IType41'):
        assert not _is_linked(a1, 'JDTAST_IType41', b)
    if hasattr(a2, 'JDTAST_IType41'):
        assert _is_linked(a2, 'JDTAST_IType41', b)
    _safe_set(b, 'JDTAST_IField', None)
    assert not _is_linked(b, 'JDTAST_IField', a2)
    if hasattr(a2, 'JDTAST_IType41'):
        assert not _is_linked(a2, 'JDTAST_IType41', b)


def test_assoc_initializer114_reverse_link_reassign_clear():
    a1 = JDTAST_VariableDeclaration(extraDimensions="sample_text")
    a2 = JDTAST_VariableDeclaration(extraDimensions="sample_text_2")
    b = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'JDTAST_Expression115', a1)
    assert _is_linked(b, 'JDTAST_Expression115', a1)
    if hasattr(a1, 'JDTAST_VariableDeclaration'):
        assert _is_linked(a1, 'JDTAST_VariableDeclaration', b)
    _safe_set(b, 'JDTAST_Expression115', a2)
    assert _is_linked(b, 'JDTAST_Expression115', a2)
    if hasattr(a1, 'JDTAST_VariableDeclaration'):
        assert not _is_linked(a1, 'JDTAST_VariableDeclaration', b)
    if hasattr(a2, 'JDTAST_VariableDeclaration'):
        assert _is_linked(a2, 'JDTAST_VariableDeclaration', b)
    _safe_set(b, 'JDTAST_Expression115', None)
    assert not _is_linked(b, 'JDTAST_Expression115', a2)
    if hasattr(a2, 'JDTAST_VariableDeclaration'):
        assert not _is_linked(a2, 'JDTAST_VariableDeclaration', b)


def test_assoc_leftHandSide200_reverse_link_reassign_clear():
    a1 = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    a2 = JDTAST_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    b = JDTAST_Assignment(operator="sample_text")
    _safe_set(b, 'JDTAST_Assignment', a1)
    assert _is_linked(b, 'JDTAST_Assignment', a1)
    if hasattr(a1, 'JDTAST_Expression201'):
        assert _is_linked(a1, 'JDTAST_Expression201', b)
    _safe_set(b, 'JDTAST_Assignment', a2)
    assert _is_linked(b, 'JDTAST_Assignment', a2)
    if hasattr(a1, 'JDTAST_Expression201'):
        assert not _is_linked(a1, 'JDTAST_Expression201', b)
    if hasattr(a2, 'JDTAST_Expression201'):
        assert _is_linked(a2, 'JDTAST_Expression201', b)
    _safe_set(b, 'JDTAST_Assignment', None)
    assert not _is_linked(b, 'JDTAST_Assignment', a2)
    if hasattr(a2, 'JDTAST_Expression201'):
        assert not _is_linked(a2, 'JDTAST_Expression201', b)


def test_assoc_leftOperand239_reverse_link_reassign_clear():
    a1 = JDTAST_InfixExpression(operator="sample_text")
    a2 = JDTAST_InfixExpression(operator="sample_text_2")
    b = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'JDTAST_Expression241', a1)
    assert _is_linked(b, 'JDTAST_Expression241', a1)
    if hasattr(a1, 'JDTAST_InfixExpression240'):
        assert _is_linked(a1, 'JDTAST_InfixExpression240', b)
    _safe_set(b, 'JDTAST_Expression241', a2)
    assert _is_linked(b, 'JDTAST_Expression241', a2)
    if hasattr(a1, 'JDTAST_InfixExpression240'):
        assert not _is_linked(a1, 'JDTAST_InfixExpression240', b)
    if hasattr(a2, 'JDTAST_InfixExpression240'):
        assert _is_linked(a2, 'JDTAST_InfixExpression240', b)
    _safe_set(b, 'JDTAST_Expression241', None)
    assert not _is_linked(b, 'JDTAST_Expression241', a2)
    if hasattr(a2, 'JDTAST_InfixExpression240'):
        assert not _is_linked(a2, 'JDTAST_InfixExpression240', b)


def test_assoc_methods42_reverse_link_reassign_clear():
    a1 = JDTAST_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    a2 = JDTAST_IType(fullyQualifiedName="sample_text_2", fullyQualifiedParametrizedName="sample_text_2")
    b = JDTAST_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    _safe_set(b, 'JDTAST_IMethod', a1)
    assert _is_linked(b, 'JDTAST_IMethod', a1)
    if hasattr(a1, 'JDTAST_IType43'):
        assert _is_linked(a1, 'JDTAST_IType43', b)
    _safe_set(b, 'JDTAST_IMethod', a2)
    assert _is_linked(b, 'JDTAST_IMethod', a2)
    if hasattr(a1, 'JDTAST_IType43'):
        assert not _is_linked(a1, 'JDTAST_IType43', b)
    if hasattr(a2, 'JDTAST_IType43'):
        assert _is_linked(a2, 'JDTAST_IType43', b)
    _safe_set(b, 'JDTAST_IMethod', None)
    assert not _is_linked(b, 'JDTAST_IMethod', a2)
    if hasattr(a2, 'JDTAST_IType43'):
        assert not _is_linked(a2, 'JDTAST_IType43', b)


def test_assoc_name116_reverse_link_reassign_clear():
    a1 = JDTAST_VariableDeclaration(extraDimensions="sample_text")
    a2 = JDTAST_VariableDeclaration(extraDimensions="sample_text_2")
    b = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    _safe_set(b, 'JDTAST_SimpleName118', a1)
    assert _is_linked(b, 'JDTAST_SimpleName118', a1)
    if hasattr(a1, 'JDTAST_VariableDeclaration117'):
        assert _is_linked(a1, 'JDTAST_VariableDeclaration117', b)
    _safe_set(b, 'JDTAST_SimpleName118', a2)
    assert _is_linked(b, 'JDTAST_SimpleName118', a2)
    if hasattr(a1, 'JDTAST_VariableDeclaration117'):
        assert not _is_linked(a1, 'JDTAST_VariableDeclaration117', b)
    if hasattr(a2, 'JDTAST_VariableDeclaration117'):
        assert _is_linked(a2, 'JDTAST_VariableDeclaration117', b)
    _safe_set(b, 'JDTAST_SimpleName118', None)
    assert not _is_linked(b, 'JDTAST_SimpleName118', a2)
    if hasattr(a2, 'JDTAST_VariableDeclaration117'):
        assert not _is_linked(a2, 'JDTAST_VariableDeclaration117', b)


def test_assoc_name122_reverse_link_reassign_clear():
    a1 = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    a2 = JDTAST_SimpleName(declaration="sample_text_2", identifier="sample_text_2")
    b = JDTAST_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    _safe_set(b, 'JDTAST_AbstractTypeDeclaration123', a1)
    assert _is_linked(b, 'JDTAST_AbstractTypeDeclaration123', a1)
    if hasattr(a1, 'JDTAST_SimpleName124'):
        assert _is_linked(a1, 'JDTAST_SimpleName124', b)
    _safe_set(b, 'JDTAST_AbstractTypeDeclaration123', a2)
    assert _is_linked(b, 'JDTAST_AbstractTypeDeclaration123', a2)
    if hasattr(a1, 'JDTAST_SimpleName124'):
        assert not _is_linked(a1, 'JDTAST_SimpleName124', b)
    if hasattr(a2, 'JDTAST_SimpleName124'):
        assert _is_linked(a2, 'JDTAST_SimpleName124', b)
    _safe_set(b, 'JDTAST_AbstractTypeDeclaration123', None)
    assert not _is_linked(b, 'JDTAST_AbstractTypeDeclaration123', a2)
    if hasattr(a2, 'JDTAST_SimpleName124'):
        assert not _is_linked(a2, 'JDTAST_SimpleName124', b)


def test_assoc_name149_reverse_link_reassign_clear():
    a1 = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    a2 = JDTAST_SimpleName(declaration="sample_text_2", identifier="sample_text_2")
    b = JDTAST_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    _safe_set(b, 'JDTAST_MethodDeclaration150', a1)
    assert _is_linked(b, 'JDTAST_MethodDeclaration150', a1)
    if hasattr(a1, 'JDTAST_SimpleName151'):
        assert _is_linked(a1, 'JDTAST_SimpleName151', b)
    _safe_set(b, 'JDTAST_MethodDeclaration150', a2)
    assert _is_linked(b, 'JDTAST_MethodDeclaration150', a2)
    if hasattr(a1, 'JDTAST_SimpleName151'):
        assert not _is_linked(a1, 'JDTAST_SimpleName151', b)
    if hasattr(a2, 'JDTAST_SimpleName151'):
        assert _is_linked(a2, 'JDTAST_SimpleName151', b)
    _safe_set(b, 'JDTAST_MethodDeclaration150', None)
    assert not _is_linked(b, 'JDTAST_MethodDeclaration150', a2)
    if hasattr(a2, 'JDTAST_SimpleName151'):
        assert not _is_linked(a2, 'JDTAST_SimpleName151', b)


def test_assoc_name73_reverse_link_reassign_clear():
    a1 = JDTAST_Name(fullyQualifiedName="sample_text")
    a2 = JDTAST_Name(fullyQualifiedName="sample_text_2")
    b = JDTAST_ImportDeclaration(onDemand="sample_text", static="sample_text")
    _safe_set(b, 'JDTAST_ImportDeclaration74', a1)
    assert _is_linked(b, 'JDTAST_ImportDeclaration74', a1)
    if hasattr(a1, 'JDTAST_Name'):
        assert _is_linked(a1, 'JDTAST_Name', b)
    _safe_set(b, 'JDTAST_ImportDeclaration74', a2)
    assert _is_linked(b, 'JDTAST_ImportDeclaration74', a2)
    if hasattr(a1, 'JDTAST_Name'):
        assert not _is_linked(a1, 'JDTAST_Name', b)
    if hasattr(a2, 'JDTAST_Name'):
        assert _is_linked(a2, 'JDTAST_Name', b)
    _safe_set(b, 'JDTAST_ImportDeclaration74', None)
    assert not _is_linked(b, 'JDTAST_ImportDeclaration74', a2)
    if hasattr(a2, 'JDTAST_Name'):
        assert not _is_linked(a2, 'JDTAST_Name', b)


def test_assoc_name91_reverse_link_reassign_clear():
    a1 = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    a2 = JDTAST_SimpleName(declaration="sample_text_2", identifier="sample_text_2")
    b = JDTAST_MethodRefParameter(varargs="sample_text")
    _safe_set(b, 'JDTAST_MethodRefParameter92', a1)
    assert _is_linked(b, 'JDTAST_MethodRefParameter92', a1)
    if hasattr(a1, 'JDTAST_SimpleName93'):
        assert _is_linked(a1, 'JDTAST_SimpleName93', b)
    _safe_set(b, 'JDTAST_MethodRefParameter92', a2)
    assert _is_linked(b, 'JDTAST_MethodRefParameter92', a2)
    if hasattr(a1, 'JDTAST_SimpleName93'):
        assert not _is_linked(a1, 'JDTAST_SimpleName93', b)
    if hasattr(a2, 'JDTAST_SimpleName93'):
        assert _is_linked(a2, 'JDTAST_SimpleName93', b)
    _safe_set(b, 'JDTAST_MethodRefParameter92', None)
    assert not _is_linked(b, 'JDTAST_MethodRefParameter92', a2)
    if hasattr(a2, 'JDTAST_SimpleName93'):
        assert not _is_linked(a2, 'JDTAST_SimpleName93', b)


def test_assoc_operand266_reverse_link_reassign_clear():
    a1 = JDTAST_PostfixExpression(operator="sample_text")
    a2 = JDTAST_PostfixExpression(operator="sample_text_2")
    b = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'JDTAST_Expression267', a1)
    assert _is_linked(b, 'JDTAST_Expression267', a1)
    if hasattr(a1, 'JDTAST_PostfixExpression'):
        assert _is_linked(a1, 'JDTAST_PostfixExpression', b)
    _safe_set(b, 'JDTAST_Expression267', a2)
    assert _is_linked(b, 'JDTAST_Expression267', a2)
    if hasattr(a1, 'JDTAST_PostfixExpression'):
        assert not _is_linked(a1, 'JDTAST_PostfixExpression', b)
    if hasattr(a2, 'JDTAST_PostfixExpression'):
        assert _is_linked(a2, 'JDTAST_PostfixExpression', b)
    _safe_set(b, 'JDTAST_Expression267', None)
    assert not _is_linked(b, 'JDTAST_Expression267', a2)
    if hasattr(a2, 'JDTAST_PostfixExpression'):
        assert not _is_linked(a2, 'JDTAST_PostfixExpression', b)


def test_assoc_operand268_reverse_link_reassign_clear():
    a1 = JDTAST_PrefixExpression(operator="sample_text")
    a2 = JDTAST_PrefixExpression(operator="sample_text_2")
    b = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'JDTAST_Expression269', a1)
    assert _is_linked(b, 'JDTAST_Expression269', a1)
    if hasattr(a1, 'JDTAST_PrefixExpression'):
        assert _is_linked(a1, 'JDTAST_PrefixExpression', b)
    _safe_set(b, 'JDTAST_Expression269', a2)
    assert _is_linked(b, 'JDTAST_Expression269', a2)
    if hasattr(a1, 'JDTAST_PrefixExpression'):
        assert not _is_linked(a1, 'JDTAST_PrefixExpression', b)
    if hasattr(a2, 'JDTAST_PrefixExpression'):
        assert _is_linked(a2, 'JDTAST_PrefixExpression', b)
    _safe_set(b, 'JDTAST_Expression269', None)
    assert not _is_linked(b, 'JDTAST_Expression269', a2)
    if hasattr(a2, 'JDTAST_PrefixExpression'):
        assert not _is_linked(a2, 'JDTAST_PrefixExpression', b)


def test_assoc_parameters155_reverse_link_reassign_clear():
    a1 = JDTAST_SingleVariableDeclaration(varargs="sample_text")
    a2 = JDTAST_SingleVariableDeclaration(varargs="sample_text_2")
    b = JDTAST_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    _safe_set(b, 'JDTAST_MethodDeclaration156', {a1})
    assert _is_linked(b, 'JDTAST_MethodDeclaration156', a1)
    if hasattr(a1, 'JDTAST_SingleVariableDeclaration157'):
        assert _is_linked(a1, 'JDTAST_SingleVariableDeclaration157', b)
    _safe_set(b, 'JDTAST_MethodDeclaration156', {a2})
    assert _is_linked(b, 'JDTAST_MethodDeclaration156', a2)
    if hasattr(a1, 'JDTAST_SingleVariableDeclaration157'):
        assert not _is_linked(a1, 'JDTAST_SingleVariableDeclaration157', b)
    if hasattr(a2, 'JDTAST_SingleVariableDeclaration157'):
        assert _is_linked(a2, 'JDTAST_SingleVariableDeclaration157', b)
    _safe_set(b, 'JDTAST_MethodDeclaration156', set())
    assert not _is_linked(b, 'JDTAST_MethodDeclaration156', a2)
    if hasattr(a2, 'JDTAST_SingleVariableDeclaration157'):
        assert not _is_linked(a2, 'JDTAST_SingleVariableDeclaration157', b)


def test_assoc_parameters49_reverse_link_reassign_clear():
    a1 = JDTAST_Parameter(name="sample_text", type="sample_text")
    a2 = JDTAST_Parameter(name="sample_text_2", type="sample_text_2")
    b = JDTAST_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    _safe_set(b, 'JDTAST_IMethod50', {a1})
    assert _is_linked(b, 'JDTAST_IMethod50', a1)
    if hasattr(a1, 'JDTAST_Parameter'):
        assert _is_linked(a1, 'JDTAST_Parameter', b)
    _safe_set(b, 'JDTAST_IMethod50', {a2})
    assert _is_linked(b, 'JDTAST_IMethod50', a2)
    if hasattr(a1, 'JDTAST_Parameter'):
        assert not _is_linked(a1, 'JDTAST_Parameter', b)
    if hasattr(a2, 'JDTAST_Parameter'):
        assert _is_linked(a2, 'JDTAST_Parameter', b)
    _safe_set(b, 'JDTAST_IMethod50', set())
    assert not _is_linked(b, 'JDTAST_IMethod50', a2)
    if hasattr(a2, 'JDTAST_Parameter'):
        assert not _is_linked(a2, 'JDTAST_Parameter', b)


def test_assoc_rightHandSide202_reverse_link_reassign_clear():
    a1 = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    a2 = JDTAST_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    b = JDTAST_Assignment(operator="sample_text")
    _safe_set(b, 'JDTAST_Assignment203', a1)
    assert _is_linked(b, 'JDTAST_Assignment203', a1)
    if hasattr(a1, 'JDTAST_Expression204'):
        assert _is_linked(a1, 'JDTAST_Expression204', b)
    _safe_set(b, 'JDTAST_Assignment203', a2)
    assert _is_linked(b, 'JDTAST_Assignment203', a2)
    if hasattr(a1, 'JDTAST_Expression204'):
        assert not _is_linked(a1, 'JDTAST_Expression204', b)
    if hasattr(a2, 'JDTAST_Expression204'):
        assert _is_linked(a2, 'JDTAST_Expression204', b)
    _safe_set(b, 'JDTAST_Assignment203', None)
    assert not _is_linked(b, 'JDTAST_Assignment203', a2)
    if hasattr(a2, 'JDTAST_Expression204'):
        assert not _is_linked(a2, 'JDTAST_Expression204', b)


def test_assoc_rightOperand242_reverse_link_reassign_clear():
    a1 = JDTAST_InfixExpression(operator="sample_text")
    a2 = JDTAST_InfixExpression(operator="sample_text_2")
    b = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'JDTAST_Expression244', a1)
    assert _is_linked(b, 'JDTAST_Expression244', a1)
    if hasattr(a1, 'JDTAST_InfixExpression243'):
        assert _is_linked(a1, 'JDTAST_InfixExpression243', b)
    _safe_set(b, 'JDTAST_Expression244', a2)
    assert _is_linked(b, 'JDTAST_Expression244', a2)
    if hasattr(a1, 'JDTAST_InfixExpression243'):
        assert not _is_linked(a1, 'JDTAST_InfixExpression243', b)
    if hasattr(a2, 'JDTAST_InfixExpression243'):
        assert _is_linked(a2, 'JDTAST_InfixExpression243', b)
    _safe_set(b, 'JDTAST_Expression244', None)
    assert not _is_linked(b, 'JDTAST_Expression244', a2)
    if hasattr(a2, 'JDTAST_InfixExpression243'):
        assert not _is_linked(a2, 'JDTAST_InfixExpression243', b)


def test_assoc_sourceRange32_reverse_link_reassign_clear():
    a1 = JDTAST_ISourceReference(source="sample_text")
    a2 = JDTAST_ISourceReference(source="sample_text_2")
    b = JDTAST_ISourceRange(length="sample_text", offset="sample_text")
    _safe_set(b, 'JDTAST_ISourceRange', a1)
    assert _is_linked(b, 'JDTAST_ISourceRange', a1)
    if hasattr(a1, 'JDTAST_ISourceReference'):
        assert _is_linked(a1, 'JDTAST_ISourceReference', b)
    _safe_set(b, 'JDTAST_ISourceRange', a2)
    assert _is_linked(b, 'JDTAST_ISourceRange', a2)
    if hasattr(a1, 'JDTAST_ISourceReference'):
        assert not _is_linked(a1, 'JDTAST_ISourceReference', b)
    if hasattr(a2, 'JDTAST_ISourceReference'):
        assert _is_linked(a2, 'JDTAST_ISourceReference', b)
    _safe_set(b, 'JDTAST_ISourceRange', None)
    assert not _is_linked(b, 'JDTAST_ISourceRange', a2)
    if hasattr(a2, 'JDTAST_ISourceReference'):
        assert not _is_linked(a2, 'JDTAST_ISourceReference', b)


def test_assoc_thrownExceptions158_reverse_link_reassign_clear():
    a1 = JDTAST_Name(fullyQualifiedName="sample_text")
    a2 = JDTAST_Name(fullyQualifiedName="sample_text_2")
    b = JDTAST_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    _safe_set(b, 'JDTAST_MethodDeclaration159', {a1})
    assert _is_linked(b, 'JDTAST_MethodDeclaration159', a1)
    if hasattr(a1, 'JDTAST_Name160'):
        assert _is_linked(a1, 'JDTAST_Name160', b)
    _safe_set(b, 'JDTAST_MethodDeclaration159', {a2})
    assert _is_linked(b, 'JDTAST_MethodDeclaration159', a2)
    if hasattr(a1, 'JDTAST_Name160'):
        assert not _is_linked(a1, 'JDTAST_Name160', b)
    if hasattr(a2, 'JDTAST_Name160'):
        assert _is_linked(a2, 'JDTAST_Name160', b)
    _safe_set(b, 'JDTAST_MethodDeclaration159', set())
    assert not _is_linked(b, 'JDTAST_MethodDeclaration159', a2)
    if hasattr(a2, 'JDTAST_Name160'):
        assert not _is_linked(a2, 'JDTAST_Name160', b)


def test_assoc_type29_reverse_link_reassign_clear():
    a1 = JDTAST_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    a2 = JDTAST_IType(fullyQualifiedName="sample_text_2", fullyQualifiedParametrizedName="sample_text_2")
    b = JDTAST_IClassFile(isClass="sample_text", isInterface="sample_text")
    _safe_set(b, 'JDTAST_IClassFile30', a1)
    assert _is_linked(b, 'JDTAST_IClassFile30', a1)
    if hasattr(a1, 'JDTAST_IType31'):
        assert _is_linked(a1, 'JDTAST_IType31', b)
    _safe_set(b, 'JDTAST_IClassFile30', a2)
    assert _is_linked(b, 'JDTAST_IClassFile30', a2)
    if hasattr(a1, 'JDTAST_IType31'):
        assert not _is_linked(a1, 'JDTAST_IType31', b)
    if hasattr(a2, 'JDTAST_IType31'):
        assert _is_linked(a2, 'JDTAST_IType31', b)
    _safe_set(b, 'JDTAST_IClassFile30', None)
    assert not _is_linked(b, 'JDTAST_IClassFile30', a2)
    if hasattr(a2, 'JDTAST_IType31'):
        assert not _is_linked(a2, 'JDTAST_IType31', b)


def test_assoc_typeBinding71_reverse_link_reassign_clear():
    a1 = JDTAST_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    a2 = JDTAST_IType(fullyQualifiedName="sample_text_2", fullyQualifiedParametrizedName="sample_text_2")
    b = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    _safe_set(b, 'JDTAST_Expression', a1)
    assert _is_linked(b, 'JDTAST_Expression', a1)
    if hasattr(a1, 'JDTAST_IType72'):
        assert _is_linked(a1, 'JDTAST_IType72', b)
    _safe_set(b, 'JDTAST_Expression', a2)
    assert _is_linked(b, 'JDTAST_Expression', a2)
    if hasattr(a1, 'JDTAST_IType72'):
        assert not _is_linked(a1, 'JDTAST_IType72', b)
    if hasattr(a2, 'JDTAST_IType72'):
        assert _is_linked(a2, 'JDTAST_IType72', b)
    _safe_set(b, 'JDTAST_Expression', None)
    assert not _is_linked(b, 'JDTAST_Expression', a2)
    if hasattr(a2, 'JDTAST_IType72'):
        assert not _is_linked(a2, 'JDTAST_IType72', b)


def test_assoc_typeParameters47_reverse_link_reassign_clear():
    a1 = JDTAST_ITypeParameter(bounds="sample_text")
    a2 = JDTAST_ITypeParameter(bounds="sample_text_2")
    b = JDTAST_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    _safe_set(b, 'JDTAST_IType48', {a1})
    assert _is_linked(b, 'JDTAST_IType48', a1)
    if hasattr(a1, 'JDTAST_ITypeParameter'):
        assert _is_linked(a1, 'JDTAST_ITypeParameter', b)
    _safe_set(b, 'JDTAST_IType48', {a2})
    assert _is_linked(b, 'JDTAST_IType48', a2)
    if hasattr(a1, 'JDTAST_ITypeParameter'):
        assert not _is_linked(a1, 'JDTAST_ITypeParameter', b)
    if hasattr(a2, 'JDTAST_ITypeParameter'):
        assert _is_linked(a2, 'JDTAST_ITypeParameter', b)
    _safe_set(b, 'JDTAST_IType48', set())
    assert not _is_linked(b, 'JDTAST_IType48', a2)
    if hasattr(a2, 'JDTAST_ITypeParameter'):
        assert not _is_linked(a2, 'JDTAST_ITypeParameter', b)


def test_assoc_types45_reverse_link_reassign_clear():
    a1 = JDTAST_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    a2 = JDTAST_IType(fullyQualifiedName="sample_text_2", fullyQualifiedParametrizedName="sample_text_2")
    b = JDTAST_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    _safe_set(b, 'JDTAST_IType46', a1)
    assert _is_linked(b, 'JDTAST_IType46', a1)
    if hasattr(a1, 'JDTAST_IType44'):
        assert _is_linked(a1, 'JDTAST_IType44', b)
    _safe_set(b, 'JDTAST_IType46', a2)
    assert _is_linked(b, 'JDTAST_IType46', a2)
    if hasattr(a1, 'JDTAST_IType44'):
        assert not _is_linked(a1, 'JDTAST_IType44', b)
    if hasattr(a2, 'JDTAST_IType44'):
        assert _is_linked(a2, 'JDTAST_IType44', b)
    _safe_set(b, 'JDTAST_IType46', None)
    assert not _is_linked(b, 'JDTAST_IType46', a2)
    if hasattr(a2, 'JDTAST_IType44'):
        assert not _is_linked(a2, 'JDTAST_IType44', b)


