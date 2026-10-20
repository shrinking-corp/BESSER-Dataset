from python_code import statemachine_ConditionalState

def test_statemachine_ConditionalState___init__():
    assert statemachine_ConditionalState.__init__(statemachine_ConditionalState(False, '', statemachine_ConditionalState=set()), False, '', statemachine_ConditionalState=set()) == None


from python_code import statemachine_FieldCondition

def test_statemachine_FieldCondition___init__():
    assert statemachine_FieldCondition.__init__(statemachine_FieldCondition(''), '') == None


from python_code import statemachine_Named

def test_statemachine_Named___init__():
    assert statemachine_Named.__init__(statemachine_Named(''), '') == None


from python_code import statemachine_State

def test_statemachine_State___init__():
    assert statemachine_State.__init__(statemachine_State(''), '') == None


from python_code import statemachine_Statemachine

def test_statemachine_Statemachine___init__():
    assert statemachine_Statemachine.__init__(statemachine_Statemachine('\x00\x00', '', statemachine_Statemachine=set()), '', '', statemachine_Statemachine=set()) == None

