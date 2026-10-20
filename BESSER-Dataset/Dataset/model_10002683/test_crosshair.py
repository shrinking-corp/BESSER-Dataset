from python_code import mypackage2_MyClass2

def test_mypackage2_MyClass2___init__():
    assert mypackage2_MyClass2.__init__(mypackage2_MyClass2('', 0.0, This_is_a0=set()), '', 0.0, This_is_a0=set()) == None


from python_code import mypackage3_MyClass3

def test_mypackage3_MyClass3___init__():
    assert mypackage3_MyClass3.__init__(mypackage3_MyClass3('', This_is_a1=set()), '', This_is_a1=set()) == None


from python_code import mypackage3_MyClass5

def test_mypackage3_MyClass5___init__():
    assert mypackage3_MyClass5.__init__(mypackage3_MyClass5(''), '') == None

