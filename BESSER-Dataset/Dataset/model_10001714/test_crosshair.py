from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer(0, 0, '', '', ''), 0, 0, '', '', '') == None


from python_code import checkingAccount

def test_checkingAccount___init__():
    assert checkingAccount.__init__(checkingAccount(0, 0), 0, 0) == None


from python_code import savingAccount

def test_savingAccount___init__():
    assert savingAccount.__init__(savingAccount('', '', '\x00\x00'), '', '', '') == None

