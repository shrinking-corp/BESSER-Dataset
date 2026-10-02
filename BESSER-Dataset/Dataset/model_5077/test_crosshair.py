from python_code import CarRental2_Check

def test_CarRental2_Check___init__():
    assert CarRental2_Check.__init__(CarRental2_Check(''), '') == None

from python_code import CarRental2_Person

def test_CarRental2_Person___init__():
    assert CarRental2_Person.__init__(CarRental2_Person('\x00\x00', '', 0, True), '', '', 0, False) == None

def test_CarRental2_Person_fullname():
    assert CarRental2_Person.fullname(CarRental2_Person('', '\x00', 0, False)) == None

from python_code import CarRental2_ServiceDepot

def test_CarRental2_ServiceDepot___init__():
    assert CarRental2_ServiceDepot.__init__(CarRental2_ServiceDepot(''), '') == None
