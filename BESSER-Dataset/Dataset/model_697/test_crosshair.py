from python_code import type_AnyType

def test_type_AnyType___init__():
    assert type_AnyType.__init__(type_AnyType('', '', '\x00\x00'), '', '', '') == None


from python_code import type_EDataType
from python_code import type_SimpleAnyType

def test_type_SimpleAnyType___init__():
    assert type_SimpleAnyType.__init__(type_SimpleAnyType('', '\x00', type_SimpleAnyType=type_EDataType()), '\x00\x00', '', type_SimpleAnyType=type_EDataType()) == None


from python_code import type_XMLTypeDocumentRoot

def test_type_XMLTypeDocumentRoot___init__():
    assert type_XMLTypeDocumentRoot.__init__(type_XMLTypeDocumentRoot('', '', '\x00', '', type_XMLTypeDocumentRoot=set(), type_XMLTypeDocumentRoot3=set(), type_XMLTypeDocumentRoot6=set()), '', '', '', '', type_XMLTypeDocumentRoot=set(), type_XMLTypeDocumentRoot3=set(), type_XMLTypeDocumentRoot6=set()) == None

