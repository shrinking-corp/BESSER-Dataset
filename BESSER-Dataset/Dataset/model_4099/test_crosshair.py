from python_code import railway_RailwayContainer
from python_code import railway_RailwayElement

def test_railway_RailwayElement___init__():
    assert railway_RailwayElement.__init__(railway_RailwayElement(0, railway_RailwayElement=railway_RailwayContainer()), 0, railway_RailwayElement=railway_RailwayContainer()) == None


from python_code import railway_Segment

def test_railway_Segment___init__():
    assert railway_Segment.__init__(railway_Segment(0), 0) == None


from python_code import railway_RailwayContainer
from python_code import railway_Route
from python_code import railway_Semaphore

def test_railway_Semaphore___init__():
    assert railway_Semaphore.__init__(railway_Semaphore('', railway_Semaphore18=railway_RailwayContainer(), railway_Semaphore=railway_Route(), railway_Semaphore9=railway_Route()), '', railway_Semaphore18=railway_RailwayContainer(), railway_Semaphore=railway_Route(), railway_Semaphore9=railway_Route()) == None

