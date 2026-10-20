from python_code import swml_IndexPage

def test_swml_IndexPage___init__():
    assert swml_IndexPage.__init__(swml_IndexPage(0), 0) == None


from python_code import swml_HypertextLayer
from python_code import swml_Link
from python_code import swml_Page

def test_swml_Page___init__():
    assert swml_Page.__init__(swml_Page('', swml_Page=swml_HypertextLayer(), swml_Page7=swml_HypertextLayer(), swml_Page21=swml_Link(), swml_Page16=set()), '', swml_Page=swml_HypertextLayer(), swml_Page7=swml_HypertextLayer(), swml_Page21=swml_Link(), swml_Page16=set()) == None


from python_code import swml_ContentLayer
from python_code import swml_HypertextLayer
from python_code import swml_WebModel

def test_swml_WebModel___init__():
    assert swml_WebModel.__init__(swml_WebModel('', swml_WebModel=swml_HypertextLayer(), swml_WebModel2=swml_ContentLayer()), '', swml_WebModel=swml_HypertextLayer(), swml_WebModel2=swml_ContentLayer()) == None

