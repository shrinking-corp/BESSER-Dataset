from python_code import Barang

def test_Barang___init__():
    assert Barang.__init__(Barang('', '\x00'), '\x00\x00', '') == None

