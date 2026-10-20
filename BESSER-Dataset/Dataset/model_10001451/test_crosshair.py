from python_code import Cuadrado

def test_Cuadrado___init__():
    assert Cuadrado.__init__(Cuadrado(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import Figura

def test_Figura___init__():
    assert Figura.__init__(Figura(False, 0), False, 0) == None


from python_code import Cuadrado
from python_code import Figura
from python_code import Ventana

def test_Ventana___init__():
    assert Ventana.__init__(Ventana(Cuadrado(0, 0, ''), Cuadrado(0, 0, ''), Cuadrado(0, 0, ''), Figura(False, 0), 0, 0, ''), Cuadrado(0, 0, ''), Cuadrado(0, 0, ''), Cuadrado(0, 0, ''), Figura(True, 0), 0, 0, '') == None

