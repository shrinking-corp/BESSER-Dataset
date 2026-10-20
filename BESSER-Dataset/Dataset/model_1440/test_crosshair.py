from python_code import RepresentationGraph_Circle

def test_RepresentationGraph_Circle___init__():
    assert RepresentationGraph_Circle.__init__(RepresentationGraph_Circle(''), '') == None


from python_code import RepresentationGraph_Diagram
from python_code import RepresentationGraph_GraphicElement

def test_RepresentationGraph_GraphicElement___init__():
    assert RepresentationGraph_GraphicElement.__init__(RepresentationGraph_GraphicElement('', '', '\x00\x00', RepresentationGraph_GraphicElement=RepresentationGraph_Diagram()), '', '', '', RepresentationGraph_GraphicElement=RepresentationGraph_Diagram()) == None


from python_code import RepresentationGraph_IconElement

def test_RepresentationGraph_IconElement___init__():
    assert RepresentationGraph_IconElement.__init__(RepresentationGraph_IconElement(''), '') == None


from python_code import RepresentationGraph_Rectangle

def test_RepresentationGraph_Rectangle___init__():
    assert RepresentationGraph_Rectangle.__init__(RepresentationGraph_Rectangle('', '\x00'), '\x00\x00', '') == None


from python_code import RepresentationGraph_Rhombus

def test_RepresentationGraph_Rhombus___init__():
    assert RepresentationGraph_Rhombus.__init__(RepresentationGraph_Rhombus('', '\x00'), '\x00\x00', '') == None

