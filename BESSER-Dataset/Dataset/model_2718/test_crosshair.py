from python_code import k4_G

def test_k4_G___init__():
    assert k4_G.__init__(k4_G(''), '') == None


from python_code import k4_C
from python_code import k4_L1
from python_code import k4_M

def test_k4_L1___init__():
    assert k4_L1.__init__(k4_L1('', 0, k4_L1=k4_M(), k4_L122=k4_C(), k4_L125=k4_M()), '', 0, k4_L1=k4_M(), k4_L122=k4_C(), k4_L125=k4_M()) == None


from python_code import k4_W
from python_code import k4_X

def test_k4_W___init__():
    assert k4_W.__init__(k4_W('', k4_W=k4_X()), '', k4_W=k4_X()) == None


from python_code import k4_X
from python_code import k4_Y

def test_k4_Y___init__():
    assert k4_Y.__init__(k4_Y(0, k4_Y=k4_X()), 0, k4_Y=k4_X()) == None


from python_code import k4_L4
from python_code import k4_X
from python_code import k4_Z

def test_k4_Z___init__():
    assert k4_Z.__init__(k4_Z('', '', '\x00\x00', k4_Z=k4_X(), k4_Z36=k4_L4()), '', '', '', k4_Z=k4_X(), k4_Z36=k4_L4()) == None

