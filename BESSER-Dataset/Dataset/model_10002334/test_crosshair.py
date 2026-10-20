from python_code import Door

def test_Door___init__():
    assert Door.__init__(Door(0, camera0=set()), 0, camera0=set()) == None


from python_code import Geyser

def test_Geyser___init__():
    assert Geyser.__init__(Geyser(''), '') == None


from python_code import User__SMS_

def test_User__SMS____init__():
    assert User__SMS_.__init__(User__SMS_(''), '') == None

