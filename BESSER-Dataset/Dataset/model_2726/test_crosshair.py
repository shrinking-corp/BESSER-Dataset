from python_code import direction_A
from python_code import direction_C

def test_direction_A___init__():
    assert direction_A.__init__(direction_A('', direction_A=direction_C()), '', direction_A=direction_C()) == None

