from python_code import extendedPO2_GlobalAddress

def test_extendedPO2_GlobalAddress___init__():
    assert extendedPO2_GlobalAddress.__init__(extendedPO2_GlobalAddress(''), '') == None


from python_code import extendedPO2_USAddress

def test_extendedPO2_USAddress___init__():
    assert extendedPO2_USAddress.__init__(extendedPO2_USAddress('\x00\x00', '', '', 0), '', '', '', 0) == None

