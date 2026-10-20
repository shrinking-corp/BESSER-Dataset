from python_code import elements_Book
from python_code import elements_EObject

def test_elements_Book___init__():
    assert elements_Book.__init__(elements_Book('\x00\x00', '', '', '', elements_Book=elements_EObject()), '', '', '', '', elements_Book=elements_EObject()) == None

