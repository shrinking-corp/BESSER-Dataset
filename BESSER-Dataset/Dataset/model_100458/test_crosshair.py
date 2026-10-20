from python_code import stext_Assignment
from python_code import stext_Expression
from python_code import stext_Variable

def test_stext_Assignment___init__():
    assert stext_Assignment.__init__(stext_Assignment('', stext_Assignment=stext_Variable(), stext_Assignment23=stext_Expression()), '', stext_Assignment=stext_Variable(), stext_Assignment23=stext_Expression()) == None


from python_code import stext_BoolLiteral

def test_stext_BoolLiteral___init__():
    assert stext_BoolLiteral.__init__(stext_BoolLiteral(True), False) == None


from python_code import stext_EventDefinition
from python_code import stext_EventDerivation

def test_stext_EventDefinition___init__():
    assert stext_EventDefinition.__init__(stext_EventDefinition('', '\x00', stext_EventDefinition=stext_EventDerivation()), '\x00\x00', '', stext_EventDefinition=stext_EventDerivation()) == None


from python_code import stext_HexLiteral

def test_stext_HexLiteral___init__():
    assert stext_HexLiteral.__init__(stext_HexLiteral(0), 0) == None


from python_code import stext_IntLiteral

def test_stext_IntLiteral___init__():
    assert stext_IntLiteral.__init__(stext_IntLiteral(0), 0) == None


from python_code import stext_InterfaceScope

def test_stext_InterfaceScope___init__():
    assert stext_InterfaceScope.__init__(stext_InterfaceScope(''), '') == None


from python_code import stext_Expression
from python_code import stext_LogicalRelationExpression

def test_stext_LogicalRelationExpression___init__():
    assert stext_LogicalRelationExpression.__init__(stext_LogicalRelationExpression('', stext_LogicalRelationExpression=stext_Expression(), stext_LogicalRelationExpression83=stext_Expression()), '', stext_LogicalRelationExpression=stext_Expression(), stext_LogicalRelationExpression83=stext_Expression()) == None


from python_code import stext_Expression
from python_code import stext_NumericalAddSubtractExpression

def test_stext_NumericalAddSubtractExpression___init__():
    assert stext_NumericalAddSubtractExpression.__init__(stext_NumericalAddSubtractExpression('', stext_NumericalAddSubtractExpression=stext_Expression(), stext_NumericalAddSubtractExpression93=stext_Expression()), '', stext_NumericalAddSubtractExpression=stext_Expression(), stext_NumericalAddSubtractExpression93=stext_Expression()) == None


from python_code import stext_Expression
from python_code import stext_NumericalMultiplyDivideExpression

def test_stext_NumericalMultiplyDivideExpression___init__():
    assert stext_NumericalMultiplyDivideExpression.__init__(stext_NumericalMultiplyDivideExpression('', stext_NumericalMultiplyDivideExpression=stext_Expression(), stext_NumericalMultiplyDivideExpression98=stext_Expression()), '', stext_NumericalMultiplyDivideExpression=stext_Expression(), stext_NumericalMultiplyDivideExpression98=stext_Expression()) == None


from python_code import stext_Expression
from python_code import stext_NumericalUnaryExpression

def test_stext_NumericalUnaryExpression___init__():
    assert stext_NumericalUnaryExpression.__init__(stext_NumericalUnaryExpression('', stext_NumericalUnaryExpression=stext_Expression()), '', stext_NumericalUnaryExpression=stext_Expression()) == None


from python_code import stext_Operation
from python_code import stext_OperationCall

def test_stext_Operation___init__():
    assert stext_Operation.__init__(stext_Operation('', '\x00', stext_Operation=stext_OperationCall()), '\x00\x00', '', stext_Operation=stext_OperationCall()) == None


from python_code import stext_ReactionPriority

def test_stext_ReactionPriority___init__():
    assert stext_ReactionPriority.__init__(stext_ReactionPriority(0), 0) == None


from python_code import stext_RealLiteral

def test_stext_RealLiteral___init__():
    assert stext_RealLiteral.__init__(stext_RealLiteral(0.0), 0.0) == None


from python_code import stext_Expression
from python_code import stext_ShiftExpression

def test_stext_ShiftExpression___init__():
    assert stext_ShiftExpression.__init__(stext_ShiftExpression('', stext_ShiftExpression=stext_Expression(), stext_ShiftExpression88=stext_Expression()), '', stext_ShiftExpression=stext_Expression(), stext_ShiftExpression88=stext_Expression()) == None


from python_code import stext_StatechartDefinition
from python_code import stext_StatechartRoot

def test_stext_StatechartDefinition___init__():
    assert stext_StatechartDefinition.__init__(stext_StatechartDefinition('', stext_StatechartDefinition=stext_StatechartRoot(), stext_StatechartDefinition5=set()), '', stext_StatechartDefinition=stext_StatechartRoot(), stext_StatechartDefinition5=set()) == None


from python_code import stext_TimeEventSpec

def test_stext_TimeEventSpec___init__():
    assert stext_TimeEventSpec.__init__(stext_TimeEventSpec('', 0, '\x00\x00'), '', 0, '') == None


from python_code import stext_Expression
from python_code import stext_VariableDefinition

def test_stext_VariableDefinition___init__():
    assert stext_VariableDefinition.__init__(stext_VariableDefinition(False, False, '\x00\x00', stext_VariableDefinition=stext_Expression()), False, False, '', stext_VariableDefinition=stext_Expression()) == None

