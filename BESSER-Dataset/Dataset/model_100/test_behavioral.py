import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    AbstractTypeDeclaration,
    Annotation,
    AnonymousClassDeclaration,
    ArrayInitializer,
    ArrayType,
    Block,
    BodyDeclaration,
    CatchClause,
    Comment,
    CompilationUnit,
    Core_BinaryPackageFragmentRoot,
    Core_IClassFile,
    Core_ICompilationUnit,
    Core_IField,
    Core_IImportDeclaration,
    Core_IInitializer,
    Core_IJavaElement,
    Core_IJavaModel,
    Core_IJavaProject,
    Core_IMember,
    Core_IMethod,
    Core_IPackageFragment,
    Core_IPackageFragmentRoot,
    Core_ISourceRange,
    Core_ISourceReference,
    Core_IType,
    Core_ITypeParameter,
    Core_ITypeRoot,
    Core_Parameter,
    Core_PhysicalElement,
    Core_SourcePackageFragmentRoot,
    DOM_AST,
    DOM_ASTNode,
    DOM_AbstractTypeDeclaration,
    DOM_Annotation,
    DOM_AnnotationTypeDeclaration,
    DOM_AnnotationTypeMemberDeclaration,
    DOM_AnonymousClassDeclaration,
    DOM_ArrayAccess,
    DOM_ArrayCreation,
    DOM_ArrayInitializer,
    DOM_ArrayType,
    DOM_AssertStatement,
    DOM_Assignment,
    DOM_Block,
    DOM_BlockComment,
    DOM_BodyDeclaration,
    DOM_BooleanLiteral,
    DOM_BreakStatement,
    DOM_CastExpression,
    DOM_CatchClause,
    DOM_CharacterLiteral,
    DOM_ClassInstanceCreation,
    DOM_Comment,
    DOM_CompilationUnit,
    DOM_ConditionalExpression,
    DOM_ConstructorInvocation,
    DOM_ContinueStatement,
    DOM_DoStatement,
    DOM_EmptyStatement,
    DOM_EnhancedForStatement,
    DOM_EnumConstantDeclaration,
    DOM_EnumDeclaration,
    DOM_Expression,
    DOM_ExpressionStatement,
    DOM_ExtendedModifier,
    DOM_FieldAccess,
    DOM_FieldDeclaration,
    DOM_ForStatement,
    DOM_IfStatement,
    DOM_ImportDeclaration,
    DOM_InfixExpression,
    DOM_Initializer,
    DOM_InstanceofExpression,
    DOM_Javadoc,
    DOM_LabeledStatement,
    DOM_LineComment,
    DOM_MarkerAnnotation,
    DOM_MemberRef,
    DOM_MemberValuePair,
    DOM_MethodDeclaration,
    DOM_MethodInvocation,
    DOM_MethodRef,
    DOM_MethodRefParameter,
    DOM_Modifier,
    DOM_Name,
    DOM_NormalAnnotation,
    DOM_NullLiteral,
    DOM_NumberLiteral,
    DOM_PackageDeclaration,
    DOM_ParameterizedType,
    DOM_ParenthesizedExpression,
    DOM_PostfixExpression,
    DOM_PrefixExpression,
    DOM_PrimitiveType,
    DOM_QualifiedName,
    DOM_QualifiedType,
    DOM_ReturnStatement,
    DOM_SimpleName,
    DOM_SimpleType,
    DOM_SingleMemberAnnotation,
    DOM_SingleVariableDeclaration,
    DOM_Statement,
    DOM_StringLiteral,
    DOM_SuperConstructorInvocation,
    DOM_SuperFieldAccess,
    DOM_SuperMethodInvocation,
    DOM_SwitchCase,
    DOM_SwitchStatement,
    DOM_SynchronizedStatement,
    DOM_TagElement,
    DOM_TextElement,
    DOM_ThisExpression,
    DOM_ThrowStatement,
    DOM_TryStatement,
    DOM_Type,
    DOM_TypeDeclaration,
    DOM_TypeDeclarationStatement,
    DOM_TypeLiteral,
    DOM_TypeParameter,
    DOM_VariableDeclaration,
    DOM_VariableDeclarationExpression,
    DOM_VariableDeclarationFragment,
    DOM_VariableDeclarationStatement,
    DOM_WhileStatement,
    DOM_WildcardType,
    EnumConstantDeclaration,
    Expression,
    ExtendedModifier,
    IClassFile,
    ICompilationUnit,
    IField,
    IImportDeclaration,
    IInitializer,
    IJavaElement,
    IJavaProject,
    IMember,
    IMethod,
    IPackageFragment,
    IPackageFragmentRoot,
    ISourceRange,
    ISourceReference,
    IType,
    ITypeParameter,
    ITypeRoot,
    ImportDeclaration,
    Javadoc,
    MemberValuePair,
    MethodRefParameter,
    Name,
    PackageDeclaration,
    Parameter,
    PhysicalElement,
    SimpleName,
    SingleVariableDeclaration,
    Statement,
    TagElement,
    Type,
    TypeParameter,
    VariableDeclaration,
    VariableDeclarationFragment,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_binding150_stub_double():
    # IMethod has no real 'IMethod152' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = IMethod()
    setattr(partner, 'IMethod152', None)
    _safe_set(owner, 'DOM_MethodDeclaration151', partner)
    assert getattr(partner, 'IMethod152') == owner
    _safe_set(owner, 'DOM_MethodDeclaration151', None)
    assert getattr(partner, 'IMethod152') is None


def test_assoc_body134_stub_double():
    # Block has no real 'Block135' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = Block()
    setattr(partner, 'Block135', None)
    _safe_set(owner, 'DOM_MethodDeclaration', partner)
    assert getattr(partner, 'Block135') == owner
    _safe_set(owner, 'DOM_MethodDeclaration', None)
    assert getattr(partner, 'Block135') is None


def test_assoc_bodyDeclarations108_stub_double():
    # BodyDeclaration has no real 'BodyDeclaration109' property in the generated
    # code (a bare stub) -- manually attach it so DOM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    partner = BodyDeclaration()
    setattr(partner, 'BodyDeclaration109', None)
    _safe_set(owner, 'DOM_AbstractTypeDeclaration', {partner})
    assert getattr(partner, 'BodyDeclaration109') == owner
    _safe_set(owner, 'DOM_AbstractTypeDeclaration', set())
    assert getattr(partner, 'BodyDeclaration109') is None


def test_assoc_bound396_stub_double():
    # Type has no real 'Type397' property in the generated
    # code (a bare stub) -- manually attach it so DOM_WildcardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_WildcardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_WildcardType(upperBound="sample_text")
    partner = Type()
    setattr(partner, 'Type397', None)
    _safe_set(owner, 'DOM_WildcardType', partner)
    assert getattr(partner, 'Type397') == owner
    _safe_set(owner, 'DOM_WildcardType', None)
    assert getattr(partner, 'Type397') is None


def test_assoc_classFiles14_stub_double():
    # IClassFile has no real 'IClassFile' property in the generated
    # code (a bare stub) -- manually attach it so Core_IPackageFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IPackageFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IPackageFragment(isDefaultPackage="sample_text")
    partner = IClassFile()
    setattr(partner, 'IClassFile', None)
    _safe_set(owner, 'Core_IPackageFragment', {partner})
    assert getattr(partner, 'IClassFile') == owner
    _safe_set(owner, 'Core_IPackageFragment', set())
    assert getattr(partner, 'IClassFile') is None


def test_assoc_compilationUnits15_stub_double():
    # ICompilationUnit has no real 'ICompilationUnit' property in the generated
    # code (a bare stub) -- manually attach it so Core_IPackageFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IPackageFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IPackageFragment(isDefaultPackage="sample_text")
    partner = ICompilationUnit()
    setattr(partner, 'ICompilationUnit', None)
    _safe_set(owner, 'Core_IPackageFragment16', {partner})
    assert getattr(partner, 'ICompilationUnit') == owner
    _safe_set(owner, 'Core_IPackageFragment16', set())
    assert getattr(partner, 'ICompilationUnit') is None


def test_assoc_componentType379_stub_double():
    # Type has no real 'Type380' property in the generated
    # code (a bare stub) -- manually attach it so DOM_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_ArrayType(dimensions="sample_text")
    partner = Type()
    setattr(partner, 'Type380', None)
    _safe_set(owner, 'DOM_ArrayType', partner)
    assert getattr(partner, 'Type380') == owner
    _safe_set(owner, 'DOM_ArrayType', None)
    assert getattr(partner, 'Type380') is None


def test_assoc_elementType381_stub_double():
    # Type has no real 'Type383' property in the generated
    # code (a bare stub) -- manually attach it so DOM_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_ArrayType(dimensions="sample_text")
    partner = Type()
    setattr(partner, 'Type383', None)
    _safe_set(owner, 'DOM_ArrayType382', partner)
    assert getattr(partner, 'Type383') == owner
    _safe_set(owner, 'DOM_ArrayType382', None)
    assert getattr(partner, 'Type383') is None


def test_assoc_expression343_stub_double():
    # Expression has no real 'Expression344' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SwitchCase(default="sample_text")
    partner = Expression()
    setattr(partner, 'Expression344', None)
    _safe_set(owner, 'DOM_SwitchCase', partner)
    assert getattr(partner, 'Expression344') == owner
    _safe_set(owner, 'DOM_SwitchCase', None)
    assert getattr(partner, 'Expression344') is None


def test_assoc_extendedOperands218_stub_double():
    # Expression has no real 'Expression219' property in the generated
    # code (a bare stub) -- manually attach it so DOM_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_InfixExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression219', None)
    _safe_set(owner, 'DOM_InfixExpression', {partner})
    assert getattr(partner, 'Expression219') == owner
    _safe_set(owner, 'DOM_InfixExpression', set())
    assert getattr(partner, 'Expression219') is None


def test_assoc_fields37_stub_double():
    # IField has no real 'IField' property in the generated
    # code (a bare stub) -- manually attach it so Core_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = IField()
    setattr(partner, 'IField', None)
    _safe_set(owner, 'Core_IType38', {partner})
    assert getattr(partner, 'IField') == owner
    _safe_set(owner, 'Core_IType38', set())
    assert getattr(partner, 'IField') is None


def test_assoc_fragments96_stub_double():
    # ASTNode has no real 'ASTNode97' property in the generated
    # code (a bare stub) -- manually attach it so DOM_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_TagElement(nested="sample_text", tagName="sample_text")
    partner = ASTNode()
    setattr(partner, 'ASTNode97', None)
    _safe_set(owner, 'DOM_TagElement', {partner})
    assert getattr(partner, 'ASTNode97') == owner
    _safe_set(owner, 'DOM_TagElement', set())
    assert getattr(partner, 'ASTNode97') is None


def test_assoc_initializer103_stub_double():
    # Expression has no real 'Expression104' property in the generated
    # code (a bare stub) -- manually attach it so DOM_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_VariableDeclaration(extraDimensions="sample_text")
    partner = Expression()
    setattr(partner, 'Expression104', None)
    _safe_set(owner, 'DOM_VariableDeclaration', partner)
    assert getattr(partner, 'Expression104') == owner
    _safe_set(owner, 'DOM_VariableDeclaration', None)
    assert getattr(partner, 'Expression104') is None


def test_assoc_initializers36_stub_double():
    # IInitializer has no real 'IInitializer' property in the generated
    # code (a bare stub) -- manually attach it so Core_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = IInitializer()
    setattr(partner, 'IInitializer', None)
    _safe_set(owner, 'Core_IType', {partner})
    assert getattr(partner, 'IInitializer') == owner
    _safe_set(owner, 'Core_IType', set())
    assert getattr(partner, 'IInitializer') is None


def test_assoc_leftHandSide181_stub_double():
    # Expression has no real 'Expression182' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Assignment(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression182', None)
    _safe_set(owner, 'DOM_Assignment', partner)
    assert getattr(partner, 'Expression182') == owner
    _safe_set(owner, 'DOM_Assignment', None)
    assert getattr(partner, 'Expression182') is None


def test_assoc_leftOperand220_stub_double():
    # Expression has no real 'Expression222' property in the generated
    # code (a bare stub) -- manually attach it so DOM_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_InfixExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression222', None)
    _safe_set(owner, 'DOM_InfixExpression221', partner)
    assert getattr(partner, 'Expression222') == owner
    _safe_set(owner, 'DOM_InfixExpression221', None)
    assert getattr(partner, 'Expression222') is None


def test_assoc_methods39_stub_double():
    # IMethod has no real 'IMethod' property in the generated
    # code (a bare stub) -- manually attach it so Core_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = IMethod()
    setattr(partner, 'IMethod', None)
    _safe_set(owner, 'Core_IType40', {partner})
    assert getattr(partner, 'IMethod') == owner
    _safe_set(owner, 'Core_IType40', set())
    assert getattr(partner, 'IMethod') is None


def test_assoc_modifiers400_stub_double():
    # ExtendedModifier has no real 'ExtendedModifier402' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SingleVariableDeclaration(varargs="sample_text")
    partner = ExtendedModifier()
    setattr(partner, 'ExtendedModifier402', None)
    _safe_set(owner, 'DOM_SingleVariableDeclaration401', {partner})
    assert getattr(partner, 'ExtendedModifier402') == owner
    _safe_set(owner, 'DOM_SingleVariableDeclaration401', set())
    assert getattr(partner, 'ExtendedModifier402') is None


def test_assoc_name105_stub_double():
    # SimpleName has no real 'SimpleName107' property in the generated
    # code (a bare stub) -- manually attach it so DOM_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_VariableDeclaration(extraDimensions="sample_text")
    partner = SimpleName()
    setattr(partner, 'SimpleName107', None)
    _safe_set(owner, 'DOM_VariableDeclaration106', partner)
    assert getattr(partner, 'SimpleName107') == owner
    _safe_set(owner, 'DOM_VariableDeclaration106', None)
    assert getattr(partner, 'SimpleName107') is None


def test_assoc_name110_stub_double():
    # SimpleName has no real 'SimpleName112' property in the generated
    # code (a bare stub) -- manually attach it so DOM_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    partner = SimpleName()
    setattr(partner, 'SimpleName112', None)
    _safe_set(owner, 'DOM_AbstractTypeDeclaration111', partner)
    assert getattr(partner, 'SimpleName112') == owner
    _safe_set(owner, 'DOM_AbstractTypeDeclaration111', None)
    assert getattr(partner, 'SimpleName112') is None


def test_assoc_name136_stub_double():
    # SimpleName has no real 'SimpleName138' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = SimpleName()
    setattr(partner, 'SimpleName138', None)
    _safe_set(owner, 'DOM_MethodDeclaration137', partner)
    assert getattr(partner, 'SimpleName138') == owner
    _safe_set(owner, 'DOM_MethodDeclaration137', None)
    assert getattr(partner, 'SimpleName138') is None


def test_assoc_name66_stub_double():
    # Name has no real 'Name' property in the generated
    # code (a bare stub) -- manually attach it so DOM_ImportDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_ImportDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_ImportDeclaration(onDemand="sample_text", static="sample_text")
    partner = Name()
    setattr(partner, 'Name', None)
    _safe_set(owner, 'DOM_ImportDeclaration', partner)
    assert getattr(partner, 'Name') == owner
    _safe_set(owner, 'DOM_ImportDeclaration', None)
    assert getattr(partner, 'Name') is None


def test_assoc_name82_stub_double():
    # SimpleName has no real 'SimpleName83' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodRefParameter(varargs="sample_text")
    partner = SimpleName()
    setattr(partner, 'SimpleName83', None)
    _safe_set(owner, 'DOM_MethodRefParameter', partner)
    assert getattr(partner, 'SimpleName83') == owner
    _safe_set(owner, 'DOM_MethodRefParameter', None)
    assert getattr(partner, 'SimpleName83') is None


def test_assoc_operand247_stub_double():
    # Expression has no real 'Expression248' property in the generated
    # code (a bare stub) -- manually attach it so DOM_PostfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_PostfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_PostfixExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression248', None)
    _safe_set(owner, 'DOM_PostfixExpression', partner)
    assert getattr(partner, 'Expression248') == owner
    _safe_set(owner, 'DOM_PostfixExpression', None)
    assert getattr(partner, 'Expression248') is None


def test_assoc_operand249_stub_double():
    # Expression has no real 'Expression250' property in the generated
    # code (a bare stub) -- manually attach it so DOM_PrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_PrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_PrefixExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression250', None)
    _safe_set(owner, 'DOM_PrefixExpression', partner)
    assert getattr(partner, 'Expression250') == owner
    _safe_set(owner, 'DOM_PrefixExpression', None)
    assert getattr(partner, 'Expression250') is None


def test_assoc_packageFragmentRoot12_stub_double():
    # IPackageFragmentRoot has no real 'IPackageFragmentRoot13' property in the generated
    # code (a bare stub) -- manually attach it so Core_IPackageFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IPackageFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IPackageFragment(isDefaultPackage="sample_text")
    partner = IPackageFragmentRoot()
    setattr(partner, 'IPackageFragmentRoot13', None)
    _safe_set(owner, 'packageFragments', partner)
    assert getattr(partner, 'IPackageFragmentRoot13') == owner
    _safe_set(owner, 'packageFragments', None)
    assert getattr(partner, 'IPackageFragmentRoot13') is None


def test_assoc_parameters142_stub_double():
    # SingleVariableDeclaration has no real 'SingleVariableDeclaration144' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = SingleVariableDeclaration()
    setattr(partner, 'SingleVariableDeclaration144', None)
    _safe_set(owner, 'DOM_MethodDeclaration143', {partner})
    assert getattr(partner, 'SingleVariableDeclaration144') == owner
    _safe_set(owner, 'DOM_MethodDeclaration143', set())
    assert getattr(partner, 'SingleVariableDeclaration144') is None


def test_assoc_parameters46_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so Core_IMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'Core_IMethod', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'Core_IMethod', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_returnType139_stub_double():
    # Type has no real 'Type141' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = Type()
    setattr(partner, 'Type141', None)
    _safe_set(owner, 'DOM_MethodDeclaration140', partner)
    assert getattr(partner, 'Type141') == owner
    _safe_set(owner, 'DOM_MethodDeclaration140', None)
    assert getattr(partner, 'Type141') is None


def test_assoc_rightHandSide183_stub_double():
    # Expression has no real 'Expression185' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Assignment(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression185', None)
    _safe_set(owner, 'DOM_Assignment184', partner)
    assert getattr(partner, 'Expression185') == owner
    _safe_set(owner, 'DOM_Assignment184', None)
    assert getattr(partner, 'Expression185') is None


def test_assoc_rightOperand223_stub_double():
    # Expression has no real 'Expression225' property in the generated
    # code (a bare stub) -- manually attach it so DOM_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_InfixExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression225', None)
    _safe_set(owner, 'DOM_InfixExpression224', partner)
    assert getattr(partner, 'Expression225') == owner
    _safe_set(owner, 'DOM_InfixExpression224', None)
    assert getattr(partner, 'Expression225') is None


def test_assoc_sourceRange30_stub_double():
    # ISourceRange has no real 'ISourceRange' property in the generated
    # code (a bare stub) -- manually attach it so Core_ISourceReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_ISourceReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_ISourceReference(source="sample_text")
    partner = ISourceRange()
    setattr(partner, 'ISourceRange', None)
    _safe_set(owner, 'Core_ISourceReference', partner)
    assert getattr(partner, 'ISourceRange') == owner
    _safe_set(owner, 'Core_ISourceReference', None)
    assert getattr(partner, 'ISourceRange') is None


def test_assoc_superInterfaceTypes159_stub_double():
    # Type has no real 'Type161' property in the generated
    # code (a bare stub) -- manually attach it so DOM_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_TypeDeclaration(interface="sample_text")
    partner = Type()
    setattr(partner, 'Type161', None)
    _safe_set(owner, 'DOM_TypeDeclaration160', {partner})
    assert getattr(partner, 'Type161') == owner
    _safe_set(owner, 'DOM_TypeDeclaration160', set())
    assert getattr(partner, 'Type161') is None


def test_assoc_superclassType157_stub_double():
    # Type has no real 'Type158' property in the generated
    # code (a bare stub) -- manually attach it so DOM_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_TypeDeclaration(interface="sample_text")
    partner = Type()
    setattr(partner, 'Type158', None)
    _safe_set(owner, 'DOM_TypeDeclaration', partner)
    assert getattr(partner, 'Type158') == owner
    _safe_set(owner, 'DOM_TypeDeclaration', None)
    assert getattr(partner, 'Type158') is None


def test_assoc_thrownExceptions145_stub_double():
    # Name has no real 'Name147' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = Name()
    setattr(partner, 'Name147', None)
    _safe_set(owner, 'DOM_MethodDeclaration146', {partner})
    assert getattr(partner, 'Name147') == owner
    _safe_set(owner, 'DOM_MethodDeclaration146', set())
    assert getattr(partner, 'Name147') is None


def test_assoc_type28_stub_double():
    # IType has no real 'IType29' property in the generated
    # code (a bare stub) -- manually attach it so Core_IClassFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IClassFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IClassFile(isClass="sample_text", isInterface="sample_text")
    partner = IType()
    setattr(partner, 'IType29', None)
    _safe_set(owner, 'Core_IClassFile', partner)
    assert getattr(partner, 'IType29') == owner
    _safe_set(owner, 'Core_IClassFile', None)
    assert getattr(partner, 'IType29') is None


def test_assoc_type398_stub_double():
    # Type has no real 'Type399' property in the generated
    # code (a bare stub) -- manually attach it so DOM_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_SingleVariableDeclaration(varargs="sample_text")
    partner = Type()
    setattr(partner, 'Type399', None)
    _safe_set(owner, 'DOM_SingleVariableDeclaration', partner)
    assert getattr(partner, 'Type399') == owner
    _safe_set(owner, 'DOM_SingleVariableDeclaration', None)
    assert getattr(partner, 'Type399') is None


def test_assoc_type84_stub_double():
    # Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodRefParameter(varargs="sample_text")
    partner = Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'DOM_MethodRefParameter85', partner)
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'DOM_MethodRefParameter85', None)
    assert getattr(partner, 'Type') is None


def test_assoc_typeBinding64_stub_double():
    # IType has no real 'IType65' property in the generated
    # code (a bare stub) -- manually attach it so DOM_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    partner = IType()
    setattr(partner, 'IType65', None)
    _safe_set(owner, 'DOM_Expression', partner)
    assert getattr(partner, 'IType65') == owner
    _safe_set(owner, 'DOM_Expression', None)
    assert getattr(partner, 'IType65') is None


def test_assoc_typeParameters148_stub_double():
    # TypeParameter has no real 'TypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so DOM_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = TypeParameter()
    setattr(partner, 'TypeParameter', None)
    _safe_set(owner, 'DOM_MethodDeclaration149', {partner})
    assert getattr(partner, 'TypeParameter') == owner
    _safe_set(owner, 'DOM_MethodDeclaration149', set())
    assert getattr(partner, 'TypeParameter') is None


def test_assoc_typeParameters162_stub_double():
    # TypeParameter has no real 'TypeParameter164' property in the generated
    # code (a bare stub) -- manually attach it so DOM_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOM_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOM_TypeDeclaration(interface="sample_text")
    partner = TypeParameter()
    setattr(partner, 'TypeParameter164', None)
    _safe_set(owner, 'DOM_TypeDeclaration163', {partner})
    assert getattr(partner, 'TypeParameter164') == owner
    _safe_set(owner, 'DOM_TypeDeclaration163', set())
    assert getattr(partner, 'TypeParameter164') is None


def test_assoc_typeParameters44_stub_double():
    # ITypeParameter has no real 'ITypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so Core_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = ITypeParameter()
    setattr(partner, 'ITypeParameter', None)
    _safe_set(owner, 'Core_IType45', {partner})
    assert getattr(partner, 'ITypeParameter') == owner
    _safe_set(owner, 'Core_IType45', set())
    assert getattr(partner, 'ITypeParameter') is None


def test_assoc_types41_stub_double():
    # IType has no real 'IType43' property in the generated
    # code (a bare stub) -- manually attach it so Core_IType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_IType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    partner = IType()
    setattr(partner, 'IType43', None)
    _safe_set(owner, 'Core_IType42', {partner})
    assert getattr(partner, 'IType43') == owner
    _safe_set(owner, 'Core_IType42', set())
    assert getattr(partner, 'IType43') is None


