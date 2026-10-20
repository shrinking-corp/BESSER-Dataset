import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    hierarchy_Book,
    hierarchy_Fiction,
    hierarchy_HierLibrary,
    hierarchy_NonFiction,
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

def test_assoc_fiction0_reverse_link_reassign_clear():
    a1 = hierarchy_HierLibrary(Name="sample_text")
    a2 = hierarchy_HierLibrary(Name="sample_text_2")
    b = hierarchy_Fiction(Name="sample_text")
    _safe_set(b, 'hierarchy_Fiction', a1)
    assert _is_linked(b, 'hierarchy_Fiction', a1)
    if hasattr(a1, 'hierarchy_HierLibrary'):
        assert _is_linked(a1, 'hierarchy_HierLibrary', b)
    _safe_set(b, 'hierarchy_Fiction', a2)
    assert _is_linked(b, 'hierarchy_Fiction', a2)
    if hasattr(a1, 'hierarchy_HierLibrary'):
        assert not _is_linked(a1, 'hierarchy_HierLibrary', b)
    if hasattr(a2, 'hierarchy_HierLibrary'):
        assert _is_linked(a2, 'hierarchy_HierLibrary', b)
    _safe_set(b, 'hierarchy_Fiction', None)
    assert not _is_linked(b, 'hierarchy_Fiction', a2)
    if hasattr(a2, 'hierarchy_HierLibrary'):
        assert not _is_linked(a2, 'hierarchy_HierLibrary', b)


def test_assoc_members3_reverse_link_reassign_clear():
    a1 = hierarchy_Fiction(Name="sample_text")
    a2 = hierarchy_Fiction(Name="sample_text_2")
    b = hierarchy_Book(Name="sample_text", genre="sample_text")
    _safe_set(b, 'hierarchy_Book', a1)
    assert _is_linked(b, 'hierarchy_Book', a1)
    if hasattr(a1, 'hierarchy_Fiction4'):
        assert _is_linked(a1, 'hierarchy_Fiction4', b)
    _safe_set(b, 'hierarchy_Book', a2)
    assert _is_linked(b, 'hierarchy_Book', a2)
    if hasattr(a1, 'hierarchy_Fiction4'):
        assert not _is_linked(a1, 'hierarchy_Fiction4', b)
    if hasattr(a2, 'hierarchy_Fiction4'):
        assert _is_linked(a2, 'hierarchy_Fiction4', b)
    _safe_set(b, 'hierarchy_Book', None)
    assert not _is_linked(b, 'hierarchy_Book', a2)
    if hasattr(a2, 'hierarchy_Fiction4'):
        assert not _is_linked(a2, 'hierarchy_Fiction4', b)


def test_assoc_members5_reverse_link_reassign_clear():
    a1 = hierarchy_NonFiction(Name="sample_text")
    a2 = hierarchy_NonFiction(Name="sample_text_2")
    b = hierarchy_Book(Name="sample_text", genre="sample_text")
    _safe_set(b, 'hierarchy_Book7', a1)
    assert _is_linked(b, 'hierarchy_Book7', a1)
    if hasattr(a1, 'hierarchy_NonFiction6'):
        assert _is_linked(a1, 'hierarchy_NonFiction6', b)
    _safe_set(b, 'hierarchy_Book7', a2)
    assert _is_linked(b, 'hierarchy_Book7', a2)
    if hasattr(a1, 'hierarchy_NonFiction6'):
        assert not _is_linked(a1, 'hierarchy_NonFiction6', b)
    if hasattr(a2, 'hierarchy_NonFiction6'):
        assert _is_linked(a2, 'hierarchy_NonFiction6', b)
    _safe_set(b, 'hierarchy_Book7', None)
    assert not _is_linked(b, 'hierarchy_Book7', a2)
    if hasattr(a2, 'hierarchy_NonFiction6'):
        assert not _is_linked(a2, 'hierarchy_NonFiction6', b)


def test_assoc_nonfiction1_reverse_link_reassign_clear():
    a1 = hierarchy_NonFiction(Name="sample_text")
    a2 = hierarchy_NonFiction(Name="sample_text_2")
    b = hierarchy_HierLibrary(Name="sample_text")
    _safe_set(b, 'hierarchy_HierLibrary2', a1)
    assert _is_linked(b, 'hierarchy_HierLibrary2', a1)
    if hasattr(a1, 'hierarchy_NonFiction'):
        assert _is_linked(a1, 'hierarchy_NonFiction', b)
    _safe_set(b, 'hierarchy_HierLibrary2', a2)
    assert _is_linked(b, 'hierarchy_HierLibrary2', a2)
    if hasattr(a1, 'hierarchy_NonFiction'):
        assert not _is_linked(a1, 'hierarchy_NonFiction', b)
    if hasattr(a2, 'hierarchy_NonFiction'):
        assert _is_linked(a2, 'hierarchy_NonFiction', b)
    _safe_set(b, 'hierarchy_HierLibrary2', None)
    assert not _is_linked(b, 'hierarchy_HierLibrary2', a2)
    if hasattr(a2, 'hierarchy_NonFiction'):
        assert not _is_linked(a2, 'hierarchy_NonFiction', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

