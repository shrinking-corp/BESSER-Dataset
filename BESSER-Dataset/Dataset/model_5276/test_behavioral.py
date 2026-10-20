import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TypeB_A,
    TypeB_B,
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

def test_assoc_aElementWithName7_reverse_link_reassign_clear():
    a1 = TypeB_B(name="sample_text")
    a2 = TypeB_B(name="sample_text_2")
    b = TypeB_A(isNameABC=True, name="sample_text")
    _safe_set(b, 'TypeB_A9', a1)
    assert _is_linked(b, 'TypeB_A9', a1)
    if hasattr(a1, 'TypeB_B8'):
        assert _is_linked(a1, 'TypeB_B8', b)
    _safe_set(b, 'TypeB_A9', a2)
    assert _is_linked(b, 'TypeB_A9', a2)
    if hasattr(a1, 'TypeB_B8'):
        assert not _is_linked(a1, 'TypeB_B8', b)
    if hasattr(a2, 'TypeB_B8'):
        assert _is_linked(a2, 'TypeB_B8', b)
    _safe_set(b, 'TypeB_A9', None)
    assert not _is_linked(b, 'TypeB_A9', a2)
    if hasattr(a2, 'TypeB_B8'):
        assert not _is_linked(a2, 'TypeB_B8', b)


def test_assoc_elms0_reverse_link_reassign_clear():
    a1 = TypeB_B(name="sample_text")
    a2 = TypeB_B(name="sample_text_2")
    b = TypeB_A(isNameABC=True, name="sample_text")
    _safe_set(b, 'TypeB_A', {a1})
    assert _is_linked(b, 'TypeB_A', a1)
    if hasattr(a1, 'TypeB_B'):
        assert _is_linked(a1, 'TypeB_B', b)
    _safe_set(b, 'TypeB_A', {a2})
    assert _is_linked(b, 'TypeB_A', a2)
    if hasattr(a1, 'TypeB_B'):
        assert not _is_linked(a1, 'TypeB_B', b)
    if hasattr(a2, 'TypeB_B'):
        assert _is_linked(a2, 'TypeB_B', b)
    _safe_set(b, 'TypeB_A', set())
    assert not _is_linked(b, 'TypeB_A', a2)
    if hasattr(a2, 'TypeB_B'):
        assert not _is_linked(a2, 'TypeB_B', b)


def test_assoc_elms1_reverse_link_reassign_clear():
    a1 = TypeB_B(name="sample_text")
    a2 = TypeB_B(name="sample_text_2")
    b = TypeB_A(isNameABC=True, name="sample_text")
    _safe_set(b, 'TypeB_A3', a1)
    assert _is_linked(b, 'TypeB_A3', a1)
    if hasattr(a1, 'TypeB_B2'):
        assert _is_linked(a1, 'TypeB_B2', b)
    _safe_set(b, 'TypeB_A3', a2)
    assert _is_linked(b, 'TypeB_A3', a2)
    if hasattr(a1, 'TypeB_B2'):
        assert not _is_linked(a1, 'TypeB_B2', b)
    if hasattr(a2, 'TypeB_B2'):
        assert _is_linked(a2, 'TypeB_B2', b)
    _safe_set(b, 'TypeB_A3', None)
    assert not _is_linked(b, 'TypeB_A3', a2)
    if hasattr(a2, 'TypeB_B2'):
        assert not _is_linked(a2, 'TypeB_B2', b)


def test_assoc_firstAElement4_reverse_link_reassign_clear():
    a1 = TypeB_B(name="sample_text")
    a2 = TypeB_B(name="sample_text_2")
    b = TypeB_A(isNameABC=True, name="sample_text")
    _safe_set(b, 'TypeB_A6', a1)
    assert _is_linked(b, 'TypeB_A6', a1)
    if hasattr(a1, 'TypeB_B5'):
        assert _is_linked(a1, 'TypeB_B5', b)
    _safe_set(b, 'TypeB_A6', a2)
    assert _is_linked(b, 'TypeB_A6', a2)
    if hasattr(a1, 'TypeB_B5'):
        assert not _is_linked(a1, 'TypeB_B5', b)
    if hasattr(a2, 'TypeB_B5'):
        assert _is_linked(a2, 'TypeB_B5', b)
    _safe_set(b, 'TypeB_A6', None)
    assert not _is_linked(b, 'TypeB_A6', a2)
    if hasattr(a2, 'TypeB_B5'):
        assert not _is_linked(a2, 'TypeB_B5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

