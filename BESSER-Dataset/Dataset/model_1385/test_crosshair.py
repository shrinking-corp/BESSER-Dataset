from python_code import lts2_LTSGenerator
from python_code import lts2_StateMachine

def test_lts2_LTSGenerator___init__():
    assert lts2_LTSGenerator.__init__(lts2_LTSGenerator(lts2_LTSGenerator=lts2_StateMachine()), lts2_LTSGenerator=lts2_StateMachine()) == None

def test_lts2_LTSGenerator_processUseCase():
    assert lts2_LTSGenerator.processUseCase(lts2_LTSGenerator(lts2_LTSGenerator=lts2_StateMachine()), '') == None

