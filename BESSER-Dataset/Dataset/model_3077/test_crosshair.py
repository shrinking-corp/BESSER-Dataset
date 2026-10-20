from python_code import entities_BasicType

def test_entities_BasicType___init__():
    assert entities_BasicType.__init__(entities_BasicType(''), '') == None


from python_code import entities_BoolConstant

def test_entities_BoolConstant___init__():
    assert entities_BoolConstant.__init__(entities_BoolConstant(''), '') == None


from python_code import entities_IntConstant

def test_entities_IntConstant___init__():
    assert entities_IntConstant.__init__(entities_IntConstant(0), 0) == None


from python_code import entities_StringConstant

def test_entities_StringConstant___init__():
    assert entities_StringConstant.__init__(entities_StringConstant(''), '') == None

