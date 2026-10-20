from python_code import Concept_Segment

def test_Concept_Segment___init__():
    assert Concept_Segment.__init__(Concept_Segment(0), 0) == None


from python_code import Concept_Route
from python_code import Concept_Signal

def test_Concept_Signal___init__():
    assert Concept_Signal.__init__(Concept_Signal('', Concept_Signal=Concept_Route(), Concept_Signal9=Concept_Route()), '', Concept_Signal=Concept_Route(), Concept_Signal9=Concept_Route()) == None

