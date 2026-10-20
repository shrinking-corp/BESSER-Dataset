from python_code import Card_Cards

def test_Card_Cards___init__():
    assert Card_Cards.__init__(Card_Cards(0, 0), 0, 0) == None


from python_code import Card_Deck

def test_Card_Deck___init__():
    assert Card_Deck.__init__(Card_Deck(0, 0, 0, 0, '', ''), 0, 0, 0, 0, '\x00', '') == None


from python_code import Game_Display

def test_Game_Display___init__():
    assert Game_Display.__init__(Game_Display('', '\x00'), '\x00\x00', '') == None


from python_code import Game_EvaluateHand

def test_Game_EvaluateHand___init__():
    assert Game_EvaluateHand.__init__(Game_EvaluateHand(''), '') == None


from python_code import Game_Ranking

def test_Game_Ranking___init__():
    assert Game_Ranking.__init__(Game_Ranking(''), '') == None


from python_code import Main_StartGame

def test_Main_StartGame___init__():
    assert Main_StartGame.__init__(Main_StartGame('', 0, '', '', ''), '', 0, '', '', '') == None


from python_code import Money_PlayerMoney

def test_Money_PlayerMoney___init__():
    assert Money_PlayerMoney.__init__(Money_PlayerMoney('', '\x00'), '\x00\x00', '') == None

