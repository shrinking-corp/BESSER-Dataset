from python_code import bpmn_Artifact
from python_code import bpmn_Association
from python_code import bpmn_AssociationTarget

def test_bpmn_Association___init__():
    assert bpmn_Association.__init__(bpmn_Association('', associations=bpmn_Artifact(), Association=bpmn_Artifact(), associations10=bpmn_AssociationTarget(), Association12=bpmn_AssociationTarget()), '', associations=bpmn_Artifact(), Association=bpmn_Artifact(), associations10=bpmn_AssociationTarget(), Association12=bpmn_AssociationTarget()) == None


from python_code import bpmn_BpmnDiagram
from python_code import bpmn_MessagingEdge
from python_code import bpmn_Pool

def test_bpmn_BpmnDiagram___init__():
    assert bpmn_BpmnDiagram.__init__(bpmn_BpmnDiagram('', '', bpmnDiagram=set(), bpmnDiagram15=set(), BpmnDiagram=bpmn_MessagingEdge(), BpmnDiagram38=bpmn_Pool()), '', '', bpmnDiagram=set(), bpmnDiagram15=set(), BpmnDiagram=bpmn_MessagingEdge(), BpmnDiagram38=bpmn_Pool()) == None


from python_code import bpmn_Identifiable

def test_bpmn_Identifiable___init__():
    assert bpmn_Identifiable.__init__(bpmn_Identifiable(''), '') == None


from python_code import bpmn_MessageVertex
from python_code import bpmn_MessagingEdge

def test_bpmn_MessageVertex___init__():
    assert bpmn_MessageVertex.__init__(bpmn_MessageVertex('', target26=set(), source29=set(), MessageVertex=bpmn_MessagingEdge(), MessageVertex33=bpmn_MessagingEdge()), '', target26=set(), source29=set(), MessageVertex=bpmn_MessagingEdge(), MessageVertex33=bpmn_MessagingEdge()) == None


from python_code import bpmn_NamedBpmnObject

def test_bpmn_NamedBpmnObject___init__():
    assert bpmn_NamedBpmnObject.__init__(bpmn_NamedBpmnObject('', '', '\x00\x00'), '', '', '') == None


from python_code import bpmn_Graph
from python_code import bpmn_SequenceEdge
from python_code import bpmn_Vertex

def test_bpmn_SequenceEdge___init__():
    assert bpmn_SequenceEdge.__init__(bpmn_SequenceEdge('', '\x00', SequenceEdge=bpmn_Graph(), sequenceEdges=bpmn_Graph(), outgoingEdges=bpmn_Vertex(), incomingEdges=bpmn_Vertex(), SequenceEdge48=bpmn_Vertex(), SequenceEdge51=bpmn_Vertex()), '\x00\x00', '', SequenceEdge=bpmn_Graph(), sequenceEdges=bpmn_Graph(), outgoingEdges=bpmn_Vertex(), incomingEdges=bpmn_Vertex(), SequenceEdge48=bpmn_Vertex(), SequenceEdge51=bpmn_Vertex()) == None

