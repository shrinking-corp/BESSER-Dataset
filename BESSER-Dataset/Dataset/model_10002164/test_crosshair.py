from python_code import Bartender

def test_Bartender___init__():
    assert Bartender.__init__(Bartender('', '\x00'), '\x00\x00', '') == None


from python_code import Chef

def test_Chef___init__():
    assert Chef.__init__(Chef('', '\x00'), '\x00\x00', '') == None


from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('', '\x00'), '\x00\x00', '') == None


from python_code import Karyawan

def test_Karyawan___init__():
    assert Karyawan.__init__(Karyawan('', '', '\x00\x00'), '', '', '') == None


from python_code import Kasir

def test_Kasir___init__():
    assert Kasir.__init__(Kasir('', '\x00'), '\x00\x00', '') == None


from python_code import Report

def test_Report___init__():
    assert Report.__init__(Report('', '', '\x00\x00'), '', '', '') == None

