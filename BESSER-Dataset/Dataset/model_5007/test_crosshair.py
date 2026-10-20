from python_code import epo2_GlobalAddress

def test_epo2_GlobalAddress___init__():
    assert epo2_GlobalAddress.__init__(epo2_GlobalAddress(''), '') == None


from python_code import epo2_GlobalLocation

def test_epo2_GlobalLocation___init__():
    assert epo2_GlobalLocation.__init__(epo2_GlobalLocation(0), 0) == None


from python_code import epo2_USAddress

def test_epo2_USAddress___init__():
    assert epo2_USAddress.__init__(epo2_USAddress('\x00\x00', '', '', ''), '', '', '', '') == None

