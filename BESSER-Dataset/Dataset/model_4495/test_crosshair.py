from python_code import marsRover_Robot

def test_marsRover_Robot___init__():
    assert marsRover_Robot.__init__(marsRover_Robot('', '', 0, 0, marsRover_Robot=set()), '', '', 0, 0, marsRover_Robot=set()) == None


from python_code import marsRover_avoid_lakes

def test_marsRover_avoid_lakes___init__():
    assert marsRover_avoid_lakes.__init__(marsRover_avoid_lakes(''), '') == None


from python_code import marsRover_avoid_obstacles

def test_marsRover_avoid_obstacles___init__():
    assert marsRover_avoid_obstacles.__init__(marsRover_avoid_obstacles('', marsRover_avoid_obstacles=set()), '', marsRover_avoid_obstacles=set()) == None


from python_code import marsRover_bumpers

def test_marsRover_bumpers___init__():
    assert marsRover_bumpers.__init__(marsRover_bumpers(''), '') == None


from python_code import marsRover_color_indication

def test_marsRover_color_indication___init__():
    assert marsRover_color_indication.__init__(marsRover_color_indication('', '\x00'), '\x00\x00', '') == None


from python_code import marsRover_message

def test_marsRover_message___init__():
    assert marsRover_message.__init__(marsRover_message('', '\x00'), '\x00\x00', '') == None


from python_code import marsRover_park

def test_marsRover_park___init__():
    assert marsRover_park.__init__(marsRover_park(''), '') == None


from python_code import marsRover_push_obstacles

def test_marsRover_push_obstacles___init__():
    assert marsRover_push_obstacles.__init__(marsRover_push_obstacles(''), '') == None


from python_code import marsRover_sound

def test_marsRover_sound___init__():
    assert marsRover_sound.__init__(marsRover_sound('', 0, 0), '\x00', 0, 0) == None


from python_code import marsRover_ultra

def test_marsRover_ultra___init__():
    assert marsRover_ultra.__init__(marsRover_ultra('', 0), '', 0) == None

