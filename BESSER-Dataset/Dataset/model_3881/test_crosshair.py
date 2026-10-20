from python_code import expressions_Expression
from python_code import expressions_Function
from python_code import expressions_FunctionCall
from python_code import expressions_Model

def test_expressions_Function___init__():
    assert expressions_Function.__init__(expressions_Function('\x00', expressions_Function=set(), expressions_Function2=expressions_Expression(), expressions_Function13=expressions_FunctionCall(), expressions_Function18=expressions_Model()), '', expressions_Function=set(), expressions_Function2=expressions_Expression(), expressions_Function13=expressions_FunctionCall(), expressions_Function18=expressions_Model()) == None


from python_code import expressions_Number

def test_expressions_Number___init__():
    assert expressions_Number.__init__(expressions_Number(0), 0) == None

