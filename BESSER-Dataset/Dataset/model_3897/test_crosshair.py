from python_code import workflow_ForEach

def test_workflow_ForEach___init__():
    assert workflow_ForEach.__init__(workflow_ForEach('\x00\x00', '', workflow_ForEach=set()), '', '', workflow_ForEach=set()) == None


from python_code import workflow_SimpleCommand

def test_workflow_SimpleCommand___init__():
    assert workflow_SimpleCommand.__init__(workflow_SimpleCommand('', workflow_SimpleCommand=set()), '', workflow_SimpleCommand=set()) == None


from python_code import workflow_Workflow

def test_workflow_Workflow___init__():
    assert workflow_Workflow.__init__(workflow_Workflow('', workflow_Workflow=set()), '', workflow_Workflow=set()) == None

