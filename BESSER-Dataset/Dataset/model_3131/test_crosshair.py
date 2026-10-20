from python_code import class_ClassModel
from python_code import class_NamedElt

def test_class_NamedElt___init__():
    assert class_NamedElt.__init__(class_NamedElt('', class_NamedElt=class_ClassModel()), '', class_NamedElt=class_ClassModel()) == None

