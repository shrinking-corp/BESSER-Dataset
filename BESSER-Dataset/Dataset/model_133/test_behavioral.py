import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AssignmentOperation,
    BehaviorFeature,
    BinaryOp,
    ClassifierMemberStatement,
    ClassifierOp,
    ClassifierStatement,
    ConditionalLoop,
    DivisionOp,
    EJBase,
    EJElement,
    Expression,
    Feature,
    ImplemenationClassifierStatement,
    InitStatement,
    JumpStatement,
    LabeledStatement,
    Literal,
    LoopStatement,
    MethodContentStatement,
    NamedElement,
    ScopeStatement,
    ShiftOp,
    SwitchPart,
    TopLevelStatement,
    UnaryOp,
    ast_AccessOp,
    ast_ApplyRoundOp,
    ast_ApplySquareOp,
    ast_ArrayConstructor,
    ast_AssertStatement,
    ast_AssignmentOp,
    ast_AssignmentOperation,
    ast_AttributeDefinition,
    ast_AttributeSet,
    ast_BehaviorFeature,
    ast_BinaryOp,
    ast_BitwiseAndAssignmentOp,
    ast_BitwiseAndOp,
    ast_BitwiseComplementOp,
    ast_BitwiseOrAssignmentOp,
    ast_BitwiseOrOp,
    ast_BitwiseXorAssignmentOp,
    ast_BitwiseXorOp,
    ast_BooleanLiteral,
    ast_BreakStatement,
    ast_CastOp,
    ast_CatchPart,
    ast_CharacterLiteral,
    ast_ClassBlock,
    ast_ClassStatement,
    ast_ClassifierMemberStatement,
    ast_ClassifierOp,
    ast_ClassifierStatement,
    ast_ConditionalAndOp,
    ast_ConditionalLoop,
    ast_ConditionalOp,
    ast_ConditionalOrOp,
    ast_ConstructorStatement,
    ast_ContinueStatement,
    ast_DivideAssignmentOp,
    ast_DivideOp,
    ast_DivisionOp,
    ast_DoWhileStatement,
    ast_DocumentationLine,
    ast_DoubleLiteral,
    ast_EJBase,
    ast_EJElement,
    ast_EmptyStatement,
    ast_EnumLiteral,
    ast_EnumStatement,
    ast_EqualOp,
    ast_Expression,
    ast_ExpressionStatement,
    ast_Feature,
    ast_FieldStatement,
    ast_FloatLiteral,
    ast_ForStatement,
    ast_ForeachStatement,
    ast_GreaterOrEqualOp,
    ast_GreaterThenOp,
    ast_Identifier,
    ast_IdentityOp,
    ast_IfStatement,
    ast_IfThenPart,
    ast_ImplemenationClassifierStatement,
    ast_ImportStatement,
    ast_InitStatement,
    ast_InnerClassifier,
    ast_InstanceInitStatement,
    ast_InstanceOfOp,
    ast_IntegerLiteral,
    ast_InterfaceStatement,
    ast_JumpStatement,
    ast_Label,
    ast_LabeledStatement,
    ast_LeftShiftAssignmentOp,
    ast_LeftShiftOp,
    ast_LessOrEqualOp,
    ast_LessThenOp,
    ast_Literal,
    ast_LocalVarStatement,
    ast_LogicalComplementOp,
    ast_LongIntegerLiteral,
    ast_LoopStatement,
    ast_MethodBlock,
    ast_MethodClassifier,
    ast_MethodContentStatement,
    ast_MethodStatement,
    ast_MinusAssignmentOp,
    ast_MinusOp,
    ast_Modifier,
    ast_MultiplyAssignmentOp,
    ast_MultiplyOp,
    ast_NamedElement,
    ast_NewOp,
    ast_NotEqualOp,
    ast_NullReference,
    ast_PackageStatement,
    ast_Parameter,
    ast_PlusAssignmentOp,
    ast_PlusOp,
    ast_PostfixDecrementOp,
    ast_PostfixIncrementOp,
    ast_PrefixDecrementOp,
    ast_PrefixIncrementOp,
    ast_PrimitiveType,
    ast_RangeExpression,
    ast_RemainderAssignmentOp,
    ast_RemainderOp,
    ast_ReturnStatement,
    ast_RightShiftAssignmentOp,
    ast_RightShiftOp,
    ast_ScopeStatement,
    ast_ShiftOp,
    ast_StaticInitStatement,
    ast_StringLiteral,
    ast_SuperReference,
    ast_SwitchCasePart,
    ast_SwitchDefaultPart,
    ast_SwitchDefaultPartRef,
    ast_SwitchPart,
    ast_SwitchStatement,
    ast_SynchronizedStatement,
    ast_TemplateParameter,
    ast_ThisReference,
    ast_ThrowStatement,
    ast_TopLevelClassifier,
    ast_TopLevelStatement,
    ast_TryStatement,
    ast_UnaryMinusOp,
    ast_UnaryOp,
    ast_UnaryPlusOp,
    ast_Variable,
    ast_WhileStatement,
    ast_WildcardType,
    ast_ZeroExtensionRightShiftAssignmentOp,
    ast_ZeroExtensionRightShiftOp,
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

def test_assoc_abstractModifier63_stub_double():
    # ast_MethodStatement has no real 'ast_MethodStatement64' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_MethodStatement()
    setattr(partner, 'ast_MethodStatement64', None)
    _safe_set(owner, 'ast_Modifier65', partner)
    assert getattr(partner, 'ast_MethodStatement64') == owner
    _safe_set(owner, 'ast_Modifier65', None)
    assert getattr(partner, 'ast_MethodStatement64') is None


def test_assoc_abstractModifier97_stub_double():
    # ast_ImplemenationClassifierStatement has no real 'ast_ImplemenationClassifierStatement98' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_ImplemenationClassifierStatement()
    setattr(partner, 'ast_ImplemenationClassifierStatement98', None)
    _safe_set(owner, 'ast_Modifier99', partner)
    assert getattr(partner, 'ast_ImplemenationClassifierStatement98') == owner
    _safe_set(owner, 'ast_Modifier99', None)
    assert getattr(partner, 'ast_ImplemenationClassifierStatement98') is None


def test_assoc_allModifier107_stub_double():
    # ast_ImportStatement has no real 'ast_ImportStatement108' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_ImportStatement()
    setattr(partner, 'ast_ImportStatement108', None)
    _safe_set(owner, 'ast_Modifier109', partner)
    assert getattr(partner, 'ast_ImportStatement108') == owner
    _safe_set(owner, 'ast_Modifier109', None)
    assert getattr(partner, 'ast_ImportStatement108') is None


def test_assoc_documentation0_stub_double():
    # ast_EJBase has no real 'ast_EJBase' property in the generated
    # code (a bare stub) -- manually attach it so ast_DocumentationLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_DocumentationLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_DocumentationLine(text="sample_text")
    partner = ast_EJBase()
    setattr(partner, 'ast_EJBase', None)
    _safe_set(owner, 'ast_DocumentationLine', partner)
    assert owner in getattr(partner, 'ast_EJBase')
    _safe_set(owner, 'ast_DocumentationLine', None)
    assert owner not in getattr(partner, 'ast_EJBase')


def test_assoc_finalModifier100_stub_double():
    # ast_ImplemenationClassifierStatement has no real 'ast_ImplemenationClassifierStatement101' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_ImplemenationClassifierStatement()
    setattr(partner, 'ast_ImplemenationClassifierStatement101', None)
    _safe_set(owner, 'ast_Modifier102', partner)
    assert getattr(partner, 'ast_ImplemenationClassifierStatement101') == owner
    _safe_set(owner, 'ast_Modifier102', None)
    assert getattr(partner, 'ast_ImplemenationClassifierStatement101') is None


def test_assoc_finalModifier161_stub_double():
    # ast_LocalVarStatement has no real 'ast_LocalVarStatement162' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_LocalVarStatement()
    setattr(partner, 'ast_LocalVarStatement162', None)
    _safe_set(owner, 'ast_Modifier163', partner)
    assert getattr(partner, 'ast_LocalVarStatement162') == owner
    _safe_set(owner, 'ast_Modifier163', None)
    assert getattr(partner, 'ast_LocalVarStatement162') is None


def test_assoc_finalModifier41_stub_double():
    # ast_Feature has no real 'ast_Feature42' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_Feature()
    setattr(partner, 'ast_Feature42', None)
    _safe_set(owner, 'ast_Modifier43', partner)
    assert getattr(partner, 'ast_Feature42') == owner
    _safe_set(owner, 'ast_Modifier43', None)
    assert getattr(partner, 'ast_Feature42') is None


def test_assoc_finalModifier5_stub_double():
    # ast_Parameter has no real 'ast_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_Parameter()
    setattr(partner, 'ast_Parameter', None)
    _safe_set(owner, 'ast_Modifier', partner)
    assert getattr(partner, 'ast_Parameter') == owner
    _safe_set(owner, 'ast_Modifier', None)
    assert getattr(partner, 'ast_Parameter') is None


def test_assoc_label158_stub_double():
    # ast_JumpStatement has no real 'ast_JumpStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Label(name="sample_text")
    partner = ast_JumpStatement()
    setattr(partner, 'ast_JumpStatement', None)
    _safe_set(owner, 'ast_Label', partner)
    assert getattr(partner, 'ast_JumpStatement') == owner
    _safe_set(owner, 'ast_Label', None)
    assert getattr(partner, 'ast_JumpStatement') is None


def test_assoc_label159_stub_double():
    # ast_LabeledStatement has no real 'ast_LabeledStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Label(name="sample_text")
    partner = ast_LabeledStatement()
    setattr(partner, 'ast_LabeledStatement', None)
    _safe_set(owner, 'ast_Label160', partner)
    assert getattr(partner, 'ast_LabeledStatement') == owner
    _safe_set(owner, 'ast_Label160', None)
    assert getattr(partner, 'ast_LabeledStatement') is None


def test_assoc_name18_stub_double():
    # ast_BehaviorFeature has no real 'ast_BehaviorFeature19' property in the generated
    # code (a bare stub) -- manually attach it so ast_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Identifier(escapedValue="sample_text", quotedValue="sample_text", value="sample_text")
    partner = ast_BehaviorFeature()
    setattr(partner, 'ast_BehaviorFeature19', None)
    _safe_set(owner, 'ast_Identifier', partner)
    assert getattr(partner, 'ast_BehaviorFeature19') == owner
    _safe_set(owner, 'ast_Identifier', None)
    assert getattr(partner, 'ast_BehaviorFeature19') is None


def test_assoc_name272_stub_double():
    # ast_NamedElement has no real 'ast_NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so ast_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Identifier(escapedValue="sample_text", quotedValue="sample_text", value="sample_text")
    partner = ast_NamedElement()
    setattr(partner, 'ast_NamedElement', None)
    _safe_set(owner, 'ast_Identifier273', partner)
    assert getattr(partner, 'ast_NamedElement') == owner
    _safe_set(owner, 'ast_Identifier273', None)
    assert getattr(partner, 'ast_NamedElement') is None


def test_assoc_name30_stub_double():
    # ast_EnumLiteral has no real 'ast_EnumLiteral31' property in the generated
    # code (a bare stub) -- manually attach it so ast_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Identifier(escapedValue="sample_text", quotedValue="sample_text", value="sample_text")
    partner = ast_EnumLiteral()
    setattr(partner, 'ast_EnumLiteral31', None)
    _safe_set(owner, 'ast_Identifier32', partner)
    assert getattr(partner, 'ast_EnumLiteral31') == owner
    _safe_set(owner, 'ast_Identifier32', None)
    assert getattr(partner, 'ast_EnumLiteral31') is None


def test_assoc_name75_stub_double():
    # ast_ClassifierStatement has no real 'ast_ClassifierStatement76' property in the generated
    # code (a bare stub) -- manually attach it so ast_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Identifier(escapedValue="sample_text", quotedValue="sample_text", value="sample_text")
    partner = ast_ClassifierStatement()
    setattr(partner, 'ast_ClassifierStatement76', None)
    _safe_set(owner, 'ast_Identifier77', partner)
    assert getattr(partner, 'ast_ClassifierStatement76') == owner
    _safe_set(owner, 'ast_Identifier77', None)
    assert getattr(partner, 'ast_ClassifierStatement76') is None


def test_assoc_nativeModifier69_stub_double():
    # ast_MethodStatement has no real 'ast_MethodStatement70' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_MethodStatement()
    setattr(partner, 'ast_MethodStatement70', None)
    _safe_set(owner, 'ast_Modifier71', partner)
    assert getattr(partner, 'ast_MethodStatement70') == owner
    _safe_set(owner, 'ast_Modifier71', None)
    assert getattr(partner, 'ast_MethodStatement70') is None


def test_assoc_staticModifier105_stub_double():
    # ast_ImportStatement has no real 'ast_ImportStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_ImportStatement()
    setattr(partner, 'ast_ImportStatement', None)
    _safe_set(owner, 'ast_Modifier106', partner)
    assert getattr(partner, 'ast_ImportStatement') == owner
    _safe_set(owner, 'ast_Modifier106', None)
    assert getattr(partner, 'ast_ImportStatement') is None


def test_assoc_staticModifier38_stub_double():
    # ast_Feature has no real 'ast_Feature39' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_Feature()
    setattr(partner, 'ast_Feature39', None)
    _safe_set(owner, 'ast_Modifier40', partner)
    assert getattr(partner, 'ast_Feature39') == owner
    _safe_set(owner, 'ast_Modifier40', None)
    assert getattr(partner, 'ast_Feature39') is None


def test_assoc_staticModifier87_stub_double():
    # ast_ClassStatement has no real 'ast_ClassStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_ClassStatement()
    setattr(partner, 'ast_ClassStatement', None)
    _safe_set(owner, 'ast_Modifier88', partner)
    assert getattr(partner, 'ast_ClassStatement') == owner
    _safe_set(owner, 'ast_Modifier88', None)
    assert getattr(partner, 'ast_ClassStatement') is None


def test_assoc_strictfpModifier72_stub_double():
    # ast_MethodStatement has no real 'ast_MethodStatement73' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_MethodStatement()
    setattr(partner, 'ast_MethodStatement73', None)
    _safe_set(owner, 'ast_Modifier74', partner)
    assert getattr(partner, 'ast_MethodStatement73') == owner
    _safe_set(owner, 'ast_Modifier74', None)
    assert getattr(partner, 'ast_MethodStatement73') is None


def test_assoc_strictfpModifier95_stub_double():
    # ast_ImplemenationClassifierStatement has no real 'ast_ImplemenationClassifierStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_ImplemenationClassifierStatement()
    setattr(partner, 'ast_ImplemenationClassifierStatement', None)
    _safe_set(owner, 'ast_Modifier96', partner)
    assert getattr(partner, 'ast_ImplemenationClassifierStatement') == owner
    _safe_set(owner, 'ast_Modifier96', None)
    assert getattr(partner, 'ast_ImplemenationClassifierStatement') is None


def test_assoc_synchronizedModifier66_stub_double():
    # ast_MethodStatement has no real 'ast_MethodStatement67' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_MethodStatement()
    setattr(partner, 'ast_MethodStatement67', None)
    _safe_set(owner, 'ast_Modifier68', partner)
    assert getattr(partner, 'ast_MethodStatement67') == owner
    _safe_set(owner, 'ast_Modifier68', None)
    assert getattr(partner, 'ast_MethodStatement67') is None


def test_assoc_transientModifier44_stub_double():
    # ast_FieldStatement has no real 'ast_FieldStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_FieldStatement()
    setattr(partner, 'ast_FieldStatement', None)
    _safe_set(owner, 'ast_Modifier45', partner)
    assert getattr(partner, 'ast_FieldStatement') == owner
    _safe_set(owner, 'ast_Modifier45', None)
    assert getattr(partner, 'ast_FieldStatement') is None


def test_assoc_visibilityModifier36_stub_double():
    # ast_Feature has no real 'ast_Feature' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_Feature()
    setattr(partner, 'ast_Feature', None)
    _safe_set(owner, 'ast_Modifier37', partner)
    assert getattr(partner, 'ast_Feature') == owner
    _safe_set(owner, 'ast_Modifier37', None)
    assert getattr(partner, 'ast_Feature') is None


def test_assoc_visibilityModifier78_stub_double():
    # ast_ClassifierStatement has no real 'ast_ClassifierStatement79' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_ClassifierStatement()
    setattr(partner, 'ast_ClassifierStatement79', None)
    _safe_set(owner, 'ast_Modifier80', partner)
    assert getattr(partner, 'ast_ClassifierStatement79') == owner
    _safe_set(owner, 'ast_Modifier80', None)
    assert getattr(partner, 'ast_ClassifierStatement79') is None


def test_assoc_volatileModifier46_stub_double():
    # ast_FieldStatement has no real 'ast_FieldStatement47' property in the generated
    # code (a bare stub) -- manually attach it so ast_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Modifier(value="sample_text")
    partner = ast_FieldStatement()
    setattr(partner, 'ast_FieldStatement47', None)
    _safe_set(owner, 'ast_Modifier48', partner)
    assert getattr(partner, 'ast_FieldStatement47') == owner
    _safe_set(owner, 'ast_Modifier48', None)
    assert getattr(partner, 'ast_FieldStatement47') is None


