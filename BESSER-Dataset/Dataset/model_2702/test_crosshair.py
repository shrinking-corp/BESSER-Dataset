from python_code import ktest206_B
from python_code import ktest206_C

def test_ktest206_C___init__():
    assert ktest206_C.__init__(ktest206_C('', ktest206_C=ktest206_B()), '', ktest206_C=ktest206_B()) == None


from python_code import ktest206_A
from python_code import ktest206_D

def test_ktest206_D___init__():
    assert ktest206_D.__init__(ktest206_D('', ktest206_D=ktest206_A()), '', ktest206_D=ktest206_A()) == None


from python_code import ktest206_N

def test_ktest206_N___init__():
    assert ktest206_N.__init__(ktest206_N(''), '') == None

