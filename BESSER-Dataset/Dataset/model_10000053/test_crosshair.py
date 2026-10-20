from python_code import Person

def test_Person___init__():
    assert Person.__init__(Person(0, '', '\x00\x00'), 0, '', '') == None


from python_code import Room

def test_Room___init__():
    assert Room.__init__(Room(0, '', patient5=set(), staff6=set()), 0, '', patient5=set(), staff6=set()) == None

