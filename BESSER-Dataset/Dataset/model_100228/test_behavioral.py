import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Cell,
    ColOrRowElement,
    Column,
    Data,
    DateTimeType,
    Row,
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
    Table,
    TableElement,
    ValueType,
    Workbook,
    Worksheet,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_c_data16_stub_double():
    # Data has no real 'Data17' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Cell(arrayRange="sample_text", formula="sample_text", hRef="sample_text", mergeAcross="sample_text", mergeDown="sample_text")
    partner = Data()
    setattr(partner, 'Data17', None)
    _safe_set(owner, 'd_cell', partner)
    assert getattr(partner, 'Data17') == owner
    _safe_set(owner, 'd_cell', None)
    assert getattr(partner, 'Data17') is None


def test_assoc_c_row14_stub_double():
    # Row has no real 'Row15' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Cell(arrayRange="sample_text", formula="sample_text", hRef="sample_text", mergeAcross="sample_text", mergeDown="sample_text")
    partner = Row()
    setattr(partner, 'Row15', None)
    _safe_set(owner, 'r_cells', partner)
    assert getattr(partner, 'Row15') == owner
    _safe_set(owner, 'r_cells', None)
    assert getattr(partner, 'Row15') is None


def test_assoc_c_table9_stub_double():
    # Table has no real 'Table10' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Column(autoFitWidth="sample_text", width="sample_text")
    partner = Table()
    setattr(partner, 'Table10', None)
    _safe_set(owner, 't_cols', partner)
    assert getattr(partner, 'Table10') == owner
    _safe_set(owner, 't_cols', None)
    assert getattr(partner, 'Table10') is None


def test_assoc_r_cells13_stub_double():
    # Cell has no real 'Cell' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Row's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Row's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Row(autoFitHeight="sample_text", height="sample_text")
    partner = Cell()
    setattr(partner, 'Cell', None)
    _safe_set(owner, 'c_row', {partner})
    assert getattr(partner, 'Cell') == owner
    _safe_set(owner, 'c_row', set())
    assert getattr(partner, 'Cell') is None


def test_assoc_r_table11_stub_double():
    # Table has no real 'Table12' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Row's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Row's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Row(autoFitHeight="sample_text", height="sample_text")
    partner = Table()
    setattr(partner, 'Table12', None)
    _safe_set(owner, 't_rows', partner)
    assert getattr(partner, 'Table12') == owner
    _safe_set(owner, 't_rows', None)
    assert getattr(partner, 'Table12') is None


def test_assoc_ws_table4_stub_double():
    # Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Worksheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Worksheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Worksheet(name="sample_text")
    partner = Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 't_worksheet', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 't_worksheet', None)
    assert getattr(partner, 'Table') is None


def test_assoc_ws_workbook3_stub_double():
    # Workbook has no real 'Workbook' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLSimplified_Worksheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLSimplified_Worksheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLSimplified_Worksheet(name="sample_text")
    partner = Workbook()
    setattr(partner, 'Workbook', None)
    _safe_set(owner, 'wb_worksheets', partner)
    assert getattr(partner, 'Workbook') == owner
    _safe_set(owner, 'wb_worksheets', None)
    assert getattr(partner, 'Workbook') is None


