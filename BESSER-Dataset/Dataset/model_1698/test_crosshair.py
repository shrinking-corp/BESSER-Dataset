from python_code import complworld_Mars
from python_code import complworld_Satellite

def test_complworld_Satellite___init__():
    assert complworld_Satellite.__init__(complworld_Satellite('', complworld_Satellite=complworld_Mars()), '', complworld_Satellite=complworld_Mars()) == None


from python_code import complworld_Thing
from python_code import complworld_World

def test_complworld_Thing___init__():
    assert complworld_Thing.__init__(complworld_Thing('', complworld_Thing=complworld_World()), '', complworld_Thing=complworld_World()) == None

