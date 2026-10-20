from python_code import MM1_B

def test_MM1_B___init__():
    assert MM1_B.__init__(MM1_B(0), 0) == None


from python_code import MM1_C

def test_MM1_C___init__():
    assert MM1_C.__init__(MM1_C(True), False) == None


from python_code import MM1_ContainerMM1

def test_MM1_ContainerMM1___init__():
    assert MM1_ContainerMM1.__init__(MM1_ContainerMM1(0, MM1_ContainerMM1=set(), MM1_ContainerMM12=set()), 0, MM1_ContainerMM1=set(), MM1_ContainerMM12=set()) == None

