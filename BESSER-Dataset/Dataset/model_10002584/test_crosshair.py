from python_code import Public

def test_Public___init__():
    assert Public.__init__(Public(''), '') == None


from python_code import Secret

def test_Secret___init__():
    assert Secret.__init__(Secret(''), '') == None

