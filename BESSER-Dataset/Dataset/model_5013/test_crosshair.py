from python_code import epo_CanadianAddress

def test_epo_CanadianAddress___init__():
    assert epo_CanadianAddress.__init__(epo_CanadianAddress('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import epo_GlobalAddress

def test_epo_GlobalAddress___init__():
    assert epo_GlobalAddress.__init__(epo_GlobalAddress(''), '') == None


from python_code import epo_GlobalLocation

def test_epo_GlobalLocation___init__():
    assert epo_GlobalLocation.__init__(epo_GlobalLocation(0), 0) == None


from python_code import epo_USAddress

def test_epo_USAddress___init__():
    assert epo_USAddress.__init__(epo_USAddress('\x00\x00', '', '', 0), '', '', '', 0) == None

