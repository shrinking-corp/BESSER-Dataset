from python_code import CarRentalModel_Agency
from python_code import CarRentalModel_CarRental

def test_CarRentalModel_Agency___init__():
    assert CarRentalModel_Agency.__init__(CarRentalModel_Agency('', '', 0, CarRentalModel_Agency=CarRentalModel_CarRental(), CarRentalModel_Agency7=CarRentalModel_CarRental()), '\x00', '', 0, CarRentalModel_Agency=CarRentalModel_CarRental(), CarRentalModel_Agency7=CarRentalModel_CarRental()) == None


from python_code import CarRentalModel_Automobile

def test_CarRentalModel_Automobile___init__():
    assert CarRentalModel_Automobile.__init__(CarRentalModel_Automobile(True), False) == None


from python_code import CarRentalModel_Motorcycle

def test_CarRentalModel_Motorcycle___init__():
    assert CarRentalModel_Motorcycle.__init__(CarRentalModel_Motorcycle(0), 0) == None


from python_code import CarRentalModel_VipCustomer

def test_CarRentalModel_VipCustomer___init__():
    assert CarRentalModel_VipCustomer.__init__(CarRentalModel_VipCustomer(0.0), 0.0) == None

