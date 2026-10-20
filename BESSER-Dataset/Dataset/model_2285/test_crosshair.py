from python_code import UniverityU_Courses
from python_code import aPerson

def test_UniverityU_Courses___init__():
    assert UniverityU_Courses.__init__(UniverityU_Courses('', 0, '', UniverityU_Courses=set(), UniverityU_Courses2=aPerson(), UniverityU_Courses4=set()), '', 0, '', UniverityU_Courses=set(), UniverityU_Courses2=aPerson(), UniverityU_Courses4=set()) == None


from python_code import UniverityU_Person
from python_code import aPerson

def test_UniverityU_Person___init__():
    assert UniverityU_Person.__init__(UniverityU_Person('', '\x00', UniverityU_Person=aPerson()), '\x00\x00', '', UniverityU_Person=aPerson()) == None


from python_code import UniverityU_uncertainty_UData

def test_UniverityU_uncertainty_UData___init__():
    assert UniverityU_uncertainty_UData.__init__(UniverityU_uncertainty_UData('', '\x00'), '\x00\x00', '') == None

