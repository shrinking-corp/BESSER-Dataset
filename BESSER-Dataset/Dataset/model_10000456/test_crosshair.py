from python_code import Bank

def test_Bank___init__():
    assert Bank.__init__(Bank('', bankAccount0=set()), '', bankAccount0=set()) == None


from python_code import FixedAccount

def test_FixedAccount___init__():
    assert FixedAccount.__init__(FixedAccount(''), '') == None


from python_code import SavingsAccount

def test_SavingsAccount___init__():
    assert SavingsAccount.__init__(SavingsAccount(0.0, False), 0.0, False) == None

