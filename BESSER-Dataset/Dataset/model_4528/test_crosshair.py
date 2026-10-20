from python_code import platoon_Constraints
from python_code import platoon_Model

def test_platoon_Constraints___init__():
    assert platoon_Constraints.__init__(platoon_Constraints(0, 0, platoon_Constraints=platoon_Model()), 0, 0, platoon_Constraints=platoon_Model()) == None


from python_code import platoon_Forward

def test_platoon_Forward___init__():
    assert platoon_Forward.__init__(platoon_Forward(0), 0) == None


from python_code import platoon_LV
from python_code import platoon_Model
from python_code import platoon_Route

def test_platoon_Route___init__():
    assert platoon_Route.__init__(platoon_Route('', platoon_Route=platoon_Model(), platoon_Route15=set(), platoon_Route13=platoon_LV()), '', platoon_Route=platoon_Model(), platoon_Route15=set(), platoon_Route13=platoon_LV()) == None


from python_code import platoon_FV
from python_code import platoon_Vehicle

def test_platoon_Vehicle___init__():
    assert platoon_Vehicle.__init__(platoon_Vehicle('', platoon_Vehicle=platoon_FV()), '', platoon_Vehicle=platoon_FV()) == None

