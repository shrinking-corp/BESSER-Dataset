from python_code import typedef_CSIDatatype

def test_typedef_CSIDatatype___init__():
    assert typedef_CSIDatatype.__init__(typedef_CSIDatatype('', False), '', False) == None


from python_code import typedef_Entity

def test_typedef_Entity___init__():
    assert typedef_Entity.__init__(typedef_Entity(0, typedef_Entity=set()), 0, typedef_Entity=set()) == None


from python_code import typedef_Exception

def test_typedef_Exception___init__():
    assert typedef_Exception.__init__(typedef_Exception(''), '') == None


from python_code import typedef_PrimitiveType

def test_typedef_PrimitiveType___init__():
    assert typedef_PrimitiveType.__init__(typedef_PrimitiveType('\x00\x00', False, typedef_PrimitiveType=set()), '', True, typedef_PrimitiveType=set()) == None

