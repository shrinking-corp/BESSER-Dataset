from python_code import uisut_UISUTElement

def test_uisut_UISUTElement___init__():
    assert uisut_UISUTElement.__init__(uisut_UISUTElement('', '', '\x00\x00'), '', '', '') == None


from python_code import uisut_AbstractState
from python_code import uisut_Action
from python_code import uisut_UICondition
from python_code import uisut_UIStatemachine
from python_code import uisut_UITransition
from python_code import uisut_UITrigger

def test_uisut_UITransition___init__():
    assert uisut_UITransition.__init__(uisut_UITransition('', '', '', '', uisut_UITransition24=uisut_Action(), uisut_UITransition26=set(), uisut_UITransition=uisut_UIStatemachine(), itsInTransition=uisut_AbstractState(), itsOutTransition=uisut_AbstractState(), uisut_UITransition20=uisut_UITrigger(), uisut_UITransition22=uisut_UICondition(), UITransition=uisut_AbstractState(), UITransition36=uisut_AbstractState()), '', '', '', '', uisut_UITransition24=uisut_Action(), uisut_UITransition26=set(), uisut_UITransition=uisut_UIStatemachine(), itsInTransition=uisut_AbstractState(), itsOutTransition=uisut_AbstractState(), uisut_UITransition20=uisut_UITrigger(), uisut_UITransition22=uisut_UICondition(), UITransition=uisut_AbstractState(), UITransition36=uisut_AbstractState()) == None

