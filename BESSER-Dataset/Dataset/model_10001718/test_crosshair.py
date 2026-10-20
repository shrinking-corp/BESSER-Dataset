from python_code import Doctor

def test_Doctor___init__():
    assert Doctor.__init__(Doctor('', '', team5=set(), patient10=set()), '', '', team5=set(), patient10=set()) == None


from python_code import Hospital

def test_Hospital___init__():
    assert Hospital.__init__(Hospital('', '', '', ward0=set(), team2=set()), '', '', '', ward0=set(), team2=set()) == None

