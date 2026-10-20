from python_code import Selects_NamedElement

def test_Selects_NamedElement___init__():
    assert Selects_NamedElement.__init__(Selects_NamedElement(''), '') == None


from python_code import Selects_Join
from python_code import Selects_Operando

def test_Selects_Operando___init__():
    assert Selects_Operando.__init__(Selects_Operando('', '\x00', Selects_Operando=Selects_Join(), Selects_Operando15=Selects_Join()), '\x00\x00', '', Selects_Operando=Selects_Join(), Selects_Operando15=Selects_Join()) == None


from python_code import Selects_From
from python_code import Selects_Tabla

def test_Selects_Tabla___init__():
    assert Selects_Tabla.__init__(Selects_Tabla('', Selects_Tabla=Selects_From()), '', Selects_Tabla=Selects_From()) == None

