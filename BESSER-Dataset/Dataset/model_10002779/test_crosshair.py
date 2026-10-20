from python_code import Administrator

def test_Administrator___init__():
    assert Administrator.__init__(Administrator('\x00\x00', '', employee1=set()), '', '', employee1=set()) == None


from python_code import Manager

def test_Manager___init__():
    assert Manager.__init__(Manager('\x00\x00', '', adds2=set()), '', '', adds2=set()) == None


from python_code import Owner

def test_Owner___init__():
    assert Owner.__init__(Owner('\x00\x00', '', property5=set()), '', '', property5=set()) == None


from python_code import Payment

def test_Payment___init__():
    assert Payment.__init__(Payment(0, '', '', '', '\x00', reg_User14=set(), property16=set()), 0, '', '', '', '', reg_User14=set(), property16=set()) == None

