from python_code import CRUD

def test_CRUD___init__():
    assert CRUD.__init__(CRUD('', '\x00'), '\x00\x00', '') == None

from python_code import Cofre

def test_Cofre___init__():
    assert Cofre.__init__(Cofre(0.0, 0.0), 0.0, 0.0) == None

from python_code import Conta_Conjunta

def test_Conta_Conjunta___init__():
    assert Conta_Conjunta.__init__(Conta_Conjunta(0), 0) == None

from python_code import Conta_Corrente

def test_Conta_Corrente___init__():
    assert Conta_Corrente.__init__(Conta_Corrente('', 0, 0.0, 0.0), '', 0, 0.0, 0.0) == None

from python_code import Conta_Normal

def test_Conta_Normal___init__():
    assert Conta_Normal.__init__(Conta_Normal(0), 0) == None

from python_code import Conta_Poupan_a

def test_Conta_Poupan_a___init__():
    assert Conta_Poupan_a.__init__(Conta_Poupan_a('', 0, 0.0), '', 0, 0.0) == None

from python_code import Deposito

def test_Deposito___init__():
    assert Deposito.__init__(Deposito(0.0, '\x00\x00'), 0.0, '') == None

from python_code import Emprestimo

def test_Emprestimo___init__():
    assert Emprestimo.__init__(Emprestimo(0.0), 0.0) == None

from python_code import FixedAccount

def test_FixedAccount___init__():
    assert FixedAccount.__init__(FixedAccount(''), '') == None

from python_code import SalvarConta

def test_SalvarConta___init__():
    assert SalvarConta.__init__(SalvarConta(0.0, False), 0.0, False) == None

from python_code import Transferencia

def test_Transferencia___init__():
    assert Transferencia.__init__(Transferencia('\x00', 0.0), '', 0.0) == None
