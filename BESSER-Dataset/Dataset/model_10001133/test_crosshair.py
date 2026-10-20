from python_code import MatchingGame

def test_MatchingGame___init__():
    assert MatchingGame.__init__(MatchingGame(0), 0) == None


from python_code import TrickGame

def test_TrickGame___init__():
    assert TrickGame.__init__(TrickGame(''), '') == None

