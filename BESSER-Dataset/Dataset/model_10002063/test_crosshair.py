from python_code import Exame
from python_code import float

def test_Exame___init__():
    assert Exame.__init__(Exame(0, '', float(), '\x00\x00'), 0, '', float(), '') == None

