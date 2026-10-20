from python_code import GraphOperations_ConstantUtils

def test_GraphOperations_ConstantUtils___init__():
    assert GraphOperations_ConstantUtils.__init__(GraphOperations_ConstantUtils()) == None

def test_GraphOperations_ConstantUtils_getDouble():
    assert GraphOperations_ConstantUtils.getDouble(GraphOperations_ConstantUtils()) == None

def test_GraphOperations_ConstantUtils_getFloat():
    assert GraphOperations_ConstantUtils.getFloat(GraphOperations_ConstantUtils()) == None

def test_GraphOperations_ConstantUtils_getLong():
    assert GraphOperations_ConstantUtils.getLong(GraphOperations_ConstantUtils()) == None

def test_GraphOperations_ConstantUtils_getString():
    assert GraphOperations_ConstantUtils.getString(GraphOperations_ConstantUtils()) == None

def test_GraphOperations_ConstantUtils_getInt():
    assert GraphOperations_ConstantUtils.getInt(GraphOperations_ConstantUtils()) == None

def test_GraphOperations_ConstantUtils_getEdgeState():
    assert GraphOperations_ConstantUtils.getEdgeState(GraphOperations_ConstantUtils()) == None


from python_code import GraphOperations_EIntContainer

def test_GraphOperations_EIntContainer___init__():
    assert GraphOperations_EIntContainer.__init__(GraphOperations_EIntContainer(0), 0) == None

def test_GraphOperations_EIntContainer_increment():
    assert GraphOperations_EIntContainer.increment(GraphOperations_EIntContainer(0)) == None

def test_GraphOperations_EIntContainer_incrementBy():
    assert GraphOperations_EIntContainer.incrementBy(GraphOperations_EIntContainer(0), 0) == None


from python_code import GraphOperations_Element

def test_GraphOperations_Element___init__():
    assert GraphOperations_Element.__init__(GraphOperations_Element(''), '') == None

