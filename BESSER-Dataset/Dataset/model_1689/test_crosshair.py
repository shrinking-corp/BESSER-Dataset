from python_code import yyk_Boul

def test_yyk_Boul___init__():
    assert yyk_Boul.__init__(yyk_Boul(''), '') == None


from python_code import yyk_Bouz

def test_yyk_Bouz___init__():
    assert yyk_Bouz.__init__(yyk_Bouz('', yyk_Bouz=set()), '', yyk_Bouz=set()) == None

