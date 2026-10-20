from python_code import workflow_AbstractState

def test_workflow_AbstractState___init__():
    assert workflow_AbstractState.__init__(workflow_AbstractState(''), '') == None


from python_code import workflow_Named

def test_workflow_Named___init__():
    assert workflow_Named.__init__(workflow_Named(''), '') == None

