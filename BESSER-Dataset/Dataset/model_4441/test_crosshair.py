from python_code import roverml_NamedElement

def test_roverml_NamedElement___init__():
    assert roverml_NamedElement.__init__(roverml_NamedElement(''), '') == None


from python_code import roverml_Repeat

def test_roverml_Repeat___init__():
    assert roverml_Repeat.__init__(roverml_Repeat(0, roverml_Repeat=set()), 0, roverml_Repeat=set()) == None


from python_code import roverml_SetLightColor

def test_roverml_SetLightColor___init__():
    assert roverml_SetLightColor.__init__(roverml_SetLightColor(''), '') == None


from python_code import roverml_Triggered

def test_roverml_Triggered___init__():
    assert roverml_Triggered.__init__(roverml_Triggered(''), '') == None

