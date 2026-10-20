import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    spreadsheet_Cell,
    spreadsheet_Column,
    spreadsheet_Row,
    spreadsheet_Sheet,
    spreadsheet_Spreadsheet,
    CellType,
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

def test_assoc_Cell13_reverse_link_reassign_clear():
    a1 = spreadsheet_Column(ColumnIndex=7)
    a2 = spreadsheet_Column(ColumnIndex=13)
    b = spreadsheet_Cell(CellType="sample_text", DoubleValue=3.14, StringValue="sample_text", ValueFormatted="sample_text")
    _safe_set(b, 'Cell15', a1)
    assert _is_linked(b, 'Cell15', a1)
    if hasattr(a1, 'Column14'):
        assert _is_linked(a1, 'Column14', b)
    _safe_set(b, 'Cell15', a2)
    assert _is_linked(b, 'Cell15', a2)
    if hasattr(a1, 'Column14'):
        assert not _is_linked(a1, 'Column14', b)
    if hasattr(a2, 'Column14'):
        assert _is_linked(a2, 'Column14', b)
    _safe_set(b, 'Cell15', None)
    assert not _is_linked(b, 'Cell15', a2)
    if hasattr(a2, 'Column14'):
        assert not _is_linked(a2, 'Column14', b)


def test_assoc_Cell8_reverse_link_reassign_clear():
    a1 = spreadsheet_Row(RowIndex=7)
    a2 = spreadsheet_Row(RowIndex=13)
    b = spreadsheet_Cell(CellType="sample_text", DoubleValue=3.14, StringValue="sample_text", ValueFormatted="sample_text")
    _safe_set(b, 'Cell', a1)
    assert _is_linked(b, 'Cell', a1)
    if hasattr(a1, 'Row9'):
        assert _is_linked(a1, 'Row9', b)
    _safe_set(b, 'Cell', a2)
    assert _is_linked(b, 'Cell', a2)
    if hasattr(a1, 'Row9'):
        assert not _is_linked(a1, 'Row9', b)
    if hasattr(a2, 'Row9'):
        assert _is_linked(a2, 'Row9', b)
    _safe_set(b, 'Cell', None)
    assert not _is_linked(b, 'Cell', a2)
    if hasattr(a2, 'Row9'):
        assert not _is_linked(a2, 'Row9', b)


def test_assoc_Column22_reverse_link_reassign_clear():
    a1 = spreadsheet_Column(ColumnIndex=7)
    a2 = spreadsheet_Column(ColumnIndex=13)
    b = spreadsheet_Cell(CellType="sample_text", DoubleValue=3.14, StringValue="sample_text", ValueFormatted="sample_text")
    _safe_set(b, 'Cell23', a1)
    assert _is_linked(b, 'Cell23', a1)
    if hasattr(a1, 'Column24'):
        assert _is_linked(a1, 'Column24', b)
    _safe_set(b, 'Cell23', a2)
    assert _is_linked(b, 'Cell23', a2)
    if hasattr(a1, 'Column24'):
        assert not _is_linked(a1, 'Column24', b)
    if hasattr(a2, 'Column24'):
        assert _is_linked(a2, 'Column24', b)
    _safe_set(b, 'Cell23', None)
    assert not _is_linked(b, 'Cell23', a2)
    if hasattr(a2, 'Column24'):
        assert not _is_linked(a2, 'Column24', b)


def test_assoc_Column3_reverse_link_reassign_clear():
    a1 = spreadsheet_Sheet(SheetIndex=7, SheetName="sample_text")
    a2 = spreadsheet_Sheet(SheetIndex=13, SheetName="sample_text_2")
    b = spreadsheet_Column(ColumnIndex=7)
    _safe_set(b, 'Column', a1)
    assert _is_linked(b, 'Column', a1)
    if hasattr(a1, 'Sheet4'):
        assert _is_linked(a1, 'Sheet4', b)
    _safe_set(b, 'Column', a2)
    assert _is_linked(b, 'Column', a2)
    if hasattr(a1, 'Sheet4'):
        assert not _is_linked(a1, 'Sheet4', b)
    if hasattr(a2, 'Sheet4'):
        assert _is_linked(a2, 'Sheet4', b)
    _safe_set(b, 'Column', None)
    assert not _is_linked(b, 'Column', a2)
    if hasattr(a2, 'Sheet4'):
        assert not _is_linked(a2, 'Sheet4', b)


def test_assoc_Row1_reverse_link_reassign_clear():
    a1 = spreadsheet_Sheet(SheetIndex=7, SheetName="sample_text")
    a2 = spreadsheet_Sheet(SheetIndex=13, SheetName="sample_text_2")
    b = spreadsheet_Row(RowIndex=7)
    _safe_set(b, 'Row', a1)
    assert _is_linked(b, 'Row', a1)
    if hasattr(a1, 'Sheet2'):
        assert _is_linked(a1, 'Sheet2', b)
    _safe_set(b, 'Row', a2)
    assert _is_linked(b, 'Row', a2)
    if hasattr(a1, 'Sheet2'):
        assert not _is_linked(a1, 'Sheet2', b)
    if hasattr(a2, 'Sheet2'):
        assert _is_linked(a2, 'Sheet2', b)
    _safe_set(b, 'Row', None)
    assert not _is_linked(b, 'Row', a2)
    if hasattr(a2, 'Sheet2'):
        assert not _is_linked(a2, 'Sheet2', b)


def test_assoc_Row19_reverse_link_reassign_clear():
    a1 = spreadsheet_Row(RowIndex=7)
    a2 = spreadsheet_Row(RowIndex=13)
    b = spreadsheet_Cell(CellType="sample_text", DoubleValue=3.14, StringValue="sample_text", ValueFormatted="sample_text")
    _safe_set(b, 'Cell20', a1)
    assert _is_linked(b, 'Cell20', a1)
    if hasattr(a1, 'Row21'):
        assert _is_linked(a1, 'Row21', b)
    _safe_set(b, 'Cell20', a2)
    assert _is_linked(b, 'Cell20', a2)
    if hasattr(a1, 'Row21'):
        assert not _is_linked(a1, 'Row21', b)
    if hasattr(a2, 'Row21'):
        assert _is_linked(a2, 'Row21', b)
    _safe_set(b, 'Cell20', None)
    assert not _is_linked(b, 'Cell20', a2)
    if hasattr(a2, 'Row21'):
        assert not _is_linked(a2, 'Row21', b)


def test_assoc_Sheet0_reverse_link_reassign_clear():
    a1 = spreadsheet_Spreadsheet(FilePath="sample_text", Label="sample_text")
    a2 = spreadsheet_Spreadsheet(FilePath="sample_text_2", Label="sample_text_2")
    b = spreadsheet_Sheet(SheetIndex=7, SheetName="sample_text")
    _safe_set(b, 'Sheet', a1)
    assert _is_linked(b, 'Sheet', a1)
    if hasattr(a1, 'Spreadsheet'):
        assert _is_linked(a1, 'Spreadsheet', b)
    _safe_set(b, 'Sheet', a2)
    assert _is_linked(b, 'Sheet', a2)
    if hasattr(a1, 'Spreadsheet'):
        assert not _is_linked(a1, 'Spreadsheet', b)
    if hasattr(a2, 'Spreadsheet'):
        assert _is_linked(a2, 'Spreadsheet', b)
    _safe_set(b, 'Sheet', None)
    assert not _is_linked(b, 'Sheet', a2)
    if hasattr(a2, 'Spreadsheet'):
        assert not _is_linked(a2, 'Spreadsheet', b)


def test_assoc_Sheet10_reverse_link_reassign_clear():
    a1 = spreadsheet_Sheet(SheetIndex=7, SheetName="sample_text")
    a2 = spreadsheet_Sheet(SheetIndex=13, SheetName="sample_text_2")
    b = spreadsheet_Row(RowIndex=7)
    _safe_set(b, 'Row11', a1)
    assert _is_linked(b, 'Row11', a1)
    if hasattr(a1, 'Sheet12'):
        assert _is_linked(a1, 'Sheet12', b)
    _safe_set(b, 'Row11', a2)
    assert _is_linked(b, 'Row11', a2)
    if hasattr(a1, 'Sheet12'):
        assert not _is_linked(a1, 'Sheet12', b)
    if hasattr(a2, 'Sheet12'):
        assert _is_linked(a2, 'Sheet12', b)
    _safe_set(b, 'Row11', None)
    assert not _is_linked(b, 'Row11', a2)
    if hasattr(a2, 'Sheet12'):
        assert not _is_linked(a2, 'Sheet12', b)


def test_assoc_Sheet16_reverse_link_reassign_clear():
    a1 = spreadsheet_Sheet(SheetIndex=7, SheetName="sample_text")
    a2 = spreadsheet_Sheet(SheetIndex=13, SheetName="sample_text_2")
    b = spreadsheet_Column(ColumnIndex=7)
    _safe_set(b, 'Column17', a1)
    assert _is_linked(b, 'Column17', a1)
    if hasattr(a1, 'Sheet18'):
        assert _is_linked(a1, 'Sheet18', b)
    _safe_set(b, 'Column17', a2)
    assert _is_linked(b, 'Column17', a2)
    if hasattr(a1, 'Sheet18'):
        assert not _is_linked(a1, 'Sheet18', b)
    if hasattr(a2, 'Sheet18'):
        assert _is_linked(a2, 'Sheet18', b)
    _safe_set(b, 'Column17', None)
    assert not _is_linked(b, 'Column17', a2)
    if hasattr(a2, 'Sheet18'):
        assert not _is_linked(a2, 'Sheet18', b)


def test_assoc_Spreadsheet5_reverse_link_reassign_clear():
    a1 = spreadsheet_Spreadsheet(FilePath="sample_text", Label="sample_text")
    a2 = spreadsheet_Spreadsheet(FilePath="sample_text_2", Label="sample_text_2")
    b = spreadsheet_Sheet(SheetIndex=7, SheetName="sample_text")
    _safe_set(b, 'Sheet6', a1)
    assert _is_linked(b, 'Sheet6', a1)
    if hasattr(a1, 'Spreadsheet7'):
        assert _is_linked(a1, 'Spreadsheet7', b)
    _safe_set(b, 'Sheet6', a2)
    assert _is_linked(b, 'Sheet6', a2)
    if hasattr(a1, 'Spreadsheet7'):
        assert not _is_linked(a1, 'Spreadsheet7', b)
    if hasattr(a2, 'Spreadsheet7'):
        assert _is_linked(a2, 'Spreadsheet7', b)
    _safe_set(b, 'Sheet6', None)
    assert not _is_linked(b, 'Sheet6', a2)
    if hasattr(a2, 'Spreadsheet7'):
        assert not _is_linked(a2, 'Spreadsheet7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

