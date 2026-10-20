from python_code import Event

def test_Event___init__():
    assert Event.__init__(Event(0, '', '', 0, ''), 0, '', '', 0, '') == None


from python_code import Room

def test_Room___init__():
    assert Room.__init__(Room(0, '\x00'), 0, '\x00') == None


from python_code import Event
from python_code import Serie

def test_Serie___init__():
    assert Serie.__init__(Serie(Event(0, '', '', 0, '')), Event(0, '', '', 0, '')) == None


from python_code import Event
from python_code import Room
from python_code import Session
from python_code import SessionType

def test_Session___init__():
    assert Session.__init__(Session(0, '', '', SessionType(0, '', ''), '\x00', Room(0, ''), Event(0, '', '', 0, '')), 0, '', '', SessionType(0, '', ''), '', Room(0, '\x00'), Event(0, '', '', 0, '')) == None


from python_code import SessionType

def test_SessionType___init__():
    assert SessionType.__init__(SessionType(0, '', '\x00\x00'), 0, '', '') == None

