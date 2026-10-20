from python_code import calculatrice_Boolean

def test_calculatrice_Boolean___init__():
    assert calculatrice_Boolean.__init__(calculatrice_Boolean(''), '') == None


from python_code import calculatrice_Number

def test_calculatrice_Number___init__():
    assert calculatrice_Number.__init__(calculatrice_Number(False, 0), False, 0) == None


from python_code import calculatrice_VarCall

def test_calculatrice_VarCall___init__():
    assert calculatrice_VarCall.__init__(calculatrice_VarCall(''), '') == None

