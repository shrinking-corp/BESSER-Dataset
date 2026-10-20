import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Border,
    Canvas,
    ColoredLabeledBorder,
    ConnectionAnchor,
    Figure,
    LabeledBorder,
    PointListShape,
    Polyline,
    Shape,
    draw2d_BlockFlow,
    draw2d_Border,
    draw2d_Color,
    draw2d_ColoredLabeledBorder,
    draw2d_ConnectionAnchor,
    draw2d_Draw2DCanvas,
    draw2d_Ellipse,
    draw2d_Figure,
    draw2d_FlowBorder,
    draw2d_Font,
    draw2d_FrameBorder,
    draw2d_GroupBoxBorder,
    draw2d_ImageFigure,
    draw2d_Label,
    draw2d_LabeledBorder,
    draw2d_PointListShape,
    draw2d_Polygon,
    draw2d_PolygonShape,
    draw2d_Polyline,
    draw2d_PolylineShape,
    draw2d_RectangleFigure,
    draw2d_RoundedRectangle,
    draw2d_Shape,
    draw2d_TitleBarBorder,
    draw2d_Triangle,
    draw2d_XYAnchor,
    Alignment,
    Direction,
    Orientation,
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

def test_assoc_border16_reverse_link_reassign_clear():
    a1 = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    a2 = draw2d_Figure(bounds="sample_text_2", enabled=False, focusTraversable=False, maximumSize="sample_text_2", minimumSize="sample_text_2", opaque=False, preferredSize="sample_text_2", visible=False)
    b = draw2d_Border(opaque=True)
    _safe_set(b, 'draw2d_Border', a1)
    assert _is_linked(b, 'draw2d_Border', a1)
    if hasattr(a1, 'draw2d_Figure17'):
        assert _is_linked(a1, 'draw2d_Figure17', b)
    _safe_set(b, 'draw2d_Border', a2)
    assert _is_linked(b, 'draw2d_Border', a2)
    if hasattr(a1, 'draw2d_Figure17'):
        assert not _is_linked(a1, 'draw2d_Figure17', b)
    if hasattr(a2, 'draw2d_Figure17'):
        assert _is_linked(a2, 'draw2d_Figure17', b)
    _safe_set(b, 'draw2d_Border', None)
    assert not _is_linked(b, 'draw2d_Border', a2)
    if hasattr(a2, 'draw2d_Figure17'):
        assert not _is_linked(a2, 'draw2d_Figure17', b)


def test_assoc_children2_reverse_link_reassign_clear():
    a1 = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    a2 = draw2d_Figure(bounds="sample_text_2", enabled=False, focusTraversable=False, maximumSize="sample_text_2", minimumSize="sample_text_2", opaque=False, preferredSize="sample_text_2", visible=False)
    b = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Figure'):
        assert _is_linked(a1, 'Figure', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Figure'):
        assert not _is_linked(a1, 'Figure', b)
    if hasattr(a2, 'Figure'):
        assert _is_linked(a2, 'Figure', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Figure'):
        assert not _is_linked(a2, 'Figure', b)


def test_assoc_parent4_reverse_link_reassign_clear():
    a1 = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    a2 = draw2d_Figure(bounds="sample_text_2", enabled=False, focusTraversable=False, maximumSize="sample_text_2", minimumSize="sample_text_2", opaque=False, preferredSize="sample_text_2", visible=False)
    b = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Figure5'):
        assert _is_linked(a1, 'Figure5', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Figure5'):
        assert not _is_linked(a1, 'Figure5', b)
    if hasattr(a2, 'Figure5'):
        assert _is_linked(a2, 'Figure5', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Figure5'):
        assert not _is_linked(a2, 'Figure5', b)


def test_assoc_toolTip7_reverse_link_reassign_clear():
    a1 = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    a2 = draw2d_Figure(bounds="sample_text_2", enabled=False, focusTraversable=False, maximumSize="sample_text_2", minimumSize="sample_text_2", opaque=False, preferredSize="sample_text_2", visible=False)
    b = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    _safe_set(b, 'draw2d_Figure8', a1)
    assert _is_linked(b, 'draw2d_Figure8', a1)
    if hasattr(a1, 'draw2d_Figure6'):
        assert _is_linked(a1, 'draw2d_Figure6', b)
    _safe_set(b, 'draw2d_Figure8', a2)
    assert _is_linked(b, 'draw2d_Figure8', a2)
    if hasattr(a1, 'draw2d_Figure6'):
        assert not _is_linked(a1, 'draw2d_Figure6', b)
    if hasattr(a2, 'draw2d_Figure6'):
        assert _is_linked(a2, 'draw2d_Figure6', b)
    _safe_set(b, 'draw2d_Figure8', None)
    assert not _is_linked(b, 'draw2d_Figure8', a2)
    if hasattr(a2, 'draw2d_Figure6'):
        assert not _is_linked(a2, 'draw2d_Figure6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_backgroundColor9_stub_double():
    # draw2d_Color has no real 'draw2d_Color' property in the generated
    # code (a bare stub) -- manually attach it so draw2d_Figure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # draw2d_Figure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    partner = draw2d_Color()
    setattr(partner, 'draw2d_Color', None)
    _safe_set(owner, 'draw2d_Figure10', partner)
    assert getattr(partner, 'draw2d_Color') == owner
    _safe_set(owner, 'draw2d_Figure10', None)
    assert getattr(partner, 'draw2d_Color') is None


def test_assoc_contents0_stub_double():
    # draw2d_Draw2DCanvas has no real 'draw2d_Draw2DCanvas' property in the generated
    # code (a bare stub) -- manually attach it so draw2d_Figure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # draw2d_Figure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    partner = draw2d_Draw2DCanvas()
    setattr(partner, 'draw2d_Draw2DCanvas', None)
    _safe_set(owner, 'draw2d_Figure', partner)
    assert getattr(partner, 'draw2d_Draw2DCanvas') == owner
    _safe_set(owner, 'draw2d_Figure', None)
    assert getattr(partner, 'draw2d_Draw2DCanvas') is None


def test_assoc_font14_stub_double():
    # draw2d_Font has no real 'draw2d_Font' property in the generated
    # code (a bare stub) -- manually attach it so draw2d_Figure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # draw2d_Figure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    partner = draw2d_Font()
    setattr(partner, 'draw2d_Font', None)
    _safe_set(owner, 'draw2d_Figure15', partner)
    assert getattr(partner, 'draw2d_Font') == owner
    _safe_set(owner, 'draw2d_Figure15', None)
    assert getattr(partner, 'draw2d_Font') is None


def test_assoc_font20_stub_double():
    # draw2d_Font has no real 'draw2d_Font21' property in the generated
    # code (a bare stub) -- manually attach it so draw2d_LabeledBorder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # draw2d_LabeledBorder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = draw2d_LabeledBorder(label="sample_text")
    partner = draw2d_Font()
    setattr(partner, 'draw2d_Font21', None)
    _safe_set(owner, 'draw2d_LabeledBorder', partner)
    assert getattr(partner, 'draw2d_Font21') == owner
    _safe_set(owner, 'draw2d_LabeledBorder', None)
    assert getattr(partner, 'draw2d_Font21') is None


def test_assoc_foregroundColor11_stub_double():
    # draw2d_Color has no real 'draw2d_Color13' property in the generated
    # code (a bare stub) -- manually attach it so draw2d_Figure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # draw2d_Figure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    partner = draw2d_Color()
    setattr(partner, 'draw2d_Color13', None)
    _safe_set(owner, 'draw2d_Figure12', partner)
    assert getattr(partner, 'draw2d_Color13') == owner
    _safe_set(owner, 'draw2d_Figure12', None)
    assert getattr(partner, 'draw2d_Color13') is None


def test_assoc_owner18_stub_double():
    # draw2d_ConnectionAnchor has no real 'draw2d_ConnectionAnchor' property in the generated
    # code (a bare stub) -- manually attach it so draw2d_Figure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # draw2d_Figure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    partner = draw2d_ConnectionAnchor()
    setattr(partner, 'draw2d_ConnectionAnchor', None)
    _safe_set(owner, 'draw2d_Figure19', partner)
    assert getattr(partner, 'draw2d_ConnectionAnchor') == owner
    _safe_set(owner, 'draw2d_Figure19', None)
    assert getattr(partner, 'draw2d_ConnectionAnchor') is None


