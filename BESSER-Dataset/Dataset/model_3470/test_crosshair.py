from python_code import featureModel_BinaryOperation
from python_code import featureModel_Expression

def test_featureModel_BinaryOperation___init__():
    assert featureModel_BinaryOperation.__init__(featureModel_BinaryOperation('', featureModel_BinaryOperation=featureModel_Expression(), featureModel_BinaryOperation12=featureModel_Expression()), '', featureModel_BinaryOperation=featureModel_Expression(), featureModel_BinaryOperation12=featureModel_Expression()) == None


from python_code import featureModel_Identifier

def test_featureModel_Identifier___init__():
    assert featureModel_Identifier.__init__(featureModel_Identifier('', featureModel_Identifier=set()), '', featureModel_Identifier=set()) == None


from python_code import featureModel_Number

def test_featureModel_Number___init__():
    assert featureModel_Number.__init__(featureModel_Number(0), 0) == None


from python_code import featureModel_Expression
from python_code import featureModel_UnaryOperation

def test_featureModel_UnaryOperation___init__():
    assert featureModel_UnaryOperation.__init__(featureModel_UnaryOperation('', featureModel_UnaryOperation=featureModel_Expression()), '', featureModel_UnaryOperation=featureModel_Expression()) == None

