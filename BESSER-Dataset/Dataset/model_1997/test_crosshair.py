from python_code import iTrace_Block
from python_code import iTrace_Code
from python_code import iTrace_M2TLink

def test_iTrace_Block___init__():
    assert iTrace_Block.__init__(iTrace_Block(0, 0, 0, 0, 0, Block17=iTrace_Code(), Block=iTrace_M2TLink(), blocks=iTrace_Code(), targetBlocks=iTrace_M2TLink()), 0, 0, 0, 0, 0, Block17=iTrace_Code(), Block=iTrace_M2TLink(), blocks=iTrace_Code(), targetBlocks=iTrace_M2TLink()) == None

