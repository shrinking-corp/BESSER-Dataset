from python_code import LinhaCuidado

def test_LinhaCuidado___init__():
    assert LinhaCuidado.__init__(LinhaCuidado('\x00\x00', 0, mensagem15=set()), '', 0, mensagem15=set()) == None


from python_code import Medicamento
from python_code import Paciente

def test_Medicamento___init__():
    assert Medicamento.__init__(Medicamento('', '', '', False, 0, '', '', paciente9=Paciente()), '', '\x00', '', False, 0, '', '', paciente9=Paciente()) == None


from python_code import TipoMedicamento

def test_TipoMedicamento___init__():
    assert TipoMedicamento.__init__(TipoMedicamento(''), '') == None


from python_code import TipoSanguineo

def test_TipoSanguineo___init__():
    assert TipoSanguineo.__init__(TipoSanguineo('', paciente22=set()), '', paciente22=set()) == None

