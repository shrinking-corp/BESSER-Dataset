from python_code import Administrator

def test_Administrator___init__():
    assert Administrator.__init__(Administrator(0, '', '\x00\x00'), 0, '', '') == None


from python_code import Restaurant_Reservation_System

def test_Restaurant_Reservation_System___init__():
    assert Restaurant_Reservation_System.__init__(Restaurant_Reservation_System('', '', interacts3=set(), interacts5=set(), booking6=set(), generates8=set()), '\x00', '', interacts3=set(), interacts5=set(), booking6=set(), generates8=set()) == None


from python_code import Restaurant_owner

def test_Restaurant_owner___init__():
    assert Restaurant_owner.__init__(Restaurant_owner('', '', '\x00\x00'), '', '', '') == None

