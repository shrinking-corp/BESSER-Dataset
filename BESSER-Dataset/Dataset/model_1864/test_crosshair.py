from python_code import decobat_Service

def test_decobat_Service___init__():
    assert decobat_Service.__init__(decobat_Service('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

