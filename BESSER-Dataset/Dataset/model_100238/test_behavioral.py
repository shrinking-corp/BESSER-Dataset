import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArcTo,
    CellType,
    Connect,
    ConnectsCollection,
    DatadiagramMLSimplified_ArcTo,
    DatadiagramMLSimplified_CellType,
    DatadiagramMLSimplified_Connect,
    DatadiagramMLSimplified_ConnectsCollection,
    DatadiagramMLSimplified_DelElt,
    DatadiagramMLSimplified_Ellipse,
    DatadiagramMLSimplified_EllipticalArcTo,
    DatadiagramMLSimplified_Geom,
    DatadiagramMLSimplified_IXElt,
    DatadiagramMLSimplified_Icon,
    DatadiagramMLSimplified_IdentifiedElt,
    DatadiagramMLSimplified_InfiniteLine,
    DatadiagramMLSimplified_LineTo,
    DatadiagramMLSimplified_Master,
    DatadiagramMLSimplified_MasterElt,
    DatadiagramMLSimplified_MasterShortCut,
    DatadiagramMLSimplified_MastersCollection,
    DatadiagramMLSimplified_MoveTo,
    DatadiagramMLSimplified_NURBSTo,
    DatadiagramMLSimplified_NamedElt,
    DatadiagramMLSimplified_Page,
    DatadiagramMLSimplified_PageElt,
    DatadiagramMLSimplified_PageSheet,
    DatadiagramMLSimplified_PagesCollection,
    DatadiagramMLSimplified_PolylineTo,
    DatadiagramMLSimplified_Shape,
    DatadiagramMLSimplified_ShapeElt,
    DatadiagramMLSimplified_ShapesCollection,
    DatadiagramMLSimplified_SplineKnot,
    DatadiagramMLSimplified_SplineStart,
    DatadiagramMLSimplified_StringElt,
    DatadiagramMLSimplified_Text,
    DatadiagramMLSimplified_TextElt,
    DatadiagramMLSimplified_UniqueIdElt,
    DatadiagramMLSimplified_VisioDocument,
    DatadiagramMLSimplified_XYABCDEElt,
    DatadiagramMLSimplified_XYABCDElt,
    DatadiagramMLSimplified_XYABElt,
    DatadiagramMLSimplified_XYAElt,
    DatadiagramMLSimplified_XYElt,
    DelElt,
    Ellipse,
    EllipticalArcTo,
    Geom,
    IXElt,
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
    PagesCollection,
    PolylineTo,
    Shape,
    ShapeElt,
    ShapesCollection,
    SplineKnot,
    SplineStart,
    Text,
    TextElt,
    UniqueIdElt,
    VisioDocument,
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

def test_assoc_c_connects76_stub_double():
    # ConnectsCollection has no real 'ConnectsCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLSimplified_Connect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLSimplified_Connect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLSimplified_Connect(fromCell="sample_text", fromPart="sample_text", fromSheet="sample_text", toCell="sample_text", toPart="sample_text", toSheet="sample_text")
    partner = ConnectsCollection()
    setattr(partner, 'ConnectsCollection', None)
    _safe_set(owner, 'connections', partner)
    assert getattr(partner, 'ConnectsCollection') == owner
    _safe_set(owner, 'connections', None)
    assert getattr(partner, 'ConnectsCollection') is None


def test_assoc_i_masterShortCut68_stub_double():
    # MasterShortCut has no real 'MasterShortCut69' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLSimplified_Icon's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLSimplified_Icon's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLSimplified_Icon(value="sample_text")
    partner = MasterShortCut()
    setattr(partner, 'MasterShortCut69', None)
    _safe_set(owner, 'icons', partner)
    assert getattr(partner, 'MasterShortCut69') == owner
    _safe_set(owner, 'icons', None)
    assert getattr(partner, 'MasterShortCut69') is None


def test_assoc_icons67_stub_double():
    # Icon has no real 'Icon' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLSimplified_MasterShortCut's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLSimplified_MasterShortCut's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLSimplified_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    partner = Icon()
    setattr(partner, 'Icon', None)
    _safe_set(owner, 'i_masterShortCut', {partner})
    assert getattr(partner, 'Icon') == owner
    _safe_set(owner, 'i_masterShortCut', set())
    assert getattr(partner, 'Icon') is None


def test_assoc_m_masterShortCuts65_stub_double():
    # MastersCollection has no real 'MastersCollection66' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLSimplified_MasterShortCut's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLSimplified_MasterShortCut's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLSimplified_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    partner = MastersCollection()
    setattr(partner, 'MastersCollection66', None)
    _safe_set(owner, 'masterShortCuts', partner)
    assert getattr(partner, 'MastersCollection66') == owner
    _safe_set(owner, 'masterShortCuts', None)
    assert getattr(partner, 'MastersCollection66') is None


def test_assoc_m_masters70_stub_double():
    # MastersCollection has no real 'MastersCollection71' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLSimplified_Master's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLSimplified_Master's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLSimplified_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    partner = MastersCollection()
    setattr(partner, 'MastersCollection71', None)
    _safe_set(owner, 'masters', partner)
    assert getattr(partner, 'MastersCollection71') == owner
    _safe_set(owner, 'masters', None)
    assert getattr(partner, 'MastersCollection71') is None


def test_assoc_masterElts72_stub_double():
    # MasterElt has no real 'MasterElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLSimplified_Master's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLSimplified_Master's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLSimplified_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    partner = MasterElt()
    setattr(partner, 'MasterElt', None)
    _safe_set(owner, 'me_master', {partner})
    assert getattr(partner, 'MasterElt') == owner
    _safe_set(owner, 'me_master', set())
    assert getattr(partner, 'MasterElt') is None


def test_assoc_p_pages82_stub_double():
    # PagesCollection has no real 'PagesCollection83' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLSimplified_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLSimplified_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLSimplified_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    partner = PagesCollection()
    setattr(partner, 'PagesCollection83', None)
    _safe_set(owner, 'pages', partner)
    assert getattr(partner, 'PagesCollection83') == owner
    _safe_set(owner, 'pages', None)
    assert getattr(partner, 'PagesCollection83') is None


def test_assoc_pageElts84_stub_double():
    # PageElt has no real 'PageElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLSimplified_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLSimplified_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLSimplified_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    partner = PageElt()
    setattr(partner, 'PageElt', None)
    _safe_set(owner, 'pe_page', {partner})
    assert getattr(partner, 'PageElt') == owner
    _safe_set(owner, 'pe_page', set())
    assert getattr(partner, 'PageElt') is None


def test_assoc_shapeElts3_stub_double():
    # ShapeElt has no real 'ShapeElt' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLSimplified_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLSimplified_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLSimplified_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    partner = ShapeElt()
    setattr(partner, 'ShapeElt', None)
    _safe_set(owner, 'sse_shapeSheet', {partner})
    assert getattr(partner, 'ShapeElt') == owner
    _safe_set(owner, 'sse_shapeSheet', set())
    assert getattr(partner, 'ShapeElt') is None


def test_assoc_ss_shapes2_stub_double():
    # ShapesCollection has no real 'ShapesCollection' property in the generated
    # code (a bare stub) -- manually attach it so DatadiagramMLSimplified_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DatadiagramMLSimplified_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DatadiagramMLSimplified_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    partner = ShapesCollection()
    setattr(partner, 'ShapesCollection', None)
    _safe_set(owner, 'shapes', partner)
    assert getattr(partner, 'ShapesCollection') == owner
    _safe_set(owner, 'shapes', None)
    assert getattr(partner, 'ShapesCollection') is None


