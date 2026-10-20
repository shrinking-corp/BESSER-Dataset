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
    assert astm_DerivesFrom.__init__(astm_DerivesFrom(True, astm_DerivesFrom105=astm_OtherSyntaxObject(), astm_DerivesFrom108=astm_NamedType(), astm_DerivesFrom=astm_ClassType()), False, astm_DerivesFrom105=astm_OtherSyntaxObject(), astm_DerivesFrom108=astm_NamedType(), astm_DerivesFrom=astm_ClassType()) == None


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


from python_code import astm_Declaration
from python_code import astm_Definition
from python_code import astm_LabelAccess
from python_code import astm_LabelDefinition
from python_code import astm_Name
from python_code import astm_NameReference
from python_code import astm_NameSpaceDefinition
from python_code import astm_NamedTypeReference
from python_code import astm_TypeDefinition

def test_astm_Name___init__():
    assert astm_Name.__init__(astm_Name('', astm_Name=astm_Definition(), astm_Name30=astm_Declaration(), astm_Name72=astm_LabelDefinition(), astm_Name61=astm_TypeDefinition(), astm_Name113=astm_NamedTypeReference(), astm_Name186=astm_NameReference(), astm_Name65=astm_NameSpaceDefinition(), astm_Name251=astm_LabelAccess()), '', astm_Name=astm_Definition(), astm_Name30=astm_Declaration(), astm_Name72=astm_LabelDefinition(), astm_Name61=astm_TypeDefinition(), astm_Name113=astm_NamedTypeReference(), astm_Name186=astm_NameReference(), astm_Name65=astm_NameSpaceDefinition(), astm_Name251=astm_LabelAccess()) == None


from python_code import astm_PrimitiveType

def test_astm_PrimitiveType___init__():
    assert astm_PrimitiveType.__init__(astm_PrimitiveType(True), False) == None


from python_code import astm_SpecificClassType

def test_astm_SpecificClassType___init__():
    assert astm_SpecificClassType.__init__(astm_SpecificClassType('', '\x00'), '\x00\x00', '') == None


from python_code import astm_NamedType
from python_code import astm_Type
from python_code import astm_TypesCatchBlock
from python_code import astm_UnnamedTypeReference

def test_astm_Type___init__():
    assert astm_Type.__init__(astm_Type(False, False, astm_Type111=astm_UnnamedTypeReference(), astm_Type177=astm_TypesCatchBlock(), astm_Type=astm_NamedType()), False, False, astm_Type111=astm_UnnamedTypeReference(), astm_Type177=astm_TypesCatchBlock(), astm_Type=astm_NamedType()) == None


from python_code import astm_VariableDeclaration

def test_astm_VariableDeclaration___init__():
    assert astm_VariableDeclaration.__init__(astm_VariableDeclaration(True), False) == None

