from python_code import nosql_CollectionType

def test_nosql_CollectionType___init__():
    assert nosql_CollectionType.__init__(nosql_CollectionType('', '\x00'), '\x00\x00', '') == None


from python_code import nosql_MapType

def test_nosql_MapType___init__():
    assert nosql_MapType.__init__(nosql_MapType('', '\x00'), '\x00\x00', '') == None


from python_code import nosql_PrimitiveType

def test_nosql_PrimitiveType___init__():
    assert nosql_PrimitiveType.__init__(nosql_PrimitiveType(''), '') == None

