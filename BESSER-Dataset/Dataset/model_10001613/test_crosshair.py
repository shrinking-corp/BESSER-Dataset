from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import E
from python_code import G

def test_E___init__():
    assert E.__init__(E('', g4=G()), '', g4=G()) == None


from python_code import F

def test_F___init__():
    assert F.__init__(F(''), '') == None

