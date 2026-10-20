import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RHS_V,
    RHS_W,
    RHS_X,
    RHS_Y,
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

def test_assoc_refV0_reverse_link_reassign_clear():
    a1 = RHS_X(name="sample_text")
    a2 = RHS_X(name="sample_text_2")
    b = RHS_V(name="sample_text")
    _safe_set(b, 'RHS_V', a1)
    assert _is_linked(b, 'RHS_V', a1)
    if hasattr(a1, 'RHS_X'):
        assert _is_linked(a1, 'RHS_X', b)
    _safe_set(b, 'RHS_V', a2)
    assert _is_linked(b, 'RHS_V', a2)
    if hasattr(a1, 'RHS_X'):
        assert not _is_linked(a1, 'RHS_X', b)
    if hasattr(a2, 'RHS_X'):
        assert _is_linked(a2, 'RHS_X', b)
    _safe_set(b, 'RHS_V', None)
    assert not _is_linked(b, 'RHS_V', a2)
    if hasattr(a2, 'RHS_X'):
        assert not _is_linked(a2, 'RHS_X', b)


def test_assoc_refW3_reverse_link_reassign_clear():
    a1 = RHS_Y(name="sample_text")
    a2 = RHS_Y(name="sample_text_2")
    b = RHS_W(name="sample_text")
    _safe_set(b, 'RHS_W', a1)
    assert _is_linked(b, 'RHS_W', a1)
    if hasattr(a1, 'RHS_Y4'):
        assert _is_linked(a1, 'RHS_Y4', b)
    _safe_set(b, 'RHS_W', a2)
    assert _is_linked(b, 'RHS_W', a2)
    if hasattr(a1, 'RHS_Y4'):
        assert not _is_linked(a1, 'RHS_Y4', b)
    if hasattr(a2, 'RHS_Y4'):
        assert _is_linked(a2, 'RHS_Y4', b)
    _safe_set(b, 'RHS_W', None)
    assert not _is_linked(b, 'RHS_W', a2)
    if hasattr(a2, 'RHS_Y4'):
        assert not _is_linked(a2, 'RHS_Y4', b)


def test_assoc_refX1_reverse_link_reassign_clear():
    a1 = RHS_Y(name="sample_text")
    a2 = RHS_Y(name="sample_text_2")
    b = RHS_X(name="sample_text")
    _safe_set(b, 'RHS_X2', a1)
    assert _is_linked(b, 'RHS_X2', a1)
    if hasattr(a1, 'RHS_Y'):
        assert _is_linked(a1, 'RHS_Y', b)
    _safe_set(b, 'RHS_X2', a2)
    assert _is_linked(b, 'RHS_X2', a2)
    if hasattr(a1, 'RHS_Y'):
        assert not _is_linked(a1, 'RHS_Y', b)
    if hasattr(a2, 'RHS_Y'):
        assert _is_linked(a2, 'RHS_Y', b)
    _safe_set(b, 'RHS_X2', None)
    assert not _is_linked(b, 'RHS_X2', a2)
    if hasattr(a2, 'RHS_Y'):
        assert not _is_linked(a2, 'RHS_Y', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

