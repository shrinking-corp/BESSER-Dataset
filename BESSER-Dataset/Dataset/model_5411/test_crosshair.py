from python_code import dynamicFaultTree_DFT
from python_code import dynamicFaultTree_TopLevelEvent

def test_dynamicFaultTree_DFT___init__():
    assert dynamicFaultTree_DFT.__init__(dynamicFaultTree_DFT('', dynamicFaultTree_DFT=dynamicFaultTree_TopLevelEvent(), dynamicFaultTree_DFT2=set()), '', dynamicFaultTree_DFT=dynamicFaultTree_TopLevelEvent(), dynamicFaultTree_DFT2=set()) == None


from python_code import dynamicFaultTree_Element

def test_dynamicFaultTree_Element___init__():
    assert dynamicFaultTree_Element.__init__(dynamicFaultTree_Element('', 0.0, 0, 0), '', 0.0, 0, 0) == None

