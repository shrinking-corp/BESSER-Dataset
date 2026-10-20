from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('', store41=set()), '', store41=set()) == None


from python_code import Service

def test_Service___init__():
    assert Service.__init__(Service('\x00\x00', '', store43=set()), '', '', store43=set()) == None

