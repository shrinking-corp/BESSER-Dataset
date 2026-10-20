from python_code import simple_csp_DescribedElement

def test_simple_csp_DescribedElement___init__():
    assert simple_csp_DescribedElement.__init__(simple_csp_DescribedElement(''), '') == None


from python_code import simple_csp_IntegerDomain

def test_simple_csp_IntegerDomain___init__():
    assert simple_csp_IntegerDomain.__init__(simple_csp_IntegerDomain('', '\x00'), '\x00\x00', '') == None


from python_code import simple_csp_NamedElement

def test_simple_csp_NamedElement___init__():
    assert simple_csp_NamedElement.__init__(simple_csp_NamedElement(''), '') == None


from python_code import simple_csp_Domain
from python_code import simple_csp_TypedElement

def test_simple_csp_TypedElement___init__():
    assert simple_csp_TypedElement.__init__(simple_csp_TypedElement('', simple_csp_TypedElement=simple_csp_Domain()), '', simple_csp_TypedElement=simple_csp_Domain()) == None

