from python_code import petrinet_NamedElement

def test_petrinet_NamedElement___init__():
    assert petrinet_NamedElement.__init__(petrinet_NamedElement(''), '') == None


from python_code import petrinet_Net
from python_code import petrinet_Place
from python_code import petrinet_Transition

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place(0, petrinet_Place=petrinet_Net(), petrinet_Place5=petrinet_Net(), petrinet_Place7=petrinet_Transition(), petrinet_Place11=petrinet_Transition(), petrinet_Place14=petrinet_Transition()), 0, petrinet_Place=petrinet_Net(), petrinet_Place5=petrinet_Net(), petrinet_Place7=petrinet_Transition(), petrinet_Place11=petrinet_Transition(), petrinet_Place14=petrinet_Transition()) == None

