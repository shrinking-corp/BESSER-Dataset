from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount(0.0, '\x00\x00'), 0.0, '') == None

