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
    assert gast_annotations_Comment.__init__(gast_annotations_Comment(False, False, 0, ''), False, False, 0, '') == None

def test_gast_annotations_Comment_OCLtodo():
    assert gast_annotations_Comment.OCLtodo(gast_annotations_Comment(False, False, 0, ''), '', '') == None


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


from python_code import BlockStatement
from python_code import DeclarationTypeAccess
from python_code import gast_functions_Function

def test_gast_functions_Function___init__():
    assert gast_functions_Function.__init__(gast_functions_Function(0, 0, 0, 0, 0, 0, False, function=DeclarationTypeAccess(), surroundingFunction=set(), surroundingFunction289=set(), gast_functions_Function=set(), gast_functions_Function293=set(), gast_functions_Function295=set(), surroundingFunction298=BlockStatement(), surroundingFunction301=set()), 0, 0, 0, 0, 0, 0, True, function=DeclarationTypeAccess(), surroundingFunction=set(), surroundingFunction289=set(), gast_functions_Function=set(), gast_functions_Function293=set(), gast_functions_Function295=set(), surroundingFunction298=BlockStatement(), surroundingFunction301=set()) == None


from python_code import GASTClass
from python_code import Property
from python_code import gast_functions_Method

def test_gast_functions_Method___init__():
    assert gast_functions_Method.__init__(gast_functions_Method(False, gast_functions_Method=Property(), methods=GASTClass()), True, gast_functions_Method=Property(), methods=GASTClass()) == None

