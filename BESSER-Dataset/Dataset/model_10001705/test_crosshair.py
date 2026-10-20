from python_code import conta

def test_conta___init__():
    assert conta.__init__(conta(''), '') == None


from python_code import conta_Poupan_a

def test_conta_Poupan_a___init__():
    assert conta_Poupan_a.__init__(conta_Poupan_a(0.0, 0), 0.0, 0) == None


from python_code import conta_investimento

def test_conta_investimento___init__():
    assert conta_investimento.__init__(conta_investimento(0.0), 0.0) == None


from python_code import transacao_deposito

def test_transacao_deposito___init__():
    assert transacao_deposito.__init__(transacao_deposito(''), '') == None


from python_code import transacao_saque

def test_transacao_saque___init__():
    assert transacao_saque.__init__(transacao_saque(''), '') == None

