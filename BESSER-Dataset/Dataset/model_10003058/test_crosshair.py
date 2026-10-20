from python_code import Administrator

def test_Administrator___init__():
    assert Administrator.__init__(Administrator('', '', Manage1=set()), '', '', Manage1=set()) == None


from python_code import Bank

def test_Bank___init__():
    assert Bank.__init__(Bank('', 0, customer2=set()), '', 0, customer2=set()) == None

