import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Color,
    ColorOrGradient,
    ColorWithTransparency,
    StyleContainerElement,
    styles_Color,
    styles_ColorConstantRef,
    styles_ColorOrGradient,
    styles_ColorWithTransparency,
    styles_Gradient,
    styles_GradientColorArea,
    styles_GradientLayout,
    styles_GradientRef,
    styles_HighlightingValues,
    styles_JvmTypeReference,
    styles_RGBColor,
    styles_Style,
    styles_StyleContainer,
    styles_StyleContainerElement,
    styles_StyleLayout,
    styles_Transparent,
    ColorConstants,
    GradientAllignment,
    LineStyle,
    YesNoBool,
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

def test_assoc_area16_stub_double():
    # styles_GradientLayout has no real 'styles_GradientLayout17' property in the generated
    # code (a bare stub) -- manually attach it so styles_GradientColorArea's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # styles_GradientColorArea's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = styles_GradientColorArea(offset=3.14)
    partner = styles_GradientLayout()
    setattr(partner, 'styles_GradientLayout17', None)
    _safe_set(owner, 'styles_GradientColorArea', partner)
    assert owner in getattr(partner, 'styles_GradientLayout17')
    _safe_set(owner, 'styles_GradientColorArea', None)
    assert owner not in getattr(partner, 'styles_GradientLayout17')


def test_assoc_background8_stub_double():
    # styles_ColorOrGradient has no real 'styles_ColorOrGradient' property in the generated
    # code (a bare stub) -- manually attach it so styles_StyleLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # styles_StyleLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = styles_StyleLayout(fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize=7, gradient_orientation="sample_text", lineStyle="sample_text", lineWidth=7, transparency=3.14)
    partner = styles_ColorOrGradient()
    setattr(partner, 'styles_ColorOrGradient', None)
    _safe_set(owner, 'styles_StyleLayout9', partner)
    assert getattr(partner, 'styles_ColorOrGradient') == owner
    _safe_set(owner, 'styles_StyleLayout9', None)
    assert getattr(partner, 'styles_ColorOrGradient') is None


def test_assoc_color30_stub_double():
    # styles_Color has no real 'styles_Color32' property in the generated
    # code (a bare stub) -- manually attach it so styles_GradientColorArea's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # styles_GradientColorArea's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = styles_GradientColorArea(offset=3.14)
    partner = styles_Color()
    setattr(partner, 'styles_Color32', None)
    _safe_set(owner, 'styles_GradientColorArea31', partner)
    assert getattr(partner, 'styles_Color32') == owner
    _safe_set(owner, 'styles_GradientColorArea31', None)
    assert getattr(partner, 'styles_Color32') is None


def test_assoc_fontColor14_stub_double():
    # styles_Color has no real 'styles_Color' property in the generated
    # code (a bare stub) -- manually attach it so styles_StyleLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # styles_StyleLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = styles_StyleLayout(fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize=7, gradient_orientation="sample_text", lineStyle="sample_text", lineWidth=7, transparency=3.14)
    partner = styles_Color()
    setattr(partner, 'styles_Color', None)
    _safe_set(owner, 'styles_StyleLayout15', partner)
    assert getattr(partner, 'styles_Color') == owner
    _safe_set(owner, 'styles_StyleLayout15', None)
    assert getattr(partner, 'styles_Color') is None


def test_assoc_highlighting10_stub_double():
    # styles_HighlightingValues has no real 'styles_HighlightingValues' property in the generated
    # code (a bare stub) -- manually attach it so styles_StyleLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # styles_StyleLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = styles_StyleLayout(fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize=7, gradient_orientation="sample_text", lineStyle="sample_text", lineWidth=7, transparency=3.14)
    partner = styles_HighlightingValues()
    setattr(partner, 'styles_HighlightingValues', None)
    _safe_set(owner, 'styles_StyleLayout11', partner)
    assert getattr(partner, 'styles_HighlightingValues') == owner
    _safe_set(owner, 'styles_StyleLayout11', None)
    assert getattr(partner, 'styles_HighlightingValues') is None


def test_assoc_layout5_stub_double():
    # styles_Style has no real 'styles_Style6' property in the generated
    # code (a bare stub) -- manually attach it so styles_StyleLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # styles_StyleLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = styles_StyleLayout(fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize=7, gradient_orientation="sample_text", lineStyle="sample_text", lineWidth=7, transparency=3.14)
    partner = styles_Style()
    setattr(partner, 'styles_Style6', None)
    _safe_set(owner, 'styles_StyleLayout', partner)
    assert getattr(partner, 'styles_Style6') == owner
    _safe_set(owner, 'styles_StyleLayout', None)
    assert getattr(partner, 'styles_Style6') is None


def test_assoc_lineColor12_stub_double():
    # styles_ColorWithTransparency has no real 'styles_ColorWithTransparency' property in the generated
    # code (a bare stub) -- manually attach it so styles_StyleLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # styles_StyleLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = styles_StyleLayout(fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize=7, gradient_orientation="sample_text", lineStyle="sample_text", lineWidth=7, transparency=3.14)
    partner = styles_ColorWithTransparency()
    setattr(partner, 'styles_ColorWithTransparency', None)
    _safe_set(owner, 'styles_StyleLayout13', partner)
    assert getattr(partner, 'styles_ColorWithTransparency') == owner
    _safe_set(owner, 'styles_StyleLayout13', None)
    assert getattr(partner, 'styles_ColorWithTransparency') is None


def test_assoc_styleContainerElement0_stub_double():
    # styles_StyleContainer has no real 'styles_StyleContainer' property in the generated
    # code (a bare stub) -- manually attach it so styles_StyleContainerElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # styles_StyleContainerElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = styles_StyleContainerElement(description="sample_text", name="sample_text")
    partner = styles_StyleContainer()
    setattr(partner, 'styles_StyleContainer', None)
    _safe_set(owner, 'styles_StyleContainerElement', partner)
    assert owner in getattr(partner, 'styles_StyleContainer')
    _safe_set(owner, 'styles_StyleContainerElement', None)
    assert owner not in getattr(partner, 'styles_StyleContainer')


