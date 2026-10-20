from python_code import robotDSL_Missions

def test_robotDSL_Missions___init__():
    assert robotDSL_Missions.__init__(robotDSL_Missions('', robotDSL_Missions=set()), '', robotDSL_Missions=set()) == None


from python_code import robotDSL_Goal
from python_code import robotDSL_Time

def test_robotDSL_Time___init__():
    assert robotDSL_Time.__init__(robotDSL_Time(0, robotDSL_Time=robotDSL_Goal()), 0, robotDSL_Time=robotDSL_Goal()) == None

