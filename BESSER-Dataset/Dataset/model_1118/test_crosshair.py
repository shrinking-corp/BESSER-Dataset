from python_code import rtsc_Connector
from python_code import rtsc_CoordinationProtocol
from python_code import rtsc_System

def test_rtsc_CoordinationProtocol___init__():
    assert rtsc_CoordinationProtocol.__init__(rtsc_CoordinationProtocol(rtsc_CoordinationProtocol=set(), rtsc_CoordinationProtocol60=rtsc_Connector(), rtsc_CoordinationProtocol68=rtsc_System()), rtsc_CoordinationProtocol=set(), rtsc_CoordinationProtocol60=rtsc_Connector(), rtsc_CoordinationProtocol68=rtsc_System()) == None

def test_rtsc_CoordinationProtocol_step():
    assert rtsc_CoordinationProtocol.step(rtsc_CoordinationProtocol(rtsc_CoordinationProtocol=set(), rtsc_CoordinationProtocol60=rtsc_Connector(), rtsc_CoordinationProtocol68=rtsc_System())) == None

def test_rtsc_CoordinationProtocol_initialize():
    assert rtsc_CoordinationProtocol.initialize(rtsc_CoordinationProtocol(rtsc_CoordinationProtocol=set(), rtsc_CoordinationProtocol60=rtsc_Connector(), rtsc_CoordinationProtocol68=rtsc_System()), 0) == None

def test_rtsc_CoordinationProtocol_main():
    assert rtsc_CoordinationProtocol.main(rtsc_CoordinationProtocol(rtsc_CoordinationProtocol=set(), rtsc_CoordinationProtocol60=rtsc_Connector(), rtsc_CoordinationProtocol68=rtsc_System())) == None


from python_code import rtsc_MessageBuffer
from python_code import rtsc_Port

def test_rtsc_MessageBuffer___init__():
    assert rtsc_MessageBuffer.__init__(rtsc_MessageBuffer(MessageBuffer=rtsc_Port(), incomingBuffer=rtsc_Port(), rtsc_MessageBuffer=set(), rtsc_MessageBuffer54=set()), MessageBuffer=rtsc_Port(), incomingBuffer=rtsc_Port(), rtsc_MessageBuffer=set(), rtsc_MessageBuffer54=set()) == None

def test_rtsc_MessageBuffer_addMessage():
    assert rtsc_MessageBuffer.addMessage(rtsc_MessageBuffer(MessageBuffer=rtsc_Port(), incomingBuffer=rtsc_Port(), rtsc_MessageBuffer=set(), rtsc_MessageBuffer54=set()), 0) == None

def test_rtsc_MessageBuffer_getMessage():
    assert rtsc_MessageBuffer.getMessage(rtsc_MessageBuffer(MessageBuffer=rtsc_Port(), incomingBuffer=rtsc_Port(), rtsc_MessageBuffer=set(), rtsc_MessageBuffer54=set()), 0) == None

def test_rtsc_MessageBuffer_hasMessage():
    assert rtsc_MessageBuffer.hasMessage(rtsc_MessageBuffer(MessageBuffer=rtsc_Port(), incomingBuffer=rtsc_Port(), rtsc_MessageBuffer=set(), rtsc_MessageBuffer54=set()), 0) == None


from python_code import rtsc_MessageEvent
from python_code import rtsc_MessageType

def test_rtsc_MessageEvent___init__():
    assert rtsc_MessageEvent.__init__(rtsc_MessageEvent(rtsc_MessageEvent=rtsc_MessageType()), rtsc_MessageEvent=rtsc_MessageType()) == None

def test_rtsc_MessageEvent_execute():
    assert rtsc_MessageEvent.execute(rtsc_MessageEvent(rtsc_MessageEvent=rtsc_MessageType())) == None


from python_code import rtsc_NamedElement

def test_rtsc_NamedElement___init__():
    assert rtsc_NamedElement.__init__(rtsc_NamedElement(''), '') == None


from python_code import rtsc_Vertex

def test_rtsc_Vertex___init__():
    assert rtsc_Vertex.__init__(rtsc_Vertex(True), False) == None

