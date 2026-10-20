from python_code import CardGame

def test_CardGame___init__():
    assert CardGame.__init__(CardGame(0, '\x00', cards1=set()), 0, '', cards1=set()) == None

