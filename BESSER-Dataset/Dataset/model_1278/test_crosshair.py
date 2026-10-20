from python_code import essentialoclcs_AbstractNameExpCS

def test_essentialoclcs_AbstractNameExpCS___init__():
    assert essentialoclcs_AbstractNameExpCS.__init__(essentialoclcs_AbstractNameExpCS()) == None

def test_essentialoclcs_AbstractNameExpCS_getNamedElement():
    assert essentialoclcs_AbstractNameExpCS.getNamedElement(essentialoclcs_AbstractNameExpCS()) == None

def test_essentialoclcs_AbstractNameExpCS_getNameExp():
    assert essentialoclcs_AbstractNameExpCS.getNameExp(essentialoclcs_AbstractNameExpCS()) == None

def test_essentialoclcs_AbstractNameExpCS_getPathName():
    assert essentialoclcs_AbstractNameExpCS.getPathName(essentialoclcs_AbstractNameExpCS()) == None


from python_code import essentialoclcs_BooleanLiteralExpCS

def test_essentialoclcs_BooleanLiteralExpCS___init__():
    assert essentialoclcs_BooleanLiteralExpCS.__init__(essentialoclcs_BooleanLiteralExpCS(''), '') == None


from python_code import essentialoclcs_CollectionLiteralExpCS
from python_code import essentialoclcs_CollectionTypeCS
from python_code import essentialoclcs_TypedRefCS

def test_essentialoclcs_CollectionTypeCS___init__():
    assert essentialoclcs_CollectionTypeCS.__init__(essentialoclcs_CollectionTypeCS('', essentialoclcs_CollectionTypeCS11=essentialoclcs_TypedRefCS(), essentialoclcs_CollectionTypeCS=essentialoclcs_CollectionLiteralExpCS()), '', essentialoclcs_CollectionTypeCS11=essentialoclcs_TypedRefCS(), essentialoclcs_CollectionTypeCS=essentialoclcs_CollectionLiteralExpCS()) == None


from python_code import essentialoclcs_ConstructorExpCS

def test_essentialoclcs_ConstructorExpCS___init__():
    assert essentialoclcs_ConstructorExpCS.__init__(essentialoclcs_ConstructorExpCS('', essentialoclcs_ConstructorExpCS=set()), '', essentialoclcs_ConstructorExpCS=set()) == None


from python_code import essentialoclcs_IndexExpCS

def test_essentialoclcs_IndexExpCS___init__():
    assert essentialoclcs_IndexExpCS.__init__(essentialoclcs_IndexExpCS(False, essentialoclcs_IndexExpCS=set(), essentialoclcs_IndexExpCS35=set()), False, essentialoclcs_IndexExpCS=set(), essentialoclcs_IndexExpCS35=set()) == None


from python_code import essentialoclcs_NameExpCS
from python_code import essentialoclcs_NamedExpCS
from python_code import essentialoclcs_PathNameCS

def test_essentialoclcs_NameExpCS___init__():
    assert essentialoclcs_NameExpCS.__init__(essentialoclcs_NameExpCS(True, essentialoclcs_NameExpCS=essentialoclcs_PathNameCS(), essentialoclcs_NameExpCS49=essentialoclcs_NamedExpCS()), False, essentialoclcs_NameExpCS=essentialoclcs_PathNameCS(), essentialoclcs_NameExpCS49=essentialoclcs_NamedExpCS()) == None


from python_code import essentialoclcs_ExpCS
from python_code import essentialoclcs_InvocationExpCS
from python_code import essentialoclcs_NavigatingArgCS
from python_code import essentialoclcs_TypedRefCS

def test_essentialoclcs_NavigatingArgCS___init__():
    assert essentialoclcs_NavigatingArgCS.__init__(essentialoclcs_NavigatingArgCS('', '\x00', NavigatingArgCS=essentialoclcs_InvocationExpCS(), argument=essentialoclcs_InvocationExpCS(), essentialoclcs_NavigatingArgCS=essentialoclcs_ExpCS(), essentialoclcs_NavigatingArgCS54=essentialoclcs_TypedRefCS(), essentialoclcs_NavigatingArgCS57=essentialoclcs_ExpCS()), '\x00\x00', '', NavigatingArgCS=essentialoclcs_InvocationExpCS(), argument=essentialoclcs_InvocationExpCS(), essentialoclcs_NavigatingArgCS=essentialoclcs_ExpCS(), essentialoclcs_NavigatingArgCS54=essentialoclcs_TypedRefCS(), essentialoclcs_NavigatingArgCS57=essentialoclcs_ExpCS()) == None


from python_code import essentialoclcs_NumberLiteralExpCS

def test_essentialoclcs_NumberLiteralExpCS___init__():
    assert essentialoclcs_NumberLiteralExpCS.__init__(essentialoclcs_NumberLiteralExpCS(''), '') == None


from python_code import essentialoclcs_SelfExpCS

def test_essentialoclcs_SelfExpCS___init__():
    assert essentialoclcs_SelfExpCS.__init__(essentialoclcs_SelfExpCS(''), '') == None


from python_code import essentialoclcs_StringLiteralExpCS

def test_essentialoclcs_StringLiteralExpCS___init__():
    assert essentialoclcs_StringLiteralExpCS.__init__(essentialoclcs_StringLiteralExpCS(''), '') == None

