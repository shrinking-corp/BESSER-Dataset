from python_code import CarRental2_Person

def test_CarRental2_Person___init__():
    assert CarRental2_Person.__init__(CarRental2_Person('\x00\x00', 0, False, ''), '', 0, False, '') == None

def test_CarRental2_Person_fullname():
    assert CarRental2_Person.fullname(CarRental2_Person('', 0, False, '')) == None

