from python_code import smalluml_ElementNomme

def test_smalluml_ElementNomme___init__():
    assert smalluml_ElementNomme.__init__(smalluml_ElementNomme(''), '') == None


from python_code import smalluml_ElementDiagramme
from python_code import smalluml_Enumeration

def test_smalluml_Enumeration___init__():
    assert smalluml_Enumeration.__init__(smalluml_Enumeration('', smalluml_Enumeration=smalluml_ElementDiagramme()), '', smalluml_Enumeration=smalluml_ElementDiagramme()) == None

