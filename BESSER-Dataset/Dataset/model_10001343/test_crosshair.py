from python_code import Funcionario

def test_Funcionario___init__():
    assert Funcionario.__init__(Funcionario(0), 0) == None


from python_code import Pessoa

def test_Pessoa___init__():
    assert Pessoa.__init__(Pessoa(0, '', 0), 0, '', 0) == None

