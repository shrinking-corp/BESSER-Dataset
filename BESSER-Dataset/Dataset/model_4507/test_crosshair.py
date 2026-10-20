from python_code import smartHome_Duration
from python_code import smartHome_Rule

def test_smartHome_Duration___init__():
    assert smartHome_Duration.__init__(smartHome_Duration('', 0, smartHome_Duration=smartHome_Rule()), '', 0, smartHome_Duration=smartHome_Rule()) == None


from python_code import smartHome_Event
from python_code import smartHome_Rule

def test_smartHome_Event___init__():
    assert smartHome_Event.__init__(smartHome_Event('', smartHome_Event=smartHome_Rule()), '', smartHome_Event=smartHome_Rule()) == None


from python_code import smartHome_Location
from python_code import smartHome_SmartHome

def test_smartHome_Location___init__():
    assert smartHome_Location.__init__(smartHome_Location('', smartHome_Location=set(), smartHome_Location4=smartHome_SmartHome()), '', smartHome_Location=set(), smartHome_Location4=smartHome_SmartHome()) == None

