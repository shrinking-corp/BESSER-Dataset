from python_code import smalluml_Association
from python_code import smalluml_Cardinalities

def test_smalluml_Cardinalities___init__():
    assert smalluml_Cardinalities.__init__(smalluml_Cardinalities(0, 0, smalluml_Cardinalities=smalluml_Association()), 0, 0, smalluml_Cardinalities=smalluml_Association()) == None


from python_code import smalluml_ClassDiagram

def test_smalluml_ClassDiagram___init__():
    assert smalluml_ClassDiagram.__init__(smalluml_ClassDiagram('\x00', smalluml_ClassDiagram=set()), '', smalluml_ClassDiagram=set()) == None


from python_code import smalluml_Enumeration

def test_smalluml_Enumeration___init__():
    assert smalluml_Enumeration.__init__(smalluml_Enumeration('', '\x00'), '\x00\x00', '') == None

