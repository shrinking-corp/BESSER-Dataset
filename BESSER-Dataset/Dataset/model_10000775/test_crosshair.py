from python_code import MyClass

def test_MyClass___init__():
    assert MyClass.__init__(MyClass('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('', '', '', '', '', '', '', '', '', '', item12=set()), '\x00', '', '', '', '', '', '', '', '', '', item12=set()) == None

