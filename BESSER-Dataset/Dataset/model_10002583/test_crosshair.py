from python_code import Cache
from python_code import RAM

def test_Cache___init__():
    assert Cache.__init__(Cache('', ramProxy10=RAM()), '', ramProxy10=RAM()) == None


from python_code import Carro

def test_Carro___init__():
    assert Carro.__init__(Carro(0.0), 0.0) == None


from python_code import Program

def test_Program___init__():
    assert Program.__init__(Program('', instructions5=set(), processor8=set()), '', instructions5=set(), processor8=set()) == None

