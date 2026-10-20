from python_code import elevator_s_buttons

def test_elevator_s_buttons___init__():
    assert elevator_s_buttons.__init__(elevator_s_buttons(0), 0) == None


from python_code import floor_s_buttons

def test_floor_s_buttons___init__():
    assert floor_s_buttons.__init__(floor_s_buttons(True), False) == None

