from python_code import gedcoml_Others

def test_gedcoml_Others___init__():
    assert gedcoml_Others.__init__(gedcoml_Others(''), '') == None


from python_code import gedcoml_PostAddress

def test_gedcoml_PostAddress___init__():
    assert gedcoml_PostAddress.__init__(gedcoml_PostAddress('', '', '\x00\x00'), '', '', '') == None

