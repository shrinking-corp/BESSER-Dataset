from python_code import platoon_Constraints
from python_code import platoon_Root

def test_platoon_Constraints___init__():
    assert platoon_Constraints.__init__(platoon_Constraints(0, 0, platoon_Constraints=platoon_Root()), 0, 0, platoon_Constraints=platoon_Root()) == None


from python_code import platoon_Forward

def test_platoon_Forward___init__():
    assert platoon_Forward.__init__(platoon_Forward(0), 0) == None


from python_code import platoon_LeaderVehicle
from python_code import platoon_Root
from python_code import platoon_Route

def test_platoon_Route___init__():
    assert platoon_Route.__init__(platoon_Route('', platoon_Route=platoon_Root(), platoon_Route6=set(), platoon_Route15=platoon_LeaderVehicle()), '', platoon_Route=platoon_Root(), platoon_Route6=set(), platoon_Route15=platoon_LeaderVehicle()) == None


from python_code import platoon_FollowingVehicle
from python_code import platoon_Vehicle

def test_platoon_Vehicle___init__():
    assert platoon_Vehicle.__init__(platoon_Vehicle('', platoon_Vehicle=platoon_FollowingVehicle()), '', platoon_Vehicle=platoon_FollowingVehicle()) == None

