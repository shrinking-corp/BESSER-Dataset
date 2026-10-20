from python_code import Room

def test_Room___init__():
    assert Room.__init__(Room(0, '\x00'), 0, '\x00') == None


from python_code import medicine

def test_medicine___init__():
    assert medicine.__init__(medicine(0, '', 0), 0, '', 0) == None

