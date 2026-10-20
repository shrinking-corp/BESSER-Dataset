from python_code import forcing_ForcingDiseaseModel

def test_forcing_ForcingDiseaseModel___init__():
    assert forcing_ForcingDiseaseModel.__init__(forcing_ForcingDiseaseModel(0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0) == None


from python_code import forcing_Gaussian2ForcingDiseaseModel

def test_forcing_Gaussian2ForcingDiseaseModel___init__():
    assert forcing_Gaussian2ForcingDiseaseModel.__init__(forcing_Gaussian2ForcingDiseaseModel(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), 0.0, 0.0, float('nan'), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0) == None


from python_code import forcing_Gaussian3ForcingDiseaseModel

def test_forcing_Gaussian3ForcingDiseaseModel___init__():
    assert forcing_Gaussian3ForcingDiseaseModel.__init__(forcing_Gaussian3ForcingDiseaseModel(0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0) == None


from python_code import forcing_GaussianForcingDiseaseModel

def test_forcing_GaussianForcingDiseaseModel___init__():
    assert forcing_GaussianForcingDiseaseModel.__init__(forcing_GaussianForcingDiseaseModel(0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0) == None

