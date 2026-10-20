from python_code import statechartexpressions_LiteralValue

def test_statechartexpressions_LiteralValue___init__():
    assert statechartexpressions_LiteralValue.__init__(statechartexpressions_LiteralValue(''), '') == None


from python_code import statechartexpressions_Procedure
from python_code import statechartexpressions_ProcedureCall

def test_statechartexpressions_Procedure___init__():
    assert statechartexpressions_Procedure.__init__(statechartexpressions_Procedure('', statechartexpressions_Procedure=statechartexpressions_ProcedureCall()), '', statechartexpressions_Procedure=statechartexpressions_ProcedureCall()) == None


from python_code import statechartexpressions_EventRaising
from python_code import statechartexpressions_SignalEvent

def test_statechartexpressions_SignalEvent___init__():
    assert statechartexpressions_SignalEvent.__init__(statechartexpressions_SignalEvent('', statechartexpressions_SignalEvent=statechartexpressions_EventRaising()), '', statechartexpressions_SignalEvent=statechartexpressions_EventRaising()) == None


from python_code import statechartexpressions_TimeConstant

def test_statechartexpressions_TimeConstant___init__():
    assert statechartexpressions_TimeConstant.__init__(statechartexpressions_TimeConstant(0, '\x00'), 0, '\x00') == None


from python_code import statechartexpressions_Variable
from python_code import statechartexpressions_VariableReference

def test_statechartexpressions_Variable___init__():
    assert statechartexpressions_Variable.__init__(statechartexpressions_Variable('', statechartexpressions_Variable=statechartexpressions_VariableReference()), '', statechartexpressions_Variable=statechartexpressions_VariableReference()) == None


from python_code import statechartexpressions_ConditionalExpression
from python_code import statechartexpressions_VariableAssignment
from python_code import statechartexpressions_VariableReference

def test_statechartexpressions_VariableAssignment___init__():
    assert statechartexpressions_VariableAssignment.__init__(statechartexpressions_VariableAssignment('', statechartexpressions_VariableAssignment=statechartexpressions_VariableReference(), statechartexpressions_VariableAssignment10=statechartexpressions_ConditionalExpression()), '', statechartexpressions_VariableAssignment=statechartexpressions_VariableReference(), statechartexpressions_VariableAssignment10=statechartexpressions_ConditionalExpression()) == None

