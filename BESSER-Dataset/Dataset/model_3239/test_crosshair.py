from python_code import expressions_ast_AbstractRoot

def test_expressions_ast_AbstractRoot___init__():
    assert expressions_ast_AbstractRoot.__init__(expressions_ast_AbstractRoot('', expressions_ast_AbstractRoot=set()), '', expressions_ast_AbstractRoot=set()) == None


from python_code import expressions_ast_AstVisitor

def test_expressions_ast_AstVisitor___init__():
    assert expressions_ast_AstVisitor.__init__(expressions_ast_AstVisitor()) == None

def test_expressions_ast_AstVisitor_visitBinaryExpression():
    assert expressions_ast_AstVisitor.visitBinaryExpression(expressions_ast_AstVisitor(), '') == None

def test_expressions_ast_AstVisitor_visitConstant():
    assert expressions_ast_AstVisitor.visitConstant(expressions_ast_AstVisitor(), '') == None

def test_expressions_ast_AstVisitor_visitVariableReference():
    assert expressions_ast_AstVisitor.visitVariableReference(expressions_ast_AstVisitor(), '') == None

def test_expressions_ast_AstVisitor_visitTernaryExpression():
    assert expressions_ast_AstVisitor.visitTernaryExpression(expressions_ast_AstVisitor(), '') == None

def test_expressions_ast_AstVisitor_visitLiteral():
    assert expressions_ast_AstVisitor.visitLiteral(expressions_ast_AstVisitor(), '') == None

def test_expressions_ast_AstVisitor_visitUnaryExpression():
    assert expressions_ast_AstVisitor.visitUnaryExpression(expressions_ast_AstVisitor(), '') == None


from python_code import expressions_ast_Expression

def test_expressions_ast_Expression___init__():
    assert expressions_ast_Expression.__init__(expressions_ast_Expression('', '\x00'), '\x00\x00', '') == None

def test_expressions_ast_Expression_visit():
    assert expressions_ast_Expression.visit(expressions_ast_Expression('', ''), '') == None


from python_code import expressions_type_Type

def test_expressions_type_Type___init__():
    assert expressions_type_Type.__init__(expressions_type_Type()) == None

def test_expressions_type_Type_add():
    assert expressions_type_Type.add(expressions_type_Type(), '') == None

def test_expressions_type_Type_getPrimitiveTypeIndex():
    assert expressions_type_Type.getPrimitiveTypeIndex(expressions_type_Type()) == None

