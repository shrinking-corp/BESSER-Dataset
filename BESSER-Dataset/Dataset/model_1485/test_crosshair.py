from python_code import petriNetEMF_Identification

def test_petriNetEMF_Identification___init__():
    assert petriNetEMF_Identification.__init__(petriNetEMF_Identification('', '\x00'), '\x00\x00', '') == None

