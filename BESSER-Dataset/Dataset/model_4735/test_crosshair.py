from python_code import swml_DynamicPage
from python_code import swml_Icon

def test_swml_Icon___init__():
    assert swml_Icon.__init__(swml_Icon('', swml_Icon=swml_DynamicPage()), '', swml_Icon=swml_DynamicPage()) == None


from python_code import swml_Link
from python_code import swml_StaticPage

def test_swml_Link___init__():
    assert swml_Link.__init__(swml_Link('', swml_Link=swml_StaticPage()), '', swml_Link=swml_StaticPage()) == None


from python_code import swml_StaticPage
from python_code import swml_WebApplication

def test_swml_WebApplication___init__():
    assert swml_WebApplication.__init__(swml_WebApplication('', swml_WebApplication=set(), swml_WebApplication2=swml_StaticPage()), '', swml_WebApplication=set(), swml_WebApplication2=swml_StaticPage()) == None


from python_code import swml_WebPage

def test_swml_WebPage___init__():
    assert swml_WebPage.__init__(swml_WebPage('', '\x00'), '\x00\x00', '') == None

