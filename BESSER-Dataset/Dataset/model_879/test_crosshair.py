from python_code import simplepdl_Guidance

def test_simplepdl_Guidance___init__():
    assert simplepdl_Guidance.__init__(simplepdl_Guidance('', simplepdl_Guidance=set()), '', simplepdl_Guidance=set()) == None


from python_code import simplepdl_Parameter
from python_code import simplepdl_ParameterSWD

def test_simplepdl_Parameter___init__():
    assert simplepdl_Parameter.__init__(simplepdl_Parameter('', 0, simplepdl_Parameter=simplepdl_ParameterSWD()), '', 0, simplepdl_Parameter=simplepdl_ParameterSWD()) == None


from python_code import simplepdl_Process

def test_simplepdl_Process___init__():
    assert simplepdl_Process.__init__(simplepdl_Process('', 0, 0, simplepdl_Process=set(), simplepdl_Process2=set()), '', 0, 0, simplepdl_Process=set(), simplepdl_Process2=set()) == None

