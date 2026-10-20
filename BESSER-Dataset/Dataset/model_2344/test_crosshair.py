from python_code import grudi_Person

def test_grudi_Person___init__():
    assert grudi_Person.__init__(grudi_Person('', '', '', '', '\x00', '', '', '', ''), '', '', '', '', '', '\x00', '', '', '') == None

