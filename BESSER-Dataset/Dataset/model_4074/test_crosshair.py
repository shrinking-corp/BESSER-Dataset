from python_code import SimpleUml_NamedElement

def test_SimpleUml_NamedElement___init__():
    assert SimpleUml_NamedElement.__init__(SimpleUml_NamedElement(''), '') == None


from python_code import SimpleUml_Class
from python_code import SimpleUml_Property

def test_SimpleUml_Property___init__():
    assert SimpleUml_Property.__init__(SimpleUml_Property('', False, SimpleUml_Property=SimpleUml_Class(), SimpleUml_Property5=SimpleUml_Class()), '', False, SimpleUml_Property=SimpleUml_Class(), SimpleUml_Property5=SimpleUml_Class()) == None

