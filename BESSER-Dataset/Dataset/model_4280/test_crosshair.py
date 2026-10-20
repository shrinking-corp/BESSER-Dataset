from python_code import bowling_League

def test_bowling_League___init__():
    assert bowling_League.__init__(bowling_League('', bowling_League=set()), '', bowling_League=set()) == None


from python_code import bowling_Matchup
from python_code import bowling_Tournament

def test_bowling_Tournament___init__():
    assert bowling_Tournament.__init__(bowling_Tournament('', bowling_Tournament=bowling_Matchup()), '', bowling_Tournament=bowling_Matchup()) == None

