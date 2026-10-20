from python_code import datatypes_ComplexType

def test_datatypes_ComplexType___init__():
    assert datatypes_ComplexType.__init__(datatypes_ComplexType()) == None

def test_datatypes_ComplexType_getLabel():
    assert datatypes_ComplexType.getLabel(datatypes_ComplexType()) == None


from python_code import datatypes_RosIDLReference

def test_datatypes_RosIDLReference___init__():
    assert datatypes_RosIDLReference.__init__(datatypes_RosIDLReference('', '\x00'), '\x00\x00', '') == None

