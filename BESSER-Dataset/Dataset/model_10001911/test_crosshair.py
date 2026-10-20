from python_code import Cache
from python_code import RAM

def test_Cache___init__():
    assert Cache.__init__(Cache('', ramProxy10=RAM()), '', ramProxy10=RAM()) == None


from python_code import Machine

def test_Machine___init__():
    assert Machine.__init__(Machine('', '', memory1=set(), processor7=set(), cards19=set()), '', '', memory1=set(), processor7=set(), cards19=set()) == None


from python_code import Program

def test_Program___init__():
    assert Program.__init__(Program('', instructions5=set(), processor8=set()), '', instructions5=set(), processor8=set()) == None

