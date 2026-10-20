from python_code import CuentaBancaria

def test_CuentaBancaria___init__():
    assert CuentaBancaria.__init__(CuentaBancaria(0), 0) == None


from python_code import Gato

def test_Gato___init__():
    assert Gato.__init__(Gato('', '', '\x00\x00'), '', '', '') == None

