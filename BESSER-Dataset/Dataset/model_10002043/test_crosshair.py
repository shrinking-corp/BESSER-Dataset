from python_code import BaseBO

def test_BaseBO___init__():
    assert BaseBO.__init__(BaseBO('', 0, False), '\x00', 0, False) == None


from python_code import Location

def test_Location___init__():
    assert Location.__init__(Location(''), '') == None


from python_code import PolicyImage

def test_PolicyImage___init__():
    assert PolicyImage.__init__(PolicyImage(''), '') == None

