from python_code import arduinoDSL_Board
from python_code import arduinoDSL_NodeDefinition

def test_arduinoDSL_Board___init__():
    assert arduinoDSL_Board.__init__(arduinoDSL_Board('', arduinoDSL_Board=arduinoDSL_NodeDefinition()), '', arduinoDSL_Board=arduinoDSL_NodeDefinition()) == None


from python_code import arduinoDSL_BooleanLiteral

def test_arduinoDSL_BooleanLiteral___init__():
    assert arduinoDSL_BooleanLiteral.__init__(arduinoDSL_BooleanLiteral(True), False) == None


from python_code import arduinoDSL_Attribute
from python_code import arduinoDSL_Node
from python_code import arduinoDSL_NodeDefinition

def test_arduinoDSL_Node___init__():
    assert arduinoDSL_Node.__init__(arduinoDSL_Node('', arduinoDSL_Node=arduinoDSL_Attribute(), arduinoDSL_Node26=arduinoDSL_NodeDefinition(), arduinoDSL_Node28=set()), '', arduinoDSL_Node=arduinoDSL_Attribute(), arduinoDSL_Node26=arduinoDSL_NodeDefinition(), arduinoDSL_Node28=set()) == None


from python_code import arduinoDSL_NumberLiteral

def test_arduinoDSL_NumberLiteral___init__():
    assert arduinoDSL_NumberLiteral.__init__(arduinoDSL_NumberLiteral('', 0), '', 0) == None


from python_code import arduinoDSL_Map
from python_code import arduinoDSL_Range

def test_arduinoDSL_Range___init__():
    assert arduinoDSL_Range.__init__(arduinoDSL_Range(0.0, 0.0, arduinoDSL_Range=arduinoDSL_Map(), arduinoDSL_Range42=arduinoDSL_Map()), 0.0, 0.0, arduinoDSL_Range=arduinoDSL_Map(), arduinoDSL_Range42=arduinoDSL_Map()) == None


from python_code import arduinoDSL_BooleanExpression
from python_code import arduinoDSL_Rule
from python_code import arduinoDSL_RuleBody

def test_arduinoDSL_Rule___init__():
    assert arduinoDSL_Rule.__init__(arduinoDSL_Rule('', arduinoDSL_Rule=arduinoDSL_BooleanExpression(), arduinoDSL_Rule3=arduinoDSL_RuleBody()), '', arduinoDSL_Rule=arduinoDSL_BooleanExpression(), arduinoDSL_Rule3=arduinoDSL_RuleBody()) == None


from python_code import arduinoDSL_State

def test_arduinoDSL_State___init__():
    assert arduinoDSL_State.__init__(arduinoDSL_State(''), '') == None

