from python_code import pghttptest_A
from python_code import pghttptest_Root

def test_pghttptest_A___init__():
    assert pghttptest_A.__init__(pghttptest_A(0, '\x00', pghttptest_A=pghttptest_Root()), 0, '\x00', pghttptest_A=pghttptest_Root()) == None


from python_code import pghttptest_B
from python_code import pghttptest_Root

def test_pghttptest_B___init__():
    assert pghttptest_B.__init__(pghttptest_B(0, pghttptest_B=pghttptest_Root(), pghttptest_B4=set()), 0, pghttptest_B=pghttptest_Root(), pghttptest_B4=set()) == None

def test_pghttptest_B_priv2():
    assert pghttptest_B.priv2(pghttptest_B(0, pghttptest_B=pghttptest_Root(), pghttptest_B4=set())) == None

def test_pghttptest_B_lastC():
    assert pghttptest_B.lastC(pghttptest_B(0, pghttptest_B=pghttptest_Root(), pghttptest_B4=set())) == None


from python_code import pghttptest_Priv

def test_pghttptest_Priv___init__():
    assert pghttptest_Priv.__init__(pghttptest_Priv(''), '') == None

