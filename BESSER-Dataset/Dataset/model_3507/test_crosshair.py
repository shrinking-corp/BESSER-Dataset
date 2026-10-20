from python_code import factorydeclorder_A

def test_factorydeclorder_A___init__():
    assert factorydeclorder_A.__init__(factorydeclorder_A(0), 0) == None


from python_code import factorydeclorder_B

def test_factorydeclorder_B___init__():
    assert factorydeclorder_B.__init__(factorydeclorder_B(''), '') == None


from python_code import factorydeclorder_C

def test_factorydeclorder_C___init__():
    assert factorydeclorder_C.__init__(factorydeclorder_C(True), False) == None

