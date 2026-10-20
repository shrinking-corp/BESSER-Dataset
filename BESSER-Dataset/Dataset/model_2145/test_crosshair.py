from python_code import graph_BoolConstant

def test_graph_BoolConstant___init__():
    assert graph_BoolConstant.__init__(graph_BoolConstant(''), '') == None


from python_code import graph_Comparison
from python_code import graph_Expr

def test_graph_Comparison___init__():
    assert graph_Comparison.__init__(graph_Comparison('', graph_Comparison=graph_Expr(), graph_Comparison46=graph_Expr()), '', graph_Comparison=graph_Expr(), graph_Comparison46=graph_Expr()) == None


from python_code import graph_AssignStmt
from python_code import graph_Declaration
from python_code import graph_MoveStmt
from python_code import graph_Program
from python_code import graph_VariableRef

def test_graph_Declaration___init__():
    assert graph_Declaration.__init__(graph_Declaration('', '\x00', graph_Declaration4=graph_AssignStmt(), graph_Declaration61=graph_VariableRef(), graph_Declaration23=graph_MoveStmt(), graph_Declaration=graph_Program()), '\x00\x00', '', graph_Declaration4=graph_AssignStmt(), graph_Declaration61=graph_VariableRef(), graph_Declaration23=graph_MoveStmt(), graph_Declaration=graph_Program()) == None


from python_code import graph_IntConstant

def test_graph_IntConstant___init__():
    assert graph_IntConstant.__init__(graph_IntConstant(0), 0) == None


from python_code import graph_Expr
from python_code import graph_MulOrDiv

def test_graph_MulOrDiv___init__():
    assert graph_MulOrDiv.__init__(graph_MulOrDiv('', graph_MulOrDiv=graph_Expr(), graph_MulOrDiv56=graph_Expr()), '', graph_MulOrDiv=graph_Expr(), graph_MulOrDiv56=graph_Expr()) == None


from python_code import graph_Expr
from python_code import graph_PlusOrMin

def test_graph_PlusOrMin___init__():
    assert graph_PlusOrMin.__init__(graph_PlusOrMin('', graph_PlusOrMin=graph_Expr(), graph_PlusOrMin51=graph_Expr()), '', graph_PlusOrMin=graph_Expr(), graph_PlusOrMin51=graph_Expr()) == None


from python_code import graph_StringConstant

def test_graph_StringConstant___init__():
    assert graph_StringConstant.__init__(graph_StringConstant(''), '') == None


from python_code import graph_Edge
from python_code import graph_GraphConstant
from python_code import graph_ParticleConstant
from python_code import graph_Vertex

def test_graph_Vertex___init__():
    assert graph_Vertex.__init__(graph_Vertex('', graph_Vertex63=graph_GraphConstant(), graph_Vertex=graph_Edge(), graph_Vertex27=graph_Edge(), graph_Vertex71=graph_ParticleConstant()), '', graph_Vertex63=graph_GraphConstant(), graph_Vertex=graph_Edge(), graph_Vertex27=graph_Edge(), graph_Vertex71=graph_ParticleConstant()) == None

