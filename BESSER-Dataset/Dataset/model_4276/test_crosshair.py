from python_code import bowling_Tournament

def test_bowling_Tournament___init__():
    assert bowling_Tournament.__init__(bowling_Tournament('', bowling_Tournament=set()), '', bowling_Tournament=set()) == None


from python_code import bowling_league

def test_bowling_league___init__():
    assert bowling_league.__init__(bowling_league('', bowling_league=set()), '\x00', bowling_league=set()) == None

