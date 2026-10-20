from python_code import dronesStructure_CooperativeAction
from python_code import dronesStructure_DronesStructure
from python_code import dronesStructure_Role
from python_code import dronesStructure_Task

def test_dronesStructure_CooperativeAction___init__():
    assert dronesStructure_CooperativeAction.__init__(dronesStructure_CooperativeAction(0.0, 0.0, dronesStructure_CooperativeAction=dronesStructure_DronesStructure(), cooperativeAction=set(), CooperativeAction=dronesStructure_Role(), dronesStructure_CooperativeAction50=dronesStructure_Task()), 0.0, 0.0, dronesStructure_CooperativeAction=dronesStructure_DronesStructure(), cooperativeAction=set(), CooperativeAction=dronesStructure_Role(), dronesStructure_CooperativeAction50=dronesStructure_Task()) == None


from python_code import dronesStructure_NamedElement

def test_dronesStructure_NamedElement___init__():
    assert dronesStructure_NamedElement.__init__(dronesStructure_NamedElement(''), '') == None


from python_code import dronesStructure_AABB
from python_code import dronesStructure_Drone
from python_code import dronesStructure_Position

def test_dronesStructure_Position___init__():
    assert dronesStructure_Position.__init__(dronesStructure_Position(0.0, 0.0, 0.0, dronesStructure_Position42=dronesStructure_AABB(), dronesStructure_Position=dronesStructure_Drone()), 0.0, 0.0, 0.0, dronesStructure_Position42=dronesStructure_AABB(), dronesStructure_Position=dronesStructure_Drone()) == None


from python_code import dronesStructure_Capability
from python_code import dronesStructure_RequiredCapability
from python_code import dronesStructure_Role

def test_dronesStructure_RequiredCapability___init__():
    assert dronesStructure_RequiredCapability.__init__(dronesStructure_RequiredCapability(0.0, RequiredCapability=dronesStructure_Role(), dronesStructure_RequiredCapability=dronesStructure_Capability(), requiredCapabilities=dronesStructure_Role()), 0.0, RequiredCapability=dronesStructure_Role(), dronesStructure_RequiredCapability=dronesStructure_Capability(), requiredCapabilities=dronesStructure_Role()) == None


from python_code import dronesStructure_DronesStructure
from python_code import dronesStructure_Scenario
from python_code import dronesStructure_ScenarioBounds

def test_dronesStructure_Scenario___init__():
    assert dronesStructure_Scenario.__init__(dronesStructure_Scenario(0.0, float('inf'), dronesStructure_Scenario=dronesStructure_DronesStructure(), dronesStructure_Scenario8=set(), dronesStructure_Scenario10=dronesStructure_ScenarioBounds(), dronesStructure_Scenario12=set(), dronesStructure_Scenario14=set(), dronesStructure_Scenario16=set()), 0.0, 0.0, dronesStructure_Scenario=dronesStructure_DronesStructure(), dronesStructure_Scenario8=set(), dronesStructure_Scenario10=dronesStructure_ScenarioBounds(), dronesStructure_Scenario12=set(), dronesStructure_Scenario14=set(), dronesStructure_Scenario16=set()) == None

