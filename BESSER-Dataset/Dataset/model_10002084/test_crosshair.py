from python_code import EventType

def test_EventType___init__():
    assert EventType.__init__(EventType('\x00\x00', 0, events2=set()), '', 0, events2=set()) == None
