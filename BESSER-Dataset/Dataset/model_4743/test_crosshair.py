from python_code import swml_v2_IndexPage

def test_swml_v2_IndexPage___init__():
    assert swml_v2_IndexPage.__init__(swml_v2_IndexPage(0), 0) == None


from python_code import swml_v2_Link
from python_code import swml_v2_NavigationLayer
from python_code import swml_v2_Page

def test_swml_v2_Page___init__():
    assert swml_v2_Page.__init__(swml_v2_Page('', swml_v2_Page=swml_v2_NavigationLayer(), swml_v2_Page7=swml_v2_NavigationLayer(), swml_v2_Page21=swml_v2_Link(), swml_v2_Page16=set()), '', swml_v2_Page=swml_v2_NavigationLayer(), swml_v2_Page7=swml_v2_NavigationLayer(), swml_v2_Page21=swml_v2_Link(), swml_v2_Page16=set()) == None


from python_code import swml_v2_ContentLayer
from python_code import swml_v2_NavigationLayer
from python_code import swml_v2_WebModel

def test_swml_v2_WebModel___init__():
    assert swml_v2_WebModel.__init__(swml_v2_WebModel('', swml_v2_WebModel=swml_v2_NavigationLayer(), swml_v2_WebModel2=swml_v2_ContentLayer()), '', swml_v2_WebModel=swml_v2_NavigationLayer(), swml_v2_WebModel2=swml_v2_ContentLayer()) == None

