from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('', 0, '', '', 0, customercare24=set(), company28=set()), '', 0, '', '', 0, customercare24=set(), company28=set()) == None


from python_code import Customercare

def test_Customercare___init__():
    assert Customercare.__init__(Customercare(0, '\x00', customer25=set()), 0, '', customer25=set()) == None


from python_code import Feedback

def test_Feedback___init__():
    assert Feedback.__init__(Feedback('', 0, 0), '\x00', 0, 0) == None


from python_code import company

def test_company___init__():
    assert company.__init__(company('', 0, '', warehouse26=set(), customer29=set()), '', 0, '', warehouse26=set(), customer29=set()) == None


from python_code import services

def test_services___init__():
    assert services.__init__(services('\x00\x00', '', product27=set()), '', '', product27=set()) == None

