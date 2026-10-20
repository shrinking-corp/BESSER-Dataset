from python_code import university_Book
from python_code import university_Library

def test_university_Book___init__():
    assert university_Book.__init__(university_Book('', '\x00', university_Book=university_Library()), '\x00\x00', '', university_Book=university_Library()) == None


from python_code import university_NamedElement

def test_university_NamedElement___init__():
    assert university_NamedElement.__init__(university_NamedElement(''), '') == None


from python_code import university_PrimitiveType

def test_university_PrimitiveType___init__():
    assert university_PrimitiveType.__init__(university_PrimitiveType('', 0, 0.0, '', '', 0.0, '', '', '', '', '', '\x00', '', '', '', False, ''), '', 0, 0.0, '', '', 0.0, '', '', '', '', '', '', '', '', '', True, '') == None

