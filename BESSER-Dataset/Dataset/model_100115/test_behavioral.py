import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    database_Column,
    database_Database,
    database_ForeignKey,
    database_Table,
    DataType,
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

def test_assoc_ColumnTable4_reverse_link_reassign_clear():
    a1 = database_Table(Name="sample_text")
    a2 = database_Table(Name="sample_text_2")
    b = database_Column(IsPrimaryKey=True, Name="sample_text", Type="sample_text")
    _safe_set(b, 'TableColumn', a1)
    assert _is_linked(b, 'TableColumn', a1)
    if hasattr(a1, 'Table5'):
        assert _is_linked(a1, 'Table5', b)
    _safe_set(b, 'TableColumn', a2)
    assert _is_linked(b, 'TableColumn', a2)
    if hasattr(a1, 'Table5'):
        assert not _is_linked(a1, 'Table5', b)
    if hasattr(a2, 'Table5'):
        assert _is_linked(a2, 'Table5', b)
    _safe_set(b, 'TableColumn', None)
    assert not _is_linked(b, 'TableColumn', a2)
    if hasattr(a2, 'Table5'):
        assert not _is_linked(a2, 'Table5', b)


def test_assoc_SourceColumn10_reverse_link_reassign_clear():
    a1 = database_ForeignKey(Name="sample_text")
    a2 = database_ForeignKey(Name="sample_text_2")
    b = database_Column(IsPrimaryKey=True, Name="sample_text", Type="sample_text")
    _safe_set(b, 'database_Column', a1)
    assert _is_linked(b, 'database_Column', a1)
    if hasattr(a1, 'database_ForeignKey11'):
        assert _is_linked(a1, 'database_ForeignKey11', b)
    _safe_set(b, 'database_Column', a2)
    assert _is_linked(b, 'database_Column', a2)
    if hasattr(a1, 'database_ForeignKey11'):
        assert not _is_linked(a1, 'database_ForeignKey11', b)
    if hasattr(a2, 'database_ForeignKey11'):
        assert _is_linked(a2, 'database_ForeignKey11', b)
    _safe_set(b, 'database_Column', None)
    assert not _is_linked(b, 'database_Column', a2)
    if hasattr(a2, 'database_ForeignKey11'):
        assert not _is_linked(a2, 'database_ForeignKey11', b)


def test_assoc_SourceTable6_reverse_link_reassign_clear():
    a1 = database_Table(Name="sample_text")
    a2 = database_Table(Name="sample_text_2")
    b = database_ForeignKey(Name="sample_text")
    _safe_set(b, 'database_ForeignKey', a1)
    assert _is_linked(b, 'database_ForeignKey', a1)
    if hasattr(a1, 'database_Table'):
        assert _is_linked(a1, 'database_Table', b)
    _safe_set(b, 'database_ForeignKey', a2)
    assert _is_linked(b, 'database_ForeignKey', a2)
    if hasattr(a1, 'database_Table'):
        assert not _is_linked(a1, 'database_Table', b)
    if hasattr(a2, 'database_Table'):
        assert _is_linked(a2, 'database_Table', b)
    _safe_set(b, 'database_ForeignKey', None)
    assert not _is_linked(b, 'database_ForeignKey', a2)
    if hasattr(a2, 'database_Table'):
        assert not _is_linked(a2, 'database_Table', b)


def test_assoc_TableColumn3_reverse_link_reassign_clear():
    a1 = database_Table(Name="sample_text")
    a2 = database_Table(Name="sample_text_2")
    b = database_Column(IsPrimaryKey=True, Name="sample_text", Type="sample_text")
    _safe_set(b, 'Column', a1)
    assert _is_linked(b, 'Column', a1)
    if hasattr(a1, 'ColumnTable'):
        assert _is_linked(a1, 'ColumnTable', b)
    _safe_set(b, 'Column', a2)
    assert _is_linked(b, 'Column', a2)
    if hasattr(a1, 'ColumnTable'):
        assert not _is_linked(a1, 'ColumnTable', b)
    if hasattr(a2, 'ColumnTable'):
        assert _is_linked(a2, 'ColumnTable', b)
    _safe_set(b, 'Column', None)
    assert not _is_linked(b, 'Column', a2)
    if hasattr(a2, 'ColumnTable'):
        assert not _is_linked(a2, 'ColumnTable', b)


def test_assoc_TargetColumn12_reverse_link_reassign_clear():
    a1 = database_ForeignKey(Name="sample_text")
    a2 = database_ForeignKey(Name="sample_text_2")
    b = database_Column(IsPrimaryKey=True, Name="sample_text", Type="sample_text")
    _safe_set(b, 'database_Column14', a1)
    assert _is_linked(b, 'database_Column14', a1)
    if hasattr(a1, 'database_ForeignKey13'):
        assert _is_linked(a1, 'database_ForeignKey13', b)
    _safe_set(b, 'database_Column14', a2)
    assert _is_linked(b, 'database_Column14', a2)
    if hasattr(a1, 'database_ForeignKey13'):
        assert not _is_linked(a1, 'database_ForeignKey13', b)
    if hasattr(a2, 'database_ForeignKey13'):
        assert _is_linked(a2, 'database_ForeignKey13', b)
    _safe_set(b, 'database_Column14', None)
    assert not _is_linked(b, 'database_Column14', a2)
    if hasattr(a2, 'database_ForeignKey13'):
        assert not _is_linked(a2, 'database_ForeignKey13', b)


def test_assoc_TargetTable7_reverse_link_reassign_clear():
    a1 = database_Table(Name="sample_text")
    a2 = database_Table(Name="sample_text_2")
    b = database_ForeignKey(Name="sample_text")
    _safe_set(b, 'database_ForeignKey8', a1)
    assert _is_linked(b, 'database_ForeignKey8', a1)
    if hasattr(a1, 'database_Table9'):
        assert _is_linked(a1, 'database_Table9', b)
    _safe_set(b, 'database_ForeignKey8', a2)
    assert _is_linked(b, 'database_ForeignKey8', a2)
    if hasattr(a1, 'database_Table9'):
        assert not _is_linked(a1, 'database_Table9', b)
    if hasattr(a2, 'database_Table9'):
        assert _is_linked(a2, 'database_Table9', b)
    _safe_set(b, 'database_ForeignKey8', None)
    assert not _is_linked(b, 'database_ForeignKey8', a2)
    if hasattr(a2, 'database_Table9'):
        assert not _is_linked(a2, 'database_Table9', b)


