from python_code import gmf_all_gmfgraph_AlignmentFacet
from python_code import gmf_all_gmfgraph_DiagramElement

def test_gmf_all_gmfgraph_AlignmentFacet___init__():
    assert gmf_all_gmfgraph_AlignmentFacet.__init__(gmf_all_gmfgraph_AlignmentFacet('', VisualFacet=gmf_all_gmfgraph_DiagramElement()), '', VisualFacet=gmf_all_gmfgraph_DiagramElement()) == None


from python_code import gmf_all_gmfgraph_BasicFont
from python_code import gmf_all_gmfgraph_Figure

def test_gmf_all_gmfgraph_BasicFont___init__():
    assert gmf_all_gmfgraph_BasicFont.__init__(gmf_all_gmfgraph_BasicFont('', 0, '\x00\x00', Font=gmf_all_gmfgraph_Figure()), '', 0, '', Font=gmf_all_gmfgraph_Figure()) == None


from python_code import gmf_all_gmfgraph_BorderLayoutData
from python_code import gmf_all_gmfgraph_Layoutable

def test_gmf_all_gmfgraph_BorderLayoutData___init__():
    assert gmf_all_gmfgraph_BorderLayoutData.__init__(gmf_all_gmfgraph_BorderLayoutData('', False, LayoutData=gmf_all_gmfgraph_Layoutable()), '', False, LayoutData=gmf_all_gmfgraph_Layoutable()) == None


from python_code import Figure
from python_code import FigureDescriptor
from python_code import gmf_all_gmfgraph_ChildAccess

def test_gmf_all_gmfgraph_ChildAccess___init__():
    assert gmf_all_gmfgraph_ChildAccess.__init__(gmf_all_gmfgraph_ChildAccess('', accessors=FigureDescriptor(), gmf_all_gmfgraph_ChildAccess=Figure()), '\x00', accessors=FigureDescriptor(), gmf_all_gmfgraph_ChildAccess=Figure()) == None


from python_code import MappingEntry
from python_code import Pin
from python_code import gmf_all_gmfgraph_ColorPin
from python_code import gmf_all_gmfgraph_PinOwner
from python_code import gmf_all_mappings_VisualEffectMapping

def test_gmf_all_gmfgraph_ColorPin___init__():
    assert gmf_all_gmfgraph_ColorPin.__init__(gmf_all_gmfgraph_ColorPin(False, Pin=gmf_all_mappings_VisualEffectMapping('\x00', gmf_all_mappings_VisualEffectMapping=Pin(), visualEffects=MappingEntry()), Pin286=gmf_all_gmfgraph_PinOwner()), False, Pin=gmf_all_mappings_VisualEffectMapping('', gmf_all_mappings_VisualEffectMapping=Pin(), visualEffects=MappingEntry()), Pin286=gmf_all_gmfgraph_PinOwner()) == None


from python_code import ChildAccess
from python_code import gmf_all_gmfgraph_Compartment

def test_gmf_all_gmfgraph_Compartment___init__():
    assert gmf_all_gmfgraph_Compartment.__init__(gmf_all_gmfgraph_Compartment(False, False, gmf_all_gmfgraph_Compartment=ChildAccess()), False, False, gmf_all_gmfgraph_Compartment=ChildAccess()) == None


from python_code import Color
from python_code import gmf_all_gmfgraph_BorderRef
from python_code import gmf_all_gmfgraph_CompoundBorder
from python_code import gmf_all_gmfgraph_ConstantColor
from python_code import gmf_all_gmfgraph_Figure
from python_code import gmf_all_gmfgraph_FigureGallery
from python_code import gmf_all_gmfgraph_LineBorder

def test_gmf_all_gmfgraph_ConstantColor___init__():
    assert gmf_all_gmfgraph_ConstantColor.__init__(gmf_all_gmfgraph_ConstantColor('', Color=gmf_all_gmfgraph_Figure(), Color205=gmf_all_gmfgraph_Figure(), Color253=gmf_all_gmfgraph_LineBorder(0, gmf_all_gmfgraph_LineBorder=Color(), Border260=gmf_all_gmfgraph_CompoundBorder(), Border221=gmf_all_gmfgraph_Figure(), Border251=gmf_all_gmfgraph_BorderRef(), Border=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), Border257=gmf_all_gmfgraph_CompoundBorder())), '', Color=gmf_all_gmfgraph_Figure(), Color205=gmf_all_gmfgraph_Figure(), Color253=gmf_all_gmfgraph_LineBorder(0, gmf_all_gmfgraph_LineBorder=Color(), Border260=gmf_all_gmfgraph_CompoundBorder(), Border221=gmf_all_gmfgraph_Figure(), Border251=gmf_all_gmfgraph_BorderRef(), Border=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), Border257=gmf_all_gmfgraph_CompoundBorder())) == None


from python_code import gmf_all_gmfgraph_CustomAttribute

def test_gmf_all_gmfgraph_CustomAttribute___init__():
    assert gmf_all_gmfgraph_CustomAttribute.__init__(gmf_all_gmfgraph_CustomAttribute('\x00\x00', '', False, True), '', '', False, False) == None


from python_code import gmf_all_gmfgraph_CustomClass

def test_gmf_all_gmfgraph_CustomClass___init__():
    assert gmf_all_gmfgraph_CustomClass.__init__(gmf_all_gmfgraph_CustomClass(''), '') == None


from python_code import MappingEntry
from python_code import Pin
from python_code import gmf_all_gmfgraph_CustomPin
from python_code import gmf_all_gmfgraph_PinOwner
from python_code import gmf_all_mappings_VisualEffectMapping

def test_gmf_all_gmfgraph_CustomPin___init__():
    assert gmf_all_gmfgraph_CustomPin.__init__(gmf_all_gmfgraph_CustomPin('', '', Pin=gmf_all_mappings_VisualEffectMapping('', gmf_all_mappings_VisualEffectMapping=Pin(), visualEffects=MappingEntry()), Pin286=gmf_all_gmfgraph_PinOwner()), '', '', Pin=gmf_all_mappings_VisualEffectMapping('', gmf_all_mappings_VisualEffectMapping=Pin(), visualEffects=MappingEntry()), Pin286=gmf_all_gmfgraph_PinOwner()) == None


from python_code import ChildAccess
from python_code import gmf_all_gmfgraph_Canvas
from python_code import gmf_all_gmfgraph_DiagramLabel
from python_code import gmf_all_mappings_NodeMapping

def test_gmf_all_gmfgraph_DiagramLabel___init__():
    assert gmf_all_gmfgraph_DiagramLabel.__init__(gmf_all_gmfgraph_DiagramLabel(False, False, gmf_all_gmfgraph_DiagramLabel=ChildAccess(), gmf_all_gmfgraph_DiagramLabel196=ChildAccess(), Node169=gmf_all_gmfgraph_Canvas(), Node=gmf_all_mappings_NodeMapping()), False, False, gmf_all_gmfgraph_DiagramLabel=ChildAccess(), gmf_all_gmfgraph_DiagramLabel196=ChildAccess(), Node169=gmf_all_gmfgraph_Canvas(), Node=gmf_all_mappings_NodeMapping()) == None


from python_code import gmf_all_gmfgraph_Dimension

def test_gmf_all_gmfgraph_Dimension___init__():
    assert gmf_all_gmfgraph_Dimension.__init__(gmf_all_gmfgraph_Dimension(0, 0), 0, 0) == None


from python_code import RealFigure
from python_code import gmf_all_gmfgraph_FigureAccessor

def test_gmf_all_gmfgraph_FigureAccessor___init__():
    assert gmf_all_gmfgraph_FigureAccessor.__init__(gmf_all_gmfgraph_FigureAccessor('', gmf_all_gmfgraph_FigureAccessor=RealFigure()), '', gmf_all_gmfgraph_FigureAccessor=RealFigure()) == None


from python_code import gmf_all_gmfgraph_FigureGallery

def test_gmf_all_gmfgraph_FigureGallery___init__():
    assert gmf_all_gmfgraph_FigureGallery.__init__(gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), '', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()) == None


from python_code import gmf_all_gmfgraph_FigureGallery
from python_code import gmf_all_gmfgraph_FlowLayout
from python_code import gmf_all_gmfgraph_LayoutRef
from python_code import gmf_all_gmfgraph_Layoutable

def test_gmf_all_gmfgraph_FlowLayout___init__():
    assert gmf_all_gmfgraph_FlowLayout.__init__(gmf_all_gmfgraph_FlowLayout(False, False, True, '', '', 0, 0, Layout269=gmf_all_gmfgraph_LayoutRef(), Layout=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), Layout267=gmf_all_gmfgraph_Layoutable()), False, False, False, '', '', 0, 0, Layout269=gmf_all_gmfgraph_LayoutRef(), Layout=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), Layout267=gmf_all_gmfgraph_Layoutable()) == None


from python_code import gmf_all_gmfgraph_DiagramElement
from python_code import gmf_all_gmfgraph_GeneralFacet

def test_gmf_all_gmfgraph_GeneralFacet___init__():
    assert gmf_all_gmfgraph_GeneralFacet.__init__(gmf_all_gmfgraph_GeneralFacet('', '\x00', VisualFacet=gmf_all_gmfgraph_DiagramElement()), '\x00\x00', '', VisualFacet=gmf_all_gmfgraph_DiagramElement()) == None


from python_code import gmf_all_gmfgraph_DiagramElement
from python_code import gmf_all_gmfgraph_GradientFacet

def test_gmf_all_gmfgraph_GradientFacet___init__():
    assert gmf_all_gmfgraph_GradientFacet.__init__(gmf_all_gmfgraph_GradientFacet('', VisualFacet=gmf_all_gmfgraph_DiagramElement()), '', VisualFacet=gmf_all_gmfgraph_DiagramElement()) == None


from python_code import Dimension
from python_code import gmf_all_gmfgraph_FigureGallery
from python_code import gmf_all_gmfgraph_GridLayout
from python_code import gmf_all_gmfgraph_LayoutRef
from python_code import gmf_all_gmfgraph_Layoutable

def test_gmf_all_gmfgraph_GridLayout___init__():
    assert gmf_all_gmfgraph_GridLayout.__init__(gmf_all_gmfgraph_GridLayout(0, False, gmf_all_gmfgraph_GridLayout=Dimension(), gmf_all_gmfgraph_GridLayout273=Dimension(), Layout269=gmf_all_gmfgraph_LayoutRef(), Layout=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), Layout267=gmf_all_gmfgraph_Layoutable()), 0, False, gmf_all_gmfgraph_GridLayout=Dimension(), gmf_all_gmfgraph_GridLayout273=Dimension(), Layout269=gmf_all_gmfgraph_LayoutRef(), Layout=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), Layout267=gmf_all_gmfgraph_Layoutable()) == None


from python_code import Dimension
from python_code import gmf_all_gmfgraph_GridLayoutData
from python_code import gmf_all_gmfgraph_Layoutable

def test_gmf_all_gmfgraph_GridLayoutData___init__():
    assert gmf_all_gmfgraph_GridLayoutData.__init__(gmf_all_gmfgraph_GridLayoutData(False, True, '', '', 0, 0, 0, gmf_all_gmfgraph_GridLayoutData=Dimension(), LayoutData=gmf_all_gmfgraph_Layoutable()), False, False, '', '', 0, 0, 0, gmf_all_gmfgraph_GridLayoutData=Dimension(), LayoutData=gmf_all_gmfgraph_Layoutable()) == None


from python_code import gmf_all_gmfgraph_Identity

def test_gmf_all_gmfgraph_Identity___init__():
    assert gmf_all_gmfgraph_Identity.__init__(gmf_all_gmfgraph_Identity(''), '') == None


from python_code import gmf_all_gmfgraph_Insets

def test_gmf_all_gmfgraph_Insets___init__():
    assert gmf_all_gmfgraph_Insets.__init__(gmf_all_gmfgraph_Insets(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import RealFigure
from python_code import gmf_all_gmfgraph_FigureAccessor
from python_code import gmf_all_gmfgraph_FigureGallery
from python_code import gmf_all_gmfgraph_FigureRef
from python_code import gmf_all_gmfgraph_Label

def test_gmf_all_gmfgraph_Label___init__():
    assert gmf_all_gmfgraph_Label.__init__(gmf_all_gmfgraph_Label('', RealFigure248=gmf_all_gmfgraph_FigureAccessor('', gmf_all_gmfgraph_FigureAccessor=RealFigure()), RealFigure237=gmf_all_gmfgraph_FigureRef(), RealFigure=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set())), '', RealFigure248=gmf_all_gmfgraph_FigureAccessor('', gmf_all_gmfgraph_FigureAccessor=RealFigure()), RealFigure237=gmf_all_gmfgraph_FigureRef(), RealFigure=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set())) == None


from python_code import gmf_all_gmfgraph_DiagramElement
from python_code import gmf_all_gmfgraph_LabelOffsetFacet

def test_gmf_all_gmfgraph_LabelOffsetFacet___init__():
    assert gmf_all_gmfgraph_LabelOffsetFacet.__init__(gmf_all_gmfgraph_LabelOffsetFacet(0, 0, VisualFacet=gmf_all_gmfgraph_DiagramElement()), 0, 0, VisualFacet=gmf_all_gmfgraph_DiagramElement()) == None


from python_code import Color
from python_code import gmf_all_gmfgraph_BorderRef
from python_code import gmf_all_gmfgraph_CompoundBorder
from python_code import gmf_all_gmfgraph_Figure
from python_code import gmf_all_gmfgraph_FigureGallery
from python_code import gmf_all_gmfgraph_LineBorder

def test_gmf_all_gmfgraph_LineBorder___init__():
    assert gmf_all_gmfgraph_LineBorder.__init__(gmf_all_gmfgraph_LineBorder(0, gmf_all_gmfgraph_LineBorder=Color(), Border260=gmf_all_gmfgraph_CompoundBorder(), Border221=gmf_all_gmfgraph_Figure(), Border251=gmf_all_gmfgraph_BorderRef(), Border=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), Border257=gmf_all_gmfgraph_CompoundBorder()), 0, gmf_all_gmfgraph_LineBorder=Color(), Border260=gmf_all_gmfgraph_CompoundBorder(), Border221=gmf_all_gmfgraph_Figure(), Border251=gmf_all_gmfgraph_BorderRef(), Border=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), Border257=gmf_all_gmfgraph_CompoundBorder()) == None


from python_code import ChildAccess
from python_code import gmf_all_gmfgraph_Node

def test_gmf_all_gmfgraph_Node___init__():
    assert gmf_all_gmfgraph_Node.__init__(gmf_all_gmfgraph_Node('', '\x00', gmf_all_gmfgraph_Node=ChildAccess()), '\x00\x00', '', gmf_all_gmfgraph_Node=ChildAccess()) == None


from python_code import gmf_all_gmfgraph_Pin

def test_gmf_all_gmfgraph_Pin___init__():
    assert gmf_all_gmfgraph_Pin.__init__(gmf_all_gmfgraph_Pin()) == None

def test_gmf_all_gmfgraph_Pin_getOperationType():
    assert gmf_all_gmfgraph_Pin.getOperationType(gmf_all_gmfgraph_Pin()) == None

def test_gmf_all_gmfgraph_Pin_getOperationName():
    assert gmf_all_gmfgraph_Pin.getOperationName(gmf_all_gmfgraph_Pin()) == None


from python_code import gmf_all_gmfgraph_Point

def test_gmf_all_gmfgraph_Point___init__():
    assert gmf_all_gmfgraph_Point.__init__(gmf_all_gmfgraph_Point(0, 0), 0, 0) == None


from python_code import Color
from python_code import gmf_all_gmfgraph_BorderRef
from python_code import gmf_all_gmfgraph_CompoundBorder
from python_code import gmf_all_gmfgraph_Figure
from python_code import gmf_all_gmfgraph_FigureGallery
from python_code import gmf_all_gmfgraph_LineBorder
from python_code import gmf_all_gmfgraph_RGBColor

def test_gmf_all_gmfgraph_RGBColor___init__():
    assert gmf_all_gmfgraph_RGBColor.__init__(gmf_all_gmfgraph_RGBColor(0, 0, 0, Color=gmf_all_gmfgraph_Figure(), Color205=gmf_all_gmfgraph_Figure(), Color253=gmf_all_gmfgraph_LineBorder(0, gmf_all_gmfgraph_LineBorder=Color(), Border260=gmf_all_gmfgraph_CompoundBorder(), Border221=gmf_all_gmfgraph_Figure(), Border251=gmf_all_gmfgraph_BorderRef(), Border=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), Border257=gmf_all_gmfgraph_CompoundBorder())), 0, 0, 0, Color=gmf_all_gmfgraph_Figure(), Color205=gmf_all_gmfgraph_Figure(), Color253=gmf_all_gmfgraph_LineBorder(0, gmf_all_gmfgraph_LineBorder=Color(), Border260=gmf_all_gmfgraph_CompoundBorder(), Border221=gmf_all_gmfgraph_Figure(), Border251=gmf_all_gmfgraph_BorderRef(), Border=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set()), Border257=gmf_all_gmfgraph_CompoundBorder())) == None


from python_code import gmf_all_gmfgraph_RealFigure

def test_gmf_all_gmfgraph_RealFigure___init__():
    assert gmf_all_gmfgraph_RealFigure.__init__(gmf_all_gmfgraph_RealFigure('', gmf_all_gmfgraph_RealFigure=set()), '', gmf_all_gmfgraph_RealFigure=set()) == None


from python_code import gmf_all_gmfgraph_Rectangle2D

def test_gmf_all_gmfgraph_Rectangle2D___init__():
    assert gmf_all_gmfgraph_Rectangle2D.__init__(gmf_all_gmfgraph_Rectangle2D(0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0) == None


from python_code import gmf_all_gmfgraph_RoundedRectangle

def test_gmf_all_gmfgraph_RoundedRectangle___init__():
    assert gmf_all_gmfgraph_RoundedRectangle.__init__(gmf_all_gmfgraph_RoundedRectangle(0, 0), 0, 0) == None


from python_code import gmf_all_gmfgraph_SVGProperty

def test_gmf_all_gmfgraph_SVGProperty___init__():
    assert gmf_all_gmfgraph_SVGProperty.__init__(gmf_all_gmfgraph_SVGProperty('', '', '', '', '', False), '', '', '', '', '\x00', False) == None


from python_code import RealFigure
from python_code import gmf_all_gmfgraph_FigureAccessor
from python_code import gmf_all_gmfgraph_FigureGallery
from python_code import gmf_all_gmfgraph_FigureRef
from python_code import gmf_all_gmfgraph_VerticalLabel

def test_gmf_all_gmfgraph_VerticalLabel___init__():
    assert gmf_all_gmfgraph_VerticalLabel.__init__(gmf_all_gmfgraph_VerticalLabel('', RealFigure248=gmf_all_gmfgraph_FigureAccessor('', gmf_all_gmfgraph_FigureAccessor=RealFigure()), RealFigure237=gmf_all_gmfgraph_FigureRef(), RealFigure=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set())), '', RealFigure248=gmf_all_gmfgraph_FigureAccessor('', gmf_all_gmfgraph_FigureAccessor=RealFigure()), RealFigure237=gmf_all_gmfgraph_FigureRef(), RealFigure=gmf_all_gmfgraph_FigureGallery('', gmf_all_gmfgraph_FigureGallery185=set(), gmf_all_gmfgraph_FigureGallery=set(), gmf_all_gmfgraph_FigureGallery181=set(), gmf_all_gmfgraph_FigureGallery183=set())) == None


from python_code import AuditContainer
from python_code import gmf_all_mappings_AuditContainer

def test_gmf_all_mappings_AuditContainer___init__():
    assert gmf_all_mappings_AuditContainer.__init__(gmf_all_mappings_AuditContainer('', '', '', childContainers=AuditContainer(), container=set(), parentContainer=set()), '', '', '', childContainers=AuditContainer(), container=set(), parentContainer=set()) == None


from python_code import AuditContainer
from python_code import Auditable
from python_code import Constraint
from python_code import gmf_all_mappings_AuditRule

def test_gmf_all_mappings_AuditRule___init__():
    assert gmf_all_mappings_AuditRule.__init__(gmf_all_mappings_AuditRule('', '', False, '', gmf_all_mappings_AuditRule=Constraint(), gmf_all_mappings_AuditRule119=Auditable(), audits=AuditContainer()), '\x00', '', False, '', gmf_all_mappings_AuditRule=Constraint(), gmf_all_mappings_AuditRule119=Auditable(), audits=AuditContainer()) == None


from python_code import AuditContainer
from python_code import Auditable
from python_code import Constraint
from python_code import gmf_all_mappings_AuditRule
from python_code import gmf_all_mappings_DomainAttributeTarget
from python_code import mappings_gmf_all_EAttribute

def test_gmf_all_mappings_DomainAttributeTarget___init__():
    assert gmf_all_mappings_DomainAttributeTarget.__init__(gmf_all_mappings_DomainAttributeTarget(False, gmf_all_mappings_DomainAttributeTarget=mappings_gmf_all_EAttribute(), Auditable=gmf_all_mappings_AuditRule('', '', False, '', gmf_all_mappings_AuditRule=Constraint(), gmf_all_mappings_AuditRule119=Auditable(), audits=AuditContainer())), True, gmf_all_mappings_DomainAttributeTarget=mappings_gmf_all_EAttribute(), Auditable=gmf_all_mappings_AuditRule('', '', False, '', gmf_all_mappings_AuditRule=Constraint(), gmf_all_mappings_AuditRule119=Auditable(), audits=AuditContainer())) == None

