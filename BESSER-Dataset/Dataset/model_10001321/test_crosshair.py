from python_code import login

def test_login___init__():
    assert login.__init__(login('', '\x00'), '\x00\x00', '') == None


from python_code import pay

def test_pay___init__():
    assert pay.__init__(pay(''), '') == None


from python_code import person

def test_person___init__():
    assert person.__init__(person('\x00\x00', '', '', ''), '', '', '', '') == None

