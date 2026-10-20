from python_code import Heater

def test_Heater___init__():
    assert Heater.__init__(Heater(True), False) == None


from python_code import Humidity_Sensor

def test_Humidity_Sensor___init__():
    assert Humidity_Sensor.__init__(Humidity_Sensor(0.0), 0.0) == None


from python_code import Cooking_System
from python_code import Ingredient_Box

def test_Ingredient_Box___init__():
    assert Ingredient_Box.__init__(Ingredient_Box(0, 0.0, home_Security_System9=Cooking_System()), 0, 0.0, home_Security_System9=Cooking_System()) == None


from python_code import SteamGenerator

def test_SteamGenerator___init__():
    assert SteamGenerator.__init__(SteamGenerator(True), False) == None


from python_code import Temperature_Sensor

def test_Temperature_Sensor___init__():
    assert Temperature_Sensor.__init__(Temperature_Sensor(0.0), 0.0) == None

