from python_code import textlink_ModelLocation
from python_code import textlink_TraceLink

def test_textlink_ModelLocation___init__():
    assert textlink_ModelLocation.__init__(textlink_ModelLocation('', textlink_ModelLocation=textlink_TraceLink()), '', textlink_ModelLocation=textlink_TraceLink()) == None

