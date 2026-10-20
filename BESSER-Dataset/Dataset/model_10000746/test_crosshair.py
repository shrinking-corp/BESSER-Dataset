from python_code import Clasificacion

def test_Clasificacion___init__():
    assert Clasificacion.__init__(Clasificacion('', '', '', '', '', '', '', '', '', '', liga27=set()), '\x00', '', '', '', '', '', '', '', '', '', liga27=set()) == None


from python_code import Estadio

def test_Estadio___init__():
    assert Estadio.__init__(Estadio('', '', '', '', '', '', '', partido5=set()), '', '', '', '', '', '', '', partido5=set()) == None


from python_code import Persona

def test_Persona___init__():
    assert Persona.__init__(Persona('', '', '', '', '', '', entrenador20=set(), arbitro16=set(), jugador18=set()), '', '', '', '', '\x00', '', entrenador20=set(), arbitro16=set(), jugador18=set()) == None


from python_code import TipoDeEvento

def test_TipoDeEvento___init__():
    assert TipoDeEvento.__init__(TipoDeEvento('\x00\x00', '', evento14=set()), '', '', evento14=set()) == None

