from python_code import Elevator1

def test_Elevator1___init__():
    assert Elevator1.__init__(Elevator1(0), 0) == None


from python_code import Elevator_Controller_2

def test_Elevator_Controller_2___init__():
    assert Elevator_Controller_2.__init__(Elevator_Controller_2(0, 0, False, ''), 0, 0, False, '') == None


from python_code import Elevator_button

def test_Elevator_button___init__():
    assert Elevator_button.__init__(Elevator_button(0), 0) == None


from python_code import Floor

def test_Floor___init__():
    assert Floor.__init__(Floor(0), 0) == None


from python_code import Floor_button

def test_Floor_button___init__():
    assert Floor_button.__init__(Floor_button(0, False), 0, False) == None

