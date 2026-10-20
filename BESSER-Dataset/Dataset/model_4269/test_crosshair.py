from python_code import bowling_League

def test_bowling_League___init__():
    assert bowling_League.__init__(bowling_League('', bowling_League=set()), '', bowling_League=set()) == None


from python_code import bowling_Tournament

def test_bowling_Tournament___init__():
    assert bowling_Tournament.__init__(bowling_Tournament('\x00\x00', '', bowling_Tournament=set()), '', '', bowling_Tournament=set()) == None

