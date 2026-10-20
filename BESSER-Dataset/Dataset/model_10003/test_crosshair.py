from python_code import CoachBus_AdultTicket

def test_CoachBus_AdultTicket___init__():
    assert CoachBus_AdultTicket.__init__(CoachBus_AdultTicket(True), False) == None


from python_code import CoachBus_ChildTicket

def test_CoachBus_ChildTicket___init__():
    assert CoachBus_ChildTicket.__init__(CoachBus_ChildTicket(True), False) == None


from python_code import CoachBus_Employee

def test_CoachBus_Employee___init__():
    assert CoachBus_Employee.__init__(CoachBus_Employee(0, 0.0), 0, 0.0) == None


from python_code import CoachBus_PrivateTrip

def test_CoachBus_PrivateTrip___init__():
    assert CoachBus_PrivateTrip.__init__(CoachBus_PrivateTrip(''), '') == None

