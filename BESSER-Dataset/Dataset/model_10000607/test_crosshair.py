from python_code import People

def test_People___init__():
    assert People.__init__(People('', '', '\x00\x00'), '', '', '') == None


from python_code import Worker

def test_Worker___init__():
    assert Worker.__init__(Worker('', '', '\x00\x00'), '', '', '') == None

