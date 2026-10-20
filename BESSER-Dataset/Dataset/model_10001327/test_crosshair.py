from python_code import A
from python_code import B

def test_A___init__():
    assert A.__init__(A(False, 0, c0=B()), False, 0, c0=B()) == None


from python_code import E
from python_code import G

def test_E___init__():
    assert E.__init__(E('', g3=G()), '', g3=G()) == None


from python_code import F

def test_F___init__():
    assert F.__init__(F(''), '') == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

