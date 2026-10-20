from python_code import DispositivoBluetooth

def test_DispositivoBluetooth___init__():
    assert DispositivoBluetooth.__init__(DispositivoBluetooth('', '\x00'), '\x00\x00', '') == None


from python_code import Instruction

def test_Instruction___init__():
    assert Instruction.__init__(Instruction('', 0), '', 0) == None


from python_code import MedicaoBatimento
from python_code import Treino
from python_code import Usu_rio_Actor

def test_MedicaoBatimento___init__():
    assert MedicaoBatimento.__init__(MedicaoBatimento(Usu_rio_Actor(), 0, False, '', Treino('')), Usu_rio_Actor(), 0, False, '', Treino('')) == None


from python_code import Treino

def test_Treino___init__():
    assert Treino.__init__(Treino(''), '') == None


from python_code import TreinoMonitoramento

def test_TreinoMonitoramento___init__():
    assert TreinoMonitoramento.__init__(TreinoMonitoramento('', '\x00'), '\x00\x00', '') == None


from python_code import TutorStep

def test_TutorStep___init__():
    assert TutorStep.__init__(TutorStep('', 0), '', 0) == None


from python_code import Usuario

def test_Usuario___init__():
    assert Usuario.__init__(Usuario('', '', '', '', ''), '', '', '', '', '') == None

