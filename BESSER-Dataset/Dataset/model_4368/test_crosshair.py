from python_code import minilang_Constant

def test_minilang_Constant___init__():
    assert minilang_Constant.__init__(minilang_Constant(0.0), 0.0) == None

def test_minilang_Constant_valueK3():
    assert minilang_Constant.valueK3(minilang_Constant(0.0)) == None


from python_code import minilang_Modulo

def test_minilang_Modulo___init__():
    assert minilang_Modulo.__init__(minilang_Modulo()) == None

def test_minilang_Modulo_valueK3():
    assert minilang_Modulo.valueK3(minilang_Modulo()) == None


from python_code import minilang_Move

def test_minilang_Move___init__():
    assert minilang_Move.__init__(minilang_Move()) == None

def test_minilang_Move_executeK3():
    assert minilang_Move.executeK3(minilang_Move()) == None


from python_code import minilang_RotateLeft

def test_minilang_RotateLeft___init__():
    assert minilang_RotateLeft.__init__(minilang_RotateLeft()) == None

def test_minilang_RotateLeft_executeK3():
    assert minilang_RotateLeft.executeK3(minilang_RotateLeft()) == None


from python_code import minilang_RotateRight

def test_minilang_RotateRight___init__():
    assert minilang_RotateRight.__init__(minilang_RotateRight()) == None

def test_minilang_RotateRight_executeK3():
    assert minilang_RotateRight.executeK3(minilang_RotateRight()) == None


from python_code import minilang_Sum

def test_minilang_Sum___init__():
    assert minilang_Sum.__init__(minilang_Sum()) == None

def test_minilang_Sum_valueK3():
    assert minilang_Sum.valueK3(minilang_Sum()) == None

