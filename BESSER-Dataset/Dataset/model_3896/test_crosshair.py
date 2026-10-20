from python_code import workflow_AbstractTask
from python_code import workflow_BaseTask

def test_workflow_AbstractTask___init__():
    assert workflow_AbstractTask.__init__(workflow_AbstractTask('', workflow_AbstractTask=set(), workflow_AbstractTask2=set(), workflow_AbstractTask4=workflow_BaseTask()), '', workflow_AbstractTask=set(), workflow_AbstractTask2=set(), workflow_AbstractTask4=workflow_BaseTask()) == None


from python_code import workflow_CustomTask

def test_workflow_CustomTask___init__():
    assert workflow_CustomTask.__init__(workflow_CustomTask(''), '') == None


from python_code import workflow_NamedElement

def test_workflow_NamedElement___init__():
    assert workflow_NamedElement.__init__(workflow_NamedElement(''), '') == None


from python_code import workflow_TypedElement

def test_workflow_TypedElement___init__():
    assert workflow_TypedElement.__init__(workflow_TypedElement('', '\x00'), '\x00\x00', '') == None


from python_code import workflow_BaseTask
from python_code import workflow_Workflow

def test_workflow_Workflow___init__():
    assert workflow_Workflow.__init__(workflow_Workflow('', workflow_Workflow=workflow_BaseTask(), workflow_Workflow13=set()), '', workflow_Workflow=workflow_BaseTask(), workflow_Workflow13=set()) == None

