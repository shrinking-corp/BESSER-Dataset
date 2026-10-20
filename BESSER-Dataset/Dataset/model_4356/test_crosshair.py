from python_code import mpl_Comparison
from python_code import mpl_Expression
from python_code import mpl_IfStatement
from python_code import mpl_WhileLoop

def test_mpl_Comparison___init__():
    assert mpl_Comparison.__init__(mpl_Comparison('', mpl_Comparison37=mpl_WhileLoop(), mpl_Comparison=mpl_IfStatement(), mpl_Comparison28=mpl_Expression(), mpl_Comparison31=mpl_Expression()), '', mpl_Comparison37=mpl_WhileLoop(), mpl_Comparison=mpl_IfStatement(), mpl_Comparison28=mpl_Expression(), mpl_Comparison31=mpl_Expression()) == None


from python_code import mpl_Assignment
from python_code import mpl_Block
from python_code import mpl_Expression
from python_code import mpl_ForLoop

def test_mpl_ForLoop___init__():
    assert mpl_ForLoop.__init__(mpl_ForLoop(True, mpl_ForLoop=mpl_Block(), mpl_ForLoop41=mpl_Assignment(), mpl_ForLoop44=mpl_Expression()), False, mpl_ForLoop=mpl_Block(), mpl_ForLoop41=mpl_Assignment(), mpl_ForLoop44=mpl_Expression()) == None


from python_code import mpl_LiteralValue

def test_mpl_LiteralValue___init__():
    assert mpl_LiteralValue.__init__(mpl_LiteralValue(0), 0) == None


from python_code import mpl_Block
from python_code import mpl_MPLModel
from python_code import mpl_Operation
from python_code import mpl_OperationCall

def test_mpl_Operation___init__():
    assert mpl_Operation.__init__(mpl_Operation('', mpl_Operation51=set(), mpl_Operation54=mpl_Block(), mpl_Operation62=mpl_OperationCall(), mpl_Operation66=mpl_MPLModel(), mpl_Operation=set()), '', mpl_Operation51=set(), mpl_Operation54=mpl_Block(), mpl_Operation62=mpl_OperationCall(), mpl_Operation66=mpl_MPLModel(), mpl_Operation=set()) == None


from python_code import mpl_Variable
from python_code import mpl_VariableDeclaration
from python_code import mpl_VariableReference

def test_mpl_Variable___init__():
    assert mpl_Variable.__init__(mpl_Variable('', 0, mpl_Variable=mpl_VariableDeclaration(), mpl_Variable11=mpl_VariableReference()), '', 0, mpl_Variable=mpl_VariableDeclaration(), mpl_Variable11=mpl_VariableReference()) == None

