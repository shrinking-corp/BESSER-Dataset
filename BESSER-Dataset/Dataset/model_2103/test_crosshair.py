from python_code import dft_Named

def test_dft_Named___init__():
    assert dft_Named.__init__(dft_Named(''), '') == None


from python_code import dft_Parametrized

def test_dft_Parametrized___init__():
    assert dft_Parametrized.__init__(dft_Parametrized('', '\x00'), '\x00\x00', '') == None

