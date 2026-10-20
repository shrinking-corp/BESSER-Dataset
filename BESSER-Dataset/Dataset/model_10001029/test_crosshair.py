from python_code import Administrator

def test_Administrator___init__():
    assert Administrator.__init__(Administrator('\x00\x00', '', employee1=set()), '', '', employee1=set()) == None


from python_code import Advertiser

def test_Advertiser___init__():
    assert Advertiser.__init__(Advertiser('\x00\x00', '', advertiesment2=set()), '', '', advertiesment2=set()) == None


from python_code import Payment

def test_Payment___init__():
    assert Payment.__init__(Payment(0, '', '', '', '\x00', reg_User14=set(), property16=set()), 0, '', '', '', '', reg_User14=set(), property16=set()) == None


from python_code import Seller

def test_Seller___init__():
    assert Seller.__init__(Seller('\x00\x00', '', property5=set()), '', '', property5=set()) == None

