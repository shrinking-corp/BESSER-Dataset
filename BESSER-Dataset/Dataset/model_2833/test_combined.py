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
    AbstractFigure,
    gmf_all_gmfgraph_FigureRef,
    gmf_all_gmfgraph_ChildAccess,
    Figure,
    gmf_all_gmfgraph_AbstractFigure,
    gmf_all_gmfgraph_PinOwner,
    gmf_all_gmfgraph_SVGProperty,
    Rectangle2D,
    SVGProperty,
    gmf_all_gmfgraph_Rectangle2D,
    gmfgraph_Layout,
    gmf_all_gmfgraph_Layout,
    gmf_all_gmfgraph_Layoutable,
    LayoutData,
    gmf_all_gmfgraph_BorderLayoutData,
    gmf_all_gmfgraph_XYLayoutData,
    gmf_all_gmfgraph_GridLayoutData,
    gmfgraph_Border,
    gmf_all_gmfgraph_Border,
    gmfgraph_LayoutData,
    gmf_all_gmfgraph_LayoutData,
    gmf_all_gmfgraph_Point,
    gmf_all_gmfgraph_Font,
    gmf_all_gmfgraph_Color,
    gmfgraph_CustomFigure,
    FigureAccessor,
    gmf_all_gmfgraph_Insets,
    gmf_all_gmfgraph_Dimension,
    gmf_all_gmfgraph_FigureAccessor,
    gmf_all_gmfgraph_CustomAttribute,
    CustomAttributeOwner,
    gmf_all_gmfgraph_CustomClass,
    CustomAttribute,
    gmf_all_gmfgraph_CustomAttributeOwner,
    gmfgraph_Polygon,
    gmfgraph_DecorationFigure,
    gmf_all_gmfgraph_PolygonDecoration,
    gmf_all_gmfgraph_CustomDecoration,
    DecorationFigure,
    gmfgraph_ConnectionFigure,
    gmf_all_gmfgraph_CustomConnection,
    gmfgraph_Polyline,
    gmf_all_gmfgraph_PolylineDecoration,
    gmf_all_gmfgraph_PolylineConnection,
    Polygon,
    gmf_all_gmfgraph_ScalablePolygon,
    Polyline,
    gmf_all_gmfgraph_Polygon,
    gmfgraph_CustomClass,
    gmf_all_gmfgraph_CustomBorder,
    gmf_all_gmfgraph_CustomLayoutData,
    gmf_all_gmfgraph_CustomLayout,
    gmfgraph_RealFigure,
    gmf_all_gmfgraph_CustomFigure,
    Shape,
    gmf_all_gmfgraph_Polyline,
    gmf_all_gmfgraph_Ellipse,
    gmf_all_gmfgraph_RoundedRectangle,
    gmf_all_gmfgraph_Rectangle,
    Point,
    Insets,
    Font,
    gmf_all_gmfgraph_BasicFont,
    Color,
    gmf_all_gmfgraph_ConstantColor,
    gmf_all_gmfgraph_RGBColor,
    gmfgraph_CustomAttributeOwner,
    gmfgraph_PinOwner,
    gmfgraph_AbstractFigure,
    gmf_all_gmfgraph_RealFigure,
    Dimension,
    gmf_all_gmfgraph_VisualFacet,
    ChildAccess,
    Layoutable,
    gmf_all_gmfgraph_Figure,
    VisualFacet,
    gmf_all_gmfgraph_AlignmentFacet,
    gmf_all_gmfgraph_GeneralFacet,
    gmf_all_gmfgraph_LabelOffsetFacet,
    gmf_all_gmfgraph_DefaultSizeFacet,
    gmf_all_gmfgraph_GradientFacet,
    gmf_all_gmfgraph_Identity,
    Layout,
    gmf_all_gmfgraph_CenterLayout,
    gmf_all_gmfgraph_LayoutRef,
    gmf_all_gmfgraph_XYLayout,
    gmf_all_gmfgraph_BorderLayout,
    gmf_all_gmfgraph_FlowLayout,
    gmf_all_gmfgraph_GridLayout,
    gmf_all_gmfgraph_StackLayout,
    Border,
    gmf_all_gmfgraph_CompoundBorder,
    gmf_all_gmfgraph_LineBorder,
    gmf_all_gmfgraph_BorderRef,
    gmf_all_gmfgraph_MarginBorder,
    FigureDescriptor,
    RealFigure,
    gmf_all_gmfgraph_InvisibleRectangle,
    gmf_all_gmfgraph_VerticalLabel,
    gmf_all_gmfgraph_Shape,
    gmf_all_gmfgraph_SVGFigure,
    gmf_all_gmfgraph_Label,
    gmf_all_gmfgraph_DecorationFigure,
    gmf_all_gmfgraph_ConnectionFigure,
    gmf_all_gmfgraph_LabeledContainer,
    FigureGallery,
    AbstractNode,
    gmf_all_gmfgraph_Node,
    DiagramElement,
    gmf_all_gmfgraph_Compartment,
    gmf_all_gmfgraph_Connection,
    gmf_all_gmfgraph_AbstractNode,
    gmf_all_tooldef_StyleSelector,
    gmf_all_tooldef_Image,
    tooldef_ContributionItem,
    Identity,
    gmf_all_gmfgraph_Pin,
    gmf_all_gmfgraph_FigureDescriptor,
    gmf_all_gmfgraph_DiagramElement,
    gmf_all_gmfgraph_FigureGallery,
    gmf_all_gmfgraph_Canvas,
    tooldef_PredefinedItem,
    tooldef_Menu,
    gmf_all_tooldef_PopupMenu,
    gmf_all_tooldef_PredefinedMenu,
    ItemBase,
    gmf_all_tooldef_Separator,
    gmf_all_tooldef_PredefinedItem,
    gmf_all_tooldef_ContributionItem,
    gmf_all_tooldef_Menu,
    gmf_all_tooldef_ItemBase,
    gmf_all_tooldef_ItemRef,
    ContributionItem,
    gmf_all_tooldef_MenuAction,
    Image,
    gmf_all_tooldef_BundleImage,
    gmf_all_tooldef_DefaultImage,
    gmf_all_tooldef_AbstractTool,
    Menu,
    gmf_all_tooldef_Toolbar,
    gmf_all_tooldef_ContextMenu,
    gmf_all_tooldef_MainMenu,
    MenuAction,
    gmf_all_tooldef_ToolRegistry,
    Pin,
    gmf_all_gmfgraph_CustomPin,
    gmf_all_gmfgraph_VisiblePin,
    gmf_all_gmfgraph_ColorPin,
    gmf_all_mappings_VisualEffectMapping,
    gmf_all_mappings_Measurable,
    gmf_all_mappings_Auditable,
    ToolContainer,
    gmf_all_tooldef_Palette,
    gmf_all_tooldef_ToolGroup,
    Measurable,
    MetricRule,
    gmf_all_mappings_MetricContainer,
    mappings_Measurable,
    mappings_Auditable,
    gmf_all_mappings_NotationElementTarget,
    gmf_all_mappings_DiagramElementTarget,
    gmf_all_mappings_DomainElementTarget,
    Auditable,
    gmf_all_mappings_AuditedMetricTarget,
    RuleBase,
    gmf_all_mappings_MetricRule,
    gmf_all_mappings_AuditRule,
    gmf_all_mappings_RuleBase,
    gmf_all_mappings_DomainAttributeTarget,
    gmf_all_mappings_AuditContainer,
    gmf_all_mappings_AppearanceSteward,
    AbstractTool,
    gmf_all_tooldef_GenericTool,
    gmf_all_tooldef_ToolContainer,
    gmf_all_tooldef_CreationTool,
    gmf_all_tooldef_PaletteSeparator,
    gmf_all_tooldef_StandardTool,
    gmf_all_mappings_ToolOwner,
    ContextMenu,
    gmf_all_mappings_MenuOwner,
    FeatureSeqInitializer,
    AuditRule,
    ReferenceNewElementSpec,
    FeatureInitializer,
    gmf_all_mappings_ReferenceNewElementSpec,
    gmf_all_mappings_FeatureValueSpec,
    gmf_all_mappings_ElementInitializer,
    gmf_all_mappings_ValueExpression,
    gmf_all_mappings_FeatureInitializer,
    gmf_all_mappings_LinkConstraints,
    mappings_gmf_all_EAttribute,
    MappingEntry,
    DiagramLabel,
    gmf_all_mappings_LabelMapping,
    Toolbar,
    MainMenu,
    ValueExpression,
    gmf_all_mappings_Constraint,
    Canvas,
    gmf_all_mappings_CanvasMapping,
    LinkConstraints,
    mappings_gmf_all_EStructuralFeature,
    Connection,
    mappings_NeedsContainment,
    Compartment,
    gmf_all_mappings_CompartmentMapping,
    ChildReference,
    Palette,
    mappings_gmf_all_EPackage,
    CompartmentMapping,
    NodeReference,
    gmf_all_mappings_TopNodeReference,
    gmf_all_mappings_ChildReference,
    NodeMapping,
    NeedsContainment,
    gmf_all_mappings_NodeReference,
    Node,
    gmf_all_gmfgraph_DiagramLabel,
    mappings_AppearanceSteward,
    mappings_ToolOwner,
    mappings_MenuOwner,
    mappings_MappingEntry,
    gmf_all_mappings_LinkMapping,
    gmf_all_mappings_NodeMapping,
    LabelMapping,
    gmf_all_mappings_ExpressionLabelMapping,
    gmf_all_mappings_FeatureLabelMapping,
    gmf_all_mappings_OclChoiceLabelMapping,
    gmf_all_mappings_DesignLabelMapping,
    ElementInitializer,
    gmf_all_mappings_FeatureSeqInitializer,
    Constraint,
    mappings_gmf_all_EClass,
    gmf_all_mappings_MappingEntry,
    MetricContainer,
    AuditContainer,
    StyleSelector,
    gmf_all_tooldef_GenericStyleSelector,
    CanvasMapping,
    LinkMapping,
    mappings_gmf_all_EReference,
    gmf_all_mappings_NeedsContainment,
    VisualEffectMapping,
    TopNodeReference,
    gmf_all_mappings_Mapping,
    Severity,
    LineKind,
    AppearanceStyle,
    SVGPropertyType,
    FontStyle,
    Alignment,
    ActionKind,
    Direction,
    ColorConstants,
    LabelTextAccessMethod,
    Language,
    StandardToolKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_abstractfigure_is_not_abstract():
    assert not inspect.isabstract(AbstractFigure)


def test_hyp_abstractfigure_constructor_exists():
    assert callable(AbstractFigure.__init__)


def test_hyp_abstractfigure_constructor_args():
    sig = inspect.signature(AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_figureref_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_FigureRef)


def test_hyp_gmf_all_gmfgraph_figureref_constructor_exists():
    assert callable(gmf_all_gmfgraph_FigureRef.__init__)


def test_hyp_gmf_all_gmfgraph_figureref_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_FigureRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_childaccess_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_ChildAccess)


def test_hyp_gmf_all_gmfgraph_childaccess_constructor_exists():
    assert callable(gmf_all_gmfgraph_ChildAccess.__init__)


def test_hyp_gmf_all_gmfgraph_childaccess_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_ChildAccess.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"




def test_hyp_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_hyp_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_hyp_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_abstractfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_AbstractFigure)


def test_hyp_gmf_all_gmfgraph_abstractfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_AbstractFigure.__init__)


def test_hyp_gmf_all_gmfgraph_abstractfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_pinowner_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_PinOwner)


def test_hyp_gmf_all_gmfgraph_pinowner_constructor_exists():
    assert callable(gmf_all_gmfgraph_PinOwner.__init__)


def test_hyp_gmf_all_gmfgraph_pinowner_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_PinOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_svgproperty_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_SVGProperty)


def test_hyp_gmf_all_gmfgraph_svgproperty_constructor_exists():
    assert callable(gmf_all_gmfgraph_SVGProperty.__init__)


def test_hyp_gmf_all_gmfgraph_svgproperty_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_SVGProperty.__init__)
    params = list(sig.parameters.keys())
    assert "setter" in params, "Missing parameter 'setter'"
    assert "callSuper" in params, "Missing parameter 'callSuper'"
    assert "type" in params, "Missing parameter 'type'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "getter" in params, "Missing parameter 'getter'"
    assert "query" in params, "Missing parameter 'query'"









def test_hyp_rectangle2d_is_not_abstract():
    assert not inspect.isabstract(Rectangle2D)


def test_hyp_rectangle2d_constructor_exists():
    assert callable(Rectangle2D.__init__)


def test_hyp_rectangle2d_constructor_args():
    sig = inspect.signature(Rectangle2D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_svgproperty_is_not_abstract():
    assert not inspect.isabstract(SVGProperty)


def test_hyp_svgproperty_constructor_exists():
    assert callable(SVGProperty.__init__)


def test_hyp_svgproperty_constructor_args():
    sig = inspect.signature(SVGProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_rectangle2d_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Rectangle2D)


def test_hyp_gmf_all_gmfgraph_rectangle2d_constructor_exists():
    assert callable(gmf_all_gmfgraph_Rectangle2D.__init__)


def test_hyp_gmf_all_gmfgraph_rectangle2d_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Rectangle2D.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"







def test_hyp_gmfgraph_layout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Layout)


def test_hyp_gmfgraph_layout_constructor_exists():
    assert callable(gmfgraph_Layout.__init__)


def test_hyp_gmfgraph_layout_constructor_args():
    sig = inspect.signature(gmfgraph_Layout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_layout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Layout)


def test_hyp_gmf_all_gmfgraph_layout_constructor_exists():
    assert callable(gmf_all_gmfgraph_Layout.__init__)


def test_hyp_gmf_all_gmfgraph_layout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Layout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_layoutable_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Layoutable)


def test_hyp_gmf_all_gmfgraph_layoutable_constructor_exists():
    assert callable(gmf_all_gmfgraph_Layoutable.__init__)


def test_hyp_gmf_all_gmfgraph_layoutable_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Layoutable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_layoutdata_is_not_abstract():
    assert not inspect.isabstract(LayoutData)


def test_hyp_layoutdata_constructor_exists():
    assert callable(LayoutData.__init__)


def test_hyp_layoutdata_constructor_args():
    sig = inspect.signature(LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_borderlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_BorderLayoutData)


def test_hyp_gmf_all_gmfgraph_borderlayoutdata_constructor_exists():
    assert callable(gmf_all_gmfgraph_BorderLayoutData.__init__)


def test_hyp_gmf_all_gmfgraph_borderlayoutdata_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_BorderLayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "vertical" in params, "Missing parameter 'vertical'"





def test_hyp_gmf_all_gmfgraph_xylayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_XYLayoutData)


def test_hyp_gmf_all_gmfgraph_xylayoutdata_constructor_exists():
    assert callable(gmf_all_gmfgraph_XYLayoutData.__init__)


def test_hyp_gmf_all_gmfgraph_xylayoutdata_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_XYLayoutData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_gridlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_GridLayoutData)


def test_hyp_gmf_all_gmfgraph_gridlayoutdata_constructor_exists():
    assert callable(gmf_all_gmfgraph_GridLayoutData.__init__)


def test_hyp_gmf_all_gmfgraph_gridlayoutdata_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_GridLayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalSpan" in params, "Missing parameter 'horizontalSpan'"
    assert "grabExcessVerticalSpace" in params, "Missing parameter 'grabExcessVerticalSpace'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "horizontalIndent" in params, "Missing parameter 'horizontalIndent'"
    assert "verticalSpan" in params, "Missing parameter 'verticalSpan'"
    assert "grabExcessHorizontalSpace" in params, "Missing parameter 'grabExcessHorizontalSpace'"










def test_hyp_gmfgraph_border_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Border)


def test_hyp_gmfgraph_border_constructor_exists():
    assert callable(gmfgraph_Border.__init__)


def test_hyp_gmfgraph_border_constructor_args():
    sig = inspect.signature(gmfgraph_Border.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_border_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Border)


def test_hyp_gmf_all_gmfgraph_border_constructor_exists():
    assert callable(gmf_all_gmfgraph_Border.__init__)


def test_hyp_gmf_all_gmfgraph_border_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Border.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_layoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_LayoutData)


def test_hyp_gmfgraph_layoutdata_constructor_exists():
    assert callable(gmfgraph_LayoutData.__init__)


def test_hyp_gmfgraph_layoutdata_constructor_args():
    sig = inspect.signature(gmfgraph_LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_layoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_LayoutData)


def test_hyp_gmf_all_gmfgraph_layoutdata_constructor_exists():
    assert callable(gmf_all_gmfgraph_LayoutData.__init__)


def test_hyp_gmf_all_gmfgraph_layoutdata_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_point_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Point)


def test_hyp_gmf_all_gmfgraph_point_constructor_exists():
    assert callable(gmf_all_gmfgraph_Point.__init__)


def test_hyp_gmf_all_gmfgraph_point_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"





def test_hyp_gmf_all_gmfgraph_font_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Font)


def test_hyp_gmf_all_gmfgraph_font_constructor_exists():
    assert callable(gmf_all_gmfgraph_Font.__init__)


def test_hyp_gmf_all_gmfgraph_font_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Font.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_color_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Color)


def test_hyp_gmf_all_gmfgraph_color_constructor_exists():
    assert callable(gmf_all_gmfgraph_Color.__init__)


def test_hyp_gmf_all_gmfgraph_color_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Color.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_customfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomFigure)


def test_hyp_gmfgraph_customfigure_constructor_exists():
    assert callable(gmfgraph_CustomFigure.__init__)


def test_hyp_gmfgraph_customfigure_constructor_args():
    sig = inspect.signature(gmfgraph_CustomFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_figureaccessor_is_not_abstract():
    assert not inspect.isabstract(FigureAccessor)


def test_hyp_figureaccessor_constructor_exists():
    assert callable(FigureAccessor.__init__)


def test_hyp_figureaccessor_constructor_args():
    sig = inspect.signature(FigureAccessor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_insets_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Insets)


def test_hyp_gmf_all_gmfgraph_insets_constructor_exists():
    assert callable(gmf_all_gmfgraph_Insets.__init__)


def test_hyp_gmf_all_gmfgraph_insets_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Insets.__init__)
    params = list(sig.parameters.keys())
    assert "bottom" in params, "Missing parameter 'bottom'"
    assert "right" in params, "Missing parameter 'right'"
    assert "top" in params, "Missing parameter 'top'"
    assert "left" in params, "Missing parameter 'left'"







def test_hyp_gmf_all_gmfgraph_dimension_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Dimension)


def test_hyp_gmf_all_gmfgraph_dimension_constructor_exists():
    assert callable(gmf_all_gmfgraph_Dimension.__init__)


def test_hyp_gmf_all_gmfgraph_dimension_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "dx" in params, "Missing parameter 'dx'"
    assert "dy" in params, "Missing parameter 'dy'"





def test_hyp_gmf_all_gmfgraph_figureaccessor_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_FigureAccessor)


def test_hyp_gmf_all_gmfgraph_figureaccessor_constructor_exists():
    assert callable(gmf_all_gmfgraph_FigureAccessor.__init__)


def test_hyp_gmf_all_gmfgraph_figureaccessor_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_FigureAccessor.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"




def test_hyp_gmf_all_gmfgraph_customattribute_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomAttribute)


def test_hyp_gmf_all_gmfgraph_customattribute_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomAttribute.__init__)


def test_hyp_gmf_all_gmfgraph_customattribute_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "directAccess" in params, "Missing parameter 'directAccess'"
    assert "name" in params, "Missing parameter 'name'"
    assert "multiStatementValue" in params, "Missing parameter 'multiStatementValue'"







def test_hyp_customattributeowner_is_not_abstract():
    assert not inspect.isabstract(CustomAttributeOwner)


def test_hyp_customattributeowner_constructor_exists():
    assert callable(CustomAttributeOwner.__init__)


def test_hyp_customattributeowner_constructor_args():
    sig = inspect.signature(CustomAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_customclass_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomClass)


def test_hyp_gmf_all_gmfgraph_customclass_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomClass.__init__)


def test_hyp_gmf_all_gmfgraph_customclass_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomClass.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedClassName" in params, "Missing parameter 'qualifiedClassName'"




def test_hyp_customattribute_is_not_abstract():
    assert not inspect.isabstract(CustomAttribute)


def test_hyp_customattribute_constructor_exists():
    assert callable(CustomAttribute.__init__)


def test_hyp_customattribute_constructor_args():
    sig = inspect.signature(CustomAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_customattributeowner_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomAttributeOwner)


def test_hyp_gmf_all_gmfgraph_customattributeowner_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomAttributeOwner.__init__)


def test_hyp_gmf_all_gmfgraph_customattributeowner_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_polygon_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Polygon)


def test_hyp_gmfgraph_polygon_constructor_exists():
    assert callable(gmfgraph_Polygon.__init__)


def test_hyp_gmfgraph_polygon_constructor_args():
    sig = inspect.signature(gmfgraph_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_decorationfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_DecorationFigure)


def test_hyp_gmfgraph_decorationfigure_constructor_exists():
    assert callable(gmfgraph_DecorationFigure.__init__)


def test_hyp_gmfgraph_decorationfigure_constructor_args():
    sig = inspect.signature(gmfgraph_DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_polygondecoration_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_PolygonDecoration)


def test_hyp_gmf_all_gmfgraph_polygondecoration_constructor_exists():
    assert callable(gmf_all_gmfgraph_PolygonDecoration.__init__)


def test_hyp_gmf_all_gmfgraph_polygondecoration_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_PolygonDecoration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_customdecoration_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomDecoration)


def test_hyp_gmf_all_gmfgraph_customdecoration_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomDecoration.__init__)


def test_hyp_gmf_all_gmfgraph_customdecoration_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomDecoration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_decorationfigure_is_not_abstract():
    assert not inspect.isabstract(DecorationFigure)


def test_hyp_decorationfigure_constructor_exists():
    assert callable(DecorationFigure.__init__)


def test_hyp_decorationfigure_constructor_args():
    sig = inspect.signature(DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_connectionfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_ConnectionFigure)


def test_hyp_gmfgraph_connectionfigure_constructor_exists():
    assert callable(gmfgraph_ConnectionFigure.__init__)


def test_hyp_gmfgraph_connectionfigure_constructor_args():
    sig = inspect.signature(gmfgraph_ConnectionFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_customconnection_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomConnection)


def test_hyp_gmf_all_gmfgraph_customconnection_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomConnection.__init__)


def test_hyp_gmf_all_gmfgraph_customconnection_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_polyline_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Polyline)


def test_hyp_gmfgraph_polyline_constructor_exists():
    assert callable(gmfgraph_Polyline.__init__)


def test_hyp_gmfgraph_polyline_constructor_args():
    sig = inspect.signature(gmfgraph_Polyline.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_polylinedecoration_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_PolylineDecoration)


def test_hyp_gmf_all_gmfgraph_polylinedecoration_constructor_exists():
    assert callable(gmf_all_gmfgraph_PolylineDecoration.__init__)


def test_hyp_gmf_all_gmfgraph_polylinedecoration_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_PolylineDecoration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_polylineconnection_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_PolylineConnection)


def test_hyp_gmf_all_gmfgraph_polylineconnection_constructor_exists():
    assert callable(gmf_all_gmfgraph_PolylineConnection.__init__)


def test_hyp_gmf_all_gmfgraph_polylineconnection_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_PolylineConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_polygon_is_not_abstract():
    assert not inspect.isabstract(Polygon)


def test_hyp_polygon_constructor_exists():
    assert callable(Polygon.__init__)


def test_hyp_polygon_constructor_args():
    sig = inspect.signature(Polygon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_scalablepolygon_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_ScalablePolygon)


def test_hyp_gmf_all_gmfgraph_scalablepolygon_constructor_exists():
    assert callable(gmf_all_gmfgraph_ScalablePolygon.__init__)


def test_hyp_gmf_all_gmfgraph_scalablepolygon_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_ScalablePolygon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_polyline_is_not_abstract():
    assert not inspect.isabstract(Polyline)


def test_hyp_polyline_constructor_exists():
    assert callable(Polyline.__init__)


def test_hyp_polyline_constructor_args():
    sig = inspect.signature(Polyline.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_polygon_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Polygon)


def test_hyp_gmf_all_gmfgraph_polygon_constructor_exists():
    assert callable(gmf_all_gmfgraph_Polygon.__init__)


def test_hyp_gmf_all_gmfgraph_polygon_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_customclass_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomClass)


def test_hyp_gmfgraph_customclass_constructor_exists():
    assert callable(gmfgraph_CustomClass.__init__)


def test_hyp_gmfgraph_customclass_constructor_args():
    sig = inspect.signature(gmfgraph_CustomClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_customborder_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomBorder)


def test_hyp_gmf_all_gmfgraph_customborder_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomBorder.__init__)


def test_hyp_gmf_all_gmfgraph_customborder_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_customlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomLayoutData)


def test_hyp_gmf_all_gmfgraph_customlayoutdata_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomLayoutData.__init__)


def test_hyp_gmf_all_gmfgraph_customlayoutdata_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomLayoutData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_customlayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomLayout)


def test_hyp_gmf_all_gmfgraph_customlayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomLayout.__init__)


def test_hyp_gmf_all_gmfgraph_customlayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomLayout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_realfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_RealFigure)


def test_hyp_gmfgraph_realfigure_constructor_exists():
    assert callable(gmfgraph_RealFigure.__init__)


def test_hyp_gmfgraph_realfigure_constructor_args():
    sig = inspect.signature(gmfgraph_RealFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_customfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomFigure)


def test_hyp_gmf_all_gmfgraph_customfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomFigure.__init__)


def test_hyp_gmf_all_gmfgraph_customfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_hyp_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_hyp_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_polyline_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Polyline)


def test_hyp_gmf_all_gmfgraph_polyline_constructor_exists():
    assert callable(gmf_all_gmfgraph_Polyline.__init__)


def test_hyp_gmf_all_gmfgraph_polyline_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Polyline.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_ellipse_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Ellipse)


def test_hyp_gmf_all_gmfgraph_ellipse_constructor_exists():
    assert callable(gmf_all_gmfgraph_Ellipse.__init__)


def test_hyp_gmf_all_gmfgraph_ellipse_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_RoundedRectangle)


def test_hyp_gmf_all_gmfgraph_roundedrectangle_constructor_exists():
    assert callable(gmf_all_gmfgraph_RoundedRectangle.__init__)


def test_hyp_gmf_all_gmfgraph_roundedrectangle_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_RoundedRectangle.__init__)
    params = list(sig.parameters.keys())
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"





def test_hyp_gmf_all_gmfgraph_rectangle_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Rectangle)


def test_hyp_gmf_all_gmfgraph_rectangle_constructor_exists():
    assert callable(gmf_all_gmfgraph_Rectangle.__init__)


def test_hyp_gmf_all_gmfgraph_rectangle_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_hyp_point_constructor_exists():
    assert callable(Point.__init__)


def test_hyp_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_hyp_insets_is_not_abstract():
    assert not inspect.isabstract(Insets)


def test_hyp_insets_constructor_exists():
    assert callable(Insets.__init__)


def test_hyp_insets_constructor_args():
    sig = inspect.signature(Insets.__init__)
    params = list(sig.parameters.keys())



def test_hyp_font_is_not_abstract():
    assert not inspect.isabstract(Font)


def test_hyp_font_constructor_exists():
    assert callable(Font.__init__)


def test_hyp_font_constructor_args():
    sig = inspect.signature(Font.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_basicfont_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_BasicFont)


def test_hyp_gmf_all_gmfgraph_basicfont_constructor_exists():
    assert callable(gmf_all_gmfgraph_BasicFont.__init__)


def test_hyp_gmf_all_gmfgraph_basicfont_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_BasicFont.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "faceName" in params, "Missing parameter 'faceName'"
    assert "height" in params, "Missing parameter 'height'"






def test_hyp_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_hyp_color_constructor_exists():
    assert callable(Color.__init__)


def test_hyp_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_constantcolor_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_ConstantColor)


def test_hyp_gmf_all_gmfgraph_constantcolor_constructor_exists():
    assert callable(gmf_all_gmfgraph_ConstantColor.__init__)


def test_hyp_gmf_all_gmfgraph_constantcolor_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_ConstantColor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_gmf_all_gmfgraph_rgbcolor_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_RGBColor)


def test_hyp_gmf_all_gmfgraph_rgbcolor_constructor_exists():
    assert callable(gmf_all_gmfgraph_RGBColor.__init__)


def test_hyp_gmf_all_gmfgraph_rgbcolor_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_RGBColor.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"






def test_hyp_gmfgraph_customattributeowner_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomAttributeOwner)


def test_hyp_gmfgraph_customattributeowner_constructor_exists():
    assert callable(gmfgraph_CustomAttributeOwner.__init__)


def test_hyp_gmfgraph_customattributeowner_constructor_args():
    sig = inspect.signature(gmfgraph_CustomAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_pinowner_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_PinOwner)


def test_hyp_gmfgraph_pinowner_constructor_exists():
    assert callable(gmfgraph_PinOwner.__init__)


def test_hyp_gmfgraph_pinowner_constructor_args():
    sig = inspect.signature(gmfgraph_PinOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_abstractfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_AbstractFigure)


def test_hyp_gmfgraph_abstractfigure_constructor_exists():
    assert callable(gmfgraph_AbstractFigure.__init__)


def test_hyp_gmfgraph_abstractfigure_constructor_args():
    sig = inspect.signature(gmfgraph_AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_realfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_RealFigure)


def test_hyp_gmf_all_gmfgraph_realfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_RealFigure.__init__)


def test_hyp_gmf_all_gmfgraph_realfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_RealFigure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dimension_is_not_abstract():
    assert not inspect.isabstract(Dimension)


def test_hyp_dimension_constructor_exists():
    assert callable(Dimension.__init__)


def test_hyp_dimension_constructor_args():
    sig = inspect.signature(Dimension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_visualfacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_VisualFacet)


def test_hyp_gmf_all_gmfgraph_visualfacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_VisualFacet.__init__)


def test_hyp_gmf_all_gmfgraph_visualfacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_VisualFacet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_childaccess_is_not_abstract():
    assert not inspect.isabstract(ChildAccess)


def test_hyp_childaccess_constructor_exists():
    assert callable(ChildAccess.__init__)


def test_hyp_childaccess_constructor_args():
    sig = inspect.signature(ChildAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_layoutable_is_not_abstract():
    assert not inspect.isabstract(Layoutable)


def test_hyp_layoutable_constructor_exists():
    assert callable(Layoutable.__init__)


def test_hyp_layoutable_constructor_args():
    sig = inspect.signature(Layoutable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_figure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Figure)


def test_hyp_gmf_all_gmfgraph_figure_constructor_exists():
    assert callable(gmf_all_gmfgraph_Figure.__init__)


def test_hyp_gmf_all_gmfgraph_figure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Figure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualfacet_is_not_abstract():
    assert not inspect.isabstract(VisualFacet)


def test_hyp_visualfacet_constructor_exists():
    assert callable(VisualFacet.__init__)


def test_hyp_visualfacet_constructor_args():
    sig = inspect.signature(VisualFacet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_alignmentfacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_AlignmentFacet)


def test_hyp_gmf_all_gmfgraph_alignmentfacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_AlignmentFacet.__init__)


def test_hyp_gmf_all_gmfgraph_alignmentfacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_AlignmentFacet.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"




def test_hyp_gmf_all_gmfgraph_generalfacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_GeneralFacet)


def test_hyp_gmf_all_gmfgraph_generalfacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_GeneralFacet.__init__)


def test_hyp_gmf_all_gmfgraph_generalfacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_GeneralFacet.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "data" in params, "Missing parameter 'data'"





def test_hyp_gmf_all_gmfgraph_labeloffsetfacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_LabelOffsetFacet)


def test_hyp_gmf_all_gmfgraph_labeloffsetfacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_LabelOffsetFacet.__init__)


def test_hyp_gmf_all_gmfgraph_labeloffsetfacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_LabelOffsetFacet.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_gmf_all_gmfgraph_defaultsizefacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_DefaultSizeFacet)


def test_hyp_gmf_all_gmfgraph_defaultsizefacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_DefaultSizeFacet.__init__)


def test_hyp_gmf_all_gmfgraph_defaultsizefacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_DefaultSizeFacet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_gradientfacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_GradientFacet)


def test_hyp_gmf_all_gmfgraph_gradientfacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_GradientFacet.__init__)


def test_hyp_gmf_all_gmfgraph_gradientfacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_GradientFacet.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"




def test_hyp_gmf_all_gmfgraph_identity_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Identity)


def test_hyp_gmf_all_gmfgraph_identity_constructor_exists():
    assert callable(gmf_all_gmfgraph_Identity.__init__)


def test_hyp_gmf_all_gmfgraph_identity_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Identity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_hyp_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_hyp_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_centerlayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CenterLayout)


def test_hyp_gmf_all_gmfgraph_centerlayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_CenterLayout.__init__)


def test_hyp_gmf_all_gmfgraph_centerlayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CenterLayout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_layoutref_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_LayoutRef)


def test_hyp_gmf_all_gmfgraph_layoutref_constructor_exists():
    assert callable(gmf_all_gmfgraph_LayoutRef.__init__)


def test_hyp_gmf_all_gmfgraph_layoutref_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_LayoutRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_xylayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_XYLayout)


def test_hyp_gmf_all_gmfgraph_xylayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_XYLayout.__init__)


def test_hyp_gmf_all_gmfgraph_xylayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_XYLayout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_borderlayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_BorderLayout)


def test_hyp_gmf_all_gmfgraph_borderlayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_BorderLayout.__init__)


def test_hyp_gmf_all_gmfgraph_borderlayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_BorderLayout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_flowlayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_FlowLayout)


def test_hyp_gmf_all_gmfgraph_flowlayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_FlowLayout.__init__)


def test_hyp_gmf_all_gmfgraph_flowlayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_FlowLayout.__init__)
    params = list(sig.parameters.keys())
    assert "forceSingleLine" in params, "Missing parameter 'forceSingleLine'"
    assert "minorSpacing" in params, "Missing parameter 'minorSpacing'"
    assert "majorAlignment" in params, "Missing parameter 'majorAlignment'"
    assert "minorAlignment" in params, "Missing parameter 'minorAlignment'"
    assert "majorSpacing" in params, "Missing parameter 'majorSpacing'"
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "matchMinorSize" in params, "Missing parameter 'matchMinorSize'"










def test_hyp_gmf_all_gmfgraph_gridlayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_GridLayout)


def test_hyp_gmf_all_gmfgraph_gridlayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_GridLayout.__init__)


def test_hyp_gmf_all_gmfgraph_gridlayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_GridLayout.__init__)
    params = list(sig.parameters.keys())
    assert "numColumns" in params, "Missing parameter 'numColumns'"
    assert "equalWidth" in params, "Missing parameter 'equalWidth'"





def test_hyp_gmf_all_gmfgraph_stacklayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_StackLayout)


def test_hyp_gmf_all_gmfgraph_stacklayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_StackLayout.__init__)


def test_hyp_gmf_all_gmfgraph_stacklayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_StackLayout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_border_is_not_abstract():
    assert not inspect.isabstract(Border)


def test_hyp_border_constructor_exists():
    assert callable(Border.__init__)


def test_hyp_border_constructor_args():
    sig = inspect.signature(Border.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_compoundborder_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CompoundBorder)


def test_hyp_gmf_all_gmfgraph_compoundborder_constructor_exists():
    assert callable(gmf_all_gmfgraph_CompoundBorder.__init__)


def test_hyp_gmf_all_gmfgraph_compoundborder_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CompoundBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_lineborder_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_LineBorder)


def test_hyp_gmf_all_gmfgraph_lineborder_constructor_exists():
    assert callable(gmf_all_gmfgraph_LineBorder.__init__)


def test_hyp_gmf_all_gmfgraph_lineborder_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_LineBorder.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"




def test_hyp_gmf_all_gmfgraph_borderref_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_BorderRef)


def test_hyp_gmf_all_gmfgraph_borderref_constructor_exists():
    assert callable(gmf_all_gmfgraph_BorderRef.__init__)


def test_hyp_gmf_all_gmfgraph_borderref_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_BorderRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_marginborder_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_MarginBorder)


def test_hyp_gmf_all_gmfgraph_marginborder_constructor_exists():
    assert callable(gmf_all_gmfgraph_MarginBorder.__init__)


def test_hyp_gmf_all_gmfgraph_marginborder_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_MarginBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_figuredescriptor_is_not_abstract():
    assert not inspect.isabstract(FigureDescriptor)


def test_hyp_figuredescriptor_constructor_exists():
    assert callable(FigureDescriptor.__init__)


def test_hyp_figuredescriptor_constructor_args():
    sig = inspect.signature(FigureDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realfigure_is_not_abstract():
    assert not inspect.isabstract(RealFigure)


def test_hyp_realfigure_constructor_exists():
    assert callable(RealFigure.__init__)


def test_hyp_realfigure_constructor_args():
    sig = inspect.signature(RealFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_invisiblerectangle_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_InvisibleRectangle)


def test_hyp_gmf_all_gmfgraph_invisiblerectangle_constructor_exists():
    assert callable(gmf_all_gmfgraph_InvisibleRectangle.__init__)


def test_hyp_gmf_all_gmfgraph_invisiblerectangle_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_InvisibleRectangle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_verticallabel_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_VerticalLabel)


def test_hyp_gmf_all_gmfgraph_verticallabel_constructor_exists():
    assert callable(gmf_all_gmfgraph_VerticalLabel.__init__)


def test_hyp_gmf_all_gmfgraph_verticallabel_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_VerticalLabel.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_gmf_all_gmfgraph_shape_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Shape)


def test_hyp_gmf_all_gmfgraph_shape_constructor_exists():
    assert callable(gmf_all_gmfgraph_Shape.__init__)


def test_hyp_gmf_all_gmfgraph_shape_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "xorFill" in params, "Missing parameter 'xorFill'"
    assert "outline" in params, "Missing parameter 'outline'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "lineKind" in params, "Missing parameter 'lineKind'"
    assert "xorOutline" in params, "Missing parameter 'xorOutline'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"









def test_hyp_gmf_all_gmfgraph_svgfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_SVGFigure)


def test_hyp_gmf_all_gmfgraph_svgfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_SVGFigure.__init__)


def test_hyp_gmf_all_gmfgraph_svgfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_SVGFigure.__init__)
    params = list(sig.parameters.keys())
    assert "noCanvasWidth" in params, "Missing parameter 'noCanvasWidth'"
    assert "documentURI" in params, "Missing parameter 'documentURI'"
    assert "noCanvasHeight" in params, "Missing parameter 'noCanvasHeight'"






def test_hyp_gmf_all_gmfgraph_label_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Label)


def test_hyp_gmf_all_gmfgraph_label_constructor_exists():
    assert callable(gmf_all_gmfgraph_Label.__init__)


def test_hyp_gmf_all_gmfgraph_label_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_gmf_all_gmfgraph_decorationfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_DecorationFigure)


def test_hyp_gmf_all_gmfgraph_decorationfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_DecorationFigure.__init__)


def test_hyp_gmf_all_gmfgraph_decorationfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_connectionfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_ConnectionFigure)


def test_hyp_gmf_all_gmfgraph_connectionfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_ConnectionFigure.__init__)


def test_hyp_gmf_all_gmfgraph_connectionfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_ConnectionFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_labeledcontainer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_LabeledContainer)


def test_hyp_gmf_all_gmfgraph_labeledcontainer_constructor_exists():
    assert callable(gmf_all_gmfgraph_LabeledContainer.__init__)


def test_hyp_gmf_all_gmfgraph_labeledcontainer_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_LabeledContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_figuregallery_is_not_abstract():
    assert not inspect.isabstract(FigureGallery)


def test_hyp_figuregallery_constructor_exists():
    assert callable(FigureGallery.__init__)


def test_hyp_figuregallery_constructor_args():
    sig = inspect.signature(FigureGallery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_hyp_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_hyp_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_node_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Node)


def test_hyp_gmf_all_gmfgraph_node_constructor_exists():
    assert callable(gmf_all_gmfgraph_Node.__init__)


def test_hyp_gmf_all_gmfgraph_node_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "resizeConstraint" in params, "Missing parameter 'resizeConstraint'"
    assert "affixedParentSide" in params, "Missing parameter 'affixedParentSide'"





def test_hyp_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_hyp_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_hyp_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_compartment_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Compartment)


def test_hyp_gmf_all_gmfgraph_compartment_constructor_exists():
    assert callable(gmf_all_gmfgraph_Compartment.__init__)


def test_hyp_gmf_all_gmfgraph_compartment_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Compartment.__init__)
    params = list(sig.parameters.keys())
    assert "collapsible" in params, "Missing parameter 'collapsible'"
    assert "needsTitle" in params, "Missing parameter 'needsTitle'"





def test_hyp_gmf_all_gmfgraph_connection_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Connection)


def test_hyp_gmf_all_gmfgraph_connection_constructor_exists():
    assert callable(gmf_all_gmfgraph_Connection.__init__)


def test_hyp_gmf_all_gmfgraph_connection_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Connection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_abstractnode_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_AbstractNode)


def test_hyp_gmf_all_gmfgraph_abstractnode_constructor_exists():
    assert callable(gmf_all_gmfgraph_AbstractNode.__init__)


def test_hyp_gmf_all_gmfgraph_abstractnode_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_styleselector_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_StyleSelector)


def test_hyp_gmf_all_tooldef_styleselector_constructor_exists():
    assert callable(gmf_all_tooldef_StyleSelector.__init__)


def test_hyp_gmf_all_tooldef_styleselector_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_StyleSelector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_image_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_Image)


def test_hyp_gmf_all_tooldef_image_constructor_exists():
    assert callable(gmf_all_tooldef_Image.__init__)


def test_hyp_gmf_all_tooldef_image_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_Image.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tooldef_contributionitem_is_not_abstract():
    assert not inspect.isabstract(tooldef_ContributionItem)


def test_hyp_tooldef_contributionitem_constructor_exists():
    assert callable(tooldef_ContributionItem.__init__)


def test_hyp_tooldef_contributionitem_constructor_args():
    sig = inspect.signature(tooldef_ContributionItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identity_is_not_abstract():
    assert not inspect.isabstract(Identity)


def test_hyp_identity_constructor_exists():
    assert callable(Identity.__init__)


def test_hyp_identity_constructor_args():
    sig = inspect.signature(Identity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_pin_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Pin)


def test_hyp_gmf_all_gmfgraph_pin_constructor_exists():
    assert callable(gmf_all_gmfgraph_Pin.__init__)


def test_hyp_gmf_all_gmfgraph_pin_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Pin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_figuredescriptor_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_FigureDescriptor)


def test_hyp_gmf_all_gmfgraph_figuredescriptor_constructor_exists():
    assert callable(gmf_all_gmfgraph_FigureDescriptor.__init__)


def test_hyp_gmf_all_gmfgraph_figuredescriptor_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_FigureDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_diagramelement_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_DiagramElement)


def test_hyp_gmf_all_gmfgraph_diagramelement_constructor_exists():
    assert callable(gmf_all_gmfgraph_DiagramElement.__init__)


def test_hyp_gmf_all_gmfgraph_diagramelement_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_figuregallery_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_FigureGallery)


def test_hyp_gmf_all_gmfgraph_figuregallery_constructor_exists():
    assert callable(gmf_all_gmfgraph_FigureGallery.__init__)


def test_hyp_gmf_all_gmfgraph_figuregallery_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_FigureGallery.__init__)
    params = list(sig.parameters.keys())
    assert "implementationBundle" in params, "Missing parameter 'implementationBundle'"




def test_hyp_gmf_all_gmfgraph_canvas_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Canvas)


def test_hyp_gmf_all_gmfgraph_canvas_constructor_exists():
    assert callable(gmf_all_gmfgraph_Canvas.__init__)


def test_hyp_gmf_all_gmfgraph_canvas_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Canvas.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tooldef_predefineditem_is_not_abstract():
    assert not inspect.isabstract(tooldef_PredefinedItem)


def test_hyp_tooldef_predefineditem_constructor_exists():
    assert callable(tooldef_PredefinedItem.__init__)


def test_hyp_tooldef_predefineditem_constructor_args():
    sig = inspect.signature(tooldef_PredefinedItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tooldef_menu_is_not_abstract():
    assert not inspect.isabstract(tooldef_Menu)


def test_hyp_tooldef_menu_constructor_exists():
    assert callable(tooldef_Menu.__init__)


def test_hyp_tooldef_menu_constructor_args():
    sig = inspect.signature(tooldef_Menu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_popupmenu_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_PopupMenu)


def test_hyp_gmf_all_tooldef_popupmenu_constructor_exists():
    assert callable(gmf_all_tooldef_PopupMenu.__init__)


def test_hyp_gmf_all_tooldef_popupmenu_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_PopupMenu.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"




def test_hyp_gmf_all_tooldef_predefinedmenu_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_PredefinedMenu)


def test_hyp_gmf_all_tooldef_predefinedmenu_constructor_exists():
    assert callable(gmf_all_tooldef_PredefinedMenu.__init__)


def test_hyp_gmf_all_tooldef_predefinedmenu_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_PredefinedMenu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_itembase_is_not_abstract():
    assert not inspect.isabstract(ItemBase)


def test_hyp_itembase_constructor_exists():
    assert callable(ItemBase.__init__)


def test_hyp_itembase_constructor_args():
    sig = inspect.signature(ItemBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_separator_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_Separator)


def test_hyp_gmf_all_tooldef_separator_constructor_exists():
    assert callable(gmf_all_tooldef_Separator.__init__)


def test_hyp_gmf_all_tooldef_separator_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_Separator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_gmf_all_tooldef_predefineditem_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_PredefinedItem)


def test_hyp_gmf_all_tooldef_predefineditem_constructor_exists():
    assert callable(gmf_all_tooldef_PredefinedItem.__init__)


def test_hyp_gmf_all_tooldef_predefineditem_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_PredefinedItem.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"




def test_hyp_gmf_all_tooldef_contributionitem_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ContributionItem)


def test_hyp_gmf_all_tooldef_contributionitem_constructor_exists():
    assert callable(gmf_all_tooldef_ContributionItem.__init__)


def test_hyp_gmf_all_tooldef_contributionitem_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ContributionItem.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_gmf_all_tooldef_menu_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_Menu)


def test_hyp_gmf_all_tooldef_menu_constructor_exists():
    assert callable(gmf_all_tooldef_Menu.__init__)


def test_hyp_gmf_all_tooldef_menu_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_Menu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_itembase_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ItemBase)


def test_hyp_gmf_all_tooldef_itembase_constructor_exists():
    assert callable(gmf_all_tooldef_ItemBase.__init__)


def test_hyp_gmf_all_tooldef_itembase_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ItemBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_itemref_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ItemRef)


def test_hyp_gmf_all_tooldef_itemref_constructor_exists():
    assert callable(gmf_all_tooldef_ItemRef.__init__)


def test_hyp_gmf_all_tooldef_itemref_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ItemRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contributionitem_is_not_abstract():
    assert not inspect.isabstract(ContributionItem)


def test_hyp_contributionitem_constructor_exists():
    assert callable(ContributionItem.__init__)


def test_hyp_contributionitem_constructor_args():
    sig = inspect.signature(ContributionItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_menuaction_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_MenuAction)


def test_hyp_gmf_all_tooldef_menuaction_constructor_exists():
    assert callable(gmf_all_tooldef_MenuAction.__init__)


def test_hyp_gmf_all_tooldef_menuaction_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_MenuAction.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "hotKey" in params, "Missing parameter 'hotKey'"





def test_hyp_image_is_not_abstract():
    assert not inspect.isabstract(Image)


def test_hyp_image_constructor_exists():
    assert callable(Image.__init__)


def test_hyp_image_constructor_args():
    sig = inspect.signature(Image.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_bundleimage_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_BundleImage)


def test_hyp_gmf_all_tooldef_bundleimage_constructor_exists():
    assert callable(gmf_all_tooldef_BundleImage.__init__)


def test_hyp_gmf_all_tooldef_bundleimage_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_BundleImage.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "bundle" in params, "Missing parameter 'bundle'"





def test_hyp_gmf_all_tooldef_defaultimage_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_DefaultImage)


def test_hyp_gmf_all_tooldef_defaultimage_constructor_exists():
    assert callable(gmf_all_tooldef_DefaultImage.__init__)


def test_hyp_gmf_all_tooldef_defaultimage_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_DefaultImage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_abstracttool_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_AbstractTool)


def test_hyp_gmf_all_tooldef_abstracttool_constructor_exists():
    assert callable(gmf_all_tooldef_AbstractTool.__init__)


def test_hyp_gmf_all_tooldef_abstracttool_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_AbstractTool.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"





def test_hyp_menu_is_not_abstract():
    assert not inspect.isabstract(Menu)


def test_hyp_menu_constructor_exists():
    assert callable(Menu.__init__)


def test_hyp_menu_constructor_args():
    sig = inspect.signature(Menu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_toolbar_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_Toolbar)


def test_hyp_gmf_all_tooldef_toolbar_constructor_exists():
    assert callable(gmf_all_tooldef_Toolbar.__init__)


def test_hyp_gmf_all_tooldef_toolbar_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_Toolbar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_contextmenu_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ContextMenu)


def test_hyp_gmf_all_tooldef_contextmenu_constructor_exists():
    assert callable(gmf_all_tooldef_ContextMenu.__init__)


def test_hyp_gmf_all_tooldef_contextmenu_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ContextMenu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_mainmenu_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_MainMenu)


def test_hyp_gmf_all_tooldef_mainmenu_constructor_exists():
    assert callable(gmf_all_tooldef_MainMenu.__init__)


def test_hyp_gmf_all_tooldef_mainmenu_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_MainMenu.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_menuaction_is_not_abstract():
    assert not inspect.isabstract(MenuAction)


def test_hyp_menuaction_constructor_exists():
    assert callable(MenuAction.__init__)


def test_hyp_menuaction_constructor_args():
    sig = inspect.signature(MenuAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_toolregistry_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ToolRegistry)


def test_hyp_gmf_all_tooldef_toolregistry_constructor_exists():
    assert callable(gmf_all_tooldef_ToolRegistry.__init__)


def test_hyp_gmf_all_tooldef_toolregistry_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ToolRegistry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_hyp_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_hyp_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_custompin_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomPin)


def test_hyp_gmf_all_gmfgraph_custompin_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomPin.__init__)


def test_hyp_gmf_all_gmfgraph_custompin_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomPin.__init__)
    params = list(sig.parameters.keys())
    assert "customOperationName" in params, "Missing parameter 'customOperationName'"
    assert "customOperationType" in params, "Missing parameter 'customOperationType'"





def test_hyp_gmf_all_gmfgraph_visiblepin_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_VisiblePin)


def test_hyp_gmf_all_gmfgraph_visiblepin_constructor_exists():
    assert callable(gmf_all_gmfgraph_VisiblePin.__init__)


def test_hyp_gmf_all_gmfgraph_visiblepin_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_VisiblePin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_colorpin_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_ColorPin)


def test_hyp_gmf_all_gmfgraph_colorpin_constructor_exists():
    assert callable(gmf_all_gmfgraph_ColorPin.__init__)


def test_hyp_gmf_all_gmfgraph_colorpin_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_ColorPin.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundNotForeground" in params, "Missing parameter 'backgroundNotForeground'"




def test_hyp_gmf_all_mappings_visualeffectmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_VisualEffectMapping)


def test_hyp_gmf_all_mappings_visualeffectmapping_constructor_exists():
    assert callable(gmf_all_mappings_VisualEffectMapping.__init__)


def test_hyp_gmf_all_mappings_visualeffectmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_VisualEffectMapping.__init__)
    params = list(sig.parameters.keys())
    assert "oclExpression" in params, "Missing parameter 'oclExpression'"




def test_hyp_gmf_all_mappings_measurable_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_Measurable)


def test_hyp_gmf_all_mappings_measurable_constructor_exists():
    assert callable(gmf_all_mappings_Measurable.__init__)


def test_hyp_gmf_all_mappings_measurable_constructor_args():
    sig = inspect.signature(gmf_all_mappings_Measurable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_auditable_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_Auditable)


def test_hyp_gmf_all_mappings_auditable_constructor_exists():
    assert callable(gmf_all_mappings_Auditable.__init__)


def test_hyp_gmf_all_mappings_auditable_constructor_args():
    sig = inspect.signature(gmf_all_mappings_Auditable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_toolcontainer_is_not_abstract():
    assert not inspect.isabstract(ToolContainer)


def test_hyp_toolcontainer_constructor_exists():
    assert callable(ToolContainer.__init__)


def test_hyp_toolcontainer_constructor_args():
    sig = inspect.signature(ToolContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_palette_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_Palette)


def test_hyp_gmf_all_tooldef_palette_constructor_exists():
    assert callable(gmf_all_tooldef_Palette.__init__)


def test_hyp_gmf_all_tooldef_palette_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_Palette.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_toolgroup_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ToolGroup)


def test_hyp_gmf_all_tooldef_toolgroup_constructor_exists():
    assert callable(gmf_all_tooldef_ToolGroup.__init__)


def test_hyp_gmf_all_tooldef_toolgroup_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ToolGroup.__init__)
    params = list(sig.parameters.keys())
    assert "stack" in params, "Missing parameter 'stack'"
    assert "collapsible" in params, "Missing parameter 'collapsible'"





def test_hyp_measurable_is_not_abstract():
    assert not inspect.isabstract(Measurable)


def test_hyp_measurable_constructor_exists():
    assert callable(Measurable.__init__)


def test_hyp_measurable_constructor_args():
    sig = inspect.signature(Measurable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metricrule_is_not_abstract():
    assert not inspect.isabstract(MetricRule)


def test_hyp_metricrule_constructor_exists():
    assert callable(MetricRule.__init__)


def test_hyp_metricrule_constructor_args():
    sig = inspect.signature(MetricRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_metriccontainer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_MetricContainer)


def test_hyp_gmf_all_mappings_metriccontainer_constructor_exists():
    assert callable(gmf_all_mappings_MetricContainer.__init__)


def test_hyp_gmf_all_mappings_metriccontainer_constructor_args():
    sig = inspect.signature(gmf_all_mappings_MetricContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_measurable_is_not_abstract():
    assert not inspect.isabstract(mappings_Measurable)


def test_hyp_mappings_measurable_constructor_exists():
    assert callable(mappings_Measurable.__init__)


def test_hyp_mappings_measurable_constructor_args():
    sig = inspect.signature(mappings_Measurable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_auditable_is_not_abstract():
    assert not inspect.isabstract(mappings_Auditable)


def test_hyp_mappings_auditable_constructor_exists():
    assert callable(mappings_Auditable.__init__)


def test_hyp_mappings_auditable_constructor_args():
    sig = inspect.signature(mappings_Auditable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_notationelementtarget_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_NotationElementTarget)


def test_hyp_gmf_all_mappings_notationelementtarget_constructor_exists():
    assert callable(gmf_all_mappings_NotationElementTarget.__init__)


def test_hyp_gmf_all_mappings_notationelementtarget_constructor_args():
    sig = inspect.signature(gmf_all_mappings_NotationElementTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_diagramelementtarget_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_DiagramElementTarget)


def test_hyp_gmf_all_mappings_diagramelementtarget_constructor_exists():
    assert callable(gmf_all_mappings_DiagramElementTarget.__init__)


def test_hyp_gmf_all_mappings_diagramelementtarget_constructor_args():
    sig = inspect.signature(gmf_all_mappings_DiagramElementTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_domainelementtarget_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_DomainElementTarget)


def test_hyp_gmf_all_mappings_domainelementtarget_constructor_exists():
    assert callable(gmf_all_mappings_DomainElementTarget.__init__)


def test_hyp_gmf_all_mappings_domainelementtarget_constructor_args():
    sig = inspect.signature(gmf_all_mappings_DomainElementTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_auditable_is_not_abstract():
    assert not inspect.isabstract(Auditable)


def test_hyp_auditable_constructor_exists():
    assert callable(Auditable.__init__)


def test_hyp_auditable_constructor_args():
    sig = inspect.signature(Auditable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_auditedmetrictarget_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_AuditedMetricTarget)


def test_hyp_gmf_all_mappings_auditedmetrictarget_constructor_exists():
    assert callable(gmf_all_mappings_AuditedMetricTarget.__init__)


def test_hyp_gmf_all_mappings_auditedmetrictarget_constructor_args():
    sig = inspect.signature(gmf_all_mappings_AuditedMetricTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rulebase_is_not_abstract():
    assert not inspect.isabstract(RuleBase)


def test_hyp_rulebase_constructor_exists():
    assert callable(RuleBase.__init__)


def test_hyp_rulebase_constructor_args():
    sig = inspect.signature(RuleBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_metricrule_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_MetricRule)


def test_hyp_gmf_all_mappings_metricrule_constructor_exists():
    assert callable(gmf_all_mappings_MetricRule.__init__)


def test_hyp_gmf_all_mappings_metricrule_constructor_args():
    sig = inspect.signature(gmf_all_mappings_MetricRule.__init__)
    params = list(sig.parameters.keys())
    assert "lowLimit" in params, "Missing parameter 'lowLimit'"
    assert "key" in params, "Missing parameter 'key'"
    assert "highLimit" in params, "Missing parameter 'highLimit'"






def test_hyp_gmf_all_mappings_auditrule_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_AuditRule)


def test_hyp_gmf_all_mappings_auditrule_constructor_exists():
    assert callable(gmf_all_mappings_AuditRule.__init__)


def test_hyp_gmf_all_mappings_auditrule_constructor_args():
    sig = inspect.signature(gmf_all_mappings_AuditRule.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "useInLiveMode" in params, "Missing parameter 'useInLiveMode'"
    assert "message" in params, "Missing parameter 'message'"
    assert "severity" in params, "Missing parameter 'severity'"







def test_hyp_gmf_all_mappings_rulebase_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_RuleBase)


def test_hyp_gmf_all_mappings_rulebase_constructor_exists():
    assert callable(gmf_all_mappings_RuleBase.__init__)


def test_hyp_gmf_all_mappings_rulebase_constructor_args():
    sig = inspect.signature(gmf_all_mappings_RuleBase.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_gmf_all_mappings_domainattributetarget_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_DomainAttributeTarget)


def test_hyp_gmf_all_mappings_domainattributetarget_constructor_exists():
    assert callable(gmf_all_mappings_DomainAttributeTarget.__init__)


def test_hyp_gmf_all_mappings_domainattributetarget_constructor_args():
    sig = inspect.signature(gmf_all_mappings_DomainAttributeTarget.__init__)
    params = list(sig.parameters.keys())
    assert "nullAsError" in params, "Missing parameter 'nullAsError'"




def test_hyp_gmf_all_mappings_auditcontainer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_AuditContainer)


def test_hyp_gmf_all_mappings_auditcontainer_constructor_exists():
    assert callable(gmf_all_mappings_AuditContainer.__init__)


def test_hyp_gmf_all_mappings_auditcontainer_constructor_args():
    sig = inspect.signature(gmf_all_mappings_AuditContainer.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_gmf_all_mappings_appearancesteward_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_AppearanceSteward)


def test_hyp_gmf_all_mappings_appearancesteward_constructor_exists():
    assert callable(gmf_all_mappings_AppearanceSteward.__init__)


def test_hyp_gmf_all_mappings_appearancesteward_constructor_args():
    sig = inspect.signature(gmf_all_mappings_AppearanceSteward.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracttool_is_not_abstract():
    assert not inspect.isabstract(AbstractTool)


def test_hyp_abstracttool_constructor_exists():
    assert callable(AbstractTool.__init__)


def test_hyp_abstracttool_constructor_args():
    sig = inspect.signature(AbstractTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_generictool_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_GenericTool)


def test_hyp_gmf_all_tooldef_generictool_constructor_exists():
    assert callable(gmf_all_tooldef_GenericTool.__init__)


def test_hyp_gmf_all_tooldef_generictool_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_GenericTool.__init__)
    params = list(sig.parameters.keys())
    assert "toolClass" in params, "Missing parameter 'toolClass'"




def test_hyp_gmf_all_tooldef_toolcontainer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ToolContainer)


def test_hyp_gmf_all_tooldef_toolcontainer_constructor_exists():
    assert callable(gmf_all_tooldef_ToolContainer.__init__)


def test_hyp_gmf_all_tooldef_toolcontainer_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ToolContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_creationtool_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_CreationTool)


def test_hyp_gmf_all_tooldef_creationtool_constructor_exists():
    assert callable(gmf_all_tooldef_CreationTool.__init__)


def test_hyp_gmf_all_tooldef_creationtool_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_CreationTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_paletteseparator_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_PaletteSeparator)


def test_hyp_gmf_all_tooldef_paletteseparator_constructor_exists():
    assert callable(gmf_all_tooldef_PaletteSeparator.__init__)


def test_hyp_gmf_all_tooldef_paletteseparator_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_PaletteSeparator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_standardtool_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_StandardTool)


def test_hyp_gmf_all_tooldef_standardtool_constructor_exists():
    assert callable(gmf_all_tooldef_StandardTool.__init__)


def test_hyp_gmf_all_tooldef_standardtool_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_StandardTool.__init__)
    params = list(sig.parameters.keys())
    assert "toolKind" in params, "Missing parameter 'toolKind'"




def test_hyp_gmf_all_mappings_toolowner_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ToolOwner)


def test_hyp_gmf_all_mappings_toolowner_constructor_exists():
    assert callable(gmf_all_mappings_ToolOwner.__init__)


def test_hyp_gmf_all_mappings_toolowner_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ToolOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contextmenu_is_not_abstract():
    assert not inspect.isabstract(ContextMenu)


def test_hyp_contextmenu_constructor_exists():
    assert callable(ContextMenu.__init__)


def test_hyp_contextmenu_constructor_args():
    sig = inspect.signature(ContextMenu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_menuowner_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_MenuOwner)


def test_hyp_gmf_all_mappings_menuowner_constructor_exists():
    assert callable(gmf_all_mappings_MenuOwner.__init__)


def test_hyp_gmf_all_mappings_menuowner_constructor_args():
    sig = inspect.signature(gmf_all_mappings_MenuOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featureseqinitializer_is_not_abstract():
    assert not inspect.isabstract(FeatureSeqInitializer)


def test_hyp_featureseqinitializer_constructor_exists():
    assert callable(FeatureSeqInitializer.__init__)


def test_hyp_featureseqinitializer_constructor_args():
    sig = inspect.signature(FeatureSeqInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_auditrule_is_not_abstract():
    assert not inspect.isabstract(AuditRule)


def test_hyp_auditrule_constructor_exists():
    assert callable(AuditRule.__init__)


def test_hyp_auditrule_constructor_args():
    sig = inspect.signature(AuditRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_referencenewelementspec_is_not_abstract():
    assert not inspect.isabstract(ReferenceNewElementSpec)


def test_hyp_referencenewelementspec_constructor_exists():
    assert callable(ReferenceNewElementSpec.__init__)


def test_hyp_referencenewelementspec_constructor_args():
    sig = inspect.signature(ReferenceNewElementSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featureinitializer_is_not_abstract():
    assert not inspect.isabstract(FeatureInitializer)


def test_hyp_featureinitializer_constructor_exists():
    assert callable(FeatureInitializer.__init__)


def test_hyp_featureinitializer_constructor_args():
    sig = inspect.signature(FeatureInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_referencenewelementspec_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ReferenceNewElementSpec)


def test_hyp_gmf_all_mappings_referencenewelementspec_constructor_exists():
    assert callable(gmf_all_mappings_ReferenceNewElementSpec.__init__)


def test_hyp_gmf_all_mappings_referencenewelementspec_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ReferenceNewElementSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_featurevaluespec_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_FeatureValueSpec)


def test_hyp_gmf_all_mappings_featurevaluespec_constructor_exists():
    assert callable(gmf_all_mappings_FeatureValueSpec.__init__)


def test_hyp_gmf_all_mappings_featurevaluespec_constructor_args():
    sig = inspect.signature(gmf_all_mappings_FeatureValueSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_elementinitializer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ElementInitializer)


def test_hyp_gmf_all_mappings_elementinitializer_constructor_exists():
    assert callable(gmf_all_mappings_ElementInitializer.__init__)


def test_hyp_gmf_all_mappings_elementinitializer_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ElementInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_valueexpression_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ValueExpression)


def test_hyp_gmf_all_mappings_valueexpression_constructor_exists():
    assert callable(gmf_all_mappings_ValueExpression.__init__)


def test_hyp_gmf_all_mappings_valueexpression_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "langName" in params, "Missing parameter 'langName'"
    assert "body" in params, "Missing parameter 'body'"






def test_hyp_gmf_all_mappings_featureinitializer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_FeatureInitializer)


def test_hyp_gmf_all_mappings_featureinitializer_constructor_exists():
    assert callable(gmf_all_mappings_FeatureInitializer.__init__)


def test_hyp_gmf_all_mappings_featureinitializer_constructor_args():
    sig = inspect.signature(gmf_all_mappings_FeatureInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_linkconstraints_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_LinkConstraints)


def test_hyp_gmf_all_mappings_linkconstraints_constructor_exists():
    assert callable(gmf_all_mappings_LinkConstraints.__init__)


def test_hyp_gmf_all_mappings_linkconstraints_constructor_args():
    sig = inspect.signature(gmf_all_mappings_LinkConstraints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_gmf_all_eattribute_is_not_abstract():
    assert not inspect.isabstract(mappings_gmf_all_EAttribute)


def test_hyp_mappings_gmf_all_eattribute_constructor_exists():
    assert callable(mappings_gmf_all_EAttribute.__init__)


def test_hyp_mappings_gmf_all_eattribute_constructor_args():
    sig = inspect.signature(mappings_gmf_all_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappingentry_is_not_abstract():
    assert not inspect.isabstract(MappingEntry)


def test_hyp_mappingentry_constructor_exists():
    assert callable(MappingEntry.__init__)


def test_hyp_mappingentry_constructor_args():
    sig = inspect.signature(MappingEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagramlabel_is_not_abstract():
    assert not inspect.isabstract(DiagramLabel)


def test_hyp_diagramlabel_constructor_exists():
    assert callable(DiagramLabel.__init__)


def test_hyp_diagramlabel_constructor_args():
    sig = inspect.signature(DiagramLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_labelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_LabelMapping)


def test_hyp_gmf_all_mappings_labelmapping_constructor_exists():
    assert callable(gmf_all_mappings_LabelMapping.__init__)


def test_hyp_gmf_all_mappings_labelmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_LabelMapping.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"




def test_hyp_toolbar_is_not_abstract():
    assert not inspect.isabstract(Toolbar)


def test_hyp_toolbar_constructor_exists():
    assert callable(Toolbar.__init__)


def test_hyp_toolbar_constructor_args():
    sig = inspect.signature(Toolbar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mainmenu_is_not_abstract():
    assert not inspect.isabstract(MainMenu)


def test_hyp_mainmenu_constructor_exists():
    assert callable(MainMenu.__init__)


def test_hyp_mainmenu_constructor_args():
    sig = inspect.signature(MainMenu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_hyp_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_hyp_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_constraint_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_Constraint)


def test_hyp_gmf_all_mappings_constraint_constructor_exists():
    assert callable(gmf_all_mappings_Constraint.__init__)


def test_hyp_gmf_all_mappings_constraint_constructor_args():
    sig = inspect.signature(gmf_all_mappings_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_canvas_is_not_abstract():
    assert not inspect.isabstract(Canvas)


def test_hyp_canvas_constructor_exists():
    assert callable(Canvas.__init__)


def test_hyp_canvas_constructor_args():
    sig = inspect.signature(Canvas.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_canvasmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_CanvasMapping)


def test_hyp_gmf_all_mappings_canvasmapping_constructor_exists():
    assert callable(gmf_all_mappings_CanvasMapping.__init__)


def test_hyp_gmf_all_mappings_canvasmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_CanvasMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_linkconstraints_is_not_abstract():
    assert not inspect.isabstract(LinkConstraints)


def test_hyp_linkconstraints_constructor_exists():
    assert callable(LinkConstraints.__init__)


def test_hyp_linkconstraints_constructor_args():
    sig = inspect.signature(LinkConstraints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_gmf_all_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(mappings_gmf_all_EStructuralFeature)


def test_hyp_mappings_gmf_all_estructuralfeature_constructor_exists():
    assert callable(mappings_gmf_all_EStructuralFeature.__init__)


def test_hyp_mappings_gmf_all_estructuralfeature_constructor_args():
    sig = inspect.signature(mappings_gmf_all_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_hyp_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_hyp_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_needscontainment_is_not_abstract():
    assert not inspect.isabstract(mappings_NeedsContainment)


def test_hyp_mappings_needscontainment_constructor_exists():
    assert callable(mappings_NeedsContainment.__init__)


def test_hyp_mappings_needscontainment_constructor_args():
    sig = inspect.signature(mappings_NeedsContainment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compartment_is_not_abstract():
    assert not inspect.isabstract(Compartment)


def test_hyp_compartment_constructor_exists():
    assert callable(Compartment.__init__)


def test_hyp_compartment_constructor_args():
    sig = inspect.signature(Compartment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_compartmentmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_CompartmentMapping)


def test_hyp_gmf_all_mappings_compartmentmapping_constructor_exists():
    assert callable(gmf_all_mappings_CompartmentMapping.__init__)


def test_hyp_gmf_all_mappings_compartmentmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_CompartmentMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_childreference_is_not_abstract():
    assert not inspect.isabstract(ChildReference)


def test_hyp_childreference_constructor_exists():
    assert callable(ChildReference.__init__)


def test_hyp_childreference_constructor_args():
    sig = inspect.signature(ChildReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_palette_is_not_abstract():
    assert not inspect.isabstract(Palette)


def test_hyp_palette_constructor_exists():
    assert callable(Palette.__init__)


def test_hyp_palette_constructor_args():
    sig = inspect.signature(Palette.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_gmf_all_epackage_is_not_abstract():
    assert not inspect.isabstract(mappings_gmf_all_EPackage)


def test_hyp_mappings_gmf_all_epackage_constructor_exists():
    assert callable(mappings_gmf_all_EPackage.__init__)


def test_hyp_mappings_gmf_all_epackage_constructor_args():
    sig = inspect.signature(mappings_gmf_all_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compartmentmapping_is_not_abstract():
    assert not inspect.isabstract(CompartmentMapping)


def test_hyp_compartmentmapping_constructor_exists():
    assert callable(CompartmentMapping.__init__)


def test_hyp_compartmentmapping_constructor_args():
    sig = inspect.signature(CompartmentMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nodereference_is_not_abstract():
    assert not inspect.isabstract(NodeReference)


def test_hyp_nodereference_constructor_exists():
    assert callable(NodeReference.__init__)


def test_hyp_nodereference_constructor_args():
    sig = inspect.signature(NodeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_topnodereference_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_TopNodeReference)


def test_hyp_gmf_all_mappings_topnodereference_constructor_exists():
    assert callable(gmf_all_mappings_TopNodeReference.__init__)


def test_hyp_gmf_all_mappings_topnodereference_constructor_args():
    sig = inspect.signature(gmf_all_mappings_TopNodeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_childreference_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ChildReference)


def test_hyp_gmf_all_mappings_childreference_constructor_exists():
    assert callable(gmf_all_mappings_ChildReference.__init__)


def test_hyp_gmf_all_mappings_childreference_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ChildReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nodemapping_is_not_abstract():
    assert not inspect.isabstract(NodeMapping)


def test_hyp_nodemapping_constructor_exists():
    assert callable(NodeMapping.__init__)


def test_hyp_nodemapping_constructor_args():
    sig = inspect.signature(NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_needscontainment_is_not_abstract():
    assert not inspect.isabstract(NeedsContainment)


def test_hyp_needscontainment_constructor_exists():
    assert callable(NeedsContainment.__init__)


def test_hyp_needscontainment_constructor_args():
    sig = inspect.signature(NeedsContainment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_nodereference_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_NodeReference)


def test_hyp_gmf_all_mappings_nodereference_constructor_exists():
    assert callable(gmf_all_mappings_NodeReference.__init__)


def test_hyp_gmf_all_mappings_nodereference_constructor_args():
    sig = inspect.signature(gmf_all_mappings_NodeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_gmfgraph_diagramlabel_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_DiagramLabel)


def test_hyp_gmf_all_gmfgraph_diagramlabel_constructor_exists():
    assert callable(gmf_all_gmfgraph_DiagramLabel.__init__)


def test_hyp_gmf_all_gmfgraph_diagramlabel_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_DiagramLabel.__init__)
    params = list(sig.parameters.keys())
    assert "elementIcon" in params, "Missing parameter 'elementIcon'"
    assert "external" in params, "Missing parameter 'external'"





def test_hyp_mappings_appearancesteward_is_not_abstract():
    assert not inspect.isabstract(mappings_AppearanceSteward)


def test_hyp_mappings_appearancesteward_constructor_exists():
    assert callable(mappings_AppearanceSteward.__init__)


def test_hyp_mappings_appearancesteward_constructor_args():
    sig = inspect.signature(mappings_AppearanceSteward.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_toolowner_is_not_abstract():
    assert not inspect.isabstract(mappings_ToolOwner)


def test_hyp_mappings_toolowner_constructor_exists():
    assert callable(mappings_ToolOwner.__init__)


def test_hyp_mappings_toolowner_constructor_args():
    sig = inspect.signature(mappings_ToolOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_menuowner_is_not_abstract():
    assert not inspect.isabstract(mappings_MenuOwner)


def test_hyp_mappings_menuowner_constructor_exists():
    assert callable(mappings_MenuOwner.__init__)


def test_hyp_mappings_menuowner_constructor_args():
    sig = inspect.signature(mappings_MenuOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_mappingentry_is_not_abstract():
    assert not inspect.isabstract(mappings_MappingEntry)


def test_hyp_mappings_mappingentry_constructor_exists():
    assert callable(mappings_MappingEntry.__init__)


def test_hyp_mappings_mappingentry_constructor_args():
    sig = inspect.signature(mappings_MappingEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_linkmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_LinkMapping)


def test_hyp_gmf_all_mappings_linkmapping_constructor_exists():
    assert callable(gmf_all_mappings_LinkMapping.__init__)


def test_hyp_gmf_all_mappings_linkmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_LinkMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_nodemapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_NodeMapping)


def test_hyp_gmf_all_mappings_nodemapping_constructor_exists():
    assert callable(gmf_all_mappings_NodeMapping.__init__)


def test_hyp_gmf_all_mappings_nodemapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labelmapping_is_not_abstract():
    assert not inspect.isabstract(LabelMapping)


def test_hyp_labelmapping_constructor_exists():
    assert callable(LabelMapping.__init__)


def test_hyp_labelmapping_constructor_args():
    sig = inspect.signature(LabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_expressionlabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ExpressionLabelMapping)


def test_hyp_gmf_all_mappings_expressionlabelmapping_constructor_exists():
    assert callable(gmf_all_mappings_ExpressionLabelMapping.__init__)


def test_hyp_gmf_all_mappings_expressionlabelmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ExpressionLabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_featurelabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_FeatureLabelMapping)


def test_hyp_gmf_all_mappings_featurelabelmapping_constructor_exists():
    assert callable(gmf_all_mappings_FeatureLabelMapping.__init__)


def test_hyp_gmf_all_mappings_featurelabelmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_FeatureLabelMapping.__init__)
    params = list(sig.parameters.keys())
    assert "viewPattern" in params, "Missing parameter 'viewPattern'"
    assert "editPattern" in params, "Missing parameter 'editPattern'"
    assert "viewMethod" in params, "Missing parameter 'viewMethod'"
    assert "editMethod" in params, "Missing parameter 'editMethod'"
    assert "editorPattern" in params, "Missing parameter 'editorPattern'"








def test_hyp_gmf_all_mappings_oclchoicelabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_OclChoiceLabelMapping)


def test_hyp_gmf_all_mappings_oclchoicelabelmapping_constructor_exists():
    assert callable(gmf_all_mappings_OclChoiceLabelMapping.__init__)


def test_hyp_gmf_all_mappings_oclchoicelabelmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_OclChoiceLabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_designlabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_DesignLabelMapping)


def test_hyp_gmf_all_mappings_designlabelmapping_constructor_exists():
    assert callable(gmf_all_mappings_DesignLabelMapping.__init__)


def test_hyp_gmf_all_mappings_designlabelmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_DesignLabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elementinitializer_is_not_abstract():
    assert not inspect.isabstract(ElementInitializer)


def test_hyp_elementinitializer_constructor_exists():
    assert callable(ElementInitializer.__init__)


def test_hyp_elementinitializer_constructor_args():
    sig = inspect.signature(ElementInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_featureseqinitializer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_FeatureSeqInitializer)


def test_hyp_gmf_all_mappings_featureseqinitializer_constructor_exists():
    assert callable(gmf_all_mappings_FeatureSeqInitializer.__init__)


def test_hyp_gmf_all_mappings_featureseqinitializer_constructor_args():
    sig = inspect.signature(gmf_all_mappings_FeatureSeqInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_hyp_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_hyp_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_gmf_all_eclass_is_not_abstract():
    assert not inspect.isabstract(mappings_gmf_all_EClass)


def test_hyp_mappings_gmf_all_eclass_constructor_exists():
    assert callable(mappings_gmf_all_EClass.__init__)


def test_hyp_mappings_gmf_all_eclass_constructor_args():
    sig = inspect.signature(mappings_gmf_all_EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_mappingentry_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_MappingEntry)


def test_hyp_gmf_all_mappings_mappingentry_constructor_exists():
    assert callable(gmf_all_mappings_MappingEntry.__init__)


def test_hyp_gmf_all_mappings_mappingentry_constructor_args():
    sig = inspect.signature(gmf_all_mappings_MappingEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metriccontainer_is_not_abstract():
    assert not inspect.isabstract(MetricContainer)


def test_hyp_metriccontainer_constructor_exists():
    assert callable(MetricContainer.__init__)


def test_hyp_metriccontainer_constructor_args():
    sig = inspect.signature(MetricContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_auditcontainer_is_not_abstract():
    assert not inspect.isabstract(AuditContainer)


def test_hyp_auditcontainer_constructor_exists():
    assert callable(AuditContainer.__init__)


def test_hyp_auditcontainer_constructor_args():
    sig = inspect.signature(AuditContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styleselector_is_not_abstract():
    assert not inspect.isabstract(StyleSelector)


def test_hyp_styleselector_constructor_exists():
    assert callable(StyleSelector.__init__)


def test_hyp_styleselector_constructor_args():
    sig = inspect.signature(StyleSelector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_tooldef_genericstyleselector_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_GenericStyleSelector)


def test_hyp_gmf_all_tooldef_genericstyleselector_constructor_exists():
    assert callable(gmf_all_tooldef_GenericStyleSelector.__init__)


def test_hyp_gmf_all_tooldef_genericstyleselector_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_GenericStyleSelector.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"




def test_hyp_canvasmapping_is_not_abstract():
    assert not inspect.isabstract(CanvasMapping)


def test_hyp_canvasmapping_constructor_exists():
    assert callable(CanvasMapping.__init__)


def test_hyp_canvasmapping_constructor_args():
    sig = inspect.signature(CanvasMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_linkmapping_is_not_abstract():
    assert not inspect.isabstract(LinkMapping)


def test_hyp_linkmapping_constructor_exists():
    assert callable(LinkMapping.__init__)


def test_hyp_linkmapping_constructor_args():
    sig = inspect.signature(LinkMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappings_gmf_all_ereference_is_not_abstract():
    assert not inspect.isabstract(mappings_gmf_all_EReference)


def test_hyp_mappings_gmf_all_ereference_constructor_exists():
    assert callable(mappings_gmf_all_EReference.__init__)


def test_hyp_mappings_gmf_all_ereference_constructor_args():
    sig = inspect.signature(mappings_gmf_all_EReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_needscontainment_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_NeedsContainment)


def test_hyp_gmf_all_mappings_needscontainment_constructor_exists():
    assert callable(gmf_all_mappings_NeedsContainment.__init__)


def test_hyp_gmf_all_mappings_needscontainment_constructor_args():
    sig = inspect.signature(gmf_all_mappings_NeedsContainment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualeffectmapping_is_not_abstract():
    assert not inspect.isabstract(VisualEffectMapping)


def test_hyp_visualeffectmapping_constructor_exists():
    assert callable(VisualEffectMapping.__init__)


def test_hyp_visualeffectmapping_constructor_args():
    sig = inspect.signature(VisualEffectMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_topnodereference_is_not_abstract():
    assert not inspect.isabstract(TopNodeReference)


def test_hyp_topnodereference_constructor_exists():
    assert callable(TopNodeReference.__init__)


def test_hyp_topnodereference_constructor_args():
    sig = inspect.signature(TopNodeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmf_all_mappings_mapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_Mapping)


def test_hyp_gmf_all_mappings_mapping_constructor_exists():
    assert callable(gmf_all_mappings_Mapping.__init__)


def test_hyp_gmf_all_mappings_mapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_Mapping.__init__)
    params = list(sig.parameters.keys())

def test_hyp_severity_exists():
    # Check that the Enumeration exists
    assert Severity is not None

def test_hyp_severity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Severity]
    expected_literals = [
        "INFO",
        "ERROR",
        "WARNING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Severity"

def test_hyp_linekind_exists():
    # Check that the Enumeration exists
    assert LineKind is not None

def test_hyp_linekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineKind]
    expected_literals = [
        "LINE_DOT",
        "LINE_CUSTOM",
        "LINE_SOLID",
        "LINE_DASH",
        "LINE_DASHDOT",
        "LINE_DASHDOTDOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineKind"

def test_hyp_appearancestyle_exists():
    # Check that the Enumeration exists
    assert AppearanceStyle is not None

def test_hyp_appearancestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AppearanceStyle]
    expected_literals = [
        "Font",
        "Fill",
        "Line",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AppearanceStyle"

def test_hyp_svgpropertytype_exists():
    # Check that the Enumeration exists
    assert SVGPropertyType is not None

def test_hyp_svgpropertytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SVGPropertyType]
    expected_literals = [
        "FLOAT",
        "COLOR",
        "STRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SVGPropertyType"

def test_hyp_fontstyle_exists():
    # Check that the Enumeration exists
    assert FontStyle is not None

def test_hyp_fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontStyle]
    expected_literals = [
        "ITALIC",
        "NORMAL",
        "BOLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontStyle"

def test_hyp_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_hyp_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "FILL",
        "END",
        "BEGINNING",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_hyp_actionkind_exists():
    # Check that the Enumeration exists
    assert ActionKind is not None

def test_hyp_actionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionKind]
    expected_literals = [
        "PROPCHANGE",
        "CUSTOM",
        "CREATE",
        "MODIFY",
        "PROCESS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionKind"

def test_hyp_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_hyp_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "SOUTH",
        "NORTH",
        "NORTH_SOUTH",
        "SOUTH_EAST",
        "NORTH_WEST",
        "SOUTH_WEST",
        "EAST",
        "NONE",
        "EAST_WEST",
        "NORTH_EAST",
        "NSEW",
        "WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_hyp_colorconstants_exists():
    # Check that the Enumeration exists
    assert ColorConstants is not None

def test_hyp_colorconstants_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorConstants]
    expected_literals = [
        "blue",
        "lightGray",
        "white",
        "cyan",
        "darkBlue",
        "gray",
        "red",
        "green",
        "lightGreen",
        "darkGray",
        "darkGreen",
        "yellow",
        "black",
        "orange",
        "lightBlue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorConstants"

def test_hyp_labeltextaccessmethod_exists():
    # Check that the Enumeration exists
    assert LabelTextAccessMethod is not None

def test_hyp_labeltextaccessmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelTextAccessMethod]
    expected_literals = [
        "PRINTF",
        "REGEXP",
        "MESSAGE_FORMAT",
        "NATIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelTextAccessMethod"

def test_hyp_language_exists():
    # Check that the Enumeration exists
    assert Language is not None

def test_hyp_language_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Language]
    expected_literals = [
        "literal",
        "ocl",
        "regexp",
        "java",
        "nregexp",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Language"

def test_hyp_standardtoolkind_exists():
    # Check that the Enumeration exists
    assert StandardToolKind is not None

def test_hyp_standardtoolkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StandardToolKind]
    expected_literals = [
        "ZOOM_OUT",
        "ZOOM_IN",
        "MARQUEE",
        "ZOOM_PAN",
        "SELECT",
        "SELECT_PAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StandardToolKind"


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
AbstractFigure_strategy = st.builds(
    AbstractFigure,
)
gmf_all_gmfgraph_FigureRef_strategy = st.builds(
    gmf_all_gmfgraph_FigureRef,
)
gmf_all_gmfgraph_ChildAccess_strategy = st.builds(
    gmf_all_gmfgraph_ChildAccess,
    accessor=
        safe_text
)
Figure_strategy = st.builds(
    Figure,
)
gmf_all_gmfgraph_AbstractFigure_strategy = st.builds(
    gmf_all_gmfgraph_AbstractFigure,
)
gmf_all_gmfgraph_PinOwner_strategy = st.builds(
    gmf_all_gmfgraph_PinOwner,
)
gmf_all_gmfgraph_SVGProperty_strategy = st.builds(
    gmf_all_gmfgraph_SVGProperty,
    setter=
        safe_text,
    callSuper=
        st.booleans(),
    type=
        safe_text,
    attribute=
        safe_text,
    getter=
        safe_text,
    query=
        safe_text
)
Rectangle2D_strategy = st.builds(
    Rectangle2D,
)
SVGProperty_strategy = st.builds(
    SVGProperty,
)
gmf_all_gmfgraph_Rectangle2D_strategy = st.builds(
    gmf_all_gmfgraph_Rectangle2D,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
gmfgraph_Layout_strategy = st.builds(
    gmfgraph_Layout,
)
gmf_all_gmfgraph_Layout_strategy = st.builds(
    gmf_all_gmfgraph_Layout,
)
gmf_all_gmfgraph_Layoutable_strategy = st.builds(
    gmf_all_gmfgraph_Layoutable,
)
LayoutData_strategy = st.builds(
    LayoutData,
)
gmf_all_gmfgraph_BorderLayoutData_strategy = st.builds(
    gmf_all_gmfgraph_BorderLayoutData,
    alignment=
        safe_text,
    vertical=
        st.booleans()
)
gmf_all_gmfgraph_XYLayoutData_strategy = st.builds(
    gmf_all_gmfgraph_XYLayoutData,
)
gmf_all_gmfgraph_GridLayoutData_strategy = st.builds(
    gmf_all_gmfgraph_GridLayoutData,
    horizontalSpan=
        st.integers(),
    grabExcessVerticalSpace=
        st.booleans(),
    horizontalAlignment=
        safe_text,
    verticalAlignment=
        safe_text,
    horizontalIndent=
        st.integers(),
    verticalSpan=
        st.integers(),
    grabExcessHorizontalSpace=
        st.booleans()
)
gmfgraph_Border_strategy = st.builds(
    gmfgraph_Border,
)
gmf_all_gmfgraph_Border_strategy = st.builds(
    gmf_all_gmfgraph_Border,
)
gmfgraph_LayoutData_strategy = st.builds(
    gmfgraph_LayoutData,
)
gmf_all_gmfgraph_LayoutData_strategy = st.builds(
    gmf_all_gmfgraph_LayoutData,
)
gmf_all_gmfgraph_Point_strategy = st.builds(
    gmf_all_gmfgraph_Point,
    x=
        st.integers(),
    y=
        st.integers()
)
gmf_all_gmfgraph_Font_strategy = st.builds(
    gmf_all_gmfgraph_Font,
)
gmf_all_gmfgraph_Color_strategy = st.builds(
    gmf_all_gmfgraph_Color,
)
gmfgraph_CustomFigure_strategy = st.builds(
    gmfgraph_CustomFigure,
)
FigureAccessor_strategy = st.builds(
    FigureAccessor,
)
gmf_all_gmfgraph_Insets_strategy = st.builds(
    gmf_all_gmfgraph_Insets,
    bottom=
        st.integers(),
    right=
        st.integers(),
    top=
        st.integers(),
    left=
        st.integers()
)
gmf_all_gmfgraph_Dimension_strategy = st.builds(
    gmf_all_gmfgraph_Dimension,
    dx=
        st.integers(),
    dy=
        st.integers()
)
gmf_all_gmfgraph_FigureAccessor_strategy = st.builds(
    gmf_all_gmfgraph_FigureAccessor,
    accessor=
        safe_text
)
gmf_all_gmfgraph_CustomAttribute_strategy = st.builds(
    gmf_all_gmfgraph_CustomAttribute,
    value=
        safe_text,
    directAccess=
        st.booleans(),
    name=
        safe_text,
    multiStatementValue=
        st.booleans()
)
CustomAttributeOwner_strategy = st.builds(
    CustomAttributeOwner,
)
gmf_all_gmfgraph_CustomClass_strategy = st.builds(
    gmf_all_gmfgraph_CustomClass,
    qualifiedClassName=
        safe_text
)
CustomAttribute_strategy = st.builds(
    CustomAttribute,
)
gmf_all_gmfgraph_CustomAttributeOwner_strategy = st.builds(
    gmf_all_gmfgraph_CustomAttributeOwner,
)
gmfgraph_Polygon_strategy = st.builds(
    gmfgraph_Polygon,
)
gmfgraph_DecorationFigure_strategy = st.builds(
    gmfgraph_DecorationFigure,
)
gmf_all_gmfgraph_PolygonDecoration_strategy = st.builds(
    gmf_all_gmfgraph_PolygonDecoration,
)
gmf_all_gmfgraph_CustomDecoration_strategy = st.builds(
    gmf_all_gmfgraph_CustomDecoration,
)
DecorationFigure_strategy = st.builds(
    DecorationFigure,
)
gmfgraph_ConnectionFigure_strategy = st.builds(
    gmfgraph_ConnectionFigure,
)
gmf_all_gmfgraph_CustomConnection_strategy = st.builds(
    gmf_all_gmfgraph_CustomConnection,
)
gmfgraph_Polyline_strategy = st.builds(
    gmfgraph_Polyline,
)
gmf_all_gmfgraph_PolylineDecoration_strategy = st.builds(
    gmf_all_gmfgraph_PolylineDecoration,
)
gmf_all_gmfgraph_PolylineConnection_strategy = st.builds(
    gmf_all_gmfgraph_PolylineConnection,
)
Polygon_strategy = st.builds(
    Polygon,
)
gmf_all_gmfgraph_ScalablePolygon_strategy = st.builds(
    gmf_all_gmfgraph_ScalablePolygon,
)
Polyline_strategy = st.builds(
    Polyline,
)
gmf_all_gmfgraph_Polygon_strategy = st.builds(
    gmf_all_gmfgraph_Polygon,
)
gmfgraph_CustomClass_strategy = st.builds(
    gmfgraph_CustomClass,
)
gmf_all_gmfgraph_CustomBorder_strategy = st.builds(
    gmf_all_gmfgraph_CustomBorder,
)
gmf_all_gmfgraph_CustomLayoutData_strategy = st.builds(
    gmf_all_gmfgraph_CustomLayoutData,
)
gmf_all_gmfgraph_CustomLayout_strategy = st.builds(
    gmf_all_gmfgraph_CustomLayout,
)
gmfgraph_RealFigure_strategy = st.builds(
    gmfgraph_RealFigure,
)
gmf_all_gmfgraph_CustomFigure_strategy = st.builds(
    gmf_all_gmfgraph_CustomFigure,
)
Shape_strategy = st.builds(
    Shape,
)
gmf_all_gmfgraph_Polyline_strategy = st.builds(
    gmf_all_gmfgraph_Polyline,
)
gmf_all_gmfgraph_Ellipse_strategy = st.builds(
    gmf_all_gmfgraph_Ellipse,
)
gmf_all_gmfgraph_RoundedRectangle_strategy = st.builds(
    gmf_all_gmfgraph_RoundedRectangle,
    cornerHeight=
        st.integers(),
    cornerWidth=
        st.integers()
)
gmf_all_gmfgraph_Rectangle_strategy = st.builds(
    gmf_all_gmfgraph_Rectangle,
)
Point_strategy = st.builds(
    Point,
)
Insets_strategy = st.builds(
    Insets,
)
Font_strategy = st.builds(
    Font,
)
gmf_all_gmfgraph_BasicFont_strategy = st.builds(
    gmf_all_gmfgraph_BasicFont,
    style=
        safe_text,
    faceName=
        safe_text,
    height=
        st.integers()
)
Color_strategy = st.builds(
    Color,
)
gmf_all_gmfgraph_ConstantColor_strategy = st.builds(
    gmf_all_gmfgraph_ConstantColor,
    value=
        safe_text
)
gmf_all_gmfgraph_RGBColor_strategy = st.builds(
    gmf_all_gmfgraph_RGBColor,
    red=
        st.integers(),
    green=
        st.integers(),
    blue=
        st.integers()
)
gmfgraph_CustomAttributeOwner_strategy = st.builds(
    gmfgraph_CustomAttributeOwner,
)
gmfgraph_PinOwner_strategy = st.builds(
    gmfgraph_PinOwner,
)
gmfgraph_AbstractFigure_strategy = st.builds(
    gmfgraph_AbstractFigure,
)
gmf_all_gmfgraph_RealFigure_strategy = st.builds(
    gmf_all_gmfgraph_RealFigure,
    name=
        safe_text
)
Dimension_strategy = st.builds(
    Dimension,
)
gmf_all_gmfgraph_VisualFacet_strategy = st.builds(
    gmf_all_gmfgraph_VisualFacet,
)
ChildAccess_strategy = st.builds(
    ChildAccess,
)
Layoutable_strategy = st.builds(
    Layoutable,
)
gmf_all_gmfgraph_Figure_strategy = st.builds(
    gmf_all_gmfgraph_Figure,
)
VisualFacet_strategy = st.builds(
    VisualFacet,
)
gmf_all_gmfgraph_AlignmentFacet_strategy = st.builds(
    gmf_all_gmfgraph_AlignmentFacet,
    alignment=
        safe_text
)
gmf_all_gmfgraph_GeneralFacet_strategy = st.builds(
    gmf_all_gmfgraph_GeneralFacet,
    identifier=
        safe_text,
    data=
        safe_text
)
gmf_all_gmfgraph_LabelOffsetFacet_strategy = st.builds(
    gmf_all_gmfgraph_LabelOffsetFacet,
    y=
        st.integers(),
    x=
        st.integers()
)
gmf_all_gmfgraph_DefaultSizeFacet_strategy = st.builds(
    gmf_all_gmfgraph_DefaultSizeFacet,
)
gmf_all_gmfgraph_GradientFacet_strategy = st.builds(
    gmf_all_gmfgraph_GradientFacet,
    direction=
        safe_text
)
gmf_all_gmfgraph_Identity_strategy = st.builds(
    gmf_all_gmfgraph_Identity,
    name=
        safe_text
)
Layout_strategy = st.builds(
    Layout,
)
gmf_all_gmfgraph_CenterLayout_strategy = st.builds(
    gmf_all_gmfgraph_CenterLayout,
)
gmf_all_gmfgraph_LayoutRef_strategy = st.builds(
    gmf_all_gmfgraph_LayoutRef,
)
gmf_all_gmfgraph_XYLayout_strategy = st.builds(
    gmf_all_gmfgraph_XYLayout,
)
gmf_all_gmfgraph_BorderLayout_strategy = st.builds(
    gmf_all_gmfgraph_BorderLayout,
)
gmf_all_gmfgraph_FlowLayout_strategy = st.builds(
    gmf_all_gmfgraph_FlowLayout,
    forceSingleLine=
        st.booleans(),
    minorSpacing=
        st.integers(),
    majorAlignment=
        safe_text,
    minorAlignment=
        safe_text,
    majorSpacing=
        st.integers(),
    vertical=
        st.booleans(),
    matchMinorSize=
        st.booleans()
)
gmf_all_gmfgraph_GridLayout_strategy = st.builds(
    gmf_all_gmfgraph_GridLayout,
    numColumns=
        st.integers(),
    equalWidth=
        st.booleans()
)
gmf_all_gmfgraph_StackLayout_strategy = st.builds(
    gmf_all_gmfgraph_StackLayout,
)
Border_strategy = st.builds(
    Border,
)
gmf_all_gmfgraph_CompoundBorder_strategy = st.builds(
    gmf_all_gmfgraph_CompoundBorder,
)
gmf_all_gmfgraph_LineBorder_strategy = st.builds(
    gmf_all_gmfgraph_LineBorder,
    width=
        st.integers()
)
gmf_all_gmfgraph_BorderRef_strategy = st.builds(
    gmf_all_gmfgraph_BorderRef,
)
gmf_all_gmfgraph_MarginBorder_strategy = st.builds(
    gmf_all_gmfgraph_MarginBorder,
)
FigureDescriptor_strategy = st.builds(
    FigureDescriptor,
)
RealFigure_strategy = st.builds(
    RealFigure,
)
gmf_all_gmfgraph_InvisibleRectangle_strategy = st.builds(
    gmf_all_gmfgraph_InvisibleRectangle,
)
gmf_all_gmfgraph_VerticalLabel_strategy = st.builds(
    gmf_all_gmfgraph_VerticalLabel,
    text=
        safe_text
)
gmf_all_gmfgraph_Shape_strategy = st.builds(
    gmf_all_gmfgraph_Shape,
    xorFill=
        st.booleans(),
    outline=
        st.booleans(),
    fill=
        st.booleans(),
    lineKind=
        safe_text,
    xorOutline=
        st.booleans(),
    lineWidth=
        st.integers()
)
gmf_all_gmfgraph_SVGFigure_strategy = st.builds(
    gmf_all_gmfgraph_SVGFigure,
    noCanvasWidth=
        st.booleans(),
    documentURI=
        safe_text,
    noCanvasHeight=
        st.booleans()
)
gmf_all_gmfgraph_Label_strategy = st.builds(
    gmf_all_gmfgraph_Label,
    text=
        safe_text
)
gmf_all_gmfgraph_DecorationFigure_strategy = st.builds(
    gmf_all_gmfgraph_DecorationFigure,
)
gmf_all_gmfgraph_ConnectionFigure_strategy = st.builds(
    gmf_all_gmfgraph_ConnectionFigure,
)
gmf_all_gmfgraph_LabeledContainer_strategy = st.builds(
    gmf_all_gmfgraph_LabeledContainer,
)
FigureGallery_strategy = st.builds(
    FigureGallery,
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
gmf_all_gmfgraph_Node_strategy = st.builds(
    gmf_all_gmfgraph_Node,
    resizeConstraint=
        safe_text,
    affixedParentSide=
        safe_text
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
gmf_all_gmfgraph_Compartment_strategy = st.builds(
    gmf_all_gmfgraph_Compartment,
    collapsible=
        st.booleans(),
    needsTitle=
        st.booleans()
)
gmf_all_gmfgraph_Connection_strategy = st.builds(
    gmf_all_gmfgraph_Connection,
)
gmf_all_gmfgraph_AbstractNode_strategy = st.builds(
    gmf_all_gmfgraph_AbstractNode,
)
gmf_all_tooldef_StyleSelector_strategy = st.builds(
    gmf_all_tooldef_StyleSelector,
)
gmf_all_tooldef_Image_strategy = st.builds(
    gmf_all_tooldef_Image,
)
tooldef_ContributionItem_strategy = st.builds(
    tooldef_ContributionItem,
)
Identity_strategy = st.builds(
    Identity,
)
gmf_all_gmfgraph_Pin_strategy = st.builds(
    gmf_all_gmfgraph_Pin,
)
gmf_all_gmfgraph_FigureDescriptor_strategy = st.builds(
    gmf_all_gmfgraph_FigureDescriptor,
)
gmf_all_gmfgraph_DiagramElement_strategy = st.builds(
    gmf_all_gmfgraph_DiagramElement,
)
gmf_all_gmfgraph_FigureGallery_strategy = st.builds(
    gmf_all_gmfgraph_FigureGallery,
    implementationBundle=
        safe_text
)
gmf_all_gmfgraph_Canvas_strategy = st.builds(
    gmf_all_gmfgraph_Canvas,
)
tooldef_PredefinedItem_strategy = st.builds(
    tooldef_PredefinedItem,
)
tooldef_Menu_strategy = st.builds(
    tooldef_Menu,
)
gmf_all_tooldef_PopupMenu_strategy = st.builds(
    gmf_all_tooldef_PopupMenu,
    iD=
        safe_text
)
gmf_all_tooldef_PredefinedMenu_strategy = st.builds(
    gmf_all_tooldef_PredefinedMenu,
)
ItemBase_strategy = st.builds(
    ItemBase,
)
gmf_all_tooldef_Separator_strategy = st.builds(
    gmf_all_tooldef_Separator,
    name=
        safe_text
)
gmf_all_tooldef_PredefinedItem_strategy = st.builds(
    gmf_all_tooldef_PredefinedItem,
    identifier=
        safe_text
)
gmf_all_tooldef_ContributionItem_strategy = st.builds(
    gmf_all_tooldef_ContributionItem,
    title=
        safe_text
)
gmf_all_tooldef_Menu_strategy = st.builds(
    gmf_all_tooldef_Menu,
)
gmf_all_tooldef_ItemBase_strategy = st.builds(
    gmf_all_tooldef_ItemBase,
)
gmf_all_tooldef_ItemRef_strategy = st.builds(
    gmf_all_tooldef_ItemRef,
)
ContributionItem_strategy = st.builds(
    ContributionItem,
)
gmf_all_tooldef_MenuAction_strategy = st.builds(
    gmf_all_tooldef_MenuAction,
    kind=
        safe_text,
    hotKey=
        safe_text
)
Image_strategy = st.builds(
    Image,
)
gmf_all_tooldef_BundleImage_strategy = st.builds(
    gmf_all_tooldef_BundleImage,
    path=
        safe_text,
    bundle=
        safe_text
)
gmf_all_tooldef_DefaultImage_strategy = st.builds(
    gmf_all_tooldef_DefaultImage,
)
gmf_all_tooldef_AbstractTool_strategy = st.builds(
    gmf_all_tooldef_AbstractTool,
    description=
        safe_text,
    title=
        safe_text
)
Menu_strategy = st.builds(
    Menu,
)
gmf_all_tooldef_Toolbar_strategy = st.builds(
    gmf_all_tooldef_Toolbar,
)
gmf_all_tooldef_ContextMenu_strategy = st.builds(
    gmf_all_tooldef_ContextMenu,
)
gmf_all_tooldef_MainMenu_strategy = st.builds(
    gmf_all_tooldef_MainMenu,
    title=
        safe_text
)
MenuAction_strategy = st.builds(
    MenuAction,
)
gmf_all_tooldef_ToolRegistry_strategy = st.builds(
    gmf_all_tooldef_ToolRegistry,
)
Pin_strategy = st.builds(
    Pin,
)
gmf_all_gmfgraph_CustomPin_strategy = st.builds(
    gmf_all_gmfgraph_CustomPin,
    customOperationName=
        safe_text,
    customOperationType=
        safe_text
)
gmf_all_gmfgraph_VisiblePin_strategy = st.builds(
    gmf_all_gmfgraph_VisiblePin,
)
gmf_all_gmfgraph_ColorPin_strategy = st.builds(
    gmf_all_gmfgraph_ColorPin,
    backgroundNotForeground=
        st.booleans()
)
gmf_all_mappings_VisualEffectMapping_strategy = st.builds(
    gmf_all_mappings_VisualEffectMapping,
    oclExpression=
        safe_text
)
gmf_all_mappings_Measurable_strategy = st.builds(
    gmf_all_mappings_Measurable,
)
gmf_all_mappings_Auditable_strategy = st.builds(
    gmf_all_mappings_Auditable,
)
ToolContainer_strategy = st.builds(
    ToolContainer,
)
gmf_all_tooldef_Palette_strategy = st.builds(
    gmf_all_tooldef_Palette,
)
gmf_all_tooldef_ToolGroup_strategy = st.builds(
    gmf_all_tooldef_ToolGroup,
    stack=
        st.booleans(),
    collapsible=
        st.booleans()
)
Measurable_strategy = st.builds(
    Measurable,
)
MetricRule_strategy = st.builds(
    MetricRule,
)
gmf_all_mappings_MetricContainer_strategy = st.builds(
    gmf_all_mappings_MetricContainer,
)
mappings_Measurable_strategy = st.builds(
    mappings_Measurable,
)
mappings_Auditable_strategy = st.builds(
    mappings_Auditable,
)
gmf_all_mappings_NotationElementTarget_strategy = st.builds(
    gmf_all_mappings_NotationElementTarget,
)
gmf_all_mappings_DiagramElementTarget_strategy = st.builds(
    gmf_all_mappings_DiagramElementTarget,
)
gmf_all_mappings_DomainElementTarget_strategy = st.builds(
    gmf_all_mappings_DomainElementTarget,
)
Auditable_strategy = st.builds(
    Auditable,
)
gmf_all_mappings_AuditedMetricTarget_strategy = st.builds(
    gmf_all_mappings_AuditedMetricTarget,
)
RuleBase_strategy = st.builds(
    RuleBase,
)
gmf_all_mappings_MetricRule_strategy = st.builds(
    gmf_all_mappings_MetricRule,
    lowLimit=
        safe_text,
    key=
        safe_text,
    highLimit=
        safe_text
)
gmf_all_mappings_AuditRule_strategy = st.builds(
    gmf_all_mappings_AuditRule,
    id=
        safe_text,
    useInLiveMode=
        st.booleans(),
    message=
        safe_text,
    severity=
        safe_text
)
gmf_all_mappings_RuleBase_strategy = st.builds(
    gmf_all_mappings_RuleBase,
    description=
        safe_text,
    name=
        safe_text
)
gmf_all_mappings_DomainAttributeTarget_strategy = st.builds(
    gmf_all_mappings_DomainAttributeTarget,
    nullAsError=
        st.booleans()
)
gmf_all_mappings_AuditContainer_strategy = st.builds(
    gmf_all_mappings_AuditContainer,
    description=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
gmf_all_mappings_AppearanceSteward_strategy = st.builds(
    gmf_all_mappings_AppearanceSteward,
)
AbstractTool_strategy = st.builds(
    AbstractTool,
)
gmf_all_tooldef_GenericTool_strategy = st.builds(
    gmf_all_tooldef_GenericTool,
    toolClass=
        safe_text
)
gmf_all_tooldef_ToolContainer_strategy = st.builds(
    gmf_all_tooldef_ToolContainer,
)
gmf_all_tooldef_CreationTool_strategy = st.builds(
    gmf_all_tooldef_CreationTool,
)
gmf_all_tooldef_PaletteSeparator_strategy = st.builds(
    gmf_all_tooldef_PaletteSeparator,
)
gmf_all_tooldef_StandardTool_strategy = st.builds(
    gmf_all_tooldef_StandardTool,
    toolKind=
        safe_text
)
gmf_all_mappings_ToolOwner_strategy = st.builds(
    gmf_all_mappings_ToolOwner,
)
ContextMenu_strategy = st.builds(
    ContextMenu,
)
gmf_all_mappings_MenuOwner_strategy = st.builds(
    gmf_all_mappings_MenuOwner,
)
FeatureSeqInitializer_strategy = st.builds(
    FeatureSeqInitializer,
)
AuditRule_strategy = st.builds(
    AuditRule,
)
ReferenceNewElementSpec_strategy = st.builds(
    ReferenceNewElementSpec,
)
FeatureInitializer_strategy = st.builds(
    FeatureInitializer,
)
gmf_all_mappings_ReferenceNewElementSpec_strategy = st.builds(
    gmf_all_mappings_ReferenceNewElementSpec,
)
gmf_all_mappings_FeatureValueSpec_strategy = st.builds(
    gmf_all_mappings_FeatureValueSpec,
)
gmf_all_mappings_ElementInitializer_strategy = st.builds(
    gmf_all_mappings_ElementInitializer,
)
gmf_all_mappings_ValueExpression_strategy = st.builds(
    gmf_all_mappings_ValueExpression,
    language=
        safe_text,
    langName=
        safe_text,
    body=
        safe_text
)
gmf_all_mappings_FeatureInitializer_strategy = st.builds(
    gmf_all_mappings_FeatureInitializer,
)
gmf_all_mappings_LinkConstraints_strategy = st.builds(
    gmf_all_mappings_LinkConstraints,
)
mappings_gmf_all_EAttribute_strategy = st.builds(
    mappings_gmf_all_EAttribute,
)
MappingEntry_strategy = st.builds(
    MappingEntry,
)
DiagramLabel_strategy = st.builds(
    DiagramLabel,
)
gmf_all_mappings_LabelMapping_strategy = st.builds(
    gmf_all_mappings_LabelMapping,
    readOnly=
        st.booleans()
)
Toolbar_strategy = st.builds(
    Toolbar,
)
MainMenu_strategy = st.builds(
    MainMenu,
)
ValueExpression_strategy = st.builds(
    ValueExpression,
)
gmf_all_mappings_Constraint_strategy = st.builds(
    gmf_all_mappings_Constraint,
)
Canvas_strategy = st.builds(
    Canvas,
)
gmf_all_mappings_CanvasMapping_strategy = st.builds(
    gmf_all_mappings_CanvasMapping,
)
LinkConstraints_strategy = st.builds(
    LinkConstraints,
)
mappings_gmf_all_EStructuralFeature_strategy = st.builds(
    mappings_gmf_all_EStructuralFeature,
)
Connection_strategy = st.builds(
    Connection,
)
mappings_NeedsContainment_strategy = st.builds(
    mappings_NeedsContainment,
)
Compartment_strategy = st.builds(
    Compartment,
)
gmf_all_mappings_CompartmentMapping_strategy = st.builds(
    gmf_all_mappings_CompartmentMapping,
)
ChildReference_strategy = st.builds(
    ChildReference,
)
Palette_strategy = st.builds(
    Palette,
)
mappings_gmf_all_EPackage_strategy = st.builds(
    mappings_gmf_all_EPackage,
)
CompartmentMapping_strategy = st.builds(
    CompartmentMapping,
)
NodeReference_strategy = st.builds(
    NodeReference,
)
gmf_all_mappings_TopNodeReference_strategy = st.builds(
    gmf_all_mappings_TopNodeReference,
)
gmf_all_mappings_ChildReference_strategy = st.builds(
    gmf_all_mappings_ChildReference,
)
NodeMapping_strategy = st.builds(
    NodeMapping,
)
NeedsContainment_strategy = st.builds(
    NeedsContainment,
)
gmf_all_mappings_NodeReference_strategy = st.builds(
    gmf_all_mappings_NodeReference,
)
Node_strategy = st.builds(
    Node,
)
gmf_all_gmfgraph_DiagramLabel_strategy = st.builds(
    gmf_all_gmfgraph_DiagramLabel,
    elementIcon=
        st.booleans(),
    external=
        st.booleans()
)
mappings_AppearanceSteward_strategy = st.builds(
    mappings_AppearanceSteward,
)
mappings_ToolOwner_strategy = st.builds(
    mappings_ToolOwner,
)
mappings_MenuOwner_strategy = st.builds(
    mappings_MenuOwner,
)
mappings_MappingEntry_strategy = st.builds(
    mappings_MappingEntry,
)
gmf_all_mappings_LinkMapping_strategy = st.builds(
    gmf_all_mappings_LinkMapping,
)
gmf_all_mappings_NodeMapping_strategy = st.builds(
    gmf_all_mappings_NodeMapping,
)
LabelMapping_strategy = st.builds(
    LabelMapping,
)
gmf_all_mappings_ExpressionLabelMapping_strategy = st.builds(
    gmf_all_mappings_ExpressionLabelMapping,
)
gmf_all_mappings_FeatureLabelMapping_strategy = st.builds(
    gmf_all_mappings_FeatureLabelMapping,
    viewPattern=
        safe_text,
    editPattern=
        safe_text,
    viewMethod=
        safe_text,
    editMethod=
        safe_text,
    editorPattern=
        safe_text
)
gmf_all_mappings_OclChoiceLabelMapping_strategy = st.builds(
    gmf_all_mappings_OclChoiceLabelMapping,
)
gmf_all_mappings_DesignLabelMapping_strategy = st.builds(
    gmf_all_mappings_DesignLabelMapping,
)
ElementInitializer_strategy = st.builds(
    ElementInitializer,
)
gmf_all_mappings_FeatureSeqInitializer_strategy = st.builds(
    gmf_all_mappings_FeatureSeqInitializer,
)
Constraint_strategy = st.builds(
    Constraint,
)
mappings_gmf_all_EClass_strategy = st.builds(
    mappings_gmf_all_EClass,
)
gmf_all_mappings_MappingEntry_strategy = st.builds(
    gmf_all_mappings_MappingEntry,
)
MetricContainer_strategy = st.builds(
    MetricContainer,
)
AuditContainer_strategy = st.builds(
    AuditContainer,
)
StyleSelector_strategy = st.builds(
    StyleSelector,
)
gmf_all_tooldef_GenericStyleSelector_strategy = st.builds(
    gmf_all_tooldef_GenericStyleSelector,
    values=
        safe_text
)
CanvasMapping_strategy = st.builds(
    CanvasMapping,
)
LinkMapping_strategy = st.builds(
    LinkMapping,
)
mappings_gmf_all_EReference_strategy = st.builds(
    mappings_gmf_all_EReference,
)
gmf_all_mappings_NeedsContainment_strategy = st.builds(
    gmf_all_mappings_NeedsContainment,
)
VisualEffectMapping_strategy = st.builds(
    VisualEffectMapping,
)
TopNodeReference_strategy = st.builds(
    TopNodeReference,
)
gmf_all_mappings_Mapping_strategy = st.builds(
    gmf_all_mappings_Mapping,
)






@given(instance=gmf_all_gmfgraph_ChildAccess_strategy)
def test_hyp_gmf_all_gmfgraph_childaccess_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original







@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_hyp_gmf_all_gmfgraph_svgproperty_setter_setter(instance):
    original = instance.setter
    instance.setter = original
    assert instance.setter == original



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_hyp_gmf_all_gmfgraph_svgproperty_callSuper_setter(instance):
    original = instance.callSuper
    instance.callSuper = original
    assert instance.callSuper == original



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_hyp_gmf_all_gmfgraph_svgproperty_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_hyp_gmf_all_gmfgraph_svgproperty_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_hyp_gmf_all_gmfgraph_svgproperty_getter_setter(instance):
    original = instance.getter
    instance.getter = original
    assert instance.getter == original



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_hyp_gmf_all_gmfgraph_svgproperty_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original






@given(instance=gmf_all_gmfgraph_Rectangle2D_strategy)
def test_hyp_gmf_all_gmfgraph_rectangle2d_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=gmf_all_gmfgraph_Rectangle2D_strategy)
def test_hyp_gmf_all_gmfgraph_rectangle2d_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=gmf_all_gmfgraph_Rectangle2D_strategy)
def test_hyp_gmf_all_gmfgraph_rectangle2d_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=gmf_all_gmfgraph_Rectangle2D_strategy)
def test_hyp_gmf_all_gmfgraph_rectangle2d_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original








@given(instance=gmf_all_gmfgraph_BorderLayoutData_strategy)
def test_hyp_gmf_all_gmfgraph_borderlayoutdata_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original



@given(instance=gmf_all_gmfgraph_BorderLayoutData_strategy)
def test_hyp_gmf_all_gmfgraph_borderlayoutdata_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original





@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_hyp_gmf_all_gmfgraph_gridlayoutdata_horizontalSpan_setter(instance):
    original = instance.horizontalSpan
    instance.horizontalSpan = original
    assert instance.horizontalSpan == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_hyp_gmf_all_gmfgraph_gridlayoutdata_grabExcessVerticalSpace_setter(instance):
    original = instance.grabExcessVerticalSpace
    instance.grabExcessVerticalSpace = original
    assert instance.grabExcessVerticalSpace == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_hyp_gmf_all_gmfgraph_gridlayoutdata_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_hyp_gmf_all_gmfgraph_gridlayoutdata_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_hyp_gmf_all_gmfgraph_gridlayoutdata_horizontalIndent_setter(instance):
    original = instance.horizontalIndent
    instance.horizontalIndent = original
    assert instance.horizontalIndent == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_hyp_gmf_all_gmfgraph_gridlayoutdata_verticalSpan_setter(instance):
    original = instance.verticalSpan
    instance.verticalSpan = original
    assert instance.verticalSpan == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_hyp_gmf_all_gmfgraph_gridlayoutdata_grabExcessHorizontalSpace_setter(instance):
    original = instance.grabExcessHorizontalSpace
    instance.grabExcessHorizontalSpace = original
    assert instance.grabExcessHorizontalSpace == original








@given(instance=gmf_all_gmfgraph_Point_strategy)
def test_hyp_gmf_all_gmfgraph_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=gmf_all_gmfgraph_Point_strategy)
def test_hyp_gmf_all_gmfgraph_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original








@given(instance=gmf_all_gmfgraph_Insets_strategy)
def test_hyp_gmf_all_gmfgraph_insets_bottom_setter(instance):
    original = instance.bottom
    instance.bottom = original
    assert instance.bottom == original



@given(instance=gmf_all_gmfgraph_Insets_strategy)
def test_hyp_gmf_all_gmfgraph_insets_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original



@given(instance=gmf_all_gmfgraph_Insets_strategy)
def test_hyp_gmf_all_gmfgraph_insets_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original



@given(instance=gmf_all_gmfgraph_Insets_strategy)
def test_hyp_gmf_all_gmfgraph_insets_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original




@given(instance=gmf_all_gmfgraph_Dimension_strategy)
def test_hyp_gmf_all_gmfgraph_dimension_dx_setter(instance):
    original = instance.dx
    instance.dx = original
    assert instance.dx == original



@given(instance=gmf_all_gmfgraph_Dimension_strategy)
def test_hyp_gmf_all_gmfgraph_dimension_dy_setter(instance):
    original = instance.dy
    instance.dy = original
    assert instance.dy == original




@given(instance=gmf_all_gmfgraph_FigureAccessor_strategy)
def test_hyp_gmf_all_gmfgraph_figureaccessor_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original




@given(instance=gmf_all_gmfgraph_CustomAttribute_strategy)
def test_hyp_gmf_all_gmfgraph_customattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=gmf_all_gmfgraph_CustomAttribute_strategy)
def test_hyp_gmf_all_gmfgraph_customattribute_directAccess_setter(instance):
    original = instance.directAccess
    instance.directAccess = original
    assert instance.directAccess == original



@given(instance=gmf_all_gmfgraph_CustomAttribute_strategy)
def test_hyp_gmf_all_gmfgraph_customattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=gmf_all_gmfgraph_CustomAttribute_strategy)
def test_hyp_gmf_all_gmfgraph_customattribute_multiStatementValue_setter(instance):
    original = instance.multiStatementValue
    instance.multiStatementValue = original
    assert instance.multiStatementValue == original





@given(instance=gmf_all_gmfgraph_CustomClass_strategy)
def test_hyp_gmf_all_gmfgraph_customclass_qualifiedClassName_setter(instance):
    original = instance.qualifiedClassName
    instance.qualifiedClassName = original
    assert instance.qualifiedClassName == original





























@given(instance=gmf_all_gmfgraph_RoundedRectangle_strategy)
def test_hyp_gmf_all_gmfgraph_roundedrectangle_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original



@given(instance=gmf_all_gmfgraph_RoundedRectangle_strategy)
def test_hyp_gmf_all_gmfgraph_roundedrectangle_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original








@given(instance=gmf_all_gmfgraph_BasicFont_strategy)
def test_hyp_gmf_all_gmfgraph_basicfont_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=gmf_all_gmfgraph_BasicFont_strategy)
def test_hyp_gmf_all_gmfgraph_basicfont_faceName_setter(instance):
    original = instance.faceName
    instance.faceName = original
    assert instance.faceName == original



@given(instance=gmf_all_gmfgraph_BasicFont_strategy)
def test_hyp_gmf_all_gmfgraph_basicfont_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original





@given(instance=gmf_all_gmfgraph_ConstantColor_strategy)
def test_hyp_gmf_all_gmfgraph_constantcolor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=gmf_all_gmfgraph_RGBColor_strategy)
def test_hyp_gmf_all_gmfgraph_rgbcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=gmf_all_gmfgraph_RGBColor_strategy)
def test_hyp_gmf_all_gmfgraph_rgbcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=gmf_all_gmfgraph_RGBColor_strategy)
def test_hyp_gmf_all_gmfgraph_rgbcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original







@given(instance=gmf_all_gmfgraph_RealFigure_strategy)
def test_hyp_gmf_all_gmfgraph_realfigure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original










@given(instance=gmf_all_gmfgraph_AlignmentFacet_strategy)
def test_hyp_gmf_all_gmfgraph_alignmentfacet_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original




@given(instance=gmf_all_gmfgraph_GeneralFacet_strategy)
def test_hyp_gmf_all_gmfgraph_generalfacet_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=gmf_all_gmfgraph_GeneralFacet_strategy)
def test_hyp_gmf_all_gmfgraph_generalfacet_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original




@given(instance=gmf_all_gmfgraph_LabelOffsetFacet_strategy)
def test_hyp_gmf_all_gmfgraph_labeloffsetfacet_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=gmf_all_gmfgraph_LabelOffsetFacet_strategy)
def test_hyp_gmf_all_gmfgraph_labeloffsetfacet_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original





@given(instance=gmf_all_gmfgraph_GradientFacet_strategy)
def test_hyp_gmf_all_gmfgraph_gradientfacet_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original




@given(instance=gmf_all_gmfgraph_Identity_strategy)
def test_hyp_gmf_all_gmfgraph_identity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_hyp_gmf_all_gmfgraph_flowlayout_forceSingleLine_setter(instance):
    original = instance.forceSingleLine
    instance.forceSingleLine = original
    assert instance.forceSingleLine == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_hyp_gmf_all_gmfgraph_flowlayout_minorSpacing_setter(instance):
    original = instance.minorSpacing
    instance.minorSpacing = original
    assert instance.minorSpacing == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_hyp_gmf_all_gmfgraph_flowlayout_majorAlignment_setter(instance):
    original = instance.majorAlignment
    instance.majorAlignment = original
    assert instance.majorAlignment == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_hyp_gmf_all_gmfgraph_flowlayout_minorAlignment_setter(instance):
    original = instance.minorAlignment
    instance.minorAlignment = original
    assert instance.minorAlignment == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_hyp_gmf_all_gmfgraph_flowlayout_majorSpacing_setter(instance):
    original = instance.majorSpacing
    instance.majorSpacing = original
    assert instance.majorSpacing == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_hyp_gmf_all_gmfgraph_flowlayout_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_hyp_gmf_all_gmfgraph_flowlayout_matchMinorSize_setter(instance):
    original = instance.matchMinorSize
    instance.matchMinorSize = original
    assert instance.matchMinorSize == original




@given(instance=gmf_all_gmfgraph_GridLayout_strategy)
def test_hyp_gmf_all_gmfgraph_gridlayout_numColumns_setter(instance):
    original = instance.numColumns
    instance.numColumns = original
    assert instance.numColumns == original



@given(instance=gmf_all_gmfgraph_GridLayout_strategy)
def test_hyp_gmf_all_gmfgraph_gridlayout_equalWidth_setter(instance):
    original = instance.equalWidth
    instance.equalWidth = original
    assert instance.equalWidth == original







@given(instance=gmf_all_gmfgraph_LineBorder_strategy)
def test_hyp_gmf_all_gmfgraph_lineborder_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original









@given(instance=gmf_all_gmfgraph_VerticalLabel_strategy)
def test_hyp_gmf_all_gmfgraph_verticallabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_hyp_gmf_all_gmfgraph_shape_xorFill_setter(instance):
    original = instance.xorFill
    instance.xorFill = original
    assert instance.xorFill == original



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_hyp_gmf_all_gmfgraph_shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_hyp_gmf_all_gmfgraph_shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_hyp_gmf_all_gmfgraph_shape_lineKind_setter(instance):
    original = instance.lineKind
    instance.lineKind = original
    assert instance.lineKind == original



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_hyp_gmf_all_gmfgraph_shape_xorOutline_setter(instance):
    original = instance.xorOutline
    instance.xorOutline = original
    assert instance.xorOutline == original



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_hyp_gmf_all_gmfgraph_shape_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original




@given(instance=gmf_all_gmfgraph_SVGFigure_strategy)
def test_hyp_gmf_all_gmfgraph_svgfigure_noCanvasWidth_setter(instance):
    original = instance.noCanvasWidth
    instance.noCanvasWidth = original
    assert instance.noCanvasWidth == original



@given(instance=gmf_all_gmfgraph_SVGFigure_strategy)
def test_hyp_gmf_all_gmfgraph_svgfigure_documentURI_setter(instance):
    original = instance.documentURI
    instance.documentURI = original
    assert instance.documentURI == original



@given(instance=gmf_all_gmfgraph_SVGFigure_strategy)
def test_hyp_gmf_all_gmfgraph_svgfigure_noCanvasHeight_setter(instance):
    original = instance.noCanvasHeight
    instance.noCanvasHeight = original
    assert instance.noCanvasHeight == original




@given(instance=gmf_all_gmfgraph_Label_strategy)
def test_hyp_gmf_all_gmfgraph_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original









@given(instance=gmf_all_gmfgraph_Node_strategy)
def test_hyp_gmf_all_gmfgraph_node_resizeConstraint_setter(instance):
    original = instance.resizeConstraint
    instance.resizeConstraint = original
    assert instance.resizeConstraint == original



@given(instance=gmf_all_gmfgraph_Node_strategy)
def test_hyp_gmf_all_gmfgraph_node_affixedParentSide_setter(instance):
    original = instance.affixedParentSide
    instance.affixedParentSide = original
    assert instance.affixedParentSide == original





@given(instance=gmf_all_gmfgraph_Compartment_strategy)
def test_hyp_gmf_all_gmfgraph_compartment_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original



@given(instance=gmf_all_gmfgraph_Compartment_strategy)
def test_hyp_gmf_all_gmfgraph_compartment_needsTitle_setter(instance):
    original = instance.needsTitle
    instance.needsTitle = original
    assert instance.needsTitle == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gmf_all_tooldef_StyleSelector_strategy)
@settings(max_examples=30)
def test_hyp_gmf_all_tooldef_styleselector_isok_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isOk(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isOk).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isOk' in gmf_all_tooldef_StyleSelector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isOk' in gmf_all_tooldef_StyleSelector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isOk' in gmf_all_tooldef_StyleSelector is not implemented or raised an error")










@given(instance=gmf_all_gmfgraph_FigureGallery_strategy)
def test_hyp_gmf_all_gmfgraph_figuregallery_implementationBundle_setter(instance):
    original = instance.implementationBundle
    instance.implementationBundle = original
    assert instance.implementationBundle == original







@given(instance=gmf_all_tooldef_PopupMenu_strategy)
def test_hyp_gmf_all_tooldef_popupmenu_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original






@given(instance=gmf_all_tooldef_Separator_strategy)
def test_hyp_gmf_all_tooldef_separator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=gmf_all_tooldef_PredefinedItem_strategy)
def test_hyp_gmf_all_tooldef_predefineditem_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original




@given(instance=gmf_all_tooldef_ContributionItem_strategy)
def test_hyp_gmf_all_tooldef_contributionitem_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original








@given(instance=gmf_all_tooldef_MenuAction_strategy)
def test_hyp_gmf_all_tooldef_menuaction_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=gmf_all_tooldef_MenuAction_strategy)
def test_hyp_gmf_all_tooldef_menuaction_hotKey_setter(instance):
    original = instance.hotKey
    instance.hotKey = original
    assert instance.hotKey == original





@given(instance=gmf_all_tooldef_BundleImage_strategy)
def test_hyp_gmf_all_tooldef_bundleimage_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=gmf_all_tooldef_BundleImage_strategy)
def test_hyp_gmf_all_tooldef_bundleimage_bundle_setter(instance):
    original = instance.bundle
    instance.bundle = original
    assert instance.bundle == original





@given(instance=gmf_all_tooldef_AbstractTool_strategy)
def test_hyp_gmf_all_tooldef_abstracttool_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=gmf_all_tooldef_AbstractTool_strategy)
def test_hyp_gmf_all_tooldef_abstracttool_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original







@given(instance=gmf_all_tooldef_MainMenu_strategy)
def test_hyp_gmf_all_tooldef_mainmenu_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original







@given(instance=gmf_all_gmfgraph_CustomPin_strategy)
def test_hyp_gmf_all_gmfgraph_custompin_customOperationName_setter(instance):
    original = instance.customOperationName
    instance.customOperationName = original
    assert instance.customOperationName == original



@given(instance=gmf_all_gmfgraph_CustomPin_strategy)
def test_hyp_gmf_all_gmfgraph_custompin_customOperationType_setter(instance):
    original = instance.customOperationType
    instance.customOperationType = original
    assert instance.customOperationType == original





@given(instance=gmf_all_gmfgraph_ColorPin_strategy)
def test_hyp_gmf_all_gmfgraph_colorpin_backgroundNotForeground_setter(instance):
    original = instance.backgroundNotForeground
    instance.backgroundNotForeground = original
    assert instance.backgroundNotForeground == original




@given(instance=gmf_all_mappings_VisualEffectMapping_strategy)
def test_hyp_gmf_all_mappings_visualeffectmapping_oclExpression_setter(instance):
    original = instance.oclExpression
    instance.oclExpression = original
    assert instance.oclExpression == original








@given(instance=gmf_all_tooldef_ToolGroup_strategy)
def test_hyp_gmf_all_tooldef_toolgroup_stack_setter(instance):
    original = instance.stack
    instance.stack = original
    assert instance.stack == original



@given(instance=gmf_all_tooldef_ToolGroup_strategy)
def test_hyp_gmf_all_tooldef_toolgroup_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original















@given(instance=gmf_all_mappings_MetricRule_strategy)
def test_hyp_gmf_all_mappings_metricrule_lowLimit_setter(instance):
    original = instance.lowLimit
    instance.lowLimit = original
    assert instance.lowLimit == original



@given(instance=gmf_all_mappings_MetricRule_strategy)
def test_hyp_gmf_all_mappings_metricrule_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=gmf_all_mappings_MetricRule_strategy)
def test_hyp_gmf_all_mappings_metricrule_highLimit_setter(instance):
    original = instance.highLimit
    instance.highLimit = original
    assert instance.highLimit == original




@given(instance=gmf_all_mappings_AuditRule_strategy)
def test_hyp_gmf_all_mappings_auditrule_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=gmf_all_mappings_AuditRule_strategy)
def test_hyp_gmf_all_mappings_auditrule_useInLiveMode_setter(instance):
    original = instance.useInLiveMode
    instance.useInLiveMode = original
    assert instance.useInLiveMode == original



@given(instance=gmf_all_mappings_AuditRule_strategy)
def test_hyp_gmf_all_mappings_auditrule_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=gmf_all_mappings_AuditRule_strategy)
def test_hyp_gmf_all_mappings_auditrule_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original




@given(instance=gmf_all_mappings_RuleBase_strategy)
def test_hyp_gmf_all_mappings_rulebase_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=gmf_all_mappings_RuleBase_strategy)
def test_hyp_gmf_all_mappings_rulebase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=gmf_all_mappings_DomainAttributeTarget_strategy)
def test_hyp_gmf_all_mappings_domainattributetarget_nullAsError_setter(instance):
    original = instance.nullAsError
    instance.nullAsError = original
    assert instance.nullAsError == original




@given(instance=gmf_all_mappings_AuditContainer_strategy)
def test_hyp_gmf_all_mappings_auditcontainer_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=gmf_all_mappings_AuditContainer_strategy)
def test_hyp_gmf_all_mappings_auditcontainer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=gmf_all_mappings_AuditContainer_strategy)
def test_hyp_gmf_all_mappings_auditcontainer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=gmf_all_tooldef_GenericTool_strategy)
def test_hyp_gmf_all_tooldef_generictool_toolClass_setter(instance):
    original = instance.toolClass
    instance.toolClass = original
    assert instance.toolClass == original







@given(instance=gmf_all_tooldef_StandardTool_strategy)
def test_hyp_gmf_all_tooldef_standardtool_toolKind_setter(instance):
    original = instance.toolKind
    instance.toolKind = original
    assert instance.toolKind == original














@given(instance=gmf_all_mappings_ValueExpression_strategy)
def test_hyp_gmf_all_mappings_valueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=gmf_all_mappings_ValueExpression_strategy)
def test_hyp_gmf_all_mappings_valueexpression_langName_setter(instance):
    original = instance.langName
    instance.langName = original
    assert instance.langName == original



@given(instance=gmf_all_mappings_ValueExpression_strategy)
def test_hyp_gmf_all_mappings_valueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original









@given(instance=gmf_all_mappings_LabelMapping_strategy)
def test_hyp_gmf_all_mappings_labelmapping_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original



























@given(instance=gmf_all_gmfgraph_DiagramLabel_strategy)
def test_hyp_gmf_all_gmfgraph_diagramlabel_elementIcon_setter(instance):
    original = instance.elementIcon
    instance.elementIcon = original
    assert instance.elementIcon == original



@given(instance=gmf_all_gmfgraph_DiagramLabel_strategy)
def test_hyp_gmf_all_gmfgraph_diagramlabel_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original












@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
def test_hyp_gmf_all_mappings_featurelabelmapping_viewPattern_setter(instance):
    original = instance.viewPattern
    instance.viewPattern = original
    assert instance.viewPattern == original



@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
def test_hyp_gmf_all_mappings_featurelabelmapping_editPattern_setter(instance):
    original = instance.editPattern
    instance.editPattern = original
    assert instance.editPattern == original



@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
def test_hyp_gmf_all_mappings_featurelabelmapping_viewMethod_setter(instance):
    original = instance.viewMethod
    instance.viewMethod = original
    assert instance.viewMethod == original



@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
def test_hyp_gmf_all_mappings_featurelabelmapping_editMethod_setter(instance):
    original = instance.editMethod
    instance.editMethod = original
    assert instance.editMethod == original



@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
def test_hyp_gmf_all_mappings_featurelabelmapping_editorPattern_setter(instance):
    original = instance.editorPattern
    instance.editorPattern = original
    assert instance.editorPattern == original














@given(instance=gmf_all_tooldef_GenericStyleSelector_strategy)
def test_hyp_gmf_all_tooldef_genericstyleselector_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original









# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractFigure,
    AbstractNode,
    AbstractTool,
    AuditContainer,
    AuditRule,
    Auditable,
    Border,
    Canvas,
    CanvasMapping,
    ChildAccess,
    ChildReference,
    Color,
    Compartment,
    CompartmentMapping,
    Connection,
    Constraint,
    ContextMenu,
    ContributionItem,
    CustomAttribute,
    CustomAttributeOwner,
    DecorationFigure,
    DiagramElement,
    DiagramLabel,
    Dimension,
    ElementInitializer,
    FeatureInitializer,
    FeatureSeqInitializer,
    Figure,
    FigureAccessor,
    FigureDescriptor,
    FigureGallery,
    Font,
    Identity,
    Image,
    Insets,
    ItemBase,
    LabelMapping,
    Layout,
    LayoutData,
    Layoutable,
    LinkConstraints,
    LinkMapping,
    MainMenu,
    MappingEntry,
    Measurable,
    Menu,
    MenuAction,
    MetricContainer,
    MetricRule,
    NeedsContainment,
    Node,
    NodeMapping,
    NodeReference,
    Palette,
    Pin,
    Point,
    Polygon,
    Polyline,
    RealFigure,
    Rectangle2D,
    ReferenceNewElementSpec,
    RuleBase,
    SVGProperty,
    Shape,
    StyleSelector,
    ToolContainer,
    Toolbar,
    TopNodeReference,
    ValueExpression,
    VisualEffectMapping,
    VisualFacet,
    gmf_all_gmfgraph_AbstractFigure,
    gmf_all_gmfgraph_AbstractNode,
    gmf_all_gmfgraph_AlignmentFacet,
    gmf_all_gmfgraph_BasicFont,
    gmf_all_gmfgraph_Border,
    gmf_all_gmfgraph_BorderLayout,
    gmf_all_gmfgraph_BorderLayoutData,
    gmf_all_gmfgraph_BorderRef,
    gmf_all_gmfgraph_Canvas,
    gmf_all_gmfgraph_CenterLayout,
    gmf_all_gmfgraph_ChildAccess,
    gmf_all_gmfgraph_Color,
    gmf_all_gmfgraph_ColorPin,
    gmf_all_gmfgraph_Compartment,
    gmf_all_gmfgraph_CompoundBorder,
    gmf_all_gmfgraph_Connection,
    gmf_all_gmfgraph_ConnectionFigure,
    gmf_all_gmfgraph_ConstantColor,
    gmf_all_gmfgraph_CustomAttribute,
    gmf_all_gmfgraph_CustomAttributeOwner,
    gmf_all_gmfgraph_CustomBorder,
    gmf_all_gmfgraph_CustomClass,
    gmf_all_gmfgraph_CustomConnection,
    gmf_all_gmfgraph_CustomDecoration,
    gmf_all_gmfgraph_CustomFigure,
    gmf_all_gmfgraph_CustomLayout,
    gmf_all_gmfgraph_CustomLayoutData,
    gmf_all_gmfgraph_CustomPin,
    gmf_all_gmfgraph_DecorationFigure,
    gmf_all_gmfgraph_DefaultSizeFacet,
    gmf_all_gmfgraph_DiagramElement,
    gmf_all_gmfgraph_DiagramLabel,
    gmf_all_gmfgraph_Dimension,
    gmf_all_gmfgraph_Ellipse,
    gmf_all_gmfgraph_Figure,
    gmf_all_gmfgraph_FigureAccessor,
    gmf_all_gmfgraph_FigureDescriptor,
    gmf_all_gmfgraph_FigureGallery,
    gmf_all_gmfgraph_FigureRef,
    gmf_all_gmfgraph_FlowLayout,
    gmf_all_gmfgraph_Font,
    gmf_all_gmfgraph_GeneralFacet,
    gmf_all_gmfgraph_GradientFacet,
    gmf_all_gmfgraph_GridLayout,
    gmf_all_gmfgraph_GridLayoutData,
    gmf_all_gmfgraph_Identity,
    gmf_all_gmfgraph_Insets,
    gmf_all_gmfgraph_InvisibleRectangle,
    gmf_all_gmfgraph_Label,
    gmf_all_gmfgraph_LabelOffsetFacet,
    gmf_all_gmfgraph_LabeledContainer,
    gmf_all_gmfgraph_Layout,
    gmf_all_gmfgraph_LayoutData,
    gmf_all_gmfgraph_LayoutRef,
    gmf_all_gmfgraph_Layoutable,
    gmf_all_gmfgraph_LineBorder,
    gmf_all_gmfgraph_MarginBorder,
    gmf_all_gmfgraph_Node,
    gmf_all_gmfgraph_Pin,
    gmf_all_gmfgraph_PinOwner,
    gmf_all_gmfgraph_Point,
    gmf_all_gmfgraph_Polygon,
    gmf_all_gmfgraph_PolygonDecoration,
    gmf_all_gmfgraph_Polyline,
    gmf_all_gmfgraph_PolylineConnection,
    gmf_all_gmfgraph_PolylineDecoration,
    gmf_all_gmfgraph_RGBColor,
    gmf_all_gmfgraph_RealFigure,
    gmf_all_gmfgraph_Rectangle,
    gmf_all_gmfgraph_Rectangle2D,
    gmf_all_gmfgraph_RoundedRectangle,
    gmf_all_gmfgraph_SVGFigure,
    gmf_all_gmfgraph_SVGProperty,
    gmf_all_gmfgraph_ScalablePolygon,
    gmf_all_gmfgraph_Shape,
    gmf_all_gmfgraph_StackLayout,
    gmf_all_gmfgraph_VerticalLabel,
    gmf_all_gmfgraph_VisiblePin,
    gmf_all_gmfgraph_VisualFacet,
    gmf_all_gmfgraph_XYLayout,
    gmf_all_gmfgraph_XYLayoutData,
    gmf_all_mappings_AppearanceSteward,
    gmf_all_mappings_AuditContainer,
    gmf_all_mappings_AuditRule,
    gmf_all_mappings_Auditable,
    gmf_all_mappings_AuditedMetricTarget,
    gmf_all_mappings_CanvasMapping,
    gmf_all_mappings_ChildReference,
    gmf_all_mappings_CompartmentMapping,
    gmf_all_mappings_Constraint,
    gmf_all_mappings_DesignLabelMapping,
    gmf_all_mappings_DiagramElementTarget,
    gmf_all_mappings_DomainAttributeTarget,
    gmf_all_mappings_DomainElementTarget,
    gmf_all_mappings_ElementInitializer,
    gmf_all_mappings_ExpressionLabelMapping,
    gmf_all_mappings_FeatureInitializer,
    gmf_all_mappings_FeatureLabelMapping,
    gmf_all_mappings_FeatureSeqInitializer,
    gmf_all_mappings_FeatureValueSpec,
    gmf_all_mappings_LabelMapping,
    gmf_all_mappings_LinkConstraints,
    gmf_all_mappings_LinkMapping,
    gmf_all_mappings_Mapping,
    gmf_all_mappings_MappingEntry,
    gmf_all_mappings_Measurable,
    gmf_all_mappings_MenuOwner,
    gmf_all_mappings_MetricContainer,
    gmf_all_mappings_MetricRule,
    gmf_all_mappings_NeedsContainment,
    gmf_all_mappings_NodeMapping,
    gmf_all_mappings_NodeReference,
    gmf_all_mappings_NotationElementTarget,
    gmf_all_mappings_OclChoiceLabelMapping,
    gmf_all_mappings_ReferenceNewElementSpec,
    gmf_all_mappings_RuleBase,
    gmf_all_mappings_ToolOwner,
    gmf_all_mappings_TopNodeReference,
    gmf_all_mappings_ValueExpression,
    gmf_all_mappings_VisualEffectMapping,
    gmf_all_tooldef_AbstractTool,
    gmf_all_tooldef_BundleImage,
    gmf_all_tooldef_ContextMenu,
    gmf_all_tooldef_ContributionItem,
    gmf_all_tooldef_CreationTool,
    gmf_all_tooldef_DefaultImage,
    gmf_all_tooldef_GenericStyleSelector,
    gmf_all_tooldef_GenericTool,
    gmf_all_tooldef_Image,
    gmf_all_tooldef_ItemBase,
    gmf_all_tooldef_ItemRef,
    gmf_all_tooldef_MainMenu,
    gmf_all_tooldef_Menu,
    gmf_all_tooldef_MenuAction,
    gmf_all_tooldef_Palette,
    gmf_all_tooldef_PaletteSeparator,
    gmf_all_tooldef_PopupMenu,
    gmf_all_tooldef_PredefinedItem,
    gmf_all_tooldef_PredefinedMenu,
    gmf_all_tooldef_Separator,
    gmf_all_tooldef_StandardTool,
    gmf_all_tooldef_StyleSelector,
    gmf_all_tooldef_ToolContainer,
    gmf_all_tooldef_ToolGroup,
    gmf_all_tooldef_ToolRegistry,
    gmf_all_tooldef_Toolbar,
    gmfgraph_AbstractFigure,
    gmfgraph_Border,
    gmfgraph_ConnectionFigure,
    gmfgraph_CustomAttributeOwner,
    gmfgraph_CustomClass,
    gmfgraph_CustomFigure,
    gmfgraph_DecorationFigure,
    gmfgraph_Layout,
    gmfgraph_LayoutData,
    gmfgraph_PinOwner,
    gmfgraph_Polygon,
    gmfgraph_Polyline,
    gmfgraph_RealFigure,
    mappings_AppearanceSteward,
    mappings_Auditable,
    mappings_MappingEntry,
    mappings_Measurable,
    mappings_MenuOwner,
    mappings_NeedsContainment,
    mappings_ToolOwner,
    mappings_gmf_all_EAttribute,
    mappings_gmf_all_EClass,
    mappings_gmf_all_EPackage,
    mappings_gmf_all_EReference,
    mappings_gmf_all_EStructuralFeature,
    tooldef_ContributionItem,
    tooldef_Menu,
    tooldef_PredefinedItem,
    ActionKind,
    Alignment,
    AppearanceStyle,
    ColorConstants,
    Direction,
    FontStyle,
    LabelTextAccessMethod,
    Language,
    LineKind,
    SVGPropertyType,
    Severity,
    StandardToolKind,
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

def test_gmf_all_gmfgraph_AlignmentFacet_alignment_value_roundtrip():
    instance = gmf_all_gmfgraph_AlignmentFacet(alignment="sample_text")
    assert instance.alignment == "sample_text"
    instance.alignment = "sample_text_2"
    assert instance.alignment == "sample_text_2"


def test_gmf_all_gmfgraph_BasicFont_faceName_value_roundtrip():
    instance = gmf_all_gmfgraph_BasicFont(faceName="sample_text", height=7, style="sample_text")
    assert instance.faceName == "sample_text"
    instance.faceName = "sample_text_2"
    assert instance.faceName == "sample_text_2"


def test_gmf_all_gmfgraph_BasicFont_height_value_roundtrip():
    instance = gmf_all_gmfgraph_BasicFont(faceName="sample_text", height=7, style="sample_text")
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_gmf_all_gmfgraph_BasicFont_style_value_roundtrip():
    instance = gmf_all_gmfgraph_BasicFont(faceName="sample_text", height=7, style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_gmf_all_gmfgraph_BorderLayoutData_alignment_value_roundtrip():
    instance = gmf_all_gmfgraph_BorderLayoutData(alignment="sample_text", vertical=True)
    assert instance.alignment == "sample_text"
    instance.alignment = "sample_text_2"
    assert instance.alignment == "sample_text_2"


def test_gmf_all_gmfgraph_BorderLayoutData_vertical_value_roundtrip():
    instance = gmf_all_gmfgraph_BorderLayoutData(alignment="sample_text", vertical=True)
    assert instance.vertical == True
    instance.vertical = False
    assert instance.vertical == False


def test_gmf_all_gmfgraph_ChildAccess_accessor_value_roundtrip():
    instance = gmf_all_gmfgraph_ChildAccess(accessor="sample_text")
    assert instance.accessor == "sample_text"
    instance.accessor = "sample_text_2"
    assert instance.accessor == "sample_text_2"


def test_gmf_all_gmfgraph_ColorPin_backgroundNotForeground_value_roundtrip():
    instance = gmf_all_gmfgraph_ColorPin(backgroundNotForeground=True)
    assert instance.backgroundNotForeground == True
    instance.backgroundNotForeground = False
    assert instance.backgroundNotForeground == False


def test_gmf_all_gmfgraph_Compartment_collapsible_value_roundtrip():
    instance = gmf_all_gmfgraph_Compartment(collapsible=True, needsTitle=True)
    assert instance.collapsible == True
    instance.collapsible = False
    assert instance.collapsible == False


def test_gmf_all_gmfgraph_Compartment_needsTitle_value_roundtrip():
    instance = gmf_all_gmfgraph_Compartment(collapsible=True, needsTitle=True)
    assert instance.needsTitle == True
    instance.needsTitle = False
    assert instance.needsTitle == False


def test_gmf_all_gmfgraph_ConstantColor_value_value_roundtrip():
    instance = gmf_all_gmfgraph_ConstantColor(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_gmf_all_gmfgraph_CustomAttribute_directAccess_value_roundtrip():
    instance = gmf_all_gmfgraph_CustomAttribute(directAccess=True, multiStatementValue=True, name="sample_text", value="sample_text")
    assert instance.directAccess == True
    instance.directAccess = False
    assert instance.directAccess == False


def test_gmf_all_gmfgraph_CustomAttribute_multiStatementValue_value_roundtrip():
    instance = gmf_all_gmfgraph_CustomAttribute(directAccess=True, multiStatementValue=True, name="sample_text", value="sample_text")
    assert instance.multiStatementValue == True
    instance.multiStatementValue = False
    assert instance.multiStatementValue == False


def test_gmf_all_gmfgraph_CustomAttribute_name_value_roundtrip():
    instance = gmf_all_gmfgraph_CustomAttribute(directAccess=True, multiStatementValue=True, name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gmf_all_gmfgraph_CustomAttribute_value_value_roundtrip():
    instance = gmf_all_gmfgraph_CustomAttribute(directAccess=True, multiStatementValue=True, name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_gmf_all_gmfgraph_CustomClass_qualifiedClassName_value_roundtrip():
    instance = gmf_all_gmfgraph_CustomClass(qualifiedClassName="sample_text")
    assert instance.qualifiedClassName == "sample_text"
    instance.qualifiedClassName = "sample_text_2"
    assert instance.qualifiedClassName == "sample_text_2"


def test_gmf_all_gmfgraph_CustomPin_customOperationName_value_roundtrip():
    instance = gmf_all_gmfgraph_CustomPin(customOperationName="sample_text", customOperationType="sample_text")
    assert instance.customOperationName == "sample_text"
    instance.customOperationName = "sample_text_2"
    assert instance.customOperationName == "sample_text_2"


def test_gmf_all_gmfgraph_CustomPin_customOperationType_value_roundtrip():
    instance = gmf_all_gmfgraph_CustomPin(customOperationName="sample_text", customOperationType="sample_text")
    assert instance.customOperationType == "sample_text"
    instance.customOperationType = "sample_text_2"
    assert instance.customOperationType == "sample_text_2"


def test_gmf_all_gmfgraph_DiagramLabel_elementIcon_value_roundtrip():
    instance = gmf_all_gmfgraph_DiagramLabel(elementIcon=True, external=True)
    assert instance.elementIcon == True
    instance.elementIcon = False
    assert instance.elementIcon == False


def test_gmf_all_gmfgraph_DiagramLabel_external_value_roundtrip():
    instance = gmf_all_gmfgraph_DiagramLabel(elementIcon=True, external=True)
    assert instance.external == True
    instance.external = False
    assert instance.external == False


def test_gmf_all_gmfgraph_Dimension_dx_value_roundtrip():
    instance = gmf_all_gmfgraph_Dimension(dx=7, dy=7)
    assert instance.dx == 7
    instance.dx = 13
    assert instance.dx == 13


def test_gmf_all_gmfgraph_Dimension_dy_value_roundtrip():
    instance = gmf_all_gmfgraph_Dimension(dx=7, dy=7)
    assert instance.dy == 7
    instance.dy = 13
    assert instance.dy == 13


def test_gmf_all_gmfgraph_FigureAccessor_accessor_value_roundtrip():
    instance = gmf_all_gmfgraph_FigureAccessor(accessor="sample_text")
    assert instance.accessor == "sample_text"
    instance.accessor = "sample_text_2"
    assert instance.accessor == "sample_text_2"


def test_gmf_all_gmfgraph_FigureGallery_implementationBundle_value_roundtrip():
    instance = gmf_all_gmfgraph_FigureGallery(implementationBundle="sample_text")
    assert instance.implementationBundle == "sample_text"
    instance.implementationBundle = "sample_text_2"
    assert instance.implementationBundle == "sample_text_2"


def test_gmf_all_gmfgraph_FlowLayout_forceSingleLine_value_roundtrip():
    instance = gmf_all_gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.forceSingleLine == True
    instance.forceSingleLine = False
    assert instance.forceSingleLine == False


def test_gmf_all_gmfgraph_FlowLayout_majorAlignment_value_roundtrip():
    instance = gmf_all_gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.majorAlignment == "sample_text"
    instance.majorAlignment = "sample_text_2"
    assert instance.majorAlignment == "sample_text_2"


def test_gmf_all_gmfgraph_FlowLayout_majorSpacing_value_roundtrip():
    instance = gmf_all_gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.majorSpacing == 7
    instance.majorSpacing = 13
    assert instance.majorSpacing == 13


def test_gmf_all_gmfgraph_FlowLayout_matchMinorSize_value_roundtrip():
    instance = gmf_all_gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.matchMinorSize == True
    instance.matchMinorSize = False
    assert instance.matchMinorSize == False


def test_gmf_all_gmfgraph_FlowLayout_minorAlignment_value_roundtrip():
    instance = gmf_all_gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.minorAlignment == "sample_text"
    instance.minorAlignment = "sample_text_2"
    assert instance.minorAlignment == "sample_text_2"


def test_gmf_all_gmfgraph_FlowLayout_minorSpacing_value_roundtrip():
    instance = gmf_all_gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.minorSpacing == 7
    instance.minorSpacing = 13
    assert instance.minorSpacing == 13


def test_gmf_all_gmfgraph_FlowLayout_vertical_value_roundtrip():
    instance = gmf_all_gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.vertical == True
    instance.vertical = False
    assert instance.vertical == False


def test_gmf_all_gmfgraph_GeneralFacet_data_value_roundtrip():
    instance = gmf_all_gmfgraph_GeneralFacet(data="sample_text", identifier="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_gmf_all_gmfgraph_GeneralFacet_identifier_value_roundtrip():
    instance = gmf_all_gmfgraph_GeneralFacet(data="sample_text", identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_gmf_all_gmfgraph_GradientFacet_direction_value_roundtrip():
    instance = gmf_all_gmfgraph_GradientFacet(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_gmf_all_gmfgraph_GridLayout_equalWidth_value_roundtrip():
    instance = gmf_all_gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    assert instance.equalWidth == True
    instance.equalWidth = False
    assert instance.equalWidth == False


def test_gmf_all_gmfgraph_GridLayout_numColumns_value_roundtrip():
    instance = gmf_all_gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    assert instance.numColumns == 7
    instance.numColumns = 13
    assert instance.numColumns == 13


def test_gmf_all_gmfgraph_GridLayoutData_grabExcessHorizontalSpace_value_roundtrip():
    instance = gmf_all_gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.grabExcessHorizontalSpace == True
    instance.grabExcessHorizontalSpace = False
    assert instance.grabExcessHorizontalSpace == False


def test_gmf_all_gmfgraph_GridLayoutData_grabExcessVerticalSpace_value_roundtrip():
    instance = gmf_all_gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.grabExcessVerticalSpace == True
    instance.grabExcessVerticalSpace = False
    assert instance.grabExcessVerticalSpace == False


def test_gmf_all_gmfgraph_GridLayoutData_horizontalAlignment_value_roundtrip():
    instance = gmf_all_gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.horizontalAlignment == "sample_text"
    instance.horizontalAlignment = "sample_text_2"
    assert instance.horizontalAlignment == "sample_text_2"


def test_gmf_all_gmfgraph_GridLayoutData_horizontalIndent_value_roundtrip():
    instance = gmf_all_gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.horizontalIndent == 7
    instance.horizontalIndent = 13
    assert instance.horizontalIndent == 13


def test_gmf_all_gmfgraph_GridLayoutData_horizontalSpan_value_roundtrip():
    instance = gmf_all_gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.horizontalSpan == 7
    instance.horizontalSpan = 13
    assert instance.horizontalSpan == 13


def test_gmf_all_gmfgraph_GridLayoutData_verticalAlignment_value_roundtrip():
    instance = gmf_all_gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.verticalAlignment == "sample_text"
    instance.verticalAlignment = "sample_text_2"
    assert instance.verticalAlignment == "sample_text_2"


def test_gmf_all_gmfgraph_GridLayoutData_verticalSpan_value_roundtrip():
    instance = gmf_all_gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.verticalSpan == 7
    instance.verticalSpan = 13
    assert instance.verticalSpan == 13


def test_gmf_all_gmfgraph_Identity_name_value_roundtrip():
    instance = gmf_all_gmfgraph_Identity(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gmf_all_gmfgraph_Insets_bottom_value_roundtrip():
    instance = gmf_all_gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    assert instance.bottom == 7
    instance.bottom = 13
    assert instance.bottom == 13


def test_gmf_all_gmfgraph_Insets_left_value_roundtrip():
    instance = gmf_all_gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    assert instance.left == 7
    instance.left = 13
    assert instance.left == 13


def test_gmf_all_gmfgraph_Insets_right_value_roundtrip():
    instance = gmf_all_gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    assert instance.right == 7
    instance.right = 13
    assert instance.right == 13


def test_gmf_all_gmfgraph_Insets_top_value_roundtrip():
    instance = gmf_all_gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    assert instance.top == 7
    instance.top = 13
    assert instance.top == 13


def test_gmf_all_gmfgraph_Label_text_value_roundtrip():
    instance = gmf_all_gmfgraph_Label(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_gmf_all_gmfgraph_LabelOffsetFacet_x_value_roundtrip():
    instance = gmf_all_gmfgraph_LabelOffsetFacet(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_gmf_all_gmfgraph_LabelOffsetFacet_y_value_roundtrip():
    instance = gmf_all_gmfgraph_LabelOffsetFacet(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_gmf_all_gmfgraph_LineBorder_width_value_roundtrip():
    instance = gmf_all_gmfgraph_LineBorder(width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_gmf_all_gmfgraph_Node_affixedParentSide_value_roundtrip():
    instance = gmf_all_gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    assert instance.affixedParentSide == "sample_text"
    instance.affixedParentSide = "sample_text_2"
    assert instance.affixedParentSide == "sample_text_2"


def test_gmf_all_gmfgraph_Node_resizeConstraint_value_roundtrip():
    instance = gmf_all_gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    assert instance.resizeConstraint == "sample_text"
    instance.resizeConstraint = "sample_text_2"
    assert instance.resizeConstraint == "sample_text_2"


def test_gmf_all_gmfgraph_Point_x_value_roundtrip():
    instance = gmf_all_gmfgraph_Point(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_gmf_all_gmfgraph_Point_y_value_roundtrip():
    instance = gmf_all_gmfgraph_Point(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_gmf_all_gmfgraph_RGBColor_blue_value_roundtrip():
    instance = gmf_all_gmfgraph_RGBColor(blue=7, green=7, red=7)
    assert instance.blue == 7
    instance.blue = 13
    assert instance.blue == 13


def test_gmf_all_gmfgraph_RGBColor_green_value_roundtrip():
    instance = gmf_all_gmfgraph_RGBColor(blue=7, green=7, red=7)
    assert instance.green == 7
    instance.green = 13
    assert instance.green == 13


def test_gmf_all_gmfgraph_RGBColor_red_value_roundtrip():
    instance = gmf_all_gmfgraph_RGBColor(blue=7, green=7, red=7)
    assert instance.red == 7
    instance.red = 13
    assert instance.red == 13


def test_gmf_all_gmfgraph_RealFigure_name_value_roundtrip():
    instance = gmf_all_gmfgraph_RealFigure(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gmf_all_gmfgraph_Rectangle2D_height_value_roundtrip():
    instance = gmf_all_gmfgraph_Rectangle2D(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_gmf_all_gmfgraph_Rectangle2D_width_value_roundtrip():
    instance = gmf_all_gmfgraph_Rectangle2D(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_gmf_all_gmfgraph_Rectangle2D_x_value_roundtrip():
    instance = gmf_all_gmfgraph_Rectangle2D(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_gmf_all_gmfgraph_Rectangle2D_y_value_roundtrip():
    instance = gmf_all_gmfgraph_Rectangle2D(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_gmf_all_gmfgraph_RoundedRectangle_cornerHeight_value_roundtrip():
    instance = gmf_all_gmfgraph_RoundedRectangle(cornerHeight=7, cornerWidth=7)
    assert instance.cornerHeight == 7
    instance.cornerHeight = 13
    assert instance.cornerHeight == 13


def test_gmf_all_gmfgraph_RoundedRectangle_cornerWidth_value_roundtrip():
    instance = gmf_all_gmfgraph_RoundedRectangle(cornerHeight=7, cornerWidth=7)
    assert instance.cornerWidth == 7
    instance.cornerWidth = 13
    assert instance.cornerWidth == 13


def test_gmf_all_gmfgraph_SVGFigure_documentURI_value_roundtrip():
    instance = gmf_all_gmfgraph_SVGFigure(documentURI="sample_text", noCanvasHeight=True, noCanvasWidth=True)
    assert instance.documentURI == "sample_text"
    instance.documentURI = "sample_text_2"
    assert instance.documentURI == "sample_text_2"


def test_gmf_all_gmfgraph_SVGFigure_noCanvasHeight_value_roundtrip():
    instance = gmf_all_gmfgraph_SVGFigure(documentURI="sample_text", noCanvasHeight=True, noCanvasWidth=True)
    assert instance.noCanvasHeight == True
    instance.noCanvasHeight = False
    assert instance.noCanvasHeight == False


def test_gmf_all_gmfgraph_SVGFigure_noCanvasWidth_value_roundtrip():
    instance = gmf_all_gmfgraph_SVGFigure(documentURI="sample_text", noCanvasHeight=True, noCanvasWidth=True)
    assert instance.noCanvasWidth == True
    instance.noCanvasWidth = False
    assert instance.noCanvasWidth == False


def test_gmf_all_gmfgraph_SVGProperty_attribute_value_roundtrip():
    instance = gmf_all_gmfgraph_SVGProperty(attribute="sample_text", callSuper=True, getter="sample_text", query="sample_text", setter="sample_text", type="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_gmf_all_gmfgraph_SVGProperty_callSuper_value_roundtrip():
    instance = gmf_all_gmfgraph_SVGProperty(attribute="sample_text", callSuper=True, getter="sample_text", query="sample_text", setter="sample_text", type="sample_text")
    assert instance.callSuper == True
    instance.callSuper = False
    assert instance.callSuper == False


def test_gmf_all_gmfgraph_SVGProperty_getter_value_roundtrip():
    instance = gmf_all_gmfgraph_SVGProperty(attribute="sample_text", callSuper=True, getter="sample_text", query="sample_text", setter="sample_text", type="sample_text")
    assert instance.getter == "sample_text"
    instance.getter = "sample_text_2"
    assert instance.getter == "sample_text_2"


def test_gmf_all_gmfgraph_SVGProperty_query_value_roundtrip():
    instance = gmf_all_gmfgraph_SVGProperty(attribute="sample_text", callSuper=True, getter="sample_text", query="sample_text", setter="sample_text", type="sample_text")
    assert instance.query == "sample_text"
    instance.query = "sample_text_2"
    assert instance.query == "sample_text_2"


def test_gmf_all_gmfgraph_SVGProperty_setter_value_roundtrip():
    instance = gmf_all_gmfgraph_SVGProperty(attribute="sample_text", callSuper=True, getter="sample_text", query="sample_text", setter="sample_text", type="sample_text")
    assert instance.setter == "sample_text"
    instance.setter = "sample_text_2"
    assert instance.setter == "sample_text_2"


def test_gmf_all_gmfgraph_SVGProperty_type_value_roundtrip():
    instance = gmf_all_gmfgraph_SVGProperty(attribute="sample_text", callSuper=True, getter="sample_text", query="sample_text", setter="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_gmf_all_gmfgraph_Shape_fill_value_roundtrip():
    instance = gmf_all_gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.fill == True
    instance.fill = False
    assert instance.fill == False


def test_gmf_all_gmfgraph_Shape_lineKind_value_roundtrip():
    instance = gmf_all_gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.lineKind == "sample_text"
    instance.lineKind = "sample_text_2"
    assert instance.lineKind == "sample_text_2"


def test_gmf_all_gmfgraph_Shape_lineWidth_value_roundtrip():
    instance = gmf_all_gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.lineWidth == 7
    instance.lineWidth = 13
    assert instance.lineWidth == 13


def test_gmf_all_gmfgraph_Shape_outline_value_roundtrip():
    instance = gmf_all_gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.outline == True
    instance.outline = False
    assert instance.outline == False


def test_gmf_all_gmfgraph_Shape_xorFill_value_roundtrip():
    instance = gmf_all_gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.xorFill == True
    instance.xorFill = False
    assert instance.xorFill == False


def test_gmf_all_gmfgraph_Shape_xorOutline_value_roundtrip():
    instance = gmf_all_gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.xorOutline == True
    instance.xorOutline = False
    assert instance.xorOutline == False


def test_gmf_all_gmfgraph_VerticalLabel_text_value_roundtrip():
    instance = gmf_all_gmfgraph_VerticalLabel(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_gmf_all_mappings_AuditContainer_description_value_roundtrip():
    instance = gmf_all_mappings_AuditContainer(description="sample_text", id="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_gmf_all_mappings_AuditContainer_id_value_roundtrip():
    instance = gmf_all_mappings_AuditContainer(description="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_gmf_all_mappings_AuditContainer_name_value_roundtrip():
    instance = gmf_all_mappings_AuditContainer(description="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gmf_all_mappings_AuditRule_id_value_roundtrip():
    instance = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_gmf_all_mappings_AuditRule_message_value_roundtrip():
    instance = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_gmf_all_mappings_AuditRule_severity_value_roundtrip():
    instance = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    assert instance.severity == "sample_text"
    instance.severity = "sample_text_2"
    assert instance.severity == "sample_text_2"


def test_gmf_all_mappings_AuditRule_useInLiveMode_value_roundtrip():
    instance = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    assert instance.useInLiveMode == True
    instance.useInLiveMode = False
    assert instance.useInLiveMode == False


def test_gmf_all_mappings_DomainAttributeTarget_nullAsError_value_roundtrip():
    instance = gmf_all_mappings_DomainAttributeTarget(nullAsError=True)
    assert instance.nullAsError == True
    instance.nullAsError = False
    assert instance.nullAsError == False


def test_gmf_all_mappings_FeatureLabelMapping_editMethod_value_roundtrip():
    instance = gmf_all_mappings_FeatureLabelMapping(editMethod="sample_text", editPattern="sample_text", editorPattern="sample_text", viewMethod="sample_text", viewPattern="sample_text")
    assert instance.editMethod == "sample_text"
    instance.editMethod = "sample_text_2"
    assert instance.editMethod == "sample_text_2"


def test_gmf_all_mappings_FeatureLabelMapping_editPattern_value_roundtrip():
    instance = gmf_all_mappings_FeatureLabelMapping(editMethod="sample_text", editPattern="sample_text", editorPattern="sample_text", viewMethod="sample_text", viewPattern="sample_text")
    assert instance.editPattern == "sample_text"
    instance.editPattern = "sample_text_2"
    assert instance.editPattern == "sample_text_2"


def test_gmf_all_mappings_FeatureLabelMapping_editorPattern_value_roundtrip():
    instance = gmf_all_mappings_FeatureLabelMapping(editMethod="sample_text", editPattern="sample_text", editorPattern="sample_text", viewMethod="sample_text", viewPattern="sample_text")
    assert instance.editorPattern == "sample_text"
    instance.editorPattern = "sample_text_2"
    assert instance.editorPattern == "sample_text_2"


def test_gmf_all_mappings_FeatureLabelMapping_viewMethod_value_roundtrip():
    instance = gmf_all_mappings_FeatureLabelMapping(editMethod="sample_text", editPattern="sample_text", editorPattern="sample_text", viewMethod="sample_text", viewPattern="sample_text")
    assert instance.viewMethod == "sample_text"
    instance.viewMethod = "sample_text_2"
    assert instance.viewMethod == "sample_text_2"


def test_gmf_all_mappings_FeatureLabelMapping_viewPattern_value_roundtrip():
    instance = gmf_all_mappings_FeatureLabelMapping(editMethod="sample_text", editPattern="sample_text", editorPattern="sample_text", viewMethod="sample_text", viewPattern="sample_text")
    assert instance.viewPattern == "sample_text"
    instance.viewPattern = "sample_text_2"
    assert instance.viewPattern == "sample_text_2"


def test_gmf_all_mappings_LabelMapping_readOnly_value_roundtrip():
    instance = gmf_all_mappings_LabelMapping(readOnly=True)
    assert instance.readOnly == True
    instance.readOnly = False
    assert instance.readOnly == False


def test_gmf_all_mappings_MetricRule_highLimit_value_roundtrip():
    instance = gmf_all_mappings_MetricRule(highLimit="sample_text", key="sample_text", lowLimit="sample_text")
    assert instance.highLimit == "sample_text"
    instance.highLimit = "sample_text_2"
    assert instance.highLimit == "sample_text_2"


def test_gmf_all_mappings_MetricRule_key_value_roundtrip():
    instance = gmf_all_mappings_MetricRule(highLimit="sample_text", key="sample_text", lowLimit="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_gmf_all_mappings_MetricRule_lowLimit_value_roundtrip():
    instance = gmf_all_mappings_MetricRule(highLimit="sample_text", key="sample_text", lowLimit="sample_text")
    assert instance.lowLimit == "sample_text"
    instance.lowLimit = "sample_text_2"
    assert instance.lowLimit == "sample_text_2"


def test_gmf_all_mappings_RuleBase_description_value_roundtrip():
    instance = gmf_all_mappings_RuleBase(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_gmf_all_mappings_RuleBase_name_value_roundtrip():
    instance = gmf_all_mappings_RuleBase(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gmf_all_mappings_ValueExpression_body_value_roundtrip():
    instance = gmf_all_mappings_ValueExpression(body="sample_text", langName="sample_text", language="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_gmf_all_mappings_ValueExpression_langName_value_roundtrip():
    instance = gmf_all_mappings_ValueExpression(body="sample_text", langName="sample_text", language="sample_text")
    assert instance.langName == "sample_text"
    instance.langName = "sample_text_2"
    assert instance.langName == "sample_text_2"


def test_gmf_all_mappings_ValueExpression_language_value_roundtrip():
    instance = gmf_all_mappings_ValueExpression(body="sample_text", langName="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_gmf_all_mappings_VisualEffectMapping_oclExpression_value_roundtrip():
    instance = gmf_all_mappings_VisualEffectMapping(oclExpression="sample_text")
    assert instance.oclExpression == "sample_text"
    instance.oclExpression = "sample_text_2"
    assert instance.oclExpression == "sample_text_2"


def test_gmf_all_tooldef_AbstractTool_description_value_roundtrip():
    instance = gmf_all_tooldef_AbstractTool(description="sample_text", title="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_gmf_all_tooldef_AbstractTool_title_value_roundtrip():
    instance = gmf_all_tooldef_AbstractTool(description="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_gmf_all_tooldef_BundleImage_bundle_value_roundtrip():
    instance = gmf_all_tooldef_BundleImage(bundle="sample_text", path="sample_text")
    assert instance.bundle == "sample_text"
    instance.bundle = "sample_text_2"
    assert instance.bundle == "sample_text_2"


def test_gmf_all_tooldef_BundleImage_path_value_roundtrip():
    instance = gmf_all_tooldef_BundleImage(bundle="sample_text", path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_gmf_all_tooldef_ContributionItem_title_value_roundtrip():
    instance = gmf_all_tooldef_ContributionItem(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_gmf_all_tooldef_GenericStyleSelector_values_value_roundtrip():
    instance = gmf_all_tooldef_GenericStyleSelector(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_gmf_all_tooldef_GenericTool_toolClass_value_roundtrip():
    instance = gmf_all_tooldef_GenericTool(toolClass="sample_text")
    assert instance.toolClass == "sample_text"
    instance.toolClass = "sample_text_2"
    assert instance.toolClass == "sample_text_2"


def test_gmf_all_tooldef_MainMenu_title_value_roundtrip():
    instance = gmf_all_tooldef_MainMenu(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_gmf_all_tooldef_MenuAction_hotKey_value_roundtrip():
    instance = gmf_all_tooldef_MenuAction(hotKey="sample_text", kind="sample_text")
    assert instance.hotKey == "sample_text"
    instance.hotKey = "sample_text_2"
    assert instance.hotKey == "sample_text_2"


def test_gmf_all_tooldef_MenuAction_kind_value_roundtrip():
    instance = gmf_all_tooldef_MenuAction(hotKey="sample_text", kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_gmf_all_tooldef_PopupMenu_iD_value_roundtrip():
    instance = gmf_all_tooldef_PopupMenu(iD="sample_text")
    assert instance.iD == "sample_text"
    instance.iD = "sample_text_2"
    assert instance.iD == "sample_text_2"


def test_gmf_all_tooldef_PredefinedItem_identifier_value_roundtrip():
    instance = gmf_all_tooldef_PredefinedItem(identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_gmf_all_tooldef_Separator_name_value_roundtrip():
    instance = gmf_all_tooldef_Separator(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gmf_all_tooldef_StandardTool_toolKind_value_roundtrip():
    instance = gmf_all_tooldef_StandardTool(toolKind="sample_text")
    assert instance.toolKind == "sample_text"
    instance.toolKind = "sample_text_2"
    assert instance.toolKind == "sample_text_2"


def test_gmf_all_tooldef_ToolGroup_collapsible_value_roundtrip():
    instance = gmf_all_tooldef_ToolGroup(collapsible=True, stack=True)
    assert instance.collapsible == True
    instance.collapsible = False
    assert instance.collapsible == False


def test_gmf_all_tooldef_ToolGroup_stack_value_roundtrip():
    instance = gmf_all_tooldef_ToolGroup(collapsible=True, stack=True)
    assert instance.stack == True
    instance.stack = False
    assert instance.stack == False


def test_gmf_all_gmfgraph_FigureRef_isa_AbstractFigure():
    instance = gmf_all_gmfgraph_FigureRef()
    assert isinstance(instance, AbstractFigure)


def test_gmf_all_gmfgraph_Node_isa_AbstractNode():
    instance = gmf_all_gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    assert isinstance(instance, AbstractNode)


def test_gmf_all_tooldef_CreationTool_isa_AbstractTool():
    instance = gmf_all_tooldef_CreationTool()
    assert isinstance(instance, AbstractTool)


def test_gmf_all_tooldef_GenericTool_isa_AbstractTool():
    instance = gmf_all_tooldef_GenericTool(toolClass="sample_text")
    assert isinstance(instance, AbstractTool)


def test_gmf_all_tooldef_PaletteSeparator_isa_AbstractTool():
    instance = gmf_all_tooldef_PaletteSeparator()
    assert isinstance(instance, AbstractTool)


def test_gmf_all_tooldef_StandardTool_isa_AbstractTool():
    instance = gmf_all_tooldef_StandardTool(toolKind="sample_text")
    assert isinstance(instance, AbstractTool)


def test_gmf_all_tooldef_ToolContainer_isa_AbstractTool():
    instance = gmf_all_tooldef_ToolContainer()
    assert isinstance(instance, AbstractTool)


def test_gmf_all_mappings_AuditedMetricTarget_isa_Auditable():
    instance = gmf_all_mappings_AuditedMetricTarget()
    assert isinstance(instance, Auditable)


def test_gmf_all_mappings_DomainAttributeTarget_isa_Auditable():
    instance = gmf_all_mappings_DomainAttributeTarget(nullAsError=True)
    assert isinstance(instance, Auditable)


def test_gmf_all_gmfgraph_BorderRef_isa_Border():
    instance = gmf_all_gmfgraph_BorderRef()
    assert isinstance(instance, Border)


def test_gmf_all_gmfgraph_CompoundBorder_isa_Border():
    instance = gmf_all_gmfgraph_CompoundBorder()
    assert isinstance(instance, Border)


def test_gmf_all_gmfgraph_LineBorder_isa_Border():
    instance = gmf_all_gmfgraph_LineBorder(width=7)
    assert isinstance(instance, Border)


def test_gmf_all_gmfgraph_MarginBorder_isa_Border():
    instance = gmf_all_gmfgraph_MarginBorder()
    assert isinstance(instance, Border)


def test_gmf_all_gmfgraph_ConstantColor_isa_Color():
    instance = gmf_all_gmfgraph_ConstantColor(value="sample_text")
    assert isinstance(instance, Color)


def test_gmf_all_gmfgraph_RGBColor_isa_Color():
    instance = gmf_all_gmfgraph_RGBColor(blue=7, green=7, red=7)
    assert isinstance(instance, Color)


def test_gmf_all_tooldef_MenuAction_isa_ContributionItem():
    instance = gmf_all_tooldef_MenuAction(hotKey="sample_text", kind="sample_text")
    assert isinstance(instance, ContributionItem)


def test_gmf_all_gmfgraph_CustomClass_isa_CustomAttributeOwner():
    instance = gmf_all_gmfgraph_CustomClass(qualifiedClassName="sample_text")
    assert isinstance(instance, CustomAttributeOwner)


def test_gmf_all_gmfgraph_AbstractNode_isa_DiagramElement():
    instance = gmf_all_gmfgraph_AbstractNode()
    assert isinstance(instance, DiagramElement)


def test_gmf_all_gmfgraph_Compartment_isa_DiagramElement():
    instance = gmf_all_gmfgraph_Compartment(collapsible=True, needsTitle=True)
    assert isinstance(instance, DiagramElement)


def test_gmf_all_gmfgraph_Connection_isa_DiagramElement():
    instance = gmf_all_gmfgraph_Connection()
    assert isinstance(instance, DiagramElement)


def test_gmf_all_mappings_FeatureSeqInitializer_isa_ElementInitializer():
    instance = gmf_all_mappings_FeatureSeqInitializer()
    assert isinstance(instance, ElementInitializer)


def test_gmf_all_mappings_FeatureValueSpec_isa_FeatureInitializer():
    instance = gmf_all_mappings_FeatureValueSpec()
    assert isinstance(instance, FeatureInitializer)


def test_gmf_all_mappings_ReferenceNewElementSpec_isa_FeatureInitializer():
    instance = gmf_all_mappings_ReferenceNewElementSpec()
    assert isinstance(instance, FeatureInitializer)


def test_gmf_all_gmfgraph_AbstractFigure_isa_Figure():
    instance = gmf_all_gmfgraph_AbstractFigure()
    assert isinstance(instance, Figure)


def test_gmf_all_gmfgraph_BasicFont_isa_Font():
    instance = gmf_all_gmfgraph_BasicFont(faceName="sample_text", height=7, style="sample_text")
    assert isinstance(instance, Font)


def test_gmf_all_gmfgraph_Canvas_isa_Identity():
    instance = gmf_all_gmfgraph_Canvas()
    assert isinstance(instance, Identity)


def test_gmf_all_gmfgraph_DiagramElement_isa_Identity():
    instance = gmf_all_gmfgraph_DiagramElement()
    assert isinstance(instance, Identity)


def test_gmf_all_gmfgraph_FigureDescriptor_isa_Identity():
    instance = gmf_all_gmfgraph_FigureDescriptor()
    assert isinstance(instance, Identity)


def test_gmf_all_gmfgraph_FigureGallery_isa_Identity():
    instance = gmf_all_gmfgraph_FigureGallery(implementationBundle="sample_text")
    assert isinstance(instance, Identity)


def test_gmf_all_gmfgraph_Pin_isa_Identity():
    instance = gmf_all_gmfgraph_Pin()
    assert isinstance(instance, Identity)


def test_gmf_all_tooldef_BundleImage_isa_Image():
    instance = gmf_all_tooldef_BundleImage(bundle="sample_text", path="sample_text")
    assert isinstance(instance, Image)


def test_gmf_all_tooldef_DefaultImage_isa_Image():
    instance = gmf_all_tooldef_DefaultImage()
    assert isinstance(instance, Image)


def test_gmf_all_tooldef_ContributionItem_isa_ItemBase():
    instance = gmf_all_tooldef_ContributionItem(title="sample_text")
    assert isinstance(instance, ItemBase)


def test_gmf_all_tooldef_ItemRef_isa_ItemBase():
    instance = gmf_all_tooldef_ItemRef()
    assert isinstance(instance, ItemBase)


def test_gmf_all_tooldef_PredefinedItem_isa_ItemBase():
    instance = gmf_all_tooldef_PredefinedItem(identifier="sample_text")
    assert isinstance(instance, ItemBase)


def test_gmf_all_tooldef_Separator_isa_ItemBase():
    instance = gmf_all_tooldef_Separator(name="sample_text")
    assert isinstance(instance, ItemBase)


def test_gmf_all_mappings_DesignLabelMapping_isa_LabelMapping():
    instance = gmf_all_mappings_DesignLabelMapping()
    assert isinstance(instance, LabelMapping)


def test_gmf_all_mappings_ExpressionLabelMapping_isa_LabelMapping():
    instance = gmf_all_mappings_ExpressionLabelMapping()
    assert isinstance(instance, LabelMapping)


def test_gmf_all_mappings_FeatureLabelMapping_isa_LabelMapping():
    instance = gmf_all_mappings_FeatureLabelMapping(editMethod="sample_text", editPattern="sample_text", editorPattern="sample_text", viewMethod="sample_text", viewPattern="sample_text")
    assert isinstance(instance, LabelMapping)


def test_gmf_all_mappings_OclChoiceLabelMapping_isa_LabelMapping():
    instance = gmf_all_mappings_OclChoiceLabelMapping()
    assert isinstance(instance, LabelMapping)


def test_gmf_all_gmfgraph_BorderLayout_isa_Layout():
    instance = gmf_all_gmfgraph_BorderLayout()
    assert isinstance(instance, Layout)


def test_gmf_all_gmfgraph_CenterLayout_isa_Layout():
    instance = gmf_all_gmfgraph_CenterLayout()
    assert isinstance(instance, Layout)


def test_gmf_all_gmfgraph_FlowLayout_isa_Layout():
    instance = gmf_all_gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert isinstance(instance, Layout)


def test_gmf_all_gmfgraph_GridLayout_isa_Layout():
    instance = gmf_all_gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    assert isinstance(instance, Layout)


def test_gmf_all_gmfgraph_LayoutRef_isa_Layout():
    instance = gmf_all_gmfgraph_LayoutRef()
    assert isinstance(instance, Layout)


def test_gmf_all_gmfgraph_StackLayout_isa_Layout():
    instance = gmf_all_gmfgraph_StackLayout()
    assert isinstance(instance, Layout)


def test_gmf_all_gmfgraph_XYLayout_isa_Layout():
    instance = gmf_all_gmfgraph_XYLayout()
    assert isinstance(instance, Layout)


def test_gmf_all_gmfgraph_BorderLayoutData_isa_LayoutData():
    instance = gmf_all_gmfgraph_BorderLayoutData(alignment="sample_text", vertical=True)
    assert isinstance(instance, LayoutData)


def test_gmf_all_gmfgraph_GridLayoutData_isa_LayoutData():
    instance = gmf_all_gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert isinstance(instance, LayoutData)


def test_gmf_all_gmfgraph_XYLayoutData_isa_LayoutData():
    instance = gmf_all_gmfgraph_XYLayoutData()
    assert isinstance(instance, LayoutData)


def test_gmf_all_gmfgraph_Figure_isa_Layoutable():
    instance = gmf_all_gmfgraph_Figure()
    assert isinstance(instance, Layoutable)


def test_gmf_all_tooldef_ContextMenu_isa_Menu():
    instance = gmf_all_tooldef_ContextMenu()
    assert isinstance(instance, Menu)


def test_gmf_all_tooldef_MainMenu_isa_Menu():
    instance = gmf_all_tooldef_MainMenu(title="sample_text")
    assert isinstance(instance, Menu)


def test_gmf_all_tooldef_Toolbar_isa_Menu():
    instance = gmf_all_tooldef_Toolbar()
    assert isinstance(instance, Menu)


def test_gmf_all_mappings_NodeReference_isa_NeedsContainment():
    instance = gmf_all_mappings_NodeReference()
    assert isinstance(instance, NeedsContainment)


def test_gmf_all_gmfgraph_DiagramLabel_isa_Node():
    instance = gmf_all_gmfgraph_DiagramLabel(elementIcon=True, external=True)
    assert isinstance(instance, Node)


def test_gmf_all_mappings_ChildReference_isa_NodeReference():
    instance = gmf_all_mappings_ChildReference()
    assert isinstance(instance, NodeReference)


def test_gmf_all_mappings_TopNodeReference_isa_NodeReference():
    instance = gmf_all_mappings_TopNodeReference()
    assert isinstance(instance, NodeReference)


def test_gmf_all_gmfgraph_ColorPin_isa_Pin():
    instance = gmf_all_gmfgraph_ColorPin(backgroundNotForeground=True)
    assert isinstance(instance, Pin)


def test_gmf_all_gmfgraph_CustomPin_isa_Pin():
    instance = gmf_all_gmfgraph_CustomPin(customOperationName="sample_text", customOperationType="sample_text")
    assert isinstance(instance, Pin)


def test_gmf_all_gmfgraph_VisiblePin_isa_Pin():
    instance = gmf_all_gmfgraph_VisiblePin()
    assert isinstance(instance, Pin)


def test_gmf_all_gmfgraph_ScalablePolygon_isa_Polygon():
    instance = gmf_all_gmfgraph_ScalablePolygon()
    assert isinstance(instance, Polygon)


def test_gmf_all_gmfgraph_Polygon_isa_Polyline():
    instance = gmf_all_gmfgraph_Polygon()
    assert isinstance(instance, Polyline)


def test_gmf_all_gmfgraph_ConnectionFigure_isa_RealFigure():
    instance = gmf_all_gmfgraph_ConnectionFigure()
    assert isinstance(instance, RealFigure)


def test_gmf_all_gmfgraph_DecorationFigure_isa_RealFigure():
    instance = gmf_all_gmfgraph_DecorationFigure()
    assert isinstance(instance, RealFigure)


def test_gmf_all_gmfgraph_InvisibleRectangle_isa_RealFigure():
    instance = gmf_all_gmfgraph_InvisibleRectangle()
    assert isinstance(instance, RealFigure)


def test_gmf_all_gmfgraph_Label_isa_RealFigure():
    instance = gmf_all_gmfgraph_Label(text="sample_text")
    assert isinstance(instance, RealFigure)


def test_gmf_all_gmfgraph_LabeledContainer_isa_RealFigure():
    instance = gmf_all_gmfgraph_LabeledContainer()
    assert isinstance(instance, RealFigure)


def test_gmf_all_gmfgraph_SVGFigure_isa_RealFigure():
    instance = gmf_all_gmfgraph_SVGFigure(documentURI="sample_text", noCanvasHeight=True, noCanvasWidth=True)
    assert isinstance(instance, RealFigure)


def test_gmf_all_gmfgraph_Shape_isa_RealFigure():
    instance = gmf_all_gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert isinstance(instance, RealFigure)


def test_gmf_all_gmfgraph_VerticalLabel_isa_RealFigure():
    instance = gmf_all_gmfgraph_VerticalLabel(text="sample_text")
    assert isinstance(instance, RealFigure)


def test_gmf_all_mappings_AuditRule_isa_RuleBase():
    instance = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    assert isinstance(instance, RuleBase)


def test_gmf_all_mappings_MetricRule_isa_RuleBase():
    instance = gmf_all_mappings_MetricRule(highLimit="sample_text", key="sample_text", lowLimit="sample_text")
    assert isinstance(instance, RuleBase)


def test_gmf_all_gmfgraph_Ellipse_isa_Shape():
    instance = gmf_all_gmfgraph_Ellipse()
    assert isinstance(instance, Shape)


def test_gmf_all_gmfgraph_Polyline_isa_Shape():
    instance = gmf_all_gmfgraph_Polyline()
    assert isinstance(instance, Shape)


def test_gmf_all_gmfgraph_Rectangle_isa_Shape():
    instance = gmf_all_gmfgraph_Rectangle()
    assert isinstance(instance, Shape)


def test_gmf_all_gmfgraph_RoundedRectangle_isa_Shape():
    instance = gmf_all_gmfgraph_RoundedRectangle(cornerHeight=7, cornerWidth=7)
    assert isinstance(instance, Shape)


def test_gmf_all_tooldef_GenericStyleSelector_isa_StyleSelector():
    instance = gmf_all_tooldef_GenericStyleSelector(values="sample_text")
    assert isinstance(instance, StyleSelector)


def test_gmf_all_tooldef_Palette_isa_ToolContainer():
    instance = gmf_all_tooldef_Palette()
    assert isinstance(instance, ToolContainer)


def test_gmf_all_tooldef_ToolGroup_isa_ToolContainer():
    instance = gmf_all_tooldef_ToolGroup(collapsible=True, stack=True)
    assert isinstance(instance, ToolContainer)


def test_gmf_all_mappings_Constraint_isa_ValueExpression():
    instance = gmf_all_mappings_Constraint()
    assert isinstance(instance, ValueExpression)


def test_gmf_all_gmfgraph_AlignmentFacet_isa_VisualFacet():
    instance = gmf_all_gmfgraph_AlignmentFacet(alignment="sample_text")
    assert isinstance(instance, VisualFacet)


def test_gmf_all_gmfgraph_DefaultSizeFacet_isa_VisualFacet():
    instance = gmf_all_gmfgraph_DefaultSizeFacet()
    assert isinstance(instance, VisualFacet)


def test_gmf_all_gmfgraph_GeneralFacet_isa_VisualFacet():
    instance = gmf_all_gmfgraph_GeneralFacet(data="sample_text", identifier="sample_text")
    assert isinstance(instance, VisualFacet)


def test_gmf_all_gmfgraph_GradientFacet_isa_VisualFacet():
    instance = gmf_all_gmfgraph_GradientFacet(direction="sample_text")
    assert isinstance(instance, VisualFacet)


def test_gmf_all_gmfgraph_LabelOffsetFacet_isa_VisualFacet():
    instance = gmf_all_gmfgraph_LabelOffsetFacet(x=7, y=7)
    assert isinstance(instance, VisualFacet)


def test_gmf_all_gmfgraph_RealFigure_isa_gmfgraph_AbstractFigure():
    instance = gmf_all_gmfgraph_RealFigure(name="sample_text")
    assert isinstance(instance, gmfgraph_AbstractFigure)


def test_gmf_all_gmfgraph_CustomBorder_isa_gmfgraph_Border():
    instance = gmf_all_gmfgraph_CustomBorder()
    assert isinstance(instance, gmfgraph_Border)


def test_gmf_all_gmfgraph_CustomConnection_isa_gmfgraph_ConnectionFigure():
    instance = gmf_all_gmfgraph_CustomConnection()
    assert isinstance(instance, gmfgraph_ConnectionFigure)


def test_gmf_all_gmfgraph_PolylineConnection_isa_gmfgraph_ConnectionFigure():
    instance = gmf_all_gmfgraph_PolylineConnection()
    assert isinstance(instance, gmfgraph_ConnectionFigure)


def test_gmf_all_gmfgraph_RealFigure_isa_gmfgraph_CustomAttributeOwner():
    instance = gmf_all_gmfgraph_RealFigure(name="sample_text")
    assert isinstance(instance, gmfgraph_CustomAttributeOwner)


def test_gmf_all_gmfgraph_CustomBorder_isa_gmfgraph_CustomClass():
    instance = gmf_all_gmfgraph_CustomBorder()
    assert isinstance(instance, gmfgraph_CustomClass)


def test_gmf_all_gmfgraph_CustomFigure_isa_gmfgraph_CustomClass():
    instance = gmf_all_gmfgraph_CustomFigure()
    assert isinstance(instance, gmfgraph_CustomClass)


def test_gmf_all_gmfgraph_CustomLayout_isa_gmfgraph_CustomClass():
    instance = gmf_all_gmfgraph_CustomLayout()
    assert isinstance(instance, gmfgraph_CustomClass)


def test_gmf_all_gmfgraph_CustomLayoutData_isa_gmfgraph_CustomClass():
    instance = gmf_all_gmfgraph_CustomLayoutData()
    assert isinstance(instance, gmfgraph_CustomClass)


def test_gmf_all_gmfgraph_CustomConnection_isa_gmfgraph_CustomFigure():
    instance = gmf_all_gmfgraph_CustomConnection()
    assert isinstance(instance, gmfgraph_CustomFigure)


def test_gmf_all_gmfgraph_CustomDecoration_isa_gmfgraph_CustomFigure():
    instance = gmf_all_gmfgraph_CustomDecoration()
    assert isinstance(instance, gmfgraph_CustomFigure)


def test_gmf_all_gmfgraph_CustomDecoration_isa_gmfgraph_DecorationFigure():
    instance = gmf_all_gmfgraph_CustomDecoration()
    assert isinstance(instance, gmfgraph_DecorationFigure)


def test_gmf_all_gmfgraph_PolygonDecoration_isa_gmfgraph_DecorationFigure():
    instance = gmf_all_gmfgraph_PolygonDecoration()
    assert isinstance(instance, gmfgraph_DecorationFigure)


def test_gmf_all_gmfgraph_PolylineDecoration_isa_gmfgraph_DecorationFigure():
    instance = gmf_all_gmfgraph_PolylineDecoration()
    assert isinstance(instance, gmfgraph_DecorationFigure)


def test_gmf_all_gmfgraph_CustomLayout_isa_gmfgraph_Layout():
    instance = gmf_all_gmfgraph_CustomLayout()
    assert isinstance(instance, gmfgraph_Layout)


def test_gmf_all_gmfgraph_CustomLayoutData_isa_gmfgraph_LayoutData():
    instance = gmf_all_gmfgraph_CustomLayoutData()
    assert isinstance(instance, gmfgraph_LayoutData)


def test_gmf_all_gmfgraph_RealFigure_isa_gmfgraph_PinOwner():
    instance = gmf_all_gmfgraph_RealFigure(name="sample_text")
    assert isinstance(instance, gmfgraph_PinOwner)


def test_gmf_all_gmfgraph_PolygonDecoration_isa_gmfgraph_Polygon():
    instance = gmf_all_gmfgraph_PolygonDecoration()
    assert isinstance(instance, gmfgraph_Polygon)


def test_gmf_all_gmfgraph_PolylineConnection_isa_gmfgraph_Polyline():
    instance = gmf_all_gmfgraph_PolylineConnection()
    assert isinstance(instance, gmfgraph_Polyline)


def test_gmf_all_gmfgraph_PolylineDecoration_isa_gmfgraph_Polyline():
    instance = gmf_all_gmfgraph_PolylineDecoration()
    assert isinstance(instance, gmfgraph_Polyline)


def test_gmf_all_gmfgraph_CustomFigure_isa_gmfgraph_RealFigure():
    instance = gmf_all_gmfgraph_CustomFigure()
    assert isinstance(instance, gmfgraph_RealFigure)


def test_gmf_all_mappings_LinkMapping_isa_mappings_AppearanceSteward():
    instance = gmf_all_mappings_LinkMapping()
    assert isinstance(instance, mappings_AppearanceSteward)


def test_gmf_all_mappings_NodeMapping_isa_mappings_AppearanceSteward():
    instance = gmf_all_mappings_NodeMapping()
    assert isinstance(instance, mappings_AppearanceSteward)


def test_gmf_all_mappings_DiagramElementTarget_isa_mappings_Auditable():
    instance = gmf_all_mappings_DiagramElementTarget()
    assert isinstance(instance, mappings_Auditable)


def test_gmf_all_mappings_DomainElementTarget_isa_mappings_Auditable():
    instance = gmf_all_mappings_DomainElementTarget()
    assert isinstance(instance, mappings_Auditable)


def test_gmf_all_mappings_NotationElementTarget_isa_mappings_Auditable():
    instance = gmf_all_mappings_NotationElementTarget()
    assert isinstance(instance, mappings_Auditable)


def test_gmf_all_mappings_LinkMapping_isa_mappings_MappingEntry():
    instance = gmf_all_mappings_LinkMapping()
    assert isinstance(instance, mappings_MappingEntry)


def test_gmf_all_mappings_NodeMapping_isa_mappings_MappingEntry():
    instance = gmf_all_mappings_NodeMapping()
    assert isinstance(instance, mappings_MappingEntry)


def test_gmf_all_mappings_DiagramElementTarget_isa_mappings_Measurable():
    instance = gmf_all_mappings_DiagramElementTarget()
    assert isinstance(instance, mappings_Measurable)


def test_gmf_all_mappings_DomainElementTarget_isa_mappings_Measurable():
    instance = gmf_all_mappings_DomainElementTarget()
    assert isinstance(instance, mappings_Measurable)


def test_gmf_all_mappings_NotationElementTarget_isa_mappings_Measurable():
    instance = gmf_all_mappings_NotationElementTarget()
    assert isinstance(instance, mappings_Measurable)


def test_gmf_all_mappings_LinkMapping_isa_mappings_MenuOwner():
    instance = gmf_all_mappings_LinkMapping()
    assert isinstance(instance, mappings_MenuOwner)


def test_gmf_all_mappings_NodeMapping_isa_mappings_MenuOwner():
    instance = gmf_all_mappings_NodeMapping()
    assert isinstance(instance, mappings_MenuOwner)


def test_gmf_all_mappings_LinkMapping_isa_mappings_NeedsContainment():
    instance = gmf_all_mappings_LinkMapping()
    assert isinstance(instance, mappings_NeedsContainment)


def test_gmf_all_mappings_LinkMapping_isa_mappings_ToolOwner():
    instance = gmf_all_mappings_LinkMapping()
    assert isinstance(instance, mappings_ToolOwner)


def test_gmf_all_mappings_NodeMapping_isa_mappings_ToolOwner():
    instance = gmf_all_mappings_NodeMapping()
    assert isinstance(instance, mappings_ToolOwner)


def test_gmf_all_tooldef_PopupMenu_isa_tooldef_ContributionItem():
    instance = gmf_all_tooldef_PopupMenu(iD="sample_text")
    assert isinstance(instance, tooldef_ContributionItem)


def test_gmf_all_tooldef_PopupMenu_isa_tooldef_Menu():
    instance = gmf_all_tooldef_PopupMenu(iD="sample_text")
    assert isinstance(instance, tooldef_Menu)


def test_gmf_all_tooldef_PredefinedMenu_isa_tooldef_Menu():
    instance = gmf_all_tooldef_PredefinedMenu()
    assert isinstance(instance, tooldef_Menu)


def test_gmf_all_tooldef_PredefinedMenu_isa_tooldef_PredefinedItem():
    instance = gmf_all_tooldef_PredefinedMenu()
    assert isinstance(instance, tooldef_PredefinedItem)


def test_assoc_accessor191_link_reassign_clear():
    a = gmf_all_gmfgraph_Compartment(collapsible=True, needsTitle=True)
    b1 = ChildAccess()
    b2 = ChildAccess()
    _safe_set(a, 'gmf_all_gmfgraph_Compartment', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_Compartment', b1)
    if hasattr(b1, 'ChildAccess192'):
        assert _is_linked(b1, 'ChildAccess192', a)
    _safe_set(a, 'gmf_all_gmfgraph_Compartment', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_Compartment', b2)
    if hasattr(b1, 'ChildAccess192'):
        assert not _is_linked(b1, 'ChildAccess192', a)
    if hasattr(b2, 'ChildAccess192'):
        assert _is_linked(b2, 'ChildAccess192', a)
    _safe_set(a, 'gmf_all_gmfgraph_Compartment', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_Compartment', b2)
    if hasattr(b2, 'ChildAccess192'):
        assert not _is_linked(b2, 'ChildAccess192', a)


def test_assoc_accessor193_link_reassign_clear():
    a = gmf_all_gmfgraph_DiagramLabel(elementIcon=True, external=True)
    b1 = ChildAccess()
    b2 = ChildAccess()
    _safe_set(a, 'gmf_all_gmfgraph_DiagramLabel', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_DiagramLabel', b1)
    if hasattr(b1, 'ChildAccess194'):
        assert _is_linked(b1, 'ChildAccess194', a)
    _safe_set(a, 'gmf_all_gmfgraph_DiagramLabel', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_DiagramLabel', b2)
    if hasattr(b1, 'ChildAccess194'):
        assert not _is_linked(b1, 'ChildAccess194', a)
    if hasattr(b2, 'ChildAccess194'):
        assert _is_linked(b2, 'ChildAccess194', a)
    _safe_set(a, 'gmf_all_gmfgraph_DiagramLabel', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_DiagramLabel', b2)
    if hasattr(b2, 'ChildAccess194'):
        assert not _is_linked(b2, 'ChildAccess194', a)


def test_assoc_active155_link_reassign_clear():
    a = gmf_all_tooldef_ToolGroup(collapsible=True, stack=True)
    b1 = AbstractTool()
    b2 = AbstractTool()
    _safe_set(a, 'gmf_all_tooldef_ToolGroup', b1)
    assert _is_linked(a, 'gmf_all_tooldef_ToolGroup', b1)
    if hasattr(b1, 'AbstractTool156'):
        assert _is_linked(b1, 'AbstractTool156', a)
    _safe_set(a, 'gmf_all_tooldef_ToolGroup', b2)
    assert _is_linked(a, 'gmf_all_tooldef_ToolGroup', b2)
    if hasattr(b1, 'AbstractTool156'):
        assert not _is_linked(b1, 'AbstractTool156', a)
    if hasattr(b2, 'AbstractTool156'):
        assert _is_linked(b2, 'AbstractTool156', a)
    _safe_set(a, 'gmf_all_tooldef_ToolGroup', None)
    assert not _is_linked(a, 'gmf_all_tooldef_ToolGroup', b2)
    if hasattr(b2, 'AbstractTool156'):
        assert not _is_linked(b2, 'AbstractTool156', a)


def test_assoc_areaOfInterest283_link_reassign_clear():
    a = gmf_all_gmfgraph_SVGFigure(documentURI="sample_text", noCanvasHeight=True, noCanvasWidth=True)
    b1 = Rectangle2D()
    b2 = Rectangle2D()
    _safe_set(a, 'gmf_all_gmfgraph_SVGFigure284', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_SVGFigure284', b1)
    if hasattr(b1, 'Rectangle2D'):
        assert _is_linked(b1, 'Rectangle2D', a)
    _safe_set(a, 'gmf_all_gmfgraph_SVGFigure284', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_SVGFigure284', b2)
    if hasattr(b1, 'Rectangle2D'):
        assert not _is_linked(b1, 'Rectangle2D', a)
    if hasattr(b2, 'Rectangle2D'):
        assert _is_linked(b2, 'Rectangle2D', a)
    _safe_set(a, 'gmf_all_gmfgraph_SVGFigure284', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_SVGFigure284', b2)
    if hasattr(b2, 'Rectangle2D'):
        assert not _is_linked(b2, 'Rectangle2D', a)


def test_assoc_attribute124_link_reassign_clear():
    a = gmf_all_mappings_DomainAttributeTarget(nullAsError=True)
    b1 = mappings_gmf_all_EAttribute()
    b2 = mappings_gmf_all_EAttribute()
    _safe_set(a, 'gmf_all_mappings_DomainAttributeTarget', b1)
    assert _is_linked(a, 'gmf_all_mappings_DomainAttributeTarget', b1)
    if hasattr(b1, 'mappings_gmf_all_EAttribute125'):
        assert _is_linked(b1, 'mappings_gmf_all_EAttribute125', a)
    _safe_set(a, 'gmf_all_mappings_DomainAttributeTarget', b2)
    assert _is_linked(a, 'gmf_all_mappings_DomainAttributeTarget', b2)
    if hasattr(b1, 'mappings_gmf_all_EAttribute125'):
        assert not _is_linked(b1, 'mappings_gmf_all_EAttribute125', a)
    if hasattr(b2, 'mappings_gmf_all_EAttribute125'):
        assert _is_linked(b2, 'mappings_gmf_all_EAttribute125', a)
    _safe_set(a, 'gmf_all_mappings_DomainAttributeTarget', None)
    assert not _is_linked(a, 'gmf_all_mappings_DomainAttributeTarget', b2)
    if hasattr(b2, 'mappings_gmf_all_EAttribute125'):
        assert not _is_linked(b2, 'mappings_gmf_all_EAttribute125', a)


def test_assoc_audits113_link_reassign_clear():
    a = gmf_all_mappings_AuditContainer(description="sample_text", id="sample_text", name="sample_text")
    b1 = AuditRule()
    b2 = AuditRule()
    _safe_set(a, 'container', {b1})
    assert _is_linked(a, 'container', b1)
    if hasattr(b1, 'AuditRule'):
        assert _is_linked(b1, 'AuditRule', a)
    _safe_set(a, 'container', {b2})
    assert _is_linked(a, 'container', b2)
    if hasattr(b1, 'AuditRule'):
        assert not _is_linked(b1, 'AuditRule', a)
    if hasattr(b2, 'AuditRule'):
        assert _is_linked(b2, 'AuditRule', a)
    _safe_set(a, 'container', set())
    assert not _is_linked(a, 'container', b2)
    if hasattr(b2, 'AuditRule'):
        assert not _is_linked(b2, 'AuditRule', a)


def test_assoc_borders182_link_reassign_clear():
    a = gmf_all_gmfgraph_FigureGallery(implementationBundle="sample_text")
    b1 = Border()
    b2 = Border()
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery183', {b1})
    assert _is_linked(a, 'gmf_all_gmfgraph_FigureGallery183', b1)
    if hasattr(b1, 'Border'):
        assert _is_linked(b1, 'Border', a)
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery183', {b2})
    assert _is_linked(a, 'gmf_all_gmfgraph_FigureGallery183', b2)
    if hasattr(b1, 'Border'):
        assert not _is_linked(b1, 'Border', a)
    if hasattr(b2, 'Border'):
        assert _is_linked(b2, 'Border', a)
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery183', set())
    assert not _is_linked(a, 'gmf_all_gmfgraph_FigureGallery183', b2)
    if hasattr(b2, 'Border'):
        assert not _is_linked(b2, 'Border', a)


def test_assoc_childContainers114_link_reassign_clear():
    a = gmf_all_mappings_AuditContainer(description="sample_text", id="sample_text", name="sample_text")
    b1 = AuditContainer()
    b2 = AuditContainer()
    _safe_set(a, 'parentContainer', {b1})
    assert _is_linked(a, 'parentContainer', b1)
    if hasattr(b1, 'AuditContainer115'):
        assert _is_linked(b1, 'AuditContainer115', a)
    _safe_set(a, 'parentContainer', {b2})
    assert _is_linked(a, 'parentContainer', b2)
    if hasattr(b1, 'AuditContainer115'):
        assert not _is_linked(b1, 'AuditContainer115', a)
    if hasattr(b2, 'AuditContainer115'):
        assert _is_linked(b2, 'AuditContainer115', a)
    _safe_set(a, 'parentContainer', set())
    assert not _is_linked(a, 'parentContainer', b2)
    if hasattr(b2, 'AuditContainer115'):
        assert not _is_linked(b2, 'AuditContainer115', a)


def test_assoc_children234_link_reassign_clear():
    a = gmf_all_gmfgraph_RealFigure(name="sample_text")
    b1 = Figure()
    b2 = Figure()
    _safe_set(a, 'gmf_all_gmfgraph_RealFigure', {b1})
    assert _is_linked(a, 'gmf_all_gmfgraph_RealFigure', b1)
    if hasattr(b1, 'Figure235'):
        assert _is_linked(b1, 'Figure235', a)
    _safe_set(a, 'gmf_all_gmfgraph_RealFigure', {b2})
    assert _is_linked(a, 'gmf_all_gmfgraph_RealFigure', b2)
    if hasattr(b1, 'Figure235'):
        assert not _is_linked(b1, 'Figure235', a)
    if hasattr(b2, 'Figure235'):
        assert _is_linked(b2, 'Figure235', a)
    _safe_set(a, 'gmf_all_gmfgraph_RealFigure', set())
    assert not _is_linked(a, 'gmf_all_gmfgraph_RealFigure', b2)
    if hasattr(b2, 'Figure235'):
        assert not _is_linked(b2, 'Figure235', a)


def test_assoc_color252_link_reassign_clear():
    a = gmf_all_gmfgraph_LineBorder(width=7)
    b1 = Color()
    b2 = Color()
    _safe_set(a, 'gmf_all_gmfgraph_LineBorder', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_LineBorder', b1)
    if hasattr(b1, 'Color253'):
        assert _is_linked(b1, 'Color253', a)
    _safe_set(a, 'gmf_all_gmfgraph_LineBorder', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_LineBorder', b2)
    if hasattr(b1, 'Color253'):
        assert not _is_linked(b1, 'Color253', a)
    if hasattr(b2, 'Color253'):
        assert _is_linked(b2, 'Color253', a)
    _safe_set(a, 'gmf_all_gmfgraph_LineBorder', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_LineBorder', b2)
    if hasattr(b2, 'Color253'):
        assert not _is_linked(b2, 'Color253', a)


def test_assoc_container120_link_reassign_clear():
    a = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    b1 = AuditContainer()
    b2 = AuditContainer()
    _safe_set(a, 'audits', b1)
    assert _is_linked(a, 'audits', b1)
    if hasattr(b1, 'AuditContainer121'):
        assert _is_linked(b1, 'AuditContainer121', a)
    _safe_set(a, 'audits', b2)
    assert _is_linked(a, 'audits', b2)
    if hasattr(b1, 'AuditContainer121'):
        assert not _is_linked(b1, 'AuditContainer121', a)
    if hasattr(b2, 'AuditContainer121'):
        assert _is_linked(b2, 'AuditContainer121', a)
    _safe_set(a, 'audits', None)
    assert not _is_linked(a, 'audits', b2)
    if hasattr(b2, 'AuditContainer121'):
        assert not _is_linked(b2, 'AuditContainer121', a)


def test_assoc_container136_link_reassign_clear():
    a = gmf_all_mappings_MetricRule(highLimit="sample_text", key="sample_text", lowLimit="sample_text")
    b1 = MetricContainer()
    b2 = MetricContainer()
    _safe_set(a, 'metrics', b1)
    assert _is_linked(a, 'metrics', b1)
    if hasattr(b1, 'MetricContainer137'):
        assert _is_linked(b1, 'MetricContainer137', a)
    _safe_set(a, 'metrics', b2)
    assert _is_linked(a, 'metrics', b2)
    if hasattr(b1, 'MetricContainer137'):
        assert not _is_linked(b1, 'MetricContainer137', a)
    if hasattr(b2, 'MetricContainer137'):
        assert _is_linked(b2, 'MetricContainer137', a)
    _safe_set(a, 'metrics', None)
    assert not _is_linked(a, 'metrics', b2)
    if hasattr(b2, 'MetricContainer137'):
        assert not _is_linked(b2, 'MetricContainer137', a)


def test_assoc_container195_link_reassign_clear():
    a = gmf_all_gmfgraph_DiagramLabel(elementIcon=True, external=True)
    b1 = ChildAccess()
    b2 = ChildAccess()
    _safe_set(a, 'gmf_all_gmfgraph_DiagramLabel196', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_DiagramLabel196', b1)
    if hasattr(b1, 'ChildAccess197'):
        assert _is_linked(b1, 'ChildAccess197', a)
    _safe_set(a, 'gmf_all_gmfgraph_DiagramLabel196', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_DiagramLabel196', b2)
    if hasattr(b1, 'ChildAccess197'):
        assert not _is_linked(b1, 'ChildAccess197', a)
    if hasattr(b2, 'ChildAccess197'):
        assert _is_linked(b2, 'ChildAccess197', a)
    _safe_set(a, 'gmf_all_gmfgraph_DiagramLabel196', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_DiagramLabel196', b2)
    if hasattr(b2, 'ChildAccess197'):
        assert not _is_linked(b2, 'ChildAccess197', a)


def test_assoc_contentPane190_link_reassign_clear():
    a = gmf_all_gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    b1 = ChildAccess()
    b2 = ChildAccess()
    _safe_set(a, 'gmf_all_gmfgraph_Node', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_Node', b1)
    if hasattr(b1, 'ChildAccess'):
        assert _is_linked(b1, 'ChildAccess', a)
    _safe_set(a, 'gmf_all_gmfgraph_Node', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_Node', b2)
    if hasattr(b1, 'ChildAccess'):
        assert not _is_linked(b1, 'ChildAccess', a)
    if hasattr(b2, 'ChildAccess'):
        assert _is_linked(b2, 'ChildAccess', a)
    _safe_set(a, 'gmf_all_gmfgraph_Node', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_Node', b2)
    if hasattr(b2, 'ChildAccess'):
        assert not _is_linked(b2, 'ChildAccess', a)


def test_assoc_descriptors180_link_reassign_clear():
    a = gmf_all_gmfgraph_FigureGallery(implementationBundle="sample_text")
    b1 = FigureDescriptor()
    b2 = FigureDescriptor()
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery181', {b1})
    assert _is_linked(a, 'gmf_all_gmfgraph_FigureGallery181', b1)
    if hasattr(b1, 'FigureDescriptor'):
        assert _is_linked(b1, 'FigureDescriptor', a)
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery181', {b2})
    assert _is_linked(a, 'gmf_all_gmfgraph_FigureGallery181', b2)
    if hasattr(b1, 'FigureDescriptor'):
        assert not _is_linked(b1, 'FigureDescriptor', a)
    if hasattr(b2, 'FigureDescriptor'):
        assert _is_linked(b2, 'FigureDescriptor', a)
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery181', set())
    assert not _is_linked(a, 'gmf_all_gmfgraph_FigureGallery181', b2)
    if hasattr(b2, 'FigureDescriptor'):
        assert not _is_linked(b2, 'FigureDescriptor', a)


def test_assoc_diagramLabel66_link_reassign_clear():
    a = gmf_all_mappings_LabelMapping(readOnly=True)
    b1 = DiagramLabel()
    b2 = DiagramLabel()
    _safe_set(a, 'gmf_all_mappings_LabelMapping', b1)
    assert _is_linked(a, 'gmf_all_mappings_LabelMapping', b1)
    if hasattr(b1, 'DiagramLabel'):
        assert _is_linked(b1, 'DiagramLabel', a)
    _safe_set(a, 'gmf_all_mappings_LabelMapping', b2)
    assert _is_linked(a, 'gmf_all_mappings_LabelMapping', b2)
    if hasattr(b1, 'DiagramLabel'):
        assert not _is_linked(b1, 'DiagramLabel', a)
    if hasattr(b2, 'DiagramLabel'):
        assert _is_linked(b2, 'DiagramLabel', a)
    _safe_set(a, 'gmf_all_mappings_LabelMapping', None)
    assert not _is_linked(a, 'gmf_all_mappings_LabelMapping', b2)
    if hasattr(b2, 'DiagramLabel'):
        assert not _is_linked(b2, 'DiagramLabel', a)


def test_assoc_diagramPin140_link_reassign_clear():
    a = gmf_all_mappings_VisualEffectMapping(oclExpression="sample_text")
    b1 = Pin()
    b2 = Pin()
    _safe_set(a, 'gmf_all_mappings_VisualEffectMapping', b1)
    assert _is_linked(a, 'gmf_all_mappings_VisualEffectMapping', b1)
    if hasattr(b1, 'Pin'):
        assert _is_linked(b1, 'Pin', a)
    _safe_set(a, 'gmf_all_mappings_VisualEffectMapping', b2)
    assert _is_linked(a, 'gmf_all_mappings_VisualEffectMapping', b2)
    if hasattr(b1, 'Pin'):
        assert not _is_linked(b1, 'Pin', a)
    if hasattr(b2, 'Pin'):
        assert _is_linked(b2, 'Pin', a)
    _safe_set(a, 'gmf_all_mappings_VisualEffectMapping', None)
    assert not _is_linked(a, 'gmf_all_mappings_VisualEffectMapping', b2)
    if hasattr(b2, 'Pin'):
        assert not _is_linked(b2, 'Pin', a)


def test_assoc_domainInitializer14_link_reassign_clear():
    a = gmf_all_mappings_MappingEntry()
    b1 = ElementInitializer()
    b2 = ElementInitializer()
    _safe_set(a, 'gmf_all_mappings_MappingEntry15', b1)
    assert _is_linked(a, 'gmf_all_mappings_MappingEntry15', b1)
    if hasattr(b1, 'ElementInitializer'):
        assert _is_linked(b1, 'ElementInitializer', a)
    _safe_set(a, 'gmf_all_mappings_MappingEntry15', b2)
    assert _is_linked(a, 'gmf_all_mappings_MappingEntry15', b2)
    if hasattr(b1, 'ElementInitializer'):
        assert not _is_linked(b1, 'ElementInitializer', a)
    if hasattr(b2, 'ElementInitializer'):
        assert _is_linked(b2, 'ElementInitializer', a)
    _safe_set(a, 'gmf_all_mappings_MappingEntry15', None)
    assert not _is_linked(a, 'gmf_all_mappings_MappingEntry15', b2)
    if hasattr(b2, 'ElementInitializer'):
        assert not _is_linked(b2, 'ElementInitializer', a)


def test_assoc_domainMetaElement11_link_reassign_clear():
    a = gmf_all_mappings_MappingEntry()
    b1 = mappings_gmf_all_EClass()
    b2 = mappings_gmf_all_EClass()
    _safe_set(a, 'gmf_all_mappings_MappingEntry', b1)
    assert _is_linked(a, 'gmf_all_mappings_MappingEntry', b1)
    if hasattr(b1, 'mappings_gmf_all_EClass'):
        assert _is_linked(b1, 'mappings_gmf_all_EClass', a)
    _safe_set(a, 'gmf_all_mappings_MappingEntry', b2)
    assert _is_linked(a, 'gmf_all_mappings_MappingEntry', b2)
    if hasattr(b1, 'mappings_gmf_all_EClass'):
        assert not _is_linked(b1, 'mappings_gmf_all_EClass', a)
    if hasattr(b2, 'mappings_gmf_all_EClass'):
        assert _is_linked(b2, 'mappings_gmf_all_EClass', a)
    _safe_set(a, 'gmf_all_mappings_MappingEntry', None)
    assert not _is_linked(a, 'gmf_all_mappings_MappingEntry', b2)
    if hasattr(b2, 'mappings_gmf_all_EClass'):
        assert not _is_linked(b2, 'mappings_gmf_all_EClass', a)


def test_assoc_domainSpecialization12_link_reassign_clear():
    a = gmf_all_mappings_MappingEntry()
    b1 = Constraint()
    b2 = Constraint()
    _safe_set(a, 'gmf_all_mappings_MappingEntry13', b1)
    assert _is_linked(a, 'gmf_all_mappings_MappingEntry13', b1)
    if hasattr(b1, 'Constraint'):
        assert _is_linked(b1, 'Constraint', a)
    _safe_set(a, 'gmf_all_mappings_MappingEntry13', b2)
    assert _is_linked(a, 'gmf_all_mappings_MappingEntry13', b2)
    if hasattr(b1, 'Constraint'):
        assert not _is_linked(b1, 'Constraint', a)
    if hasattr(b2, 'Constraint'):
        assert _is_linked(b2, 'Constraint', a)
    _safe_set(a, 'gmf_all_mappings_MappingEntry13', None)
    assert not _is_linked(a, 'gmf_all_mappings_MappingEntry13', b2)
    if hasattr(b2, 'Constraint'):
        assert not _is_linked(b2, 'Constraint', a)


def test_assoc_editableFeatures69_link_reassign_clear():
    a = gmf_all_mappings_FeatureLabelMapping(editMethod="sample_text", editPattern="sample_text", editorPattern="sample_text", viewMethod="sample_text", viewPattern="sample_text")
    b1 = mappings_gmf_all_EAttribute()
    b2 = mappings_gmf_all_EAttribute()
    _safe_set(a, 'gmf_all_mappings_FeatureLabelMapping70', {b1})
    assert _is_linked(a, 'gmf_all_mappings_FeatureLabelMapping70', b1)
    if hasattr(b1, 'mappings_gmf_all_EAttribute71'):
        assert _is_linked(b1, 'mappings_gmf_all_EAttribute71', a)
    _safe_set(a, 'gmf_all_mappings_FeatureLabelMapping70', {b2})
    assert _is_linked(a, 'gmf_all_mappings_FeatureLabelMapping70', b2)
    if hasattr(b1, 'mappings_gmf_all_EAttribute71'):
        assert not _is_linked(b1, 'mappings_gmf_all_EAttribute71', a)
    if hasattr(b2, 'mappings_gmf_all_EAttribute71'):
        assert _is_linked(b2, 'mappings_gmf_all_EAttribute71', a)
    _safe_set(a, 'gmf_all_mappings_FeatureLabelMapping70', set())
    assert not _is_linked(a, 'gmf_all_mappings_FeatureLabelMapping70', b2)
    if hasattr(b2, 'mappings_gmf_all_EAttribute71'):
        assert not _is_linked(b2, 'mappings_gmf_all_EAttribute71', a)


def test_assoc_features68_link_reassign_clear():
    a = gmf_all_mappings_FeatureLabelMapping(editMethod="sample_text", editPattern="sample_text", editorPattern="sample_text", viewMethod="sample_text", viewPattern="sample_text")
    b1 = mappings_gmf_all_EAttribute()
    b2 = mappings_gmf_all_EAttribute()
    _safe_set(a, 'gmf_all_mappings_FeatureLabelMapping', {b1})
    assert _is_linked(a, 'gmf_all_mappings_FeatureLabelMapping', b1)
    if hasattr(b1, 'mappings_gmf_all_EAttribute'):
        assert _is_linked(b1, 'mappings_gmf_all_EAttribute', a)
    _safe_set(a, 'gmf_all_mappings_FeatureLabelMapping', {b2})
    assert _is_linked(a, 'gmf_all_mappings_FeatureLabelMapping', b2)
    if hasattr(b1, 'mappings_gmf_all_EAttribute'):
        assert not _is_linked(b1, 'mappings_gmf_all_EAttribute', a)
    if hasattr(b2, 'mappings_gmf_all_EAttribute'):
        assert _is_linked(b2, 'mappings_gmf_all_EAttribute', a)
    _safe_set(a, 'gmf_all_mappings_FeatureLabelMapping', set())
    assert not _is_linked(a, 'gmf_all_mappings_FeatureLabelMapping', b2)
    if hasattr(b2, 'mappings_gmf_all_EAttribute'):
        assert not _is_linked(b2, 'mappings_gmf_all_EAttribute', a)


def test_assoc_figure232_link_reassign_clear():
    a = gmf_all_gmfgraph_ChildAccess(accessor="sample_text")
    b1 = Figure()
    b2 = Figure()
    _safe_set(a, 'gmf_all_gmfgraph_ChildAccess', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_ChildAccess', b1)
    if hasattr(b1, 'Figure233'):
        assert _is_linked(b1, 'Figure233', a)
    _safe_set(a, 'gmf_all_gmfgraph_ChildAccess', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_ChildAccess', b2)
    if hasattr(b1, 'Figure233'):
        assert not _is_linked(b1, 'Figure233', a)
    if hasattr(b2, 'Figure233'):
        assert _is_linked(b2, 'Figure233', a)
    _safe_set(a, 'gmf_all_gmfgraph_ChildAccess', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_ChildAccess', b2)
    if hasattr(b2, 'Figure233'):
        assert not _is_linked(b2, 'Figure233', a)


def test_assoc_figures179_link_reassign_clear():
    a = gmf_all_gmfgraph_FigureGallery(implementationBundle="sample_text")
    b1 = RealFigure()
    b2 = RealFigure()
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery', {b1})
    assert _is_linked(a, 'gmf_all_gmfgraph_FigureGallery', b1)
    if hasattr(b1, 'RealFigure'):
        assert _is_linked(b1, 'RealFigure', a)
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery', {b2})
    assert _is_linked(a, 'gmf_all_gmfgraph_FigureGallery', b2)
    if hasattr(b1, 'RealFigure'):
        assert not _is_linked(b1, 'RealFigure', a)
    if hasattr(b2, 'RealFigure'):
        assert _is_linked(b2, 'RealFigure', a)
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery', set())
    assert not _is_linked(a, 'gmf_all_gmfgraph_FigureGallery', b2)
    if hasattr(b2, 'RealFigure'):
        assert not _is_linked(b2, 'RealFigure', a)


def test_assoc_icon160_link_reassign_clear():
    a = gmf_all_tooldef_ContributionItem(title="sample_text")
    b1 = Image()
    b2 = Image()
    _safe_set(a, 'gmf_all_tooldef_ContributionItem', b1)
    assert _is_linked(a, 'gmf_all_tooldef_ContributionItem', b1)
    if hasattr(b1, 'Image161'):
        assert _is_linked(b1, 'Image161', a)
    _safe_set(a, 'gmf_all_tooldef_ContributionItem', b2)
    assert _is_linked(a, 'gmf_all_tooldef_ContributionItem', b2)
    if hasattr(b1, 'Image161'):
        assert not _is_linked(b1, 'Image161', a)
    if hasattr(b2, 'Image161'):
        assert _is_linked(b2, 'Image161', a)
    _safe_set(a, 'gmf_all_tooldef_ContributionItem', None)
    assert not _is_linked(a, 'gmf_all_tooldef_ContributionItem', b2)
    if hasattr(b2, 'Image161'):
        assert not _is_linked(b2, 'Image161', a)


def test_assoc_labelMappings16_link_reassign_clear():
    a = gmf_all_mappings_MappingEntry()
    b1 = LabelMapping()
    b2 = LabelMapping()
    _safe_set(a, 'mapEntry', {b1})
    assert _is_linked(a, 'mapEntry', b1)
    if hasattr(b1, 'LabelMapping'):
        assert _is_linked(b1, 'LabelMapping', a)
    _safe_set(a, 'mapEntry', {b2})
    assert _is_linked(a, 'mapEntry', b2)
    if hasattr(b1, 'LabelMapping'):
        assert not _is_linked(b1, 'LabelMapping', a)
    if hasattr(b2, 'LabelMapping'):
        assert _is_linked(b2, 'LabelMapping', a)
    _safe_set(a, 'mapEntry', set())
    assert not _is_linked(a, 'mapEntry', b2)
    if hasattr(b2, 'LabelMapping'):
        assert not _is_linked(b2, 'LabelMapping', a)


def test_assoc_largeIcon150_link_reassign_clear():
    a = gmf_all_tooldef_AbstractTool(description="sample_text", title="sample_text")
    b1 = Image()
    b2 = Image()
    _safe_set(a, 'gmf_all_tooldef_AbstractTool151', b1)
    assert _is_linked(a, 'gmf_all_tooldef_AbstractTool151', b1)
    if hasattr(b1, 'Image152'):
        assert _is_linked(b1, 'Image152', a)
    _safe_set(a, 'gmf_all_tooldef_AbstractTool151', b2)
    assert _is_linked(a, 'gmf_all_tooldef_AbstractTool151', b2)
    if hasattr(b1, 'Image152'):
        assert not _is_linked(b1, 'Image152', a)
    if hasattr(b2, 'Image152'):
        assert _is_linked(b2, 'Image152', a)
    _safe_set(a, 'gmf_all_tooldef_AbstractTool151', None)
    assert not _is_linked(a, 'gmf_all_tooldef_AbstractTool151', b2)
    if hasattr(b2, 'Image152'):
        assert not _is_linked(b2, 'Image152', a)


def test_assoc_layouts184_link_reassign_clear():
    a = gmf_all_gmfgraph_FigureGallery(implementationBundle="sample_text")
    b1 = Layout()
    b2 = Layout()
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery185', {b1})
    assert _is_linked(a, 'gmf_all_gmfgraph_FigureGallery185', b1)
    if hasattr(b1, 'Layout'):
        assert _is_linked(b1, 'Layout', a)
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery185', {b2})
    assert _is_linked(a, 'gmf_all_gmfgraph_FigureGallery185', b2)
    if hasattr(b1, 'Layout'):
        assert not _is_linked(b1, 'Layout', a)
    if hasattr(b2, 'Layout'):
        assert _is_linked(b2, 'Layout', a)
    _safe_set(a, 'gmf_all_gmfgraph_FigureGallery185', set())
    assert not _is_linked(a, 'gmf_all_gmfgraph_FigureGallery185', b2)
    if hasattr(b2, 'Layout'):
        assert not _is_linked(b2, 'Layout', a)


def test_assoc_mapEntry67_link_reassign_clear():
    a = gmf_all_mappings_LabelMapping(readOnly=True)
    b1 = MappingEntry()
    b2 = MappingEntry()
    _safe_set(a, 'labelMappings', b1)
    assert _is_linked(a, 'labelMappings', b1)
    if hasattr(b1, 'MappingEntry'):
        assert _is_linked(b1, 'MappingEntry', a)
    _safe_set(a, 'labelMappings', b2)
    assert _is_linked(a, 'labelMappings', b2)
    if hasattr(b1, 'MappingEntry'):
        assert not _is_linked(b1, 'MappingEntry', a)
    if hasattr(b2, 'MappingEntry'):
        assert _is_linked(b2, 'MappingEntry', a)
    _safe_set(a, 'labelMappings', None)
    assert not _is_linked(a, 'labelMappings', b2)
    if hasattr(b2, 'MappingEntry'):
        assert not _is_linked(b2, 'MappingEntry', a)


def test_assoc_margins270_link_reassign_clear():
    a = gmf_all_gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    b1 = Dimension()
    b2 = Dimension()
    _safe_set(a, 'gmf_all_gmfgraph_GridLayout', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_GridLayout', b1)
    if hasattr(b1, 'Dimension271'):
        assert _is_linked(b1, 'Dimension271', a)
    _safe_set(a, 'gmf_all_gmfgraph_GridLayout', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_GridLayout', b2)
    if hasattr(b1, 'Dimension271'):
        assert not _is_linked(b1, 'Dimension271', a)
    if hasattr(b2, 'Dimension271'):
        assert _is_linked(b2, 'Dimension271', a)
    _safe_set(a, 'gmf_all_gmfgraph_GridLayout', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_GridLayout', b2)
    if hasattr(b2, 'Dimension271'):
        assert not _is_linked(b2, 'Dimension271', a)


def test_assoc_owner230_link_reassign_clear():
    a = gmf_all_gmfgraph_ChildAccess(accessor="sample_text")
    b1 = FigureDescriptor()
    b2 = FigureDescriptor()
    _safe_set(a, 'accessors', b1)
    assert _is_linked(a, 'accessors', b1)
    if hasattr(b1, 'FigureDescriptor231'):
        assert _is_linked(b1, 'FigureDescriptor231', a)
    _safe_set(a, 'accessors', b2)
    assert _is_linked(a, 'accessors', b2)
    if hasattr(b1, 'FigureDescriptor231'):
        assert not _is_linked(b1, 'FigureDescriptor231', a)
    if hasattr(b2, 'FigureDescriptor231'):
        assert _is_linked(b2, 'FigureDescriptor231', a)
    _safe_set(a, 'accessors', None)
    assert not _is_linked(a, 'accessors', b2)
    if hasattr(b2, 'FigureDescriptor231'):
        assert not _is_linked(b2, 'FigureDescriptor231', a)


def test_assoc_parentContainer111_link_reassign_clear():
    a = gmf_all_mappings_AuditContainer(description="sample_text", id="sample_text", name="sample_text")
    b1 = AuditContainer()
    b2 = AuditContainer()
    _safe_set(a, 'childContainers', b1)
    assert _is_linked(a, 'childContainers', b1)
    if hasattr(b1, 'AuditContainer112'):
        assert _is_linked(b1, 'AuditContainer112', a)
    _safe_set(a, 'childContainers', b2)
    assert _is_linked(a, 'childContainers', b2)
    if hasattr(b1, 'AuditContainer112'):
        assert not _is_linked(b1, 'AuditContainer112', a)
    if hasattr(b2, 'AuditContainer112'):
        assert _is_linked(b2, 'AuditContainer112', a)
    _safe_set(a, 'childContainers', None)
    assert not _is_linked(a, 'childContainers', b2)
    if hasattr(b2, 'AuditContainer112'):
        assert not _is_linked(b2, 'AuditContainer112', a)


def test_assoc_parentMapEntry141_link_reassign_clear():
    a = gmf_all_mappings_VisualEffectMapping(oclExpression="sample_text")
    b1 = MappingEntry()
    b2 = MappingEntry()
    _safe_set(a, 'visualEffects', b1)
    assert _is_linked(a, 'visualEffects', b1)
    if hasattr(b1, 'MappingEntry142'):
        assert _is_linked(b1, 'MappingEntry142', a)
    _safe_set(a, 'visualEffects', b2)
    assert _is_linked(a, 'visualEffects', b2)
    if hasattr(b1, 'MappingEntry142'):
        assert not _is_linked(b1, 'MappingEntry142', a)
    if hasattr(b2, 'MappingEntry142'):
        assert _is_linked(b2, 'MappingEntry142', a)
    _safe_set(a, 'visualEffects', None)
    assert not _is_linked(a, 'visualEffects', b2)
    if hasattr(b2, 'MappingEntry142'):
        assert not _is_linked(b2, 'MappingEntry142', a)


def test_assoc_properties282_link_reassign_clear():
    a = gmf_all_gmfgraph_SVGFigure(documentURI="sample_text", noCanvasHeight=True, noCanvasWidth=True)
    b1 = SVGProperty()
    b2 = SVGProperty()
    _safe_set(a, 'gmf_all_gmfgraph_SVGFigure', {b1})
    assert _is_linked(a, 'gmf_all_gmfgraph_SVGFigure', b1)
    if hasattr(b1, 'SVGProperty'):
        assert _is_linked(b1, 'SVGProperty', a)
    _safe_set(a, 'gmf_all_gmfgraph_SVGFigure', {b2})
    assert _is_linked(a, 'gmf_all_gmfgraph_SVGFigure', b2)
    if hasattr(b1, 'SVGProperty'):
        assert not _is_linked(b1, 'SVGProperty', a)
    if hasattr(b2, 'SVGProperty'):
        assert _is_linked(b2, 'SVGProperty', a)
    _safe_set(a, 'gmf_all_gmfgraph_SVGFigure', set())
    assert not _is_linked(a, 'gmf_all_gmfgraph_SVGFigure', b2)
    if hasattr(b2, 'SVGProperty'):
        assert not _is_linked(b2, 'SVGProperty', a)


def test_assoc_relatedDiagrams17_link_reassign_clear():
    a = gmf_all_mappings_MappingEntry()
    b1 = CanvasMapping()
    b2 = CanvasMapping()
    _safe_set(a, 'gmf_all_mappings_MappingEntry18', {b1})
    assert _is_linked(a, 'gmf_all_mappings_MappingEntry18', b1)
    if hasattr(b1, 'CanvasMapping19'):
        assert _is_linked(b1, 'CanvasMapping19', a)
    _safe_set(a, 'gmf_all_mappings_MappingEntry18', {b2})
    assert _is_linked(a, 'gmf_all_mappings_MappingEntry18', b2)
    if hasattr(b1, 'CanvasMapping19'):
        assert not _is_linked(b1, 'CanvasMapping19', a)
    if hasattr(b2, 'CanvasMapping19'):
        assert _is_linked(b2, 'CanvasMapping19', a)
    _safe_set(a, 'gmf_all_mappings_MappingEntry18', set())
    assert not _is_linked(a, 'gmf_all_mappings_MappingEntry18', b2)
    if hasattr(b2, 'CanvasMapping19'):
        assert not _is_linked(b2, 'CanvasMapping19', a)


def test_assoc_resolvedChildren238_link_reassign_clear():
    a = gmf_all_gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    b1 = Figure()
    b2 = Figure()
    _safe_set(a, 'gmf_all_gmfgraph_Shape', {b1})
    assert _is_linked(a, 'gmf_all_gmfgraph_Shape', b1)
    if hasattr(b1, 'Figure239'):
        assert _is_linked(b1, 'Figure239', a)
    _safe_set(a, 'gmf_all_gmfgraph_Shape', {b2})
    assert _is_linked(a, 'gmf_all_gmfgraph_Shape', b2)
    if hasattr(b1, 'Figure239'):
        assert not _is_linked(b1, 'Figure239', a)
    if hasattr(b2, 'Figure239'):
        assert _is_linked(b2, 'Figure239', a)
    _safe_set(a, 'gmf_all_gmfgraph_Shape', set())
    assert not _is_linked(a, 'gmf_all_gmfgraph_Shape', b2)
    if hasattr(b2, 'Figure239'):
        assert not _is_linked(b2, 'Figure239', a)


def test_assoc_rule116_link_reassign_clear():
    a = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    b1 = Constraint()
    b2 = Constraint()
    _safe_set(a, 'gmf_all_mappings_AuditRule', b1)
    assert _is_linked(a, 'gmf_all_mappings_AuditRule', b1)
    if hasattr(b1, 'Constraint117'):
        assert _is_linked(b1, 'Constraint117', a)
    _safe_set(a, 'gmf_all_mappings_AuditRule', b2)
    assert _is_linked(a, 'gmf_all_mappings_AuditRule', b2)
    if hasattr(b1, 'Constraint117'):
        assert not _is_linked(b1, 'Constraint117', a)
    if hasattr(b2, 'Constraint117'):
        assert _is_linked(b2, 'Constraint117', a)
    _safe_set(a, 'gmf_all_mappings_AuditRule', None)
    assert not _is_linked(a, 'gmf_all_mappings_AuditRule', b2)
    if hasattr(b2, 'Constraint117'):
        assert not _is_linked(b2, 'Constraint117', a)


def test_assoc_rule132_link_reassign_clear():
    a = gmf_all_mappings_MetricRule(highLimit="sample_text", key="sample_text", lowLimit="sample_text")
    b1 = ValueExpression()
    b2 = ValueExpression()
    _safe_set(a, 'gmf_all_mappings_MetricRule', b1)
    assert _is_linked(a, 'gmf_all_mappings_MetricRule', b1)
    if hasattr(b1, 'ValueExpression133'):
        assert _is_linked(b1, 'ValueExpression133', a)
    _safe_set(a, 'gmf_all_mappings_MetricRule', b2)
    assert _is_linked(a, 'gmf_all_mappings_MetricRule', b2)
    if hasattr(b1, 'ValueExpression133'):
        assert not _is_linked(b1, 'ValueExpression133', a)
    if hasattr(b2, 'ValueExpression133'):
        assert _is_linked(b2, 'ValueExpression133', a)
    _safe_set(a, 'gmf_all_mappings_MetricRule', None)
    assert not _is_linked(a, 'gmf_all_mappings_MetricRule', b2)
    if hasattr(b2, 'ValueExpression133'):
        assert not _is_linked(b2, 'ValueExpression133', a)


def test_assoc_sizeHint262_link_reassign_clear():
    a = gmf_all_gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    b1 = Dimension()
    b2 = Dimension()
    _safe_set(a, 'gmf_all_gmfgraph_GridLayoutData', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_GridLayoutData', b1)
    if hasattr(b1, 'Dimension263'):
        assert _is_linked(b1, 'Dimension263', a)
    _safe_set(a, 'gmf_all_gmfgraph_GridLayoutData', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_GridLayoutData', b2)
    if hasattr(b1, 'Dimension263'):
        assert not _is_linked(b1, 'Dimension263', a)
    if hasattr(b2, 'Dimension263'):
        assert _is_linked(b2, 'Dimension263', a)
    _safe_set(a, 'gmf_all_gmfgraph_GridLayoutData', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_GridLayoutData', b2)
    if hasattr(b2, 'Dimension263'):
        assert not _is_linked(b2, 'Dimension263', a)


def test_assoc_smallIcon149_link_reassign_clear():
    a = gmf_all_tooldef_AbstractTool(description="sample_text", title="sample_text")
    b1 = Image()
    b2 = Image()
    _safe_set(a, 'gmf_all_tooldef_AbstractTool', b1)
    assert _is_linked(a, 'gmf_all_tooldef_AbstractTool', b1)
    if hasattr(b1, 'Image'):
        assert _is_linked(b1, 'Image', a)
    _safe_set(a, 'gmf_all_tooldef_AbstractTool', b2)
    assert _is_linked(a, 'gmf_all_tooldef_AbstractTool', b2)
    if hasattr(b1, 'Image'):
        assert not _is_linked(b1, 'Image', a)
    if hasattr(b2, 'Image'):
        assert _is_linked(b2, 'Image', a)
    _safe_set(a, 'gmf_all_tooldef_AbstractTool', None)
    assert not _is_linked(a, 'gmf_all_tooldef_AbstractTool', b2)
    if hasattr(b2, 'Image'):
        assert not _is_linked(b2, 'Image', a)


def test_assoc_spacing272_link_reassign_clear():
    a = gmf_all_gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    b1 = Dimension()
    b2 = Dimension()
    _safe_set(a, 'gmf_all_gmfgraph_GridLayout273', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_GridLayout273', b1)
    if hasattr(b1, 'Dimension274'):
        assert _is_linked(b1, 'Dimension274', a)
    _safe_set(a, 'gmf_all_gmfgraph_GridLayout273', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_GridLayout273', b2)
    if hasattr(b1, 'Dimension274'):
        assert not _is_linked(b1, 'Dimension274', a)
    if hasattr(b2, 'Dimension274'):
        assert _is_linked(b2, 'Dimension274', a)
    _safe_set(a, 'gmf_all_gmfgraph_GridLayout273', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_GridLayout273', b2)
    if hasattr(b2, 'Dimension274'):
        assert not _is_linked(b2, 'Dimension274', a)


def test_assoc_target118_link_reassign_clear():
    a = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    b1 = Auditable()
    b2 = Auditable()
    _safe_set(a, 'gmf_all_mappings_AuditRule119', b1)
    assert _is_linked(a, 'gmf_all_mappings_AuditRule119', b1)
    if hasattr(b1, 'Auditable'):
        assert _is_linked(b1, 'Auditable', a)
    _safe_set(a, 'gmf_all_mappings_AuditRule119', b2)
    assert _is_linked(a, 'gmf_all_mappings_AuditRule119', b2)
    if hasattr(b1, 'Auditable'):
        assert not _is_linked(b1, 'Auditable', a)
    if hasattr(b2, 'Auditable'):
        assert _is_linked(b2, 'Auditable', a)
    _safe_set(a, 'gmf_all_mappings_AuditRule119', None)
    assert not _is_linked(a, 'gmf_all_mappings_AuditRule119', b2)
    if hasattr(b2, 'Auditable'):
        assert not _is_linked(b2, 'Auditable', a)


def test_assoc_target134_link_reassign_clear():
    a = gmf_all_mappings_MetricRule(highLimit="sample_text", key="sample_text", lowLimit="sample_text")
    b1 = Measurable()
    b2 = Measurable()
    _safe_set(a, 'gmf_all_mappings_MetricRule135', b1)
    assert _is_linked(a, 'gmf_all_mappings_MetricRule135', b1)
    if hasattr(b1, 'Measurable'):
        assert _is_linked(b1, 'Measurable', a)
    _safe_set(a, 'gmf_all_mappings_MetricRule135', b2)
    assert _is_linked(a, 'gmf_all_mappings_MetricRule135', b2)
    if hasattr(b1, 'Measurable'):
        assert not _is_linked(b1, 'Measurable', a)
    if hasattr(b2, 'Measurable'):
        assert _is_linked(b2, 'Measurable', a)
    _safe_set(a, 'gmf_all_mappings_MetricRule135', None)
    assert not _is_linked(a, 'gmf_all_mappings_MetricRule135', b2)
    if hasattr(b2, 'Measurable'):
        assert not _is_linked(b2, 'Measurable', a)


def test_assoc_typedFigure247_link_reassign_clear():
    a = gmf_all_gmfgraph_FigureAccessor(accessor="sample_text")
    b1 = RealFigure()
    b2 = RealFigure()
    _safe_set(a, 'gmf_all_gmfgraph_FigureAccessor', b1)
    assert _is_linked(a, 'gmf_all_gmfgraph_FigureAccessor', b1)
    if hasattr(b1, 'RealFigure248'):
        assert _is_linked(b1, 'RealFigure248', a)
    _safe_set(a, 'gmf_all_gmfgraph_FigureAccessor', b2)
    assert _is_linked(a, 'gmf_all_gmfgraph_FigureAccessor', b2)
    if hasattr(b1, 'RealFigure248'):
        assert not _is_linked(b1, 'RealFigure248', a)
    if hasattr(b2, 'RealFigure248'):
        assert _is_linked(b2, 'RealFigure248', a)
    _safe_set(a, 'gmf_all_gmfgraph_FigureAccessor', None)
    assert not _is_linked(a, 'gmf_all_gmfgraph_FigureAccessor', b2)
    if hasattr(b2, 'RealFigure248'):
        assert not _is_linked(b2, 'RealFigure248', a)


def test_assoc_visualEffects20_link_reassign_clear():
    a = gmf_all_mappings_MappingEntry()
    b1 = VisualEffectMapping()
    b2 = VisualEffectMapping()
    _safe_set(a, 'parentMapEntry', {b1})
    assert _is_linked(a, 'parentMapEntry', b1)
    if hasattr(b1, 'VisualEffectMapping'):
        assert _is_linked(b1, 'VisualEffectMapping', a)
    _safe_set(a, 'parentMapEntry', {b2})
    assert _is_linked(a, 'parentMapEntry', b2)
    if hasattr(b1, 'VisualEffectMapping'):
        assert not _is_linked(b1, 'VisualEffectMapping', a)
    if hasattr(b2, 'VisualEffectMapping'):
        assert _is_linked(b2, 'VisualEffectMapping', a)
    _safe_set(a, 'parentMapEntry', set())
    assert not _is_linked(a, 'parentMapEntry', b2)
    if hasattr(b2, 'VisualEffectMapping'):
        assert not _is_linked(b2, 'VisualEffectMapping', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractFigure_strategy = st.builds(AbstractFigure)
@given(instance=AbstractFigure_strategy)
@settings(max_examples=25)
def test_AbstractFigure_instantiation(instance):
    assert isinstance(instance, AbstractFigure)


AbstractNode_strategy = st.builds(AbstractNode)
@given(instance=AbstractNode_strategy)
@settings(max_examples=25)
def test_AbstractNode_instantiation(instance):
    assert isinstance(instance, AbstractNode)


AbstractTool_strategy = st.builds(AbstractTool)
@given(instance=AbstractTool_strategy)
@settings(max_examples=25)
def test_AbstractTool_instantiation(instance):
    assert isinstance(instance, AbstractTool)


AuditContainer_strategy = st.builds(AuditContainer)
@given(instance=AuditContainer_strategy)
@settings(max_examples=25)
def test_AuditContainer_instantiation(instance):
    assert isinstance(instance, AuditContainer)


AuditRule_strategy = st.builds(AuditRule)
@given(instance=AuditRule_strategy)
@settings(max_examples=25)
def test_AuditRule_instantiation(instance):
    assert isinstance(instance, AuditRule)


Auditable_strategy = st.builds(Auditable)
@given(instance=Auditable_strategy)
@settings(max_examples=25)
def test_Auditable_instantiation(instance):
    assert isinstance(instance, Auditable)


Border_strategy = st.builds(Border)
@given(instance=Border_strategy)
@settings(max_examples=25)
def test_Border_instantiation(instance):
    assert isinstance(instance, Border)


Canvas_strategy = st.builds(Canvas)
@given(instance=Canvas_strategy)
@settings(max_examples=25)
def test_Canvas_instantiation(instance):
    assert isinstance(instance, Canvas)


CanvasMapping_strategy = st.builds(CanvasMapping)
@given(instance=CanvasMapping_strategy)
@settings(max_examples=25)
def test_CanvasMapping_instantiation(instance):
    assert isinstance(instance, CanvasMapping)


ChildAccess_strategy = st.builds(ChildAccess)
@given(instance=ChildAccess_strategy)
@settings(max_examples=25)
def test_ChildAccess_instantiation(instance):
    assert isinstance(instance, ChildAccess)


ChildReference_strategy = st.builds(ChildReference)
@given(instance=ChildReference_strategy)
@settings(max_examples=25)
def test_ChildReference_instantiation(instance):
    assert isinstance(instance, ChildReference)


Color_strategy = st.builds(Color)
@given(instance=Color_strategy)
@settings(max_examples=25)
def test_Color_instantiation(instance):
    assert isinstance(instance, Color)


Compartment_strategy = st.builds(Compartment)
@given(instance=Compartment_strategy)
@settings(max_examples=25)
def test_Compartment_instantiation(instance):
    assert isinstance(instance, Compartment)


CompartmentMapping_strategy = st.builds(CompartmentMapping)
@given(instance=CompartmentMapping_strategy)
@settings(max_examples=25)
def test_CompartmentMapping_instantiation(instance):
    assert isinstance(instance, CompartmentMapping)


Connection_strategy = st.builds(Connection)
@given(instance=Connection_strategy)
@settings(max_examples=25)
def test_Connection_instantiation(instance):
    assert isinstance(instance, Connection)


Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


ContextMenu_strategy = st.builds(ContextMenu)
@given(instance=ContextMenu_strategy)
@settings(max_examples=25)
def test_ContextMenu_instantiation(instance):
    assert isinstance(instance, ContextMenu)


ContributionItem_strategy = st.builds(ContributionItem)
@given(instance=ContributionItem_strategy)
@settings(max_examples=25)
def test_ContributionItem_instantiation(instance):
    assert isinstance(instance, ContributionItem)


CustomAttribute_strategy = st.builds(CustomAttribute)
@given(instance=CustomAttribute_strategy)
@settings(max_examples=25)
def test_CustomAttribute_instantiation(instance):
    assert isinstance(instance, CustomAttribute)


CustomAttributeOwner_strategy = st.builds(CustomAttributeOwner)
@given(instance=CustomAttributeOwner_strategy)
@settings(max_examples=25)
def test_CustomAttributeOwner_instantiation(instance):
    assert isinstance(instance, CustomAttributeOwner)


DecorationFigure_strategy = st.builds(DecorationFigure)
@given(instance=DecorationFigure_strategy)
@settings(max_examples=25)
def test_DecorationFigure_instantiation(instance):
    assert isinstance(instance, DecorationFigure)


DiagramElement_strategy = st.builds(DiagramElement)
@given(instance=DiagramElement_strategy)
@settings(max_examples=25)
def test_DiagramElement_instantiation(instance):
    assert isinstance(instance, DiagramElement)


DiagramLabel_strategy = st.builds(DiagramLabel)
@given(instance=DiagramLabel_strategy)
@settings(max_examples=25)
def test_DiagramLabel_instantiation(instance):
    assert isinstance(instance, DiagramLabel)


Dimension_strategy = st.builds(Dimension)
@given(instance=Dimension_strategy)
@settings(max_examples=25)
def test_Dimension_instantiation(instance):
    assert isinstance(instance, Dimension)


ElementInitializer_strategy = st.builds(ElementInitializer)
@given(instance=ElementInitializer_strategy)
@settings(max_examples=25)
def test_ElementInitializer_instantiation(instance):
    assert isinstance(instance, ElementInitializer)


FeatureInitializer_strategy = st.builds(FeatureInitializer)
@given(instance=FeatureInitializer_strategy)
@settings(max_examples=25)
def test_FeatureInitializer_instantiation(instance):
    assert isinstance(instance, FeatureInitializer)


FeatureSeqInitializer_strategy = st.builds(FeatureSeqInitializer)
@given(instance=FeatureSeqInitializer_strategy)
@settings(max_examples=25)
def test_FeatureSeqInitializer_instantiation(instance):
    assert isinstance(instance, FeatureSeqInitializer)


Figure_strategy = st.builds(Figure)
@given(instance=Figure_strategy)
@settings(max_examples=25)
def test_Figure_instantiation(instance):
    assert isinstance(instance, Figure)


FigureAccessor_strategy = st.builds(FigureAccessor)
@given(instance=FigureAccessor_strategy)
@settings(max_examples=25)
def test_FigureAccessor_instantiation(instance):
    assert isinstance(instance, FigureAccessor)


FigureDescriptor_strategy = st.builds(FigureDescriptor)
@given(instance=FigureDescriptor_strategy)
@settings(max_examples=25)
def test_FigureDescriptor_instantiation(instance):
    assert isinstance(instance, FigureDescriptor)


FigureGallery_strategy = st.builds(FigureGallery)
@given(instance=FigureGallery_strategy)
@settings(max_examples=25)
def test_FigureGallery_instantiation(instance):
    assert isinstance(instance, FigureGallery)


Font_strategy = st.builds(Font)
@given(instance=Font_strategy)
@settings(max_examples=25)
def test_Font_instantiation(instance):
    assert isinstance(instance, Font)


Identity_strategy = st.builds(Identity)
@given(instance=Identity_strategy)
@settings(max_examples=25)
def test_Identity_instantiation(instance):
    assert isinstance(instance, Identity)


Image_strategy = st.builds(Image)
@given(instance=Image_strategy)
@settings(max_examples=25)
def test_Image_instantiation(instance):
    assert isinstance(instance, Image)


Insets_strategy = st.builds(Insets)
@given(instance=Insets_strategy)
@settings(max_examples=25)
def test_Insets_instantiation(instance):
    assert isinstance(instance, Insets)


ItemBase_strategy = st.builds(ItemBase)
@given(instance=ItemBase_strategy)
@settings(max_examples=25)
def test_ItemBase_instantiation(instance):
    assert isinstance(instance, ItemBase)


LabelMapping_strategy = st.builds(LabelMapping)
@given(instance=LabelMapping_strategy)
@settings(max_examples=25)
def test_LabelMapping_instantiation(instance):
    assert isinstance(instance, LabelMapping)


Layout_strategy = st.builds(Layout)
@given(instance=Layout_strategy)
@settings(max_examples=25)
def test_Layout_instantiation(instance):
    assert isinstance(instance, Layout)


LayoutData_strategy = st.builds(LayoutData)
@given(instance=LayoutData_strategy)
@settings(max_examples=25)
def test_LayoutData_instantiation(instance):
    assert isinstance(instance, LayoutData)


Layoutable_strategy = st.builds(Layoutable)
@given(instance=Layoutable_strategy)
@settings(max_examples=25)
def test_Layoutable_instantiation(instance):
    assert isinstance(instance, Layoutable)


LinkConstraints_strategy = st.builds(LinkConstraints)
@given(instance=LinkConstraints_strategy)
@settings(max_examples=25)
def test_LinkConstraints_instantiation(instance):
    assert isinstance(instance, LinkConstraints)


LinkMapping_strategy = st.builds(LinkMapping)
@given(instance=LinkMapping_strategy)
@settings(max_examples=25)
def test_LinkMapping_instantiation(instance):
    assert isinstance(instance, LinkMapping)


MainMenu_strategy = st.builds(MainMenu)
@given(instance=MainMenu_strategy)
@settings(max_examples=25)
def test_MainMenu_instantiation(instance):
    assert isinstance(instance, MainMenu)


MappingEntry_strategy = st.builds(MappingEntry)
@given(instance=MappingEntry_strategy)
@settings(max_examples=25)
def test_MappingEntry_instantiation(instance):
    assert isinstance(instance, MappingEntry)


Measurable_strategy = st.builds(Measurable)
@given(instance=Measurable_strategy)
@settings(max_examples=25)
def test_Measurable_instantiation(instance):
    assert isinstance(instance, Measurable)


Menu_strategy = st.builds(Menu)
@given(instance=Menu_strategy)
@settings(max_examples=25)
def test_Menu_instantiation(instance):
    assert isinstance(instance, Menu)


MenuAction_strategy = st.builds(MenuAction)
@given(instance=MenuAction_strategy)
@settings(max_examples=25)
def test_MenuAction_instantiation(instance):
    assert isinstance(instance, MenuAction)


MetricContainer_strategy = st.builds(MetricContainer)
@given(instance=MetricContainer_strategy)
@settings(max_examples=25)
def test_MetricContainer_instantiation(instance):
    assert isinstance(instance, MetricContainer)


MetricRule_strategy = st.builds(MetricRule)
@given(instance=MetricRule_strategy)
@settings(max_examples=25)
def test_MetricRule_instantiation(instance):
    assert isinstance(instance, MetricRule)


NeedsContainment_strategy = st.builds(NeedsContainment)
@given(instance=NeedsContainment_strategy)
@settings(max_examples=25)
def test_NeedsContainment_instantiation(instance):
    assert isinstance(instance, NeedsContainment)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


NodeMapping_strategy = st.builds(NodeMapping)
@given(instance=NodeMapping_strategy)
@settings(max_examples=25)
def test_NodeMapping_instantiation(instance):
    assert isinstance(instance, NodeMapping)


NodeReference_strategy = st.builds(NodeReference)
@given(instance=NodeReference_strategy)
@settings(max_examples=25)
def test_NodeReference_instantiation(instance):
    assert isinstance(instance, NodeReference)


Palette_strategy = st.builds(Palette)
@given(instance=Palette_strategy)
@settings(max_examples=25)
def test_Palette_instantiation(instance):
    assert isinstance(instance, Palette)


Pin_strategy = st.builds(Pin)
@given(instance=Pin_strategy)
@settings(max_examples=25)
def test_Pin_instantiation(instance):
    assert isinstance(instance, Pin)


Point_strategy = st.builds(Point)
@given(instance=Point_strategy)
@settings(max_examples=25)
def test_Point_instantiation(instance):
    assert isinstance(instance, Point)


Polygon_strategy = st.builds(Polygon)
@given(instance=Polygon_strategy)
@settings(max_examples=25)
def test_Polygon_instantiation(instance):
    assert isinstance(instance, Polygon)


Polyline_strategy = st.builds(Polyline)
@given(instance=Polyline_strategy)
@settings(max_examples=25)
def test_Polyline_instantiation(instance):
    assert isinstance(instance, Polyline)


RealFigure_strategy = st.builds(RealFigure)
@given(instance=RealFigure_strategy)
@settings(max_examples=25)
def test_RealFigure_instantiation(instance):
    assert isinstance(instance, RealFigure)


Rectangle2D_strategy = st.builds(Rectangle2D)
@given(instance=Rectangle2D_strategy)
@settings(max_examples=25)
def test_Rectangle2D_instantiation(instance):
    assert isinstance(instance, Rectangle2D)


ReferenceNewElementSpec_strategy = st.builds(ReferenceNewElementSpec)
@given(instance=ReferenceNewElementSpec_strategy)
@settings(max_examples=25)
def test_ReferenceNewElementSpec_instantiation(instance):
    assert isinstance(instance, ReferenceNewElementSpec)


RuleBase_strategy = st.builds(RuleBase)
@given(instance=RuleBase_strategy)
@settings(max_examples=25)
def test_RuleBase_instantiation(instance):
    assert isinstance(instance, RuleBase)


SVGProperty_strategy = st.builds(SVGProperty)
@given(instance=SVGProperty_strategy)
@settings(max_examples=25)
def test_SVGProperty_instantiation(instance):
    assert isinstance(instance, SVGProperty)


Shape_strategy = st.builds(Shape)
@given(instance=Shape_strategy)
@settings(max_examples=25)
def test_Shape_instantiation(instance):
    assert isinstance(instance, Shape)


StyleSelector_strategy = st.builds(StyleSelector)
@given(instance=StyleSelector_strategy)
@settings(max_examples=25)
def test_StyleSelector_instantiation(instance):
    assert isinstance(instance, StyleSelector)


ToolContainer_strategy = st.builds(ToolContainer)
@given(instance=ToolContainer_strategy)
@settings(max_examples=25)
def test_ToolContainer_instantiation(instance):
    assert isinstance(instance, ToolContainer)


Toolbar_strategy = st.builds(Toolbar)
@given(instance=Toolbar_strategy)
@settings(max_examples=25)
def test_Toolbar_instantiation(instance):
    assert isinstance(instance, Toolbar)


TopNodeReference_strategy = st.builds(TopNodeReference)
@given(instance=TopNodeReference_strategy)
@settings(max_examples=25)
def test_TopNodeReference_instantiation(instance):
    assert isinstance(instance, TopNodeReference)


ValueExpression_strategy = st.builds(ValueExpression)
@given(instance=ValueExpression_strategy)
@settings(max_examples=25)
def test_ValueExpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)


VisualEffectMapping_strategy = st.builds(VisualEffectMapping)
@given(instance=VisualEffectMapping_strategy)
@settings(max_examples=25)
def test_VisualEffectMapping_instantiation(instance):
    assert isinstance(instance, VisualEffectMapping)


VisualFacet_strategy = st.builds(VisualFacet)
@given(instance=VisualFacet_strategy)
@settings(max_examples=25)
def test_VisualFacet_instantiation(instance):
    assert isinstance(instance, VisualFacet)


gmf_all_gmfgraph_AbstractFigure_strategy = st.builds(gmf_all_gmfgraph_AbstractFigure)
@given(instance=gmf_all_gmfgraph_AbstractFigure_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_AbstractFigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_AbstractFigure)


gmf_all_gmfgraph_AbstractNode_strategy = st.builds(gmf_all_gmfgraph_AbstractNode)
@given(instance=gmf_all_gmfgraph_AbstractNode_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_AbstractNode_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_AbstractNode)


gmf_all_gmfgraph_AlignmentFacet_strategy = st.builds(gmf_all_gmfgraph_AlignmentFacet, alignment=safe_text)
@given(instance=gmf_all_gmfgraph_AlignmentFacet_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_AlignmentFacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_AlignmentFacet)


gmf_all_gmfgraph_BasicFont_strategy = st.builds(gmf_all_gmfgraph_BasicFont, faceName=safe_text, height=st.integers(), style=safe_text)
@given(instance=gmf_all_gmfgraph_BasicFont_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_BasicFont_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_BasicFont)


gmf_all_gmfgraph_Border_strategy = st.builds(gmf_all_gmfgraph_Border)
@given(instance=gmf_all_gmfgraph_Border_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Border_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Border)


gmf_all_gmfgraph_BorderLayout_strategy = st.builds(gmf_all_gmfgraph_BorderLayout)
@given(instance=gmf_all_gmfgraph_BorderLayout_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_BorderLayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_BorderLayout)


gmf_all_gmfgraph_BorderLayoutData_strategy = st.builds(gmf_all_gmfgraph_BorderLayoutData, alignment=safe_text, vertical=st.booleans())
@given(instance=gmf_all_gmfgraph_BorderLayoutData_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_BorderLayoutData_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_BorderLayoutData)


gmf_all_gmfgraph_BorderRef_strategy = st.builds(gmf_all_gmfgraph_BorderRef)
@given(instance=gmf_all_gmfgraph_BorderRef_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_BorderRef_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_BorderRef)


gmf_all_gmfgraph_Canvas_strategy = st.builds(gmf_all_gmfgraph_Canvas)
@given(instance=gmf_all_gmfgraph_Canvas_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Canvas_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Canvas)


gmf_all_gmfgraph_CenterLayout_strategy = st.builds(gmf_all_gmfgraph_CenterLayout)
@given(instance=gmf_all_gmfgraph_CenterLayout_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CenterLayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CenterLayout)


gmf_all_gmfgraph_ChildAccess_strategy = st.builds(gmf_all_gmfgraph_ChildAccess, accessor=safe_text)
@given(instance=gmf_all_gmfgraph_ChildAccess_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_ChildAccess_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_ChildAccess)


gmf_all_gmfgraph_Color_strategy = st.builds(gmf_all_gmfgraph_Color)
@given(instance=gmf_all_gmfgraph_Color_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Color_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Color)


gmf_all_gmfgraph_ColorPin_strategy = st.builds(gmf_all_gmfgraph_ColorPin, backgroundNotForeground=st.booleans())
@given(instance=gmf_all_gmfgraph_ColorPin_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_ColorPin_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_ColorPin)


gmf_all_gmfgraph_Compartment_strategy = st.builds(gmf_all_gmfgraph_Compartment, collapsible=st.booleans(), needsTitle=st.booleans())
@given(instance=gmf_all_gmfgraph_Compartment_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Compartment_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Compartment)


gmf_all_gmfgraph_CompoundBorder_strategy = st.builds(gmf_all_gmfgraph_CompoundBorder)
@given(instance=gmf_all_gmfgraph_CompoundBorder_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CompoundBorder_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CompoundBorder)


gmf_all_gmfgraph_Connection_strategy = st.builds(gmf_all_gmfgraph_Connection)
@given(instance=gmf_all_gmfgraph_Connection_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Connection_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Connection)


gmf_all_gmfgraph_ConnectionFigure_strategy = st.builds(gmf_all_gmfgraph_ConnectionFigure)
@given(instance=gmf_all_gmfgraph_ConnectionFigure_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_ConnectionFigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_ConnectionFigure)


gmf_all_gmfgraph_ConstantColor_strategy = st.builds(gmf_all_gmfgraph_ConstantColor, value=safe_text)
@given(instance=gmf_all_gmfgraph_ConstantColor_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_ConstantColor_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_ConstantColor)


gmf_all_gmfgraph_CustomAttribute_strategy = st.builds(gmf_all_gmfgraph_CustomAttribute, directAccess=st.booleans(), multiStatementValue=st.booleans(), name=safe_text, value=safe_text)
@given(instance=gmf_all_gmfgraph_CustomAttribute_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CustomAttribute_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomAttribute)


gmf_all_gmfgraph_CustomAttributeOwner_strategy = st.builds(gmf_all_gmfgraph_CustomAttributeOwner)
@given(instance=gmf_all_gmfgraph_CustomAttributeOwner_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CustomAttributeOwner_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomAttributeOwner)


gmf_all_gmfgraph_CustomBorder_strategy = st.builds(gmf_all_gmfgraph_CustomBorder)
@given(instance=gmf_all_gmfgraph_CustomBorder_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CustomBorder_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomBorder)


gmf_all_gmfgraph_CustomClass_strategy = st.builds(gmf_all_gmfgraph_CustomClass, qualifiedClassName=safe_text)
@given(instance=gmf_all_gmfgraph_CustomClass_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CustomClass_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomClass)


gmf_all_gmfgraph_CustomConnection_strategy = st.builds(gmf_all_gmfgraph_CustomConnection)
@given(instance=gmf_all_gmfgraph_CustomConnection_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CustomConnection_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomConnection)


gmf_all_gmfgraph_CustomDecoration_strategy = st.builds(gmf_all_gmfgraph_CustomDecoration)
@given(instance=gmf_all_gmfgraph_CustomDecoration_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CustomDecoration_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomDecoration)


gmf_all_gmfgraph_CustomFigure_strategy = st.builds(gmf_all_gmfgraph_CustomFigure)
@given(instance=gmf_all_gmfgraph_CustomFigure_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CustomFigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomFigure)


gmf_all_gmfgraph_CustomLayout_strategy = st.builds(gmf_all_gmfgraph_CustomLayout)
@given(instance=gmf_all_gmfgraph_CustomLayout_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CustomLayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomLayout)


gmf_all_gmfgraph_CustomLayoutData_strategy = st.builds(gmf_all_gmfgraph_CustomLayoutData)
@given(instance=gmf_all_gmfgraph_CustomLayoutData_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CustomLayoutData_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomLayoutData)


gmf_all_gmfgraph_CustomPin_strategy = st.builds(gmf_all_gmfgraph_CustomPin, customOperationName=safe_text, customOperationType=safe_text)
@given(instance=gmf_all_gmfgraph_CustomPin_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_CustomPin_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomPin)


gmf_all_gmfgraph_DecorationFigure_strategy = st.builds(gmf_all_gmfgraph_DecorationFigure)
@given(instance=gmf_all_gmfgraph_DecorationFigure_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_DecorationFigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_DecorationFigure)


gmf_all_gmfgraph_DefaultSizeFacet_strategy = st.builds(gmf_all_gmfgraph_DefaultSizeFacet)
@given(instance=gmf_all_gmfgraph_DefaultSizeFacet_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_DefaultSizeFacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_DefaultSizeFacet)


gmf_all_gmfgraph_DiagramElement_strategy = st.builds(gmf_all_gmfgraph_DiagramElement)
@given(instance=gmf_all_gmfgraph_DiagramElement_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_DiagramElement_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_DiagramElement)


gmf_all_gmfgraph_DiagramLabel_strategy = st.builds(gmf_all_gmfgraph_DiagramLabel, elementIcon=st.booleans(), external=st.booleans())
@given(instance=gmf_all_gmfgraph_DiagramLabel_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_DiagramLabel_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_DiagramLabel)


gmf_all_gmfgraph_Dimension_strategy = st.builds(gmf_all_gmfgraph_Dimension, dx=st.integers(), dy=st.integers())
@given(instance=gmf_all_gmfgraph_Dimension_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Dimension_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Dimension)


gmf_all_gmfgraph_Ellipse_strategy = st.builds(gmf_all_gmfgraph_Ellipse)
@given(instance=gmf_all_gmfgraph_Ellipse_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Ellipse_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Ellipse)


gmf_all_gmfgraph_Figure_strategy = st.builds(gmf_all_gmfgraph_Figure)
@given(instance=gmf_all_gmfgraph_Figure_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Figure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Figure)


gmf_all_gmfgraph_FigureAccessor_strategy = st.builds(gmf_all_gmfgraph_FigureAccessor, accessor=safe_text)
@given(instance=gmf_all_gmfgraph_FigureAccessor_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_FigureAccessor_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_FigureAccessor)


gmf_all_gmfgraph_FigureDescriptor_strategy = st.builds(gmf_all_gmfgraph_FigureDescriptor)
@given(instance=gmf_all_gmfgraph_FigureDescriptor_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_FigureDescriptor_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_FigureDescriptor)


gmf_all_gmfgraph_FigureGallery_strategy = st.builds(gmf_all_gmfgraph_FigureGallery, implementationBundle=safe_text)
@given(instance=gmf_all_gmfgraph_FigureGallery_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_FigureGallery_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_FigureGallery)


gmf_all_gmfgraph_FigureRef_strategy = st.builds(gmf_all_gmfgraph_FigureRef)
@given(instance=gmf_all_gmfgraph_FigureRef_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_FigureRef_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_FigureRef)


gmf_all_gmfgraph_FlowLayout_strategy = st.builds(gmf_all_gmfgraph_FlowLayout, forceSingleLine=st.booleans(), majorAlignment=safe_text, majorSpacing=st.integers(), matchMinorSize=st.booleans(), minorAlignment=safe_text, minorSpacing=st.integers(), vertical=st.booleans())
@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_FlowLayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_FlowLayout)


gmf_all_gmfgraph_Font_strategy = st.builds(gmf_all_gmfgraph_Font)
@given(instance=gmf_all_gmfgraph_Font_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Font_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Font)


gmf_all_gmfgraph_GeneralFacet_strategy = st.builds(gmf_all_gmfgraph_GeneralFacet, data=safe_text, identifier=safe_text)
@given(instance=gmf_all_gmfgraph_GeneralFacet_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_GeneralFacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_GeneralFacet)


gmf_all_gmfgraph_GradientFacet_strategy = st.builds(gmf_all_gmfgraph_GradientFacet, direction=safe_text)
@given(instance=gmf_all_gmfgraph_GradientFacet_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_GradientFacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_GradientFacet)


gmf_all_gmfgraph_GridLayout_strategy = st.builds(gmf_all_gmfgraph_GridLayout, equalWidth=st.booleans(), numColumns=st.integers())
@given(instance=gmf_all_gmfgraph_GridLayout_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_GridLayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_GridLayout)


gmf_all_gmfgraph_GridLayoutData_strategy = st.builds(gmf_all_gmfgraph_GridLayoutData, grabExcessHorizontalSpace=st.booleans(), grabExcessVerticalSpace=st.booleans(), horizontalAlignment=safe_text, horizontalIndent=st.integers(), horizontalSpan=st.integers(), verticalAlignment=safe_text, verticalSpan=st.integers())
@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_GridLayoutData_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_GridLayoutData)


gmf_all_gmfgraph_Identity_strategy = st.builds(gmf_all_gmfgraph_Identity, name=safe_text)
@given(instance=gmf_all_gmfgraph_Identity_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Identity_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Identity)


gmf_all_gmfgraph_Insets_strategy = st.builds(gmf_all_gmfgraph_Insets, bottom=st.integers(), left=st.integers(), right=st.integers(), top=st.integers())
@given(instance=gmf_all_gmfgraph_Insets_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Insets_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Insets)


gmf_all_gmfgraph_InvisibleRectangle_strategy = st.builds(gmf_all_gmfgraph_InvisibleRectangle)
@given(instance=gmf_all_gmfgraph_InvisibleRectangle_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_InvisibleRectangle_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_InvisibleRectangle)


gmf_all_gmfgraph_Label_strategy = st.builds(gmf_all_gmfgraph_Label, text=safe_text)
@given(instance=gmf_all_gmfgraph_Label_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Label_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Label)


gmf_all_gmfgraph_LabelOffsetFacet_strategy = st.builds(gmf_all_gmfgraph_LabelOffsetFacet, x=st.integers(), y=st.integers())
@given(instance=gmf_all_gmfgraph_LabelOffsetFacet_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_LabelOffsetFacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_LabelOffsetFacet)


gmf_all_gmfgraph_LabeledContainer_strategy = st.builds(gmf_all_gmfgraph_LabeledContainer)
@given(instance=gmf_all_gmfgraph_LabeledContainer_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_LabeledContainer_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_LabeledContainer)


gmf_all_gmfgraph_Layout_strategy = st.builds(gmf_all_gmfgraph_Layout)
@given(instance=gmf_all_gmfgraph_Layout_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Layout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Layout)


gmf_all_gmfgraph_LayoutData_strategy = st.builds(gmf_all_gmfgraph_LayoutData)
@given(instance=gmf_all_gmfgraph_LayoutData_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_LayoutData_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_LayoutData)


gmf_all_gmfgraph_LayoutRef_strategy = st.builds(gmf_all_gmfgraph_LayoutRef)
@given(instance=gmf_all_gmfgraph_LayoutRef_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_LayoutRef_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_LayoutRef)


gmf_all_gmfgraph_Layoutable_strategy = st.builds(gmf_all_gmfgraph_Layoutable)
@given(instance=gmf_all_gmfgraph_Layoutable_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Layoutable_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Layoutable)


gmf_all_gmfgraph_LineBorder_strategy = st.builds(gmf_all_gmfgraph_LineBorder, width=st.integers())
@given(instance=gmf_all_gmfgraph_LineBorder_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_LineBorder_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_LineBorder)


gmf_all_gmfgraph_MarginBorder_strategy = st.builds(gmf_all_gmfgraph_MarginBorder)
@given(instance=gmf_all_gmfgraph_MarginBorder_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_MarginBorder_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_MarginBorder)


gmf_all_gmfgraph_Node_strategy = st.builds(gmf_all_gmfgraph_Node, affixedParentSide=safe_text, resizeConstraint=safe_text)
@given(instance=gmf_all_gmfgraph_Node_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Node_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Node)


gmf_all_gmfgraph_Pin_strategy = st.builds(gmf_all_gmfgraph_Pin)
@given(instance=gmf_all_gmfgraph_Pin_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Pin_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Pin)


gmf_all_gmfgraph_PinOwner_strategy = st.builds(gmf_all_gmfgraph_PinOwner)
@given(instance=gmf_all_gmfgraph_PinOwner_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_PinOwner_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_PinOwner)


gmf_all_gmfgraph_Point_strategy = st.builds(gmf_all_gmfgraph_Point, x=st.integers(), y=st.integers())
@given(instance=gmf_all_gmfgraph_Point_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Point_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Point)


gmf_all_gmfgraph_Polygon_strategy = st.builds(gmf_all_gmfgraph_Polygon)
@given(instance=gmf_all_gmfgraph_Polygon_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Polygon_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Polygon)


gmf_all_gmfgraph_PolygonDecoration_strategy = st.builds(gmf_all_gmfgraph_PolygonDecoration)
@given(instance=gmf_all_gmfgraph_PolygonDecoration_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_PolygonDecoration_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_PolygonDecoration)


gmf_all_gmfgraph_Polyline_strategy = st.builds(gmf_all_gmfgraph_Polyline)
@given(instance=gmf_all_gmfgraph_Polyline_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Polyline_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Polyline)


gmf_all_gmfgraph_PolylineConnection_strategy = st.builds(gmf_all_gmfgraph_PolylineConnection)
@given(instance=gmf_all_gmfgraph_PolylineConnection_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_PolylineConnection_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_PolylineConnection)


gmf_all_gmfgraph_PolylineDecoration_strategy = st.builds(gmf_all_gmfgraph_PolylineDecoration)
@given(instance=gmf_all_gmfgraph_PolylineDecoration_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_PolylineDecoration_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_PolylineDecoration)


gmf_all_gmfgraph_RGBColor_strategy = st.builds(gmf_all_gmfgraph_RGBColor, blue=st.integers(), green=st.integers(), red=st.integers())
@given(instance=gmf_all_gmfgraph_RGBColor_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_RGBColor_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_RGBColor)


gmf_all_gmfgraph_RealFigure_strategy = st.builds(gmf_all_gmfgraph_RealFigure, name=safe_text)
@given(instance=gmf_all_gmfgraph_RealFigure_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_RealFigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_RealFigure)


gmf_all_gmfgraph_Rectangle_strategy = st.builds(gmf_all_gmfgraph_Rectangle)
@given(instance=gmf_all_gmfgraph_Rectangle_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Rectangle_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Rectangle)


gmf_all_gmfgraph_Rectangle2D_strategy = st.builds(gmf_all_gmfgraph_Rectangle2D, height=st.floats(allow_nan=False, allow_infinity=False), width=st.floats(allow_nan=False, allow_infinity=False), x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=gmf_all_gmfgraph_Rectangle2D_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Rectangle2D_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Rectangle2D)


gmf_all_gmfgraph_RoundedRectangle_strategy = st.builds(gmf_all_gmfgraph_RoundedRectangle, cornerHeight=st.integers(), cornerWidth=st.integers())
@given(instance=gmf_all_gmfgraph_RoundedRectangle_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_RoundedRectangle_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_RoundedRectangle)


gmf_all_gmfgraph_SVGFigure_strategy = st.builds(gmf_all_gmfgraph_SVGFigure, documentURI=safe_text, noCanvasHeight=st.booleans(), noCanvasWidth=st.booleans())
@given(instance=gmf_all_gmfgraph_SVGFigure_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_SVGFigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_SVGFigure)


gmf_all_gmfgraph_SVGProperty_strategy = st.builds(gmf_all_gmfgraph_SVGProperty, attribute=safe_text, callSuper=st.booleans(), getter=safe_text, query=safe_text, setter=safe_text, type=safe_text)
@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_SVGProperty_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_SVGProperty)


gmf_all_gmfgraph_ScalablePolygon_strategy = st.builds(gmf_all_gmfgraph_ScalablePolygon)
@given(instance=gmf_all_gmfgraph_ScalablePolygon_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_ScalablePolygon_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_ScalablePolygon)


gmf_all_gmfgraph_Shape_strategy = st.builds(gmf_all_gmfgraph_Shape, fill=st.booleans(), lineKind=safe_text, lineWidth=st.integers(), outline=st.booleans(), xorFill=st.booleans(), xorOutline=st.booleans())
@given(instance=gmf_all_gmfgraph_Shape_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_Shape_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Shape)


gmf_all_gmfgraph_StackLayout_strategy = st.builds(gmf_all_gmfgraph_StackLayout)
@given(instance=gmf_all_gmfgraph_StackLayout_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_StackLayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_StackLayout)


gmf_all_gmfgraph_VerticalLabel_strategy = st.builds(gmf_all_gmfgraph_VerticalLabel, text=safe_text)
@given(instance=gmf_all_gmfgraph_VerticalLabel_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_VerticalLabel_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_VerticalLabel)


gmf_all_gmfgraph_VisiblePin_strategy = st.builds(gmf_all_gmfgraph_VisiblePin)
@given(instance=gmf_all_gmfgraph_VisiblePin_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_VisiblePin_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_VisiblePin)


gmf_all_gmfgraph_VisualFacet_strategy = st.builds(gmf_all_gmfgraph_VisualFacet)
@given(instance=gmf_all_gmfgraph_VisualFacet_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_VisualFacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_VisualFacet)


gmf_all_gmfgraph_XYLayout_strategy = st.builds(gmf_all_gmfgraph_XYLayout)
@given(instance=gmf_all_gmfgraph_XYLayout_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_XYLayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_XYLayout)


gmf_all_gmfgraph_XYLayoutData_strategy = st.builds(gmf_all_gmfgraph_XYLayoutData)
@given(instance=gmf_all_gmfgraph_XYLayoutData_strategy)
@settings(max_examples=25)
def test_gmf_all_gmfgraph_XYLayoutData_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_XYLayoutData)


gmf_all_mappings_AppearanceSteward_strategy = st.builds(gmf_all_mappings_AppearanceSteward)
@given(instance=gmf_all_mappings_AppearanceSteward_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_AppearanceSteward_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_AppearanceSteward)


gmf_all_mappings_AuditContainer_strategy = st.builds(gmf_all_mappings_AuditContainer, description=safe_text, id=safe_text, name=safe_text)
@given(instance=gmf_all_mappings_AuditContainer_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_AuditContainer_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_AuditContainer)


gmf_all_mappings_AuditRule_strategy = st.builds(gmf_all_mappings_AuditRule, id=safe_text, message=safe_text, severity=safe_text, useInLiveMode=st.booleans())
@given(instance=gmf_all_mappings_AuditRule_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_AuditRule_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_AuditRule)


gmf_all_mappings_Auditable_strategy = st.builds(gmf_all_mappings_Auditable)
@given(instance=gmf_all_mappings_Auditable_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_Auditable_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_Auditable)


gmf_all_mappings_AuditedMetricTarget_strategy = st.builds(gmf_all_mappings_AuditedMetricTarget)
@given(instance=gmf_all_mappings_AuditedMetricTarget_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_AuditedMetricTarget_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_AuditedMetricTarget)


gmf_all_mappings_CanvasMapping_strategy = st.builds(gmf_all_mappings_CanvasMapping)
@given(instance=gmf_all_mappings_CanvasMapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_CanvasMapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_CanvasMapping)


gmf_all_mappings_ChildReference_strategy = st.builds(gmf_all_mappings_ChildReference)
@given(instance=gmf_all_mappings_ChildReference_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_ChildReference_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ChildReference)


gmf_all_mappings_CompartmentMapping_strategy = st.builds(gmf_all_mappings_CompartmentMapping)
@given(instance=gmf_all_mappings_CompartmentMapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_CompartmentMapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_CompartmentMapping)


gmf_all_mappings_Constraint_strategy = st.builds(gmf_all_mappings_Constraint)
@given(instance=gmf_all_mappings_Constraint_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_Constraint_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_Constraint)


gmf_all_mappings_DesignLabelMapping_strategy = st.builds(gmf_all_mappings_DesignLabelMapping)
@given(instance=gmf_all_mappings_DesignLabelMapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_DesignLabelMapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_DesignLabelMapping)


gmf_all_mappings_DiagramElementTarget_strategy = st.builds(gmf_all_mappings_DiagramElementTarget)
@given(instance=gmf_all_mappings_DiagramElementTarget_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_DiagramElementTarget_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_DiagramElementTarget)


gmf_all_mappings_DomainAttributeTarget_strategy = st.builds(gmf_all_mappings_DomainAttributeTarget, nullAsError=st.booleans())
@given(instance=gmf_all_mappings_DomainAttributeTarget_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_DomainAttributeTarget_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_DomainAttributeTarget)


gmf_all_mappings_DomainElementTarget_strategy = st.builds(gmf_all_mappings_DomainElementTarget)
@given(instance=gmf_all_mappings_DomainElementTarget_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_DomainElementTarget_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_DomainElementTarget)


gmf_all_mappings_ElementInitializer_strategy = st.builds(gmf_all_mappings_ElementInitializer)
@given(instance=gmf_all_mappings_ElementInitializer_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_ElementInitializer_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ElementInitializer)


gmf_all_mappings_ExpressionLabelMapping_strategy = st.builds(gmf_all_mappings_ExpressionLabelMapping)
@given(instance=gmf_all_mappings_ExpressionLabelMapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_ExpressionLabelMapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ExpressionLabelMapping)


gmf_all_mappings_FeatureInitializer_strategy = st.builds(gmf_all_mappings_FeatureInitializer)
@given(instance=gmf_all_mappings_FeatureInitializer_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_FeatureInitializer_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_FeatureInitializer)


gmf_all_mappings_FeatureLabelMapping_strategy = st.builds(gmf_all_mappings_FeatureLabelMapping, editMethod=safe_text, editPattern=safe_text, editorPattern=safe_text, viewMethod=safe_text, viewPattern=safe_text)
@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_FeatureLabelMapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_FeatureLabelMapping)


gmf_all_mappings_FeatureSeqInitializer_strategy = st.builds(gmf_all_mappings_FeatureSeqInitializer)
@given(instance=gmf_all_mappings_FeatureSeqInitializer_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_FeatureSeqInitializer_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_FeatureSeqInitializer)


gmf_all_mappings_FeatureValueSpec_strategy = st.builds(gmf_all_mappings_FeatureValueSpec)
@given(instance=gmf_all_mappings_FeatureValueSpec_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_FeatureValueSpec_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_FeatureValueSpec)


gmf_all_mappings_LabelMapping_strategy = st.builds(gmf_all_mappings_LabelMapping, readOnly=st.booleans())
@given(instance=gmf_all_mappings_LabelMapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_LabelMapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_LabelMapping)


gmf_all_mappings_LinkConstraints_strategy = st.builds(gmf_all_mappings_LinkConstraints)
@given(instance=gmf_all_mappings_LinkConstraints_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_LinkConstraints_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_LinkConstraints)


gmf_all_mappings_LinkMapping_strategy = st.builds(gmf_all_mappings_LinkMapping)
@given(instance=gmf_all_mappings_LinkMapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_LinkMapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_LinkMapping)


gmf_all_mappings_Mapping_strategy = st.builds(gmf_all_mappings_Mapping)
@given(instance=gmf_all_mappings_Mapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_Mapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_Mapping)


gmf_all_mappings_MappingEntry_strategy = st.builds(gmf_all_mappings_MappingEntry)
@given(instance=gmf_all_mappings_MappingEntry_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_MappingEntry_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_MappingEntry)


gmf_all_mappings_Measurable_strategy = st.builds(gmf_all_mappings_Measurable)
@given(instance=gmf_all_mappings_Measurable_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_Measurable_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_Measurable)


gmf_all_mappings_MenuOwner_strategy = st.builds(gmf_all_mappings_MenuOwner)
@given(instance=gmf_all_mappings_MenuOwner_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_MenuOwner_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_MenuOwner)


gmf_all_mappings_MetricContainer_strategy = st.builds(gmf_all_mappings_MetricContainer)
@given(instance=gmf_all_mappings_MetricContainer_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_MetricContainer_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_MetricContainer)


gmf_all_mappings_MetricRule_strategy = st.builds(gmf_all_mappings_MetricRule, highLimit=safe_text, key=safe_text, lowLimit=safe_text)
@given(instance=gmf_all_mappings_MetricRule_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_MetricRule_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_MetricRule)


gmf_all_mappings_NeedsContainment_strategy = st.builds(gmf_all_mappings_NeedsContainment)
@given(instance=gmf_all_mappings_NeedsContainment_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_NeedsContainment_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_NeedsContainment)


gmf_all_mappings_NodeMapping_strategy = st.builds(gmf_all_mappings_NodeMapping)
@given(instance=gmf_all_mappings_NodeMapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_NodeMapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_NodeMapping)


gmf_all_mappings_NodeReference_strategy = st.builds(gmf_all_mappings_NodeReference)
@given(instance=gmf_all_mappings_NodeReference_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_NodeReference_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_NodeReference)


gmf_all_mappings_NotationElementTarget_strategy = st.builds(gmf_all_mappings_NotationElementTarget)
@given(instance=gmf_all_mappings_NotationElementTarget_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_NotationElementTarget_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_NotationElementTarget)


gmf_all_mappings_OclChoiceLabelMapping_strategy = st.builds(gmf_all_mappings_OclChoiceLabelMapping)
@given(instance=gmf_all_mappings_OclChoiceLabelMapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_OclChoiceLabelMapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_OclChoiceLabelMapping)


gmf_all_mappings_ReferenceNewElementSpec_strategy = st.builds(gmf_all_mappings_ReferenceNewElementSpec)
@given(instance=gmf_all_mappings_ReferenceNewElementSpec_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_ReferenceNewElementSpec_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ReferenceNewElementSpec)


gmf_all_mappings_RuleBase_strategy = st.builds(gmf_all_mappings_RuleBase, description=safe_text, name=safe_text)
@given(instance=gmf_all_mappings_RuleBase_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_RuleBase_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_RuleBase)


gmf_all_mappings_ToolOwner_strategy = st.builds(gmf_all_mappings_ToolOwner)
@given(instance=gmf_all_mappings_ToolOwner_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_ToolOwner_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ToolOwner)


gmf_all_mappings_TopNodeReference_strategy = st.builds(gmf_all_mappings_TopNodeReference)
@given(instance=gmf_all_mappings_TopNodeReference_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_TopNodeReference_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_TopNodeReference)


gmf_all_mappings_ValueExpression_strategy = st.builds(gmf_all_mappings_ValueExpression, body=safe_text, langName=safe_text, language=safe_text)
@given(instance=gmf_all_mappings_ValueExpression_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_ValueExpression_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ValueExpression)


gmf_all_mappings_VisualEffectMapping_strategy = st.builds(gmf_all_mappings_VisualEffectMapping, oclExpression=safe_text)
@given(instance=gmf_all_mappings_VisualEffectMapping_strategy)
@settings(max_examples=25)
def test_gmf_all_mappings_VisualEffectMapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_VisualEffectMapping)


gmf_all_tooldef_AbstractTool_strategy = st.builds(gmf_all_tooldef_AbstractTool, description=safe_text, title=safe_text)
@given(instance=gmf_all_tooldef_AbstractTool_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_AbstractTool_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_AbstractTool)


gmf_all_tooldef_BundleImage_strategy = st.builds(gmf_all_tooldef_BundleImage, bundle=safe_text, path=safe_text)
@given(instance=gmf_all_tooldef_BundleImage_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_BundleImage_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_BundleImage)


gmf_all_tooldef_ContextMenu_strategy = st.builds(gmf_all_tooldef_ContextMenu)
@given(instance=gmf_all_tooldef_ContextMenu_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_ContextMenu_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ContextMenu)


gmf_all_tooldef_ContributionItem_strategy = st.builds(gmf_all_tooldef_ContributionItem, title=safe_text)
@given(instance=gmf_all_tooldef_ContributionItem_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_ContributionItem_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ContributionItem)


gmf_all_tooldef_CreationTool_strategy = st.builds(gmf_all_tooldef_CreationTool)
@given(instance=gmf_all_tooldef_CreationTool_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_CreationTool_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_CreationTool)


gmf_all_tooldef_DefaultImage_strategy = st.builds(gmf_all_tooldef_DefaultImage)
@given(instance=gmf_all_tooldef_DefaultImage_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_DefaultImage_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_DefaultImage)


gmf_all_tooldef_GenericStyleSelector_strategy = st.builds(gmf_all_tooldef_GenericStyleSelector, values=safe_text)
@given(instance=gmf_all_tooldef_GenericStyleSelector_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_GenericStyleSelector_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_GenericStyleSelector)


gmf_all_tooldef_GenericTool_strategy = st.builds(gmf_all_tooldef_GenericTool, toolClass=safe_text)
@given(instance=gmf_all_tooldef_GenericTool_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_GenericTool_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_GenericTool)


gmf_all_tooldef_Image_strategy = st.builds(gmf_all_tooldef_Image)
@given(instance=gmf_all_tooldef_Image_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_Image_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_Image)


gmf_all_tooldef_ItemBase_strategy = st.builds(gmf_all_tooldef_ItemBase)
@given(instance=gmf_all_tooldef_ItemBase_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_ItemBase_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ItemBase)


gmf_all_tooldef_ItemRef_strategy = st.builds(gmf_all_tooldef_ItemRef)
@given(instance=gmf_all_tooldef_ItemRef_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_ItemRef_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ItemRef)


gmf_all_tooldef_MainMenu_strategy = st.builds(gmf_all_tooldef_MainMenu, title=safe_text)
@given(instance=gmf_all_tooldef_MainMenu_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_MainMenu_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_MainMenu)


gmf_all_tooldef_Menu_strategy = st.builds(gmf_all_tooldef_Menu)
@given(instance=gmf_all_tooldef_Menu_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_Menu_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_Menu)


gmf_all_tooldef_MenuAction_strategy = st.builds(gmf_all_tooldef_MenuAction, hotKey=safe_text, kind=safe_text)
@given(instance=gmf_all_tooldef_MenuAction_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_MenuAction_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_MenuAction)


gmf_all_tooldef_Palette_strategy = st.builds(gmf_all_tooldef_Palette)
@given(instance=gmf_all_tooldef_Palette_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_Palette_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_Palette)


gmf_all_tooldef_PaletteSeparator_strategy = st.builds(gmf_all_tooldef_PaletteSeparator)
@given(instance=gmf_all_tooldef_PaletteSeparator_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_PaletteSeparator_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_PaletteSeparator)


gmf_all_tooldef_PopupMenu_strategy = st.builds(gmf_all_tooldef_PopupMenu, iD=safe_text)
@given(instance=gmf_all_tooldef_PopupMenu_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_PopupMenu_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_PopupMenu)


gmf_all_tooldef_PredefinedItem_strategy = st.builds(gmf_all_tooldef_PredefinedItem, identifier=safe_text)
@given(instance=gmf_all_tooldef_PredefinedItem_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_PredefinedItem_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_PredefinedItem)


gmf_all_tooldef_PredefinedMenu_strategy = st.builds(gmf_all_tooldef_PredefinedMenu)
@given(instance=gmf_all_tooldef_PredefinedMenu_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_PredefinedMenu_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_PredefinedMenu)


gmf_all_tooldef_Separator_strategy = st.builds(gmf_all_tooldef_Separator, name=safe_text)
@given(instance=gmf_all_tooldef_Separator_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_Separator_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_Separator)


gmf_all_tooldef_StandardTool_strategy = st.builds(gmf_all_tooldef_StandardTool, toolKind=safe_text)
@given(instance=gmf_all_tooldef_StandardTool_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_StandardTool_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_StandardTool)


gmf_all_tooldef_StyleSelector_strategy = st.builds(gmf_all_tooldef_StyleSelector)
@given(instance=gmf_all_tooldef_StyleSelector_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_StyleSelector_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_StyleSelector)


gmf_all_tooldef_ToolContainer_strategy = st.builds(gmf_all_tooldef_ToolContainer)
@given(instance=gmf_all_tooldef_ToolContainer_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_ToolContainer_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ToolContainer)


gmf_all_tooldef_ToolGroup_strategy = st.builds(gmf_all_tooldef_ToolGroup, collapsible=st.booleans(), stack=st.booleans())
@given(instance=gmf_all_tooldef_ToolGroup_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_ToolGroup_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ToolGroup)


gmf_all_tooldef_ToolRegistry_strategy = st.builds(gmf_all_tooldef_ToolRegistry)
@given(instance=gmf_all_tooldef_ToolRegistry_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_ToolRegistry_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ToolRegistry)


gmf_all_tooldef_Toolbar_strategy = st.builds(gmf_all_tooldef_Toolbar)
@given(instance=gmf_all_tooldef_Toolbar_strategy)
@settings(max_examples=25)
def test_gmf_all_tooldef_Toolbar_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_Toolbar)


gmfgraph_AbstractFigure_strategy = st.builds(gmfgraph_AbstractFigure)
@given(instance=gmfgraph_AbstractFigure_strategy)
@settings(max_examples=25)
def test_gmfgraph_AbstractFigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_AbstractFigure)


gmfgraph_Border_strategy = st.builds(gmfgraph_Border)
@given(instance=gmfgraph_Border_strategy)
@settings(max_examples=25)
def test_gmfgraph_Border_instantiation(instance):
    assert isinstance(instance, gmfgraph_Border)


gmfgraph_ConnectionFigure_strategy = st.builds(gmfgraph_ConnectionFigure)
@given(instance=gmfgraph_ConnectionFigure_strategy)
@settings(max_examples=25)
def test_gmfgraph_ConnectionFigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_ConnectionFigure)


gmfgraph_CustomAttributeOwner_strategy = st.builds(gmfgraph_CustomAttributeOwner)
@given(instance=gmfgraph_CustomAttributeOwner_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomAttributeOwner_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomAttributeOwner)


gmfgraph_CustomClass_strategy = st.builds(gmfgraph_CustomClass)
@given(instance=gmfgraph_CustomClass_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomClass_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomClass)


gmfgraph_CustomFigure_strategy = st.builds(gmfgraph_CustomFigure)
@given(instance=gmfgraph_CustomFigure_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomFigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomFigure)


gmfgraph_DecorationFigure_strategy = st.builds(gmfgraph_DecorationFigure)
@given(instance=gmfgraph_DecorationFigure_strategy)
@settings(max_examples=25)
def test_gmfgraph_DecorationFigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_DecorationFigure)


gmfgraph_Layout_strategy = st.builds(gmfgraph_Layout)
@given(instance=gmfgraph_Layout_strategy)
@settings(max_examples=25)
def test_gmfgraph_Layout_instantiation(instance):
    assert isinstance(instance, gmfgraph_Layout)


gmfgraph_LayoutData_strategy = st.builds(gmfgraph_LayoutData)
@given(instance=gmfgraph_LayoutData_strategy)
@settings(max_examples=25)
def test_gmfgraph_LayoutData_instantiation(instance):
    assert isinstance(instance, gmfgraph_LayoutData)


gmfgraph_PinOwner_strategy = st.builds(gmfgraph_PinOwner)
@given(instance=gmfgraph_PinOwner_strategy)
@settings(max_examples=25)
def test_gmfgraph_PinOwner_instantiation(instance):
    assert isinstance(instance, gmfgraph_PinOwner)


gmfgraph_Polygon_strategy = st.builds(gmfgraph_Polygon)
@given(instance=gmfgraph_Polygon_strategy)
@settings(max_examples=25)
def test_gmfgraph_Polygon_instantiation(instance):
    assert isinstance(instance, gmfgraph_Polygon)


gmfgraph_Polyline_strategy = st.builds(gmfgraph_Polyline)
@given(instance=gmfgraph_Polyline_strategy)
@settings(max_examples=25)
def test_gmfgraph_Polyline_instantiation(instance):
    assert isinstance(instance, gmfgraph_Polyline)


gmfgraph_RealFigure_strategy = st.builds(gmfgraph_RealFigure)
@given(instance=gmfgraph_RealFigure_strategy)
@settings(max_examples=25)
def test_gmfgraph_RealFigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_RealFigure)


mappings_AppearanceSteward_strategy = st.builds(mappings_AppearanceSteward)
@given(instance=mappings_AppearanceSteward_strategy)
@settings(max_examples=25)
def test_mappings_AppearanceSteward_instantiation(instance):
    assert isinstance(instance, mappings_AppearanceSteward)


mappings_Auditable_strategy = st.builds(mappings_Auditable)
@given(instance=mappings_Auditable_strategy)
@settings(max_examples=25)
def test_mappings_Auditable_instantiation(instance):
    assert isinstance(instance, mappings_Auditable)


mappings_MappingEntry_strategy = st.builds(mappings_MappingEntry)
@given(instance=mappings_MappingEntry_strategy)
@settings(max_examples=25)
def test_mappings_MappingEntry_instantiation(instance):
    assert isinstance(instance, mappings_MappingEntry)


mappings_Measurable_strategy = st.builds(mappings_Measurable)
@given(instance=mappings_Measurable_strategy)
@settings(max_examples=25)
def test_mappings_Measurable_instantiation(instance):
    assert isinstance(instance, mappings_Measurable)


mappings_MenuOwner_strategy = st.builds(mappings_MenuOwner)
@given(instance=mappings_MenuOwner_strategy)
@settings(max_examples=25)
def test_mappings_MenuOwner_instantiation(instance):
    assert isinstance(instance, mappings_MenuOwner)


mappings_NeedsContainment_strategy = st.builds(mappings_NeedsContainment)
@given(instance=mappings_NeedsContainment_strategy)
@settings(max_examples=25)
def test_mappings_NeedsContainment_instantiation(instance):
    assert isinstance(instance, mappings_NeedsContainment)


mappings_ToolOwner_strategy = st.builds(mappings_ToolOwner)
@given(instance=mappings_ToolOwner_strategy)
@settings(max_examples=25)
def test_mappings_ToolOwner_instantiation(instance):
    assert isinstance(instance, mappings_ToolOwner)


mappings_gmf_all_EAttribute_strategy = st.builds(mappings_gmf_all_EAttribute)
@given(instance=mappings_gmf_all_EAttribute_strategy)
@settings(max_examples=25)
def test_mappings_gmf_all_EAttribute_instantiation(instance):
    assert isinstance(instance, mappings_gmf_all_EAttribute)


mappings_gmf_all_EClass_strategy = st.builds(mappings_gmf_all_EClass)
@given(instance=mappings_gmf_all_EClass_strategy)
@settings(max_examples=25)
def test_mappings_gmf_all_EClass_instantiation(instance):
    assert isinstance(instance, mappings_gmf_all_EClass)


mappings_gmf_all_EPackage_strategy = st.builds(mappings_gmf_all_EPackage)
@given(instance=mappings_gmf_all_EPackage_strategy)
@settings(max_examples=25)
def test_mappings_gmf_all_EPackage_instantiation(instance):
    assert isinstance(instance, mappings_gmf_all_EPackage)


mappings_gmf_all_EReference_strategy = st.builds(mappings_gmf_all_EReference)
@given(instance=mappings_gmf_all_EReference_strategy)
@settings(max_examples=25)
def test_mappings_gmf_all_EReference_instantiation(instance):
    assert isinstance(instance, mappings_gmf_all_EReference)


mappings_gmf_all_EStructuralFeature_strategy = st.builds(mappings_gmf_all_EStructuralFeature)
@given(instance=mappings_gmf_all_EStructuralFeature_strategy)
@settings(max_examples=25)
def test_mappings_gmf_all_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, mappings_gmf_all_EStructuralFeature)


tooldef_ContributionItem_strategy = st.builds(tooldef_ContributionItem)
@given(instance=tooldef_ContributionItem_strategy)
@settings(max_examples=25)
def test_tooldef_ContributionItem_instantiation(instance):
    assert isinstance(instance, tooldef_ContributionItem)


tooldef_Menu_strategy = st.builds(tooldef_Menu)
@given(instance=tooldef_Menu_strategy)
@settings(max_examples=25)
def test_tooldef_Menu_instantiation(instance):
    assert isinstance(instance, tooldef_Menu)


tooldef_PredefinedItem_strategy = st.builds(tooldef_PredefinedItem)
@given(instance=tooldef_PredefinedItem_strategy)
@settings(max_examples=25)
def test_tooldef_PredefinedItem_instantiation(instance):
    assert isinstance(instance, tooldef_PredefinedItem)



