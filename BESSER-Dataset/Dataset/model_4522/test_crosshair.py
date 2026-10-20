from python_code import PrimitivesProv_Instruction
from python_code import PrimitivesProv_LogoProgram

def test_PrimitivesProv_Instruction___init__():
    assert PrimitivesProv_Instruction.__init__(PrimitivesProv_Instruction(PrimitivesProv_Instruction=PrimitivesProv_LogoProgram()), PrimitivesProv_Instruction=PrimitivesProv_LogoProgram()) == None

def test_PrimitivesProv_Instruction_evalInstruction():
    assert PrimitivesProv_Instruction.evalInstruction(PrimitivesProv_Instruction(PrimitivesProv_Instruction=PrimitivesProv_LogoProgram()), '') == None

