from python_code import simplepdl_Guidance
from python_code import simplepdl_ProcessElements

def test_simplepdl_Guidance___init__():
    assert simplepdl_Guidance.__init__(simplepdl_Guidance('', simplepdl_Guidance=simplepdl_ProcessElements()), '', simplepdl_Guidance=simplepdl_ProcessElements()) == None


from python_code import simplepdl_Process

def test_simplepdl_Process___init__():
    assert simplepdl_Process.__init__(simplepdl_Process('', simplepdl_Process=set()), '', simplepdl_Process=set()) == None

