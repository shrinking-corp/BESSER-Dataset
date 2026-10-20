from python_code import publicGroup

def test_publicGroup___init__():
    assert publicGroup.__init__(publicGroup(''), '') == None


from python_code import secretGroup

def test_secretGroup___init__():
    assert secretGroup.__init__(secretGroup(''), '') == None

