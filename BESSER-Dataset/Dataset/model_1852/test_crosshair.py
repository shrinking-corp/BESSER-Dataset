from python_code import message_MessageLibrary

def test_message_MessageLibrary___init__():
    assert message_MessageLibrary.__init__(message_MessageLibrary('\x00\x00', '', message_MessageLibrary=set()), '', '', message_MessageLibrary=set()) == None

