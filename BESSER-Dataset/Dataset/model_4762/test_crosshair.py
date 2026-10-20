from python_code import effbd101_Description
from python_code import effbd101_Function

def test_effbd101_Description___init__():
    assert effbd101_Description.__init__(effbd101_Description('', effbd101_Description=effbd101_Function()), '', effbd101_Description=effbd101_Function()) == None


from python_code import effbd101_Flow
from python_code import effbd101_Item

def test_effbd101_Item___init__():
    assert effbd101_Item.__init__(effbd101_Item('', effbd101_Item=effbd101_Flow()), '', effbd101_Item=effbd101_Flow()) == None


from python_code import effbd101_Port

def test_effbd101_Port___init__():
    assert effbd101_Port.__init__(effbd101_Port(''), '') == None


from python_code import effbd101_ProcessNode

def test_effbd101_ProcessNode___init__():
    assert effbd101_ProcessNode.__init__(effbd101_ProcessNode(''), '') == None

