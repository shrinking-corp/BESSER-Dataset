from python_code import ClassA

def test_ClassA___init__():
    assert ClassA.__init__(ClassA(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import GMTPage

def test_GMTPage___init__():
    assert GMTPage.__init__(GMTPage('\x00', 0.0), '', 0.0) == None

