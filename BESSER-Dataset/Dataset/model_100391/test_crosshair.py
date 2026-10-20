from python_code import sgraph_Entry

def test_sgraph_Entry___init__():
    assert sgraph_Entry.__init__(sgraph_Entry(''), '') == None


from python_code import sgraph_ExpressionElement

def test_sgraph_ExpressionElement___init__():
    assert sgraph_ExpressionElement.__init__(sgraph_ExpressionElement(''), '') == None


from python_code import sgraph_NamedElement

def test_sgraph_NamedElement___init__():
    assert sgraph_NamedElement.__init__(sgraph_NamedElement(''), '') == None


from python_code import sgraph_State
from python_code import sgraph_Statechart

def test_sgraph_State___init__():
    assert sgraph_State.__init__(sgraph_State(False, True, False, False, False, sgraph_State=set(), sgraph_State28=sgraph_Statechart()), False, False, False, False, False, sgraph_State=set(), sgraph_State28=sgraph_Statechart()) == None


from python_code import sgraph_Transition
from python_code import sgraph_Vertex

def test_sgraph_Transition___init__():
    assert sgraph_Transition.__init__(sgraph_Transition(0, Transition=sgraph_Vertex(), Transition3=sgraph_Vertex(), incomingTransitions=sgraph_Vertex(), outgoingTransitions=sgraph_Vertex()), 0, Transition=sgraph_Vertex(), Transition3=sgraph_Vertex(), incomingTransitions=sgraph_Vertex(), outgoingTransitions=sgraph_Vertex()) == None

