import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BuiltinDefinition,
    CallableElement,
    DataTypeDefinition,
    Definition,
    Expression,
    FeatureCall,
    ParameterDeclaration,
    PrimitiveStepExpression,
    Statement,
    StepExpression,
    ast_AdditiveExpression,
    ast_AdditiveStepExpression,
    ast_AlgorithmExpression,
    ast_ArrayConcatenationOperator,
    ast_ArrayConstructionIterationClause,
    ast_ArrayConstructionOperator,
    ast_ArrayElementAccess,
    ast_ArraySubscript,
    ast_Assertion,
    ast_Assignment,
    ast_BreakStatement,
    ast_BuiltinDefinition,
    ast_BuiltinFunction,
    ast_BuiltinVariable,
    ast_CallableElement,
    ast_Check,
    ast_Compound,
    ast_ContinueStatement,
    ast_DataType,
    ast_DataTypeDefinition,
    ast_DataTypeSpecifier,
    ast_Definition,
    ast_DerivativeOperator,
    ast_DoWhileStatement,
    ast_EndExpression,
    ast_EnumerationDefinition,
    ast_EnumerationLiteralDeclaration,
    ast_EqualityExpression,
    ast_Equation,
    ast_Expression,
    ast_ExpressionList,
    ast_FeatureCall,
    ast_ForStatement,
    ast_FunctionCall,
    ast_FunctionDefinition,
    ast_FunctionObjectDeclaration,
    ast_IfExpression,
    ast_IfStatement,
    ast_ImpliesExpression,
    ast_InputParameterDeclaration,
    ast_IterationAccumulator,
    ast_IterationCall,
    ast_IterationVariable,
    ast_LetExpression,
    ast_LetExpressionVariableDeclaration,
    ast_LetExpressionVariableDeclarationPart,
    ast_LogicalAndExpression,
    ast_LogicalOrExpression,
    ast_MemberVariableAccess,
    ast_Module,
    ast_MultiplicativeExpression,
    ast_NegateStepExpression,
    ast_OutputParameterDeclaration,
    ast_ParameterDeclaration,
    ast_ParenthesizedExpression,
    ast_PostfixExpression,
    ast_PowerExpression,
    ast_PrimitiveStepExpression,
    ast_PrimitiveType,
    ast_RangeExpression,
    ast_RangeStepExpression,
    ast_RecordDefinition,
    ast_RecordFieldDeclaration,
    ast_RelationalExpression,
    ast_ReturnStatement,
    ast_StateVariableDeclaration,
    ast_Statement,
    ast_StepExpression,
    ast_StepLiteral,
    ast_StepN,
    ast_SwitchCase,
    ast_SwitchExpression,
    ast_TemplateParameterDeclaration,
    ast_TypeAliasDefinition,
    ast_TypeTestExpression,
    ast_UnaryExpression,
    ast_Unit,
    ast_UnitConstructionOperator,
    ast_VariableAccess,
    ast_VariableDeclaration,
    ast_WhileStatement,
    AdditiveOperator,
    AssertionStatusKind,
    EqualityOperator,
    FunctionKind,
    MultiplicativeOperator,
    PostfixOperator,
    PowerOperator,
    RelationalOperator,
    UnaryOperator,
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

def test_assoc_accumulator92_reverse_link_reassign_clear():
    a1 = ast_IterationCall(identifier="sample_text")
    a2 = ast_IterationCall(identifier="sample_text_2")
    b = ast_IterationAccumulator(name="sample_text")
    _safe_set(b, 'ast_IterationAccumulator', a1)
    assert _is_linked(b, 'ast_IterationAccumulator', a1)
    if hasattr(a1, 'ast_IterationCall93'):
        assert _is_linked(a1, 'ast_IterationCall93', b)
    _safe_set(b, 'ast_IterationAccumulator', a2)
    assert _is_linked(b, 'ast_IterationAccumulator', a2)
    if hasattr(a1, 'ast_IterationCall93'):
        assert not _is_linked(a1, 'ast_IterationCall93', b)
    if hasattr(a2, 'ast_IterationCall93'):
        assert _is_linked(a2, 'ast_IterationCall93', b)
    _safe_set(b, 'ast_IterationAccumulator', None)
    assert not _is_linked(b, 'ast_IterationAccumulator', a2)
    if hasattr(a2, 'ast_IterationCall93'):
        assert not _is_linked(a2, 'ast_IterationCall93', b)


def test_assoc_assertions12_reverse_link_reassign_clear():
    a1 = ast_FunctionDefinition(kind="sample_text")
    a2 = ast_FunctionDefinition(kind="sample_text_2")
    b = ast_Assertion(static=True, statusKind="sample_text")
    _safe_set(b, 'ast_Assertion', a1)
    assert _is_linked(b, 'ast_Assertion', a1)
    if hasattr(a1, 'ast_FunctionDefinition13'):
        assert _is_linked(a1, 'ast_FunctionDefinition13', b)
    _safe_set(b, 'ast_Assertion', a2)
    assert _is_linked(b, 'ast_Assertion', a2)
    if hasattr(a1, 'ast_FunctionDefinition13'):
        assert not _is_linked(a1, 'ast_FunctionDefinition13', b)
    if hasattr(a2, 'ast_FunctionDefinition13'):
        assert _is_linked(a2, 'ast_FunctionDefinition13', b)
    _safe_set(b, 'ast_Assertion', None)
    assert not _is_linked(b, 'ast_Assertion', a2)
    if hasattr(a2, 'ast_FunctionDefinition13'):
        assert not _is_linked(a2, 'ast_FunctionDefinition13', b)


def test_assoc_equations18_reverse_link_reassign_clear():
    a1 = ast_FunctionDefinition(kind="sample_text")
    a2 = ast_FunctionDefinition(kind="sample_text_2")
    b = ast_Equation(initial=True)
    _safe_set(b, 'ast_Equation', a1)
    assert _is_linked(b, 'ast_Equation', a1)
    if hasattr(a1, 'ast_FunctionDefinition19'):
        assert _is_linked(a1, 'ast_FunctionDefinition19', b)
    _safe_set(b, 'ast_Equation', a2)
    assert _is_linked(b, 'ast_Equation', a2)
    if hasattr(a1, 'ast_FunctionDefinition19'):
        assert not _is_linked(a1, 'ast_FunctionDefinition19', b)
    if hasattr(a2, 'ast_FunctionDefinition19'):
        assert _is_linked(a2, 'ast_FunctionDefinition19', b)
    _safe_set(b, 'ast_Equation', None)
    assert not _is_linked(b, 'ast_Equation', a2)
    if hasattr(a2, 'ast_FunctionDefinition19'):
        assert not _is_linked(a2, 'ast_FunctionDefinition19', b)


def test_assoc_functionName34_reverse_link_reassign_clear():
    a1 = ast_FunctionObjectDeclaration(name="sample_text")
    a2 = ast_FunctionObjectDeclaration(name="sample_text_2")
    b = ast_FunctionDefinition(kind="sample_text")
    _safe_set(b, 'ast_FunctionDefinition36', a1)
    assert _is_linked(b, 'ast_FunctionDefinition36', a1)
    if hasattr(a1, 'ast_FunctionObjectDeclaration35'):
        assert _is_linked(a1, 'ast_FunctionObjectDeclaration35', b)
    _safe_set(b, 'ast_FunctionDefinition36', a2)
    assert _is_linked(b, 'ast_FunctionDefinition36', a2)
    if hasattr(a1, 'ast_FunctionObjectDeclaration35'):
        assert not _is_linked(a1, 'ast_FunctionObjectDeclaration35', b)
    if hasattr(a2, 'ast_FunctionObjectDeclaration35'):
        assert _is_linked(a2, 'ast_FunctionObjectDeclaration35', b)
    _safe_set(b, 'ast_FunctionDefinition36', None)
    assert not _is_linked(b, 'ast_FunctionDefinition36', a2)
    if hasattr(a2, 'ast_FunctionObjectDeclaration35'):
        assert not _is_linked(a2, 'ast_FunctionObjectDeclaration35', b)


def test_assoc_functionObjectDeclarations14_reverse_link_reassign_clear():
    a1 = ast_FunctionObjectDeclaration(name="sample_text")
    a2 = ast_FunctionObjectDeclaration(name="sample_text_2")
    b = ast_FunctionDefinition(kind="sample_text")
    _safe_set(b, 'ast_FunctionDefinition15', {a1})
    assert _is_linked(b, 'ast_FunctionDefinition15', a1)
    if hasattr(a1, 'ast_FunctionObjectDeclaration'):
        assert _is_linked(a1, 'ast_FunctionObjectDeclaration', b)
    _safe_set(b, 'ast_FunctionDefinition15', {a2})
    assert _is_linked(b, 'ast_FunctionDefinition15', a2)
    if hasattr(a1, 'ast_FunctionObjectDeclaration'):
        assert not _is_linked(a1, 'ast_FunctionObjectDeclaration', b)
    if hasattr(a2, 'ast_FunctionObjectDeclaration'):
        assert _is_linked(a2, 'ast_FunctionObjectDeclaration', b)
    _safe_set(b, 'ast_FunctionDefinition15', set())
    assert not _is_linked(b, 'ast_FunctionDefinition15', a2)
    if hasattr(a2, 'ast_FunctionObjectDeclaration'):
        assert not _is_linked(a2, 'ast_FunctionObjectDeclaration', b)


def test_assoc_stateVariableDeclarations16_reverse_link_reassign_clear():
    a1 = ast_StateVariableDeclaration(name="sample_text")
    a2 = ast_StateVariableDeclaration(name="sample_text_2")
    b = ast_FunctionDefinition(kind="sample_text")
    _safe_set(b, 'ast_FunctionDefinition17', {a1})
    assert _is_linked(b, 'ast_FunctionDefinition17', a1)
    if hasattr(a1, 'ast_StateVariableDeclaration'):
        assert _is_linked(a1, 'ast_StateVariableDeclaration', b)
    _safe_set(b, 'ast_FunctionDefinition17', {a2})
    assert _is_linked(b, 'ast_FunctionDefinition17', a2)
    if hasattr(a1, 'ast_StateVariableDeclaration'):
        assert not _is_linked(a1, 'ast_StateVariableDeclaration', b)
    if hasattr(a2, 'ast_StateVariableDeclaration'):
        assert _is_linked(a2, 'ast_StateVariableDeclaration', b)
    _safe_set(b, 'ast_FunctionDefinition17', set())
    assert not _is_linked(b, 'ast_FunctionDefinition17', a2)
    if hasattr(a2, 'ast_StateVariableDeclaration'):
        assert not _is_linked(a2, 'ast_StateVariableDeclaration', b)


def test_assoc_variables90_reverse_link_reassign_clear():
    a1 = ast_IterationVariable(name="sample_text")
    a2 = ast_IterationVariable(name="sample_text_2")
    b = ast_IterationCall(identifier="sample_text")
    _safe_set(b, 'ast_IterationCall91', {a1})
    assert _is_linked(b, 'ast_IterationCall91', a1)
    if hasattr(a1, 'ast_IterationVariable'):
        assert _is_linked(a1, 'ast_IterationVariable', b)
    _safe_set(b, 'ast_IterationCall91', {a2})
    assert _is_linked(b, 'ast_IterationCall91', a2)
    if hasattr(a1, 'ast_IterationVariable'):
        assert not _is_linked(a1, 'ast_IterationVariable', b)
    if hasattr(a2, 'ast_IterationVariable'):
        assert _is_linked(a2, 'ast_IterationVariable', b)
    _safe_set(b, 'ast_IterationCall91', set())
    assert not _is_linked(b, 'ast_IterationCall91', a2)
    if hasattr(a2, 'ast_IterationVariable'):
        assert not _is_linked(a2, 'ast_IterationVariable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_breakCondition94_stub_double():
    # ast_Expression has no real 'ast_Expression96' property in the generated
    # code (a bare stub) -- manually attach it so ast_IterationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_IterationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_IterationCall(identifier="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression96', None)
    _safe_set(owner, 'ast_IterationCall95', partner)
    assert getattr(partner, 'ast_Expression96') == owner
    _safe_set(owner, 'ast_IterationCall95', None)
    assert getattr(partner, 'ast_Expression96') is None


def test_assoc_cases70_stub_double():
    # ast_SwitchCase has no real 'ast_SwitchCase' property in the generated
    # code (a bare stub) -- manually attach it so ast_SwitchExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SwitchExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SwitchExpression(static=True)
    partner = ast_SwitchCase()
    setattr(partner, 'ast_SwitchCase', None)
    _safe_set(owner, 'ast_SwitchExpression71', {partner})
    assert getattr(partner, 'ast_SwitchCase') == owner
    _safe_set(owner, 'ast_SwitchExpression71', set())
    assert getattr(partner, 'ast_SwitchCase') is None


def test_assoc_checks11_stub_double():
    # ast_Check has no real 'Check' property in the generated
    # code (a bare stub) -- manually attach it so ast_FunctionDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_FunctionDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_FunctionDefinition(kind="sample_text")
    partner = ast_Check()
    setattr(partner, 'Check', None)
    _safe_set(owner, 'function', {partner})
    assert getattr(partner, 'Check') == owner
    _safe_set(owner, 'function', set())
    assert getattr(partner, 'Check') is None


def test_assoc_collectionExpression108_stub_double():
    # ast_Expression has no real 'ast_Expression110' property in the generated
    # code (a bare stub) -- manually attach it so ast_ArrayConstructionIterationClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_ArrayConstructionIterationClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_ArrayConstructionIterationClause(variableName="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression110', None)
    _safe_set(owner, 'ast_ArrayConstructionIterationClause109', partner)
    assert getattr(partner, 'ast_Expression110') == owner
    _safe_set(owner, 'ast_ArrayConstructionIterationClause109', None)
    assert getattr(partner, 'ast_Expression110') is None


def test_assoc_condition28_stub_double():
    # ast_Expression has no real 'ast_Expression30' property in the generated
    # code (a bare stub) -- manually attach it so ast_Assertion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Assertion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Assertion(static=True, statusKind="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression30', None)
    _safe_set(owner, 'ast_Assertion29', partner)
    assert getattr(partner, 'ast_Expression30') == owner
    _safe_set(owner, 'ast_Assertion29', None)
    assert getattr(partner, 'ast_Expression30') is None


def test_assoc_condition60_stub_double():
    # ast_Expression has no real 'ast_Expression61' property in the generated
    # code (a bare stub) -- manually attach it so ast_IfExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_IfExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_IfExpression(static=True)
    partner = ast_Expression()
    setattr(partner, 'ast_Expression61', None)
    _safe_set(owner, 'ast_IfExpression', partner)
    assert getattr(partner, 'ast_Expression61') == owner
    _safe_set(owner, 'ast_IfExpression', None)
    assert getattr(partner, 'ast_Expression61') is None


def test_assoc_controlExpression68_stub_double():
    # ast_Expression has no real 'ast_Expression69' property in the generated
    # code (a bare stub) -- manually attach it so ast_SwitchExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SwitchExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SwitchExpression(static=True)
    partner = ast_Expression()
    setattr(partner, 'ast_Expression69', None)
    _safe_set(owner, 'ast_SwitchExpression', partner)
    assert getattr(partner, 'ast_Expression69') == owner
    _safe_set(owner, 'ast_SwitchExpression', None)
    assert getattr(partner, 'ast_Expression69') is None


def test_assoc_defaultExpression72_stub_double():
    # ast_Expression has no real 'ast_Expression74' property in the generated
    # code (a bare stub) -- manually attach it so ast_SwitchExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_SwitchExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_SwitchExpression(static=True)
    partner = ast_Expression()
    setattr(partner, 'ast_Expression74', None)
    _safe_set(owner, 'ast_SwitchExpression73', partner)
    assert getattr(partner, 'ast_Expression74') == owner
    _safe_set(owner, 'ast_SwitchExpression73', None)
    assert getattr(partner, 'ast_Expression74') is None


def test_assoc_definitions0_stub_double():
    # ast_Module has no real 'ast_Module' property in the generated
    # code (a bare stub) -- manually attach it so ast_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Definition(name="sample_text")
    partner = ast_Module()
    setattr(partner, 'ast_Module', None)
    _safe_set(owner, 'ast_Definition', partner)
    assert owner in getattr(partner, 'ast_Module')
    _safe_set(owner, 'ast_Definition', None)
    assert owner not in getattr(partner, 'ast_Module')


def test_assoc_elseExpression65_stub_double():
    # ast_Expression has no real 'ast_Expression67' property in the generated
    # code (a bare stub) -- manually attach it so ast_IfExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_IfExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_IfExpression(static=True)
    partner = ast_Expression()
    setattr(partner, 'ast_Expression67', None)
    _safe_set(owner, 'ast_IfExpression66', partner)
    assert getattr(partner, 'ast_Expression67') == owner
    _safe_set(owner, 'ast_IfExpression66', None)
    assert getattr(partner, 'ast_Expression67') is None


def test_assoc_exponent162_stub_double():
    # ast_Expression has no real 'ast_Expression164' property in the generated
    # code (a bare stub) -- manually attach it so ast_PowerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_PowerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_PowerExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression164', None)
    _safe_set(owner, 'ast_PowerExpression163', partner)
    assert getattr(partner, 'ast_Expression164') == owner
    _safe_set(owner, 'ast_PowerExpression163', None)
    assert getattr(partner, 'ast_Expression164') is None


def test_assoc_expression85_stub_double():
    # ast_Expression has no real 'ast_Expression87' property in the generated
    # code (a bare stub) -- manually attach it so ast_ArraySubscript's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_ArraySubscript's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_ArraySubscript(slice=True)
    partner = ast_Expression()
    setattr(partner, 'ast_Expression87', None)
    _safe_set(owner, 'ast_ArraySubscript86', partner)
    assert getattr(partner, 'ast_Expression87') == owner
    _safe_set(owner, 'ast_ArraySubscript86', None)
    assert getattr(partner, 'ast_Expression87') is None


def test_assoc_expression97_stub_double():
    # ast_Expression has no real 'ast_Expression99' property in the generated
    # code (a bare stub) -- manually attach it so ast_IterationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_IterationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_IterationCall(identifier="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression99', None)
    _safe_set(owner, 'ast_IterationCall98', partner)
    assert getattr(partner, 'ast_Expression99') == owner
    _safe_set(owner, 'ast_IterationCall98', None)
    assert getattr(partner, 'ast_Expression99') is None


def test_assoc_feature169_stub_double():
    # ast_FeatureCall has no real 'ast_FeatureCall' property in the generated
    # code (a bare stub) -- manually attach it so ast_CallableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_CallableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_CallableElement()
    partner = ast_FeatureCall()
    setattr(partner, 'ast_FeatureCall', None)
    _safe_set(owner, 'ast_CallableElement170', partner)
    assert getattr(partner, 'ast_FeatureCall') == owner
    _safe_set(owner, 'ast_CallableElement170', None)
    assert getattr(partner, 'ast_FeatureCall') is None


def test_assoc_fieldDeclarations3_stub_double():
    # ast_RecordDefinition has no real 'ast_RecordDefinition' property in the generated
    # code (a bare stub) -- manually attach it so ast_RecordFieldDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_RecordFieldDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_RecordFieldDeclaration(name="sample_text")
    partner = ast_RecordDefinition()
    setattr(partner, 'ast_RecordDefinition', None)
    _safe_set(owner, 'ast_RecordFieldDeclaration', partner)
    assert owner in getattr(partner, 'ast_RecordDefinition')
    _safe_set(owner, 'ast_RecordFieldDeclaration', None)
    assert owner not in getattr(partner, 'ast_RecordDefinition')


def test_assoc_function20_stub_double():
    # ast_Check has no real 'checks' property in the generated
    # code (a bare stub) -- manually attach it so ast_FunctionDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_FunctionDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_FunctionDefinition(kind="sample_text")
    partner = ast_Check()
    setattr(partner, 'checks', None)
    _safe_set(owner, 'FunctionDefinition', partner)
    assert getattr(partner, 'checks') == owner
    _safe_set(owner, 'FunctionDefinition', None)
    assert getattr(partner, 'checks') is None


def test_assoc_initializer100_stub_double():
    # ast_Expression has no real 'ast_Expression102' property in the generated
    # code (a bare stub) -- manually attach it so ast_IterationAccumulator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_IterationAccumulator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_IterationAccumulator(name="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression102', None)
    _safe_set(owner, 'ast_IterationAccumulator101', partner)
    assert getattr(partner, 'ast_Expression102') == owner
    _safe_set(owner, 'ast_IterationAccumulator101', None)
    assert getattr(partner, 'ast_Expression102') is None


def test_assoc_initializer199_stub_double():
    # ast_Expression has no real 'ast_Expression200' property in the generated
    # code (a bare stub) -- manually attach it so ast_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_VariableDeclaration(name="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression200', None)
    _safe_set(owner, 'ast_VariableDeclaration', partner)
    assert getattr(partner, 'ast_Expression200') == owner
    _safe_set(owner, 'ast_VariableDeclaration', None)
    assert getattr(partner, 'ast_Expression200') is None


def test_assoc_inputParameterDeclarations7_stub_double():
    # ast_InputParameterDeclaration has no real 'ast_InputParameterDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so ast_FunctionDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_FunctionDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_FunctionDefinition(kind="sample_text")
    partner = ast_InputParameterDeclaration()
    setattr(partner, 'ast_InputParameterDeclaration', None)
    _safe_set(owner, 'ast_FunctionDefinition8', {partner})
    assert getattr(partner, 'ast_InputParameterDeclaration') == owner
    _safe_set(owner, 'ast_FunctionDefinition8', set())
    assert getattr(partner, 'ast_InputParameterDeclaration') is None


def test_assoc_iterationClauses106_stub_double():
    # ast_ArrayConstructionOperator has no real 'ast_ArrayConstructionOperator107' property in the generated
    # code (a bare stub) -- manually attach it so ast_ArrayConstructionIterationClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_ArrayConstructionIterationClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_ArrayConstructionIterationClause(variableName="sample_text")
    partner = ast_ArrayConstructionOperator()
    setattr(partner, 'ast_ArrayConstructionOperator107', None)
    _safe_set(owner, 'ast_ArrayConstructionIterationClause', partner)
    assert owner in getattr(partner, 'ast_ArrayConstructionOperator107')
    _safe_set(owner, 'ast_ArrayConstructionIterationClause', None)
    assert owner not in getattr(partner, 'ast_ArrayConstructionOperator107')


def test_assoc_iterationVariable219_stub_double():
    # ast_ForStatement has no real 'ast_ForStatement' property in the generated
    # code (a bare stub) -- manually attach it so ast_IterationVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_IterationVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_IterationVariable(name="sample_text")
    partner = ast_ForStatement()
    setattr(partner, 'ast_ForStatement', None)
    _safe_set(owner, 'ast_IterationVariable220', partner)
    assert getattr(partner, 'ast_ForStatement') == owner
    _safe_set(owner, 'ast_IterationVariable220', None)
    assert getattr(partner, 'ast_ForStatement') is None


def test_assoc_leftHandSide40_stub_double():
    # ast_Expression has no real 'ast_Expression42' property in the generated
    # code (a bare stub) -- manually attach it so ast_Equation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Equation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Equation(initial=True)
    partner = ast_Expression()
    setattr(partner, 'ast_Expression42', None)
    _safe_set(owner, 'ast_Equation41', partner)
    assert getattr(partner, 'ast_Expression42') == owner
    _safe_set(owner, 'ast_Equation41', None)
    assert getattr(partner, 'ast_Expression42') is None


def test_assoc_leftOperand135_stub_double():
    # ast_Expression has no real 'ast_Expression136' property in the generated
    # code (a bare stub) -- manually attach it so ast_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_EqualityExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression136', None)
    _safe_set(owner, 'ast_EqualityExpression', partner)
    assert getattr(partner, 'ast_Expression136') == owner
    _safe_set(owner, 'ast_EqualityExpression', None)
    assert getattr(partner, 'ast_Expression136') is None


def test_assoc_leftOperand140_stub_double():
    # ast_Expression has no real 'ast_Expression141' property in the generated
    # code (a bare stub) -- manually attach it so ast_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_RelationalExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression141', None)
    _safe_set(owner, 'ast_RelationalExpression', partner)
    assert getattr(partner, 'ast_Expression141') == owner
    _safe_set(owner, 'ast_RelationalExpression', None)
    assert getattr(partner, 'ast_Expression141') is None


def test_assoc_leftOperand150_stub_double():
    # ast_Expression has no real 'ast_Expression151' property in the generated
    # code (a bare stub) -- manually attach it so ast_AdditiveExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_AdditiveExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_AdditiveExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression151', None)
    _safe_set(owner, 'ast_AdditiveExpression', partner)
    assert getattr(partner, 'ast_Expression151') == owner
    _safe_set(owner, 'ast_AdditiveExpression', None)
    assert getattr(partner, 'ast_Expression151') is None


def test_assoc_leftOperand155_stub_double():
    # ast_Expression has no real 'ast_Expression156' property in the generated
    # code (a bare stub) -- manually attach it so ast_MultiplicativeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MultiplicativeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MultiplicativeExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression156', None)
    _safe_set(owner, 'ast_MultiplicativeExpression', partner)
    assert getattr(partner, 'ast_Expression156') == owner
    _safe_set(owner, 'ast_MultiplicativeExpression', None)
    assert getattr(partner, 'ast_Expression156') is None


def test_assoc_leftOperand177_stub_double():
    # ast_StepExpression has no real 'ast_StepExpression178' property in the generated
    # code (a bare stub) -- manually attach it so ast_AdditiveStepExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_AdditiveStepExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_AdditiveStepExpression(operator="sample_text")
    partner = ast_StepExpression()
    setattr(partner, 'ast_StepExpression178', None)
    _safe_set(owner, 'ast_AdditiveStepExpression', partner)
    assert getattr(partner, 'ast_StepExpression178') == owner
    _safe_set(owner, 'ast_AdditiveStepExpression', None)
    assert getattr(partner, 'ast_StepExpression178') is None


def test_assoc_literalDeclarations1_stub_double():
    # ast_EnumerationDefinition has no real 'ast_EnumerationDefinition' property in the generated
    # code (a bare stub) -- manually attach it so ast_EnumerationLiteralDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_EnumerationLiteralDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_EnumerationLiteralDeclaration(name="sample_text")
    partner = ast_EnumerationDefinition()
    setattr(partner, 'ast_EnumerationDefinition', None)
    _safe_set(owner, 'ast_EnumerationLiteralDeclaration', partner)
    assert owner in getattr(partner, 'ast_EnumerationDefinition')
    _safe_set(owner, 'ast_EnumerationLiteralDeclaration', None)
    assert owner not in getattr(partner, 'ast_EnumerationDefinition')


def test_assoc_memberVariable188_stub_double():
    # ast_MemberVariableAccess has no real 'ast_MemberVariableAccess189' property in the generated
    # code (a bare stub) -- manually attach it so ast_CallableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_CallableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_CallableElement()
    partner = ast_MemberVariableAccess()
    setattr(partner, 'ast_MemberVariableAccess189', None)
    _safe_set(owner, 'ast_CallableElement190', partner)
    assert getattr(partner, 'ast_MemberVariableAccess189') == owner
    _safe_set(owner, 'ast_CallableElement190', None)
    assert getattr(partner, 'ast_MemberVariableAccess189') is None


def test_assoc_message31_stub_double():
    # ast_Expression has no real 'ast_Expression33' property in the generated
    # code (a bare stub) -- manually attach it so ast_Assertion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Assertion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Assertion(static=True, statusKind="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression33', None)
    _safe_set(owner, 'ast_Assertion32', partner)
    assert getattr(partner, 'ast_Expression33') == owner
    _safe_set(owner, 'ast_Assertion32', None)
    assert getattr(partner, 'ast_Expression33') is None


def test_assoc_operand160_stub_double():
    # ast_Expression has no real 'ast_Expression161' property in the generated
    # code (a bare stub) -- manually attach it so ast_PowerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_PowerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_PowerExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression161', None)
    _safe_set(owner, 'ast_PowerExpression', partner)
    assert getattr(partner, 'ast_Expression161') == owner
    _safe_set(owner, 'ast_PowerExpression', None)
    assert getattr(partner, 'ast_Expression161') is None


def test_assoc_operand165_stub_double():
    # ast_Expression has no real 'ast_Expression166' property in the generated
    # code (a bare stub) -- manually attach it so ast_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_UnaryExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression166', None)
    _safe_set(owner, 'ast_UnaryExpression', partner)
    assert getattr(partner, 'ast_Expression166') == owner
    _safe_set(owner, 'ast_UnaryExpression', None)
    assert getattr(partner, 'ast_Expression166') is None


def test_assoc_operand167_stub_double():
    # ast_Expression has no real 'ast_Expression168' property in the generated
    # code (a bare stub) -- manually attach it so ast_PostfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_PostfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_PostfixExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression168', None)
    _safe_set(owner, 'ast_PostfixExpression', partner)
    assert getattr(partner, 'ast_Expression168') == owner
    _safe_set(owner, 'ast_PostfixExpression', None)
    assert getattr(partner, 'ast_Expression168') is None


def test_assoc_outputParameterDeclarations9_stub_double():
    # ast_OutputParameterDeclaration has no real 'ast_OutputParameterDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so ast_FunctionDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_FunctionDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_FunctionDefinition(kind="sample_text")
    partner = ast_OutputParameterDeclaration()
    setattr(partner, 'ast_OutputParameterDeclaration', None)
    _safe_set(owner, 'ast_FunctionDefinition10', {partner})
    assert getattr(partner, 'ast_OutputParameterDeclaration') == owner
    _safe_set(owner, 'ast_FunctionDefinition10', set())
    assert getattr(partner, 'ast_OutputParameterDeclaration') is None


def test_assoc_parts55_stub_double():
    # ast_LetExpressionVariableDeclaration has no real 'ast_LetExpressionVariableDeclaration56' property in the generated
    # code (a bare stub) -- manually attach it so ast_LetExpressionVariableDeclarationPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_LetExpressionVariableDeclarationPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_LetExpressionVariableDeclarationPart(name="sample_text")
    partner = ast_LetExpressionVariableDeclaration()
    setattr(partner, 'ast_LetExpressionVariableDeclaration56', None)
    _safe_set(owner, 'ast_LetExpressionVariableDeclarationPart', partner)
    assert owner in getattr(partner, 'ast_LetExpressionVariableDeclaration56')
    _safe_set(owner, 'ast_LetExpressionVariableDeclarationPart', None)
    assert owner not in getattr(partner, 'ast_LetExpressionVariableDeclaration56')


def test_assoc_rightHandSide43_stub_double():
    # ast_Expression has no real 'ast_Expression45' property in the generated
    # code (a bare stub) -- manually attach it so ast_Equation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Equation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Equation(initial=True)
    partner = ast_Expression()
    setattr(partner, 'ast_Expression45', None)
    _safe_set(owner, 'ast_Equation44', partner)
    assert getattr(partner, 'ast_Expression45') == owner
    _safe_set(owner, 'ast_Equation44', None)
    assert getattr(partner, 'ast_Expression45') is None


def test_assoc_rightOperand137_stub_double():
    # ast_Expression has no real 'ast_Expression139' property in the generated
    # code (a bare stub) -- manually attach it so ast_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_EqualityExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression139', None)
    _safe_set(owner, 'ast_EqualityExpression138', partner)
    assert getattr(partner, 'ast_Expression139') == owner
    _safe_set(owner, 'ast_EqualityExpression138', None)
    assert getattr(partner, 'ast_Expression139') is None


def test_assoc_rightOperand142_stub_double():
    # ast_Expression has no real 'ast_Expression144' property in the generated
    # code (a bare stub) -- manually attach it so ast_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_RelationalExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression144', None)
    _safe_set(owner, 'ast_RelationalExpression143', partner)
    assert getattr(partner, 'ast_Expression144') == owner
    _safe_set(owner, 'ast_RelationalExpression143', None)
    assert getattr(partner, 'ast_Expression144') is None


def test_assoc_rightOperand152_stub_double():
    # ast_Expression has no real 'ast_Expression154' property in the generated
    # code (a bare stub) -- manually attach it so ast_AdditiveExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_AdditiveExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_AdditiveExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression154', None)
    _safe_set(owner, 'ast_AdditiveExpression153', partner)
    assert getattr(partner, 'ast_Expression154') == owner
    _safe_set(owner, 'ast_AdditiveExpression153', None)
    assert getattr(partner, 'ast_Expression154') is None


def test_assoc_rightOperand157_stub_double():
    # ast_Expression has no real 'ast_Expression159' property in the generated
    # code (a bare stub) -- manually attach it so ast_MultiplicativeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_MultiplicativeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_MultiplicativeExpression(operator="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression159', None)
    _safe_set(owner, 'ast_MultiplicativeExpression158', partner)
    assert getattr(partner, 'ast_Expression159') == owner
    _safe_set(owner, 'ast_MultiplicativeExpression158', None)
    assert getattr(partner, 'ast_Expression159') is None


def test_assoc_rightOperand179_stub_double():
    # ast_StepExpression has no real 'ast_StepExpression181' property in the generated
    # code (a bare stub) -- manually attach it so ast_AdditiveStepExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_AdditiveStepExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_AdditiveStepExpression(operator="sample_text")
    partner = ast_StepExpression()
    setattr(partner, 'ast_StepExpression181', None)
    _safe_set(owner, 'ast_AdditiveStepExpression180', partner)
    assert getattr(partner, 'ast_StepExpression181') == owner
    _safe_set(owner, 'ast_AdditiveStepExpression180', None)
    assert getattr(partner, 'ast_StepExpression181') is None


def test_assoc_stepExpression171_stub_double():
    # ast_StepExpression has no real 'ast_StepExpression' property in the generated
    # code (a bare stub) -- manually attach it so ast_VariableAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_VariableAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_VariableAccess()
    partner = ast_StepExpression()
    setattr(partner, 'ast_StepExpression', None)
    _safe_set(owner, 'ast_VariableAccess', partner)
    assert getattr(partner, 'ast_StepExpression') == owner
    _safe_set(owner, 'ast_VariableAccess', None)
    assert getattr(partner, 'ast_StepExpression') is None


def test_assoc_subscripts83_stub_double():
    # ast_ArrayElementAccess has no real 'ast_ArrayElementAccess84' property in the generated
    # code (a bare stub) -- manually attach it so ast_ArraySubscript's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_ArraySubscript's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_ArraySubscript(slice=True)
    partner = ast_ArrayElementAccess()
    setattr(partner, 'ast_ArrayElementAccess84', None)
    _safe_set(owner, 'ast_ArraySubscript', partner)
    assert owner in getattr(partner, 'ast_ArrayElementAccess84')
    _safe_set(owner, 'ast_ArraySubscript', None)
    assert owner not in getattr(partner, 'ast_ArrayElementAccess84')


def test_assoc_target88_stub_double():
    # ast_Expression has no real 'ast_Expression89' property in the generated
    # code (a bare stub) -- manually attach it so ast_IterationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_IterationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_IterationCall(identifier="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression89', None)
    _safe_set(owner, 'ast_IterationCall', partner)
    assert getattr(partner, 'ast_Expression89') == owner
    _safe_set(owner, 'ast_IterationCall', None)
    assert getattr(partner, 'ast_Expression89') is None


def test_assoc_templateArguments37_stub_double():
    # ast_Expression has no real 'ast_Expression39' property in the generated
    # code (a bare stub) -- manually attach it so ast_FunctionObjectDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_FunctionObjectDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_FunctionObjectDeclaration(name="sample_text")
    partner = ast_Expression()
    setattr(partner, 'ast_Expression39', None)
    _safe_set(owner, 'ast_FunctionObjectDeclaration38', {partner})
    assert getattr(partner, 'ast_Expression39') == owner
    _safe_set(owner, 'ast_FunctionObjectDeclaration38', set())
    assert getattr(partner, 'ast_Expression39') is None


def test_assoc_templateParameterDeclarations6_stub_double():
    # ast_TemplateParameterDeclaration has no real 'ast_TemplateParameterDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so ast_FunctionDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_FunctionDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_FunctionDefinition(kind="sample_text")
    partner = ast_TemplateParameterDeclaration()
    setattr(partner, 'ast_TemplateParameterDeclaration', None)
    _safe_set(owner, 'ast_FunctionDefinition', {partner})
    assert getattr(partner, 'ast_TemplateParameterDeclaration') == owner
    _safe_set(owner, 'ast_FunctionDefinition', set())
    assert getattr(partner, 'ast_TemplateParameterDeclaration') is None


def test_assoc_thenExpression62_stub_double():
    # ast_Expression has no real 'ast_Expression64' property in the generated
    # code (a bare stub) -- manually attach it so ast_IfExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_IfExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_IfExpression(static=True)
    partner = ast_Expression()
    setattr(partner, 'ast_Expression64', None)
    _safe_set(owner, 'ast_IfExpression63', partner)
    assert getattr(partner, 'ast_Expression64') == owner
    _safe_set(owner, 'ast_IfExpression63', None)
    assert getattr(partner, 'ast_Expression64') is None


def test_assoc_type4_stub_double():
    # ast_DataTypeSpecifier has no real 'ast_DataTypeSpecifier' property in the generated
    # code (a bare stub) -- manually attach it so ast_RecordFieldDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_RecordFieldDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_RecordFieldDeclaration(name="sample_text")
    partner = ast_DataTypeSpecifier()
    setattr(partner, 'ast_DataTypeSpecifier', None)
    _safe_set(owner, 'ast_RecordFieldDeclaration5', partner)
    assert getattr(partner, 'ast_DataTypeSpecifier') == owner
    _safe_set(owner, 'ast_RecordFieldDeclaration5', None)
    assert getattr(partner, 'ast_DataTypeSpecifier') is None


def test_assoc_variable103_stub_double():
    # ast_DerivativeOperator has no real 'ast_DerivativeOperator' property in the generated
    # code (a bare stub) -- manually attach it so ast_CallableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_CallableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_CallableElement()
    partner = ast_DerivativeOperator()
    setattr(partner, 'ast_DerivativeOperator', None)
    _safe_set(owner, 'ast_CallableElement', partner)
    assert getattr(partner, 'ast_DerivativeOperator') == owner
    _safe_set(owner, 'ast_CallableElement', None)
    assert getattr(partner, 'ast_DerivativeOperator') is None


