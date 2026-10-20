from python_code import BJPlayer

def test_BJPlayer___init__():
    assert BJPlayer.__init__(BJPlayer(0, '\x00'), 0, '\x00') == None


from python_code import HandDeck

def test_HandDeck___init__():
    assert HandDeck.__init__(HandDeck(False, False, False, False), False, False, False, True) == None


from python_code import JokerCard

def test_JokerCard___init__():
    assert JokerCard.__init__(JokerCard(False, False), False, False) == None


from python_code import Player

def test_Player___init__():
    assert Player.__init__(Player('', 0), '', 0) == None


from python_code import PlayingCard

def test_PlayingCard___init__():
    assert PlayingCard.__init__(PlayingCard(False, False, False), False, False, False) == None

