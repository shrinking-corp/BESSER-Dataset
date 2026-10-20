from python_code import simpleuml_Enumeration
from python_code import simpleuml_EnumerationLiteral

def test_simpleuml_EnumerationLiteral___init__():
    assert simpleuml_EnumerationLiteral.__init__(simpleuml_EnumerationLiteral('', simpleuml_EnumerationLiteral=simpleuml_Enumeration()), '', simpleuml_EnumerationLiteral=simpleuml_Enumeration()) == None


from python_code import simpleuml_Model

def test_simpleuml_Model___init__():
    assert simpleuml_Model.__init__(simpleuml_Model()) == None

def test_simpleuml_Model_getCustomProperty():
    assert simpleuml_Model.getCustomProperty(simpleuml_Model(), '') == None


from python_code import simpleuml_ModelElement

def test_simpleuml_ModelElement___init__():
    assert simpleuml_ModelElement.__init__(simpleuml_ModelElement('\x00\x00', '', simpleuml_ModelElement=set()), '', '', simpleuml_ModelElement=set()) == None

