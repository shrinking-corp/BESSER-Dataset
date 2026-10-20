from python_code import Reqtify_Attribute

def test_Reqtify_Attribute___init__():
    assert Reqtify_Attribute.__init__(Reqtify_Attribute(''), '') == None


from python_code import Reqtify_ElementWithIL

def test_Reqtify_ElementWithIL___init__():
    assert Reqtify_ElementWithIL.__init__(Reqtify_ElementWithIL('', '\x00'), '\x00\x00', '') == None


from python_code import Reqtify_TextElement

def test_Reqtify_TextElement___init__():
    assert Reqtify_TextElement.__init__(Reqtify_TextElement(''), '') == None


from python_code import Reqtify_TypedElement

def test_Reqtify_TypedElement___init__():
    assert Reqtify_TypedElement.__init__(Reqtify_TypedElement(''), '') == None

