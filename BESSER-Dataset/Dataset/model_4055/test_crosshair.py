from python_code import smalluml_NamedElement

def test_smalluml_NamedElement___init__():
    assert smalluml_NamedElement.__init__(smalluml_NamedElement(''), '') == None


from python_code import smalluml_Association
from python_code import smalluml_Class
from python_code import smalluml_Heritage
from python_code import smalluml_Role

def test_smalluml_Role___init__():
    assert smalluml_Role.__init__(smalluml_Role(0, 0, smalluml_Role=smalluml_Association(), smalluml_Role12=smalluml_Association(), smalluml_Role14=smalluml_Heritage(), smalluml_Role17=smalluml_Heritage(), smalluml_Role19=smalluml_Class()), 0, 0, smalluml_Role=smalluml_Association(), smalluml_Role12=smalluml_Association(), smalluml_Role14=smalluml_Heritage(), smalluml_Role17=smalluml_Heritage(), smalluml_Role19=smalluml_Class()) == None

