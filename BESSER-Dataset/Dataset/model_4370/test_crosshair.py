from python_code import klang_Event
from python_code import klang_EventHandler

def test_klang_Event___init__():
    assert klang_Event.__init__(klang_Event(klang_Event=klang_EventHandler()), klang_Event=klang_EventHandler()) == None

def test_klang_Event_matchingEvent():
    assert klang_Event.matchingEvent(klang_Event(klang_Event=klang_EventHandler()), '') == None


from python_code import klang_KeyPressEvent

def test_klang_KeyPressEvent___init__():
    assert klang_KeyPressEvent.__init__(klang_KeyPressEvent(''), '') == None


from python_code import klang_MessageReceivedEvent

def test_klang_MessageReceivedEvent___init__():
    assert klang_MessageReceivedEvent.__init__(klang_MessageReceivedEvent(''), '') == None

