from python_code import robot_Connection
from python_code import robot_Robot

def test_robot_Connection___init__():
    assert robot_Connection.__init__(robot_Connection('', 0, robot_Connection=robot_Robot()), '', 0, robot_Connection=robot_Robot()) == None


from python_code import robot_ControlStatement

def test_robot_ControlStatement___init__():
    assert robot_ControlStatement.__init__(robot_ControlStatement(0), 0) == None


from python_code import robot_NamedElement

def test_robot_NamedElement___init__():
    assert robot_NamedElement.__init__(robot_NamedElement(''), '') == None


from python_code import robot_PrintStatement

def test_robot_PrintStatement___init__():
    assert robot_PrintStatement.__init__(robot_PrintStatement(''), '') == None

