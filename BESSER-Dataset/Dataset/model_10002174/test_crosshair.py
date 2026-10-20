from python_code import ImageQuestion

def test_ImageQuestion___init__():
    assert ImageQuestion.__init__(ImageQuestion(''), '') == None


from python_code import SoundQuestion

def test_SoundQuestion___init__():
    assert SoundQuestion.__init__(SoundQuestion(''), '') == None


from python_code import TextQuestion

def test_TextQuestion___init__():
    assert TextQuestion.__init__(TextQuestion('', False), '', False) == None


from python_code import User

def test_User___init__():
    assert User.__init__(User('', '', 0, '', '', '', has_users10=set(), has_owner13=set(), has_owner19=set(), has_owner8=set()), '\x00', '', 0, '', '', '', has_users10=set(), has_owner13=set(), has_owner19=set(), has_owner8=set()) == None

