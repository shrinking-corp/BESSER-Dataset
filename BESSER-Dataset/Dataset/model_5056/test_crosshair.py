from python_code import cbpmn_DecisionGateway

def test_cbpmn_DecisionGateway___init__():
    assert cbpmn_DecisionGateway.__init__(cbpmn_DecisionGateway(''), '') == None

def test_cbpmn_DecisionGateway_addBranchWithCondition():
    assert cbpmn_DecisionGateway.addBranchWithCondition(cbpmn_DecisionGateway(''), 0, '\x00\x00', '') == None

def test_cbpmn_DecisionGateway_getDefaultBranch():
    assert cbpmn_DecisionGateway.getDefaultBranch(cbpmn_DecisionGateway('')) == None

def test_cbpmn_DecisionGateway_getRandomBranch():
    assert cbpmn_DecisionGateway.getRandomBranch(cbpmn_DecisionGateway('')) == None

