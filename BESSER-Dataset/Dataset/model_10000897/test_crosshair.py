from python_code import Cache
from python_code import RAM

def test_Cache___init__():
    assert Cache.__init__(Cache('', ramProxy6=RAM()), '', ramProxy6=RAM()) == None


from python_code import Class

def test_Class___init__():
    assert Class.__init__(Class(''), '') == None


from python_code import Program

def test_Program___init__():
    assert Program.__init__(Program('', instructions3=set(), processor4=set()), '', instructions3=set(), processor4=set()) == None

