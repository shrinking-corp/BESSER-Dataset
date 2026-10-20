from python_code import fc_BooleanValue

def test_fc_BooleanValue___init__():
    assert fc_BooleanValue.__init__(fc_BooleanValue(True), False) == None


from python_code import fc_DoubleValue

def test_fc_DoubleValue___init__():
    assert fc_DoubleValue.__init__(fc_DoubleValue(0.0), 0.0) == None


from python_code import fc_IntegerValue

def test_fc_IntegerValue___init__():
    assert fc_IntegerValue.__init__(fc_IntegerValue(0), 0) == None


from python_code import fc_StringValue

def test_fc_StringValue___init__():
    assert fc_StringValue.__init__(fc_StringValue(''), '') == None

