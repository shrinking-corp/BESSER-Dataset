from python_code import effbd104_Flow
from python_code import effbd104_Item

def test_effbd104_Item___init__():
    assert effbd104_Item.__init__(effbd104_Item('', effbd104_Item=effbd104_Flow()), '', effbd104_Item=effbd104_Flow()) == None


from python_code import effbd104_Port

def test_effbd104_Port___init__():
    assert effbd104_Port.__init__(effbd104_Port(''), '') == None


from python_code import effbd104_ProcessNode

def test_effbd104_ProcessNode___init__():
    assert effbd104_ProcessNode.__init__(effbd104_ProcessNode(''), '') == None

