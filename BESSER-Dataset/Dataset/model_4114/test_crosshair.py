from python_code import py_Affect

def test_py_Affect___init__():
    assert py_Affect.__init__(py_Affect('', py_Affect=set()), '', py_Affect=set()) == None


from python_code import py_ExprAnd
from python_code import py_ExprEq
from python_code import py_ExprOr
from python_code import py_ExprSimple

def test_py_ExprSimple___init__():
    assert py_ExprSimple.__init__(py_ExprSimple('', '', '\x00\x00', py_ExprSimple=py_ExprAnd(), py_ExprSimple66=py_ExprEq(), py_ExprSimple47=py_ExprOr()), '', '', '', py_ExprSimple=py_ExprAnd(), py_ExprSimple66=py_ExprEq(), py_ExprSimple47=py_ExprOr()) == None


from python_code import py_ExprSym

def test_py_ExprSym___init__():
    assert py_ExprSym.__init__(py_ExprSym('', py_ExprSym=set()), '', py_ExprSym=set()) == None


from python_code import py_Commands
from python_code import py_Expr
from python_code import py_Foreach

def test_py_Foreach___init__():
    assert py_Foreach.__init__(py_Foreach('', py_Foreach=py_Expr(), py_Foreach32=py_Commands()), '', py_Foreach=py_Expr(), py_Foreach32=py_Commands()) == None


from python_code import py_Definition
from python_code import py_FunctionP
from python_code import py_Program

def test_py_FunctionP___init__():
    assert py_FunctionP.__init__(py_FunctionP('', py_FunctionP=py_Program(), py_FunctionP4=py_Definition()), '', py_FunctionP=py_Program(), py_FunctionP4=py_Definition()) == None


from python_code import py_Definition
from python_code import py_Input

def test_py_Input___init__():
    assert py_Input.__init__(py_Input('', py_Input=py_Definition()), '', py_Input=py_Definition()) == None


from python_code import py_Nop

def test_py_Nop___init__():
    assert py_Nop.__init__(py_Nop(''), '') == None


from python_code import py_Definition
from python_code import py_Output

def test_py_Output___init__():
    assert py_Output.__init__(py_Output('', py_Output=py_Definition()), '', py_Output=py_Definition()) == None

