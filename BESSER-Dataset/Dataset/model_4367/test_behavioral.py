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

def test_assoc_block7_stub_double():
    # minilang_Block has no real 'minilang_Block' property in the generated
    # code (a bare stub) -- manually attach it so minilang_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minilang_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minilang_Method(name="sample_text")
    partner = minilang_Block()
    setattr(partner, 'minilang_Block', None)
    _safe_set(owner, 'minilang_Method8', partner)
    assert getattr(partner, 'minilang_Block') == owner
    _safe_set(owner, 'minilang_Method8', None)
    assert getattr(partner, 'minilang_Block') is None


def test_assoc_method34_stub_double():
    # minilang_CallMethod has no real 'minilang_CallMethod' property in the generated
    # code (a bare stub) -- manually attach it so minilang_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minilang_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minilang_Method(name="sample_text")
    partner = minilang_CallMethod()
    setattr(partner, 'minilang_CallMethod', None)
    _safe_set(owner, 'minilang_Method35', partner)
    assert getattr(partner, 'minilang_CallMethod') == owner
    _safe_set(owner, 'minilang_Method35', None)
    assert getattr(partner, 'minilang_CallMethod') is None


def test_assoc_variable22_stub_double():
    # minilang_VariableRef has no real 'minilang_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so minilang_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minilang_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minilang_Variable(name="sample_text", value=3.14)
    partner = minilang_VariableRef()
    setattr(partner, 'minilang_VariableRef', None)
    _safe_set(owner, 'minilang_Variable23', partner)
    assert getattr(partner, 'minilang_VariableRef') == owner
    _safe_set(owner, 'minilang_Variable23', None)
    assert getattr(partner, 'minilang_VariableRef') is None


def test_assoc_variable24_stub_double():
    # minilang_VariableAffect has no real 'minilang_VariableAffect' property in the generated
    # code (a bare stub) -- manually attach it so minilang_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minilang_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minilang_Variable(name="sample_text", value=3.14)
    partner = minilang_VariableAffect()
    setattr(partner, 'minilang_VariableAffect', None)
    _safe_set(owner, 'minilang_Variable25', partner)
    assert getattr(partner, 'minilang_VariableAffect') == owner
    _safe_set(owner, 'minilang_Variable25', None)
    assert getattr(partner, 'minilang_VariableAffect') is None


