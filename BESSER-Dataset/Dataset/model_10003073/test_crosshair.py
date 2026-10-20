from python_code import Registration

def test_Registration___init__():
    assert Registration.__init__(Registration('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import ReservationManagementSystem

def test_ReservationManagementSystem___init__():
    assert ReservationManagementSystem.__init__(ReservationManagementSystem('', booking0=set(), generates2=set()), '', booking0=set(), generates2=set()) == None


from python_code import User

def test_User___init__():
    assert User.__init__(User('', '\x00'), '\x00\x00', '') == None

