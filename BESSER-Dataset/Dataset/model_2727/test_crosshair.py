from python_code import a_A

def test_a_A___init__():
    assert a_A.__init__(a_A('', '', a_A=set()), '', '', a_A=set()) == None

def test_a_A_foo():
    assert a_A.foo(a_A('', '', a_A=set()), '', 0) == None

