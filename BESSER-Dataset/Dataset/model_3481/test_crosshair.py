from python_code import feature_AttributeConstraint
from python_code import feature_AttributeOperand

def test_feature_AttributeConstraint___init__():
    assert feature_AttributeConstraint.__init__(feature_AttributeConstraint('', feature_AttributeConstraint=feature_AttributeOperand(), feature_AttributeConstraint18=feature_AttributeOperand()), '', feature_AttributeConstraint=feature_AttributeOperand(), feature_AttributeConstraint18=feature_AttributeOperand()) == None


from python_code import feature_AttributeValue

def test_feature_AttributeValue___init__():
    assert feature_AttributeValue.__init__(feature_AttributeValue('', 0), '', 0) == None


from python_code import feature_DiscreteDomain
from python_code import feature_DomainValue

def test_feature_DomainValue___init__():
    assert feature_DomainValue.__init__(feature_DomainValue(0, '\x00', feature_DomainValue=feature_DiscreteDomain()), 0, '\x00', feature_DomainValue=feature_DiscreteDomain()) == None


from python_code import feature_Identifiable

def test_feature_Identifiable___init__():
    assert feature_Identifiable.__init__(feature_Identifiable(''), '') == None


from python_code import feature_Interval
from python_code import feature_NumericalDomain

def test_feature_Interval___init__():
    assert feature_Interval.__init__(feature_Interval(0, 0, feature_Interval=feature_NumericalDomain()), 0, 0, feature_Interval=feature_NumericalDomain()) == None

