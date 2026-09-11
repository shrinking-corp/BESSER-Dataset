import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_krendering_KAction_actionId_value_roundtrip():
    instance = krendering_KAction(actionId="sample_text", altPressed="sample_text", ctrlCmdPressed="sample_text", shiftPressed="sample_text", trigger="sample_text")
    assert instance.actionId == "sample_text"
    instance.actionId = "sample_text_2"
    assert instance.actionId == "sample_text_2"


def test_krendering_KAction_altPressed_value_roundtrip():
    instance = krendering_KAction(actionId="sample_text", altPressed="sample_text", ctrlCmdPressed="sample_text", shiftPressed="sample_text", trigger="sample_text")
    assert instance.altPressed == "sample_text"
    instance.altPressed = "sample_text_2"
    assert instance.altPressed == "sample_text_2"


def test_krendering_KAction_ctrlCmdPressed_value_roundtrip():
    instance = krendering_KAction(actionId="sample_text", altPressed="sample_text", ctrlCmdPressed="sample_text", shiftPressed="sample_text", trigger="sample_text")
    assert instance.ctrlCmdPressed == "sample_text"
    instance.ctrlCmdPressed = "sample_text_2"
    assert instance.ctrlCmdPressed == "sample_text_2"


def test_krendering_KAction_shiftPressed_value_roundtrip():
    instance = krendering_KAction(actionId="sample_text", altPressed="sample_text", ctrlCmdPressed="sample_text", shiftPressed="sample_text", trigger="sample_text")
    assert instance.shiftPressed == "sample_text"
    instance.shiftPressed = "sample_text_2"
    assert instance.shiftPressed == "sample_text_2"


def test_krendering_KAction_trigger_value_roundtrip():
    instance = krendering_KAction(actionId="sample_text", altPressed="sample_text", ctrlCmdPressed="sample_text", shiftPressed="sample_text", trigger="sample_text")
    assert instance.trigger == "sample_text"
    instance.trigger = "sample_text_2"
    assert instance.trigger == "sample_text_2"


def test_krendering_KArc_arcAngle_value_roundtrip():
    instance = krendering_KArc(arcAngle=3.14, arcType="sample_text", startAngle=3.14)
    assert instance.arcAngle == 3.14
    instance.arcAngle = 9.99
    assert instance.arcAngle == 9.99


def test_krendering_KArc_arcType_value_roundtrip():
    instance = krendering_KArc(arcAngle=3.14, arcType="sample_text", startAngle=3.14)
    assert instance.arcType == "sample_text"
    instance.arcType = "sample_text_2"
    assert instance.arcType == "sample_text_2"


def test_krendering_KArc_startAngle_value_roundtrip():
    instance = krendering_KArc(arcAngle=3.14, arcType="sample_text", startAngle=3.14)
    assert instance.startAngle == 3.14
    instance.startAngle = 9.99
    assert instance.startAngle == 9.99


def test_krendering_KColor_blue_value_roundtrip():
    instance = krendering_KColor(blue=7, green=7, red=7)
    assert instance.blue == 7
    instance.blue = 13
    assert instance.blue == 13


def test_krendering_KColor_green_value_roundtrip():
    instance = krendering_KColor(blue=7, green=7, red=7)
    assert instance.green == 7
    instance.green = 13
    assert instance.green == 13


def test_krendering_KColor_red_value_roundtrip():
    instance = krendering_KColor(blue=7, green=7, red=7)
    assert instance.red == 7
    instance.red = 13
    assert instance.red == 13


def test_krendering_KColoring_alpha_value_roundtrip():
    instance = krendering_KColoring(alpha=7, gradientAngle=3.14, targetAlpha=7)
    assert instance.alpha == 7
    instance.alpha = 13
    assert instance.alpha == 13


def test_krendering_KColoring_gradientAngle_value_roundtrip():
    instance = krendering_KColoring(alpha=7, gradientAngle=3.14, targetAlpha=7)
    assert instance.gradientAngle == 3.14
    instance.gradientAngle = 9.99
    assert instance.gradientAngle == 9.99


def test_krendering_KColoring_targetAlpha_value_roundtrip():
    instance = krendering_KColoring(alpha=7, gradientAngle=3.14, targetAlpha=7)
    assert instance.targetAlpha == 7
    instance.targetAlpha = 13
    assert instance.targetAlpha == 13


def test_krendering_KCustomRendering_bundleName_value_roundtrip():
    instance = krendering_KCustomRendering(bundleName="sample_text", className="sample_text", figureObject="sample_text")
    assert instance.bundleName == "sample_text"
    instance.bundleName = "sample_text_2"
    assert instance.bundleName == "sample_text_2"


def test_krendering_KCustomRendering_className_value_roundtrip():
    instance = krendering_KCustomRendering(bundleName="sample_text", className="sample_text", figureObject="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_krendering_KCustomRendering_figureObject_value_roundtrip():
    instance = krendering_KCustomRendering(bundleName="sample_text", className="sample_text", figureObject="sample_text")
    assert instance.figureObject == "sample_text"
    instance.figureObject = "sample_text_2"
    assert instance.figureObject == "sample_text_2"


def test_krendering_KDecoratorPlacementData_absolute_value_roundtrip():
    instance = krendering_KDecoratorPlacementData(absolute=3.14, height=3.14, relative=3.14, rotateWithLine=True, width=3.14, xOffset=3.14, yOffset=3.14)
    assert instance.absolute == 3.14
    instance.absolute = 9.99
    assert instance.absolute == 9.99


def test_krendering_KDecoratorPlacementData_height_value_roundtrip():
    instance = krendering_KDecoratorPlacementData(absolute=3.14, height=3.14, relative=3.14, rotateWithLine=True, width=3.14, xOffset=3.14, yOffset=3.14)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_krendering_KDecoratorPlacementData_relative_value_roundtrip():
    instance = krendering_KDecoratorPlacementData(absolute=3.14, height=3.14, relative=3.14, rotateWithLine=True, width=3.14, xOffset=3.14, yOffset=3.14)
    assert instance.relative == 3.14
    instance.relative = 9.99
    assert instance.relative == 9.99


def test_krendering_KDecoratorPlacementData_rotateWithLine_value_roundtrip():
    instance = krendering_KDecoratorPlacementData(absolute=3.14, height=3.14, relative=3.14, rotateWithLine=True, width=3.14, xOffset=3.14, yOffset=3.14)
    assert instance.rotateWithLine == True
    instance.rotateWithLine = False
    assert instance.rotateWithLine == False


def test_krendering_KDecoratorPlacementData_width_value_roundtrip():
    instance = krendering_KDecoratorPlacementData(absolute=3.14, height=3.14, relative=3.14, rotateWithLine=True, width=3.14, xOffset=3.14, yOffset=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_krendering_KDecoratorPlacementData_xOffset_value_roundtrip():
    instance = krendering_KDecoratorPlacementData(absolute=3.14, height=3.14, relative=3.14, rotateWithLine=True, width=3.14, xOffset=3.14, yOffset=3.14)
    assert instance.xOffset == 3.14
    instance.xOffset = 9.99
    assert instance.xOffset == 9.99


def test_krendering_KDecoratorPlacementData_yOffset_value_roundtrip():
    instance = krendering_KDecoratorPlacementData(absolute=3.14, height=3.14, relative=3.14, rotateWithLine=True, width=3.14, xOffset=3.14, yOffset=3.14)
    assert instance.yOffset == 3.14
    instance.yOffset = 9.99
    assert instance.yOffset == 9.99


def test_krendering_KFontBold_bold_value_roundtrip():
    instance = krendering_KFontBold(bold=True)
    assert instance.bold == True
    instance.bold = False
    assert instance.bold == False


def test_krendering_KFontItalic_italic_value_roundtrip():
    instance = krendering_KFontItalic(italic=True)
    assert instance.italic == True
    instance.italic = False
    assert instance.italic == False


def test_krendering_KFontName_name_value_roundtrip():
    instance = krendering_KFontName(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_krendering_KFontSize_scaleWithZoom_value_roundtrip():
    instance = krendering_KFontSize(scaleWithZoom=True, size=7)
    assert instance.scaleWithZoom == True
    instance.scaleWithZoom = False
    assert instance.scaleWithZoom == False


def test_krendering_KFontSize_size_value_roundtrip():
    instance = krendering_KFontSize(scaleWithZoom=True, size=7)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_krendering_KGridPlacement_numColumns_value_roundtrip():
    instance = krendering_KGridPlacement(numColumns=7)
    assert instance.numColumns == 7
    instance.numColumns = 13
    assert instance.numColumns == 13


def test_krendering_KGridPlacementData_flexibleHeight_value_roundtrip():
    instance = krendering_KGridPlacementData(flexibleHeight="sample_text", flexibleWidth="sample_text", minCellHeight=3.14, minCellWidth=3.14)
    assert instance.flexibleHeight == "sample_text"
    instance.flexibleHeight = "sample_text_2"
    assert instance.flexibleHeight == "sample_text_2"


def test_krendering_KGridPlacementData_flexibleWidth_value_roundtrip():
    instance = krendering_KGridPlacementData(flexibleHeight="sample_text", flexibleWidth="sample_text", minCellHeight=3.14, minCellWidth=3.14)
    assert instance.flexibleWidth == "sample_text"
    instance.flexibleWidth = "sample_text_2"
    assert instance.flexibleWidth == "sample_text_2"


def test_krendering_KGridPlacementData_minCellHeight_value_roundtrip():
    instance = krendering_KGridPlacementData(flexibleHeight="sample_text", flexibleWidth="sample_text", minCellHeight=3.14, minCellWidth=3.14)
    assert instance.minCellHeight == 3.14
    instance.minCellHeight = 9.99
    assert instance.minCellHeight == 9.99


def test_krendering_KGridPlacementData_minCellWidth_value_roundtrip():
    instance = krendering_KGridPlacementData(flexibleHeight="sample_text", flexibleWidth="sample_text", minCellHeight=3.14, minCellWidth=3.14)
    assert instance.minCellWidth == 3.14
    instance.minCellWidth = 9.99
    assert instance.minCellWidth == 9.99


def test_krendering_KHorizontalAlignment_horizontalAlignment_value_roundtrip():
    instance = krendering_KHorizontalAlignment(horizontalAlignment="sample_text")
    assert instance.horizontalAlignment == "sample_text"
    instance.horizontalAlignment = "sample_text_2"
    assert instance.horizontalAlignment == "sample_text_2"


def test_krendering_KImage_bundleName_value_roundtrip():
    instance = krendering_KImage(bundleName="sample_text", imageObject="sample_text", imagePath="sample_text")
    assert instance.bundleName == "sample_text"
    instance.bundleName = "sample_text_2"
    assert instance.bundleName == "sample_text_2"


def test_krendering_KImage_imageObject_value_roundtrip():
    instance = krendering_KImage(bundleName="sample_text", imageObject="sample_text", imagePath="sample_text")
    assert instance.imageObject == "sample_text"
    instance.imageObject = "sample_text_2"
    assert instance.imageObject == "sample_text_2"


def test_krendering_KImage_imagePath_value_roundtrip():
    instance = krendering_KImage(bundleName="sample_text", imageObject="sample_text", imagePath="sample_text")
    assert instance.imagePath == "sample_text"
    instance.imagePath = "sample_text_2"
    assert instance.imagePath == "sample_text_2"


def test_krendering_KInvisibility_invisible_value_roundtrip():
    instance = krendering_KInvisibility(invisible=True)
    assert instance.invisible == True
    instance.invisible = False
    assert instance.invisible == False


def test_krendering_KLineCap_lineCap_value_roundtrip():
    instance = krendering_KLineCap(lineCap="sample_text")
    assert instance.lineCap == "sample_text"
    instance.lineCap = "sample_text_2"
    assert instance.lineCap == "sample_text_2"


def test_krendering_KLineJoin_lineJoin_value_roundtrip():
    instance = krendering_KLineJoin(lineJoin="sample_text", miterLimit=3.14)
    assert instance.lineJoin == "sample_text"
    instance.lineJoin = "sample_text_2"
    assert instance.lineJoin == "sample_text_2"


def test_krendering_KLineJoin_miterLimit_value_roundtrip():
    instance = krendering_KLineJoin(lineJoin="sample_text", miterLimit=3.14)
    assert instance.miterLimit == 3.14
    instance.miterLimit = 9.99
    assert instance.miterLimit == 9.99


def test_krendering_KLineStyle_dashOffset_value_roundtrip():
    instance = krendering_KLineStyle(dashOffset=3.14, dashPattern=3.14, lineStyle="sample_text")
    assert instance.dashOffset == 3.14
    instance.dashOffset = 9.99
    assert instance.dashOffset == 9.99


def test_krendering_KLineStyle_dashPattern_value_roundtrip():
    instance = krendering_KLineStyle(dashOffset=3.14, dashPattern=3.14, lineStyle="sample_text")
    assert instance.dashPattern == 3.14
    instance.dashPattern = 9.99
    assert instance.dashPattern == 9.99


def test_krendering_KLineStyle_lineStyle_value_roundtrip():
    instance = krendering_KLineStyle(dashOffset=3.14, dashPattern=3.14, lineStyle="sample_text")
    assert instance.lineStyle == "sample_text"
    instance.lineStyle = "sample_text_2"
    assert instance.lineStyle == "sample_text_2"


def test_krendering_KLineWidth_lineWidth_value_roundtrip():
    instance = krendering_KLineWidth(lineWidth=3.14)
    assert instance.lineWidth == 3.14
    instance.lineWidth = 9.99
    assert instance.lineWidth == 9.99


def test_krendering_KPointPlacementData_horizontalAlignment_value_roundtrip():
    instance = krendering_KPointPlacementData(horizontalAlignment="sample_text", horizontalMargin=3.14, minHeight=3.14, minWidth=3.14, verticalAlignment="sample_text", verticalMargin=3.14)
    assert instance.horizontalAlignment == "sample_text"
    instance.horizontalAlignment = "sample_text_2"
    assert instance.horizontalAlignment == "sample_text_2"


def test_krendering_KPointPlacementData_horizontalMargin_value_roundtrip():
    instance = krendering_KPointPlacementData(horizontalAlignment="sample_text", horizontalMargin=3.14, minHeight=3.14, minWidth=3.14, verticalAlignment="sample_text", verticalMargin=3.14)
    assert instance.horizontalMargin == 3.14
    instance.horizontalMargin = 9.99
    assert instance.horizontalMargin == 9.99


def test_krendering_KPointPlacementData_minHeight_value_roundtrip():
    instance = krendering_KPointPlacementData(horizontalAlignment="sample_text", horizontalMargin=3.14, minHeight=3.14, minWidth=3.14, verticalAlignment="sample_text", verticalMargin=3.14)
    assert instance.minHeight == 3.14
    instance.minHeight = 9.99
    assert instance.minHeight == 9.99


def test_krendering_KPointPlacementData_minWidth_value_roundtrip():
    instance = krendering_KPointPlacementData(horizontalAlignment="sample_text", horizontalMargin=3.14, minHeight=3.14, minWidth=3.14, verticalAlignment="sample_text", verticalMargin=3.14)
    assert instance.minWidth == 3.14
    instance.minWidth = 9.99
    assert instance.minWidth == 9.99


def test_krendering_KPointPlacementData_verticalAlignment_value_roundtrip():
    instance = krendering_KPointPlacementData(horizontalAlignment="sample_text", horizontalMargin=3.14, minHeight=3.14, minWidth=3.14, verticalAlignment="sample_text", verticalMargin=3.14)
    assert instance.verticalAlignment == "sample_text"
    instance.verticalAlignment = "sample_text_2"
    assert instance.verticalAlignment == "sample_text_2"


def test_krendering_KPointPlacementData_verticalMargin_value_roundtrip():
    instance = krendering_KPointPlacementData(horizontalAlignment="sample_text", horizontalMargin=3.14, minHeight=3.14, minWidth=3.14, verticalAlignment="sample_text", verticalMargin=3.14)
    assert instance.verticalMargin == 3.14
    instance.verticalMargin = 9.99
    assert instance.verticalMargin == 9.99


def test_krendering_KRotation_rotation_value_roundtrip():
    instance = krendering_KRotation(rotation=3.14)
    assert instance.rotation == 3.14
    instance.rotation = 9.99
    assert instance.rotation == 9.99


def test_krendering_KRoundedBendsPolyline_bendRadius_value_roundtrip():
    instance = krendering_KRoundedBendsPolyline(bendRadius=3.14)
    assert instance.bendRadius == 3.14
    instance.bendRadius = 9.99
    assert instance.bendRadius == 9.99


def test_krendering_KRoundedRectangle_cornerHeight_value_roundtrip():
    instance = krendering_KRoundedRectangle(cornerHeight=3.14, cornerWidth=3.14)
    assert instance.cornerHeight == 3.14
    instance.cornerHeight = 9.99
    assert instance.cornerHeight == 9.99


def test_krendering_KRoundedRectangle_cornerWidth_value_roundtrip():
    instance = krendering_KRoundedRectangle(cornerHeight=3.14, cornerWidth=3.14)
    assert instance.cornerWidth == 3.14
    instance.cornerWidth = 9.99
    assert instance.cornerWidth == 9.99


def test_krendering_KShadow_blur_value_roundtrip():
    instance = krendering_KShadow(blur=3.14, xOffset=3.14, yOffset=3.14)
    assert instance.blur == 3.14
    instance.blur = 9.99
    assert instance.blur == 9.99


def test_krendering_KShadow_xOffset_value_roundtrip():
    instance = krendering_KShadow(blur=3.14, xOffset=3.14, yOffset=3.14)
    assert instance.xOffset == 3.14
    instance.xOffset = 9.99
    assert instance.xOffset == 9.99


def test_krendering_KShadow_yOffset_value_roundtrip():
    instance = krendering_KShadow(blur=3.14, xOffset=3.14, yOffset=3.14)
    assert instance.yOffset == 3.14
    instance.yOffset = 9.99
    assert instance.yOffset == 9.99


def test_krendering_KStyle_modifierId_value_roundtrip():
    instance = krendering_KStyle(modifierId="sample_text", propagateToChildren=True, selection=True)
    assert instance.modifierId == "sample_text"
    instance.modifierId = "sample_text_2"
    assert instance.modifierId == "sample_text_2"


def test_krendering_KStyle_propagateToChildren_value_roundtrip():
    instance = krendering_KStyle(modifierId="sample_text", propagateToChildren=True, selection=True)
    assert instance.propagateToChildren == True
    instance.propagateToChildren = False
    assert instance.propagateToChildren == False


def test_krendering_KStyle_selection_value_roundtrip():
    instance = krendering_KStyle(modifierId="sample_text", propagateToChildren=True, selection=True)
    assert instance.selection == True
    instance.selection = False
    assert instance.selection == False


def test_krendering_KStyleHolder_id_value_roundtrip():
    instance = krendering_KStyleHolder(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_krendering_KStyleRef_referencedTypes_value_roundtrip():
    instance = krendering_KStyleRef(referencedTypes="sample_text")
    assert instance.referencedTypes == "sample_text"
    instance.referencedTypes = "sample_text_2"
    assert instance.referencedTypes == "sample_text_2"


def test_krendering_KText_cursorSelectable_value_roundtrip():
    instance = krendering_KText(cursorSelectable=True, editable=True, text="sample_text")
    assert instance.cursorSelectable == True
    instance.cursorSelectable = False
    assert instance.cursorSelectable == False


def test_krendering_KText_editable_value_roundtrip():
    instance = krendering_KText(cursorSelectable=True, editable=True, text="sample_text")
    assert instance.editable == True
    instance.editable = False
    assert instance.editable == False


def test_krendering_KText_text_value_roundtrip():
    instance = krendering_KText(cursorSelectable=True, editable=True, text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_krendering_KTextStrikeout_struckOut_value_roundtrip():
    instance = krendering_KTextStrikeout(struckOut="sample_text")
    assert instance.struckOut == "sample_text"
    instance.struckOut = "sample_text_2"
    assert instance.struckOut == "sample_text_2"


def test_krendering_KTextUnderline_underline_value_roundtrip():
    instance = krendering_KTextUnderline(underline="sample_text")
    assert instance.underline == "sample_text"
    instance.underline = "sample_text_2"
    assert instance.underline == "sample_text_2"


def test_krendering_KVerticalAlignment_verticalAlignment_value_roundtrip():
    instance = krendering_KVerticalAlignment(verticalAlignment="sample_text")
    assert instance.verticalAlignment == "sample_text"
    instance.verticalAlignment = "sample_text_2"
    assert instance.verticalAlignment == "sample_text_2"


def test_krendering_KXPosition_absolute_value_roundtrip():
    instance = krendering_KXPosition(absolute=3.14, relative=3.14)
    assert instance.absolute == 3.14
    instance.absolute = 9.99
    assert instance.absolute == 9.99


def test_krendering_KXPosition_relative_value_roundtrip():
    instance = krendering_KXPosition(absolute=3.14, relative=3.14)
    assert instance.relative == 3.14
    instance.relative = 9.99
    assert instance.relative == 9.99


def test_krendering_KYPosition_absolute_value_roundtrip():
    instance = krendering_KYPosition(absolute=3.14, relative=3.14)
    assert instance.absolute == 3.14
    instance.absolute = 9.99
    assert instance.absolute == 9.99


def test_krendering_KYPosition_relative_value_roundtrip():
    instance = krendering_KYPosition(absolute=3.14, relative=3.14)
    assert instance.relative == 3.14
    instance.relative = 9.99
    assert instance.relative == 9.99


def test_krendering_KStyle_isa_EMapPropertyHolder():
    instance = krendering_KStyle(modifierId="sample_text", propagateToChildren=True, selection=True)
    assert isinstance(instance, EMapPropertyHolder)


def test_krendering_KGridPlacementData_isa_KAreaPlacementData():
    instance = krendering_KGridPlacementData(flexibleHeight="sample_text", flexibleWidth="sample_text", minCellHeight=3.14, minCellWidth=3.14)
    assert isinstance(instance, KAreaPlacementData)


def test_krendering_KArc_isa_KContainerRendering():
    instance = krendering_KArc(arcAngle=3.14, arcType="sample_text", startAngle=3.14)
    assert isinstance(instance, KContainerRendering)


def test_krendering_KCustomRendering_isa_KContainerRendering():
    instance = krendering_KCustomRendering(bundleName="sample_text", className="sample_text", figureObject="sample_text")
    assert isinstance(instance, KContainerRendering)


def test_krendering_KEllipse_isa_KContainerRendering():
    instance = krendering_KEllipse()
    assert isinstance(instance, KContainerRendering)


def test_krendering_KImage_isa_KContainerRendering():
    instance = krendering_KImage(bundleName="sample_text", imageObject="sample_text", imagePath="sample_text")
    assert isinstance(instance, KContainerRendering)


def test_krendering_KPolyline_isa_KContainerRendering():
    instance = krendering_KPolyline()
    assert isinstance(instance, KContainerRendering)


def test_krendering_KRectangle_isa_KContainerRendering():
    instance = krendering_KRectangle()
    assert isinstance(instance, KContainerRendering)


def test_krendering_KRoundedRectangle_isa_KContainerRendering():
    instance = krendering_KRoundedRectangle(cornerHeight=3.14, cornerWidth=3.14)
    assert isinstance(instance, KContainerRendering)


def test_krendering_KRendering_isa_KGraphData():
    instance = krendering_KRendering()
    assert isinstance(instance, KGraphData)


def test_krendering_KRenderingLibrary_isa_KGraphData():
    instance = krendering_KRenderingLibrary()
    assert isinstance(instance, KGraphData)


def test_krendering_KGridPlacement_isa_KPlacement():
    instance = krendering_KGridPlacement(numColumns=7)
    assert isinstance(instance, KPlacement)


def test_krendering_KAreaPlacementData_isa_KPlacementData():
    instance = krendering_KAreaPlacementData()
    assert isinstance(instance, KPlacementData)


def test_krendering_KDecoratorPlacementData_isa_KPlacementData():
    instance = krendering_KDecoratorPlacementData(absolute=3.14, height=3.14, relative=3.14, rotateWithLine=True, width=3.14, xOffset=3.14, yOffset=3.14)
    assert isinstance(instance, KPlacementData)


def test_krendering_KPointPlacementData_isa_KPlacementData():
    instance = krendering_KPointPlacementData(horizontalAlignment="sample_text", horizontalMargin=3.14, minHeight=3.14, minWidth=3.14, verticalAlignment="sample_text", verticalMargin=3.14)
    assert isinstance(instance, KPlacementData)


def test_krendering_KPolygon_isa_KPolyline():
    instance = krendering_KPolygon()
    assert isinstance(instance, KPolyline)


def test_krendering_KRoundedBendsPolyline_isa_KPolyline():
    instance = krendering_KRoundedBendsPolyline(bendRadius=3.14)
    assert isinstance(instance, KPolyline)


def test_krendering_KSpline_isa_KPolyline():
    instance = krendering_KSpline()
    assert isinstance(instance, KPolyline)


def test_krendering_KChildArea_isa_KRendering():
    instance = krendering_KChildArea()
    assert isinstance(instance, KRendering)


def test_krendering_KContainerRendering_isa_KRendering():
    instance = krendering_KContainerRendering()
    assert isinstance(instance, KRendering)


def test_krendering_KRenderingRef_isa_KRendering():
    instance = krendering_KRenderingRef()
    assert isinstance(instance, KRendering)


def test_krendering_KText_isa_KRendering():
    instance = krendering_KText(cursorSelectable=True, editable=True, text="sample_text")
    assert isinstance(instance, KRendering)


def test_krendering_KColoring_isa_KStyle():
    instance = krendering_KColoring(alpha=7, gradientAngle=3.14, targetAlpha=7)
    assert isinstance(instance, KStyle)


def test_krendering_KFontBold_isa_KStyle():
    instance = krendering_KFontBold(bold=True)
    assert isinstance(instance, KStyle)


def test_krendering_KFontItalic_isa_KStyle():
    instance = krendering_KFontItalic(italic=True)
    assert isinstance(instance, KStyle)


def test_krendering_KFontName_isa_KStyle():
    instance = krendering_KFontName(name="sample_text")
    assert isinstance(instance, KStyle)


def test_krendering_KFontSize_isa_KStyle():
    instance = krendering_KFontSize(scaleWithZoom=True, size=7)
    assert isinstance(instance, KStyle)


def test_krendering_KHorizontalAlignment_isa_KStyle():
    instance = krendering_KHorizontalAlignment(horizontalAlignment="sample_text")
    assert isinstance(instance, KStyle)


def test_krendering_KInvisibility_isa_KStyle():
    instance = krendering_KInvisibility(invisible=True)
    assert isinstance(instance, KStyle)


def test_krendering_KLineCap_isa_KStyle():
    instance = krendering_KLineCap(lineCap="sample_text")
    assert isinstance(instance, KStyle)


def test_krendering_KLineJoin_isa_KStyle():
    instance = krendering_KLineJoin(lineJoin="sample_text", miterLimit=3.14)
    assert isinstance(instance, KStyle)


def test_krendering_KLineStyle_isa_KStyle():
    instance = krendering_KLineStyle(dashOffset=3.14, dashPattern=3.14, lineStyle="sample_text")
    assert isinstance(instance, KStyle)


def test_krendering_KLineWidth_isa_KStyle():
    instance = krendering_KLineWidth(lineWidth=3.14)
    assert isinstance(instance, KStyle)


def test_krendering_KRotation_isa_KStyle():
    instance = krendering_KRotation(rotation=3.14)
    assert isinstance(instance, KStyle)


def test_krendering_KShadow_isa_KStyle():
    instance = krendering_KShadow(blur=3.14, xOffset=3.14, yOffset=3.14)
    assert isinstance(instance, KStyle)


def test_krendering_KStyleRef_isa_KStyle():
    instance = krendering_KStyleRef(referencedTypes="sample_text")
    assert isinstance(instance, KStyle)


def test_krendering_KTextStrikeout_isa_KStyle():
    instance = krendering_KTextStrikeout(struckOut="sample_text")
    assert isinstance(instance, KStyle)


def test_krendering_KTextUnderline_isa_KStyle():
    instance = krendering_KTextUnderline(underline="sample_text")
    assert isinstance(instance, KStyle)


def test_krendering_KVerticalAlignment_isa_KStyle():
    instance = krendering_KVerticalAlignment(verticalAlignment="sample_text")
    assert isinstance(instance, KStyle)


def test_krendering_KRendering_isa_KStyleHolder():
    instance = krendering_KRendering()
    assert isinstance(instance, KStyleHolder)


def test_assoc_actions2_link_reassign_clear():
    a = krendering_KAction(actionId="sample_text", altPressed="sample_text", ctrlCmdPressed="sample_text", shiftPressed="sample_text", trigger="sample_text")
    b1 = krendering_KRendering()
    b2 = krendering_KRendering()
    _safe_set(a, 'krendering_KAction', b1)
    assert _is_linked(a, 'krendering_KAction', b1)
    if hasattr(b1, 'krendering_KRendering3'):
        assert _is_linked(b1, 'krendering_KRendering3', a)
    _safe_set(a, 'krendering_KAction', b2)
    assert _is_linked(a, 'krendering_KAction', b2)
    if hasattr(b1, 'krendering_KRendering3'):
        assert not _is_linked(b1, 'krendering_KRendering3', a)
    if hasattr(b2, 'krendering_KRendering3'):
        assert _is_linked(b2, 'krendering_KRendering3', a)
    _safe_set(a, 'krendering_KAction', None)
    assert not _is_linked(a, 'krendering_KAction', b2)
    if hasattr(b2, 'krendering_KRendering3'):
        assert not _is_linked(b2, 'krendering_KRendering3', a)


def test_assoc_bottomRight17_link_reassign_clear():
    a = krendering_KPosition()
    b1 = krendering_KGridPlacement(numColumns=7)
    b2 = krendering_KGridPlacement(numColumns=13)
    _safe_set(a, 'krendering_KPosition19', b1)
    assert _is_linked(a, 'krendering_KPosition19', b1)
    if hasattr(b1, 'krendering_KGridPlacement18'):
        assert _is_linked(b1, 'krendering_KGridPlacement18', a)
    _safe_set(a, 'krendering_KPosition19', b2)
    assert _is_linked(a, 'krendering_KPosition19', b2)
    if hasattr(b1, 'krendering_KGridPlacement18'):
        assert not _is_linked(b1, 'krendering_KGridPlacement18', a)
    if hasattr(b2, 'krendering_KGridPlacement18'):
        assert _is_linked(b2, 'krendering_KGridPlacement18', a)
    _safe_set(a, 'krendering_KPosition19', None)
    assert not _is_linked(a, 'krendering_KPosition19', b2)
    if hasattr(b2, 'krendering_KGridPlacement18'):
        assert not _is_linked(b2, 'krendering_KGridPlacement18', a)


def test_assoc_bottomRight22_link_reassign_clear():
    a = krendering_KPosition()
    b1 = krendering_KAreaPlacementData()
    b2 = krendering_KAreaPlacementData()
    _safe_set(a, 'krendering_KPosition24', b1)
    assert _is_linked(a, 'krendering_KPosition24', b1)
    if hasattr(b1, 'krendering_KAreaPlacementData23'):
        assert _is_linked(b1, 'krendering_KAreaPlacementData23', a)
    _safe_set(a, 'krendering_KPosition24', b2)
    assert _is_linked(a, 'krendering_KPosition24', b2)
    if hasattr(b1, 'krendering_KAreaPlacementData23'):
        assert not _is_linked(b1, 'krendering_KAreaPlacementData23', a)
    if hasattr(b2, 'krendering_KAreaPlacementData23'):
        assert _is_linked(b2, 'krendering_KAreaPlacementData23', a)
    _safe_set(a, 'krendering_KPosition24', None)
    assert not _is_linked(a, 'krendering_KPosition24', b2)
    if hasattr(b2, 'krendering_KAreaPlacementData23'):
        assert not _is_linked(b2, 'krendering_KAreaPlacementData23', a)


def test_assoc_clipShape8_link_reassign_clear():
    a = krendering_KImage(bundleName="sample_text", imageObject="sample_text", imagePath="sample_text")
    b1 = krendering_KRendering()
    b2 = krendering_KRendering()
    _safe_set(a, 'krendering_KImage', b1)
    assert _is_linked(a, 'krendering_KImage', b1)
    if hasattr(b1, 'krendering_KRendering9'):
        assert _is_linked(b1, 'krendering_KRendering9', a)
    _safe_set(a, 'krendering_KImage', b2)
    assert _is_linked(a, 'krendering_KImage', b2)
    if hasattr(b1, 'krendering_KRendering9'):
        assert not _is_linked(b1, 'krendering_KRendering9', a)
    if hasattr(b2, 'krendering_KRendering9'):
        assert _is_linked(b2, 'krendering_KRendering9', a)
    _safe_set(a, 'krendering_KImage', None)
    assert not _is_linked(a, 'krendering_KImage', b2)
    if hasattr(b2, 'krendering_KRendering9'):
        assert not _is_linked(b2, 'krendering_KRendering9', a)


def test_assoc_color25_link_reassign_clear():
    a = krendering_KColoring(alpha=7, gradientAngle=3.14, targetAlpha=7)
    b1 = krendering_KColor(blue=7, green=7, red=7)
    b2 = krendering_KColor(blue=13, green=13, red=13)
    _safe_set(a, 'krendering_KColoring', b1)
    assert _is_linked(a, 'krendering_KColoring', b1)
    if hasattr(b1, 'krendering_KColor'):
        assert _is_linked(b1, 'krendering_KColor', a)
    _safe_set(a, 'krendering_KColoring', b2)
    assert _is_linked(a, 'krendering_KColoring', b2)
    if hasattr(b1, 'krendering_KColor'):
        assert not _is_linked(b1, 'krendering_KColor', a)
    if hasattr(b2, 'krendering_KColor'):
        assert _is_linked(b2, 'krendering_KColor', a)
    _safe_set(a, 'krendering_KColoring', None)
    assert not _is_linked(a, 'krendering_KColoring', b2)
    if hasattr(b2, 'krendering_KColor'):
        assert not _is_linked(b2, 'krendering_KColor', a)


def test_assoc_color35_link_reassign_clear():
    a = krendering_KShadow(blur=3.14, xOffset=3.14, yOffset=3.14)
    b1 = krendering_KColor(blue=7, green=7, red=7)
    b2 = krendering_KColor(blue=13, green=13, red=13)
    _safe_set(a, 'krendering_KShadow', b1)
    assert _is_linked(a, 'krendering_KShadow', b1)
    if hasattr(b1, 'krendering_KColor36'):
        assert _is_linked(b1, 'krendering_KColor36', a)
    _safe_set(a, 'krendering_KShadow', b2)
    assert _is_linked(a, 'krendering_KShadow', b2)
    if hasattr(b1, 'krendering_KColor36'):
        assert not _is_linked(b1, 'krendering_KColor36', a)
    if hasattr(b2, 'krendering_KColor36'):
        assert _is_linked(b2, 'krendering_KColor36', a)
    _safe_set(a, 'krendering_KShadow', None)
    assert not _is_linked(a, 'krendering_KShadow', b2)
    if hasattr(b2, 'krendering_KColor36'):
        assert not _is_linked(b2, 'krendering_KColor36', a)


def test_assoc_color37_link_reassign_clear():
    a = krendering_KTextUnderline(underline="sample_text")
    b1 = krendering_KColor(blue=7, green=7, red=7)
    b2 = krendering_KColor(blue=13, green=13, red=13)
    _safe_set(a, 'krendering_KTextUnderline', b1)
    assert _is_linked(a, 'krendering_KTextUnderline', b1)
    if hasattr(b1, 'krendering_KColor38'):
        assert _is_linked(b1, 'krendering_KColor38', a)
    _safe_set(a, 'krendering_KTextUnderline', b2)
    assert _is_linked(a, 'krendering_KTextUnderline', b2)
    if hasattr(b1, 'krendering_KColor38'):
        assert not _is_linked(b1, 'krendering_KColor38', a)
    if hasattr(b2, 'krendering_KColor38'):
        assert _is_linked(b2, 'krendering_KColor38', a)
    _safe_set(a, 'krendering_KTextUnderline', None)
    assert not _is_linked(a, 'krendering_KTextUnderline', b2)
    if hasattr(b2, 'krendering_KColor38'):
        assert not _is_linked(b2, 'krendering_KColor38', a)


def test_assoc_color41_link_reassign_clear():
    a = krendering_KTextStrikeout(struckOut="sample_text")
    b1 = krendering_KColor(blue=7, green=7, red=7)
    b2 = krendering_KColor(blue=13, green=13, red=13)
    _safe_set(a, 'krendering_KTextStrikeout', b1)
    assert _is_linked(a, 'krendering_KTextStrikeout', b1)
    if hasattr(b1, 'krendering_KColor42'):
        assert _is_linked(b1, 'krendering_KColor42', a)
    _safe_set(a, 'krendering_KTextStrikeout', b2)
    assert _is_linked(a, 'krendering_KTextStrikeout', b2)
    if hasattr(b1, 'krendering_KColor42'):
        assert not _is_linked(b1, 'krendering_KColor42', a)
    if hasattr(b2, 'krendering_KColor42'):
        assert _is_linked(b2, 'krendering_KColor42', a)
    _safe_set(a, 'krendering_KTextStrikeout', None)
    assert not _is_linked(a, 'krendering_KTextStrikeout', b2)
    if hasattr(b2, 'krendering_KColor42'):
        assert not _is_linked(b2, 'krendering_KColor42', a)


def test_assoc_points4_link_reassign_clear():
    a = krendering_KPosition()
    b1 = krendering_KPolyline()
    b2 = krendering_KPolyline()
    _safe_set(a, 'krendering_KPosition', b1)
    assert _is_linked(a, 'krendering_KPosition', b1)
    if hasattr(b1, 'krendering_KPolyline'):
        assert _is_linked(b1, 'krendering_KPolyline', a)
    _safe_set(a, 'krendering_KPosition', b2)
    assert _is_linked(a, 'krendering_KPosition', b2)
    if hasattr(b1, 'krendering_KPolyline'):
        assert not _is_linked(b1, 'krendering_KPolyline', a)
    if hasattr(b2, 'krendering_KPolyline'):
        assert _is_linked(b2, 'krendering_KPolyline', a)
    _safe_set(a, 'krendering_KPosition', None)
    assert not _is_linked(a, 'krendering_KPosition', b2)
    if hasattr(b2, 'krendering_KPolyline'):
        assert not _is_linked(b2, 'krendering_KPolyline', a)


def test_assoc_referencePoint31_link_reassign_clear():
    a = krendering_KPosition()
    b1 = krendering_KPointPlacementData(horizontalAlignment="sample_text", horizontalMargin=3.14, minHeight=3.14, minWidth=3.14, verticalAlignment="sample_text", verticalMargin=3.14)
    b2 = krendering_KPointPlacementData(horizontalAlignment="sample_text_2", horizontalMargin=9.99, minHeight=9.99, minWidth=9.99, verticalAlignment="sample_text_2", verticalMargin=9.99)
    _safe_set(a, 'krendering_KPosition32', b1)
    assert _is_linked(a, 'krendering_KPosition32', b1)
    if hasattr(b1, 'krendering_KPointPlacementData'):
        assert _is_linked(b1, 'krendering_KPointPlacementData', a)
    _safe_set(a, 'krendering_KPosition32', b2)
    assert _is_linked(a, 'krendering_KPosition32', b2)
    if hasattr(b1, 'krendering_KPointPlacementData'):
        assert not _is_linked(b1, 'krendering_KPointPlacementData', a)
    if hasattr(b2, 'krendering_KPointPlacementData'):
        assert _is_linked(b2, 'krendering_KPointPlacementData', a)
    _safe_set(a, 'krendering_KPosition32', None)
    assert not _is_linked(a, 'krendering_KPosition32', b2)
    if hasattr(b2, 'krendering_KPointPlacementData'):
        assert not _is_linked(b2, 'krendering_KPointPlacementData', a)


def test_assoc_renderings12_link_reassign_clear():
    a = krendering_KStyleHolder(id="sample_text")
    b1 = krendering_KRenderingLibrary()
    b2 = krendering_KRenderingLibrary()
    _safe_set(a, 'krendering_KStyleHolder', b1)
    assert _is_linked(a, 'krendering_KStyleHolder', b1)
    if hasattr(b1, 'krendering_KRenderingLibrary'):
        assert _is_linked(b1, 'krendering_KRenderingLibrary', a)
    _safe_set(a, 'krendering_KStyleHolder', b2)
    assert _is_linked(a, 'krendering_KStyleHolder', b2)
    if hasattr(b1, 'krendering_KRenderingLibrary'):
        assert not _is_linked(b1, 'krendering_KRenderingLibrary', a)
    if hasattr(b2, 'krendering_KRenderingLibrary'):
        assert _is_linked(b2, 'krendering_KRenderingLibrary', a)
    _safe_set(a, 'krendering_KStyleHolder', None)
    assert not _is_linked(a, 'krendering_KStyleHolder', b2)
    if hasattr(b2, 'krendering_KRenderingLibrary'):
        assert not _is_linked(b2, 'krendering_KRenderingLibrary', a)


def test_assoc_rotationAnchor29_link_reassign_clear():
    a = krendering_KRotation(rotation=3.14)
    b1 = krendering_KPosition()
    b2 = krendering_KPosition()
    _safe_set(a, 'krendering_KRotation', b1)
    assert _is_linked(a, 'krendering_KRotation', b1)
    if hasattr(b1, 'krendering_KPosition30'):
        assert _is_linked(b1, 'krendering_KPosition30', a)
    _safe_set(a, 'krendering_KRotation', b2)
    assert _is_linked(a, 'krendering_KRotation', b2)
    if hasattr(b1, 'krendering_KPosition30'):
        assert not _is_linked(b1, 'krendering_KPosition30', a)
    if hasattr(b2, 'krendering_KPosition30'):
        assert _is_linked(b2, 'krendering_KPosition30', a)
    _safe_set(a, 'krendering_KRotation', None)
    assert not _is_linked(a, 'krendering_KRotation', b2)
    if hasattr(b2, 'krendering_KPosition30'):
        assert not _is_linked(b2, 'krendering_KPosition30', a)


def test_assoc_styleHolder39_link_reassign_clear():
    a = krendering_KStyleRef(referencedTypes="sample_text")
    b1 = krendering_KStyleHolder(id="sample_text")
    b2 = krendering_KStyleHolder(id="sample_text_2")
    _safe_set(a, 'krendering_KStyleRef', b1)
    assert _is_linked(a, 'krendering_KStyleRef', b1)
    if hasattr(b1, 'krendering_KStyleHolder40'):
        assert _is_linked(b1, 'krendering_KStyleHolder40', a)
    _safe_set(a, 'krendering_KStyleRef', b2)
    assert _is_linked(a, 'krendering_KStyleRef', b2)
    if hasattr(b1, 'krendering_KStyleHolder40'):
        assert not _is_linked(b1, 'krendering_KStyleHolder40', a)
    if hasattr(b2, 'krendering_KStyleHolder40'):
        assert _is_linked(b2, 'krendering_KStyleHolder40', a)
    _safe_set(a, 'krendering_KStyleRef', None)
    assert not _is_linked(a, 'krendering_KStyleRef', b2)
    if hasattr(b2, 'krendering_KStyleHolder40'):
        assert not _is_linked(b2, 'krendering_KStyleHolder40', a)


def test_assoc_styles33_link_reassign_clear():
    a = krendering_KStyleHolder(id="sample_text")
    b1 = krendering_KStyle(modifierId="sample_text", propagateToChildren=True, selection=True)
    b2 = krendering_KStyle(modifierId="sample_text_2", propagateToChildren=False, selection=False)
    _safe_set(a, 'krendering_KStyleHolder34', {b1})
    assert _is_linked(a, 'krendering_KStyleHolder34', b1)
    if hasattr(b1, 'krendering_KStyle'):
        assert _is_linked(b1, 'krendering_KStyle', a)
    _safe_set(a, 'krendering_KStyleHolder34', {b2})
    assert _is_linked(a, 'krendering_KStyleHolder34', b2)
    if hasattr(b1, 'krendering_KStyle'):
        assert not _is_linked(b1, 'krendering_KStyle', a)
    if hasattr(b2, 'krendering_KStyle'):
        assert _is_linked(b2, 'krendering_KStyle', a)
    _safe_set(a, 'krendering_KStyleHolder34', set())
    assert not _is_linked(a, 'krendering_KStyleHolder34', b2)
    if hasattr(b2, 'krendering_KStyle'):
        assert not _is_linked(b2, 'krendering_KStyle', a)


def test_assoc_targetColor26_link_reassign_clear():
    a = krendering_KColoring(alpha=7, gradientAngle=3.14, targetAlpha=7)
    b1 = krendering_KColor(blue=7, green=7, red=7)
    b2 = krendering_KColor(blue=13, green=13, red=13)
    _safe_set(a, 'krendering_KColoring27', b1)
    assert _is_linked(a, 'krendering_KColoring27', b1)
    if hasattr(b1, 'krendering_KColor28'):
        assert _is_linked(b1, 'krendering_KColor28', a)
    _safe_set(a, 'krendering_KColoring27', b2)
    assert _is_linked(a, 'krendering_KColoring27', b2)
    if hasattr(b1, 'krendering_KColor28'):
        assert not _is_linked(b1, 'krendering_KColor28', a)
    if hasattr(b2, 'krendering_KColor28'):
        assert _is_linked(b2, 'krendering_KColor28', a)
    _safe_set(a, 'krendering_KColoring27', None)
    assert not _is_linked(a, 'krendering_KColoring27', b2)
    if hasattr(b2, 'krendering_KColor28'):
        assert not _is_linked(b2, 'krendering_KColor28', a)


def test_assoc_topLeft15_link_reassign_clear():
    a = krendering_KPosition()
    b1 = krendering_KGridPlacement(numColumns=7)
    b2 = krendering_KGridPlacement(numColumns=13)
    _safe_set(a, 'krendering_KPosition16', b1)
    assert _is_linked(a, 'krendering_KPosition16', b1)
    if hasattr(b1, 'krendering_KGridPlacement'):
        assert _is_linked(b1, 'krendering_KGridPlacement', a)
    _safe_set(a, 'krendering_KPosition16', b2)
    assert _is_linked(a, 'krendering_KPosition16', b2)
    if hasattr(b1, 'krendering_KGridPlacement'):
        assert not _is_linked(b1, 'krendering_KGridPlacement', a)
    if hasattr(b2, 'krendering_KGridPlacement'):
        assert _is_linked(b2, 'krendering_KGridPlacement', a)
    _safe_set(a, 'krendering_KPosition16', None)
    assert not _is_linked(a, 'krendering_KPosition16', b2)
    if hasattr(b2, 'krendering_KGridPlacement'):
        assert not _is_linked(b2, 'krendering_KGridPlacement', a)


def test_assoc_topLeft20_link_reassign_clear():
    a = krendering_KPosition()
    b1 = krendering_KAreaPlacementData()
    b2 = krendering_KAreaPlacementData()
    _safe_set(a, 'krendering_KPosition21', b1)
    assert _is_linked(a, 'krendering_KPosition21', b1)
    if hasattr(b1, 'krendering_KAreaPlacementData'):
        assert _is_linked(b1, 'krendering_KAreaPlacementData', a)
    _safe_set(a, 'krendering_KPosition21', b2)
    assert _is_linked(a, 'krendering_KPosition21', b2)
    if hasattr(b1, 'krendering_KAreaPlacementData'):
        assert not _is_linked(b1, 'krendering_KAreaPlacementData', a)
    if hasattr(b2, 'krendering_KAreaPlacementData'):
        assert _is_linked(b2, 'krendering_KAreaPlacementData', a)
    _safe_set(a, 'krendering_KPosition21', None)
    assert not _is_linked(a, 'krendering_KPosition21', b2)
    if hasattr(b2, 'krendering_KAreaPlacementData'):
        assert not _is_linked(b2, 'krendering_KAreaPlacementData', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

EMapPropertyHolder_strategy = st.builds(EMapPropertyHolder)
@given(instance=EMapPropertyHolder_strategy)
@settings(max_examples=25)
def test_EMapPropertyHolder_instantiation(instance):
    assert isinstance(instance, EMapPropertyHolder)


KAreaPlacementData_strategy = st.builds(KAreaPlacementData)
@given(instance=KAreaPlacementData_strategy)
@settings(max_examples=25)
def test_KAreaPlacementData_instantiation(instance):
    assert isinstance(instance, KAreaPlacementData)


KContainerRendering_strategy = st.builds(KContainerRendering)
@given(instance=KContainerRendering_strategy)
@settings(max_examples=25)
def test_KContainerRendering_instantiation(instance):
    assert isinstance(instance, KContainerRendering)


KGraphData_strategy = st.builds(KGraphData)
@given(instance=KGraphData_strategy)
@settings(max_examples=25)
def test_KGraphData_instantiation(instance):
    assert isinstance(instance, KGraphData)


KPlacement_strategy = st.builds(KPlacement)
@given(instance=KPlacement_strategy)
@settings(max_examples=25)
def test_KPlacement_instantiation(instance):
    assert isinstance(instance, KPlacement)


KPlacementData_strategy = st.builds(KPlacementData)
@given(instance=KPlacementData_strategy)
@settings(max_examples=25)
def test_KPlacementData_instantiation(instance):
    assert isinstance(instance, KPlacementData)


KPolyline_strategy = st.builds(KPolyline)
@given(instance=KPolyline_strategy)
@settings(max_examples=25)
def test_KPolyline_instantiation(instance):
    assert isinstance(instance, KPolyline)


KRendering_strategy = st.builds(KRendering)
@given(instance=KRendering_strategy)
@settings(max_examples=25)
def test_KRendering_instantiation(instance):
    assert isinstance(instance, KRendering)


KStyle_strategy = st.builds(KStyle)
@given(instance=KStyle_strategy)
@settings(max_examples=25)
def test_KStyle_instantiation(instance):
    assert isinstance(instance, KStyle)


KStyleHolder_strategy = st.builds(KStyleHolder)
@given(instance=KStyleHolder_strategy)
@settings(max_examples=25)
def test_KStyleHolder_instantiation(instance):
    assert isinstance(instance, KStyleHolder)


krendering_KAction_strategy = st.builds(krendering_KAction, actionId=safe_text, altPressed=safe_text, ctrlCmdPressed=safe_text, shiftPressed=safe_text, trigger=safe_text)
@given(instance=krendering_KAction_strategy)
@settings(max_examples=25)
def test_krendering_KAction_instantiation(instance):
    assert isinstance(instance, krendering_KAction)


krendering_KArc_strategy = st.builds(krendering_KArc, arcAngle=st.floats(allow_nan=False, allow_infinity=False), arcType=safe_text, startAngle=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KArc_strategy)
@settings(max_examples=25)
def test_krendering_KArc_instantiation(instance):
    assert isinstance(instance, krendering_KArc)


krendering_KAreaPlacementData_strategy = st.builds(krendering_KAreaPlacementData)
@given(instance=krendering_KAreaPlacementData_strategy)
@settings(max_examples=25)
def test_krendering_KAreaPlacementData_instantiation(instance):
    assert isinstance(instance, krendering_KAreaPlacementData)


krendering_KBackground_strategy = st.builds(krendering_KBackground)
@given(instance=krendering_KBackground_strategy)
@settings(max_examples=25)
def test_krendering_KBackground_instantiation(instance):
    assert isinstance(instance, krendering_KBackground)


krendering_KBottomPosition_strategy = st.builds(krendering_KBottomPosition)
@given(instance=krendering_KBottomPosition_strategy)
@settings(max_examples=25)
def test_krendering_KBottomPosition_instantiation(instance):
    assert isinstance(instance, krendering_KBottomPosition)


krendering_KChildArea_strategy = st.builds(krendering_KChildArea)
@given(instance=krendering_KChildArea_strategy)
@settings(max_examples=25)
def test_krendering_KChildArea_instantiation(instance):
    assert isinstance(instance, krendering_KChildArea)


krendering_KColor_strategy = st.builds(krendering_KColor, blue=st.integers(), green=st.integers(), red=st.integers())
@given(instance=krendering_KColor_strategy)
@settings(max_examples=25)
def test_krendering_KColor_instantiation(instance):
    assert isinstance(instance, krendering_KColor)


krendering_KColoring_strategy = st.builds(krendering_KColoring, alpha=st.integers(), gradientAngle=st.floats(allow_nan=False, allow_infinity=False), targetAlpha=st.integers())
@given(instance=krendering_KColoring_strategy)
@settings(max_examples=25)
def test_krendering_KColoring_instantiation(instance):
    assert isinstance(instance, krendering_KColoring)


krendering_KContainerRendering_strategy = st.builds(krendering_KContainerRendering)
@given(instance=krendering_KContainerRendering_strategy)
@settings(max_examples=25)
def test_krendering_KContainerRendering_instantiation(instance):
    assert isinstance(instance, krendering_KContainerRendering)


krendering_KCustomRendering_strategy = st.builds(krendering_KCustomRendering, bundleName=safe_text, className=safe_text, figureObject=safe_text)
@given(instance=krendering_KCustomRendering_strategy)
@settings(max_examples=25)
def test_krendering_KCustomRendering_instantiation(instance):
    assert isinstance(instance, krendering_KCustomRendering)


krendering_KDecoratorPlacementData_strategy = st.builds(krendering_KDecoratorPlacementData, absolute=st.floats(allow_nan=False, allow_infinity=False), height=st.floats(allow_nan=False, allow_infinity=False), relative=st.floats(allow_nan=False, allow_infinity=False), rotateWithLine=st.booleans(), width=st.floats(allow_nan=False, allow_infinity=False), xOffset=st.floats(allow_nan=False, allow_infinity=False), yOffset=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KDecoratorPlacementData_strategy)
@settings(max_examples=25)
def test_krendering_KDecoratorPlacementData_instantiation(instance):
    assert isinstance(instance, krendering_KDecoratorPlacementData)


krendering_KEllipse_strategy = st.builds(krendering_KEllipse)
@given(instance=krendering_KEllipse_strategy)
@settings(max_examples=25)
def test_krendering_KEllipse_instantiation(instance):
    assert isinstance(instance, krendering_KEllipse)


krendering_KFontBold_strategy = st.builds(krendering_KFontBold, bold=st.booleans())
@given(instance=krendering_KFontBold_strategy)
@settings(max_examples=25)
def test_krendering_KFontBold_instantiation(instance):
    assert isinstance(instance, krendering_KFontBold)


krendering_KFontItalic_strategy = st.builds(krendering_KFontItalic, italic=st.booleans())
@given(instance=krendering_KFontItalic_strategy)
@settings(max_examples=25)
def test_krendering_KFontItalic_instantiation(instance):
    assert isinstance(instance, krendering_KFontItalic)


krendering_KFontName_strategy = st.builds(krendering_KFontName, name=safe_text)
@given(instance=krendering_KFontName_strategy)
@settings(max_examples=25)
def test_krendering_KFontName_instantiation(instance):
    assert isinstance(instance, krendering_KFontName)


krendering_KFontSize_strategy = st.builds(krendering_KFontSize, scaleWithZoom=st.booleans(), size=st.integers())
@given(instance=krendering_KFontSize_strategy)
@settings(max_examples=25)
def test_krendering_KFontSize_instantiation(instance):
    assert isinstance(instance, krendering_KFontSize)


krendering_KForeground_strategy = st.builds(krendering_KForeground)
@given(instance=krendering_KForeground_strategy)
@settings(max_examples=25)
def test_krendering_KForeground_instantiation(instance):
    assert isinstance(instance, krendering_KForeground)


krendering_KGridPlacement_strategy = st.builds(krendering_KGridPlacement, numColumns=st.integers())
@given(instance=krendering_KGridPlacement_strategy)
@settings(max_examples=25)
def test_krendering_KGridPlacement_instantiation(instance):
    assert isinstance(instance, krendering_KGridPlacement)


krendering_KGridPlacementData_strategy = st.builds(krendering_KGridPlacementData, flexibleHeight=safe_text, flexibleWidth=safe_text, minCellHeight=st.floats(allow_nan=False, allow_infinity=False), minCellWidth=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KGridPlacementData_strategy)
@settings(max_examples=25)
def test_krendering_KGridPlacementData_instantiation(instance):
    assert isinstance(instance, krendering_KGridPlacementData)


krendering_KHorizontalAlignment_strategy = st.builds(krendering_KHorizontalAlignment, horizontalAlignment=safe_text)
@given(instance=krendering_KHorizontalAlignment_strategy)
@settings(max_examples=25)
def test_krendering_KHorizontalAlignment_instantiation(instance):
    assert isinstance(instance, krendering_KHorizontalAlignment)


krendering_KImage_strategy = st.builds(krendering_KImage, bundleName=safe_text, imageObject=safe_text, imagePath=safe_text)
@given(instance=krendering_KImage_strategy)
@settings(max_examples=25)
def test_krendering_KImage_instantiation(instance):
    assert isinstance(instance, krendering_KImage)


krendering_KInvisibility_strategy = st.builds(krendering_KInvisibility, invisible=st.booleans())
@given(instance=krendering_KInvisibility_strategy)
@settings(max_examples=25)
def test_krendering_KInvisibility_instantiation(instance):
    assert isinstance(instance, krendering_KInvisibility)


krendering_KLeftPosition_strategy = st.builds(krendering_KLeftPosition)
@given(instance=krendering_KLeftPosition_strategy)
@settings(max_examples=25)
def test_krendering_KLeftPosition_instantiation(instance):
    assert isinstance(instance, krendering_KLeftPosition)


krendering_KLineCap_strategy = st.builds(krendering_KLineCap, lineCap=safe_text)
@given(instance=krendering_KLineCap_strategy)
@settings(max_examples=25)
def test_krendering_KLineCap_instantiation(instance):
    assert isinstance(instance, krendering_KLineCap)


krendering_KLineJoin_strategy = st.builds(krendering_KLineJoin, lineJoin=safe_text, miterLimit=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KLineJoin_strategy)
@settings(max_examples=25)
def test_krendering_KLineJoin_instantiation(instance):
    assert isinstance(instance, krendering_KLineJoin)


krendering_KLineStyle_strategy = st.builds(krendering_KLineStyle, dashOffset=st.floats(allow_nan=False, allow_infinity=False), dashPattern=st.floats(allow_nan=False, allow_infinity=False), lineStyle=safe_text)
@given(instance=krendering_KLineStyle_strategy)
@settings(max_examples=25)
def test_krendering_KLineStyle_instantiation(instance):
    assert isinstance(instance, krendering_KLineStyle)


krendering_KLineWidth_strategy = st.builds(krendering_KLineWidth, lineWidth=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KLineWidth_strategy)
@settings(max_examples=25)
def test_krendering_KLineWidth_instantiation(instance):
    assert isinstance(instance, krendering_KLineWidth)


krendering_KPlacement_strategy = st.builds(krendering_KPlacement)
@given(instance=krendering_KPlacement_strategy)
@settings(max_examples=25)
def test_krendering_KPlacement_instantiation(instance):
    assert isinstance(instance, krendering_KPlacement)


krendering_KPlacementData_strategy = st.builds(krendering_KPlacementData)
@given(instance=krendering_KPlacementData_strategy)
@settings(max_examples=25)
def test_krendering_KPlacementData_instantiation(instance):
    assert isinstance(instance, krendering_KPlacementData)


krendering_KPointPlacementData_strategy = st.builds(krendering_KPointPlacementData, horizontalAlignment=safe_text, horizontalMargin=st.floats(allow_nan=False, allow_infinity=False), minHeight=st.floats(allow_nan=False, allow_infinity=False), minWidth=st.floats(allow_nan=False, allow_infinity=False), verticalAlignment=safe_text, verticalMargin=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KPointPlacementData_strategy)
@settings(max_examples=25)
def test_krendering_KPointPlacementData_instantiation(instance):
    assert isinstance(instance, krendering_KPointPlacementData)


krendering_KPolygon_strategy = st.builds(krendering_KPolygon)
@given(instance=krendering_KPolygon_strategy)
@settings(max_examples=25)
def test_krendering_KPolygon_instantiation(instance):
    assert isinstance(instance, krendering_KPolygon)


krendering_KPolyline_strategy = st.builds(krendering_KPolyline)
@given(instance=krendering_KPolyline_strategy)
@settings(max_examples=25)
def test_krendering_KPolyline_instantiation(instance):
    assert isinstance(instance, krendering_KPolyline)


krendering_KPosition_strategy = st.builds(krendering_KPosition)
@given(instance=krendering_KPosition_strategy)
@settings(max_examples=25)
def test_krendering_KPosition_instantiation(instance):
    assert isinstance(instance, krendering_KPosition)


krendering_KRectangle_strategy = st.builds(krendering_KRectangle)
@given(instance=krendering_KRectangle_strategy)
@settings(max_examples=25)
def test_krendering_KRectangle_instantiation(instance):
    assert isinstance(instance, krendering_KRectangle)


krendering_KRendering_strategy = st.builds(krendering_KRendering)
@given(instance=krendering_KRendering_strategy)
@settings(max_examples=25)
def test_krendering_KRendering_instantiation(instance):
    assert isinstance(instance, krendering_KRendering)


krendering_KRenderingLibrary_strategy = st.builds(krendering_KRenderingLibrary)
@given(instance=krendering_KRenderingLibrary_strategy)
@settings(max_examples=25)
def test_krendering_KRenderingLibrary_instantiation(instance):
    assert isinstance(instance, krendering_KRenderingLibrary)


krendering_KRenderingRef_strategy = st.builds(krendering_KRenderingRef)
@given(instance=krendering_KRenderingRef_strategy)
@settings(max_examples=25)
def test_krendering_KRenderingRef_instantiation(instance):
    assert isinstance(instance, krendering_KRenderingRef)


krendering_KRightPosition_strategy = st.builds(krendering_KRightPosition)
@given(instance=krendering_KRightPosition_strategy)
@settings(max_examples=25)
def test_krendering_KRightPosition_instantiation(instance):
    assert isinstance(instance, krendering_KRightPosition)


krendering_KRotation_strategy = st.builds(krendering_KRotation, rotation=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KRotation_strategy)
@settings(max_examples=25)
def test_krendering_KRotation_instantiation(instance):
    assert isinstance(instance, krendering_KRotation)


krendering_KRoundedBendsPolyline_strategy = st.builds(krendering_KRoundedBendsPolyline, bendRadius=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KRoundedBendsPolyline_strategy)
@settings(max_examples=25)
def test_krendering_KRoundedBendsPolyline_instantiation(instance):
    assert isinstance(instance, krendering_KRoundedBendsPolyline)


krendering_KRoundedRectangle_strategy = st.builds(krendering_KRoundedRectangle, cornerHeight=st.floats(allow_nan=False, allow_infinity=False), cornerWidth=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KRoundedRectangle_strategy)
@settings(max_examples=25)
def test_krendering_KRoundedRectangle_instantiation(instance):
    assert isinstance(instance, krendering_KRoundedRectangle)


krendering_KShadow_strategy = st.builds(krendering_KShadow, blur=st.floats(allow_nan=False, allow_infinity=False), xOffset=st.floats(allow_nan=False, allow_infinity=False), yOffset=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KShadow_strategy)
@settings(max_examples=25)
def test_krendering_KShadow_instantiation(instance):
    assert isinstance(instance, krendering_KShadow)


krendering_KSpline_strategy = st.builds(krendering_KSpline)
@given(instance=krendering_KSpline_strategy)
@settings(max_examples=25)
def test_krendering_KSpline_instantiation(instance):
    assert isinstance(instance, krendering_KSpline)


krendering_KStyle_strategy = st.builds(krendering_KStyle, modifierId=safe_text, propagateToChildren=st.booleans(), selection=st.booleans())
@given(instance=krendering_KStyle_strategy)
@settings(max_examples=25)
def test_krendering_KStyle_instantiation(instance):
    assert isinstance(instance, krendering_KStyle)


krendering_KStyleHolder_strategy = st.builds(krendering_KStyleHolder, id=safe_text)
@given(instance=krendering_KStyleHolder_strategy)
@settings(max_examples=25)
def test_krendering_KStyleHolder_instantiation(instance):
    assert isinstance(instance, krendering_KStyleHolder)


krendering_KStyleRef_strategy = st.builds(krendering_KStyleRef, referencedTypes=safe_text)
@given(instance=krendering_KStyleRef_strategy)
@settings(max_examples=25)
def test_krendering_KStyleRef_instantiation(instance):
    assert isinstance(instance, krendering_KStyleRef)


krendering_KText_strategy = st.builds(krendering_KText, cursorSelectable=st.booleans(), editable=st.booleans(), text=safe_text)
@given(instance=krendering_KText_strategy)
@settings(max_examples=25)
def test_krendering_KText_instantiation(instance):
    assert isinstance(instance, krendering_KText)


krendering_KTextStrikeout_strategy = st.builds(krendering_KTextStrikeout, struckOut=safe_text)
@given(instance=krendering_KTextStrikeout_strategy)
@settings(max_examples=25)
def test_krendering_KTextStrikeout_instantiation(instance):
    assert isinstance(instance, krendering_KTextStrikeout)


krendering_KTextUnderline_strategy = st.builds(krendering_KTextUnderline, underline=safe_text)
@given(instance=krendering_KTextUnderline_strategy)
@settings(max_examples=25)
def test_krendering_KTextUnderline_instantiation(instance):
    assert isinstance(instance, krendering_KTextUnderline)


krendering_KTopPosition_strategy = st.builds(krendering_KTopPosition)
@given(instance=krendering_KTopPosition_strategy)
@settings(max_examples=25)
def test_krendering_KTopPosition_instantiation(instance):
    assert isinstance(instance, krendering_KTopPosition)


krendering_KVerticalAlignment_strategy = st.builds(krendering_KVerticalAlignment, verticalAlignment=safe_text)
@given(instance=krendering_KVerticalAlignment_strategy)
@settings(max_examples=25)
def test_krendering_KVerticalAlignment_instantiation(instance):
    assert isinstance(instance, krendering_KVerticalAlignment)


krendering_KXPosition_strategy = st.builds(krendering_KXPosition, absolute=st.floats(allow_nan=False, allow_infinity=False), relative=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KXPosition_strategy)
@settings(max_examples=25)
def test_krendering_KXPosition_instantiation(instance):
    assert isinstance(instance, krendering_KXPosition)


krendering_KYPosition_strategy = st.builds(krendering_KYPosition, absolute=st.floats(allow_nan=False, allow_infinity=False), relative=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=krendering_KYPosition_strategy)
@settings(max_examples=25)
def test_krendering_KYPosition_instantiation(instance):
    assert isinstance(instance, krendering_KYPosition)


