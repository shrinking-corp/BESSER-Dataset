from python_code import ConceptASE_Segment

def test_ConceptASE_Segment___init__():
    assert ConceptASE_Segment.__init__(ConceptASE_Segment(0, 0), 0, 0) == None


from python_code import ConceptASE_Route
from python_code import ConceptASE_Sensor
from python_code import ConceptASE_Trackelement

def test_ConceptASE_Sensor___init__():
    assert ConceptASE_Sensor.__init__(ConceptASE_Sensor(0, ConceptASE_Sensor=ConceptASE_Route(), Sensor=ConceptASE_Trackelement(), TrackElement_sensor=set()), 0, ConceptASE_Sensor=ConceptASE_Route(), Sensor=ConceptASE_Trackelement(), TrackElement_sensor=set()) == None


from python_code import ConceptASE_Route
from python_code import ConceptASE_Signal

def test_ConceptASE_Signal___init__():
    assert ConceptASE_Signal.__init__(ConceptASE_Signal('', ConceptASE_Signal9=ConceptASE_Route(), ConceptASE_Signal=ConceptASE_Route()), '', ConceptASE_Signal9=ConceptASE_Route(), ConceptASE_Signal=ConceptASE_Route()) == None

