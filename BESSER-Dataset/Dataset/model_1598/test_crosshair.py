from python_code import Petrinet_Element
from python_code import Petrinet_Petrinet

def test_Petrinet_Element___init__():
    assert Petrinet_Element.__init__(Petrinet_Element('', Petrinet_Element=Petrinet_Petrinet()), '', Petrinet_Element=Petrinet_Petrinet()) == None


from python_code import Petrinet_InputArc
from python_code import Petrinet_OutputArc
from python_code import Petrinet_Transition

def test_Petrinet_Transition___init__():
    assert Petrinet_Transition.__init__(Petrinet_Transition(0.0, 0.0, Petrinet_Transition=Petrinet_OutputArc(), Petrinet_Transition5=Petrinet_InputArc()), 0.0, 0.0, Petrinet_Transition=Petrinet_OutputArc(), Petrinet_Transition5=Petrinet_InputArc()) == None

