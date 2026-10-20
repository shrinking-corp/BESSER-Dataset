from python_code import pDL1_Guidance

def test_pDL1_Guidance___init__():
    assert pDL1_Guidance.__init__(pDL1_Guidance(''), '') == None


from python_code import pDL1_Process

def test_pDL1_Process___init__():
    assert pDL1_Process.__init__(pDL1_Process('', pDL1_Process=set()), '', pDL1_Process=set()) == None

