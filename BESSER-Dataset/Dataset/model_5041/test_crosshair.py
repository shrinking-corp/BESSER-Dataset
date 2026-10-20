from python_code import bank_Account
from python_code import bank_Bank

def test_bank_Account___init__():
    assert bank_Account.__init__(bank_Account('', '', '', 0, bank_Account=bank_Bank(), bank_Account14=set()), '', '', '', 0, bank_Account=bank_Bank(), bank_Account14=set()) == None


from python_code import bank_EMail

def test_bank_EMail___init__():
    assert bank_EMail.__init__(bank_EMail(''), '') == None


from python_code import bank_MobilePhone

def test_bank_MobilePhone___init__():
    assert bank_MobilePhone.__init__(bank_MobilePhone('', '\x00'), '\x00\x00', '') == None


import datetime as _ch_datetime
from python_code import bank_Customer
from python_code import bank_OnlineSession

def test_bank_OnlineSession___init__():
    assert bank_OnlineSession.__init__(bank_OnlineSession('', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), bank_OnlineSession=bank_Customer()), '\x00', _ch_datetime.date(1, 1, 3), _ch_datetime.date(1, 1, 1), bank_OnlineSession=bank_Customer()) == None


from python_code import bank_Party

def test_bank_Party___init__():
    assert bank_Party.__init__(bank_Party('', bank_Party=set()), '', bank_Party=set()) == None


from python_code import bank_Phone

def test_bank_Phone___init__():
    assert bank_Phone.__init__(bank_Phone(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import bank_Bank
from python_code import bank_CustomerAccount
from python_code import bank_Product

def test_bank_Product___init__():
    assert bank_Product.__init__(bank_Product('', '\x00', bank_Product=bank_Bank(), bank_Product35=bank_CustomerAccount()), '\x00\x00', '', bank_Product=bank_Bank(), bank_Product35=bank_CustomerAccount()) == None


from python_code import bank_Device
from python_code import bank_Merchant
from python_code import bank_Token

def test_bank_Token___init__():
    assert bank_Token.__init__(bank_Token('', bank_Token=bank_Device(), bank_Token38=bank_Merchant()), '', bank_Token=bank_Device(), bank_Token38=bank_Merchant()) == None


from python_code import bank_WebAddress

def test_bank_WebAddress___init__():
    assert bank_WebAddress.__init__(bank_WebAddress(''), '') == None

