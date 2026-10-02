from python_code import workflow_AgentContainer

def test_workflow_AgentContainer___init__():
    assert workflow_AgentContainer.__init__(workflow_AgentContainer('', workflow_AgentContainer=set()), '', workflow_AgentContainer=set()) == None

from python_code import workflow_ConstantAtom

def test_workflow_ConstantAtom___init__():
    assert workflow_ConstantAtom.__init__(workflow_ConstantAtom(''), '') == None

from python_code import workflow_DefaultDocument

def test_workflow_DefaultDocument___init__():
    assert workflow_DefaultDocument.__init__(workflow_DefaultDocument(False, workflow_DefaultDocument=set(), workflow_DefaultDocument132=set()), False, workflow_DefaultDocument=set(), workflow_DefaultDocument132=set()) == None

from python_code import workflow_DocumentCondition
from python_code import workflow_TaskI

def test_workflow_DocumentCondition___init__():
    assert workflow_DocumentCondition.__init__(workflow_DocumentCondition('', workflow_DocumentCondition=workflow_TaskI(), workflow_DocumentCondition70=workflow_TaskI()), '', workflow_DocumentCondition=workflow_TaskI(), workflow_DocumentCondition70=workflow_TaskI()) == None

from python_code import workflow_DocumentTypeContainer

def test_workflow_DocumentTypeContainer___init__():
    assert workflow_DocumentTypeContainer.__init__(workflow_DocumentTypeContainer('', workflow_DocumentTypeContainer=set()), '', workflow_DocumentTypeContainer=set()) == None

from python_code import workflow_RuntimeInformation

def test_workflow_RuntimeInformation___init__():
    assert workflow_RuntimeInformation.__init__(workflow_RuntimeInformation(''), '') == None

from python_code import workflow_TaskC

def test_workflow_TaskC___init__():
    assert workflow_TaskC.__init__(workflow_TaskC(''), '') == None
