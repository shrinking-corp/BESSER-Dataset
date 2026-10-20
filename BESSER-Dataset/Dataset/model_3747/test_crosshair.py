from python_code import actionpak1_IncomingCall2

def test_actionpak1_IncomingCall2___init__():
    assert actionpak1_IncomingCall2.__init__(actionpak1_IncomingCall2(''), '') == None


from python_code import DynamicValue
from python_code import actionpak1_InvokeSaflet2

def test_actionpak1_InvokeSaflet2___init__():
    assert actionpak1_InvokeSaflet2.__init__(actionpak1_InvokeSaflet2('', actionpak1_InvokeSaflet2=DynamicValue()), '', actionpak1_InvokeSaflet2=DynamicValue()) == None

