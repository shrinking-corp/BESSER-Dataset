from python_code import CarRental2_Check
from python_code import CarRental2_TernaryRelationMaintenance

def test_CarRental2_Check___init__():
    assert CarRental2_Check.__init__(CarRental2_Check(0, toCheck=set(), Check=CarRental2_TernaryRelationMaintenance()), 0, toCheck=set(), Check=CarRental2_TernaryRelationMaintenance()) == None


from python_code import CarRental2_Person

def test_CarRental2_Person___init__():
    assert CarRental2_Person.__init__(CarRental2_Person(0, 0, 0, False), 0, 0, 0, True) == None

def test_CarRental2_Person_fullname():
    assert CarRental2_Person.fullname(CarRental2_Person(0, 0, 0, False), '') == None


from python_code import CarRental2_ServiceDepot
from python_code import CarRental2_TernaryRelationMaintenance

def test_CarRental2_ServiceDepot___init__():
    assert CarRental2_ServiceDepot.__init__(CarRental2_ServiceDepot(0, toServiceDepot=set(), ServiceDepot=CarRental2_TernaryRelationMaintenance()), 0, toServiceDepot=set(), ServiceDepot=CarRental2_TernaryRelationMaintenance()) == None

