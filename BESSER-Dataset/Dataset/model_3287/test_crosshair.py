from python_code import dSLPolicies_AlgorithmType
from python_code import dSLPolicies_PathGeneratorStopCondition

def test_dSLPolicies_AlgorithmType___init__():
    assert dSLPolicies_AlgorithmType.__init__(dSLPolicies_AlgorithmType('', dSLPolicies_AlgorithmType=dSLPolicies_PathGeneratorStopCondition()), '', dSLPolicies_AlgorithmType=dSLPolicies_PathGeneratorStopCondition()) == None


from python_code import dSLPolicies_GraphPolicies
from python_code import dSLPolicies_Model

def test_dSLPolicies_GraphPolicies___init__():
    assert dSLPolicies_GraphPolicies.__init__(dSLPolicies_GraphPolicies('', dSLPolicies_GraphPolicies=dSLPolicies_Model(), dSLPolicies_GraphPolicies2=set()), '', dSLPolicies_GraphPolicies=dSLPolicies_Model(), dSLPolicies_GraphPolicies2=set()) == None

