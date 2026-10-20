from python_code import gast_accesses_InheritanceTypeAccess

def test_gast_accesses_InheritanceTypeAccess___init__():
    assert gast_accesses_InheritanceTypeAccess.__init__(gast_accesses_InheritanceTypeAccess(True), False) == None


from python_code import gast_accesses_SelfAccess

def test_gast_accesses_SelfAccess___init__():
    assert gast_accesses_SelfAccess.__init__(gast_accesses_SelfAccess(True), False) == None


from python_code import gast_accesses_ThrowTypeAccess

def test_gast_accesses_ThrowTypeAccess___init__():
    assert gast_accesses_ThrowTypeAccess.__init__(gast_accesses_ThrowTypeAccess(True), False) == None


from python_code import gast_annotations_Comment

def test_gast_annotations_Comment___init__():
    assert gast_annotations_Comment.__init__(gast_annotations_Comment(False, 0, '', False), False, 0, '', True) == None

def test_gast_annotations_Comment_OCLtodo():
    assert gast_annotations_Comment.OCLtodo(gast_annotations_Comment(False, 0, '', False), '', '') == None


from python_code import BasePath
from python_code import Directory
from python_code import gast_core_Directory

def test_gast_core_Directory___init__():
    assert gast_core_Directory.__init__(gast_core_Directory('', '', parentDirectory=set(), subDirectory=Directory(), directory=set(), directories=BasePath()), '', '', parentDirectory=set(), subDirectory=Directory(), directory=set(), directories=BasePath()) == None


from python_code import gast_core_Identifier

def test_gast_core_Identifier___init__():
    assert gast_core_Identifier.__init__(gast_core_Identifier(''), '') == None

def test_gast_core_Identifier_idHasToBeUnique():
    assert gast_core_Identifier.idHasToBeUnique(gast_core_Identifier(''), 0, '\x00\x00') == None


from python_code import gast_core_ModelElement

def test_gast_core_ModelElement___init__():
    assert gast_core_ModelElement.__init__(gast_core_ModelElement('\x00\x00', 0, gast_core_ModelElement=set()), '', 0, gast_core_ModelElement=set()) == None


from python_code import GASTClass
from python_code import gast_functions_Constructor

def test_gast_functions_Constructor___init__():
    assert gast_functions_Constructor.__init__(gast_functions_Constructor(False, constructors=GASTClass()), True, constructors=GASTClass()) == None


from python_code import GASTClass
from python_code import Property
from python_code import gast_functions_Method

def test_gast_functions_Method___init__():
    assert gast_functions_Method.__init__(gast_functions_Method(False, gast_functions_Method=Property(), methods=GASTClass()), True, gast_functions_Method=Property(), methods=GASTClass()) == None


from python_code import gast_statements_FlowInstr

def test_gast_statements_FlowInstr___init__():
    assert gast_statements_FlowInstr.__init__(gast_statements_FlowInstr('', gast_statements_FlowInstr=set(), gast_statements_FlowInstr50=set(), cfPrev=set(), cfnext=set()), '', gast_statements_FlowInstr=set(), gast_statements_FlowInstr50=set(), cfPrev=set(), cfnext=set()) == None


from python_code import GASTExpression
from python_code import gast_statements_JumpStatement

def test_gast_statements_JumpStatement___init__():
    assert gast_statements_JumpStatement.__init__(gast_statements_JumpStatement('', gast_statements_JumpStatement=GASTExpression()), '', gast_statements_JumpStatement=GASTExpression()) == None


from python_code import Exit
from python_code import gast_statements_Methods

def test_gast_statements_Methods___init__():
    assert gast_statements_Methods.__init__(gast_statements_Methods('', gast_statements_Methods=Exit()), '', gast_statements_Methods=Exit()) == None


from python_code import gast_statements_Var

def test_gast_statements_Var___init__():
    assert gast_statements_Var.__init__(gast_statements_Var(''), '') == None


from python_code import GASTType
from python_code import gast_types_GASTArray

def test_gast_types_GASTArray___init__():
    assert gast_types_GASTArray.__init__(gast_types_GASTArray(0, gast_types_GASTArray=GASTType()), 0, gast_types_GASTArray=GASTType()) == None


from python_code import gast_types_GASTType

def test_gast_types_GASTType___init__():
    assert gast_types_GASTType.__init__(gast_types_GASTType('', False), '', False) == None


from python_code import File
from python_code import Member
from python_code import SourceEntity
from python_code import gast_core_Position
from python_code import gast_types_Member

def test_gast_types_Member___init__():
    assert gast_types_Member.__init__(gast_types_Member('', False, False, False, False, False, False, False, False, False, gast_types_Member=Member(), SourceEntity=gast_core_Position(0, 0, 0, 0, gast_core_Position=File(), gast_core_Position163=File(), position=SourceEntity())), '', False, False, True, False, False, False, True, False, False, gast_types_Member=Member(), SourceEntity=gast_core_Position(0, 0, 0, 0, gast_core_Position=File(), gast_core_Position163=File(), position=SourceEntity())) == None

def test_gast_types_Member_getSurroundingClass():
    assert gast_types_Member.getSurroundingClass(gast_types_Member('', False, False, False, False, False, False, False, False, False, gast_types_Member=Member(), SourceEntity=gast_core_Position(0, 0, 0, 0, gast_core_Position=File(), gast_core_Position163=File(), position=SourceEntity()))) == None


from python_code import GASTType
from python_code import gast_types_Reference

def test_gast_types_Reference___init__():
    assert gast_types_Reference.__init__(gast_types_Reference(False, gast_types_Reference=GASTType()), False, gast_types_Reference=GASTType()) == None


from python_code import GASTClass
from python_code import GASTType
from python_code import Package
from python_code import gast_types_TypeAlias

def test_gast_types_TypeAlias___init__():
    assert gast_types_TypeAlias.__init__(gast_types_TypeAlias(False, gast_types_TypeAlias=GASTType(), innerTypeAliases=GASTClass(), typeAliases=Package()), False, gast_types_TypeAlias=GASTType(), innerTypeAliases=GASTClass(), typeAliases=Package()) == None


from python_code import GASTClass
from python_code import gast_variables_Field

def test_gast_variables_Field___init__():
    assert gast_variables_Field.__init__(gast_variables_Field(False, fields=GASTClass()), True, fields=GASTClass()) == None


from python_code import DeclarationTypeAccess
from python_code import GASTType
from python_code import gast_variables_Variable

def test_gast_variables_Variable___init__():
    assert gast_variables_Variable.__init__(gast_variables_Variable(False, gast_variables_Variable=GASTType(), surroundingVariable=DeclarationTypeAccess()), False, gast_variables_Variable=GASTType(), surroundingVariable=DeclarationTypeAccess()) == None

