from python_code import kmLogo_ASM_Back
from python_code import kmLogo_ASM_BinaryExp
from python_code import kmLogo_ASM_Constant
from python_code import kmLogo_ASM_ControlStructure
from python_code import kmLogo_ASM_Forward
from python_code import kmLogo_ASM_Left
from python_code import kmLogo_ASM_ProcCall
from python_code import kmLogo_ASM_Right

def test_kmLogo_ASM_Constant___init__():
    assert kmLogo_ASM_Constant.__init__(kmLogo_ASM_Constant('', Expression8=kmLogo_ASM_BinaryExp(), Expression13=kmLogo_ASM_ProcCall(), Expression2=kmLogo_ASM_Forward(), Expression4=kmLogo_ASM_Left(), Expression=kmLogo_ASM_Back(), Expression26=kmLogo_ASM_ControlStructure(), Expression11=kmLogo_ASM_BinaryExp(), Expression6=kmLogo_ASM_Right()), '', Expression8=kmLogo_ASM_BinaryExp(), Expression13=kmLogo_ASM_ProcCall(), Expression2=kmLogo_ASM_Forward(), Expression4=kmLogo_ASM_Left(), Expression=kmLogo_ASM_Back(), Expression26=kmLogo_ASM_ControlStructure(), Expression11=kmLogo_ASM_BinaryExp(), Expression6=kmLogo_ASM_Right()) == None


from python_code import kmLogo_ASM_Parameter

def test_kmLogo_ASM_Parameter___init__():
    assert kmLogo_ASM_Parameter.__init__(kmLogo_ASM_Parameter(''), '') == None

