from python_code import LogEntry

def test_LogEntry___init__():
    assert LogEntry.__init__(LogEntry('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Profile2

def test_Profile2___init__():
    assert Profile2.__init__(Profile2('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Tenant

def test_Tenant___init__():
    assert Tenant.__init__(Tenant('', '', abstractEntity15=set(), abstractEntity26=set()), '', '', abstractEntity15=set(), abstractEntity26=set()) == None

