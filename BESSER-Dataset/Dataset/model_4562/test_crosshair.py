from python_code import drones_MovableObject

def test_drones_MovableObject___init__():
    assert drones_MovableObject.__init__(drones_MovableObject(0.0), 0.0) == None


from python_code import drones_NamedElement

def test_drones_NamedElement___init__():
    assert drones_NamedElement.__init__(drones_NamedElement(''), '') == None


from python_code import drones_FieldObject
from python_code import drones_Parameter

def test_drones_Parameter___init__():
    assert drones_Parameter.__init__(drones_Parameter('', '\x00', drones_Parameter=drones_FieldObject()), '\x00\x00', '', drones_Parameter=drones_FieldObject()) == None


from python_code import drones_SizedElement

def test_drones_SizedElement___init__():
    assert drones_SizedElement.__init__(drones_SizedElement(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0) == None

