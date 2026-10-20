from python_code import idl_Case
from python_code import idl_CaseLabel
from python_code import idl_ConstExp

def test_idl_CaseLabel___init__():
    assert idl_CaseLabel.__init__(idl_CaseLabel(False, False, idl_CaseLabel=idl_Case(), idl_CaseLabel107=idl_ConstExp()), False, False, idl_CaseLabel=idl_Case(), idl_CaseLabel107=idl_ConstExp()) == None


from python_code import idl_ComponentForwardDecl

def test_idl_ComponentForwardDecl___init__():
    assert idl_ComponentForwardDecl.__init__(idl_ComponentForwardDecl(''), '') == None


from python_code import idl_ConstrForwardDecl

def test_idl_ConstrForwardDecl___init__():
    assert idl_ConstrForwardDecl.__init__(idl_ConstrForwardDecl(''), '') == None


from python_code import idl_Declarator
from python_code import idl_ElementSpec
from python_code import idl_Member
from python_code import idl_TypeDeclarator

def test_idl_Declarator___init__():
    assert idl_Declarator.__init__(idl_Declarator('', idl_Declarator=idl_Member(), idl_Declarator114=idl_ElementSpec(), idl_Declarator90=idl_TypeDeclarator()), '', idl_Declarator=idl_Member(), idl_Declarator114=idl_ElementSpec(), idl_Declarator90=idl_TypeDeclarator()) == None


from python_code import idl_Event

def test_idl_Event___init__():
    assert idl_Event.__init__(idl_Event(False, '\x00'), False, '\x00') == None


from python_code import idl_EventDcl

def test_idl_EventDcl___init__():
    assert idl_EventDcl.__init__(idl_EventDcl(False, False, idl_EventDcl=set(), idl_EventDcl239=set(), idl_EventDcl242=set(), idl_EventDcl245=set()), False, False, idl_EventDcl=set(), idl_EventDcl239=set(), idl_EventDcl242=set(), idl_EventDcl245=set()) == None


from python_code import idl_Excluded_File_Marker

def test_idl_Excluded_File_Marker___init__():
    assert idl_Excluded_File_Marker.__init__(idl_Excluded_File_Marker(''), '') == None


from python_code import idl_File_Marker

def test_idl_File_Marker___init__():
    assert idl_File_Marker.__init__(idl_File_Marker(''), '') == None


from python_code import idl_FixedModule

def test_idl_FixedModule___init__():
    assert idl_FixedModule.__init__(idl_FixedModule('', idl_FixedModule=set()), '', idl_FixedModule=set()) == None


from python_code import idl_Forward_decl

def test_idl_Forward_decl___init__():
    assert idl_Forward_decl.__init__(idl_Forward_decl(''), '') == None


from python_code import idl_Import_decl
from python_code import idl_Specification

def test_idl_Import_decl___init__():
    assert idl_Import_decl.__init__(idl_Import_decl('', idl_Import_decl=idl_Specification()), '', idl_Import_decl=idl_Specification()) == None

