from python_code import kmlogo_asm_Back
from python_code import kmlogo_asm_BinaryExp
from python_code import kmlogo_asm_Constant
from python_code import kmlogo_asm_ControlStructure
from python_code import kmlogo_asm_Forward
from python_code import kmlogo_asm_Left
from python_code import kmlogo_asm_ProcCall
from python_code import kmlogo_asm_Right

def test_kmlogo_asm_Constant___init__():
    assert kmlogo_asm_Constant.__init__(kmlogo_asm_Constant('', Expression11=kmlogo_asm_BinaryExp(), Expression4=kmlogo_asm_Left(), Expression8=kmlogo_asm_BinaryExp(), Expression6=kmlogo_asm_Right(), Expression26=kmlogo_asm_ControlStructure(), Expression=kmlogo_asm_Back(), Expression2=kmlogo_asm_Forward(), Expression13=kmlogo_asm_ProcCall()), '', Expression11=kmlogo_asm_BinaryExp(), Expression4=kmlogo_asm_Left(), Expression8=kmlogo_asm_BinaryExp(), Expression6=kmlogo_asm_Right(), Expression26=kmlogo_asm_ControlStructure(), Expression=kmlogo_asm_Back(), Expression2=kmlogo_asm_Forward(), Expression13=kmlogo_asm_ProcCall()) == None


from python_code import kmlogo_asm_Parameter

def test_kmlogo_asm_Parameter___init__():
    assert kmlogo_asm_Parameter.__init__(kmlogo_asm_Parameter(''), '') == None

