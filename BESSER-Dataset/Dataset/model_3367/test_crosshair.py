from python_code import netModel_BooleanLiteral

def test_netModel_BooleanLiteral___init__():
    assert netModel_BooleanLiteral.__init__(netModel_BooleanLiteral(''), '') == None


from python_code import netModel_Client

def test_netModel_Client___init__():
    assert netModel_Client.__init__(netModel_Client('', netModel_Client=set()), '', netModel_Client=set()) == None


from python_code import netModel_EnumMember
from python_code import netModel_EnumTypeLiteral

def test_netModel_EnumMember___init__():
    assert netModel_EnumMember.__init__(netModel_EnumMember('', False, 0, netModel_EnumMember=netModel_EnumTypeLiteral()), '\x00', False, 0, netModel_EnumMember=netModel_EnumTypeLiteral()) == None


from python_code import netModel_GenericListType
from python_code import netModel_Type

def test_netModel_GenericListType___init__():
    assert netModel_GenericListType.__init__(netModel_GenericListType('', netModel_GenericListType=netModel_Type()), '', netModel_GenericListType=netModel_Type()) == None


from python_code import netModel_Header
from python_code import netModel_HeaderBlock

def test_netModel_Header___init__():
    assert netModel_Header.__init__(netModel_Header('', '\x00', netModel_Header=netModel_HeaderBlock()), '\x00\x00', '', netModel_Header=netModel_HeaderBlock()) == None


from python_code import netModel_ComplexTypeLiteral
from python_code import netModel_Member

def test_netModel_Member___init__():
    assert netModel_Member.__init__(netModel_Member('', netModel_Member=netModel_ComplexTypeLiteral()), '', netModel_Member=netModel_ComplexTypeLiteral()) == None


from python_code import netModel_Model

def test_netModel_Model___init__():
    assert netModel_Model.__init__(netModel_Model('\x00', netModel_Model=set()), '', netModel_Model=set()) == None


from python_code import netModel_NumericLiteral

def test_netModel_NumericLiteral___init__():
    assert netModel_NumericLiteral.__init__(netModel_NumericLiteral(''), '') == None


from python_code import netModel_StringLiteral

def test_netModel_StringLiteral___init__():
    assert netModel_StringLiteral.__init__(netModel_StringLiteral(''), '') == None


from python_code import netModel_UserType
from python_code import netModel_UserTypeDeclaration

def test_netModel_UserTypeDeclaration___init__():
    assert netModel_UserTypeDeclaration.__init__(netModel_UserTypeDeclaration('', False, netModel_UserTypeDeclaration=netModel_UserType()), '', False, netModel_UserTypeDeclaration=netModel_UserType()) == None

