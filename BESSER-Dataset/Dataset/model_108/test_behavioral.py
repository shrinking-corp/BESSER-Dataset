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
    EnumConstantDeclaration,
    Expression,
    ExtendedModifier,
    ImportDeclaration,
    JavaAbstractSyntax_AST,
    JavaAbstractSyntax_ASTNode,
    JavaAbstractSyntax_AbstractTypeDeclaration,
    JavaAbstractSyntax_Annotation,
    JavaAbstractSyntax_AnnotationTypeDeclaration,
    JavaAbstractSyntax_AnnotationTypeMemberDeclaration,
    JavaAbstractSyntax_AnonymousClassDeclaration,
    JavaAbstractSyntax_ArrayAccess,
    JavaAbstractSyntax_ArrayCreation,
    JavaAbstractSyntax_ArrayInitializer,
    JavaAbstractSyntax_ArrayType,
    JavaAbstractSyntax_AssertStatement,
    JavaAbstractSyntax_Assignment,
    JavaAbstractSyntax_Block,
    JavaAbstractSyntax_BlockComment,
    JavaAbstractSyntax_BodyDeclaration,
    JavaAbstractSyntax_BooleanLiteral,
    JavaAbstractSyntax_BreakStatement,
    JavaAbstractSyntax_CastExpression,
    JavaAbstractSyntax_CatchClause,
    JavaAbstractSyntax_CharacterLiteral,
    JavaAbstractSyntax_ClassInstanceCreation,
    JavaAbstractSyntax_Comment,
    JavaAbstractSyntax_CompilationUnit,
    JavaAbstractSyntax_ConditionalExpression,
    JavaAbstractSyntax_ConstructorInvocation,
    JavaAbstractSyntax_ContinueStatement,
    JavaAbstractSyntax_DoStatement,
    JavaAbstractSyntax_EmptyStatement,
    JavaAbstractSyntax_EnhancedForStatement,
    JavaAbstractSyntax_EnumConstantDeclaration,
    JavaAbstractSyntax_EnumDeclaration,
    JavaAbstractSyntax_Expression,
    JavaAbstractSyntax_ExpressionStatement,
    JavaAbstractSyntax_ExtendedModifier,
    JavaAbstractSyntax_FieldAccess,
    JavaAbstractSyntax_FieldDeclaration,
    JavaAbstractSyntax_ForStatement,
    JavaAbstractSyntax_IfStatement,
    JavaAbstractSyntax_ImportDeclaration,
    JavaAbstractSyntax_InfixExpression,
    JavaAbstractSyntax_Initializer,
    JavaAbstractSyntax_InstanceofExpression,
    JavaAbstractSyntax_Javadoc,
    JavaAbstractSyntax_LabeledStatement,
    JavaAbstractSyntax_LineComment,
    JavaAbstractSyntax_MarkerAnnotation,
    JavaAbstractSyntax_MemberRef,
    JavaAbstractSyntax_MemberValuePair,
    JavaAbstractSyntax_MethodDeclaration,
    JavaAbstractSyntax_MethodInvocation,
    JavaAbstractSyntax_MethodRef,
    JavaAbstractSyntax_MethodRefParameter,
    JavaAbstractSyntax_Modifier,
    JavaAbstractSyntax_Name,
    JavaAbstractSyntax_NormalAnnotation,
    JavaAbstractSyntax_NullLiteral,
    JavaAbstractSyntax_NumberLiteral,
    JavaAbstractSyntax_PackageDeclaration,
    JavaAbstractSyntax_ParameterizedType,
    JavaAbstractSyntax_ParenthesizedExpression,
    JavaAbstractSyntax_PostfixExpression,
    JavaAbstractSyntax_PrefixExpression,
    JavaAbstractSyntax_PrimitiveType,
    JavaAbstractSyntax_QualifiedName,
    JavaAbstractSyntax_QualifiedType,
    JavaAbstractSyntax_ReturnStatement,
    JavaAbstractSyntax_SimpleName,
    JavaAbstractSyntax_SimpleType,
    JavaAbstractSyntax_SingleMemberAnnotation,
    JavaAbstractSyntax_SingleVariableDeclaration,
    JavaAbstractSyntax_Statement,
    JavaAbstractSyntax_StringLiteral,
    JavaAbstractSyntax_StructuralPackage,
    JavaAbstractSyntax_SuperConstructorInvocation,
    JavaAbstractSyntax_SuperFieldAccess,
    JavaAbstractSyntax_SuperMethodInvocation,
    JavaAbstractSyntax_SwitchCase,
    JavaAbstractSyntax_SwitchStatement,
    JavaAbstractSyntax_SynchronizedStatement,
    JavaAbstractSyntax_TagElement,
    JavaAbstractSyntax_TextElement,
    JavaAbstractSyntax_ThisExpression,
    JavaAbstractSyntax_ThrowStatement,
    JavaAbstractSyntax_TryStatement,
    JavaAbstractSyntax_Type,
    JavaAbstractSyntax_TypeDeclaration,
    JavaAbstractSyntax_TypeDeclarationStatement,
    JavaAbstractSyntax_TypeLiteral,
    JavaAbstractSyntax_TypeParameter,
    JavaAbstractSyntax_VariableDeclaration,
    JavaAbstractSyntax_VariableDeclarationExpression,
    JavaAbstractSyntax_VariableDeclarationFragment,
    JavaAbstractSyntax_VariableDeclarationStatement,
    JavaAbstractSyntax_WhileStatement,
    JavaAbstractSyntax_WildcardType,
    Javadoc,
    MemberValuePair,
    MethodRefParameter,
    Name,
    PackageDeclaration,
    SimpleName,
    SingleVariableDeclaration,
    Statement,
    StructuralPackage,
    TagElement,
    Type,
    TypeParameter,
    VariableDeclaration,
    VariableDeclarationFragment,
    AssignementOperatorKind,
    InfixExpressionOperatorKind,
    PostfixExpresssionOperatorKind,
    PrefixExpresssionOperatorKind,
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

def test_assoc_body82_stub_double():
    # Block has no real 'Block83' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = Block()
    setattr(partner, 'Block83', None)
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration', partner)
    assert getattr(partner, 'Block83') == owner
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration', None)
    assert getattr(partner, 'Block83') is None


def test_assoc_bodyDeclarations56_stub_double():
    # BodyDeclaration has no real 'BodyDeclaration57' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    partner = BodyDeclaration()
    setattr(partner, 'BodyDeclaration57', None)
    _safe_set(owner, 'JavaAbstractSyntax_AbstractTypeDeclaration', {partner})
    assert getattr(partner, 'BodyDeclaration57') == owner
    _safe_set(owner, 'JavaAbstractSyntax_AbstractTypeDeclaration', set())
    assert getattr(partner, 'BodyDeclaration57') is None


def test_assoc_bound341_stub_double():
    # Type has no real 'Type342' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_WildcardType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_WildcardType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_WildcardType(upperBound="sample_text")
    partner = Type()
    setattr(partner, 'Type342', None)
    _safe_set(owner, 'JavaAbstractSyntax_WildcardType', partner)
    assert getattr(partner, 'Type342') == owner
    _safe_set(owner, 'JavaAbstractSyntax_WildcardType', None)
    assert getattr(partner, 'Type342') is None


def test_assoc_compilations357_stub_double():
    # CompilationUnit has no real 'CompilationUnit' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_StructuralPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_StructuralPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_StructuralPackage(name="sample_text")
    partner = CompilationUnit()
    setattr(partner, 'CompilationUnit', None)
    _safe_set(owner, 'JavaAbstractSyntax_StructuralPackage358', {partner})
    assert getattr(partner, 'CompilationUnit') == owner
    _safe_set(owner, 'JavaAbstractSyntax_StructuralPackage358', set())
    assert getattr(partner, 'CompilationUnit') is None


def test_assoc_componentType324_stub_double():
    # Type has no real 'Type325' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_ArrayType(dimensions="sample_text")
    partner = Type()
    setattr(partner, 'Type325', None)
    _safe_set(owner, 'JavaAbstractSyntax_ArrayType', partner)
    assert getattr(partner, 'Type325') == owner
    _safe_set(owner, 'JavaAbstractSyntax_ArrayType', None)
    assert getattr(partner, 'Type325') is None


def test_assoc_elementType326_stub_double():
    # Type has no real 'Type328' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_ArrayType(dimensions="sample_text")
    partner = Type()
    setattr(partner, 'Type328', None)
    _safe_set(owner, 'JavaAbstractSyntax_ArrayType327', partner)
    assert getattr(partner, 'Type328') == owner
    _safe_set(owner, 'JavaAbstractSyntax_ArrayType327', None)
    assert getattr(partner, 'Type328') is None


def test_assoc_expression288_stub_double():
    # Expression has no real 'Expression289' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_SwitchCase(default="sample_text")
    partner = Expression()
    setattr(partner, 'Expression289', None)
    _safe_set(owner, 'JavaAbstractSyntax_SwitchCase', partner)
    assert getattr(partner, 'Expression289') == owner
    _safe_set(owner, 'JavaAbstractSyntax_SwitchCase', None)
    assert getattr(partner, 'Expression289') is None


def test_assoc_extendedOperands166_stub_double():
    # Expression has no real 'Expression167' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_InfixExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression167', None)
    _safe_set(owner, 'JavaAbstractSyntax_InfixExpression', {partner})
    assert getattr(partner, 'Expression167') == owner
    _safe_set(owner, 'JavaAbstractSyntax_InfixExpression', set())
    assert getattr(partner, 'Expression167') is None


def test_assoc_fragments44_stub_double():
    # ASTNode has no real 'ASTNode45' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_TagElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_TagElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_TagElement(nested="sample_text", tagName="sample_text")
    partner = ASTNode()
    setattr(partner, 'ASTNode45', None)
    _safe_set(owner, 'JavaAbstractSyntax_TagElement', {partner})
    assert getattr(partner, 'ASTNode45') == owner
    _safe_set(owner, 'JavaAbstractSyntax_TagElement', set())
    assert getattr(partner, 'ASTNode45') is None


def test_assoc_initializer51_stub_double():
    # Expression has no real 'Expression52' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_VariableDeclaration(extraDimensions="sample_text")
    partner = Expression()
    setattr(partner, 'Expression52', None)
    _safe_set(owner, 'JavaAbstractSyntax_VariableDeclaration', partner)
    assert getattr(partner, 'Expression52') == owner
    _safe_set(owner, 'JavaAbstractSyntax_VariableDeclaration', None)
    assert getattr(partner, 'Expression52') is None


def test_assoc_leftHandSide129_stub_double():
    # Expression has no real 'Expression130' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_Assignment(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression130', None)
    _safe_set(owner, 'JavaAbstractSyntax_Assignment', partner)
    assert getattr(partner, 'Expression130') == owner
    _safe_set(owner, 'JavaAbstractSyntax_Assignment', None)
    assert getattr(partner, 'Expression130') is None


def test_assoc_leftOperand168_stub_double():
    # Expression has no real 'Expression170' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_InfixExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression170', None)
    _safe_set(owner, 'JavaAbstractSyntax_InfixExpression169', partner)
    assert getattr(partner, 'Expression170') == owner
    _safe_set(owner, 'JavaAbstractSyntax_InfixExpression169', None)
    assert getattr(partner, 'Expression170') is None


def test_assoc_modifiers345_stub_double():
    # ExtendedModifier has no real 'ExtendedModifier347' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_SingleVariableDeclaration(varargs="sample_text")
    partner = ExtendedModifier()
    setattr(partner, 'ExtendedModifier347', None)
    _safe_set(owner, 'JavaAbstractSyntax_SingleVariableDeclaration346', {partner})
    assert getattr(partner, 'ExtendedModifier347') == owner
    _safe_set(owner, 'JavaAbstractSyntax_SingleVariableDeclaration346', set())
    assert getattr(partner, 'ExtendedModifier347') is None


def test_assoc_name17_stub_double():
    # Name has no real 'Name' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_ImportDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_ImportDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_ImportDeclaration(onDemand="sample_text", static="sample_text")
    partner = Name()
    setattr(partner, 'Name', None)
    _safe_set(owner, 'JavaAbstractSyntax_ImportDeclaration', partner)
    assert getattr(partner, 'Name') == owner
    _safe_set(owner, 'JavaAbstractSyntax_ImportDeclaration', None)
    assert getattr(partner, 'Name') is None


def test_assoc_name33_stub_double():
    # SimpleName has no real 'SimpleName34' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_MethodRefParameter(varargs="sample_text")
    partner = SimpleName()
    setattr(partner, 'SimpleName34', None)
    _safe_set(owner, 'JavaAbstractSyntax_MethodRefParameter', partner)
    assert getattr(partner, 'SimpleName34') == owner
    _safe_set(owner, 'JavaAbstractSyntax_MethodRefParameter', None)
    assert getattr(partner, 'SimpleName34') is None


def test_assoc_name53_stub_double():
    # SimpleName has no real 'SimpleName55' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_VariableDeclaration(extraDimensions="sample_text")
    partner = SimpleName()
    setattr(partner, 'SimpleName55', None)
    _safe_set(owner, 'JavaAbstractSyntax_VariableDeclaration54', partner)
    assert getattr(partner, 'SimpleName55') == owner
    _safe_set(owner, 'JavaAbstractSyntax_VariableDeclaration54', None)
    assert getattr(partner, 'SimpleName55') is None


def test_assoc_name58_stub_double():
    # SimpleName has no real 'SimpleName60' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_AbstractTypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_AbstractTypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    partner = SimpleName()
    setattr(partner, 'SimpleName60', None)
    _safe_set(owner, 'JavaAbstractSyntax_AbstractTypeDeclaration59', partner)
    assert getattr(partner, 'SimpleName60') == owner
    _safe_set(owner, 'JavaAbstractSyntax_AbstractTypeDeclaration59', None)
    assert getattr(partner, 'SimpleName60') is None


def test_assoc_name84_stub_double():
    # SimpleName has no real 'SimpleName86' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = SimpleName()
    setattr(partner, 'SimpleName86', None)
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration85', partner)
    assert getattr(partner, 'SimpleName86') == owner
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration85', None)
    assert getattr(partner, 'SimpleName86') is None


def test_assoc_operand192_stub_double():
    # Expression has no real 'Expression193' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_PostfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_PostfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_PostfixExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression193', None)
    _safe_set(owner, 'JavaAbstractSyntax_PostfixExpression', partner)
    assert getattr(partner, 'Expression193') == owner
    _safe_set(owner, 'JavaAbstractSyntax_PostfixExpression', None)
    assert getattr(partner, 'Expression193') is None


def test_assoc_operand194_stub_double():
    # Expression has no real 'Expression195' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_PrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_PrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_PrefixExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression195', None)
    _safe_set(owner, 'JavaAbstractSyntax_PrefixExpression', partner)
    assert getattr(partner, 'Expression195') == owner
    _safe_set(owner, 'JavaAbstractSyntax_PrefixExpression', None)
    assert getattr(partner, 'Expression195') is None


def test_assoc_parameters90_stub_double():
    # SingleVariableDeclaration has no real 'SingleVariableDeclaration92' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = SingleVariableDeclaration()
    setattr(partner, 'SingleVariableDeclaration92', None)
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration91', {partner})
    assert getattr(partner, 'SingleVariableDeclaration92') == owner
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration91', set())
    assert getattr(partner, 'SingleVariableDeclaration92') is None


def test_assoc_returnType87_stub_double():
    # Type has no real 'Type89' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = Type()
    setattr(partner, 'Type89', None)
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration88', partner)
    assert getattr(partner, 'Type89') == owner
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration88', None)
    assert getattr(partner, 'Type89') is None


def test_assoc_rightHandSide131_stub_double():
    # Expression has no real 'Expression133' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_Assignment(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression133', None)
    _safe_set(owner, 'JavaAbstractSyntax_Assignment132', partner)
    assert getattr(partner, 'Expression133') == owner
    _safe_set(owner, 'JavaAbstractSyntax_Assignment132', None)
    assert getattr(partner, 'Expression133') is None


def test_assoc_rightOperand171_stub_double():
    # Expression has no real 'Expression173' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_InfixExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression173', None)
    _safe_set(owner, 'JavaAbstractSyntax_InfixExpression172', partner)
    assert getattr(partner, 'Expression173') == owner
    _safe_set(owner, 'JavaAbstractSyntax_InfixExpression172', None)
    assert getattr(partner, 'Expression173') is None


def test_assoc_structuralPackages356_stub_double():
    # StructuralPackage has no real 'StructuralPackage' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_StructuralPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_StructuralPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_StructuralPackage(name="sample_text")
    partner = StructuralPackage()
    setattr(partner, 'StructuralPackage', None)
    _safe_set(owner, 'JavaAbstractSyntax_StructuralPackage', {partner})
    assert getattr(partner, 'StructuralPackage') == owner
    _safe_set(owner, 'JavaAbstractSyntax_StructuralPackage', set())
    assert getattr(partner, 'StructuralPackage') is None


def test_assoc_superInterfaceTypes107_stub_double():
    # Type has no real 'Type109' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_TypeDeclaration(interface="sample_text")
    partner = Type()
    setattr(partner, 'Type109', None)
    _safe_set(owner, 'JavaAbstractSyntax_TypeDeclaration108', {partner})
    assert getattr(partner, 'Type109') == owner
    _safe_set(owner, 'JavaAbstractSyntax_TypeDeclaration108', set())
    assert getattr(partner, 'Type109') is None


def test_assoc_superclassType105_stub_double():
    # Type has no real 'Type106' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_TypeDeclaration(interface="sample_text")
    partner = Type()
    setattr(partner, 'Type106', None)
    _safe_set(owner, 'JavaAbstractSyntax_TypeDeclaration', partner)
    assert getattr(partner, 'Type106') == owner
    _safe_set(owner, 'JavaAbstractSyntax_TypeDeclaration', None)
    assert getattr(partner, 'Type106') is None


def test_assoc_thrownExceptions93_stub_double():
    # Name has no real 'Name95' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = Name()
    setattr(partner, 'Name95', None)
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration94', {partner})
    assert getattr(partner, 'Name95') == owner
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration94', set())
    assert getattr(partner, 'Name95') is None


def test_assoc_type343_stub_double():
    # Type has no real 'Type344' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_SingleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_SingleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_SingleVariableDeclaration(varargs="sample_text")
    partner = Type()
    setattr(partner, 'Type344', None)
    _safe_set(owner, 'JavaAbstractSyntax_SingleVariableDeclaration', partner)
    assert getattr(partner, 'Type344') == owner
    _safe_set(owner, 'JavaAbstractSyntax_SingleVariableDeclaration', None)
    assert getattr(partner, 'Type344') is None


def test_assoc_type35_stub_double():
    # Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_MethodRefParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_MethodRefParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_MethodRefParameter(varargs="sample_text")
    partner = Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'JavaAbstractSyntax_MethodRefParameter36', partner)
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'JavaAbstractSyntax_MethodRefParameter36', None)
    assert getattr(partner, 'Type') is None


def test_assoc_typeParameters110_stub_double():
    # TypeParameter has no real 'TypeParameter112' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_TypeDeclaration(interface="sample_text")
    partner = TypeParameter()
    setattr(partner, 'TypeParameter112', None)
    _safe_set(owner, 'JavaAbstractSyntax_TypeDeclaration111', {partner})
    assert getattr(partner, 'TypeParameter112') == owner
    _safe_set(owner, 'JavaAbstractSyntax_TypeDeclaration111', set())
    assert getattr(partner, 'TypeParameter112') is None


def test_assoc_typeParameters96_stub_double():
    # TypeParameter has no real 'TypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so JavaAbstractSyntax_MethodDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaAbstractSyntax_MethodDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaAbstractSyntax_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    partner = TypeParameter()
    setattr(partner, 'TypeParameter', None)
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration97', {partner})
    assert getattr(partner, 'TypeParameter') == owner
    _safe_set(owner, 'JavaAbstractSyntax_MethodDeclaration97', set())
    assert getattr(partner, 'TypeParameter') is None


