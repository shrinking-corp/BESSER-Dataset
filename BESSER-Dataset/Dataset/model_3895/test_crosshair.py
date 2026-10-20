from python_code import workflow_IPort

def test_workflow_IPort___init__():
    assert workflow_IPort.__init__(workflow_IPort(''), '') == None


from python_code import workflow_IWorkflowElement

def test_workflow_IWorkflowElement___init__():
    assert workflow_IWorkflowElement.__init__(workflow_IWorkflowElement('', '\x00'), '\x00\x00', '') == None


from python_code import workflow_IWorkflowJob

def test_workflow_IWorkflowJob___init__():
    assert workflow_IWorkflowJob.__init__(workflow_IWorkflowJob('', '\x00'), '\x00\x00', '') == None


from python_code import workflow_IInputPort
from python_code import workflow_IOutputPort
from python_code import workflow_IWorkflow
from python_code import workflow_IWorkflowNode

def test_workflow_IWorkflowNode___init__():
    assert workflow_IWorkflowNode.__init__(workflow_IWorkflowNode(False, False, nodes=workflow_IWorkflow(), node=set(), node21=set(), IWorkflowNode=workflow_IInputPort(), IWorkflowNode8=workflow_IOutputPort(), IWorkflowNode12=workflow_IWorkflow()), False, True, nodes=workflow_IWorkflow(), node=set(), node21=set(), IWorkflowNode=workflow_IInputPort(), IWorkflowNode8=workflow_IOutputPort(), IWorkflowNode12=workflow_IWorkflow()) == None

