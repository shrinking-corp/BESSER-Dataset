from python_code import behavior_AbstractBehaviorModelGraph

def test_behavior_AbstractBehaviorModelGraph___init__():
    assert behavior_AbstractBehaviorModelGraph.__init__(behavior_AbstractBehaviorModelGraph('', behavior_AbstractBehaviorModelGraph=set()), '', behavior_AbstractBehaviorModelGraph=set()) == None


from python_code import behavior_BehaviorMix
from python_code import behavior_BehaviorMixEntry
from python_code import behavior_BehaviorModelRelative

def test_behavior_BehaviorMixEntry___init__():
    assert behavior_BehaviorMixEntry.__init__(behavior_BehaviorMixEntry('\x00', 0.0, behavior_BehaviorMixEntry=behavior_BehaviorMix(), behavior_BehaviorMixEntry17=behavior_BehaviorModelRelative()), '', 0.0, behavior_BehaviorMixEntry=behavior_BehaviorMix(), behavior_BehaviorMixEntry17=behavior_BehaviorModelRelative()) == None


from python_code import behavior_Session
from python_code import behavior_SessionRepository

def test_behavior_Session___init__():
    assert behavior_Session.__init__(behavior_Session('', '', '', '', behavior_Session=behavior_SessionRepository(), behavior_Session3=set()), '', '', '', '', behavior_Session=behavior_SessionRepository(), behavior_Session3=set()) == None


from python_code import behavior_Transition
from python_code import behavior_Vertex

def test_behavior_Transition___init__():
    assert behavior_Transition.__init__(behavior_Transition(0.0, '', '', behavior_Transition=behavior_Vertex(), behavior_Transition10=behavior_Vertex(), behavior_Transition13=behavior_Vertex()), 0.0, '', '', behavior_Transition=behavior_Vertex(), behavior_Transition10=behavior_Vertex(), behavior_Transition13=behavior_Vertex()) == None


from python_code import behavior_AbstractUseCaseExecution
from python_code import behavior_UseCase
from python_code import behavior_UseCaseRepository

def test_behavior_UseCase___init__():
    assert behavior_UseCase.__init__(behavior_UseCase('', '\x00', behavior_UseCase=behavior_UseCaseRepository(), behavior_UseCase5=behavior_AbstractUseCaseExecution()), '\x00\x00', '', behavior_UseCase=behavior_UseCaseRepository(), behavior_UseCase5=behavior_AbstractUseCaseExecution()) == None

