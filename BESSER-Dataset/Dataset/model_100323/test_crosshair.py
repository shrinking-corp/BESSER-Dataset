from python_code import PNML_AnyElement

def test_PNML_AnyElement___init__():
    assert PNML_AnyElement.__init__(PNML_AnyElement('', '\x00'), '\x00\x00', '') == None


from python_code import PNML_Coordinate

def test_PNML_Coordinate___init__():
    assert PNML_Coordinate.__init__(PNML_Coordinate('', '\x00'), '\x00\x00', '') == None


from python_code import NodeGraphics
from python_code import PNML_Dimension

def test_PNML_Dimension___init__():
    assert PNML_Dimension.__init__(PNML_Dimension('', '\x00', dimension=NodeGraphics()), '\x00\x00', '', dimension=NodeGraphics()) == None


from python_code import AnnotationGraphics
from python_code import Color
from python_code import EdgeGraphics
from python_code import NodeGraphics
from python_code import PNML_Fill
from python_code import URI

def test_PNML_Fill___init__():
    assert PNML_Fill.__init__(PNML_Fill('', PNML_Fill=Color(), PNML_Fill101=Color(), PNML_Fill104=URI(), fill=NodeGraphics(), fill109=EdgeGraphics(), fill112=AnnotationGraphics()), '', PNML_Fill=Color(), PNML_Fill101=Color(), PNML_Fill104=URI(), fill=NodeGraphics(), fill109=EdgeGraphics(), fill112=AnnotationGraphics()) == None


from python_code import AnnotationGraphics
from python_code import PNML_Font

def test_PNML_Font___init__():
    assert PNML_Font.__init__(PNML_Font('', '', '', '', '', '', '', font=AnnotationGraphics()), '', '\x00', '', '', '', '', '', font=AnnotationGraphics()) == None


from python_code import PNML_IdedElement

def test_PNML_IdedElement___init__():
    assert PNML_IdedElement.__init__(PNML_IdedElement(''), '') == None


from python_code import PNML_Label
from python_code import PNML_Name

def test_PNML_Label___init__():
    assert PNML_Label.__init__(PNML_Label('', labels=PNML_Name()), '', labels=PNML_Name()) == None


from python_code import AnnotationGraphics
from python_code import Color
from python_code import EdgeGraphics
from python_code import NodeGraphics
from python_code import PNML_Line

def test_PNML_Line___init__():
    assert PNML_Line.__init__(PNML_Line('', '', '\x00\x00', PNML_Line=Color(), line=NodeGraphics(), line119=EdgeGraphics(), line122=AnnotationGraphics()), '', '', '', PNML_Line=Color(), line=NodeGraphics(), line119=EdgeGraphics(), line122=AnnotationGraphics()) == None


from python_code import Arc
from python_code import NetElement
from python_code import Node
from python_code import PNML_ToolSpecific

def test_PNML_ToolSpecific___init__():
    assert PNML_ToolSpecific.__init__(PNML_ToolSpecific('\x00\x00', '', tools20=Arc(), tools22=Node(), PNML_ToolSpecific=set(), tools=NetElement()), '', '', tools20=Arc(), tools22=Node(), PNML_ToolSpecific=set(), tools=NetElement()) == None


from python_code import PNML_URI

def test_PNML_URI___init__():
    assert PNML_URI.__init__(PNML_URI(''), '') == None

