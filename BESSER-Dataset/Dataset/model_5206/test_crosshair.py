from python_code import FaultyUMLmodel_A

def test_FaultyUMLmodel_A___init__():
    assert FaultyUMLmodel_A.__init__(FaultyUMLmodel_A(0, False), 0, False) == None


from python_code import FaultyUMLmodel_B

def test_FaultyUMLmodel_B___init__():
    assert FaultyUMLmodel_B.__init__(FaultyUMLmodel_B(0, 0), 0, 0) == None


from python_code import FaultyUMLmodel_C

def test_FaultyUMLmodel_C___init__():
    assert FaultyUMLmodel_C.__init__(FaultyUMLmodel_C(0), 0) == None


from python_code import FaultyUMLmodel_D

def test_FaultyUMLmodel_D___init__():
    assert FaultyUMLmodel_D.__init__(FaultyUMLmodel_D(True), False) == None

