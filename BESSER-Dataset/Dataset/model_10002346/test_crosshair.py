from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login(0, '\x00'), 0, '\x00') == None


from python_code import ffddsff

def test_ffddsff___init__():
    assert ffddsff.__init__(ffddsff(0.0, 0, '', '', ''), 0.0, 0, '', '', '\x00') == None

