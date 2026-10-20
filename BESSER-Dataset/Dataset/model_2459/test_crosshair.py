from python_code import dscDiagramModel_DSCDiagram

def test_dscDiagramModel_DSCDiagram___init__():
    assert dscDiagramModel_DSCDiagram.__init__(dscDiagramModel_DSCDiagram('', '', '', '', ''), '', '', '', '', '') == None


from python_code import dscDiagramModel_DSCState
from python_code import dscDiagramModel_DeepHistory
from python_code import dscDiagramModel_ShallowHistory
from python_code import dscDiagramModel_StartPoint

def test_dscDiagramModel_DSCState___init__():
    assert dscDiagramModel_DSCState.__init__(dscDiagramModel_DSCState('', False, compositeState=dscDiagramModel_StartPoint(), compositeState7=dscDiagramModel_ShallowHistory(), compositeState9=dscDiagramModel_DeepHistory(), DSCState=dscDiagramModel_StartPoint(), DSCState2=dscDiagramModel_ShallowHistory(), DSCState4=dscDiagramModel_DeepHistory()), '', False, compositeState=dscDiagramModel_StartPoint(), compositeState7=dscDiagramModel_ShallowHistory(), compositeState9=dscDiagramModel_DeepHistory(), DSCState=dscDiagramModel_StartPoint(), DSCState2=dscDiagramModel_ShallowHistory(), DSCState4=dscDiagramModel_DeepHistory()) == None


from python_code import dscDiagramModel_Transition

def test_dscDiagramModel_Transition___init__():
    assert dscDiagramModel_Transition.__init__(dscDiagramModel_Transition('', '', '', '', False, False, False), '', '\x00', '', '', False, False, False) == None

