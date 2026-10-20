from python_code import turtlebotmission_Area
from python_code import turtlebotmission_TurtleBot

def test_turtlebotmission_Area___init__():
    assert turtlebotmission_Area.__init__(turtlebotmission_Area(0, 0, turtlebotmission_Area=turtlebotmission_TurtleBot()), 0, 0, turtlebotmission_Area=turtlebotmission_TurtleBot()) == None


from python_code import turtlebotmission_NamedElement

def test_turtlebotmission_NamedElement___init__():
    assert turtlebotmission_NamedElement.__init__(turtlebotmission_NamedElement(''), '') == None


from python_code import turtlebotmission_LineTask
from python_code import turtlebotmission_ShortestPathTask
from python_code import turtlebotmission_TurtleBot
from python_code import turtlebotmission_WayPoint

def test_turtlebotmission_WayPoint___init__():
    assert turtlebotmission_WayPoint.__init__(turtlebotmission_WayPoint(0, 0, turtlebotmission_WayPoint=turtlebotmission_TurtleBot(), turtlebotmission_WayPoint7=turtlebotmission_TurtleBot(), turtlebotmission_WayPoint11=set(), turtlebotmission_WayPoint16=turtlebotmission_LineTask(), turtlebotmission_WayPoint18=turtlebotmission_ShortestPathTask()), 0, 0, turtlebotmission_WayPoint=turtlebotmission_TurtleBot(), turtlebotmission_WayPoint7=turtlebotmission_TurtleBot(), turtlebotmission_WayPoint11=set(), turtlebotmission_WayPoint16=turtlebotmission_LineTask(), turtlebotmission_WayPoint18=turtlebotmission_ShortestPathTask()) == None

