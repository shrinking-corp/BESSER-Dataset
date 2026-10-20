from python_code import post

def test_post___init__():
    assert post.__init__(post(0, '\x00', lineItems10=set()), 0, '', lineItems10=set()) == None

