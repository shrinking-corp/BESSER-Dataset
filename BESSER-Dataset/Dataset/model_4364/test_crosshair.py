from python_code import workflow_CompilationUnit

def test_workflow_CompilationUnit___init__():
    assert workflow_CompilationUnit.__init__(workflow_CompilationUnit('\x00\x00', '', workflow_CompilationUnit=set()), '', '', workflow_CompilationUnit=set()) == None


from python_code import workflow_Constant

def test_workflow_Constant___init__():
    assert workflow_Constant.__init__(workflow_Constant('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import workflow_Declaration

def test_workflow_Declaration___init__():
    assert workflow_Declaration.__init__(workflow_Declaration(''), '') == None


from python_code import workflow_ProcedureCall

def test_workflow_ProcedureCall___init__():
    assert workflow_ProcedureCall.__init__(workflow_ProcedureCall('', workflow_ProcedureCall=set()), '', workflow_ProcedureCall=set()) == None

