from python_code import VisualInterface_Arc

def test_VisualInterface_Arc___init__():
    assert VisualInterface_Arc.__init__(VisualInterface_Arc(0, 0), 0, 0) == None


from python_code import VisualInterface_BorderContainer

def test_VisualInterface_BorderContainer___init__():
    assert VisualInterface_BorderContainer.__init__(VisualInterface_BorderContainer(0, 0, VisualInterface_BorderContainer=set()), 0, 0, VisualInterface_BorderContainer=set()) == None


from python_code import VisualInterface_GridContainer

def test_VisualInterface_GridContainer___init__():
    assert VisualInterface_GridContainer.__init__(VisualInterface_GridContainer(0, True, 0, 0, 0, 0, VisualInterface_GridContainer=set()), 0, True, 0, 0, 0, 0, VisualInterface_GridContainer=set()) == None


from python_code import VisualInterface_Image

def test_VisualInterface_Image___init__():
    assert VisualInterface_Image.__init__(VisualInterface_Image(''), '') == None


from python_code import VisualInterface_Line
from python_code import VisualInterface_Position
from python_code import VisualInterface_XYChild

def test_VisualInterface_Position___init__():
    assert VisualInterface_Position.__init__(VisualInterface_Position(0.0, 0.0, VisualInterface_Position=VisualInterface_XYChild(), VisualInterface_Position18=VisualInterface_Line()), 0.0, 0.0, VisualInterface_Position=VisualInterface_XYChild(), VisualInterface_Position18=VisualInterface_Line()) == None


from python_code import VisualInterface_Shape

def test_VisualInterface_Shape___init__():
    assert VisualInterface_Shape.__init__(VisualInterface_Shape(0.0, '', '', False, False), 0.0, '', '', False, False) == None


from python_code import VisualInterface_SymbolReference

def test_VisualInterface_SymbolReference___init__():
    assert VisualInterface_SymbolReference.__init__(VisualInterface_SymbolReference('', '', '', VisualInterface_SymbolReference=set()), '', '', '', VisualInterface_SymbolReference=set()) == None


from python_code import VisualInterface_SystemCursor

def test_VisualInterface_SystemCursor___init__():
    assert VisualInterface_SystemCursor.__init__(VisualInterface_SystemCursor(''), '') == None


from python_code import VisualInterface_Text

def test_VisualInterface_Text___init__():
    assert VisualInterface_Text.__init__(VisualInterface_Text('', '', '', '', '\x00', '', 0, False, False), '', '', '', '', '', '\x00', 0, False, False) == None

