from python_code import brmodel_Method

def test_brmodel_Method___init__():
    assert brmodel_Method.__init__(brmodel_Method('', '\x00'), '\x00\x00', '') == None


from python_code import brmodel_Variable

def test_brmodel_Variable___init__():
    assert brmodel_Variable.__init__(brmodel_Variable(''), '') == None

