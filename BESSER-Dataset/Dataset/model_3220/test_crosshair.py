from python_code import mil_ConstantInteger

def test_mil_ConstantInteger___init__():
    assert mil_ConstantInteger.__init__(mil_ConstantInteger(0), 0) == None


from python_code import mil_CallInstruction
from python_code import mil_JumpInstruction
from python_code import mil_LabelInstruction

def test_mil_LabelInstruction___init__():
    assert mil_LabelInstruction.__init__(mil_LabelInstruction('', mil_LabelInstruction=mil_JumpInstruction(), mil_LabelInstruction5=mil_CallInstruction()), '', mil_LabelInstruction=mil_JumpInstruction(), mil_LabelInstruction5=mil_CallInstruction()) == None


from python_code import mil_PrintInstruction

def test_mil_PrintInstruction___init__():
    assert mil_PrintInstruction.__init__(mil_PrintInstruction(''), '') == None


from python_code import mil_RegisterReference
from python_code import mil_StoreInstruction

def test_mil_RegisterReference___init__():
    assert mil_RegisterReference.__init__(mil_RegisterReference('', mil_RegisterReference=mil_StoreInstruction()), '', mil_RegisterReference=mil_StoreInstruction()) == None

