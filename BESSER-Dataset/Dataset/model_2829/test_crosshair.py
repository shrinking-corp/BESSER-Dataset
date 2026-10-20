from python_code import mm_Property
from python_code import mm_PropertyContainer

def test_mm_Property___init__():
    assert mm_Property.__init__(mm_Property('', '\x00', mm_Property=mm_PropertyContainer()), '\x00\x00', '', mm_Property=mm_PropertyContainer()) == None


from python_code import GraphicsAlgorithm
from python_code import PictogramElement
from python_code import mm_algorithms_GraphicsAlgorithm
from python_code import styles_Style

def test_mm_algorithms_GraphicsAlgorithm___init__():
    assert mm_algorithms_GraphicsAlgorithm.__init__(mm_algorithms_GraphicsAlgorithm(0, 0, 0, 0, mm_algorithms_GraphicsAlgorithm=styles_Style(), parentGraphicsAlgorithm=set(), graphicsAlgorithmChildren=GraphicsAlgorithm(), graphicsAlgorithm=PictogramElement()), 0, 0, 0, 0, mm_algorithms_GraphicsAlgorithm=styles_Style(), parentGraphicsAlgorithm=set(), graphicsAlgorithmChildren=GraphicsAlgorithm(), graphicsAlgorithm=PictogramElement()) == None


from python_code import GraphicsAlgorithm
from python_code import PictogramElement
from python_code import PictogramLink
from python_code import mm_algorithms_GraphicsAlgorithm
from python_code import mm_algorithms_PlatformGraphicsAlgorithm
from python_code import mm_pictograms_Anchor
from python_code import mm_pictograms_PictogramElement
from python_code import styles_Style

def test_mm_algorithms_PlatformGraphicsAlgorithm___init__():
    assert mm_algorithms_PlatformGraphicsAlgorithm.__init__(mm_algorithms_PlatformGraphicsAlgorithm('', GraphicsAlgorithm39=mm_algorithms_GraphicsAlgorithm(0, 0, 0, 0, mm_algorithms_GraphicsAlgorithm=styles_Style(), parentGraphicsAlgorithm=set(), graphicsAlgorithmChildren=GraphicsAlgorithm(), graphicsAlgorithm=PictogramElement()), GraphicsAlgorithm=mm_pictograms_PictogramElement(False, False, pictogramElement=GraphicsAlgorithm(), pictogramElement12=PictogramLink()), GraphicsAlgorithm41=mm_algorithms_GraphicsAlgorithm(0, 0, 0, 0, mm_algorithms_GraphicsAlgorithm=styles_Style(), parentGraphicsAlgorithm=set(), graphicsAlgorithmChildren=GraphicsAlgorithm(), graphicsAlgorithm=PictogramElement()), GraphicsAlgorithm25=mm_pictograms_Anchor()), '', GraphicsAlgorithm39=mm_algorithms_GraphicsAlgorithm(0, 0, 0, 0, mm_algorithms_GraphicsAlgorithm=styles_Style(), parentGraphicsAlgorithm=set(), graphicsAlgorithmChildren=GraphicsAlgorithm(), graphicsAlgorithm=PictogramElement()), GraphicsAlgorithm=mm_pictograms_PictogramElement(False, False, pictogramElement=GraphicsAlgorithm(), pictogramElement12=PictogramLink()), GraphicsAlgorithm41=mm_algorithms_GraphicsAlgorithm(0, 0, 0, 0, mm_algorithms_GraphicsAlgorithm=styles_Style(), parentGraphicsAlgorithm=set(), graphicsAlgorithmChildren=GraphicsAlgorithm(), graphicsAlgorithm=PictogramElement()), GraphicsAlgorithm25=mm_pictograms_Anchor()) == None


from python_code import GraphicsAlgorithm
from python_code import PictogramElement
from python_code import PictogramLink
from python_code import mm_algorithms_GraphicsAlgorithm
from python_code import mm_algorithms_RoundedRectangle
from python_code import mm_pictograms_Anchor
from python_code import mm_pictograms_AnchorContainer
from python_code import mm_pictograms_PictogramElement
from python_code import styles_Style

def test_mm_algorithms_RoundedRectangle___init__():
    assert mm_algorithms_RoundedRectangle.__init__(mm_algorithms_RoundedRectangle(0, 0, GraphicsAlgorithm39=mm_algorithms_GraphicsAlgorithm(0, 0, 0, 0, mm_algorithms_GraphicsAlgorithm=styles_Style(), parentGraphicsAlgorithm=set(), graphicsAlgorithmChildren=GraphicsAlgorithm(), graphicsAlgorithm=mm_pictograms_AnchorContainer()), GraphicsAlgorithm=mm_pictograms_PictogramElement(True, False, pictogramElement=GraphicsAlgorithm(), pictogramElement12=PictogramLink()), GraphicsAlgorithm41=mm_algorithms_GraphicsAlgorithm(0, 0, 0, 0, mm_algorithms_GraphicsAlgorithm=styles_Style(), parentGraphicsAlgorithm=set(), graphicsAlgorithmChildren=GraphicsAlgorithm(), graphicsAlgorithm=PictogramElement()), GraphicsAlgorithm25=mm_pictograms_Anchor()), 0, 0, GraphicsAlgorithm39=mm_algorithms_GraphicsAlgorithm(0, 0, 0, 0, mm_algorithms_GraphicsAlgorithm=styles_Style(), parentGraphicsAlgorithm=set(), graphicsAlgorithmChildren=GraphicsAlgorithm(), graphicsAlgorithm=PictogramElement()), GraphicsAlgorithm=mm_pictograms_PictogramElement(False, False, pictogramElement=GraphicsAlgorithm(), pictogramElement12=PictogramLink()), GraphicsAlgorithm41=mm_algorithms_GraphicsAlgorithm(0, 0, 0, 0, mm_algorithms_GraphicsAlgorithm=styles_Style(), parentGraphicsAlgorithm=set(), graphicsAlgorithmChildren=GraphicsAlgorithm(), graphicsAlgorithm=PictogramElement()), GraphicsAlgorithm25=mm_pictograms_Anchor()) == None


from python_code import mm_pictograms_AdvancedAnchor
from python_code import mm_pictograms_AnchorContainer
from python_code import mm_pictograms_Connection

def test_mm_pictograms_AdvancedAnchor___init__():
    assert mm_pictograms_AdvancedAnchor.__init__(mm_pictograms_AdvancedAnchor(True, Anchor=mm_pictograms_Connection(), Anchor16=mm_pictograms_Connection(), Anchor28=mm_pictograms_AnchorContainer()), False, Anchor=mm_pictograms_Connection(), Anchor16=mm_pictograms_Connection(), Anchor28=mm_pictograms_AnchorContainer()) == None


from python_code import mm_pictograms_BoxRelativeAnchor

def test_mm_pictograms_BoxRelativeAnchor___init__():
    assert mm_pictograms_BoxRelativeAnchor.__init__(mm_pictograms_BoxRelativeAnchor(0.0, 0.0), 0.0, 0.0) == None


from python_code import Connection
from python_code import mm_pictograms_ConnectionDecorator
from python_code import mm_pictograms_ContainerShape

def test_mm_pictograms_ConnectionDecorator___init__():
    assert mm_pictograms_ConnectionDecorator.__init__(mm_pictograms_ConnectionDecorator(False, 0.0, connectionDecorators=Connection(), Shape=mm_pictograms_ContainerShape()), True, 0.0, connectionDecorators=Connection(), Shape=mm_pictograms_ContainerShape()) == None


from python_code import mm_pictograms_Diagram

def test_mm_pictograms_Diagram___init__():
    assert mm_pictograms_Diagram.__init__(mm_pictograms_Diagram(0, '', '', False, False, 0, '', parent=set(), mm_pictograms_Diagram=set(), mm_pictograms_Diagram7=set(), mm_pictograms_Diagram9=set()), 0, '', '', True, False, 0, '', parent=set(), mm_pictograms_Diagram=set(), mm_pictograms_Diagram7=set(), mm_pictograms_Diagram9=set()) == None


from python_code import GraphicsAlgorithm
from python_code import PictogramLink
from python_code import mm_pictograms_PictogramElement

def test_mm_pictograms_PictogramElement___init__():
    assert mm_pictograms_PictogramElement.__init__(mm_pictograms_PictogramElement(False, False, pictogramElement=GraphicsAlgorithm(), pictogramElement12=PictogramLink()), False, True, pictogramElement=GraphicsAlgorithm(), pictogramElement12=PictogramLink()) == None


from python_code import mm_styles_AbstractStyle
from python_code import styles_Color
from python_code import styles_RenderingStyle

def test_mm_styles_AbstractStyle___init__():
    assert mm_styles_AbstractStyle.__init__(mm_styles_AbstractStyle('', '', '', '', '', mm_styles_AbstractStyle=styles_Color(), mm_styles_AbstractStyle58=styles_Color(), mm_styles_AbstractStyle61=styles_RenderingStyle()), '', '', '', '', '', mm_styles_AbstractStyle=styles_Color(), mm_styles_AbstractStyle58=styles_Color(), mm_styles_AbstractStyle61=styles_RenderingStyle()) == None


from python_code import mm_styles_AdaptedGradientColoredAreas

def test_mm_styles_AdaptedGradientColoredAreas___init__():
    assert mm_styles_AdaptedGradientColoredAreas.__init__(mm_styles_AdaptedGradientColoredAreas('\x00\x00', '', mm_styles_AdaptedGradientColoredAreas=set()), '', '', mm_styles_AdaptedGradientColoredAreas=set()) == None


from python_code import mm_styles_Color

def test_mm_styles_Color___init__():
    assert mm_styles_Color.__init__(mm_styles_Color(0, 0, 0), 0, 0, 0) == None


from python_code import mm_styles_Font

def test_mm_styles_Font___init__():
    assert mm_styles_Font.__init__(mm_styles_Font('\x00\x00', 0, False, True), '', 0, False, False) == None


from python_code import mm_styles_GradientColoredAreas

def test_mm_styles_GradientColoredAreas___init__():
    assert mm_styles_GradientColoredAreas.__init__(mm_styles_GradientColoredAreas('', mm_styles_GradientColoredAreas=set()), '', mm_styles_GradientColoredAreas=set()) == None


from python_code import mm_styles_GradientColoredLocation
from python_code import styles_Color

def test_mm_styles_GradientColoredLocation___init__():
    assert mm_styles_GradientColoredLocation.__init__(mm_styles_GradientColoredLocation('', '\x00', mm_styles_GradientColoredLocation=styles_Color()), '\x00\x00', '', mm_styles_GradientColoredLocation=styles_Color()) == None


from python_code import mm_styles_Point

def test_mm_styles_Point___init__():
    assert mm_styles_Point.__init__(mm_styles_Point(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import mm_styles_PrecisionPoint

def test_mm_styles_PrecisionPoint___init__():
    assert mm_styles_PrecisionPoint.__init__(mm_styles_PrecisionPoint(0.0, 0.0), 0.0, 0.0) == None


from python_code import mm_styles_Style
from python_code import styles_Font
from python_code import styles_mm_StyleContainer

def test_mm_styles_Style___init__():
    assert mm_styles_Style.__init__(mm_styles_Style('', '', '', '', '\x00', '', '', '', '', mm_styles_Style=styles_Font(), styles=styles_mm_StyleContainer()), '', '', '', '', '', '\x00', '', '', '', mm_styles_Style=styles_Font(), styles=styles_mm_StyleContainer()) == None


from python_code import mm_styles_TextStyle
from python_code import styles_Color
from python_code import styles_Font

def test_mm_styles_TextStyle___init__():
    assert mm_styles_TextStyle.__init__(mm_styles_TextStyle(False, '', False, mm_styles_TextStyle=styles_Font(), mm_styles_TextStyle73=styles_Color(), mm_styles_TextStyle76=styles_Color(), mm_styles_TextStyle79=styles_Color(), mm_styles_TextStyle82=styles_Color()), False, '', False, mm_styles_TextStyle=styles_Font(), mm_styles_TextStyle73=styles_Color(), mm_styles_TextStyle76=styles_Color(), mm_styles_TextStyle79=styles_Color(), mm_styles_TextStyle82=styles_Color()) == None


from python_code import mm_styles_TextStyleRegion
from python_code import styles_TextStyle

def test_mm_styles_TextStyleRegion___init__():
    assert mm_styles_TextStyleRegion.__init__(mm_styles_TextStyleRegion(0, 0, mm_styles_TextStyleRegion=styles_TextStyle()), 0, 0, mm_styles_TextStyleRegion=styles_TextStyle()) == None

