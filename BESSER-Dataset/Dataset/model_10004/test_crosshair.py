from python_code import CoachBusWithEDataType_AdultTicket

def test_CoachBusWithEDataType_AdultTicket___init__():
    assert CoachBusWithEDataType_AdultTicket.__init__(CoachBusWithEDataType_AdultTicket(True), False) == None


from python_code import CoachBusWithEDataType_ChildTicket

def test_CoachBusWithEDataType_ChildTicket___init__():
    assert CoachBusWithEDataType_ChildTicket.__init__(CoachBusWithEDataType_ChildTicket(True), False) == None


from python_code import CoachBusWithEDataType_Employee

def test_CoachBusWithEDataType_Employee___init__():
    assert CoachBusWithEDataType_Employee.__init__(CoachBusWithEDataType_Employee(0, 0.0), 0, 0.0) == None


from python_code import CoachBusWithEDataType_PrivateTrip

def test_CoachBusWithEDataType_PrivateTrip___init__():
    assert CoachBusWithEDataType_PrivateTrip.__init__(CoachBusWithEDataType_PrivateTrip(''), '') == None

