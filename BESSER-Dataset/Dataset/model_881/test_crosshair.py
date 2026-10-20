from python_code import simplepdl_Guidance

def test_simplepdl_Guidance___init__():
    assert simplepdl_Guidance.__init__(simplepdl_Guidance('', simplepdl_Guidance=set()), '', simplepdl_Guidance=set()) == None


from python_code import simplepdl_Process
from python_code import simplepdl_ProcessElement

def test_simplepdl_Process___init__():
    assert simplepdl_Process.__init__(simplepdl_Process('', process=set(), Process=simplepdl_ProcessElement()), '', process=set(), Process=simplepdl_ProcessElement()) == None

