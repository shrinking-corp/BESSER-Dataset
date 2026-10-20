from python_code import trip_NamedElement
from python_code import trip_TripModel

def test_trip_NamedElement___init__():
    assert trip_NamedElement.__init__(trip_NamedElement('', trip_NamedElement=trip_TripModel()), '', trip_NamedElement=trip_TripModel()) == None


from python_code import trip_Trip
from python_code import trip_Vehicle

def test_trip_Vehicle___init__():
    assert trip_Vehicle.__init__(trip_Vehicle(0, trip_Vehicle=trip_Trip()), 0, trip_Vehicle=trip_Trip()) == None

