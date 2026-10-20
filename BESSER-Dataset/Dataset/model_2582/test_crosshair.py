from python_code import vql_BoolValue
from python_code import vql_XBooleanLiteral

def test_vql_BoolValue___init__():
    assert vql_BoolValue.__init__(vql_BoolValue(vql_BoolValue=vql_XBooleanLiteral()), vql_BoolValue=vql_XBooleanLiteral()) == None

def test_vql_BoolValue_toString():
    assert vql_BoolValue.toString(vql_BoolValue(vql_BoolValue=vql_XBooleanLiteral())) == None


from python_code import vql_CheckConstraint
from python_code import vql_XExpression

def test_vql_CheckConstraint___init__():
    assert vql_CheckConstraint.__init__(vql_CheckConstraint(vql_CheckConstraint=vql_XExpression()), vql_CheckConstraint=vql_XExpression()) == None

def test_vql_CheckConstraint_toString():
    assert vql_CheckConstraint.toString(vql_CheckConstraint(vql_CheckConstraint=vql_XExpression())) == None


from python_code import vql_ComputationValue

def test_vql_ComputationValue___init__():
    assert vql_ComputationValue.__init__(vql_ComputationValue()) == None

def test_vql_ComputationValue_toString():
    assert vql_ComputationValue.toString(vql_ComputationValue()) == None


from python_code import vql_EClassifierConstraint

def test_vql_EClassifierConstraint___init__():
    assert vql_EClassifierConstraint.__init__(vql_EClassifierConstraint()) == None

def test_vql_EClassifierConstraint_toString():
    assert vql_EClassifierConstraint.toString(vql_EClassifierConstraint()) == None


from python_code import vql_EEnum
from python_code import vql_EEnumLiteral
from python_code import vql_EnumValue

def test_vql_EnumValue___init__():
    assert vql_EnumValue.__init__(vql_EnumValue(vql_EnumValue=vql_EEnum(), vql_EnumValue12=vql_EEnumLiteral()), vql_EnumValue=vql_EEnum(), vql_EnumValue12=vql_EEnumLiteral()) == None

def test_vql_EnumValue_toString():
    assert vql_EnumValue.toString(vql_EnumValue(vql_EnumValue=vql_EEnum(), vql_EnumValue12=vql_EEnumLiteral())) == None


from python_code import vql_Expression

def test_vql_Expression___init__():
    assert vql_Expression.__init__(vql_Expression()) == None

def test_vql_Expression_toString():
    assert vql_Expression.toString(vql_Expression()) == None


from python_code import vql_FunctionEvaluationValue
from python_code import vql_XExpression

def test_vql_FunctionEvaluationValue___init__():
    assert vql_FunctionEvaluationValue.__init__(vql_FunctionEvaluationValue(vql_FunctionEvaluationValue=vql_XExpression()), vql_FunctionEvaluationValue=vql_XExpression()) == None

def test_vql_FunctionEvaluationValue_toString():
    assert vql_FunctionEvaluationValue.toString(vql_FunctionEvaluationValue(vql_FunctionEvaluationValue=vql_XExpression())) == None


from python_code import vql_JavaType
from python_code import vql_JvmDeclaredType

def test_vql_JavaType___init__():
    assert vql_JavaType.__init__(vql_JavaType(vql_JavaType=vql_JvmDeclaredType()), vql_JavaType=vql_JvmDeclaredType()) == None

def test_vql_JavaType_toString():
    assert vql_JavaType.toString(vql_JavaType(vql_JavaType=vql_JvmDeclaredType())) == None


from python_code import vql_LiteralValueReference

def test_vql_LiteralValueReference___init__():
    assert vql_LiteralValueReference.__init__(vql_LiteralValueReference()) == None

def test_vql_LiteralValueReference_toString():
    assert vql_LiteralValueReference.toString(vql_LiteralValueReference()) == None


from python_code import vql_LocalVariable

def test_vql_LocalVariable___init__():
    assert vql_LocalVariable.__init__(vql_LocalVariable()) == None

def test_vql_LocalVariable_toString():
    assert vql_LocalVariable.toString(vql_LocalVariable()) == None


from python_code import vql_NumberValue
from python_code import vql_XNumberLiteral

def test_vql_NumberValue___init__():
    assert vql_NumberValue.__init__(vql_NumberValue(True, vql_NumberValue=vql_XNumberLiteral()), False, vql_NumberValue=vql_XNumberLiteral()) == None

def test_vql_NumberValue_toString():
    assert vql_NumberValue.toString(vql_NumberValue(False, vql_NumberValue=vql_XNumberLiteral())) == None


from python_code import vql_Parameter

def test_vql_Parameter___init__():
    assert vql_Parameter.__init__(vql_Parameter(''), '') == None

def test_vql_Parameter_toString():
    assert vql_Parameter.toString(vql_Parameter('')) == None


from python_code import vql_RelationType

def test_vql_RelationType___init__():
    assert vql_RelationType.__init__(vql_RelationType()) == None

def test_vql_RelationType_toString():
    assert vql_RelationType.toString(vql_RelationType()) == None


from python_code import vql_StringValue

def test_vql_StringValue___init__():
    assert vql_StringValue.__init__(vql_StringValue(''), '') == None

def test_vql_StringValue_toString():
    assert vql_StringValue.toString(vql_StringValue('')) == None


from python_code import vql_TypeCheckConstraint

def test_vql_TypeCheckConstraint___init__():
    assert vql_TypeCheckConstraint.__init__(vql_TypeCheckConstraint()) == None

def test_vql_TypeCheckConstraint_toString():
    assert vql_TypeCheckConstraint.toString(vql_TypeCheckConstraint()) == None

