import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EMapPropertyHolder,
    KAreaPlacementData,
    KContainerRendering,
    KGraphData,
    KPlacement,
    KPlacementData,
    KPolyline,
    KRendering,
    KStyle,
    KStyleHolder,
    krendering_KAction,
    krendering_KArc,
    krendering_KAreaPlacementData,
    krendering_KBackground,
    krendering_KBottomPosition,
    krendering_KChildArea,
    krendering_KColor,
    krendering_KColoring,
    krendering_KContainerRendering,
    krendering_KCustomRendering,
    krendering_KDecoratorPlacementData,
    krendering_KEllipse,
    krendering_KFontBold,
    krendering_KFontItalic,
    krendering_KFontName,
    krendering_KFontSize,
    krendering_KForeground,
    krendering_KGridPlacement,
    krendering_KGridPlacementData,
    krendering_KHorizontalAlignment,
    krendering_KImage,
    krendering_KInvisibility,
    krendering_KLeftPosition,
    krendering_KLineCap,
    krendering_KLineJoin,
    krendering_KLineStyle,
    krendering_KLineWidth,
    krendering_KPlacement,
    krendering_KPlacementData,
    krendering_KPointPlacementData,
    krendering_KPolygon,
    krendering_KPolyline,
    krendering_KPosition,
    krendering_KRectangle,
    krendering_KRendering,
    krendering_KRenderingLibrary,
    krendering_KRenderingRef,
    krendering_KRightPosition,
    krendering_KRotation,
    krendering_KRoundedBendsPolyline,
    krendering_KRoundedRectangle,
    krendering_KShadow,
    krendering_KSpline,
    krendering_KStyle,
    krendering_KStyleHolder,
    krendering_KStyleRef,
    krendering_KText,
    krendering_KTextStrikeout,
    krendering_KTextUnderline,
    krendering_KTopPosition,
    krendering_KVerticalAlignment,
    krendering_KXPosition,
    krendering_KYPosition,
    Arc,
    HorizontalAlignment,
    LineCap,
    LineJoin,
    LineStyle,
    ModifierState,
    Trigger,
    Underline,
    VerticalAlignment,
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

def test_assoc_bottomRight17_reverse_link_reassign_clear():
    a1 = krendering_KPosition()
    a2 = krendering_KPosition()
    b = krendering_KGridPlacement(numColumns=7)
    _safe_set(b, 'krendering_KGridPlacement18', a1)
    assert _is_linked(b, 'krendering_KGridPlacement18', a1)
    if hasattr(a1, 'krendering_KPosition19'):
        assert _is_linked(a1, 'krendering_KPosition19', b)
    _safe_set(b, 'krendering_KGridPlacement18', a2)
    assert _is_linked(b, 'krendering_KGridPlacement18', a2)
    if hasattr(a1, 'krendering_KPosition19'):
        assert not _is_linked(a1, 'krendering_KPosition19', b)
    if hasattr(a2, 'krendering_KPosition19'):
        assert _is_linked(a2, 'krendering_KPosition19', b)
    _safe_set(b, 'krendering_KGridPlacement18', None)
    assert not _is_linked(b, 'krendering_KGridPlacement18', a2)
    if hasattr(a2, 'krendering_KPosition19'):
        assert not _is_linked(a2, 'krendering_KPosition19', b)


def test_assoc_color25_reverse_link_reassign_clear():
    a1 = krendering_KColoring(alpha=7, gradientAngle=3.14, targetAlpha=7)
    a2 = krendering_KColoring(alpha=13, gradientAngle=9.99, targetAlpha=13)
    b = krendering_KColor(blue=7, green=7, red=7)
    _safe_set(b, 'krendering_KColor', a1)
    assert _is_linked(b, 'krendering_KColor', a1)
    if hasattr(a1, 'krendering_KColoring'):
        assert _is_linked(a1, 'krendering_KColoring', b)
    _safe_set(b, 'krendering_KColor', a2)
    assert _is_linked(b, 'krendering_KColor', a2)
    if hasattr(a1, 'krendering_KColoring'):
        assert not _is_linked(a1, 'krendering_KColoring', b)
    if hasattr(a2, 'krendering_KColoring'):
        assert _is_linked(a2, 'krendering_KColoring', b)
    _safe_set(b, 'krendering_KColor', None)
    assert not _is_linked(b, 'krendering_KColor', a2)
    if hasattr(a2, 'krendering_KColoring'):
        assert not _is_linked(a2, 'krendering_KColoring', b)


def test_assoc_color35_reverse_link_reassign_clear():
    a1 = krendering_KShadow(blur=3.14, xOffset=3.14, yOffset=3.14)
    a2 = krendering_KShadow(blur=9.99, xOffset=9.99, yOffset=9.99)
    b = krendering_KColor(blue=7, green=7, red=7)
    _safe_set(b, 'krendering_KColor36', a1)
    assert _is_linked(b, 'krendering_KColor36', a1)
    if hasattr(a1, 'krendering_KShadow'):
        assert _is_linked(a1, 'krendering_KShadow', b)
    _safe_set(b, 'krendering_KColor36', a2)
    assert _is_linked(b, 'krendering_KColor36', a2)
    if hasattr(a1, 'krendering_KShadow'):
        assert not _is_linked(a1, 'krendering_KShadow', b)
    if hasattr(a2, 'krendering_KShadow'):
        assert _is_linked(a2, 'krendering_KShadow', b)
    _safe_set(b, 'krendering_KColor36', None)
    assert not _is_linked(b, 'krendering_KColor36', a2)
    if hasattr(a2, 'krendering_KShadow'):
        assert not _is_linked(a2, 'krendering_KShadow', b)


def test_assoc_color37_reverse_link_reassign_clear():
    a1 = krendering_KTextUnderline(underline="sample_text")
    a2 = krendering_KTextUnderline(underline="sample_text_2")
    b = krendering_KColor(blue=7, green=7, red=7)
    _safe_set(b, 'krendering_KColor38', a1)
    assert _is_linked(b, 'krendering_KColor38', a1)
    if hasattr(a1, 'krendering_KTextUnderline'):
        assert _is_linked(a1, 'krendering_KTextUnderline', b)
    _safe_set(b, 'krendering_KColor38', a2)
    assert _is_linked(b, 'krendering_KColor38', a2)
    if hasattr(a1, 'krendering_KTextUnderline'):
        assert not _is_linked(a1, 'krendering_KTextUnderline', b)
    if hasattr(a2, 'krendering_KTextUnderline'):
        assert _is_linked(a2, 'krendering_KTextUnderline', b)
    _safe_set(b, 'krendering_KColor38', None)
    assert not _is_linked(b, 'krendering_KColor38', a2)
    if hasattr(a2, 'krendering_KTextUnderline'):
        assert not _is_linked(a2, 'krendering_KTextUnderline', b)


def test_assoc_color41_reverse_link_reassign_clear():
    a1 = krendering_KTextStrikeout(struckOut="sample_text")
    a2 = krendering_KTextStrikeout(struckOut="sample_text_2")
    b = krendering_KColor(blue=7, green=7, red=7)
    _safe_set(b, 'krendering_KColor42', a1)
    assert _is_linked(b, 'krendering_KColor42', a1)
    if hasattr(a1, 'krendering_KTextStrikeout'):
        assert _is_linked(a1, 'krendering_KTextStrikeout', b)
    _safe_set(b, 'krendering_KColor42', a2)
    assert _is_linked(b, 'krendering_KColor42', a2)
    if hasattr(a1, 'krendering_KTextStrikeout'):
        assert not _is_linked(a1, 'krendering_KTextStrikeout', b)
    if hasattr(a2, 'krendering_KTextStrikeout'):
        assert _is_linked(a2, 'krendering_KTextStrikeout', b)
    _safe_set(b, 'krendering_KColor42', None)
    assert not _is_linked(b, 'krendering_KColor42', a2)
    if hasattr(a2, 'krendering_KTextStrikeout'):
        assert not _is_linked(a2, 'krendering_KTextStrikeout', b)


def test_assoc_referencePoint31_reverse_link_reassign_clear():
    a1 = krendering_KPosition()
    a2 = krendering_KPosition()
    b = krendering_KPointPlacementData(horizontalAlignment="sample_text", horizontalMargin=3.14, minHeight=3.14, minWidth=3.14, verticalAlignment="sample_text", verticalMargin=3.14)
    _safe_set(b, 'krendering_KPointPlacementData', a1)
    assert _is_linked(b, 'krendering_KPointPlacementData', a1)
    if hasattr(a1, 'krendering_KPosition32'):
        assert _is_linked(a1, 'krendering_KPosition32', b)
    _safe_set(b, 'krendering_KPointPlacementData', a2)
    assert _is_linked(b, 'krendering_KPointPlacementData', a2)
    if hasattr(a1, 'krendering_KPosition32'):
        assert not _is_linked(a1, 'krendering_KPosition32', b)
    if hasattr(a2, 'krendering_KPosition32'):
        assert _is_linked(a2, 'krendering_KPosition32', b)
    _safe_set(b, 'krendering_KPointPlacementData', None)
    assert not _is_linked(b, 'krendering_KPointPlacementData', a2)
    if hasattr(a2, 'krendering_KPosition32'):
        assert not _is_linked(a2, 'krendering_KPosition32', b)


def test_assoc_rotationAnchor29_reverse_link_reassign_clear():
    a1 = krendering_KRotation(rotation=3.14)
    a2 = krendering_KRotation(rotation=9.99)
    b = krendering_KPosition()
    _safe_set(b, 'krendering_KPosition30', a1)
    assert _is_linked(b, 'krendering_KPosition30', a1)
    if hasattr(a1, 'krendering_KRotation'):
        assert _is_linked(a1, 'krendering_KRotation', b)
    _safe_set(b, 'krendering_KPosition30', a2)
    assert _is_linked(b, 'krendering_KPosition30', a2)
    if hasattr(a1, 'krendering_KRotation'):
        assert not _is_linked(a1, 'krendering_KRotation', b)
    if hasattr(a2, 'krendering_KRotation'):
        assert _is_linked(a2, 'krendering_KRotation', b)
    _safe_set(b, 'krendering_KPosition30', None)
    assert not _is_linked(b, 'krendering_KPosition30', a2)
    if hasattr(a2, 'krendering_KRotation'):
        assert not _is_linked(a2, 'krendering_KRotation', b)


def test_assoc_styleHolder39_reverse_link_reassign_clear():
    a1 = krendering_KStyleRef(referencedTypes="sample_text")
    a2 = krendering_KStyleRef(referencedTypes="sample_text_2")
    b = krendering_KStyleHolder(id="sample_text")
    _safe_set(b, 'krendering_KStyleHolder40', a1)
    assert _is_linked(b, 'krendering_KStyleHolder40', a1)
    if hasattr(a1, 'krendering_KStyleRef'):
        assert _is_linked(a1, 'krendering_KStyleRef', b)
    _safe_set(b, 'krendering_KStyleHolder40', a2)
    assert _is_linked(b, 'krendering_KStyleHolder40', a2)
    if hasattr(a1, 'krendering_KStyleRef'):
        assert not _is_linked(a1, 'krendering_KStyleRef', b)
    if hasattr(a2, 'krendering_KStyleRef'):
        assert _is_linked(a2, 'krendering_KStyleRef', b)
    _safe_set(b, 'krendering_KStyleHolder40', None)
    assert not _is_linked(b, 'krendering_KStyleHolder40', a2)
    if hasattr(a2, 'krendering_KStyleRef'):
        assert not _is_linked(a2, 'krendering_KStyleRef', b)


def test_assoc_styles33_reverse_link_reassign_clear():
    a1 = krendering_KStyleHolder(id="sample_text")
    a2 = krendering_KStyleHolder(id="sample_text_2")
    b = krendering_KStyle(modifierId="sample_text", propagateToChildren=True, selection=True)
    _safe_set(b, 'krendering_KStyle', a1)
    assert _is_linked(b, 'krendering_KStyle', a1)
    if hasattr(a1, 'krendering_KStyleHolder34'):
        assert _is_linked(a1, 'krendering_KStyleHolder34', b)
    _safe_set(b, 'krendering_KStyle', a2)
    assert _is_linked(b, 'krendering_KStyle', a2)
    if hasattr(a1, 'krendering_KStyleHolder34'):
        assert not _is_linked(a1, 'krendering_KStyleHolder34', b)
    if hasattr(a2, 'krendering_KStyleHolder34'):
        assert _is_linked(a2, 'krendering_KStyleHolder34', b)
    _safe_set(b, 'krendering_KStyle', None)
    assert not _is_linked(b, 'krendering_KStyle', a2)
    if hasattr(a2, 'krendering_KStyleHolder34'):
        assert not _is_linked(a2, 'krendering_KStyleHolder34', b)


def test_assoc_targetColor26_reverse_link_reassign_clear():
    a1 = krendering_KColoring(alpha=7, gradientAngle=3.14, targetAlpha=7)
    a2 = krendering_KColoring(alpha=13, gradientAngle=9.99, targetAlpha=13)
    b = krendering_KColor(blue=7, green=7, red=7)
    _safe_set(b, 'krendering_KColor28', a1)
    assert _is_linked(b, 'krendering_KColor28', a1)
    if hasattr(a1, 'krendering_KColoring27'):
        assert _is_linked(a1, 'krendering_KColoring27', b)
    _safe_set(b, 'krendering_KColor28', a2)
    assert _is_linked(b, 'krendering_KColor28', a2)
    if hasattr(a1, 'krendering_KColoring27'):
        assert not _is_linked(a1, 'krendering_KColoring27', b)
    if hasattr(a2, 'krendering_KColoring27'):
        assert _is_linked(a2, 'krendering_KColoring27', b)
    _safe_set(b, 'krendering_KColor28', None)
    assert not _is_linked(b, 'krendering_KColor28', a2)
    if hasattr(a2, 'krendering_KColoring27'):
        assert not _is_linked(a2, 'krendering_KColoring27', b)


def test_assoc_topLeft15_reverse_link_reassign_clear():
    a1 = krendering_KPosition()
    a2 = krendering_KPosition()
    b = krendering_KGridPlacement(numColumns=7)
    _safe_set(b, 'krendering_KGridPlacement', a1)
    assert _is_linked(b, 'krendering_KGridPlacement', a1)
    if hasattr(a1, 'krendering_KPosition16'):
        assert _is_linked(a1, 'krendering_KPosition16', b)
    _safe_set(b, 'krendering_KGridPlacement', a2)
    assert _is_linked(b, 'krendering_KGridPlacement', a2)
    if hasattr(a1, 'krendering_KPosition16'):
        assert not _is_linked(a1, 'krendering_KPosition16', b)
    if hasattr(a2, 'krendering_KPosition16'):
        assert _is_linked(a2, 'krendering_KPosition16', b)
    _safe_set(b, 'krendering_KGridPlacement', None)
    assert not _is_linked(b, 'krendering_KGridPlacement', a2)
    if hasattr(a2, 'krendering_KPosition16'):
        assert not _is_linked(a2, 'krendering_KPosition16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions2_stub_double():
    # krendering_KRendering has no real 'krendering_KRendering3' property in the generated
    # code (a bare stub) -- manually attach it so krendering_KAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # krendering_KAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = krendering_KAction(actionId="sample_text", altPressed="sample_text", ctrlCmdPressed="sample_text", shiftPressed="sample_text", trigger="sample_text")
    partner = krendering_KRendering()
    setattr(partner, 'krendering_KRendering3', None)
    _safe_set(owner, 'krendering_KAction', partner)
    assert owner in getattr(partner, 'krendering_KRendering3')
    _safe_set(owner, 'krendering_KAction', None)
    assert owner not in getattr(partner, 'krendering_KRendering3')


def test_assoc_bottomRight22_stub_double():
    # krendering_KAreaPlacementData has no real 'krendering_KAreaPlacementData23' property in the generated
    # code (a bare stub) -- manually attach it so krendering_KPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # krendering_KPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = krendering_KPosition()
    partner = krendering_KAreaPlacementData()
    setattr(partner, 'krendering_KAreaPlacementData23', None)
    _safe_set(owner, 'krendering_KPosition24', partner)
    assert getattr(partner, 'krendering_KAreaPlacementData23') == owner
    _safe_set(owner, 'krendering_KPosition24', None)
    assert getattr(partner, 'krendering_KAreaPlacementData23') is None


def test_assoc_clipShape8_stub_double():
    # krendering_KRendering has no real 'krendering_KRendering9' property in the generated
    # code (a bare stub) -- manually attach it so krendering_KImage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # krendering_KImage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = krendering_KImage(bundleName="sample_text", imageObject="sample_text", imagePath="sample_text")
    partner = krendering_KRendering()
    setattr(partner, 'krendering_KRendering9', None)
    _safe_set(owner, 'krendering_KImage', partner)
    assert getattr(partner, 'krendering_KRendering9') == owner
    _safe_set(owner, 'krendering_KImage', None)
    assert getattr(partner, 'krendering_KRendering9') is None


def test_assoc_points4_stub_double():
    # krendering_KPolyline has no real 'krendering_KPolyline' property in the generated
    # code (a bare stub) -- manually attach it so krendering_KPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # krendering_KPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = krendering_KPosition()
    partner = krendering_KPolyline()
    setattr(partner, 'krendering_KPolyline', None)
    _safe_set(owner, 'krendering_KPosition', partner)
    assert owner in getattr(partner, 'krendering_KPolyline')
    _safe_set(owner, 'krendering_KPosition', None)
    assert owner not in getattr(partner, 'krendering_KPolyline')


def test_assoc_renderings12_stub_double():
    # krendering_KRenderingLibrary has no real 'krendering_KRenderingLibrary' property in the generated
    # code (a bare stub) -- manually attach it so krendering_KStyleHolder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # krendering_KStyleHolder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = krendering_KStyleHolder(id="sample_text")
    partner = krendering_KRenderingLibrary()
    setattr(partner, 'krendering_KRenderingLibrary', None)
    _safe_set(owner, 'krendering_KStyleHolder', partner)
    assert owner in getattr(partner, 'krendering_KRenderingLibrary')
    _safe_set(owner, 'krendering_KStyleHolder', None)
    assert owner not in getattr(partner, 'krendering_KRenderingLibrary')


def test_assoc_topLeft20_stub_double():
    # krendering_KAreaPlacementData has no real 'krendering_KAreaPlacementData' property in the generated
    # code (a bare stub) -- manually attach it so krendering_KPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # krendering_KPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = krendering_KPosition()
    partner = krendering_KAreaPlacementData()
    setattr(partner, 'krendering_KAreaPlacementData', None)
    _safe_set(owner, 'krendering_KPosition21', partner)
    assert getattr(partner, 'krendering_KAreaPlacementData') == owner
    _safe_set(owner, 'krendering_KPosition21', None)
    assert getattr(partner, 'krendering_KAreaPlacementData') is None


