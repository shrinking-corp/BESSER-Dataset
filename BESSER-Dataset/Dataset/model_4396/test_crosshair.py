from python_code import arduino_Delay

def test_arduino_Delay___init__():
    assert arduino_Delay.__init__(arduino_Delay(''), '') == None

def test_arduino_Delay_execute():
    assert arduino_Delay.execute(arduino_Delay('')) == None


from python_code import arduino_NamedElement

def test_arduino_NamedElement___init__():
    assert arduino_NamedElement.__init__(arduino_NamedElement(''), '') == None


from python_code import arduino_PushButton

def test_arduino_PushButton___init__():
    assert arduino_PushButton.__init__(arduino_PushButton()) == None

def test_arduino_PushButton_release():
    assert arduino_PushButton.release(arduino_PushButton()) == None

def test_arduino_PushButton_press():
    assert arduino_PushButton.press(arduino_PushButton()) == None


from python_code import arduino_Led
from python_code import arduino_SetLed

def test_arduino_SetLed___init__():
    assert arduino_SetLed.__init__(arduino_SetLed(arduino_SetLed=arduino_Led()), arduino_SetLed=arduino_Led()) == None

def test_arduino_SetLed_execute():
    assert arduino_SetLed.execute(arduino_SetLed(arduino_SetLed=arduino_Led())) == None

