from python_code import Nurse

def test_Nurse___init__():
    assert Nurse.__init__(Nurse(0, '', 0, doctor3=set()), 0, '', 0, doctor3=set()) == None


from python_code import Room

def test_Room___init__():
    assert Room.__init__(Room(0, '', patient5=set(), staff6=set()), 0, '', patient5=set(), staff6=set()) == None

