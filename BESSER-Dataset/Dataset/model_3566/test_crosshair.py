from python_code import myDsl_AliasDecl
from python_code import myDsl_Type
from python_code import myDsl_TypeSpec

def test_myDsl_AliasDecl___init__():
    assert myDsl_AliasDecl.__init__(myDsl_AliasDecl('', myDsl_AliasDecl=myDsl_TypeSpec(), myDsl_AliasDecl142=myDsl_Type()), '', myDsl_AliasDecl=myDsl_TypeSpec(), myDsl_AliasDecl142=myDsl_Type()) == None


from python_code import myDsl_BINARY_OP
from python_code import myDsl_Expression_Linha

def test_myDsl_BINARY_OP___init__():
    assert myDsl_BINARY_OP.__init__(myDsl_BINARY_OP('', '\x00', myDsl_BINARY_OP=myDsl_Expression_Linha()), '\x00\x00', '', myDsl_BINARY_OP=myDsl_Expression_Linha()) == None


from python_code import myDsl_BasicLit
from python_code import myDsl_Literal

def test_myDsl_BasicLit___init__():
    assert myDsl_BasicLit.__init__(myDsl_BasicLit('', '', '', '', '', myDsl_BasicLit=myDsl_Literal()), '', '', '', '', '', myDsl_BasicLit=myDsl_Literal()) == None


from python_code import myDsl_CommCase
from python_code import myDsl_CommCaseLinha
from python_code import myDsl_CommClause
from python_code import myDsl_Expression

def test_myDsl_CommCase___init__():
    assert myDsl_CommCase.__init__(myDsl_CommCase('', '\x00', myDsl_CommCase=myDsl_CommClause(), myDsl_CommCase533=myDsl_Expression(), myDsl_CommCase536=myDsl_CommCaseLinha()), '\x00\x00', '', myDsl_CommCase=myDsl_CommClause(), myDsl_CommCase533=myDsl_Expression(), myDsl_CommCase536=myDsl_CommCaseLinha()) == None


from python_code import myDsl_ConstDecl
from python_code import myDsl_ConstSpec
from python_code import myDsl_Declaration

def test_myDsl_ConstDecl___init__():
    assert myDsl_ConstDecl.__init__(myDsl_ConstDecl('', myDsl_ConstDecl=myDsl_Declaration(), myDsl_ConstDecl116=set(), myDsl_ConstDecl114=myDsl_ConstSpec()), '', myDsl_ConstDecl=myDsl_Declaration(), myDsl_ConstDecl116=set(), myDsl_ConstDecl114=myDsl_ConstSpec()) == None


from python_code import myDsl_DeferStmt
from python_code import myDsl_Expression
from python_code import myDsl_Statement

def test_myDsl_DeferStmt___init__():
    assert myDsl_DeferStmt.__init__(myDsl_DeferStmt('', myDsl_DeferStmt=myDsl_Statement(), myDsl_DeferStmt564=myDsl_Expression()), '', myDsl_DeferStmt=myDsl_Statement(), myDsl_DeferStmt564=myDsl_Expression()) == None


from python_code import myDsl_ExprCaseClause
from python_code import myDsl_ExprSwitchCase
from python_code import myDsl_ExpressionList

def test_myDsl_ExprSwitchCase___init__():
    assert myDsl_ExprSwitchCase.__init__(myDsl_ExprSwitchCase('', '\x00', myDsl_ExprSwitchCase=myDsl_ExprCaseClause(), myDsl_ExprSwitchCase441=myDsl_ExpressionList()), '\x00\x00', '', myDsl_ExprSwitchCase=myDsl_ExprCaseClause(), myDsl_ExprSwitchCase441=myDsl_ExpressionList()) == None


from python_code import myDsl_ExprSwitchStmt
from python_code import myDsl_Expression
from python_code import myDsl_SimpleStmt
from python_code import myDsl_SwitchStmt

def test_myDsl_ExprSwitchStmt___init__():
    assert myDsl_ExprSwitchStmt.__init__(myDsl_ExprSwitchStmt('', myDsl_ExprSwitchStmt=myDsl_SwitchStmt(), myDsl_ExprSwitchStmt428=myDsl_SimpleStmt(), myDsl_ExprSwitchStmt434=set(), myDsl_ExprSwitchStmt431=myDsl_Expression()), '', myDsl_ExprSwitchStmt=myDsl_SwitchStmt(), myDsl_ExprSwitchStmt428=myDsl_SimpleStmt(), myDsl_ExprSwitchStmt434=set(), myDsl_ExprSwitchStmt431=myDsl_Expression()) == None


from python_code import myDsl_FallthroughStmt
from python_code import myDsl_Statement

def test_myDsl_FallthroughStmt___init__():
    assert myDsl_FallthroughStmt.__init__(myDsl_FallthroughStmt('', myDsl_FallthroughStmt=myDsl_Statement()), '', myDsl_FallthroughStmt=myDsl_Statement()) == None


from python_code import myDsl_FieldName
from python_code import myDsl_Key

def test_myDsl_FieldName___init__():
    assert myDsl_FieldName.__init__(myDsl_FieldName('', myDsl_FieldName=myDsl_Key()), '', myDsl_FieldName=myDsl_Key()) == None


from python_code import myDsl_FunctionBody
from python_code import myDsl_FunctionLit
from python_code import myDsl_Literal
from python_code import myDsl_Signature

def test_myDsl_FunctionLit___init__():
    assert myDsl_FunctionLit.__init__(myDsl_FunctionLit('', myDsl_FunctionLit=myDsl_Literal(), myDsl_FunctionLit249=myDsl_Signature(), myDsl_FunctionLit252=myDsl_FunctionBody()), '', myDsl_FunctionLit=myDsl_Literal(), myDsl_FunctionLit249=myDsl_Signature(), myDsl_FunctionLit252=myDsl_FunctionBody()) == None


from python_code import myDsl_FunctionDecl
from python_code import myDsl_FunctionName

def test_myDsl_FunctionName___init__():
    assert myDsl_FunctionName.__init__(myDsl_FunctionName('', myDsl_FunctionName=myDsl_FunctionDecl()), '', myDsl_FunctionName=myDsl_FunctionDecl()) == None


from python_code import myDsl_FunctionType
from python_code import myDsl_Signature
from python_code import myDsl_TypeLit

def test_myDsl_FunctionType___init__():
    assert myDsl_FunctionType.__init__(myDsl_FunctionType('', myDsl_FunctionType50=myDsl_Signature(), myDsl_FunctionType=myDsl_TypeLit()), '', myDsl_FunctionType50=myDsl_Signature(), myDsl_FunctionType=myDsl_TypeLit()) == None


from python_code import myDsl_Expression
from python_code import myDsl_GoStmt
from python_code import myDsl_Statement

def test_myDsl_GoStmt___init__():
    assert myDsl_GoStmt.__init__(myDsl_GoStmt('', myDsl_GoStmt=myDsl_Statement(), myDsl_GoStmt523=myDsl_Expression()), '', myDsl_GoStmt=myDsl_Statement(), myDsl_GoStmt523=myDsl_Expression()) == None


from python_code import myDsl_InterfaceType
from python_code import myDsl_TypeLit

def test_myDsl_InterfaceType___init__():
    assert myDsl_InterfaceType.__init__(myDsl_InterfaceType('', myDsl_InterfaceType75=set(), myDsl_InterfaceType=myDsl_TypeLit()), '', myDsl_InterfaceType75=set(), myDsl_InterfaceType=myDsl_TypeLit()) == None


from python_code import myDsl_ElementType
from python_code import myDsl_KeyType
from python_code import myDsl_LiteralType
from python_code import myDsl_MapType
from python_code import myDsl_TypeLit

def test_myDsl_MapType___init__():
    assert myDsl_MapType.__init__(myDsl_MapType('', myDsl_MapType=myDsl_TypeLit(), myDsl_MapType87=myDsl_KeyType(), myDsl_MapType89=myDsl_ElementType(), myDsl_MapType211=myDsl_LiteralType()), '', myDsl_MapType=myDsl_TypeLit(), myDsl_MapType87=myDsl_KeyType(), myDsl_MapType89=myDsl_ElementType(), myDsl_MapType211=myDsl_LiteralType()) == None


from python_code import myDsl_MethodDecl
from python_code import myDsl_MethodExpr
from python_code import myDsl_MethodName
from python_code import myDsl_MethodSpec

def test_myDsl_MethodName___init__():
    assert myDsl_MethodName.__init__(myDsl_MethodName('', myDsl_MethodName=myDsl_MethodSpec(), myDsl_MethodName180=myDsl_MethodDecl(), myDsl_MethodName300=myDsl_MethodExpr()), '', myDsl_MethodName=myDsl_MethodSpec(), myDsl_MethodName180=myDsl_MethodDecl(), myDsl_MethodName300=myDsl_MethodExpr()) == None


from python_code import myDsl_Operand
from python_code import myDsl_OperandName

def test_myDsl_OperandName___init__():
    assert myDsl_OperandName.__init__(myDsl_OperandName('', myDsl_OperandName=myDsl_Operand()), '', myDsl_OperandName=myDsl_Operand()) == None


from python_code import myDsl_ExpressionList
from python_code import myDsl_ReturnStmt
from python_code import myDsl_Statement

def test_myDsl_ReturnStmt___init__():
    assert myDsl_ReturnStmt.__init__(myDsl_ReturnStmt('', myDsl_ReturnStmt=myDsl_Statement(), myDsl_ReturnStmt552=myDsl_ExpressionList()), '', myDsl_ReturnStmt=myDsl_Statement(), myDsl_ReturnStmt552=myDsl_ExpressionList()) == None


from python_code import myDsl_SelectStmt
from python_code import myDsl_Statement

def test_myDsl_SelectStmt___init__():
    assert myDsl_SelectStmt.__init__(myDsl_SelectStmt('', myDsl_SelectStmt=myDsl_Statement(), myDsl_SelectStmt526=set()), '', myDsl_SelectStmt=myDsl_Statement(), myDsl_SelectStmt526=set()) == None


from python_code import myDsl_PrimaryExprLinha
from python_code import myDsl_Selector

def test_myDsl_Selector___init__():
    assert myDsl_Selector.__init__(myDsl_Selector('', myDsl_Selector=myDsl_PrimaryExprLinha()), '', myDsl_Selector=myDsl_PrimaryExprLinha()) == None


from python_code import myDsl_LiteralType
from python_code import myDsl_StructType
from python_code import myDsl_TypeLit

def test_myDsl_StructType___init__():
    assert myDsl_StructType.__init__(myDsl_StructType('', myDsl_StructType=myDsl_TypeLit(), myDsl_StructType31=set(), myDsl_StructType208=myDsl_LiteralType()), '', myDsl_StructType=myDsl_TypeLit(), myDsl_StructType31=set(), myDsl_StructType208=myDsl_LiteralType()) == None


from python_code import myDsl_FieldDecl
from python_code import myDsl_Tag

def test_myDsl_Tag___init__():
    assert myDsl_Tag.__init__(myDsl_Tag('', myDsl_Tag=myDsl_FieldDecl()), '', myDsl_Tag=myDsl_FieldDecl()) == None


from python_code import myDsl_Declaration
from python_code import myDsl_TypeDecl
from python_code import myDsl_TypeSpec

def test_myDsl_TypeDecl___init__():
    assert myDsl_TypeDecl.__init__(myDsl_TypeDecl('', myDsl_TypeDecl=myDsl_Declaration(), myDsl_TypeDecl133=myDsl_TypeSpec(), myDsl_TypeDecl135=set()), '', myDsl_TypeDecl=myDsl_Declaration(), myDsl_TypeDecl133=myDsl_TypeSpec(), myDsl_TypeDecl135=set()) == None


from python_code import myDsl_Type
from python_code import myDsl_TypeDef
from python_code import myDsl_TypeSpec

def test_myDsl_TypeDef___init__():
    assert myDsl_TypeDef.__init__(myDsl_TypeDef('', myDsl_TypeDef=myDsl_TypeSpec(), myDsl_TypeDef145=myDsl_Type()), '', myDsl_TypeDef=myDsl_TypeSpec(), myDsl_TypeDef145=myDsl_Type()) == None


from python_code import myDsl_EmbeddedField
from python_code import myDsl_InterfaceTypeName
from python_code import myDsl_LiteralType
from python_code import myDsl_Type
from python_code import myDsl_TypeName

def test_myDsl_TypeName___init__():
    assert myDsl_TypeName.__init__(myDsl_TypeName('', myDsl_TypeName=myDsl_Type(), myDsl_TypeName43=myDsl_EmbeddedField(), myDsl_TypeName85=myDsl_InterfaceTypeName(), myDsl_TypeName214=myDsl_LiteralType()), '', myDsl_TypeName=myDsl_Type(), myDsl_TypeName43=myDsl_EmbeddedField(), myDsl_TypeName85=myDsl_InterfaceTypeName(), myDsl_TypeName214=myDsl_LiteralType()) == None


from python_code import myDsl_TypeNameLinha

def test_myDsl_TypeNameLinha___init__():
    assert myDsl_TypeNameLinha.__init__(myDsl_TypeNameLinha(''), '') == None


from python_code import myDsl_TypeCaseClause
from python_code import myDsl_TypeList
from python_code import myDsl_TypeSwitchCase

def test_myDsl_TypeSwitchCase___init__():
    assert myDsl_TypeSwitchCase.__init__(myDsl_TypeSwitchCase('', '\x00', myDsl_TypeSwitchCase=myDsl_TypeCaseClause(), myDsl_TypeSwitchCase459=myDsl_TypeList()), '\x00\x00', '', myDsl_TypeSwitchCase=myDsl_TypeCaseClause(), myDsl_TypeSwitchCase459=myDsl_TypeList()) == None


from python_code import myDsl_Declaration
from python_code import myDsl_VarDecl
from python_code import myDsl_VarSpec

def test_myDsl_VarDecl___init__():
    assert myDsl_VarDecl.__init__(myDsl_VarDecl('', myDsl_VarDecl=myDsl_Declaration(), myDsl_VarDecl148=myDsl_VarSpec(), myDsl_VarDecl150=set()), '', myDsl_VarDecl=myDsl_Declaration(), myDsl_VarDecl148=myDsl_VarSpec(), myDsl_VarDecl150=set()) == None

