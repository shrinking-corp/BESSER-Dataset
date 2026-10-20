from python_code import smalluml_BooleanV

def test_smalluml_BooleanV___init__():
    assert smalluml_BooleanV.__init__(smalluml_BooleanV(''), '') == None


from python_code import smalluml_Association
from python_code import smalluml_Cardinalite

def test_smalluml_Cardinalite___init__():
    assert smalluml_Cardinalite.__init__(smalluml_Cardinalite('', '\x00', smalluml_Cardinalite=smalluml_Association(), smalluml_Cardinalite17=smalluml_Association()), '\x00\x00', '', smalluml_Cardinalite=smalluml_Association(), smalluml_Cardinalite17=smalluml_Association()) == None


from python_code import smalluml_Enumeration

def test_smalluml_Enumeration___init__():
    assert smalluml_Enumeration.__init__(smalluml_Enumeration(''), '') == None


from python_code import smalluml_IntegerV

def test_smalluml_IntegerV___init__():
    assert smalluml_IntegerV.__init__(smalluml_IntegerV(''), '') == None


from python_code import smalluml_NamedElement

def test_smalluml_NamedElement___init__():
    assert smalluml_NamedElement.__init__(smalluml_NamedElement(''), '') == None


from python_code import smalluml_RealV

def test_smalluml_RealV___init__():
    assert smalluml_RealV.__init__(smalluml_RealV(''), '') == None


from python_code import smalluml_StringV

def test_smalluml_StringV___init__():
    assert smalluml_StringV.__init__(smalluml_StringV(''), '') == None

