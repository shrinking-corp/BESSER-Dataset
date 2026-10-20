from python_code import ApuestaEquipoGanador

def test_ApuestaEquipoGanador___init__():
    assert ApuestaEquipoGanador.__init__(ApuestaEquipoGanador(''), '') == None


from python_code import ApuestaMarcadorEspecifico

def test_ApuestaMarcadorEspecifico___init__():
    assert ApuestaMarcadorEspecifico.__init__(ApuestaMarcadorEspecifico('\x00\x00', '', 0, 0), '', '', 0, 0) == None

