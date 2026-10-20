from python_code import room_ActorContainerRef
from python_code import room_BindingEndPoint
from python_code import room_RefSAPoint
from python_code import room_SPPoint

def test_room_ActorContainerRef___init__():
    assert room_ActorContainerRef.__init__(room_ActorContainerRef('', room_ActorContainerRef155=room_RefSAPoint(), room_ActorContainerRef160=room_SPPoint(), room_ActorContainerRef=room_BindingEndPoint()), '', room_ActorContainerRef155=room_RefSAPoint(), room_ActorContainerRef160=room_SPPoint(), room_ActorContainerRef=room_BindingEndPoint()) == None


from python_code import room_BaseState
from python_code import room_RefinedState
from python_code import room_StateTerminal
from python_code import room_SubStateTrPointTerminal

def test_room_BaseState___init__():
    assert room_BaseState.__init__(room_BaseState('', room_BaseState=room_RefinedState(), room_BaseState196=room_StateTerminal(), room_BaseState203=room_SubStateTrPointTerminal()), '', room_BaseState=room_RefinedState(), room_BaseState196=room_StateTerminal(), room_BaseState203=room_SubStateTrPointTerminal()) == None


from python_code import room_ChoicePoint
from python_code import room_ChoicepointTerminal
from python_code import room_StateGraph

def test_room_ChoicePoint___init__():
    assert room_ChoicePoint.__init__(room_ChoicePoint('', room_ChoicePoint=room_StateGraph(), room_ChoicePoint205=room_ChoicepointTerminal()), '', room_ChoicePoint=room_StateGraph(), room_ChoicePoint205=room_ChoicepointTerminal()) == None


from python_code import room_InterfaceItem
from python_code import room_MessageFromIf
from python_code import room_ProtocolClass

def test_room_InterfaceItem___init__():
    assert room_InterfaceItem.__init__(room_InterfaceItem('', room_InterfaceItem215=room_MessageFromIf(), room_InterfaceItem=room_ProtocolClass()), '', room_InterfaceItem215=room_MessageFromIf(), room_InterfaceItem=room_ProtocolClass()) == None


from python_code import room_LogicalThread
from python_code import room_SubSystemClass

def test_room_LogicalThread___init__():
    assert room_LogicalThread.__init__(room_LogicalThread('\x00', room_LogicalThread=room_SubSystemClass(), room_LogicalThread139=set()), '', room_LogicalThread=room_SubSystemClass(), room_LogicalThread139=set()) == None


from python_code import room_RoomClass

def test_room_RoomClass___init__():
    assert room_RoomClass.__init__(room_RoomClass(''), '') == None


from python_code import room_StateGraph
from python_code import room_SubStateTrPointTerminal
from python_code import room_TrPoint
from python_code import room_TrPointTerminal

def test_room_TrPoint___init__():
    assert room_TrPoint.__init__(room_TrPoint('', room_TrPoint198=room_TrPointTerminal(), room_TrPoint200=room_SubStateTrPointTerminal(), room_TrPoint=room_StateGraph()), '', room_TrPoint198=room_TrPointTerminal(), room_TrPoint200=room_SubStateTrPointTerminal(), room_TrPoint=room_StateGraph()) == None


from python_code import room_TransitionPoint

def test_room_TransitionPoint___init__():
    assert room_TransitionPoint.__init__(room_TransitionPoint(True), False) == None

