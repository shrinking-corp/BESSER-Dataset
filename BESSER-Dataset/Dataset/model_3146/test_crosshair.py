from python_code import XPath_IntegerExp

def test_XPath_IntegerExp___init__():
    assert XPath_IntegerExp.__init__(XPath_IntegerExp(''), '') == None


from python_code import XPath_LocatedElement

def test_XPath_LocatedElement___init__():
    assert XPath_LocatedElement.__init__(XPath_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import XPath_NamedElement

def test_XPath_NamedElement___init__():
    assert XPath_NamedElement.__init__(XPath_NamedElement(''), '') == None


from python_code import XPath_PathExpression

def test_XPath_PathExpression___init__():
    assert XPath_PathExpression.__init__(XPath_PathExpression('', XPath_PathExpression=set()), '', XPath_PathExpression=set()) == None


from python_code import XPath_StringExp

def test_XPath_StringExp___init__():
    assert XPath_StringExp.__init__(XPath_StringExp(''), '') == None

