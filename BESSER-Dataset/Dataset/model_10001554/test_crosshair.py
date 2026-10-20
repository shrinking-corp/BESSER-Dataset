from python_code import Dept

def test_Dept___init__():
    assert Dept.__init__(Dept(0, '', 0, doctor11=set()), 0, '', 0, doctor11=set()) == None


from python_code import ReceptionList

def test_ReceptionList___init__():
    assert ReceptionList.__init__(ReceptionList(0, '', patient3=set(), bill7=set()), 0, '', patient3=set(), bill7=set()) == None

