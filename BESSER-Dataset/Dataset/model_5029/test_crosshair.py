from python_code import cbpmn_DecisionGateway

def test_cbpmn_DecisionGateway___init__():
    assert cbpmn_DecisionGateway.__init__(cbpmn_DecisionGateway('\x00', cbpmn_DecisionGateway=set()), '', cbpmn_DecisionGateway=set()) == None

def test_cbpmn_DecisionGateway_addBranchWithCondition():
    assert cbpmn_DecisionGateway.addBranchWithCondition(cbpmn_DecisionGateway('', cbpmn_DecisionGateway=set()), '', 0, '') == None

