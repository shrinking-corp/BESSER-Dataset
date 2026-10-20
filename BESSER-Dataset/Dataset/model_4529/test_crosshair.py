from python_code import behaviour_Choice
from python_code import behaviour_Move

def test_behaviour_Choice___init__():
    assert behaviour_Choice.__init__(behaviour_Choice('', behaviour_Choice=behaviour_Move()), '', behaviour_Choice=behaviour_Move()) == None


from python_code import behaviour_DeviceAction

def test_behaviour_DeviceAction___init__():
    assert behaviour_DeviceAction.__init__(behaviour_DeviceAction('', behaviour_DeviceAction=set()), '', behaviour_DeviceAction=set()) == None


from python_code import behaviour_Feedback

def test_behaviour_Feedback___init__():
    assert behaviour_Feedback.__init__(behaviour_Feedback('', behaviour_Feedback=set()), '', behaviour_Feedback=set()) == None


from python_code import behaviour_HeadTo

def test_behaviour_HeadTo___init__():
    assert behaviour_HeadTo.__init__(behaviour_HeadTo(0.0), 0.0) == None


from python_code import behaviour_Hover

def test_behaviour_Hover___init__():
    assert behaviour_Hover.__init__(behaviour_Hover(0.0), 0.0) == None


from python_code import behaviour_NamedElement

def test_behaviour_NamedElement___init__():
    assert behaviour_NamedElement.__init__(behaviour_NamedElement(''), '') == None


from python_code import behaviour_TakeOff

def test_behaviour_TakeOff___init__():
    assert behaviour_TakeOff.__init__(behaviour_TakeOff(0.0), 0.0) == None

