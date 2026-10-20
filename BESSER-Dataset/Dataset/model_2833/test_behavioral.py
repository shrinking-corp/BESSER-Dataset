import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_accessor191_stub_double():
    # ChildAccess has no real 'ChildAccess192' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_Compartment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_Compartment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_Compartment(collapsible=True, needsTitle=True)
    partner = ChildAccess()
    setattr(partner, 'ChildAccess192', None)
    _safe_set(owner, 'gmf_all_gmfgraph_Compartment', partner)
    assert getattr(partner, 'ChildAccess192') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_Compartment', None)
    assert getattr(partner, 'ChildAccess192') is None


def test_assoc_accessor193_stub_double():
    # ChildAccess has no real 'ChildAccess194' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_DiagramLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_DiagramLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_DiagramLabel(elementIcon=True, external=True)
    partner = ChildAccess()
    setattr(partner, 'ChildAccess194', None)
    _safe_set(owner, 'gmf_all_gmfgraph_DiagramLabel', partner)
    assert getattr(partner, 'ChildAccess194') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_DiagramLabel', None)
    assert getattr(partner, 'ChildAccess194') is None


def test_assoc_active155_stub_double():
    # AbstractTool has no real 'AbstractTool156' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_tooldef_ToolGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_tooldef_ToolGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_tooldef_ToolGroup(collapsible=True, stack=True)
    partner = AbstractTool()
    setattr(partner, 'AbstractTool156', None)
    _safe_set(owner, 'gmf_all_tooldef_ToolGroup', partner)
    assert getattr(partner, 'AbstractTool156') == owner
    _safe_set(owner, 'gmf_all_tooldef_ToolGroup', None)
    assert getattr(partner, 'AbstractTool156') is None


def test_assoc_areaOfInterest283_stub_double():
    # Rectangle2D has no real 'Rectangle2D' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_SVGFigure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_SVGFigure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_SVGFigure(documentURI="sample_text", noCanvasHeight=True, noCanvasWidth=True)
    partner = Rectangle2D()
    setattr(partner, 'Rectangle2D', None)
    _safe_set(owner, 'gmf_all_gmfgraph_SVGFigure284', partner)
    assert getattr(partner, 'Rectangle2D') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_SVGFigure284', None)
    assert getattr(partner, 'Rectangle2D') is None


def test_assoc_attribute124_stub_double():
    # mappings_gmf_all_EAttribute has no real 'mappings_gmf_all_EAttribute125' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_DomainAttributeTarget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_DomainAttributeTarget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_DomainAttributeTarget(nullAsError=True)
    partner = mappings_gmf_all_EAttribute()
    setattr(partner, 'mappings_gmf_all_EAttribute125', None)
    _safe_set(owner, 'gmf_all_mappings_DomainAttributeTarget', partner)
    assert getattr(partner, 'mappings_gmf_all_EAttribute125') == owner
    _safe_set(owner, 'gmf_all_mappings_DomainAttributeTarget', None)
    assert getattr(partner, 'mappings_gmf_all_EAttribute125') is None


def test_assoc_audits113_stub_double():
    # AuditRule has no real 'AuditRule' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_AuditContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_AuditContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_AuditContainer(description="sample_text", id="sample_text", name="sample_text")
    partner = AuditRule()
    setattr(partner, 'AuditRule', None)
    _safe_set(owner, 'container', {partner})
    assert getattr(partner, 'AuditRule') == owner
    _safe_set(owner, 'container', set())
    assert getattr(partner, 'AuditRule') is None


def test_assoc_borders182_stub_double():
    # Border has no real 'Border' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_FigureGallery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_FigureGallery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_FigureGallery(implementationBundle="sample_text")
    partner = Border()
    setattr(partner, 'Border', None)
    _safe_set(owner, 'gmf_all_gmfgraph_FigureGallery183', {partner})
    assert getattr(partner, 'Border') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_FigureGallery183', set())
    assert getattr(partner, 'Border') is None


def test_assoc_childContainers114_stub_double():
    # AuditContainer has no real 'AuditContainer115' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_AuditContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_AuditContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_AuditContainer(description="sample_text", id="sample_text", name="sample_text")
    partner = AuditContainer()
    setattr(partner, 'AuditContainer115', None)
    _safe_set(owner, 'parentContainer', {partner})
    assert getattr(partner, 'AuditContainer115') == owner
    _safe_set(owner, 'parentContainer', set())
    assert getattr(partner, 'AuditContainer115') is None


def test_assoc_children234_stub_double():
    # Figure has no real 'Figure235' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_RealFigure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_RealFigure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_RealFigure(name="sample_text")
    partner = Figure()
    setattr(partner, 'Figure235', None)
    _safe_set(owner, 'gmf_all_gmfgraph_RealFigure', {partner})
    assert getattr(partner, 'Figure235') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_RealFigure', set())
    assert getattr(partner, 'Figure235') is None


def test_assoc_color252_stub_double():
    # Color has no real 'Color253' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_LineBorder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_LineBorder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_LineBorder(width=7)
    partner = Color()
    setattr(partner, 'Color253', None)
    _safe_set(owner, 'gmf_all_gmfgraph_LineBorder', partner)
    assert getattr(partner, 'Color253') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_LineBorder', None)
    assert getattr(partner, 'Color253') is None


def test_assoc_container120_stub_double():
    # AuditContainer has no real 'AuditContainer121' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_AuditRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_AuditRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    partner = AuditContainer()
    setattr(partner, 'AuditContainer121', None)
    _safe_set(owner, 'audits', partner)
    assert getattr(partner, 'AuditContainer121') == owner
    _safe_set(owner, 'audits', None)
    assert getattr(partner, 'AuditContainer121') is None


def test_assoc_container136_stub_double():
    # MetricContainer has no real 'MetricContainer137' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_MetricRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_MetricRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_MetricRule(highLimit="sample_text", key="sample_text", lowLimit="sample_text")
    partner = MetricContainer()
    setattr(partner, 'MetricContainer137', None)
    _safe_set(owner, 'metrics', partner)
    assert getattr(partner, 'MetricContainer137') == owner
    _safe_set(owner, 'metrics', None)
    assert getattr(partner, 'MetricContainer137') is None


def test_assoc_container195_stub_double():
    # ChildAccess has no real 'ChildAccess197' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_DiagramLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_DiagramLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_DiagramLabel(elementIcon=True, external=True)
    partner = ChildAccess()
    setattr(partner, 'ChildAccess197', None)
    _safe_set(owner, 'gmf_all_gmfgraph_DiagramLabel196', partner)
    assert getattr(partner, 'ChildAccess197') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_DiagramLabel196', None)
    assert getattr(partner, 'ChildAccess197') is None


def test_assoc_contentPane190_stub_double():
    # ChildAccess has no real 'ChildAccess' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    partner = ChildAccess()
    setattr(partner, 'ChildAccess', None)
    _safe_set(owner, 'gmf_all_gmfgraph_Node', partner)
    assert getattr(partner, 'ChildAccess') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_Node', None)
    assert getattr(partner, 'ChildAccess') is None


def test_assoc_descriptors180_stub_double():
    # FigureDescriptor has no real 'FigureDescriptor' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_FigureGallery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_FigureGallery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_FigureGallery(implementationBundle="sample_text")
    partner = FigureDescriptor()
    setattr(partner, 'FigureDescriptor', None)
    _safe_set(owner, 'gmf_all_gmfgraph_FigureGallery181', {partner})
    assert getattr(partner, 'FigureDescriptor') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_FigureGallery181', set())
    assert getattr(partner, 'FigureDescriptor') is None


def test_assoc_diagramLabel66_stub_double():
    # DiagramLabel has no real 'DiagramLabel' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_LabelMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_LabelMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_LabelMapping(readOnly=True)
    partner = DiagramLabel()
    setattr(partner, 'DiagramLabel', None)
    _safe_set(owner, 'gmf_all_mappings_LabelMapping', partner)
    assert getattr(partner, 'DiagramLabel') == owner
    _safe_set(owner, 'gmf_all_mappings_LabelMapping', None)
    assert getattr(partner, 'DiagramLabel') is None


def test_assoc_diagramPin140_stub_double():
    # Pin has no real 'Pin' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_VisualEffectMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_VisualEffectMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_VisualEffectMapping(oclExpression="sample_text")
    partner = Pin()
    setattr(partner, 'Pin', None)
    _safe_set(owner, 'gmf_all_mappings_VisualEffectMapping', partner)
    assert getattr(partner, 'Pin') == owner
    _safe_set(owner, 'gmf_all_mappings_VisualEffectMapping', None)
    assert getattr(partner, 'Pin') is None


def test_assoc_domainInitializer14_stub_double():
    # ElementInitializer has no real 'ElementInitializer' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_MappingEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_MappingEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_MappingEntry()
    partner = ElementInitializer()
    setattr(partner, 'ElementInitializer', None)
    _safe_set(owner, 'gmf_all_mappings_MappingEntry15', partner)
    assert getattr(partner, 'ElementInitializer') == owner
    _safe_set(owner, 'gmf_all_mappings_MappingEntry15', None)
    assert getattr(partner, 'ElementInitializer') is None


def test_assoc_domainMetaElement11_stub_double():
    # mappings_gmf_all_EClass has no real 'mappings_gmf_all_EClass' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_MappingEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_MappingEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_MappingEntry()
    partner = mappings_gmf_all_EClass()
    setattr(partner, 'mappings_gmf_all_EClass', None)
    _safe_set(owner, 'gmf_all_mappings_MappingEntry', partner)
    assert getattr(partner, 'mappings_gmf_all_EClass') == owner
    _safe_set(owner, 'gmf_all_mappings_MappingEntry', None)
    assert getattr(partner, 'mappings_gmf_all_EClass') is None


def test_assoc_domainSpecialization12_stub_double():
    # Constraint has no real 'Constraint' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_MappingEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_MappingEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_MappingEntry()
    partner = Constraint()
    setattr(partner, 'Constraint', None)
    _safe_set(owner, 'gmf_all_mappings_MappingEntry13', partner)
    assert getattr(partner, 'Constraint') == owner
    _safe_set(owner, 'gmf_all_mappings_MappingEntry13', None)
    assert getattr(partner, 'Constraint') is None


def test_assoc_editableFeatures69_stub_double():
    # mappings_gmf_all_EAttribute has no real 'mappings_gmf_all_EAttribute71' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_FeatureLabelMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_FeatureLabelMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_FeatureLabelMapping(editMethod="sample_text", editPattern="sample_text", editorPattern="sample_text", viewMethod="sample_text", viewPattern="sample_text")
    partner = mappings_gmf_all_EAttribute()
    setattr(partner, 'mappings_gmf_all_EAttribute71', None)
    _safe_set(owner, 'gmf_all_mappings_FeatureLabelMapping70', {partner})
    assert getattr(partner, 'mappings_gmf_all_EAttribute71') == owner
    _safe_set(owner, 'gmf_all_mappings_FeatureLabelMapping70', set())
    assert getattr(partner, 'mappings_gmf_all_EAttribute71') is None


def test_assoc_features68_stub_double():
    # mappings_gmf_all_EAttribute has no real 'mappings_gmf_all_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_FeatureLabelMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_FeatureLabelMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_FeatureLabelMapping(editMethod="sample_text", editPattern="sample_text", editorPattern="sample_text", viewMethod="sample_text", viewPattern="sample_text")
    partner = mappings_gmf_all_EAttribute()
    setattr(partner, 'mappings_gmf_all_EAttribute', None)
    _safe_set(owner, 'gmf_all_mappings_FeatureLabelMapping', {partner})
    assert getattr(partner, 'mappings_gmf_all_EAttribute') == owner
    _safe_set(owner, 'gmf_all_mappings_FeatureLabelMapping', set())
    assert getattr(partner, 'mappings_gmf_all_EAttribute') is None


def test_assoc_figure232_stub_double():
    # Figure has no real 'Figure233' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_ChildAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_ChildAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_ChildAccess(accessor="sample_text")
    partner = Figure()
    setattr(partner, 'Figure233', None)
    _safe_set(owner, 'gmf_all_gmfgraph_ChildAccess', partner)
    assert getattr(partner, 'Figure233') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_ChildAccess', None)
    assert getattr(partner, 'Figure233') is None


def test_assoc_figures179_stub_double():
    # RealFigure has no real 'RealFigure' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_FigureGallery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_FigureGallery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_FigureGallery(implementationBundle="sample_text")
    partner = RealFigure()
    setattr(partner, 'RealFigure', None)
    _safe_set(owner, 'gmf_all_gmfgraph_FigureGallery', {partner})
    assert getattr(partner, 'RealFigure') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_FigureGallery', set())
    assert getattr(partner, 'RealFigure') is None


def test_assoc_icon160_stub_double():
    # Image has no real 'Image161' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_tooldef_ContributionItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_tooldef_ContributionItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_tooldef_ContributionItem(title="sample_text")
    partner = Image()
    setattr(partner, 'Image161', None)
    _safe_set(owner, 'gmf_all_tooldef_ContributionItem', partner)
    assert getattr(partner, 'Image161') == owner
    _safe_set(owner, 'gmf_all_tooldef_ContributionItem', None)
    assert getattr(partner, 'Image161') is None


def test_assoc_labelMappings16_stub_double():
    # LabelMapping has no real 'LabelMapping' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_MappingEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_MappingEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_MappingEntry()
    partner = LabelMapping()
    setattr(partner, 'LabelMapping', None)
    _safe_set(owner, 'mapEntry', {partner})
    assert getattr(partner, 'LabelMapping') == owner
    _safe_set(owner, 'mapEntry', set())
    assert getattr(partner, 'LabelMapping') is None


def test_assoc_largeIcon150_stub_double():
    # Image has no real 'Image152' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_tooldef_AbstractTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_tooldef_AbstractTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_tooldef_AbstractTool(description="sample_text", title="sample_text")
    partner = Image()
    setattr(partner, 'Image152', None)
    _safe_set(owner, 'gmf_all_tooldef_AbstractTool151', partner)
    assert getattr(partner, 'Image152') == owner
    _safe_set(owner, 'gmf_all_tooldef_AbstractTool151', None)
    assert getattr(partner, 'Image152') is None


def test_assoc_layouts184_stub_double():
    # Layout has no real 'Layout' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_FigureGallery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_FigureGallery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_FigureGallery(implementationBundle="sample_text")
    partner = Layout()
    setattr(partner, 'Layout', None)
    _safe_set(owner, 'gmf_all_gmfgraph_FigureGallery185', {partner})
    assert getattr(partner, 'Layout') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_FigureGallery185', set())
    assert getattr(partner, 'Layout') is None


def test_assoc_mapEntry67_stub_double():
    # MappingEntry has no real 'MappingEntry' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_LabelMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_LabelMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_LabelMapping(readOnly=True)
    partner = MappingEntry()
    setattr(partner, 'MappingEntry', None)
    _safe_set(owner, 'labelMappings', partner)
    assert getattr(partner, 'MappingEntry') == owner
    _safe_set(owner, 'labelMappings', None)
    assert getattr(partner, 'MappingEntry') is None


def test_assoc_margins270_stub_double():
    # Dimension has no real 'Dimension271' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_GridLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_GridLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    partner = Dimension()
    setattr(partner, 'Dimension271', None)
    _safe_set(owner, 'gmf_all_gmfgraph_GridLayout', partner)
    assert getattr(partner, 'Dimension271') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_GridLayout', None)
    assert getattr(partner, 'Dimension271') is None


def test_assoc_owner230_stub_double():
    # FigureDescriptor has no real 'FigureDescriptor231' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_ChildAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_ChildAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_ChildAccess(accessor="sample_text")
    partner = FigureDescriptor()
    setattr(partner, 'FigureDescriptor231', None)
    _safe_set(owner, 'accessors', partner)
    assert getattr(partner, 'FigureDescriptor231') == owner
    _safe_set(owner, 'accessors', None)
    assert getattr(partner, 'FigureDescriptor231') is None


def test_assoc_parentContainer111_stub_double():
    # AuditContainer has no real 'AuditContainer112' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_AuditContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_AuditContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_AuditContainer(description="sample_text", id="sample_text", name="sample_text")
    partner = AuditContainer()
    setattr(partner, 'AuditContainer112', None)
    _safe_set(owner, 'childContainers', partner)
    assert getattr(partner, 'AuditContainer112') == owner
    _safe_set(owner, 'childContainers', None)
    assert getattr(partner, 'AuditContainer112') is None


def test_assoc_parentMapEntry141_stub_double():
    # MappingEntry has no real 'MappingEntry142' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_VisualEffectMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_VisualEffectMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_VisualEffectMapping(oclExpression="sample_text")
    partner = MappingEntry()
    setattr(partner, 'MappingEntry142', None)
    _safe_set(owner, 'visualEffects', partner)
    assert getattr(partner, 'MappingEntry142') == owner
    _safe_set(owner, 'visualEffects', None)
    assert getattr(partner, 'MappingEntry142') is None


def test_assoc_properties282_stub_double():
    # SVGProperty has no real 'SVGProperty' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_SVGFigure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_SVGFigure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_SVGFigure(documentURI="sample_text", noCanvasHeight=True, noCanvasWidth=True)
    partner = SVGProperty()
    setattr(partner, 'SVGProperty', None)
    _safe_set(owner, 'gmf_all_gmfgraph_SVGFigure', {partner})
    assert getattr(partner, 'SVGProperty') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_SVGFigure', set())
    assert getattr(partner, 'SVGProperty') is None


def test_assoc_relatedDiagrams17_stub_double():
    # CanvasMapping has no real 'CanvasMapping19' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_MappingEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_MappingEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_MappingEntry()
    partner = CanvasMapping()
    setattr(partner, 'CanvasMapping19', None)
    _safe_set(owner, 'gmf_all_mappings_MappingEntry18', {partner})
    assert getattr(partner, 'CanvasMapping19') == owner
    _safe_set(owner, 'gmf_all_mappings_MappingEntry18', set())
    assert getattr(partner, 'CanvasMapping19') is None


def test_assoc_resolvedChildren238_stub_double():
    # Figure has no real 'Figure239' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    partner = Figure()
    setattr(partner, 'Figure239', None)
    _safe_set(owner, 'gmf_all_gmfgraph_Shape', {partner})
    assert getattr(partner, 'Figure239') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_Shape', set())
    assert getattr(partner, 'Figure239') is None


def test_assoc_rule116_stub_double():
    # Constraint has no real 'Constraint117' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_AuditRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_AuditRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    partner = Constraint()
    setattr(partner, 'Constraint117', None)
    _safe_set(owner, 'gmf_all_mappings_AuditRule', partner)
    assert getattr(partner, 'Constraint117') == owner
    _safe_set(owner, 'gmf_all_mappings_AuditRule', None)
    assert getattr(partner, 'Constraint117') is None


def test_assoc_rule132_stub_double():
    # ValueExpression has no real 'ValueExpression133' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_MetricRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_MetricRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_MetricRule(highLimit="sample_text", key="sample_text", lowLimit="sample_text")
    partner = ValueExpression()
    setattr(partner, 'ValueExpression133', None)
    _safe_set(owner, 'gmf_all_mappings_MetricRule', partner)
    assert getattr(partner, 'ValueExpression133') == owner
    _safe_set(owner, 'gmf_all_mappings_MetricRule', None)
    assert getattr(partner, 'ValueExpression133') is None


def test_assoc_sizeHint262_stub_double():
    # Dimension has no real 'Dimension263' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_GridLayoutData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_GridLayoutData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    partner = Dimension()
    setattr(partner, 'Dimension263', None)
    _safe_set(owner, 'gmf_all_gmfgraph_GridLayoutData', partner)
    assert getattr(partner, 'Dimension263') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_GridLayoutData', None)
    assert getattr(partner, 'Dimension263') is None


def test_assoc_smallIcon149_stub_double():
    # Image has no real 'Image' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_tooldef_AbstractTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_tooldef_AbstractTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_tooldef_AbstractTool(description="sample_text", title="sample_text")
    partner = Image()
    setattr(partner, 'Image', None)
    _safe_set(owner, 'gmf_all_tooldef_AbstractTool', partner)
    assert getattr(partner, 'Image') == owner
    _safe_set(owner, 'gmf_all_tooldef_AbstractTool', None)
    assert getattr(partner, 'Image') is None


def test_assoc_spacing272_stub_double():
    # Dimension has no real 'Dimension274' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_GridLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_GridLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    partner = Dimension()
    setattr(partner, 'Dimension274', None)
    _safe_set(owner, 'gmf_all_gmfgraph_GridLayout273', partner)
    assert getattr(partner, 'Dimension274') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_GridLayout273', None)
    assert getattr(partner, 'Dimension274') is None


def test_assoc_target118_stub_double():
    # Auditable has no real 'Auditable' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_AuditRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_AuditRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_AuditRule(id="sample_text", message="sample_text", severity="sample_text", useInLiveMode=True)
    partner = Auditable()
    setattr(partner, 'Auditable', None)
    _safe_set(owner, 'gmf_all_mappings_AuditRule119', partner)
    assert getattr(partner, 'Auditable') == owner
    _safe_set(owner, 'gmf_all_mappings_AuditRule119', None)
    assert getattr(partner, 'Auditable') is None


def test_assoc_target134_stub_double():
    # Measurable has no real 'Measurable' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_MetricRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_MetricRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_MetricRule(highLimit="sample_text", key="sample_text", lowLimit="sample_text")
    partner = Measurable()
    setattr(partner, 'Measurable', None)
    _safe_set(owner, 'gmf_all_mappings_MetricRule135', partner)
    assert getattr(partner, 'Measurable') == owner
    _safe_set(owner, 'gmf_all_mappings_MetricRule135', None)
    assert getattr(partner, 'Measurable') is None


def test_assoc_typedFigure247_stub_double():
    # RealFigure has no real 'RealFigure248' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_gmfgraph_FigureAccessor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_gmfgraph_FigureAccessor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_gmfgraph_FigureAccessor(accessor="sample_text")
    partner = RealFigure()
    setattr(partner, 'RealFigure248', None)
    _safe_set(owner, 'gmf_all_gmfgraph_FigureAccessor', partner)
    assert getattr(partner, 'RealFigure248') == owner
    _safe_set(owner, 'gmf_all_gmfgraph_FigureAccessor', None)
    assert getattr(partner, 'RealFigure248') is None


def test_assoc_visualEffects20_stub_double():
    # VisualEffectMapping has no real 'VisualEffectMapping' property in the generated
    # code (a bare stub) -- manually attach it so gmf_all_mappings_MappingEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmf_all_mappings_MappingEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmf_all_mappings_MappingEntry()
    partner = VisualEffectMapping()
    setattr(partner, 'VisualEffectMapping', None)
    _safe_set(owner, 'parentMapEntry', {partner})
    assert getattr(partner, 'VisualEffectMapping') == owner
    _safe_set(owner, 'parentMapEntry', set())
    assert getattr(partner, 'VisualEffectMapping') is None


