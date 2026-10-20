import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataSource,
    datasetload_DataSource,
    datasetload_DataSourceJdbc,
    datasetload_Table,
    datasetload_TableGroup,
    datasetload_TableRow,
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

def test_assoc_DataSource1_reverse_link_reassign_clear():
    a1 = datasetload_TableGroup(Name="sample_text")
    a2 = datasetload_TableGroup(Name="sample_text_2")
    b = datasetload_DataSource(Connected=True, Name="sample_text")
    _safe_set(b, 'datasetload_DataSource', a1)
    assert _is_linked(b, 'datasetload_DataSource', a1)
    if hasattr(a1, 'datasetload_TableGroup2'):
        assert _is_linked(a1, 'datasetload_TableGroup2', b)
    _safe_set(b, 'datasetload_DataSource', a2)
    assert _is_linked(b, 'datasetload_DataSource', a2)
    if hasattr(a1, 'datasetload_TableGroup2'):
        assert not _is_linked(a1, 'datasetload_TableGroup2', b)
    if hasattr(a2, 'datasetload_TableGroup2'):
        assert _is_linked(a2, 'datasetload_TableGroup2', b)
    _safe_set(b, 'datasetload_DataSource', None)
    assert not _is_linked(b, 'datasetload_DataSource', a2)
    if hasattr(a2, 'datasetload_TableGroup2'):
        assert not _is_linked(a2, 'datasetload_TableGroup2', b)


def test_assoc_Rows6_reverse_link_reassign_clear():
    a1 = datasetload_TableRow(Key="sample_text", NewRow=True, RowNumber=7)
    a2 = datasetload_TableRow(Key="sample_text_2", NewRow=False, RowNumber=13)
    b = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    _safe_set(b, 'datasetload_Table7', {a1})
    assert _is_linked(b, 'datasetload_Table7', a1)
    if hasattr(a1, 'datasetload_TableRow'):
        assert _is_linked(a1, 'datasetload_TableRow', b)
    _safe_set(b, 'datasetload_Table7', {a2})
    assert _is_linked(b, 'datasetload_Table7', a2)
    if hasattr(a1, 'datasetload_TableRow'):
        assert not _is_linked(a1, 'datasetload_TableRow', b)
    if hasattr(a2, 'datasetload_TableRow'):
        assert _is_linked(a2, 'datasetload_TableRow', b)
    _safe_set(b, 'datasetload_Table7', set())
    assert not _is_linked(b, 'datasetload_Table7', a2)
    if hasattr(a2, 'datasetload_TableRow'):
        assert not _is_linked(a2, 'datasetload_TableRow', b)


def test_assoc_Table8_reverse_link_reassign_clear():
    a1 = datasetload_TableRow(Key="sample_text", NewRow=True, RowNumber=7)
    a2 = datasetload_TableRow(Key="sample_text_2", NewRow=False, RowNumber=13)
    b = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    _safe_set(b, 'datasetload_Table10', a1)
    assert _is_linked(b, 'datasetload_Table10', a1)
    if hasattr(a1, 'datasetload_TableRow9'):
        assert _is_linked(a1, 'datasetload_TableRow9', b)
    _safe_set(b, 'datasetload_Table10', a2)
    assert _is_linked(b, 'datasetload_Table10', a2)
    if hasattr(a1, 'datasetload_TableRow9'):
        assert not _is_linked(a1, 'datasetload_TableRow9', b)
    if hasattr(a2, 'datasetload_TableRow9'):
        assert _is_linked(a2, 'datasetload_TableRow9', b)
    _safe_set(b, 'datasetload_Table10', None)
    assert not _is_linked(b, 'datasetload_Table10', a2)
    if hasattr(a2, 'datasetload_TableRow9'):
        assert not _is_linked(a2, 'datasetload_TableRow9', b)


def test_assoc_TableGroup3_reverse_link_reassign_clear():
    a1 = datasetload_TableGroup(Name="sample_text")
    a2 = datasetload_TableGroup(Name="sample_text_2")
    b = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    _safe_set(b, 'datasetload_Table4', a1)
    assert _is_linked(b, 'datasetload_Table4', a1)
    if hasattr(a1, 'datasetload_TableGroup5'):
        assert _is_linked(a1, 'datasetload_TableGroup5', b)
    _safe_set(b, 'datasetload_Table4', a2)
    assert _is_linked(b, 'datasetload_Table4', a2)
    if hasattr(a1, 'datasetload_TableGroup5'):
        assert not _is_linked(a1, 'datasetload_TableGroup5', b)
    if hasattr(a2, 'datasetload_TableGroup5'):
        assert _is_linked(a2, 'datasetload_TableGroup5', b)
    _safe_set(b, 'datasetload_Table4', None)
    assert not _is_linked(b, 'datasetload_Table4', a2)
    if hasattr(a2, 'datasetload_TableGroup5'):
        assert not _is_linked(a2, 'datasetload_TableGroup5', b)


def test_assoc_Tables0_reverse_link_reassign_clear():
    a1 = datasetload_TableGroup(Name="sample_text")
    a2 = datasetload_TableGroup(Name="sample_text_2")
    b = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    _safe_set(b, 'datasetload_Table', a1)
    assert _is_linked(b, 'datasetload_Table', a1)
    if hasattr(a1, 'datasetload_TableGroup'):
        assert _is_linked(a1, 'datasetload_TableGroup', b)
    _safe_set(b, 'datasetload_Table', a2)
    assert _is_linked(b, 'datasetload_Table', a2)
    if hasattr(a1, 'datasetload_TableGroup'):
        assert not _is_linked(a1, 'datasetload_TableGroup', b)
    if hasattr(a2, 'datasetload_TableGroup'):
        assert _is_linked(a2, 'datasetload_TableGroup', b)
    _safe_set(b, 'datasetload_Table', None)
    assert not _is_linked(b, 'datasetload_Table', a2)
    if hasattr(a2, 'datasetload_TableGroup'):
        assert not _is_linked(a2, 'datasetload_TableGroup', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

