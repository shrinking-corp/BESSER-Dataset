from python_code import RDM_RDMElement

def test_RDM_RDMElement___init__():
    assert RDM_RDMElement.__init__(RDM_RDMElement('', 0), '', 0) == None


from python_code import RDM_RailwayDomainModel
from python_code import RDM_Route
from python_code import RDM_Station
from python_code import RDM_TrackElement
from python_code import RDM_Train

def test_RDM_Train___init__():
    assert RDM_Train.__init__(RDM_Train('\x00\x00', '', occupiedBy=set(), Train=RDM_TrackElement(), RDM_Train16=RDM_Station(), RDM_Train18=RDM_Station(), RDM_Train21=RDM_Route(), RDM_Train=RDM_RailwayDomainModel()), '', '', occupiedBy=set(), Train=RDM_TrackElement(), RDM_Train16=RDM_Station(), RDM_Train18=RDM_Station(), RDM_Train21=RDM_Route(), RDM_Train=RDM_RailwayDomainModel()) == None

