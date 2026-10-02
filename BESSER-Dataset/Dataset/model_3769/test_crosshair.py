from python_code import d_X

def test_d_X___init__():
    assert d_X.__init__(d_X()) == None

def test_d_X_baz():
    assert d_X.baz(d_X(), '') == None

from python_code import d_Y

def test_d_Y___init__():
    assert d_Y.__init__(d_Y(''), '') == None

from python_code import d_B
from python_code import d_Z

def test_d_Z___init__():
    assert d_Z.__init__(d_Z(0, d_Z=d_B()), 0, d_Z=d_B()) == None
