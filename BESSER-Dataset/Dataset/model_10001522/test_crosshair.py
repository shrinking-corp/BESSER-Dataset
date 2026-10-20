from python_code import CSV

def test_CSV___init__():
    assert CSV.__init__(CSV('', '\x00'), '\x00\x00', '') == None


from python_code import XML

def test_XML___init__():
    assert XML.__init__(XML('', '\x00'), '\x00\x00', '') == None

