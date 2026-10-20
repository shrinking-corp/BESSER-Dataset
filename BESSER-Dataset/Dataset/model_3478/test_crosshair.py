from python_code import feature_AttributeComparisonExpression
from python_code import feature_AttributeOperand

def test_feature_AttributeComparisonExpression___init__():
    assert feature_AttributeComparisonExpression.__init__(feature_AttributeComparisonExpression('', feature_AttributeComparisonExpression=feature_AttributeOperand(), feature_AttributeComparisonExpression36=feature_AttributeOperand()), '', feature_AttributeComparisonExpression=feature_AttributeOperand(), feature_AttributeComparisonExpression36=feature_AttributeOperand()) == None


from python_code import feature_AttributeValueLiteral

def test_feature_AttributeValueLiteral___init__():
    assert feature_AttributeValueLiteral.__init__(feature_AttributeValueLiteral(''), '') == None


from python_code import feature_EnumDomain

def test_feature_EnumDomain___init__():
    assert feature_EnumDomain.__init__(feature_EnumDomain(''), '') == None


from python_code import feature_Identifiable

def test_feature_Identifiable___init__():
    assert feature_Identifiable.__init__(feature_Identifiable(''), '') == None


from python_code import feature_ContinuousDomain
from python_code import feature_Interval

def test_feature_Interval___init__():
    assert feature_Interval.__init__(feature_Interval(0, 0, feature_Interval=feature_ContinuousDomain()), 0, 0, feature_Interval=feature_ContinuousDomain()) == None

