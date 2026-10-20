from python_code import Button
from python_code import ElevatorControl

def test_Button___init__():
    assert Button.__init__(Button(0, False, elevatorControl2=ElevatorControl()), 0, False, elevatorControl2=ElevatorControl()) == None


from python_code import Elevator
from python_code import ElevatorControl

def test_Elevator___init__():
    assert Elevator.__init__(Elevator(0, 0, 0, elevatorControl0=ElevatorControl()), 0, 0, 0, elevatorControl0=ElevatorControl()) == None

