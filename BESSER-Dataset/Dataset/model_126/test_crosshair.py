from python_code import astm_Comment

def test_astm_Comment___init__():
    assert astm_Comment.__init__(astm_Comment(''), '') == None


from python_code import astm_CompilationUnit
from python_code import astm_ProgramScope
from python_code import astm_Project

def test_astm_CompilationUnit___init__():
    assert astm_CompilationUnit.__init__(astm_CompilationUnit('', astm_CompilationUnit=astm_Project(), astm_CompilationUnit37=set(), astm_CompilationUnit40=astm_ProgramScope()), '', astm_CompilationUnit=astm_Project(), astm_CompilationUnit37=set(), astm_CompilationUnit40=astm_ProgramScope()) == None


from python_code import astm_DataDefinition
from python_code import astm_Expression
from python_code import astm_VariableCatchBlock

def test_astm_DataDefinition___init__():
    assert astm_DataDefinition.__init__(astm_DataDefinition(True, astm_DataDefinition=astm_Expression(), astm_DataDefinition206=astm_VariableCatchBlock()), False, astm_DataDefinition=astm_Expression(), astm_DataDefinition206=astm_VariableCatchBlock()) == None


from python_code import astm_DeclarationOrDefinition
from python_code import astm_OtherSyntaxObject

def test_astm_DeclarationOrDefinition___init__():
    assert astm_DeclarationOrDefinition.__init__(astm_DeclarationOrDefinition(False, '\x00', astm_DeclarationOrDefinition=astm_OtherSyntaxObject(), astm_DeclarationOrDefinition43=astm_OtherSyntaxObject()), False, '\x00', astm_DeclarationOrDefinition=astm_OtherSyntaxObject(), astm_DeclarationOrDefinition43=astm_OtherSyntaxObject()) == None


from python_code import astm_ClassType
from python_code import astm_DerivesFrom
from python_code import astm_NamedType
from python_code import astm_OtherSyntaxObject

def test_astm_DerivesFrom___init__():
    assert astm_DerivesFrom.__init__(astm_DerivesFrom(True, astm_DerivesFrom131=astm_OtherSyntaxObject(), astm_DerivesFrom134=astm_NamedType(), astm_DerivesFrom=astm_ClassType()), False, astm_DerivesFrom131=astm_OtherSyntaxObject(), astm_DerivesFrom134=astm_NamedType(), astm_DerivesFrom=astm_ClassType()) == None


from python_code import astm_FunctionDeclaration
from python_code import astm_FunctionDefinition
from python_code import astm_FunctionMemberAttributes
from python_code import astm_VirtualSpecification

def test_astm_FunctionMemberAttributes___init__():
    assert astm_FunctionMemberAttributes.__init__(astm_FunctionMemberAttributes(False, False, False, astm_FunctionMemberAttributes=astm_FunctionDeclaration(), astm_FunctionMemberAttributes71=astm_FunctionDefinition(), astm_FunctionMemberAttributes75=astm_VirtualSpecification()), False, False, False, astm_FunctionMemberAttributes=astm_FunctionDeclaration(), astm_FunctionMemberAttributes71=astm_FunctionDefinition(), astm_FunctionMemberAttributes75=astm_VirtualSpecification()) == None


from python_code import astm_Literal

def test_astm_Literal___init__():
    assert astm_Literal.__init__(astm_Literal(''), '') == None


from python_code import astm_MacroCall
from python_code import astm_MacroDefinition

def test_astm_MacroDefinition___init__():
    assert astm_MacroDefinition.__init__(astm_MacroDefinition('', '\x00', astm_MacroDefinition=astm_MacroCall()), '\x00\x00', '', astm_MacroDefinition=astm_MacroCall()) == None


from python_code import astm_Declaration
from python_code import astm_Definition
from python_code import astm_DelphiUnit
from python_code import astm_LabelAccess
from python_code import astm_LabelDefinition
from python_code import astm_Name
from python_code import astm_NameReference
from python_code import astm_NameSpaceDefinition
from python_code import astm_NamedTypeReference
from python_code import astm_TypeDefinition

def test_astm_Name___init__():
    assert astm_Name.__init__(astm_Name('', astm_Name=astm_DelphiUnit(), astm_Name46=astm_Definition(), astm_Name53=astm_Declaration(), astm_Name87=astm_TypeDefinition(), astm_Name98=astm_LabelDefinition(), astm_Name91=astm_NameSpaceDefinition(), astm_Name140=astm_NamedTypeReference(), astm_Name213=astm_NameReference(), astm_Name277=astm_LabelAccess()), '', astm_Name=astm_DelphiUnit(), astm_Name46=astm_Definition(), astm_Name53=astm_Declaration(), astm_Name87=astm_TypeDefinition(), astm_Name98=astm_LabelDefinition(), astm_Name91=astm_NameSpaceDefinition(), astm_Name140=astm_NamedTypeReference(), astm_Name213=astm_NameReference(), astm_Name277=astm_LabelAccess()) == None


from python_code import astm_PrimitiveType

def test_astm_PrimitiveType___init__():
    assert astm_PrimitiveType.__init__(astm_PrimitiveType(True), False) == None


from python_code import astm_NamedType
from python_code import astm_Type
from python_code import astm_TypesCatchBlock
from python_code import astm_UnnamedTypeReference

def test_astm_Type___init__():
    assert astm_Type.__init__(astm_Type(False, False, astm_Type204=astm_TypesCatchBlock(), astm_Type=astm_NamedType(), astm_Type137=astm_UnnamedTypeReference()), False, False, astm_Type204=astm_TypesCatchBlock(), astm_Type=astm_NamedType(), astm_Type137=astm_UnnamedTypeReference()) == None


from python_code import astm_VariableDeclaration

def test_astm_VariableDeclaration___init__():
    assert astm_VariableDeclaration.__init__(astm_VariableDeclaration(True), False) == None

