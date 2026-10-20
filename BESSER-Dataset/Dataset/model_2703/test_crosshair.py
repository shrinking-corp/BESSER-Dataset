from python_code import sample_A
from python_code import sample_C

def test_sample_A___init__():
    assert sample_A.__init__(sample_A('', False, 0, sample_A=sample_C()), '\x00', False, 0, sample_A=sample_C()) == None


from python_code import sample_B

def test_sample_B___init__():
    assert sample_B.__init__(sample_B('', sample_B=set()), '', sample_B=set()) == None

