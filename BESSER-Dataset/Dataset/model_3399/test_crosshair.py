from python_code import Predicate
from python_code import guigraph_ConditionActionTransition
from python_code import guigraph_PreGenerationSequence

def test_guigraph_ConditionActionTransition___init__():
    assert guigraph_ConditionActionTransition.__init__(guigraph_ConditionActionTransition('', '\x00', guigraph_ConditionActionTransition=Predicate(), guigraph_ConditionActionTransition10=guigraph_PreGenerationSequence()), '\x00\x00', '', guigraph_ConditionActionTransition=Predicate(), guigraph_ConditionActionTransition10=guigraph_PreGenerationSequence()) == None


from python_code import Predicate
from python_code import guigraph_GuiGraph
from python_code import guigraph_PageTransition

def test_guigraph_GuiGraph___init__():
    assert guigraph_GuiGraph.__init__(guigraph_GuiGraph('', guigraph_GuiGraph=set(), guigraph_GuiGraph2=set(), guigraph_GuiGraph4=Predicate(), guigraph_GuiGraph19=guigraph_PageTransition()), '', guigraph_GuiGraph=set(), guigraph_GuiGraph2=set(), guigraph_GuiGraph4=Predicate(), guigraph_GuiGraph19=guigraph_PageTransition()) == None


from python_code import guigraph_PageMappingArc
from python_code import guigraph_Place

def test_guigraph_Place___init__():
    assert guigraph_Place.__init__(guigraph_Place(0, False, guigraph_Place=guigraph_PageMappingArc()), 0, False, guigraph_Place=guigraph_PageMappingArc()) == None


from python_code import guigraph_StandardArc

def test_guigraph_StandardArc___init__():
    assert guigraph_StandardArc.__init__(guigraph_StandardArc(0), 0) == None


from python_code import ITimeConsumer
from python_code import guigraph_TimerTransition

def test_guigraph_TimerTransition___init__():
    assert guigraph_TimerTransition.__init__(guigraph_TimerTransition(0, guigraph_TimerTransition=ITimeConsumer()), 0, guigraph_TimerTransition=ITimeConsumer()) == None


from python_code import guigraph_Transition

def test_guigraph_Transition___init__():
    assert guigraph_Transition.__init__(guigraph_Transition(0.0, False, '', '', ''), 0.0, False, '', '', '\x00') == None

