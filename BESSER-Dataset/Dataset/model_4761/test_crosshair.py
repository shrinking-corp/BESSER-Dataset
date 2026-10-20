from python_code import effbd102_Flow
from python_code import effbd102_Item

def test_effbd102_Item___init__():
    assert effbd102_Item.__init__(effbd102_Item('', effbd102_Item=effbd102_Flow()), '', effbd102_Item=effbd102_Flow()) == None


from python_code import effbd102_Port

def test_effbd102_Port___init__():
    assert effbd102_Port.__init__(effbd102_Port(''), '') == None


from python_code import effbd102_ProcessNode

def test_effbd102_ProcessNode___init__():
    assert effbd102_ProcessNode.__init__(effbd102_ProcessNode(''), '') == None

