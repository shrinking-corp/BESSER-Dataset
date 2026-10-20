from python_code import xDrone_BackWall
from python_code import xDrone_Walls

def test_xDrone_BackWall___init__():
    assert xDrone_BackWall.__init__(xDrone_BackWall('', xDrone_BackWall=xDrone_Walls()), '', xDrone_BackWall=xDrone_Walls()) == None


from python_code import xDrone_Backward

def test_xDrone_Backward___init__():
    assert xDrone_Backward.__init__(xDrone_Backward(''), '') == None


from python_code import xDrone_Down

def test_xDrone_Down___init__():
    assert xDrone_Down.__init__(xDrone_Down(''), '') == None


from python_code import xDrone_Drone
from python_code import xDrone_Environment
from python_code import xDrone_Position

def test_xDrone_Drone___init__():
    assert xDrone_Drone.__init__(xDrone_Drone('', xDrone_Drone=xDrone_Environment(), xDrone_Drone14=xDrone_Position()), '', xDrone_Drone=xDrone_Environment(), xDrone_Drone14=xDrone_Position()) == None


from python_code import xDrone_Fly
from python_code import xDrone_Main

def test_xDrone_Fly___init__():
    assert xDrone_Fly.__init__(xDrone_Fly('\x00\x00', '', xDrone_Fly=xDrone_Main(), xDrone_Fly6=set()), '', '', xDrone_Fly=xDrone_Main(), xDrone_Fly6=set()) == None


from python_code import xDrone_Forward

def test_xDrone_Forward___init__():
    assert xDrone_Forward.__init__(xDrone_Forward(''), '') == None


from python_code import xDrone_FrontWall
from python_code import xDrone_Walls

def test_xDrone_FrontWall___init__():
    assert xDrone_FrontWall.__init__(xDrone_FrontWall('', xDrone_FrontWall=xDrone_Walls()), '', xDrone_FrontWall=xDrone_Walls()) == None


from python_code import xDrone_GoTo

def test_xDrone_GoTo___init__():
    assert xDrone_GoTo.__init__(xDrone_GoTo(''), '') == None


from python_code import xDrone_Left

def test_xDrone_Left___init__():
    assert xDrone_Left.__init__(xDrone_Left(''), '') == None


from python_code import xDrone_LeftWall
from python_code import xDrone_Walls

def test_xDrone_LeftWall___init__():
    assert xDrone_LeftWall.__init__(xDrone_LeftWall('', xDrone_LeftWall=xDrone_Walls()), '', xDrone_LeftWall=xDrone_Walls()) == None


from python_code import xDrone_Right

def test_xDrone_Right___init__():
    assert xDrone_Right.__init__(xDrone_Right(''), '') == None


from python_code import xDrone_RightWall
from python_code import xDrone_Walls

def test_xDrone_RightWall___init__():
    assert xDrone_RightWall.__init__(xDrone_RightWall('', xDrone_RightWall=xDrone_Walls()), '', xDrone_RightWall=xDrone_Walls()) == None


from python_code import xDrone_RotateL

def test_xDrone_RotateL___init__():
    assert xDrone_RotateL.__init__(xDrone_RotateL(''), '') == None


from python_code import xDrone_RotateR

def test_xDrone_RotateR___init__():
    assert xDrone_RotateR.__init__(xDrone_RotateR(''), '') == None


from python_code import xDrone_Up

def test_xDrone_Up___init__():
    assert xDrone_Up.__init__(xDrone_Up(''), '') == None


from python_code import xDrone_UpWall
from python_code import xDrone_Walls

def test_xDrone_UpWall___init__():
    assert xDrone_UpWall.__init__(xDrone_UpWall('', xDrone_UpWall=xDrone_Walls()), '', xDrone_UpWall=xDrone_Walls()) == None


from python_code import xDrone_Origin
from python_code import xDrone_Position
from python_code import xDrone_Size
from python_code import xDrone_Vector

def test_xDrone_Vector___init__():
    assert xDrone_Vector.__init__(xDrone_Vector('', '', '\x00\x00', xDrone_Vector=xDrone_Origin(), xDrone_Vector25=xDrone_Size(), xDrone_Vector28=xDrone_Position()), '', '', '', xDrone_Vector=xDrone_Origin(), xDrone_Vector25=xDrone_Size(), xDrone_Vector28=xDrone_Position()) == None


from python_code import xDrone_Wait

def test_xDrone_Wait___init__():
    assert xDrone_Wait.__init__(xDrone_Wait(''), '') == None

