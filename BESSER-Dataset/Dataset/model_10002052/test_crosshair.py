from python_code import Admin_staff

def test_Admin_staff___init__():
    assert Admin_staff.__init__(Admin_staff('', '', '\x00\x00'), '', '', '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None

