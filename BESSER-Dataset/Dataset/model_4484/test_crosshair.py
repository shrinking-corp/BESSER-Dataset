from python_code import behaviour_Choice
from python_code import behaviour_Condition
from python_code import behaviour_FieldObject
from python_code import behaviour_While

def test_behaviour_Condition___init__():
    assert behaviour_Condition.__init__(behaviour_Condition('', '', '\x00\x00', behaviour_Condition16=behaviour_FieldObject(), behaviour_Condition27=behaviour_While(), behaviour_Condition=behaviour_Choice()), '', '', '', behaviour_Condition16=behaviour_FieldObject(), behaviour_Condition27=behaviour_While(), behaviour_Condition=behaviour_Choice()) == None


from python_code import behaviour_DroneBehaviour

def test_behaviour_DroneBehaviour___init__():
    assert behaviour_DroneBehaviour.__init__(behaviour_DroneBehaviour(False, behaviour_DroneBehaviour2=set(), behaviour_DroneBehaviour=set()), False, behaviour_DroneBehaviour2=set(), behaviour_DroneBehaviour=set()) == None


from python_code import behaviour_NamedElement

def test_behaviour_NamedElement___init__():
    assert behaviour_NamedElement.__init__(behaviour_NamedElement(''), '') == None


from python_code import behaviour_Pause

def test_behaviour_Pause___init__():
    assert behaviour_Pause.__init__(behaviour_Pause(0.0), 0.0) == None


from python_code import behaviour_SendMessage

def test_behaviour_SendMessage___init__():
    assert behaviour_SendMessage.__init__(behaviour_SendMessage(''), '') == None


from python_code import behaviour_WaitForMessage

def test_behaviour_WaitForMessage___init__():
    assert behaviour_WaitForMessage.__init__(behaviour_WaitForMessage('', 0.0, behaviour_WaitForMessage=set(), behaviour_WaitForMessage21=set()), '', 0.0, behaviour_WaitForMessage=set(), behaviour_WaitForMessage21=set()) == None

