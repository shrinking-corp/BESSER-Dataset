from python_code import Entrenador

def test_Entrenador___init__():
    assert Entrenador.__init__(Entrenador('', 0), '', 0) == None


from python_code import Personas

def test_Personas___init__():
    assert Personas.__init__(Personas('', '\x00'), '\x00\x00', '') == None

