from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount('\x00', 0.0), '', 0.0) == None


from python_code import ClassA

def test_ClassA___init__():
    assert ClassA.__init__(ClassA(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import Component

def test_Component___init__():
    assert Component.__init__(Component('', '\x00', 0.0, 0.0), '', '', 0.0, 0.0) == None


from python_code import ComponentenLijst

def test_ComponentenLijst___init__():
    assert ComponentenLijst.__init__(ComponentenLijst(''), '') == None

