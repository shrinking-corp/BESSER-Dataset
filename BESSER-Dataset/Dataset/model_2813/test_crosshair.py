from python_code import shape_AnchorFixPointPosition

def test_shape_AnchorFixPointPosition___init__():
    assert shape_AnchorFixPointPosition.__init__(shape_AnchorFixPointPosition(0, 0), 0, 0) == None


from python_code import shape_AnchorPredefinied

def test_shape_AnchorPredefinied___init__():
    assert shape_AnchorPredefinied.__init__(shape_AnchorPredefinied(''), '') == None


from python_code import shape_AnchorRelativePosition

def test_shape_AnchorRelativePosition___init__():
    assert shape_AnchorRelativePosition.__init__(shape_AnchorRelativePosition('', '\x00'), '\x00\x00', '') == None


from python_code import shape_Compartment
from python_code import shape_CompartmentShape

def test_shape_Compartment___init__():
    assert shape_Compartment.__init__(shape_Compartment('', shape_Compartment=shape_CompartmentShape()), '', shape_Compartment=shape_CompartmentShape()) == None


from python_code import shape_ConnectionDefinition
from python_code import shape_ShapestyleLayout

def test_shape_ConnectionDefinition___init__():
    assert shape_ConnectionDefinition.__init__(shape_ConnectionDefinition('', shape_ConnectionDefinition=shape_ShapestyleLayout(), shape_ConnectionDefinition3=set()), '', shape_ConnectionDefinition=shape_ShapestyleLayout(), shape_ConnectionDefinition3=set()) == None


from python_code import shape_LineLayout
from python_code import shape_Point
from python_code import shape_PolyLineLayout

def test_shape_Point___init__():
    assert shape_Point.__init__(shape_Point('\x00\x00', '', 0, 0, shape_Point=shape_LineLayout(), shape_Point98=shape_PolyLineLayout()), '', '', 0, 0, shape_Point=shape_LineLayout(), shape_Point98=shape_PolyLineLayout()) == None


from python_code import shape_Ellipse
from python_code import shape_Polygon
from python_code import shape_Rectangle
from python_code import shape_RoundedRectangle
from python_code import shape_Shape
from python_code import shape_ShapeDefinition

def test_shape_Shape___init__():
    assert shape_Shape.__init__(shape_Shape('', shape_Shape39=shape_Rectangle(), shape_Shape44=shape_RoundedRectangle(), shape_Shape49=shape_Polygon(), shape_Shape=shape_ShapeDefinition(), shape_Shape57=shape_Ellipse()), '', shape_Shape39=shape_Rectangle(), shape_Shape44=shape_RoundedRectangle(), shape_Shape49=shape_Polygon(), shape_Shape=shape_ShapeDefinition(), shape_Shape57=shape_Ellipse()) == None


from python_code import shape_ShapeContainer
from python_code import shape_ShapeContainerElement

def test_shape_ShapeContainerElement___init__():
    assert shape_ShapeContainerElement.__init__(shape_ShapeContainerElement('', '\x00', shape_ShapeContainerElement=shape_ShapeContainer()), '\x00\x00', '', shape_ShapeContainerElement=shape_ShapeContainer()) == None


from python_code import shape_ShapeDefinition
from python_code import shape_ShapeLayout

def test_shape_ShapeLayout___init__():
    assert shape_ShapeLayout.__init__(shape_ShapeLayout(0, 0, 0, 0, '', '', '', shape_ShapeLayout=shape_ShapeDefinition()), 0, 0, 0, 0, '', '', '', shape_ShapeLayout=shape_ShapeDefinition()) == None

