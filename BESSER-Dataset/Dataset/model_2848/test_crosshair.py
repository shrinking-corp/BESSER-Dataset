from python_code import aDSL_BoolConstant

def test_aDSL_BoolConstant___init__():
    assert aDSL_BoolConstant.__init__(aDSL_BoolConstant(''), '') == None


from python_code import aDSL_Comparison
from python_code import aDSL_Expression

def test_aDSL_Comparison___init__():
    assert aDSL_Comparison.__init__(aDSL_Comparison('', aDSL_Comparison=aDSL_Expression(), aDSL_Comparison147=aDSL_Expression()), '', aDSL_Comparison=aDSL_Expression(), aDSL_Comparison147=aDSL_Expression()) == None


from python_code import aDSL_Equality
from python_code import aDSL_Expression

def test_aDSL_Equality___init__():
    assert aDSL_Equality.__init__(aDSL_Equality('', aDSL_Equality=aDSL_Expression(), aDSL_Equality142=aDSL_Expression()), '', aDSL_Equality=aDSL_Expression(), aDSL_Equality142=aDSL_Expression()) == None


from python_code import aDSL_IntConstant
from python_code import aDSL_IntegerNegative

def test_aDSL_IntegerNegative___init__():
    assert aDSL_IntegerNegative.__init__(aDSL_IntegerNegative(False, 0, aDSL_IntegerNegative=aDSL_IntConstant()), False, 0, aDSL_IntegerNegative=aDSL_IntConstant()) == None


from python_code import aDSL_Expression
from python_code import aDSL_MulOrDiv

def test_aDSL_MulOrDiv___init__():
    assert aDSL_MulOrDiv.__init__(aDSL_MulOrDiv('', aDSL_MulOrDiv=aDSL_Expression(), aDSL_MulOrDiv162=aDSL_Expression()), '', aDSL_MulOrDiv=aDSL_Expression(), aDSL_MulOrDiv162=aDSL_Expression()) == None


from python_code import aDSL_Program

def test_aDSL_Program___init__():
    assert aDSL_Program.__init__(aDSL_Program('', aDSL_Program=set(), aDSL_Program2=set()), '', aDSL_Program=set(), aDSL_Program2=set()) == None


from python_code import aDSL_Reference
from python_code import aDSL_VarDef

def test_aDSL_Reference___init__():
    assert aDSL_Reference.__init__(aDSL_Reference(False, aDSL_Reference=aDSL_VarDef(), aDSL_Reference172=set()), False, aDSL_Reference=aDSL_VarDef(), aDSL_Reference172=set()) == None


from python_code import aDSL_StringConstant

def test_aDSL_StringConstant___init__():
    assert aDSL_StringConstant.__init__(aDSL_StringConstant(''), '') == None


from python_code import aDSL_Body
from python_code import aDSL_TryCatchStat

def test_aDSL_TryCatchStat___init__():
    assert aDSL_TryCatchStat.__init__(aDSL_TryCatchStat('', aDSL_TryCatchStat=aDSL_Body(), aDSL_TryCatchStat85=aDSL_Body()), '', aDSL_TryCatchStat=aDSL_Body(), aDSL_TryCatchStat85=aDSL_Body()) == None

