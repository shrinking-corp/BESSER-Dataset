from python_code import model_NormalDistribution

def test_model_NormalDistribution___init__():
    assert model_NormalDistribution.__init__(model_NormalDistribution(0.0, 0.0), 0.0, 0.0) == None


from python_code import model_Sampling

def test_model_Sampling___init__():
    assert model_Sampling.__init__(model_Sampling('', model_Sampling=set()), '', model_Sampling=set()) == None

