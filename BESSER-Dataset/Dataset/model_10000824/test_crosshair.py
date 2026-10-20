from python_code import Adult

def test_Adult___init__():
    assert Adult.__init__(Adult('', '\x00'), '\x00\x00', '') == None


from python_code import Business_Seats

def test_Business_Seats___init__():
    assert Business_Seats.__init__(Business_Seats('', '\x00'), '\x00\x00', '') == None


from python_code import Child

def test_Child___init__():
    assert Child.__init__(Child('', '\x00'), '\x00\x00', '') == None


from python_code import Economy_Seats

def test_Economy_Seats___init__():
    assert Economy_Seats.__init__(Economy_Seats('', '\x00'), '\x00\x00', '') == None


from python_code import First_Class

def test_First_Class___init__():
    assert First_Class.__init__(First_Class('', '\x00'), '\x00\x00', '') == None


from python_code import Infant

def test_Infant___init__():
    assert Infant.__init__(Infant('', '\x00'), '\x00\x00', '') == None

