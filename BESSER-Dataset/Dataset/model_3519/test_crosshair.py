from python_code import modelA_A

def test_modelA_A___init__():
    assert modelA_A.__init__(modelA_A(0), 0) == None


from python_code import modelA_B

def test_modelA_B___init__():
    assert modelA_B.__init__(modelA_B(True), False) == None

