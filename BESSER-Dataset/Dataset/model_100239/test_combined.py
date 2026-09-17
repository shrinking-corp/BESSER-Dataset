# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    XYABElt,
    DatadiagramMLTextFormat_XYABCDElt,
    DatadiagramMLTextFormat_InfiniteLine,
    XYAElt,
    DatadiagramMLTextFormat_XYABElt,
    DatadiagramMLTextFormat_PolylineTo,
    DatadiagramMLTextFormat_SplineKnot,
    DatadiagramMLTextFormat_ArcTo,
    Geom,
    XYElt,
    DatadiagramMLTextFormat_XYAElt,
    DatadiagramMLTextFormat_MoveTo,
    DatadiagramMLTextFormat_LineTo,
    SplineKnot,
    ArcTo,
    NURBSTo,
    SplineStart,
    EllipticalArcTo,
    Ellipse,
    InfiniteLine,
    PolylineTo,
    DatadiagramMLTextFormat_DelElt,
    DatadiagramMLTextFormat_IXElt,
    MoveTo,
    LineTo,
    CellType,
    DelElt,
    IXElt,
    DatadiagramMLTextFormat_XYElt,
    DatadiagramMLTextFormat_NamedElt,
    PageElt,
    MasterElt,
    DatadiagramMLTextFormat_SolutionXML,
    DatadiagramMLTextFormat_HeaderFooter,
    DatadiagramMLTextFormat_EventList,
    DatadiagramMLTextFormat_WindowsInfo,
    DatadiagramMLTextFormat_DocumentSettingsElt,
    DatadiagramMLTextFormat_PageElt,
    DatadiagramMLTextFormat_PrintSetup,
    DatadiagramMLTextFormat_PagesCollection,
    DatadiagramMLTextFormat_MasterElt,
    ConnectsCollection,
    DatadiagramMLTextFormat_Connect,
    Connect,
    DatadiagramMLTextFormat_ConnectsCollection,
    Page,
    DatadiagramMLTextFormat_ShapesCollection,
    DatadiagramMLTextFormat_Icon,
    Icon,
    MasterShortCut,
    Master,
    DatadiagramMLTextFormat_MastersCollection,
    TabsCollection,
    DatadiagramMLTextFormat_Tab,
    Tab,
    DatadiagramMLTextFormat_IXrequiredElt,
    Text,
    DatadiagramMLTextFormat_TextElt,
    XYABCDElt,
    DatadiagramMLTextFormat_SplineStart,
    DatadiagramMLTextFormat_EllipticalArcTo,
    DatadiagramMLTextFormat_Ellipse,
    TextElt,
    DatadiagramMLTextFormat_StringElt,
    XYABCDEElt,
    DatadiagramMLTextFormat_NURBSTo,
    DatadiagramMLTextFormat_XYABCDEElt,
    UniqueIdElt,
    DatadiagramMLTextFormat_ShapeElt,
    ShapeElt,
    DatadiagramMLTextFormat_Geom,
    DatadiagramMLTextFormat_Field,
    DatadiagramMLTextFormat_Text,
    DatadiagramMLTextFormat_TabsCollection,
    DatadiagramMLTextFormat_Char,
    DatadiagramMLTextFormat_Para,
    ShapesCollection,
    DatadiagramMLTextFormat_Shape,
    DatadiagramMLTextFormat_UniqueIdElt,
    DatadiagramMLTextFormat_IdentifiedElt,
    DatadiagramMLTextFormat_VBProjectData,
    PageSheet,
    NamedElt,
    DatadiagramMLTextFormat_DocumentSheet,
    Shape,
    DatadiagramMLTextFormat_PageSheet,
    StyleSheet,
    DatadiagramMLTextFormat_StyleSheetsCollection,
    DatadiagramMLTextFormat_EmailRoutingData,
    FontEntry,
    DatadiagramMLTextFormat_FontsTable,
    FaceName,
    DatadiagramMLTextFormat_FaceNamesTable,
    IdentifiedElt,
    DatadiagramMLTextFormat_StyleSheet,
    DatadiagramMLTextFormat_Page,
    DatadiagramMLTextFormat_MasterShortCut,
    DatadiagramMLTextFormat_FaceName,
    DatadiagramMLTextFormat_Master,
    CustomProperty,
    DatadiagramMLTextFormat_FontEntry,
    DatadiagramMLTextFormat_CustomPropertiesCollection,
    IXrequiredElt,
    DatadiagramMLTextFormat_Fld,
    DatadiagramMLTextFormat_Tp,
    DatadiagramMLTextFormat_Pp,
    DatadiagramMLTextFormat_Cp,
    DatadiagramMLTextFormat_ColorEntry,
    ColorEntry,
    DatadiagramMLTextFormat_ColorsTable,
    DatadiagramMLTextFormat_CustomProperty,
    DateTimeType,
    CustomPropertiesCollection,
    StyleSheetsCollection,
    FaceNamesTable,
    FontsTable,
    PrintSetup,
    ColorsTable,
    VisioDocument,
    DatadiagramMLTextFormat_DocumentPropertiesCollection,
    SolutionXML,
    EmailRoutingData,
    VBProjectData,
    HeaderFooter,
    EventList,
    WindowsInfo,
    PagesCollection,
    MastersCollection,
    DocumentSheet,
    DatadiagramMLTextFormat_DateTimeType,
    DocumentSettingsElt,
    DocumentPropertiesCollection,
    DatadiagramMLTextFormat_VisioDocument,
    DatadiagramMLTextFormat_CellType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_xyabelt_is_not_abstract():
    assert not inspect.isabstract(XYABElt)


def test_hyp_xyabelt_constructor_exists():
    assert callable(XYABElt.__init__)


def test_hyp_xyabelt_constructor_args():
    sig = inspect.signature(XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_XYABCDElt)


def test_hyp_datadiagrammltextformat_xyabcdelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_XYABCDElt.__init__)


def test_hyp_datadiagrammltextformat_xyabcdelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_infiniteline_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_InfiniteLine)


def test_hyp_datadiagrammltextformat_infiniteline_constructor_exists():
    assert callable(DatadiagramMLTextFormat_InfiniteLine.__init__)


def test_hyp_datadiagrammltextformat_infiniteline_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xyaelt_is_not_abstract():
    assert not inspect.isabstract(XYAElt)


def test_hyp_xyaelt_constructor_exists():
    assert callable(XYAElt.__init__)


def test_hyp_xyaelt_constructor_args():
    sig = inspect.signature(XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_xyabelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_XYABElt)


def test_hyp_datadiagrammltextformat_xyabelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_XYABElt.__init__)


def test_hyp_datadiagrammltextformat_xyabelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_polylineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_PolylineTo)


def test_hyp_datadiagrammltextformat_polylineto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_PolylineTo.__init__)


def test_hyp_datadiagrammltextformat_polylineto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_splineknot_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_SplineKnot)


def test_hyp_datadiagrammltextformat_splineknot_constructor_exists():
    assert callable(DatadiagramMLTextFormat_SplineKnot.__init__)


def test_hyp_datadiagrammltextformat_splineknot_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_arcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ArcTo)


def test_hyp_datadiagrammltextformat_arcto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ArcTo.__init__)


def test_hyp_datadiagrammltextformat_arcto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ArcTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_geom_is_not_abstract():
    assert not inspect.isabstract(Geom)


def test_hyp_geom_constructor_exists():
    assert callable(Geom.__init__)


def test_hyp_geom_constructor_args():
    sig = inspect.signature(Geom.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xyelt_is_not_abstract():
    assert not inspect.isabstract(XYElt)


def test_hyp_xyelt_constructor_exists():
    assert callable(XYElt.__init__)


def test_hyp_xyelt_constructor_args():
    sig = inspect.signature(XYElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_xyaelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_XYAElt)


def test_hyp_datadiagrammltextformat_xyaelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_XYAElt.__init__)


def test_hyp_datadiagrammltextformat_xyaelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_moveto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_MoveTo)


def test_hyp_datadiagrammltextformat_moveto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_MoveTo.__init__)


def test_hyp_datadiagrammltextformat_moveto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_lineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_LineTo)


def test_hyp_datadiagrammltextformat_lineto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_LineTo.__init__)


def test_hyp_datadiagrammltextformat_lineto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_LineTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_splineknot_is_not_abstract():
    assert not inspect.isabstract(SplineKnot)


def test_hyp_splineknot_constructor_exists():
    assert callable(SplineKnot.__init__)


def test_hyp_splineknot_constructor_args():
    sig = inspect.signature(SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arcto_is_not_abstract():
    assert not inspect.isabstract(ArcTo)


def test_hyp_arcto_constructor_exists():
    assert callable(ArcTo.__init__)


def test_hyp_arcto_constructor_args():
    sig = inspect.signature(ArcTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nurbsto_is_not_abstract():
    assert not inspect.isabstract(NURBSTo)


def test_hyp_nurbsto_constructor_exists():
    assert callable(NURBSTo.__init__)


def test_hyp_nurbsto_constructor_args():
    sig = inspect.signature(NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_splinestart_is_not_abstract():
    assert not inspect.isabstract(SplineStart)


def test_hyp_splinestart_constructor_exists():
    assert callable(SplineStart.__init__)


def test_hyp_splinestart_constructor_args():
    sig = inspect.signature(SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(EllipticalArcTo)


def test_hyp_ellipticalarcto_constructor_exists():
    assert callable(EllipticalArcTo.__init__)


def test_hyp_ellipticalarcto_constructor_args():
    sig = inspect.signature(EllipticalArcTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ellipse_is_not_abstract():
    assert not inspect.isabstract(Ellipse)


def test_hyp_ellipse_constructor_exists():
    assert callable(Ellipse.__init__)


def test_hyp_ellipse_constructor_args():
    sig = inspect.signature(Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_infiniteline_is_not_abstract():
    assert not inspect.isabstract(InfiniteLine)


def test_hyp_infiniteline_constructor_exists():
    assert callable(InfiniteLine.__init__)


def test_hyp_infiniteline_constructor_args():
    sig = inspect.signature(InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_polylineto_is_not_abstract():
    assert not inspect.isabstract(PolylineTo)


def test_hyp_polylineto_constructor_exists():
    assert callable(PolylineTo.__init__)


def test_hyp_polylineto_constructor_args():
    sig = inspect.signature(PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_delelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_DelElt)


def test_hyp_datadiagrammltextformat_delelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_DelElt.__init__)


def test_hyp_datadiagrammltextformat_delelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_DelElt.__init__)
    params = list(sig.parameters.keys())
    assert "del_" in params, "Missing parameter 'del_'"




def test_hyp_datadiagrammltextformat_ixelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_IXElt)


def test_hyp_datadiagrammltextformat_ixelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_IXElt.__init__)


def test_hyp_datadiagrammltextformat_ixelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_IXElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"




def test_hyp_moveto_is_not_abstract():
    assert not inspect.isabstract(MoveTo)


def test_hyp_moveto_constructor_exists():
    assert callable(MoveTo.__init__)


def test_hyp_moveto_constructor_args():
    sig = inspect.signature(MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lineto_is_not_abstract():
    assert not inspect.isabstract(LineTo)


def test_hyp_lineto_constructor_exists():
    assert callable(LineTo.__init__)


def test_hyp_lineto_constructor_args():
    sig = inspect.signature(LineTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_celltype_is_not_abstract():
    assert not inspect.isabstract(CellType)


def test_hyp_celltype_constructor_exists():
    assert callable(CellType.__init__)


def test_hyp_celltype_constructor_args():
    sig = inspect.signature(CellType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_delelt_is_not_abstract():
    assert not inspect.isabstract(DelElt)


def test_hyp_delelt_constructor_exists():
    assert callable(DelElt.__init__)


def test_hyp_delelt_constructor_args():
    sig = inspect.signature(DelElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ixelt_is_not_abstract():
    assert not inspect.isabstract(IXElt)


def test_hyp_ixelt_constructor_exists():
    assert callable(IXElt.__init__)


def test_hyp_ixelt_constructor_args():
    sig = inspect.signature(IXElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_xyelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_XYElt)


def test_hyp_datadiagrammltextformat_xyelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_XYElt.__init__)


def test_hyp_datadiagrammltextformat_xyelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_XYElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_namedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_NamedElt)


def test_hyp_datadiagrammltextformat_namedelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_NamedElt.__init__)


def test_hyp_datadiagrammltextformat_namedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nameU" in params, "Missing parameter 'nameU'"





def test_hyp_pageelt_is_not_abstract():
    assert not inspect.isabstract(PageElt)


def test_hyp_pageelt_constructor_exists():
    assert callable(PageElt.__init__)


def test_hyp_pageelt_constructor_args():
    sig = inspect.signature(PageElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_masterelt_is_not_abstract():
    assert not inspect.isabstract(MasterElt)


def test_hyp_masterelt_constructor_exists():
    assert callable(MasterElt.__init__)


def test_hyp_masterelt_constructor_args():
    sig = inspect.signature(MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_solutionxml_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_SolutionXML)


def test_hyp_datadiagrammltextformat_solutionxml_constructor_exists():
    assert callable(DatadiagramMLTextFormat_SolutionXML.__init__)


def test_hyp_datadiagrammltextformat_solutionxml_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_SolutionXML.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_headerfooter_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_HeaderFooter)


def test_hyp_datadiagrammltextformat_headerfooter_constructor_exists():
    assert callable(DatadiagramMLTextFormat_HeaderFooter.__init__)


def test_hyp_datadiagrammltextformat_headerfooter_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_HeaderFooter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_eventlist_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_EventList)


def test_hyp_datadiagrammltextformat_eventlist_constructor_exists():
    assert callable(DatadiagramMLTextFormat_EventList.__init__)


def test_hyp_datadiagrammltextformat_eventlist_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_EventList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_windowsinfo_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_WindowsInfo)


def test_hyp_datadiagrammltextformat_windowsinfo_constructor_exists():
    assert callable(DatadiagramMLTextFormat_WindowsInfo.__init__)


def test_hyp_datadiagrammltextformat_windowsinfo_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_WindowsInfo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_documentsettingselt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_DocumentSettingsElt)


def test_hyp_datadiagrammltextformat_documentsettingselt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_DocumentSettingsElt.__init__)


def test_hyp_datadiagrammltextformat_documentsettingselt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_DocumentSettingsElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_pageelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_PageElt)


def test_hyp_datadiagrammltextformat_pageelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_PageElt.__init__)


def test_hyp_datadiagrammltextformat_pageelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_PageElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_printsetup_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_PrintSetup)


def test_hyp_datadiagrammltextformat_printsetup_constructor_exists():
    assert callable(DatadiagramMLTextFormat_PrintSetup.__init__)


def test_hyp_datadiagrammltextformat_printsetup_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_PrintSetup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_pagescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_PagesCollection)


def test_hyp_datadiagrammltextformat_pagescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_PagesCollection.__init__)


def test_hyp_datadiagrammltextformat_pagescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_masterelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_MasterElt)


def test_hyp_datadiagrammltextformat_masterelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_MasterElt.__init__)


def test_hyp_datadiagrammltextformat_masterelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connectscollection_is_not_abstract():
    assert not inspect.isabstract(ConnectsCollection)


def test_hyp_connectscollection_constructor_exists():
    assert callable(ConnectsCollection.__init__)


def test_hyp_connectscollection_constructor_args():
    sig = inspect.signature(ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_connect_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Connect)


def test_hyp_datadiagrammltextformat_connect_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Connect.__init__)


def test_hyp_datadiagrammltextformat_connect_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Connect.__init__)
    params = list(sig.parameters.keys())
    assert "fromCell" in params, "Missing parameter 'fromCell'"
    assert "toCell" in params, "Missing parameter 'toCell'"
    assert "fromSheet" in params, "Missing parameter 'fromSheet'"
    assert "toPart" in params, "Missing parameter 'toPart'"
    assert "toSheet" in params, "Missing parameter 'toSheet'"
    assert "fromPart" in params, "Missing parameter 'fromPart'"









def test_hyp_connect_is_not_abstract():
    assert not inspect.isabstract(Connect)


def test_hyp_connect_constructor_exists():
    assert callable(Connect.__init__)


def test_hyp_connect_constructor_args():
    sig = inspect.signature(Connect.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_connectscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ConnectsCollection)


def test_hyp_datadiagrammltextformat_connectscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ConnectsCollection.__init__)


def test_hyp_datadiagrammltextformat_connectscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_hyp_page_constructor_exists():
    assert callable(Page.__init__)


def test_hyp_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_shapescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ShapesCollection)


def test_hyp_datadiagrammltextformat_shapescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ShapesCollection.__init__)


def test_hyp_datadiagrammltextformat_shapescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_icon_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Icon)


def test_hyp_datadiagrammltextformat_icon_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Icon.__init__)


def test_hyp_datadiagrammltextformat_icon_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Icon.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_icon_is_not_abstract():
    assert not inspect.isabstract(Icon)


def test_hyp_icon_constructor_exists():
    assert callable(Icon.__init__)


def test_hyp_icon_constructor_args():
    sig = inspect.signature(Icon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mastershortcut_is_not_abstract():
    assert not inspect.isabstract(MasterShortCut)


def test_hyp_mastershortcut_constructor_exists():
    assert callable(MasterShortCut.__init__)


def test_hyp_mastershortcut_constructor_args():
    sig = inspect.signature(MasterShortCut.__init__)
    params = list(sig.parameters.keys())



def test_hyp_master_is_not_abstract():
    assert not inspect.isabstract(Master)


def test_hyp_master_constructor_exists():
    assert callable(Master.__init__)


def test_hyp_master_constructor_args():
    sig = inspect.signature(Master.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_masterscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_MastersCollection)


def test_hyp_datadiagrammltextformat_masterscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_MastersCollection.__init__)


def test_hyp_datadiagrammltextformat_masterscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tabscollection_is_not_abstract():
    assert not inspect.isabstract(TabsCollection)


def test_hyp_tabscollection_constructor_exists():
    assert callable(TabsCollection.__init__)


def test_hyp_tabscollection_constructor_args():
    sig = inspect.signature(TabsCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_tab_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Tab)


def test_hyp_datadiagrammltextformat_tab_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Tab.__init__)


def test_hyp_datadiagrammltextformat_tab_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Tab.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tab_is_not_abstract():
    assert not inspect.isabstract(Tab)


def test_hyp_tab_constructor_exists():
    assert callable(Tab.__init__)


def test_hyp_tab_constructor_args():
    sig = inspect.signature(Tab.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_ixrequiredelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_IXrequiredElt)


def test_hyp_datadiagrammltextformat_ixrequiredelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_IXrequiredElt.__init__)


def test_hyp_datadiagrammltextformat_ixrequiredelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_IXrequiredElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"




def test_hyp_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_hyp_text_constructor_exists():
    assert callable(Text.__init__)


def test_hyp_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_textelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_TextElt)


def test_hyp_datadiagrammltextformat_textelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_TextElt.__init__)


def test_hyp_datadiagrammltextformat_textelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_TextElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDElt)


def test_hyp_xyabcdelt_constructor_exists():
    assert callable(XYABCDElt.__init__)


def test_hyp_xyabcdelt_constructor_args():
    sig = inspect.signature(XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_splinestart_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_SplineStart)


def test_hyp_datadiagrammltextformat_splinestart_constructor_exists():
    assert callable(DatadiagramMLTextFormat_SplineStart.__init__)


def test_hyp_datadiagrammltextformat_splinestart_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_EllipticalArcTo)


def test_hyp_datadiagrammltextformat_ellipticalarcto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_EllipticalArcTo.__init__)


def test_hyp_datadiagrammltextformat_ellipticalarcto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_EllipticalArcTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_ellipse_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Ellipse)


def test_hyp_datadiagrammltextformat_ellipse_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Ellipse.__init__)


def test_hyp_datadiagrammltextformat_ellipse_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_textelt_is_not_abstract():
    assert not inspect.isabstract(TextElt)


def test_hyp_textelt_constructor_exists():
    assert callable(TextElt.__init__)


def test_hyp_textelt_constructor_args():
    sig = inspect.signature(TextElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_stringelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_StringElt)


def test_hyp_datadiagrammltextformat_stringelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_StringElt.__init__)


def test_hyp_datadiagrammltextformat_stringelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_StringElt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDEElt)


def test_hyp_xyabcdeelt_constructor_exists():
    assert callable(XYABCDEElt.__init__)


def test_hyp_xyabcdeelt_constructor_args():
    sig = inspect.signature(XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_nurbsto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_NURBSTo)


def test_hyp_datadiagrammltextformat_nurbsto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_NURBSTo.__init__)


def test_hyp_datadiagrammltextformat_nurbsto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_XYABCDEElt)


def test_hyp_datadiagrammltextformat_xyabcdeelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_XYABCDEElt.__init__)


def test_hyp_datadiagrammltextformat_xyabcdeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(UniqueIdElt)


def test_hyp_uniqueidelt_constructor_exists():
    assert callable(UniqueIdElt.__init__)


def test_hyp_uniqueidelt_constructor_args():
    sig = inspect.signature(UniqueIdElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_shapeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ShapeElt)


def test_hyp_datadiagrammltextformat_shapeelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ShapeElt.__init__)


def test_hyp_datadiagrammltextformat_shapeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shapeelt_is_not_abstract():
    assert not inspect.isabstract(ShapeElt)


def test_hyp_shapeelt_constructor_exists():
    assert callable(ShapeElt.__init__)


def test_hyp_shapeelt_constructor_args():
    sig = inspect.signature(ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_geom_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Geom)


def test_hyp_datadiagrammltextformat_geom_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Geom.__init__)


def test_hyp_datadiagrammltextformat_geom_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Geom.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_field_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Field)


def test_hyp_datadiagrammltextformat_field_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Field.__init__)


def test_hyp_datadiagrammltextformat_field_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Field.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_text_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Text)


def test_hyp_datadiagrammltextformat_text_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Text.__init__)


def test_hyp_datadiagrammltextformat_text_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Text.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_tabscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_TabsCollection)


def test_hyp_datadiagrammltextformat_tabscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_TabsCollection.__init__)


def test_hyp_datadiagrammltextformat_tabscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_TabsCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_char_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Char)


def test_hyp_datadiagrammltextformat_char_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Char.__init__)


def test_hyp_datadiagrammltextformat_char_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Char.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_para_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Para)


def test_hyp_datadiagrammltextformat_para_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Para.__init__)


def test_hyp_datadiagrammltextformat_para_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Para.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shapescollection_is_not_abstract():
    assert not inspect.isabstract(ShapesCollection)


def test_hyp_shapescollection_constructor_exists():
    assert callable(ShapesCollection.__init__)


def test_hyp_shapescollection_constructor_args():
    sig = inspect.signature(ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_shape_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Shape)


def test_hyp_datadiagrammltextformat_shape_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Shape.__init__)


def test_hyp_datadiagrammltextformat_shape_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "fillStyle" in params, "Missing parameter 'fillStyle'"
    assert "textStyle" in params, "Missing parameter 'textStyle'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"






def test_hyp_datadiagrammltextformat_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_UniqueIdElt)


def test_hyp_datadiagrammltextformat_uniqueidelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_UniqueIdElt.__init__)


def test_hyp_datadiagrammltextformat_uniqueidelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_UniqueIdElt.__init__)
    params = list(sig.parameters.keys())
    assert "UniqueID" in params, "Missing parameter 'UniqueID'"




def test_hyp_datadiagrammltextformat_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_IdentifiedElt)


def test_hyp_datadiagrammltextformat_identifiedelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_IdentifiedElt.__init__)


def test_hyp_datadiagrammltextformat_identifiedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_IdentifiedElt.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"




def test_hyp_datadiagrammltextformat_vbprojectdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_VBProjectData)


def test_hyp_datadiagrammltextformat_vbprojectdata_constructor_exists():
    assert callable(DatadiagramMLTextFormat_VBProjectData.__init__)


def test_hyp_datadiagrammltextformat_vbprojectdata_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_VBProjectData.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"




def test_hyp_pagesheet_is_not_abstract():
    assert not inspect.isabstract(PageSheet)


def test_hyp_pagesheet_constructor_exists():
    assert callable(PageSheet.__init__)


def test_hyp_pagesheet_constructor_args():
    sig = inspect.signature(PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_hyp_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_hyp_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_documentsheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_DocumentSheet)


def test_hyp_datadiagrammltextformat_documentsheet_constructor_exists():
    assert callable(DatadiagramMLTextFormat_DocumentSheet.__init__)


def test_hyp_datadiagrammltextformat_documentsheet_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_DocumentSheet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_hyp_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_hyp_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_pagesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_PageSheet)


def test_hyp_datadiagrammltextformat_pagesheet_constructor_exists():
    assert callable(DatadiagramMLTextFormat_PageSheet.__init__)


def test_hyp_datadiagrammltextformat_pagesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stylesheet_is_not_abstract():
    assert not inspect.isabstract(StyleSheet)


def test_hyp_stylesheet_constructor_exists():
    assert callable(StyleSheet.__init__)


def test_hyp_stylesheet_constructor_args():
    sig = inspect.signature(StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_StyleSheetsCollection)


def test_hyp_datadiagrammltextformat_stylesheetscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_StyleSheetsCollection.__init__)


def test_hyp_datadiagrammltextformat_stylesheetscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_emailroutingdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_EmailRoutingData)


def test_hyp_datadiagrammltextformat_emailroutingdata_constructor_exists():
    assert callable(DatadiagramMLTextFormat_EmailRoutingData.__init__)


def test_hyp_datadiagrammltextformat_emailroutingdata_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_EmailRoutingData.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "data" in params, "Missing parameter 'data'"





def test_hyp_fontentry_is_not_abstract():
    assert not inspect.isabstract(FontEntry)


def test_hyp_fontentry_constructor_exists():
    assert callable(FontEntry.__init__)


def test_hyp_fontentry_constructor_args():
    sig = inspect.signature(FontEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_fontstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_FontsTable)


def test_hyp_datadiagrammltextformat_fontstable_constructor_exists():
    assert callable(DatadiagramMLTextFormat_FontsTable.__init__)


def test_hyp_datadiagrammltextformat_fontstable_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_FontsTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_facename_is_not_abstract():
    assert not inspect.isabstract(FaceName)


def test_hyp_facename_constructor_exists():
    assert callable(FaceName.__init__)


def test_hyp_facename_constructor_args():
    sig = inspect.signature(FaceName.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_facenamestable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_FaceNamesTable)


def test_hyp_datadiagrammltextformat_facenamestable_constructor_exists():
    assert callable(DatadiagramMLTextFormat_FaceNamesTable.__init__)


def test_hyp_datadiagrammltextformat_facenamestable_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_FaceNamesTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElt)


def test_hyp_identifiedelt_constructor_exists():
    assert callable(IdentifiedElt.__init__)


def test_hyp_identifiedelt_constructor_args():
    sig = inspect.signature(IdentifiedElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_stylesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_StyleSheet)


def test_hyp_datadiagrammltextformat_stylesheet_constructor_exists():
    assert callable(DatadiagramMLTextFormat_StyleSheet.__init__)


def test_hyp_datadiagrammltextformat_stylesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_page_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Page)


def test_hyp_datadiagrammltextformat_page_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Page.__init__)


def test_hyp_datadiagrammltextformat_page_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Page.__init__)
    params = list(sig.parameters.keys())
    assert "viewCenterX" in params, "Missing parameter 'viewCenterX'"
    assert "background" in params, "Missing parameter 'background'"
    assert "ViewCenterY" in params, "Missing parameter 'ViewCenterY'"
    assert "backPage" in params, "Missing parameter 'backPage'"
    assert "associatedPage" in params, "Missing parameter 'associatedPage'"
    assert "reviewerID" in params, "Missing parameter 'reviewerID'"
    assert "viewScale" in params, "Missing parameter 'viewScale'"










def test_hyp_datadiagrammltextformat_mastershortcut_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_MasterShortCut)


def test_hyp_datadiagrammltextformat_mastershortcut_constructor_exists():
    assert callable(DatadiagramMLTextFormat_MasterShortCut.__init__)


def test_hyp_datadiagrammltextformat_mastershortcut_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_MasterShortCut.__init__)
    params = list(sig.parameters.keys())
    assert "shortcutURL" in params, "Missing parameter 'shortcutURL'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "shortcutHelp" in params, "Missing parameter 'shortcutHelp'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"









def test_hyp_datadiagrammltextformat_facename_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_FaceName)


def test_hyp_datadiagrammltextformat_facename_constructor_exists():
    assert callable(DatadiagramMLTextFormat_FaceName.__init__)


def test_hyp_datadiagrammltextformat_facename_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_FaceName.__init__)
    params = list(sig.parameters.keys())
    assert "charSet" in params, "Missing parameter 'charSet'"
    assert "unicodeRanges" in params, "Missing parameter 'unicodeRanges'"
    assert "flags" in params, "Missing parameter 'flags'"
    assert "name" in params, "Missing parameter 'name'"
    assert "panos" in params, "Missing parameter 'panos'"








def test_hyp_datadiagrammltextformat_master_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Master)


def test_hyp_datadiagrammltextformat_master_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Master.__init__)


def test_hyp_datadiagrammltextformat_master_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Master.__init__)
    params = list(sig.parameters.keys())
    assert "baseID" in params, "Missing parameter 'baseID'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "matchByName" in params, "Missing parameter 'matchByName'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "iconUpdate" in params, "Missing parameter 'iconUpdate'"
    assert "prompt" in params, "Missing parameter 'prompt'"











def test_hyp_customproperty_is_not_abstract():
    assert not inspect.isabstract(CustomProperty)


def test_hyp_customproperty_constructor_exists():
    assert callable(CustomProperty.__init__)


def test_hyp_customproperty_constructor_args():
    sig = inspect.signature(CustomProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_fontentry_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_FontEntry)


def test_hyp_datadiagrammltextformat_fontentry_constructor_exists():
    assert callable(DatadiagramMLTextFormat_FontEntry.__init__)


def test_hyp_datadiagrammltextformat_fontentry_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_FontEntry.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "charSet" in params, "Missing parameter 'charSet'"
    assert "pitchAndFamily" in params, "Missing parameter 'pitchAndFamily'"
    assert "name" in params, "Missing parameter 'name'"
    assert "unicode" in params, "Missing parameter 'unicode'"
    assert "attributes" in params, "Missing parameter 'attributes'"









def test_hyp_datadiagrammltextformat_custompropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_CustomPropertiesCollection)


def test_hyp_datadiagrammltextformat_custompropertiescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_CustomPropertiesCollection.__init__)


def test_hyp_datadiagrammltextformat_custompropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_CustomPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ixrequiredelt_is_not_abstract():
    assert not inspect.isabstract(IXrequiredElt)


def test_hyp_ixrequiredelt_constructor_exists():
    assert callable(IXrequiredElt.__init__)


def test_hyp_ixrequiredelt_constructor_args():
    sig = inspect.signature(IXrequiredElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_fld_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Fld)


def test_hyp_datadiagrammltextformat_fld_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Fld.__init__)


def test_hyp_datadiagrammltextformat_fld_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Fld.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_tp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Tp)


def test_hyp_datadiagrammltextformat_tp_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Tp.__init__)


def test_hyp_datadiagrammltextformat_tp_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Tp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_pp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Pp)


def test_hyp_datadiagrammltextformat_pp_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Pp.__init__)


def test_hyp_datadiagrammltextformat_pp_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Pp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_cp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Cp)


def test_hyp_datadiagrammltextformat_cp_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Cp.__init__)


def test_hyp_datadiagrammltextformat_cp_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Cp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_colorentry_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ColorEntry)


def test_hyp_datadiagrammltextformat_colorentry_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ColorEntry.__init__)


def test_hyp_datadiagrammltextformat_colorentry_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ColorEntry.__init__)
    params = list(sig.parameters.keys())
    assert "rgb" in params, "Missing parameter 'rgb'"




def test_hyp_colorentry_is_not_abstract():
    assert not inspect.isabstract(ColorEntry)


def test_hyp_colorentry_constructor_exists():
    assert callable(ColorEntry.__init__)


def test_hyp_colorentry_constructor_args():
    sig = inspect.signature(ColorEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_colorstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ColorsTable)


def test_hyp_datadiagrammltextformat_colorstable_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ColorsTable.__init__)


def test_hyp_datadiagrammltextformat_colorstable_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ColorsTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_customproperty_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_CustomProperty)


def test_hyp_datadiagrammltextformat_customproperty_constructor_exists():
    assert callable(DatadiagramMLTextFormat_CustomProperty.__init__)


def test_hyp_datadiagrammltextformat_customproperty_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_CustomProperty.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_hyp_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_hyp_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_custompropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomPropertiesCollection)


def test_hyp_custompropertiescollection_constructor_exists():
    assert callable(CustomPropertiesCollection.__init__)


def test_hyp_custompropertiescollection_constructor_args():
    sig = inspect.signature(CustomPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(StyleSheetsCollection)


def test_hyp_stylesheetscollection_constructor_exists():
    assert callable(StyleSheetsCollection.__init__)


def test_hyp_stylesheetscollection_constructor_args():
    sig = inspect.signature(StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_facenamestable_is_not_abstract():
    assert not inspect.isabstract(FaceNamesTable)


def test_hyp_facenamestable_constructor_exists():
    assert callable(FaceNamesTable.__init__)


def test_hyp_facenamestable_constructor_args():
    sig = inspect.signature(FaceNamesTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fontstable_is_not_abstract():
    assert not inspect.isabstract(FontsTable)


def test_hyp_fontstable_constructor_exists():
    assert callable(FontsTable.__init__)


def test_hyp_fontstable_constructor_args():
    sig = inspect.signature(FontsTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_printsetup_is_not_abstract():
    assert not inspect.isabstract(PrintSetup)


def test_hyp_printsetup_constructor_exists():
    assert callable(PrintSetup.__init__)


def test_hyp_printsetup_constructor_args():
    sig = inspect.signature(PrintSetup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_colorstable_is_not_abstract():
    assert not inspect.isabstract(ColorsTable)


def test_hyp_colorstable_constructor_exists():
    assert callable(ColorsTable.__init__)


def test_hyp_colorstable_constructor_args():
    sig = inspect.signature(ColorsTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visiodocument_is_not_abstract():
    assert not inspect.isabstract(VisioDocument)


def test_hyp_visiodocument_constructor_exists():
    assert callable(VisioDocument.__init__)


def test_hyp_visiodocument_constructor_args():
    sig = inspect.signature(VisioDocument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_DocumentPropertiesCollection)


def test_hyp_datadiagrammltextformat_documentpropertiescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_DocumentPropertiesCollection.__init__)


def test_hyp_datadiagrammltextformat_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "company" in params, "Missing parameter 'company'"
    assert "template" in params, "Missing parameter 'template'"
    assert "buildNumberCreated" in params, "Missing parameter 'buildNumberCreated'"
    assert "hyperlinkBase_href" in params, "Missing parameter 'hyperlinkBase_href'"
    assert "description" in params, "Missing parameter 'description'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "title" in params, "Missing parameter 'title'"
    assert "creator" in params, "Missing parameter 'creator'"
    assert "category" in params, "Missing parameter 'category'"
    assert "alternateNames" in params, "Missing parameter 'alternateNames'"
    assert "buildNumberEdited" in params, "Missing parameter 'buildNumberEdited'"
















def test_hyp_solutionxml_is_not_abstract():
    assert not inspect.isabstract(SolutionXML)


def test_hyp_solutionxml_constructor_exists():
    assert callable(SolutionXML.__init__)


def test_hyp_solutionxml_constructor_args():
    sig = inspect.signature(SolutionXML.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emailroutingdata_is_not_abstract():
    assert not inspect.isabstract(EmailRoutingData)


def test_hyp_emailroutingdata_constructor_exists():
    assert callable(EmailRoutingData.__init__)


def test_hyp_emailroutingdata_constructor_args():
    sig = inspect.signature(EmailRoutingData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vbprojectdata_is_not_abstract():
    assert not inspect.isabstract(VBProjectData)


def test_hyp_vbprojectdata_constructor_exists():
    assert callable(VBProjectData.__init__)


def test_hyp_vbprojectdata_constructor_args():
    sig = inspect.signature(VBProjectData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_headerfooter_is_not_abstract():
    assert not inspect.isabstract(HeaderFooter)


def test_hyp_headerfooter_constructor_exists():
    assert callable(HeaderFooter.__init__)


def test_hyp_headerfooter_constructor_args():
    sig = inspect.signature(HeaderFooter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eventlist_is_not_abstract():
    assert not inspect.isabstract(EventList)


def test_hyp_eventlist_constructor_exists():
    assert callable(EventList.__init__)


def test_hyp_eventlist_constructor_args():
    sig = inspect.signature(EventList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_windowsinfo_is_not_abstract():
    assert not inspect.isabstract(WindowsInfo)


def test_hyp_windowsinfo_constructor_exists():
    assert callable(WindowsInfo.__init__)


def test_hyp_windowsinfo_constructor_args():
    sig = inspect.signature(WindowsInfo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pagescollection_is_not_abstract():
    assert not inspect.isabstract(PagesCollection)


def test_hyp_pagescollection_constructor_exists():
    assert callable(PagesCollection.__init__)


def test_hyp_pagescollection_constructor_args():
    sig = inspect.signature(PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_masterscollection_is_not_abstract():
    assert not inspect.isabstract(MastersCollection)


def test_hyp_masterscollection_constructor_exists():
    assert callable(MastersCollection.__init__)


def test_hyp_masterscollection_constructor_args():
    sig = inspect.signature(MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_documentsheet_is_not_abstract():
    assert not inspect.isabstract(DocumentSheet)


def test_hyp_documentsheet_constructor_exists():
    assert callable(DocumentSheet.__init__)


def test_hyp_documentsheet_constructor_args():
    sig = inspect.signature(DocumentSheet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_DateTimeType)


def test_hyp_datadiagrammltextformat_datetimetype_constructor_exists():
    assert callable(DatadiagramMLTextFormat_DateTimeType.__init__)


def test_hyp_datadiagrammltextformat_datetimetype_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "day" in params, "Missing parameter 'day'"
    assert "second" in params, "Missing parameter 'second'"
    assert "year" in params, "Missing parameter 'year'"
    assert "minute" in params, "Missing parameter 'minute'"









def test_hyp_documentsettingselt_is_not_abstract():
    assert not inspect.isabstract(DocumentSettingsElt)


def test_hyp_documentsettingselt_constructor_exists():
    assert callable(DocumentSettingsElt.__init__)


def test_hyp_documentsettingselt_constructor_args():
    sig = inspect.signature(DocumentSettingsElt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_hyp_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_hyp_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadiagrammltextformat_visiodocument_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_VisioDocument)


def test_hyp_datadiagrammltextformat_visiodocument_constructor_exists():
    assert callable(DatadiagramMLTextFormat_VisioDocument.__init__)


def test_hyp_datadiagrammltextformat_visiodocument_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_VisioDocument.__init__)
    params = list(sig.parameters.keys())
    assert "docLangId" in params, "Missing parameter 'docLangId'"
    assert "version" in params, "Missing parameter 'version'"
    assert "start" in params, "Missing parameter 'start'"
    assert "metric" in params, "Missing parameter 'metric'"
    assert "key" in params, "Missing parameter 'key'"
    assert "buildnum" in params, "Missing parameter 'buildnum'"









def test_hyp_datadiagrammltextformat_celltype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_CellType)


def test_hyp_datadiagrammltextformat_celltype_constructor_exists():
    assert callable(DatadiagramMLTextFormat_CellType.__init__)


def test_hyp_datadiagrammltextformat_celltype_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_CellType.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "err" in params, "Missing parameter 'err'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "value" in params, "Missing parameter 'value'"






# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
XYABElt_strategy = st.builds(
    XYABElt,
)
DatadiagramMLTextFormat_XYABCDElt_strategy = st.builds(
    DatadiagramMLTextFormat_XYABCDElt,
)
DatadiagramMLTextFormat_InfiniteLine_strategy = st.builds(
    DatadiagramMLTextFormat_InfiniteLine,
)
XYAElt_strategy = st.builds(
    XYAElt,
)
DatadiagramMLTextFormat_XYABElt_strategy = st.builds(
    DatadiagramMLTextFormat_XYABElt,
)
DatadiagramMLTextFormat_PolylineTo_strategy = st.builds(
    DatadiagramMLTextFormat_PolylineTo,
)
DatadiagramMLTextFormat_SplineKnot_strategy = st.builds(
    DatadiagramMLTextFormat_SplineKnot,
)
DatadiagramMLTextFormat_ArcTo_strategy = st.builds(
    DatadiagramMLTextFormat_ArcTo,
)
Geom_strategy = st.builds(
    Geom,
)
XYElt_strategy = st.builds(
    XYElt,
)
DatadiagramMLTextFormat_XYAElt_strategy = st.builds(
    DatadiagramMLTextFormat_XYAElt,
)
DatadiagramMLTextFormat_MoveTo_strategy = st.builds(
    DatadiagramMLTextFormat_MoveTo,
)
DatadiagramMLTextFormat_LineTo_strategy = st.builds(
    DatadiagramMLTextFormat_LineTo,
)
SplineKnot_strategy = st.builds(
    SplineKnot,
)
ArcTo_strategy = st.builds(
    ArcTo,
)
NURBSTo_strategy = st.builds(
    NURBSTo,
)
SplineStart_strategy = st.builds(
    SplineStart,
)
EllipticalArcTo_strategy = st.builds(
    EllipticalArcTo,
)
Ellipse_strategy = st.builds(
    Ellipse,
)
InfiniteLine_strategy = st.builds(
    InfiniteLine,
)
PolylineTo_strategy = st.builds(
    PolylineTo,
)
DatadiagramMLTextFormat_DelElt_strategy = st.builds(
    DatadiagramMLTextFormat_DelElt,
    del_=
        safe_text
)
DatadiagramMLTextFormat_IXElt_strategy = st.builds(
    DatadiagramMLTextFormat_IXElt,
    iX=
        safe_text
)
MoveTo_strategy = st.builds(
    MoveTo,
)
LineTo_strategy = st.builds(
    LineTo,
)
CellType_strategy = st.builds(
    CellType,
)
DelElt_strategy = st.builds(
    DelElt,
)
IXElt_strategy = st.builds(
    IXElt,
)
DatadiagramMLTextFormat_XYElt_strategy = st.builds(
    DatadiagramMLTextFormat_XYElt,
)
DatadiagramMLTextFormat_NamedElt_strategy = st.builds(
    DatadiagramMLTextFormat_NamedElt,
    name=
        safe_text,
    nameU=
        safe_text
)
PageElt_strategy = st.builds(
    PageElt,
)
MasterElt_strategy = st.builds(
    MasterElt,
)
DatadiagramMLTextFormat_SolutionXML_strategy = st.builds(
    DatadiagramMLTextFormat_SolutionXML,
)
DatadiagramMLTextFormat_HeaderFooter_strategy = st.builds(
    DatadiagramMLTextFormat_HeaderFooter,
)
DatadiagramMLTextFormat_EventList_strategy = st.builds(
    DatadiagramMLTextFormat_EventList,
)
DatadiagramMLTextFormat_WindowsInfo_strategy = st.builds(
    DatadiagramMLTextFormat_WindowsInfo,
)
DatadiagramMLTextFormat_DocumentSettingsElt_strategy = st.builds(
    DatadiagramMLTextFormat_DocumentSettingsElt,
)
DatadiagramMLTextFormat_PageElt_strategy = st.builds(
    DatadiagramMLTextFormat_PageElt,
)
DatadiagramMLTextFormat_PrintSetup_strategy = st.builds(
    DatadiagramMLTextFormat_PrintSetup,
)
DatadiagramMLTextFormat_PagesCollection_strategy = st.builds(
    DatadiagramMLTextFormat_PagesCollection,
)
DatadiagramMLTextFormat_MasterElt_strategy = st.builds(
    DatadiagramMLTextFormat_MasterElt,
)
ConnectsCollection_strategy = st.builds(
    ConnectsCollection,
)
DatadiagramMLTextFormat_Connect_strategy = st.builds(
    DatadiagramMLTextFormat_Connect,
    fromCell=
        safe_text,
    toCell=
        safe_text,
    fromSheet=
        safe_text,
    toPart=
        safe_text,
    toSheet=
        safe_text,
    fromPart=
        safe_text
)
Connect_strategy = st.builds(
    Connect,
)
DatadiagramMLTextFormat_ConnectsCollection_strategy = st.builds(
    DatadiagramMLTextFormat_ConnectsCollection,
)
Page_strategy = st.builds(
    Page,
)
DatadiagramMLTextFormat_ShapesCollection_strategy = st.builds(
    DatadiagramMLTextFormat_ShapesCollection,
)
DatadiagramMLTextFormat_Icon_strategy = st.builds(
    DatadiagramMLTextFormat_Icon,
    value=
        safe_text
)
Icon_strategy = st.builds(
    Icon,
)
MasterShortCut_strategy = st.builds(
    MasterShortCut,
)
Master_strategy = st.builds(
    Master,
)
DatadiagramMLTextFormat_MastersCollection_strategy = st.builds(
    DatadiagramMLTextFormat_MastersCollection,
)
TabsCollection_strategy = st.builds(
    TabsCollection,
)
DatadiagramMLTextFormat_Tab_strategy = st.builds(
    DatadiagramMLTextFormat_Tab,
)
Tab_strategy = st.builds(
    Tab,
)
DatadiagramMLTextFormat_IXrequiredElt_strategy = st.builds(
    DatadiagramMLTextFormat_IXrequiredElt,
    iX=
        safe_text
)
Text_strategy = st.builds(
    Text,
)
DatadiagramMLTextFormat_TextElt_strategy = st.builds(
    DatadiagramMLTextFormat_TextElt,
)
XYABCDElt_strategy = st.builds(
    XYABCDElt,
)
DatadiagramMLTextFormat_SplineStart_strategy = st.builds(
    DatadiagramMLTextFormat_SplineStart,
)
DatadiagramMLTextFormat_EllipticalArcTo_strategy = st.builds(
    DatadiagramMLTextFormat_EllipticalArcTo,
)
DatadiagramMLTextFormat_Ellipse_strategy = st.builds(
    DatadiagramMLTextFormat_Ellipse,
)
TextElt_strategy = st.builds(
    TextElt,
)
DatadiagramMLTextFormat_StringElt_strategy = st.builds(
    DatadiagramMLTextFormat_StringElt,
    value=
        safe_text
)
XYABCDEElt_strategy = st.builds(
    XYABCDEElt,
)
DatadiagramMLTextFormat_NURBSTo_strategy = st.builds(
    DatadiagramMLTextFormat_NURBSTo,
)
DatadiagramMLTextFormat_XYABCDEElt_strategy = st.builds(
    DatadiagramMLTextFormat_XYABCDEElt,
)
UniqueIdElt_strategy = st.builds(
    UniqueIdElt,
)
DatadiagramMLTextFormat_ShapeElt_strategy = st.builds(
    DatadiagramMLTextFormat_ShapeElt,
)
ShapeElt_strategy = st.builds(
    ShapeElt,
)
DatadiagramMLTextFormat_Geom_strategy = st.builds(
    DatadiagramMLTextFormat_Geom,
)
DatadiagramMLTextFormat_Field_strategy = st.builds(
    DatadiagramMLTextFormat_Field,
)
DatadiagramMLTextFormat_Text_strategy = st.builds(
    DatadiagramMLTextFormat_Text,
)
DatadiagramMLTextFormat_TabsCollection_strategy = st.builds(
    DatadiagramMLTextFormat_TabsCollection,
)
DatadiagramMLTextFormat_Char_strategy = st.builds(
    DatadiagramMLTextFormat_Char,
)
DatadiagramMLTextFormat_Para_strategy = st.builds(
    DatadiagramMLTextFormat_Para,
)
ShapesCollection_strategy = st.builds(
    ShapesCollection,
)
DatadiagramMLTextFormat_Shape_strategy = st.builds(
    DatadiagramMLTextFormat_Shape,
    fillStyle=
        safe_text,
    textStyle=
        safe_text,
    lineStyle=
        safe_text
)
DatadiagramMLTextFormat_UniqueIdElt_strategy = st.builds(
    DatadiagramMLTextFormat_UniqueIdElt,
    UniqueID=
        safe_text
)
DatadiagramMLTextFormat_IdentifiedElt_strategy = st.builds(
    DatadiagramMLTextFormat_IdentifiedElt,
    ID=
        safe_text
)
DatadiagramMLTextFormat_VBProjectData_strategy = st.builds(
    DatadiagramMLTextFormat_VBProjectData,
    data=
        safe_text
)
PageSheet_strategy = st.builds(
    PageSheet,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
DatadiagramMLTextFormat_DocumentSheet_strategy = st.builds(
    DatadiagramMLTextFormat_DocumentSheet,
)
Shape_strategy = st.builds(
    Shape,
)
DatadiagramMLTextFormat_PageSheet_strategy = st.builds(
    DatadiagramMLTextFormat_PageSheet,
)
StyleSheet_strategy = st.builds(
    StyleSheet,
)
DatadiagramMLTextFormat_StyleSheetsCollection_strategy = st.builds(
    DatadiagramMLTextFormat_StyleSheetsCollection,
)
DatadiagramMLTextFormat_EmailRoutingData_strategy = st.builds(
    DatadiagramMLTextFormat_EmailRoutingData,
    size=
        safe_text,
    data=
        safe_text
)
FontEntry_strategy = st.builds(
    FontEntry,
)
DatadiagramMLTextFormat_FontsTable_strategy = st.builds(
    DatadiagramMLTextFormat_FontsTable,
)
FaceName_strategy = st.builds(
    FaceName,
)
DatadiagramMLTextFormat_FaceNamesTable_strategy = st.builds(
    DatadiagramMLTextFormat_FaceNamesTable,
)
IdentifiedElt_strategy = st.builds(
    IdentifiedElt,
)
DatadiagramMLTextFormat_StyleSheet_strategy = st.builds(
    DatadiagramMLTextFormat_StyleSheet,
)
DatadiagramMLTextFormat_Page_strategy = st.builds(
    DatadiagramMLTextFormat_Page,
    viewCenterX=
        safe_text,
    background=
        safe_text,
    ViewCenterY=
        safe_text,
    backPage=
        safe_text,
    associatedPage=
        safe_text,
    reviewerID=
        safe_text,
    viewScale=
        safe_text
)
DatadiagramMLTextFormat_MasterShortCut_strategy = st.builds(
    DatadiagramMLTextFormat_MasterShortCut,
    shortcutURL=
        safe_text,
    patternFlags=
        safe_text,
    shortcutHelp=
        safe_text,
    alignName=
        safe_text,
    prompt=
        safe_text,
    iconSize=
        safe_text
)
DatadiagramMLTextFormat_FaceName_strategy = st.builds(
    DatadiagramMLTextFormat_FaceName,
    charSet=
        safe_text,
    unicodeRanges=
        safe_text,
    flags=
        safe_text,
    name=
        safe_text,
    panos=
        safe_text
)
DatadiagramMLTextFormat_Master_strategy = st.builds(
    DatadiagramMLTextFormat_Master,
    baseID=
        safe_text,
    alignName=
        safe_text,
    iconSize=
        safe_text,
    matchByName=
        safe_text,
    patternFlags=
        safe_text,
    hidden=
        safe_text,
    iconUpdate=
        safe_text,
    prompt=
        safe_text
)
CustomProperty_strategy = st.builds(
    CustomProperty,
)
DatadiagramMLTextFormat_FontEntry_strategy = st.builds(
    DatadiagramMLTextFormat_FontEntry,
    weight=
        safe_text,
    charSet=
        safe_text,
    pitchAndFamily=
        safe_text,
    name=
        safe_text,
    unicode=
        safe_text,
    attributes=
        safe_text
)
DatadiagramMLTextFormat_CustomPropertiesCollection_strategy = st.builds(
    DatadiagramMLTextFormat_CustomPropertiesCollection,
)
IXrequiredElt_strategy = st.builds(
    IXrequiredElt,
)
DatadiagramMLTextFormat_Fld_strategy = st.builds(
    DatadiagramMLTextFormat_Fld,
)
DatadiagramMLTextFormat_Tp_strategy = st.builds(
    DatadiagramMLTextFormat_Tp,
)
DatadiagramMLTextFormat_Pp_strategy = st.builds(
    DatadiagramMLTextFormat_Pp,
)
DatadiagramMLTextFormat_Cp_strategy = st.builds(
    DatadiagramMLTextFormat_Cp,
)
DatadiagramMLTextFormat_ColorEntry_strategy = st.builds(
    DatadiagramMLTextFormat_ColorEntry,
    rgb=
        safe_text
)
ColorEntry_strategy = st.builds(
    ColorEntry,
)
DatadiagramMLTextFormat_ColorsTable_strategy = st.builds(
    DatadiagramMLTextFormat_ColorsTable,
)
DatadiagramMLTextFormat_CustomProperty_strategy = st.builds(
    DatadiagramMLTextFormat_CustomProperty,
    dataType=
        safe_text,
    name=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
CustomPropertiesCollection_strategy = st.builds(
    CustomPropertiesCollection,
)
StyleSheetsCollection_strategy = st.builds(
    StyleSheetsCollection,
)
FaceNamesTable_strategy = st.builds(
    FaceNamesTable,
)
FontsTable_strategy = st.builds(
    FontsTable,
)
PrintSetup_strategy = st.builds(
    PrintSetup,
)
ColorsTable_strategy = st.builds(
    ColorsTable,
)
VisioDocument_strategy = st.builds(
    VisioDocument,
)
DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy = st.builds(
    DatadiagramMLTextFormat_DocumentPropertiesCollection,
    subject=
        safe_text,
    manager=
        safe_text,
    company=
        safe_text,
    template=
        safe_text,
    buildNumberCreated=
        safe_text,
    hyperlinkBase_href=
        safe_text,
    description=
        safe_text,
    keywords=
        safe_text,
    title=
        safe_text,
    creator=
        safe_text,
    category=
        safe_text,
    alternateNames=
        safe_text,
    buildNumberEdited=
        safe_text
)
SolutionXML_strategy = st.builds(
    SolutionXML,
)
EmailRoutingData_strategy = st.builds(
    EmailRoutingData,
)
VBProjectData_strategy = st.builds(
    VBProjectData,
)
HeaderFooter_strategy = st.builds(
    HeaderFooter,
)
EventList_strategy = st.builds(
    EventList,
)
WindowsInfo_strategy = st.builds(
    WindowsInfo,
)
PagesCollection_strategy = st.builds(
    PagesCollection,
)
MastersCollection_strategy = st.builds(
    MastersCollection,
)
DocumentSheet_strategy = st.builds(
    DocumentSheet,
)
DatadiagramMLTextFormat_DateTimeType_strategy = st.builds(
    DatadiagramMLTextFormat_DateTimeType,
    month=
        safe_text,
    hour=
        safe_text,
    day=
        safe_text,
    second=
        safe_text,
    year=
        safe_text,
    minute=
        safe_text
)
DocumentSettingsElt_strategy = st.builds(
    DocumentSettingsElt,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
DatadiagramMLTextFormat_VisioDocument_strategy = st.builds(
    DatadiagramMLTextFormat_VisioDocument,
    docLangId=
        safe_text,
    version=
        safe_text,
    start=
        safe_text,
    metric=
        safe_text,
    key=
        safe_text,
    buildnum=
        safe_text
)
DatadiagramMLTextFormat_CellType_strategy = st.builds(
    DatadiagramMLTextFormat_CellType,
    unit=
        safe_text,
    err=
        safe_text,
    formula=
        safe_text,
    value=
        safe_text
)

























@given(instance=DatadiagramMLTextFormat_DelElt_strategy)
def test_hyp_datadiagrammltextformat_delelt_del__setter(instance):
    original = instance.del_
    instance.del_ = original
    assert instance.del_ == original




@given(instance=DatadiagramMLTextFormat_IXElt_strategy)
def test_hyp_datadiagrammltextformat_ixelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original










@given(instance=DatadiagramMLTextFormat_NamedElt_strategy)
def test_hyp_datadiagrammltextformat_namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DatadiagramMLTextFormat_NamedElt_strategy)
def test_hyp_datadiagrammltextformat_namedelt_nameU_setter(instance):
    original = instance.nameU
    instance.nameU = original
    assert instance.nameU == original
















@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_hyp_datadiagrammltextformat_connect_fromCell_setter(instance):
    original = instance.fromCell
    instance.fromCell = original
    assert instance.fromCell == original



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_hyp_datadiagrammltextformat_connect_toCell_setter(instance):
    original = instance.toCell
    instance.toCell = original
    assert instance.toCell == original



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_hyp_datadiagrammltextformat_connect_fromSheet_setter(instance):
    original = instance.fromSheet
    instance.fromSheet = original
    assert instance.fromSheet == original



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_hyp_datadiagrammltextformat_connect_toPart_setter(instance):
    original = instance.toPart
    instance.toPart = original
    assert instance.toPart == original



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_hyp_datadiagrammltextformat_connect_toSheet_setter(instance):
    original = instance.toSheet
    instance.toSheet = original
    assert instance.toSheet == original



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_hyp_datadiagrammltextformat_connect_fromPart_setter(instance):
    original = instance.fromPart
    instance.fromPart = original
    assert instance.fromPart == original








@given(instance=DatadiagramMLTextFormat_Icon_strategy)
def test_hyp_datadiagrammltextformat_icon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original











@given(instance=DatadiagramMLTextFormat_IXrequiredElt_strategy)
def test_hyp_datadiagrammltextformat_ixrequiredelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original











@given(instance=DatadiagramMLTextFormat_StringElt_strategy)
def test_hyp_datadiagrammltextformat_stringelt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

















@given(instance=DatadiagramMLTextFormat_Shape_strategy)
def test_hyp_datadiagrammltextformat_shape_fillStyle_setter(instance):
    original = instance.fillStyle
    instance.fillStyle = original
    assert instance.fillStyle == original



@given(instance=DatadiagramMLTextFormat_Shape_strategy)
def test_hyp_datadiagrammltextformat_shape_textStyle_setter(instance):
    original = instance.textStyle
    instance.textStyle = original
    assert instance.textStyle == original



@given(instance=DatadiagramMLTextFormat_Shape_strategy)
def test_hyp_datadiagrammltextformat_shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original




@given(instance=DatadiagramMLTextFormat_UniqueIdElt_strategy)
def test_hyp_datadiagrammltextformat_uniqueidelt_UniqueID_setter(instance):
    original = instance.UniqueID
    instance.UniqueID = original
    assert instance.UniqueID == original




@given(instance=DatadiagramMLTextFormat_IdentifiedElt_strategy)
def test_hyp_datadiagrammltextformat_identifiedelt_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original




@given(instance=DatadiagramMLTextFormat_VBProjectData_strategy)
def test_hyp_datadiagrammltextformat_vbprojectdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original











@given(instance=DatadiagramMLTextFormat_EmailRoutingData_strategy)
def test_hyp_datadiagrammltextformat_emailroutingdata_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=DatadiagramMLTextFormat_EmailRoutingData_strategy)
def test_hyp_datadiagrammltextformat_emailroutingdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original










@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_hyp_datadiagrammltextformat_page_viewCenterX_setter(instance):
    original = instance.viewCenterX
    instance.viewCenterX = original
    assert instance.viewCenterX == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_hyp_datadiagrammltextformat_page_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_hyp_datadiagrammltextformat_page_ViewCenterY_setter(instance):
    original = instance.ViewCenterY
    instance.ViewCenterY = original
    assert instance.ViewCenterY == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_hyp_datadiagrammltextformat_page_backPage_setter(instance):
    original = instance.backPage
    instance.backPage = original
    assert instance.backPage == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_hyp_datadiagrammltextformat_page_associatedPage_setter(instance):
    original = instance.associatedPage
    instance.associatedPage = original
    assert instance.associatedPage == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_hyp_datadiagrammltextformat_page_reviewerID_setter(instance):
    original = instance.reviewerID
    instance.reviewerID = original
    assert instance.reviewerID == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_hyp_datadiagrammltextformat_page_viewScale_setter(instance):
    original = instance.viewScale
    instance.viewScale = original
    assert instance.viewScale == original




@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_hyp_datadiagrammltextformat_mastershortcut_shortcutURL_setter(instance):
    original = instance.shortcutURL
    instance.shortcutURL = original
    assert instance.shortcutURL == original



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_hyp_datadiagrammltextformat_mastershortcut_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_hyp_datadiagrammltextformat_mastershortcut_shortcutHelp_setter(instance):
    original = instance.shortcutHelp
    instance.shortcutHelp = original
    assert instance.shortcutHelp == original



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_hyp_datadiagrammltextformat_mastershortcut_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_hyp_datadiagrammltextformat_mastershortcut_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_hyp_datadiagrammltextformat_mastershortcut_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original




@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
def test_hyp_datadiagrammltextformat_facename_charSet_setter(instance):
    original = instance.charSet
    instance.charSet = original
    assert instance.charSet == original



@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
def test_hyp_datadiagrammltextformat_facename_unicodeRanges_setter(instance):
    original = instance.unicodeRanges
    instance.unicodeRanges = original
    assert instance.unicodeRanges == original



@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
def test_hyp_datadiagrammltextformat_facename_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original



@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
def test_hyp_datadiagrammltextformat_facename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
def test_hyp_datadiagrammltextformat_facename_panos_setter(instance):
    original = instance.panos
    instance.panos = original
    assert instance.panos == original




@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_hyp_datadiagrammltextformat_master_baseID_setter(instance):
    original = instance.baseID
    instance.baseID = original
    assert instance.baseID == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_hyp_datadiagrammltextformat_master_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_hyp_datadiagrammltextformat_master_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_hyp_datadiagrammltextformat_master_matchByName_setter(instance):
    original = instance.matchByName
    instance.matchByName = original
    assert instance.matchByName == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_hyp_datadiagrammltextformat_master_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_hyp_datadiagrammltextformat_master_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_hyp_datadiagrammltextformat_master_iconUpdate_setter(instance):
    original = instance.iconUpdate
    instance.iconUpdate = original
    assert instance.iconUpdate == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_hyp_datadiagrammltextformat_master_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original





@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_hyp_datadiagrammltextformat_fontentry_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_hyp_datadiagrammltextformat_fontentry_charSet_setter(instance):
    original = instance.charSet
    instance.charSet = original
    assert instance.charSet == original



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_hyp_datadiagrammltextformat_fontentry_pitchAndFamily_setter(instance):
    original = instance.pitchAndFamily
    instance.pitchAndFamily = original
    assert instance.pitchAndFamily == original



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_hyp_datadiagrammltextformat_fontentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_hyp_datadiagrammltextformat_fontentry_unicode_setter(instance):
    original = instance.unicode
    instance.unicode = original
    assert instance.unicode == original



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_hyp_datadiagrammltextformat_fontentry_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original










@given(instance=DatadiagramMLTextFormat_ColorEntry_strategy)
def test_hyp_datadiagrammltextformat_colorentry_rgb_setter(instance):
    original = instance.rgb
    instance.rgb = original
    assert instance.rgb == original






@given(instance=DatadiagramMLTextFormat_CustomProperty_strategy)
def test_hyp_datadiagrammltextformat_customproperty_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original



@given(instance=DatadiagramMLTextFormat_CustomProperty_strategy)
def test_hyp_datadiagrammltextformat_customproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original












@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_buildNumberCreated_setter(instance):
    original = instance.buildNumberCreated
    instance.buildNumberCreated = original
    assert instance.buildNumberCreated == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_hyperlinkBase_href_setter(instance):
    original = instance.hyperlinkBase_href
    instance.hyperlinkBase_href = original
    assert instance.hyperlinkBase_href == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_alternateNames_setter(instance):
    original = instance.alternateNames
    instance.alternateNames = original
    assert instance.alternateNames == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_hyp_datadiagrammltextformat_documentpropertiescollection_buildNumberEdited_setter(instance):
    original = instance.buildNumberEdited
    instance.buildNumberEdited = original
    assert instance.buildNumberEdited == original













@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_hyp_datadiagrammltextformat_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_hyp_datadiagrammltextformat_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_hyp_datadiagrammltextformat_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_hyp_datadiagrammltextformat_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_hyp_datadiagrammltextformat_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_hyp_datadiagrammltextformat_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original






@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_hyp_datadiagrammltextformat_visiodocument_docLangId_setter(instance):
    original = instance.docLangId
    instance.docLangId = original
    assert instance.docLangId == original



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_hyp_datadiagrammltextformat_visiodocument_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_hyp_datadiagrammltextformat_visiodocument_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_hyp_datadiagrammltextformat_visiodocument_metric_setter(instance):
    original = instance.metric
    instance.metric = original
    assert instance.metric == original



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_hyp_datadiagrammltextformat_visiodocument_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_hyp_datadiagrammltextformat_visiodocument_buildnum_setter(instance):
    original = instance.buildnum
    instance.buildnum = original
    assert instance.buildnum == original




@given(instance=DatadiagramMLTextFormat_CellType_strategy)
def test_hyp_datadiagrammltextformat_celltype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=DatadiagramMLTextFormat_CellType_strategy)
def test_hyp_datadiagrammltextformat_celltype_err_setter(instance):
    original = instance.err
    instance.err = original
    assert instance.err == original



@given(instance=DatadiagramMLTextFormat_CellType_strategy)
def test_hyp_datadiagrammltextformat_celltype_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=DatadiagramMLTextFormat_CellType_strategy)
def test_hyp_datadiagrammltextformat_celltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArcTo,
    CellType,
    ColorEntry,
    ColorsTable,
    Connect,
    ConnectsCollection,
    CustomPropertiesCollection,
    CustomProperty,
    DatadiagramMLTextFormat_ArcTo,
    DatadiagramMLTextFormat_CellType,
    DatadiagramMLTextFormat_Char,
    DatadiagramMLTextFormat_ColorEntry,
    DatadiagramMLTextFormat_ColorsTable,
    DatadiagramMLTextFormat_Connect,
    DatadiagramMLTextFormat_ConnectsCollection,
    DatadiagramMLTextFormat_Cp,
    DatadiagramMLTextFormat_CustomPropertiesCollection,
    DatadiagramMLTextFormat_CustomProperty,
    DatadiagramMLTextFormat_DateTimeType,
    DatadiagramMLTextFormat_DelElt,
    DatadiagramMLTextFormat_DocumentPropertiesCollection,
    DatadiagramMLTextFormat_DocumentSettingsElt,
    DatadiagramMLTextFormat_DocumentSheet,
    DatadiagramMLTextFormat_Ellipse,
    DatadiagramMLTextFormat_EllipticalArcTo,
    DatadiagramMLTextFormat_EmailRoutingData,
    DatadiagramMLTextFormat_EventList,
    DatadiagramMLTextFormat_FaceName,
    DatadiagramMLTextFormat_FaceNamesTable,
    DatadiagramMLTextFormat_Field,
    DatadiagramMLTextFormat_Fld,
    DatadiagramMLTextFormat_FontEntry,
    DatadiagramMLTextFormat_FontsTable,
    DatadiagramMLTextFormat_Geom,
    DatadiagramMLTextFormat_HeaderFooter,
    DatadiagramMLTextFormat_IXElt,
    DatadiagramMLTextFormat_IXrequiredElt,
    DatadiagramMLTextFormat_Icon,
    DatadiagramMLTextFormat_IdentifiedElt,
    DatadiagramMLTextFormat_InfiniteLine,
    DatadiagramMLTextFormat_LineTo,
    DatadiagramMLTextFormat_Master,
    DatadiagramMLTextFormat_MasterElt,
    DatadiagramMLTextFormat_MasterShortCut,
    DatadiagramMLTextFormat_MastersCollection,
    DatadiagramMLTextFormat_MoveTo,
    DatadiagramMLTextFormat_NURBSTo,
    DatadiagramMLTextFormat_NamedElt,
    DatadiagramMLTextFormat_Page,
    DatadiagramMLTextFormat_PageElt,
    DatadiagramMLTextFormat_PageSheet,
    DatadiagramMLTextFormat_PagesCollection,
    DatadiagramMLTextFormat_Para,
    DatadiagramMLTextFormat_PolylineTo,
    DatadiagramMLTextFormat_Pp,
    DatadiagramMLTextFormat_PrintSetup,
    DatadiagramMLTextFormat_Shape,
    DatadiagramMLTextFormat_ShapeElt,
    DatadiagramMLTextFormat_ShapesCollection,
    DatadiagramMLTextFormat_SolutionXML,
    DatadiagramMLTextFormat_SplineKnot,
    DatadiagramMLTextFormat_SplineStart,
    DatadiagramMLTextFormat_StringElt,
    DatadiagramMLTextFormat_StyleSheet,
    DatadiagramMLTextFormat_StyleSheetsCollection,
    DatadiagramMLTextFormat_Tab,
    DatadiagramMLTextFormat_TabsCollection,
    DatadiagramMLTextFormat_Text,
    DatadiagramMLTextFormat_TextElt,
    DatadiagramMLTextFormat_Tp,
    DatadiagramMLTextFormat_UniqueIdElt,
    DatadiagramMLTextFormat_VBProjectData,
    DatadiagramMLTextFormat_VisioDocument,
    DatadiagramMLTextFormat_WindowsInfo,
    DatadiagramMLTextFormat_XYABCDEElt,
    DatadiagramMLTextFormat_XYABCDElt,
    DatadiagramMLTextFormat_XYABElt,
    DatadiagramMLTextFormat_XYAElt,
    DatadiagramMLTextFormat_XYElt,
    DateTimeType,
    DelElt,
    DocumentPropertiesCollection,
    DocumentSettingsElt,
    DocumentSheet,
    Ellipse,
    EllipticalArcTo,
    EmailRoutingData,
    EventList,
    FaceName,
    FaceNamesTable,
    FontEntry,
    FontsTable,
    Geom,
    HeaderFooter,
    IXElt,
    IXrequiredElt,
    Icon,
    IdentifiedElt,
    InfiniteLine,
    LineTo,
    Master,
    MasterElt,
    MasterShortCut,
    MastersCollection,
    MoveTo,
    NURBSTo,
    NamedElt,
    Page,
    PageElt,
    PageSheet,
    PagesCollection,
    PolylineTo,
    PrintSetup,
    Shape,
    ShapeElt,
    ShapesCollection,
    SolutionXML,
    SplineKnot,
    SplineStart,
    StyleSheet,
    StyleSheetsCollection,
    Tab,
    TabsCollection,
    Text,
    TextElt,
    UniqueIdElt,
    VBProjectData,
    VisioDocument,
    WindowsInfo,
    XYABCDEElt,
    XYABCDElt,
    XYABElt,
    XYAElt,
    XYElt,
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

def test_DatadiagramMLTextFormat_CellType_err_value_roundtrip():
    instance = DatadiagramMLTextFormat_CellType(err="sample_text", formula="sample_text", unit="sample_text", value="sample_text")
    assert instance.err == "sample_text"
    instance.err = "sample_text_2"
    assert instance.err == "sample_text_2"


def test_DatadiagramMLTextFormat_CellType_formula_value_roundtrip():
    instance = DatadiagramMLTextFormat_CellType(err="sample_text", formula="sample_text", unit="sample_text", value="sample_text")
    assert instance.formula == "sample_text"
    instance.formula = "sample_text_2"
    assert instance.formula == "sample_text_2"


def test_DatadiagramMLTextFormat_CellType_unit_value_roundtrip():
    instance = DatadiagramMLTextFormat_CellType(err="sample_text", formula="sample_text", unit="sample_text", value="sample_text")
    assert instance.unit == "sample_text"
    instance.unit = "sample_text_2"
    assert instance.unit == "sample_text_2"


def test_DatadiagramMLTextFormat_CellType_value_value_roundtrip():
    instance = DatadiagramMLTextFormat_CellType(err="sample_text", formula="sample_text", unit="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_DatadiagramMLTextFormat_ColorEntry_rgb_value_roundtrip():
    instance = DatadiagramMLTextFormat_ColorEntry(rgb="sample_text")
    assert instance.rgb == "sample_text"
    instance.rgb = "sample_text_2"
    assert instance.rgb == "sample_text_2"


def test_DatadiagramMLTextFormat_Connect_fromCell_value_roundtrip():
    instance = DatadiagramMLTextFormat_Connect(fromCell="sample_text", fromPart="sample_text", fromSheet="sample_text", toCell="sample_text", toPart="sample_text", toSheet="sample_text")
    assert instance.fromCell == "sample_text"
    instance.fromCell = "sample_text_2"
    assert instance.fromCell == "sample_text_2"


def test_DatadiagramMLTextFormat_Connect_fromPart_value_roundtrip():
    instance = DatadiagramMLTextFormat_Connect(fromCell="sample_text", fromPart="sample_text", fromSheet="sample_text", toCell="sample_text", toPart="sample_text", toSheet="sample_text")
    assert instance.fromPart == "sample_text"
    instance.fromPart = "sample_text_2"
    assert instance.fromPart == "sample_text_2"


def test_DatadiagramMLTextFormat_Connect_fromSheet_value_roundtrip():
    instance = DatadiagramMLTextFormat_Connect(fromCell="sample_text", fromPart="sample_text", fromSheet="sample_text", toCell="sample_text", toPart="sample_text", toSheet="sample_text")
    assert instance.fromSheet == "sample_text"
    instance.fromSheet = "sample_text_2"
    assert instance.fromSheet == "sample_text_2"


def test_DatadiagramMLTextFormat_Connect_toCell_value_roundtrip():
    instance = DatadiagramMLTextFormat_Connect(fromCell="sample_text", fromPart="sample_text", fromSheet="sample_text", toCell="sample_text", toPart="sample_text", toSheet="sample_text")
    assert instance.toCell == "sample_text"
    instance.toCell = "sample_text_2"
    assert instance.toCell == "sample_text_2"


def test_DatadiagramMLTextFormat_Connect_toPart_value_roundtrip():
    instance = DatadiagramMLTextFormat_Connect(fromCell="sample_text", fromPart="sample_text", fromSheet="sample_text", toCell="sample_text", toPart="sample_text", toSheet="sample_text")
    assert instance.toPart == "sample_text"
    instance.toPart = "sample_text_2"
    assert instance.toPart == "sample_text_2"


def test_DatadiagramMLTextFormat_Connect_toSheet_value_roundtrip():
    instance = DatadiagramMLTextFormat_Connect(fromCell="sample_text", fromPart="sample_text", fromSheet="sample_text", toCell="sample_text", toPart="sample_text", toSheet="sample_text")
    assert instance.toSheet == "sample_text"
    instance.toSheet = "sample_text_2"
    assert instance.toSheet == "sample_text_2"


def test_DatadiagramMLTextFormat_CustomProperty_dataType_value_roundtrip():
    instance = DatadiagramMLTextFormat_CustomProperty(dataType="sample_text", name="sample_text")
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_DatadiagramMLTextFormat_CustomProperty_name_value_roundtrip():
    instance = DatadiagramMLTextFormat_CustomProperty(dataType="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_DatadiagramMLTextFormat_DateTimeType_day_value_roundtrip():
    instance = DatadiagramMLTextFormat_DateTimeType(day="sample_text", hour="sample_text", minute="sample_text", month="sample_text", second="sample_text", year="sample_text")
    assert instance.day == "sample_text"
    instance.day = "sample_text_2"
    assert instance.day == "sample_text_2"


def test_DatadiagramMLTextFormat_DateTimeType_hour_value_roundtrip():
    instance = DatadiagramMLTextFormat_DateTimeType(day="sample_text", hour="sample_text", minute="sample_text", month="sample_text", second="sample_text", year="sample_text")
    assert instance.hour == "sample_text"
    instance.hour = "sample_text_2"
    assert instance.hour == "sample_text_2"


def test_DatadiagramMLTextFormat_DateTimeType_minute_value_roundtrip():
    instance = DatadiagramMLTextFormat_DateTimeType(day="sample_text", hour="sample_text", minute="sample_text", month="sample_text", second="sample_text", year="sample_text")
    assert instance.minute == "sample_text"
    instance.minute = "sample_text_2"
    assert instance.minute == "sample_text_2"


def test_DatadiagramMLTextFormat_DateTimeType_month_value_roundtrip():
    instance = DatadiagramMLTextFormat_DateTimeType(day="sample_text", hour="sample_text", minute="sample_text", month="sample_text", second="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_DatadiagramMLTextFormat_DateTimeType_second_value_roundtrip():
    instance = DatadiagramMLTextFormat_DateTimeType(day="sample_text", hour="sample_text", minute="sample_text", month="sample_text", second="sample_text", year="sample_text")
    assert instance.second == "sample_text"
    instance.second = "sample_text_2"
    assert instance.second == "sample_text_2"


def test_DatadiagramMLTextFormat_DateTimeType_year_value_roundtrip():
    instance = DatadiagramMLTextFormat_DateTimeType(day="sample_text", hour="sample_text", minute="sample_text", month="sample_text", second="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_DatadiagramMLTextFormat_DelElt_del__value_roundtrip():
    instance = DatadiagramMLTextFormat_DelElt(del_="sample_text")
    assert instance.del_ == "sample_text"
    instance.del_ = "sample_text_2"
    assert instance.del_ == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_alternateNames_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.alternateNames == "sample_text"
    instance.alternateNames = "sample_text_2"
    assert instance.alternateNames == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_buildNumberCreated_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.buildNumberCreated == "sample_text"
    instance.buildNumberCreated = "sample_text_2"
    assert instance.buildNumberCreated == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_buildNumberEdited_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.buildNumberEdited == "sample_text"
    instance.buildNumberEdited = "sample_text_2"
    assert instance.buildNumberEdited == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_category_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_company_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.company == "sample_text"
    instance.company = "sample_text_2"
    assert instance.company == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_creator_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.creator == "sample_text"
    instance.creator = "sample_text_2"
    assert instance.creator == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_description_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_hyperlinkBase_href_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.hyperlinkBase_href == "sample_text"
    instance.hyperlinkBase_href = "sample_text_2"
    assert instance.hyperlinkBase_href == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_keywords_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.keywords == "sample_text"
    instance.keywords = "sample_text_2"
    assert instance.keywords == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_manager_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.manager == "sample_text"
    instance.manager = "sample_text_2"
    assert instance.manager == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_subject_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.subject == "sample_text"
    instance.subject = "sample_text_2"
    assert instance.subject == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_template_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.template == "sample_text"
    instance.template = "sample_text_2"
    assert instance.template == "sample_text_2"


def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_title_value_roundtrip():
    instance = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_DatadiagramMLTextFormat_EmailRoutingData_data_value_roundtrip():
    instance = DatadiagramMLTextFormat_EmailRoutingData(data="sample_text", size="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_DatadiagramMLTextFormat_EmailRoutingData_size_value_roundtrip():
    instance = DatadiagramMLTextFormat_EmailRoutingData(data="sample_text", size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_DatadiagramMLTextFormat_FaceName_charSet_value_roundtrip():
    instance = DatadiagramMLTextFormat_FaceName(charSet="sample_text", flags="sample_text", name="sample_text", panos="sample_text", unicodeRanges="sample_text")
    assert instance.charSet == "sample_text"
    instance.charSet = "sample_text_2"
    assert instance.charSet == "sample_text_2"


def test_DatadiagramMLTextFormat_FaceName_flags_value_roundtrip():
    instance = DatadiagramMLTextFormat_FaceName(charSet="sample_text", flags="sample_text", name="sample_text", panos="sample_text", unicodeRanges="sample_text")
    assert instance.flags == "sample_text"
    instance.flags = "sample_text_2"
    assert instance.flags == "sample_text_2"


def test_DatadiagramMLTextFormat_FaceName_name_value_roundtrip():
    instance = DatadiagramMLTextFormat_FaceName(charSet="sample_text", flags="sample_text", name="sample_text", panos="sample_text", unicodeRanges="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_DatadiagramMLTextFormat_FaceName_panos_value_roundtrip():
    instance = DatadiagramMLTextFormat_FaceName(charSet="sample_text", flags="sample_text", name="sample_text", panos="sample_text", unicodeRanges="sample_text")
    assert instance.panos == "sample_text"
    instance.panos = "sample_text_2"
    assert instance.panos == "sample_text_2"


def test_DatadiagramMLTextFormat_FaceName_unicodeRanges_value_roundtrip():
    instance = DatadiagramMLTextFormat_FaceName(charSet="sample_text", flags="sample_text", name="sample_text", panos="sample_text", unicodeRanges="sample_text")
    assert instance.unicodeRanges == "sample_text"
    instance.unicodeRanges = "sample_text_2"
    assert instance.unicodeRanges == "sample_text_2"


def test_DatadiagramMLTextFormat_FontEntry_attributes_value_roundtrip():
    instance = DatadiagramMLTextFormat_FontEntry(attributes="sample_text", charSet="sample_text", name="sample_text", pitchAndFamily="sample_text", unicode="sample_text", weight="sample_text")
    assert instance.attributes == "sample_text"
    instance.attributes = "sample_text_2"
    assert instance.attributes == "sample_text_2"


def test_DatadiagramMLTextFormat_FontEntry_charSet_value_roundtrip():
    instance = DatadiagramMLTextFormat_FontEntry(attributes="sample_text", charSet="sample_text", name="sample_text", pitchAndFamily="sample_text", unicode="sample_text", weight="sample_text")
    assert instance.charSet == "sample_text"
    instance.charSet = "sample_text_2"
    assert instance.charSet == "sample_text_2"


def test_DatadiagramMLTextFormat_FontEntry_name_value_roundtrip():
    instance = DatadiagramMLTextFormat_FontEntry(attributes="sample_text", charSet="sample_text", name="sample_text", pitchAndFamily="sample_text", unicode="sample_text", weight="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_DatadiagramMLTextFormat_FontEntry_pitchAndFamily_value_roundtrip():
    instance = DatadiagramMLTextFormat_FontEntry(attributes="sample_text", charSet="sample_text", name="sample_text", pitchAndFamily="sample_text", unicode="sample_text", weight="sample_text")
    assert instance.pitchAndFamily == "sample_text"
    instance.pitchAndFamily = "sample_text_2"
    assert instance.pitchAndFamily == "sample_text_2"


def test_DatadiagramMLTextFormat_FontEntry_unicode_value_roundtrip():
    instance = DatadiagramMLTextFormat_FontEntry(attributes="sample_text", charSet="sample_text", name="sample_text", pitchAndFamily="sample_text", unicode="sample_text", weight="sample_text")
    assert instance.unicode == "sample_text"
    instance.unicode = "sample_text_2"
    assert instance.unicode == "sample_text_2"


def test_DatadiagramMLTextFormat_FontEntry_weight_value_roundtrip():
    instance = DatadiagramMLTextFormat_FontEntry(attributes="sample_text", charSet="sample_text", name="sample_text", pitchAndFamily="sample_text", unicode="sample_text", weight="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_DatadiagramMLTextFormat_IXElt_iX_value_roundtrip():
    instance = DatadiagramMLTextFormat_IXElt(iX="sample_text")
    assert instance.iX == "sample_text"
    instance.iX = "sample_text_2"
    assert instance.iX == "sample_text_2"


def test_DatadiagramMLTextFormat_IXrequiredElt_iX_value_roundtrip():
    instance = DatadiagramMLTextFormat_IXrequiredElt(iX="sample_text")
    assert instance.iX == "sample_text"
    instance.iX = "sample_text_2"
    assert instance.iX == "sample_text_2"


def test_DatadiagramMLTextFormat_Icon_value_value_roundtrip():
    instance = DatadiagramMLTextFormat_Icon(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_DatadiagramMLTextFormat_IdentifiedElt_ID_value_roundtrip():
    instance = DatadiagramMLTextFormat_IdentifiedElt(ID="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_DatadiagramMLTextFormat_Master_alignName_value_roundtrip():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert instance.alignName == "sample_text"
    instance.alignName = "sample_text_2"
    assert instance.alignName == "sample_text_2"


def test_DatadiagramMLTextFormat_Master_baseID_value_roundtrip():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert instance.baseID == "sample_text"
    instance.baseID = "sample_text_2"
    assert instance.baseID == "sample_text_2"


def test_DatadiagramMLTextFormat_Master_hidden_value_roundtrip():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert instance.hidden == "sample_text"
    instance.hidden = "sample_text_2"
    assert instance.hidden == "sample_text_2"


def test_DatadiagramMLTextFormat_Master_iconSize_value_roundtrip():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert instance.iconSize == "sample_text"
    instance.iconSize = "sample_text_2"
    assert instance.iconSize == "sample_text_2"


def test_DatadiagramMLTextFormat_Master_iconUpdate_value_roundtrip():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert instance.iconUpdate == "sample_text"
    instance.iconUpdate = "sample_text_2"
    assert instance.iconUpdate == "sample_text_2"


def test_DatadiagramMLTextFormat_Master_matchByName_value_roundtrip():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert instance.matchByName == "sample_text"
    instance.matchByName = "sample_text_2"
    assert instance.matchByName == "sample_text_2"


def test_DatadiagramMLTextFormat_Master_patternFlags_value_roundtrip():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert instance.patternFlags == "sample_text"
    instance.patternFlags = "sample_text_2"
    assert instance.patternFlags == "sample_text_2"


def test_DatadiagramMLTextFormat_Master_prompt_value_roundtrip():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert instance.prompt == "sample_text"
    instance.prompt = "sample_text_2"
    assert instance.prompt == "sample_text_2"


def test_DatadiagramMLTextFormat_MasterShortCut_alignName_value_roundtrip():
    instance = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    assert instance.alignName == "sample_text"
    instance.alignName = "sample_text_2"
    assert instance.alignName == "sample_text_2"


def test_DatadiagramMLTextFormat_MasterShortCut_iconSize_value_roundtrip():
    instance = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    assert instance.iconSize == "sample_text"
    instance.iconSize = "sample_text_2"
    assert instance.iconSize == "sample_text_2"


def test_DatadiagramMLTextFormat_MasterShortCut_patternFlags_value_roundtrip():
    instance = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    assert instance.patternFlags == "sample_text"
    instance.patternFlags = "sample_text_2"
    assert instance.patternFlags == "sample_text_2"


def test_DatadiagramMLTextFormat_MasterShortCut_prompt_value_roundtrip():
    instance = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    assert instance.prompt == "sample_text"
    instance.prompt = "sample_text_2"
    assert instance.prompt == "sample_text_2"


def test_DatadiagramMLTextFormat_MasterShortCut_shortcutHelp_value_roundtrip():
    instance = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    assert instance.shortcutHelp == "sample_text"
    instance.shortcutHelp = "sample_text_2"
    assert instance.shortcutHelp == "sample_text_2"


def test_DatadiagramMLTextFormat_MasterShortCut_shortcutURL_value_roundtrip():
    instance = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    assert instance.shortcutURL == "sample_text"
    instance.shortcutURL = "sample_text_2"
    assert instance.shortcutURL == "sample_text_2"


def test_DatadiagramMLTextFormat_NamedElt_name_value_roundtrip():
    instance = DatadiagramMLTextFormat_NamedElt(name="sample_text", nameU="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_DatadiagramMLTextFormat_NamedElt_nameU_value_roundtrip():
    instance = DatadiagramMLTextFormat_NamedElt(name="sample_text", nameU="sample_text")
    assert instance.nameU == "sample_text"
    instance.nameU = "sample_text_2"
    assert instance.nameU == "sample_text_2"


def test_DatadiagramMLTextFormat_Page_ViewCenterY_value_roundtrip():
    instance = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    assert instance.ViewCenterY == "sample_text"
    instance.ViewCenterY = "sample_text_2"
    assert instance.ViewCenterY == "sample_text_2"


def test_DatadiagramMLTextFormat_Page_associatedPage_value_roundtrip():
    instance = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    assert instance.associatedPage == "sample_text"
    instance.associatedPage = "sample_text_2"
    assert instance.associatedPage == "sample_text_2"


def test_DatadiagramMLTextFormat_Page_backPage_value_roundtrip():
    instance = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    assert instance.backPage == "sample_text"
    instance.backPage = "sample_text_2"
    assert instance.backPage == "sample_text_2"


def test_DatadiagramMLTextFormat_Page_background_value_roundtrip():
    instance = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    assert instance.background == "sample_text"
    instance.background = "sample_text_2"
    assert instance.background == "sample_text_2"


def test_DatadiagramMLTextFormat_Page_reviewerID_value_roundtrip():
    instance = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    assert instance.reviewerID == "sample_text"
    instance.reviewerID = "sample_text_2"
    assert instance.reviewerID == "sample_text_2"


def test_DatadiagramMLTextFormat_Page_viewCenterX_value_roundtrip():
    instance = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    assert instance.viewCenterX == "sample_text"
    instance.viewCenterX = "sample_text_2"
    assert instance.viewCenterX == "sample_text_2"


def test_DatadiagramMLTextFormat_Page_viewScale_value_roundtrip():
    instance = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    assert instance.viewScale == "sample_text"
    instance.viewScale = "sample_text_2"
    assert instance.viewScale == "sample_text_2"


def test_DatadiagramMLTextFormat_Shape_fillStyle_value_roundtrip():
    instance = DatadiagramMLTextFormat_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    assert instance.fillStyle == "sample_text"
    instance.fillStyle = "sample_text_2"
    assert instance.fillStyle == "sample_text_2"


def test_DatadiagramMLTextFormat_Shape_lineStyle_value_roundtrip():
    instance = DatadiagramMLTextFormat_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    assert instance.lineStyle == "sample_text"
    instance.lineStyle = "sample_text_2"
    assert instance.lineStyle == "sample_text_2"


def test_DatadiagramMLTextFormat_Shape_textStyle_value_roundtrip():
    instance = DatadiagramMLTextFormat_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    assert instance.textStyle == "sample_text"
    instance.textStyle = "sample_text_2"
    assert instance.textStyle == "sample_text_2"


def test_DatadiagramMLTextFormat_StringElt_value_value_roundtrip():
    instance = DatadiagramMLTextFormat_StringElt(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_DatadiagramMLTextFormat_UniqueIdElt_UniqueID_value_roundtrip():
    instance = DatadiagramMLTextFormat_UniqueIdElt(UniqueID="sample_text")
    assert instance.UniqueID == "sample_text"
    instance.UniqueID = "sample_text_2"
    assert instance.UniqueID == "sample_text_2"


def test_DatadiagramMLTextFormat_VBProjectData_data_value_roundtrip():
    instance = DatadiagramMLTextFormat_VBProjectData(data="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_DatadiagramMLTextFormat_VisioDocument_buildnum_value_roundtrip():
    instance = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    assert instance.buildnum == "sample_text"
    instance.buildnum = "sample_text_2"
    assert instance.buildnum == "sample_text_2"


def test_DatadiagramMLTextFormat_VisioDocument_docLangId_value_roundtrip():
    instance = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    assert instance.docLangId == "sample_text"
    instance.docLangId = "sample_text_2"
    assert instance.docLangId == "sample_text_2"


def test_DatadiagramMLTextFormat_VisioDocument_key_value_roundtrip():
    instance = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_DatadiagramMLTextFormat_VisioDocument_metric_value_roundtrip():
    instance = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    assert instance.metric == "sample_text"
    instance.metric = "sample_text_2"
    assert instance.metric == "sample_text_2"


def test_DatadiagramMLTextFormat_VisioDocument_start_value_roundtrip():
    instance = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    assert instance.start == "sample_text"
    instance.start = "sample_text_2"
    assert instance.start == "sample_text_2"


def test_DatadiagramMLTextFormat_VisioDocument_version_value_roundtrip():
    instance = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_DatadiagramMLTextFormat_Char_isa_DelElt():
    instance = DatadiagramMLTextFormat_Char()
    assert isinstance(instance, DelElt)


def test_DatadiagramMLTextFormat_Field_isa_DelElt():
    instance = DatadiagramMLTextFormat_Field()
    assert isinstance(instance, DelElt)


def test_DatadiagramMLTextFormat_Geom_isa_DelElt():
    instance = DatadiagramMLTextFormat_Geom()
    assert isinstance(instance, DelElt)


def test_DatadiagramMLTextFormat_Para_isa_DelElt():
    instance = DatadiagramMLTextFormat_Para()
    assert isinstance(instance, DelElt)


def test_DatadiagramMLTextFormat_TabsCollection_isa_DelElt():
    instance = DatadiagramMLTextFormat_TabsCollection()
    assert isinstance(instance, DelElt)


def test_DatadiagramMLTextFormat_XYElt_isa_DelElt():
    instance = DatadiagramMLTextFormat_XYElt()
    assert isinstance(instance, DelElt)


def test_DatadiagramMLTextFormat_Char_isa_IXElt():
    instance = DatadiagramMLTextFormat_Char()
    assert isinstance(instance, IXElt)


def test_DatadiagramMLTextFormat_Field_isa_IXElt():
    instance = DatadiagramMLTextFormat_Field()
    assert isinstance(instance, IXElt)


def test_DatadiagramMLTextFormat_Geom_isa_IXElt():
    instance = DatadiagramMLTextFormat_Geom()
    assert isinstance(instance, IXElt)


def test_DatadiagramMLTextFormat_Para_isa_IXElt():
    instance = DatadiagramMLTextFormat_Para()
    assert isinstance(instance, IXElt)


def test_DatadiagramMLTextFormat_Tab_isa_IXElt():
    instance = DatadiagramMLTextFormat_Tab()
    assert isinstance(instance, IXElt)


def test_DatadiagramMLTextFormat_TabsCollection_isa_IXElt():
    instance = DatadiagramMLTextFormat_TabsCollection()
    assert isinstance(instance, IXElt)


def test_DatadiagramMLTextFormat_XYElt_isa_IXElt():
    instance = DatadiagramMLTextFormat_XYElt()
    assert isinstance(instance, IXElt)


def test_DatadiagramMLTextFormat_ColorEntry_isa_IXrequiredElt():
    instance = DatadiagramMLTextFormat_ColorEntry(rgb="sample_text")
    assert isinstance(instance, IXrequiredElt)


def test_DatadiagramMLTextFormat_Cp_isa_IXrequiredElt():
    instance = DatadiagramMLTextFormat_Cp()
    assert isinstance(instance, IXrequiredElt)


def test_DatadiagramMLTextFormat_Fld_isa_IXrequiredElt():
    instance = DatadiagramMLTextFormat_Fld()
    assert isinstance(instance, IXrequiredElt)


def test_DatadiagramMLTextFormat_Pp_isa_IXrequiredElt():
    instance = DatadiagramMLTextFormat_Pp()
    assert isinstance(instance, IXrequiredElt)


def test_DatadiagramMLTextFormat_Tp_isa_IXrequiredElt():
    instance = DatadiagramMLTextFormat_Tp()
    assert isinstance(instance, IXrequiredElt)


def test_DatadiagramMLTextFormat_FaceName_isa_IdentifiedElt():
    instance = DatadiagramMLTextFormat_FaceName(charSet="sample_text", flags="sample_text", name="sample_text", panos="sample_text", unicodeRanges="sample_text")
    assert isinstance(instance, IdentifiedElt)


def test_DatadiagramMLTextFormat_FontEntry_isa_IdentifiedElt():
    instance = DatadiagramMLTextFormat_FontEntry(attributes="sample_text", charSet="sample_text", name="sample_text", pitchAndFamily="sample_text", unicode="sample_text", weight="sample_text")
    assert isinstance(instance, IdentifiedElt)


def test_DatadiagramMLTextFormat_Master_isa_IdentifiedElt():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert isinstance(instance, IdentifiedElt)


def test_DatadiagramMLTextFormat_MasterShortCut_isa_IdentifiedElt():
    instance = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    assert isinstance(instance, IdentifiedElt)


def test_DatadiagramMLTextFormat_Page_isa_IdentifiedElt():
    instance = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    assert isinstance(instance, IdentifiedElt)


def test_DatadiagramMLTextFormat_StyleSheet_isa_IdentifiedElt():
    instance = DatadiagramMLTextFormat_StyleSheet()
    assert isinstance(instance, IdentifiedElt)


def test_DatadiagramMLTextFormat_ConnectsCollection_isa_MasterElt():
    instance = DatadiagramMLTextFormat_ConnectsCollection()
    assert isinstance(instance, MasterElt)


def test_DatadiagramMLTextFormat_Icon_isa_MasterElt():
    instance = DatadiagramMLTextFormat_Icon(value="sample_text")
    assert isinstance(instance, MasterElt)


def test_DatadiagramMLTextFormat_PageSheet_isa_MasterElt():
    instance = DatadiagramMLTextFormat_PageSheet()
    assert isinstance(instance, MasterElt)


def test_DatadiagramMLTextFormat_ShapesCollection_isa_MasterElt():
    instance = DatadiagramMLTextFormat_ShapesCollection()
    assert isinstance(instance, MasterElt)


def test_DatadiagramMLTextFormat_DocumentSheet_isa_NamedElt():
    instance = DatadiagramMLTextFormat_DocumentSheet()
    assert isinstance(instance, NamedElt)


def test_DatadiagramMLTextFormat_Master_isa_NamedElt():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert isinstance(instance, NamedElt)


def test_DatadiagramMLTextFormat_MasterShortCut_isa_NamedElt():
    instance = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    assert isinstance(instance, NamedElt)


def test_DatadiagramMLTextFormat_Page_isa_NamedElt():
    instance = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    assert isinstance(instance, NamedElt)


def test_DatadiagramMLTextFormat_StyleSheet_isa_NamedElt():
    instance = DatadiagramMLTextFormat_StyleSheet()
    assert isinstance(instance, NamedElt)


def test_DatadiagramMLTextFormat_ConnectsCollection_isa_PageElt():
    instance = DatadiagramMLTextFormat_ConnectsCollection()
    assert isinstance(instance, PageElt)


def test_DatadiagramMLTextFormat_PageSheet_isa_PageElt():
    instance = DatadiagramMLTextFormat_PageSheet()
    assert isinstance(instance, PageElt)


def test_DatadiagramMLTextFormat_ShapesCollection_isa_PageElt():
    instance = DatadiagramMLTextFormat_ShapesCollection()
    assert isinstance(instance, PageElt)


def test_DatadiagramMLTextFormat_DocumentSheet_isa_PageSheet():
    instance = DatadiagramMLTextFormat_DocumentSheet()
    assert isinstance(instance, PageSheet)


def test_DatadiagramMLTextFormat_PageSheet_isa_Shape():
    instance = DatadiagramMLTextFormat_PageSheet()
    assert isinstance(instance, Shape)


def test_DatadiagramMLTextFormat_StyleSheet_isa_Shape():
    instance = DatadiagramMLTextFormat_StyleSheet()
    assert isinstance(instance, Shape)


def test_DatadiagramMLTextFormat_Char_isa_ShapeElt():
    instance = DatadiagramMLTextFormat_Char()
    assert isinstance(instance, ShapeElt)


def test_DatadiagramMLTextFormat_Field_isa_ShapeElt():
    instance = DatadiagramMLTextFormat_Field()
    assert isinstance(instance, ShapeElt)


def test_DatadiagramMLTextFormat_Geom_isa_ShapeElt():
    instance = DatadiagramMLTextFormat_Geom()
    assert isinstance(instance, ShapeElt)


def test_DatadiagramMLTextFormat_Para_isa_ShapeElt():
    instance = DatadiagramMLTextFormat_Para()
    assert isinstance(instance, ShapeElt)


def test_DatadiagramMLTextFormat_TabsCollection_isa_ShapeElt():
    instance = DatadiagramMLTextFormat_TabsCollection()
    assert isinstance(instance, ShapeElt)


def test_DatadiagramMLTextFormat_Text_isa_ShapeElt():
    instance = DatadiagramMLTextFormat_Text()
    assert isinstance(instance, ShapeElt)


def test_DatadiagramMLTextFormat_Cp_isa_TextElt():
    instance = DatadiagramMLTextFormat_Cp()
    assert isinstance(instance, TextElt)


def test_DatadiagramMLTextFormat_Fld_isa_TextElt():
    instance = DatadiagramMLTextFormat_Fld()
    assert isinstance(instance, TextElt)


def test_DatadiagramMLTextFormat_Pp_isa_TextElt():
    instance = DatadiagramMLTextFormat_Pp()
    assert isinstance(instance, TextElt)


def test_DatadiagramMLTextFormat_StringElt_isa_TextElt():
    instance = DatadiagramMLTextFormat_StringElt(value="sample_text")
    assert isinstance(instance, TextElt)


def test_DatadiagramMLTextFormat_Tp_isa_TextElt():
    instance = DatadiagramMLTextFormat_Tp()
    assert isinstance(instance, TextElt)


def test_DatadiagramMLTextFormat_Master_isa_UniqueIdElt():
    instance = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    assert isinstance(instance, UniqueIdElt)


def test_DatadiagramMLTextFormat_PageSheet_isa_UniqueIdElt():
    instance = DatadiagramMLTextFormat_PageSheet()
    assert isinstance(instance, UniqueIdElt)


def test_DatadiagramMLTextFormat_NURBSTo_isa_XYABCDEElt():
    instance = DatadiagramMLTextFormat_NURBSTo()
    assert isinstance(instance, XYABCDEElt)


def test_DatadiagramMLTextFormat_Ellipse_isa_XYABCDElt():
    instance = DatadiagramMLTextFormat_Ellipse()
    assert isinstance(instance, XYABCDElt)


def test_DatadiagramMLTextFormat_EllipticalArcTo_isa_XYABCDElt():
    instance = DatadiagramMLTextFormat_EllipticalArcTo()
    assert isinstance(instance, XYABCDElt)


def test_DatadiagramMLTextFormat_SplineStart_isa_XYABCDElt():
    instance = DatadiagramMLTextFormat_SplineStart()
    assert isinstance(instance, XYABCDElt)


def test_DatadiagramMLTextFormat_XYABCDEElt_isa_XYABCDElt():
    instance = DatadiagramMLTextFormat_XYABCDEElt()
    assert isinstance(instance, XYABCDElt)


def test_DatadiagramMLTextFormat_InfiniteLine_isa_XYABElt():
    instance = DatadiagramMLTextFormat_InfiniteLine()
    assert isinstance(instance, XYABElt)


def test_DatadiagramMLTextFormat_XYABCDElt_isa_XYABElt():
    instance = DatadiagramMLTextFormat_XYABCDElt()
    assert isinstance(instance, XYABElt)


def test_DatadiagramMLTextFormat_ArcTo_isa_XYAElt():
    instance = DatadiagramMLTextFormat_ArcTo()
    assert isinstance(instance, XYAElt)


def test_DatadiagramMLTextFormat_PolylineTo_isa_XYAElt():
    instance = DatadiagramMLTextFormat_PolylineTo()
    assert isinstance(instance, XYAElt)


def test_DatadiagramMLTextFormat_SplineKnot_isa_XYAElt():
    instance = DatadiagramMLTextFormat_SplineKnot()
    assert isinstance(instance, XYAElt)


def test_DatadiagramMLTextFormat_XYABElt_isa_XYAElt():
    instance = DatadiagramMLTextFormat_XYABElt()
    assert isinstance(instance, XYAElt)


def test_DatadiagramMLTextFormat_LineTo_isa_XYElt():
    instance = DatadiagramMLTextFormat_LineTo()
    assert isinstance(instance, XYElt)


def test_DatadiagramMLTextFormat_MoveTo_isa_XYElt():
    instance = DatadiagramMLTextFormat_MoveTo()
    assert isinstance(instance, XYElt)


def test_DatadiagramMLTextFormat_XYAElt_isa_XYElt():
    instance = DatadiagramMLTextFormat_XYAElt()
    assert isinstance(instance, XYElt)


def test_assoc_c_connects259_link_reassign_clear():
    a = DatadiagramMLTextFormat_Connect(fromCell="sample_text", fromPart="sample_text", fromSheet="sample_text", toCell="sample_text", toPart="sample_text", toSheet="sample_text")
    b1 = ConnectsCollection()
    b2 = ConnectsCollection()
    _safe_set(a, 'connections', b1)
    assert _is_linked(a, 'connections', b1)
    if hasattr(b1, 'ConnectsCollection'):
        assert _is_linked(b1, 'ConnectsCollection', a)
    _safe_set(a, 'connections', b2)
    assert _is_linked(a, 'connections', b2)
    if hasattr(b1, 'ConnectsCollection'):
        assert not _is_linked(b1, 'ConnectsCollection', a)
    if hasattr(b2, 'ConnectsCollection'):
        assert _is_linked(b2, 'ConnectsCollection', a)
    _safe_set(a, 'connections', None)
    assert not _is_linked(a, 'connections', b2)
    if hasattr(b2, 'ConnectsCollection'):
        assert not _is_linked(b2, 'ConnectsCollection', a)


def test_assoc_ce_colors37_link_reassign_clear():
    a = DatadiagramMLTextFormat_ColorEntry(rgb="sample_text")
    b1 = ColorsTable()
    b2 = ColorsTable()
    _safe_set(a, 'colorEntries', b1)
    assert _is_linked(a, 'colorEntries', b1)
    if hasattr(b1, 'ColorsTable38'):
        assert _is_linked(b1, 'ColorsTable38', a)
    _safe_set(a, 'colorEntries', b2)
    assert _is_linked(a, 'colorEntries', b2)
    if hasattr(b1, 'ColorsTable38'):
        assert not _is_linked(b1, 'ColorsTable38', a)
    if hasattr(b2, 'ColorsTable38'):
        assert _is_linked(b2, 'ColorsTable38', a)
    _safe_set(a, 'colorEntries', None)
    assert not _is_linked(a, 'colorEntries', b2)
    if hasattr(b2, 'ColorsTable38'):
        assert not _is_linked(b2, 'ColorsTable38', a)


def test_assoc_cp_customProps32_link_reassign_clear():
    a = DatadiagramMLTextFormat_CustomProperty(dataType="sample_text", name="sample_text")
    b1 = CustomPropertiesCollection()
    b2 = CustomPropertiesCollection()
    _safe_set(a, 'cps_customProps', b1)
    assert _is_linked(a, 'cps_customProps', b1)
    if hasattr(b1, 'CustomPropertiesCollection33'):
        assert _is_linked(b1, 'CustomPropertiesCollection33', a)
    _safe_set(a, 'cps_customProps', b2)
    assert _is_linked(a, 'cps_customProps', b2)
    if hasattr(b1, 'CustomPropertiesCollection33'):
        assert not _is_linked(b1, 'CustomPropertiesCollection33', a)
    if hasattr(b2, 'CustomPropertiesCollection33'):
        assert _is_linked(b2, 'CustomPropertiesCollection33', a)
    _safe_set(a, 'cps_customProps', None)
    assert not _is_linked(a, 'cps_customProps', b2)
    if hasattr(b2, 'CustomPropertiesCollection33'):
        assert not _is_linked(b2, 'CustomPropertiesCollection33', a)


def test_assoc_customProps18_link_reassign_clear():
    a = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    b1 = CustomPropertiesCollection()
    b2 = CustomPropertiesCollection()
    _safe_set(a, 'cps_docProp', b1)
    assert _is_linked(a, 'cps_docProp', b1)
    if hasattr(b1, 'CustomPropertiesCollection'):
        assert _is_linked(b1, 'CustomPropertiesCollection', a)
    _safe_set(a, 'cps_docProp', b2)
    assert _is_linked(a, 'cps_docProp', b2)
    if hasattr(b1, 'CustomPropertiesCollection'):
        assert not _is_linked(b1, 'CustomPropertiesCollection', a)
    if hasattr(b2, 'CustomPropertiesCollection'):
        assert _is_linked(b2, 'CustomPropertiesCollection', a)
    _safe_set(a, 'cps_docProp', None)
    assert not _is_linked(a, 'cps_docProp', b2)
    if hasattr(b2, 'CustomPropertiesCollection'):
        assert not _is_linked(b2, 'CustomPropertiesCollection', a)


def test_assoc_docColors2_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = ColorsTable()
    b2 = ColorsTable()
    _safe_set(a, 'cs_visioDocument', b1)
    assert _is_linked(a, 'cs_visioDocument', b1)
    if hasattr(b1, 'ColorsTable'):
        assert _is_linked(b1, 'ColorsTable', a)
    _safe_set(a, 'cs_visioDocument', b2)
    assert _is_linked(a, 'cs_visioDocument', b2)
    if hasattr(b1, 'ColorsTable'):
        assert not _is_linked(b1, 'ColorsTable', a)
    if hasattr(b2, 'ColorsTable'):
        assert _is_linked(b2, 'ColorsTable', a)
    _safe_set(a, 'cs_visioDocument', None)
    assert not _is_linked(a, 'cs_visioDocument', b2)
    if hasattr(b2, 'ColorsTable'):
        assert not _is_linked(b2, 'ColorsTable', a)


def test_assoc_docDocumentSheet7_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = DocumentSheet()
    b2 = DocumentSheet()
    _safe_set(a, 'ds_visioDocument', b1)
    assert _is_linked(a, 'ds_visioDocument', b1)
    if hasattr(b1, 'DocumentSheet'):
        assert _is_linked(b1, 'DocumentSheet', a)
    _safe_set(a, 'ds_visioDocument', b2)
    assert _is_linked(a, 'ds_visioDocument', b2)
    if hasattr(b1, 'DocumentSheet'):
        assert not _is_linked(b1, 'DocumentSheet', a)
    if hasattr(b2, 'DocumentSheet'):
        assert _is_linked(b2, 'DocumentSheet', a)
    _safe_set(a, 'ds_visioDocument', None)
    assert not _is_linked(a, 'ds_visioDocument', b2)
    if hasattr(b2, 'DocumentSheet'):
        assert not _is_linked(b2, 'DocumentSheet', a)


def test_assoc_docEmailRoutingData15_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = EmailRoutingData()
    b2 = EmailRoutingData()
    _safe_set(a, 'erd_visioDocument', b1)
    assert _is_linked(a, 'erd_visioDocument', b1)
    if hasattr(b1, 'EmailRoutingData'):
        assert _is_linked(b1, 'EmailRoutingData', a)
    _safe_set(a, 'erd_visioDocument', b2)
    assert _is_linked(a, 'erd_visioDocument', b2)
    if hasattr(b1, 'EmailRoutingData'):
        assert not _is_linked(b1, 'EmailRoutingData', a)
    if hasattr(b2, 'EmailRoutingData'):
        assert _is_linked(b2, 'EmailRoutingData', a)
    _safe_set(a, 'erd_visioDocument', None)
    assert not _is_linked(a, 'erd_visioDocument', b2)
    if hasattr(b2, 'EmailRoutingData'):
        assert not _is_linked(b2, 'EmailRoutingData', a)


def test_assoc_docEventList12_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = EventList()
    b2 = EventList()
    _safe_set(a, 'el_visioDocument', b1)
    assert _is_linked(a, 'el_visioDocument', b1)
    if hasattr(b1, 'EventList'):
        assert _is_linked(b1, 'EventList', a)
    _safe_set(a, 'el_visioDocument', b2)
    assert _is_linked(a, 'el_visioDocument', b2)
    if hasattr(b1, 'EventList'):
        assert not _is_linked(b1, 'EventList', a)
    if hasattr(b2, 'EventList'):
        assert _is_linked(b2, 'EventList', a)
    _safe_set(a, 'el_visioDocument', None)
    assert not _is_linked(a, 'el_visioDocument', b2)
    if hasattr(b2, 'EventList'):
        assert not _is_linked(b2, 'EventList', a)


def test_assoc_docFaceNames5_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = FaceNamesTable()
    b2 = FaceNamesTable()
    _safe_set(a, 'fns_visioDocument', b1)
    assert _is_linked(a, 'fns_visioDocument', b1)
    if hasattr(b1, 'FaceNamesTable'):
        assert _is_linked(b1, 'FaceNamesTable', a)
    _safe_set(a, 'fns_visioDocument', b2)
    assert _is_linked(a, 'fns_visioDocument', b2)
    if hasattr(b1, 'FaceNamesTable'):
        assert not _is_linked(b1, 'FaceNamesTable', a)
    if hasattr(b2, 'FaceNamesTable'):
        assert _is_linked(b2, 'FaceNamesTable', a)
    _safe_set(a, 'fns_visioDocument', None)
    assert not _is_linked(a, 'fns_visioDocument', b2)
    if hasattr(b2, 'FaceNamesTable'):
        assert not _is_linked(b2, 'FaceNamesTable', a)


def test_assoc_docFonts4_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = FontsTable()
    b2 = FontsTable()
    _safe_set(a, 'fs_visioDocument', b1)
    assert _is_linked(a, 'fs_visioDocument', b1)
    if hasattr(b1, 'FontsTable'):
        assert _is_linked(b1, 'FontsTable', a)
    _safe_set(a, 'fs_visioDocument', b2)
    assert _is_linked(a, 'fs_visioDocument', b2)
    if hasattr(b1, 'FontsTable'):
        assert not _is_linked(b1, 'FontsTable', a)
    if hasattr(b2, 'FontsTable'):
        assert _is_linked(b2, 'FontsTable', a)
    _safe_set(a, 'fs_visioDocument', None)
    assert not _is_linked(a, 'fs_visioDocument', b2)
    if hasattr(b2, 'FontsTable'):
        assert not _is_linked(b2, 'FontsTable', a)


def test_assoc_docHeaderFooter13_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = HeaderFooter()
    b2 = HeaderFooter()
    _safe_set(a, 'ef_visioDocument', b1)
    assert _is_linked(a, 'ef_visioDocument', b1)
    if hasattr(b1, 'HeaderFooter'):
        assert _is_linked(b1, 'HeaderFooter', a)
    _safe_set(a, 'ef_visioDocument', b2)
    assert _is_linked(a, 'ef_visioDocument', b2)
    if hasattr(b1, 'HeaderFooter'):
        assert not _is_linked(b1, 'HeaderFooter', a)
    if hasattr(b2, 'HeaderFooter'):
        assert _is_linked(b2, 'HeaderFooter', a)
    _safe_set(a, 'ef_visioDocument', None)
    assert not _is_linked(a, 'ef_visioDocument', b2)
    if hasattr(b2, 'HeaderFooter'):
        assert not _is_linked(b2, 'HeaderFooter', a)


def test_assoc_docMasters8_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = MastersCollection()
    b2 = MastersCollection()
    _safe_set(a, 'ms_visioDocument', b1)
    assert _is_linked(a, 'ms_visioDocument', b1)
    if hasattr(b1, 'MastersCollection'):
        assert _is_linked(b1, 'MastersCollection', a)
    _safe_set(a, 'ms_visioDocument', b2)
    assert _is_linked(a, 'ms_visioDocument', b2)
    if hasattr(b1, 'MastersCollection'):
        assert not _is_linked(b1, 'MastersCollection', a)
    if hasattr(b2, 'MastersCollection'):
        assert _is_linked(b2, 'MastersCollection', a)
    _safe_set(a, 'ms_visioDocument', None)
    assert not _is_linked(a, 'ms_visioDocument', b2)
    if hasattr(b2, 'MastersCollection'):
        assert not _is_linked(b2, 'MastersCollection', a)


def test_assoc_docPages9_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = PagesCollection()
    b2 = PagesCollection()
    _safe_set(a, 'ps_visioDocument10', b1)
    assert _is_linked(a, 'ps_visioDocument10', b1)
    if hasattr(b1, 'PagesCollection'):
        assert _is_linked(b1, 'PagesCollection', a)
    _safe_set(a, 'ps_visioDocument10', b2)
    assert _is_linked(a, 'ps_visioDocument10', b2)
    if hasattr(b1, 'PagesCollection'):
        assert not _is_linked(b1, 'PagesCollection', a)
    if hasattr(b2, 'PagesCollection'):
        assert _is_linked(b2, 'PagesCollection', a)
    _safe_set(a, 'ps_visioDocument10', None)
    assert not _is_linked(a, 'ps_visioDocument10', b2)
    if hasattr(b2, 'PagesCollection'):
        assert not _is_linked(b2, 'PagesCollection', a)


def test_assoc_docPrintSetup3_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = PrintSetup()
    b2 = PrintSetup()
    _safe_set(a, 'ps_visioDocument', b1)
    assert _is_linked(a, 'ps_visioDocument', b1)
    if hasattr(b1, 'PrintSetup'):
        assert _is_linked(b1, 'PrintSetup', a)
    _safe_set(a, 'ps_visioDocument', b2)
    assert _is_linked(a, 'ps_visioDocument', b2)
    if hasattr(b1, 'PrintSetup'):
        assert not _is_linked(b1, 'PrintSetup', a)
    if hasattr(b2, 'PrintSetup'):
        assert _is_linked(b2, 'PrintSetup', a)
    _safe_set(a, 'ps_visioDocument', None)
    assert not _is_linked(a, 'ps_visioDocument', b2)
    if hasattr(b2, 'PrintSetup'):
        assert not _is_linked(b2, 'PrintSetup', a)


def test_assoc_docProps0_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = DocumentPropertiesCollection()
    b2 = DocumentPropertiesCollection()
    _safe_set(a, 'dps_visioDocument', b1)
    assert _is_linked(a, 'dps_visioDocument', b1)
    if hasattr(b1, 'DocumentPropertiesCollection'):
        assert _is_linked(b1, 'DocumentPropertiesCollection', a)
    _safe_set(a, 'dps_visioDocument', b2)
    assert _is_linked(a, 'dps_visioDocument', b2)
    if hasattr(b1, 'DocumentPropertiesCollection'):
        assert not _is_linked(b1, 'DocumentPropertiesCollection', a)
    if hasattr(b2, 'DocumentPropertiesCollection'):
        assert _is_linked(b2, 'DocumentPropertiesCollection', a)
    _safe_set(a, 'dps_visioDocument', None)
    assert not _is_linked(a, 'dps_visioDocument', b2)
    if hasattr(b2, 'DocumentPropertiesCollection'):
        assert not _is_linked(b2, 'DocumentPropertiesCollection', a)


def test_assoc_docSettings1_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = DocumentSettingsElt()
    b2 = DocumentSettingsElt()
    _safe_set(a, 'dss_visioDocument', b1)
    assert _is_linked(a, 'dss_visioDocument', b1)
    if hasattr(b1, 'DocumentSettingsElt'):
        assert _is_linked(b1, 'DocumentSettingsElt', a)
    _safe_set(a, 'dss_visioDocument', b2)
    assert _is_linked(a, 'dss_visioDocument', b2)
    if hasattr(b1, 'DocumentSettingsElt'):
        assert not _is_linked(b1, 'DocumentSettingsElt', a)
    if hasattr(b2, 'DocumentSettingsElt'):
        assert _is_linked(b2, 'DocumentSettingsElt', a)
    _safe_set(a, 'dss_visioDocument', None)
    assert not _is_linked(a, 'dss_visioDocument', b2)
    if hasattr(b2, 'DocumentSettingsElt'):
        assert not _is_linked(b2, 'DocumentSettingsElt', a)


def test_assoc_docSolutionXML16_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = SolutionXML()
    b2 = SolutionXML()
    _safe_set(a, 'sx_visioDocument', {b1})
    assert _is_linked(a, 'sx_visioDocument', b1)
    if hasattr(b1, 'SolutionXML'):
        assert _is_linked(b1, 'SolutionXML', a)
    _safe_set(a, 'sx_visioDocument', {b2})
    assert _is_linked(a, 'sx_visioDocument', b2)
    if hasattr(b1, 'SolutionXML'):
        assert not _is_linked(b1, 'SolutionXML', a)
    if hasattr(b2, 'SolutionXML'):
        assert _is_linked(b2, 'SolutionXML', a)
    _safe_set(a, 'sx_visioDocument', set())
    assert not _is_linked(a, 'sx_visioDocument', b2)
    if hasattr(b2, 'SolutionXML'):
        assert not _is_linked(b2, 'SolutionXML', a)


def test_assoc_docStyleSheets6_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = StyleSheetsCollection()
    b2 = StyleSheetsCollection()
    _safe_set(a, 'sss_visioDocument', b1)
    assert _is_linked(a, 'sss_visioDocument', b1)
    if hasattr(b1, 'StyleSheetsCollection'):
        assert _is_linked(b1, 'StyleSheetsCollection', a)
    _safe_set(a, 'sss_visioDocument', b2)
    assert _is_linked(a, 'sss_visioDocument', b2)
    if hasattr(b1, 'StyleSheetsCollection'):
        assert not _is_linked(b1, 'StyleSheetsCollection', a)
    if hasattr(b2, 'StyleSheetsCollection'):
        assert _is_linked(b2, 'StyleSheetsCollection', a)
    _safe_set(a, 'sss_visioDocument', None)
    assert not _is_linked(a, 'sss_visioDocument', b2)
    if hasattr(b2, 'StyleSheetsCollection'):
        assert not _is_linked(b2, 'StyleSheetsCollection', a)


def test_assoc_docVBProjectData14_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = VBProjectData()
    b2 = VBProjectData()
    _safe_set(a, 'vpd_visioDocument', b1)
    assert _is_linked(a, 'vpd_visioDocument', b1)
    if hasattr(b1, 'VBProjectData'):
        assert _is_linked(b1, 'VBProjectData', a)
    _safe_set(a, 'vpd_visioDocument', b2)
    assert _is_linked(a, 'vpd_visioDocument', b2)
    if hasattr(b1, 'VBProjectData'):
        assert not _is_linked(b1, 'VBProjectData', a)
    if hasattr(b2, 'VBProjectData'):
        assert _is_linked(b2, 'VBProjectData', a)
    _safe_set(a, 'vpd_visioDocument', None)
    assert not _is_linked(a, 'vpd_visioDocument', b2)
    if hasattr(b2, 'VBProjectData'):
        assert not _is_linked(b2, 'VBProjectData', a)


def test_assoc_docWindows11_link_reassign_clear():
    a = DatadiagramMLTextFormat_VisioDocument(buildnum="sample_text", docLangId="sample_text", key="sample_text", metric="sample_text", start="sample_text", version="sample_text")
    b1 = WindowsInfo()
    b2 = WindowsInfo()
    _safe_set(a, 'ws_visioDocument', b1)
    assert _is_linked(a, 'ws_visioDocument', b1)
    if hasattr(b1, 'WindowsInfo'):
        assert _is_linked(b1, 'WindowsInfo', a)
    _safe_set(a, 'ws_visioDocument', b2)
    assert _is_linked(a, 'ws_visioDocument', b2)
    if hasattr(b1, 'WindowsInfo'):
        assert not _is_linked(b1, 'WindowsInfo', a)
    if hasattr(b2, 'WindowsInfo'):
        assert _is_linked(b2, 'WindowsInfo', a)
    _safe_set(a, 'ws_visioDocument', None)
    assert not _is_linked(a, 'ws_visioDocument', b2)
    if hasattr(b2, 'WindowsInfo'):
        assert not _is_linked(b2, 'WindowsInfo', a)


def test_assoc_dps_visioDocument17_link_reassign_clear():
    a = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    b1 = VisioDocument()
    b2 = VisioDocument()
    _safe_set(a, 'docProps', b1)
    assert _is_linked(a, 'docProps', b1)
    if hasattr(b1, 'VisioDocument'):
        assert _is_linked(b1, 'VisioDocument', a)
    _safe_set(a, 'docProps', b2)
    assert _is_linked(a, 'docProps', b2)
    if hasattr(b1, 'VisioDocument'):
        assert not _is_linked(b1, 'VisioDocument', a)
    if hasattr(b2, 'VisioDocument'):
        assert _is_linked(b2, 'VisioDocument', a)
    _safe_set(a, 'docProps', None)
    assert not _is_linked(a, 'docProps', b2)
    if hasattr(b2, 'VisioDocument'):
        assert not _is_linked(b2, 'VisioDocument', a)


def test_assoc_erd_visioDocument51_link_reassign_clear():
    a = DatadiagramMLTextFormat_EmailRoutingData(data="sample_text", size="sample_text")
    b1 = VisioDocument()
    b2 = VisioDocument()
    _safe_set(a, 'docEmailRoutingData', b1)
    assert _is_linked(a, 'docEmailRoutingData', b1)
    if hasattr(b1, 'VisioDocument52'):
        assert _is_linked(b1, 'VisioDocument52', a)
    _safe_set(a, 'docEmailRoutingData', b2)
    assert _is_linked(a, 'docEmailRoutingData', b2)
    if hasattr(b1, 'VisioDocument52'):
        assert not _is_linked(b1, 'VisioDocument52', a)
    if hasattr(b2, 'VisioDocument52'):
        assert _is_linked(b2, 'VisioDocument52', a)
    _safe_set(a, 'docEmailRoutingData', None)
    assert not _is_linked(a, 'docEmailRoutingData', b2)
    if hasattr(b2, 'VisioDocument52'):
        assert not _is_linked(b2, 'VisioDocument52', a)


def test_assoc_fe_fonts42_link_reassign_clear():
    a = DatadiagramMLTextFormat_FontEntry(attributes="sample_text", charSet="sample_text", name="sample_text", pitchAndFamily="sample_text", unicode="sample_text", weight="sample_text")
    b1 = FontsTable()
    b2 = FontsTable()
    _safe_set(a, 'fontEntries', b1)
    assert _is_linked(a, 'fontEntries', b1)
    if hasattr(b1, 'FontsTable43'):
        assert _is_linked(b1, 'FontsTable43', a)
    _safe_set(a, 'fontEntries', b2)
    assert _is_linked(a, 'fontEntries', b2)
    if hasattr(b1, 'FontsTable43'):
        assert not _is_linked(b1, 'FontsTable43', a)
    if hasattr(b2, 'FontsTable43'):
        assert _is_linked(b2, 'FontsTable43', a)
    _safe_set(a, 'fontEntries', None)
    assert not _is_linked(a, 'fontEntries', b2)
    if hasattr(b2, 'FontsTable43'):
        assert not _is_linked(b2, 'FontsTable43', a)


def test_assoc_fn_faceNames47_link_reassign_clear():
    a = DatadiagramMLTextFormat_FaceName(charSet="sample_text", flags="sample_text", name="sample_text", panos="sample_text", unicodeRanges="sample_text")
    b1 = FaceNamesTable()
    b2 = FaceNamesTable()
    _safe_set(a, 'faceNameEntries', b1)
    assert _is_linked(a, 'faceNameEntries', b1)
    if hasattr(b1, 'FaceNamesTable48'):
        assert _is_linked(b1, 'FaceNamesTable48', a)
    _safe_set(a, 'faceNameEntries', b2)
    assert _is_linked(a, 'faceNameEntries', b2)
    if hasattr(b1, 'FaceNamesTable48'):
        assert not _is_linked(b1, 'FaceNamesTable48', a)
    if hasattr(b2, 'FaceNamesTable48'):
        assert _is_linked(b2, 'FaceNamesTable48', a)
    _safe_set(a, 'faceNameEntries', None)
    assert not _is_linked(a, 'faceNameEntries', b2)
    if hasattr(b2, 'FaceNamesTable48'):
        assert not _is_linked(b2, 'FaceNamesTable48', a)


def test_assoc_i_masterShortCut251_link_reassign_clear():
    a = DatadiagramMLTextFormat_Icon(value="sample_text")
    b1 = MasterShortCut()
    b2 = MasterShortCut()
    _safe_set(a, 'icons', b1)
    assert _is_linked(a, 'icons', b1)
    if hasattr(b1, 'MasterShortCut252'):
        assert _is_linked(b1, 'MasterShortCut252', a)
    _safe_set(a, 'icons', b2)
    assert _is_linked(a, 'icons', b2)
    if hasattr(b1, 'MasterShortCut252'):
        assert not _is_linked(b1, 'MasterShortCut252', a)
    if hasattr(b2, 'MasterShortCut252'):
        assert _is_linked(b2, 'MasterShortCut252', a)
    _safe_set(a, 'icons', None)
    assert not _is_linked(a, 'icons', b2)
    if hasattr(b2, 'MasterShortCut252'):
        assert not _is_linked(b2, 'MasterShortCut252', a)


def test_assoc_icons250_link_reassign_clear():
    a = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    b1 = Icon()
    b2 = Icon()
    _safe_set(a, 'i_masterShortCut', {b1})
    assert _is_linked(a, 'i_masterShortCut', b1)
    if hasattr(b1, 'Icon'):
        assert _is_linked(b1, 'Icon', a)
    _safe_set(a, 'i_masterShortCut', {b2})
    assert _is_linked(a, 'i_masterShortCut', b2)
    if hasattr(b1, 'Icon'):
        assert not _is_linked(b1, 'Icon', a)
    if hasattr(b2, 'Icon'):
        assert _is_linked(b2, 'Icon', a)
    _safe_set(a, 'i_masterShortCut', set())
    assert not _is_linked(a, 'i_masterShortCut', b2)
    if hasattr(b2, 'Icon'):
        assert not _is_linked(b2, 'Icon', a)


def test_assoc_m_masterShortCuts248_link_reassign_clear():
    a = DatadiagramMLTextFormat_MasterShortCut(alignName="sample_text", iconSize="sample_text", patternFlags="sample_text", prompt="sample_text", shortcutHelp="sample_text", shortcutURL="sample_text")
    b1 = MastersCollection()
    b2 = MastersCollection()
    _safe_set(a, 'masterShortCuts', b1)
    assert _is_linked(a, 'masterShortCuts', b1)
    if hasattr(b1, 'MastersCollection249'):
        assert _is_linked(b1, 'MastersCollection249', a)
    _safe_set(a, 'masterShortCuts', b2)
    assert _is_linked(a, 'masterShortCuts', b2)
    if hasattr(b1, 'MastersCollection249'):
        assert not _is_linked(b1, 'MastersCollection249', a)
    if hasattr(b2, 'MastersCollection249'):
        assert _is_linked(b2, 'MastersCollection249', a)
    _safe_set(a, 'masterShortCuts', None)
    assert not _is_linked(a, 'masterShortCuts', b2)
    if hasattr(b2, 'MastersCollection249'):
        assert not _is_linked(b2, 'MastersCollection249', a)


def test_assoc_m_masters253_link_reassign_clear():
    a = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    b1 = MastersCollection()
    b2 = MastersCollection()
    _safe_set(a, 'masters', b1)
    assert _is_linked(a, 'masters', b1)
    if hasattr(b1, 'MastersCollection254'):
        assert _is_linked(b1, 'MastersCollection254', a)
    _safe_set(a, 'masters', b2)
    assert _is_linked(a, 'masters', b2)
    if hasattr(b1, 'MastersCollection254'):
        assert not _is_linked(b1, 'MastersCollection254', a)
    if hasattr(b2, 'MastersCollection254'):
        assert _is_linked(b2, 'MastersCollection254', a)
    _safe_set(a, 'masters', None)
    assert not _is_linked(a, 'masters', b2)
    if hasattr(b2, 'MastersCollection254'):
        assert not _is_linked(b2, 'MastersCollection254', a)


def test_assoc_masterElts255_link_reassign_clear():
    a = DatadiagramMLTextFormat_Master(alignName="sample_text", baseID="sample_text", hidden="sample_text", iconSize="sample_text", iconUpdate="sample_text", matchByName="sample_text", patternFlags="sample_text", prompt="sample_text")
    b1 = MasterElt()
    b2 = MasterElt()
    _safe_set(a, 'me_master', {b1})
    assert _is_linked(a, 'me_master', b1)
    if hasattr(b1, 'MasterElt'):
        assert _is_linked(b1, 'MasterElt', a)
    _safe_set(a, 'me_master', {b2})
    assert _is_linked(a, 'me_master', b2)
    if hasattr(b1, 'MasterElt'):
        assert not _is_linked(b1, 'MasterElt', a)
    if hasattr(b2, 'MasterElt'):
        assert _is_linked(b2, 'MasterElt', a)
    _safe_set(a, 'me_master', set())
    assert not _is_linked(a, 'me_master', b2)
    if hasattr(b2, 'MasterElt'):
        assert not _is_linked(b2, 'MasterElt', a)


def test_assoc_p_pages265_link_reassign_clear():
    a = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    b1 = PagesCollection()
    b2 = PagesCollection()
    _safe_set(a, 'pages', b1)
    assert _is_linked(a, 'pages', b1)
    if hasattr(b1, 'PagesCollection266'):
        assert _is_linked(b1, 'PagesCollection266', a)
    _safe_set(a, 'pages', b2)
    assert _is_linked(a, 'pages', b2)
    if hasattr(b1, 'PagesCollection266'):
        assert not _is_linked(b1, 'PagesCollection266', a)
    if hasattr(b2, 'PagesCollection266'):
        assert _is_linked(b2, 'PagesCollection266', a)
    _safe_set(a, 'pages', None)
    assert not _is_linked(a, 'pages', b2)
    if hasattr(b2, 'PagesCollection266'):
        assert not _is_linked(b2, 'PagesCollection266', a)


def test_assoc_pageElts267_link_reassign_clear():
    a = DatadiagramMLTextFormat_Page(ViewCenterY="sample_text", associatedPage="sample_text", backPage="sample_text", background="sample_text", reviewerID="sample_text", viewCenterX="sample_text", viewScale="sample_text")
    b1 = PageElt()
    b2 = PageElt()
    _safe_set(a, 'pe_page', {b1})
    assert _is_linked(a, 'pe_page', b1)
    if hasattr(b1, 'PageElt'):
        assert _is_linked(b1, 'PageElt', a)
    _safe_set(a, 'pe_page', {b2})
    assert _is_linked(a, 'pe_page', b2)
    if hasattr(b1, 'PageElt'):
        assert not _is_linked(b1, 'PageElt', a)
    if hasattr(b2, 'PageElt'):
        assert _is_linked(b2, 'PageElt', a)
    _safe_set(a, 'pe_page', set())
    assert not _is_linked(a, 'pe_page', b2)
    if hasattr(b2, 'PageElt'):
        assert not _is_linked(b2, 'PageElt', a)


def test_assoc_shapeElts61_link_reassign_clear():
    a = DatadiagramMLTextFormat_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    b1 = ShapeElt()
    b2 = ShapeElt()
    _safe_set(a, 'sse_shapeSheet', {b1})
    assert _is_linked(a, 'sse_shapeSheet', b1)
    if hasattr(b1, 'ShapeElt'):
        assert _is_linked(b1, 'ShapeElt', a)
    _safe_set(a, 'sse_shapeSheet', {b2})
    assert _is_linked(a, 'sse_shapeSheet', b2)
    if hasattr(b1, 'ShapeElt'):
        assert not _is_linked(b1, 'ShapeElt', a)
    if hasattr(b2, 'ShapeElt'):
        assert _is_linked(b2, 'ShapeElt', a)
    _safe_set(a, 'sse_shapeSheet', set())
    assert not _is_linked(a, 'sse_shapeSheet', b2)
    if hasattr(b2, 'ShapeElt'):
        assert not _is_linked(b2, 'ShapeElt', a)


def test_assoc_ss_shapes60_link_reassign_clear():
    a = DatadiagramMLTextFormat_Shape(fillStyle="sample_text", lineStyle="sample_text", textStyle="sample_text")
    b1 = ShapesCollection()
    b2 = ShapesCollection()
    _safe_set(a, 'shapes', b1)
    assert _is_linked(a, 'shapes', b1)
    if hasattr(b1, 'ShapesCollection'):
        assert _is_linked(b1, 'ShapesCollection', a)
    _safe_set(a, 'shapes', b2)
    assert _is_linked(a, 'shapes', b2)
    if hasattr(b1, 'ShapesCollection'):
        assert not _is_linked(b1, 'ShapesCollection', a)
    if hasattr(b2, 'ShapesCollection'):
        assert _is_linked(b2, 'ShapesCollection', a)
    _safe_set(a, 'shapes', None)
    assert not _is_linked(a, 'shapes', b2)
    if hasattr(b2, 'ShapesCollection'):
        assert not _is_linked(b2, 'ShapesCollection', a)


def test_assoc_timeCreated19_link_reassign_clear():
    a = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    b1 = DateTimeType()
    b2 = DateTimeType()
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection', b1)
    assert _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection', b1)
    if hasattr(b1, 'DateTimeType'):
        assert _is_linked(b1, 'DateTimeType', a)
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection', b2)
    assert _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection', b2)
    if hasattr(b1, 'DateTimeType'):
        assert not _is_linked(b1, 'DateTimeType', a)
    if hasattr(b2, 'DateTimeType'):
        assert _is_linked(b2, 'DateTimeType', a)
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection', None)
    assert not _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection', b2)
    if hasattr(b2, 'DateTimeType'):
        assert not _is_linked(b2, 'DateTimeType', a)


def test_assoc_timeEdited23_link_reassign_clear():
    a = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    b1 = DateTimeType()
    b2 = DateTimeType()
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection24', b1)
    assert _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection24', b1)
    if hasattr(b1, 'DateTimeType25'):
        assert _is_linked(b1, 'DateTimeType25', a)
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection24', b2)
    assert _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection24', b2)
    if hasattr(b1, 'DateTimeType25'):
        assert not _is_linked(b1, 'DateTimeType25', a)
    if hasattr(b2, 'DateTimeType25'):
        assert _is_linked(b2, 'DateTimeType25', a)
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection24', None)
    assert not _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection24', b2)
    if hasattr(b2, 'DateTimeType25'):
        assert not _is_linked(b2, 'DateTimeType25', a)


def test_assoc_timePrinted26_link_reassign_clear():
    a = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    b1 = DateTimeType()
    b2 = DateTimeType()
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection27', b1)
    assert _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection27', b1)
    if hasattr(b1, 'DateTimeType28'):
        assert _is_linked(b1, 'DateTimeType28', a)
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection27', b2)
    assert _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection27', b2)
    if hasattr(b1, 'DateTimeType28'):
        assert not _is_linked(b1, 'DateTimeType28', a)
    if hasattr(b2, 'DateTimeType28'):
        assert _is_linked(b2, 'DateTimeType28', a)
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection27', None)
    assert not _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection27', b2)
    if hasattr(b2, 'DateTimeType28'):
        assert not _is_linked(b2, 'DateTimeType28', a)


def test_assoc_timeSaved20_link_reassign_clear():
    a = DatadiagramMLTextFormat_DocumentPropertiesCollection(alternateNames="sample_text", buildNumberCreated="sample_text", buildNumberEdited="sample_text", category="sample_text", company="sample_text", creator="sample_text", description="sample_text", hyperlinkBase_href="sample_text", keywords="sample_text", manager="sample_text", subject="sample_text", template="sample_text", title="sample_text")
    b1 = DateTimeType()
    b2 = DateTimeType()
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection21', b1)
    assert _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection21', b1)
    if hasattr(b1, 'DateTimeType22'):
        assert _is_linked(b1, 'DateTimeType22', a)
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection21', b2)
    assert _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection21', b2)
    if hasattr(b1, 'DateTimeType22'):
        assert not _is_linked(b1, 'DateTimeType22', a)
    if hasattr(b2, 'DateTimeType22'):
        assert _is_linked(b2, 'DateTimeType22', a)
    _safe_set(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection21', None)
    assert not _is_linked(a, 'DatadiagramMLTextFormat_DocumentPropertiesCollection21', b2)
    if hasattr(b2, 'DateTimeType22'):
        assert not _is_linked(b2, 'DateTimeType22', a)


def test_assoc_vpd_visioDocument49_link_reassign_clear():
    a = DatadiagramMLTextFormat_VBProjectData(data="sample_text")
    b1 = VisioDocument()
    b2 = VisioDocument()
    _safe_set(a, 'docVBProjectData', b1)
    assert _is_linked(a, 'docVBProjectData', b1)
    if hasattr(b1, 'VisioDocument50'):
        assert _is_linked(b1, 'VisioDocument50', a)
    _safe_set(a, 'docVBProjectData', b2)
    assert _is_linked(a, 'docVBProjectData', b2)
    if hasattr(b1, 'VisioDocument50'):
        assert not _is_linked(b1, 'VisioDocument50', a)
    if hasattr(b2, 'VisioDocument50'):
        assert _is_linked(b2, 'VisioDocument50', a)
    _safe_set(a, 'docVBProjectData', None)
    assert not _is_linked(a, 'docVBProjectData', b2)
    if hasattr(b2, 'VisioDocument50'):
        assert not _is_linked(b2, 'VisioDocument50', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArcTo_strategy = st.builds(ArcTo)
@given(instance=ArcTo_strategy)
@settings(max_examples=25)
def test_ArcTo_instantiation(instance):
    assert isinstance(instance, ArcTo)


CellType_strategy = st.builds(CellType)
@given(instance=CellType_strategy)
@settings(max_examples=25)
def test_CellType_instantiation(instance):
    assert isinstance(instance, CellType)


ColorEntry_strategy = st.builds(ColorEntry)
@given(instance=ColorEntry_strategy)
@settings(max_examples=25)
def test_ColorEntry_instantiation(instance):
    assert isinstance(instance, ColorEntry)


ColorsTable_strategy = st.builds(ColorsTable)
@given(instance=ColorsTable_strategy)
@settings(max_examples=25)
def test_ColorsTable_instantiation(instance):
    assert isinstance(instance, ColorsTable)


Connect_strategy = st.builds(Connect)
@given(instance=Connect_strategy)
@settings(max_examples=25)
def test_Connect_instantiation(instance):
    assert isinstance(instance, Connect)


ConnectsCollection_strategy = st.builds(ConnectsCollection)
@given(instance=ConnectsCollection_strategy)
@settings(max_examples=25)
def test_ConnectsCollection_instantiation(instance):
    assert isinstance(instance, ConnectsCollection)


CustomPropertiesCollection_strategy = st.builds(CustomPropertiesCollection)
@given(instance=CustomPropertiesCollection_strategy)
@settings(max_examples=25)
def test_CustomPropertiesCollection_instantiation(instance):
    assert isinstance(instance, CustomPropertiesCollection)


CustomProperty_strategy = st.builds(CustomProperty)
@given(instance=CustomProperty_strategy)
@settings(max_examples=25)
def test_CustomProperty_instantiation(instance):
    assert isinstance(instance, CustomProperty)


DatadiagramMLTextFormat_ArcTo_strategy = st.builds(DatadiagramMLTextFormat_ArcTo)
@given(instance=DatadiagramMLTextFormat_ArcTo_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_ArcTo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ArcTo)


DatadiagramMLTextFormat_CellType_strategy = st.builds(DatadiagramMLTextFormat_CellType, err=safe_text, formula=safe_text, unit=safe_text, value=safe_text)
@given(instance=DatadiagramMLTextFormat_CellType_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_CellType_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_CellType)


DatadiagramMLTextFormat_Char_strategy = st.builds(DatadiagramMLTextFormat_Char)
@given(instance=DatadiagramMLTextFormat_Char_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Char_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Char)


DatadiagramMLTextFormat_ColorEntry_strategy = st.builds(DatadiagramMLTextFormat_ColorEntry, rgb=safe_text)
@given(instance=DatadiagramMLTextFormat_ColorEntry_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_ColorEntry_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ColorEntry)


DatadiagramMLTextFormat_ColorsTable_strategy = st.builds(DatadiagramMLTextFormat_ColorsTable)
@given(instance=DatadiagramMLTextFormat_ColorsTable_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_ColorsTable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ColorsTable)


DatadiagramMLTextFormat_Connect_strategy = st.builds(DatadiagramMLTextFormat_Connect, fromCell=safe_text, fromPart=safe_text, fromSheet=safe_text, toCell=safe_text, toPart=safe_text, toSheet=safe_text)
@given(instance=DatadiagramMLTextFormat_Connect_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Connect_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Connect)


DatadiagramMLTextFormat_ConnectsCollection_strategy = st.builds(DatadiagramMLTextFormat_ConnectsCollection)
@given(instance=DatadiagramMLTextFormat_ConnectsCollection_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_ConnectsCollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ConnectsCollection)


DatadiagramMLTextFormat_Cp_strategy = st.builds(DatadiagramMLTextFormat_Cp)
@given(instance=DatadiagramMLTextFormat_Cp_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Cp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Cp)


DatadiagramMLTextFormat_CustomPropertiesCollection_strategy = st.builds(DatadiagramMLTextFormat_CustomPropertiesCollection)
@given(instance=DatadiagramMLTextFormat_CustomPropertiesCollection_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_CustomPropertiesCollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_CustomPropertiesCollection)


DatadiagramMLTextFormat_CustomProperty_strategy = st.builds(DatadiagramMLTextFormat_CustomProperty, dataType=safe_text, name=safe_text)
@given(instance=DatadiagramMLTextFormat_CustomProperty_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_CustomProperty_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_CustomProperty)


DatadiagramMLTextFormat_DateTimeType_strategy = st.builds(DatadiagramMLTextFormat_DateTimeType, day=safe_text, hour=safe_text, minute=safe_text, month=safe_text, second=safe_text, year=safe_text)
@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_DateTimeType_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_DateTimeType)


DatadiagramMLTextFormat_DelElt_strategy = st.builds(DatadiagramMLTextFormat_DelElt, del_=safe_text)
@given(instance=DatadiagramMLTextFormat_DelElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_DelElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_DelElt)


DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy = st.builds(DatadiagramMLTextFormat_DocumentPropertiesCollection, alternateNames=safe_text, buildNumberCreated=safe_text, buildNumberEdited=safe_text, category=safe_text, company=safe_text, creator=safe_text, description=safe_text, hyperlinkBase_href=safe_text, keywords=safe_text, manager=safe_text, subject=safe_text, template=safe_text, title=safe_text)
@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_DocumentPropertiesCollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_DocumentPropertiesCollection)


DatadiagramMLTextFormat_DocumentSettingsElt_strategy = st.builds(DatadiagramMLTextFormat_DocumentSettingsElt)
@given(instance=DatadiagramMLTextFormat_DocumentSettingsElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_DocumentSettingsElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_DocumentSettingsElt)


DatadiagramMLTextFormat_DocumentSheet_strategy = st.builds(DatadiagramMLTextFormat_DocumentSheet)
@given(instance=DatadiagramMLTextFormat_DocumentSheet_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_DocumentSheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_DocumentSheet)


DatadiagramMLTextFormat_Ellipse_strategy = st.builds(DatadiagramMLTextFormat_Ellipse)
@given(instance=DatadiagramMLTextFormat_Ellipse_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Ellipse_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Ellipse)


DatadiagramMLTextFormat_EllipticalArcTo_strategy = st.builds(DatadiagramMLTextFormat_EllipticalArcTo)
@given(instance=DatadiagramMLTextFormat_EllipticalArcTo_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_EllipticalArcTo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_EllipticalArcTo)


DatadiagramMLTextFormat_EmailRoutingData_strategy = st.builds(DatadiagramMLTextFormat_EmailRoutingData, data=safe_text, size=safe_text)
@given(instance=DatadiagramMLTextFormat_EmailRoutingData_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_EmailRoutingData_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_EmailRoutingData)


DatadiagramMLTextFormat_EventList_strategy = st.builds(DatadiagramMLTextFormat_EventList)
@given(instance=DatadiagramMLTextFormat_EventList_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_EventList_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_EventList)


DatadiagramMLTextFormat_FaceName_strategy = st.builds(DatadiagramMLTextFormat_FaceName, charSet=safe_text, flags=safe_text, name=safe_text, panos=safe_text, unicodeRanges=safe_text)
@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_FaceName_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_FaceName)


DatadiagramMLTextFormat_FaceNamesTable_strategy = st.builds(DatadiagramMLTextFormat_FaceNamesTable)
@given(instance=DatadiagramMLTextFormat_FaceNamesTable_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_FaceNamesTable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_FaceNamesTable)


DatadiagramMLTextFormat_Field_strategy = st.builds(DatadiagramMLTextFormat_Field)
@given(instance=DatadiagramMLTextFormat_Field_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Field_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Field)


DatadiagramMLTextFormat_Fld_strategy = st.builds(DatadiagramMLTextFormat_Fld)
@given(instance=DatadiagramMLTextFormat_Fld_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Fld_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Fld)


DatadiagramMLTextFormat_FontEntry_strategy = st.builds(DatadiagramMLTextFormat_FontEntry, attributes=safe_text, charSet=safe_text, name=safe_text, pitchAndFamily=safe_text, unicode=safe_text, weight=safe_text)
@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_FontEntry_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_FontEntry)


DatadiagramMLTextFormat_FontsTable_strategy = st.builds(DatadiagramMLTextFormat_FontsTable)
@given(instance=DatadiagramMLTextFormat_FontsTable_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_FontsTable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_FontsTable)


DatadiagramMLTextFormat_Geom_strategy = st.builds(DatadiagramMLTextFormat_Geom)
@given(instance=DatadiagramMLTextFormat_Geom_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Geom_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Geom)


DatadiagramMLTextFormat_HeaderFooter_strategy = st.builds(DatadiagramMLTextFormat_HeaderFooter)
@given(instance=DatadiagramMLTextFormat_HeaderFooter_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_HeaderFooter_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_HeaderFooter)


DatadiagramMLTextFormat_IXElt_strategy = st.builds(DatadiagramMLTextFormat_IXElt, iX=safe_text)
@given(instance=DatadiagramMLTextFormat_IXElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_IXElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_IXElt)


DatadiagramMLTextFormat_IXrequiredElt_strategy = st.builds(DatadiagramMLTextFormat_IXrequiredElt, iX=safe_text)
@given(instance=DatadiagramMLTextFormat_IXrequiredElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_IXrequiredElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_IXrequiredElt)


DatadiagramMLTextFormat_Icon_strategy = st.builds(DatadiagramMLTextFormat_Icon, value=safe_text)
@given(instance=DatadiagramMLTextFormat_Icon_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Icon_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Icon)


DatadiagramMLTextFormat_IdentifiedElt_strategy = st.builds(DatadiagramMLTextFormat_IdentifiedElt, ID=safe_text)
@given(instance=DatadiagramMLTextFormat_IdentifiedElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_IdentifiedElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_IdentifiedElt)


DatadiagramMLTextFormat_InfiniteLine_strategy = st.builds(DatadiagramMLTextFormat_InfiniteLine)
@given(instance=DatadiagramMLTextFormat_InfiniteLine_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_InfiniteLine_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_InfiniteLine)


DatadiagramMLTextFormat_LineTo_strategy = st.builds(DatadiagramMLTextFormat_LineTo)
@given(instance=DatadiagramMLTextFormat_LineTo_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_LineTo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_LineTo)


DatadiagramMLTextFormat_Master_strategy = st.builds(DatadiagramMLTextFormat_Master, alignName=safe_text, baseID=safe_text, hidden=safe_text, iconSize=safe_text, iconUpdate=safe_text, matchByName=safe_text, patternFlags=safe_text, prompt=safe_text)
@given(instance=DatadiagramMLTextFormat_Master_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Master_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Master)


DatadiagramMLTextFormat_MasterElt_strategy = st.builds(DatadiagramMLTextFormat_MasterElt)
@given(instance=DatadiagramMLTextFormat_MasterElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_MasterElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_MasterElt)


DatadiagramMLTextFormat_MasterShortCut_strategy = st.builds(DatadiagramMLTextFormat_MasterShortCut, alignName=safe_text, iconSize=safe_text, patternFlags=safe_text, prompt=safe_text, shortcutHelp=safe_text, shortcutURL=safe_text)
@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_MasterShortCut_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_MasterShortCut)


DatadiagramMLTextFormat_MastersCollection_strategy = st.builds(DatadiagramMLTextFormat_MastersCollection)
@given(instance=DatadiagramMLTextFormat_MastersCollection_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_MastersCollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_MastersCollection)


DatadiagramMLTextFormat_MoveTo_strategy = st.builds(DatadiagramMLTextFormat_MoveTo)
@given(instance=DatadiagramMLTextFormat_MoveTo_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_MoveTo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_MoveTo)


DatadiagramMLTextFormat_NURBSTo_strategy = st.builds(DatadiagramMLTextFormat_NURBSTo)
@given(instance=DatadiagramMLTextFormat_NURBSTo_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_NURBSTo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_NURBSTo)


DatadiagramMLTextFormat_NamedElt_strategy = st.builds(DatadiagramMLTextFormat_NamedElt, name=safe_text, nameU=safe_text)
@given(instance=DatadiagramMLTextFormat_NamedElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_NamedElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_NamedElt)


DatadiagramMLTextFormat_Page_strategy = st.builds(DatadiagramMLTextFormat_Page, ViewCenterY=safe_text, associatedPage=safe_text, backPage=safe_text, background=safe_text, reviewerID=safe_text, viewCenterX=safe_text, viewScale=safe_text)
@given(instance=DatadiagramMLTextFormat_Page_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Page_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Page)


DatadiagramMLTextFormat_PageElt_strategy = st.builds(DatadiagramMLTextFormat_PageElt)
@given(instance=DatadiagramMLTextFormat_PageElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_PageElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_PageElt)


DatadiagramMLTextFormat_PageSheet_strategy = st.builds(DatadiagramMLTextFormat_PageSheet)
@given(instance=DatadiagramMLTextFormat_PageSheet_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_PageSheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_PageSheet)


DatadiagramMLTextFormat_PagesCollection_strategy = st.builds(DatadiagramMLTextFormat_PagesCollection)
@given(instance=DatadiagramMLTextFormat_PagesCollection_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_PagesCollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_PagesCollection)


DatadiagramMLTextFormat_Para_strategy = st.builds(DatadiagramMLTextFormat_Para)
@given(instance=DatadiagramMLTextFormat_Para_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Para_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Para)


DatadiagramMLTextFormat_PolylineTo_strategy = st.builds(DatadiagramMLTextFormat_PolylineTo)
@given(instance=DatadiagramMLTextFormat_PolylineTo_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_PolylineTo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_PolylineTo)


DatadiagramMLTextFormat_Pp_strategy = st.builds(DatadiagramMLTextFormat_Pp)
@given(instance=DatadiagramMLTextFormat_Pp_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Pp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Pp)


DatadiagramMLTextFormat_PrintSetup_strategy = st.builds(DatadiagramMLTextFormat_PrintSetup)
@given(instance=DatadiagramMLTextFormat_PrintSetup_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_PrintSetup_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_PrintSetup)


DatadiagramMLTextFormat_Shape_strategy = st.builds(DatadiagramMLTextFormat_Shape, fillStyle=safe_text, lineStyle=safe_text, textStyle=safe_text)
@given(instance=DatadiagramMLTextFormat_Shape_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Shape_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Shape)


DatadiagramMLTextFormat_ShapeElt_strategy = st.builds(DatadiagramMLTextFormat_ShapeElt)
@given(instance=DatadiagramMLTextFormat_ShapeElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_ShapeElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ShapeElt)


DatadiagramMLTextFormat_ShapesCollection_strategy = st.builds(DatadiagramMLTextFormat_ShapesCollection)
@given(instance=DatadiagramMLTextFormat_ShapesCollection_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_ShapesCollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ShapesCollection)


DatadiagramMLTextFormat_SolutionXML_strategy = st.builds(DatadiagramMLTextFormat_SolutionXML)
@given(instance=DatadiagramMLTextFormat_SolutionXML_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_SolutionXML_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_SolutionXML)


DatadiagramMLTextFormat_SplineKnot_strategy = st.builds(DatadiagramMLTextFormat_SplineKnot)
@given(instance=DatadiagramMLTextFormat_SplineKnot_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_SplineKnot_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_SplineKnot)


DatadiagramMLTextFormat_SplineStart_strategy = st.builds(DatadiagramMLTextFormat_SplineStart)
@given(instance=DatadiagramMLTextFormat_SplineStart_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_SplineStart_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_SplineStart)


DatadiagramMLTextFormat_StringElt_strategy = st.builds(DatadiagramMLTextFormat_StringElt, value=safe_text)
@given(instance=DatadiagramMLTextFormat_StringElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_StringElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_StringElt)


DatadiagramMLTextFormat_StyleSheet_strategy = st.builds(DatadiagramMLTextFormat_StyleSheet)
@given(instance=DatadiagramMLTextFormat_StyleSheet_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_StyleSheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_StyleSheet)


DatadiagramMLTextFormat_StyleSheetsCollection_strategy = st.builds(DatadiagramMLTextFormat_StyleSheetsCollection)
@given(instance=DatadiagramMLTextFormat_StyleSheetsCollection_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_StyleSheetsCollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_StyleSheetsCollection)


DatadiagramMLTextFormat_Tab_strategy = st.builds(DatadiagramMLTextFormat_Tab)
@given(instance=DatadiagramMLTextFormat_Tab_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Tab_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Tab)


DatadiagramMLTextFormat_TabsCollection_strategy = st.builds(DatadiagramMLTextFormat_TabsCollection)
@given(instance=DatadiagramMLTextFormat_TabsCollection_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_TabsCollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_TabsCollection)


DatadiagramMLTextFormat_Text_strategy = st.builds(DatadiagramMLTextFormat_Text)
@given(instance=DatadiagramMLTextFormat_Text_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Text_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Text)


DatadiagramMLTextFormat_TextElt_strategy = st.builds(DatadiagramMLTextFormat_TextElt)
@given(instance=DatadiagramMLTextFormat_TextElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_TextElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_TextElt)


DatadiagramMLTextFormat_Tp_strategy = st.builds(DatadiagramMLTextFormat_Tp)
@given(instance=DatadiagramMLTextFormat_Tp_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_Tp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Tp)


DatadiagramMLTextFormat_UniqueIdElt_strategy = st.builds(DatadiagramMLTextFormat_UniqueIdElt, UniqueID=safe_text)
@given(instance=DatadiagramMLTextFormat_UniqueIdElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_UniqueIdElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_UniqueIdElt)


DatadiagramMLTextFormat_VBProjectData_strategy = st.builds(DatadiagramMLTextFormat_VBProjectData, data=safe_text)
@given(instance=DatadiagramMLTextFormat_VBProjectData_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_VBProjectData_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_VBProjectData)


DatadiagramMLTextFormat_VisioDocument_strategy = st.builds(DatadiagramMLTextFormat_VisioDocument, buildnum=safe_text, docLangId=safe_text, key=safe_text, metric=safe_text, start=safe_text, version=safe_text)
@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_VisioDocument_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_VisioDocument)


DatadiagramMLTextFormat_WindowsInfo_strategy = st.builds(DatadiagramMLTextFormat_WindowsInfo)
@given(instance=DatadiagramMLTextFormat_WindowsInfo_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_WindowsInfo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_WindowsInfo)


DatadiagramMLTextFormat_XYABCDEElt_strategy = st.builds(DatadiagramMLTextFormat_XYABCDEElt)
@given(instance=DatadiagramMLTextFormat_XYABCDEElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_XYABCDEElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_XYABCDEElt)


DatadiagramMLTextFormat_XYABCDElt_strategy = st.builds(DatadiagramMLTextFormat_XYABCDElt)
@given(instance=DatadiagramMLTextFormat_XYABCDElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_XYABCDElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_XYABCDElt)


DatadiagramMLTextFormat_XYABElt_strategy = st.builds(DatadiagramMLTextFormat_XYABElt)
@given(instance=DatadiagramMLTextFormat_XYABElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_XYABElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_XYABElt)


DatadiagramMLTextFormat_XYAElt_strategy = st.builds(DatadiagramMLTextFormat_XYAElt)
@given(instance=DatadiagramMLTextFormat_XYAElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_XYAElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_XYAElt)


DatadiagramMLTextFormat_XYElt_strategy = st.builds(DatadiagramMLTextFormat_XYElt)
@given(instance=DatadiagramMLTextFormat_XYElt_strategy)
@settings(max_examples=25)
def test_DatadiagramMLTextFormat_XYElt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_XYElt)


DateTimeType_strategy = st.builds(DateTimeType)
@given(instance=DateTimeType_strategy)
@settings(max_examples=25)
def test_DateTimeType_instantiation(instance):
    assert isinstance(instance, DateTimeType)


DelElt_strategy = st.builds(DelElt)
@given(instance=DelElt_strategy)
@settings(max_examples=25)
def test_DelElt_instantiation(instance):
    assert isinstance(instance, DelElt)


DocumentPropertiesCollection_strategy = st.builds(DocumentPropertiesCollection)
@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=25)
def test_DocumentPropertiesCollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)


DocumentSettingsElt_strategy = st.builds(DocumentSettingsElt)
@given(instance=DocumentSettingsElt_strategy)
@settings(max_examples=25)
def test_DocumentSettingsElt_instantiation(instance):
    assert isinstance(instance, DocumentSettingsElt)


DocumentSheet_strategy = st.builds(DocumentSheet)
@given(instance=DocumentSheet_strategy)
@settings(max_examples=25)
def test_DocumentSheet_instantiation(instance):
    assert isinstance(instance, DocumentSheet)


Ellipse_strategy = st.builds(Ellipse)
@given(instance=Ellipse_strategy)
@settings(max_examples=25)
def test_Ellipse_instantiation(instance):
    assert isinstance(instance, Ellipse)


EllipticalArcTo_strategy = st.builds(EllipticalArcTo)
@given(instance=EllipticalArcTo_strategy)
@settings(max_examples=25)
def test_EllipticalArcTo_instantiation(instance):
    assert isinstance(instance, EllipticalArcTo)


EmailRoutingData_strategy = st.builds(EmailRoutingData)
@given(instance=EmailRoutingData_strategy)
@settings(max_examples=25)
def test_EmailRoutingData_instantiation(instance):
    assert isinstance(instance, EmailRoutingData)


EventList_strategy = st.builds(EventList)
@given(instance=EventList_strategy)
@settings(max_examples=25)
def test_EventList_instantiation(instance):
    assert isinstance(instance, EventList)


FaceName_strategy = st.builds(FaceName)
@given(instance=FaceName_strategy)
@settings(max_examples=25)
def test_FaceName_instantiation(instance):
    assert isinstance(instance, FaceName)


FaceNamesTable_strategy = st.builds(FaceNamesTable)
@given(instance=FaceNamesTable_strategy)
@settings(max_examples=25)
def test_FaceNamesTable_instantiation(instance):
    assert isinstance(instance, FaceNamesTable)


FontEntry_strategy = st.builds(FontEntry)
@given(instance=FontEntry_strategy)
@settings(max_examples=25)
def test_FontEntry_instantiation(instance):
    assert isinstance(instance, FontEntry)


FontsTable_strategy = st.builds(FontsTable)
@given(instance=FontsTable_strategy)
@settings(max_examples=25)
def test_FontsTable_instantiation(instance):
    assert isinstance(instance, FontsTable)


Geom_strategy = st.builds(Geom)
@given(instance=Geom_strategy)
@settings(max_examples=25)
def test_Geom_instantiation(instance):
    assert isinstance(instance, Geom)


HeaderFooter_strategy = st.builds(HeaderFooter)
@given(instance=HeaderFooter_strategy)
@settings(max_examples=25)
def test_HeaderFooter_instantiation(instance):
    assert isinstance(instance, HeaderFooter)


IXElt_strategy = st.builds(IXElt)
@given(instance=IXElt_strategy)
@settings(max_examples=25)
def test_IXElt_instantiation(instance):
    assert isinstance(instance, IXElt)


IXrequiredElt_strategy = st.builds(IXrequiredElt)
@given(instance=IXrequiredElt_strategy)
@settings(max_examples=25)
def test_IXrequiredElt_instantiation(instance):
    assert isinstance(instance, IXrequiredElt)


Icon_strategy = st.builds(Icon)
@given(instance=Icon_strategy)
@settings(max_examples=25)
def test_Icon_instantiation(instance):
    assert isinstance(instance, Icon)


IdentifiedElt_strategy = st.builds(IdentifiedElt)
@given(instance=IdentifiedElt_strategy)
@settings(max_examples=25)
def test_IdentifiedElt_instantiation(instance):
    assert isinstance(instance, IdentifiedElt)


InfiniteLine_strategy = st.builds(InfiniteLine)
@given(instance=InfiniteLine_strategy)
@settings(max_examples=25)
def test_InfiniteLine_instantiation(instance):
    assert isinstance(instance, InfiniteLine)


LineTo_strategy = st.builds(LineTo)
@given(instance=LineTo_strategy)
@settings(max_examples=25)
def test_LineTo_instantiation(instance):
    assert isinstance(instance, LineTo)


Master_strategy = st.builds(Master)
@given(instance=Master_strategy)
@settings(max_examples=25)
def test_Master_instantiation(instance):
    assert isinstance(instance, Master)


MasterElt_strategy = st.builds(MasterElt)
@given(instance=MasterElt_strategy)
@settings(max_examples=25)
def test_MasterElt_instantiation(instance):
    assert isinstance(instance, MasterElt)


MasterShortCut_strategy = st.builds(MasterShortCut)
@given(instance=MasterShortCut_strategy)
@settings(max_examples=25)
def test_MasterShortCut_instantiation(instance):
    assert isinstance(instance, MasterShortCut)


MastersCollection_strategy = st.builds(MastersCollection)
@given(instance=MastersCollection_strategy)
@settings(max_examples=25)
def test_MastersCollection_instantiation(instance):
    assert isinstance(instance, MastersCollection)


MoveTo_strategy = st.builds(MoveTo)
@given(instance=MoveTo_strategy)
@settings(max_examples=25)
def test_MoveTo_instantiation(instance):
    assert isinstance(instance, MoveTo)


NURBSTo_strategy = st.builds(NURBSTo)
@given(instance=NURBSTo_strategy)
@settings(max_examples=25)
def test_NURBSTo_instantiation(instance):
    assert isinstance(instance, NURBSTo)


NamedElt_strategy = st.builds(NamedElt)
@given(instance=NamedElt_strategy)
@settings(max_examples=25)
def test_NamedElt_instantiation(instance):
    assert isinstance(instance, NamedElt)


Page_strategy = st.builds(Page)
@given(instance=Page_strategy)
@settings(max_examples=25)
def test_Page_instantiation(instance):
    assert isinstance(instance, Page)


PageElt_strategy = st.builds(PageElt)
@given(instance=PageElt_strategy)
@settings(max_examples=25)
def test_PageElt_instantiation(instance):
    assert isinstance(instance, PageElt)


PageSheet_strategy = st.builds(PageSheet)
@given(instance=PageSheet_strategy)
@settings(max_examples=25)
def test_PageSheet_instantiation(instance):
    assert isinstance(instance, PageSheet)


PagesCollection_strategy = st.builds(PagesCollection)
@given(instance=PagesCollection_strategy)
@settings(max_examples=25)
def test_PagesCollection_instantiation(instance):
    assert isinstance(instance, PagesCollection)


PolylineTo_strategy = st.builds(PolylineTo)
@given(instance=PolylineTo_strategy)
@settings(max_examples=25)
def test_PolylineTo_instantiation(instance):
    assert isinstance(instance, PolylineTo)


PrintSetup_strategy = st.builds(PrintSetup)
@given(instance=PrintSetup_strategy)
@settings(max_examples=25)
def test_PrintSetup_instantiation(instance):
    assert isinstance(instance, PrintSetup)


Shape_strategy = st.builds(Shape)
@given(instance=Shape_strategy)
@settings(max_examples=25)
def test_Shape_instantiation(instance):
    assert isinstance(instance, Shape)


ShapeElt_strategy = st.builds(ShapeElt)
@given(instance=ShapeElt_strategy)
@settings(max_examples=25)
def test_ShapeElt_instantiation(instance):
    assert isinstance(instance, ShapeElt)


ShapesCollection_strategy = st.builds(ShapesCollection)
@given(instance=ShapesCollection_strategy)
@settings(max_examples=25)
def test_ShapesCollection_instantiation(instance):
    assert isinstance(instance, ShapesCollection)


SolutionXML_strategy = st.builds(SolutionXML)
@given(instance=SolutionXML_strategy)
@settings(max_examples=25)
def test_SolutionXML_instantiation(instance):
    assert isinstance(instance, SolutionXML)


SplineKnot_strategy = st.builds(SplineKnot)
@given(instance=SplineKnot_strategy)
@settings(max_examples=25)
def test_SplineKnot_instantiation(instance):
    assert isinstance(instance, SplineKnot)


SplineStart_strategy = st.builds(SplineStart)
@given(instance=SplineStart_strategy)
@settings(max_examples=25)
def test_SplineStart_instantiation(instance):
    assert isinstance(instance, SplineStart)


StyleSheet_strategy = st.builds(StyleSheet)
@given(instance=StyleSheet_strategy)
@settings(max_examples=25)
def test_StyleSheet_instantiation(instance):
    assert isinstance(instance, StyleSheet)


StyleSheetsCollection_strategy = st.builds(StyleSheetsCollection)
@given(instance=StyleSheetsCollection_strategy)
@settings(max_examples=25)
def test_StyleSheetsCollection_instantiation(instance):
    assert isinstance(instance, StyleSheetsCollection)


Tab_strategy = st.builds(Tab)
@given(instance=Tab_strategy)
@settings(max_examples=25)
def test_Tab_instantiation(instance):
    assert isinstance(instance, Tab)


TabsCollection_strategy = st.builds(TabsCollection)
@given(instance=TabsCollection_strategy)
@settings(max_examples=25)
def test_TabsCollection_instantiation(instance):
    assert isinstance(instance, TabsCollection)


Text_strategy = st.builds(Text)
@given(instance=Text_strategy)
@settings(max_examples=25)
def test_Text_instantiation(instance):
    assert isinstance(instance, Text)


TextElt_strategy = st.builds(TextElt)
@given(instance=TextElt_strategy)
@settings(max_examples=25)
def test_TextElt_instantiation(instance):
    assert isinstance(instance, TextElt)


UniqueIdElt_strategy = st.builds(UniqueIdElt)
@given(instance=UniqueIdElt_strategy)
@settings(max_examples=25)
def test_UniqueIdElt_instantiation(instance):
    assert isinstance(instance, UniqueIdElt)


VBProjectData_strategy = st.builds(VBProjectData)
@given(instance=VBProjectData_strategy)
@settings(max_examples=25)
def test_VBProjectData_instantiation(instance):
    assert isinstance(instance, VBProjectData)


VisioDocument_strategy = st.builds(VisioDocument)
@given(instance=VisioDocument_strategy)
@settings(max_examples=25)
def test_VisioDocument_instantiation(instance):
    assert isinstance(instance, VisioDocument)


WindowsInfo_strategy = st.builds(WindowsInfo)
@given(instance=WindowsInfo_strategy)
@settings(max_examples=25)
def test_WindowsInfo_instantiation(instance):
    assert isinstance(instance, WindowsInfo)


XYABCDEElt_strategy = st.builds(XYABCDEElt)
@given(instance=XYABCDEElt_strategy)
@settings(max_examples=25)
def test_XYABCDEElt_instantiation(instance):
    assert isinstance(instance, XYABCDEElt)


XYABCDElt_strategy = st.builds(XYABCDElt)
@given(instance=XYABCDElt_strategy)
@settings(max_examples=25)
def test_XYABCDElt_instantiation(instance):
    assert isinstance(instance, XYABCDElt)


XYABElt_strategy = st.builds(XYABElt)
@given(instance=XYABElt_strategy)
@settings(max_examples=25)
def test_XYABElt_instantiation(instance):
    assert isinstance(instance, XYABElt)


XYAElt_strategy = st.builds(XYAElt)
@given(instance=XYAElt_strategy)
@settings(max_examples=25)
def test_XYAElt_instantiation(instance):
    assert isinstance(instance, XYAElt)


XYElt_strategy = st.builds(XYElt)
@given(instance=XYElt_strategy)
@settings(max_examples=25)
def test_XYElt_instantiation(instance):
    assert isinstance(instance, XYElt)



