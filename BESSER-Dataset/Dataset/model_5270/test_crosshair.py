from python_code import testup_AUp
from python_code import testup_B

def test_testup_B___init__():
    assert testup_B.__init__(testup_B('', testup_B=testup_AUp()), '', testup_B=testup_AUp()) == None


from python_code import testup_D

def test_testup_D___init__():
    assert testup_D.__init__(testup_D('', testup_D=set()), '', testup_D=set()) == None


from python_code import testup_E

def test_testup_E___init__():
    assert testup_E.__init__(testup_E(''), '') == None

