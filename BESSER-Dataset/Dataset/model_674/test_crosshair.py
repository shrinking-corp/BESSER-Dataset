from python_code import smalluml_NamedElement

def test_smalluml_NamedElement___init__():
    assert smalluml_NamedElement.__init__(smalluml_NamedElement(''), '') == None


from python_code import smalluml_Class
from python_code import smalluml_Property
from python_code import smalluml_Type

def test_smalluml_Property___init__():
    assert smalluml_Property.__init__(smalluml_Property(0, 0, smalluml_Property=smalluml_Class(), smalluml_Property12=smalluml_Type()), 0, 0, smalluml_Property=smalluml_Class(), smalluml_Property12=smalluml_Type()) == None


from python_code import smalluml_TypeBoolean

def test_smalluml_TypeBoolean___init__():
    assert smalluml_TypeBoolean.__init__(smalluml_TypeBoolean(''), '') == None


from python_code import smalluml_TypeInteger

def test_smalluml_TypeInteger___init__():
    assert smalluml_TypeInteger.__init__(smalluml_TypeInteger(''), '') == None


from python_code import smalluml_TypeReal

def test_smalluml_TypeReal___init__():
    assert smalluml_TypeReal.__init__(smalluml_TypeReal(''), '') == None


from python_code import smalluml_TypeString

def test_smalluml_TypeString___init__():
    assert smalluml_TypeString.__init__(smalluml_TypeString(''), '') == None


from python_code import smalluml_TypeUnlimitedNatural

def test_smalluml_TypeUnlimitedNatural___init__():
    assert smalluml_TypeUnlimitedNatural.__init__(smalluml_TypeUnlimitedNatural(''), '') == None

