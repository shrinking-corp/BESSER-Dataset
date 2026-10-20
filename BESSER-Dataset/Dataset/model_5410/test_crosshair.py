from python_code import fault_tree_Event
from python_code import fault_tree_FaultTree
from python_code import fault_tree_Gate
from python_code import fault_tree_IntermediateEvent

def test_fault_tree_Event___init__():
    assert fault_tree_Event.__init__(fault_tree_Event('', '\x00', Event=fault_tree_Gate(), Event8=fault_tree_Gate(), outputEvent=fault_tree_Gate(), inputEvents=fault_tree_Gate(), event=fault_tree_FaultTree(), fault_tree_Event=fault_tree_IntermediateEvent(), fault_tree_Event21=fault_tree_IntermediateEvent(), Event55=fault_tree_FaultTree()), '\x00\x00', '', Event=fault_tree_Gate(), Event8=fault_tree_Gate(), outputEvent=fault_tree_Gate(), inputEvents=fault_tree_Gate(), event=fault_tree_FaultTree(), fault_tree_Event=fault_tree_IntermediateEvent(), fault_tree_Event21=fault_tree_IntermediateEvent(), Event55=fault_tree_FaultTree()) == None

