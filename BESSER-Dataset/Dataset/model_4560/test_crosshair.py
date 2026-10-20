from python_code import platoon_ForwardCommand

def test_platoon_ForwardCommand___init__():
    assert platoon_ForwardCommand.__init__(platoon_ForwardCommand(0), 0) == None


from python_code import platoon_HeadwayConstraint

def test_platoon_HeadwayConstraint___init__():
    assert platoon_HeadwayConstraint.__init__(platoon_HeadwayConstraint(0, 0), 0, 0) == None


from python_code import platoon_LeadingVehicle
from python_code import platoon_Route
from python_code import platoon_World

def test_platoon_Route___init__():
    assert platoon_Route.__init__(platoon_Route('', platoon_Route=set(), platoon_Route8=platoon_LeadingVehicle(), platoon_Route13=platoon_World()), '', platoon_Route=set(), platoon_Route8=platoon_LeadingVehicle(), platoon_Route13=platoon_World()) == None


from python_code import platoon_TurnCommand

def test_platoon_TurnCommand___init__():
    assert platoon_TurnCommand.__init__(platoon_TurnCommand(''), '') == None


from python_code import platoon_FollowVehicle
from python_code import platoon_Vehicle

def test_platoon_Vehicle___init__():
    assert platoon_Vehicle.__init__(platoon_Vehicle('', platoon_Vehicle=platoon_FollowVehicle()), '', platoon_Vehicle=platoon_FollowVehicle()) == None

