from python_code import minuml2_OpaqueExpression

def test_minuml2_OpaqueExpression___init__():
    assert minuml2_OpaqueExpression.__init__(minuml2_OpaqueExpression('', '\x00'), '\x00\x00', '') == None

