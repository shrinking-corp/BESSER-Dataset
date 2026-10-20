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

