from python_code import typesystem_BooleanLiteral

def test_typesystem_BooleanLiteral___init__():
    assert typesystem_BooleanLiteral.__init__(typesystem_BooleanLiteral(True), False) == None


from python_code import typesystem_IntegerLiteral

def test_typesystem_IntegerLiteral___init__():
    assert typesystem_IntegerLiteral.__init__(typesystem_IntegerLiteral(''), '') == None


from python_code import typesystem_RealLiteral

def test_typesystem_RealLiteral___init__():
    assert typesystem_RealLiteral.__init__(typesystem_RealLiteral(0.0), 0.0) == None


from python_code import typesystem_StringLiteral

def test_typesystem_StringLiteral___init__():
    assert typesystem_StringLiteral.__init__(typesystem_StringLiteral(''), '') == None


from python_code import typesystem_TensorType

def test_typesystem_TensorType___init__():
    assert typesystem_TensorType.__init__(typesystem_TensorType(False, False), False, False) == None


from python_code import typesystem_UnitProduct

def test_typesystem_UnitProduct___init__():
    assert typesystem_UnitProduct.__init__(typesystem_UnitProduct(typesystem_UnitProduct=set()), typesystem_UnitProduct=set()) == None

def test_typesystem_UnitProduct_getFactor():
    assert typesystem_UnitProduct.getFactor(typesystem_UnitProduct(typesystem_UnitProduct=set()), 0) == None

