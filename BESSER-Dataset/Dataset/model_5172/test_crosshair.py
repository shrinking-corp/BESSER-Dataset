from python_code import binDsl_B
from python_code import binDsl_L

def test_binDsl_B___init__():
    assert binDsl_B.__init__(binDsl_B('', binDsl_B=binDsl_L()), '', binDsl_B=binDsl_L()) == None


from python_code import binDsl_L
from python_code import binDsl_N

def test_binDsl_N___init__():
    assert binDsl_N.__init__(binDsl_N(True, binDsl_N=binDsl_L(), binDsl_N2=binDsl_L()), False, binDsl_N=binDsl_L(), binDsl_N2=binDsl_L()) == None

