from python_code import mpl_Assignment
from python_code import mpl_Expression
from python_code import mpl_For

def test_mpl_For___init__():
    assert mpl_For.__init__(mpl_For('', mpl_For=mpl_Assignment(), mpl_For56=mpl_Expression()), '', mpl_For=mpl_Assignment(), mpl_For56=mpl_Expression()) == None


from python_code import mpl_Block
from python_code import mpl_FunctionalUnit

def test_mpl_FunctionalUnit___init__():
    assert mpl_FunctionalUnit.__init__(mpl_FunctionalUnit('', mpl_FunctionalUnit5=mpl_Block(), mpl_FunctionalUnit=set()), '', mpl_FunctionalUnit5=mpl_Block(), mpl_FunctionalUnit=set()) == None


from python_code import mpl_InputExpression
from python_code import mpl_LiteralValue

def test_mpl_LiteralValue___init__():
    assert mpl_LiteralValue.__init__(mpl_LiteralValue(0, mpl_LiteralValue=mpl_InputExpression(), mpl_LiteralValue33=mpl_InputExpression()), 0, mpl_LiteralValue=mpl_InputExpression(), mpl_LiteralValue33=mpl_InputExpression()) == None


from python_code import mpl_Operation
from python_code import mpl_Variable
from python_code import mpl_VariableDeclaration
from python_code import mpl_VariableReference

def test_mpl_Variable___init__():
    assert mpl_Variable.__init__(mpl_Variable('', mpl_Variable=mpl_VariableDeclaration(), mpl_Variable22=mpl_VariableReference(), mpl_Variable60=mpl_Operation()), '', mpl_Variable=mpl_VariableDeclaration(), mpl_Variable22=mpl_VariableReference(), mpl_Variable60=mpl_Operation()) == None

