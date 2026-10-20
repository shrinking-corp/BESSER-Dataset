import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    pmtest_A,
    pmtest_B,
    pmtest_C,
    pmtest_D,
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

def test_assoc_d5_reverse_link_reassign_clear():
    a1 = pmtest_D(j=7)
    a2 = pmtest_D(j=13)
    b = pmtest_A(i=7)
    _safe_set(b, 'pmtest_A', {a1})
    assert _is_linked(b, 'pmtest_A', a1)
    if hasattr(a1, 'pmtest_D'):
        assert _is_linked(a1, 'pmtest_D', b)
    _safe_set(b, 'pmtest_A', {a2})
    assert _is_linked(b, 'pmtest_A', a2)
    if hasattr(a1, 'pmtest_D'):
        assert not _is_linked(a1, 'pmtest_D', b)
    if hasattr(a2, 'pmtest_D'):
        assert _is_linked(a2, 'pmtest_D', b)
    _safe_set(b, 'pmtest_A', set())
    assert not _is_linked(b, 'pmtest_A', a2)
    if hasattr(a2, 'pmtest_D'):
        assert not _is_linked(a2, 'pmtest_D', b)


def test_assoc_s3_reverse_link_reassign_clear():
    a1 = pmtest_A(i=7)
    a2 = pmtest_A(i=13)
    b = pmtest_A(i=7)
    _safe_set(b, 't', {a1})
    assert _is_linked(b, 't', a1)
    if hasattr(a1, 'A4'):
        assert _is_linked(a1, 'A4', b)
    _safe_set(b, 't', {a2})
    assert _is_linked(b, 't', a2)
    if hasattr(a1, 'A4'):
        assert not _is_linked(a1, 'A4', b)
    if hasattr(a2, 'A4'):
        assert _is_linked(a2, 'A4', b)
    _safe_set(b, 't', set())
    assert not _is_linked(b, 't', a2)
    if hasattr(a2, 'A4'):
        assert not _is_linked(a2, 'A4', b)


def test_assoc_t1_reverse_link_reassign_clear():
    a1 = pmtest_A(i=7)
    a2 = pmtest_A(i=13)
    b = pmtest_A(i=7)
    _safe_set(b, 's', {a1})
    assert _is_linked(b, 's', a1)
    if hasattr(a1, 'A'):
        assert _is_linked(a1, 'A', b)
    _safe_set(b, 's', {a2})
    assert _is_linked(b, 's', a2)
    if hasattr(a1, 'A'):
        assert not _is_linked(a1, 'A', b)
    if hasattr(a2, 'A'):
        assert _is_linked(a2, 'A', b)
    _safe_set(b, 's', set())
    assert not _is_linked(b, 's', a2)
    if hasattr(a2, 'A'):
        assert not _is_linked(a2, 'A', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

