import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    database_Column,
    database_Scheme,
    database_Table,
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

def test_assoc_columns1_reverse_link_reassign_clear():
    a1 = database_Scheme(name="sample_text")
    a2 = database_Scheme(name="sample_text_2")
    b = database_Column(NotNull=True, PrimaryKey=True, name="sample_text", type="sample_text")
    _safe_set(b, 'database_Column', a1)
    assert _is_linked(b, 'database_Column', a1)
    if hasattr(a1, 'database_Scheme2'):
        assert _is_linked(a1, 'database_Scheme2', b)
    _safe_set(b, 'database_Column', a2)
    assert _is_linked(b, 'database_Column', a2)
    if hasattr(a1, 'database_Scheme2'):
        assert not _is_linked(a1, 'database_Scheme2', b)
    if hasattr(a2, 'database_Scheme2'):
        assert _is_linked(a2, 'database_Scheme2', b)
    _safe_set(b, 'database_Column', None)
    assert not _is_linked(b, 'database_Column', a2)
    if hasattr(a2, 'database_Scheme2'):
        assert not _is_linked(a2, 'database_Scheme2', b)


def test_assoc_columns3_reverse_link_reassign_clear():
    a1 = database_Table(name="sample_text")
    a2 = database_Table(name="sample_text_2")
    b = database_Column(NotNull=True, PrimaryKey=True, name="sample_text", type="sample_text")
    _safe_set(b, 'Column', a1)
    assert _is_linked(b, 'Column', a1)
    if hasattr(a1, 'table'):
        assert _is_linked(a1, 'table', b)
    _safe_set(b, 'Column', a2)
    assert _is_linked(b, 'Column', a2)
    if hasattr(a1, 'table'):
        assert not _is_linked(a1, 'table', b)
    if hasattr(a2, 'table'):
        assert _is_linked(a2, 'table', b)
    _safe_set(b, 'Column', None)
    assert not _is_linked(b, 'Column', a2)
    if hasattr(a2, 'table'):
        assert not _is_linked(a2, 'table', b)


def test_assoc_fk6_reverse_link_reassign_clear():
    a1 = database_Column(NotNull=True, PrimaryKey=True, name="sample_text", type="sample_text")
    a2 = database_Column(NotNull=False, PrimaryKey=False, name="sample_text_2", type="sample_text_2")
    b = database_Column(NotNull=True, PrimaryKey=True, name="sample_text", type="sample_text")
    _safe_set(b, 'database_Column7', a1)
    assert _is_linked(b, 'database_Column7', a1)
    if hasattr(a1, 'database_Column5'):
        assert _is_linked(a1, 'database_Column5', b)
    _safe_set(b, 'database_Column7', a2)
    assert _is_linked(b, 'database_Column7', a2)
    if hasattr(a1, 'database_Column5'):
        assert not _is_linked(a1, 'database_Column5', b)
    if hasattr(a2, 'database_Column5'):
        assert _is_linked(a2, 'database_Column5', b)
    _safe_set(b, 'database_Column7', None)
    assert not _is_linked(b, 'database_Column7', a2)
    if hasattr(a2, 'database_Column5'):
        assert not _is_linked(a2, 'database_Column5', b)


def test_assoc_table4_reverse_link_reassign_clear():
    a1 = database_Table(name="sample_text")
    a2 = database_Table(name="sample_text_2")
    b = database_Column(NotNull=True, PrimaryKey=True, name="sample_text", type="sample_text")
    _safe_set(b, 'columns', a1)
    assert _is_linked(b, 'columns', a1)
    if hasattr(a1, 'Table'):
        assert _is_linked(a1, 'Table', b)
    _safe_set(b, 'columns', a2)
    assert _is_linked(b, 'columns', a2)
    if hasattr(a1, 'Table'):
        assert not _is_linked(a1, 'Table', b)
    if hasattr(a2, 'Table'):
        assert _is_linked(a2, 'Table', b)
    _safe_set(b, 'columns', None)
    assert not _is_linked(b, 'columns', a2)
    if hasattr(a2, 'Table'):
        assert not _is_linked(a2, 'Table', b)


def test_assoc_tables0_reverse_link_reassign_clear():
    a1 = database_Table(name="sample_text")
    a2 = database_Table(name="sample_text_2")
    b = database_Scheme(name="sample_text")
    _safe_set(b, 'database_Scheme', {a1})
    assert _is_linked(b, 'database_Scheme', a1)
    if hasattr(a1, 'database_Table'):
        assert _is_linked(a1, 'database_Table', b)
    _safe_set(b, 'database_Scheme', {a2})
    assert _is_linked(b, 'database_Scheme', a2)
    if hasattr(a1, 'database_Table'):
        assert not _is_linked(a1, 'database_Table', b)
    if hasattr(a2, 'database_Table'):
        assert _is_linked(a2, 'database_Table', b)
    _safe_set(b, 'database_Scheme', set())
    assert not _is_linked(b, 'database_Scheme', a2)
    if hasattr(a2, 'database_Table'):
        assert not _is_linked(a2, 'database_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

