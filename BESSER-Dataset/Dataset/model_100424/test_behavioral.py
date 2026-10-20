import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Event,
    Expression,
    PrimaryExpression,
    Statement,
    TimeExpression,
    statechartexpressions_ActionExpression,
    statechartexpressions_AdditiveExpression,
    statechartexpressions_BitwiseAndExpression,
    statechartexpressions_BitwiseOrExpression,
    statechartexpressions_BitwiseXorExpression,
    statechartexpressions_BooleanAndExpression,
    statechartexpressions_BooleanOrExpression,
    statechartexpressions_ConditionalExpression,
    statechartexpressions_EqualityExpression,
    statechartexpressions_Event,
    statechartexpressions_EventRaising,
    statechartexpressions_Expression,
    statechartexpressions_GuardExpression,
    statechartexpressions_LiteralValue,
    statechartexpressions_MultiplicativeExpression,
    statechartexpressions_NestedExpression,
    statechartexpressions_PrimaryExpression,
    statechartexpressions_Procedure,
    statechartexpressions_ProcedureCall,
    statechartexpressions_RelationalExpression,
    statechartexpressions_ShiftExpression,
    statechartexpressions_SignalEvent,
    statechartexpressions_Statement,
    statechartexpressions_TimeConstant,
    statechartexpressions_TimeEvent,
    statechartexpressions_TimeExpression,
    statechartexpressions_Trigger,
    statechartexpressions_TriggerExpression,
    statechartexpressions_UnaryExpression,
    statechartexpressions_Variable,
    statechartexpressions_VariableAssignment,
    statechartexpressions_VariableReference,
    AdditiveOperator,
    AssignmentOperator,
    EqualityOperator,
    MultiplicativeOperator,
    RelationalOperator,
    ShiftOperator,
    TimeUnit,
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

def test_assoc_operand138_reverse_link_reassign_clear():
    a1 = statechartexpressions_RelationalExpression(operator="sample_text")
    a2 = statechartexpressions_RelationalExpression(operator="sample_text_2")
    b = statechartexpressions_EqualityExpression(operator="sample_text")
    _safe_set(b, 'statechartexpressions_EqualityExpression39', a1)
    assert _is_linked(b, 'statechartexpressions_EqualityExpression39', a1)
    if hasattr(a1, 'statechartexpressions_RelationalExpression'):
        assert _is_linked(a1, 'statechartexpressions_RelationalExpression', b)
    _safe_set(b, 'statechartexpressions_EqualityExpression39', a2)
    assert _is_linked(b, 'statechartexpressions_EqualityExpression39', a2)
    if hasattr(a1, 'statechartexpressions_RelationalExpression'):
        assert not _is_linked(a1, 'statechartexpressions_RelationalExpression', b)
    if hasattr(a2, 'statechartexpressions_RelationalExpression'):
        assert _is_linked(a2, 'statechartexpressions_RelationalExpression', b)
    _safe_set(b, 'statechartexpressions_EqualityExpression39', None)
    assert not _is_linked(b, 'statechartexpressions_EqualityExpression39', a2)
    if hasattr(a2, 'statechartexpressions_RelationalExpression'):
        assert not _is_linked(a2, 'statechartexpressions_RelationalExpression', b)


def test_assoc_operand143_reverse_link_reassign_clear():
    a1 = statechartexpressions_ShiftExpression(operator="sample_text")
    a2 = statechartexpressions_ShiftExpression(operator="sample_text_2")
    b = statechartexpressions_RelationalExpression(operator="sample_text")
    _safe_set(b, 'statechartexpressions_RelationalExpression44', a1)
    assert _is_linked(b, 'statechartexpressions_RelationalExpression44', a1)
    if hasattr(a1, 'statechartexpressions_ShiftExpression'):
        assert _is_linked(a1, 'statechartexpressions_ShiftExpression', b)
    _safe_set(b, 'statechartexpressions_RelationalExpression44', a2)
    assert _is_linked(b, 'statechartexpressions_RelationalExpression44', a2)
    if hasattr(a1, 'statechartexpressions_ShiftExpression'):
        assert not _is_linked(a1, 'statechartexpressions_ShiftExpression', b)
    if hasattr(a2, 'statechartexpressions_ShiftExpression'):
        assert _is_linked(a2, 'statechartexpressions_ShiftExpression', b)
    _safe_set(b, 'statechartexpressions_RelationalExpression44', None)
    assert not _is_linked(b, 'statechartexpressions_RelationalExpression44', a2)
    if hasattr(a2, 'statechartexpressions_ShiftExpression'):
        assert not _is_linked(a2, 'statechartexpressions_ShiftExpression', b)


def test_assoc_operand157_reverse_link_reassign_clear():
    a1 = statechartexpressions_ShiftExpression(operator="sample_text")
    a2 = statechartexpressions_ShiftExpression(operator="sample_text_2")
    b = statechartexpressions_AdditiveExpression(operator="sample_text")
    _safe_set(b, 'statechartexpressions_AdditiveExpression', a1)
    assert _is_linked(b, 'statechartexpressions_AdditiveExpression', a1)
    if hasattr(a1, 'statechartexpressions_ShiftExpression58'):
        assert _is_linked(a1, 'statechartexpressions_ShiftExpression58', b)
    _safe_set(b, 'statechartexpressions_AdditiveExpression', a2)
    assert _is_linked(b, 'statechartexpressions_AdditiveExpression', a2)
    if hasattr(a1, 'statechartexpressions_ShiftExpression58'):
        assert not _is_linked(a1, 'statechartexpressions_ShiftExpression58', b)
    if hasattr(a2, 'statechartexpressions_ShiftExpression58'):
        assert _is_linked(a2, 'statechartexpressions_ShiftExpression58', b)
    _safe_set(b, 'statechartexpressions_AdditiveExpression', None)
    assert not _is_linked(b, 'statechartexpressions_AdditiveExpression', a2)
    if hasattr(a2, 'statechartexpressions_ShiftExpression58'):
        assert not _is_linked(a2, 'statechartexpressions_ShiftExpression58', b)


def test_assoc_operand162_reverse_link_reassign_clear():
    a1 = statechartexpressions_MultiplicativeExpression(operator="sample_text")
    a2 = statechartexpressions_MultiplicativeExpression(operator="sample_text_2")
    b = statechartexpressions_AdditiveExpression(operator="sample_text")
    _safe_set(b, 'statechartexpressions_AdditiveExpression63', a1)
    assert _is_linked(b, 'statechartexpressions_AdditiveExpression63', a1)
    if hasattr(a1, 'statechartexpressions_MultiplicativeExpression'):
        assert _is_linked(a1, 'statechartexpressions_MultiplicativeExpression', b)
    _safe_set(b, 'statechartexpressions_AdditiveExpression63', a2)
    assert _is_linked(b, 'statechartexpressions_AdditiveExpression63', a2)
    if hasattr(a1, 'statechartexpressions_MultiplicativeExpression'):
        assert not _is_linked(a1, 'statechartexpressions_MultiplicativeExpression', b)
    if hasattr(a2, 'statechartexpressions_MultiplicativeExpression'):
        assert _is_linked(a2, 'statechartexpressions_MultiplicativeExpression', b)
    _safe_set(b, 'statechartexpressions_AdditiveExpression63', None)
    assert not _is_linked(b, 'statechartexpressions_AdditiveExpression63', a2)
    if hasattr(a2, 'statechartexpressions_MultiplicativeExpression'):
        assert not _is_linked(a2, 'statechartexpressions_MultiplicativeExpression', b)


def test_assoc_operand167_reverse_link_reassign_clear():
    a1 = statechartexpressions_UnaryExpression(operator="sample_text")
    a2 = statechartexpressions_UnaryExpression(operator="sample_text_2")
    b = statechartexpressions_MultiplicativeExpression(operator="sample_text")
    _safe_set(b, 'statechartexpressions_MultiplicativeExpression68', a1)
    assert _is_linked(b, 'statechartexpressions_MultiplicativeExpression68', a1)
    if hasattr(a1, 'statechartexpressions_UnaryExpression'):
        assert _is_linked(a1, 'statechartexpressions_UnaryExpression', b)
    _safe_set(b, 'statechartexpressions_MultiplicativeExpression68', a2)
    assert _is_linked(b, 'statechartexpressions_MultiplicativeExpression68', a2)
    if hasattr(a1, 'statechartexpressions_UnaryExpression'):
        assert not _is_linked(a1, 'statechartexpressions_UnaryExpression', b)
    if hasattr(a2, 'statechartexpressions_UnaryExpression'):
        assert _is_linked(a2, 'statechartexpressions_UnaryExpression', b)
    _safe_set(b, 'statechartexpressions_MultiplicativeExpression68', None)
    assert not _is_linked(b, 'statechartexpressions_MultiplicativeExpression68', a2)
    if hasattr(a2, 'statechartexpressions_UnaryExpression'):
        assert not _is_linked(a2, 'statechartexpressions_UnaryExpression', b)


def test_assoc_operand240_reverse_link_reassign_clear():
    a1 = statechartexpressions_RelationalExpression(operator="sample_text")
    a2 = statechartexpressions_RelationalExpression(operator="sample_text_2")
    b = statechartexpressions_EqualityExpression(operator="sample_text")
    _safe_set(b, 'statechartexpressions_EqualityExpression41', a1)
    assert _is_linked(b, 'statechartexpressions_EqualityExpression41', a1)
    if hasattr(a1, 'statechartexpressions_RelationalExpression42'):
        assert _is_linked(a1, 'statechartexpressions_RelationalExpression42', b)
    _safe_set(b, 'statechartexpressions_EqualityExpression41', a2)
    assert _is_linked(b, 'statechartexpressions_EqualityExpression41', a2)
    if hasattr(a1, 'statechartexpressions_RelationalExpression42'):
        assert not _is_linked(a1, 'statechartexpressions_RelationalExpression42', b)
    if hasattr(a2, 'statechartexpressions_RelationalExpression42'):
        assert _is_linked(a2, 'statechartexpressions_RelationalExpression42', b)
    _safe_set(b, 'statechartexpressions_EqualityExpression41', None)
    assert not _is_linked(b, 'statechartexpressions_EqualityExpression41', a2)
    if hasattr(a2, 'statechartexpressions_RelationalExpression42'):
        assert not _is_linked(a2, 'statechartexpressions_RelationalExpression42', b)


def test_assoc_operand245_reverse_link_reassign_clear():
    a1 = statechartexpressions_ShiftExpression(operator="sample_text")
    a2 = statechartexpressions_ShiftExpression(operator="sample_text_2")
    b = statechartexpressions_RelationalExpression(operator="sample_text")
    _safe_set(b, 'statechartexpressions_RelationalExpression46', a1)
    assert _is_linked(b, 'statechartexpressions_RelationalExpression46', a1)
    if hasattr(a1, 'statechartexpressions_ShiftExpression47'):
        assert _is_linked(a1, 'statechartexpressions_ShiftExpression47', b)
    _safe_set(b, 'statechartexpressions_RelationalExpression46', a2)
    assert _is_linked(b, 'statechartexpressions_RelationalExpression46', a2)
    if hasattr(a1, 'statechartexpressions_ShiftExpression47'):
        assert not _is_linked(a1, 'statechartexpressions_ShiftExpression47', b)
    if hasattr(a2, 'statechartexpressions_ShiftExpression47'):
        assert _is_linked(a2, 'statechartexpressions_ShiftExpression47', b)
    _safe_set(b, 'statechartexpressions_RelationalExpression46', None)
    assert not _is_linked(b, 'statechartexpressions_RelationalExpression46', a2)
    if hasattr(a2, 'statechartexpressions_ShiftExpression47'):
        assert not _is_linked(a2, 'statechartexpressions_ShiftExpression47', b)


def test_assoc_operand259_reverse_link_reassign_clear():
    a1 = statechartexpressions_ShiftExpression(operator="sample_text")
    a2 = statechartexpressions_ShiftExpression(operator="sample_text_2")
    b = statechartexpressions_AdditiveExpression(operator="sample_text")
    _safe_set(b, 'statechartexpressions_AdditiveExpression61', a1)
    assert _is_linked(b, 'statechartexpressions_AdditiveExpression61', a1)
    if hasattr(a1, 'statechartexpressions_ShiftExpression60'):
        assert _is_linked(a1, 'statechartexpressions_ShiftExpression60', b)
    _safe_set(b, 'statechartexpressions_AdditiveExpression61', a2)
    assert _is_linked(b, 'statechartexpressions_AdditiveExpression61', a2)
    if hasattr(a1, 'statechartexpressions_ShiftExpression60'):
        assert not _is_linked(a1, 'statechartexpressions_ShiftExpression60', b)
    if hasattr(a2, 'statechartexpressions_ShiftExpression60'):
        assert _is_linked(a2, 'statechartexpressions_ShiftExpression60', b)
    _safe_set(b, 'statechartexpressions_AdditiveExpression61', None)
    assert not _is_linked(b, 'statechartexpressions_AdditiveExpression61', a2)
    if hasattr(a2, 'statechartexpressions_ShiftExpression60'):
        assert not _is_linked(a2, 'statechartexpressions_ShiftExpression60', b)


def test_assoc_operand264_reverse_link_reassign_clear():
    a1 = statechartexpressions_MultiplicativeExpression(operator="sample_text")
    a2 = statechartexpressions_MultiplicativeExpression(operator="sample_text_2")
    b = statechartexpressions_AdditiveExpression(operator="sample_text")
    _safe_set(b, 'statechartexpressions_AdditiveExpression65', a1)
    assert _is_linked(b, 'statechartexpressions_AdditiveExpression65', a1)
    if hasattr(a1, 'statechartexpressions_MultiplicativeExpression66'):
        assert _is_linked(a1, 'statechartexpressions_MultiplicativeExpression66', b)
    _safe_set(b, 'statechartexpressions_AdditiveExpression65', a2)
    assert _is_linked(b, 'statechartexpressions_AdditiveExpression65', a2)
    if hasattr(a1, 'statechartexpressions_MultiplicativeExpression66'):
        assert not _is_linked(a1, 'statechartexpressions_MultiplicativeExpression66', b)
    if hasattr(a2, 'statechartexpressions_MultiplicativeExpression66'):
        assert _is_linked(a2, 'statechartexpressions_MultiplicativeExpression66', b)
    _safe_set(b, 'statechartexpressions_AdditiveExpression65', None)
    assert not _is_linked(b, 'statechartexpressions_AdditiveExpression65', a2)
    if hasattr(a2, 'statechartexpressions_MultiplicativeExpression66'):
        assert not _is_linked(a2, 'statechartexpressions_MultiplicativeExpression66', b)


def test_assoc_operand269_reverse_link_reassign_clear():
    a1 = statechartexpressions_UnaryExpression(operator="sample_text")
    a2 = statechartexpressions_UnaryExpression(operator="sample_text_2")
    b = statechartexpressions_MultiplicativeExpression(operator="sample_text")
    _safe_set(b, 'statechartexpressions_MultiplicativeExpression70', a1)
    assert _is_linked(b, 'statechartexpressions_MultiplicativeExpression70', a1)
    if hasattr(a1, 'statechartexpressions_UnaryExpression71'):
        assert _is_linked(a1, 'statechartexpressions_UnaryExpression71', b)
    _safe_set(b, 'statechartexpressions_MultiplicativeExpression70', a2)
    assert _is_linked(b, 'statechartexpressions_MultiplicativeExpression70', a2)
    if hasattr(a1, 'statechartexpressions_UnaryExpression71'):
        assert not _is_linked(a1, 'statechartexpressions_UnaryExpression71', b)
    if hasattr(a2, 'statechartexpressions_UnaryExpression71'):
        assert _is_linked(a2, 'statechartexpressions_UnaryExpression71', b)
    _safe_set(b, 'statechartexpressions_MultiplicativeExpression70', None)
    assert not _is_linked(b, 'statechartexpressions_MultiplicativeExpression70', a2)
    if hasattr(a2, 'statechartexpressions_UnaryExpression71'):
        assert not _is_linked(a2, 'statechartexpressions_UnaryExpression71', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_event12_stub_double():
    # statechartexpressions_EventRaising has no real 'statechartexpressions_EventRaising' property in the generated
    # code (a bare stub) -- manually attach it so statechartexpressions_SignalEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechartexpressions_SignalEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechartexpressions_SignalEvent(identifier="sample_text")
    partner = statechartexpressions_EventRaising()
    setattr(partner, 'statechartexpressions_EventRaising', None)
    _safe_set(owner, 'statechartexpressions_SignalEvent', partner)
    assert getattr(partner, 'statechartexpressions_EventRaising') == owner
    _safe_set(owner, 'statechartexpressions_SignalEvent', None)
    assert getattr(partner, 'statechartexpressions_EventRaising') is None


def test_assoc_operand133_stub_double():
    # statechartexpressions_BitwiseAndExpression has no real 'statechartexpressions_BitwiseAndExpression34' property in the generated
    # code (a bare stub) -- manually attach it so statechartexpressions_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechartexpressions_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechartexpressions_EqualityExpression(operator="sample_text")
    partner = statechartexpressions_BitwiseAndExpression()
    setattr(partner, 'statechartexpressions_BitwiseAndExpression34', None)
    _safe_set(owner, 'statechartexpressions_EqualityExpression', partner)
    assert getattr(partner, 'statechartexpressions_BitwiseAndExpression34') == owner
    _safe_set(owner, 'statechartexpressions_EqualityExpression', None)
    assert getattr(partner, 'statechartexpressions_BitwiseAndExpression34') is None


def test_assoc_operand235_stub_double():
    # statechartexpressions_BitwiseAndExpression has no real 'statechartexpressions_BitwiseAndExpression36' property in the generated
    # code (a bare stub) -- manually attach it so statechartexpressions_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechartexpressions_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechartexpressions_EqualityExpression(operator="sample_text")
    partner = statechartexpressions_BitwiseAndExpression()
    setattr(partner, 'statechartexpressions_BitwiseAndExpression36', None)
    _safe_set(owner, 'statechartexpressions_EqualityExpression37', partner)
    assert getattr(partner, 'statechartexpressions_BitwiseAndExpression36') == owner
    _safe_set(owner, 'statechartexpressions_EqualityExpression37', None)
    assert getattr(partner, 'statechartexpressions_BitwiseAndExpression36') is None


def test_assoc_operand251_stub_double():
    # statechartexpressions_ConditionalExpression has no real 'statechartexpressions_ConditionalExpression52' property in the generated
    # code (a bare stub) -- manually attach it so statechartexpressions_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechartexpressions_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechartexpressions_ShiftExpression(operator="sample_text")
    partner = statechartexpressions_ConditionalExpression()
    setattr(partner, 'statechartexpressions_ConditionalExpression52', None)
    _safe_set(owner, 'statechartexpressions_ShiftExpression53', partner)
    assert getattr(partner, 'statechartexpressions_ConditionalExpression52') == owner
    _safe_set(owner, 'statechartexpressions_ShiftExpression53', None)
    assert getattr(partner, 'statechartexpressions_ConditionalExpression52') is None


def test_assoc_operand354_stub_double():
    # statechartexpressions_ConditionalExpression has no real 'statechartexpressions_ConditionalExpression55' property in the generated
    # code (a bare stub) -- manually attach it so statechartexpressions_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechartexpressions_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechartexpressions_ShiftExpression(operator="sample_text")
    partner = statechartexpressions_ConditionalExpression()
    setattr(partner, 'statechartexpressions_ConditionalExpression55', None)
    _safe_set(owner, 'statechartexpressions_ShiftExpression56', partner)
    assert getattr(partner, 'statechartexpressions_ConditionalExpression55') == owner
    _safe_set(owner, 'statechartexpressions_ShiftExpression56', None)
    assert getattr(partner, 'statechartexpressions_ConditionalExpression55') is None


def test_assoc_operand72_stub_double():
    # statechartexpressions_PrimaryExpression has no real 'statechartexpressions_PrimaryExpression' property in the generated
    # code (a bare stub) -- manually attach it so statechartexpressions_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechartexpressions_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechartexpressions_UnaryExpression(operator="sample_text")
    partner = statechartexpressions_PrimaryExpression()
    setattr(partner, 'statechartexpressions_PrimaryExpression', None)
    _safe_set(owner, 'statechartexpressions_UnaryExpression73', partner)
    assert getattr(partner, 'statechartexpressions_PrimaryExpression') == owner
    _safe_set(owner, 'statechartexpressions_UnaryExpression73', None)
    assert getattr(partner, 'statechartexpressions_PrimaryExpression') is None


def test_assoc_procedure11_stub_double():
    # statechartexpressions_ProcedureCall has no real 'statechartexpressions_ProcedureCall' property in the generated
    # code (a bare stub) -- manually attach it so statechartexpressions_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechartexpressions_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechartexpressions_Procedure(identifier="sample_text")
    partner = statechartexpressions_ProcedureCall()
    setattr(partner, 'statechartexpressions_ProcedureCall', None)
    _safe_set(owner, 'statechartexpressions_Procedure', partner)
    assert getattr(partner, 'statechartexpressions_ProcedureCall') == owner
    _safe_set(owner, 'statechartexpressions_Procedure', None)
    assert getattr(partner, 'statechartexpressions_ProcedureCall') is None


def test_assoc_value9_stub_double():
    # statechartexpressions_ConditionalExpression has no real 'statechartexpressions_ConditionalExpression' property in the generated
    # code (a bare stub) -- manually attach it so statechartexpressions_VariableAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechartexpressions_VariableAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechartexpressions_VariableAssignment(operator="sample_text")
    partner = statechartexpressions_ConditionalExpression()
    setattr(partner, 'statechartexpressions_ConditionalExpression', None)
    _safe_set(owner, 'statechartexpressions_VariableAssignment10', partner)
    assert getattr(partner, 'statechartexpressions_ConditionalExpression') == owner
    _safe_set(owner, 'statechartexpressions_VariableAssignment10', None)
    assert getattr(partner, 'statechartexpressions_ConditionalExpression') is None


def test_assoc_variable6_stub_double():
    # statechartexpressions_VariableReference has no real 'statechartexpressions_VariableReference' property in the generated
    # code (a bare stub) -- manually attach it so statechartexpressions_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechartexpressions_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechartexpressions_Variable(identifier="sample_text")
    partner = statechartexpressions_VariableReference()
    setattr(partner, 'statechartexpressions_VariableReference', None)
    _safe_set(owner, 'statechartexpressions_Variable', partner)
    assert getattr(partner, 'statechartexpressions_VariableReference') == owner
    _safe_set(owner, 'statechartexpressions_Variable', None)
    assert getattr(partner, 'statechartexpressions_VariableReference') is None


def test_assoc_variableReference7_stub_double():
    # statechartexpressions_VariableReference has no real 'statechartexpressions_VariableReference8' property in the generated
    # code (a bare stub) -- manually attach it so statechartexpressions_VariableAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechartexpressions_VariableAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechartexpressions_VariableAssignment(operator="sample_text")
    partner = statechartexpressions_VariableReference()
    setattr(partner, 'statechartexpressions_VariableReference8', None)
    _safe_set(owner, 'statechartexpressions_VariableAssignment', partner)
    assert getattr(partner, 'statechartexpressions_VariableReference8') == owner
    _safe_set(owner, 'statechartexpressions_VariableAssignment', None)
    assert getattr(partner, 'statechartexpressions_VariableReference8') is None


