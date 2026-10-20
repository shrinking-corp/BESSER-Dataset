from python_code import astm_Comment

def test_astm_Comment___init__():
    assert astm_Comment.__init__(astm_Comment(''), '') == None


from python_code import astm_CompilationUnit
from python_code import astm_ProgramScope
from python_code import astm_Project

def test_astm_CompilationUnit___init__():
    assert astm_CompilationUnit.__init__(astm_CompilationUnit('', astm_CompilationUnit=astm_Project(), astm_CompilationUnit15=set(), astm_CompilationUnit18=astm_ProgramScope()), '', astm_CompilationUnit=astm_Project(), astm_CompilationUnit15=set(), astm_CompilationUnit18=astm_ProgramScope()) == None


from python_code import astm_DataDefinition
from python_code import astm_Expression
from python_code import astm_VariableCatchBlock

def test_astm_DataDefinition___init__():
    assert astm_DataDefinition.__init__(astm_DataDefinition(True, astm_DataDefinition=astm_Expression(), astm_DataDefinition179=astm_VariableCatchBlock()), False, astm_DataDefinition=astm_Expression(), astm_DataDefinition179=astm_VariableCatchBlock()) == None


from python_code import astm_DeclarationOrDefinition
from python_code import astm_OtherSyntaxObject

def test_astm_DeclarationOrDefinition___init__():
    assert astm_DeclarationOrDefinition.__init__(astm_DeclarationOrDefinition(False, '\x00', astm_DeclarationOrDefinition=astm_OtherSyntaxObject(), astm_DeclarationOrDefinition21=astm_OtherSyntaxObject()), False, '\x00', astm_DeclarationOrDefinition=astm_OtherSyntaxObject(), astm_DeclarationOrDefinition21=astm_OtherSyntaxObject()) == None


from python_code import astm_ClassType
from python_code import astm_DerivesFrom
from python_code import astm_NamedType
from python_code import astm_OtherSyntaxObject

def test_astm_DerivesFrom___init__():
    assert astm_DerivesFrom.__init__(astm_DerivesFrom(True, astm_DerivesFrom=astm_ClassType(), astm_DerivesFrom105=astm_OtherSyntaxObject(), astm_DerivesFrom108=astm_NamedType()), False, astm_DerivesFrom=astm_ClassType(), astm_DerivesFrom105=astm_OtherSyntaxObject(), astm_DerivesFrom108=astm_NamedType()) == None


from python_code import astm_FunctionDeclaration
from python_code import astm_FunctionDefinition
from python_code import astm_FunctionMemberAttributes
from python_code import astm_VirtualSpecification

def test_astm_FunctionMemberAttributes___init__():
    assert astm_FunctionMemberAttributes.__init__(astm_FunctionMemberAttributes(False, False, False, astm_FunctionMemberAttributes=astm_FunctionDeclaration(), astm_FunctionMemberAttributes45=astm_FunctionDefinition(), astm_FunctionMemberAttributes49=astm_VirtualSpecification()), False, False, False, astm_FunctionMemberAttributes=astm_FunctionDeclaration(), astm_FunctionMemberAttributes45=astm_FunctionDefinition(), astm_FunctionMemberAttributes49=astm_VirtualSpecification()) == None


from python_code import astm_Literal

def test_astm_Literal___init__():
    assert astm_Literal.__init__(astm_Literal(''), '') == None


from python_code import astm_MacroCall
from python_code import astm_MacroDefinition

def test_astm_MacroDefinition___init__():
    assert astm_MacroDefinition.__init__(astm_MacroDefinition('', '\x00', astm_MacroDefinition=astm_MacroCall()), '\x00\x00', '', astm_MacroDefinition=astm_MacroCall()) == None


from python_code import astm_PrimitiveType

def test_astm_PrimitiveType___init__():
    assert astm_PrimitiveType.__init__(astm_PrimitiveType(True), False) == None


from python_code import astm_RDBCheckConstraint

def test_astm_RDBCheckConstraint___init__():
    assert astm_RDBCheckConstraint.__init__(astm_RDBCheckConstraint('', '\x00'), '\x00\x00', '') == None


from python_code import astm_RDBIndex
from python_code import astm_RDBTableDefinition

def test_astm_RDBIndex___init__():
    assert astm_RDBIndex.__init__(astm_RDBIndex(False, False, astm_RDBIndex=astm_RDBTableDefinition(), astm_RDBIndex286=set()), False, False, astm_RDBIndex=astm_RDBTableDefinition(), astm_RDBIndex286=set()) == None


from python_code import astm_IncludeUnit
from python_code import astm_RDBIndexColumn

def test_astm_RDBIndexColumn___init__():
    assert astm_RDBIndexColumn.__init__(astm_RDBIndexColumn('', astm_RDBIndexColumn=astm_IncludeUnit()), '', astm_RDBIndexColumn=astm_IncludeUnit()) == None


from python_code import astm_NamedType
from python_code import astm_Type
from python_code import astm_TypesCatchBlock
from python_code import astm_UnnamedTypeReference

def test_astm_Type___init__():
    assert astm_Type.__init__(astm_Type(False, False, astm_Type=astm_NamedType(), astm_Type111=astm_UnnamedTypeReference(), astm_Type177=astm_TypesCatchBlock()), False, False, astm_Type=astm_NamedType(), astm_Type111=astm_UnnamedTypeReference(), astm_Type177=astm_TypesCatchBlock()) == None


from python_code import astm_VariableDeclaration

def test_astm_VariableDeclaration___init__():
    assert astm_VariableDeclaration.__init__(astm_VariableDeclaration(True), False) == None

