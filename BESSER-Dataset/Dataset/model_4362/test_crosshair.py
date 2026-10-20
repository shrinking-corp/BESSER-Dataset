from python_code import mpl_LiteralValue

def test_mpl_LiteralValue___init__():
    assert mpl_LiteralValue.__init__(mpl_LiteralValue(0), 0) == None


from python_code import mpl_Program

def test_mpl_Program___init__():
    assert mpl_Program.__init__(mpl_Program('', mpl_Program=set(), mpl_Program2=set()), '', mpl_Program=set(), mpl_Program2=set()) == None


from python_code import mpl_Variable
from python_code import mpl_VariableDeclaration
from python_code import mpl_VariableRefrence

def test_mpl_Variable___init__():
    assert mpl_Variable.__init__(mpl_Variable('', mpl_Variable=mpl_VariableDeclaration(), mpl_Variable17=mpl_VariableRefrence()), '', mpl_Variable=mpl_VariableDeclaration(), mpl_Variable17=mpl_VariableRefrence()) == None

