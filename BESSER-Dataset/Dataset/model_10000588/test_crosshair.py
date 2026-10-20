from python_code import Model_Queue

def test_Model_Queue___init__():
    assert Model_Queue.__init__(Model_Queue(''), '') == None


from python_code import Model_Session

def test_Model_Session___init__():
    assert Model_Session.__init__(Model_Session('', 0, '\x00\x00'), '', 0, '') == None


from python_code import Model_Transaction
from python_code import Presenter

def test_Model_Transaction___init__():
    assert Model_Transaction.__init__(Model_Transaction('', Presenter('', '\x00\x00')), '', Presenter('', '')) == None


from python_code import Model_WithdrawTransaction

def test_Model_WithdrawTransaction___init__():
    assert Model_WithdrawTransaction.__init__(Model_WithdrawTransaction(0), 0) == None


from python_code import Presenter

def test_Presenter___init__():
    assert Presenter.__init__(Presenter('', '\x00'), '\x00\x00', '') == None

