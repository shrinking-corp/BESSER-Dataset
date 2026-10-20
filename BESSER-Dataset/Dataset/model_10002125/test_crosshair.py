from python_code import Bewegungssensor

def test_Bewegungssensor___init__():
    assert Bewegungssensor.__init__(Bewegungssensor(0), 0) == None


from python_code import Fenstersensor

def test_Fenstersensor___init__():
    assert Fenstersensor.__init__(Fenstersensor(0), 0) == None


from python_code import Sensoren

def test_Sensoren___init__():
    assert Sensoren.__init__(Sensoren(0), 0) == None


from python_code import T_rsensor

def test_T_rsensor___init__():
    assert T_rsensor.__init__(T_rsensor(0), 0) == None

