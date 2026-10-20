from python_code import ActionsProv_AcceptEventAction

def test_ActionsProv_AcceptEventAction___init__():
    assert ActionsProv_AcceptEventAction.__init__(ActionsProv_AcceptEventAction(False, ActionsProv_AcceptEventAction=set()), False, ActionsProv_AcceptEventAction=set()) == None


from python_code import ActionsProv_CallAction

def test_ActionsProv_CallAction___init__():
    assert ActionsProv_CallAction.__init__(ActionsProv_CallAction(False, ActionsProv_CallAction=set()), False, ActionsProv_CallAction=set()) == None


from python_code import ActionsProv_InputPin
from python_code import ActionsProv_LinkEndCreationData

def test_ActionsProv_LinkEndCreationData___init__():
    assert ActionsProv_LinkEndCreationData.__init__(ActionsProv_LinkEndCreationData(True, ActionsProv_LinkEndCreationData=ActionsProv_InputPin()), False, ActionsProv_LinkEndCreationData=ActionsProv_InputPin()) == None


from python_code import ActionsProv_InputPin
from python_code import ActionsProv_LinkEndDestructionData

def test_ActionsProv_LinkEndDestructionData___init__():
    assert ActionsProv_LinkEndDestructionData.__init__(ActionsProv_LinkEndDestructionData(True, ActionsProv_LinkEndDestructionData=ActionsProv_InputPin()), False, ActionsProv_LinkEndDestructionData=ActionsProv_InputPin()) == None


from python_code import ActionsProv_OpaqueAction

def test_ActionsProv_OpaqueAction___init__():
    assert ActionsProv_OpaqueAction.__init__(ActionsProv_OpaqueAction('', '', ActionsProv_OpaqueAction=set(), ActionsProv_OpaqueAction6=set()), '', '', ActionsProv_OpaqueAction=set(), ActionsProv_OpaqueAction6=set()) == None


from python_code import ActionsProv_InputPin
from python_code import ActionsProv_ReclassifyObjectAction

def test_ActionsProv_ReclassifyObjectAction___init__():
    assert ActionsProv_ReclassifyObjectAction.__init__(ActionsProv_ReclassifyObjectAction(True, ActionsProv_ReclassifyObjectAction=ActionsProv_InputPin()), False, ActionsProv_ReclassifyObjectAction=ActionsProv_InputPin()) == None


from python_code import ActionsProv_InputPin
from python_code import ActionsProv_OutputPin
from python_code import ActionsProv_ReduceAction

def test_ActionsProv_ReduceAction___init__():
    assert ActionsProv_ReduceAction.__init__(ActionsProv_ReduceAction(True, ActionsProv_ReduceAction=ActionsProv_OutputPin(), ActionsProv_ReduceAction112=ActionsProv_InputPin()), False, ActionsProv_ReduceAction=ActionsProv_OutputPin(), ActionsProv_ReduceAction112=ActionsProv_InputPin()) == None

