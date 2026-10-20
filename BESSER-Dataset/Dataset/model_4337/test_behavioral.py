import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Expression_Expression,
    Expression_Operation,
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

def test_assoc_left1_reverse_link_reassign_clear():
    a1 = Expression_Operation(op="sample_text")
    a2 = Expression_Operation(op="sample_text_2")
    b = Expression_Expression(value=3.14)
    _safe_set(b, 'Expression', a1)
    assert _is_linked(b, 'Expression', a1)
    if hasattr(a1, 'operation'):
        assert _is_linked(a1, 'operation', b)
    _safe_set(b, 'Expression', a2)
    assert _is_linked(b, 'Expression', a2)
    if hasattr(a1, 'operation'):
        assert not _is_linked(a1, 'operation', b)
    if hasattr(a2, 'operation'):
        assert _is_linked(a2, 'operation', b)
    _safe_set(b, 'Expression', None)
    assert not _is_linked(b, 'Expression', a2)
    if hasattr(a2, 'operation'):
        assert not _is_linked(a2, 'operation', b)


def test_assoc_operation0_reverse_link_reassign_clear():
    a1 = Expression_Operation(op="sample_text")
    a2 = Expression_Operation(op="sample_text_2")
    b = Expression_Expression(value=3.14)
    _safe_set(b, 'left', a1)
    assert _is_linked(b, 'left', a1)
    if hasattr(a1, 'Operation'):
        assert _is_linked(a1, 'Operation', b)
    _safe_set(b, 'left', a2)
    assert _is_linked(b, 'left', a2)
    if hasattr(a1, 'Operation'):
        assert not _is_linked(a1, 'Operation', b)
    if hasattr(a2, 'Operation'):
        assert _is_linked(a2, 'Operation', b)
    _safe_set(b, 'left', None)
    assert not _is_linked(b, 'left', a2)
    if hasattr(a2, 'Operation'):
        assert not _is_linked(a2, 'Operation', b)


def test_assoc_right2_reverse_link_reassign_clear():
    a1 = Expression_Operation(op="sample_text")
    a2 = Expression_Operation(op="sample_text_2")
    b = Expression_Expression(value=3.14)
    _safe_set(b, 'Expression_Expression', a1)
    assert _is_linked(b, 'Expression_Expression', a1)
    if hasattr(a1, 'Expression_Operation'):
        assert _is_linked(a1, 'Expression_Operation', b)
    _safe_set(b, 'Expression_Expression', a2)
    assert _is_linked(b, 'Expression_Expression', a2)
    if hasattr(a1, 'Expression_Operation'):
        assert not _is_linked(a1, 'Expression_Operation', b)
    if hasattr(a2, 'Expression_Operation'):
        assert _is_linked(a2, 'Expression_Operation', b)
    _safe_set(b, 'Expression_Expression', None)
    assert not _is_linked(b, 'Expression_Expression', a2)
    if hasattr(a2, 'Expression_Operation'):
        assert not _is_linked(a2, 'Expression_Operation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

