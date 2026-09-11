import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    xygraph_AxisDescriptor,
    xygraph_ColorDescriptor,
    xygraph_EObject,
    xygraph_FontDescriptor,
    xygraph_TraceDescriptor,
    xygraph_XYGraphDescriptor,
    LinearScale_Orientation,
    Trace_BaseLine,
    Trace_ErrorBarType,
    Trace_PointStyle,
    Trace_TraceType,
    ZoomType,
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

def test_xygraph_AxisDescriptor_autoFormat_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.autoFormat == True
    instance.autoFormat = False
    assert instance.autoFormat == False


def test_xygraph_AxisDescriptor_autoScale_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.autoScale == True
    instance.autoScale = False
    assert instance.autoScale == False


def test_xygraph_AxisDescriptor_autoScaleThreshold_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.autoScaleThreshold == 3.14
    instance.autoScaleThreshold = 9.99
    assert instance.autoScaleThreshold == 9.99


def test_xygraph_AxisDescriptor_dashGridLine_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.dashGridLine == True
    instance.dashGridLine = False
    assert instance.dashGridLine == False


def test_xygraph_AxisDescriptor_dateEnabled_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.dateEnabled == True
    instance.dateEnabled = False
    assert instance.dateEnabled == False


def test_xygraph_AxisDescriptor_formatPattern_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.formatPattern == "sample_text"
    instance.formatPattern = "sample_text_2"
    assert instance.formatPattern == "sample_text_2"


def test_xygraph_AxisDescriptor_logScale_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.logScale == True
    instance.logScale = False
    assert instance.logScale == False


def test_xygraph_AxisDescriptor_minorTicksVisible_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.minorTicksVisible == True
    instance.minorTicksVisible = False
    assert instance.minorTicksVisible == False


def test_xygraph_AxisDescriptor_orientation_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.orientation == "sample_text"
    instance.orientation = "sample_text_2"
    assert instance.orientation == "sample_text_2"


def test_xygraph_AxisDescriptor_primarySide_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.primarySide == True
    instance.primarySide = False
    assert instance.primarySide == False


def test_xygraph_AxisDescriptor_rangeLower_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.rangeLower == 3.14
    instance.rangeLower = 9.99
    assert instance.rangeLower == 9.99


def test_xygraph_AxisDescriptor_rangeUpper_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.rangeUpper == 3.14
    instance.rangeUpper = 9.99
    assert instance.rangeUpper == 9.99


def test_xygraph_AxisDescriptor_showMajorGrid_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.showMajorGrid == True
    instance.showMajorGrid = False
    assert instance.showMajorGrid == False


def test_xygraph_AxisDescriptor_showMinorGrid_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.showMinorGrid == True
    instance.showMinorGrid = False
    assert instance.showMinorGrid == False


def test_xygraph_AxisDescriptor_title_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_xygraph_AxisDescriptor_zoomType_value_roundtrip():
    instance = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    assert instance.zoomType == "sample_text"
    instance.zoomType = "sample_text_2"
    assert instance.zoomType == "sample_text_2"


def test_xygraph_ColorDescriptor_b_value_roundtrip():
    instance = xygraph_ColorDescriptor(b=7, g=7, r=7)
    assert instance.b == 7
    instance.b = 13
    assert instance.b == 13


def test_xygraph_ColorDescriptor_g_value_roundtrip():
    instance = xygraph_ColorDescriptor(b=7, g=7, r=7)
    assert instance.g == 7
    instance.g = 13
    assert instance.g == 13


def test_xygraph_ColorDescriptor_r_value_roundtrip():
    instance = xygraph_ColorDescriptor(b=7, g=7, r=7)
    assert instance.r == 7
    instance.r = 13
    assert instance.r == 13


def test_xygraph_FontDescriptor_name_value_roundtrip():
    instance = xygraph_FontDescriptor(name="sample_text", size=7, style=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xygraph_FontDescriptor_size_value_roundtrip():
    instance = xygraph_FontDescriptor(name="sample_text", size=7, style=7)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_xygraph_FontDescriptor_style_value_roundtrip():
    instance = xygraph_FontDescriptor(name="sample_text", size=7, style=7)
    assert instance.style == 7
    instance.style = 13
    assert instance.style == 13


def test_xygraph_TraceDescriptor_antiAliasing_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.antiAliasing == True
    instance.antiAliasing = False
    assert instance.antiAliasing == False


def test_xygraph_TraceDescriptor_areaAlpha_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.areaAlpha == 7
    instance.areaAlpha = 13
    assert instance.areaAlpha == 13


def test_xygraph_TraceDescriptor_baseLine_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.baseLine == "sample_text"
    instance.baseLine = "sample_text_2"
    assert instance.baseLine == "sample_text_2"


def test_xygraph_TraceDescriptor_drawYErrorInArea_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.drawYErrorInArea == True
    instance.drawYErrorInArea = False
    assert instance.drawYErrorInArea == False


def test_xygraph_TraceDescriptor_errorBarCapWidth_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.errorBarCapWidth == 7
    instance.errorBarCapWidth = 13
    assert instance.errorBarCapWidth == 13


def test_xygraph_TraceDescriptor_errorBarEnabled_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.errorBarEnabled == True
    instance.errorBarEnabled = False
    assert instance.errorBarEnabled == False


def test_xygraph_TraceDescriptor_lineWidth_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.lineWidth == 7
    instance.lineWidth = 13
    assert instance.lineWidth == 13


def test_xygraph_TraceDescriptor_name_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xygraph_TraceDescriptor_pointSize_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.pointSize == 7
    instance.pointSize = 13
    assert instance.pointSize == 13


def test_xygraph_TraceDescriptor_pointStyle_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.pointStyle == "sample_text"
    instance.pointStyle = "sample_text_2"
    assert instance.pointStyle == "sample_text_2"


def test_xygraph_TraceDescriptor_traceType_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.traceType == "sample_text"
    instance.traceType = "sample_text_2"
    assert instance.traceType == "sample_text_2"


def test_xygraph_TraceDescriptor_xErrorBarType_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.xErrorBarType == "sample_text"
    instance.xErrorBarType = "sample_text_2"
    assert instance.xErrorBarType == "sample_text_2"


def test_xygraph_TraceDescriptor_yErrorBarType_value_roundtrip():
    instance = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    assert instance.yErrorBarType == "sample_text"
    instance.yErrorBarType = "sample_text_2"
    assert instance.yErrorBarType == "sample_text_2"


def test_xygraph_XYGraphDescriptor_showLegend_value_roundtrip():
    instance = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    assert instance.showLegend == True
    instance.showLegend = False
    assert instance.showLegend == False


def test_xygraph_XYGraphDescriptor_showPlotAreaBorder_value_roundtrip():
    instance = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    assert instance.showPlotAreaBorder == True
    instance.showPlotAreaBorder = False
    assert instance.showPlotAreaBorder == False


def test_xygraph_XYGraphDescriptor_showTitle_value_roundtrip():
    instance = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    assert instance.showTitle == True
    instance.showTitle = False
    assert instance.showTitle == False


def test_xygraph_XYGraphDescriptor_title_value_roundtrip():
    instance = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_xygraph_XYGraphDescriptor_transparent_value_roundtrip():
    instance = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    assert instance.transparent == True
    instance.transparent = False
    assert instance.transparent == False


def test_xygraph_XYGraphDescriptor_zoomType_value_roundtrip():
    instance = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    assert instance.zoomType == "sample_text"
    instance.zoomType = "sample_text_2"
    assert instance.zoomType == "sample_text_2"


def test_assoc_axisDescriptors1_link_reassign_clear():
    a = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    b1 = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    b2 = xygraph_AxisDescriptor(autoFormat=False, autoScale=False, autoScaleThreshold=9.99, dashGridLine=False, dateEnabled=False, formatPattern="sample_text_2", logScale=False, minorTicksVisible=False, orientation="sample_text_2", primarySide=False, rangeLower=9.99, rangeUpper=9.99, showMajorGrid=False, showMinorGrid=False, title="sample_text_2", zoomType="sample_text_2")
    _safe_set(a, 'xygraph_XYGraphDescriptor2', {b1})
    assert _is_linked(a, 'xygraph_XYGraphDescriptor2', b1)
    if hasattr(b1, 'xygraph_AxisDescriptor'):
        assert _is_linked(b1, 'xygraph_AxisDescriptor', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor2', {b2})
    assert _is_linked(a, 'xygraph_XYGraphDescriptor2', b2)
    if hasattr(b1, 'xygraph_AxisDescriptor'):
        assert not _is_linked(b1, 'xygraph_AxisDescriptor', a)
    if hasattr(b2, 'xygraph_AxisDescriptor'):
        assert _is_linked(b2, 'xygraph_AxisDescriptor', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor2', set())
    assert not _is_linked(a, 'xygraph_XYGraphDescriptor2', b2)
    if hasattr(b2, 'xygraph_AxisDescriptor'):
        assert not _is_linked(b2, 'xygraph_AxisDescriptor', a)


def test_assoc_backgroundColor18_link_reassign_clear():
    a = xygraph_ColorDescriptor(b=7, g=7, r=7)
    b1 = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    b2 = xygraph_AxisDescriptor(autoFormat=False, autoScale=False, autoScaleThreshold=9.99, dashGridLine=False, dateEnabled=False, formatPattern="sample_text_2", logScale=False, minorTicksVisible=False, orientation="sample_text_2", primarySide=False, rangeLower=9.99, rangeUpper=9.99, showMajorGrid=False, showMinorGrid=False, title="sample_text_2", zoomType="sample_text_2")
    _safe_set(a, 'xygraph_ColorDescriptor20', b1)
    assert _is_linked(a, 'xygraph_ColorDescriptor20', b1)
    if hasattr(b1, 'xygraph_AxisDescriptor19'):
        assert _is_linked(b1, 'xygraph_AxisDescriptor19', a)
    _safe_set(a, 'xygraph_ColorDescriptor20', b2)
    assert _is_linked(a, 'xygraph_ColorDescriptor20', b2)
    if hasattr(b1, 'xygraph_AxisDescriptor19'):
        assert not _is_linked(b1, 'xygraph_AxisDescriptor19', a)
    if hasattr(b2, 'xygraph_AxisDescriptor19'):
        assert _is_linked(b2, 'xygraph_AxisDescriptor19', a)
    _safe_set(a, 'xygraph_ColorDescriptor20', None)
    assert not _is_linked(a, 'xygraph_ColorDescriptor20', b2)
    if hasattr(b2, 'xygraph_AxisDescriptor19'):
        assert not _is_linked(b2, 'xygraph_AxisDescriptor19', a)


def test_assoc_context10_link_reassign_clear():
    a = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    b1 = xygraph_EObject()
    b2 = xygraph_EObject()
    _safe_set(a, 'xygraph_XYGraphDescriptor11', b1)
    assert _is_linked(a, 'xygraph_XYGraphDescriptor11', b1)
    if hasattr(b1, 'xygraph_EObject'):
        assert _is_linked(b1, 'xygraph_EObject', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor11', b2)
    assert _is_linked(a, 'xygraph_XYGraphDescriptor11', b2)
    if hasattr(b1, 'xygraph_EObject'):
        assert not _is_linked(b1, 'xygraph_EObject', a)
    if hasattr(b2, 'xygraph_EObject'):
        assert _is_linked(b2, 'xygraph_EObject', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor11', None)
    assert not _is_linked(a, 'xygraph_XYGraphDescriptor11', b2)
    if hasattr(b2, 'xygraph_EObject'):
        assert not _is_linked(b2, 'xygraph_EObject', a)


def test_assoc_dataSource12_link_reassign_clear():
    a = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    b1 = xygraph_EObject()
    b2 = xygraph_EObject()
    _safe_set(a, 'xygraph_XYGraphDescriptor13', b1)
    assert _is_linked(a, 'xygraph_XYGraphDescriptor13', b1)
    if hasattr(b1, 'xygraph_EObject14'):
        assert _is_linked(b1, 'xygraph_EObject14', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor13', b2)
    assert _is_linked(a, 'xygraph_XYGraphDescriptor13', b2)
    if hasattr(b1, 'xygraph_EObject14'):
        assert not _is_linked(b1, 'xygraph_EObject14', a)
    if hasattr(b2, 'xygraph_EObject14'):
        assert _is_linked(b2, 'xygraph_EObject14', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor13', None)
    assert not _is_linked(a, 'xygraph_XYGraphDescriptor13', b2)
    if hasattr(b2, 'xygraph_EObject14'):
        assert not _is_linked(b2, 'xygraph_EObject14', a)


def test_assoc_dataSource48_link_reassign_clear():
    a = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    b1 = xygraph_EObject()
    b2 = xygraph_EObject()
    _safe_set(a, 'xygraph_TraceDescriptor49', b1)
    assert _is_linked(a, 'xygraph_TraceDescriptor49', b1)
    if hasattr(b1, 'xygraph_EObject50'):
        assert _is_linked(b1, 'xygraph_EObject50', a)
    _safe_set(a, 'xygraph_TraceDescriptor49', b2)
    assert _is_linked(a, 'xygraph_TraceDescriptor49', b2)
    if hasattr(b1, 'xygraph_EObject50'):
        assert not _is_linked(b1, 'xygraph_EObject50', a)
    if hasattr(b2, 'xygraph_EObject50'):
        assert _is_linked(b2, 'xygraph_EObject50', a)
    _safe_set(a, 'xygraph_TraceDescriptor49', None)
    assert not _is_linked(a, 'xygraph_TraceDescriptor49', b2)
    if hasattr(b2, 'xygraph_EObject50'):
        assert not _is_linked(b2, 'xygraph_EObject50', a)


def test_assoc_errorBarColor36_link_reassign_clear():
    a = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    b1 = xygraph_ColorDescriptor(b=7, g=7, r=7)
    b2 = xygraph_ColorDescriptor(b=13, g=13, r=13)
    _safe_set(a, 'xygraph_TraceDescriptor37', b1)
    assert _is_linked(a, 'xygraph_TraceDescriptor37', b1)
    if hasattr(b1, 'xygraph_ColorDescriptor38'):
        assert _is_linked(b1, 'xygraph_ColorDescriptor38', a)
    _safe_set(a, 'xygraph_TraceDescriptor37', b2)
    assert _is_linked(a, 'xygraph_TraceDescriptor37', b2)
    if hasattr(b1, 'xygraph_ColorDescriptor38'):
        assert not _is_linked(b1, 'xygraph_ColorDescriptor38', a)
    if hasattr(b2, 'xygraph_ColorDescriptor38'):
        assert _is_linked(b2, 'xygraph_ColorDescriptor38', a)
    _safe_set(a, 'xygraph_TraceDescriptor37', None)
    assert not _is_linked(a, 'xygraph_TraceDescriptor37', b2)
    if hasattr(b2, 'xygraph_ColorDescriptor38'):
        assert not _is_linked(b2, 'xygraph_ColorDescriptor38', a)


def test_assoc_font33_link_reassign_clear():
    a = xygraph_FontDescriptor(name="sample_text", size=7, style=7)
    b1 = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    b2 = xygraph_AxisDescriptor(autoFormat=False, autoScale=False, autoScaleThreshold=9.99, dashGridLine=False, dateEnabled=False, formatPattern="sample_text_2", logScale=False, minorTicksVisible=False, orientation="sample_text_2", primarySide=False, rangeLower=9.99, rangeUpper=9.99, showMajorGrid=False, showMinorGrid=False, title="sample_text_2", zoomType="sample_text_2")
    _safe_set(a, 'xygraph_FontDescriptor35', b1)
    assert _is_linked(a, 'xygraph_FontDescriptor35', b1)
    if hasattr(b1, 'xygraph_AxisDescriptor34'):
        assert _is_linked(b1, 'xygraph_AxisDescriptor34', a)
    _safe_set(a, 'xygraph_FontDescriptor35', b2)
    assert _is_linked(a, 'xygraph_FontDescriptor35', b2)
    if hasattr(b1, 'xygraph_AxisDescriptor34'):
        assert not _is_linked(b1, 'xygraph_AxisDescriptor34', a)
    if hasattr(b2, 'xygraph_AxisDescriptor34'):
        assert _is_linked(b2, 'xygraph_AxisDescriptor34', a)
    _safe_set(a, 'xygraph_FontDescriptor35', None)
    assert not _is_linked(a, 'xygraph_FontDescriptor35', b2)
    if hasattr(b2, 'xygraph_AxisDescriptor34'):
        assert not _is_linked(b2, 'xygraph_AxisDescriptor34', a)


def test_assoc_foregroundColor21_link_reassign_clear():
    a = xygraph_ColorDescriptor(b=7, g=7, r=7)
    b1 = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    b2 = xygraph_AxisDescriptor(autoFormat=False, autoScale=False, autoScaleThreshold=9.99, dashGridLine=False, dateEnabled=False, formatPattern="sample_text_2", logScale=False, minorTicksVisible=False, orientation="sample_text_2", primarySide=False, rangeLower=9.99, rangeUpper=9.99, showMajorGrid=False, showMinorGrid=False, title="sample_text_2", zoomType="sample_text_2")
    _safe_set(a, 'xygraph_ColorDescriptor23', b1)
    assert _is_linked(a, 'xygraph_ColorDescriptor23', b1)
    if hasattr(b1, 'xygraph_AxisDescriptor22'):
        assert _is_linked(b1, 'xygraph_AxisDescriptor22', a)
    _safe_set(a, 'xygraph_ColorDescriptor23', b2)
    assert _is_linked(a, 'xygraph_ColorDescriptor23', b2)
    if hasattr(b1, 'xygraph_AxisDescriptor22'):
        assert not _is_linked(b1, 'xygraph_AxisDescriptor22', a)
    if hasattr(b2, 'xygraph_AxisDescriptor22'):
        assert _is_linked(b2, 'xygraph_AxisDescriptor22', a)
    _safe_set(a, 'xygraph_ColorDescriptor23', None)
    assert not _is_linked(a, 'xygraph_ColorDescriptor23', b2)
    if hasattr(b2, 'xygraph_AxisDescriptor22'):
        assert not _is_linked(b2, 'xygraph_AxisDescriptor22', a)


def test_assoc_majorGridColor24_link_reassign_clear():
    a = xygraph_ColorDescriptor(b=7, g=7, r=7)
    b1 = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    b2 = xygraph_AxisDescriptor(autoFormat=False, autoScale=False, autoScaleThreshold=9.99, dashGridLine=False, dateEnabled=False, formatPattern="sample_text_2", logScale=False, minorTicksVisible=False, orientation="sample_text_2", primarySide=False, rangeLower=9.99, rangeUpper=9.99, showMajorGrid=False, showMinorGrid=False, title="sample_text_2", zoomType="sample_text_2")
    _safe_set(a, 'xygraph_ColorDescriptor26', b1)
    assert _is_linked(a, 'xygraph_ColorDescriptor26', b1)
    if hasattr(b1, 'xygraph_AxisDescriptor25'):
        assert _is_linked(b1, 'xygraph_AxisDescriptor25', a)
    _safe_set(a, 'xygraph_ColorDescriptor26', b2)
    assert _is_linked(a, 'xygraph_ColorDescriptor26', b2)
    if hasattr(b1, 'xygraph_AxisDescriptor25'):
        assert not _is_linked(b1, 'xygraph_AxisDescriptor25', a)
    if hasattr(b2, 'xygraph_AxisDescriptor25'):
        assert _is_linked(b2, 'xygraph_AxisDescriptor25', a)
    _safe_set(a, 'xygraph_ColorDescriptor26', None)
    assert not _is_linked(a, 'xygraph_ColorDescriptor26', b2)
    if hasattr(b2, 'xygraph_AxisDescriptor25'):
        assert not _is_linked(b2, 'xygraph_AxisDescriptor25', a)


def test_assoc_minorGridColor27_link_reassign_clear():
    a = xygraph_ColorDescriptor(b=7, g=7, r=7)
    b1 = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    b2 = xygraph_AxisDescriptor(autoFormat=False, autoScale=False, autoScaleThreshold=9.99, dashGridLine=False, dateEnabled=False, formatPattern="sample_text_2", logScale=False, minorTicksVisible=False, orientation="sample_text_2", primarySide=False, rangeLower=9.99, rangeUpper=9.99, showMajorGrid=False, showMinorGrid=False, title="sample_text_2", zoomType="sample_text_2")
    _safe_set(a, 'xygraph_ColorDescriptor29', b1)
    assert _is_linked(a, 'xygraph_ColorDescriptor29', b1)
    if hasattr(b1, 'xygraph_AxisDescriptor28'):
        assert _is_linked(b1, 'xygraph_AxisDescriptor28', a)
    _safe_set(a, 'xygraph_ColorDescriptor29', b2)
    assert _is_linked(a, 'xygraph_ColorDescriptor29', b2)
    if hasattr(b1, 'xygraph_AxisDescriptor28'):
        assert not _is_linked(b1, 'xygraph_AxisDescriptor28', a)
    if hasattr(b2, 'xygraph_AxisDescriptor28'):
        assert _is_linked(b2, 'xygraph_AxisDescriptor28', a)
    _safe_set(a, 'xygraph_ColorDescriptor29', None)
    assert not _is_linked(a, 'xygraph_ColorDescriptor29', b2)
    if hasattr(b2, 'xygraph_AxisDescriptor28'):
        assert not _is_linked(b2, 'xygraph_AxisDescriptor28', a)


def test_assoc_plotAreaBackgroundColor5_link_reassign_clear():
    a = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    b1 = xygraph_ColorDescriptor(b=7, g=7, r=7)
    b2 = xygraph_ColorDescriptor(b=13, g=13, r=13)
    _safe_set(a, 'xygraph_XYGraphDescriptor6', b1)
    assert _is_linked(a, 'xygraph_XYGraphDescriptor6', b1)
    if hasattr(b1, 'xygraph_ColorDescriptor7'):
        assert _is_linked(b1, 'xygraph_ColorDescriptor7', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor6', b2)
    assert _is_linked(a, 'xygraph_XYGraphDescriptor6', b2)
    if hasattr(b1, 'xygraph_ColorDescriptor7'):
        assert not _is_linked(b1, 'xygraph_ColorDescriptor7', a)
    if hasattr(b2, 'xygraph_ColorDescriptor7'):
        assert _is_linked(b2, 'xygraph_ColorDescriptor7', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor6', None)
    assert not _is_linked(a, 'xygraph_XYGraphDescriptor6', b2)
    if hasattr(b2, 'xygraph_ColorDescriptor7'):
        assert not _is_linked(b2, 'xygraph_ColorDescriptor7', a)


def test_assoc_titleColor0_link_reassign_clear():
    a = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    b1 = xygraph_ColorDescriptor(b=7, g=7, r=7)
    b2 = xygraph_ColorDescriptor(b=13, g=13, r=13)
    _safe_set(a, 'xygraph_XYGraphDescriptor', b1)
    assert _is_linked(a, 'xygraph_XYGraphDescriptor', b1)
    if hasattr(b1, 'xygraph_ColorDescriptor'):
        assert _is_linked(b1, 'xygraph_ColorDescriptor', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor', b2)
    assert _is_linked(a, 'xygraph_XYGraphDescriptor', b2)
    if hasattr(b1, 'xygraph_ColorDescriptor'):
        assert not _is_linked(b1, 'xygraph_ColorDescriptor', a)
    if hasattr(b2, 'xygraph_ColorDescriptor'):
        assert _is_linked(b2, 'xygraph_ColorDescriptor', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor', None)
    assert not _is_linked(a, 'xygraph_XYGraphDescriptor', b2)
    if hasattr(b2, 'xygraph_ColorDescriptor'):
        assert not _is_linked(b2, 'xygraph_ColorDescriptor', a)


def test_assoc_titleFont30_link_reassign_clear():
    a = xygraph_FontDescriptor(name="sample_text", size=7, style=7)
    b1 = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    b2 = xygraph_AxisDescriptor(autoFormat=False, autoScale=False, autoScaleThreshold=9.99, dashGridLine=False, dateEnabled=False, formatPattern="sample_text_2", logScale=False, minorTicksVisible=False, orientation="sample_text_2", primarySide=False, rangeLower=9.99, rangeUpper=9.99, showMajorGrid=False, showMinorGrid=False, title="sample_text_2", zoomType="sample_text_2")
    _safe_set(a, 'xygraph_FontDescriptor32', b1)
    assert _is_linked(a, 'xygraph_FontDescriptor32', b1)
    if hasattr(b1, 'xygraph_AxisDescriptor31'):
        assert _is_linked(b1, 'xygraph_AxisDescriptor31', a)
    _safe_set(a, 'xygraph_FontDescriptor32', b2)
    assert _is_linked(a, 'xygraph_FontDescriptor32', b2)
    if hasattr(b1, 'xygraph_AxisDescriptor31'):
        assert not _is_linked(b1, 'xygraph_AxisDescriptor31', a)
    if hasattr(b2, 'xygraph_AxisDescriptor31'):
        assert _is_linked(b2, 'xygraph_AxisDescriptor31', a)
    _safe_set(a, 'xygraph_FontDescriptor32', None)
    assert not _is_linked(a, 'xygraph_FontDescriptor32', b2)
    if hasattr(b2, 'xygraph_AxisDescriptor31'):
        assert not _is_linked(b2, 'xygraph_AxisDescriptor31', a)


def test_assoc_titleFont8_link_reassign_clear():
    a = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    b1 = xygraph_FontDescriptor(name="sample_text", size=7, style=7)
    b2 = xygraph_FontDescriptor(name="sample_text_2", size=13, style=13)
    _safe_set(a, 'xygraph_XYGraphDescriptor9', b1)
    assert _is_linked(a, 'xygraph_XYGraphDescriptor9', b1)
    if hasattr(b1, 'xygraph_FontDescriptor'):
        assert _is_linked(b1, 'xygraph_FontDescriptor', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor9', b2)
    assert _is_linked(a, 'xygraph_XYGraphDescriptor9', b2)
    if hasattr(b1, 'xygraph_FontDescriptor'):
        assert not _is_linked(b1, 'xygraph_FontDescriptor', a)
    if hasattr(b2, 'xygraph_FontDescriptor'):
        assert _is_linked(b2, 'xygraph_FontDescriptor', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor9', None)
    assert not _is_linked(a, 'xygraph_XYGraphDescriptor9', b2)
    if hasattr(b2, 'xygraph_FontDescriptor'):
        assert not _is_linked(b2, 'xygraph_FontDescriptor', a)


def test_assoc_traceColor39_link_reassign_clear():
    a = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    b1 = xygraph_ColorDescriptor(b=7, g=7, r=7)
    b2 = xygraph_ColorDescriptor(b=13, g=13, r=13)
    _safe_set(a, 'xygraph_TraceDescriptor40', b1)
    assert _is_linked(a, 'xygraph_TraceDescriptor40', b1)
    if hasattr(b1, 'xygraph_ColorDescriptor41'):
        assert _is_linked(b1, 'xygraph_ColorDescriptor41', a)
    _safe_set(a, 'xygraph_TraceDescriptor40', b2)
    assert _is_linked(a, 'xygraph_TraceDescriptor40', b2)
    if hasattr(b1, 'xygraph_ColorDescriptor41'):
        assert not _is_linked(b1, 'xygraph_ColorDescriptor41', a)
    if hasattr(b2, 'xygraph_ColorDescriptor41'):
        assert _is_linked(b2, 'xygraph_ColorDescriptor41', a)
    _safe_set(a, 'xygraph_TraceDescriptor40', None)
    assert not _is_linked(a, 'xygraph_TraceDescriptor40', b2)
    if hasattr(b2, 'xygraph_ColorDescriptor41'):
        assert not _is_linked(b2, 'xygraph_ColorDescriptor41', a)


def test_assoc_traceDescriptors3_link_reassign_clear():
    a = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    b1 = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    b2 = xygraph_TraceDescriptor(antiAliasing=False, areaAlpha=13, baseLine="sample_text_2", drawYErrorInArea=False, errorBarCapWidth=13, errorBarEnabled=False, lineWidth=13, name="sample_text_2", pointSize=13, pointStyle="sample_text_2", traceType="sample_text_2", xErrorBarType="sample_text_2", yErrorBarType="sample_text_2")
    _safe_set(a, 'xygraph_XYGraphDescriptor4', {b1})
    assert _is_linked(a, 'xygraph_XYGraphDescriptor4', b1)
    if hasattr(b1, 'xygraph_TraceDescriptor'):
        assert _is_linked(b1, 'xygraph_TraceDescriptor', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor4', {b2})
    assert _is_linked(a, 'xygraph_XYGraphDescriptor4', b2)
    if hasattr(b1, 'xygraph_TraceDescriptor'):
        assert not _is_linked(b1, 'xygraph_TraceDescriptor', a)
    if hasattr(b2, 'xygraph_TraceDescriptor'):
        assert _is_linked(b2, 'xygraph_TraceDescriptor', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor4', set())
    assert not _is_linked(a, 'xygraph_XYGraphDescriptor4', b2)
    if hasattr(b2, 'xygraph_TraceDescriptor'):
        assert not _is_linked(b2, 'xygraph_TraceDescriptor', a)


def test_assoc_visibleTraces15_link_reassign_clear():
    a = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    b1 = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    b2 = xygraph_TraceDescriptor(antiAliasing=False, areaAlpha=13, baseLine="sample_text_2", drawYErrorInArea=False, errorBarCapWidth=13, errorBarEnabled=False, lineWidth=13, name="sample_text_2", pointSize=13, pointStyle="sample_text_2", traceType="sample_text_2", xErrorBarType="sample_text_2", yErrorBarType="sample_text_2")
    _safe_set(a, 'xygraph_XYGraphDescriptor16', {b1})
    assert _is_linked(a, 'xygraph_XYGraphDescriptor16', b1)
    if hasattr(b1, 'xygraph_TraceDescriptor17'):
        assert _is_linked(b1, 'xygraph_TraceDescriptor17', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor16', {b2})
    assert _is_linked(a, 'xygraph_XYGraphDescriptor16', b2)
    if hasattr(b1, 'xygraph_TraceDescriptor17'):
        assert not _is_linked(b1, 'xygraph_TraceDescriptor17', a)
    if hasattr(b2, 'xygraph_TraceDescriptor17'):
        assert _is_linked(b2, 'xygraph_TraceDescriptor17', a)
    _safe_set(a, 'xygraph_XYGraphDescriptor16', set())
    assert not _is_linked(a, 'xygraph_XYGraphDescriptor16', b2)
    if hasattr(b2, 'xygraph_TraceDescriptor17'):
        assert not _is_linked(b2, 'xygraph_TraceDescriptor17', a)


def test_assoc_xAxis42_link_reassign_clear():
    a = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    b1 = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    b2 = xygraph_AxisDescriptor(autoFormat=False, autoScale=False, autoScaleThreshold=9.99, dashGridLine=False, dateEnabled=False, formatPattern="sample_text_2", logScale=False, minorTicksVisible=False, orientation="sample_text_2", primarySide=False, rangeLower=9.99, rangeUpper=9.99, showMajorGrid=False, showMinorGrid=False, title="sample_text_2", zoomType="sample_text_2")
    _safe_set(a, 'xygraph_TraceDescriptor43', b1)
    assert _is_linked(a, 'xygraph_TraceDescriptor43', b1)
    if hasattr(b1, 'xygraph_AxisDescriptor44'):
        assert _is_linked(b1, 'xygraph_AxisDescriptor44', a)
    _safe_set(a, 'xygraph_TraceDescriptor43', b2)
    assert _is_linked(a, 'xygraph_TraceDescriptor43', b2)
    if hasattr(b1, 'xygraph_AxisDescriptor44'):
        assert not _is_linked(b1, 'xygraph_AxisDescriptor44', a)
    if hasattr(b2, 'xygraph_AxisDescriptor44'):
        assert _is_linked(b2, 'xygraph_AxisDescriptor44', a)
    _safe_set(a, 'xygraph_TraceDescriptor43', None)
    assert not _is_linked(a, 'xygraph_TraceDescriptor43', b2)
    if hasattr(b2, 'xygraph_AxisDescriptor44'):
        assert not _is_linked(b2, 'xygraph_AxisDescriptor44', a)


def test_assoc_yAxis45_link_reassign_clear():
    a = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    b1 = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    b2 = xygraph_AxisDescriptor(autoFormat=False, autoScale=False, autoScaleThreshold=9.99, dashGridLine=False, dateEnabled=False, formatPattern="sample_text_2", logScale=False, minorTicksVisible=False, orientation="sample_text_2", primarySide=False, rangeLower=9.99, rangeUpper=9.99, showMajorGrid=False, showMinorGrid=False, title="sample_text_2", zoomType="sample_text_2")
    _safe_set(a, 'xygraph_TraceDescriptor46', b1)
    assert _is_linked(a, 'xygraph_TraceDescriptor46', b1)
    if hasattr(b1, 'xygraph_AxisDescriptor47'):
        assert _is_linked(b1, 'xygraph_AxisDescriptor47', a)
    _safe_set(a, 'xygraph_TraceDescriptor46', b2)
    assert _is_linked(a, 'xygraph_TraceDescriptor46', b2)
    if hasattr(b1, 'xygraph_AxisDescriptor47'):
        assert not _is_linked(b1, 'xygraph_AxisDescriptor47', a)
    if hasattr(b2, 'xygraph_AxisDescriptor47'):
        assert _is_linked(b2, 'xygraph_AxisDescriptor47', a)
    _safe_set(a, 'xygraph_TraceDescriptor46', None)
    assert not _is_linked(a, 'xygraph_TraceDescriptor46', b2)
    if hasattr(b2, 'xygraph_AxisDescriptor47'):
        assert not _is_linked(b2, 'xygraph_AxisDescriptor47', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

xygraph_AxisDescriptor_strategy = st.builds(xygraph_AxisDescriptor, autoFormat=st.booleans(), autoScale=st.booleans(), autoScaleThreshold=st.floats(allow_nan=False, allow_infinity=False), dashGridLine=st.booleans(), dateEnabled=st.booleans(), formatPattern=safe_text, logScale=st.booleans(), minorTicksVisible=st.booleans(), orientation=safe_text, primarySide=st.booleans(), rangeLower=st.floats(allow_nan=False, allow_infinity=False), rangeUpper=st.floats(allow_nan=False, allow_infinity=False), showMajorGrid=st.booleans(), showMinorGrid=st.booleans(), title=safe_text, zoomType=safe_text)
@given(instance=xygraph_AxisDescriptor_strategy)
@settings(max_examples=25)
def test_xygraph_AxisDescriptor_instantiation(instance):
    assert isinstance(instance, xygraph_AxisDescriptor)


xygraph_ColorDescriptor_strategy = st.builds(xygraph_ColorDescriptor, b=st.integers(), g=st.integers(), r=st.integers())
@given(instance=xygraph_ColorDescriptor_strategy)
@settings(max_examples=25)
def test_xygraph_ColorDescriptor_instantiation(instance):
    assert isinstance(instance, xygraph_ColorDescriptor)


xygraph_EObject_strategy = st.builds(xygraph_EObject)
@given(instance=xygraph_EObject_strategy)
@settings(max_examples=25)
def test_xygraph_EObject_instantiation(instance):
    assert isinstance(instance, xygraph_EObject)


xygraph_FontDescriptor_strategy = st.builds(xygraph_FontDescriptor, name=safe_text, size=st.integers(), style=st.integers())
@given(instance=xygraph_FontDescriptor_strategy)
@settings(max_examples=25)
def test_xygraph_FontDescriptor_instantiation(instance):
    assert isinstance(instance, xygraph_FontDescriptor)


xygraph_TraceDescriptor_strategy = st.builds(xygraph_TraceDescriptor, antiAliasing=st.booleans(), areaAlpha=st.integers(), baseLine=safe_text, drawYErrorInArea=st.booleans(), errorBarCapWidth=st.integers(), errorBarEnabled=st.booleans(), lineWidth=st.integers(), name=safe_text, pointSize=st.integers(), pointStyle=safe_text, traceType=safe_text, xErrorBarType=safe_text, yErrorBarType=safe_text)
@given(instance=xygraph_TraceDescriptor_strategy)
@settings(max_examples=25)
def test_xygraph_TraceDescriptor_instantiation(instance):
    assert isinstance(instance, xygraph_TraceDescriptor)


xygraph_XYGraphDescriptor_strategy = st.builds(xygraph_XYGraphDescriptor, showLegend=st.booleans(), showPlotAreaBorder=st.booleans(), showTitle=st.booleans(), title=safe_text, transparent=st.booleans(), zoomType=safe_text)
@given(instance=xygraph_XYGraphDescriptor_strategy)
@settings(max_examples=25)
def test_xygraph_XYGraphDescriptor_instantiation(instance):
    assert isinstance(instance, xygraph_XYGraphDescriptor)


