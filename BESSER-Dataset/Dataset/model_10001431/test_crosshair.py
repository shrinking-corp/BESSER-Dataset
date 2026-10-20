from python_code import bill

def test_bill___init__():
    assert bill.__init__(bill(0, 0, '\x00\x00'), 0, 0, '') == None

