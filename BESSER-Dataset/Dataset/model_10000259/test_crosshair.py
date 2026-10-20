from python_code import Chef

def test_Chef___init__():
    assert Chef.__init__(Chef(0, '\x00'), 0, '\x00') == None


from python_code import ReservationManagementSystem

def test_ReservationManagementSystem___init__():
    assert ReservationManagementSystem.__init__(ReservationManagementSystem('', interacts3=set(), interacts5=set(), booking6=set(), generates8=set()), '\x00', interacts3=set(), interacts5=set(), booking6=set(), generates8=set()) == None

