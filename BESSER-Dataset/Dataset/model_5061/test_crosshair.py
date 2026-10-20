from python_code import bpmn2_AdHocSubProcess
from python_code import bpmn2_Expression

def test_bpmn2_AdHocSubProcess___init__():
    assert bpmn2_AdHocSubProcess.__init__(bpmn2_AdHocSubProcess('', False, bpmn2_AdHocSubProcess=bpmn2_Expression()), '', False, bpmn2_AdHocSubProcess=bpmn2_Expression()) == None


from python_code import bpmn2_BusinessRuleTask

def test_bpmn2_BusinessRuleTask___init__():
    assert bpmn2_BusinessRuleTask.__init__(bpmn2_BusinessRuleTask(''), '') == None


from python_code import bpmn2_DataObject
from python_code import bpmn2_DataObjectReference

def test_bpmn2_DataObject___init__():
    assert bpmn2_DataObject.__init__(bpmn2_DataObject(True, bpmn2_DataObject=bpmn2_DataObjectReference()), False, bpmn2_DataObject=bpmn2_DataObjectReference()) == None


from python_code import bpmn2_DataState
from python_code import bpmn2_ItemAwareElement

def test_bpmn2_DataState___init__():
    assert bpmn2_DataState.__init__(bpmn2_DataState('', bpmn2_DataState=bpmn2_ItemAwareElement()), '', bpmn2_DataState=bpmn2_ItemAwareElement()) == None


from python_code import bpmn2_DataStore
from python_code import bpmn2_DataStoreReference

def test_bpmn2_DataStore___init__():
    assert bpmn2_DataStore.__init__(bpmn2_DataStore('', 0, False, bpmn2_DataStore=bpmn2_DataStoreReference()), '\x00', 0, False, bpmn2_DataStore=bpmn2_DataStoreReference()) == None


from python_code import bpmn2_EventBasedGateway

def test_bpmn2_EventBasedGateway___init__():
    assert bpmn2_EventBasedGateway.__init__(bpmn2_EventBasedGateway(False, '\x00'), False, '\x00') == None


from python_code import bpmn2_Gateway

def test_bpmn2_Gateway___init__():
    assert bpmn2_Gateway.__init__(bpmn2_Gateway(''), '') == None


from python_code import bpmn2_GlobalBusinessRuleTask

def test_bpmn2_GlobalBusinessRuleTask___init__():
    assert bpmn2_GlobalBusinessRuleTask.__init__(bpmn2_GlobalBusinessRuleTask(''), '') == None


from python_code import bpmn2_GlobalScriptTask

def test_bpmn2_GlobalScriptTask___init__():
    assert bpmn2_GlobalScriptTask.__init__(bpmn2_GlobalScriptTask('', '\x00'), '\x00\x00', '') == None


from python_code import bpmn2_GlobalUserTask

def test_bpmn2_GlobalUserTask___init__():
    assert bpmn2_GlobalUserTask.__init__(bpmn2_GlobalUserTask('', bpmn2_GlobalUserTask=set()), '', bpmn2_GlobalUserTask=set()) == None


from python_code import bpmn2_PartnerEntity

def test_bpmn2_PartnerEntity___init__():
    assert bpmn2_PartnerEntity.__init__(bpmn2_PartnerEntity('', bpmn2_PartnerEntity=set()), '', bpmn2_PartnerEntity=set()) == None


from python_code import bpmn2_PartnerRole

def test_bpmn2_PartnerRole___init__():
    assert bpmn2_PartnerRole.__init__(bpmn2_PartnerRole('', bpmn2_PartnerRole=set()), '', bpmn2_PartnerRole=set()) == None


from python_code import bpmn2_ScriptTask

def test_bpmn2_ScriptTask___init__():
    assert bpmn2_ScriptTask.__init__(bpmn2_ScriptTask('', '\x00'), '\x00\x00', '') == None


from python_code import bpmn2_Expression
from python_code import bpmn2_StandardLoopCharacteristics

def test_bpmn2_StandardLoopCharacteristics___init__():
    assert bpmn2_StandardLoopCharacteristics.__init__(bpmn2_StandardLoopCharacteristics(True, bpmn2_StandardLoopCharacteristics=bpmn2_Expression(), bpmn2_StandardLoopCharacteristics456=bpmn2_Expression()), False, bpmn2_StandardLoopCharacteristics=bpmn2_Expression(), bpmn2_StandardLoopCharacteristics456=bpmn2_Expression()) == None


from python_code import bpmn2_StartEvent

def test_bpmn2_StartEvent___init__():
    assert bpmn2_StartEvent.__init__(bpmn2_StartEvent(True), False) == None


from python_code import bpmn2_SubProcess

def test_bpmn2_SubProcess___init__():
    assert bpmn2_SubProcess.__init__(bpmn2_SubProcess(False, bpmn2_SubProcess=set()), False, bpmn2_SubProcess=set()) == None


from python_code import bpmn2_TextAnnotation

def test_bpmn2_TextAnnotation___init__():
    assert bpmn2_TextAnnotation.__init__(bpmn2_TextAnnotation('', '\x00'), '\x00\x00', '') == None


from python_code import bpmn2_Transaction

def test_bpmn2_Transaction___init__():
    assert bpmn2_Transaction.__init__(bpmn2_Transaction('', '\x00'), '\x00\x00', '') == None


from python_code import bpmn2_UserTask

def test_bpmn2_UserTask___init__():
    assert bpmn2_UserTask.__init__(bpmn2_UserTask('', bpmn2_UserTask=set()), '', bpmn2_UserTask=set()) == None

