from python_code import Gato

def test_Gato___init__():
    assert Gato.__init__(Gato('', '', '\x00\x00'), '', '', '') == None

