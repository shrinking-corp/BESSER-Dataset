from python_code import Card

def test_Card___init__():
    assert Card.__init__(Card(0, 0), 0, 0) == None


from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck(''), '') == None

