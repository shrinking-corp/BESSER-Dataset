from python_code import mt_Resource
from python_code import mt_ResourceSet

def test_mt_Resource___init__():
    assert mt_Resource.__init__(mt_Resource('', mt_Resource=mt_ResourceSet()), '', mt_Resource=mt_ResourceSet()) == None


from python_code import mt_core_ASTNode

def test_mt_core_ASTNode___init__():
    assert mt_core_ASTNode.__init__(mt_core_ASTNode(0, 0), 0, 0) == None

def test_mt_core_ASTNode_getTemplate():
    assert mt_core_ASTNode.getTemplate(mt_core_ASTNode(0, 0)) == None


from python_code import mt_core_Metamodel

def test_mt_core_Metamodel___init__():
    assert mt_core_Metamodel.__init__(mt_core_Metamodel(''), '') == None


from python_code import mt_core_Method

def test_mt_core_Method___init__():
    assert mt_core_Method.__init__(mt_core_Method('\x00\x00', '', mt_core_Method=set()), '', '', mt_core_Method=set()) == None


from python_code import mt_core_Parameter

def test_mt_core_Parameter___init__():
    assert mt_core_Parameter.__init__(mt_core_Parameter(''), '') == None


from python_code import mt_core_Template

def test_mt_core_Template___init__():
    assert mt_core_Template.__init__(mt_core_Template('', '', mt_core_Template=set(), mt_core_Template3=set()), '', '', mt_core_Template=set(), mt_core_Template3=set()) == None


from python_code import mt_expressions_BooleanLiteral

def test_mt_expressions_BooleanLiteral___init__():
    assert mt_expressions_BooleanLiteral.__init__(mt_expressions_BooleanLiteral(True), False) == None


from python_code import mt_expressions_DoubleLiteral

def test_mt_expressions_DoubleLiteral___init__():
    assert mt_expressions_DoubleLiteral.__init__(mt_expressions_DoubleLiteral(0.0), 0.0) == None


from python_code import mt_expressions_IntegerLiteral

def test_mt_expressions_IntegerLiteral___init__():
    assert mt_expressions_IntegerLiteral.__init__(mt_expressions_IntegerLiteral(0), 0) == None


from python_code import mt_expressions_StringLiteral

def test_mt_expressions_StringLiteral___init__():
    assert mt_expressions_StringLiteral.__init__(mt_expressions_StringLiteral(''), '') == None


from python_code import mt_core_FilePath
from python_code import mt_core_Script
from python_code import mt_statements_Comment
from python_code import mt_statements_For
from python_code import mt_statements_If

def test_mt_statements_Comment___init__():
    assert mt_statements_Comment.__init__(mt_statements_Comment('', Statement30=mt_statements_If(), Statement33=mt_statements_If(), Statement11=mt_core_FilePath(), Statement=mt_core_Script(), Statement40=mt_statements_For()), '', Statement30=mt_statements_If(), Statement33=mt_statements_If(), Statement11=mt_core_FilePath(), Statement=mt_core_Script(), Statement40=mt_statements_For()) == None


from python_code import mt_core_FilePath
from python_code import mt_core_Script
from python_code import mt_statements_For
from python_code import mt_statements_If
from python_code import mt_statements_Text

def test_mt_statements_Text___init__():
    assert mt_statements_Text.__init__(mt_statements_Text('', Statement30=mt_statements_If(), Statement33=mt_statements_If(), Statement11=mt_core_FilePath(), Statement=mt_core_Script(), Statement40=mt_statements_For()), '', Statement30=mt_statements_If(), Statement33=mt_statements_If(), Statement11=mt_core_FilePath(), Statement=mt_core_Script(), Statement40=mt_statements_For()) == None

