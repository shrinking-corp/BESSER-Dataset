from python_code import Monopoly1

def test_Monopoly1___init__():
    assert Monopoly1.__init__(Monopoly1(''), '') == None


from python_code import TCobrarJugadores1

def test_TCobrarJugadores1___init__():
    assert TCobrarJugadores1.__init__(TCobrarJugadores1(0), 0) == None


from python_code import TPagarBanco1

def test_TPagarBanco1___init__():
    assert TPagarBanco1.__init__(TPagarBanco1(0), 0) == None


from python_code import TPagarJugadores1

def test_TPagarJugadores1___init__():
    assert TPagarJugadores1.__init__(TPagarJugadores1(0), 0) == None


from python_code import Tarjeta1

def test_Tarjeta1___init__():
    assert Tarjeta1.__init__(Tarjeta1('', '\x00'), '\x00\x00', '') == None

