from python_code import Bank

def test_Bank___init__():
    assert Bank.__init__(Bank('', '', debit_Card1=set(), customer4=set(), aTM_INFO6=set()), '', '', debit_Card1=set(), customer4=set(), aTM_INFO6=set()) == None


from python_code import CheckBalance

def test_CheckBalance___init__():
    assert CheckBalance.__init__(CheckBalance(''), '') == None


from python_code import Current_Account

def test_Current_Account___init__():
    assert Current_Account.__init__(Current_Account('', '\x00'), '\x00\x00', '') == None


from python_code import Savings_Account

def test_Savings_Account___init__():
    assert Savings_Account.__init__(Savings_Account('', '\x00'), '\x00\x00', '') == None


from python_code import Transfer_Money

def test_Transfer_Money___init__():
    assert Transfer_Money.__init__(Transfer_Money(0, '\x00'), 0, '\x00') == None


from python_code import Withdraw_Transaction

def test_Withdraw_Transaction___init__():
    assert Withdraw_Transaction.__init__(Withdraw_Transaction(0), 0) == None

