from python_code import effbd201_Flow
from python_code import effbd201_Item

def test_effbd201_Item___init__():
    assert effbd201_Item.__init__(effbd201_Item('', effbd201_Item=effbd201_Flow()), '', effbd201_Item=effbd201_Flow()) == None


from python_code import effbd201_Flow
from python_code import effbd201_Port

def test_effbd201_Port___init__():
    assert effbd201_Port.__init__(effbd201_Port('', effbd201_Port20=effbd201_Flow(), effbd201_Port=set()), '', effbd201_Port20=effbd201_Flow(), effbd201_Port=set()) == None


from python_code import effbd201_ProcessNode

def test_effbd201_ProcessNode___init__():
    assert effbd201_ProcessNode.__init__(effbd201_ProcessNode(''), '') == None

