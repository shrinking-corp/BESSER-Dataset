from python_code import iotw_ArduinoUNOR3

def test_iotw_ArduinoUNOR3___init__():
    assert iotw_ArduinoUNOR3.__init__(iotw_ArduinoUNOR3('', '', '', '', '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', '', ''), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '') == None


from python_code import iotw_BluetoothHC06

def test_iotw_BluetoothHC06___init__():
    assert iotw_BluetoothHC06.__init__(iotw_BluetoothHC06('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import iotw_Button

def test_iotw_Button___init__():
    assert iotw_Button.__init__(iotw_Button(''), '') == None


from python_code import iotw_Buzzer

def test_iotw_Buzzer___init__():
    assert iotw_Buzzer.__init__(iotw_Buzzer('\x00\x00', '', 0, 0), '', '', 0, 0) == None


from python_code import iotw_I2CLCD

def test_iotw_I2CLCD___init__():
    assert iotw_I2CLCD.__init__(iotw_I2CLCD('', '', '', '', ''), '', '', '', '', '') == None


from python_code import iotw_Keypad4x4

def test_iotw_Keypad4x4___init__():
    assert iotw_Keypad4x4.__init__(iotw_Keypad4x4('', 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''), '', 0, 0, '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '') == None

def test_iotw_Keypad4x4_getButton():
    assert iotw_Keypad4x4.getButton(iotw_Keypad4x4('', 0, 0, '', '', '', '', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00', '', '', ''), '') == None


from python_code import iotw_LED

def test_iotw_LED___init__():
    assert iotw_LED.__init__(iotw_LED('', '\x00'), '\x00\x00', '') == None


from python_code import iotw_StateComponent
from python_code import iotw_StateSchema

def test_iotw_StateComponent___init__():
    assert iotw_StateComponent.__init__(iotw_StateComponent('', iotw_StateComponent=iotw_StateSchema(), iotw_StateComponent8=set(), iotw_StateComponent11=set()), '', iotw_StateComponent=iotw_StateSchema(), iotw_StateComponent8=set(), iotw_StateComponent11=set()) == None


from python_code import iotw_StateFrame

def test_iotw_StateFrame___init__():
    assert iotw_StateFrame.__init__(iotw_StateFrame(''), '') == None


from python_code import iotw_WifiESP8266

def test_iotw_WifiESP8266___init__():
    assert iotw_WifiESP8266.__init__(iotw_WifiESP8266('', '', '\x00', '', '', '', '', '', '', '', '', 0, '', '', '', ''), '', '', '\x00', '', '', '', '', '', '', '', '', 0, '', '', '', '') == None

