import datetime as _ch_datetime
from python_code import Profile

def test_Profile___init__():
    assert Profile.__init__(Profile('', '', '', _ch_datetime.date(1, 1, 1), '', '', '', '', '\x00', '', '', '', 0, ''), '', '', '', _ch_datetime.date(1, 1, 1), '', '', '', '', '', '', '\x00', '', 0, '') == None


from python_code import User

def test_User___init__():
    assert User.__init__(User('', '', '', '', ''), '', '', '', '', '') == None


from python_code import account_SavingsAccount

def test_account_SavingsAccount___init__():
    assert account_SavingsAccount.__init__(account_SavingsAccount(0.0), 0.0) == None


from python_code import transaction_ExternalAccount

def test_transaction_ExternalAccount___init__():
    assert transaction_ExternalAccount.__init__(transaction_ExternalAccount('', '', '\x00\x00'), '', '', '') == None


from python_code import transaction_Payee

def test_transaction_Payee___init__():
    assert transaction_Payee.__init__(transaction_Payee('', '', '\x00', '', '', '', '', '', '', ''), '', '', '\x00', '', '', '', '', '', '', '') == None

