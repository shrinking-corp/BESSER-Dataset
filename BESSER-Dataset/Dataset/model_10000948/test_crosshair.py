from python_code import WebUser

def test_WebUser___init__():
    assert WebUser.__init__(WebUser('', '', '\x00\x00'), '', '', '') == None

