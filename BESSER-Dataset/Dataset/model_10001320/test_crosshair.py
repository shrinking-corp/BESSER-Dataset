from python_code import Especialidade

def test_Especialidade___init__():
    assert Especialidade.__init__(Especialidade(0, '\x00', agenda3=set()), 0, '', agenda3=set()) == None


from python_code import Agenda
from python_code import Funcionario

def test_Funcionario___init__():
    assert Funcionario.__init__(Funcionario(0, '', '', '', 0, agenda1=Agenda()), 0, '', '', '', 0, agenda1=Agenda()) == None

