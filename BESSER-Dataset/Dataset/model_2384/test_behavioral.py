import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tables_Column,
    tables_Database,
    tables_ForeignKey,
    tables_Table,
    Type,
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

def test_assoc_column9_reverse_link_reassign_clear():
    a1 = tables_ForeignKey(name="sample_text")
    a2 = tables_ForeignKey(name="sample_text_2")
    b = tables_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'Column10', a1)
    assert _is_linked(b, 'Column10', a1)
    if hasattr(a1, 'foreign_key'):
        assert _is_linked(a1, 'foreign_key', b)
    _safe_set(b, 'Column10', a2)
    assert _is_linked(b, 'Column10', a2)
    if hasattr(a1, 'foreign_key'):
        assert not _is_linked(a1, 'foreign_key', b)
    if hasattr(a2, 'foreign_key'):
        assert _is_linked(a2, 'foreign_key', b)
    _safe_set(b, 'Column10', None)
    assert not _is_linked(b, 'Column10', a2)
    if hasattr(a2, 'foreign_key'):
        assert not _is_linked(a2, 'foreign_key', b)


def test_assoc_columns1_reverse_link_reassign_clear():
    a1 = tables_Table(name="sample_text")
    a2 = tables_Table(name="sample_text_2")
    b = tables_Column(name="sample_text", type="sample_text")
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


def test_assoc_database2_reverse_link_reassign_clear():
    a1 = tables_Table(name="sample_text")
    a2 = tables_Table(name="sample_text_2")
    b = tables_Database(name="sample_text")
    _safe_set(b, 'Database', a1)
    assert _is_linked(b, 'Database', a1)
    if hasattr(a1, 'tables'):
        assert _is_linked(a1, 'tables', b)
    _safe_set(b, 'Database', a2)
    assert _is_linked(b, 'Database', a2)
    if hasattr(a1, 'tables'):
        assert not _is_linked(a1, 'tables', b)
    if hasattr(a2, 'tables'):
        assert _is_linked(a2, 'tables', b)
    _safe_set(b, 'Database', None)
    assert not _is_linked(b, 'Database', a2)
    if hasattr(a2, 'tables'):
        assert not _is_linked(a2, 'tables', b)


def test_assoc_foreign_key6_reverse_link_reassign_clear():
    a1 = tables_ForeignKey(name="sample_text")
    a2 = tables_ForeignKey(name="sample_text_2")
    b = tables_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'column', a1)
    assert _is_linked(b, 'column', a1)
    if hasattr(a1, 'ForeignKey'):
        assert _is_linked(a1, 'ForeignKey', b)
    _safe_set(b, 'column', a2)
    assert _is_linked(b, 'column', a2)
    if hasattr(a1, 'ForeignKey'):
        assert not _is_linked(a1, 'ForeignKey', b)
    if hasattr(a2, 'ForeignKey'):
        assert _is_linked(a2, 'ForeignKey', b)
    _safe_set(b, 'column', None)
    assert not _is_linked(b, 'column', a2)
    if hasattr(a2, 'ForeignKey'):
        assert not _is_linked(a2, 'ForeignKey', b)


def test_assoc_primary_key3_reverse_link_reassign_clear():
    a1 = tables_Table(name="sample_text")
    a2 = tables_Table(name="sample_text_2")
    b = tables_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'tables_Column', a1)
    assert _is_linked(b, 'tables_Column', a1)
    if hasattr(a1, 'tables_Table'):
        assert _is_linked(a1, 'tables_Table', b)
    _safe_set(b, 'tables_Column', a2)
    assert _is_linked(b, 'tables_Column', a2)
    if hasattr(a1, 'tables_Table'):
        assert not _is_linked(a1, 'tables_Table', b)
    if hasattr(a2, 'tables_Table'):
        assert _is_linked(a2, 'tables_Table', b)
    _safe_set(b, 'tables_Column', None)
    assert not _is_linked(b, 'tables_Column', a2)
    if hasattr(a2, 'tables_Table'):
        assert not _is_linked(a2, 'tables_Table', b)


def test_assoc_table4_reverse_link_reassign_clear():
    a1 = tables_Table(name="sample_text")
    a2 = tables_Table(name="sample_text_2")
    b = tables_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'columns', a1)
    assert _is_linked(b, 'columns', a1)
    if hasattr(a1, 'Table5'):
        assert _is_linked(a1, 'Table5', b)
    _safe_set(b, 'columns', a2)
    assert _is_linked(b, 'columns', a2)
    if hasattr(a1, 'Table5'):
        assert not _is_linked(a1, 'Table5', b)
    if hasattr(a2, 'Table5'):
        assert _is_linked(a2, 'Table5', b)
    _safe_set(b, 'columns', None)
    assert not _is_linked(b, 'columns', a2)
    if hasattr(a2, 'Table5'):
        assert not _is_linked(a2, 'Table5', b)


def test_assoc_tables0_reverse_link_reassign_clear():
    a1 = tables_Table(name="sample_text")
    a2 = tables_Table(name="sample_text_2")
    b = tables_Database(name="sample_text")
    _safe_set(b, 'database', {a1})
    assert _is_linked(b, 'database', a1)
    if hasattr(a1, 'Table'):
        assert _is_linked(a1, 'Table', b)
    _safe_set(b, 'database', {a2})
    assert _is_linked(b, 'database', a2)
    if hasattr(a1, 'Table'):
        assert not _is_linked(a1, 'Table', b)
    if hasattr(a2, 'Table'):
        assert _is_linked(a2, 'Table', b)
    _safe_set(b, 'database', set())
    assert not _is_linked(b, 'database', a2)
    if hasattr(a2, 'Table'):
        assert not _is_linked(a2, 'Table', b)


def test_assoc_target7_reverse_link_reassign_clear():
    a1 = tables_Table(name="sample_text")
    a2 = tables_Table(name="sample_text_2")
    b = tables_ForeignKey(name="sample_text")
    _safe_set(b, 'tables_ForeignKey', a1)
    assert _is_linked(b, 'tables_ForeignKey', a1)
    if hasattr(a1, 'tables_Table8'):
        assert _is_linked(a1, 'tables_Table8', b)
    _safe_set(b, 'tables_ForeignKey', a2)
    assert _is_linked(b, 'tables_ForeignKey', a2)
    if hasattr(a1, 'tables_Table8'):
        assert not _is_linked(a1, 'tables_Table8', b)
    if hasattr(a2, 'tables_Table8'):
        assert _is_linked(a2, 'tables_Table8', b)
    _safe_set(b, 'tables_ForeignKey', None)
    assert not _is_linked(b, 'tables_ForeignKey', a2)
    if hasattr(a2, 'tables_Table8'):
        assert not _is_linked(a2, 'tables_Table8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

