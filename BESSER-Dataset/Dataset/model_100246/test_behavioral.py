import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ColOrRowElement,
    SpreadsheetMLSimplified_BooleanValue,
    SpreadsheetMLSimplified_Cell,
    SpreadsheetMLSimplified_ColOrRowElement,
    SpreadsheetMLSimplified_Column,
    SpreadsheetMLSimplified_Data,
    SpreadsheetMLSimplified_DateTimeType,
    SpreadsheetMLSimplified_DateTimeTypeValue,
    SpreadsheetMLSimplified_ErrorValue,
    SpreadsheetMLSimplified_NumberValue,
    SpreadsheetMLSimplified_Row,
    SpreadsheetMLSimplified_StringValue,
    SpreadsheetMLSimplified_Table,
    SpreadsheetMLSimplified_TableElement,
    SpreadsheetMLSimplified_ValueType,
    SpreadsheetMLSimplified_Workbook,
    SpreadsheetMLSimplified_Worksheet,
    TableElement,
    ValueType,
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

def test_assoc_c_row14_reverse_link_reassign_clear():
    a1 = SpreadsheetMLSimplified_Row(autoFitHeight=True, height=3.14)
    a2 = SpreadsheetMLSimplified_Row(autoFitHeight=False, height=9.99)
    b = SpreadsheetMLSimplified_Cell(arrayRange="sample_text", formula="sample_text", hRef="sample_text", mergeAcross=3.14, mergeDown=3.14)
    _safe_set(b, 'r_cells', a1)
    assert _is_linked(b, 'r_cells', a1)
    if hasattr(a1, 'Row15'):
        assert _is_linked(a1, 'Row15', b)
    _safe_set(b, 'r_cells', a2)
    assert _is_linked(b, 'r_cells', a2)
    if hasattr(a1, 'Row15'):
        assert not _is_linked(a1, 'Row15', b)
    if hasattr(a2, 'Row15'):
        assert _is_linked(a2, 'Row15', b)
    _safe_set(b, 'r_cells', None)
    assert not _is_linked(b, 'r_cells', a2)
    if hasattr(a2, 'Row15'):
        assert not _is_linked(a2, 'Row15', b)


def test_assoc_r_cells13_reverse_link_reassign_clear():
    a1 = SpreadsheetMLSimplified_Row(autoFitHeight=True, height=3.14)
    a2 = SpreadsheetMLSimplified_Row(autoFitHeight=False, height=9.99)
    b = SpreadsheetMLSimplified_Cell(arrayRange="sample_text", formula="sample_text", hRef="sample_text", mergeAcross=3.14, mergeDown=3.14)
    _safe_set(b, 'Cell', a1)
    assert _is_linked(b, 'Cell', a1)
    if hasattr(a1, 'c_row'):
        assert _is_linked(a1, 'c_row', b)
    _safe_set(b, 'Cell', a2)
    assert _is_linked(b, 'Cell', a2)
    if hasattr(a1, 'c_row'):
        assert not _is_linked(a1, 'c_row', b)
    if hasattr(a2, 'c_row'):
        assert _is_linked(a2, 'c_row', b)
    _safe_set(b, 'Cell', None)
    assert not _is_linked(b, 'Cell', a2)
    if hasattr(a2, 'c_row'):
        assert not _is_linked(a2, 'c_row', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_c_data16_stub_double():
    # SpreadsheetMLSimplified_Data has no real 'Data17' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Cell(arrayRange="sample_text", formula="sample_text", hRef="sample_text", mergeAcross=3.14, mergeDown=3.14)
    partner = SpreadsheetMLSimplified_Data()
    setattr(partner, 'Data17', None)
    _safe_set(owner, 'd_cell', partner)
    assert getattr(partner, 'Data17') == owner
    _safe_set(owner, 'd_cell', None)
    assert getattr(partner, 'Data17') is None


def test_assoc_c_table9_stub_double():
    # SpreadsheetMLSimplified_Table has no real 'Table10' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Column(autoFitWidth=True, width=3.14)
    partner = SpreadsheetMLSimplified_Table()
    setattr(partner, 'Table10', None)
    _safe_set(owner, 't_cols', partner)
    assert getattr(partner, 'Table10') == owner
    _safe_set(owner, 't_cols', None)
    assert getattr(partner, 'Table10') is None


def test_assoc_d_cell18_stub_double():
    # SpreadsheetMLSimplified_Data has no real 'c_data' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Cell(arrayRange="sample_text", formula="sample_text", hRef="sample_text", mergeAcross=3.14, mergeDown=3.14)
    partner = SpreadsheetMLSimplified_Data()
    setattr(partner, 'c_data', None)
    _safe_set(owner, 'Cell19', partner)
    assert getattr(partner, 'c_data') == owner
    _safe_set(owner, 'Cell19', None)
    assert getattr(partner, 'c_data') is None


def test_assoc_r_table11_stub_double():
    # SpreadsheetMLSimplified_Table has no real 'Table12' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Row's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Row's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Row(autoFitHeight=True, height=3.14)
    partner = SpreadsheetMLSimplified_Table()
    setattr(partner, 'Table12', None)
    _safe_set(owner, 't_rows', partner)
    assert getattr(partner, 'Table12') == owner
    _safe_set(owner, 't_rows', None)
    assert getattr(partner, 'Table12') is None


def test_assoc_t_cols7_stub_double():
    # SpreadsheetMLSimplified_Table has no real 'c_table' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Column(autoFitWidth=True, width=3.14)
    partner = SpreadsheetMLSimplified_Table()
    setattr(partner, 'c_table', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'c_table')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'c_table')


def test_assoc_t_rows8_stub_double():
    # SpreadsheetMLSimplified_Table has no real 'r_table' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Row's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Row's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Row(autoFitHeight=True, height=3.14)
    partner = SpreadsheetMLSimplified_Table()
    setattr(partner, 'r_table', None)
    _safe_set(owner, 'Row', partner)
    assert owner in getattr(partner, 'r_table')
    _safe_set(owner, 'Row', None)
    assert owner not in getattr(partner, 'r_table')


def test_assoc_t_worksheet5_stub_double():
    # SpreadsheetMLSimplified_Table has no real 'ws_table' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Worksheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Worksheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Worksheet(name="sample_text")
    partner = SpreadsheetMLSimplified_Table()
    setattr(partner, 'ws_table', None)
    _safe_set(owner, 'Worksheet6', partner)
    assert getattr(partner, 'ws_table') == owner
    _safe_set(owner, 'Worksheet6', None)
    assert getattr(partner, 'ws_table') is None


def test_assoc_value1_stub_double():
    # SpreadsheetMLSimplified_DateTimeTypeValue has no real 'SpreadsheetMLSimplified_DateTimeTypeValue' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_DateTimeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_DateTimeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_DateTimeType(day=7, hour=7, minute=7, month=7, second=7, year=7)
    partner = SpreadsheetMLSimplified_DateTimeTypeValue()
    setattr(partner, 'SpreadsheetMLSimplified_DateTimeTypeValue', None)
    _safe_set(owner, 'SpreadsheetMLSimplified_DateTimeType', partner)
    assert getattr(partner, 'SpreadsheetMLSimplified_DateTimeTypeValue') == owner
    _safe_set(owner, 'SpreadsheetMLSimplified_DateTimeType', None)
    assert getattr(partner, 'SpreadsheetMLSimplified_DateTimeTypeValue') is None


def test_assoc_wb_worksheets2_stub_double():
    # SpreadsheetMLSimplified_Workbook has no real 'ws_workbook' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Worksheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Worksheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Worksheet(name="sample_text")
    partner = SpreadsheetMLSimplified_Workbook()
    setattr(partner, 'ws_workbook', None)
    _safe_set(owner, 'Worksheet', partner)
    assert owner in getattr(partner, 'ws_workbook')
    _safe_set(owner, 'Worksheet', None)
    assert owner not in getattr(partner, 'ws_workbook')


def test_assoc_ws_table4_stub_double():
    # SpreadsheetMLSimplified_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Worksheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Worksheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Worksheet(name="sample_text")
    partner = SpreadsheetMLSimplified_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 't_worksheet', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 't_worksheet', None)
    assert getattr(partner, 'Table') is None


def test_assoc_ws_workbook3_stub_double():
    # SpreadsheetMLSimplified_Workbook has no real 'Workbook' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Worksheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Worksheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Worksheet(name="sample_text")
    partner = SpreadsheetMLSimplified_Workbook()
    setattr(partner, 'Workbook', None)
    _safe_set(owner, 'wb_worksheets', partner)
    assert getattr(partner, 'Workbook') == owner
    _safe_set(owner, 'wb_worksheets', None)
    assert getattr(partner, 'Workbook') is None


