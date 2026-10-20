from python_code import sourcecleaner_LocatedElement

def test_sourcecleaner_LocatedElement___init__():
    assert sourcecleaner_LocatedElement.__init__(sourcecleaner_LocatedElement('', '\x00'), '\x00\x00', '') == None


from python_code import sourcecleaner_Source

def test_sourcecleaner_Source___init__():
    assert sourcecleaner_Source.__init__(sourcecleaner_Source('\x00\x00', False, False, ''), '', False, False, '') == None

