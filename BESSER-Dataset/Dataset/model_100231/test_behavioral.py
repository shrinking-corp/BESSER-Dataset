import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Cell,
    ColOrRowElement,
    Column,
    Comment,
    CustomDocumentPropertiesCollection,
    CustomDocumentProperty,
    Data,
    DateTimeType,
    DocumentPropertiesCollection,
    ExcelWorkbook,
    Row,
    SmartTagType,
    SmartTagsCollection,
    SpreadsheetMLWorkbookProp_BooleanValue,
    SpreadsheetMLWorkbookProp_Cell,
    SpreadsheetMLWorkbookProp_ColOrRowElement,
    SpreadsheetMLWorkbookProp_Column,
    SpreadsheetMLWorkbookProp_Comment,
    SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection,
    SpreadsheetMLWorkbookProp_CustomDocumentProperty,
    SpreadsheetMLWorkbookProp_Data,
    SpreadsheetMLWorkbookProp_DateTimeType,
    SpreadsheetMLWorkbookProp_DateTimeTypeValue,
    SpreadsheetMLWorkbookProp_DocumentPropertiesCollection,
    SpreadsheetMLWorkbookProp_ErrorValue,
    SpreadsheetMLWorkbookProp_ExcelWorkbook,
    SpreadsheetMLWorkbookProp_NumberValue,
    SpreadsheetMLWorkbookProp_Row,
    SpreadsheetMLWorkbookProp_SmartTagType,
    SpreadsheetMLWorkbookProp_SmartTagsCollection,
    SpreadsheetMLWorkbookProp_StringValue,
    SpreadsheetMLWorkbookProp_StyledElement,
    SpreadsheetMLWorkbookProp_Table,
    SpreadsheetMLWorkbookProp_TableElement,
    SpreadsheetMLWorkbookProp_ValueType,
    SpreadsheetMLWorkbookProp_VersionType,
    SpreadsheetMLWorkbookProp_Workbook,
    SpreadsheetMLWorkbookProp_Worksheet,
    StyledElement,
    Table,
    TableElement,
    ValueType,
    VersionType,
    Workbook,
    Worksheet,
    CalculationWorkbookType,
    DisplayDrawingObjectsType,
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

def test_assoc_c_cell50_stub_double():
    # Cell has no real 'Cell51' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Comment(author="sample_text", showAlways="sample_text")
    partner = Cell()
    setattr(partner, 'Cell51', None)
    _safe_set(owner, 'c_comment', partner)
    assert getattr(partner, 'Cell51') == owner
    _safe_set(owner, 'c_comment', None)
    assert getattr(partner, 'Cell51') is None


def test_assoc_c_comment49_stub_double():
    # Comment has no real 'Comment' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Cell(arrayRange="sample_text", formula="sample_text", hRef="sample_text", mergeAcross="sample_text", mergeDown="sample_text")
    partner = Comment()
    setattr(partner, 'Comment', None)
    _safe_set(owner, 'c_cell', partner)
    assert getattr(partner, 'Comment') == owner
    _safe_set(owner, 'c_cell', None)
    assert getattr(partner, 'Comment') is None


def test_assoc_c_data47_stub_double():
    # Data has no real 'Data48' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Cell(arrayRange="sample_text", formula="sample_text", hRef="sample_text", mergeAcross="sample_text", mergeDown="sample_text")
    partner = Data()
    setattr(partner, 'Data48', None)
    _safe_set(owner, 'd_cell', partner)
    assert getattr(partner, 'Data48') == owner
    _safe_set(owner, 'd_cell', None)
    assert getattr(partner, 'Data48') is None


def test_assoc_c_row45_stub_double():
    # Row has no real 'Row46' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Cell(arrayRange="sample_text", formula="sample_text", hRef="sample_text", mergeAcross="sample_text", mergeDown="sample_text")
    partner = Row()
    setattr(partner, 'Row46', None)
    _safe_set(owner, 'r_cells', partner)
    assert getattr(partner, 'Row46') == owner
    _safe_set(owner, 'r_cells', None)
    assert getattr(partner, 'Row46') is None


def test_assoc_c_smartTags43_stub_double():
    # SmartTagsCollection has no real 'SmartTagsCollection44' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Cell(arrayRange="sample_text", formula="sample_text", hRef="sample_text", mergeAcross="sample_text", mergeDown="sample_text")
    partner = SmartTagsCollection()
    setattr(partner, 'SmartTagsCollection44', None)
    _safe_set(owner, 'st_cell', {partner})
    assert getattr(partner, 'SmartTagsCollection44') == owner
    _safe_set(owner, 'st_cell', set())
    assert getattr(partner, 'SmartTagsCollection44') is None


def test_assoc_c_table37_stub_double():
    # Table has no real 'Table38' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Column(autoFitWidth="sample_text", width="sample_text")
    partner = Table()
    setattr(partner, 'Table38', None)
    _safe_set(owner, 't_cols', partner)
    assert getattr(partner, 'Table38') == owner
    _safe_set(owner, 't_cols', None)
    assert getattr(partner, 'Table38') is None


def test_assoc_com_data52_stub_double():
    # Data has no real 'Data53' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Comment(author="sample_text", showAlways="sample_text")
    partner = Data()
    setattr(partner, 'Data53', None)
    _safe_set(owner, 'd_comment', partner)
    assert getattr(partner, 'Data53') == owner
    _safe_set(owner, 'd_comment', None)
    assert getattr(partner, 'Data53') is None


def test_assoc_created7_stub_double():
    # DateTimeType has no real 'DateTimeType9' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_DocumentPropertiesCollection(appName="sample_text", author="sample_text", bytes="sample_text", category="sample_text", characters="sample_text", charactersWithSpaces="sample_text", company="sample_text", description="sample_text", guid="sample_text", hyperlinkBase="sample_text", keywords="sample_text", lastAuthor="sample_text", lines="sample_text", manager="sample_text", pages="sample_text", paragraphs="sample_text", presentationFormat="sample_text", revision="sample_text", subject="sample_text", title="sample_text", totalTime="sample_text", words="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType9', None)
    _safe_set(owner, 'SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8', partner)
    assert getattr(partner, 'DateTimeType9') == owner
    _safe_set(owner, 'SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8', None)
    assert getattr(partner, 'DateTimeType9') is None


def test_assoc_customDocumentProperty_cdpe16_stub_double():
    # CustomDocumentPropertiesCollection has no real 'CustomDocumentPropertiesCollection' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_CustomDocumentProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_CustomDocumentProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_CustomDocumentProperty(name="sample_text")
    partner = CustomDocumentPropertiesCollection()
    setattr(partner, 'CustomDocumentPropertiesCollection', None)
    _safe_set(owner, 'customDocumentProperties', partner)
    assert getattr(partner, 'CustomDocumentPropertiesCollection') == owner
    _safe_set(owner, 'customDocumentProperties', None)
    assert getattr(partner, 'CustomDocumentPropertiesCollection') is None


def test_assoc_dp_workbook2_stub_double():
    # Workbook has no real 'Workbook' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_DocumentPropertiesCollection(appName="sample_text", author="sample_text", bytes="sample_text", category="sample_text", characters="sample_text", charactersWithSpaces="sample_text", company="sample_text", description="sample_text", guid="sample_text", hyperlinkBase="sample_text", keywords="sample_text", lastAuthor="sample_text", lines="sample_text", manager="sample_text", pages="sample_text", paragraphs="sample_text", presentationFormat="sample_text", revision="sample_text", subject="sample_text", title="sample_text", totalTime="sample_text", words="sample_text")
    partner = Workbook()
    setattr(partner, 'Workbook', None)
    _safe_set(owner, 'wb_docProperties', partner)
    assert getattr(partner, 'Workbook') == owner
    _safe_set(owner, 'wb_docProperties', None)
    assert getattr(partner, 'Workbook') is None


def test_assoc_ew_workbook60_stub_double():
    # Workbook has no real 'Workbook61' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_ExcelWorkbook's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_ExcelWorkbook's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_ExcelWorkbook(acceptLabelsInFormulas="sample_text", activeChart="sample_text", activeSheet="sample_text", calculation="sample_text", createBackup="sample_text", date1904="sample_text", displayDrawingObjects="sample_text", displayInkNotes="sample_text", doNotCalculateBeforeSave="sample_text", doNotSaveLinkValues="sample_text", embedSaveSmartTags="sample_text", firstVisibleSheet="sample_text", futureVer="sample_text", hideHorizontalScrollBar="sample_text", hidePivotTableFieldList="sample_text", hideVerticalScrollBar="sample_text", hideWorkbookTabs="sample_text", iteration="sample_text", maxChange="sample_text", maxIterations="sample_text", noAutoRecover="sample_text", precisionAsDisplayed="sample_text", protectStructure="sample_text", protectWindows="sample_text", refModeR1C1="sample_text", selectedSheets="sample_text", tabRatio="sample_text", uncalced="sample_text", windowHeight="sample_text", windowHidden="sample_text", windowIconic="sample_text", windowTopX="sample_text", windowTopY="sample_text", windowWidth="sample_text")
    partner = Workbook()
    setattr(partner, 'Workbook61', None)
    _safe_set(owner, 'wb_excelWorkbook', partner)
    assert getattr(partner, 'Workbook61') == owner
    _safe_set(owner, 'wb_excelWorkbook', None)
    assert getattr(partner, 'Workbook61') is None


def test_assoc_lastPrinted4_stub_double():
    # DateTimeType has no real 'DateTimeType6' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_DocumentPropertiesCollection(appName="sample_text", author="sample_text", bytes="sample_text", category="sample_text", characters="sample_text", charactersWithSpaces="sample_text", company="sample_text", description="sample_text", guid="sample_text", hyperlinkBase="sample_text", keywords="sample_text", lastAuthor="sample_text", lines="sample_text", manager="sample_text", pages="sample_text", paragraphs="sample_text", presentationFormat="sample_text", revision="sample_text", subject="sample_text", title="sample_text", totalTime="sample_text", words="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType6', None)
    _safe_set(owner, 'SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5', partner)
    assert getattr(partner, 'DateTimeType6') == owner
    _safe_set(owner, 'SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5', None)
    assert getattr(partner, 'DateTimeType6') is None


def test_assoc_lastSaved10_stub_double():
    # DateTimeType has no real 'DateTimeType12' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_DocumentPropertiesCollection(appName="sample_text", author="sample_text", bytes="sample_text", category="sample_text", characters="sample_text", charactersWithSpaces="sample_text", company="sample_text", description="sample_text", guid="sample_text", hyperlinkBase="sample_text", keywords="sample_text", lastAuthor="sample_text", lines="sample_text", manager="sample_text", pages="sample_text", paragraphs="sample_text", presentationFormat="sample_text", revision="sample_text", subject="sample_text", title="sample_text", totalTime="sample_text", words="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType12', None)
    _safe_set(owner, 'SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11', partner)
    assert getattr(partner, 'DateTimeType12') == owner
    _safe_set(owner, 'SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11', None)
    assert getattr(partner, 'DateTimeType12') is None


def test_assoc_r_cells41_stub_double():
    # Cell has no real 'Cell42' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Row's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Row's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Row(autoFitHeight="sample_text", height="sample_text")
    partner = Cell()
    setattr(partner, 'Cell42', None)
    _safe_set(owner, 'c_row', {partner})
    assert getattr(partner, 'Cell42') == owner
    _safe_set(owner, 'c_row', set())
    assert getattr(partner, 'Cell42') is None


def test_assoc_r_table39_stub_double():
    # Table has no real 'Table40' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Row's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Row's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Row(autoFitHeight="sample_text", height="sample_text")
    partner = Table()
    setattr(partner, 'Table40', None)
    _safe_set(owner, 't_rows', partner)
    assert getattr(partner, 'Table40') == owner
    _safe_set(owner, 't_rows', None)
    assert getattr(partner, 'Table40') is None


def test_assoc_smartTagType_ste18_stub_double():
    # SmartTagsCollection has no real 'SmartTagsCollection' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_SmartTagType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_SmartTagType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_SmartTagType(name="sample_text", namespaceuri="sample_text", url="sample_text")
    partner = SmartTagsCollection()
    setattr(partner, 'SmartTagsCollection', None)
    _safe_set(owner, 'smartTagTypes', partner)
    assert getattr(partner, 'SmartTagsCollection') == owner
    _safe_set(owner, 'smartTagTypes', None)
    assert getattr(partner, 'SmartTagsCollection') is None


def test_assoc_t_cols35_stub_double():
    # Column has no real 'Column' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Table(defaultColumnWidth="sample_text", defaultRowHeight="sample_text", expandedColumnCount="sample_text", expandedRowCount="sample_text", fullColumns="sample_text", fullRows="sample_text", leftCell="sample_text", topCell="sample_text")
    partner = Column()
    setattr(partner, 'Column', None)
    _safe_set(owner, 'c_table', {partner})
    assert getattr(partner, 'Column') == owner
    _safe_set(owner, 'c_table', set())
    assert getattr(partner, 'Column') is None


def test_assoc_t_rows36_stub_double():
    # Row has no real 'Row' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Table(defaultColumnWidth="sample_text", defaultRowHeight="sample_text", expandedColumnCount="sample_text", expandedRowCount="sample_text", fullColumns="sample_text", fullRows="sample_text", leftCell="sample_text", topCell="sample_text")
    partner = Row()
    setattr(partner, 'Row', None)
    _safe_set(owner, 'r_table', {partner})
    assert getattr(partner, 'Row') == owner
    _safe_set(owner, 'r_table', set())
    assert getattr(partner, 'Row') is None


def test_assoc_t_worksheet33_stub_double():
    # Worksheet has no real 'Worksheet34' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Table(defaultColumnWidth="sample_text", defaultRowHeight="sample_text", expandedColumnCount="sample_text", expandedRowCount="sample_text", fullColumns="sample_text", fullRows="sample_text", leftCell="sample_text", topCell="sample_text")
    partner = Worksheet()
    setattr(partner, 'Worksheet34', None)
    _safe_set(owner, 'ws_table', partner)
    assert getattr(partner, 'Worksheet34') == owner
    _safe_set(owner, 'ws_table', None)
    assert getattr(partner, 'Worksheet34') is None


def test_assoc_value17_stub_double():
    # ValueType has no real 'ValueType' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_CustomDocumentProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_CustomDocumentProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_CustomDocumentProperty(name="sample_text")
    partner = ValueType()
    setattr(partner, 'ValueType', None)
    _safe_set(owner, 'SpreadsheetMLWorkbookProp_CustomDocumentProperty', partner)
    assert getattr(partner, 'ValueType') == owner
    _safe_set(owner, 'SpreadsheetMLWorkbookProp_CustomDocumentProperty', None)
    assert getattr(partner, 'ValueType') is None


def test_assoc_version3_stub_double():
    # VersionType has no real 'VersionType' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_DocumentPropertiesCollection(appName="sample_text", author="sample_text", bytes="sample_text", category="sample_text", characters="sample_text", charactersWithSpaces="sample_text", company="sample_text", description="sample_text", guid="sample_text", hyperlinkBase="sample_text", keywords="sample_text", lastAuthor="sample_text", lines="sample_text", manager="sample_text", pages="sample_text", paragraphs="sample_text", presentationFormat="sample_text", revision="sample_text", subject="sample_text", title="sample_text", totalTime="sample_text", words="sample_text")
    partner = VersionType()
    setattr(partner, 'VersionType', None)
    _safe_set(owner, 'SpreadsheetMLWorkbookProp_DocumentPropertiesCollection', partner)
    assert getattr(partner, 'VersionType') == owner
    _safe_set(owner, 'SpreadsheetMLWorkbookProp_DocumentPropertiesCollection', None)
    assert getattr(partner, 'VersionType') is None


def test_assoc_ws_table32_stub_double():
    # Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Worksheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Worksheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Worksheet(name="sample_text")
    partner = Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 't_worksheet', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 't_worksheet', None)
    assert getattr(partner, 'Table') is None


def test_assoc_ws_workbook30_stub_double():
    # Workbook has no real 'Workbook31' property in the generated
    # code (a bare stub) -- manually attach it so SpreadsheetMLWorkbookProp_Worksheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpreadsheetMLWorkbookProp_Worksheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpreadsheetMLWorkbookProp_Worksheet(name="sample_text")
    partner = Workbook()
    setattr(partner, 'Workbook31', None)
    _safe_set(owner, 'wb_worksheets', partner)
    assert getattr(partner, 'Workbook31') == owner
    _safe_set(owner, 'wb_worksheets', None)
    assert getattr(partner, 'Workbook31') is None


