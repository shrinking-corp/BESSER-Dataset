from python_code import effbd902_Flow
from python_code import effbd902_Item

def test_effbd902_Item___init__():
    assert effbd902_Item.__init__(effbd902_Item('', effbd902_Item=effbd902_Flow()), '', effbd902_Item=effbd902_Flow()) == None


from python_code import effbd902_Port

def test_effbd902_Port___init__():
    assert effbd902_Port.__init__(effbd902_Port(''), '') == None


from python_code import effbd902_ProcessNode

def test_effbd902_ProcessNode___init__():
    assert effbd902_ProcessNode.__init__(effbd902_ProcessNode(''), '') == None

