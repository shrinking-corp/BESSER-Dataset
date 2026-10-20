from python_code import cfgraph_BodyVertex
from python_code import cfgraph_BranchingVertex
from python_code import cfgraph_ControlFlowEdge
from python_code import cfgraph_StartVertex
from python_code import cfgraph_StatementVertex

def test_cfgraph_ControlFlowEdge___init__():
    assert cfgraph_ControlFlowEdge.__init__(cfgraph_ControlFlowEdge(True, cfgraph_ControlFlowEdge=cfgraph_StartVertex(), ControlFlowEdge=cfgraph_BodyVertex(), incomingEdges=cfgraph_BodyVertex(), cfgraph_ControlFlowEdge6=cfgraph_StatementVertex(), cfgraph_ControlFlowEdge10=cfgraph_BranchingVertex()), False, cfgraph_ControlFlowEdge=cfgraph_StartVertex(), ControlFlowEdge=cfgraph_BodyVertex(), incomingEdges=cfgraph_BodyVertex(), cfgraph_ControlFlowEdge6=cfgraph_StatementVertex(), cfgraph_ControlFlowEdge10=cfgraph_BranchingVertex()) == None

