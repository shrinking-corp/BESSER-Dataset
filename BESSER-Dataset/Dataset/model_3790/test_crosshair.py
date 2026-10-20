from python_code import model_ComparisonProblem

def test_model_ComparisonProblem___init__():
    assert model_ComparisonProblem.__init__(model_ComparisonProblem('', '\x00'), '\x00\x00', '') == None


from python_code import model_Metadata

def test_model_Metadata___init__():
    assert model_Metadata.__init__(model_Metadata('', '\x00'), '\x00\x00', '') == None


from python_code import model_TestRoot

def test_model_TestRoot___init__():
    assert model_TestRoot.__init__(model_TestRoot(''), '') == None

