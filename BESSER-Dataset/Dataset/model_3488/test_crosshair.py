from python_code import model_ExistsContextualExpression
from python_code import model_Expression

def test_model_ExistsContextualExpression___init__():
    assert model_ExistsContextualExpression.__init__(model_ExistsContextualExpression('', model_ExistsContextualExpression=model_Expression()), '', model_ExistsContextualExpression=model_Expression()) == None


from python_code import model_Expression
from python_code import model_ForAllContextualExpression

def test_model_ForAllContextualExpression___init__():
    assert model_ForAllContextualExpression.__init__(model_ForAllContextualExpression('', model_ForAllContextualExpression=model_Expression()), '', model_ForAllContextualExpression=model_Expression()) == None


from python_code import model_PrimaryExpression

def test_model_PrimaryExpression___init__():
    assert model_PrimaryExpression.__init__(model_PrimaryExpression(''), '') == None

