from python_code import Entity_Entity
from python_code import Entity_System

def test_Entity_Entity___init__():
    assert Entity_Entity.__init__(Entity_Entity('', '\x00', Entity=Entity_System(), entity=Entity_System()), '\x00\x00', '', Entity=Entity_System(), entity=Entity_System()) == None

