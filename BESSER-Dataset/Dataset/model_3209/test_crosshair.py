from python_code import llp_CommitInstruction
from python_code import llp_IOInstruction
from python_code import llp_MemoryReference
from python_code import llp_SynchronisationInstruction

def test_llp_MemoryReference___init__():
    assert llp_MemoryReference.__init__(llp_MemoryReference('', llp_MemoryReference=llp_IOInstruction(), llp_MemoryReference10=llp_CommitInstruction(), llp_MemoryReference21=llp_SynchronisationInstruction()), '', llp_MemoryReference=llp_IOInstruction(), llp_MemoryReference10=llp_CommitInstruction(), llp_MemoryReference21=llp_SynchronisationInstruction()) == None


from python_code import llp_Block
from python_code import llp_RepetitionInstruction

def test_llp_RepetitionInstruction___init__():
    assert llp_RepetitionInstruction.__init__(llp_RepetitionInstruction(0, llp_RepetitionInstruction=llp_Block()), 0, llp_RepetitionInstruction=llp_Block()) == None


from python_code import llp_Block
from python_code import llp_LowLevelProgram
from python_code import llp_SpawnInstruction
from python_code import llp_Task

def test_llp_Task___init__():
    assert llp_Task.__init__(llp_Task('', llp_Task=llp_LowLevelProgram(), llp_Task4=llp_Block(), llp_Task12=llp_SpawnInstruction()), '', llp_Task=llp_LowLevelProgram(), llp_Task4=llp_Block(), llp_Task12=llp_SpawnInstruction()) == None

