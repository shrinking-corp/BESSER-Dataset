from python_code import k5_G

def test_k5_G___init__():
    assert k5_G.__init__(k5_G(''), '') == None


from python_code import k5_C
from python_code import k5_L1
from python_code import k5_M

def test_k5_L1___init__():
    assert k5_L1.__init__(k5_L1('', 0, k5_L1=k5_M(), k5_L125=k5_C(), k5_L128=k5_M()), '', 0, k5_L1=k5_M(), k5_L125=k5_C(), k5_L128=k5_M()) == None


from python_code import k5_W
from python_code import k5_X

def test_k5_W___init__():
    assert k5_W.__init__(k5_W('', k5_W=k5_X()), '', k5_W=k5_X()) == None


from python_code import k5_B
from python_code import k5_X
from python_code import k5_Y

def test_k5_Y___init__():
    assert k5_Y.__init__(k5_Y(0, k5_Y=k5_X(), k5_Y12=k5_B()), 0, k5_Y=k5_X(), k5_Y12=k5_B()) == None


from python_code import k5_L3
from python_code import k5_X
from python_code import k5_Z

def test_k5_Z___init__():
    assert k5_Z.__init__(k5_Z('', '', '\x00\x00', k5_Z=k5_X(), k5_Z37=k5_L3()), '', '', '', k5_Z=k5_X(), k5_Z37=k5_L3()) == None

