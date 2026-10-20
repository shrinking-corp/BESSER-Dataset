from python_code import testmodel_A

def test_testmodel_A___init__():
    assert testmodel_A.__init__(testmodel_A(''), '') == None

def test_testmodel_A_aOp():
    assert testmodel_A.aOp(testmodel_A('')) == None


from python_code import testmodel_B

def test_testmodel_B___init__():
    assert testmodel_B.__init__(testmodel_B(''), '') == None

def test_testmodel_B_bOp():
    assert testmodel_B.bOp(testmodel_B('')) == None


from python_code import testmodel_C

def test_testmodel_C___init__():
    assert testmodel_C.__init__(testmodel_C(''), '') == None

def test_testmodel_C_aOp():
    assert testmodel_C.aOp(testmodel_C('')) == None

def test_testmodel_C_bOp():
    assert testmodel_C.bOp(testmodel_C('')) == None

