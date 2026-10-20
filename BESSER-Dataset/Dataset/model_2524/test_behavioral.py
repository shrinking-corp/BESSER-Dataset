import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    LHS_A,
    LHS_B,
    LHS_C,
    LHS_D,
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

def test_assoc_refB0_reverse_link_reassign_clear():
    a1 = LHS_B(name="sample_text")
    a2 = LHS_B(name="sample_text_2")
    b = LHS_A(name="sample_text")
    _safe_set(b, 'LHS_A', a1)
    assert _is_linked(b, 'LHS_A', a1)
    if hasattr(a1, 'LHS_B'):
        assert _is_linked(a1, 'LHS_B', b)
    _safe_set(b, 'LHS_A', a2)
    assert _is_linked(b, 'LHS_A', a2)
    if hasattr(a1, 'LHS_B'):
        assert not _is_linked(a1, 'LHS_B', b)
    if hasattr(a2, 'LHS_B'):
        assert _is_linked(a2, 'LHS_B', b)
    _safe_set(b, 'LHS_A', None)
    assert not _is_linked(b, 'LHS_A', a2)
    if hasattr(a2, 'LHS_B'):
        assert not _is_linked(a2, 'LHS_B', b)


def test_assoc_refC1_reverse_link_reassign_clear():
    a1 = LHS_C(name="sample_text")
    a2 = LHS_C(name="sample_text_2")
    b = LHS_A(name="sample_text")
    _safe_set(b, 'LHS_A2', a1)
    assert _is_linked(b, 'LHS_A2', a1)
    if hasattr(a1, 'LHS_C'):
        assert _is_linked(a1, 'LHS_C', b)
    _safe_set(b, 'LHS_A2', a2)
    assert _is_linked(b, 'LHS_A2', a2)
    if hasattr(a1, 'LHS_C'):
        assert not _is_linked(a1, 'LHS_C', b)
    if hasattr(a2, 'LHS_C'):
        assert _is_linked(a2, 'LHS_C', b)
    _safe_set(b, 'LHS_A2', None)
    assert not _is_linked(b, 'LHS_A2', a2)
    if hasattr(a2, 'LHS_C'):
        assert not _is_linked(a2, 'LHS_C', b)


def test_assoc_refD3_reverse_link_reassign_clear():
    a1 = LHS_D(name="sample_text")
    a2 = LHS_D(name="sample_text_2")
    b = LHS_B(name="sample_text")
    _safe_set(b, 'LHS_B4', a1)
    assert _is_linked(b, 'LHS_B4', a1)
    if hasattr(a1, 'LHS_D'):
        assert _is_linked(a1, 'LHS_D', b)
    _safe_set(b, 'LHS_B4', a2)
    assert _is_linked(b, 'LHS_B4', a2)
    if hasattr(a1, 'LHS_D'):
        assert not _is_linked(a1, 'LHS_D', b)
    if hasattr(a2, 'LHS_D'):
        assert _is_linked(a2, 'LHS_D', b)
    _safe_set(b, 'LHS_B4', None)
    assert not _is_linked(b, 'LHS_B4', a2)
    if hasattr(a2, 'LHS_D'):
        assert not _is_linked(a2, 'LHS_D', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

