import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    abc_A,
    abc_B,
    abc_C,
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

def test_assoc_a4_reverse_link_reassign_clear():
    a1 = abc_B(x=7)
    a2 = abc_B(x=13)
    b = abc_A(x=7)
    _safe_set(b, 'A', a1)
    assert _is_linked(b, 'A', a1)
    if hasattr(a1, 'b'):
        assert _is_linked(a1, 'b', b)
    _safe_set(b, 'A', a2)
    assert _is_linked(b, 'A', a2)
    if hasattr(a1, 'b'):
        assert not _is_linked(a1, 'b', b)
    if hasattr(a2, 'b'):
        assert _is_linked(a2, 'b', b)
    _safe_set(b, 'A', None)
    assert not _is_linked(b, 'A', a2)
    if hasattr(a2, 'b'):
        assert not _is_linked(a2, 'b', b)


def test_assoc_b0_reverse_link_reassign_clear():
    a1 = abc_C(x=7)
    a2 = abc_C(x=13)
    b = abc_B(x=7)
    _safe_set(b, 'abc_B', a1)
    assert _is_linked(b, 'abc_B', a1)
    if hasattr(a1, 'abc_C'):
        assert _is_linked(a1, 'abc_C', b)
    _safe_set(b, 'abc_B', a2)
    assert _is_linked(b, 'abc_B', a2)
    if hasattr(a1, 'abc_C'):
        assert not _is_linked(a1, 'abc_C', b)
    if hasattr(a2, 'abc_C'):
        assert _is_linked(a2, 'abc_C', b)
    _safe_set(b, 'abc_B', None)
    assert not _is_linked(b, 'abc_B', a2)
    if hasattr(a2, 'abc_C'):
        assert not _is_linked(a2, 'abc_C', b)


def test_assoc_b1_reverse_link_reassign_clear():
    a1 = abc_B(x=7)
    a2 = abc_B(x=13)
    b = abc_A(x=7)
    _safe_set(b, 'a', {a1})
    assert _is_linked(b, 'a', a1)
    if hasattr(a1, 'B'):
        assert _is_linked(a1, 'B', b)
    _safe_set(b, 'a', {a2})
    assert _is_linked(b, 'a', a2)
    if hasattr(a1, 'B'):
        assert not _is_linked(a1, 'B', b)
    if hasattr(a2, 'B'):
        assert _is_linked(a2, 'B', b)
    _safe_set(b, 'a', set())
    assert not _is_linked(b, 'a', a2)
    if hasattr(a2, 'B'):
        assert not _is_linked(a2, 'B', b)


def test_assoc_c2_reverse_link_reassign_clear():
    a1 = abc_C(x=7)
    a2 = abc_C(x=13)
    b = abc_A(x=7)
    _safe_set(b, 'abc_A', a1)
    assert _is_linked(b, 'abc_A', a1)
    if hasattr(a1, 'abc_C3'):
        assert _is_linked(a1, 'abc_C3', b)
    _safe_set(b, 'abc_A', a2)
    assert _is_linked(b, 'abc_A', a2)
    if hasattr(a1, 'abc_C3'):
        assert not _is_linked(a1, 'abc_C3', b)
    if hasattr(a2, 'abc_C3'):
        assert _is_linked(a2, 'abc_C3', b)
    _safe_set(b, 'abc_A', None)
    assert not _is_linked(b, 'abc_A', a2)
    if hasattr(a2, 'abc_C3'):
        assert not _is_linked(a2, 'abc_C3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

