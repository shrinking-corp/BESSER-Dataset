from python_code import model_ConfigExpectedResultPair
from python_code import model_ExpectedResult

def test_model_ExpectedResult___init__():
    assert model_ExpectedResult.__init__(model_ExpectedResult('', '', '\x00\x00', model_ExpectedResult=model_ConfigExpectedResultPair()), '', '', '', model_ExpectedResult=model_ConfigExpectedResultPair()) == None


from python_code import model_Scenario

def test_model_Scenario___init__():
    assert model_Scenario.__init__(model_Scenario('', model_Scenario=set()), '', model_Scenario=set()) == None

