from python_code import mpl_ComparisonExpression
from python_code import mpl_Expression
from python_code import mpl_IfStatement
from python_code import mpl_WhileLoop

def test_mpl_ComparisonExpression___init__():
    assert mpl_ComparisonExpression.__init__(mpl_ComparisonExpression('', mpl_ComparisonExpression=mpl_IfStatement(), mpl_ComparisonExpression27=mpl_WhileLoop(), mpl_ComparisonExpression49=mpl_Expression(), mpl_ComparisonExpression52=mpl_Expression()), '', mpl_ComparisonExpression=mpl_IfStatement(), mpl_ComparisonExpression27=mpl_WhileLoop(), mpl_ComparisonExpression49=mpl_Expression(), mpl_ComparisonExpression52=mpl_Expression()) == None


from python_code import mpl_Assignment
from python_code import mpl_Block
from python_code import mpl_Expression
from python_code import mpl_ForLoop

def test_mpl_ForLoop___init__():
    assert mpl_ForLoop.__init__(mpl_ForLoop('', mpl_ForLoop=mpl_Assignment(), mpl_ForLoop34=mpl_Expression(), mpl_ForLoop37=mpl_Block()), '', mpl_ForLoop=mpl_Assignment(), mpl_ForLoop34=mpl_Expression(), mpl_ForLoop37=mpl_Block()) == None


from python_code import mpl_Block
from python_code import mpl_FunctionalUnit

def test_mpl_FunctionalUnit___init__():
    assert mpl_FunctionalUnit.__init__(mpl_FunctionalUnit('', mpl_FunctionalUnit=set(), mpl_FunctionalUnit5=mpl_Block()), '', mpl_FunctionalUnit=set(), mpl_FunctionalUnit5=mpl_Block()) == None


from python_code import mpl_LiteralValue

def test_mpl_LiteralValue___init__():
    assert mpl_LiteralValue.__init__(mpl_LiteralValue(0), 0) == None


from python_code import mpl_Operation
from python_code import mpl_Variable
from python_code import mpl_VariableDeclaration
from python_code import mpl_VariableReference

def test_mpl_Variable___init__():
    assert mpl_Variable.__init__(mpl_Variable('', mpl_Variable10=mpl_VariableDeclaration(), mpl_Variable=mpl_Operation(), mpl_Variable47=mpl_VariableReference()), '', mpl_Variable10=mpl_VariableDeclaration(), mpl_Variable=mpl_Operation(), mpl_Variable47=mpl_VariableReference()) == None

