from python_code import MySM_Action
from python_code import MySM_LabeledTransition
from python_code import MySM_Statemachine

def test_MySM_Action___init__():
    assert MySM_Action.__init__(MySM_Action('', MySM_Action=MySM_Statemachine(), MySM_Action17=MySM_LabeledTransition()), '', MySM_Action=MySM_Statemachine(), MySM_Action17=MySM_LabeledTransition()) == None


from python_code import MySM_Statemachine
from python_code import MySM_Transition
from python_code import MySM_Vertex

def test_MySM_Transition___init__():
    assert MySM_Transition.__init__(MySM_Transition('', MySM_Transition=MySM_Statemachine(), MySM_Transition11=MySM_Vertex(), MySM_Transition14=MySM_Vertex(), MySM_Transition7=MySM_Vertex()), '', MySM_Transition=MySM_Statemachine(), MySM_Transition11=MySM_Vertex(), MySM_Transition14=MySM_Vertex(), MySM_Transition7=MySM_Vertex()) == None

