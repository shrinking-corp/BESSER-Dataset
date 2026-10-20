from python_code import CarRental_Check

def test_CarRental_Check___init__():
    assert CarRental_Check.__init__(CarRental_Check(''), '') == None


from python_code import CarRental_Person

def test_CarRental_Person___init__():
    assert CarRental_Person.__init__(CarRental_Person('\x00\x00', '', 0, True), '', '', 0, False) == None

def test_CarRental_Person_email():
    assert CarRental_Person.email(CarRental_Person('', '\x00', 0, False)) == None

def test_CarRental_Person_updateAge():
    assert CarRental_Person.updateAge(CarRental_Person('', '\x00', 0, False), 0) == None


from python_code import CarRental_ServiceDepot

def test_CarRental_ServiceDepot___init__():
    assert CarRental_ServiceDepot.__init__(CarRental_ServiceDepot(''), '') == None

