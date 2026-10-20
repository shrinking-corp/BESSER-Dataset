from python_code import relational_RelationalEntity

def test_relational_RelationalEntity___init__():
    assert relational_RelationalEntity.__init__(relational_RelationalEntity('', '\x00'), '\x00\x00', '') == None

