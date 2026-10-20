from python_code import model1_Address

def test_model1_Address___init__():
    assert model1_Address.__init__(model1_Address('', '', '\x00\x00'), '', '', '') == None


from python_code import model1_OrderAddress

def test_model1_OrderAddress___init__():
    assert model1_OrderAddress.__init__(model1_OrderAddress(True), False) == None

