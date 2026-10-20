from python_code import Statecharts_BooleanExpression

def test_Statecharts_BooleanExpression___init__():
    assert Statecharts_BooleanExpression.__init__(Statecharts_BooleanExpression(''), '') == None


from python_code import Statecharts_CompositeState
from python_code import Statecharts_Event
from python_code import Statecharts_StateMachine
from python_code import Statecharts_Transition

def test_Statecharts_CompositeState___init__():
    assert Statecharts_CompositeState.__init__(Statecharts_CompositeState('', sv_container=set(), State29=Statecharts_Event(), State10=Statecharts_Transition(), State=Statecharts_StateMachine()), '', sv_container=set(), State29=Statecharts_Event(), State10=Statecharts_Transition(), State=Statecharts_StateMachine()) == None

