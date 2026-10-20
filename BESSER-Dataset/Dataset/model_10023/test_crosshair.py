from python_code import EA_Model_CrashedVehicle
from python_code import EA_Model_RoadTrafficAccident
from python_code import EA_Model_RoadwayWithAccident
from python_code import EA_Model_Victim

def test_EA_Model_RoadTrafficAccident___init__():
    assert EA_Model_RoadTrafficAccident.__init__(EA_Model_RoadTrafficAccident(0, RoadTrafficAccident=EA_Model_CrashedVehicle(), RoadTrafficAccident8=EA_Model_RoadwayWithAccident(), accident=set(), accident4=set(), roadtrafficaccident=EA_Model_RoadwayWithAccident(), RoadTrafficAccident19=EA_Model_Victim()), 0, RoadTrafficAccident=EA_Model_CrashedVehicle(), RoadTrafficAccident8=EA_Model_RoadwayWithAccident(), accident=set(), accident4=set(), roadtrafficaccident=EA_Model_RoadwayWithAccident(), RoadTrafficAccident19=EA_Model_Victim()) == None

