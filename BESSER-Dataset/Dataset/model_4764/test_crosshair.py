from python_code import itemflow101_Description
from python_code import itemflow101_Function

def test_itemflow101_Description___init__():
    assert itemflow101_Description.__init__(itemflow101_Description('', itemflow101_Description=itemflow101_Function()), '', itemflow101_Description=itemflow101_Function()) == None


from python_code import itemflow101_Flow
from python_code import itemflow101_Item

def test_itemflow101_Item___init__():
    assert itemflow101_Item.__init__(itemflow101_Item('', itemflow101_Item=itemflow101_Flow()), '', itemflow101_Item=itemflow101_Flow()) == None


from python_code import itemflow101_Port

def test_itemflow101_Port___init__():
    assert itemflow101_Port.__init__(itemflow101_Port(''), '') == None


from python_code import itemflow101_ProcessNode

def test_itemflow101_ProcessNode___init__():
    assert itemflow101_ProcessNode.__init__(itemflow101_ProcessNode(''), '') == None

