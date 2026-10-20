from python_code import Animal

def test_Animal___init__():
    assert Animal.__init__(Animal('', '', '\x00\x00'), '', '', '') == None


from python_code import Cliente

def test_Cliente___init__():
    assert Cliente.__init__(Cliente('', '', '\x00\x00'), '', '', '') == None


from python_code import CoordenadaGPS

def test_CoordenadaGPS___init__():
    assert CoordenadaGPS.__init__(CoordenadaGPS('', '\x00'), '\x00\x00', '') == None


from python_code import Gato

def test_Gato___init__():
    assert Gato.__init__(Gato('', '\x00'), '\x00\x00', '') == None


from python_code import Perro

def test_Perro___init__():
    assert Perro.__init__(Perro(''), '') == None

