from python_code import pDL2_Guidance

def test_pDL2_Guidance___init__():
    assert pDL2_Guidance.__init__(pDL2_Guidance(''), '') == None


from python_code import pDL2_Process

def test_pDL2_Process___init__():
    assert pDL2_Process.__init__(pDL2_Process('', pDL2_Process=set()), '', pDL2_Process=set()) == None


from python_code import pDL2_DependanceFinish
from python_code import pDL2_DependanceStart
from python_code import pDL2_WorkDefinition

def test_pDL2_WorkDefinition___init__():
    assert pDL2_WorkDefinition.__init__(pDL2_WorkDefinition('', pDL2_WorkDefinition=set(), pDL2_WorkDefinition3=pDL2_DependanceStart(), pDL2_WorkDefinition7=pDL2_DependanceFinish()), '', pDL2_WorkDefinition=set(), pDL2_WorkDefinition3=pDL2_DependanceStart(), pDL2_WorkDefinition7=pDL2_DependanceFinish()) == None


from python_code import pDL2_DependanceFinish
from python_code import pDL2_WorkSequenceKindFinish

def test_pDL2_WorkSequenceKindFinish___init__():
    assert pDL2_WorkSequenceKindFinish.__init__(pDL2_WorkSequenceKindFinish('', '\x00', pDL2_WorkSequenceKindFinish=pDL2_DependanceFinish()), '\x00\x00', '', pDL2_WorkSequenceKindFinish=pDL2_DependanceFinish()) == None


from python_code import pDL2_DependanceStart
from python_code import pDL2_WorkSequenceKindStart

def test_pDL2_WorkSequenceKindStart___init__():
    assert pDL2_WorkSequenceKindStart.__init__(pDL2_WorkSequenceKindStart('', '\x00', pDL2_WorkSequenceKindStart=pDL2_DependanceStart()), '\x00\x00', '', pDL2_WorkSequenceKindStart=pDL2_DependanceStart()) == None

