from python_code import kmLogo_ASM_Back
from python_code import kmLogo_ASM_BinaryExp
from python_code import kmLogo_ASM_Constant
from python_code import kmLogo_ASM_ControlStructure
from python_code import kmLogo_ASM_Forward
from python_code import kmLogo_ASM_Left
from python_code import kmLogo_ASM_ProcCall
from python_code import kmLogo_ASM_Right
from python_code import kmLogo_ASM_UnaryExpression

def test_kmLogo_ASM_Constant___init__():
    assert kmLogo_ASM_Constant.__init__(kmLogo_ASM_Constant(0.0, Expression8=kmLogo_ASM_BinaryExp(), Expression6=kmLogo_ASM_Right(), Expression28=kmLogo_ASM_ControlStructure(), Expression13=kmLogo_ASM_UnaryExpression(), Expression15=kmLogo_ASM_ProcCall(), Expression2=kmLogo_ASM_Forward(), Expression=kmLogo_ASM_Back(), Expression11=kmLogo_ASM_BinaryExp(), Expression4=kmLogo_ASM_Left()), 0.0, Expression8=kmLogo_ASM_BinaryExp(), Expression6=kmLogo_ASM_Right(), Expression28=kmLogo_ASM_ControlStructure(), Expression13=kmLogo_ASM_UnaryExpression(), Expression15=kmLogo_ASM_ProcCall(), Expression2=kmLogo_ASM_Forward(), Expression=kmLogo_ASM_Back(), Expression11=kmLogo_ASM_BinaryExp(), Expression4=kmLogo_ASM_Left()) == None


from python_code import kmLogo_ASM_Parameter

def test_kmLogo_ASM_Parameter___init__():
    assert kmLogo_ASM_Parameter.__init__(kmLogo_ASM_Parameter(''), '') == None

