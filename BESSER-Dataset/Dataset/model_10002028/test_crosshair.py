from python_code import Banker

def test_Banker___init__():
    assert Banker.__init__(Banker(0), 0) == None


from python_code import Business_Owner
from python_code import Cards_external

def test_Business_Owner___init__():
    assert Business_Owner.__init__(Business_Owner(0, cards5=Cards_external()), 0, cards5=Cards_external()) == None

