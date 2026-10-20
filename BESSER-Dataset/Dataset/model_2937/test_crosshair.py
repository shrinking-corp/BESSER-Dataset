from python_code import test7_FiniteDomainSC
from python_code import test7_FiniteDomainSCValueReference

def test_test7_FiniteDomainSCValueReference___init__():
    assert test7_FiniteDomainSCValueReference.__init__(test7_FiniteDomainSCValueReference('', test7_FiniteDomainSCValueReference=test7_FiniteDomainSC()), '', test7_FiniteDomainSCValueReference=test7_FiniteDomainSC()) == None


from python_code import test7_Model
from python_code import test7_SolutionConstraint

def test_test7_SolutionConstraint___init__():
    assert test7_SolutionConstraint.__init__(test7_SolutionConstraint('', '\x00', test7_SolutionConstraint=test7_Model()), '\x00\x00', '', test7_SolutionConstraint=test7_Model()) == None

