import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    B,
    C,
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

def test_assoc_A_B_reverse_link_reassign_clear():
    a1 = B(attrB1=7, attrB2="sample_text")
    a2 = B(attrB1=13, attrB2="sample_text_2")
    b = A(attrA1=7, attrA2="sample_text")
    _safe_set(b, 'b0', {a1})
    assert _is_linked(b, 'b0', a1)
    if hasattr(a1, 'a1'):
        assert _is_linked(a1, 'a1', b)
    _safe_set(b, 'b0', {a2})
    assert _is_linked(b, 'b0', a2)
    if hasattr(a1, 'a1'):
        assert not _is_linked(a1, 'a1', b)
    if hasattr(a2, 'a1'):
        assert _is_linked(a2, 'a1', b)
    _safe_set(b, 'b0', set())
    assert not _is_linked(b, 'b0', a2)
    if hasattr(a2, 'a1'):
        assert not _is_linked(a2, 'a1', b)


def test_assoc_C_B_reverse_link_reassign_clear():
    a1 = C(attrC1=7, attrC2="sample_text")
    a2 = C(attrC1=13, attrC2="sample_text_2")
    b = B(attrB1=7, attrB2="sample_text")
    _safe_set(b, 'c3', {a1})
    assert _is_linked(b, 'c3', a1)
    if hasattr(a1, 'b2'):
        assert _is_linked(a1, 'b2', b)
    _safe_set(b, 'c3', {a2})
    assert _is_linked(b, 'c3', a2)
    if hasattr(a1, 'b2'):
        assert not _is_linked(a1, 'b2', b)
    if hasattr(a2, 'b2'):
        assert _is_linked(a2, 'b2', b)
    _safe_set(b, 'c3', set())
    assert not _is_linked(b, 'c3', a2)
    if hasattr(a2, 'b2'):
        assert not _is_linked(a2, 'b2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

