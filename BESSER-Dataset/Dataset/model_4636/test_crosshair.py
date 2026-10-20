from python_code import trnet_SomeOperand

def test_trnet_SomeOperand___init__():
    assert trnet_SomeOperand.__init__(trnet_SomeOperand(0), 0) == None


from python_code import trnet_SomeResult

def test_trnet_SomeResult___init__():
    assert trnet_SomeResult.__init__(trnet_SomeResult(0), 0) == None


from python_code import trnet_StringLiteral

def test_trnet_StringLiteral___init__():
    assert trnet_StringLiteral.__init__(trnet_StringLiteral(''), '') == None

