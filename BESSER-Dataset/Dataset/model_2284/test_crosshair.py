from python_code import Univerity_Courses
from python_code import aPerson

def test_Univerity_Courses___init__():
    assert Univerity_Courses.__init__(Univerity_Courses('', 0, '', Univerity_Courses=set(), Univerity_Courses2=aPerson(), Univerity_Courses4=set()), '', 0, '', Univerity_Courses=set(), Univerity_Courses2=aPerson(), Univerity_Courses4=set()) == None


from python_code import Univerity_Person
from python_code import aPerson

def test_Univerity_Person___init__():
    assert Univerity_Person.__init__(Univerity_Person('', '\x00', Univerity_Person=aPerson()), '\x00\x00', '', Univerity_Person=aPerson()) == None


from python_code import Univerity_uncertainty_UData

def test_Univerity_uncertainty_UData___init__():
    assert Univerity_uncertainty_UData.__init__(Univerity_uncertainty_UData('', '\x00'), '\x00\x00', '') == None

