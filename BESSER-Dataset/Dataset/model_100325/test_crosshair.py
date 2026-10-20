from python_code import PNML_IdedElement

def test_PNML_IdedElement___init__():
    assert PNML_IdedElement.__init__(PNML_IdedElement(''), '') == None


from python_code import PNML_Label
from python_code import PNML_Name

def test_PNML_Label___init__():
    assert PNML_Label.__init__(PNML_Label('', labels=PNML_Name()), '', labels=PNML_Name()) == None


from python_code import PNML_LocatedElement

def test_PNML_LocatedElement___init__():
    assert PNML_LocatedElement.__init__(PNML_LocatedElement(''), '') == None


from python_code import PNML_URI

def test_PNML_URI___init__():
    assert PNML_URI.__init__(PNML_URI(''), '') == None

