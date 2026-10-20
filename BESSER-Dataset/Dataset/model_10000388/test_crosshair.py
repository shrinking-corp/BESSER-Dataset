from python_code import Actor

def test_Actor___init__():
    assert Actor.__init__(Actor('', '', '', listing0=set()), '', '', '', listing0=set()) == None


from python_code import Apartment

def test_Apartment___init__():
    assert Apartment.__init__(Apartment(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import House

def test_House___init__():
    assert House.__init__(House(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import RealEstateAgent

def test_RealEstateAgent___init__():
    assert RealEstateAgent.__init__(RealEstateAgent(''), '') == None

