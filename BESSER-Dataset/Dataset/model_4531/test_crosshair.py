from python_code import drone_NamedElement

def test_drone_NamedElement___init__():
    assert drone_NamedElement.__init__(drone_NamedElement(''), '') == None


from python_code import drone_Action
from python_code import drone_Parameter

def test_drone_Parameter___init__():
    assert drone_Parameter.__init__(drone_Parameter('', '\x00', drone_Parameter=drone_Action()), '\x00\x00', '', drone_Parameter=drone_Action()) == None


from python_code import drone_Device
from python_code import drone_Property

def test_drone_Property___init__():
    assert drone_Property.__init__(drone_Property('', drone_Property=drone_Device()), '', drone_Property=drone_Device()) == None

