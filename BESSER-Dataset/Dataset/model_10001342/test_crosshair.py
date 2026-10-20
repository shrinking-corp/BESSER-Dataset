from python_code import Inventory

def test_Inventory___init__():
    assert Inventory.__init__(Inventory('', '\x00'), '\x00\x00', '') == None


from python_code import Manager

def test_Manager___init__():
    assert Manager.__init__(Manager('', 0, 0), '\x00', 0, 0) == None

