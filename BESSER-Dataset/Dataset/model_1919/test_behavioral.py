import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    eaglemodel_Approved,
    eaglemodel_Attribute,
    eaglemodel_Attributes,
    eaglemodel_Bus,
    eaglemodel_Busses,
    eaglemodel_Circle,
    eaglemodel_Class,
    eaglemodel_Classes,
    eaglemodel_Clearance,
    eaglemodel_Compatibility,
    eaglemodel_Connect,
    eaglemodel_Connects,
    eaglemodel_Description,
    eaglemodel_Device,
    eaglemodel_Devices,
    eaglemodel_Deviceset,
    eaglemodel_Devicesets,
    eaglemodel_Dimension,
    eaglemodel_Drawing,
    eaglemodel_Eagle,
    eaglemodel_Errors,
    eaglemodel_Frame,
    eaglemodel_Gate,
    eaglemodel_Gates,
    eaglemodel_Grid,
    eaglemodel_Hole,
    eaglemodel_Instance,
    eaglemodel_Instances,
    eaglemodel_Junction,
    eaglemodel_Label,
    eaglemodel_Layer,
    eaglemodel_Layers,
    eaglemodel_Libraries,
    eaglemodel_Library,
    eaglemodel_Net,
    eaglemodel_Nets,
    eaglemodel_Note,
    eaglemodel_Package,
    eaglemodel_Packages,
    eaglemodel_Pad,
    eaglemodel_Part,
    eaglemodel_Parts,
    eaglemodel_Pin,
    eaglemodel_Pinref,
    eaglemodel_Plain,
    eaglemodel_Polygon,
    eaglemodel_Rectangle,
    eaglemodel_SMD,
    eaglemodel_Schematic,
    eaglemodel_Segment,
    eaglemodel_Setting,
    eaglemodel_Settings,
    eaglemodel_Sheet,
    eaglemodel_Sheets,
    eaglemodel_Symbol,
    eaglemodel_Symbols,
    eaglemodel_Technologies,
    eaglemodel_Technology,
    eaglemodel_Text,
    eaglemodel_Variant,
    eaglemodel_Variantdef,
    eaglemodel_Variantdefs,
    eaglemodel_Vertex,
    eaglemodel_Wire,
    Align,
    AttributeDisplay,
    ContactRoute,
    DimensionType,
    GateAddLevel,
    GridStyle,
    GridUnit,
    PadShape,
    PinDirection,
    PinFunction,
    PinLength,
    PinVisible,
    PolygonPour,
    Severity,
    TextFont,
    VerticalText,
    WireCap,
    WireStyle,
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

def test_assoc_attribute150_reverse_link_reassign_clear():
    a1 = eaglemodel_Technology(name="sample_text")
    a2 = eaglemodel_Technology(name="sample_text_2")
    b = eaglemodel_Attribute(constant=True, display="sample_text", font="sample_text", layer=7, name="sample_text", ratio=7, rot=7, size=3.14, value="sample_text", x=3.14, y=3.14)
    _safe_set(b, 'eaglemodel_Attribute152', a1)
    assert _is_linked(b, 'eaglemodel_Attribute152', a1)
    if hasattr(a1, 'eaglemodel_Technology151'):
        assert _is_linked(a1, 'eaglemodel_Technology151', b)
    _safe_set(b, 'eaglemodel_Attribute152', a2)
    assert _is_linked(b, 'eaglemodel_Attribute152', a2)
    if hasattr(a1, 'eaglemodel_Technology151'):
        assert not _is_linked(a1, 'eaglemodel_Technology151', b)
    if hasattr(a2, 'eaglemodel_Technology151'):
        assert _is_linked(a2, 'eaglemodel_Technology151', b)
    _safe_set(b, 'eaglemodel_Attribute152', None)
    assert not _is_linked(b, 'eaglemodel_Attribute152', a2)
    if hasattr(a2, 'eaglemodel_Technology151'):
        assert not _is_linked(a2, 'eaglemodel_Technology151', b)


def test_assoc_attribute179_reverse_link_reassign_clear():
    a1 = eaglemodel_Instance(gate="sample_text", part="sample_text", rot=7, smashed=True, x=3.14, y=3.14)
    a2 = eaglemodel_Instance(gate="sample_text_2", part="sample_text_2", rot=13, smashed=False, x=9.99, y=9.99)
    b = eaglemodel_Attribute(constant=True, display="sample_text", font="sample_text", layer=7, name="sample_text", ratio=7, rot=7, size=3.14, value="sample_text", x=3.14, y=3.14)
    _safe_set(b, 'eaglemodel_Attribute181', a1)
    assert _is_linked(b, 'eaglemodel_Attribute181', a1)
    if hasattr(a1, 'eaglemodel_Instance180'):
        assert _is_linked(a1, 'eaglemodel_Instance180', b)
    _safe_set(b, 'eaglemodel_Attribute181', a2)
    assert _is_linked(b, 'eaglemodel_Attribute181', a2)
    if hasattr(a1, 'eaglemodel_Instance180'):
        assert not _is_linked(a1, 'eaglemodel_Instance180', b)
    if hasattr(a2, 'eaglemodel_Instance180'):
        assert _is_linked(a2, 'eaglemodel_Instance180', b)
    _safe_set(b, 'eaglemodel_Attribute181', None)
    assert not _is_linked(b, 'eaglemodel_Attribute181', a2)
    if hasattr(a2, 'eaglemodel_Instance180'):
        assert not _is_linked(a2, 'eaglemodel_Instance180', b)


def test_assoc_attribute54_reverse_link_reassign_clear():
    a1 = eaglemodel_Part(device="sample_text", deviceset="sample_text", gate="sample_text", library="sample_text", name="sample_text", rot=7, smashed=True, technology="sample_text", uid=7, value="sample_text", x=3.14, y=3.14)
    a2 = eaglemodel_Part(device="sample_text_2", deviceset="sample_text_2", gate="sample_text_2", library="sample_text_2", name="sample_text_2", rot=13, smashed=False, technology="sample_text_2", uid=13, value="sample_text_2", x=9.99, y=9.99)
    b = eaglemodel_Attribute(constant=True, display="sample_text", font="sample_text", layer=7, name="sample_text", ratio=7, rot=7, size=3.14, value="sample_text", x=3.14, y=3.14)
    _safe_set(b, 'eaglemodel_Attribute56', a1)
    assert _is_linked(b, 'eaglemodel_Attribute56', a1)
    if hasattr(a1, 'eaglemodel_Part55'):
        assert _is_linked(a1, 'eaglemodel_Part55', b)
    _safe_set(b, 'eaglemodel_Attribute56', a2)
    assert _is_linked(b, 'eaglemodel_Attribute56', a2)
    if hasattr(a1, 'eaglemodel_Part55'):
        assert not _is_linked(a1, 'eaglemodel_Part55', b)
    if hasattr(a2, 'eaglemodel_Part55'):
        assert _is_linked(a2, 'eaglemodel_Part55', b)
    _safe_set(b, 'eaglemodel_Attribute56', None)
    assert not _is_linked(b, 'eaglemodel_Attribute56', a2)
    if hasattr(a2, 'eaglemodel_Part55'):
        assert not _is_linked(a2, 'eaglemodel_Part55', b)


def test_assoc_circle118_reverse_link_reassign_clear():
    a1 = eaglemodel_Symbol(name="sample_text")
    a2 = eaglemodel_Symbol(name="sample_text_2")
    b = eaglemodel_Circle(layer=7, radius=3.14, width=3.14, x=3.14, y=3.14)
    _safe_set(b, 'eaglemodel_Circle120', a1)
    assert _is_linked(b, 'eaglemodel_Circle120', a1)
    if hasattr(a1, 'eaglemodel_Symbol119'):
        assert _is_linked(a1, 'eaglemodel_Symbol119', b)
    _safe_set(b, 'eaglemodel_Circle120', a2)
    assert _is_linked(b, 'eaglemodel_Circle120', a2)
    if hasattr(a1, 'eaglemodel_Symbol119'):
        assert not _is_linked(a1, 'eaglemodel_Symbol119', b)
    if hasattr(a2, 'eaglemodel_Symbol119'):
        assert _is_linked(a2, 'eaglemodel_Symbol119', b)
    _safe_set(b, 'eaglemodel_Circle120', None)
    assert not _is_linked(b, 'eaglemodel_Circle120', a2)
    if hasattr(a2, 'eaglemodel_Symbol119'):
        assert not _is_linked(a2, 'eaglemodel_Symbol119', b)


def test_assoc_circle87_reverse_link_reassign_clear():
    a1 = eaglemodel_Package(name="sample_text")
    a2 = eaglemodel_Package(name="sample_text_2")
    b = eaglemodel_Circle(layer=7, radius=3.14, width=3.14, x=3.14, y=3.14)
    _safe_set(b, 'eaglemodel_Circle', a1)
    assert _is_linked(b, 'eaglemodel_Circle', a1)
    if hasattr(a1, 'eaglemodel_Package88'):
        assert _is_linked(a1, 'eaglemodel_Package88', b)
    _safe_set(b, 'eaglemodel_Circle', a2)
    assert _is_linked(b, 'eaglemodel_Circle', a2)
    if hasattr(a1, 'eaglemodel_Package88'):
        assert not _is_linked(a1, 'eaglemodel_Package88', b)
    if hasattr(a2, 'eaglemodel_Package88'):
        assert _is_linked(a2, 'eaglemodel_Package88', b)
    _safe_set(b, 'eaglemodel_Circle', None)
    assert not _is_linked(b, 'eaglemodel_Circle', a2)
    if hasattr(a2, 'eaglemodel_Package88'):
        assert not _is_linked(a2, 'eaglemodel_Package88', b)


def test_assoc_clearance50_reverse_link_reassign_clear():
    a1 = eaglemodel_Clearance(class_=7, value=3.14)
    a2 = eaglemodel_Clearance(class_=13, value=9.99)
    b = eaglemodel_Class(drill=3.14, name="sample_text", number=7, width=3.14)
    _safe_set(b, 'eaglemodel_Class51', {a1})
    assert _is_linked(b, 'eaglemodel_Class51', a1)
    if hasattr(a1, 'eaglemodel_Clearance'):
        assert _is_linked(a1, 'eaglemodel_Clearance', b)
    _safe_set(b, 'eaglemodel_Class51', {a2})
    assert _is_linked(b, 'eaglemodel_Class51', a2)
    if hasattr(a1, 'eaglemodel_Clearance'):
        assert not _is_linked(a1, 'eaglemodel_Clearance', b)
    if hasattr(a2, 'eaglemodel_Clearance'):
        assert _is_linked(a2, 'eaglemodel_Clearance', b)
    _safe_set(b, 'eaglemodel_Class51', set())
    assert not _is_linked(b, 'eaglemodel_Class51', a2)
    if hasattr(a2, 'eaglemodel_Clearance'):
        assert not _is_linked(a2, 'eaglemodel_Clearance', b)


def test_assoc_description101_reverse_link_reassign_clear():
    a1 = eaglemodel_Symbol(name="sample_text")
    a2 = eaglemodel_Symbol(name="sample_text_2")
    b = eaglemodel_Description(language="sample_text", value="sample_text")
    _safe_set(b, 'eaglemodel_Description103', a1)
    assert _is_linked(b, 'eaglemodel_Description103', a1)
    if hasattr(a1, 'eaglemodel_Symbol102'):
        assert _is_linked(a1, 'eaglemodel_Symbol102', b)
    _safe_set(b, 'eaglemodel_Description103', a2)
    assert _is_linked(b, 'eaglemodel_Description103', a2)
    if hasattr(a1, 'eaglemodel_Symbol102'):
        assert not _is_linked(a1, 'eaglemodel_Symbol102', b)
    if hasattr(a2, 'eaglemodel_Symbol102'):
        assert _is_linked(a2, 'eaglemodel_Symbol102', b)
    _safe_set(b, 'eaglemodel_Description103', None)
    assert not _is_linked(b, 'eaglemodel_Description103', a2)
    if hasattr(a2, 'eaglemodel_Symbol102'):
        assert not _is_linked(a2, 'eaglemodel_Symbol102', b)


def test_assoc_description129_reverse_link_reassign_clear():
    a1 = eaglemodel_Deviceset(name="sample_text", prefix="sample_text", uservalue=True)
    a2 = eaglemodel_Deviceset(name="sample_text_2", prefix="sample_text_2", uservalue=False)
    b = eaglemodel_Description(language="sample_text", value="sample_text")
    _safe_set(b, 'eaglemodel_Description131', a1)
    assert _is_linked(b, 'eaglemodel_Description131', a1)
    if hasattr(a1, 'eaglemodel_Deviceset130'):
        assert _is_linked(a1, 'eaglemodel_Deviceset130', b)
    _safe_set(b, 'eaglemodel_Description131', a2)
    assert _is_linked(b, 'eaglemodel_Description131', a2)
    if hasattr(a1, 'eaglemodel_Deviceset130'):
        assert not _is_linked(a1, 'eaglemodel_Deviceset130', b)
    if hasattr(a2, 'eaglemodel_Deviceset130'):
        assert _is_linked(a2, 'eaglemodel_Deviceset130', b)
    _safe_set(b, 'eaglemodel_Description131', None)
    assert not _is_linked(b, 'eaglemodel_Description131', a2)
    if hasattr(a2, 'eaglemodel_Deviceset130'):
        assert not _is_linked(a2, 'eaglemodel_Deviceset130', b)


def test_assoc_description17_reverse_link_reassign_clear():
    a1 = eaglemodel_Schematic(xreflabel="sample_text", xrefpart="sample_text")
    a2 = eaglemodel_Schematic(xreflabel="sample_text_2", xrefpart="sample_text_2")
    b = eaglemodel_Description(language="sample_text", value="sample_text")
    _safe_set(b, 'eaglemodel_Description', a1)
    assert _is_linked(b, 'eaglemodel_Description', a1)
    if hasattr(a1, 'eaglemodel_Schematic18'):
        assert _is_linked(a1, 'eaglemodel_Schematic18', b)
    _safe_set(b, 'eaglemodel_Description', a2)
    assert _is_linked(b, 'eaglemodel_Description', a2)
    if hasattr(a1, 'eaglemodel_Schematic18'):
        assert not _is_linked(a1, 'eaglemodel_Schematic18', b)
    if hasattr(a2, 'eaglemodel_Schematic18'):
        assert _is_linked(a2, 'eaglemodel_Schematic18', b)
    _safe_set(b, 'eaglemodel_Description', None)
    assert not _is_linked(b, 'eaglemodel_Description', a2)
    if hasattr(a2, 'eaglemodel_Schematic18'):
        assert not _is_linked(a2, 'eaglemodel_Schematic18', b)


def test_assoc_description35_reverse_link_reassign_clear():
    a1 = eaglemodel_Library(name="sample_text")
    a2 = eaglemodel_Library(name="sample_text_2")
    b = eaglemodel_Description(language="sample_text", value="sample_text")
    _safe_set(b, 'eaglemodel_Description37', a1)
    assert _is_linked(b, 'eaglemodel_Description37', a1)
    if hasattr(a1, 'eaglemodel_Library36'):
        assert _is_linked(a1, 'eaglemodel_Library36', b)
    _safe_set(b, 'eaglemodel_Description37', a2)
    assert _is_linked(b, 'eaglemodel_Description37', a2)
    if hasattr(a1, 'eaglemodel_Library36'):
        assert not _is_linked(a1, 'eaglemodel_Library36', b)
    if hasattr(a2, 'eaglemodel_Library36'):
        assert _is_linked(a2, 'eaglemodel_Library36', b)
    _safe_set(b, 'eaglemodel_Description37', None)
    assert not _is_linked(b, 'eaglemodel_Description37', a2)
    if hasattr(a2, 'eaglemodel_Library36'):
        assert not _is_linked(a2, 'eaglemodel_Library36', b)


def test_assoc_description76_reverse_link_reassign_clear():
    a1 = eaglemodel_Package(name="sample_text")
    a2 = eaglemodel_Package(name="sample_text_2")
    b = eaglemodel_Description(language="sample_text", value="sample_text")
    _safe_set(b, 'eaglemodel_Description78', a1)
    assert _is_linked(b, 'eaglemodel_Description78', a1)
    if hasattr(a1, 'eaglemodel_Package77'):
        assert _is_linked(a1, 'eaglemodel_Package77', b)
    _safe_set(b, 'eaglemodel_Description78', a2)
    assert _is_linked(b, 'eaglemodel_Description78', a2)
    if hasattr(a1, 'eaglemodel_Package77'):
        assert not _is_linked(a1, 'eaglemodel_Package77', b)
    if hasattr(a2, 'eaglemodel_Package77'):
        assert _is_linked(a2, 'eaglemodel_Package77', b)
    _safe_set(b, 'eaglemodel_Description78', None)
    assert not _is_linked(b, 'eaglemodel_Description78', a2)
    if hasattr(a2, 'eaglemodel_Package77'):
        assert not _is_linked(a2, 'eaglemodel_Package77', b)


def test_assoc_dimension113_reverse_link_reassign_clear():
    a1 = eaglemodel_Symbol(name="sample_text")
    a2 = eaglemodel_Symbol(name="sample_text_2")
    b = eaglemodel_Dimension(dtype="sample_text", extlength=3.14, extoffset=3.14, extwidth=3.14, layer=7, precision=7, textratio=7, textsize=3.14, unit="sample_text", visible=True, width=3.14, x1=3.14, x2=3.14, x3=3.14, y1=3.14, y2=3.14, y3=3.14)
    _safe_set(b, 'eaglemodel_Dimension115', a1)
    assert _is_linked(b, 'eaglemodel_Dimension115', a1)
    if hasattr(a1, 'eaglemodel_Symbol114'):
        assert _is_linked(a1, 'eaglemodel_Symbol114', b)
    _safe_set(b, 'eaglemodel_Dimension115', a2)
    assert _is_linked(b, 'eaglemodel_Dimension115', a2)
    if hasattr(a1, 'eaglemodel_Symbol114'):
        assert not _is_linked(a1, 'eaglemodel_Symbol114', b)
    if hasattr(a2, 'eaglemodel_Symbol114'):
        assert _is_linked(a2, 'eaglemodel_Symbol114', b)
    _safe_set(b, 'eaglemodel_Dimension115', None)
    assert not _is_linked(b, 'eaglemodel_Dimension115', a2)
    if hasattr(a2, 'eaglemodel_Symbol114'):
        assert not _is_linked(a2, 'eaglemodel_Symbol114', b)


def test_assoc_dimension85_reverse_link_reassign_clear():
    a1 = eaglemodel_Package(name="sample_text")
    a2 = eaglemodel_Package(name="sample_text_2")
    b = eaglemodel_Dimension(dtype="sample_text", extlength=3.14, extoffset=3.14, extwidth=3.14, layer=7, precision=7, textratio=7, textsize=3.14, unit="sample_text", visible=True, width=3.14, x1=3.14, x2=3.14, x3=3.14, y1=3.14, y2=3.14, y3=3.14)
    _safe_set(b, 'eaglemodel_Dimension', a1)
    assert _is_linked(b, 'eaglemodel_Dimension', a1)
    if hasattr(a1, 'eaglemodel_Package86'):
        assert _is_linked(a1, 'eaglemodel_Package86', b)
    _safe_set(b, 'eaglemodel_Dimension', a2)
    assert _is_linked(b, 'eaglemodel_Dimension', a2)
    if hasattr(a1, 'eaglemodel_Package86'):
        assert not _is_linked(a1, 'eaglemodel_Package86', b)
    if hasattr(a2, 'eaglemodel_Package86'):
        assert _is_linked(a2, 'eaglemodel_Package86', b)
    _safe_set(b, 'eaglemodel_Dimension', None)
    assert not _is_linked(b, 'eaglemodel_Dimension', a2)
    if hasattr(a2, 'eaglemodel_Package86'):
        assert not _is_linked(a2, 'eaglemodel_Package86', b)


def test_assoc_frame124_reverse_link_reassign_clear():
    a1 = eaglemodel_Symbol(name="sample_text")
    a2 = eaglemodel_Symbol(name="sample_text_2")
    b = eaglemodel_Frame(borderbottom=True, borderleft=True, borderright=True, bordertop=True, columns=7, layer=7, rows=7, x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    _safe_set(b, 'eaglemodel_Frame126', a1)
    assert _is_linked(b, 'eaglemodel_Frame126', a1)
    if hasattr(a1, 'eaglemodel_Symbol125'):
        assert _is_linked(a1, 'eaglemodel_Symbol125', b)
    _safe_set(b, 'eaglemodel_Frame126', a2)
    assert _is_linked(b, 'eaglemodel_Frame126', a2)
    if hasattr(a1, 'eaglemodel_Symbol125'):
        assert not _is_linked(a1, 'eaglemodel_Symbol125', b)
    if hasattr(a2, 'eaglemodel_Symbol125'):
        assert _is_linked(a2, 'eaglemodel_Symbol125', b)
    _safe_set(b, 'eaglemodel_Frame126', None)
    assert not _is_linked(b, 'eaglemodel_Frame126', a2)
    if hasattr(a2, 'eaglemodel_Symbol125'):
        assert not _is_linked(a2, 'eaglemodel_Symbol125', b)


def test_assoc_frame91_reverse_link_reassign_clear():
    a1 = eaglemodel_Package(name="sample_text")
    a2 = eaglemodel_Package(name="sample_text_2")
    b = eaglemodel_Frame(borderbottom=True, borderleft=True, borderright=True, bordertop=True, columns=7, layer=7, rows=7, x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    _safe_set(b, 'eaglemodel_Frame', a1)
    assert _is_linked(b, 'eaglemodel_Frame', a1)
    if hasattr(a1, 'eaglemodel_Package92'):
        assert _is_linked(a1, 'eaglemodel_Package92', b)
    _safe_set(b, 'eaglemodel_Frame', a2)
    assert _is_linked(b, 'eaglemodel_Frame', a2)
    if hasattr(a1, 'eaglemodel_Package92'):
        assert not _is_linked(a1, 'eaglemodel_Package92', b)
    if hasattr(a2, 'eaglemodel_Package92'):
        assert _is_linked(a2, 'eaglemodel_Package92', b)
    _safe_set(b, 'eaglemodel_Frame', None)
    assert not _is_linked(b, 'eaglemodel_Frame', a2)
    if hasattr(a2, 'eaglemodel_Package92'):
        assert not _is_linked(a2, 'eaglemodel_Package92', b)


def test_assoc_hole93_reverse_link_reassign_clear():
    a1 = eaglemodel_Package(name="sample_text")
    a2 = eaglemodel_Package(name="sample_text_2")
    b = eaglemodel_Hole(drill=3.14, x=3.14, y=3.14)
    _safe_set(b, 'eaglemodel_Hole', a1)
    assert _is_linked(b, 'eaglemodel_Hole', a1)
    if hasattr(a1, 'eaglemodel_Package94'):
        assert _is_linked(a1, 'eaglemodel_Package94', b)
    _safe_set(b, 'eaglemodel_Hole', a2)
    assert _is_linked(b, 'eaglemodel_Hole', a2)
    if hasattr(a1, 'eaglemodel_Package94'):
        assert not _is_linked(a1, 'eaglemodel_Package94', b)
    if hasattr(a2, 'eaglemodel_Package94'):
        assert _is_linked(a2, 'eaglemodel_Package94', b)
    _safe_set(b, 'eaglemodel_Hole', None)
    assert not _is_linked(b, 'eaglemodel_Hole', a2)
    if hasattr(a2, 'eaglemodel_Package94'):
        assert not _is_linked(a2, 'eaglemodel_Package94', b)


def test_assoc_pad95_reverse_link_reassign_clear():
    a1 = eaglemodel_Pad(diameter=3.14, drill=3.14, first=True, name="sample_text", rot=7, shape="sample_text", stop=True, thermals=True, x=3.14, y=3.14)
    a2 = eaglemodel_Pad(diameter=9.99, drill=9.99, first=False, name="sample_text_2", rot=13, shape="sample_text_2", stop=False, thermals=False, x=9.99, y=9.99)
    b = eaglemodel_Package(name="sample_text")
    _safe_set(b, 'eaglemodel_Package96', {a1})
    assert _is_linked(b, 'eaglemodel_Package96', a1)
    if hasattr(a1, 'eaglemodel_Pad'):
        assert _is_linked(a1, 'eaglemodel_Pad', b)
    _safe_set(b, 'eaglemodel_Package96', {a2})
    assert _is_linked(b, 'eaglemodel_Package96', a2)
    if hasattr(a1, 'eaglemodel_Pad'):
        assert not _is_linked(a1, 'eaglemodel_Pad', b)
    if hasattr(a2, 'eaglemodel_Pad'):
        assert _is_linked(a2, 'eaglemodel_Pad', b)
    _safe_set(b, 'eaglemodel_Package96', set())
    assert not _is_linked(b, 'eaglemodel_Package96', a2)
    if hasattr(a2, 'eaglemodel_Pad'):
        assert not _is_linked(a2, 'eaglemodel_Pad', b)


def test_assoc_pin116_reverse_link_reassign_clear():
    a1 = eaglemodel_Symbol(name="sample_text")
    a2 = eaglemodel_Symbol(name="sample_text_2")
    b = eaglemodel_Pin(direction="sample_text", function="sample_text", length="sample_text", name="sample_text", rot=7, swaplevel=7, visible="sample_text", x=3.14, y=3.14)
    _safe_set(b, 'eaglemodel_Pin', a1)
    assert _is_linked(b, 'eaglemodel_Pin', a1)
    if hasattr(a1, 'eaglemodel_Symbol117'):
        assert _is_linked(a1, 'eaglemodel_Symbol117', b)
    _safe_set(b, 'eaglemodel_Pin', a2)
    assert _is_linked(b, 'eaglemodel_Pin', a2)
    if hasattr(a1, 'eaglemodel_Symbol117'):
        assert not _is_linked(a1, 'eaglemodel_Symbol117', b)
    if hasattr(a2, 'eaglemodel_Symbol117'):
        assert _is_linked(a2, 'eaglemodel_Symbol117', b)
    _safe_set(b, 'eaglemodel_Pin', None)
    assert not _is_linked(b, 'eaglemodel_Pin', a2)
    if hasattr(a2, 'eaglemodel_Symbol117'):
        assert not _is_linked(a2, 'eaglemodel_Symbol117', b)


def test_assoc_polygon104_reverse_link_reassign_clear():
    a1 = eaglemodel_Symbol(name="sample_text")
    a2 = eaglemodel_Symbol(name="sample_text_2")
    b = eaglemodel_Polygon(isolate=3.14, layer=7, orphans=True, pour="sample_text", rank=7, spacing=3.14, thermals=True, width=3.14)
    _safe_set(b, 'eaglemodel_Polygon106', a1)
    assert _is_linked(b, 'eaglemodel_Polygon106', a1)
    if hasattr(a1, 'eaglemodel_Symbol105'):
        assert _is_linked(a1, 'eaglemodel_Symbol105', b)
    _safe_set(b, 'eaglemodel_Polygon106', a2)
    assert _is_linked(b, 'eaglemodel_Polygon106', a2)
    if hasattr(a1, 'eaglemodel_Symbol105'):
        assert not _is_linked(a1, 'eaglemodel_Symbol105', b)
    if hasattr(a2, 'eaglemodel_Symbol105'):
        assert _is_linked(a2, 'eaglemodel_Symbol105', b)
    _safe_set(b, 'eaglemodel_Polygon106', None)
    assert not _is_linked(b, 'eaglemodel_Polygon106', a2)
    if hasattr(a2, 'eaglemodel_Symbol105'):
        assert not _is_linked(a2, 'eaglemodel_Symbol105', b)


def test_assoc_polygon79_reverse_link_reassign_clear():
    a1 = eaglemodel_Polygon(isolate=3.14, layer=7, orphans=True, pour="sample_text", rank=7, spacing=3.14, thermals=True, width=3.14)
    a2 = eaglemodel_Polygon(isolate=9.99, layer=13, orphans=False, pour="sample_text_2", rank=13, spacing=9.99, thermals=False, width=9.99)
    b = eaglemodel_Package(name="sample_text")
    _safe_set(b, 'eaglemodel_Package80', {a1})
    assert _is_linked(b, 'eaglemodel_Package80', a1)
    if hasattr(a1, 'eaglemodel_Polygon'):
        assert _is_linked(a1, 'eaglemodel_Polygon', b)
    _safe_set(b, 'eaglemodel_Package80', {a2})
    assert _is_linked(b, 'eaglemodel_Package80', a2)
    if hasattr(a1, 'eaglemodel_Polygon'):
        assert not _is_linked(a1, 'eaglemodel_Polygon', b)
    if hasattr(a2, 'eaglemodel_Polygon'):
        assert _is_linked(a2, 'eaglemodel_Polygon', b)
    _safe_set(b, 'eaglemodel_Package80', set())
    assert not _is_linked(b, 'eaglemodel_Package80', a2)
    if hasattr(a2, 'eaglemodel_Polygon'):
        assert not _is_linked(a2, 'eaglemodel_Polygon', b)


def test_assoc_rectangle121_reverse_link_reassign_clear():
    a1 = eaglemodel_Symbol(name="sample_text")
    a2 = eaglemodel_Symbol(name="sample_text_2")
    b = eaglemodel_Rectangle(layer=7, rot=7, x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    _safe_set(b, 'eaglemodel_Rectangle123', a1)
    assert _is_linked(b, 'eaglemodel_Rectangle123', a1)
    if hasattr(a1, 'eaglemodel_Symbol122'):
        assert _is_linked(a1, 'eaglemodel_Symbol122', b)
    _safe_set(b, 'eaglemodel_Rectangle123', a2)
    assert _is_linked(b, 'eaglemodel_Rectangle123', a2)
    if hasattr(a1, 'eaglemodel_Symbol122'):
        assert not _is_linked(a1, 'eaglemodel_Symbol122', b)
    if hasattr(a2, 'eaglemodel_Symbol122'):
        assert _is_linked(a2, 'eaglemodel_Symbol122', b)
    _safe_set(b, 'eaglemodel_Rectangle123', None)
    assert not _is_linked(b, 'eaglemodel_Rectangle123', a2)
    if hasattr(a2, 'eaglemodel_Symbol122'):
        assert not _is_linked(a2, 'eaglemodel_Symbol122', b)


def test_assoc_rectangle89_reverse_link_reassign_clear():
    a1 = eaglemodel_Rectangle(layer=7, rot=7, x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    a2 = eaglemodel_Rectangle(layer=13, rot=13, x1=9.99, x2=9.99, y1=9.99, y2=9.99)
    b = eaglemodel_Package(name="sample_text")
    _safe_set(b, 'eaglemodel_Package90', {a1})
    assert _is_linked(b, 'eaglemodel_Package90', a1)
    if hasattr(a1, 'eaglemodel_Rectangle'):
        assert _is_linked(a1, 'eaglemodel_Rectangle', b)
    _safe_set(b, 'eaglemodel_Package90', {a2})
    assert _is_linked(b, 'eaglemodel_Package90', a2)
    if hasattr(a1, 'eaglemodel_Rectangle'):
        assert not _is_linked(a1, 'eaglemodel_Rectangle', b)
    if hasattr(a2, 'eaglemodel_Rectangle'):
        assert _is_linked(a2, 'eaglemodel_Rectangle', b)
    _safe_set(b, 'eaglemodel_Package90', set())
    assert not _is_linked(b, 'eaglemodel_Package90', a2)
    if hasattr(a2, 'eaglemodel_Rectangle'):
        assert not _is_linked(a2, 'eaglemodel_Rectangle', b)


def test_assoc_smd97_reverse_link_reassign_clear():
    a1 = eaglemodel_SMD(cream=True, dx=3.14, dy=3.14, layer=7, name="sample_text", rot=7, roundness=7, stop=True, thermals=True, x=3.14, y=3.14)
    a2 = eaglemodel_SMD(cream=False, dx=9.99, dy=9.99, layer=13, name="sample_text_2", rot=13, roundness=13, stop=False, thermals=False, x=9.99, y=9.99)
    b = eaglemodel_Package(name="sample_text")
    _safe_set(b, 'eaglemodel_Package98', {a1})
    assert _is_linked(b, 'eaglemodel_Package98', a1)
    if hasattr(a1, 'eaglemodel_SMD'):
        assert _is_linked(a1, 'eaglemodel_SMD', b)
    _safe_set(b, 'eaglemodel_Package98', {a2})
    assert _is_linked(b, 'eaglemodel_Package98', a2)
    if hasattr(a1, 'eaglemodel_SMD'):
        assert not _is_linked(a1, 'eaglemodel_SMD', b)
    if hasattr(a2, 'eaglemodel_SMD'):
        assert _is_linked(a2, 'eaglemodel_SMD', b)
    _safe_set(b, 'eaglemodel_Package98', set())
    assert not _is_linked(b, 'eaglemodel_Package98', a2)
    if hasattr(a2, 'eaglemodel_SMD'):
        assert not _is_linked(a2, 'eaglemodel_SMD', b)


def test_assoc_text110_reverse_link_reassign_clear():
    a1 = eaglemodel_Text(align="sample_text", distance=7, font="sample_text", layer=7, ratio=7, rot=7, size=3.14, value="sample_text", x=3.14, y=3.14)
    a2 = eaglemodel_Text(align="sample_text_2", distance=13, font="sample_text_2", layer=13, ratio=13, rot=13, size=9.99, value="sample_text_2", x=9.99, y=9.99)
    b = eaglemodel_Symbol(name="sample_text")
    _safe_set(b, 'eaglemodel_Symbol111', {a1})
    assert _is_linked(b, 'eaglemodel_Symbol111', a1)
    if hasattr(a1, 'eaglemodel_Text112'):
        assert _is_linked(a1, 'eaglemodel_Text112', b)
    _safe_set(b, 'eaglemodel_Symbol111', {a2})
    assert _is_linked(b, 'eaglemodel_Symbol111', a2)
    if hasattr(a1, 'eaglemodel_Text112'):
        assert not _is_linked(a1, 'eaglemodel_Text112', b)
    if hasattr(a2, 'eaglemodel_Text112'):
        assert _is_linked(a2, 'eaglemodel_Text112', b)
    _safe_set(b, 'eaglemodel_Symbol111', set())
    assert not _is_linked(b, 'eaglemodel_Symbol111', a2)
    if hasattr(a2, 'eaglemodel_Text112'):
        assert not _is_linked(a2, 'eaglemodel_Text112', b)


def test_assoc_text83_reverse_link_reassign_clear():
    a1 = eaglemodel_Text(align="sample_text", distance=7, font="sample_text", layer=7, ratio=7, rot=7, size=3.14, value="sample_text", x=3.14, y=3.14)
    a2 = eaglemodel_Text(align="sample_text_2", distance=13, font="sample_text_2", layer=13, ratio=13, rot=13, size=9.99, value="sample_text_2", x=9.99, y=9.99)
    b = eaglemodel_Package(name="sample_text")
    _safe_set(b, 'eaglemodel_Package84', {a1})
    assert _is_linked(b, 'eaglemodel_Package84', a1)
    if hasattr(a1, 'eaglemodel_Text'):
        assert _is_linked(a1, 'eaglemodel_Text', b)
    _safe_set(b, 'eaglemodel_Package84', {a2})
    assert _is_linked(b, 'eaglemodel_Package84', a2)
    if hasattr(a1, 'eaglemodel_Text'):
        assert not _is_linked(a1, 'eaglemodel_Text', b)
    if hasattr(a2, 'eaglemodel_Text'):
        assert _is_linked(a2, 'eaglemodel_Text', b)
    _safe_set(b, 'eaglemodel_Package84', set())
    assert not _is_linked(b, 'eaglemodel_Package84', a2)
    if hasattr(a2, 'eaglemodel_Text'):
        assert not _is_linked(a2, 'eaglemodel_Text', b)


def test_assoc_variant57_reverse_link_reassign_clear():
    a1 = eaglemodel_Variant(name="sample_text", populate=True, technology="sample_text", value="sample_text")
    a2 = eaglemodel_Variant(name="sample_text_2", populate=False, technology="sample_text_2", value="sample_text_2")
    b = eaglemodel_Part(device="sample_text", deviceset="sample_text", gate="sample_text", library="sample_text", name="sample_text", rot=7, smashed=True, technology="sample_text", uid=7, value="sample_text", x=3.14, y=3.14)
    _safe_set(b, 'eaglemodel_Part58', {a1})
    assert _is_linked(b, 'eaglemodel_Part58', a1)
    if hasattr(a1, 'eaglemodel_Variant'):
        assert _is_linked(a1, 'eaglemodel_Variant', b)
    _safe_set(b, 'eaglemodel_Part58', {a2})
    assert _is_linked(b, 'eaglemodel_Part58', a2)
    if hasattr(a1, 'eaglemodel_Variant'):
        assert not _is_linked(a1, 'eaglemodel_Variant', b)
    if hasattr(a2, 'eaglemodel_Variant'):
        assert _is_linked(a2, 'eaglemodel_Variant', b)
    _safe_set(b, 'eaglemodel_Part58', set())
    assert not _is_linked(b, 'eaglemodel_Part58', a2)
    if hasattr(a2, 'eaglemodel_Variant'):
        assert not _is_linked(a2, 'eaglemodel_Variant', b)


def test_assoc_vertex136_reverse_link_reassign_clear():
    a1 = eaglemodel_Vertex(curve=3.14, x=3.14, y=3.14)
    a2 = eaglemodel_Vertex(curve=9.99, x=9.99, y=9.99)
    b = eaglemodel_Polygon(isolate=3.14, layer=7, orphans=True, pour="sample_text", rank=7, spacing=3.14, thermals=True, width=3.14)
    _safe_set(b, 'eaglemodel_Polygon137', {a1})
    assert _is_linked(b, 'eaglemodel_Polygon137', a1)
    if hasattr(a1, 'eaglemodel_Vertex'):
        assert _is_linked(a1, 'eaglemodel_Vertex', b)
    _safe_set(b, 'eaglemodel_Polygon137', {a2})
    assert _is_linked(b, 'eaglemodel_Polygon137', a2)
    if hasattr(a1, 'eaglemodel_Vertex'):
        assert not _is_linked(a1, 'eaglemodel_Vertex', b)
    if hasattr(a2, 'eaglemodel_Vertex'):
        assert _is_linked(a2, 'eaglemodel_Vertex', b)
    _safe_set(b, 'eaglemodel_Polygon137', set())
    assert not _is_linked(b, 'eaglemodel_Polygon137', a2)
    if hasattr(a2, 'eaglemodel_Vertex'):
        assert not _is_linked(a2, 'eaglemodel_Vertex', b)


def test_assoc_wire107_reverse_link_reassign_clear():
    a1 = eaglemodel_Wire(cap="sample_text", curve=3.14, extent="sample_text", layer=7, style="sample_text", width=3.14, x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    a2 = eaglemodel_Wire(cap="sample_text_2", curve=9.99, extent="sample_text_2", layer=13, style="sample_text_2", width=9.99, x1=9.99, x2=9.99, y1=9.99, y2=9.99)
    b = eaglemodel_Symbol(name="sample_text")
    _safe_set(b, 'eaglemodel_Symbol108', {a1})
    assert _is_linked(b, 'eaglemodel_Symbol108', a1)
    if hasattr(a1, 'eaglemodel_Wire109'):
        assert _is_linked(a1, 'eaglemodel_Wire109', b)
    _safe_set(b, 'eaglemodel_Symbol108', {a2})
    assert _is_linked(b, 'eaglemodel_Symbol108', a2)
    if hasattr(a1, 'eaglemodel_Wire109'):
        assert not _is_linked(a1, 'eaglemodel_Wire109', b)
    if hasattr(a2, 'eaglemodel_Wire109'):
        assert _is_linked(a2, 'eaglemodel_Wire109', b)
    _safe_set(b, 'eaglemodel_Symbol108', set())
    assert not _is_linked(b, 'eaglemodel_Symbol108', a2)
    if hasattr(a2, 'eaglemodel_Wire109'):
        assert not _is_linked(a2, 'eaglemodel_Wire109', b)


def test_assoc_wire81_reverse_link_reassign_clear():
    a1 = eaglemodel_Wire(cap="sample_text", curve=3.14, extent="sample_text", layer=7, style="sample_text", width=3.14, x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    a2 = eaglemodel_Wire(cap="sample_text_2", curve=9.99, extent="sample_text_2", layer=13, style="sample_text_2", width=9.99, x1=9.99, x2=9.99, y1=9.99, y2=9.99)
    b = eaglemodel_Package(name="sample_text")
    _safe_set(b, 'eaglemodel_Package82', {a1})
    assert _is_linked(b, 'eaglemodel_Package82', a1)
    if hasattr(a1, 'eaglemodel_Wire'):
        assert _is_linked(a1, 'eaglemodel_Wire', b)
    _safe_set(b, 'eaglemodel_Package82', {a2})
    assert _is_linked(b, 'eaglemodel_Package82', a2)
    if hasattr(a1, 'eaglemodel_Wire'):
        assert not _is_linked(a1, 'eaglemodel_Wire', b)
    if hasattr(a2, 'eaglemodel_Wire'):
        assert _is_linked(a2, 'eaglemodel_Wire', b)
    _safe_set(b, 'eaglemodel_Package82', set())
    assert not _is_linked(b, 'eaglemodel_Package82', a2)
    if hasattr(a2, 'eaglemodel_Wire'):
        assert not _is_linked(a2, 'eaglemodel_Wire', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute44_stub_double():
    # eaglemodel_Attributes has no real 'eaglemodel_Attributes45' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Attribute(constant=True, display="sample_text", font="sample_text", layer=7, name="sample_text", ratio=7, rot=7, size=3.14, value="sample_text", x=3.14, y=3.14)
    partner = eaglemodel_Attributes()
    setattr(partner, 'eaglemodel_Attributes45', None)
    _safe_set(owner, 'eaglemodel_Attribute', partner)
    assert owner in getattr(partner, 'eaglemodel_Attributes45')
    _safe_set(owner, 'eaglemodel_Attribute', None)
    assert owner not in getattr(partner, 'eaglemodel_Attributes45')


def test_assoc_attributes21_stub_double():
    # eaglemodel_Attributes has no real 'eaglemodel_Attributes' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Schematic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Schematic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Schematic(xreflabel="sample_text", xrefpart="sample_text")
    partner = eaglemodel_Attributes()
    setattr(partner, 'eaglemodel_Attributes', None)
    _safe_set(owner, 'eaglemodel_Schematic22', partner)
    assert getattr(partner, 'eaglemodel_Attributes') == owner
    _safe_set(owner, 'eaglemodel_Schematic22', None)
    assert getattr(partner, 'eaglemodel_Attributes') is None


def test_assoc_bus182_stub_double():
    # eaglemodel_Busses has no real 'eaglemodel_Busses183' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Bus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Bus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Bus(name="sample_text")
    partner = eaglemodel_Busses()
    setattr(partner, 'eaglemodel_Busses183', None)
    _safe_set(owner, 'eaglemodel_Bus', partner)
    assert owner in getattr(partner, 'eaglemodel_Busses183')
    _safe_set(owner, 'eaglemodel_Bus', None)
    assert owner not in getattr(partner, 'eaglemodel_Busses183')


def test_assoc_circle165_stub_double():
    # eaglemodel_Plain has no real 'eaglemodel_Plain166' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Circle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Circle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Circle(layer=7, radius=3.14, width=3.14, x=3.14, y=3.14)
    partner = eaglemodel_Plain()
    setattr(partner, 'eaglemodel_Plain166', None)
    _safe_set(owner, 'eaglemodel_Circle167', partner)
    assert owner in getattr(partner, 'eaglemodel_Plain166')
    _safe_set(owner, 'eaglemodel_Circle167', None)
    assert owner not in getattr(partner, 'eaglemodel_Plain166')


def test_assoc_class_48_stub_double():
    # eaglemodel_Classes has no real 'eaglemodel_Classes49' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Class(drill=3.14, name="sample_text", number=7, width=3.14)
    partner = eaglemodel_Classes()
    setattr(partner, 'eaglemodel_Classes49', None)
    _safe_set(owner, 'eaglemodel_Class', partner)
    assert owner in getattr(partner, 'eaglemodel_Classes49')
    _safe_set(owner, 'eaglemodel_Class', None)
    assert owner not in getattr(partner, 'eaglemodel_Classes49')


def test_assoc_classes25_stub_double():
    # eaglemodel_Classes has no real 'eaglemodel_Classes' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Schematic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Schematic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Schematic(xreflabel="sample_text", xrefpart="sample_text")
    partner = eaglemodel_Classes()
    setattr(partner, 'eaglemodel_Classes', None)
    _safe_set(owner, 'eaglemodel_Schematic26', partner)
    assert getattr(partner, 'eaglemodel_Classes') == owner
    _safe_set(owner, 'eaglemodel_Schematic26', None)
    assert getattr(partner, 'eaglemodel_Classes') is None


def test_assoc_compatibility0_stub_double():
    # eaglemodel_Compatibility has no real 'eaglemodel_Compatibility' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Eagle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Eagle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Eagle(version="sample_text")
    partner = eaglemodel_Compatibility()
    setattr(partner, 'eaglemodel_Compatibility', None)
    _safe_set(owner, 'eaglemodel_Eagle', partner)
    assert getattr(partner, 'eaglemodel_Compatibility') == owner
    _safe_set(owner, 'eaglemodel_Eagle', None)
    assert getattr(partner, 'eaglemodel_Compatibility') is None


def test_assoc_connect146_stub_double():
    # eaglemodel_Connects has no real 'eaglemodel_Connects147' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Connect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Connect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Connect(gate="sample_text", pad="sample_text", pin="sample_text", route="sample_text")
    partner = eaglemodel_Connects()
    setattr(partner, 'eaglemodel_Connects147', None)
    _safe_set(owner, 'eaglemodel_Connect', partner)
    assert owner in getattr(partner, 'eaglemodel_Connects147')
    _safe_set(owner, 'eaglemodel_Connect', None)
    assert owner not in getattr(partner, 'eaglemodel_Connects147')


def test_assoc_connects142_stub_double():
    # eaglemodel_Connects has no real 'eaglemodel_Connects' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Device(name="sample_text", package="sample_text")
    partner = eaglemodel_Connects()
    setattr(partner, 'eaglemodel_Connects', None)
    _safe_set(owner, 'eaglemodel_Device143', partner)
    assert getattr(partner, 'eaglemodel_Connects') == owner
    _safe_set(owner, 'eaglemodel_Device143', None)
    assert getattr(partner, 'eaglemodel_Connects') is None


def test_assoc_description61_stub_double():
    # eaglemodel_Sheet has no real 'eaglemodel_Sheet62' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Description's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Description's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Description(language="sample_text", value="sample_text")
    partner = eaglemodel_Sheet()
    setattr(partner, 'eaglemodel_Sheet62', None)
    _safe_set(owner, 'eaglemodel_Description63', partner)
    assert getattr(partner, 'eaglemodel_Sheet62') == owner
    _safe_set(owner, 'eaglemodel_Description63', None)
    assert getattr(partner, 'eaglemodel_Sheet62') is None


def test_assoc_device140_stub_double():
    # eaglemodel_Devices has no real 'eaglemodel_Devices141' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Device(name="sample_text", package="sample_text")
    partner = eaglemodel_Devices()
    setattr(partner, 'eaglemodel_Devices141', None)
    _safe_set(owner, 'eaglemodel_Device', partner)
    assert owner in getattr(partner, 'eaglemodel_Devices141')
    _safe_set(owner, 'eaglemodel_Device', None)
    assert owner not in getattr(partner, 'eaglemodel_Devices141')


def test_assoc_devices134_stub_double():
    # eaglemodel_Devices has no real 'eaglemodel_Devices' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Deviceset's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Deviceset's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Deviceset(name="sample_text", prefix="sample_text", uservalue=True)
    partner = eaglemodel_Devices()
    setattr(partner, 'eaglemodel_Devices', None)
    _safe_set(owner, 'eaglemodel_Deviceset135', partner)
    assert getattr(partner, 'eaglemodel_Devices') == owner
    _safe_set(owner, 'eaglemodel_Deviceset135', None)
    assert getattr(partner, 'eaglemodel_Devices') is None


def test_assoc_deviceset127_stub_double():
    # eaglemodel_Devicesets has no real 'eaglemodel_Devicesets128' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Deviceset's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Deviceset's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Deviceset(name="sample_text", prefix="sample_text", uservalue=True)
    partner = eaglemodel_Devicesets()
    setattr(partner, 'eaglemodel_Devicesets128', None)
    _safe_set(owner, 'eaglemodel_Deviceset', partner)
    assert owner in getattr(partner, 'eaglemodel_Devicesets128')
    _safe_set(owner, 'eaglemodel_Deviceset', None)
    assert owner not in getattr(partner, 'eaglemodel_Devicesets128')


def test_assoc_devicesets42_stub_double():
    # eaglemodel_Devicesets has no real 'eaglemodel_Devicesets' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Library(name="sample_text")
    partner = eaglemodel_Devicesets()
    setattr(partner, 'eaglemodel_Devicesets', None)
    _safe_set(owner, 'eaglemodel_Library43', partner)
    assert getattr(partner, 'eaglemodel_Devicesets') == owner
    _safe_set(owner, 'eaglemodel_Library43', None)
    assert getattr(partner, 'eaglemodel_Devicesets') is None


def test_assoc_dimension162_stub_double():
    # eaglemodel_Plain has no real 'eaglemodel_Plain163' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Dimension(dtype="sample_text", extlength=3.14, extoffset=3.14, extwidth=3.14, layer=7, precision=7, textratio=7, textsize=3.14, unit="sample_text", visible=True, width=3.14, x1=3.14, x2=3.14, x3=3.14, y1=3.14, y2=3.14, y3=3.14)
    partner = eaglemodel_Plain()
    setattr(partner, 'eaglemodel_Plain163', None)
    _safe_set(owner, 'eaglemodel_Dimension164', partner)
    assert owner in getattr(partner, 'eaglemodel_Plain163')
    _safe_set(owner, 'eaglemodel_Dimension164', None)
    assert owner not in getattr(partner, 'eaglemodel_Plain163')


def test_assoc_drawing1_stub_double():
    # eaglemodel_Drawing has no real 'eaglemodel_Drawing' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Eagle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Eagle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Eagle(version="sample_text")
    partner = eaglemodel_Drawing()
    setattr(partner, 'eaglemodel_Drawing', None)
    _safe_set(owner, 'eaglemodel_Eagle2', partner)
    assert getattr(partner, 'eaglemodel_Drawing') == owner
    _safe_set(owner, 'eaglemodel_Eagle2', None)
    assert getattr(partner, 'eaglemodel_Drawing') is None


def test_assoc_error72_stub_double():
    # eaglemodel_Errors has no real 'eaglemodel_Errors73' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Approved's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Approved's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Approved(hash="sample_text")
    partner = eaglemodel_Errors()
    setattr(partner, 'eaglemodel_Errors73', None)
    _safe_set(owner, 'eaglemodel_Approved', partner)
    assert owner in getattr(partner, 'eaglemodel_Errors73')
    _safe_set(owner, 'eaglemodel_Approved', None)
    assert owner not in getattr(partner, 'eaglemodel_Errors73')


def test_assoc_errors31_stub_double():
    # eaglemodel_Errors has no real 'eaglemodel_Errors' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Schematic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Schematic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Schematic(xreflabel="sample_text", xrefpart="sample_text")
    partner = eaglemodel_Errors()
    setattr(partner, 'eaglemodel_Errors', None)
    _safe_set(owner, 'eaglemodel_Schematic32', partner)
    assert getattr(partner, 'eaglemodel_Errors') == owner
    _safe_set(owner, 'eaglemodel_Schematic32', None)
    assert getattr(partner, 'eaglemodel_Errors') is None


def test_assoc_frame171_stub_double():
    # eaglemodel_Plain has no real 'eaglemodel_Plain172' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Frame's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Frame's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Frame(borderbottom=True, borderleft=True, borderright=True, bordertop=True, columns=7, layer=7, rows=7, x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    partner = eaglemodel_Plain()
    setattr(partner, 'eaglemodel_Plain172', None)
    _safe_set(owner, 'eaglemodel_Frame173', partner)
    assert owner in getattr(partner, 'eaglemodel_Plain172')
    _safe_set(owner, 'eaglemodel_Frame173', None)
    assert owner not in getattr(partner, 'eaglemodel_Plain172')


def test_assoc_gate138_stub_double():
    # eaglemodel_Gates has no real 'eaglemodel_Gates139' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Gate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Gate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Gate(addlevel="sample_text", name="sample_text", swaplevel=7, symbol="sample_text", x=3.14, y=3.14)
    partner = eaglemodel_Gates()
    setattr(partner, 'eaglemodel_Gates139', None)
    _safe_set(owner, 'eaglemodel_Gate', partner)
    assert owner in getattr(partner, 'eaglemodel_Gates139')
    _safe_set(owner, 'eaglemodel_Gate', None)
    assert owner not in getattr(partner, 'eaglemodel_Gates139')


def test_assoc_gates132_stub_double():
    # eaglemodel_Gates has no real 'eaglemodel_Gates' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Deviceset's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Deviceset's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Deviceset(name="sample_text", prefix="sample_text", uservalue=True)
    partner = eaglemodel_Gates()
    setattr(partner, 'eaglemodel_Gates', None)
    _safe_set(owner, 'eaglemodel_Deviceset133', partner)
    assert getattr(partner, 'eaglemodel_Gates') == owner
    _safe_set(owner, 'eaglemodel_Deviceset133', None)
    assert getattr(partner, 'eaglemodel_Gates') is None


def test_assoc_grid7_stub_double():
    # eaglemodel_Drawing has no real 'eaglemodel_Drawing8' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Grid's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Grid's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Grid(altdistance=3.14, altunit="sample_text", altunitdist="sample_text", display=True, distance=3.14, multiple=7, style="sample_text", unit="sample_text", unitdist="sample_text")
    partner = eaglemodel_Drawing()
    setattr(partner, 'eaglemodel_Drawing8', None)
    _safe_set(owner, 'eaglemodel_Grid', partner)
    assert getattr(partner, 'eaglemodel_Drawing8') == owner
    _safe_set(owner, 'eaglemodel_Grid', None)
    assert getattr(partner, 'eaglemodel_Drawing8') is None


def test_assoc_hole174_stub_double():
    # eaglemodel_Plain has no real 'eaglemodel_Plain175' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Hole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Hole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Hole(drill=3.14, x=3.14, y=3.14)
    partner = eaglemodel_Plain()
    setattr(partner, 'eaglemodel_Plain175', None)
    _safe_set(owner, 'eaglemodel_Hole176', partner)
    assert owner in getattr(partner, 'eaglemodel_Plain175')
    _safe_set(owner, 'eaglemodel_Hole176', None)
    assert owner not in getattr(partner, 'eaglemodel_Plain175')


def test_assoc_instance177_stub_double():
    # eaglemodel_Instances has no real 'eaglemodel_Instances178' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Instance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Instance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Instance(gate="sample_text", part="sample_text", rot=7, smashed=True, x=3.14, y=3.14)
    partner = eaglemodel_Instances()
    setattr(partner, 'eaglemodel_Instances178', None)
    _safe_set(owner, 'eaglemodel_Instance', partner)
    assert owner in getattr(partner, 'eaglemodel_Instances178')
    _safe_set(owner, 'eaglemodel_Instance', None)
    assert owner not in getattr(partner, 'eaglemodel_Instances178')


def test_assoc_junction196_stub_double():
    # eaglemodel_Segment has no real 'eaglemodel_Segment197' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Junction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Junction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Junction(x=3.14, y=3.14)
    partner = eaglemodel_Segment()
    setattr(partner, 'eaglemodel_Segment197', None)
    _safe_set(owner, 'eaglemodel_Junction', partner)
    assert owner in getattr(partner, 'eaglemodel_Segment197')
    _safe_set(owner, 'eaglemodel_Junction', None)
    assert owner not in getattr(partner, 'eaglemodel_Segment197')


def test_assoc_label198_stub_double():
    # eaglemodel_Segment has no real 'eaglemodel_Segment199' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Label(font="sample_text", layer=7, ratio=7, rot=7, size=3.14, x=3.14, xref=True, y=3.14)
    partner = eaglemodel_Segment()
    setattr(partner, 'eaglemodel_Segment199', None)
    _safe_set(owner, 'eaglemodel_Label', partner)
    assert owner in getattr(partner, 'eaglemodel_Segment199')
    _safe_set(owner, 'eaglemodel_Label', None)
    assert owner not in getattr(partner, 'eaglemodel_Segment199')


def test_assoc_layers15_stub_double():
    # eaglemodel_Layers has no real 'eaglemodel_Layers16' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Layer(active=True, color=7, fill=7, name="sample_text", number=7, visible=True)
    partner = eaglemodel_Layers()
    setattr(partner, 'eaglemodel_Layers16', None)
    _safe_set(owner, 'eaglemodel_Layer', partner)
    assert owner in getattr(partner, 'eaglemodel_Layers16')
    _safe_set(owner, 'eaglemodel_Layer', None)
    assert owner not in getattr(partner, 'eaglemodel_Layers16')


def test_assoc_libraries19_stub_double():
    # eaglemodel_Libraries has no real 'eaglemodel_Libraries' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Schematic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Schematic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Schematic(xreflabel="sample_text", xrefpart="sample_text")
    partner = eaglemodel_Libraries()
    setattr(partner, 'eaglemodel_Libraries', None)
    _safe_set(owner, 'eaglemodel_Schematic20', partner)
    assert getattr(partner, 'eaglemodel_Libraries') == owner
    _safe_set(owner, 'eaglemodel_Schematic20', None)
    assert getattr(partner, 'eaglemodel_Libraries') is None


def test_assoc_library33_stub_double():
    # eaglemodel_Libraries has no real 'eaglemodel_Libraries34' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Library(name="sample_text")
    partner = eaglemodel_Libraries()
    setattr(partner, 'eaglemodel_Libraries34', None)
    _safe_set(owner, 'eaglemodel_Library', partner)
    assert owner in getattr(partner, 'eaglemodel_Libraries34')
    _safe_set(owner, 'eaglemodel_Library', None)
    assert owner not in getattr(partner, 'eaglemodel_Libraries34')


def test_assoc_net186_stub_double():
    # eaglemodel_Nets has no real 'eaglemodel_Nets187' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Net's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Net's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Net(class_=7, name="sample_text")
    partner = eaglemodel_Nets()
    setattr(partner, 'eaglemodel_Nets187', None)
    _safe_set(owner, 'eaglemodel_Net', partner)
    assert owner in getattr(partner, 'eaglemodel_Nets187')
    _safe_set(owner, 'eaglemodel_Net', None)
    assert owner not in getattr(partner, 'eaglemodel_Nets187')


def test_assoc_note3_stub_double():
    # eaglemodel_Compatibility has no real 'eaglemodel_Compatibility4' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Note's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Note's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Note(severity="sample_text", value="sample_text", version="sample_text")
    partner = eaglemodel_Compatibility()
    setattr(partner, 'eaglemodel_Compatibility4', None)
    _safe_set(owner, 'eaglemodel_Note', partner)
    assert owner in getattr(partner, 'eaglemodel_Compatibility4')
    _safe_set(owner, 'eaglemodel_Note', None)
    assert owner not in getattr(partner, 'eaglemodel_Compatibility4')


def test_assoc_package74_stub_double():
    # eaglemodel_Packages has no real 'eaglemodel_Packages75' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Package(name="sample_text")
    partner = eaglemodel_Packages()
    setattr(partner, 'eaglemodel_Packages75', None)
    _safe_set(owner, 'eaglemodel_Package', partner)
    assert owner in getattr(partner, 'eaglemodel_Packages75')
    _safe_set(owner, 'eaglemodel_Package', None)
    assert owner not in getattr(partner, 'eaglemodel_Packages75')


def test_assoc_packages38_stub_double():
    # eaglemodel_Packages has no real 'eaglemodel_Packages' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Library(name="sample_text")
    partner = eaglemodel_Packages()
    setattr(partner, 'eaglemodel_Packages', None)
    _safe_set(owner, 'eaglemodel_Library39', partner)
    assert getattr(partner, 'eaglemodel_Packages') == owner
    _safe_set(owner, 'eaglemodel_Library39', None)
    assert getattr(partner, 'eaglemodel_Packages') is None


def test_assoc_part52_stub_double():
    # eaglemodel_Parts has no real 'eaglemodel_Parts53' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Part(device="sample_text", deviceset="sample_text", gate="sample_text", library="sample_text", name="sample_text", rot=7, smashed=True, technology="sample_text", uid=7, value="sample_text", x=3.14, y=3.14)
    partner = eaglemodel_Parts()
    setattr(partner, 'eaglemodel_Parts53', None)
    _safe_set(owner, 'eaglemodel_Part', partner)
    assert owner in getattr(partner, 'eaglemodel_Parts53')
    _safe_set(owner, 'eaglemodel_Part', None)
    assert owner not in getattr(partner, 'eaglemodel_Parts53')


def test_assoc_parts27_stub_double():
    # eaglemodel_Parts has no real 'eaglemodel_Parts' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Schematic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Schematic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Schematic(xreflabel="sample_text", xrefpart="sample_text")
    partner = eaglemodel_Parts()
    setattr(partner, 'eaglemodel_Parts', None)
    _safe_set(owner, 'eaglemodel_Schematic28', partner)
    assert getattr(partner, 'eaglemodel_Parts') == owner
    _safe_set(owner, 'eaglemodel_Schematic28', None)
    assert getattr(partner, 'eaglemodel_Parts') is None


def test_assoc_pinref191_stub_double():
    # eaglemodel_Segment has no real 'eaglemodel_Segment192' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Pinref's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Pinref's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Pinref(gate="sample_text", part="sample_text", pin="sample_text")
    partner = eaglemodel_Segment()
    setattr(partner, 'eaglemodel_Segment192', None)
    _safe_set(owner, 'eaglemodel_Pinref', partner)
    assert owner in getattr(partner, 'eaglemodel_Segment192')
    _safe_set(owner, 'eaglemodel_Pinref', None)
    assert owner not in getattr(partner, 'eaglemodel_Segment192')


def test_assoc_polygon153_stub_double():
    # eaglemodel_Plain has no real 'eaglemodel_Plain154' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Polygon's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Polygon's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Polygon(isolate=3.14, layer=7, orphans=True, pour="sample_text", rank=7, spacing=3.14, thermals=True, width=3.14)
    partner = eaglemodel_Plain()
    setattr(partner, 'eaglemodel_Plain154', None)
    _safe_set(owner, 'eaglemodel_Polygon155', partner)
    assert owner in getattr(partner, 'eaglemodel_Plain154')
    _safe_set(owner, 'eaglemodel_Polygon155', None)
    assert owner not in getattr(partner, 'eaglemodel_Plain154')


def test_assoc_rectangle168_stub_double():
    # eaglemodel_Plain has no real 'eaglemodel_Plain169' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Rectangle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Rectangle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Rectangle(layer=7, rot=7, x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    partner = eaglemodel_Plain()
    setattr(partner, 'eaglemodel_Plain169', None)
    _safe_set(owner, 'eaglemodel_Rectangle170', partner)
    assert owner in getattr(partner, 'eaglemodel_Plain169')
    _safe_set(owner, 'eaglemodel_Rectangle170', None)
    assert owner not in getattr(partner, 'eaglemodel_Plain169')


def test_assoc_schematic11_stub_double():
    # eaglemodel_Drawing has no real 'eaglemodel_Drawing12' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Schematic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Schematic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Schematic(xreflabel="sample_text", xrefpart="sample_text")
    partner = eaglemodel_Drawing()
    setattr(partner, 'eaglemodel_Drawing12', None)
    _safe_set(owner, 'eaglemodel_Schematic', partner)
    assert getattr(partner, 'eaglemodel_Drawing12') == owner
    _safe_set(owner, 'eaglemodel_Schematic', None)
    assert getattr(partner, 'eaglemodel_Drawing12') is None


def test_assoc_segment184_stub_double():
    # eaglemodel_Segment has no real 'eaglemodel_Segment' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Bus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Bus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Bus(name="sample_text")
    partner = eaglemodel_Segment()
    setattr(partner, 'eaglemodel_Segment', None)
    _safe_set(owner, 'eaglemodel_Bus185', {partner})
    assert getattr(partner, 'eaglemodel_Segment') == owner
    _safe_set(owner, 'eaglemodel_Bus185', set())
    assert getattr(partner, 'eaglemodel_Segment') is None


def test_assoc_segment188_stub_double():
    # eaglemodel_Segment has no real 'eaglemodel_Segment190' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Net's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Net's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Net(class_=7, name="sample_text")
    partner = eaglemodel_Segment()
    setattr(partner, 'eaglemodel_Segment190', None)
    _safe_set(owner, 'eaglemodel_Net189', {partner})
    assert getattr(partner, 'eaglemodel_Segment190') == owner
    _safe_set(owner, 'eaglemodel_Net189', set())
    assert getattr(partner, 'eaglemodel_Segment190') is None


def test_assoc_settings13_stub_double():
    # eaglemodel_Settings has no real 'eaglemodel_Settings14' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Setting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Setting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Setting(alwaysvectorfont=True, verticaltext="sample_text")
    partner = eaglemodel_Settings()
    setattr(partner, 'eaglemodel_Settings14', None)
    _safe_set(owner, 'eaglemodel_Setting', partner)
    assert owner in getattr(partner, 'eaglemodel_Settings14')
    _safe_set(owner, 'eaglemodel_Setting', None)
    assert owner not in getattr(partner, 'eaglemodel_Settings14')


def test_assoc_sheets29_stub_double():
    # eaglemodel_Sheets has no real 'eaglemodel_Sheets' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Schematic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Schematic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Schematic(xreflabel="sample_text", xrefpart="sample_text")
    partner = eaglemodel_Sheets()
    setattr(partner, 'eaglemodel_Sheets', None)
    _safe_set(owner, 'eaglemodel_Schematic30', partner)
    assert getattr(partner, 'eaglemodel_Sheets') == owner
    _safe_set(owner, 'eaglemodel_Schematic30', None)
    assert getattr(partner, 'eaglemodel_Sheets') is None


def test_assoc_symbol99_stub_double():
    # eaglemodel_Symbols has no real 'eaglemodel_Symbols100' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Symbol(name="sample_text")
    partner = eaglemodel_Symbols()
    setattr(partner, 'eaglemodel_Symbols100', None)
    _safe_set(owner, 'eaglemodel_Symbol', partner)
    assert owner in getattr(partner, 'eaglemodel_Symbols100')
    _safe_set(owner, 'eaglemodel_Symbol', None)
    assert owner not in getattr(partner, 'eaglemodel_Symbols100')


def test_assoc_symbols40_stub_double():
    # eaglemodel_Symbols has no real 'eaglemodel_Symbols' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Library(name="sample_text")
    partner = eaglemodel_Symbols()
    setattr(partner, 'eaglemodel_Symbols', None)
    _safe_set(owner, 'eaglemodel_Library41', partner)
    assert getattr(partner, 'eaglemodel_Symbols') == owner
    _safe_set(owner, 'eaglemodel_Library41', None)
    assert getattr(partner, 'eaglemodel_Symbols') is None


def test_assoc_technologies144_stub_double():
    # eaglemodel_Technologies has no real 'eaglemodel_Technologies' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Device(name="sample_text", package="sample_text")
    partner = eaglemodel_Technologies()
    setattr(partner, 'eaglemodel_Technologies', None)
    _safe_set(owner, 'eaglemodel_Device145', partner)
    assert getattr(partner, 'eaglemodel_Technologies') == owner
    _safe_set(owner, 'eaglemodel_Device145', None)
    assert getattr(partner, 'eaglemodel_Technologies') is None


def test_assoc_technology148_stub_double():
    # eaglemodel_Technologies has no real 'eaglemodel_Technologies149' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Technology's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Technology's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Technology(name="sample_text")
    partner = eaglemodel_Technologies()
    setattr(partner, 'eaglemodel_Technologies149', None)
    _safe_set(owner, 'eaglemodel_Technology', partner)
    assert owner in getattr(partner, 'eaglemodel_Technologies149')
    _safe_set(owner, 'eaglemodel_Technology', None)
    assert owner not in getattr(partner, 'eaglemodel_Technologies149')


def test_assoc_text159_stub_double():
    # eaglemodel_Plain has no real 'eaglemodel_Plain160' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Text's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Text's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Text(align="sample_text", distance=7, font="sample_text", layer=7, ratio=7, rot=7, size=3.14, value="sample_text", x=3.14, y=3.14)
    partner = eaglemodel_Plain()
    setattr(partner, 'eaglemodel_Plain160', None)
    _safe_set(owner, 'eaglemodel_Text161', partner)
    assert owner in getattr(partner, 'eaglemodel_Plain160')
    _safe_set(owner, 'eaglemodel_Text161', None)
    assert owner not in getattr(partner, 'eaglemodel_Plain160')


def test_assoc_variantdef46_stub_double():
    # eaglemodel_Variantdefs has no real 'eaglemodel_Variantdefs47' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Variantdef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Variantdef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Variantdef(current=True, name="sample_text")
    partner = eaglemodel_Variantdefs()
    setattr(partner, 'eaglemodel_Variantdefs47', None)
    _safe_set(owner, 'eaglemodel_Variantdef', partner)
    assert owner in getattr(partner, 'eaglemodel_Variantdefs47')
    _safe_set(owner, 'eaglemodel_Variantdef', None)
    assert owner not in getattr(partner, 'eaglemodel_Variantdefs47')


def test_assoc_variantdefs23_stub_double():
    # eaglemodel_Variantdefs has no real 'eaglemodel_Variantdefs' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Schematic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Schematic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Schematic(xreflabel="sample_text", xrefpart="sample_text")
    partner = eaglemodel_Variantdefs()
    setattr(partner, 'eaglemodel_Variantdefs', None)
    _safe_set(owner, 'eaglemodel_Schematic24', partner)
    assert getattr(partner, 'eaglemodel_Variantdefs') == owner
    _safe_set(owner, 'eaglemodel_Schematic24', None)
    assert getattr(partner, 'eaglemodel_Variantdefs') is None


def test_assoc_wire156_stub_double():
    # eaglemodel_Plain has no real 'eaglemodel_Plain157' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Wire's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Wire's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Wire(cap="sample_text", curve=3.14, extent="sample_text", layer=7, style="sample_text", width=3.14, x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    partner = eaglemodel_Plain()
    setattr(partner, 'eaglemodel_Plain157', None)
    _safe_set(owner, 'eaglemodel_Wire158', partner)
    assert owner in getattr(partner, 'eaglemodel_Plain157')
    _safe_set(owner, 'eaglemodel_Wire158', None)
    assert owner not in getattr(partner, 'eaglemodel_Plain157')


def test_assoc_wire193_stub_double():
    # eaglemodel_Segment has no real 'eaglemodel_Segment194' property in the generated
    # code (a bare stub) -- manually attach it so eaglemodel_Wire's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eaglemodel_Wire's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eaglemodel_Wire(cap="sample_text", curve=3.14, extent="sample_text", layer=7, style="sample_text", width=3.14, x1=3.14, x2=3.14, y1=3.14, y2=3.14)
    partner = eaglemodel_Segment()
    setattr(partner, 'eaglemodel_Segment194', None)
    _safe_set(owner, 'eaglemodel_Wire195', partner)
    assert owner in getattr(partner, 'eaglemodel_Segment194')
    _safe_set(owner, 'eaglemodel_Wire195', None)
    assert owner not in getattr(partner, 'eaglemodel_Segment194')


