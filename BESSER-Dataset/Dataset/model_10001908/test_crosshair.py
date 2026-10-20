from python_code import data_CustomerProfileRepository

def test_data_CustomerProfileRepository___init__():
    assert data_CustomerProfileRepository.__init__(data_CustomerProfileRepository(0, '\x00'), 0, '\x00') == None


from python_code import model_CheckingAccount

def test_model_CheckingAccount___init__():
    assert model_CheckingAccount.__init__(model_CheckingAccount(0.0, '\x00\x00'), 0.0, '') == None


from python_code import model_CreditAccount

def test_model_CreditAccount___init__():
    assert model_CreditAccount.__init__(model_CreditAccount(0.0, 0.0, '', ''), 0.0, 0.0, '', '') == None


from python_code import model_Loan

def test_model_Loan___init__():
    assert model_Loan.__init__(model_Loan(0.0, 0.0, '', ''), 0.0, 0.0, '', '') == None


from python_code import model_SavingsAccount

def test_model_SavingsAccount___init__():
    assert model_SavingsAccount.__init__(model_SavingsAccount(0.0, '\x00\x00'), 0.0, '') == None


from python_code import genmymodelreverse_java_util_Date
from python_code import model_Transaction

def test_model_Transaction___init__():
    assert model_Transaction.__init__(model_Transaction(genmymodelreverse_java_util_Date(), 0.0), genmymodelreverse_java_util_Date(), 0.0) == None

