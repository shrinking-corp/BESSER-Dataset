from python_code import Funcion_rio

def test_Funcion_rio___init__():
    assert Funcion_rio.__init__(Funcion_rio('', '\x00'), '\x00\x00', '') == None


from python_code import M_dico

def test_M_dico___init__():
    assert M_dico.__init__(M_dico('', '', 0), '\x00', '', 0) == None

