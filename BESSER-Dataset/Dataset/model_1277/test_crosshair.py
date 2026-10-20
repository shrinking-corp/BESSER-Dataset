from python_code import essentialoclcs_BooleanLiteralExpCS

def test_essentialoclcs_BooleanLiteralExpCS___init__():
    assert essentialoclcs_BooleanLiteralExpCS.__init__(essentialoclcs_BooleanLiteralExpCS(''), '') == None


from python_code import essentialoclcs_MapLiteralExpCS
from python_code import essentialoclcs_MapTypeCS
from python_code import essentialoclcs_TypedRefCS

def test_essentialoclcs_MapTypeCS___init__():
    assert essentialoclcs_MapTypeCS.__init__(essentialoclcs_MapTypeCS('', essentialoclcs_MapTypeCS=essentialoclcs_MapLiteralExpCS(), essentialoclcs_MapTypeCS99=essentialoclcs_TypedRefCS(), essentialoclcs_MapTypeCS102=essentialoclcs_TypedRefCS()), '', essentialoclcs_MapTypeCS=essentialoclcs_MapLiteralExpCS(), essentialoclcs_MapTypeCS99=essentialoclcs_TypedRefCS(), essentialoclcs_MapTypeCS102=essentialoclcs_TypedRefCS()) == None


from python_code import essentialoclcs_NumberLiteralExpCS

def test_essentialoclcs_NumberLiteralExpCS___init__():
    assert essentialoclcs_NumberLiteralExpCS.__init__(essentialoclcs_NumberLiteralExpCS(''), '') == None


from python_code import essentialoclcs_SelfExpCS

def test_essentialoclcs_SelfExpCS___init__():
    assert essentialoclcs_SelfExpCS.__init__(essentialoclcs_SelfExpCS(''), '') == None


from python_code import essentialoclcs_ShadowExpCS
from python_code import essentialoclcs_TypeNameExpCS

def test_essentialoclcs_ShadowExpCS___init__():
    assert essentialoclcs_ShadowExpCS.__init__(essentialoclcs_ShadowExpCS('', essentialoclcs_ShadowExpCS=set(), essentialoclcs_ShadowExpCS131=essentialoclcs_TypeNameExpCS()), '', essentialoclcs_ShadowExpCS=set(), essentialoclcs_ShadowExpCS131=essentialoclcs_TypeNameExpCS()) == None


from python_code import essentialoclcs_StringLiteralExpCS

def test_essentialoclcs_StringLiteralExpCS___init__():
    assert essentialoclcs_StringLiteralExpCS.__init__(essentialoclcs_StringLiteralExpCS(''), '') == None

