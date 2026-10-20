from python_code import Behaviour_Colour
from python_code import Behaviour_Token

def test_Behaviour_Colour___init__():
    assert Behaviour_Colour.__init__(Behaviour_Colour('', Behaviour_Colour=Behaviour_Token()), '', Behaviour_Colour=Behaviour_Token()) == None


from python_code import Behaviour_ConditionalTransition
from python_code import Behaviour_PostTransitionConnection
from python_code import Behaviour_StochasticTransition
from python_code import Behaviour_TransitionFunction

def test_Behaviour_TransitionFunction___init__():
    assert Behaviour_TransitionFunction.__init__(Behaviour_TransitionFunction('', Behaviour_TransitionFunction=Behaviour_ConditionalTransition(), Behaviour_TransitionFunction21=Behaviour_StochasticTransition(), Behaviour_TransitionFunction44=Behaviour_PostTransitionConnection(), Behaviour_TransitionFunction47=set()), '', Behaviour_TransitionFunction=Behaviour_ConditionalTransition(), Behaviour_TransitionFunction21=Behaviour_StochasticTransition(), Behaviour_TransitionFunction44=Behaviour_PostTransitionConnection(), Behaviour_TransitionFunction47=set()) == None

