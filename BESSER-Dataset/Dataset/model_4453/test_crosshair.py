from python_code import rover_Angle
from python_code import rover_Compass
from python_code import rover_CompassTrigger
from python_code import rover_Rotate

def test_rover_Angle___init__():
    assert rover_Angle.__init__(rover_Angle('', rover_Angle=rover_Compass(), rover_Angle36=rover_Rotate(), rover_Angle58=rover_CompassTrigger()), '', rover_Angle=rover_Compass(), rover_Angle36=rover_Rotate(), rover_Angle58=rover_CompassTrigger()) == None


from python_code import rover_Distance
from python_code import rover_DistanceSensorTrigger
from python_code import rover_Length
from python_code import rover_Move
from python_code import rover_Position

def test_rover_Length___init__():
    assert rover_Length.__init__(rover_Length('', rover_Length32=rover_Move(), rover_Length=rover_Distance(), rover_Length66=rover_Position(), rover_Length69=rover_Position(), rover_Length53=rover_DistanceSensorTrigger()), '', rover_Length32=rover_Move(), rover_Length=rover_Distance(), rover_Length66=rover_Position(), rover_Length69=rover_Position(), rover_Length53=rover_DistanceSensorTrigger()) == None


from python_code import rover_Block
from python_code import rover_Repeat

def test_rover_Repeat___init__():
    assert rover_Repeat.__init__(rover_Repeat(0, rover_Repeat=rover_Block(), rover_Repeat38=set(), rover_Repeat41=set(), rover_Repeat44=set(), rover_Repeat47=set()), 0, rover_Repeat=rover_Block(), rover_Repeat38=set(), rover_Repeat41=set(), rover_Repeat44=set(), rover_Repeat47=set()) == None


from python_code import rover_SingleQuantity

def test_rover_SingleQuantity___init__():
    assert rover_SingleQuantity.__init__(rover_SingleQuantity(0.0), 0.0) == None


from python_code import rover_Time
from python_code import rover_Wait

def test_rover_Time___init__():
    assert rover_Time.__init__(rover_Time('', rover_Time=rover_Wait()), '', rover_Time=rover_Wait()) == None


from python_code import rover_TriggeredTransition

def test_rover_TriggeredTransition___init__():
    assert rover_TriggeredTransition.__init__(rover_TriggeredTransition(''), '') == None


from python_code import rover_Move
from python_code import rover_Velocity

def test_rover_Velocity___init__():
    assert rover_Velocity.__init__(rover_Velocity('', rover_Velocity=rover_Move()), '', rover_Velocity=rover_Move()) == None

