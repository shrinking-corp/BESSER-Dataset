from python_code import roverml_Angle
from python_code import roverml_Rotate

def test_roverml_Angle___init__():
    assert roverml_Angle.__init__(roverml_Angle('', roverml_Angle=roverml_Rotate()), '', roverml_Angle=roverml_Rotate()) == None


from python_code import roverml_Component
from python_code import roverml_Rover

def test_roverml_Component___init__():
    assert roverml_Component.__init__(roverml_Component('', roverml_Component=roverml_Rover()), '', roverml_Component=roverml_Rover()) == None


from python_code import roverml_Length
from python_code import roverml_Move
from python_code import roverml_Position

def test_roverml_Length___init__():
    assert roverml_Length.__init__(roverml_Length('', roverml_Length=roverml_Move(), roverml_Length33=roverml_Position(), roverml_Length36=roverml_Position()), '', roverml_Length=roverml_Move(), roverml_Length33=roverml_Position(), roverml_Length36=roverml_Position()) == None


from python_code import roverml_NamedElement

def test_roverml_NamedElement___init__():
    assert roverml_NamedElement.__init__(roverml_NamedElement(''), '') == None


from python_code import roverml_Repeat

def test_roverml_Repeat___init__():
    assert roverml_Repeat.__init__(roverml_Repeat(0), 0) == None


from python_code import roverml_SetLightColor

def test_roverml_SetLightColor___init__():
    assert roverml_SetLightColor.__init__(roverml_SetLightColor('', roverml_SetLightColor=set()), '', roverml_SetLightColor=set()) == None


from python_code import roverml_SingleQuantity

def test_roverml_SingleQuantity___init__():
    assert roverml_SingleQuantity.__init__(roverml_SingleQuantity(0.0), 0.0) == None


from python_code import roverml_Time
from python_code import roverml_Wait

def test_roverml_Time___init__():
    assert roverml_Time.__init__(roverml_Time('', roverml_Time=roverml_Wait()), '', roverml_Time=roverml_Wait()) == None


from python_code import roverml_TriggeredTransition

def test_roverml_TriggeredTransition___init__():
    assert roverml_TriggeredTransition.__init__(roverml_TriggeredTransition(''), '') == None


from python_code import roverml_Move
from python_code import roverml_Velocity

def test_roverml_Velocity___init__():
    assert roverml_Velocity.__init__(roverml_Velocity('', roverml_Velocity=roverml_Move()), '', roverml_Velocity=roverml_Move()) == None

