from python_code import petrinet_ArcEntrant
from python_code import petrinet_ArcSortant
from python_code import petrinet_Place

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place(0, petrinet_Place=petrinet_ArcSortant(), petrinet_Place5=petrinet_ArcEntrant()), 0, petrinet_Place=petrinet_ArcSortant(), petrinet_Place5=petrinet_ArcEntrant()) == None


from python_code import petrinet_Reseau

def test_petrinet_Reseau___init__():
    assert petrinet_Reseau.__init__(petrinet_Reseau('', petrinet_Reseau=set(), petrinet_Reseau10=set()), '', petrinet_Reseau=set(), petrinet_Reseau10=set()) == None

