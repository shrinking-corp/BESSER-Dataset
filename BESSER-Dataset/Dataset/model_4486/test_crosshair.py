from python_code import minidrone_Go

def test_minidrone_Go___init__():
    assert minidrone_Go.__init__(minidrone_Go(0), 0) == None


from python_code import minidrone_Jump

def test_minidrone_Jump___init__():
    assert minidrone_Jump.__init__(minidrone_Jump(''), '') == None


from python_code import minidrone_MiniDroneProgram

def test_minidrone_MiniDroneProgram___init__():
    assert minidrone_MiniDroneProgram.__init__(minidrone_MiniDroneProgram('', minidrone_MiniDroneProgram=set()), '', minidrone_MiniDroneProgram=set()) == None


from python_code import minidrone_Turn

def test_minidrone_Turn___init__():
    assert minidrone_Turn.__init__(minidrone_Turn(0), 0) == None

