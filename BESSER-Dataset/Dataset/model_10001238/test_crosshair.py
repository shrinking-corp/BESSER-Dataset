from python_code import account_SavingsAccount

def test_account_SavingsAccount___init__():
    assert account_SavingsAccount.__init__(account_SavingsAccount(0.0), 0.0) == None


from python_code import transaction_ExternalAccount

def test_transaction_ExternalAccount___init__():
    assert transaction_ExternalAccount.__init__(transaction_ExternalAccount('', '', '', transferTransaction3=set()), '', '', '', transferTransaction3=set()) == None


from python_code import transaction_Payee

def test_transaction_Payee___init__():
    assert transaction_Payee.__init__(transaction_Payee('', '', '', '', '', '', '', '', '', '', paybillsTransaction5=set()), '\x00', '', '', '', '', '', '', '', '', '', paybillsTransaction5=set()) == None

