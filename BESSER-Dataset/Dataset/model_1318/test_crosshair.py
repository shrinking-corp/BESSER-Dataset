from python_code import stateMachine_Condition
from python_code import stateMachine_Transition

def test_stateMachine_Condition___init__():
    assert stateMachine_Condition.__init__(stateMachine_Condition('', stateMachine_Condition=stateMachine_Transition()), '', stateMachine_Condition=stateMachine_Transition()) == None


from python_code import stateMachine_Modifier

def test_stateMachine_Modifier___init__():
    assert stateMachine_Modifier.__init__(stateMachine_Modifier(''), '') == None


from python_code import stateMachine_DeclaredParameter
from python_code import stateMachine_VarName

def test_stateMachine_VarName___init__():
    assert stateMachine_VarName.__init__(stateMachine_VarName('', stateMachine_VarName=stateMachine_DeclaredParameter()), '', stateMachine_VarName=stateMachine_DeclaredParameter()) == None

