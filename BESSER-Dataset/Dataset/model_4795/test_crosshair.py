from python_code import jkind_BinaryExpr
from python_code import jkind_Expr

def test_jkind_BinaryExpr___init__():
    assert jkind_BinaryExpr.__init__(jkind_BinaryExpr('', jkind_BinaryExpr=jkind_Expr(), jkind_BinaryExpr51=jkind_Expr()), '', jkind_BinaryExpr=jkind_Expr(), jkind_BinaryExpr51=jkind_Expr()) == None


from python_code import jkind_BoolExpr

def test_jkind_BoolExpr___init__():
    assert jkind_BoolExpr.__init__(jkind_BoolExpr(''), '') == None


from python_code import jkind_Field
from python_code import jkind_ProjectionExpr
from python_code import jkind_RecordExpr
from python_code import jkind_RecordType

def test_jkind_Field___init__():
    assert jkind_Field.__init__(jkind_Field('', jkind_Field59=jkind_ProjectionExpr(), jkind_Field=jkind_RecordType(), jkind_Field78=jkind_RecordExpr()), '', jkind_Field59=jkind_ProjectionExpr(), jkind_Field=jkind_RecordType(), jkind_Field78=jkind_RecordExpr()) == None


from python_code import jkind_IdExpr
from python_code import jkind_IdRef

def test_jkind_IdRef___init__():
    assert jkind_IdRef.__init__(jkind_IdRef('', jkind_IdRef=jkind_IdExpr()), '', jkind_IdRef=jkind_IdExpr()) == None


from python_code import jkind_IntExpr

def test_jkind_IntExpr___init__():
    assert jkind_IntExpr.__init__(jkind_IntExpr(''), '') == None


from python_code import jkind_File
from python_code import jkind_Node
from python_code import jkind_NodeCallExpr

def test_jkind_Node___init__():
    assert jkind_Node.__init__(jkind_Node('', '', jkind_Node18=set(), jkind_Node20=set(), jkind_Node22=set(), jkind_Node=jkind_File(), jkind_Node10=set(), jkind_Node12=set(), jkind_Node15=set(), jkind_Node70=jkind_NodeCallExpr()), '', '', jkind_Node18=set(), jkind_Node20=set(), jkind_Node22=set(), jkind_Node=jkind_File(), jkind_Node10=set(), jkind_Node12=set(), jkind_Node15=set(), jkind_Node70=jkind_NodeCallExpr()) == None


from python_code import jkind_RealExpr

def test_jkind_RealExpr___init__():
    assert jkind_RealExpr.__init__(jkind_RealExpr(''), '') == None


from python_code import jkind_SubrangeType

def test_jkind_SubrangeType___init__():
    assert jkind_SubrangeType.__init__(jkind_SubrangeType('', '\x00'), '\x00\x00', '') == None


from python_code import jkind_File
from python_code import jkind_Typedef
from python_code import jkind_UserType

def test_jkind_Typedef___init__():
    assert jkind_Typedef.__init__(jkind_Typedef('', jkind_Typedef=jkind_File(), jkind_Typedef47=jkind_UserType()), '', jkind_Typedef=jkind_File(), jkind_Typedef47=jkind_UserType()) == None


from python_code import jkind_Expr
from python_code import jkind_UnaryExpr

def test_jkind_UnaryExpr___init__():
    assert jkind_UnaryExpr.__init__(jkind_UnaryExpr('', jkind_UnaryExpr=jkind_Expr()), '', jkind_UnaryExpr=jkind_Expr()) == None

