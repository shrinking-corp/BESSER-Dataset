from python_code import draw2d_BlockFlow

def test_draw2d_BlockFlow___init__():
    assert draw2d_BlockFlow.__init__(draw2d_BlockFlow(''), '') == None


from python_code import draw2d_FlowBorder

def test_draw2d_FlowBorder___init__():
    assert draw2d_FlowBorder.__init__(draw2d_FlowBorder(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import draw2d_ImageFigure

def test_draw2d_ImageFigure___init__():
    assert draw2d_ImageFigure.__init__(draw2d_ImageFigure(''), '') == None


from python_code import draw2d_Label

def test_draw2d_Label___init__():
    assert draw2d_Label.__init__(draw2d_Label('', '', '', '', '', 0), '', '', '', '', '\x00', 0) == None


from python_code import draw2d_Font
from python_code import draw2d_LabeledBorder

def test_draw2d_LabeledBorder___init__():
    assert draw2d_LabeledBorder.__init__(draw2d_LabeledBorder('', draw2d_LabeledBorder=draw2d_Font()), '', draw2d_LabeledBorder=draw2d_Font()) == None


from python_code import draw2d_PointListShape

def test_draw2d_PointListShape___init__():
    assert draw2d_PointListShape.__init__(draw2d_PointListShape(0), 0) == None


from python_code import draw2d_Polyline

def test_draw2d_Polyline___init__():
    assert draw2d_Polyline.__init__(draw2d_Polyline(0), 0) == None


from python_code import draw2d_PolylineShape

def test_draw2d_PolylineShape___init__():
    assert draw2d_PolylineShape.__init__(draw2d_PolylineShape(0), 0) == None


from python_code import draw2d_RoundedRectangle

def test_draw2d_RoundedRectangle___init__():
    assert draw2d_RoundedRectangle.__init__(draw2d_RoundedRectangle(''), '') == None


from python_code import draw2d_Shape

def test_draw2d_Shape___init__():
    assert draw2d_Shape.__init__(draw2d_Shape(0.0, 0.0, 0.0, True, False, False, False, '', '', 0.0, '', '', ''), 0.0, 0.0, 0.0, False, False, False, True, '', '', 0.0, '', '', '') == None


from python_code import draw2d_Triangle

def test_draw2d_Triangle___init__():
    assert draw2d_Triangle.__init__(draw2d_Triangle('', '\x00'), '\x00\x00', '') == None


from python_code import draw2d_XYAnchor

def test_draw2d_XYAnchor___init__():
    assert draw2d_XYAnchor.__init__(draw2d_XYAnchor(''), '') == None

