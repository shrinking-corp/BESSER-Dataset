from python_code import petrinet2_Element
from python_code import petrinet2_Petrinet

def test_petrinet2_Element___init__():
    assert petrinet2_Element.__init__(petrinet2_Element('', petrinet2_Element=petrinet2_Petrinet()), '', petrinet2_Element=petrinet2_Petrinet()) == None


from python_code import petrinet2_Transition

def test_petrinet2_Transition___init__():
    assert petrinet2_Transition.__init__(petrinet2_Transition(0.0, 0.0), 0.0, 0.0) == None

