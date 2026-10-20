from python_code import gastm_Comment

def test_gastm_Comment___init__():
    assert gastm_Comment.__init__(gastm_Comment(''), '') == None


from python_code import gastm_CompilationUnit
from python_code import gastm_ProgramScope
from python_code import gastm_Project

def test_gastm_CompilationUnit___init__():
    assert gastm_CompilationUnit.__init__(gastm_CompilationUnit('', gastm_CompilationUnit=set(), gastm_CompilationUnit9=gastm_ProgramScope(), gastm_CompilationUnit16=gastm_Project()), '', gastm_CompilationUnit=set(), gastm_CompilationUnit9=gastm_ProgramScope(), gastm_CompilationUnit16=gastm_Project()) == None


from python_code import gastm_DataDefinition
from python_code import gastm_Expression
from python_code import gastm_VariableCatchBlock

def test_gastm_DataDefinition___init__():
    assert gastm_DataDefinition.__init__(gastm_DataDefinition('', gastm_DataDefinition=gastm_Expression(), gastm_DataDefinition197=gastm_VariableCatchBlock()), '', gastm_DataDefinition=gastm_Expression(), gastm_DataDefinition197=gastm_VariableCatchBlock()) == None


from python_code import gastm_AccessKind
from python_code import gastm_DeclarationOrDefinition
from python_code import gastm_StorageSpecification

def test_gastm_DeclarationOrDefinition___init__():
    assert gastm_DeclarationOrDefinition.__init__(gastm_DeclarationOrDefinition('', gastm_DeclarationOrDefinition=gastm_StorageSpecification(), gastm_DeclarationOrDefinition44=gastm_AccessKind()), '', gastm_DeclarationOrDefinition=gastm_StorageSpecification(), gastm_DeclarationOrDefinition44=gastm_AccessKind()) == None


from python_code import gastm_FunctionDeclaration
from python_code import gastm_FunctionDefinition
from python_code import gastm_FunctionMemberAttributes
from python_code import gastm_VirtualSpecification

def test_gastm_FunctionMemberAttributes___init__():
    assert gastm_FunctionMemberAttributes.__init__(gastm_FunctionMemberAttributes('', '', '\x00\x00', gastm_FunctionMemberAttributes=gastm_VirtualSpecification(), gastm_FunctionMemberAttributes82=gastm_FunctionDefinition(), gastm_FunctionMemberAttributes97=gastm_FunctionDeclaration()), '', '', '', gastm_FunctionMemberAttributes=gastm_VirtualSpecification(), gastm_FunctionMemberAttributes82=gastm_FunctionDefinition(), gastm_FunctionMemberAttributes97=gastm_FunctionDeclaration()) == None


from python_code import gastm_IntegralType

def test_gastm_IntegralType___init__():
    assert gastm_IntegralType.__init__(gastm_IntegralType(''), '') == None


from python_code import gastm_Literal

def test_gastm_Literal___init__():
    assert gastm_Literal.__init__(gastm_Literal(''), '') == None


from python_code import gastm_MacroCall
from python_code import gastm_MacroDefinition

def test_gastm_MacroDefinition___init__():
    assert gastm_MacroDefinition.__init__(gastm_MacroDefinition('', '\x00', gastm_MacroDefinition=gastm_MacroCall()), '\x00\x00', '', gastm_MacroDefinition=gastm_MacroCall()) == None


from python_code import gastm_AggregateType
from python_code import gastm_DefinitionObject
from python_code import gastm_MemberObject

def test_gastm_MemberObject___init__():
    assert gastm_MemberObject.__init__(gastm_MemberObject('', gastm_MemberObject=gastm_DefinitionObject(), gastm_MemberObject117=gastm_AggregateType()), '', gastm_MemberObject=gastm_DefinitionObject(), gastm_MemberObject117=gastm_AggregateType()) == None


from python_code import gastm_Declaration
from python_code import gastm_Definition
from python_code import gastm_LabelAccess
from python_code import gastm_LabelDefinition
from python_code import gastm_Name
from python_code import gastm_NameReference
from python_code import gastm_NameSpaceDefinition
from python_code import gastm_NamedTypeReference
from python_code import gastm_TypeDefinition

def test_gastm_Name___init__():
    assert gastm_Name.__init__(gastm_Name('', gastm_Name=gastm_TypeDefinition(), gastm_Name48=gastm_NameSpaceDefinition(), gastm_Name55=gastm_LabelDefinition(), gastm_Name69=gastm_Declaration(), gastm_Name133=gastm_NamedTypeReference(), gastm_Name61=gastm_Definition(), gastm_Name239=gastm_NameReference(), gastm_Name245=gastm_LabelAccess()), '', gastm_Name=gastm_TypeDefinition(), gastm_Name48=gastm_NameSpaceDefinition(), gastm_Name55=gastm_LabelDefinition(), gastm_Name69=gastm_Declaration(), gastm_Name133=gastm_NamedTypeReference(), gastm_Name61=gastm_Definition(), gastm_Name239=gastm_NameReference(), gastm_Name245=gastm_LabelAccess()) == None


from python_code import gastm_NumberType

def test_gastm_NumberType___init__():
    assert gastm_NumberType.__init__(gastm_NumberType(''), '') == None


from python_code import gastm_PointerType

def test_gastm_PointerType___init__():
    assert gastm_PointerType.__init__(gastm_PointerType(''), '') == None


from python_code import gastm_RealType

def test_gastm_RealType___init__():
    assert gastm_RealType.__init__(gastm_RealType(''), '') == None


from python_code import gastm_SwitchCase
from python_code import gastm_SwitchStatement

def test_gastm_SwitchCase___init__():
    assert gastm_SwitchCase.__init__(gastm_SwitchCase('', gastm_SwitchCase=set(), gastm_SwitchCase165=gastm_SwitchStatement()), '', gastm_SwitchCase=set(), gastm_SwitchCase165=gastm_SwitchStatement()) == None


from python_code import gastm_NamedType
from python_code import gastm_Type
from python_code import gastm_TypesCatchBlock
from python_code import gastm_UnnamedTypeReference

def test_gastm_Type___init__():
    assert gastm_Type.__init__(gastm_Type('', gastm_Type=gastm_NamedType(), gastm_Type130=gastm_UnnamedTypeReference(), gastm_Type195=gastm_TypesCatchBlock()), '', gastm_Type=gastm_NamedType(), gastm_Type130=gastm_UnnamedTypeReference(), gastm_Type195=gastm_TypesCatchBlock()) == None


from python_code import gastm_VariableDeclaration

def test_gastm_VariableDeclaration___init__():
    assert gastm_VariableDeclaration.__init__(gastm_VariableDeclaration(''), '') == None

