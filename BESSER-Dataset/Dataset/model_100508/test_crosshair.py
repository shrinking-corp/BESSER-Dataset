from python_code import requirement_AttributeLink

def test_requirement_AttributeLink___init__():
    assert requirement_AttributeLink.__init__(requirement_AttributeLink(''), '') == None


from python_code import requirement_AttributeConfiguration
from python_code import requirement_ConfiguratedAttribute
from python_code import requirement_DefaultAttributeValue

def test_requirement_ConfiguratedAttribute___init__():
    assert requirement_ConfiguratedAttribute.__init__(requirement_ConfiguratedAttribute('\x00\x00', '', requirement_ConfiguratedAttribute=requirement_AttributeConfiguration(), requirement_ConfiguratedAttribute19=requirement_DefaultAttributeValue(), requirement_ConfiguratedAttribute21=set()), '', '', requirement_ConfiguratedAttribute=requirement_AttributeConfiguration(), requirement_ConfiguratedAttribute19=requirement_DefaultAttributeValue(), requirement_ConfiguratedAttribute21=set()) == None


from python_code import requirement_CurrentRequirement

def test_requirement_CurrentRequirement___init__():
    assert requirement_CurrentRequirement.__init__(requirement_CurrentRequirement(True), False) == None


from python_code import requirement_IdentifiedElement

def test_requirement_IdentifiedElement___init__():
    assert requirement_IdentifiedElement.__init__(requirement_IdentifiedElement('', '\x00'), '\x00\x00', '') == None


from python_code import requirement_TextAttribute

def test_requirement_TextAttribute___init__():
    assert requirement_TextAttribute.__init__(requirement_TextAttribute(''), '') == None

