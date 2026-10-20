from python_code import Payment

def test_Payment___init__():
    assert Payment.__init__(Payment(0, '\x00'), 0, '\x00') == None

