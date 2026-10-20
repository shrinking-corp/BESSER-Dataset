from python_code import core_COREInterface
from python_code import core_COREModel
from python_code import core_COREModelElement

def test_core_COREModelElement___init__():
    assert core_COREModelElement.__init__(core_COREModelElement('', '\x00', core_COREModelElement37=core_COREInterface(), core_COREModelElement40=core_COREInterface(), core_COREModelElement=core_COREModel()), '\x00\x00', '', core_COREModelElement37=core_COREInterface(), core_COREModelElement40=core_COREInterface(), core_COREModelElement=core_COREModel()) == None


from python_code import core_CORENamedElement

def test_core_CORENamedElement___init__():
    assert core_CORENamedElement.__init__(core_CORENamedElement(''), '') == None


from python_code import core_LayoutElement
from python_code import core_LayoutMap

def test_core_LayoutElement___init__():
    assert core_LayoutElement.__init__(core_LayoutElement(0.0, 0.0, core_LayoutElement=core_LayoutMap()), 0.0, 0.0, core_LayoutElement=core_LayoutMap()) == None

