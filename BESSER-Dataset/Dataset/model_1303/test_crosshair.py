from python_code import StateMachines_ConnectionPointReference
from python_code import StateMachines_Pseudostate
from python_code import StateMachines_State

def test_StateMachines_Pseudostate___init__():
    assert StateMachines_Pseudostate.__init__(StateMachines_Pseudostate('', StateMachines_Pseudostate35=StateMachines_ConnectionPointReference(), StateMachines_Pseudostate38=StateMachines_ConnectionPointReference(), StateMachines_Pseudostate=StateMachines_State()), '', StateMachines_Pseudostate35=StateMachines_ConnectionPointReference(), StateMachines_Pseudostate38=StateMachines_ConnectionPointReference(), StateMachines_Pseudostate=StateMachines_State()) == None


from python_code import StateMachines_Region
from python_code import StateMachines_Transition
from python_code import StateMachines_Vertex

def test_StateMachines_Transition___init__():
    assert StateMachines_Transition.__init__(StateMachines_Transition('', StateMachines_Transition=StateMachines_Region(), StateMachines_Transition7=StateMachines_Vertex(), StateMachines_Transition10=StateMachines_Vertex(), StateMachines_Transition12=set()), '', StateMachines_Transition=StateMachines_Region(), StateMachines_Transition7=StateMachines_Vertex(), StateMachines_Transition10=StateMachines_Vertex(), StateMachines_Transition12=set()) == None

