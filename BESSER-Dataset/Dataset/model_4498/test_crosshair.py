from python_code import ArduinoCard_Block
from python_code import ArduinoCard_Card

def test_ArduinoCard_Block___init__():
    assert ArduinoCard_Block.__init__(ArduinoCard_Block(0, '', '\x00\x00', ArduinoCard_Block=ArduinoCard_Card()), 0, '', '', ArduinoCard_Block=ArduinoCard_Card()) == None


from python_code import ArduinoCard_BlockInteraction
from python_code import ArduinoCard_Card

def test_ArduinoCard_BlockInteraction___init__():
    assert ArduinoCard_BlockInteraction.__init__(ArduinoCard_BlockInteraction(False, '\x00', ArduinoCard_BlockInteraction=ArduinoCard_Card()), False, '\x00', ArduinoCard_BlockInteraction=ArduinoCard_Card()) == None

