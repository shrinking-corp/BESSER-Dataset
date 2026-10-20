from python_code import Pessoa

def test_Pessoa___init__():
    assert Pessoa.__init__(Pessoa('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None

