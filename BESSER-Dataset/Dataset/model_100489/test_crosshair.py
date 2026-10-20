from python_code import ActionExpression
from python_code import ActionSequence
from python_code import Common_Behavior_Action
from python_code import Core_Namespace
from python_code import IterationExpression
from python_code import ObjectSetExpression
from python_code import State_Machines_StateMachine

def test_Common_Behavior_Action___init__():
    assert Common_Behavior_Action.__init__(Common_Behavior_Action('', action=set(), action2=ActionSequence(), Common_Behavior_Action=IterationExpression(), Common_Behavior_Action5=ObjectSetExpression(), Common_Behavior_Action7=ActionExpression(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace()), '', action=set(), action2=ActionSequence(), Common_Behavior_Action=IterationExpression(), Common_Behavior_Action5=ObjectSetExpression(), Common_Behavior_Action7=ActionExpression(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace()) == None


from python_code import BehavioralFeature
from python_code import Classifier
from python_code import Common_Behavior_Reception
from python_code import Core_Namespace
from python_code import Core_Parameter
from python_code import Expression
from python_code import Signal
from python_code import State_Machines_StateMachine

def test_Common_Behavior_Reception___init__():
    assert Common_Behavior_Reception.__init__(Common_Behavior_Reception('\x01', '', '', '', Common_Behavior_Reception=Signal(), BehavioralFeature=Core_Parameter('', Core_Parameter=Classifier(), parameter=BehavioralFeature(), Core_Parameter82=Expression(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace())), '', '', '', '', Common_Behavior_Reception=Signal(), BehavioralFeature=Core_Parameter('\x00', Core_Parameter=Classifier(), parameter=BehavioralFeature(), Core_Parameter82=Expression(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace())) == None


from python_code import Core_BehavioralFeature
from python_code import Core_Classifier

def test_Core_BehavioralFeature___init__():
    assert Core_BehavioralFeature.__init__(Core_BehavioralFeature('', behavioralFeature=set(), Feature=Core_Classifier()), '', behavioralFeature=set(), Feature=Core_Classifier()) == None


from python_code import Classifier
from python_code import Core_Feature
from python_code import Core_Namespace
from python_code import State_Machines_StateMachine

def test_Core_Feature___init__():
    assert Core_Feature.__init__(Core_Feature('', feature=Classifier(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace()), '\x00', feature=Classifier(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace()) == None


from python_code import Core_GeneralizableElement
from python_code import Core_Namespace
from python_code import State_Machines_StateMachine

def test_Core_GeneralizableElement___init__():
    assert Core_GeneralizableElement.__init__(Core_GeneralizableElement('', '', '', child=set(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace()), '', '', '', child=set(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace()) == None


from python_code import Classifier
from python_code import Core_Classifier
from python_code import Core_Generalization_

def test_Core_Generalization____init__():
    assert Core_Generalization_.__init__(Core_Generalization_('', Core_Generalization=Core_Classifier(), powertypeRange=Classifier(), generalization=Core_Classifier()), '\x00', Core_Generalization=Core_Classifier(), powertypeRange=Classifier(), generalization=Core_Classifier()) == None


from python_code import Core_Classifier
from python_code import Core_ModelElement
from python_code import Namespace

def test_Core_ModelElement___init__():
    assert Core_ModelElement.__init__(Core_ModelElement('', '', '', ownedElement=Core_Classifier()), '', '', '', ownedElement=Namespace()) == None


from python_code import BehavioralFeature
from python_code import Classifier
from python_code import Core_Namespace
from python_code import Core_Operation
from python_code import Core_Parameter
from python_code import Expression
from python_code import State_Machines_StateMachine

def test_Core_Operation___init__():
    assert Core_Operation.__init__(Core_Operation('', '', '', '', '', BehavioralFeature=Core_Parameter('', Core_Parameter=Classifier(), parameter=BehavioralFeature(), Core_Parameter82=Expression(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace())), '', '', '', '', '', BehavioralFeature=Core_Parameter('', Core_Parameter=Classifier(), parameter=BehavioralFeature(), Core_Parameter82=Expression(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace())) == None


from python_code import BehavioralFeature
from python_code import Classifier
from python_code import Core_Namespace
from python_code import Core_Parameter
from python_code import Expression
from python_code import State_Machines_StateMachine

def test_Core_Parameter___init__():
    assert Core_Parameter.__init__(Core_Parameter('', Core_Parameter=Classifier(), parameter=BehavioralFeature(), Core_Parameter82=Expression(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace()), '', Core_Parameter=Classifier(), parameter=BehavioralFeature(), Core_Parameter82=Expression(), ModelElement=State_Machines_StateMachine(), ModelElement70=Core_Namespace()) == None


from python_code import Data_Types_Expression

def test_Data_Types_Expression___init__():
    assert Data_Types_Expression.__init__(Data_Types_Expression('', '\x00'), '\x00\x00', '') == None


from python_code import State_Machines_CompositeState
from python_code import State_Machines_StateMachine

def test_State_Machines_CompositeState___init__():
    assert State_Machines_CompositeState.__init__(State_Machines_CompositeState('\x00', container=set(), State=State_Machines_StateMachine()), '', container=set(), State=State_Machines_StateMachine()) == None


from python_code import State_Machines_CompositeState
from python_code import State_Machines_Pseudostate
from python_code import State_Machines_StateMachine
from python_code import State_Machines_Transition

def test_State_Machines_Pseudostate___init__():
    assert State_Machines_Pseudostate.__init__(State_Machines_Pseudostate('\x00\x00', StateVertex53=State_Machines_Transition(), StateVertex59=State_Machines_CompositeState('', container=set(), State=State_Machines_StateMachine()), StateVertex=State_Machines_Transition()), '', StateVertex53=State_Machines_Transition(), StateVertex59=State_Machines_CompositeState('', container=set(), State=State_Machines_StateMachine()), StateVertex=State_Machines_Transition()) == None


from python_code import State_Machines_CompositeState
from python_code import State_Machines_StateMachine
from python_code import State_Machines_StubState
from python_code import State_Machines_Transition

def test_State_Machines_StubState___init__():
    assert State_Machines_StubState.__init__(State_Machines_StubState('\x00\x00', StateVertex53=State_Machines_Transition(), StateVertex59=State_Machines_CompositeState('', container=set(), State=State_Machines_StateMachine()), StateVertex=State_Machines_Transition()), '', StateVertex53=State_Machines_Transition(), StateVertex59=State_Machines_CompositeState('', container=set(), State=State_Machines_StateMachine()), StateVertex=State_Machines_Transition()) == None


from python_code import State_Machines_CompositeState
from python_code import State_Machines_StateMachine
from python_code import State_Machines_SynchState
from python_code import State_Machines_Transition

def test_State_Machines_SynchState___init__():
    assert State_Machines_SynchState.__init__(State_Machines_SynchState('\x00\x00', StateVertex53=State_Machines_Transition(), StateVertex59=State_Machines_CompositeState('', container=set(), State=State_Machines_StateMachine()), StateVertex=State_Machines_Transition()), '', StateVertex53=State_Machines_Transition(), StateVertex59=State_Machines_CompositeState('', container=set(), State=State_Machines_StateMachine()), StateVertex=State_Machines_Transition()) == None

