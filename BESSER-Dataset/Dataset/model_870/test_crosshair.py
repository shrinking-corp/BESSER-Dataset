from python_code import simplepdl_Guidance

def test_simplepdl_Guidance___init__():
    assert simplepdl_Guidance.__init__(simplepdl_Guidance('', simplepdl_Guidance=set()), '', simplepdl_Guidance=set()) == None


from python_code import simplepdl_Process

def test_simplepdl_Process___init__():
    assert simplepdl_Process.__init__(simplepdl_Process('', simplepdl_Process=set()), '', simplepdl_Process=set()) == None


from python_code import simplepdl_Ressource

def test_simplepdl_Ressource___init__():
    assert simplepdl_Ressource.__init__(simplepdl_Ressource('', 0), '', 0) == None

