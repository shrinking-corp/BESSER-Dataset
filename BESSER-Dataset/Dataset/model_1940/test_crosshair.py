from python_code import Flights_FlightObject

def test_Flights_FlightObject___init__():
    assert Flights_FlightObject.__init__(Flights_FlightObject(''), '') == None


from python_code import Flights_Person
from python_code import Flights_Persons
from python_code import Flights_Travel

def test_Flights_Person___init__():
    assert Flights_Person.__init__(Flights_Person('', Person=Flights_Travel(), Flights_Person=Flights_Persons(), person=set()), '', Person=Flights_Travel(), Flights_Person=Flights_Persons(), person=set()) == None

