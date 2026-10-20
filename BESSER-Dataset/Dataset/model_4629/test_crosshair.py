from python_code import model_Arc

def test_model_Arc___init__():
    assert model_Arc.__init__(model_Arc(0, 0), 0, 0) == None


from python_code import model_GridContainer

def test_model_GridContainer___init__():
    assert model_GridContainer.__init__(model_GridContainer(0, True, 0, 0, 0, 0, model_GridContainer=set()), 0, True, 0, 0, 0, 0, model_GridContainer=set()) == None


from python_code import model_Image

def test_model_Image___init__():
    assert model_Image.__init__(model_Image('', '\x00'), '\x00\x00', '') == None


from python_code import model_Line
from python_code import model_Position
from python_code import model_XYChild

def test_model_Position___init__():
    assert model_Position.__init__(model_Position(0.0, 0.0, model_Position18=model_Line(), model_Position=model_XYChild()), 0.0, 0.0, model_Position18=model_Line(), model_Position=model_XYChild()) == None


from python_code import model_Shape

def test_model_Shape___init__():
    assert model_Shape.__init__(model_Shape(0.0, '', '', False, False), 0.0, '', '', False, False) == None


from python_code import model_SymbolReference

def test_model_SymbolReference___init__():
    assert model_SymbolReference.__init__(model_SymbolReference('', '', '', model_SymbolReference=set()), '', '', '', model_SymbolReference=set()) == None


from python_code import model_SystemCursor

def test_model_SystemCursor___init__():
    assert model_SystemCursor.__init__(model_SystemCursor(''), '') == None


from python_code import model_Text

def test_model_Text___init__():
    assert model_Text.__init__(model_Text('', '', '', '', '\x00', '', 0, False, False), '', '', '', '', '', '\x00', 0, False, False) == None

