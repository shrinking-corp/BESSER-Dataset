from python_code import arduino_CommunicationParams
from python_code import arduino_SystemDefinition

def test_arduino_CommunicationParams___init__():
    assert arduino_CommunicationParams.__init__(arduino_CommunicationParams('', '', '', '', '', '', 0, arduino_CommunicationParams=arduino_SystemDefinition()), '', '\x00', '', '', '', '', 0, arduino_CommunicationParams=arduino_SystemDefinition()) == None


from python_code import arduino_Dispatch
from python_code import arduino_ForwardDispatch
from python_code import arduino_ServeDispatch

def test_arduino_Dispatch___init__():
    assert arduino_Dispatch.__init__(arduino_Dispatch('', arduino_Dispatch=arduino_ForwardDispatch(), arduino_Dispatch66=arduino_ServeDispatch()), '', arduino_Dispatch=arduino_ForwardDispatch(), arduino_Dispatch66=arduino_ServeDispatch()) == None


from python_code import arduino_EmptyPrecondition

def test_arduino_EmptyPrecondition___init__():
    assert arduino_EmptyPrecondition.__init__(arduino_EmptyPrecondition(''), '') == None


from python_code import arduino_ExplicitSupportData

def test_arduino_ExplicitSupportData___init__():
    assert arduino_ExplicitSupportData.__init__(arduino_ExplicitSupportData('', 0), '', 0) == None


from python_code import arduino_IODevice

def test_arduino_IODevice___init__():
    assert arduino_IODevice.__init__(arduino_IODevice(False, False), False, False) == None


from python_code import arduino_IP

def test_arduino_IP___init__():
    assert arduino_IP.__init__(arduino_IP(''), '') == None


from python_code import arduino_OutInMessage

def test_arduino_OutInMessage___init__():
    assert arduino_OutInMessage.__init__(arduino_OutInMessage(''), '') == None


from python_code import arduino_Sketch
from python_code import arduino_SystemDefinition

def test_arduino_Sketch___init__():
    assert arduino_Sketch.__init__(arduino_Sketch(False, '', '', arduino_Sketch12=arduino_SystemDefinition(), arduino_Sketch=set(), arduino_Sketch2=set(), arduino_Sketch4=set(), arduino_Sketch6=set(), arduino_Sketch8=set(), arduino_Sketch10=set()), False, '\x00', '', arduino_Sketch12=arduino_SystemDefinition(), arduino_Sketch=set(), arduino_Sketch2=set(), arduino_Sketch4=set(), arduino_Sketch6=set(), arduino_Sketch8=set(), arduino_Sketch10=set()) == None


from python_code import arduino_InAcquireOperation
from python_code import arduino_SupportSpecification

def test_arduino_SupportSpecification___init__():
    assert arduino_SupportSpecification.__init__(arduino_SupportSpecification('', arduino_SupportSpecification=arduino_InAcquireOperation()), '', arduino_SupportSpecification=arduino_InAcquireOperation()) == None

