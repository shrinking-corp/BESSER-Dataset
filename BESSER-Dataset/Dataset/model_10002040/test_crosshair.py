from python_code import Bill

def test_Bill___init__():
    assert Bill.__init__(Bill(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import Corporation

def test_Corporation___init__():
    assert Corporation.__init__(Corporation(0, '', '', personel7=set(), personel12=set()), 0, '', '', personel7=set(), personel12=set()) == None

