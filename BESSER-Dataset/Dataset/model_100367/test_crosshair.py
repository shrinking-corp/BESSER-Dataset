from python_code import FSmachine_ReasonConnection

def test_FSmachine_ReasonConnection___init__():
    assert FSmachine_ReasonConnection.__init__(FSmachine_ReasonConnection(''), '') == None


from python_code import FSmachine_State

def test_FSmachine_State___init__():
    assert FSmachine_State.__init__(FSmachine_State('', '\x00'), '\x00\x00', '') == None


from python_code import FSmachine_TimeConnection

def test_FSmachine_TimeConnection___init__():
    assert FSmachine_TimeConnection.__init__(FSmachine_TimeConnection(''), '') == None

