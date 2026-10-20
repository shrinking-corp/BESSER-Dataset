from python_code import ATM_Card

def test_ATM_Card___init__():
    assert ATM_Card.__init__(ATM_Card('', '\x00'), '\x00\x00', '') == None


from python_code import ATM_Card2

def test_ATM_Card2___init__():
    assert ATM_Card2.__init__(ATM_Card2('', '\x00'), '\x00\x00', '') == None


from python_code import Bank

def test_Bank___init__():
    assert Bank.__init__(Bank('', '\x00'), '\x00\x00', '') == None


from python_code import Bank2

def test_Bank2___init__():
    assert Bank2.__init__(Bank2('', '\x00'), '\x00\x00', '') == None


import datetime as _ch_datetime
from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('\x00\x00', _ch_datetime.date(1, 1, 1), '', '', ''), '', _ch_datetime.date(1, 1, 1), '', '', '') == None


import datetime as _ch_datetime
from python_code import Customer2

def test_Customer2___init__():
    assert Customer2.__init__(Customer2('\x00\x00', _ch_datetime.date(1, 1, 1), '', '', ''), '', _ch_datetime.date(1, 1, 1), '', '', '') == None


from python_code import Savings_Account

def test_Savings_Account___init__():
    assert Savings_Account.__init__(Savings_Account('', 0), '', 0) == None


from python_code import Savings_Account2

def test_Savings_Account2___init__():
    assert Savings_Account2.__init__(Savings_Account2('', 0), '', 0) == None


from python_code import TransferTransaction

def test_TransferTransaction___init__():
    assert TransferTransaction.__init__(TransferTransaction('', '\x00'), '\x00\x00', '') == None


from python_code import TransferTransaction2

def test_TransferTransaction2___init__():
    assert TransferTransaction2.__init__(TransferTransaction2('', '\x00'), '\x00\x00', '') == None

