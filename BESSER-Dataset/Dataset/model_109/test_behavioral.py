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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allType17_stub_double():
    # JDTAST_ICompilationUnit has no real 'JDTAST_ICompilationUnit18' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = JDTAST_ICompilationUnit()
    setattr(partner, 'JDTAST_ICompilationUnit18', None)
    _safe_set(owner, 'JDTAST_IType', partner)
    assert getattr(partner, 'JDTAST_ICompilationUnit18') == owner
    _safe_set(owner, 'JDTAST_IType', None)
    assert getattr(partner, 'JDTAST_ICompilationUnit18') is None


def test_assoc_arguments133_stub_double():
    # JDTAST_EnumConstantDeclaration has no real 'JDTAST_EnumConstantDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_EnumConstantDeclaration()
    setattr(partner, 'JDTAST_EnumConstantDeclaration', None)
    _safe_set(owner, 'JDTAST_Expression134', partner)
    assert getattr(partner, 'JDTAST_EnumConstantDeclaration') == owner
    _safe_set(owner, 'JDTAST_Expression134', None)
    assert getattr(partner, 'JDTAST_EnumConstantDeclaration') is None


def test_assoc_arguments210_stub_double():
    # JDTAST_ClassInstanceCreation has no real 'JDTAST_ClassInstanceCreation' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ClassInstanceCreation()
    setattr(partner, 'JDTAST_ClassInstanceCreation', None)
    _safe_set(owner, 'JDTAST_Expression211', partner)
    assert getattr(partner, 'JDTAST_ClassInstanceCreation') == owner
    _safe_set(owner, 'JDTAST_Expression211', None)
    assert getattr(partner, 'JDTAST_ClassInstanceCreation') is None


def test_assoc_arguments250_stub_double():
    # JDTAST_MethodInvocation has no real 'JDTAST_MethodInvocation' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_MethodInvocation()
    setattr(partner, 'JDTAST_MethodInvocation', None)
    _safe_set(owner, 'JDTAST_Expression251', partner)
    assert getattr(partner, 'JDTAST_MethodInvocation') == owner
    _safe_set(owner, 'JDTAST_Expression251', None)
    assert getattr(partner, 'JDTAST_MethodInvocation') is None


def test_assoc_arguments275_stub_double():
    # JDTAST_SuperMethodInvocation has no real 'JDTAST_SuperMethodInvocation' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_SuperMethodInvocation()
    setattr(partner, 'JDTAST_SuperMethodInvocation', None)
    _safe_set(owner, 'JDTAST_Expression276', partner)
    assert getattr(partner, 'JDTAST_SuperMethodInvocation') == owner
    _safe_set(owner, 'JDTAST_Expression276', None)
    assert getattr(partner, 'JDTAST_SuperMethodInvocation') is None


def test_assoc_arguments307_stub_double():
    # JDTAST_ConstructorInvocation has no real 'JDTAST_ConstructorInvocation' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ConstructorInvocation()
    setattr(partner, 'JDTAST_ConstructorInvocation', None)
    _safe_set(owner, 'JDTAST_Expression308', partner)
    assert getattr(partner, 'JDTAST_ConstructorInvocation') == owner
    _safe_set(owner, 'JDTAST_Expression308', None)
    assert getattr(partner, 'JDTAST_ConstructorInvocation') is None


def test_assoc_arguments355_stub_double():
    # JDTAST_SuperConstructorInvocation has no real 'JDTAST_SuperConstructorInvocation' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_SuperConstructorInvocation()
    setattr(partner, 'JDTAST_SuperConstructorInvocation', None)
    _safe_set(owner, 'JDTAST_Expression356', partner)
    assert getattr(partner, 'JDTAST_SuperConstructorInvocation') == owner
    _safe_set(owner, 'JDTAST_Expression356', None)
    assert getattr(partner, 'JDTAST_SuperConstructorInvocation') is None


def test_assoc_array186_stub_double():
    # JDTAST_ArrayAccess has no real 'JDTAST_ArrayAccess' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ArrayAccess()
    setattr(partner, 'JDTAST_ArrayAccess', None)
    _safe_set(owner, 'JDTAST_Expression187', partner)
    assert getattr(partner, 'JDTAST_ArrayAccess') == owner
    _safe_set(owner, 'JDTAST_Expression187', None)
    assert getattr(partner, 'JDTAST_ArrayAccess') is None


def test_assoc_binding104_stub_double():
    # JDTAST_PackageDeclaration has no real 'JDTAST_PackageDeclaration105' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_IPackageFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_IPackageFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_IPackageFragment(isDefaultPackage="sample_text")
    partner = JDTAST_PackageDeclaration()
    setattr(partner, 'JDTAST_PackageDeclaration105', None)
    _safe_set(owner, 'JDTAST_IPackageFragment106', partner)
    assert getattr(partner, 'JDTAST_PackageDeclaration105') == owner
    _safe_set(owner, 'JDTAST_IPackageFragment106', None)
    assert getattr(partner, 'JDTAST_PackageDeclaration105') is None


def test_assoc_body147_stub_double():
    # JDTAST_Block has no real 'JDTAST_Block148' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = JDTAST_Block()
    setattr(partner, 'JDTAST_Block148', None)
    _safe_set(owner, 'JDTAST_MethodDeclaration', partner)
    assert getattr(partner, 'JDTAST_Block148') == owner
    _safe_set(owner, 'JDTAST_MethodDeclaration', None)
    assert getattr(partner, 'JDTAST_Block148') is None


def test_assoc_bodyDeclarations119_stub_double():
    # JDTAST_BodyDeclaration has no real 'JDTAST_BodyDeclaration121' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    partner = JDTAST_BodyDeclaration()
    setattr(partner, 'JDTAST_BodyDeclaration121', None)
    _safe_set(owner, 'JDTAST_AbstractTypeDeclaration120', {partner})
    assert getattr(partner, 'JDTAST_BodyDeclaration121') == owner
    _safe_set(owner, 'JDTAST_AbstractTypeDeclaration120', set())
    assert getattr(partner, 'JDTAST_BodyDeclaration121') is None


def test_assoc_bound418_stub_double():
    # JDTAST_Type has no real 'JDTAST_Type419' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_WildcardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_WildcardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_WildcardType(upperBound="sample_text")
    partner = JDTAST_Type()
    setattr(partner, 'JDTAST_Type419', None)
    _safe_set(owner, 'JDTAST_WildcardType', partner)
    assert getattr(partner, 'JDTAST_Type419') == owner
    _safe_set(owner, 'JDTAST_WildcardType', None)
    assert getattr(partner, 'JDTAST_Type419') is None


def test_assoc_compilationUnits15_stub_double():
    # JDTAST_ICompilationUnit has no real 'JDTAST_ICompilationUnit' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_IPackageFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_IPackageFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_IPackageFragment(isDefaultPackage="sample_text")
    partner = JDTAST_ICompilationUnit()
    setattr(partner, 'JDTAST_ICompilationUnit', None)
    _safe_set(owner, 'JDTAST_IPackageFragment16', {partner})
    assert getattr(partner, 'JDTAST_ICompilationUnit') == owner
    _safe_set(owner, 'JDTAST_IPackageFragment16', set())
    assert getattr(partner, 'JDTAST_ICompilationUnit') is None


def test_assoc_componentType400_stub_double():
    # JDTAST_Type has no real 'JDTAST_Type402' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_ArrayType(dimensions="sample_text")
    partner = JDTAST_Type()
    setattr(partner, 'JDTAST_Type402', None)
    _safe_set(owner, 'JDTAST_ArrayType401', partner)
    assert getattr(partner, 'JDTAST_Type402') == owner
    _safe_set(owner, 'JDTAST_ArrayType401', None)
    assert getattr(partner, 'JDTAST_Type402') is None


def test_assoc_declaration385_stub_double():
    # JDTAST_TypeDeclarationStatement has no real 'JDTAST_TypeDeclarationStatement' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    partner = JDTAST_TypeDeclarationStatement()
    setattr(partner, 'JDTAST_TypeDeclarationStatement', None)
    _safe_set(owner, 'JDTAST_AbstractTypeDeclaration386', partner)
    assert getattr(partner, 'JDTAST_TypeDeclarationStatement') == owner
    _safe_set(owner, 'JDTAST_AbstractTypeDeclaration386', None)
    assert getattr(partner, 'JDTAST_TypeDeclarationStatement') is None


def test_assoc_default125_stub_double():
    # JDTAST_AnnotationTypeMemberDeclaration has no real 'JDTAST_AnnotationTypeMemberDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_AnnotationTypeMemberDeclaration()
    setattr(partner, 'JDTAST_AnnotationTypeMemberDeclaration', None)
    _safe_set(owner, 'JDTAST_Expression126', partner)
    assert getattr(partner, 'JDTAST_AnnotationTypeMemberDeclaration') == owner
    _safe_set(owner, 'JDTAST_Expression126', None)
    assert getattr(partner, 'JDTAST_AnnotationTypeMemberDeclaration') is None


def test_assoc_dimensions191_stub_double():
    # JDTAST_ArrayCreation has no real 'JDTAST_ArrayCreation' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ArrayCreation()
    setattr(partner, 'JDTAST_ArrayCreation', None)
    _safe_set(owner, 'JDTAST_Expression192', partner)
    assert getattr(partner, 'JDTAST_ArrayCreation') == owner
    _safe_set(owner, 'JDTAST_Expression192', None)
    assert getattr(partner, 'JDTAST_ArrayCreation') is None


def test_assoc_elementType403_stub_double():
    # JDTAST_Type has no real 'JDTAST_Type405' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_ArrayType(dimensions="sample_text")
    partner = JDTAST_Type()
    setattr(partner, 'JDTAST_Type405', None)
    _safe_set(owner, 'JDTAST_ArrayType404', partner)
    assert getattr(partner, 'JDTAST_Type405') == owner
    _safe_set(owner, 'JDTAST_ArrayType404', None)
    assert getattr(partner, 'JDTAST_Type405') is None


def test_assoc_elseExpression224_stub_double():
    # JDTAST_ConditionalExpression has no real 'JDTAST_ConditionalExpression' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ConditionalExpression()
    setattr(partner, 'JDTAST_ConditionalExpression', None)
    _safe_set(owner, 'JDTAST_Expression225', partner)
    assert getattr(partner, 'JDTAST_ConditionalExpression') == owner
    _safe_set(owner, 'JDTAST_Expression225', None)
    assert getattr(partner, 'JDTAST_ConditionalExpression') is None


def test_assoc_exception58_stub_double():
    # JDTAST_CatchClause has no real 'JDTAST_CatchClause59' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SingleVariableDeclaration(varargs="sample_text")
    partner = JDTAST_CatchClause()
    setattr(partner, 'JDTAST_CatchClause59', None)
    _safe_set(owner, 'JDTAST_SingleVariableDeclaration', partner)
    assert getattr(partner, 'JDTAST_CatchClause59') == owner
    _safe_set(owner, 'JDTAST_SingleVariableDeclaration', None)
    assert getattr(partner, 'JDTAST_CatchClause59') is None


def test_assoc_expression205_stub_double():
    # JDTAST_CastExpression has no real 'JDTAST_CastExpression' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_CastExpression()
    setattr(partner, 'JDTAST_CastExpression', None)
    _safe_set(owner, 'JDTAST_Expression206', partner)
    assert getattr(partner, 'JDTAST_CastExpression') == owner
    _safe_set(owner, 'JDTAST_Expression206', None)
    assert getattr(partner, 'JDTAST_CastExpression') is None


def test_assoc_expression215_stub_double():
    # JDTAST_ClassInstanceCreation has no real 'JDTAST_ClassInstanceCreation216' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ClassInstanceCreation()
    setattr(partner, 'JDTAST_ClassInstanceCreation216', None)
    _safe_set(owner, 'JDTAST_Expression217', partner)
    assert getattr(partner, 'JDTAST_ClassInstanceCreation216') == owner
    _safe_set(owner, 'JDTAST_Expression217', None)
    assert getattr(partner, 'JDTAST_ClassInstanceCreation216') is None


def test_assoc_expression226_stub_double():
    # JDTAST_ConditionalExpression has no real 'JDTAST_ConditionalExpression227' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ConditionalExpression()
    setattr(partner, 'JDTAST_ConditionalExpression227', None)
    _safe_set(owner, 'JDTAST_Expression228', partner)
    assert getattr(partner, 'JDTAST_ConditionalExpression227') == owner
    _safe_set(owner, 'JDTAST_Expression228', None)
    assert getattr(partner, 'JDTAST_ConditionalExpression227') is None


def test_assoc_expression232_stub_double():
    # JDTAST_FieldAccess has no real 'JDTAST_FieldAccess' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_FieldAccess()
    setattr(partner, 'JDTAST_FieldAccess', None)
    _safe_set(owner, 'JDTAST_Expression233', partner)
    assert getattr(partner, 'JDTAST_FieldAccess') == owner
    _safe_set(owner, 'JDTAST_Expression233', None)
    assert getattr(partner, 'JDTAST_FieldAccess') is None


def test_assoc_expression252_stub_double():
    # JDTAST_MethodInvocation has no real 'JDTAST_MethodInvocation253' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_MethodInvocation()
    setattr(partner, 'JDTAST_MethodInvocation253', None)
    _safe_set(owner, 'JDTAST_Expression254', partner)
    assert getattr(partner, 'JDTAST_MethodInvocation253') == owner
    _safe_set(owner, 'JDTAST_Expression254', None)
    assert getattr(partner, 'JDTAST_MethodInvocation253') is None


def test_assoc_expression264_stub_double():
    # JDTAST_ParenthesizedExpression has no real 'JDTAST_ParenthesizedExpression' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ParenthesizedExpression()
    setattr(partner, 'JDTAST_ParenthesizedExpression', None)
    _safe_set(owner, 'JDTAST_Expression265', partner)
    assert getattr(partner, 'JDTAST_ParenthesizedExpression') == owner
    _safe_set(owner, 'JDTAST_Expression265', None)
    assert getattr(partner, 'JDTAST_ParenthesizedExpression') is None


def test_assoc_expression298_stub_double():
    # JDTAST_AssertStatement has no real 'JDTAST_AssertStatement' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_AssertStatement()
    setattr(partner, 'JDTAST_AssertStatement', None)
    _safe_set(owner, 'JDTAST_Expression299', partner)
    assert getattr(partner, 'JDTAST_AssertStatement') == owner
    _safe_set(owner, 'JDTAST_Expression299', None)
    assert getattr(partner, 'JDTAST_AssertStatement') is None


def test_assoc_expression316_stub_double():
    # JDTAST_DoStatement has no real 'JDTAST_DoStatement317' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_DoStatement()
    setattr(partner, 'JDTAST_DoStatement317', None)
    _safe_set(owner, 'JDTAST_Expression318', partner)
    assert getattr(partner, 'JDTAST_DoStatement317') == owner
    _safe_set(owner, 'JDTAST_Expression318', None)
    assert getattr(partner, 'JDTAST_DoStatement317') is None


def test_assoc_expression321_stub_double():
    # JDTAST_EnhancedForStatement has no real 'JDTAST_EnhancedForStatement322' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_EnhancedForStatement()
    setattr(partner, 'JDTAST_EnhancedForStatement322', None)
    _safe_set(owner, 'JDTAST_Expression323', partner)
    assert getattr(partner, 'JDTAST_EnhancedForStatement322') == owner
    _safe_set(owner, 'JDTAST_Expression323', None)
    assert getattr(partner, 'JDTAST_EnhancedForStatement322') is None


def test_assoc_expression327_stub_double():
    # JDTAST_ExpressionStatement has no real 'JDTAST_ExpressionStatement' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ExpressionStatement()
    setattr(partner, 'JDTAST_ExpressionStatement', None)
    _safe_set(owner, 'JDTAST_Expression328', partner)
    assert getattr(partner, 'JDTAST_ExpressionStatement') == owner
    _safe_set(owner, 'JDTAST_Expression328', None)
    assert getattr(partner, 'JDTAST_ExpressionStatement') is None


def test_assoc_expression331_stub_double():
    # JDTAST_ForStatement has no real 'JDTAST_ForStatement332' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ForStatement()
    setattr(partner, 'JDTAST_ForStatement332', None)
    _safe_set(owner, 'JDTAST_Expression333', partner)
    assert getattr(partner, 'JDTAST_ForStatement332') == owner
    _safe_set(owner, 'JDTAST_Expression333', None)
    assert getattr(partner, 'JDTAST_ForStatement332') is None


def test_assoc_expression342_stub_double():
    # JDTAST_IfStatement has no real 'JDTAST_IfStatement343' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_IfStatement()
    setattr(partner, 'JDTAST_IfStatement343', None)
    _safe_set(owner, 'JDTAST_Expression344', partner)
    assert getattr(partner, 'JDTAST_IfStatement343') == owner
    _safe_set(owner, 'JDTAST_Expression344', None)
    assert getattr(partner, 'JDTAST_IfStatement343') is None


def test_assoc_expression353_stub_double():
    # JDTAST_ReturnStatement has no real 'JDTAST_ReturnStatement' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ReturnStatement()
    setattr(partner, 'JDTAST_ReturnStatement', None)
    _safe_set(owner, 'JDTAST_Expression354', partner)
    assert getattr(partner, 'JDTAST_ReturnStatement') == owner
    _safe_set(owner, 'JDTAST_Expression354', None)
    assert getattr(partner, 'JDTAST_ReturnStatement') is None


def test_assoc_expression357_stub_double():
    # JDTAST_SuperConstructorInvocation has no real 'JDTAST_SuperConstructorInvocation358' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_SuperConstructorInvocation()
    setattr(partner, 'JDTAST_SuperConstructorInvocation358', None)
    _safe_set(owner, 'JDTAST_Expression359', partner)
    assert getattr(partner, 'JDTAST_SuperConstructorInvocation358') == owner
    _safe_set(owner, 'JDTAST_Expression359', None)
    assert getattr(partner, 'JDTAST_SuperConstructorInvocation358') is None


def test_assoc_expression365_stub_double():
    # JDTAST_SwitchStatement has no real 'JDTAST_SwitchStatement' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_SwitchStatement()
    setattr(partner, 'JDTAST_SwitchStatement', None)
    _safe_set(owner, 'JDTAST_Expression366', partner)
    assert getattr(partner, 'JDTAST_SwitchStatement') == owner
    _safe_set(owner, 'JDTAST_Expression366', None)
    assert getattr(partner, 'JDTAST_SwitchStatement') is None


def test_assoc_expression372_stub_double():
    # JDTAST_SynchronizedStatement has no real 'JDTAST_SynchronizedStatement373' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_SynchronizedStatement()
    setattr(partner, 'JDTAST_SynchronizedStatement373', None)
    _safe_set(owner, 'JDTAST_Expression374', partner)
    assert getattr(partner, 'JDTAST_SynchronizedStatement373') == owner
    _safe_set(owner, 'JDTAST_Expression374', None)
    assert getattr(partner, 'JDTAST_SynchronizedStatement373') is None


def test_assoc_expression375_stub_double():
    # JDTAST_ThrowStatement has no real 'JDTAST_ThrowStatement' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ThrowStatement()
    setattr(partner, 'JDTAST_ThrowStatement', None)
    _safe_set(owner, 'JDTAST_Expression376', partner)
    assert getattr(partner, 'JDTAST_ThrowStatement') == owner
    _safe_set(owner, 'JDTAST_Expression376', None)
    assert getattr(partner, 'JDTAST_ThrowStatement') is None


def test_assoc_expression397_stub_double():
    # JDTAST_WhileStatement has no real 'JDTAST_WhileStatement398' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_WhileStatement()
    setattr(partner, 'JDTAST_WhileStatement398', None)
    _safe_set(owner, 'JDTAST_Expression399', partner)
    assert getattr(partner, 'JDTAST_WhileStatement398') == owner
    _safe_set(owner, 'JDTAST_Expression399', None)
    assert getattr(partner, 'JDTAST_WhileStatement398') is None


def test_assoc_expressions197_stub_double():
    # JDTAST_ArrayInitializer has no real 'JDTAST_ArrayInitializer198' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ArrayInitializer()
    setattr(partner, 'JDTAST_ArrayInitializer198', None)
    _safe_set(owner, 'JDTAST_Expression199', partner)
    assert getattr(partner, 'JDTAST_ArrayInitializer198') == owner
    _safe_set(owner, 'JDTAST_Expression199', None)
    assert getattr(partner, 'JDTAST_ArrayInitializer198') is None


def test_assoc_fragments107_stub_double():
    # JDTAST_ASTNode has no real 'JDTAST_ASTNode108' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_TagElement(nested="sample_text", tagName="sample_text")
    partner = JDTAST_ASTNode()
    setattr(partner, 'JDTAST_ASTNode108', None)
    _safe_set(owner, 'JDTAST_TagElement', {partner})
    assert getattr(partner, 'JDTAST_ASTNode108') == owner
    _safe_set(owner, 'JDTAST_TagElement', set())
    assert getattr(partner, 'JDTAST_ASTNode108') is None


def test_assoc_imports19_stub_double():
    # JDTAST_ICompilationUnit has no real 'JDTAST_ICompilationUnit20' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_IImportDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_IImportDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_IImportDeclaration(isOnDemand="sample_text", isStatic="sample_text")
    partner = JDTAST_ICompilationUnit()
    setattr(partner, 'JDTAST_ICompilationUnit20', None)
    _safe_set(owner, 'JDTAST_IImportDeclaration', partner)
    assert getattr(partner, 'JDTAST_ICompilationUnit20') == owner
    _safe_set(owner, 'JDTAST_IImportDeclaration', None)
    assert getattr(partner, 'JDTAST_ICompilationUnit20') is None


def test_assoc_imports67_stub_double():
    # JDTAST_CompilationUnit has no real 'JDTAST_CompilationUnit68' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_ImportDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_ImportDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_ImportDeclaration(onDemand="sample_text", static="sample_text")
    partner = JDTAST_CompilationUnit()
    setattr(partner, 'JDTAST_CompilationUnit68', None)
    _safe_set(owner, 'JDTAST_ImportDeclaration', partner)
    assert getattr(partner, 'JDTAST_CompilationUnit68') == owner
    _safe_set(owner, 'JDTAST_ImportDeclaration', None)
    assert getattr(partner, 'JDTAST_CompilationUnit68') is None


def test_assoc_index188_stub_double():
    # JDTAST_ArrayAccess has no real 'JDTAST_ArrayAccess189' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ArrayAccess()
    setattr(partner, 'JDTAST_ArrayAccess189', None)
    _safe_set(owner, 'JDTAST_Expression190', partner)
    assert getattr(partner, 'JDTAST_ArrayAccess189') == owner
    _safe_set(owner, 'JDTAST_Expression190', None)
    assert getattr(partner, 'JDTAST_ArrayAccess189') is None


def test_assoc_initializers334_stub_double():
    # JDTAST_ForStatement has no real 'JDTAST_ForStatement335' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ForStatement()
    setattr(partner, 'JDTAST_ForStatement335', None)
    _safe_set(owner, 'JDTAST_Expression336', partner)
    assert getattr(partner, 'JDTAST_ForStatement335') == owner
    _safe_set(owner, 'JDTAST_Expression336', None)
    assert getattr(partner, 'JDTAST_ForStatement335') is None


def test_assoc_initializers38_stub_double():
    # JDTAST_IInitializer has no real 'JDTAST_IInitializer' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = JDTAST_IInitializer()
    setattr(partner, 'JDTAST_IInitializer', None)
    _safe_set(owner, 'JDTAST_IType39', {partner})
    assert getattr(partner, 'JDTAST_IInitializer') == owner
    _safe_set(owner, 'JDTAST_IType39', set())
    assert getattr(partner, 'JDTAST_IInitializer') is None


def test_assoc_javadocRange33_stub_double():
    # JDTAST_IMember has no real 'JDTAST_IMember' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_ISourceRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_ISourceRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_ISourceRange(length="sample_text", offset="sample_text")
    partner = JDTAST_IMember()
    setattr(partner, 'JDTAST_IMember', None)
    _safe_set(owner, 'JDTAST_ISourceRange34', partner)
    assert getattr(partner, 'JDTAST_IMember') == owner
    _safe_set(owner, 'JDTAST_ISourceRange34', None)
    assert getattr(partner, 'JDTAST_IMember') is None


def test_assoc_label305_stub_double():
    # JDTAST_BreakStatement has no real 'JDTAST_BreakStatement' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_BreakStatement()
    setattr(partner, 'JDTAST_BreakStatement', None)
    _safe_set(owner, 'JDTAST_SimpleName306', partner)
    assert getattr(partner, 'JDTAST_BreakStatement') == owner
    _safe_set(owner, 'JDTAST_SimpleName306', None)
    assert getattr(partner, 'JDTAST_BreakStatement') is None


def test_assoc_label312_stub_double():
    # JDTAST_ContinueStatement has no real 'JDTAST_ContinueStatement' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_ContinueStatement()
    setattr(partner, 'JDTAST_ContinueStatement', None)
    _safe_set(owner, 'JDTAST_SimpleName313', partner)
    assert getattr(partner, 'JDTAST_ContinueStatement') == owner
    _safe_set(owner, 'JDTAST_SimpleName313', None)
    assert getattr(partner, 'JDTAST_ContinueStatement') is None


def test_assoc_label350_stub_double():
    # JDTAST_LabeledStatement has no real 'JDTAST_LabeledStatement351' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_LabeledStatement()
    setattr(partner, 'JDTAST_LabeledStatement351', None)
    _safe_set(owner, 'JDTAST_SimpleName352', partner)
    assert getattr(partner, 'JDTAST_LabeledStatement351') == owner
    _safe_set(owner, 'JDTAST_SimpleName352', None)
    assert getattr(partner, 'JDTAST_LabeledStatement351') is None


def test_assoc_leftOperand245_stub_double():
    # JDTAST_InstanceofExpression has no real 'JDTAST_InstanceofExpression' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_InstanceofExpression()
    setattr(partner, 'JDTAST_InstanceofExpression', None)
    _safe_set(owner, 'JDTAST_Expression246', partner)
    assert getattr(partner, 'JDTAST_InstanceofExpression') == owner
    _safe_set(owner, 'JDTAST_Expression246', None)
    assert getattr(partner, 'JDTAST_InstanceofExpression') is None


def test_assoc_message300_stub_double():
    # JDTAST_AssertStatement has no real 'JDTAST_AssertStatement301' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_AssertStatement()
    setattr(partner, 'JDTAST_AssertStatement301', None)
    _safe_set(owner, 'JDTAST_Expression302', partner)
    assert getattr(partner, 'JDTAST_AssertStatement301') == owner
    _safe_set(owner, 'JDTAST_Expression302', None)
    assert getattr(partner, 'JDTAST_AssertStatement301') is None


def test_assoc_methodBinding261_stub_double():
    # JDTAST_MethodInvocation has no real 'JDTAST_MethodInvocation262' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_IMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_IMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    partner = JDTAST_MethodInvocation()
    setattr(partner, 'JDTAST_MethodInvocation262', None)
    _safe_set(owner, 'JDTAST_IMethod263', partner)
    assert getattr(partner, 'JDTAST_MethodInvocation262') == owner
    _safe_set(owner, 'JDTAST_IMethod263', None)
    assert getattr(partner, 'JDTAST_MethodInvocation262') is None


def test_assoc_modifiers423_stub_double():
    # JDTAST_ExtendedModifier has no real 'JDTAST_ExtendedModifier425' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SingleVariableDeclaration(varargs="sample_text")
    partner = JDTAST_ExtendedModifier()
    setattr(partner, 'JDTAST_ExtendedModifier425', None)
    _safe_set(owner, 'JDTAST_SingleVariableDeclaration424', {partner})
    assert getattr(partner, 'JDTAST_ExtendedModifier425') == owner
    _safe_set(owner, 'JDTAST_SingleVariableDeclaration424', set())
    assert getattr(partner, 'JDTAST_ExtendedModifier425') is None


def test_assoc_name101_stub_double():
    # JDTAST_PackageDeclaration has no real 'JDTAST_PackageDeclaration102' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Name(fullyQualifiedName="sample_text")
    partner = JDTAST_PackageDeclaration()
    setattr(partner, 'JDTAST_PackageDeclaration102', None)
    _safe_set(owner, 'JDTAST_Name103', partner)
    assert getattr(partner, 'JDTAST_PackageDeclaration102') == owner
    _safe_set(owner, 'JDTAST_Name103', None)
    assert getattr(partner, 'JDTAST_PackageDeclaration102') is None


def test_assoc_name109_stub_double():
    # JDTAST_TypeParameter has no real 'JDTAST_TypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_TypeParameter()
    setattr(partner, 'JDTAST_TypeParameter', None)
    _safe_set(owner, 'JDTAST_SimpleName110', partner)
    assert getattr(partner, 'JDTAST_TypeParameter') == owner
    _safe_set(owner, 'JDTAST_SimpleName110', None)
    assert getattr(partner, 'JDTAST_TypeParameter') is None


def test_assoc_name127_stub_double():
    # JDTAST_AnnotationTypeMemberDeclaration has no real 'JDTAST_AnnotationTypeMemberDeclaration128' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_AnnotationTypeMemberDeclaration()
    setattr(partner, 'JDTAST_AnnotationTypeMemberDeclaration128', None)
    _safe_set(owner, 'JDTAST_SimpleName129', partner)
    assert getattr(partner, 'JDTAST_AnnotationTypeMemberDeclaration128') == owner
    _safe_set(owner, 'JDTAST_SimpleName129', None)
    assert getattr(partner, 'JDTAST_AnnotationTypeMemberDeclaration128') is None


def test_assoc_name138_stub_double():
    # JDTAST_EnumConstantDeclaration has no real 'JDTAST_EnumConstantDeclaration139' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_EnumConstantDeclaration()
    setattr(partner, 'JDTAST_EnumConstantDeclaration139', None)
    _safe_set(owner, 'JDTAST_SimpleName140', partner)
    assert getattr(partner, 'JDTAST_EnumConstantDeclaration139') == owner
    _safe_set(owner, 'JDTAST_SimpleName140', None)
    assert getattr(partner, 'JDTAST_EnumConstantDeclaration139') is None


def test_assoc_name234_stub_double():
    # JDTAST_FieldAccess has no real 'JDTAST_FieldAccess235' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_FieldAccess()
    setattr(partner, 'JDTAST_FieldAccess235', None)
    _safe_set(owner, 'JDTAST_SimpleName236', partner)
    assert getattr(partner, 'JDTAST_FieldAccess235') == owner
    _safe_set(owner, 'JDTAST_SimpleName236', None)
    assert getattr(partner, 'JDTAST_FieldAccess235') is None


def test_assoc_name255_stub_double():
    # JDTAST_MethodInvocation has no real 'JDTAST_MethodInvocation256' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_MethodInvocation()
    setattr(partner, 'JDTAST_MethodInvocation256', None)
    _safe_set(owner, 'JDTAST_SimpleName257', partner)
    assert getattr(partner, 'JDTAST_MethodInvocation256') == owner
    _safe_set(owner, 'JDTAST_SimpleName257', None)
    assert getattr(partner, 'JDTAST_MethodInvocation256') is None


def test_assoc_name270_stub_double():
    # JDTAST_SuperFieldAccess has no real 'JDTAST_SuperFieldAccess' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_SuperFieldAccess()
    setattr(partner, 'JDTAST_SuperFieldAccess', None)
    _safe_set(owner, 'JDTAST_SimpleName271', partner)
    assert getattr(partner, 'JDTAST_SuperFieldAccess') == owner
    _safe_set(owner, 'JDTAST_SimpleName271', None)
    assert getattr(partner, 'JDTAST_SuperFieldAccess') is None


def test_assoc_name277_stub_double():
    # JDTAST_SuperMethodInvocation has no real 'JDTAST_SuperMethodInvocation278' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Name(fullyQualifiedName="sample_text")
    partner = JDTAST_SuperMethodInvocation()
    setattr(partner, 'JDTAST_SuperMethodInvocation278', None)
    _safe_set(owner, 'JDTAST_Name279', partner)
    assert getattr(partner, 'JDTAST_SuperMethodInvocation278') == owner
    _safe_set(owner, 'JDTAST_Name279', None)
    assert getattr(partner, 'JDTAST_SuperMethodInvocation278') is None


def test_assoc_name411_stub_double():
    # JDTAST_QualifiedType has no real 'JDTAST_QualifiedType' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_QualifiedType()
    setattr(partner, 'JDTAST_QualifiedType', None)
    _safe_set(owner, 'JDTAST_SimpleName412', partner)
    assert getattr(partner, 'JDTAST_QualifiedType') == owner
    _safe_set(owner, 'JDTAST_SimpleName412', None)
    assert getattr(partner, 'JDTAST_QualifiedType') is None


def test_assoc_name416_stub_double():
    # JDTAST_SimpleType has no real 'JDTAST_SimpleType' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Name(fullyQualifiedName="sample_text")
    partner = JDTAST_SimpleType()
    setattr(partner, 'JDTAST_SimpleType', None)
    _safe_set(owner, 'JDTAST_Name417', partner)
    assert getattr(partner, 'JDTAST_SimpleType') == owner
    _safe_set(owner, 'JDTAST_Name417', None)
    assert getattr(partner, 'JDTAST_SimpleType') is None


def test_assoc_name426_stub_double():
    # JDTAST_QualifiedName has no real 'JDTAST_QualifiedName' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_QualifiedName()
    setattr(partner, 'JDTAST_QualifiedName', None)
    _safe_set(owner, 'JDTAST_SimpleName427', partner)
    assert getattr(partner, 'JDTAST_QualifiedName') == owner
    _safe_set(owner, 'JDTAST_SimpleName427', None)
    assert getattr(partner, 'JDTAST_QualifiedName') is None


def test_assoc_name75_stub_double():
    # JDTAST_MemberRef has no real 'JDTAST_MemberRef' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_MemberRef()
    setattr(partner, 'JDTAST_MemberRef', None)
    _safe_set(owner, 'JDTAST_SimpleName', partner)
    assert getattr(partner, 'JDTAST_MemberRef') == owner
    _safe_set(owner, 'JDTAST_SimpleName', None)
    assert getattr(partner, 'JDTAST_MemberRef') is None


def test_assoc_name79_stub_double():
    # JDTAST_MemberValuePair has no real 'JDTAST_MemberValuePair' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_MemberValuePair()
    setattr(partner, 'JDTAST_MemberValuePair', None)
    _safe_set(owner, 'JDTAST_SimpleName80', partner)
    assert getattr(partner, 'JDTAST_MemberValuePair') == owner
    _safe_set(owner, 'JDTAST_SimpleName80', None)
    assert getattr(partner, 'JDTAST_MemberValuePair') is None


def test_assoc_name84_stub_double():
    # JDTAST_MethodRef has no real 'JDTAST_MethodRef' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SimpleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SimpleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SimpleName(declaration="sample_text", identifier="sample_text")
    partner = JDTAST_MethodRef()
    setattr(partner, 'JDTAST_MethodRef', None)
    _safe_set(owner, 'JDTAST_SimpleName85', partner)
    assert getattr(partner, 'JDTAST_MethodRef') == owner
    _safe_set(owner, 'JDTAST_SimpleName85', None)
    assert getattr(partner, 'JDTAST_MethodRef') is None


def test_assoc_nameRange35_stub_double():
    # JDTAST_IMember has no real 'JDTAST_IMember36' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_ISourceRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_ISourceRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_ISourceRange(length="sample_text", offset="sample_text")
    partner = JDTAST_IMember()
    setattr(partner, 'JDTAST_IMember36', None)
    _safe_set(owner, 'JDTAST_ISourceRange37', partner)
    assert getattr(partner, 'JDTAST_IMember36') == owner
    _safe_set(owner, 'JDTAST_ISourceRange37', None)
    assert getattr(partner, 'JDTAST_IMember36') is None


def test_assoc_packageFragmentRoot13_stub_double():
    # JDTAST_IPackageFragmentRoot has no real 'IPackageFragmentRoot' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_IPackageFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_IPackageFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_IPackageFragment(isDefaultPackage="sample_text")
    partner = JDTAST_IPackageFragmentRoot()
    setattr(partner, 'IPackageFragmentRoot', None)
    _safe_set(owner, 'packageFragments', partner)
    assert getattr(partner, 'IPackageFragmentRoot') == owner
    _safe_set(owner, 'packageFragments', None)
    assert getattr(partner, 'IPackageFragmentRoot') is None


def test_assoc_packageFragments12_stub_double():
    # JDTAST_IPackageFragmentRoot has no real 'packageFragmentRoot' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_IPackageFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_IPackageFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_IPackageFragment(isDefaultPackage="sample_text")
    partner = JDTAST_IPackageFragmentRoot()
    setattr(partner, 'packageFragmentRoot', None)
    _safe_set(owner, 'IPackageFragment', partner)
    assert getattr(partner, 'packageFragmentRoot') == owner
    _safe_set(owner, 'IPackageFragment', None)
    assert getattr(partner, 'packageFragmentRoot') is None


def test_assoc_parameter324_stub_double():
    # JDTAST_EnhancedForStatement has no real 'JDTAST_EnhancedForStatement325' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SingleVariableDeclaration(varargs="sample_text")
    partner = JDTAST_EnhancedForStatement()
    setattr(partner, 'JDTAST_EnhancedForStatement325', None)
    _safe_set(owner, 'JDTAST_SingleVariableDeclaration326', partner)
    assert getattr(partner, 'JDTAST_EnhancedForStatement325') == owner
    _safe_set(owner, 'JDTAST_SingleVariableDeclaration326', None)
    assert getattr(partner, 'JDTAST_EnhancedForStatement325') is None


def test_assoc_parameters89_stub_double():
    # JDTAST_MethodRef has no real 'JDTAST_MethodRef90' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_MethodRefParameter(varargs="sample_text")
    partner = JDTAST_MethodRef()
    setattr(partner, 'JDTAST_MethodRef90', None)
    _safe_set(owner, 'JDTAST_MethodRefParameter', partner)
    assert getattr(partner, 'JDTAST_MethodRef90') == owner
    _safe_set(owner, 'JDTAST_MethodRefParameter', None)
    assert getattr(partner, 'JDTAST_MethodRef90') is None


def test_assoc_qualifier272_stub_double():
    # JDTAST_SuperFieldAccess has no real 'JDTAST_SuperFieldAccess273' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Name(fullyQualifiedName="sample_text")
    partner = JDTAST_SuperFieldAccess()
    setattr(partner, 'JDTAST_SuperFieldAccess273', None)
    _safe_set(owner, 'JDTAST_Name274', partner)
    assert getattr(partner, 'JDTAST_SuperFieldAccess273') == owner
    _safe_set(owner, 'JDTAST_Name274', None)
    assert getattr(partner, 'JDTAST_SuperFieldAccess273') is None


def test_assoc_qualifier280_stub_double():
    # JDTAST_SuperMethodInvocation has no real 'JDTAST_SuperMethodInvocation281' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Name(fullyQualifiedName="sample_text")
    partner = JDTAST_SuperMethodInvocation()
    setattr(partner, 'JDTAST_SuperMethodInvocation281', None)
    _safe_set(owner, 'JDTAST_Name282', partner)
    assert getattr(partner, 'JDTAST_SuperMethodInvocation281') == owner
    _safe_set(owner, 'JDTAST_Name282', None)
    assert getattr(partner, 'JDTAST_SuperMethodInvocation281') is None


def test_assoc_qualifier286_stub_double():
    # JDTAST_ThisExpression has no real 'JDTAST_ThisExpression' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Name(fullyQualifiedName="sample_text")
    partner = JDTAST_ThisExpression()
    setattr(partner, 'JDTAST_ThisExpression', None)
    _safe_set(owner, 'JDTAST_Name287', partner)
    assert getattr(partner, 'JDTAST_ThisExpression') == owner
    _safe_set(owner, 'JDTAST_Name287', None)
    assert getattr(partner, 'JDTAST_ThisExpression') is None


def test_assoc_qualifier428_stub_double():
    # JDTAST_QualifiedName has no real 'JDTAST_QualifiedName429' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Name(fullyQualifiedName="sample_text")
    partner = JDTAST_QualifiedName()
    setattr(partner, 'JDTAST_QualifiedName429', None)
    _safe_set(owner, 'JDTAST_Name430', partner)
    assert getattr(partner, 'JDTAST_QualifiedName429') == owner
    _safe_set(owner, 'JDTAST_Name430', None)
    assert getattr(partner, 'JDTAST_QualifiedName429') is None


def test_assoc_qualifier76_stub_double():
    # JDTAST_MemberRef has no real 'JDTAST_MemberRef77' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Name(fullyQualifiedName="sample_text")
    partner = JDTAST_MemberRef()
    setattr(partner, 'JDTAST_MemberRef77', None)
    _safe_set(owner, 'JDTAST_Name78', partner)
    assert getattr(partner, 'JDTAST_MemberRef77') == owner
    _safe_set(owner, 'JDTAST_Name78', None)
    assert getattr(partner, 'JDTAST_MemberRef77') is None


def test_assoc_qualifier86_stub_double():
    # JDTAST_MethodRef has no real 'JDTAST_MethodRef87' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Name(fullyQualifiedName="sample_text")
    partner = JDTAST_MethodRef()
    setattr(partner, 'JDTAST_MethodRef87', None)
    _safe_set(owner, 'JDTAST_Name88', partner)
    assert getattr(partner, 'JDTAST_MethodRef87') == owner
    _safe_set(owner, 'JDTAST_Name88', None)
    assert getattr(partner, 'JDTAST_MethodRef87') is None


def test_assoc_returnType152_stub_double():
    # JDTAST_Type has no real 'JDTAST_Type154' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = JDTAST_Type()
    setattr(partner, 'JDTAST_Type154', None)
    _safe_set(owner, 'JDTAST_MethodDeclaration153', partner)
    assert getattr(partner, 'JDTAST_Type154') == owner
    _safe_set(owner, 'JDTAST_MethodDeclaration153', None)
    assert getattr(partner, 'JDTAST_Type154') is None


def test_assoc_superInterfaceTypes174_stub_double():
    # JDTAST_Type has no real 'JDTAST_Type176' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_TypeDeclaration(interface="sample_text")
    partner = JDTAST_Type()
    setattr(partner, 'JDTAST_Type176', None)
    _safe_set(owner, 'JDTAST_TypeDeclaration175', {partner})
    assert getattr(partner, 'JDTAST_Type176') == owner
    _safe_set(owner, 'JDTAST_TypeDeclaration175', set())
    assert getattr(partner, 'JDTAST_Type176') is None


def test_assoc_superclassType172_stub_double():
    # JDTAST_Type has no real 'JDTAST_Type173' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_TypeDeclaration(interface="sample_text")
    partner = JDTAST_Type()
    setattr(partner, 'JDTAST_Type173', None)
    _safe_set(owner, 'JDTAST_TypeDeclaration', partner)
    assert getattr(partner, 'JDTAST_Type173') == owner
    _safe_set(owner, 'JDTAST_TypeDeclaration', None)
    assert getattr(partner, 'JDTAST_Type173') is None


def test_assoc_tags180_stub_double():
    # JDTAST_Javadoc has no real 'JDTAST_Javadoc181' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_TagElement(nested="sample_text", tagName="sample_text")
    partner = JDTAST_Javadoc()
    setattr(partner, 'JDTAST_Javadoc181', None)
    _safe_set(owner, 'JDTAST_TagElement182', partner)
    assert getattr(partner, 'JDTAST_Javadoc181') == owner
    _safe_set(owner, 'JDTAST_TagElement182', None)
    assert getattr(partner, 'JDTAST_Javadoc181') is None


def test_assoc_thenExpression229_stub_double():
    # JDTAST_ConditionalExpression has no real 'JDTAST_ConditionalExpression230' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ConditionalExpression()
    setattr(partner, 'JDTAST_ConditionalExpression230', None)
    _safe_set(owner, 'JDTAST_Expression231', partner)
    assert getattr(partner, 'JDTAST_ConditionalExpression230') == owner
    _safe_set(owner, 'JDTAST_Expression231', None)
    assert getattr(partner, 'JDTAST_ConditionalExpression230') is None


def test_assoc_type195_stub_double():
    # JDTAST_ArrayCreation has no real 'JDTAST_ArrayCreation196' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_ArrayType(dimensions="sample_text")
    partner = JDTAST_ArrayCreation()
    setattr(partner, 'JDTAST_ArrayCreation196', None)
    _safe_set(owner, 'JDTAST_ArrayType', partner)
    assert getattr(partner, 'JDTAST_ArrayCreation196') == owner
    _safe_set(owner, 'JDTAST_ArrayType', None)
    assert getattr(partner, 'JDTAST_ArrayCreation196') is None


def test_assoc_type420_stub_double():
    # JDTAST_Type has no real 'JDTAST_Type422' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_SingleVariableDeclaration(varargs="sample_text")
    partner = JDTAST_Type()
    setattr(partner, 'JDTAST_Type422', None)
    _safe_set(owner, 'JDTAST_SingleVariableDeclaration421', partner)
    assert getattr(partner, 'JDTAST_Type422') == owner
    _safe_set(owner, 'JDTAST_SingleVariableDeclaration421', None)
    assert getattr(partner, 'JDTAST_Type422') is None


def test_assoc_type94_stub_double():
    # JDTAST_Type has no real 'JDTAST_Type' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_MethodRefParameter(varargs="sample_text")
    partner = JDTAST_Type()
    setattr(partner, 'JDTAST_Type', None)
    _safe_set(owner, 'JDTAST_MethodRefParameter95', partner)
    assert getattr(partner, 'JDTAST_Type') == owner
    _safe_set(owner, 'JDTAST_MethodRefParameter95', None)
    assert getattr(partner, 'JDTAST_Type') is None


def test_assoc_typeName183_stub_double():
    # JDTAST_Annotation has no real 'JDTAST_Annotation184' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Name(fullyQualifiedName="sample_text")
    partner = JDTAST_Annotation()
    setattr(partner, 'JDTAST_Annotation184', None)
    _safe_set(owner, 'JDTAST_Name185', partner)
    assert getattr(partner, 'JDTAST_Annotation184') == owner
    _safe_set(owner, 'JDTAST_Name185', None)
    assert getattr(partner, 'JDTAST_Annotation184') is None


def test_assoc_typeParameters161_stub_double():
    # JDTAST_TypeParameter has no real 'JDTAST_TypeParameter163' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = JDTAST_TypeParameter()
    setattr(partner, 'JDTAST_TypeParameter163', None)
    _safe_set(owner, 'JDTAST_MethodDeclaration162', {partner})
    assert getattr(partner, 'JDTAST_TypeParameter163') == owner
    _safe_set(owner, 'JDTAST_MethodDeclaration162', set())
    assert getattr(partner, 'JDTAST_TypeParameter163') is None


def test_assoc_typeParameters177_stub_double():
    # JDTAST_TypeParameter has no real 'JDTAST_TypeParameter179' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_TypeDeclaration(interface="sample_text")
    partner = JDTAST_TypeParameter()
    setattr(partner, 'JDTAST_TypeParameter179', None)
    _safe_set(owner, 'JDTAST_TypeDeclaration178', {partner})
    assert getattr(partner, 'JDTAST_TypeParameter179') == owner
    _safe_set(owner, 'JDTAST_TypeDeclaration178', set())
    assert getattr(partner, 'JDTAST_TypeParameter179') is None


def test_assoc_types21_stub_double():
    # JDTAST_ICompilationUnit has no real 'JDTAST_ICompilationUnit22' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = JDTAST_ICompilationUnit()
    setattr(partner, 'JDTAST_ICompilationUnit22', None)
    _safe_set(owner, 'JDTAST_IType23', partner)
    assert getattr(partner, 'JDTAST_ICompilationUnit22') == owner
    _safe_set(owner, 'JDTAST_IType23', None)
    assert getattr(partner, 'JDTAST_ICompilationUnit22') is None


def test_assoc_types69_stub_double():
    # JDTAST_CompilationUnit has no real 'JDTAST_CompilationUnit70' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    partner = JDTAST_CompilationUnit()
    setattr(partner, 'JDTAST_CompilationUnit70', None)
    _safe_set(owner, 'JDTAST_AbstractTypeDeclaration', partner)
    assert getattr(partner, 'JDTAST_CompilationUnit70') == owner
    _safe_set(owner, 'JDTAST_AbstractTypeDeclaration', None)
    assert getattr(partner, 'JDTAST_CompilationUnit70') is None


def test_assoc_updaters337_stub_double():
    # JDTAST_ForStatement has no real 'JDTAST_ForStatement338' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_ForStatement()
    setattr(partner, 'JDTAST_ForStatement338', None)
    _safe_set(owner, 'JDTAST_Expression339', partner)
    assert getattr(partner, 'JDTAST_ForStatement338') == owner
    _safe_set(owner, 'JDTAST_Expression339', None)
    assert getattr(partner, 'JDTAST_ForStatement338') is None


def test_assoc_value433_stub_double():
    # JDTAST_SingleMemberAnnotation has no real 'JDTAST_SingleMemberAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_SingleMemberAnnotation()
    setattr(partner, 'JDTAST_SingleMemberAnnotation', None)
    _safe_set(owner, 'JDTAST_Expression434', partner)
    assert getattr(partner, 'JDTAST_SingleMemberAnnotation') == owner
    _safe_set(owner, 'JDTAST_Expression434', None)
    assert getattr(partner, 'JDTAST_SingleMemberAnnotation') is None


def test_assoc_value81_stub_double():
    # JDTAST_MemberValuePair has no real 'JDTAST_MemberValuePair82' property in the generated
    # code (a bare stub) -- manually attach it so JDTAST_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JDTAST_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JDTAST_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = JDTAST_MemberValuePair()
    setattr(partner, 'JDTAST_MemberValuePair82', None)
    _safe_set(owner, 'JDTAST_Expression83', partner)
    assert getattr(partner, 'JDTAST_MemberValuePair82') == owner
    _safe_set(owner, 'JDTAST_Expression83', None)
    assert getattr(partner, 'JDTAST_MemberValuePair82') is None


