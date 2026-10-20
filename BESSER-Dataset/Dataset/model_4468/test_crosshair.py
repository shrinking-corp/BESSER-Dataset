from python_code import polybot_modelling_language_MoveStraight

def test_polybot_modelling_language_MoveStraight___init__():
    assert polybot_modelling_language_MoveStraight.__init__(polybot_modelling_language_MoveStraight(0), 0) == None


from python_code import polybot_modelling_language_Robot
from python_code import polybot_modelling_language_Scene

def test_polybot_modelling_language_Robot___init__():
    assert polybot_modelling_language_Robot.__init__(polybot_modelling_language_Robot(False, polybot_modelling_language_Robot2=set(), polybot_modelling_language_Robot=polybot_modelling_language_Scene()), False, polybot_modelling_language_Robot2=set(), polybot_modelling_language_Robot=polybot_modelling_language_Scene()) == None


from python_code import polybot_modelling_language_Turn

def test_polybot_modelling_language_Turn___init__():
    assert polybot_modelling_language_Turn.__init__(polybot_modelling_language_Turn(0), 0) == None

