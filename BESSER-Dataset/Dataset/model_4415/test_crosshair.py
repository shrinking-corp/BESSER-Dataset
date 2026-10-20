from python_code import arduino_Apagar
from python_code import arduino_Encender
from python_code import arduino_Esperar

def test_arduino_Esperar___init__():
    assert arduino_Esperar.__init__(arduino_Esperar('', arduino_Esperar=arduino_Apagar(), arduino_Esperar17=arduino_Apagar(), arduino_Esperar20=arduino_Encender(), arduino_Esperar23=arduino_Encender()), '', arduino_Esperar=arduino_Apagar(), arduino_Esperar17=arduino_Apagar(), arduino_Esperar20=arduino_Encender(), arduino_Esperar23=arduino_Encender()) == None


from python_code import arduino_If

def test_arduino_If___init__():
    assert arduino_If.__init__(arduino_If('', '', '\x00\x00'), '', '', '') == None


from python_code import arduino_Servo

def test_arduino_Servo___init__():
    assert arduino_Servo.__init__(arduino_Servo('', '\x00'), '\x00\x00', '') == None


from python_code import arduino_Temperatura

def test_arduino_Temperatura___init__():
    assert arduino_Temperatura.__init__(arduino_Temperatura(''), '') == None


from python_code import arduino_While

def test_arduino_While___init__():
    assert arduino_While.__init__(arduino_While('', '', '\x00\x00'), '', '', '') == None

