from python_code import transformation_BooleanLiteral

def test_transformation_BooleanLiteral___init__():
    assert transformation_BooleanLiteral.__init__(transformation_BooleanLiteral(True), False) == None


from python_code import transformation_ClassMapping
from python_code import transformation_ContentMapping
from python_code import transformation_EClass

def test_transformation_ClassMapping___init__():
    assert transformation_ClassMapping.__init__(transformation_ClassMapping(True, transformation_ClassMapping=transformation_EClass(), transformation_ClassMapping14=transformation_EClass(), transformation_ClassMapping17=transformation_ContentMapping()), False, transformation_ClassMapping=transformation_EClass(), transformation_ClassMapping14=transformation_EClass(), transformation_ClassMapping17=transformation_ContentMapping()) == None


from python_code import transformation_ExplicitMetamodel

def test_transformation_ExplicitMetamodel___init__():
    assert transformation_ExplicitMetamodel.__init__(transformation_ExplicitMetamodel(''), '') == None


from python_code import transformation_ExtentMetamodel
from python_code import transformation_SourceMetamodel

def test_transformation_ExtentMetamodel___init__():
    assert transformation_ExtentMetamodel.__init__(transformation_ExtentMetamodel(True, transformation_ExtentMetamodel=transformation_SourceMetamodel()), False, transformation_ExtentMetamodel=transformation_SourceMetamodel()) == None


from python_code import transformation_ETypedElement
from python_code import transformation_Expression
from python_code import transformation_FeatureAccess

def test_transformation_FeatureAccess___init__():
    assert transformation_FeatureAccess.__init__(transformation_FeatureAccess(False, False, transformation_FeatureAccess=transformation_Expression(), transformation_FeatureAccess67=transformation_ETypedElement()), False, False, transformation_FeatureAccess=transformation_Expression(), transformation_FeatureAccess67=transformation_ETypedElement()) == None


from python_code import transformation_IntegerLiteral

def test_transformation_IntegerLiteral___init__():
    assert transformation_IntegerLiteral.__init__(transformation_IntegerLiteral(0), 0) == None


from python_code import transformation_RealLiteral

def test_transformation_RealLiteral___init__():
    assert transformation_RealLiteral.__init__(transformation_RealLiteral(0.0), 0.0) == None


from python_code import transformation_StringLiteral

def test_transformation_StringLiteral___init__():
    assert transformation_StringLiteral.__init__(transformation_StringLiteral(''), '') == None


from python_code import transformation_Transformation

def test_transformation_Transformation___init__():
    assert transformation_Transformation.__init__(transformation_Transformation('', transformation_Transformation=set(), transformation_Transformation2=set()), '', transformation_Transformation=set(), transformation_Transformation2=set()) == None


from python_code import transformation_Lambda
from python_code import transformation_VariableDefinition
from python_code import transformation_VariableInitialization
from python_code import transformation_VariableUse

def test_transformation_VariableDefinition___init__():
    assert transformation_VariableDefinition.__init__(transformation_VariableDefinition('', transformation_VariableDefinition78=transformation_Lambda(), transformation_VariableDefinition87=transformation_VariableUse(), transformation_VariableDefinition=transformation_VariableInitialization()), '', transformation_VariableDefinition78=transformation_Lambda(), transformation_VariableDefinition87=transformation_VariableUse(), transformation_VariableDefinition=transformation_VariableInitialization()) == None

