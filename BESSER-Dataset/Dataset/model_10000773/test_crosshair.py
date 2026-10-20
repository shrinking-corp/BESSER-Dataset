from python_code import Light

def test_Light___init__():
    assert Light.__init__(Light(0), 0) == None


from python_code import ROOM

def test_ROOM___init__():
    assert ROOM.__init__(ROOM(''), '') == None


from python_code import TechSupport

def test_TechSupport___init__():
    assert TechSupport.__init__(TechSupport(0), 0) == None


from python_code import UserProfile

def test_UserProfile___init__():
    assert UserProfile.__init__(UserProfile(0), 0) == None

