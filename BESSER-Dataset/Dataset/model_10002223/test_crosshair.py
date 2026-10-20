from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('\x00\x00', '', employee0=set()), '', '', employee0=set()) == None


from python_code import Work_days

def test_Work_days___init__():
    assert Work_days.__init__(Work_days(0, 0, daysAttended5=set(), salary6=set()), 0, 0, daysAttended5=set(), salary6=set()) == None

