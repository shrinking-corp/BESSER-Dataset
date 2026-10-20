from python_code import rover_Component
from python_code import rover_Rover

def test_rover_Component___init__():
    assert rover_Component.__init__(rover_Component('', rover_Component=rover_Rover()), '', rover_Component=rover_Rover()) == None


from python_code import rover_DistanceSensor

def test_rover_DistanceSensor___init__():
    assert rover_DistanceSensor.__init__(rover_DistanceSensor(0.0), 0.0) == None


from python_code import rover_GPS

def test_rover_GPS___init__():
    assert rover_GPS.__init__(rover_GPS(0.0), 0.0) == None


from python_code import rover_Command
from python_code import rover_Move

def test_rover_Move___init__():
    assert rover_Move.__init__(rover_Move(0, 0, rover_Move=rover_Command()), 0, 0, rover_Move=rover_Command()) == None


from python_code import rover_Command
from python_code import rover_Repeate

def test_rover_Repeate___init__():
    assert rover_Repeate.__init__(rover_Repeate(0, rover_Repeate=rover_Command()), 0, rover_Repeate=rover_Command()) == None


from python_code import rover_Command
from python_code import rover_Rotate

def test_rover_Rotate___init__():
    assert rover_Rotate.__init__(rover_Rotate(0, rover_Rotate=rover_Command()), 0, rover_Rotate=rover_Command()) == None


from python_code import rover_Command
from python_code import rover_SetLightColor

def test_rover_SetLightColor___init__():
    assert rover_SetLightColor.__init__(rover_SetLightColor('', rover_SetLightColor=rover_Command()), '', rover_SetLightColor=rover_Command()) == None


from python_code import rover_Command
from python_code import rover_Wait

def test_rover_Wait___init__():
    assert rover_Wait.__init__(rover_Wait(0, rover_Wait=rover_Command()), 0, rover_Wait=rover_Command()) == None


from python_code import rover_directionFacing

def test_rover_directionFacing___init__():
    assert rover_directionFacing.__init__(rover_directionFacing(0.0), 0.0) == None

