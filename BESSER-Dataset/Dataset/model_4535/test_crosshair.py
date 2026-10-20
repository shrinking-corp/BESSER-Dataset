from python_code import mission_Mission
from python_code import mission_Swarm

def test_mission_Mission___init__():
    assert mission_Mission.__init__(mission_Mission('', mission_Mission=set(), mission_Mission2=set(), mission_Mission4=mission_Swarm()), '', mission_Mission=set(), mission_Mission2=set(), mission_Mission4=mission_Swarm()) == None


from python_code import mission_NamedElement

def test_mission_NamedElement___init__():
    assert mission_NamedElement.__init__(mission_NamedElement(''), '') == None

