from python_code import iotdsl_BoolConstant

def test_iotdsl_BoolConstant___init__():
    assert iotdsl_BoolConstant.__init__(iotdsl_BoolConstant(''), '') == None


from python_code import iotdsl_Delay
from python_code import iotdsl_WithinExpression

def test_iotdsl_Delay___init__():
    assert iotdsl_Delay.__init__(iotdsl_Delay('', 0, iotdsl_Delay=iotdsl_WithinExpression()), '', 0, iotdsl_Delay=iotdsl_WithinExpression()) == None


from python_code import iotdsl_EnumLiteral
from python_code import iotdsl_Enumeration

def test_iotdsl_EnumLiteral___init__():
    assert iotdsl_EnumLiteral.__init__(iotdsl_EnumLiteral('', iotdsl_EnumLiteral=iotdsl_Enumeration()), '', iotdsl_EnumLiteral=iotdsl_Enumeration()) == None


from python_code import iotdsl_Device
from python_code import iotdsl_Feature

def test_iotdsl_Feature___init__():
    assert iotdsl_Feature.__init__(iotdsl_Feature('', iotdsl_Feature=iotdsl_Device()), '', iotdsl_Feature=iotdsl_Device()) == None


from python_code import iotdsl_IntConstant

def test_iotdsl_IntConstant___init__():
    assert iotdsl_IntConstant.__init__(iotdsl_IntConstant(0), 0) == None


from python_code import iotdsl_IotModel

def test_iotdsl_IotModel___init__():
    assert iotdsl_IotModel.__init__(iotdsl_IotModel('', iotdsl_IotModel=set(), iotdsl_IotModel2=set()), '', iotdsl_IotModel=set(), iotdsl_IotModel2=set()) == None


from python_code import iotdsl_Expression
from python_code import iotdsl_Rule

def test_iotdsl_Rule___init__():
    assert iotdsl_Rule.__init__(iotdsl_Rule('', iotdsl_Rule=iotdsl_Expression(), iotdsl_Rule23=set()), '', iotdsl_Rule=iotdsl_Expression(), iotdsl_Rule23=set()) == None


from python_code import iotdsl_StringConstant

def test_iotdsl_StringConstant___init__():
    assert iotdsl_StringConstant.__init__(iotdsl_StringConstant(''), '') == None

