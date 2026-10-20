from python_code import swml_Page

def test_swml_Page___init__():
    assert swml_Page.__init__(swml_Page(''), '') == None


from python_code import swml_Link
from python_code import swml_Parameter

def test_swml_Parameter___init__():
    assert swml_Parameter.__init__(swml_Parameter('', swml_Parameter=swml_Link()), '', swml_Parameter=swml_Link()) == None


from python_code import swml_ContentModel
from python_code import swml_HypertextModel
from python_code import swml_WebApplication

def test_swml_WebApplication___init__():
    assert swml_WebApplication.__init__(swml_WebApplication('', swml_WebApplication=swml_ContentModel(), swml_WebApplication2=swml_HypertextModel()), '', swml_WebApplication=swml_ContentModel(), swml_WebApplication2=swml_HypertextModel()) == None

