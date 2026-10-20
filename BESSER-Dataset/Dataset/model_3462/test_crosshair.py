from python_code import featuremodels_SimpleAttribute

def test_featuremodels_SimpleAttribute___init__():
    assert featuremodels_SimpleAttribute.__init__(featuremodels_SimpleAttribute('', '\x00'), '\x00\x00', '') == None

