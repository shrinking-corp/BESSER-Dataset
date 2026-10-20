from python_code import Game

def test_Game___init__():
    assert Game.__init__(Game('', player2=set()), '', player2=set()) == None

