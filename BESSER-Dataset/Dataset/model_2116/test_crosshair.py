from python_code import test_Basic

def test_test_Basic___init__():
    assert test_Basic.__init__(test_Basic('', '\x00'), '\x00\x00', '') == None


from python_code import test_ComplianceAssertion

def test_test_ComplianceAssertion___init__():
    assert test_ComplianceAssertion.__init__(test_ComplianceAssertion(''), '') == None


from python_code import test_HTTPStatusAssertion

def test_test_HTTPStatusAssertion___init__():
    assert test_HTTPStatusAssertion.__init__(test_HTTPStatusAssertion(''), '') == None


from python_code import test_HeaderAssertion

def test_test_HeaderAssertion___init__():
    assert test_HeaderAssertion.__init__(test_HeaderAssertion(''), '') == None


from python_code import test_HeaderEqualsAssertion

def test_test_HeaderEqualsAssertion___init__():
    assert test_HeaderEqualsAssertion.__init__(test_HeaderEqualsAssertion(''), '') == None


from python_code import test_NamedElement

def test_test_NamedElement___init__():
    assert test_NamedElement.__init__(test_NamedElement(''), '') == None


from python_code import test_OAuth2

def test_test_OAuth2___init__():
    assert test_OAuth2.__init__(test_OAuth2(''), '') == None


from python_code import test_Property
from python_code import test_PropertyTransfer

def test_test_Property___init__():
    assert test_Property.__init__(test_Property('', '\x00', test_Property=test_PropertyTransfer(), test_Property11=test_PropertyTransfer()), '\x00\x00', '', test_Property=test_PropertyTransfer(), test_Property11=test_PropertyTransfer()) == None


from python_code import test_ResponseMessageAssertion

def test_test_ResponseMessageAssertion___init__():
    assert test_ResponseMessageAssertion.__init__(test_ResponseMessageAssertion(''), '') == None


from python_code import test_SLAAssertion

def test_test_SLAAssertion___init__():
    assert test_SLAAssertion.__init__(test_SLAAssertion(''), '') == None


from python_code import test_TestSuite

def test_test_TestSuite___init__():
    assert test_TestSuite.__init__(test_TestSuite('\x00\x00', '', test_TestSuite=set()), '', '', test_TestSuite=set()) == None

