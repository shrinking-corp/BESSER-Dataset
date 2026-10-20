from python_code import linkinher_Named
from python_code import linkinher_X

def test_linkinher_Named___init__():
    assert linkinher_Named.__init__(linkinher_Named('', linkinher_Named=linkinher_X()), '', linkinher_Named=linkinher_X()) == None

