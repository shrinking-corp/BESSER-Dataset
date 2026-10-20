from python_code import dot_Assignment

def test_dot_Assignment___init__():
    assert dot_Assignment.__init__(dot_Assignment('', '\x00'), '\x00\x00', '') == None


from python_code import dot_Identifiable

def test_dot_Identifiable___init__():
    assert dot_Identifiable.__init__(dot_Identifiable(''), '') == None


from python_code import dot_Settings

def test_dot_Settings___init__():
    assert dot_Settings.__init__(dot_Settings(''), '') == None


from python_code import dot_AttributedItem
from python_code import dot_StringToStringMapEntry

def test_dot_StringToStringMapEntry___init__():
    assert dot_StringToStringMapEntry.__init__(dot_StringToStringMapEntry('', '\x00', dot_StringToStringMapEntry=dot_AttributedItem()), '\x00\x00', '', dot_StringToStringMapEntry=dot_AttributedItem()) == None

