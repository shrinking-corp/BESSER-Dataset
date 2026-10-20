from python_code import dsml_DContainment

def test_dsml_DContainment___init__():
    assert dsml_DContainment.__init__(dsml_DContainment(True), False) == None


from python_code import dsml_DGraphElement

def test_dsml_DGraphElement___init__():
    assert dsml_DGraphElement.__init__(dsml_DGraphElement(''), '') == None


from python_code import dsml_DModelElementBridge
from python_code import dsml_DSemanticBridge

def test_dsml_DModelElementBridge___init__():
    assert dsml_DModelElementBridge.__init__(dsml_DModelElementBridge('', '\x00', dsml_DModelElementBridge=dsml_DSemanticBridge()), '\x00\x00', '', dsml_DModelElementBridge=dsml_DSemanticBridge()) == None


from python_code import dsml_DReference

def test_dsml_DReference___init__():
    assert dsml_DReference.__init__(dsml_DReference(True), False) == None

