from python_code import Cache
from python_code import RAM

def test_Cache___init__():
    assert Cache.__init__(Cache('', ramProxy4=RAM()), '', ramProxy4=RAM()) == None


from python_code import Chess

def test_Chess___init__():
    assert Chess.__init__(Chess(''), '') == None


from python_code import Program

def test_Program___init__():
    assert Program.__init__(Program('', instructions1=set(), processor2=set()), '', instructions1=set(), processor2=set()) == None

