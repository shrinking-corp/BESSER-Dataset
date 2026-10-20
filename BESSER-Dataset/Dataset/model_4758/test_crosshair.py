from python_code import effbd106_Flow
from python_code import effbd106_Item

def test_effbd106_Item___init__():
    assert effbd106_Item.__init__(effbd106_Item('', effbd106_Item=effbd106_Flow()), '', effbd106_Item=effbd106_Flow()) == None


from python_code import effbd106_Port

def test_effbd106_Port___init__():
    assert effbd106_Port.__init__(effbd106_Port(''), '') == None


from python_code import effbd106_ProcessNode

def test_effbd106_ProcessNode___init__():
    assert effbd106_ProcessNode.__init__(effbd106_ProcessNode(''), '') == None

