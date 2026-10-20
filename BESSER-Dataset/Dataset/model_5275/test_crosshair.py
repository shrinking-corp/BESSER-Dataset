from python_code import B
from python_code import foo_A

def test_foo_A___init__():
    assert foo_A.__init__(foo_A('', foo_A=B()), '', foo_A=B()) == None

