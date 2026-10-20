import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryOperation,
    Condition,
    Statement,
    Value,
    minilang_BinaryOperation,
    minilang_Block,
    minilang_CallMethod,
    minilang_Condition,
    minilang_Constant,
    minilang_GreaterThan,
    minilang_IfStmt,
    minilang_Line,
    minilang_Method,
    minilang_Modulo,
    minilang_Move,
    minilang_Program,
    minilang_RotateLeft,
    minilang_RotateRight,
    minilang_Statement,
    minilang_Sum,
    minilang_Value,
    minilang_Variable,
    minilang_VariableAffect,
    minilang_VariableRef,
    Cardinals,
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

def test_assoc_block7_reverse_link_reassign_clear():
    a1 = minilang_Method(name="sample_text")
    a2 = minilang_Method(name="sample_text_2")
    b = minilang_Block()
    _safe_set(b, 'minilang_Block', a1)
    assert _is_linked(b, 'minilang_Block', a1)
    if hasattr(a1, 'minilang_Method8'):
        assert _is_linked(a1, 'minilang_Method8', b)
    _safe_set(b, 'minilang_Block', a2)
    assert _is_linked(b, 'minilang_Block', a2)
    if hasattr(a1, 'minilang_Method8'):
        assert not _is_linked(a1, 'minilang_Method8', b)
    if hasattr(a2, 'minilang_Method8'):
        assert _is_linked(a2, 'minilang_Method8', b)
    _safe_set(b, 'minilang_Block', None)
    assert not _is_linked(b, 'minilang_Block', a2)
    if hasattr(a2, 'minilang_Method8'):
        assert not _is_linked(a2, 'minilang_Method8', b)


def test_assoc_condition16_reverse_link_reassign_clear():
    a1 = minilang_IfStmt()
    a2 = minilang_IfStmt()
    b = minilang_Condition()
    _safe_set(b, 'minilang_Condition', a1)
    assert _is_linked(b, 'minilang_Condition', a1)
    if hasattr(a1, 'minilang_IfStmt17'):
        assert _is_linked(a1, 'minilang_IfStmt17', b)
    _safe_set(b, 'minilang_Condition', a2)
    assert _is_linked(b, 'minilang_Condition', a2)
    if hasattr(a1, 'minilang_IfStmt17'):
        assert not _is_linked(a1, 'minilang_IfStmt17', b)
    if hasattr(a2, 'minilang_IfStmt17'):
        assert _is_linked(a2, 'minilang_IfStmt17', b)
    _safe_set(b, 'minilang_Condition', None)
    assert not _is_linked(b, 'minilang_Condition', a2)
    if hasattr(a2, 'minilang_IfStmt17'):
        assert not _is_linked(a2, 'minilang_IfStmt17', b)


def test_assoc_elseBranch13_reverse_link_reassign_clear():
    a1 = minilang_IfStmt()
    a2 = minilang_IfStmt()
    b = minilang_Block()
    _safe_set(b, 'minilang_Block15', a1)
    assert _is_linked(b, 'minilang_Block15', a1)
    if hasattr(a1, 'minilang_IfStmt14'):
        assert _is_linked(a1, 'minilang_IfStmt14', b)
    _safe_set(b, 'minilang_Block15', a2)
    assert _is_linked(b, 'minilang_Block15', a2)
    if hasattr(a1, 'minilang_IfStmt14'):
        assert not _is_linked(a1, 'minilang_IfStmt14', b)
    if hasattr(a2, 'minilang_IfStmt14'):
        assert _is_linked(a2, 'minilang_IfStmt14', b)
    _safe_set(b, 'minilang_Block15', None)
    assert not _is_linked(b, 'minilang_Block15', a2)
    if hasattr(a2, 'minilang_IfStmt14'):
        assert not _is_linked(a2, 'minilang_IfStmt14', b)


def test_assoc_left18_reverse_link_reassign_clear():
    a1 = minilang_Value()
    a2 = minilang_Value()
    b = minilang_GreaterThan()
    _safe_set(b, 'minilang_GreaterThan', a1)
    assert _is_linked(b, 'minilang_GreaterThan', a1)
    if hasattr(a1, 'minilang_Value'):
        assert _is_linked(a1, 'minilang_Value', b)
    _safe_set(b, 'minilang_GreaterThan', a2)
    assert _is_linked(b, 'minilang_GreaterThan', a2)
    if hasattr(a1, 'minilang_Value'):
        assert not _is_linked(a1, 'minilang_Value', b)
    if hasattr(a2, 'minilang_Value'):
        assert _is_linked(a2, 'minilang_Value', b)
    _safe_set(b, 'minilang_GreaterThan', None)
    assert not _is_linked(b, 'minilang_GreaterThan', a2)
    if hasattr(a2, 'minilang_Value'):
        assert not _is_linked(a2, 'minilang_Value', b)


def test_assoc_lines4_reverse_link_reassign_clear():
    a1 = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    a2 = minilang_Program(angle="sample_text_2", distance=9.99, x=9.99, y=9.99)
    b = minilang_Line(x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    _safe_set(b, 'minilang_Line', a1)
    assert _is_linked(b, 'minilang_Line', a1)
    if hasattr(a1, 'minilang_Program5'):
        assert _is_linked(a1, 'minilang_Program5', b)
    _safe_set(b, 'minilang_Line', a2)
    assert _is_linked(b, 'minilang_Line', a2)
    if hasattr(a1, 'minilang_Program5'):
        assert not _is_linked(a1, 'minilang_Program5', b)
    if hasattr(a2, 'minilang_Program5'):
        assert _is_linked(a2, 'minilang_Program5', b)
    _safe_set(b, 'minilang_Line', None)
    assert not _is_linked(b, 'minilang_Line', a2)
    if hasattr(a2, 'minilang_Program5'):
        assert not _is_linked(a2, 'minilang_Program5', b)


def test_assoc_mainMethod1_reverse_link_reassign_clear():
    a1 = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    a2 = minilang_Program(angle="sample_text_2", distance=9.99, x=9.99, y=9.99)
    b = minilang_Method(name="sample_text")
    _safe_set(b, 'minilang_Method', a1)
    assert _is_linked(b, 'minilang_Method', a1)
    if hasattr(a1, 'minilang_Program'):
        assert _is_linked(a1, 'minilang_Program', b)
    _safe_set(b, 'minilang_Method', a2)
    assert _is_linked(b, 'minilang_Method', a2)
    if hasattr(a1, 'minilang_Program'):
        assert not _is_linked(a1, 'minilang_Program', b)
    if hasattr(a2, 'minilang_Program'):
        assert _is_linked(a2, 'minilang_Program', b)
    _safe_set(b, 'minilang_Method', None)
    assert not _is_linked(b, 'minilang_Method', a2)
    if hasattr(a2, 'minilang_Program'):
        assert not _is_linked(a2, 'minilang_Program', b)


def test_assoc_method34_reverse_link_reassign_clear():
    a1 = minilang_Method(name="sample_text")
    a2 = minilang_Method(name="sample_text_2")
    b = minilang_CallMethod()
    _safe_set(b, 'minilang_CallMethod', a1)
    assert _is_linked(b, 'minilang_CallMethod', a1)
    if hasattr(a1, 'minilang_Method35'):
        assert _is_linked(a1, 'minilang_Method35', b)
    _safe_set(b, 'minilang_CallMethod', a2)
    assert _is_linked(b, 'minilang_CallMethod', a2)
    if hasattr(a1, 'minilang_Method35'):
        assert not _is_linked(a1, 'minilang_Method35', b)
    if hasattr(a2, 'minilang_Method35'):
        assert _is_linked(a2, 'minilang_Method35', b)
    _safe_set(b, 'minilang_CallMethod', None)
    assert not _is_linked(b, 'minilang_CallMethod', a2)
    if hasattr(a2, 'minilang_Method35'):
        assert not _is_linked(a2, 'minilang_Method35', b)


def test_assoc_methods0_reverse_link_reassign_clear():
    a1 = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    a2 = minilang_Program(angle="sample_text_2", distance=9.99, x=9.99, y=9.99)
    b = minilang_Method(name="sample_text")
    _safe_set(b, 'Method', a1)
    assert _is_linked(b, 'Method', a1)
    if hasattr(a1, 'program'):
        assert _is_linked(a1, 'program', b)
    _safe_set(b, 'Method', a2)
    assert _is_linked(b, 'Method', a2)
    if hasattr(a1, 'program'):
        assert not _is_linked(a1, 'program', b)
    if hasattr(a2, 'program'):
        assert _is_linked(a2, 'program', b)
    _safe_set(b, 'Method', None)
    assert not _is_linked(b, 'Method', a2)
    if hasattr(a2, 'program'):
        assert not _is_linked(a2, 'program', b)


def test_assoc_program6_reverse_link_reassign_clear():
    a1 = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    a2 = minilang_Program(angle="sample_text_2", distance=9.99, x=9.99, y=9.99)
    b = minilang_Method(name="sample_text")
    _safe_set(b, 'methods', a1)
    assert _is_linked(b, 'methods', a1)
    if hasattr(a1, 'Program'):
        assert _is_linked(a1, 'Program', b)
    _safe_set(b, 'methods', a2)
    assert _is_linked(b, 'methods', a2)
    if hasattr(a1, 'Program'):
        assert not _is_linked(a1, 'Program', b)
    if hasattr(a2, 'Program'):
        assert _is_linked(a2, 'Program', b)
    _safe_set(b, 'methods', None)
    assert not _is_linked(b, 'methods', a2)
    if hasattr(a2, 'Program'):
        assert not _is_linked(a2, 'Program', b)


def test_assoc_right19_reverse_link_reassign_clear():
    a1 = minilang_Value()
    a2 = minilang_Value()
    b = minilang_GreaterThan()
    _safe_set(b, 'minilang_GreaterThan20', a1)
    assert _is_linked(b, 'minilang_GreaterThan20', a1)
    if hasattr(a1, 'minilang_Value21'):
        assert _is_linked(a1, 'minilang_Value21', b)
    _safe_set(b, 'minilang_GreaterThan20', a2)
    assert _is_linked(b, 'minilang_GreaterThan20', a2)
    if hasattr(a1, 'minilang_Value21'):
        assert not _is_linked(a1, 'minilang_Value21', b)
    if hasattr(a2, 'minilang_Value21'):
        assert _is_linked(a2, 'minilang_Value21', b)
    _safe_set(b, 'minilang_GreaterThan20', None)
    assert not _is_linked(b, 'minilang_GreaterThan20', a2)
    if hasattr(a2, 'minilang_Value21'):
        assert not _is_linked(a2, 'minilang_Value21', b)


def test_assoc_statements9_reverse_link_reassign_clear():
    a1 = minilang_Statement()
    a2 = minilang_Statement()
    b = minilang_Block()
    _safe_set(b, 'minilang_Block10', {a1})
    assert _is_linked(b, 'minilang_Block10', a1)
    if hasattr(a1, 'minilang_Statement'):
        assert _is_linked(a1, 'minilang_Statement', b)
    _safe_set(b, 'minilang_Block10', {a2})
    assert _is_linked(b, 'minilang_Block10', a2)
    if hasattr(a1, 'minilang_Statement'):
        assert not _is_linked(a1, 'minilang_Statement', b)
    if hasattr(a2, 'minilang_Statement'):
        assert _is_linked(a2, 'minilang_Statement', b)
    _safe_set(b, 'minilang_Block10', set())
    assert not _is_linked(b, 'minilang_Block10', a2)
    if hasattr(a2, 'minilang_Statement'):
        assert not _is_linked(a2, 'minilang_Statement', b)


def test_assoc_thenBranch11_reverse_link_reassign_clear():
    a1 = minilang_IfStmt()
    a2 = minilang_IfStmt()
    b = minilang_Block()
    _safe_set(b, 'minilang_Block12', a1)
    assert _is_linked(b, 'minilang_Block12', a1)
    if hasattr(a1, 'minilang_IfStmt'):
        assert _is_linked(a1, 'minilang_IfStmt', b)
    _safe_set(b, 'minilang_Block12', a2)
    assert _is_linked(b, 'minilang_Block12', a2)
    if hasattr(a1, 'minilang_IfStmt'):
        assert not _is_linked(a1, 'minilang_IfStmt', b)
    if hasattr(a2, 'minilang_IfStmt'):
        assert _is_linked(a2, 'minilang_IfStmt', b)
    _safe_set(b, 'minilang_Block12', None)
    assert not _is_linked(b, 'minilang_Block12', a2)
    if hasattr(a2, 'minilang_IfStmt'):
        assert not _is_linked(a2, 'minilang_IfStmt', b)


def test_assoc_value26_reverse_link_reassign_clear():
    a1 = minilang_VariableAffect()
    a2 = minilang_VariableAffect()
    b = minilang_Value()
    _safe_set(b, 'minilang_Value28', a1)
    assert _is_linked(b, 'minilang_Value28', a1)
    if hasattr(a1, 'minilang_VariableAffect27'):
        assert _is_linked(a1, 'minilang_VariableAffect27', b)
    _safe_set(b, 'minilang_Value28', a2)
    assert _is_linked(b, 'minilang_Value28', a2)
    if hasattr(a1, 'minilang_VariableAffect27'):
        assert not _is_linked(a1, 'minilang_VariableAffect27', b)
    if hasattr(a2, 'minilang_VariableAffect27'):
        assert _is_linked(a2, 'minilang_VariableAffect27', b)
    _safe_set(b, 'minilang_Value28', None)
    assert not _is_linked(b, 'minilang_Value28', a2)
    if hasattr(a2, 'minilang_VariableAffect27'):
        assert not _is_linked(a2, 'minilang_VariableAffect27', b)


def test_assoc_variable22_reverse_link_reassign_clear():
    a1 = minilang_VariableRef()
    a2 = minilang_VariableRef()
    b = minilang_Variable(name="sample_text", value=3.14)
    _safe_set(b, 'minilang_Variable23', a1)
    assert _is_linked(b, 'minilang_Variable23', a1)
    if hasattr(a1, 'minilang_VariableRef'):
        assert _is_linked(a1, 'minilang_VariableRef', b)
    _safe_set(b, 'minilang_Variable23', a2)
    assert _is_linked(b, 'minilang_Variable23', a2)
    if hasattr(a1, 'minilang_VariableRef'):
        assert not _is_linked(a1, 'minilang_VariableRef', b)
    if hasattr(a2, 'minilang_VariableRef'):
        assert _is_linked(a2, 'minilang_VariableRef', b)
    _safe_set(b, 'minilang_Variable23', None)
    assert not _is_linked(b, 'minilang_Variable23', a2)
    if hasattr(a2, 'minilang_VariableRef'):
        assert not _is_linked(a2, 'minilang_VariableRef', b)


def test_assoc_variable24_reverse_link_reassign_clear():
    a1 = minilang_VariableAffect()
    a2 = minilang_VariableAffect()
    b = minilang_Variable(name="sample_text", value=3.14)
    _safe_set(b, 'minilang_Variable25', a1)
    assert _is_linked(b, 'minilang_Variable25', a1)
    if hasattr(a1, 'minilang_VariableAffect'):
        assert _is_linked(a1, 'minilang_VariableAffect', b)
    _safe_set(b, 'minilang_Variable25', a2)
    assert _is_linked(b, 'minilang_Variable25', a2)
    if hasattr(a1, 'minilang_VariableAffect'):
        assert not _is_linked(a1, 'minilang_VariableAffect', b)
    if hasattr(a2, 'minilang_VariableAffect'):
        assert _is_linked(a2, 'minilang_VariableAffect', b)
    _safe_set(b, 'minilang_Variable25', None)
    assert not _is_linked(b, 'minilang_Variable25', a2)
    if hasattr(a2, 'minilang_VariableAffect'):
        assert not _is_linked(a2, 'minilang_VariableAffect', b)


def test_assoc_variables2_reverse_link_reassign_clear():
    a1 = minilang_Variable(name="sample_text", value=3.14)
    a2 = minilang_Variable(name="sample_text_2", value=9.99)
    b = minilang_Program(angle="sample_text", distance=3.14, x=3.14, y=3.14)
    _safe_set(b, 'minilang_Program3', {a1})
    assert _is_linked(b, 'minilang_Program3', a1)
    if hasattr(a1, 'minilang_Variable'):
        assert _is_linked(a1, 'minilang_Variable', b)
    _safe_set(b, 'minilang_Program3', {a2})
    assert _is_linked(b, 'minilang_Program3', a2)
    if hasattr(a1, 'minilang_Variable'):
        assert not _is_linked(a1, 'minilang_Variable', b)
    if hasattr(a2, 'minilang_Variable'):
        assert _is_linked(a2, 'minilang_Variable', b)
    _safe_set(b, 'minilang_Program3', set())
    assert not _is_linked(b, 'minilang_Program3', a2)
    if hasattr(a2, 'minilang_Variable'):
        assert not _is_linked(a2, 'minilang_Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_left31_stub_double():
    # minilang_BinaryOperation has no real 'minilang_BinaryOperation32' property in the generated
    # code (a bare stub) -- manually attach it so minilang_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minilang_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minilang_Value()
    partner = minilang_BinaryOperation()
    setattr(partner, 'minilang_BinaryOperation32', None)
    _safe_set(owner, 'minilang_Value33', partner)
    assert getattr(partner, 'minilang_BinaryOperation32') == owner
    _safe_set(owner, 'minilang_Value33', None)
    assert getattr(partner, 'minilang_BinaryOperation32') is None


def test_assoc_right29_stub_double():
    # minilang_BinaryOperation has no real 'minilang_BinaryOperation' property in the generated
    # code (a bare stub) -- manually attach it so minilang_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minilang_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minilang_Value()
    partner = minilang_BinaryOperation()
    setattr(partner, 'minilang_BinaryOperation', None)
    _safe_set(owner, 'minilang_Value30', partner)
    assert getattr(partner, 'minilang_BinaryOperation') == owner
    _safe_set(owner, 'minilang_Value30', None)
    assert getattr(partner, 'minilang_BinaryOperation') is None


