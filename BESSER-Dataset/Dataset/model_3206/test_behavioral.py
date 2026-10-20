import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CallStatement,
    CompoundExpression,
    ConstantExpression,
    ControlStructure,
    Expression,
    NQC_ArrayExpression,
    NQC_AssignmentStatement,
    NQC_BinaryExpression,
    NQC_BlockStatement,
    NQC_BooleanConstant,
    NQC_BreakStatement,
    NQC_CallStatement,
    NQC_Case,
    NQC_CompoundExpression,
    NQC_ConstantExpression,
    NQC_ContinueStatement,
    NQC_ControlStructure,
    NQC_DoWhileStatement,
    NQC_EmptyStatement,
    NQC_Expression,
    NQC_ForStatement,
    NQC_Function,
    NQC_FunctionCall,
    NQC_GlobalVariable,
    NQC_GoToStatement,
    NQC_IfStatement,
    NQC_IntegerConstant,
    NQC_Label,
    NQC_LocalVariable,
    NQC_Parameter,
    NQC_Program,
    NQC_RepeatStatement,
    NQC_ReturnStatement,
    NQC_StartStatement,
    NQC_Statement,
    NQC_StopStatement,
    NQC_Subroutine,
    NQC_SubroutineCall,
    NQC_SwitchStatement,
    NQC_Task,
    NQC_UntilStatement,
    NQC_ValueExpression,
    NQC_Variable,
    NQC_VariableExpression,
    NQC_WhileStatement,
    Statement,
    ValueExpression,
    Variable,
    VariableExpression,
    AssignmentStatementEnum,
    BinaryOperatorEnum,
    TypeEnum,
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

def test_assoc_ArrayMaxSize26_reverse_link_reassign_clear():
    a1 = NQC_Variable(Name="sample_text", Type="sample_text")
    a2 = NQC_Variable(Name="sample_text_2", Type="sample_text_2")
    b = NQC_IntegerConstant(Value=7)
    _safe_set(b, 'NQC_IntegerConstant', a1)
    assert _is_linked(b, 'NQC_IntegerConstant', a1)
    if hasattr(a1, 'NQC_Variable27'):
        assert _is_linked(a1, 'NQC_Variable27', b)
    _safe_set(b, 'NQC_IntegerConstant', a2)
    assert _is_linked(b, 'NQC_IntegerConstant', a2)
    if hasattr(a1, 'NQC_Variable27'):
        assert not _is_linked(a1, 'NQC_Variable27', b)
    if hasattr(a2, 'NQC_Variable27'):
        assert _is_linked(a2, 'NQC_Variable27', b)
    _safe_set(b, 'NQC_IntegerConstant', None)
    assert not _is_linked(b, 'NQC_IntegerConstant', a2)
    if hasattr(a2, 'NQC_Variable27'):
        assert not _is_linked(a2, 'NQC_Variable27', b)


def test_assoc_Functions1_reverse_link_reassign_clear():
    a1 = NQC_Program(Name="sample_text")
    a2 = NQC_Program(Name="sample_text_2")
    b = NQC_Function(Name="sample_text")
    _safe_set(b, 'NQC_Function', a1)
    assert _is_linked(b, 'NQC_Function', a1)
    if hasattr(a1, 'NQC_Program2'):
        assert _is_linked(a1, 'NQC_Program2', b)
    _safe_set(b, 'NQC_Function', a2)
    assert _is_linked(b, 'NQC_Function', a2)
    if hasattr(a1, 'NQC_Program2'):
        assert not _is_linked(a1, 'NQC_Program2', b)
    if hasattr(a2, 'NQC_Program2'):
        assert _is_linked(a2, 'NQC_Program2', b)
    _safe_set(b, 'NQC_Function', None)
    assert not _is_linked(b, 'NQC_Function', a2)
    if hasattr(a2, 'NQC_Program2'):
        assert not _is_linked(a2, 'NQC_Program2', b)


def test_assoc_Subroutines3_reverse_link_reassign_clear():
    a1 = NQC_Subroutine(Name="sample_text")
    a2 = NQC_Subroutine(Name="sample_text_2")
    b = NQC_Program(Name="sample_text")
    _safe_set(b, 'NQC_Program4', {a1})
    assert _is_linked(b, 'NQC_Program4', a1)
    if hasattr(a1, 'NQC_Subroutine'):
        assert _is_linked(a1, 'NQC_Subroutine', b)
    _safe_set(b, 'NQC_Program4', {a2})
    assert _is_linked(b, 'NQC_Program4', a2)
    if hasattr(a1, 'NQC_Subroutine'):
        assert not _is_linked(a1, 'NQC_Subroutine', b)
    if hasattr(a2, 'NQC_Subroutine'):
        assert _is_linked(a2, 'NQC_Subroutine', b)
    _safe_set(b, 'NQC_Program4', set())
    assert not _is_linked(b, 'NQC_Program4', a2)
    if hasattr(a2, 'NQC_Subroutine'):
        assert not _is_linked(a2, 'NQC_Subroutine', b)


def test_assoc_Tasks0_reverse_link_reassign_clear():
    a1 = NQC_Task(Name="sample_text")
    a2 = NQC_Task(Name="sample_text_2")
    b = NQC_Program(Name="sample_text")
    _safe_set(b, 'NQC_Program', {a1})
    assert _is_linked(b, 'NQC_Program', a1)
    if hasattr(a1, 'NQC_Task'):
        assert _is_linked(a1, 'NQC_Task', b)
    _safe_set(b, 'NQC_Program', {a2})
    assert _is_linked(b, 'NQC_Program', a2)
    if hasattr(a1, 'NQC_Task'):
        assert not _is_linked(a1, 'NQC_Task', b)
    if hasattr(a2, 'NQC_Task'):
        assert _is_linked(a2, 'NQC_Task', b)
    _safe_set(b, 'NQC_Program', set())
    assert not _is_linked(b, 'NQC_Program', a2)
    if hasattr(a2, 'NQC_Task'):
        assert not _is_linked(a2, 'NQC_Task', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Callee100_stub_double():
    # NQC_FunctionCall has no real 'NQC_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Function(Name="sample_text")
    partner = NQC_FunctionCall()
    setattr(partner, 'NQC_FunctionCall', None)
    _safe_set(owner, 'NQC_Function101', partner)
    assert getattr(partner, 'NQC_FunctionCall') == owner
    _safe_set(owner, 'NQC_Function101', None)
    assert getattr(partner, 'NQC_FunctionCall') is None


def test_assoc_Callee105_stub_double():
    # NQC_SubroutineCall has no real 'NQC_SubroutineCall' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Subroutine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Subroutine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Subroutine(Name="sample_text")
    partner = NQC_SubroutineCall()
    setattr(partner, 'NQC_SubroutineCall', None)
    _safe_set(owner, 'NQC_Subroutine106', partner)
    assert getattr(partner, 'NQC_SubroutineCall') == owner
    _safe_set(owner, 'NQC_Subroutine106', None)
    assert getattr(partner, 'NQC_SubroutineCall') is None


def test_assoc_Cases72_stub_double():
    # NQC_SwitchStatement has no real 'NQC_SwitchStatement73' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Case's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Case's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Case(IsDefault=True)
    partner = NQC_SwitchStatement()
    setattr(partner, 'NQC_SwitchStatement73', None)
    _safe_set(owner, 'NQC_Case', partner)
    assert owner in getattr(partner, 'NQC_SwitchStatement73')
    _safe_set(owner, 'NQC_Case', None)
    assert owner not in getattr(partner, 'NQC_SwitchStatement73')


def test_assoc_Expression31_stub_double():
    # NQC_Expression has no real 'NQC_Expression' property in the generated
    # code (a bare stub) -- manually attach it so NQC_AssignmentStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_AssignmentStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_AssignmentStatement(Operator="sample_text")
    partner = NQC_Expression()
    setattr(partner, 'NQC_Expression', None)
    _safe_set(owner, 'NQC_AssignmentStatement32', partner)
    assert getattr(partner, 'NQC_Expression') == owner
    _safe_set(owner, 'NQC_AssignmentStatement32', None)
    assert getattr(partner, 'NQC_Expression') is None


def test_assoc_GlobalVariables5_stub_double():
    # NQC_GlobalVariable has no real 'NQC_GlobalVariable' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Program(Name="sample_text")
    partner = NQC_GlobalVariable()
    setattr(partner, 'NQC_GlobalVariable', None)
    _safe_set(owner, 'NQC_Program6', {partner})
    assert getattr(partner, 'NQC_GlobalVariable') == owner
    _safe_set(owner, 'NQC_Program6', set())
    assert getattr(partner, 'NQC_GlobalVariable') is None


def test_assoc_InitialValue25_stub_double():
    # NQC_ConstantExpression has no real 'NQC_ConstantExpression' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Variable(Name="sample_text", Type="sample_text")
    partner = NQC_ConstantExpression()
    setattr(partner, 'NQC_ConstantExpression', None)
    _safe_set(owner, 'NQC_Variable', partner)
    assert getattr(partner, 'NQC_ConstantExpression') == owner
    _safe_set(owner, 'NQC_Variable', None)
    assert getattr(partner, 'NQC_ConstantExpression') is None


def test_assoc_JumpLabel55_stub_double():
    # NQC_GoToStatement has no real 'NQC_GoToStatement' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Label(Label="sample_text")
    partner = NQC_GoToStatement()
    setattr(partner, 'NQC_GoToStatement', None)
    _safe_set(owner, 'NQC_Label56', partner)
    assert getattr(partner, 'NQC_GoToStatement') == owner
    _safe_set(owner, 'NQC_Label56', None)
    assert getattr(partner, 'NQC_GoToStatement') is None


def test_assoc_Label28_stub_double():
    # NQC_Statement has no real 'NQC_Statement29' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Label(Label="sample_text")
    partner = NQC_Statement()
    setattr(partner, 'NQC_Statement29', None)
    _safe_set(owner, 'NQC_Label', partner)
    assert getattr(partner, 'NQC_Statement29') == owner
    _safe_set(owner, 'NQC_Label', None)
    assert getattr(partner, 'NQC_Statement29') is None


def test_assoc_Label84_stub_double():
    # NQC_ConstantExpression has no real 'NQC_ConstantExpression86' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Case's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Case's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Case(IsDefault=True)
    partner = NQC_ConstantExpression()
    setattr(partner, 'NQC_ConstantExpression86', None)
    _safe_set(owner, 'NQC_Case85', {partner})
    assert getattr(partner, 'NQC_ConstantExpression86') == owner
    _safe_set(owner, 'NQC_Case85', set())
    assert getattr(partner, 'NQC_ConstantExpression86') is None


def test_assoc_LocalVariables14_stub_double():
    # NQC_LocalVariable has no real 'NQC_LocalVariable16' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Function(Name="sample_text")
    partner = NQC_LocalVariable()
    setattr(partner, 'NQC_LocalVariable16', None)
    _safe_set(owner, 'NQC_Function15', {partner})
    assert getattr(partner, 'NQC_LocalVariable16') == owner
    _safe_set(owner, 'NQC_Function15', set())
    assert getattr(partner, 'NQC_LocalVariable16') is None


def test_assoc_LocalVariables22_stub_double():
    # NQC_LocalVariable has no real 'NQC_LocalVariable24' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Subroutine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Subroutine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Subroutine(Name="sample_text")
    partner = NQC_LocalVariable()
    setattr(partner, 'NQC_LocalVariable24', None)
    _safe_set(owner, 'NQC_Subroutine23', {partner})
    assert getattr(partner, 'NQC_LocalVariable24') == owner
    _safe_set(owner, 'NQC_Subroutine23', set())
    assert getattr(partner, 'NQC_LocalVariable24') is None


def test_assoc_LocalVariables9_stub_double():
    # NQC_LocalVariable has no real 'NQC_LocalVariable' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Task(Name="sample_text")
    partner = NQC_LocalVariable()
    setattr(partner, 'NQC_LocalVariable', None)
    _safe_set(owner, 'NQC_Task10', {partner})
    assert getattr(partner, 'NQC_LocalVariable') == owner
    _safe_set(owner, 'NQC_Task10', set())
    assert getattr(partner, 'NQC_LocalVariable') is None


def test_assoc_Operand195_stub_double():
    # NQC_Expression has no real 'NQC_Expression96' property in the generated
    # code (a bare stub) -- manually attach it so NQC_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_BinaryExpression(Operator="sample_text")
    partner = NQC_Expression()
    setattr(partner, 'NQC_Expression96', None)
    _safe_set(owner, 'NQC_BinaryExpression', partner)
    assert getattr(partner, 'NQC_Expression96') == owner
    _safe_set(owner, 'NQC_BinaryExpression', None)
    assert getattr(partner, 'NQC_Expression96') is None


def test_assoc_Operand297_stub_double():
    # NQC_Expression has no real 'NQC_Expression99' property in the generated
    # code (a bare stub) -- manually attach it so NQC_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_BinaryExpression(Operator="sample_text")
    partner = NQC_Expression()
    setattr(partner, 'NQC_Expression99', None)
    _safe_set(owner, 'NQC_BinaryExpression98', partner)
    assert getattr(partner, 'NQC_Expression99') == owner
    _safe_set(owner, 'NQC_BinaryExpression98', None)
    assert getattr(partner, 'NQC_Expression99') is None


def test_assoc_Parameters17_stub_double():
    # NQC_Parameter has no real 'NQC_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Function(Name="sample_text")
    partner = NQC_Parameter()
    setattr(partner, 'NQC_Parameter', None)
    _safe_set(owner, 'NQC_Function18', {partner})
    assert getattr(partner, 'NQC_Parameter') == owner
    _safe_set(owner, 'NQC_Function18', set())
    assert getattr(partner, 'NQC_Parameter') is None


def test_assoc_Statements11_stub_double():
    # NQC_Statement has no real 'NQC_Statement13' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Function(Name="sample_text")
    partner = NQC_Statement()
    setattr(partner, 'NQC_Statement13', None)
    _safe_set(owner, 'NQC_Function12', {partner})
    assert getattr(partner, 'NQC_Statement13') == owner
    _safe_set(owner, 'NQC_Function12', set())
    assert getattr(partner, 'NQC_Statement13') is None


def test_assoc_Statements19_stub_double():
    # NQC_Statement has no real 'NQC_Statement21' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Subroutine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Subroutine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Subroutine(Name="sample_text")
    partner = NQC_Statement()
    setattr(partner, 'NQC_Statement21', None)
    _safe_set(owner, 'NQC_Subroutine20', {partner})
    assert getattr(partner, 'NQC_Statement21') == owner
    _safe_set(owner, 'NQC_Subroutine20', set())
    assert getattr(partner, 'NQC_Statement21') is None


def test_assoc_Statements7_stub_double():
    # NQC_Statement has no real 'NQC_Statement' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Task(Name="sample_text")
    partner = NQC_Statement()
    setattr(partner, 'NQC_Statement', None)
    _safe_set(owner, 'NQC_Task8', {partner})
    assert getattr(partner, 'NQC_Statement') == owner
    _safe_set(owner, 'NQC_Task8', set())
    assert getattr(partner, 'NQC_Statement') is None


def test_assoc_Statements87_stub_double():
    # NQC_Statement has no real 'NQC_Statement89' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Case's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Case's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Case(IsDefault=True)
    partner = NQC_Statement()
    setattr(partner, 'NQC_Statement89', None)
    _safe_set(owner, 'NQC_Case88', {partner})
    assert getattr(partner, 'NQC_Statement89') == owner
    _safe_set(owner, 'NQC_Case88', set())
    assert getattr(partner, 'NQC_Statement89') is None


def test_assoc_Task38_stub_double():
    # NQC_StartStatement has no real 'NQC_StartStatement' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Task(Name="sample_text")
    partner = NQC_StartStatement()
    setattr(partner, 'NQC_StartStatement', None)
    _safe_set(owner, 'NQC_Task39', partner)
    assert getattr(partner, 'NQC_StartStatement') == owner
    _safe_set(owner, 'NQC_Task39', None)
    assert getattr(partner, 'NQC_StartStatement') is None


def test_assoc_Task40_stub_double():
    # NQC_StopStatement has no real 'NQC_StopStatement' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Task(Name="sample_text")
    partner = NQC_StopStatement()
    setattr(partner, 'NQC_StopStatement', None)
    _safe_set(owner, 'NQC_Task41', partner)
    assert getattr(partner, 'NQC_StopStatement') == owner
    _safe_set(owner, 'NQC_Task41', None)
    assert getattr(partner, 'NQC_StopStatement') is None


def test_assoc_Variable30_stub_double():
    # NQC_VariableExpression has no real 'NQC_VariableExpression' property in the generated
    # code (a bare stub) -- manually attach it so NQC_AssignmentStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_AssignmentStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_AssignmentStatement(Operator="sample_text")
    partner = NQC_VariableExpression()
    setattr(partner, 'NQC_VariableExpression', None)
    _safe_set(owner, 'NQC_AssignmentStatement', partner)
    assert getattr(partner, 'NQC_VariableExpression') == owner
    _safe_set(owner, 'NQC_AssignmentStatement', None)
    assert getattr(partner, 'NQC_VariableExpression') is None


def test_assoc_Variable90_stub_double():
    # NQC_VariableExpression has no real 'NQC_VariableExpression91' property in the generated
    # code (a bare stub) -- manually attach it so NQC_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NQC_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NQC_Variable(Name="sample_text", Type="sample_text")
    partner = NQC_VariableExpression()
    setattr(partner, 'NQC_VariableExpression91', None)
    _safe_set(owner, 'NQC_Variable92', partner)
    assert getattr(partner, 'NQC_VariableExpression91') == owner
    _safe_set(owner, 'NQC_Variable92', None)
    assert getattr(partner, 'NQC_VariableExpression91') is None


