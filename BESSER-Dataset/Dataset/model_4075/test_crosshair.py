from python_code import SimpleUML_NamedElement

def test_SimpleUML_NamedElement___init__():
    assert SimpleUML_NamedElement.__init__(SimpleUML_NamedElement(''), '') == None


from python_code import SimpleUML_Class
from python_code import SimpleUML_Property

def test_SimpleUML_Property___init__():
    assert SimpleUML_Property.__init__(SimpleUML_Property('', False, SimpleUML_Property5=SimpleUML_Class(), SimpleUML_Property=SimpleUML_Class()), '', False, SimpleUML_Property5=SimpleUML_Class(), SimpleUML_Property=SimpleUML_Class()) == None

