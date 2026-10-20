from python_code import UML_Element

def test_UML_Element___init__():
    assert UML_Element.__init__(UML_Element('', '\x00'), '\x00\x00', '') == None


from python_code import UML_LiteralUnlimitedNatural
from python_code import UML_TypedElement

def test_UML_LiteralUnlimitedNatural___init__():
    assert UML_LiteralUnlimitedNatural.__init__(UML_LiteralUnlimitedNatural(0, UML_LiteralUnlimitedNatural=UML_TypedElement()), 0, UML_LiteralUnlimitedNatural=UML_TypedElement()) == None


from python_code import UML_Operation
from python_code import UML_Parameter

def test_UML_Parameter___init__():
    assert UML_Parameter.__init__(UML_Parameter('', UML_Parameter=UML_Operation()), '', UML_Parameter=UML_Operation()) == None

