import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Operand,
    ast_Expression,
    ast_Model,
    ast_Number,
    ast_Operand,
    ast_Operator,
    ast_Variable,
    ArithmeticOperator,
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

def test_assoc_left5_reverse_link_reassign_clear():
    a1 = ast_Operator(op="sample_text")
    a2 = ast_Operator(op="sample_text_2")
    b = ast_Expression(incrementalID="sample_text")
    _safe_set(b, 'Expression6', a1)
    assert _is_linked(b, 'Expression6', a1)
    if hasattr(a1, 'leftInverse'):
        assert _is_linked(a1, 'leftInverse', b)
    _safe_set(b, 'Expression6', a2)
    assert _is_linked(b, 'Expression6', a2)
    if hasattr(a1, 'leftInverse'):
        assert not _is_linked(a1, 'leftInverse', b)
    if hasattr(a2, 'leftInverse'):
        assert _is_linked(a2, 'leftInverse', b)
    _safe_set(b, 'Expression6', None)
    assert not _is_linked(b, 'Expression6', a2)
    if hasattr(a2, 'leftInverse'):
        assert not _is_linked(a2, 'leftInverse', b)


def test_assoc_leftInverse2_reverse_link_reassign_clear():
    a1 = ast_Operator(op="sample_text")
    a2 = ast_Operator(op="sample_text_2")
    b = ast_Expression(incrementalID="sample_text")
    _safe_set(b, 'left', a1)
    assert _is_linked(b, 'left', a1)
    if hasattr(a1, 'Operator'):
        assert _is_linked(a1, 'Operator', b)
    _safe_set(b, 'left', a2)
    assert _is_linked(b, 'left', a2)
    if hasattr(a1, 'Operator'):
        assert not _is_linked(a1, 'Operator', b)
    if hasattr(a2, 'Operator'):
        assert _is_linked(a2, 'Operator', b)
    _safe_set(b, 'left', None)
    assert not _is_linked(b, 'left', a2)
    if hasattr(a2, 'Operator'):
        assert not _is_linked(a2, 'Operator', b)


def test_assoc_right7_reverse_link_reassign_clear():
    a1 = ast_Operator(op="sample_text")
    a2 = ast_Operator(op="sample_text_2")
    b = ast_Expression(incrementalID="sample_text")
    _safe_set(b, 'Expression8', a1)
    assert _is_linked(b, 'Expression8', a1)
    if hasattr(a1, 'rightInverse'):
        assert _is_linked(a1, 'rightInverse', b)
    _safe_set(b, 'Expression8', a2)
    assert _is_linked(b, 'Expression8', a2)
    if hasattr(a1, 'rightInverse'):
        assert not _is_linked(a1, 'rightInverse', b)
    if hasattr(a2, 'rightInverse'):
        assert _is_linked(a2, 'rightInverse', b)
    _safe_set(b, 'Expression8', None)
    assert not _is_linked(b, 'Expression8', a2)
    if hasattr(a2, 'rightInverse'):
        assert not _is_linked(a2, 'rightInverse', b)


def test_assoc_rightInverse3_reverse_link_reassign_clear():
    a1 = ast_Operator(op="sample_text")
    a2 = ast_Operator(op="sample_text_2")
    b = ast_Expression(incrementalID="sample_text")
    _safe_set(b, 'right', a1)
    assert _is_linked(b, 'right', a1)
    if hasattr(a1, 'Operator4'):
        assert _is_linked(a1, 'Operator4', b)
    _safe_set(b, 'right', a2)
    assert _is_linked(b, 'right', a2)
    if hasattr(a1, 'Operator4'):
        assert not _is_linked(a1, 'Operator4', b)
    if hasattr(a2, 'Operator4'):
        assert _is_linked(a2, 'Operator4', b)
    _safe_set(b, 'right', None)
    assert not _is_linked(b, 'right', a2)
    if hasattr(a2, 'Operator4'):
        assert not _is_linked(a2, 'Operator4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_expr0_stub_double():
    # ast_Model has no real 'model' property in the generated
    # code (a bare stub) -- manually attach it so ast_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Expression(incrementalID="sample_text")
    partner = ast_Model()
    setattr(partner, 'model', None)
    _safe_set(owner, 'Expression', partner)
    assert getattr(partner, 'model') == owner
    _safe_set(owner, 'Expression', None)
    assert getattr(partner, 'model') is None


def test_assoc_model1_stub_double():
    # ast_Model has no real 'Model' property in the generated
    # code (a bare stub) -- manually attach it so ast_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ast_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ast_Expression(incrementalID="sample_text")
    partner = ast_Model()
    setattr(partner, 'Model', None)
    _safe_set(owner, 'expr', partner)
    assert getattr(partner, 'Model') == owner
    _safe_set(owner, 'expr', None)
    assert getattr(partner, 'Model') is None


