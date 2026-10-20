from python_code import Inventory

def test_Inventory___init__():
    assert Inventory.__init__(Inventory('\x00\x00', '', product2=set()), '', '', product2=set()) == None

