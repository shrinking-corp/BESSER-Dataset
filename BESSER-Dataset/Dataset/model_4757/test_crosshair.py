from python_code import effbd103_Flow
from python_code import effbd103_Item

def test_effbd103_Item___init__():
    assert effbd103_Item.__init__(effbd103_Item('', effbd103_Item=effbd103_Flow()), '', effbd103_Item=effbd103_Flow()) == None


from python_code import effbd103_Port

def test_effbd103_Port___init__():
    assert effbd103_Port.__init__(effbd103_Port(''), '') == None


from python_code import effbd103_ProcessNode

def test_effbd103_ProcessNode___init__():
    assert effbd103_ProcessNode.__init__(effbd103_ProcessNode(''), '') == None

