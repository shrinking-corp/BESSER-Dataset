from python_code import mil_ConstantInteger

def test_mil_ConstantInteger___init__():
    assert mil_ConstantInteger.__init__(mil_ConstantInteger(0), 0) == None


from python_code import mil_JumpMarker
from python_code import mil_Jumper

def test_mil_JumpMarker___init__():
    assert mil_JumpMarker.__init__(mil_JumpMarker('', mil_JumpMarker=mil_Jumper()), '', mil_JumpMarker=mil_Jumper()) == None


from python_code import mil_PrintInstruction

def test_mil_PrintInstruction___init__():
    assert mil_PrintInstruction.__init__(mil_PrintInstruction(''), '') == None


from python_code import mil_RegisterReference
from python_code import mil_StoreInstruction

def test_mil_RegisterReference___init__():
    assert mil_RegisterReference.__init__(mil_RegisterReference('', mil_RegisterReference=mil_StoreInstruction()), '', mil_RegisterReference=mil_StoreInstruction()) == None

