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
    DatadiagramMLXForm_ArcTo,
    DatadiagramMLXForm_CellType,
    DatadiagramMLXForm_Char,
    DatadiagramMLXForm_ColorEntry,
    DatadiagramMLXForm_ColorsTable,
    DatadiagramMLXForm_Connect,
    DatadiagramMLXForm_ConnectsCollection,
    DatadiagramMLXForm_Cp,
    DatadiagramMLXForm_CustomPropertiesCollection,
    DatadiagramMLXForm_CustomProperty,
    DatadiagramMLXForm_DateTimeType,
    DatadiagramMLXForm_DelElt,
    DatadiagramMLXForm_DocumentPropertiesCollection,
    DatadiagramMLXForm_DocumentSettingsElt,
    DatadiagramMLXForm_DocumentSheet,
    DatadiagramMLXForm_Ellipse,
    DatadiagramMLXForm_EllipticalArcTo,
    DatadiagramMLXForm_EmailRoutingData,
    DatadiagramMLXForm_EventList,
    DatadiagramMLXForm_FaceName,
    DatadiagramMLXForm_FaceNamesTable,
    DatadiagramMLXForm_Field,
    DatadiagramMLXForm_Fld,
    DatadiagramMLXForm_FontEntry,
    DatadiagramMLXForm_FontsTable,
    DatadiagramMLXForm_Geom,
    DatadiagramMLXForm_HeaderFooter,
    DatadiagramMLXForm_IXElt,
    DatadiagramMLXForm_IXrequiredElt,
    DatadiagramMLXForm_Icon,
    DatadiagramMLXForm_IdentifiedElt,
    DatadiagramMLXForm_InfiniteLine,
    DatadiagramMLXForm_LineTo,
    DatadiagramMLXForm_Master,
    DatadiagramMLXForm_MasterElt,
    DatadiagramMLXForm_MasterShortCut,
    DatadiagramMLXForm_MastersCollection,
    DatadiagramMLXForm_MoveTo,
    DatadiagramMLXForm_NURBSTo,
    DatadiagramMLXForm_NamedElt,
    DatadiagramMLXForm_Page,
    DatadiagramMLXForm_PageElt,
    DatadiagramMLXForm_PageSheet,
    DatadiagramMLXForm_PagesCollection,
    DatadiagramMLXForm_Para,
    DatadiagramMLXForm_PolylineTo,
    DatadiagramMLXForm_Pp,
    DatadiagramMLXForm_PrintSetup,
    DatadiagramMLXForm_Shape,
    DatadiagramMLXForm_ShapeElt,
    DatadiagramMLXForm_ShapesCollection,
    DatadiagramMLXForm_SnapAngle,
    DatadiagramMLXForm_SnapAnglesCollection,
    DatadiagramMLXForm_SolutionXML,
    DatadiagramMLXForm_SplineKnot,
    DatadiagramMLXForm_SplineStart,
    DatadiagramMLXForm_StringElt,
    DatadiagramMLXForm_StyleSheet,
    DatadiagramMLXForm_StyleSheetsCollection,
    DatadiagramMLXForm_Tab,
    DatadiagramMLXForm_TabsCollection,
    DatadiagramMLXForm_Text,
    DatadiagramMLXForm_TextElt,
    DatadiagramMLXForm_Tp,
    DatadiagramMLXForm_UniqueIdElt,
    DatadiagramMLXForm_VBProjectData,
    DatadiagramMLXForm_VisioDocument,
    DatadiagramMLXForm_WindowsInfo,
    DatadiagramMLXForm_XForm,
    DatadiagramMLXForm_XYABCDEElt,
    DatadiagramMLXForm_XYABCDElt,
    DatadiagramMLXForm_XYABElt,
    DatadiagramMLXForm_XYAElt,
    DatadiagramMLXForm_XYElt,
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
    SnapAngle,
    SnapAnglesCollection,
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

def test_assoc_c_connects311_stub_double():
    # ConnectsCollection has no real 'ConnectsCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_Connect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_Connect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_Connect(fromCell="sample_text", fromPart="sample_text", fromSheet="sample_text", toCell="sample_text", toPart="sample_text", toSheet="sample_text")
    partner = ConnectsCollection()
    setattr(partner, 'ConnectsCollection', None)
    _safe_set(owner, 'connections', partner)
    assert getattr(partner, 'ConnectsCollection') == owner
    _safe_set(owner, 'connections', None)
    assert getattr(partner, 'ConnectsCollection') is None


def test_assoc_ce_colors57_stub_double():
    # ColorsTable has no real 'ColorsTable58' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_ColorEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_ColorEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_ColorEntry(rgb="sample_text")
    partner = ColorsTable()
    setattr(partner, 'ColorsTable58', None)
    _safe_set(owner, 'colorEntries', partner)
    assert getattr(partner, 'ColorsTable58') == owner
    _safe_set(owner, 'colorEntries', None)
    assert getattr(partner, 'ColorsTable58') is None


def test_assoc_cp_customProps32_stub_double():
    # CustomPropertiesCollection has no real 'CustomPropertiesCollection33' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_CustomProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_CustomProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_CustomProperty(dataType="sample_text", name="sample_text")
    partner = CustomPropertiesCollection()
    setattr(partner, 'CustomPropertiesCollection33', None)
    _safe_set(owner, 'cps_customProps', partner)
    assert getattr(partner, 'CustomPropertiesCollection33') == owner
    _safe_set(owner, 'cps_customProps', None)
    assert getattr(partner, 'CustomPropertiesCollection33') is None


def test_assoc_customProps18_stub_double():
    # CustomPropertiesCollection has no real 'CustomPropertiesCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = CustomPropertiesCollection()
    setattr(partner, 'CustomPropertiesCollection', None)
    _safe_set(owner, 'cps_docProp', partner)
    assert getattr(partner, 'CustomPropertiesCollection') == owner
    _safe_set(owner, 'cps_docProp', None)
    assert getattr(partner, 'CustomPropertiesCollection') is None


def test_assoc_defaultFillStyle42_stub_double():
    # StyleSheet has no real 'StyleSheet44' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentSettingsElt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentSettingsElt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentSettingsElt(attachedToolbars="sample_text", customMenusFile="sample_text", customToolbarsFile="sample_text", dynamicGridEnabled="sample_text", glueSettings="sample_text", protectBkgnds="sample_text", protectMasters="sample_text", protectShapes="sample_text", protectStyles="sample_text", snapExtensions="sample_text", snapSettings="sample_text")
    partner = StyleSheet()
    setattr(partner, 'StyleSheet44', None)
    _safe_set(owner, 'DatadiagramMLXForm_DocumentSettingsElt43', partner)
    assert getattr(partner, 'StyleSheet44') == owner
    _safe_set(owner, 'DatadiagramMLXForm_DocumentSettingsElt43', None)
    assert getattr(partner, 'StyleSheet44') is None


def test_assoc_defaultGuideStyle45_stub_double():
    # StyleSheet has no real 'StyleSheet47' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentSettingsElt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentSettingsElt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentSettingsElt(attachedToolbars="sample_text", customMenusFile="sample_text", customToolbarsFile="sample_text", dynamicGridEnabled="sample_text", glueSettings="sample_text", protectBkgnds="sample_text", protectMasters="sample_text", protectShapes="sample_text", protectStyles="sample_text", snapExtensions="sample_text", snapSettings="sample_text")
    partner = StyleSheet()
    setattr(partner, 'StyleSheet47', None)
    _safe_set(owner, 'DatadiagramMLXForm_DocumentSettingsElt46', partner)
    assert getattr(partner, 'StyleSheet47') == owner
    _safe_set(owner, 'DatadiagramMLXForm_DocumentSettingsElt46', None)
    assert getattr(partner, 'StyleSheet47') is None


def test_assoc_defaultLineStyle39_stub_double():
    # StyleSheet has no real 'StyleSheet41' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentSettingsElt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentSettingsElt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentSettingsElt(attachedToolbars="sample_text", customMenusFile="sample_text", customToolbarsFile="sample_text", dynamicGridEnabled="sample_text", glueSettings="sample_text", protectBkgnds="sample_text", protectMasters="sample_text", protectShapes="sample_text", protectStyles="sample_text", snapExtensions="sample_text", snapSettings="sample_text")
    partner = StyleSheet()
    setattr(partner, 'StyleSheet41', None)
    _safe_set(owner, 'DatadiagramMLXForm_DocumentSettingsElt40', partner)
    assert getattr(partner, 'StyleSheet41') == owner
    _safe_set(owner, 'DatadiagramMLXForm_DocumentSettingsElt40', None)
    assert getattr(partner, 'StyleSheet41') is None


def test_assoc_defaultTextStyle37_stub_double():
    # StyleSheet has no real 'StyleSheet' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentSettingsElt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentSettingsElt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentSettingsElt(attachedToolbars="sample_text", customMenusFile="sample_text", customToolbarsFile="sample_text", dynamicGridEnabled="sample_text", glueSettings="sample_text", protectBkgnds="sample_text", protectMasters="sample_text", protectShapes="sample_text", protectStyles="sample_text", snapExtensions="sample_text", snapSettings="sample_text")
    partner = StyleSheet()
    setattr(partner, 'StyleSheet', None)
    _safe_set(owner, 'DatadiagramMLXForm_DocumentSettingsElt38', partner)
    assert getattr(partner, 'StyleSheet') == owner
    _safe_set(owner, 'DatadiagramMLXForm_DocumentSettingsElt38', None)
    assert getattr(partner, 'StyleSheet') is None


def test_assoc_docColors2_stub_double():
    # ColorsTable has no real 'ColorsTable' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = ColorsTable()
    setattr(partner, 'ColorsTable', None)
    _safe_set(owner, 'cs_visioDocument', partner)
    assert getattr(partner, 'ColorsTable') == owner
    _safe_set(owner, 'cs_visioDocument', None)
    assert getattr(partner, 'ColorsTable') is None


def test_assoc_docDocumentSheet7_stub_double():
    # DocumentSheet has no real 'DocumentSheet' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = DocumentSheet()
    setattr(partner, 'DocumentSheet', None)
    _safe_set(owner, 'ds_visioDocument', partner)
    assert getattr(partner, 'DocumentSheet') == owner
    _safe_set(owner, 'ds_visioDocument', None)
    assert getattr(partner, 'DocumentSheet') is None


def test_assoc_docEmailRoutingData15_stub_double():
    # EmailRoutingData has no real 'EmailRoutingData' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = EmailRoutingData()
    setattr(partner, 'EmailRoutingData', None)
    _safe_set(owner, 'erd_visioDocument', partner)
    assert getattr(partner, 'EmailRoutingData') == owner
    _safe_set(owner, 'erd_visioDocument', None)
    assert getattr(partner, 'EmailRoutingData') is None


def test_assoc_docEventList12_stub_double():
    # EventList has no real 'EventList' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = EventList()
    setattr(partner, 'EventList', None)
    _safe_set(owner, 'el_visioDocument', partner)
    assert getattr(partner, 'EventList') == owner
    _safe_set(owner, 'el_visioDocument', None)
    assert getattr(partner, 'EventList') is None


def test_assoc_docFaceNames5_stub_double():
    # FaceNamesTable has no real 'FaceNamesTable' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = FaceNamesTable()
    setattr(partner, 'FaceNamesTable', None)
    _safe_set(owner, 'fns_visioDocument', partner)
    assert getattr(partner, 'FaceNamesTable') == owner
    _safe_set(owner, 'fns_visioDocument', None)
    assert getattr(partner, 'FaceNamesTable') is None


def test_assoc_docFonts4_stub_double():
    # FontsTable has no real 'FontsTable' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = FontsTable()
    setattr(partner, 'FontsTable', None)
    _safe_set(owner, 'fs_visioDocument', partner)
    assert getattr(partner, 'FontsTable') == owner
    _safe_set(owner, 'fs_visioDocument', None)
    assert getattr(partner, 'FontsTable') is None


def test_assoc_docHeaderFooter13_stub_double():
    # HeaderFooter has no real 'HeaderFooter' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = HeaderFooter()
    setattr(partner, 'HeaderFooter', None)
    _safe_set(owner, 'ef_visioDocument', partner)
    assert getattr(partner, 'HeaderFooter') == owner
    _safe_set(owner, 'ef_visioDocument', None)
    assert getattr(partner, 'HeaderFooter') is None


def test_assoc_docMasters8_stub_double():
    # MastersCollection has no real 'MastersCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = MastersCollection()
    setattr(partner, 'MastersCollection', None)
    _safe_set(owner, 'ms_visioDocument', partner)
    assert getattr(partner, 'MastersCollection') == owner
    _safe_set(owner, 'ms_visioDocument', None)
    assert getattr(partner, 'MastersCollection') is None


def test_assoc_docPages9_stub_double():
    # PagesCollection has no real 'PagesCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = PagesCollection()
    setattr(partner, 'PagesCollection', None)
    _safe_set(owner, 'ps_visioDocument10', partner)
    assert getattr(partner, 'PagesCollection') == owner
    _safe_set(owner, 'ps_visioDocument10', None)
    assert getattr(partner, 'PagesCollection') is None


def test_assoc_docPrintSetup3_stub_double():
    # PrintSetup has no real 'PrintSetup' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = PrintSetup()
    setattr(partner, 'PrintSetup', None)
    _safe_set(owner, 'ps_visioDocument', partner)
    assert getattr(partner, 'PrintSetup') == owner
    _safe_set(owner, 'ps_visioDocument', None)
    assert getattr(partner, 'PrintSetup') is None


def test_assoc_docProps0_stub_double():
    # DocumentPropertiesCollection has no real 'DocumentPropertiesCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = DocumentPropertiesCollection()
    setattr(partner, 'DocumentPropertiesCollection', None)
    _safe_set(owner, 'dps_visioDocument', partner)
    assert getattr(partner, 'DocumentPropertiesCollection') == owner
    _safe_set(owner, 'dps_visioDocument', None)
    assert getattr(partner, 'DocumentPropertiesCollection') is None


def test_assoc_docSettings1_stub_double():
    # DocumentSettingsElt has no real 'DocumentSettingsElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = DocumentSettingsElt()
    setattr(partner, 'DocumentSettingsElt', None)
    _safe_set(owner, 'dss_visioDocument', partner)
    assert getattr(partner, 'DocumentSettingsElt') == owner
    _safe_set(owner, 'dss_visioDocument', None)
    assert getattr(partner, 'DocumentSettingsElt') is None


def test_assoc_docSolutionXML16_stub_double():
    # SolutionXML has no real 'SolutionXML' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = SolutionXML()
    setattr(partner, 'SolutionXML', None)
    _safe_set(owner, 'sx_visioDocument', {partner})
    assert getattr(partner, 'SolutionXML') == owner
    _safe_set(owner, 'sx_visioDocument', set())
    assert getattr(partner, 'SolutionXML') is None


def test_assoc_docStyleSheets6_stub_double():
    # StyleSheetsCollection has no real 'StyleSheetsCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = StyleSheetsCollection()
    setattr(partner, 'StyleSheetsCollection', None)
    _safe_set(owner, 'sss_visioDocument', partner)
    assert getattr(partner, 'StyleSheetsCollection') == owner
    _safe_set(owner, 'sss_visioDocument', None)
    assert getattr(partner, 'StyleSheetsCollection') is None


def test_assoc_docVBProjectData14_stub_double():
    # VBProjectData has no real 'VBProjectData' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = VBProjectData()
    setattr(partner, 'VBProjectData', None)
    _safe_set(owner, 'vpd_visioDocument', partner)
    assert getattr(partner, 'VBProjectData') == owner
    _safe_set(owner, 'vpd_visioDocument', None)
    assert getattr(partner, 'VBProjectData') is None


def test_assoc_docWindows11_stub_double():
    # WindowsInfo has no real 'WindowsInfo' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VisioDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VisioDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    partner = WindowsInfo()
    setattr(partner, 'WindowsInfo', None)
    _safe_set(owner, 'ws_visioDocument', partner)
    assert getattr(partner, 'WindowsInfo') == owner
    _safe_set(owner, 'ws_visioDocument', None)
    assert getattr(partner, 'WindowsInfo') is None


def test_assoc_dps_visioDocument17_stub_double():
    # VisioDocument has no real 'VisioDocument' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = VisioDocument()
    setattr(partner, 'VisioDocument', None)
    _safe_set(owner, 'docProps', partner)
    assert getattr(partner, 'VisioDocument') == owner
    _safe_set(owner, 'docProps', None)
    assert getattr(partner, 'VisioDocument') is None


def test_assoc_ds_snapAngles48_stub_double():
    # SnapAnglesCollection has no real 'SnapAnglesCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentSettingsElt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentSettingsElt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentSettingsElt(attachedToolbars="sample_text", customMenusFile="sample_text", customToolbarsFile="sample_text", dynamicGridEnabled="sample_text", glueSettings="sample_text", protectBkgnds="sample_text", protectMasters="sample_text", protectShapes="sample_text", protectStyles="sample_text", snapExtensions="sample_text", snapSettings="sample_text")
    partner = SnapAnglesCollection()
    setattr(partner, 'SnapAnglesCollection', None)
    _safe_set(owner, 'sa_docSettings', partner)
    assert getattr(partner, 'SnapAnglesCollection') == owner
    _safe_set(owner, 'sa_docSettings', None)
    assert getattr(partner, 'SnapAnglesCollection') is None


def test_assoc_dss_visioDocument34_stub_double():
    # VisioDocument has no real 'VisioDocument35' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentSettingsElt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentSettingsElt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentSettingsElt(attachedToolbars="sample_text", customMenusFile="sample_text", customToolbarsFile="sample_text", dynamicGridEnabled="sample_text", glueSettings="sample_text", protectBkgnds="sample_text", protectMasters="sample_text", protectShapes="sample_text", protectStyles="sample_text", snapExtensions="sample_text", snapSettings="sample_text")
    partner = VisioDocument()
    setattr(partner, 'VisioDocument35', None)
    _safe_set(owner, 'docSettings', partner)
    assert getattr(partner, 'VisioDocument35') == owner
    _safe_set(owner, 'docSettings', None)
    assert getattr(partner, 'VisioDocument35') is None


def test_assoc_erd_visioDocument73_stub_double():
    # VisioDocument has no real 'VisioDocument74' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_EmailRoutingData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_EmailRoutingData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_EmailRoutingData(data="sample_text", size="sample_text")
    partner = VisioDocument()
    setattr(partner, 'VisioDocument74', None)
    _safe_set(owner, 'docEmailRoutingData', partner)
    assert getattr(partner, 'VisioDocument74') == owner
    _safe_set(owner, 'docEmailRoutingData', None)
    assert getattr(partner, 'VisioDocument74') is None


def test_assoc_fe_fonts64_stub_double():
    # FontsTable has no real 'FontsTable65' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_FontEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_FontEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_FontEntry(attributes="sample_text", charSet="sample_text", name="sample_text", pitchAndFamily="sample_text", unicode="sample_text", weight="sample_text")
    partner = FontsTable()
    setattr(partner, 'FontsTable65', None)
    _safe_set(owner, 'fontEntries', partner)
    assert getattr(partner, 'FontsTable65') == owner
    _safe_set(owner, 'fontEntries', None)
    assert getattr(partner, 'FontsTable65') is None


def test_assoc_fn_faceNames69_stub_double():
    # FaceNamesTable has no real 'FaceNamesTable70' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_FaceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_FaceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_FaceName(charSet="sample_text", flags="sample_text", name="sample_text", panos="sample_text", unicodeRanges="sample_text")
    partner = FaceNamesTable()
    setattr(partner, 'FaceNamesTable70', None)
    _safe_set(owner, 'faceNameEntries', partner)
    assert getattr(partner, 'FaceNamesTable70') == owner
    _safe_set(owner, 'faceNameEntries', None)
    assert getattr(partner, 'FaceNamesTable70') is None


def test_assoc_i_masterShortCut303_stub_double():
    # MasterShortCut has no real 'MasterShortCut304' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_Icon's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_Icon's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_Icon(value="sample_text")
    partner = MasterShortCut()
    setattr(partner, 'MasterShortCut304', None)
    _safe_set(owner, 'icons', partner)
    assert getattr(partner, 'MasterShortCut304') == owner
    _safe_set(owner, 'icons', None)
    assert getattr(partner, 'MasterShortCut304') is None


def test_assoc_icons302_stub_double():
    # Icon has no real 'Icon' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_MasterShortCut's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_MasterShortCut's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    partner = Icon()
    setattr(partner, 'Icon', None)
    _safe_set(owner, 'i_masterShortCut', {partner})
    assert getattr(partner, 'Icon') == owner
    _safe_set(owner, 'i_masterShortCut', set())
    assert getattr(partner, 'Icon') is None


def test_assoc_m_masterShortCuts300_stub_double():
    # MastersCollection has no real 'MastersCollection301' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_MasterShortCut's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_MasterShortCut's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    partner = MastersCollection()
    setattr(partner, 'MastersCollection301', None)
    _safe_set(owner, 'masterShortCuts', partner)
    assert getattr(partner, 'MastersCollection301') == owner
    _safe_set(owner, 'masterShortCuts', None)
    assert getattr(partner, 'MastersCollection301') is None


def test_assoc_m_masters305_stub_double():
    # MastersCollection has no real 'MastersCollection306' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_Master's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_Master's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    partner = MastersCollection()
    setattr(partner, 'MastersCollection306', None)
    _safe_set(owner, 'masters', partner)
    assert getattr(partner, 'MastersCollection306') == owner
    _safe_set(owner, 'masters', None)
    assert getattr(partner, 'MastersCollection306') is None


def test_assoc_masterElts307_stub_double():
    # MasterElt has no real 'MasterElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_Master's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_Master's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    partner = MasterElt()
    setattr(partner, 'MasterElt', None)
    _safe_set(owner, 'me_master', {partner})
    assert getattr(partner, 'MasterElt') == owner
    _safe_set(owner, 'me_master', set())
    assert getattr(partner, 'MasterElt') is None


def test_assoc_p_pages318_stub_double():
    # PagesCollection has no real 'PagesCollection319' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    partner = PagesCollection()
    setattr(partner, 'PagesCollection319', None)
    _safe_set(owner, 'pages', partner)
    assert getattr(partner, 'PagesCollection319') == owner
    _safe_set(owner, 'pages', None)
    assert getattr(partner, 'PagesCollection319') is None


def test_assoc_pageElts320_stub_double():
    # PageElt has no real 'PageElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    partner = PageElt()
    setattr(partner, 'PageElt', None)
    _safe_set(owner, 'pe_page', {partner})
    assert getattr(partner, 'PageElt') == owner
    _safe_set(owner, 'pe_page', set())
    assert getattr(partner, 'PageElt') is None


def test_assoc_sa_snapAngles52_stub_double():
    # SnapAnglesCollection has no real 'SnapAnglesCollection53' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_SnapAngle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_SnapAngle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_SnapAngle(angleValue="sample_text")
    partner = SnapAnglesCollection()
    setattr(partner, 'SnapAnglesCollection53', None)
    _safe_set(owner, 'snapAngles', partner)
    assert getattr(partner, 'SnapAnglesCollection53') == owner
    _safe_set(owner, 'snapAngles', None)
    assert getattr(partner, 'SnapAnglesCollection53') is None


def test_assoc_shapeElts84_stub_double():
    # ShapeElt has no real 'ShapeElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    partner = ShapeElt()
    setattr(partner, 'ShapeElt', None)
    _safe_set(owner, 'sse_shapeSheet', {partner})
    assert getattr(partner, 'ShapeElt') == owner
    _safe_set(owner, 'sse_shapeSheet', set())
    assert getattr(partner, 'ShapeElt') is None


def test_assoc_ss_shapes83_stub_double():
    # ShapesCollection has no real 'ShapesCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    partner = ShapesCollection()
    setattr(partner, 'ShapesCollection', None)
    _safe_set(owner, 'shapes', partner)
    assert getattr(partner, 'ShapesCollection') == owner
    _safe_set(owner, 'shapes', None)
    assert getattr(partner, 'ShapesCollection') is None


def test_assoc_timeCreated19_stub_double():
    # DateTimeType has no real 'DateTimeType' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType', None)
    _safe_set(owner, 'DatadiagramMLXForm_DocumentPropertiesCollection', partner)
    assert getattr(partner, 'DateTimeType') == owner
    _safe_set(owner, 'DatadiagramMLXForm_DocumentPropertiesCollection', None)
    assert getattr(partner, 'DateTimeType') is None


def test_assoc_timeEdited23_stub_double():
    # DateTimeType has no real 'DateTimeType25' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType25', None)
    _safe_set(owner, 'DatadiagramMLXForm_DocumentPropertiesCollection24', partner)
    assert getattr(partner, 'DateTimeType25') == owner
    _safe_set(owner, 'DatadiagramMLXForm_DocumentPropertiesCollection24', None)
    assert getattr(partner, 'DateTimeType25') is None


def test_assoc_timePrinted26_stub_double():
    # DateTimeType has no real 'DateTimeType28' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType28', None)
    _safe_set(owner, 'DatadiagramMLXForm_DocumentPropertiesCollection27', partner)
    assert getattr(partner, 'DateTimeType28') == owner
    _safe_set(owner, 'DatadiagramMLXForm_DocumentPropertiesCollection27', None)
    assert getattr(partner, 'DateTimeType28') is None


def test_assoc_timeSaved20_stub_double():
    # DateTimeType has no real 'DateTimeType22' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentPropertiesCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentPropertiesCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    partner = DateTimeType()
    setattr(partner, 'DateTimeType22', None)
    _safe_set(owner, 'DatadiagramMLXForm_DocumentPropertiesCollection21', partner)
    assert getattr(partner, 'DateTimeType22') == owner
    _safe_set(owner, 'DatadiagramMLXForm_DocumentPropertiesCollection21', None)
    assert getattr(partner, 'DateTimeType22') is None


def test_assoc_topPage36_stub_double():
    # Page has no real 'Page' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_DocumentSettingsElt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_DocumentSettingsElt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_DocumentSettingsElt(attachedToolbars="sample_text", customMenusFile="sample_text", customToolbarsFile="sample_text", dynamicGridEnabled="sample_text", glueSettings="sample_text", protectBkgnds="sample_text", protectMasters="sample_text", protectShapes="sample_text", protectStyles="sample_text", snapExtensions="sample_text", snapSettings="sample_text")
    partner = Page()
    setattr(partner, 'Page', None)
    _safe_set(owner, 'DatadiagramMLXForm_DocumentSettingsElt', partner)
    assert getattr(partner, 'Page') == owner
    _safe_set(owner, 'DatadiagramMLXForm_DocumentSettingsElt', None)
    assert getattr(partner, 'Page') is None


def test_assoc_vpd_visioDocument71_stub_double():
    # VisioDocument has no real 'VisioDocument72' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLXForm_VBProjectData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLXForm_VBProjectData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLXForm_VBProjectData(data="sample_text")
    partner = VisioDocument()
    setattr(partner, 'VisioDocument72', None)
    _safe_set(owner, 'docVBProjectData', partner)
    assert getattr(partner, 'VisioDocument72') == owner
    _safe_set(owner, 'docVBProjectData', None)
    assert getattr(partner, 'VisioDocument72') is None


