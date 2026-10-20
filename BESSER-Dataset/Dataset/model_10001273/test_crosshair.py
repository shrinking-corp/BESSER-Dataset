from python_code import Class

def test_Class___init__():
    assert Class.__init__(Class(''), '') == None


from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('', 0, '', item12=set()), '', 0, '', item12=set()) == None

