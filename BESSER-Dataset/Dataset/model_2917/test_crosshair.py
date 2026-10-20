from python_code import persistence_AssociationWithContainment

def test_persistence_AssociationWithContainment___init__():
    assert persistence_AssociationWithContainment.__init__(persistence_AssociationWithContainment(True), False) == None


from python_code import persistence_AssociationWithoutContainment

def test_persistence_AssociationWithoutContainment___init__():
    assert persistence_AssociationWithoutContainment.__init__(persistence_AssociationWithoutContainment('', False), '', False) == None


from python_code import persistence_DataType
from python_code import persistence_DataTypeAttribute

def test_persistence_DataTypeAttribute___init__():
    assert persistence_DataTypeAttribute.__init__(persistence_DataTypeAttribute(False, False, False, persistence_DataTypeAttribute=persistence_DataType()), False, False, False, persistence_DataTypeAttribute=persistence_DataType()) == None


from python_code import persistence_DateAttribute

def test_persistence_DateAttribute___init__():
    assert persistence_DateAttribute.__init__(persistence_DateAttribute('', '\x00'), '\x00\x00', '') == None


from python_code import persistence_DatePathElement

def test_persistence_DatePathElement___init__():
    assert persistence_DatePathElement.__init__(persistence_DatePathElement(''), '') == None


from python_code import persistence_EncapsulatedFeature

def test_persistence_EncapsulatedFeature___init__():
    assert persistence_EncapsulatedFeature.__init__(persistence_EncapsulatedFeature('', '', '\x00\x00'), '', '', '') == None


from python_code import persistence_EntityAttribute

def test_persistence_EntityAttribute___init__():
    assert persistence_EntityAttribute.__init__(persistence_EntityAttribute(False, False, '', '', ''), True, False, '', '', '') == None

