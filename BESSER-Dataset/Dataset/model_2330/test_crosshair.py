from python_code import Actions_BasicActions_CallAction

def test_Actions_BasicActions_CallAction___init__():
    assert Actions_BasicActions_CallAction.__init__(Actions_BasicActions_CallAction(False, Actions_BasicActions_CallAction=set()), False, Actions_BasicActions_CallAction=set()) == None


from python_code import Actions_BasicActions_OpaqueAction
from python_code import Actions_StructuredActions_ActionInputPin

def test_Actions_BasicActions_OpaqueAction___init__():
    assert Actions_BasicActions_OpaqueAction.__init__(Actions_BasicActions_OpaqueAction('', '', Actions_BasicActions_OpaqueAction=set(), Actions_BasicActions_OpaqueAction8=set(), Action=Actions_StructuredActions_ActionInputPin()), '', '', Actions_BasicActions_OpaqueAction=set(), Actions_BasicActions_OpaqueAction8=set(), Action=Actions_StructuredActions_ActionInputPin()) == None


from python_code import Actions_CompleteActions_AcceptEventAction
from python_code import Actions_StructuredActions_ActionInputPin

def test_Actions_CompleteActions_AcceptEventAction___init__():
    assert Actions_CompleteActions_AcceptEventAction.__init__(Actions_CompleteActions_AcceptEventAction(False, Actions_CompleteActions_AcceptEventAction104=set(), Actions_CompleteActions_AcceptEventAction=set(), Action=Actions_StructuredActions_ActionInputPin()), False, Actions_CompleteActions_AcceptEventAction104=set(), Actions_CompleteActions_AcceptEventAction=set(), Action=Actions_StructuredActions_ActionInputPin()) == None


from python_code import Actions_CompleteActions_ReclassifyObjectAction
from python_code import Actions_StructuredActions_ActionInputPin
from python_code import InputPin

def test_Actions_CompleteActions_ReclassifyObjectAction___init__():
    assert Actions_CompleteActions_ReclassifyObjectAction.__init__(Actions_CompleteActions_ReclassifyObjectAction(False, Actions_CompleteActions_ReclassifyObjectAction=InputPin(), Actions_CompleteActions_ReclassifyObjectAction116=set(), Actions_CompleteActions_ReclassifyObjectAction119=set(), Action=Actions_StructuredActions_ActionInputPin()), False, Actions_CompleteActions_ReclassifyObjectAction=InputPin(), Actions_CompleteActions_ReclassifyObjectAction116=set(), Actions_CompleteActions_ReclassifyObjectAction119=set(), Action=Actions_StructuredActions_ActionInputPin()) == None


from python_code import Actions_CompleteActions_ReduceAction
from python_code import Actions_StructuredActions_ActionInputPin
from python_code import Behavior
from python_code import InputPin
from python_code import OutputPin

def test_Actions_CompleteActions_ReduceAction___init__():
    assert Actions_CompleteActions_ReduceAction.__init__(Actions_CompleteActions_ReduceAction(False, Actions_CompleteActions_ReduceAction=OutputPin(), Actions_CompleteActions_ReduceAction156=InputPin(), Actions_CompleteActions_ReduceAction159=Behavior(), Action=Actions_StructuredActions_ActionInputPin()), False, Actions_CompleteActions_ReduceAction=OutputPin(), Actions_CompleteActions_ReduceAction156=InputPin(), Actions_CompleteActions_ReduceAction159=Behavior(), Action=Actions_StructuredActions_ActionInputPin()) == None


from python_code import Actions_IntermediateActions_LinkAction
from python_code import Actions_IntermediateActions_LinkEndCreationData
from python_code import InputPin

def test_Actions_IntermediateActions_LinkEndCreationData___init__():
    assert Actions_IntermediateActions_LinkEndCreationData.__init__(Actions_IntermediateActions_LinkEndCreationData(False, Actions_IntermediateActions_LinkEndCreationData=InputPin(), LinkEndData=Actions_IntermediateActions_LinkAction()), False, Actions_IntermediateActions_LinkEndCreationData=InputPin(), LinkEndData=Actions_IntermediateActions_LinkAction()) == None


from python_code import Actions_IntermediateActions_LinkAction
from python_code import Actions_IntermediateActions_LinkEndDestructionData
from python_code import InputPin

def test_Actions_IntermediateActions_LinkEndDestructionData___init__():
    assert Actions_IntermediateActions_LinkEndDestructionData.__init__(Actions_IntermediateActions_LinkEndDestructionData(False, Actions_IntermediateActions_LinkEndDestructionData=InputPin(), LinkEndData=Actions_IntermediateActions_LinkAction()), False, Actions_IntermediateActions_LinkEndDestructionData=InputPin(), LinkEndData=Actions_IntermediateActions_LinkAction()) == None

