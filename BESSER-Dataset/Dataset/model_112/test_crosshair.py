from python_code import javasimplified_BooleanLiteral

def test_javasimplified_BooleanLiteral___init__():
    assert javasimplified_BooleanLiteral.__init__(javasimplified_BooleanLiteral(True), False) == None


from python_code import javasimplified_ImportDeclaration
from python_code import javasimplified_NamedElement

def test_javasimplified_NamedElement___init__():
    assert javasimplified_NamedElement.__init__(javasimplified_NamedElement('', javasimplified_NamedElement=javasimplified_ImportDeclaration()), '', javasimplified_NamedElement=javasimplified_ImportDeclaration()) == None


from python_code import javasimplified_NumberLiteral

def test_javasimplified_NumberLiteral___init__():
    assert javasimplified_NumberLiteral.__init__(javasimplified_NumberLiteral(''), '') == None


from python_code import javasimplified_StringLiteral

def test_javasimplified_StringLiteral___init__():
    assert javasimplified_StringLiteral.__init__(javasimplified_StringLiteral(''), '') == None

