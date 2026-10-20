from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer(0, '', '', '', 0), 0, '', '', '', 0) == None

