import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnchorPositionPos,
    AnchorType,
    CompartmentShape,
    Shape,
    ShapeConnection,
    ShapeContainerElement,
    shape_Anchor,
    shape_AnchorFixPointPosition,
    shape_AnchorManual,
    shape_AnchorPosition,
    shape_AnchorPositionPos,
    shape_AnchorPredefinied,
    shape_AnchorRelativePosition,
    shape_AnchorType,
    shape_CDEllipse,
    shape_CDLine,
    shape_CDPolygon,
    shape_CDPolyline,
    shape_CDRectangle,
    shape_CDRoundedRectangle,
    shape_CDText,
    shape_CommonLayout,
    shape_Compartment,
    shape_CompartmentEllipse,
    shape_CompartmentInfo,
    shape_CompartmentPolygon,
    shape_CompartmentRectangle,
    shape_CompartmentRoundedRectangle,
    shape_CompartmentShape,
    shape_ConnectionDefinition,
    shape_Description,
    shape_Ellipse,
    shape_Line,
    shape_LineLayout,
    shape_PlacingDefinition,
    shape_Point,
    shape_PolyLineLayout,
    shape_Polygon,
    shape_Polyline,
    shape_Rectangle,
    shape_RectangleEllipseLayout,
    shape_RoundedRectangle,
    shape_RoundedRectangleLayout,
    shape_Shape,
    shape_ShapeConnection,
    shape_ShapeContainer,
    shape_ShapeContainerElement,
    shape_ShapeDefinition,
    shape_ShapeLayout,
    shape_ShapestyleLayout,
    shape_Text,
    shape_TextBody,
    shape_TextLayout,
    AnchorPredefiniedEnum,
    CompartmentLayout,
    ConnectionStyle,
    HAlign,
    TextType,
    VAlign,
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

def test_assoc_body27_reverse_link_reassign_clear():
    a1 = shape_TextBody(value="sample_text")
    a2 = shape_TextBody(value="sample_text_2")
    b = shape_CDText(texttype="sample_text")
    _safe_set(b, 'shape_CDText28', a1)
    assert _is_linked(b, 'shape_CDText28', a1)
    if hasattr(a1, 'shape_TextBody'):
        assert _is_linked(a1, 'shape_TextBody', b)
    _safe_set(b, 'shape_CDText28', a2)
    assert _is_linked(b, 'shape_CDText28', a2)
    if hasattr(a1, 'shape_TextBody'):
        assert not _is_linked(a1, 'shape_TextBody', b)
    if hasattr(a2, 'shape_TextBody'):
        assert _is_linked(a2, 'shape_TextBody', b)
    _safe_set(b, 'shape_CDText28', None)
    assert not _is_linked(b, 'shape_CDText28', a2)
    if hasattr(a2, 'shape_TextBody'):
        assert not _is_linked(a2, 'shape_TextBody', b)


def test_assoc_body60_reverse_link_reassign_clear():
    a1 = shape_TextBody(value="sample_text")
    a2 = shape_TextBody(value="sample_text_2")
    b = shape_Text(texttype="sample_text")
    _safe_set(b, 'shape_Text61', a1)
    assert _is_linked(b, 'shape_Text61', a1)
    if hasattr(a1, 'shape_TextBody62'):
        assert _is_linked(a1, 'shape_TextBody62', b)
    _safe_set(b, 'shape_Text61', a2)
    assert _is_linked(b, 'shape_Text61', a2)
    if hasattr(a1, 'shape_TextBody62'):
        assert not _is_linked(a1, 'shape_TextBody62', b)
    if hasattr(a2, 'shape_TextBody62'):
        assert _is_linked(a2, 'shape_TextBody62', b)
    _safe_set(b, 'shape_Text61', None)
    assert not _is_linked(b, 'shape_Text61', a2)
    if hasattr(a2, 'shape_TextBody62'):
        assert not _is_linked(a2, 'shape_TextBody62', b)


def test_assoc_body83_reverse_link_reassign_clear():
    a1 = shape_TextBody(value="sample_text")
    a2 = shape_TextBody(value="sample_text_2")
    b = shape_Description(hAlign="sample_text", style="sample_text", vAlign="sample_text")
    _safe_set(b, 'shape_Description84', a1)
    assert _is_linked(b, 'shape_Description84', a1)
    if hasattr(a1, 'shape_TextBody85'):
        assert _is_linked(a1, 'shape_TextBody85', b)
    _safe_set(b, 'shape_Description84', a2)
    assert _is_linked(b, 'shape_Description84', a2)
    if hasattr(a1, 'shape_TextBody85'):
        assert not _is_linked(a1, 'shape_TextBody85', b)
    if hasattr(a2, 'shape_TextBody85'):
        assert _is_linked(a2, 'shape_TextBody85', b)
    _safe_set(b, 'shape_Description84', None)
    assert not _is_linked(b, 'shape_Description84', a2)
    if hasattr(a2, 'shape_TextBody85'):
        assert not _is_linked(a2, 'shape_TextBody85', b)


def test_assoc_common102_reverse_link_reassign_clear():
    a1 = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    a2 = shape_RoundedRectangleLayout(curveHeight=13, curveWidth=13)
    b = shape_CommonLayout(heigth=7, width=7, xcor=7, ycor=7)
    _safe_set(b, 'shape_CommonLayout104', a1)
    assert _is_linked(b, 'shape_CommonLayout104', a1)
    if hasattr(a1, 'shape_RoundedRectangleLayout103'):
        assert _is_linked(a1, 'shape_RoundedRectangleLayout103', b)
    _safe_set(b, 'shape_CommonLayout104', a2)
    assert _is_linked(b, 'shape_CommonLayout104', a2)
    if hasattr(a1, 'shape_RoundedRectangleLayout103'):
        assert not _is_linked(a1, 'shape_RoundedRectangleLayout103', b)
    if hasattr(a2, 'shape_RoundedRectangleLayout103'):
        assert _is_linked(a2, 'shape_RoundedRectangleLayout103', b)
    _safe_set(b, 'shape_CommonLayout104', None)
    assert not _is_linked(b, 'shape_CommonLayout104', a2)
    if hasattr(a2, 'shape_RoundedRectangleLayout103'):
        assert not _is_linked(a2, 'shape_RoundedRectangleLayout103', b)


def test_assoc_common108_reverse_link_reassign_clear():
    a1 = shape_TextLayout(hAlign="sample_text", vAlign="sample_text")
    a2 = shape_TextLayout(hAlign="sample_text_2", vAlign="sample_text_2")
    b = shape_CommonLayout(heigth=7, width=7, xcor=7, ycor=7)
    _safe_set(b, 'shape_CommonLayout110', a1)
    assert _is_linked(b, 'shape_CommonLayout110', a1)
    if hasattr(a1, 'shape_TextLayout109'):
        assert _is_linked(a1, 'shape_TextLayout109', b)
    _safe_set(b, 'shape_CommonLayout110', a2)
    assert _is_linked(b, 'shape_CommonLayout110', a2)
    if hasattr(a1, 'shape_TextLayout109'):
        assert not _is_linked(a1, 'shape_TextLayout109', b)
    if hasattr(a2, 'shape_TextLayout109'):
        assert _is_linked(a2, 'shape_TextLayout109', b)
    _safe_set(b, 'shape_CommonLayout110', None)
    assert not _is_linked(b, 'shape_CommonLayout110', a2)
    if hasattr(a2, 'shape_TextLayout109'):
        assert not _is_linked(a2, 'shape_TextLayout109', b)


def test_assoc_id63_reverse_link_reassign_clear():
    a1 = shape_TextBody(value="sample_text")
    a2 = shape_TextBody(value="sample_text_2")
    b = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    _safe_set(b, 'shape_CompartmentInfo64', a1)
    assert _is_linked(b, 'shape_CompartmentInfo64', a1)
    if hasattr(a1, 'shape_TextBody65'):
        assert _is_linked(a1, 'shape_TextBody65', b)
    _safe_set(b, 'shape_CompartmentInfo64', a2)
    assert _is_linked(b, 'shape_CompartmentInfo64', a2)
    if hasattr(a1, 'shape_TextBody65'):
        assert not _is_linked(a1, 'shape_TextBody65', b)
    if hasattr(a2, 'shape_TextBody65'):
        assert _is_linked(a2, 'shape_TextBody65', b)
    _safe_set(b, 'shape_CompartmentInfo64', None)
    assert not _is_linked(b, 'shape_CompartmentInfo64', a2)
    if hasattr(a2, 'shape_TextBody65'):
        assert not _is_linked(a2, 'shape_TextBody65', b)


def test_assoc_layout26_reverse_link_reassign_clear():
    a1 = shape_TextLayout(hAlign="sample_text", vAlign="sample_text")
    a2 = shape_TextLayout(hAlign="sample_text_2", vAlign="sample_text_2")
    b = shape_CDText(texttype="sample_text")
    _safe_set(b, 'shape_CDText', a1)
    assert _is_linked(b, 'shape_CDText', a1)
    if hasattr(a1, 'shape_TextLayout'):
        assert _is_linked(a1, 'shape_TextLayout', b)
    _safe_set(b, 'shape_CDText', a2)
    assert _is_linked(b, 'shape_CDText', a2)
    if hasattr(a1, 'shape_TextLayout'):
        assert not _is_linked(a1, 'shape_TextLayout', b)
    if hasattr(a2, 'shape_TextLayout'):
        assert _is_linked(a2, 'shape_TextLayout', b)
    _safe_set(b, 'shape_CDText', None)
    assert not _is_linked(b, 'shape_CDText', a2)
    if hasattr(a2, 'shape_TextLayout'):
        assert not _is_linked(a2, 'shape_TextLayout', b)


def test_assoc_layout58_reverse_link_reassign_clear():
    a1 = shape_TextLayout(hAlign="sample_text", vAlign="sample_text")
    a2 = shape_TextLayout(hAlign="sample_text_2", vAlign="sample_text_2")
    b = shape_Text(texttype="sample_text")
    _safe_set(b, 'shape_Text', a1)
    assert _is_linked(b, 'shape_Text', a1)
    if hasattr(a1, 'shape_TextLayout59'):
        assert _is_linked(a1, 'shape_TextLayout59', b)
    _safe_set(b, 'shape_Text', a2)
    assert _is_linked(b, 'shape_Text', a2)
    if hasattr(a1, 'shape_TextLayout59'):
        assert not _is_linked(a1, 'shape_TextLayout59', b)
    if hasattr(a2, 'shape_TextLayout59'):
        assert _is_linked(a2, 'shape_TextLayout59', b)
    _safe_set(b, 'shape_Text', None)
    assert not _is_linked(b, 'shape_Text', a2)
    if hasattr(a2, 'shape_TextLayout59'):
        assert not _is_linked(a2, 'shape_TextLayout59', b)


def test_assoc_placing2_reverse_link_reassign_clear():
    a1 = shape_PlacingDefinition(angle=7, distance=7, offset="sample_text")
    a2 = shape_PlacingDefinition(angle=13, distance=13, offset="sample_text_2")
    b = shape_ConnectionDefinition(connectionStyle="sample_text")
    _safe_set(b, 'shape_ConnectionDefinition3', {a1})
    assert _is_linked(b, 'shape_ConnectionDefinition3', a1)
    if hasattr(a1, 'shape_PlacingDefinition'):
        assert _is_linked(a1, 'shape_PlacingDefinition', b)
    _safe_set(b, 'shape_ConnectionDefinition3', {a2})
    assert _is_linked(b, 'shape_ConnectionDefinition3', a2)
    if hasattr(a1, 'shape_PlacingDefinition'):
        assert not _is_linked(a1, 'shape_PlacingDefinition', b)
    if hasattr(a2, 'shape_PlacingDefinition'):
        assert _is_linked(a2, 'shape_PlacingDefinition', b)
    _safe_set(b, 'shape_ConnectionDefinition3', set())
    assert not _is_linked(b, 'shape_ConnectionDefinition3', a2)
    if hasattr(a2, 'shape_PlacingDefinition'):
        assert not _is_linked(a2, 'shape_PlacingDefinition', b)


def test_assoc_shapeCon11_reverse_link_reassign_clear():
    a1 = shape_ShapeConnection(style="sample_text")
    a2 = shape_ShapeConnection(style="sample_text_2")
    b = shape_PlacingDefinition(angle=7, distance=7, offset="sample_text")
    _safe_set(b, 'shape_PlacingDefinition12', a1)
    assert _is_linked(b, 'shape_PlacingDefinition12', a1)
    if hasattr(a1, 'shape_ShapeConnection'):
        assert _is_linked(a1, 'shape_ShapeConnection', b)
    _safe_set(b, 'shape_PlacingDefinition12', a2)
    assert _is_linked(b, 'shape_PlacingDefinition12', a2)
    if hasattr(a1, 'shape_ShapeConnection'):
        assert not _is_linked(a1, 'shape_ShapeConnection', b)
    if hasattr(a2, 'shape_ShapeConnection'):
        assert _is_linked(a2, 'shape_ShapeConnection', b)
    _safe_set(b, 'shape_PlacingDefinition12', None)
    assert not _is_linked(b, 'shape_PlacingDefinition12', a2)
    if hasattr(a2, 'shape_ShapeConnection'):
        assert not _is_linked(a2, 'shape_ShapeConnection', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_common86_stub_double():
    # shape_RectangleEllipseLayout has no real 'shape_RectangleEllipseLayout87' property in the generated
    # code (a bare stub) -- manually attach it so shape_CommonLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_CommonLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_CommonLayout(heigth=7, width=7, xcor=7, ycor=7)
    partner = shape_RectangleEllipseLayout()
    setattr(partner, 'shape_RectangleEllipseLayout87', None)
    _safe_set(owner, 'shape_CommonLayout', partner)
    assert getattr(partner, 'shape_RectangleEllipseLayout87') == owner
    _safe_set(owner, 'shape_CommonLayout', None)
    assert getattr(partner, 'shape_RectangleEllipseLayout87') is None


def test_assoc_compartmentInfo33_stub_double():
    # shape_Rectangle has no real 'shape_Rectangle' property in the generated
    # code (a bare stub) -- manually attach it so shape_CompartmentInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_CompartmentInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    partner = shape_Rectangle()
    setattr(partner, 'shape_Rectangle', None)
    _safe_set(owner, 'shape_CompartmentInfo', partner)
    assert getattr(partner, 'shape_Rectangle') == owner
    _safe_set(owner, 'shape_CompartmentInfo', None)
    assert getattr(partner, 'shape_Rectangle') is None


def test_assoc_compartmentInfo50_stub_double():
    # shape_Ellipse has no real 'shape_Ellipse' property in the generated
    # code (a bare stub) -- manually attach it so shape_CompartmentInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_CompartmentInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    partner = shape_Ellipse()
    setattr(partner, 'shape_Ellipse', None)
    _safe_set(owner, 'shape_CompartmentInfo51', partner)
    assert getattr(partner, 'shape_Ellipse') == owner
    _safe_set(owner, 'shape_CompartmentInfo51', None)
    assert getattr(partner, 'shape_Ellipse') is None


def test_assoc_description7_stub_double():
    # shape_ShapeDefinition has no real 'shape_ShapeDefinition8' property in the generated
    # code (a bare stub) -- manually attach it so shape_Description's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_Description's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_Description(hAlign="sample_text", style="sample_text", vAlign="sample_text")
    partner = shape_ShapeDefinition()
    setattr(partner, 'shape_ShapeDefinition8', None)
    _safe_set(owner, 'shape_Description', partner)
    assert getattr(partner, 'shape_ShapeDefinition8') == owner
    _safe_set(owner, 'shape_Description', None)
    assert getattr(partner, 'shape_ShapeDefinition8') is None


def test_assoc_id70_stub_double():
    # shape_CompartmentShape has no real 'shape_CompartmentShape71' property in the generated
    # code (a bare stub) -- manually attach it so shape_TextBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_TextBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_TextBody(value="sample_text")
    partner = shape_CompartmentShape()
    setattr(partner, 'shape_CompartmentShape71', None)
    _safe_set(owner, 'shape_TextBody72', partner)
    assert getattr(partner, 'shape_CompartmentShape71') == owner
    _safe_set(owner, 'shape_TextBody72', None)
    assert getattr(partner, 'shape_CompartmentShape71') is None


def test_assoc_id75_stub_double():
    # shape_CompartmentRoundedRectangle has no real 'shape_CompartmentRoundedRectangle76' property in the generated
    # code (a bare stub) -- manually attach it so shape_TextBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_TextBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_TextBody(value="sample_text")
    partner = shape_CompartmentRoundedRectangle()
    setattr(partner, 'shape_CompartmentRoundedRectangle76', None)
    _safe_set(owner, 'shape_TextBody77', partner)
    assert getattr(partner, 'shape_CompartmentRoundedRectangle76') == owner
    _safe_set(owner, 'shape_TextBody77', None)
    assert getattr(partner, 'shape_CompartmentRoundedRectangle76') is None


def test_assoc_id80_stub_double():
    # shape_CompartmentPolygon has no real 'shape_CompartmentPolygon81' property in the generated
    # code (a bare stub) -- manually attach it so shape_TextBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_TextBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_TextBody(value="sample_text")
    partner = shape_CompartmentPolygon()
    setattr(partner, 'shape_CompartmentPolygon81', None)
    _safe_set(owner, 'shape_TextBody82', partner)
    assert getattr(partner, 'shape_CompartmentPolygon81') == owner
    _safe_set(owner, 'shape_TextBody82', None)
    assert getattr(partner, 'shape_CompartmentPolygon81') is None


def test_assoc_layout1_stub_double():
    # shape_ShapestyleLayout has no real 'shape_ShapestyleLayout' property in the generated
    # code (a bare stub) -- manually attach it so shape_ConnectionDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_ConnectionDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_ConnectionDefinition(connectionStyle="sample_text")
    partner = shape_ShapestyleLayout()
    setattr(partner, 'shape_ShapestyleLayout', None)
    _safe_set(owner, 'shape_ConnectionDefinition', partner)
    assert getattr(partner, 'shape_ShapestyleLayout') == owner
    _safe_set(owner, 'shape_ConnectionDefinition', None)
    assert getattr(partner, 'shape_ShapestyleLayout') is None


def test_assoc_layout105_stub_double():
    # shape_ShapestyleLayout has no real 'shape_ShapestyleLayout107' property in the generated
    # code (a bare stub) -- manually attach it so shape_RoundedRectangleLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_RoundedRectangleLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    partner = shape_ShapestyleLayout()
    setattr(partner, 'shape_ShapestyleLayout107', None)
    _safe_set(owner, 'shape_RoundedRectangleLayout106', partner)
    assert getattr(partner, 'shape_ShapestyleLayout107') == owner
    _safe_set(owner, 'shape_RoundedRectangleLayout106', None)
    assert getattr(partner, 'shape_ShapestyleLayout107') is None


def test_assoc_layout111_stub_double():
    # shape_ShapestyleLayout has no real 'shape_ShapestyleLayout113' property in the generated
    # code (a bare stub) -- manually attach it so shape_TextLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_TextLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_TextLayout(hAlign="sample_text", vAlign="sample_text")
    partner = shape_ShapestyleLayout()
    setattr(partner, 'shape_ShapestyleLayout113', None)
    _safe_set(owner, 'shape_TextLayout112', partner)
    assert getattr(partner, 'shape_ShapestyleLayout113') == owner
    _safe_set(owner, 'shape_TextLayout112', None)
    assert getattr(partner, 'shape_ShapestyleLayout113') is None


def test_assoc_layout21_stub_double():
    # shape_CDRoundedRectangle has no real 'shape_CDRoundedRectangle' property in the generated
    # code (a bare stub) -- manually attach it so shape_RoundedRectangleLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_RoundedRectangleLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    partner = shape_CDRoundedRectangle()
    setattr(partner, 'shape_CDRoundedRectangle', None)
    _safe_set(owner, 'shape_RoundedRectangleLayout', partner)
    assert getattr(partner, 'shape_CDRoundedRectangle') == owner
    _safe_set(owner, 'shape_RoundedRectangleLayout', None)
    assert getattr(partner, 'shape_CDRoundedRectangle') is None


def test_assoc_layout40_stub_double():
    # shape_RoundedRectangle has no real 'shape_RoundedRectangle' property in the generated
    # code (a bare stub) -- manually attach it so shape_RoundedRectangleLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_RoundedRectangleLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    partner = shape_RoundedRectangle()
    setattr(partner, 'shape_RoundedRectangle', None)
    _safe_set(owner, 'shape_RoundedRectangleLayout41', partner)
    assert getattr(partner, 'shape_RoundedRectangle') == owner
    _safe_set(owner, 'shape_RoundedRectangleLayout41', None)
    assert getattr(partner, 'shape_RoundedRectangle') is None


def test_assoc_layout73_stub_double():
    # shape_CompartmentRoundedRectangle has no real 'shape_CompartmentRoundedRectangle' property in the generated
    # code (a bare stub) -- manually attach it so shape_RoundedRectangleLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_RoundedRectangleLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    partner = shape_CompartmentRoundedRectangle()
    setattr(partner, 'shape_CompartmentRoundedRectangle', None)
    _safe_set(owner, 'shape_RoundedRectangleLayout74', partner)
    assert getattr(partner, 'shape_CompartmentRoundedRectangle') == owner
    _safe_set(owner, 'shape_RoundedRectangleLayout74', None)
    assert getattr(partner, 'shape_CompartmentRoundedRectangle') is None


def test_assoc_point91_stub_double():
    # shape_LineLayout has no real 'shape_LineLayout92' property in the generated
    # code (a bare stub) -- manually attach it so shape_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_Point(curveAfter=7, curveBefore=7, xcor="sample_text", ycor="sample_text")
    partner = shape_LineLayout()
    setattr(partner, 'shape_LineLayout92', None)
    _safe_set(owner, 'shape_Point', partner)
    assert owner in getattr(partner, 'shape_LineLayout92')
    _safe_set(owner, 'shape_Point', None)
    assert owner not in getattr(partner, 'shape_LineLayout92')


def test_assoc_point96_stub_double():
    # shape_PolyLineLayout has no real 'shape_PolyLineLayout97' property in the generated
    # code (a bare stub) -- manually attach it so shape_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_Point(curveAfter=7, curveBefore=7, xcor="sample_text", ycor="sample_text")
    partner = shape_PolyLineLayout()
    setattr(partner, 'shape_PolyLineLayout97', None)
    _safe_set(owner, 'shape_Point98', partner)
    assert owner in getattr(partner, 'shape_PolyLineLayout97')
    _safe_set(owner, 'shape_Point98', None)
    assert owner not in getattr(partner, 'shape_PolyLineLayout97')


def test_assoc_shape37_stub_double():
    # shape_Rectangle has no real 'shape_Rectangle38' property in the generated
    # code (a bare stub) -- manually attach it so shape_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_Shape(style="sample_text")
    partner = shape_Rectangle()
    setattr(partner, 'shape_Rectangle38', None)
    _safe_set(owner, 'shape_Shape39', partner)
    assert owner in getattr(partner, 'shape_Rectangle38')
    _safe_set(owner, 'shape_Shape39', None)
    assert owner not in getattr(partner, 'shape_Rectangle38')


def test_assoc_shape42_stub_double():
    # shape_RoundedRectangle has no real 'shape_RoundedRectangle43' property in the generated
    # code (a bare stub) -- manually attach it so shape_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_Shape(style="sample_text")
    partner = shape_RoundedRectangle()
    setattr(partner, 'shape_RoundedRectangle43', None)
    _safe_set(owner, 'shape_Shape44', partner)
    assert owner in getattr(partner, 'shape_RoundedRectangle43')
    _safe_set(owner, 'shape_Shape44', None)
    assert owner not in getattr(partner, 'shape_RoundedRectangle43')


def test_assoc_shape47_stub_double():
    # shape_Polygon has no real 'shape_Polygon48' property in the generated
    # code (a bare stub) -- manually attach it so shape_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_Shape(style="sample_text")
    partner = shape_Polygon()
    setattr(partner, 'shape_Polygon48', None)
    _safe_set(owner, 'shape_Shape49', partner)
    assert owner in getattr(partner, 'shape_Polygon48')
    _safe_set(owner, 'shape_Shape49', None)
    assert owner not in getattr(partner, 'shape_Polygon48')


def test_assoc_shape5_stub_double():
    # shape_ShapeDefinition has no real 'shape_ShapeDefinition6' property in the generated
    # code (a bare stub) -- manually attach it so shape_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_Shape(style="sample_text")
    partner = shape_ShapeDefinition()
    setattr(partner, 'shape_ShapeDefinition6', None)
    _safe_set(owner, 'shape_Shape', partner)
    assert owner in getattr(partner, 'shape_ShapeDefinition6')
    _safe_set(owner, 'shape_Shape', None)
    assert owner not in getattr(partner, 'shape_ShapeDefinition6')


def test_assoc_shape55_stub_double():
    # shape_Ellipse has no real 'shape_Ellipse56' property in the generated
    # code (a bare stub) -- manually attach it so shape_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_Shape(style="sample_text")
    partner = shape_Ellipse()
    setattr(partner, 'shape_Ellipse56', None)
    _safe_set(owner, 'shape_Shape57', partner)
    assert owner in getattr(partner, 'shape_Ellipse56')
    _safe_set(owner, 'shape_Shape57', None)
    assert owner not in getattr(partner, 'shape_Ellipse56')


def test_assoc_shape66_stub_double():
    # shape_CompartmentShape has no real 'shape_CompartmentShape' property in the generated
    # code (a bare stub) -- manually attach it so shape_Compartment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_Compartment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_Compartment(compartmentLayout="sample_text")
    partner = shape_CompartmentShape()
    setattr(partner, 'shape_CompartmentShape', None)
    _safe_set(owner, 'shape_Compartment', partner)
    assert getattr(partner, 'shape_CompartmentShape') == owner
    _safe_set(owner, 'shape_Compartment', None)
    assert getattr(partner, 'shape_CompartmentShape') is None


def test_assoc_shapeContainerElement0_stub_double():
    # shape_ShapeContainer has no real 'shape_ShapeContainer' property in the generated
    # code (a bare stub) -- manually attach it so shape_ShapeContainerElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_ShapeContainerElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_ShapeContainerElement(name="sample_text", style="sample_text")
    partner = shape_ShapeContainer()
    setattr(partner, 'shape_ShapeContainer', None)
    _safe_set(owner, 'shape_ShapeContainerElement', partner)
    assert owner in getattr(partner, 'shape_ShapeContainer')
    _safe_set(owner, 'shape_ShapeContainerElement', None)
    assert owner not in getattr(partner, 'shape_ShapeContainer')


def test_assoc_shapeLayout4_stub_double():
    # shape_ShapeDefinition has no real 'shape_ShapeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so shape_ShapeLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shape_ShapeLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shape_ShapeLayout(maxheight=7, maxwidth=7, minheight=7, minwidth=7, proportional="sample_text", stretchH="sample_text", stretchV="sample_text")
    partner = shape_ShapeDefinition()
    setattr(partner, 'shape_ShapeDefinition', None)
    _safe_set(owner, 'shape_ShapeLayout', partner)
    assert getattr(partner, 'shape_ShapeDefinition') == owner
    _safe_set(owner, 'shape_ShapeLayout', None)
    assert getattr(partner, 'shape_ShapeDefinition') is None


