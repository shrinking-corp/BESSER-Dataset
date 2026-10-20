from python_code import room_InterfaceItem
from python_code import room_MessageFromIf

def test_room_InterfaceItem___init__():
    assert room_InterfaceItem.__init__(room_InterfaceItem('', room_InterfaceItem=room_MessageFromIf()), '', room_InterfaceItem=room_MessageFromIf()) == None

def test_room_InterfaceItem_getGeneralProtocol():
    assert room_InterfaceItem.getGeneralProtocol(room_InterfaceItem('', room_InterfaceItem=room_MessageFromIf())) == None


from python_code import room_LogicalThread
from python_code import room_SubSystemClass

def test_room_LogicalThread___init__():
    assert room_LogicalThread.__init__(room_LogicalThread('\x00\x00', 0, room_LogicalThread=room_SubSystemClass(), room_LogicalThread199=set()), '', 0, room_LogicalThread=room_SubSystemClass(), room_LogicalThread199=set()) == None


from python_code import room_SimpleState

def test_room_SimpleState___init__():
    assert room_SimpleState.__init__(room_SimpleState(''), '') == None


from python_code import room_StateGraphItem

def test_room_StateGraphItem___init__():
    assert room_StateGraphItem.__init__(room_StateGraphItem()) == None

def test_room_StateGraphItem_getName():
    assert room_StateGraphItem.getName(room_StateGraphItem()) == None


from python_code import room_BindingEndPoint
from python_code import room_CompoundProtocolClass
from python_code import room_GeneralProtocolClass
from python_code import room_SubProtocol

def test_room_SubProtocol___init__():
    assert room_SubProtocol.__init__(room_SubProtocol('', room_SubProtocol213=room_BindingEndPoint(), room_SubProtocol=room_CompoundProtocolClass(), room_SubProtocol104=room_GeneralProtocolClass()), '', room_SubProtocol213=room_BindingEndPoint(), room_SubProtocol=room_CompoundProtocolClass(), room_SubProtocol104=room_GeneralProtocolClass()) == None


from python_code import room_StateGraph
from python_code import room_SubStateTrPointTerminal
from python_code import room_TrPoint
from python_code import room_TrPointTerminal

def test_room_TrPoint___init__():
    assert room_TrPoint.__init__(room_TrPoint('', room_TrPoint=room_StateGraph(), room_TrPoint288=room_TrPointTerminal(), room_TrPoint290=room_SubStateTrPointTerminal()), '', room_TrPoint=room_StateGraph(), room_TrPoint288=room_TrPointTerminal(), room_TrPoint290=room_SubStateTrPointTerminal()) == None


from python_code import room_TransitionPoint

def test_room_TransitionPoint___init__():
    assert room_TransitionPoint.__init__(room_TransitionPoint(True), False) == None

