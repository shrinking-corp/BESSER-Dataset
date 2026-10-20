from python_code import platoon_Forward

def test_platoon_Forward___init__():
    assert platoon_Forward.__init__(platoon_Forward(0), 0) == None


from python_code import platoon_LeadVehicle
from python_code import platoon_Route
from python_code import platoon_World

def test_platoon_Route___init__():
    assert platoon_Route.__init__(platoon_Route('', platoon_Route15=set(), platoon_Route=platoon_World(), platoon_Route11=platoon_LeadVehicle()), '', platoon_Route15=set(), platoon_Route=platoon_World(), platoon_Route11=platoon_LeadVehicle()) == None


from python_code import platoon_FollowVehicle
from python_code import platoon_Vehicle

def test_platoon_Vehicle___init__():
    assert platoon_Vehicle.__init__(platoon_Vehicle('', platoon_Vehicle=platoon_FollowVehicle()), '', platoon_Vehicle=platoon_FollowVehicle()) == None


from python_code import platoon_headway

def test_platoon_headway___init__():
    assert platoon_headway.__init__(platoon_headway(0, 0), 0, 0) == None

