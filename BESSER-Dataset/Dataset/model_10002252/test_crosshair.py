from python_code import ClassA

def test_ClassA___init__():
    assert ClassA.__init__(ClassA(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC('', '', 0.0, 0), '', '', 0.0, 0) == None


from python_code import F1

def test_F1___init__():
    assert F1.__init__(F1('\x00', 0.0), '', 0.0) == None

