from python_code import candyCrushPackage_RegularCandy

def test_candyCrushPackage_RegularCandy___init__():
    assert candyCrushPackage_RegularCandy.__init__(candyCrushPackage_RegularCandy(False, 0), False, 0) == None


from python_code import candyCrushPackage_StrippedCandy

def test_candyCrushPackage_StrippedCandy___init__():
    assert candyCrushPackage_StrippedCandy.__init__(candyCrushPackage_StrippedCandy(True), False) == None


from python_code import candyCrushPackage_WrappedCandy

def test_candyCrushPackage_WrappedCandy___init__():
    assert candyCrushPackage_WrappedCandy.__init__(candyCrushPackage_WrappedCandy(0), 0) == None

