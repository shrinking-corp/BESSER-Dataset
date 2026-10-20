from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount(0, 0, 0, 0.0, 0.0, False), 0, 0, 0, 0.0, 0.0, False) == None

