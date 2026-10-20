from python_code import SimpleUML_Class
from python_code import SimpleUML_Feature

def test_SimpleUML_Feature___init__():
    assert SimpleUML_Feature.__init__(SimpleUML_Feature(True, SimpleUML_Feature=SimpleUML_Class(), SimpleUML_Feature4=SimpleUML_Class()), False, SimpleUML_Feature=SimpleUML_Class(), SimpleUML_Feature4=SimpleUML_Class()) == None


from python_code import SimpleUML_NamedElement

def test_SimpleUML_NamedElement___init__():
    assert SimpleUML_NamedElement.__init__(SimpleUML_NamedElement(''), '') == None

