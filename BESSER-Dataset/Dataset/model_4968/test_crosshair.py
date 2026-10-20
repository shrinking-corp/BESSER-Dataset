from python_code import dcmddandroid_ClassElement

def test_dcmddandroid_ClassElement___init__():
    assert dcmddandroid_ClassElement.__init__(dcmddandroid_ClassElement(False, False), False, False) == None


from python_code import dcmddandroid_EVisibility

def test_dcmddandroid_EVisibility___init__():
    assert dcmddandroid_EVisibility.__init__(dcmddandroid_EVisibility(''), '') == None


from python_code import dcmddandroid_Enum
from python_code import dcmddandroid_EnumValue

def test_dcmddandroid_EnumValue___init__():
    assert dcmddandroid_EnumValue.__init__(dcmddandroid_EnumValue(0, dcmddandroid_EnumValue=dcmddandroid_Enum()), 0, dcmddandroid_EnumValue=dcmddandroid_Enum()) == None


from python_code import dcmddandroid_NamedElement

def test_dcmddandroid_NamedElement___init__():
    assert dcmddandroid_NamedElement.__init__(dcmddandroid_NamedElement(''), '') == None

