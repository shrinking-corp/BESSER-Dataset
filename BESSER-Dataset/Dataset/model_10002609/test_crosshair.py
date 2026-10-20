from python_code import Cache
from python_code import RAM

def test_Cache___init__():
    assert Cache.__init__(Cache('', machine0=set(), processor2=set(), ramProxy10=RAM()), '', machine0=set(), processor2=set(), ramProxy10=RAM()) == None


from python_code import Program

def test_Program___init__():
    assert Program.__init__(Program('', instructions5=set(), processor8=set()), '', instructions5=set(), processor8=set()) == None

