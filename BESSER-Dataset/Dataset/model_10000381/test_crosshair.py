from python_code import Membership_Function

def test_Membership_Function___init__():
    assert Membership_Function.__init__(Membership_Function(0.0, '', 0.0, 0.0), 0.0, '\x00', 0.0, 0.0) == None


from python_code import Trapezoidal

def test_Trapezoidal___init__():
    assert Trapezoidal.__init__(Trapezoidal(0.0, 0.0), 0.0, 0.0) == None


from python_code import Triangular

def test_Triangular___init__():
    assert Triangular.__init__(Triangular(0.0), 0.0) == None

