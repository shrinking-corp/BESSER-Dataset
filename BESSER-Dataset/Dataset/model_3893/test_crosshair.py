from python_code import workflow_ConditionalOutputPort

def test_workflow_ConditionalOutputPort___init__():
    assert workflow_ConditionalOutputPort.__init__(workflow_ConditionalOutputPort(''), '') == None


from python_code import workflow_LoopTask

def test_workflow_LoopTask___init__():
    assert workflow_LoopTask.__init__(workflow_LoopTask(''), '') == None


from python_code import workflow_TransformationTask

def test_workflow_TransformationTask___init__():
    assert workflow_TransformationTask.__init__(workflow_TransformationTask(''), '') == None


from python_code import workflow_WorkflowElement

def test_workflow_WorkflowElement___init__():
    assert workflow_WorkflowElement.__init__(workflow_WorkflowElement('', '', 0, 0, 0, 0, ''), '', '\x00', 0, 0, 0, 0, '') == None


from python_code import workflow_InputPort
from python_code import workflow_OutputPort
from python_code import workflow_Workflow
from python_code import workflow_WorkflowNode

def test_workflow_WorkflowNode___init__():
    assert workflow_WorkflowNode.__init__(workflow_WorkflowNode(False, False, WorkflowNode=workflow_Workflow(), WorkflowNode22=workflow_OutputPort(), nodes=workflow_Workflow(), node=set(), node8=set(), WorkflowNode18=workflow_InputPort()), False, True, WorkflowNode=workflow_Workflow(), WorkflowNode22=workflow_OutputPort(), nodes=workflow_Workflow(), node=set(), node8=set(), WorkflowNode18=workflow_InputPort()) == None

