from python_code import Example_A

def test_Example_A___init__():
    assert Example_A.__init__(Example_A(''), '') == None

def test_Example_A_getAs():
    assert Example_A.getAs(Example_A('')) == None


from python_code import Example_B

def test_Example_B___init__():
    assert Example_B.__init__(Example_B(''), '') == None

def test_Example_B_getBs():
    assert Example_B.getBs(Example_B('')) == None


from python_code import Example_Ba

def test_Example_Ba___init__():
    assert Example_Ba.__init__(Example_Ba(''), '') == None

