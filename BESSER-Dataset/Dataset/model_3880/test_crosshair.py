from python_code import flinkie2_BoolVal

def test_flinkie2_BoolVal___init__():
    assert flinkie2_BoolVal.__init__(flinkie2_BoolVal(True), False) == None


from python_code import flinkie2_Comparison
from python_code import flinkie2_IntExpr

def test_flinkie2_Comparison___init__():
    assert flinkie2_Comparison.__init__(flinkie2_Comparison('', flinkie2_Comparison=flinkie2_IntExpr(), flinkie2_Comparison62=flinkie2_IntExpr()), '', flinkie2_Comparison=flinkie2_IntExpr(), flinkie2_Comparison62=flinkie2_IntExpr()) == None


from python_code import flinkie2_Message
from python_code import flinkie2_Node

def test_flinkie2_Message___init__():
    assert flinkie2_Message.__init__(flinkie2_Message('', flinkie2_Message=set(), flinkie2_Message21=flinkie2_Node()), '', flinkie2_Message=set(), flinkie2_Message21=flinkie2_Node()) == None


from python_code import flinkie2_Number

def test_flinkie2_Number___init__():
    assert flinkie2_Number.__init__(flinkie2_Number(0), 0) == None


from python_code import flinkie2_BoolExpr
from python_code import flinkie2_OneOpBool

def test_flinkie2_OneOpBool___init__():
    assert flinkie2_OneOpBool.__init__(flinkie2_OneOpBool('', flinkie2_OneOpBool=flinkie2_BoolExpr()), '', flinkie2_OneOpBool=flinkie2_BoolExpr()) == None


from python_code import flinkie2_IntExpr
from python_code import flinkie2_OneOpInt

def test_flinkie2_OneOpInt___init__():
    assert flinkie2_OneOpInt.__init__(flinkie2_OneOpInt('', flinkie2_OneOpInt=flinkie2_IntExpr()), '', flinkie2_OneOpInt=flinkie2_IntExpr()) == None


from python_code import flinkie2_Question

def test_flinkie2_Question___init__():
    assert flinkie2_Question.__init__(flinkie2_Question('', flinkie2_Question=set(), flinkie2_Question16=set()), '', flinkie2_Question=set(), flinkie2_Question16=set()) == None


from python_code import flinkie2_BoolExpr
from python_code import flinkie2_TwoOpBool

def test_flinkie2_TwoOpBool___init__():
    assert flinkie2_TwoOpBool.__init__(flinkie2_TwoOpBool('', flinkie2_TwoOpBool=flinkie2_BoolExpr(), flinkie2_TwoOpBool55=flinkie2_BoolExpr()), '', flinkie2_TwoOpBool=flinkie2_BoolExpr(), flinkie2_TwoOpBool55=flinkie2_BoolExpr()) == None


from python_code import flinkie2_IntExpr
from python_code import flinkie2_TwoOpInt

def test_flinkie2_TwoOpInt___init__():
    assert flinkie2_TwoOpInt.__init__(flinkie2_TwoOpInt('', flinkie2_TwoOpInt=flinkie2_IntExpr(), flinkie2_TwoOpInt33=flinkie2_IntExpr()), '', flinkie2_TwoOpInt=flinkie2_IntExpr(), flinkie2_TwoOpInt33=flinkie2_IntExpr()) == None


from python_code import flinkie2_DeclStat
from python_code import flinkie2_Variable
from python_code import flinkie2_VariableExpr

def test_flinkie2_Variable___init__():
    assert flinkie2_Variable.__init__(flinkie2_Variable('', flinkie2_Variable=flinkie2_DeclStat(), flinkie2_Variable49=flinkie2_VariableExpr()), '', flinkie2_Variable=flinkie2_DeclStat(), flinkie2_Variable49=flinkie2_VariableExpr()) == None

