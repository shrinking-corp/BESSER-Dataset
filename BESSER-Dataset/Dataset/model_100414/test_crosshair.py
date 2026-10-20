from python_code import state_Event
from python_code import state_Trigger

def test_state_Event___init__():
    assert state_Event.__init__(state_Event('', state_Event=state_Trigger()), '', state_Event=state_Trigger()) == None


from python_code import state_NamedElement
from python_code import state_StateModel

def test_state_NamedElement___init__():
    assert state_NamedElement.__init__(state_NamedElement('', '\x00', state_NamedElement=state_StateModel()), '\x00\x00', '', state_NamedElement=state_StateModel()) == None


from python_code import state_Constraint
from python_code import state_OpaqueExpression

def test_state_OpaqueExpression___init__():
    assert state_OpaqueExpression.__init__(state_OpaqueExpression('', state_OpaqueExpression=state_Constraint()), '', state_OpaqueExpression=state_Constraint()) == None


from python_code import state_PseudoState

def test_state_PseudoState___init__():
    assert state_PseudoState.__init__(state_PseudoState(''), '') == None

