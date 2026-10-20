from python_code import Abstract_Component

def test_Abstract_Component___init__():
    assert Abstract_Component.__init__(Abstract_Component(''), '') == None


from python_code import Abstract_Door

def test_Abstract_Door___init__():
    assert Abstract_Door.__init__(Abstract_Door('', '', '\x00\x00'), '', '', '') == None


from python_code import Break_in

def test_Break_in___init__():
    assert Break_in.__init__(Break_in(True), False) == None


from python_code import Coil_Spring_Cables

def test_Coil_Spring_Cables___init__():
    assert Coil_Spring_Cables.__init__(Coil_Spring_Cables(''), '') == None


from python_code import Controlling_Circuit

def test_Controlling_Circuit___init__():
    assert Controlling_Circuit.__init__(Controlling_Circuit('', '\x00'), '\x00\x00', '') == None


from python_code import Door_Status

def test_Door_Status___init__():
    assert Door_Status.__init__(Door_Status(False, '\x00'), False, '\x00') == None


from python_code import External_Component

def test_External_Component___init__():
    assert External_Component.__init__(External_Component(True), False) == None


from python_code import In_house_Component

def test_In_house_Component___init__():
    assert In_house_Component.__init__(In_house_Component('', '\x00'), '\x00\x00', '') == None


from python_code import Light_Motion

def test_Light_Motion___init__():
    assert Light_Motion.__init__(Light_Motion(True), False) == None


from python_code import Locks_Handles

def test_Locks_Handles___init__():
    assert Locks_Handles.__init__(Locks_Handles('', '\x00'), '\x00\x00', '') == None


from python_code import Motor

def test_Motor___init__():
    assert Motor.__init__(Motor('', '\x00'), '\x00\x00', '') == None


from python_code import Remote_Controller_Interface

def test_Remote_Controller_Interface___init__():
    assert Remote_Controller_Interface.__init__(Remote_Controller_Interface('', '\x00'), '\x00\x00', '') == None


from python_code import Rollers_Rails

def test_Rollers_Rails___init__():
    assert Rollers_Rails.__init__(Rollers_Rails(''), '') == None


from python_code import Rolling

def test_Rolling___init__():
    assert Rolling.__init__(Rolling(''), '') == None


from python_code import Swing_out

def test_Swing_out___init__():
    assert Swing_out.__init__(Swing_out(''), '') == None

