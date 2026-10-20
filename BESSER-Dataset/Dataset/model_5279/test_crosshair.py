from python_code import sample_SampleClassA
from python_code import sample_SampleClassC

def test_sample_SampleClassA___init__():
    assert sample_SampleClassA.__init__(sample_SampleClassA('', sample_SampleClassA=sample_SampleClassC()), '', sample_SampleClassA=sample_SampleClassC()) == None


from python_code import sample_SampleClassInterface

def test_sample_SampleClassInterface___init__():
    assert sample_SampleClassInterface.__init__(sample_SampleClassInterface()) == None

def test_sample_SampleClassInterface_doSomething():
    assert sample_SampleClassInterface.doSomething(sample_SampleClassInterface(), '') == None

