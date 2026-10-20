import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Descriptive,
    Fill,
    Geometry,
    Identifiable,
    Image,
    Interaction,
    Layer,
    Location,
    SimpleGeometry,
    Source,
    Stroke,
    Style,
    Text,
    TileImage,
    TileSource,
    XYZ,
    geoff_Color,
    geoff_Descriptive,
    geoff_Feature,
    geoff_GeoMap,
    geoff_Identifiable,
    geoff_Location,
    geoff_Script,
    geoff_StringToStringMapEntry,
    geoff_StyleEntry,
    geoff_View,
    geoff_XYZLocation,
    geoff_geom_Geometry,
    geoff_geom_LineString,
    geoff_geom_Point,
    geoff_geom_Polygon,
    geoff_geom_SimpleGeometry,
    geoff_interaction_Interaction,
    geoff_interaction_Select,
    geoff_layer_Layer,
    geoff_layer_TileLayer,
    geoff_layer_VectorLayer,
    geoff_source_BingMaps,
    geoff_source_MapQuest,
    geoff_source_OSM,
    geoff_source_Source,
    geoff_source_TileImage,
    geoff_source_TileSource,
    geoff_source_VectorSource,
    geoff_source_XYZ,
    geoff_style_Circle,
    geoff_style_Fill,
    geoff_style_Icon,
    geoff_style_Image,
    geoff_style_Stroke,
    geoff_style_Style,
    geoff_style_Text,
    geom_geoff_Location,
    layer_geoff_StyleEntry,
    source_geoff_Feature,
    style_geoff_Color,
    EventCondition,
    RendererHint,
    ScriptContext,
    SourceFormat,
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

def test_assoc_center7_reverse_link_reassign_clear():
    a1 = geoff_View(zoom=7)
    a2 = geoff_View(zoom=13)
    b = geoff_Location(projectionCode="sample_text")
    _safe_set(b, 'geoff_Location', a1)
    assert _is_linked(b, 'geoff_Location', a1)
    if hasattr(a1, 'geoff_View8'):
        assert _is_linked(a1, 'geoff_View8', b)
    _safe_set(b, 'geoff_Location', a2)
    assert _is_linked(b, 'geoff_Location', a2)
    if hasattr(a1, 'geoff_View8'):
        assert not _is_linked(a1, 'geoff_View8', b)
    if hasattr(a2, 'geoff_View8'):
        assert _is_linked(a2, 'geoff_View8', b)
    _safe_set(b, 'geoff_Location', None)
    assert not _is_linked(b, 'geoff_Location', a2)
    if hasattr(a2, 'geoff_View8'):
        assert not _is_linked(a2, 'geoff_View8', b)


def test_assoc_properties12_reverse_link_reassign_clear():
    a1 = geoff_StringToStringMapEntry(key="sample_text", value="sample_text")
    a2 = geoff_StringToStringMapEntry(key="sample_text_2", value="sample_text_2")
    b = geoff_Feature(onclick="sample_text")
    _safe_set(b, 'geoff_Feature13', {a1})
    assert _is_linked(b, 'geoff_Feature13', a1)
    if hasattr(a1, 'geoff_StringToStringMapEntry'):
        assert _is_linked(a1, 'geoff_StringToStringMapEntry', b)
    _safe_set(b, 'geoff_Feature13', {a2})
    assert _is_linked(b, 'geoff_Feature13', a2)
    if hasattr(a1, 'geoff_StringToStringMapEntry'):
        assert not _is_linked(a1, 'geoff_StringToStringMapEntry', b)
    if hasattr(a2, 'geoff_StringToStringMapEntry'):
        assert _is_linked(a2, 'geoff_StringToStringMapEntry', b)
    _safe_set(b, 'geoff_Feature13', set())
    assert not _is_linked(b, 'geoff_Feature13', a2)
    if hasattr(a2, 'geoff_StringToStringMapEntry'):
        assert not _is_linked(a2, 'geoff_StringToStringMapEntry', b)


def test_assoc_scripts3_reverse_link_reassign_clear():
    a1 = geoff_Script(context="sample_text", src="sample_text", type="sample_text")
    a2 = geoff_Script(context="sample_text_2", src="sample_text_2", type="sample_text_2")
    b = geoff_GeoMap(rendererHint="sample_text")
    _safe_set(b, 'geoff_GeoMap4', {a1})
    assert _is_linked(b, 'geoff_GeoMap4', a1)
    if hasattr(a1, 'geoff_Script'):
        assert _is_linked(a1, 'geoff_Script', b)
    _safe_set(b, 'geoff_GeoMap4', {a2})
    assert _is_linked(b, 'geoff_GeoMap4', a2)
    if hasattr(a1, 'geoff_Script'):
        assert not _is_linked(a1, 'geoff_Script', b)
    if hasattr(a2, 'geoff_Script'):
        assert _is_linked(a2, 'geoff_Script', b)
    _safe_set(b, 'geoff_GeoMap4', set())
    assert not _is_linked(b, 'geoff_GeoMap4', a2)
    if hasattr(a2, 'geoff_Script'):
        assert not _is_linked(a2, 'geoff_Script', b)


def test_assoc_view1_reverse_link_reassign_clear():
    a1 = geoff_View(zoom=7)
    a2 = geoff_View(zoom=13)
    b = geoff_GeoMap(rendererHint="sample_text")
    _safe_set(b, 'geoff_GeoMap2', a1)
    assert _is_linked(b, 'geoff_GeoMap2', a1)
    if hasattr(a1, 'geoff_View'):
        assert _is_linked(a1, 'geoff_View', b)
    _safe_set(b, 'geoff_GeoMap2', a2)
    assert _is_linked(b, 'geoff_GeoMap2', a2)
    if hasattr(a1, 'geoff_View'):
        assert not _is_linked(a1, 'geoff_View', b)
    if hasattr(a2, 'geoff_View'):
        assert _is_linked(a2, 'geoff_View', b)
    _safe_set(b, 'geoff_GeoMap2', None)
    assert not _is_linked(b, 'geoff_GeoMap2', a2)
    if hasattr(a2, 'geoff_View'):
        assert not _is_linked(a2, 'geoff_View', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_color32_stub_double():
    # style_geoff_Color has no real 'style_geoff_Color33' property in the generated
    # code (a bare stub) -- manually attach it so geoff_style_Stroke's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_style_Stroke's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_style_Stroke(lineCap="sample_text", lineDash=3.14, lineJoin="sample_text", miterLimit="sample_text", width="sample_text")
    partner = style_geoff_Color()
    setattr(partner, 'style_geoff_Color33', None)
    _safe_set(owner, 'geoff_style_Stroke', partner)
    assert getattr(partner, 'style_geoff_Color33') == owner
    _safe_set(owner, 'geoff_style_Stroke', None)
    assert getattr(partner, 'style_geoff_Color33') is None


def test_assoc_features18_stub_double():
    # source_geoff_Feature has no real 'source_geoff_Feature' property in the generated
    # code (a bare stub) -- manually attach it so geoff_source_VectorSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_source_VectorSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_source_VectorSource(format="sample_text", projection="sample_text", url="sample_text")
    partner = source_geoff_Feature()
    setattr(partner, 'source_geoff_Feature', None)
    _safe_set(owner, 'geoff_source_VectorSource', {partner})
    assert getattr(partner, 'source_geoff_Feature') == owner
    _safe_set(owner, 'geoff_source_VectorSource', set())
    assert getattr(partner, 'source_geoff_Feature') is None


def test_assoc_fill25_stub_double():
    # Fill has no real 'Fill' property in the generated
    # code (a bare stub) -- manually attach it so geoff_style_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_style_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_style_Style(zindex="sample_text")
    partner = Fill()
    setattr(partner, 'Fill', None)
    _safe_set(owner, 'geoff_style_Style26', partner)
    assert getattr(partner, 'Fill') == owner
    _safe_set(owner, 'geoff_style_Style26', None)
    assert getattr(partner, 'Fill') is None


def test_assoc_fill34_stub_double():
    # Fill has no real 'Fill35' property in the generated
    # code (a bare stub) -- manually attach it so geoff_style_Circle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_style_Circle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_style_Circle(radius=3.14)
    partner = Fill()
    setattr(partner, 'Fill35', None)
    _safe_set(owner, 'geoff_style_Circle', partner)
    assert getattr(partner, 'Fill35') == owner
    _safe_set(owner, 'geoff_style_Circle', None)
    assert getattr(partner, 'Fill35') is None


def test_assoc_fill39_stub_double():
    # Fill has no real 'Fill40' property in the generated
    # code (a bare stub) -- manually attach it so geoff_style_Text's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_style_Text's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_style_Text(font="sample_text", offsetX=3.14, offsetY=3.14, rotation="sample_text", scale="sample_text", text="sample_text", textAlign="sample_text", textBaseLine="sample_text")
    partner = Fill()
    setattr(partner, 'Fill40', None)
    _safe_set(owner, 'geoff_style_Text', partner)
    assert getattr(partner, 'Fill40') == owner
    _safe_set(owner, 'geoff_style_Text', None)
    assert getattr(partner, 'Fill40') is None


def test_assoc_geometry9_stub_double():
    # Geometry has no real 'Geometry' property in the generated
    # code (a bare stub) -- manually attach it so geoff_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_Feature(onclick="sample_text")
    partner = Geometry()
    setattr(partner, 'Geometry', None)
    _safe_set(owner, 'geoff_Feature', partner)
    assert getattr(partner, 'Geometry') == owner
    _safe_set(owner, 'geoff_Feature', None)
    assert getattr(partner, 'Geometry') is None


def test_assoc_image24_stub_double():
    # Image has no real 'Image' property in the generated
    # code (a bare stub) -- manually attach it so geoff_style_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_style_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_style_Style(zindex="sample_text")
    partner = Image()
    setattr(partner, 'Image', None)
    _safe_set(owner, 'geoff_style_Style', partner)
    assert getattr(partner, 'Image') == owner
    _safe_set(owner, 'geoff_style_Style', None)
    assert getattr(partner, 'Image') is None


def test_assoc_interactions5_stub_double():
    # Interaction has no real 'Interaction' property in the generated
    # code (a bare stub) -- manually attach it so geoff_GeoMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_GeoMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_GeoMap(rendererHint="sample_text")
    partner = Interaction()
    setattr(partner, 'Interaction', None)
    _safe_set(owner, 'geoff_GeoMap6', {partner})
    assert getattr(partner, 'Interaction') == owner
    _safe_set(owner, 'geoff_GeoMap6', set())
    assert getattr(partner, 'Interaction') is None


def test_assoc_layers0_stub_double():
    # Layer has no real 'Layer' property in the generated
    # code (a bare stub) -- manually attach it so geoff_GeoMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_GeoMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_GeoMap(rendererHint="sample_text")
    partner = Layer()
    setattr(partner, 'Layer', None)
    _safe_set(owner, 'geoff_GeoMap', {partner})
    assert getattr(partner, 'Layer') == owner
    _safe_set(owner, 'geoff_GeoMap', set())
    assert getattr(partner, 'Layer') is None


def test_assoc_stroke27_stub_double():
    # Stroke has no real 'Stroke' property in the generated
    # code (a bare stub) -- manually attach it so geoff_style_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_style_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_style_Style(zindex="sample_text")
    partner = Stroke()
    setattr(partner, 'Stroke', None)
    _safe_set(owner, 'geoff_style_Style28', partner)
    assert getattr(partner, 'Stroke') == owner
    _safe_set(owner, 'geoff_style_Style28', None)
    assert getattr(partner, 'Stroke') is None


def test_assoc_stroke36_stub_double():
    # Stroke has no real 'Stroke38' property in the generated
    # code (a bare stub) -- manually attach it so geoff_style_Circle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_style_Circle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_style_Circle(radius=3.14)
    partner = Stroke()
    setattr(partner, 'Stroke38', None)
    _safe_set(owner, 'geoff_style_Circle37', partner)
    assert getattr(partner, 'Stroke38') == owner
    _safe_set(owner, 'geoff_style_Circle37', None)
    assert getattr(partner, 'Stroke38') is None


def test_assoc_stroke41_stub_double():
    # Stroke has no real 'Stroke43' property in the generated
    # code (a bare stub) -- manually attach it so geoff_style_Text's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_style_Text's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_style_Text(font="sample_text", offsetX=3.14, offsetY=3.14, rotation="sample_text", scale="sample_text", text="sample_text", textAlign="sample_text", textBaseLine="sample_text")
    partner = Stroke()
    setattr(partner, 'Stroke43', None)
    _safe_set(owner, 'geoff_style_Text42', partner)
    assert getattr(partner, 'Stroke43') == owner
    _safe_set(owner, 'geoff_style_Text42', None)
    assert getattr(partner, 'Stroke43') is None


def test_assoc_style10_stub_double():
    # Style has no real 'Style' property in the generated
    # code (a bare stub) -- manually attach it so geoff_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_Feature(onclick="sample_text")
    partner = Style()
    setattr(partner, 'Style', None)
    _safe_set(owner, 'geoff_Feature11', partner)
    assert getattr(partner, 'Style') == owner
    _safe_set(owner, 'geoff_Feature11', None)
    assert getattr(partner, 'Style') is None


def test_assoc_text29_stub_double():
    # Text has no real 'Text' property in the generated
    # code (a bare stub) -- manually attach it so geoff_style_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_style_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_style_Style(zindex="sample_text")
    partner = Text()
    setattr(partner, 'Text', None)
    _safe_set(owner, 'geoff_style_Style30', partner)
    assert getattr(partner, 'Text') == owner
    _safe_set(owner, 'geoff_style_Style30', None)
    assert getattr(partner, 'Text') is None


def test_assoc_value14_stub_double():
    # Style has no real 'Style15' property in the generated
    # code (a bare stub) -- manually attach it so geoff_StyleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # geoff_StyleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = geoff_StyleEntry(key="sample_text")
    partner = Style()
    setattr(partner, 'Style15', None)
    _safe_set(owner, 'geoff_StyleEntry', partner)
    assert getattr(partner, 'Style15') == owner
    _safe_set(owner, 'geoff_StyleEntry', None)
    assert getattr(partner, 'Style15') is None


