from python_code import Empleado

def test_Empleado___init__():
    assert Empleado.__init__(Empleado('', '', '\x00\x00'), '', '', '') == None


from python_code import provvedor

def test_provvedor___init__():
    assert provvedor.__init__(provvedor('', '\x00'), '\x00\x00', '') == None

