from python_code import mil_ConstantInteger
from python_code import mil_InpInstruction

def test_mil_ConstantInteger___init__():
    assert mil_ConstantInteger.__init__(mil_ConstantInteger(0, mil_ConstantInteger=mil_InpInstruction(), mil_ConstantInteger7=mil_InpInstruction()), 0, mil_ConstantInteger=mil_InpInstruction(), mil_ConstantInteger7=mil_InpInstruction()) == None


from python_code import mil_JumpInstruction
from python_code import mil_LabelInstruction

def test_mil_LabelInstruction___init__():
    assert mil_LabelInstruction.__init__(mil_LabelInstruction('', mil_LabelInstruction=mil_JumpInstruction()), '', mil_LabelInstruction=mil_JumpInstruction()) == None


from python_code import mil_PrtInstruction

def test_mil_PrtInstruction___init__():
    assert mil_PrtInstruction.__init__(mil_PrtInstruction(''), '') == None


from python_code import mil_RegisterReference
from python_code import mil_StoreInstruction

def test_mil_RegisterReference___init__():
    assert mil_RegisterReference.__init__(mil_RegisterReference('', mil_RegisterReference=mil_StoreInstruction()), '', mil_RegisterReference=mil_StoreInstruction()) == None

