from python_code import jkind_ArrayType
from python_code import jkind_Type

def test_jkind_ArrayType___init__():
    assert jkind_ArrayType.__init__(jkind_ArrayType('', jkind_ArrayType=jkind_Type()), '', jkind_ArrayType=jkind_Type()) == None


from python_code import jkind_BinaryExpr
from python_code import jkind_Expr

def test_jkind_BinaryExpr___init__():
    assert jkind_BinaryExpr.__init__(jkind_BinaryExpr('', jkind_BinaryExpr=jkind_Expr(), jkind_BinaryExpr70=jkind_Expr()), '', jkind_BinaryExpr=jkind_Expr(), jkind_BinaryExpr70=jkind_Expr()) == None


from python_code import jkind_BoolExpr

def test_jkind_BoolExpr___init__():
    assert jkind_BoolExpr.__init__(jkind_BoolExpr(''), '') == None


from python_code import jkind_CallExpr
from python_code import jkind_Callable

def test_jkind_Callable___init__():
    assert jkind_Callable.__init__(jkind_Callable('', jkind_Callable=jkind_CallExpr(), jkind_Callable51=set(), jkind_Callable54=set()), '', jkind_Callable=jkind_CallExpr(), jkind_Callable51=set(), jkind_Callable54=set()) == None


from python_code import jkind_CastExpr
from python_code import jkind_Expr

def test_jkind_CastExpr___init__():
    assert jkind_CastExpr.__init__(jkind_CastExpr('', jkind_CastExpr=jkind_Expr()), '', jkind_CastExpr=jkind_Expr()) == None


from python_code import jkind_Field
from python_code import jkind_RecordAccessExpr
from python_code import jkind_RecordExpr
from python_code import jkind_RecordType
from python_code import jkind_RecordUpdateExpr

def test_jkind_Field___init__():
    assert jkind_Field.__init__(jkind_Field('', jkind_Field122=jkind_RecordExpr(), jkind_Field=jkind_RecordType(), jkind_Field78=jkind_RecordAccessExpr(), jkind_Field83=jkind_RecordUpdateExpr()), '', jkind_Field122=jkind_RecordExpr(), jkind_Field=jkind_RecordType(), jkind_Field78=jkind_RecordAccessExpr(), jkind_Field83=jkind_RecordUpdateExpr()) == None


from python_code import jkind_IdExpr
from python_code import jkind_IdRef

def test_jkind_IdRef___init__():
    assert jkind_IdRef.__init__(jkind_IdRef('', jkind_IdRef=jkind_IdExpr()), '', jkind_IdRef=jkind_IdExpr()) == None


from python_code import jkind_IntExpr

def test_jkind_IntExpr___init__():
    assert jkind_IntExpr.__init__(jkind_IntExpr(''), '') == None


from python_code import jkind_File
from python_code import jkind_Node

def test_jkind_Node___init__():
    assert jkind_Node.__init__(jkind_Node('', jkind_Node16=set(), jkind_Node18=set(), jkind_Node20=set(), jkind_Node=jkind_File(), jkind_Node12=set(), jkind_Node14=set(), jkind_Node22=set()), '', jkind_Node16=set(), jkind_Node18=set(), jkind_Node20=set(), jkind_Node=jkind_File(), jkind_Node12=set(), jkind_Node14=set(), jkind_Node22=set()) == None


from python_code import jkind_RealExpr

def test_jkind_RealExpr___init__():
    assert jkind_RealExpr.__init__(jkind_RealExpr(''), '') == None


from python_code import jkind_SubrangeType

def test_jkind_SubrangeType___init__():
    assert jkind_SubrangeType.__init__(jkind_SubrangeType('', '\x00'), '\x00\x00', '') == None


from python_code import jkind_File
from python_code import jkind_TypeDef
from python_code import jkind_UserType

def test_jkind_TypeDef___init__():
    assert jkind_TypeDef.__init__(jkind_TypeDef('', jkind_TypeDef=jkind_File(), jkind_TypeDef66=jkind_UserType()), '', jkind_TypeDef=jkind_File(), jkind_TypeDef66=jkind_UserType()) == None


from python_code import jkind_Expr
from python_code import jkind_UnaryExpr

def test_jkind_UnaryExpr___init__():
    assert jkind_UnaryExpr.__init__(jkind_UnaryExpr('', jkind_UnaryExpr=jkind_Expr()), '', jkind_UnaryExpr=jkind_Expr()) == None

