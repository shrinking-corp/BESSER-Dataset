from python_code import Khoa

def test_Khoa___init__():
    assert Khoa.__init__(Khoa('\x00\x00', '', co8=set()), '', '', co8=set()) == None

