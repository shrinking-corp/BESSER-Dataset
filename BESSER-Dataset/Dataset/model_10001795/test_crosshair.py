from python_code import Canino
from python_code import Int

def test_Canino___init__():
    assert Canino.__init__(Canino('', '', Int(), Int(), Int(), '\x00\x00'), '', '', Int(), Int(), Int(), '') == None


from python_code import Empresa

def test_Empresa___init__():
    assert Empresa.__init__(Empresa(''), '') == None

