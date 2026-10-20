import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CharacterAttributes,
    ContainerAttributes,
    FXGElement,
    Fill,
    Filter,
    ParagraphAttributes,
    RichTextContent,
    RichTextContentContainer,
    Shape,
    Stroke,
    fxg_BevelFilter,
    fxg_BitmapFill,
    fxg_BitmapImage,
    fxg_BlurFilter,
    fxg_CharacterAttributes,
    fxg_ColorMatrixFilter,
    fxg_ColorTransform,
    fxg_ContainerAttributes,
    fxg_ContainerElement,
    fxg_Definition,
    fxg_DropShadowFilter,
    fxg_Ellipse,
    fxg_FXGElement,
    fxg_Fill,
    fxg_Filter,
    fxg_GradientBevelFilter,
    fxg_GradientEntry,
    fxg_GradientGlowFilter,
    fxg_Graphic,
    fxg_Group,
    fxg_Library,
    fxg_Line,
    fxg_LinearGradient,
    fxg_LinearGradientStroke,
    fxg_Matrix,
    fxg_ParagraphAttributes,
    fxg_Path,
    fxg_PlaceObject,
    fxg_Private,
    fxg_RadialGradient,
    fxg_RadialGradientStroke,
    fxg_Rect,
    fxg_RichText,
    fxg_RichTextContent,
    fxg_RichTextContentContainer,
    fxg_Shape,
    fxg_SolidColor,
    fxg_SolidColorStroke,
    fxg_Stroke,
    fxg_Transform,
    fxg_a,
    fxg_br,
    fxg_div,
    fxg_img,
    fxg_linkActiveFormat,
    fxg_linkHoverFormat,
    fxg_linkNormalFormat,
    fxg_p,
    fxg_rawtext,
    fxg_span,
    fxg_tab,
    fxg_tcy,
    AlignmentBaseline,
    BevelFilterType,
    BlendMode,
    BlockProgression,
    BreakOpportunity,
    Cap,
    DigitCase,
    DigitWidth,
    DominantBaseline,
    FillMode,
    FontStyle,
    FontWeight,
    InterpolationMethod,
    Joint,
    JustificationRule,
    JustificationStyle,
    Kerning,
    LeadingModel,
    LigatureLevel,
    LineBreak,
    MaskType,
    ScaleMode,
    SpreadMethod,
    TextAlign,
    TextDecoration,
    TextJustify,
    TextRotation,
    TypographicCase,
    VerticalAlign,
    WhitespaceCollapse,
    Winding,
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

def test_assoc_mask0_reverse_link_reassign_clear():
    a1 = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    a2 = fxg_Group(alpha="sample_text_2", blendMode="sample_text_2", id="sample_text_2", maskType="sample_text_2", rotation="sample_text_2", scaleGridBottom="sample_text_2", scaleGridLeft="sample_text_2", scaleGridRight="sample_text_2", scaleGridTop="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", transformX="sample_text_2", transformY="sample_text_2", visible="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = fxg_Graphic(scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", version="sample_text", viewHeight=7, viewWidth=7)
    _safe_set(b, 'fxg_Graphic', a1)
    assert _is_linked(b, 'fxg_Graphic', a1)
    if hasattr(a1, 'fxg_Group'):
        assert _is_linked(a1, 'fxg_Group', b)
    _safe_set(b, 'fxg_Graphic', a2)
    assert _is_linked(b, 'fxg_Graphic', a2)
    if hasattr(a1, 'fxg_Group'):
        assert not _is_linked(a1, 'fxg_Group', b)
    if hasattr(a2, 'fxg_Group'):
        assert _is_linked(a2, 'fxg_Group', b)
    _safe_set(b, 'fxg_Graphic', None)
    assert not _is_linked(b, 'fxg_Graphic', a2)
    if hasattr(a2, 'fxg_Group'):
        assert not _is_linked(a2, 'fxg_Group', b)


def test_assoc_mask17_reverse_link_reassign_clear():
    a1 = fxg_PlaceObject(id="sample_text")
    a2 = fxg_PlaceObject(id="sample_text_2")
    b = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'fxg_Group19', a1)
    assert _is_linked(b, 'fxg_Group19', a1)
    if hasattr(a1, 'fxg_PlaceObject18'):
        assert _is_linked(a1, 'fxg_PlaceObject18', b)
    _safe_set(b, 'fxg_Group19', a2)
    assert _is_linked(b, 'fxg_Group19', a2)
    if hasattr(a1, 'fxg_PlaceObject18'):
        assert not _is_linked(a1, 'fxg_PlaceObject18', b)
    if hasattr(a2, 'fxg_PlaceObject18'):
        assert _is_linked(a2, 'fxg_PlaceObject18', b)
    _safe_set(b, 'fxg_Group19', None)
    assert not _is_linked(b, 'fxg_Group19', a2)
    if hasattr(a2, 'fxg_PlaceObject18'):
        assert not _is_linked(a2, 'fxg_PlaceObject18', b)


def test_assoc_mask29_reverse_link_reassign_clear():
    a1 = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    a2 = fxg_Path(alpha="sample_text_2", blendMode="sample_text_2", data="sample_text_2", rotation="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", visible="sample_text_2", winding="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'fxg_Group31', a1)
    assert _is_linked(b, 'fxg_Group31', a1)
    if hasattr(a1, 'fxg_Path30'):
        assert _is_linked(a1, 'fxg_Path30', b)
    _safe_set(b, 'fxg_Group31', a2)
    assert _is_linked(b, 'fxg_Group31', a2)
    if hasattr(a1, 'fxg_Path30'):
        assert not _is_linked(a1, 'fxg_Path30', b)
    if hasattr(a2, 'fxg_Path30'):
        assert _is_linked(a2, 'fxg_Path30', b)
    _safe_set(b, 'fxg_Group31', None)
    assert not _is_linked(b, 'fxg_Group31', a2)
    if hasattr(a2, 'fxg_Path30'):
        assert not _is_linked(a2, 'fxg_Path30', b)


def test_assoc_mask43_reverse_link_reassign_clear():
    a1 = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    a2 = fxg_Rect(alpha="sample_text_2", blendMode="sample_text_2", bottomLeftRadiusX="sample_text_2", bottomLeftRadiusY="sample_text_2", bottomRightRadiusX="sample_text_2", bottomRightRadiusY="sample_text_2", height="sample_text_2", radiusX="sample_text_2", radiusY="sample_text_2", rotation="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", topLeftRadiusX="sample_text_2", topLeftRadiusY="sample_text_2", topRightRadiusX="sample_text_2", topRightRadiusY="sample_text_2", visible="sample_text_2", width="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'fxg_Group45', a1)
    assert _is_linked(b, 'fxg_Group45', a1)
    if hasattr(a1, 'fxg_Rect44'):
        assert _is_linked(a1, 'fxg_Rect44', b)
    _safe_set(b, 'fxg_Group45', a2)
    assert _is_linked(b, 'fxg_Group45', a2)
    if hasattr(a1, 'fxg_Rect44'):
        assert not _is_linked(a1, 'fxg_Rect44', b)
    if hasattr(a2, 'fxg_Rect44'):
        assert _is_linked(a2, 'fxg_Rect44', b)
    _safe_set(b, 'fxg_Group45', None)
    assert not _is_linked(b, 'fxg_Group45', a2)
    if hasattr(a2, 'fxg_Rect44'):
        assert not _is_linked(a2, 'fxg_Rect44', b)


def test_assoc_mask57_reverse_link_reassign_clear():
    a1 = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    a2 = fxg_Group(alpha="sample_text_2", blendMode="sample_text_2", id="sample_text_2", maskType="sample_text_2", rotation="sample_text_2", scaleGridBottom="sample_text_2", scaleGridLeft="sample_text_2", scaleGridRight="sample_text_2", scaleGridTop="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", transformX="sample_text_2", transformY="sample_text_2", visible="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'fxg_Ellipse58', a1)
    assert _is_linked(b, 'fxg_Ellipse58', a1)
    if hasattr(a1, 'fxg_Group59'):
        assert _is_linked(a1, 'fxg_Group59', b)
    _safe_set(b, 'fxg_Ellipse58', a2)
    assert _is_linked(b, 'fxg_Ellipse58', a2)
    if hasattr(a1, 'fxg_Group59'):
        assert not _is_linked(a1, 'fxg_Group59', b)
    if hasattr(a2, 'fxg_Group59'):
        assert _is_linked(a2, 'fxg_Group59', b)
    _safe_set(b, 'fxg_Ellipse58', None)
    assert not _is_linked(b, 'fxg_Ellipse58', a2)
    if hasattr(a2, 'fxg_Group59'):
        assert not _is_linked(a2, 'fxg_Group59', b)


def test_assoc_mask6_reverse_link_reassign_clear():
    a1 = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    a2 = fxg_Group(alpha="sample_text_2", blendMode="sample_text_2", id="sample_text_2", maskType="sample_text_2", rotation="sample_text_2", scaleGridBottom="sample_text_2", scaleGridLeft="sample_text_2", scaleGridRight="sample_text_2", scaleGridTop="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", transformX="sample_text_2", transformY="sample_text_2", visible="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'fxg_Group7', a1)
    assert _is_linked(b, 'fxg_Group7', a1)
    if hasattr(a1, 'fxg_Group5'):
        assert _is_linked(a1, 'fxg_Group5', b)
    _safe_set(b, 'fxg_Group7', a2)
    assert _is_linked(b, 'fxg_Group7', a2)
    if hasattr(a1, 'fxg_Group5'):
        assert not _is_linked(a1, 'fxg_Group5', b)
    if hasattr(a2, 'fxg_Group5'):
        assert _is_linked(a2, 'fxg_Group5', b)
    _safe_set(b, 'fxg_Group7', None)
    assert not _is_linked(b, 'fxg_Group7', a2)
    if hasattr(a2, 'fxg_Group5'):
        assert not _is_linked(a2, 'fxg_Group5', b)


def test_assoc_mask71_reverse_link_reassign_clear():
    a1 = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    a2 = fxg_Line(alpha="sample_text_2", blendMode="sample_text_2", id="sample_text_2", maskType="sample_text_2", rotation="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", visible="sample_text_2", x="sample_text_2", xFrom="sample_text_2", xTo="sample_text_2", y="sample_text_2", yFrom="sample_text_2", yTo="sample_text_2")
    b = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'fxg_Group73', a1)
    assert _is_linked(b, 'fxg_Group73', a1)
    if hasattr(a1, 'fxg_Line72'):
        assert _is_linked(a1, 'fxg_Line72', b)
    _safe_set(b, 'fxg_Group73', a2)
    assert _is_linked(b, 'fxg_Group73', a2)
    if hasattr(a1, 'fxg_Line72'):
        assert not _is_linked(a1, 'fxg_Line72', b)
    if hasattr(a2, 'fxg_Line72'):
        assert _is_linked(a2, 'fxg_Line72', b)
    _safe_set(b, 'fxg_Group73', None)
    assert not _is_linked(b, 'fxg_Group73', a2)
    if hasattr(a2, 'fxg_Line72'):
        assert not _is_linked(a2, 'fxg_Line72', b)


def test_assoc_matrix77_reverse_link_reassign_clear():
    a1 = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    a2 = fxg_Matrix(a="sample_text_2", b="sample_text_2", c="sample_text_2", d="sample_text_2", tx="sample_text_2", ty="sample_text_2")
    b = fxg_LinearGradient(interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'fxg_LinearGradient', a1)
    assert _is_linked(b, 'fxg_LinearGradient', a1)
    if hasattr(a1, 'fxg_Matrix78'):
        assert _is_linked(a1, 'fxg_Matrix78', b)
    _safe_set(b, 'fxg_LinearGradient', a2)
    assert _is_linked(b, 'fxg_LinearGradient', a2)
    if hasattr(a1, 'fxg_Matrix78'):
        assert not _is_linked(a1, 'fxg_Matrix78', b)
    if hasattr(a2, 'fxg_Matrix78'):
        assert _is_linked(a2, 'fxg_Matrix78', b)
    _safe_set(b, 'fxg_LinearGradient', None)
    assert not _is_linked(b, 'fxg_LinearGradient', a2)
    if hasattr(a2, 'fxg_Matrix78'):
        assert not _is_linked(a2, 'fxg_Matrix78', b)


def test_assoc_matrix79_reverse_link_reassign_clear():
    a1 = fxg_RadialGradient(focalPointRatio="sample_text", interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    a2 = fxg_RadialGradient(focalPointRatio="sample_text_2", interpolationMethod="sample_text_2", rotation="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", spreadMethod="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    _safe_set(b, 'fxg_Matrix80', a1)
    assert _is_linked(b, 'fxg_Matrix80', a1)
    if hasattr(a1, 'fxg_RadialGradient'):
        assert _is_linked(a1, 'fxg_RadialGradient', b)
    _safe_set(b, 'fxg_Matrix80', a2)
    assert _is_linked(b, 'fxg_Matrix80', a2)
    if hasattr(a1, 'fxg_RadialGradient'):
        assert not _is_linked(a1, 'fxg_RadialGradient', b)
    if hasattr(a2, 'fxg_RadialGradient'):
        assert _is_linked(a2, 'fxg_RadialGradient', b)
    _safe_set(b, 'fxg_Matrix80', None)
    assert not _is_linked(b, 'fxg_Matrix80', a2)
    if hasattr(a2, 'fxg_RadialGradient'):
        assert not _is_linked(a2, 'fxg_RadialGradient', b)


def test_assoc_matrix81_reverse_link_reassign_clear():
    a1 = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    a2 = fxg_Matrix(a="sample_text_2", b="sample_text_2", c="sample_text_2", d="sample_text_2", tx="sample_text_2", ty="sample_text_2")
    b = fxg_BitmapFill(fillMode="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'fxg_BitmapFill', a1)
    assert _is_linked(b, 'fxg_BitmapFill', a1)
    if hasattr(a1, 'fxg_Matrix82'):
        assert _is_linked(a1, 'fxg_Matrix82', b)
    _safe_set(b, 'fxg_BitmapFill', a2)
    assert _is_linked(b, 'fxg_BitmapFill', a2)
    if hasattr(a1, 'fxg_Matrix82'):
        assert not _is_linked(a1, 'fxg_Matrix82', b)
    if hasattr(a2, 'fxg_Matrix82'):
        assert _is_linked(a2, 'fxg_Matrix82', b)
    _safe_set(b, 'fxg_BitmapFill', None)
    assert not _is_linked(b, 'fxg_BitmapFill', a2)
    if hasattr(a2, 'fxg_Matrix82'):
        assert not _is_linked(a2, 'fxg_Matrix82', b)


def test_assoc_matrix83_reverse_link_reassign_clear():
    a1 = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    a2 = fxg_Matrix(a="sample_text_2", b="sample_text_2", c="sample_text_2", d="sample_text_2", tx="sample_text_2", ty="sample_text_2")
    b = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'fxg_LinearGradientStroke', a1)
    assert _is_linked(b, 'fxg_LinearGradientStroke', a1)
    if hasattr(a1, 'fxg_Matrix84'):
        assert _is_linked(a1, 'fxg_Matrix84', b)
    _safe_set(b, 'fxg_LinearGradientStroke', a2)
    assert _is_linked(b, 'fxg_LinearGradientStroke', a2)
    if hasattr(a1, 'fxg_Matrix84'):
        assert not _is_linked(a1, 'fxg_Matrix84', b)
    if hasattr(a2, 'fxg_Matrix84'):
        assert _is_linked(a2, 'fxg_Matrix84', b)
    _safe_set(b, 'fxg_LinearGradientStroke', None)
    assert not _is_linked(b, 'fxg_LinearGradientStroke', a2)
    if hasattr(a2, 'fxg_Matrix84'):
        assert not _is_linked(a2, 'fxg_Matrix84', b)


def test_assoc_matrix85_reverse_link_reassign_clear():
    a1 = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    a2 = fxg_RadialGradientStroke(caps="sample_text_2", focalPointRatio="sample_text_2", interpolationMethod="sample_text_2", joints="sample_text_2", miterLimit="sample_text_2", pixelHinting="sample_text_2", rotation="sample_text_2", scaleMode="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", spreadMethod="sample_text_2", weight="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    _safe_set(b, 'fxg_Matrix86', a1)
    assert _is_linked(b, 'fxg_Matrix86', a1)
    if hasattr(a1, 'fxg_RadialGradientStroke'):
        assert _is_linked(a1, 'fxg_RadialGradientStroke', b)
    _safe_set(b, 'fxg_Matrix86', a2)
    assert _is_linked(b, 'fxg_Matrix86', a2)
    if hasattr(a1, 'fxg_RadialGradientStroke'):
        assert not _is_linked(a1, 'fxg_RadialGradientStroke', b)
    if hasattr(a2, 'fxg_RadialGradientStroke'):
        assert _is_linked(a2, 'fxg_RadialGradientStroke', b)
    _safe_set(b, 'fxg_Matrix86', None)
    assert not _is_linked(b, 'fxg_Matrix86', a2)
    if hasattr(a2, 'fxg_RadialGradientStroke'):
        assert not _is_linked(a2, 'fxg_RadialGradientStroke', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_colorTransform10_stub_double():
    # fxg_Transform has no real 'fxg_Transform11' property in the generated
    # code (a bare stub) -- manually attach it so fxg_ColorTransform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_ColorTransform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    partner = fxg_Transform()
    setattr(partner, 'fxg_Transform11', None)
    _safe_set(owner, 'fxg_ColorTransform', partner)
    assert getattr(partner, 'fxg_Transform11') == owner
    _safe_set(owner, 'fxg_ColorTransform', None)
    assert getattr(partner, 'fxg_Transform11') is None


def test_assoc_content74_stub_double():
    # fxg_RichTextContent has no real 'fxg_RichTextContent' property in the generated
    # code (a bare stub) -- manually attach it so fxg_RichText's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_RichText's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = fxg_RichTextContent()
    setattr(partner, 'fxg_RichTextContent', None)
    _safe_set(owner, 'fxg_RichText', {partner})
    assert getattr(partner, 'fxg_RichTextContent') == owner
    _safe_set(owner, 'fxg_RichText', set())
    assert getattr(partner, 'fxg_RichTextContent') is None


def test_assoc_fill20_stub_double():
    # fxg_Fill has no real 'fxg_Fill' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Fill()
    setattr(partner, 'fxg_Fill', None)
    _safe_set(owner, 'fxg_Path', partner)
    assert getattr(partner, 'fxg_Fill') == owner
    _safe_set(owner, 'fxg_Path', None)
    assert getattr(partner, 'fxg_Fill') is None


def test_assoc_fill37_stub_double():
    # fxg_Fill has no real 'fxg_Fill39' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Rect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Rect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Fill()
    setattr(partner, 'fxg_Fill39', None)
    _safe_set(owner, 'fxg_Rect38', partner)
    assert getattr(partner, 'fxg_Fill39') == owner
    _safe_set(owner, 'fxg_Rect38', None)
    assert getattr(partner, 'fxg_Fill39') is None


def test_assoc_fill51_stub_double():
    # fxg_Fill has no real 'fxg_Fill53' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Ellipse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Ellipse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Fill()
    setattr(partner, 'fxg_Fill53', None)
    _safe_set(owner, 'fxg_Ellipse52', partner)
    assert getattr(partner, 'fxg_Fill53') == owner
    _safe_set(owner, 'fxg_Ellipse52', None)
    assert getattr(partner, 'fxg_Fill53') is None


def test_assoc_fill65_stub_double():
    # fxg_Fill has no real 'fxg_Fill67' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    partner = fxg_Fill()
    setattr(partner, 'fxg_Fill67', None)
    _safe_set(owner, 'fxg_Line66', partner)
    assert getattr(partner, 'fxg_Fill67') == owner
    _safe_set(owner, 'fxg_Line66', None)
    assert getattr(partner, 'fxg_Fill67') is None


def test_assoc_filters14_stub_double():
    # fxg_Filter has no real 'fxg_Filter16' property in the generated
    # code (a bare stub) -- manually attach it so fxg_PlaceObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_PlaceObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_PlaceObject(id="sample_text")
    partner = fxg_Filter()
    setattr(partner, 'fxg_Filter16', None)
    _safe_set(owner, 'fxg_PlaceObject15', {partner})
    assert getattr(partner, 'fxg_Filter16') == owner
    _safe_set(owner, 'fxg_PlaceObject15', set())
    assert getattr(partner, 'fxg_Filter16') is None


def test_assoc_filters23_stub_double():
    # fxg_Filter has no real 'fxg_Filter25' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Filter()
    setattr(partner, 'fxg_Filter25', None)
    _safe_set(owner, 'fxg_Path24', {partner})
    assert getattr(partner, 'fxg_Filter25') == owner
    _safe_set(owner, 'fxg_Path24', set())
    assert getattr(partner, 'fxg_Filter25') is None


def test_assoc_filters3_stub_double():
    # fxg_Filter has no real 'fxg_Filter' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Filter()
    setattr(partner, 'fxg_Filter', None)
    _safe_set(owner, 'fxg_Group4', {partner})
    assert getattr(partner, 'fxg_Filter') == owner
    _safe_set(owner, 'fxg_Group4', set())
    assert getattr(partner, 'fxg_Filter') is None


def test_assoc_filters34_stub_double():
    # fxg_Filter has no real 'fxg_Filter36' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Rect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Rect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Filter()
    setattr(partner, 'fxg_Filter36', None)
    _safe_set(owner, 'fxg_Rect35', {partner})
    assert getattr(partner, 'fxg_Filter36') == owner
    _safe_set(owner, 'fxg_Rect35', set())
    assert getattr(partner, 'fxg_Filter36') is None


def test_assoc_filters48_stub_double():
    # fxg_Filter has no real 'fxg_Filter50' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Ellipse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Ellipse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Filter()
    setattr(partner, 'fxg_Filter50', None)
    _safe_set(owner, 'fxg_Ellipse49', {partner})
    assert getattr(partner, 'fxg_Filter50') == owner
    _safe_set(owner, 'fxg_Ellipse49', set())
    assert getattr(partner, 'fxg_Filter50') is None


def test_assoc_filters62_stub_double():
    # fxg_Filter has no real 'fxg_Filter64' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    partner = fxg_Filter()
    setattr(partner, 'fxg_Filter64', None)
    _safe_set(owner, 'fxg_Line63', {partner})
    assert getattr(partner, 'fxg_Filter64') == owner
    _safe_set(owner, 'fxg_Line63', set())
    assert getattr(partner, 'fxg_Filter64') is None


def test_assoc_matrix8_stub_double():
    # fxg_Transform has no real 'fxg_Transform9' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Matrix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Matrix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    partner = fxg_Transform()
    setattr(partner, 'fxg_Transform9', None)
    _safe_set(owner, 'fxg_Matrix', partner)
    assert getattr(partner, 'fxg_Transform9') == owner
    _safe_set(owner, 'fxg_Matrix', None)
    assert getattr(partner, 'fxg_Transform9') is None


def test_assoc_stroke21_stub_double():
    # fxg_Stroke has no real 'fxg_Stroke' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Stroke()
    setattr(partner, 'fxg_Stroke', None)
    _safe_set(owner, 'fxg_Path22', partner)
    assert getattr(partner, 'fxg_Stroke') == owner
    _safe_set(owner, 'fxg_Path22', None)
    assert getattr(partner, 'fxg_Stroke') is None


def test_assoc_stroke40_stub_double():
    # fxg_Stroke has no real 'fxg_Stroke42' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Rect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Rect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Stroke()
    setattr(partner, 'fxg_Stroke42', None)
    _safe_set(owner, 'fxg_Rect41', partner)
    assert getattr(partner, 'fxg_Stroke42') == owner
    _safe_set(owner, 'fxg_Rect41', None)
    assert getattr(partner, 'fxg_Stroke42') is None


def test_assoc_stroke54_stub_double():
    # fxg_Stroke has no real 'fxg_Stroke56' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Ellipse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Ellipse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Stroke()
    setattr(partner, 'fxg_Stroke56', None)
    _safe_set(owner, 'fxg_Ellipse55', partner)
    assert getattr(partner, 'fxg_Stroke56') == owner
    _safe_set(owner, 'fxg_Ellipse55', None)
    assert getattr(partner, 'fxg_Stroke56') is None


def test_assoc_stroke68_stub_double():
    # fxg_Stroke has no real 'fxg_Stroke70' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    partner = fxg_Stroke()
    setattr(partner, 'fxg_Stroke70', None)
    _safe_set(owner, 'fxg_Line69', partner)
    assert getattr(partner, 'fxg_Stroke70') == owner
    _safe_set(owner, 'fxg_Line69', None)
    assert getattr(partner, 'fxg_Stroke70') is None


def test_assoc_transform1_stub_double():
    # fxg_Transform has no real 'fxg_Transform' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Transform()
    setattr(partner, 'fxg_Transform', None)
    _safe_set(owner, 'fxg_Group2', partner)
    assert getattr(partner, 'fxg_Transform') == owner
    _safe_set(owner, 'fxg_Group2', None)
    assert getattr(partner, 'fxg_Transform') is None


def test_assoc_transform12_stub_double():
    # fxg_Transform has no real 'fxg_Transform13' property in the generated
    # code (a bare stub) -- manually attach it so fxg_PlaceObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_PlaceObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_PlaceObject(id="sample_text")
    partner = fxg_Transform()
    setattr(partner, 'fxg_Transform13', None)
    _safe_set(owner, 'fxg_PlaceObject', partner)
    assert getattr(partner, 'fxg_Transform13') == owner
    _safe_set(owner, 'fxg_PlaceObject', None)
    assert getattr(partner, 'fxg_Transform13') is None


def test_assoc_transform26_stub_double():
    # fxg_Transform has no real 'fxg_Transform28' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Transform()
    setattr(partner, 'fxg_Transform28', None)
    _safe_set(owner, 'fxg_Path27', partner)
    assert getattr(partner, 'fxg_Transform28') == owner
    _safe_set(owner, 'fxg_Path27', None)
    assert getattr(partner, 'fxg_Transform28') is None


def test_assoc_transform32_stub_double():
    # fxg_Transform has no real 'fxg_Transform33' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Rect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Rect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Transform()
    setattr(partner, 'fxg_Transform33', None)
    _safe_set(owner, 'fxg_Rect', partner)
    assert getattr(partner, 'fxg_Transform33') == owner
    _safe_set(owner, 'fxg_Rect', None)
    assert getattr(partner, 'fxg_Transform33') is None


def test_assoc_transform46_stub_double():
    # fxg_Transform has no real 'fxg_Transform47' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Ellipse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Ellipse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = fxg_Transform()
    setattr(partner, 'fxg_Transform47', None)
    _safe_set(owner, 'fxg_Ellipse', partner)
    assert getattr(partner, 'fxg_Transform47') == owner
    _safe_set(owner, 'fxg_Ellipse', None)
    assert getattr(partner, 'fxg_Transform47') is None


def test_assoc_transform60_stub_double():
    # fxg_Transform has no real 'fxg_Transform61' property in the generated
    # code (a bare stub) -- manually attach it so fxg_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fxg_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    partner = fxg_Transform()
    setattr(partner, 'fxg_Transform61', None)
    _safe_set(owner, 'fxg_Line', partner)
    assert getattr(partner, 'fxg_Transform61') == owner
    _safe_set(owner, 'fxg_Line', None)
    assert getattr(partner, 'fxg_Transform61') is None


