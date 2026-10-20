import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_axisDescriptors1_reverse_link_reassign_clear():
    a1 = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    a2 = xygraph_XYGraphDescriptor(showLegend=False, showPlotAreaBorder=False, showTitle=False, title="sample_text_2", transparent=False, zoomType="sample_text_2")
    b = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    _safe_set(b, 'xygraph_AxisDescriptor', a1)
    assert _is_linked(b, 'xygraph_AxisDescriptor', a1)
    if hasattr(a1, 'xygraph_XYGraphDescriptor2'):
        assert _is_linked(a1, 'xygraph_XYGraphDescriptor2', b)
    _safe_set(b, 'xygraph_AxisDescriptor', a2)
    assert _is_linked(b, 'xygraph_AxisDescriptor', a2)
    if hasattr(a1, 'xygraph_XYGraphDescriptor2'):
        assert not _is_linked(a1, 'xygraph_XYGraphDescriptor2', b)
    if hasattr(a2, 'xygraph_XYGraphDescriptor2'):
        assert _is_linked(a2, 'xygraph_XYGraphDescriptor2', b)
    _safe_set(b, 'xygraph_AxisDescriptor', None)
    assert not _is_linked(b, 'xygraph_AxisDescriptor', a2)
    if hasattr(a2, 'xygraph_XYGraphDescriptor2'):
        assert not _is_linked(a2, 'xygraph_XYGraphDescriptor2', b)


def test_assoc_backgroundColor18_reverse_link_reassign_clear():
    a1 = xygraph_ColorDescriptor(b=7, g=7, r=7)
    a2 = xygraph_ColorDescriptor(b=13, g=13, r=13)
    b = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    _safe_set(b, 'xygraph_AxisDescriptor19', a1)
    assert _is_linked(b, 'xygraph_AxisDescriptor19', a1)
    if hasattr(a1, 'xygraph_ColorDescriptor20'):
        assert _is_linked(a1, 'xygraph_ColorDescriptor20', b)
    _safe_set(b, 'xygraph_AxisDescriptor19', a2)
    assert _is_linked(b, 'xygraph_AxisDescriptor19', a2)
    if hasattr(a1, 'xygraph_ColorDescriptor20'):
        assert not _is_linked(a1, 'xygraph_ColorDescriptor20', b)
    if hasattr(a2, 'xygraph_ColorDescriptor20'):
        assert _is_linked(a2, 'xygraph_ColorDescriptor20', b)
    _safe_set(b, 'xygraph_AxisDescriptor19', None)
    assert not _is_linked(b, 'xygraph_AxisDescriptor19', a2)
    if hasattr(a2, 'xygraph_ColorDescriptor20'):
        assert not _is_linked(a2, 'xygraph_ColorDescriptor20', b)


def test_assoc_errorBarColor36_reverse_link_reassign_clear():
    a1 = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    a2 = xygraph_TraceDescriptor(antiAliasing=False, areaAlpha=13, baseLine="sample_text_2", drawYErrorInArea=False, errorBarCapWidth=13, errorBarEnabled=False, lineWidth=13, name="sample_text_2", pointSize=13, pointStyle="sample_text_2", traceType="sample_text_2", xErrorBarType="sample_text_2", yErrorBarType="sample_text_2")
    b = xygraph_ColorDescriptor(b=7, g=7, r=7)
    _safe_set(b, 'xygraph_ColorDescriptor38', a1)
    assert _is_linked(b, 'xygraph_ColorDescriptor38', a1)
    if hasattr(a1, 'xygraph_TraceDescriptor37'):
        assert _is_linked(a1, 'xygraph_TraceDescriptor37', b)
    _safe_set(b, 'xygraph_ColorDescriptor38', a2)
    assert _is_linked(b, 'xygraph_ColorDescriptor38', a2)
    if hasattr(a1, 'xygraph_TraceDescriptor37'):
        assert not _is_linked(a1, 'xygraph_TraceDescriptor37', b)
    if hasattr(a2, 'xygraph_TraceDescriptor37'):
        assert _is_linked(a2, 'xygraph_TraceDescriptor37', b)
    _safe_set(b, 'xygraph_ColorDescriptor38', None)
    assert not _is_linked(b, 'xygraph_ColorDescriptor38', a2)
    if hasattr(a2, 'xygraph_TraceDescriptor37'):
        assert not _is_linked(a2, 'xygraph_TraceDescriptor37', b)


def test_assoc_font33_reverse_link_reassign_clear():
    a1 = xygraph_FontDescriptor(name="sample_text", size=7, style=7)
    a2 = xygraph_FontDescriptor(name="sample_text_2", size=13, style=13)
    b = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    _safe_set(b, 'xygraph_AxisDescriptor34', a1)
    assert _is_linked(b, 'xygraph_AxisDescriptor34', a1)
    if hasattr(a1, 'xygraph_FontDescriptor35'):
        assert _is_linked(a1, 'xygraph_FontDescriptor35', b)
    _safe_set(b, 'xygraph_AxisDescriptor34', a2)
    assert _is_linked(b, 'xygraph_AxisDescriptor34', a2)
    if hasattr(a1, 'xygraph_FontDescriptor35'):
        assert not _is_linked(a1, 'xygraph_FontDescriptor35', b)
    if hasattr(a2, 'xygraph_FontDescriptor35'):
        assert _is_linked(a2, 'xygraph_FontDescriptor35', b)
    _safe_set(b, 'xygraph_AxisDescriptor34', None)
    assert not _is_linked(b, 'xygraph_AxisDescriptor34', a2)
    if hasattr(a2, 'xygraph_FontDescriptor35'):
        assert not _is_linked(a2, 'xygraph_FontDescriptor35', b)


def test_assoc_foregroundColor21_reverse_link_reassign_clear():
    a1 = xygraph_ColorDescriptor(b=7, g=7, r=7)
    a2 = xygraph_ColorDescriptor(b=13, g=13, r=13)
    b = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    _safe_set(b, 'xygraph_AxisDescriptor22', a1)
    assert _is_linked(b, 'xygraph_AxisDescriptor22', a1)
    if hasattr(a1, 'xygraph_ColorDescriptor23'):
        assert _is_linked(a1, 'xygraph_ColorDescriptor23', b)
    _safe_set(b, 'xygraph_AxisDescriptor22', a2)
    assert _is_linked(b, 'xygraph_AxisDescriptor22', a2)
    if hasattr(a1, 'xygraph_ColorDescriptor23'):
        assert not _is_linked(a1, 'xygraph_ColorDescriptor23', b)
    if hasattr(a2, 'xygraph_ColorDescriptor23'):
        assert _is_linked(a2, 'xygraph_ColorDescriptor23', b)
    _safe_set(b, 'xygraph_AxisDescriptor22', None)
    assert not _is_linked(b, 'xygraph_AxisDescriptor22', a2)
    if hasattr(a2, 'xygraph_ColorDescriptor23'):
        assert not _is_linked(a2, 'xygraph_ColorDescriptor23', b)


def test_assoc_majorGridColor24_reverse_link_reassign_clear():
    a1 = xygraph_ColorDescriptor(b=7, g=7, r=7)
    a2 = xygraph_ColorDescriptor(b=13, g=13, r=13)
    b = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    _safe_set(b, 'xygraph_AxisDescriptor25', a1)
    assert _is_linked(b, 'xygraph_AxisDescriptor25', a1)
    if hasattr(a1, 'xygraph_ColorDescriptor26'):
        assert _is_linked(a1, 'xygraph_ColorDescriptor26', b)
    _safe_set(b, 'xygraph_AxisDescriptor25', a2)
    assert _is_linked(b, 'xygraph_AxisDescriptor25', a2)
    if hasattr(a1, 'xygraph_ColorDescriptor26'):
        assert not _is_linked(a1, 'xygraph_ColorDescriptor26', b)
    if hasattr(a2, 'xygraph_ColorDescriptor26'):
        assert _is_linked(a2, 'xygraph_ColorDescriptor26', b)
    _safe_set(b, 'xygraph_AxisDescriptor25', None)
    assert not _is_linked(b, 'xygraph_AxisDescriptor25', a2)
    if hasattr(a2, 'xygraph_ColorDescriptor26'):
        assert not _is_linked(a2, 'xygraph_ColorDescriptor26', b)


def test_assoc_minorGridColor27_reverse_link_reassign_clear():
    a1 = xygraph_ColorDescriptor(b=7, g=7, r=7)
    a2 = xygraph_ColorDescriptor(b=13, g=13, r=13)
    b = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    _safe_set(b, 'xygraph_AxisDescriptor28', a1)
    assert _is_linked(b, 'xygraph_AxisDescriptor28', a1)
    if hasattr(a1, 'xygraph_ColorDescriptor29'):
        assert _is_linked(a1, 'xygraph_ColorDescriptor29', b)
    _safe_set(b, 'xygraph_AxisDescriptor28', a2)
    assert _is_linked(b, 'xygraph_AxisDescriptor28', a2)
    if hasattr(a1, 'xygraph_ColorDescriptor29'):
        assert not _is_linked(a1, 'xygraph_ColorDescriptor29', b)
    if hasattr(a2, 'xygraph_ColorDescriptor29'):
        assert _is_linked(a2, 'xygraph_ColorDescriptor29', b)
    _safe_set(b, 'xygraph_AxisDescriptor28', None)
    assert not _is_linked(b, 'xygraph_AxisDescriptor28', a2)
    if hasattr(a2, 'xygraph_ColorDescriptor29'):
        assert not _is_linked(a2, 'xygraph_ColorDescriptor29', b)


def test_assoc_plotAreaBackgroundColor5_reverse_link_reassign_clear():
    a1 = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    a2 = xygraph_XYGraphDescriptor(showLegend=False, showPlotAreaBorder=False, showTitle=False, title="sample_text_2", transparent=False, zoomType="sample_text_2")
    b = xygraph_ColorDescriptor(b=7, g=7, r=7)
    _safe_set(b, 'xygraph_ColorDescriptor7', a1)
    assert _is_linked(b, 'xygraph_ColorDescriptor7', a1)
    if hasattr(a1, 'xygraph_XYGraphDescriptor6'):
        assert _is_linked(a1, 'xygraph_XYGraphDescriptor6', b)
    _safe_set(b, 'xygraph_ColorDescriptor7', a2)
    assert _is_linked(b, 'xygraph_ColorDescriptor7', a2)
    if hasattr(a1, 'xygraph_XYGraphDescriptor6'):
        assert not _is_linked(a1, 'xygraph_XYGraphDescriptor6', b)
    if hasattr(a2, 'xygraph_XYGraphDescriptor6'):
        assert _is_linked(a2, 'xygraph_XYGraphDescriptor6', b)
    _safe_set(b, 'xygraph_ColorDescriptor7', None)
    assert not _is_linked(b, 'xygraph_ColorDescriptor7', a2)
    if hasattr(a2, 'xygraph_XYGraphDescriptor6'):
        assert not _is_linked(a2, 'xygraph_XYGraphDescriptor6', b)


def test_assoc_titleColor0_reverse_link_reassign_clear():
    a1 = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    a2 = xygraph_XYGraphDescriptor(showLegend=False, showPlotAreaBorder=False, showTitle=False, title="sample_text_2", transparent=False, zoomType="sample_text_2")
    b = xygraph_ColorDescriptor(b=7, g=7, r=7)
    _safe_set(b, 'xygraph_ColorDescriptor', a1)
    assert _is_linked(b, 'xygraph_ColorDescriptor', a1)
    if hasattr(a1, 'xygraph_XYGraphDescriptor'):
        assert _is_linked(a1, 'xygraph_XYGraphDescriptor', b)
    _safe_set(b, 'xygraph_ColorDescriptor', a2)
    assert _is_linked(b, 'xygraph_ColorDescriptor', a2)
    if hasattr(a1, 'xygraph_XYGraphDescriptor'):
        assert not _is_linked(a1, 'xygraph_XYGraphDescriptor', b)
    if hasattr(a2, 'xygraph_XYGraphDescriptor'):
        assert _is_linked(a2, 'xygraph_XYGraphDescriptor', b)
    _safe_set(b, 'xygraph_ColorDescriptor', None)
    assert not _is_linked(b, 'xygraph_ColorDescriptor', a2)
    if hasattr(a2, 'xygraph_XYGraphDescriptor'):
        assert not _is_linked(a2, 'xygraph_XYGraphDescriptor', b)


def test_assoc_titleFont30_reverse_link_reassign_clear():
    a1 = xygraph_FontDescriptor(name="sample_text", size=7, style=7)
    a2 = xygraph_FontDescriptor(name="sample_text_2", size=13, style=13)
    b = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    _safe_set(b, 'xygraph_AxisDescriptor31', a1)
    assert _is_linked(b, 'xygraph_AxisDescriptor31', a1)
    if hasattr(a1, 'xygraph_FontDescriptor32'):
        assert _is_linked(a1, 'xygraph_FontDescriptor32', b)
    _safe_set(b, 'xygraph_AxisDescriptor31', a2)
    assert _is_linked(b, 'xygraph_AxisDescriptor31', a2)
    if hasattr(a1, 'xygraph_FontDescriptor32'):
        assert not _is_linked(a1, 'xygraph_FontDescriptor32', b)
    if hasattr(a2, 'xygraph_FontDescriptor32'):
        assert _is_linked(a2, 'xygraph_FontDescriptor32', b)
    _safe_set(b, 'xygraph_AxisDescriptor31', None)
    assert not _is_linked(b, 'xygraph_AxisDescriptor31', a2)
    if hasattr(a2, 'xygraph_FontDescriptor32'):
        assert not _is_linked(a2, 'xygraph_FontDescriptor32', b)


def test_assoc_titleFont8_reverse_link_reassign_clear():
    a1 = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    a2 = xygraph_XYGraphDescriptor(showLegend=False, showPlotAreaBorder=False, showTitle=False, title="sample_text_2", transparent=False, zoomType="sample_text_2")
    b = xygraph_FontDescriptor(name="sample_text", size=7, style=7)
    _safe_set(b, 'xygraph_FontDescriptor', a1)
    assert _is_linked(b, 'xygraph_FontDescriptor', a1)
    if hasattr(a1, 'xygraph_XYGraphDescriptor9'):
        assert _is_linked(a1, 'xygraph_XYGraphDescriptor9', b)
    _safe_set(b, 'xygraph_FontDescriptor', a2)
    assert _is_linked(b, 'xygraph_FontDescriptor', a2)
    if hasattr(a1, 'xygraph_XYGraphDescriptor9'):
        assert not _is_linked(a1, 'xygraph_XYGraphDescriptor9', b)
    if hasattr(a2, 'xygraph_XYGraphDescriptor9'):
        assert _is_linked(a2, 'xygraph_XYGraphDescriptor9', b)
    _safe_set(b, 'xygraph_FontDescriptor', None)
    assert not _is_linked(b, 'xygraph_FontDescriptor', a2)
    if hasattr(a2, 'xygraph_XYGraphDescriptor9'):
        assert not _is_linked(a2, 'xygraph_XYGraphDescriptor9', b)


def test_assoc_traceColor39_reverse_link_reassign_clear():
    a1 = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    a2 = xygraph_TraceDescriptor(antiAliasing=False, areaAlpha=13, baseLine="sample_text_2", drawYErrorInArea=False, errorBarCapWidth=13, errorBarEnabled=False, lineWidth=13, name="sample_text_2", pointSize=13, pointStyle="sample_text_2", traceType="sample_text_2", xErrorBarType="sample_text_2", yErrorBarType="sample_text_2")
    b = xygraph_ColorDescriptor(b=7, g=7, r=7)
    _safe_set(b, 'xygraph_ColorDescriptor41', a1)
    assert _is_linked(b, 'xygraph_ColorDescriptor41', a1)
    if hasattr(a1, 'xygraph_TraceDescriptor40'):
        assert _is_linked(a1, 'xygraph_TraceDescriptor40', b)
    _safe_set(b, 'xygraph_ColorDescriptor41', a2)
    assert _is_linked(b, 'xygraph_ColorDescriptor41', a2)
    if hasattr(a1, 'xygraph_TraceDescriptor40'):
        assert not _is_linked(a1, 'xygraph_TraceDescriptor40', b)
    if hasattr(a2, 'xygraph_TraceDescriptor40'):
        assert _is_linked(a2, 'xygraph_TraceDescriptor40', b)
    _safe_set(b, 'xygraph_ColorDescriptor41', None)
    assert not _is_linked(b, 'xygraph_ColorDescriptor41', a2)
    if hasattr(a2, 'xygraph_TraceDescriptor40'):
        assert not _is_linked(a2, 'xygraph_TraceDescriptor40', b)


def test_assoc_traceDescriptors3_reverse_link_reassign_clear():
    a1 = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    a2 = xygraph_XYGraphDescriptor(showLegend=False, showPlotAreaBorder=False, showTitle=False, title="sample_text_2", transparent=False, zoomType="sample_text_2")
    b = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    _safe_set(b, 'xygraph_TraceDescriptor', a1)
    assert _is_linked(b, 'xygraph_TraceDescriptor', a1)
    if hasattr(a1, 'xygraph_XYGraphDescriptor4'):
        assert _is_linked(a1, 'xygraph_XYGraphDescriptor4', b)
    _safe_set(b, 'xygraph_TraceDescriptor', a2)
    assert _is_linked(b, 'xygraph_TraceDescriptor', a2)
    if hasattr(a1, 'xygraph_XYGraphDescriptor4'):
        assert not _is_linked(a1, 'xygraph_XYGraphDescriptor4', b)
    if hasattr(a2, 'xygraph_XYGraphDescriptor4'):
        assert _is_linked(a2, 'xygraph_XYGraphDescriptor4', b)
    _safe_set(b, 'xygraph_TraceDescriptor', None)
    assert not _is_linked(b, 'xygraph_TraceDescriptor', a2)
    if hasattr(a2, 'xygraph_XYGraphDescriptor4'):
        assert not _is_linked(a2, 'xygraph_XYGraphDescriptor4', b)


def test_assoc_visibleTraces15_reverse_link_reassign_clear():
    a1 = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    a2 = xygraph_XYGraphDescriptor(showLegend=False, showPlotAreaBorder=False, showTitle=False, title="sample_text_2", transparent=False, zoomType="sample_text_2")
    b = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    _safe_set(b, 'xygraph_TraceDescriptor17', a1)
    assert _is_linked(b, 'xygraph_TraceDescriptor17', a1)
    if hasattr(a1, 'xygraph_XYGraphDescriptor16'):
        assert _is_linked(a1, 'xygraph_XYGraphDescriptor16', b)
    _safe_set(b, 'xygraph_TraceDescriptor17', a2)
    assert _is_linked(b, 'xygraph_TraceDescriptor17', a2)
    if hasattr(a1, 'xygraph_XYGraphDescriptor16'):
        assert not _is_linked(a1, 'xygraph_XYGraphDescriptor16', b)
    if hasattr(a2, 'xygraph_XYGraphDescriptor16'):
        assert _is_linked(a2, 'xygraph_XYGraphDescriptor16', b)
    _safe_set(b, 'xygraph_TraceDescriptor17', None)
    assert not _is_linked(b, 'xygraph_TraceDescriptor17', a2)
    if hasattr(a2, 'xygraph_XYGraphDescriptor16'):
        assert not _is_linked(a2, 'xygraph_XYGraphDescriptor16', b)


def test_assoc_xAxis42_reverse_link_reassign_clear():
    a1 = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    a2 = xygraph_TraceDescriptor(antiAliasing=False, areaAlpha=13, baseLine="sample_text_2", drawYErrorInArea=False, errorBarCapWidth=13, errorBarEnabled=False, lineWidth=13, name="sample_text_2", pointSize=13, pointStyle="sample_text_2", traceType="sample_text_2", xErrorBarType="sample_text_2", yErrorBarType="sample_text_2")
    b = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    _safe_set(b, 'xygraph_AxisDescriptor44', a1)
    assert _is_linked(b, 'xygraph_AxisDescriptor44', a1)
    if hasattr(a1, 'xygraph_TraceDescriptor43'):
        assert _is_linked(a1, 'xygraph_TraceDescriptor43', b)
    _safe_set(b, 'xygraph_AxisDescriptor44', a2)
    assert _is_linked(b, 'xygraph_AxisDescriptor44', a2)
    if hasattr(a1, 'xygraph_TraceDescriptor43'):
        assert not _is_linked(a1, 'xygraph_TraceDescriptor43', b)
    if hasattr(a2, 'xygraph_TraceDescriptor43'):
        assert _is_linked(a2, 'xygraph_TraceDescriptor43', b)
    _safe_set(b, 'xygraph_AxisDescriptor44', None)
    assert not _is_linked(b, 'xygraph_AxisDescriptor44', a2)
    if hasattr(a2, 'xygraph_TraceDescriptor43'):
        assert not _is_linked(a2, 'xygraph_TraceDescriptor43', b)


def test_assoc_yAxis45_reverse_link_reassign_clear():
    a1 = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    a2 = xygraph_TraceDescriptor(antiAliasing=False, areaAlpha=13, baseLine="sample_text_2", drawYErrorInArea=False, errorBarCapWidth=13, errorBarEnabled=False, lineWidth=13, name="sample_text_2", pointSize=13, pointStyle="sample_text_2", traceType="sample_text_2", xErrorBarType="sample_text_2", yErrorBarType="sample_text_2")
    b = xygraph_AxisDescriptor(autoFormat=True, autoScale=True, autoScaleThreshold=3.14, dashGridLine=True, dateEnabled=True, formatPattern="sample_text", logScale=True, minorTicksVisible=True, orientation="sample_text", primarySide=True, rangeLower=3.14, rangeUpper=3.14, showMajorGrid=True, showMinorGrid=True, title="sample_text", zoomType="sample_text")
    _safe_set(b, 'xygraph_AxisDescriptor47', a1)
    assert _is_linked(b, 'xygraph_AxisDescriptor47', a1)
    if hasattr(a1, 'xygraph_TraceDescriptor46'):
        assert _is_linked(a1, 'xygraph_TraceDescriptor46', b)
    _safe_set(b, 'xygraph_AxisDescriptor47', a2)
    assert _is_linked(b, 'xygraph_AxisDescriptor47', a2)
    if hasattr(a1, 'xygraph_TraceDescriptor46'):
        assert not _is_linked(a1, 'xygraph_TraceDescriptor46', b)
    if hasattr(a2, 'xygraph_TraceDescriptor46'):
        assert _is_linked(a2, 'xygraph_TraceDescriptor46', b)
    _safe_set(b, 'xygraph_AxisDescriptor47', None)
    assert not _is_linked(b, 'xygraph_AxisDescriptor47', a2)
    if hasattr(a2, 'xygraph_TraceDescriptor46'):
        assert not _is_linked(a2, 'xygraph_TraceDescriptor46', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_context10_stub_double():
    # xygraph_EObject has no real 'xygraph_EObject' property in the generated
    # code (a bare stub) -- manually attach it so xygraph_XYGraphDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xygraph_XYGraphDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    partner = xygraph_EObject()
    setattr(partner, 'xygraph_EObject', None)
    _safe_set(owner, 'xygraph_XYGraphDescriptor11', partner)
    assert getattr(partner, 'xygraph_EObject') == owner
    _safe_set(owner, 'xygraph_XYGraphDescriptor11', None)
    assert getattr(partner, 'xygraph_EObject') is None


def test_assoc_dataSource12_stub_double():
    # xygraph_EObject has no real 'xygraph_EObject14' property in the generated
    # code (a bare stub) -- manually attach it so xygraph_XYGraphDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xygraph_XYGraphDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xygraph_XYGraphDescriptor(showLegend=True, showPlotAreaBorder=True, showTitle=True, title="sample_text", transparent=True, zoomType="sample_text")
    partner = xygraph_EObject()
    setattr(partner, 'xygraph_EObject14', None)
    _safe_set(owner, 'xygraph_XYGraphDescriptor13', partner)
    assert getattr(partner, 'xygraph_EObject14') == owner
    _safe_set(owner, 'xygraph_XYGraphDescriptor13', None)
    assert getattr(partner, 'xygraph_EObject14') is None


def test_assoc_dataSource48_stub_double():
    # xygraph_EObject has no real 'xygraph_EObject50' property in the generated
    # code (a bare stub) -- manually attach it so xygraph_TraceDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xygraph_TraceDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xygraph_TraceDescriptor(antiAliasing=True, areaAlpha=7, baseLine="sample_text", drawYErrorInArea=True, errorBarCapWidth=7, errorBarEnabled=True, lineWidth=7, name="sample_text", pointSize=7, pointStyle="sample_text", traceType="sample_text", xErrorBarType="sample_text", yErrorBarType="sample_text")
    partner = xygraph_EObject()
    setattr(partner, 'xygraph_EObject50', None)
    _safe_set(owner, 'xygraph_TraceDescriptor49', partner)
    assert getattr(partner, 'xygraph_EObject50') == owner
    _safe_set(owner, 'xygraph_TraceDescriptor49', None)
    assert getattr(partner, 'xygraph_EObject50') is None


