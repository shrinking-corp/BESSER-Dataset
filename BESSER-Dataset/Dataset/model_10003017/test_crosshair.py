from python_code import CPU1

def test_CPU1___init__():
    assert CPU1.__init__(CPU1(0.0), 0.0) == None


from python_code import Cache
from python_code import RAM

def test_Cache___init__():
    assert Cache.__init__(Cache('', ramProxy10=RAM()), '', ramProxy10=RAM()) == None


from python_code import Hardware

def test_Hardware___init__():
    assert Hardware.__init__(Hardware('', '\x00'), '\x00\x00', '') == None


from python_code import Program

def test_Program___init__():
    assert Program.__init__(Program('', instructions5=set(), processor8=set()), '', instructions5=set(), processor8=set()) == None


from python_code import RAM1

def test_RAM1___init__():
    assert RAM1.__init__(RAM1(0.0), 0.0) == None

