from python_code import Cirurgiao

def test_Cirurgiao___init__():
    assert Cirurgiao.__init__(Cirurgiao(0, '', '', consulta2=set()), 0, '', '', consulta2=set()) == None


from python_code import Cliente

def test_Cliente___init__():
    assert Cliente.__init__(Cliente(0, '', '', '', '', consulta1=set()), 0, '', '', '\x00', '', consulta1=set()) == None

