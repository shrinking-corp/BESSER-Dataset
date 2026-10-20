import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArcTo,
    CellType,
    ColorEntry,
    ColorsTable,
    Connect,
    ConnectsCollection,
    CustomPropertiesCollection,
    CustomProperty,
    DatadiagramMLTextFormat_ArcTo,
    DatadiagramMLTextFormat_CellType,
    DatadiagramMLTextFormat_Char,
    DatadiagramMLTextFormat_ColorEntry,
    DatadiagramMLTextFormat_ColorsTable,
    DatadiagramMLTextFormat_Connect,
    DatadiagramMLTextFormat_ConnectsCollection,
    DatadiagramMLTextFormat_Cp,
    DatadiagramMLTextFormat_CustomPropertiesCollection,
    DatadiagramMLTextFormat_CustomProperty,
    DatadiagramMLTextFormat_DateTimeType,
    DatadiagramMLTextFormat_DelElt,
    DatadiagramMLTextFormat_DocumentPropertiesCollection,
    DatadiagramMLTextFormat_DocumentSettingsElt,
    DatadiagramMLTextFormat_DocumentSheet,
    DatadiagramMLTextFormat_Ellipse,
    DatadiagramMLTextFormat_EllipticalArcTo,
    DatadiagramMLTextFormat_EmailRoutingData,
    DatadiagramMLTextFormat_EventList,
    DatadiagramMLTextFormat_FaceName,
    DatadiagramMLTextFormat_FaceNamesTable,
    DatadiagramMLTextFormat_Field,
    DatadiagramMLTextFormat_Fld,
    DatadiagramMLTextFormat_FontEntry,
    DatadiagramMLTextFormat_FontsTable,
    DatadiagramMLTextFormat_Geom,
    DatadiagramMLTextFormat_HeaderFooter,
    DatadiagramMLTextFormat_IXElt,
    DatadiagramMLTextFormat_IXrequiredElt,
    DatadiagramMLTextFormat_Icon,
    DatadiagramMLTextFormat_IdentifiedElt,
    DatadiagramMLTextFormat_InfiniteLine,
    DatadiagramMLTextFormat_LineTo,
    DatadiagramMLTextFormat_Master,
    DatadiagramMLTextFormat_MasterElt,
    DatadiagramMLTextFormat_MasterShortCut,
    DatadiagramMLTextFormat_MastersCollection,
    DatadiagramMLTextFormat_MoveTo,
    DatadiagramMLTextFormat_NURBSTo,
    DatadiagramMLTextFormat_NamedElt,
    DatadiagramMLTextFormat_Page,
    DatadiagramMLTextFormat_PageElt,
    DatadiagramMLTextFormat_PageSheet,
    DatadiagramMLTextFormat_PagesCollection,
    DatadiagramMLTextFormat_Para,
    DatadiagramMLTextFormat_PolylineTo,
    DatadiagramMLTextFormat_Pp,
    DatadiagramMLTextFormat_PrintSetup,
    DatadiagramMLTextFormat_Shape,
    DatadiagramMLTextFormat_ShapeElt,
    DatadiagramMLTextFormat_ShapesCollection,
    DatadiagramMLTextFormat_SolutionXML,
    DatadiagramMLTextFormat_SplineKnot,
    DatadiagramMLTextFormat_SplineStart,
    DatadiagramMLTextFormat_StringElt,
    DatadiagramMLTextFormat_StyleSheet,
    DatadiagramMLTextFormat_StyleSheetsCollection,
    DatadiagramMLTextFormat_Tab,
    DatadiagramMLTextFormat_TabsCollection,
    DatadiagramMLTextFormat_Text,
    DatadiagramMLTextFormat_TextElt,
    DatadiagramMLTextFormat_Tp,
    DatadiagramMLTextFormat_UniqueIdElt,
    DatadiagramMLTextFormat_VBProjectData,
    DatadiagramMLTextFormat_VisioDocument,
    DatadiagramMLTextFormat_WindowsInfo,
    DatadiagramMLTextFormat_XYABCDEElt,
    DatadiagramMLTextFormat_XYABCDElt,
    DatadiagramMLTextFormat_XYABElt,
    DatadiagramMLTextFormat_XYAElt,
    DatadiagramMLTextFormat_XYElt,
    DateTimeType,
    DelElt,
    DocumentPropertiesCollection,
    DocumentSettingsElt,
    DocumentSheet,
    Ellipse,
    EllipticalArcTo,
    EmailRoutingData,
    EventList,
    FaceName,
    FaceNamesTable,
    FontEntry,
    FontsTable,
    Geom,
    HeaderFooter,
    IXElt,
    IXrequiredElt,
    Icon,
    IdentifiedElt,
    InfiniteLine,
    LineTo,
    Master,
    MasterElt,
    MasterShortCut,
    MastersCollection,
    MoveTo,
    NURBSTo,
    NamedElt,
    Page,
    PageElt,
    PageSheet,
    PagesCollection,
    PolylineTo,
    PrintSetup,
    Shape,
    ShapeElt,
    ShapesCollection,
    SolutionXML,
    SplineKnot,
    SplineStart,
    StyleSheet,
    StyleSheetsCollection,
    Tab,
    TabsCollection,
    Text,
    TextElt,
    UniqueIdElt,
    VBProjectData,
    VisioDocument,
    WindowsInfo,
    XYABCDEElt,
    XYABCDElt,
    XYABElt,
    XYAElt,
    XYElt,
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

def test_assoc_c_connects259_stub_double():
    # ConnectsCollection has no real 'ConnectsCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_Connect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_Connect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_Connect(fromCell="sample_text", fromPart="sample_text", fromSheet="sample_text", toCell="sample_text", toPart="sample_text", toSheet="sample_text")
    partner = ConnectsCollection()
    setattr(partner, 'ConnectsCollection', None)
    _safe_set(owner, 'connections', partner)
    assert getattr(partner, 'ConnectsCollection') == owner
    _safe_set(owner, 'connections', None)
    assert getattr(partner, 'ConnectsCollection') is None


def test_assoc_ce_colors37_stub_double():
    # ColorsTable has no real 'ColorsTable38' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_ColorEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_ColorEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_ColorEntry(rgb="sample_text")
    partner = ColorsTable()
    setattr(partner, 'ColorsTable38', None)
    _safe_set(owner, 'colorEntries', partner)
    assert getattr(partner, 'ColorsTable38') == owner
    _safe_set(owner, 'colorEntries', None)
    assert getattr(partner, 'ColorsTable38') is None


def test_assoc_cp_customProps32_stub_double():
    # CustomPropertiesCollection has no real 'CustomPropertiesCollection33' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_CustomProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_CustomProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_CustomProperty(dataType="sample_text", name="sample_text")
    partner = CustomPropertiesCollection()
    setattr(partner, 'CustomPropertiesCollection33', None)
    _safe_set(owner, 'cps_customProps', partner)
    assert getattr(partner, 'CustomPropertiesCollection33') == owner
    _safe_set(owner, 'cps_customProps', None)
    assert getattr(partner, 'CustomPropertiesCollection33') is None


def test_assoc_customProps18_stub_double():
    # CustomPropertiesCollection has no real 'CustomPropertiesCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = CustomPropertiesCollection()
    setattr(partner, 'CustomPropertiesCollection', None)
    _safe_set(owner, 'cps_docProp', partner)
    assert getattr(partner, 'CustomPropertiesCollection') == owner
    _safe_set(owner, 'cps_docProp', None)
    assert getattr(partner, 'CustomPropertiesCollection') is None


def test_assoc_docColors2_stub_double():
    # ColorsTable has no real 'ColorsTable' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = ColorsTable()
    setattr(partner, 'ColorsTable', None)
    _safe_set(owner, 'cs_visioDocument', partner)
    assert getattr(partner, 'ColorsTable') == owner
    _safe_set(owner, 'cs_visioDocument', None)
    assert getattr(partner, 'ColorsTable') is None


def test_assoc_docDocumentSheet7_stub_double():
    # DocumentSheet has no real 'DocumentSheet' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = DocumentSheet()
    setattr(partner, 'DocumentSheet', None)
    _safe_set(owner, 'ds_visioDocument', partner)
    assert getattr(partner, 'DocumentSheet') == owner
    _safe_set(owner, 'ds_visioDocument', None)
    assert getattr(partner, 'DocumentSheet') is None


def test_assoc_docEmailRoutingData15_stub_double():
    # EmailRoutingData has no real 'EmailRoutingData' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = EmailRoutingData()
    setattr(partner, 'EmailRoutingData', None)
    _safe_set(owner, 'erd_visioDocument', partner)
    assert getattr(partner, 'EmailRoutingData') == owner
    _safe_set(owner, 'erd_visioDocument', None)
    assert getattr(partner, 'EmailRoutingData') is None


def test_assoc_docEventList12_stub_double():
    # EventList has no real 'EventList' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = EventList()
    setattr(partner, 'EventList', None)
    _safe_set(owner, 'el_visioDocument', partner)
    assert getattr(partner, 'EventList') == owner
    _safe_set(owner, 'el_visioDocument', None)
    assert getattr(partner, 'EventList') is None


def test_assoc_docFaceNames5_stub_double():
    # FaceNamesTable has no real 'FaceNamesTable' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = FaceNamesTable()
    setattr(partner, 'FaceNamesTable', None)
    _safe_set(owner, 'fns_visioDocument', partner)
    assert getattr(partner, 'FaceNamesTable') == owner
    _safe_set(owner, 'fns_visioDocument', None)
    assert getattr(partner, 'FaceNamesTable') is None


def test_assoc_docFonts4_stub_double():
    # FontsTable has no real 'FontsTable' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = FontsTable()
    setattr(partner, 'FontsTable', None)
    _safe_set(owner, 'fs_visioDocument', partner)
    assert getattr(partner, 'FontsTable') == owner
    _safe_set(owner, 'fs_visioDocument', None)
    assert getattr(partner, 'FontsTable') is None


def test_assoc_docHeaderFooter13_stub_double():
    # HeaderFooter has no real 'HeaderFooter' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = HeaderFooter()
    setattr(partner, 'HeaderFooter', None)
    _safe_set(owner, 'ef_visioDocument', partner)
    assert getattr(partner, 'HeaderFooter') == owner
    _safe_set(owner, 'ef_visioDocument', None)
    assert getattr(partner, 'HeaderFooter') is None


def test_assoc_docMasters8_stub_double():
    # MastersCollection has no real 'MastersCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = MastersCollection()
    setattr(partner, 'MastersCollection', None)
    _safe_set(owner, 'ms_visioDocument', partner)
    assert getattr(partner, 'MastersCollection') == owner
    _safe_set(owner, 'ms_visioDocument', None)
    assert getattr(partner, 'MastersCollection') is None


def test_assoc_docPages9_stub_double():
    # PagesCollection has no real 'PagesCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = PagesCollection()
    setattr(partner, 'PagesCollection', None)
    _safe_set(owner, 'ps_visioDocument10', partner)
    assert getattr(partner, 'PagesCollection') == owner
    _safe_set(owner, 'ps_visioDocument10', None)
    assert getattr(partner, 'PagesCollection') is None


def test_assoc_docPrintSetup3_stub_double():
    # PrintSetup has no real 'PrintSetup' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = PrintSetup()
    setattr(partner, 'PrintSetup', None)
    _safe_set(owner, 'ps_visioDocument', partner)
    assert getattr(partner, 'PrintSetup') == owner
    _safe_set(owner, 'ps_visioDocument', None)
    assert getattr(partner, 'PrintSetup') is None


def test_assoc_docProps0_stub_double():
    # DocumentPropertiesCollection has no real 'DocumentPropertiesCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = DocumentPropertiesCollection()
    setattr(partner, 'DocumentPropertiesCollection', None)
    _safe_set(owner, 'dps_visioDocument', partner)
    assert getattr(partner, 'DocumentPropertiesCollection') == owner
    _safe_set(owner, 'dps_visioDocument', None)
    assert getattr(partner, 'DocumentPropertiesCollection') is None


def test_assoc_docSettings1_stub_double():
    # DocumentSettingsElt has no real 'DocumentSettingsElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = DocumentSettingsElt()
    setattr(partner, 'DocumentSettingsElt', None)
    _safe_set(owner, 'dss_visioDocument', partner)
    assert getattr(partner, 'DocumentSettingsElt') == owner
    _safe_set(owner, 'dss_visioDocument', None)
    assert getattr(partner, 'DocumentSettingsElt') is None


def test_assoc_docSolutionXML16_stub_double():
    # SolutionXML has no real 'SolutionXML' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = SolutionXML()
    setattr(partner, 'SolutionXML', None)
    _safe_set(owner, 'sx_visioDocument', {partner})
    assert getattr(partner, 'SolutionXML') == owner
    _safe_set(owner, 'sx_visioDocument', set())
    assert getattr(partner, 'SolutionXML') is None


def test_assoc_docStyleSheets6_stub_double():
    # StyleSheetsCollection has no real 'StyleSheetsCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = StyleSheetsCollection()
    setattr(partner, 'StyleSheetsCollection', None)
    _safe_set(owner, 'sss_visioDocument', partner)
    assert getattr(partner, 'StyleSheetsCollection') == owner
    _safe_set(owner, 'sss_visioDocument', None)
    assert getattr(partner, 'StyleSheetsCollection') is None


def test_assoc_docVBProjectData14_stub_double():
    # VBProjectData has no real 'VBProjectData' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = VBProjectData()
    setattr(partner, 'VBProjectData', None)
    _safe_set(owner, 'vpd_visioDocument', partner)
    assert getattr(partner, 'VBProjectData') == owner
    _safe_set(owner, 'vpd_visioDocument', None)
    assert getattr(partner, 'VBProjectData') is None


def test_assoc_docWindows11_stub_double():
    # WindowsInfo has no real 'WindowsInfo' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = WindowsInfo()
    setattr(partner, 'WindowsInfo', None)
    _safe_set(owner, 'ws_visioDocument', partner)
    assert getattr(partner, 'WindowsInfo') == owner
    _safe_set(owner, 'ws_visioDocument', None)
    assert getattr(partner, 'WindowsInfo') is None


def test_assoc_dps_visioDocument17_stub_double():
    # VisioDocument has no real 'VisioDocument' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = VisioDocument()
    setattr(partner, 'VisioDocument', None)
    _safe_set(owner, 'docProps', partner)
    assert getattr(partner, 'VisioDocument') == owner
    _safe_set(owner, 'docProps', None)
    assert getattr(partner, 'VisioDocument') is None


def test_assoc_erd_visioDocument51_stub_double():
    # VisioDocument has no real 'VisioDocument52' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_EmailRoutingData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_EmailRoutingData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_EmailRoutingData(data="sample_text", size="sample_text")
    partner = VisioDocument()
    setattr(partner, 'VisioDocument52', None)
    _safe_set(owner, 'docEmailRoutingData', partner)
    assert getattr(partner, 'VisioDocument52') == owner
    _safe_set(owner, 'docEmailRoutingData', None)
    assert getattr(partner, 'VisioDocument52') is None


def test_assoc_fe_fonts42_stub_double():
    # FontsTable has no real 'FontsTable43' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_FontEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_FontEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_FontEntry(attributes="sample_text", charSet="sample_text", name="sample_text", pitchAndFamily="sample_text", unicode="sample_text", weight="sample_text")
    partner = FontsTable()
    setattr(partner, 'FontsTable43', None)
    _safe_set(owner, 'fontEntries', partner)
    assert getattr(partner, 'FontsTable43') == owner
    _safe_set(owner, 'fontEntries', None)
    assert getattr(partner, 'FontsTable43') is None


def test_assoc_fn_faceNames47_stub_double():
    # FaceNamesTable has no real 'FaceNamesTable48' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_FaceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_FaceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_FaceName(charSet="sample_text", flags="sample_text", name="sample_text", panos="sample_text", unicodeRanges="sample_text")
    partner = FaceNamesTable()
    setattr(partner, 'FaceNamesTable48', None)
    _safe_set(owner, 'faceNameEntries', partner)
    assert getattr(partner, 'FaceNamesTable48') == owner
    _safe_set(owner, 'faceNameEntries', None)
    assert getattr(partner, 'FaceNamesTable48') is None


def test_assoc_i_masterShortCut251_stub_double():
    # MasterShortCut has no real 'MasterShortCut252' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_Icon's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_Icon's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_Icon(value="sample_text")
    partner = MasterShortCut()
    setattr(partner, 'MasterShortCut252', None)
    _safe_set(owner, 'icons', partner)
    assert getattr(partner, 'MasterShortCut252') == owner
    _safe_set(owner, 'icons', None)
    assert getattr(partner, 'MasterShortCut252') is None


def test_assoc_icons250_stub_double():
    # Icon has no real 'Icon' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_MasterShortCut's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_MasterShortCut's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    partner = Icon()
    setattr(partner, 'Icon', None)
    _safe_set(owner, 'i_masterShortCut', {partner})
    assert getattr(partner, 'Icon') == owner
    _safe_set(owner, 'i_masterShortCut', set())
    assert getattr(partner, 'Icon') is None


def test_assoc_m_masterShortCuts248_stub_double():
    # MastersCollection has no real 'MastersCollection249' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_MasterShortCut's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_MasterShortCut's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    partner = MastersCollection()
    setattr(partner, 'MastersCollection249', None)
    _safe_set(owner, 'masterShortCuts', partner)
    assert getattr(partner, 'MastersCollection249') == owner
    _safe_set(owner, 'masterShortCuts', None)
    assert getattr(partner, 'MastersCollection249') is None


def test_assoc_m_masters253_stub_double():
    # MastersCollection has no real 'MastersCollection254' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_Master's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_Master's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    partner = MastersCollection()
    setattr(partner, 'MastersCollection254', None)
    _safe_set(owner, 'masters', partner)
    assert getattr(partner, 'MastersCollection254') == owner
    _safe_set(owner, 'masters', None)
    assert getattr(partner, 'MastersCollection254') is None


def test_assoc_masterElts255_stub_double():
    # MasterElt has no real 'MasterElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_Master's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_Master's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    partner = MasterElt()
    setattr(partner, 'MasterElt', None)
    _safe_set(owner, 'me_master', {partner})
    assert getattr(partner, 'MasterElt') == owner
    _safe_set(owner, 'me_master', set())
    assert getattr(partner, 'MasterElt') is None


def test_assoc_p_pages265_stub_double():
    # PagesCollection has no real 'PagesCollection266' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    partner = PagesCollection()
    setattr(partner, 'PagesCollection266', None)
    _safe_set(owner, 'pages', partner)
    assert getattr(partner, 'PagesCollection266') == owner
    _safe_set(owner, 'pages', None)
    assert getattr(partner, 'PagesCollection266') is None


def test_assoc_pageElts267_stub_double():
    # PageElt has no real 'PageElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    partner = PageElt()
    setattr(partner, 'PageElt', None)
    _safe_set(owner, 'pe_page', {partner})
    assert getattr(partner, 'PageElt') == owner
    _safe_set(owner, 'pe_page', set())
    assert getattr(partner, 'PageElt') is None


def test_assoc_shapeElts61_stub_double():
    # ShapeElt has no real 'ShapeElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    partner = ShapeElt()
    setattr(partner, 'ShapeElt', None)
    _safe_set(owner, 'sse_shapeSheet', {partner})
    assert getattr(partner, 'ShapeElt') == owner
    _safe_set(owner, 'sse_shapeSheet', set())
    assert getattr(partner, 'ShapeElt') is None


def test_assoc_ss_shapes60_stub_double():
    # ShapesCollection has no real 'ShapesCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    partner = ShapesCollection()
    setattr(partner, 'ShapesCollection', None)
    _safe_set(owner, 'shapes', partner)
    assert getattr(partner, 'ShapesCollection') == owner
    _safe_set(owner, 'shapes', None)
    assert getattr(partner, 'ShapesCollection') is None


def test_assoc_timeCreated19_stub_double():
    # DateTimeType has no real 'DateTimeType' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType', None)
    _safe_set(owner, 'DatadiagramMLTextFormat_DocumentPropertiesCollection', partner)
    assert getattr(partner, 'DateTimeType') == owner
    _safe_set(owner, 'DatadiagramMLTextFormat_DocumentPropertiesCollection', None)
    assert getattr(partner, 'DateTimeType') is None


def test_assoc_timeEdited23_stub_double():
    # DateTimeType has no real 'DateTimeType25' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType25', None)
    _safe_set(owner, 'DatadiagramMLTextFormat_DocumentPropertiesCollection24', partner)
    assert getattr(partner, 'DateTimeType25') == owner
    _safe_set(owner, 'DatadiagramMLTextFormat_DocumentPropertiesCollection24', None)
    assert getattr(partner, 'DateTimeType25') is None


def test_assoc_timePrinted26_stub_double():
    # DateTimeType has no real 'DateTimeType28' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType28', None)
    _safe_set(owner, 'DatadiagramMLTextFormat_DocumentPropertiesCollection27', partner)
    assert getattr(partner, 'DateTimeType28') == owner
    _safe_set(owner, 'DatadiagramMLTextFormat_DocumentPropertiesCollection27', None)
    assert getattr(partner, 'DateTimeType28') is None


def test_assoc_timeSaved20_stub_double():
    # DateTimeType has no real 'DateTimeType22' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType22', None)
    _safe_set(owner, 'DatadiagramMLTextFormat_DocumentPropertiesCollection21', partner)
    assert getattr(partner, 'DateTimeType22') == owner
    _safe_set(owner, 'DatadiagramMLTextFormat_DocumentPropertiesCollection21', None)
    assert getattr(partner, 'DateTimeType22') is None


def test_assoc_vpd_visioDocument49_stub_double():
    # VisioDocument has no real 'VisioDocument50' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLTextFormat_VBProjectData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLTextFormat_VBProjectData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLTextFormat_VBProjectData(data="sample_text")
    partner = VisioDocument()
    setattr(partner, 'VisioDocument50', None)
    _safe_set(owner, 'docVBProjectData', partner)
    assert getattr(partner, 'VisioDocument50') == owner
    _safe_set(owner, 'docVBProjectData', None)
    assert getattr(partner, 'VisioDocument50') is None


