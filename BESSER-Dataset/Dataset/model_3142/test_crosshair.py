from python_code import smalluml_Cardinality
from python_code import smalluml_Relation

def test_smalluml_Cardinality___init__():
    assert smalluml_Cardinality.__init__(smalluml_Cardinality(0, 0, smalluml_Cardinality=smalluml_Relation()), 0, 0, smalluml_Cardinality=smalluml_Relation()) == None


from python_code import smalluml_Enumeration
from python_code import smalluml_EnumerationElement

def test_smalluml_EnumerationElement___init__():
    assert smalluml_EnumerationElement.__init__(smalluml_EnumerationElement('', smalluml_EnumerationElement=smalluml_Enumeration()), '', smalluml_EnumerationElement=smalluml_Enumeration()) == None


from python_code import smalluml_NamedElement

def test_smalluml_NamedElement___init__():
    assert smalluml_NamedElement.__init__(smalluml_NamedElement(''), '') == None

