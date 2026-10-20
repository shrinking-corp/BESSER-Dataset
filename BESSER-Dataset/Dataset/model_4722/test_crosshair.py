from python_code import Model_AtomicDEVS
from python_code import Model_Phase
from python_code import Model_PhaseTransition

def test_Model_Phase___init__():
    assert Model_Phase.__init__(Model_Phase('', 0.0, Model_Phase63=set(), Model_Phase66=Model_PhaseTransition(), Model_Phase69=Model_PhaseTransition(), Model_Phase=Model_AtomicDEVS()), '', 0.0, Model_Phase63=set(), Model_Phase66=Model_PhaseTransition(), Model_Phase69=Model_PhaseTransition(), Model_Phase=Model_AtomicDEVS()) == None

