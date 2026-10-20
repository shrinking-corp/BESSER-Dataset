from python_code import Account
from python_code import Bank

def test_Account___init__():
    assert Account.__init__(Account('', '', '', '', '\x00', transaction2=set(), bank5=Bank(), customer7=set()), '', '', '', '', '', transaction2=set(), bank5=Bank(), customer7=set()) == None


from python_code import CheckTransaction

def test_CheckTransaction___init__():
    assert CheckTransaction.__init__(CheckTransaction(''), '') == None


from python_code import CoDTransaction

def test_CoDTransaction___init__():
    assert CoDTransaction.__init__(CoDTransaction('', '', '\x00\x00'), '', '', '') == None


from python_code import Bank
from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('\x00\x00', '', bank1=Bank(), account6=set()), '', '', bank1=Bank(), account6=set()) == None


from python_code import Bank
from python_code import Customer
from python_code import Transaction

def test_Transaction___init__():
    assert Transaction.__init__(Transaction('', Customer('', '', bank1=Bank(), account6=set()), '', '\x00', account3=set()), '', Customer('', '', bank1=Bank(), account6=set()), '', '', account3=set()) == None

