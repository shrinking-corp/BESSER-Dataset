from python_code import go_BINARY_EXP
from python_code import go_BOOL_OP
from python_code import go_EXPRESSAO

def test_go_BINARY_EXP___init__():
    assert go_BINARY_EXP.__init__(go_BINARY_EXP('', go_BINARY_EXP122=set(), go_BINARY_EXP=go_EXPRESSAO(), go_BINARY_EXP116=set(), go_BINARY_EXP119=set(), go_BINARY_EXP125=go_BOOL_OP()), '', go_BINARY_EXP122=set(), go_BINARY_EXP=go_EXPRESSAO(), go_BINARY_EXP116=set(), go_BINARY_EXP119=set(), go_BINARY_EXP125=go_BOOL_OP()) == None


from python_code import go_COMPARISON
from python_code import go_Condition

def test_go_COMPARISON___init__():
    assert go_COMPARISON.__init__(go_COMPARISON('', '', '', '', '', go_COMPARISON=go_Condition()), '', '', '', '', '', go_COMPARISON=go_Condition()) == None


from python_code import go_Const
from python_code import go_TIPO

def test_go_Const___init__():
    assert go_Const.__init__(go_Const('', go_Const=go_TIPO()), '', go_Const=go_TIPO()) == None


from python_code import go_BLOCK
from python_code import go_EXPRESSAO
from python_code import go_FunctionType
from python_code import go_GoDecl
from python_code import go_Signature

def test_go_FunctionType___init__():
    assert go_FunctionType.__init__(go_FunctionType('', go_FunctionType=go_GoDecl(), go_FunctionType81=go_EXPRESSAO(), go_FunctionType127=go_Signature(), go_FunctionType129=go_BLOCK()), '', go_FunctionType=go_GoDecl(), go_FunctionType81=go_EXPRESSAO(), go_FunctionType127=go_Signature(), go_FunctionType129=go_BLOCK()) == None


from python_code import go_ArrayValue
from python_code import go_LiteraisList

def test_go_LiteraisList___init__():
    assert go_LiteraisList.__init__(go_LiteraisList('', go_LiteraisList=go_ArrayValue(), go_LiteraisList112=set()), '', go_LiteraisList=go_ArrayValue(), go_LiteraisList112=set()) == None


from python_code import go_SignatureDel
from python_code import go_TIPO
from python_code import go_Types
from python_code import go_VarDecl

def test_go_SignatureDel___init__():
    assert go_SignatureDel.__init__(go_SignatureDel('', go_SignatureDel60=go_Types(), go_SignatureDel=go_VarDecl(), go_SignatureDel58=go_TIPO()), '', go_SignatureDel60=go_Types(), go_SignatureDel=go_VarDecl(), go_SignatureDel58=go_TIPO()) == None


from python_code import go_TIPO
from python_code import go_Var

def test_go_Var___init__():
    assert go_Var.__init__(go_Var('', go_Var=go_TIPO()), '', go_Var=go_TIPO()) == None

