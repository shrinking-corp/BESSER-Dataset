from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck('\x00', Deck_Card_00=set()), '', Deck_Card_00=set()) == None


from python_code import Hand

def test_Hand___init__():
    assert Hand.__init__(Hand('', Hand_Card_02=set(), CardPlayer_Hand_15=set()), '', Hand_Card_02=set(), CardPlayer_Hand_15=set()) == None

