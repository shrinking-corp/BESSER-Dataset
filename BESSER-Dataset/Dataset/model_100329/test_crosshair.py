from python_code import pnml_PNMLDocument

def test_pnml_PNMLDocument___init__():
    assert pnml_PNMLDocument.__init__(pnml_PNMLDocument('', pnml_PNMLDocument=set()), '', pnml_PNMLDocument=set()) == None


from python_code import pnml_ArcPlace2Transition
from python_code import pnml_ArcTransition2Place
from python_code import pnml_PlaceElement

def test_pnml_PlaceElement___init__():
    assert pnml_PlaceElement.__init__(pnml_PlaceElement('', 0, pnml_PlaceElement=pnml_ArcPlace2Transition(), pnml_PlaceElement5=pnml_ArcTransition2Place()), '', 0, pnml_PlaceElement=pnml_ArcPlace2Transition(), pnml_PlaceElement5=pnml_ArcTransition2Place()) == None


from python_code import pnml_ArcPlace2Transition
from python_code import pnml_ArcTransition2Place
from python_code import pnml_TransitionElement

def test_pnml_TransitionElement___init__():
    assert pnml_TransitionElement.__init__(pnml_TransitionElement('', pnml_TransitionElement=pnml_ArcPlace2Transition(), pnml_TransitionElement8=pnml_ArcTransition2Place()), '', pnml_TransitionElement=pnml_ArcPlace2Transition(), pnml_TransitionElement8=pnml_ArcTransition2Place()) == None

