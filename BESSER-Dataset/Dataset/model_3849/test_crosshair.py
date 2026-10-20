from python_code import model_Comparison
from python_code import model_ComparisonOperator

def test_model_Comparison___init__():
    assert model_Comparison.__init__(model_Comparison('', '\x00', model_Comparison=model_ComparisonOperator()), '\x00\x00', '', model_Comparison=model_ComparisonOperator()) == None

