from python_code import becontent_Apply

def test_becontent_Apply___init__():
    assert becontent_Apply.__init__(becontent_Apply(''), '') == None


from python_code import becontent_ApplyItem

def test_becontent_ApplyItem___init__():
    assert becontent_ApplyItem.__init__(becontent_ApplyItem('', '\x00'), '\x00\x00', '') == None


from python_code import becontent_AttributeInteger

def test_becontent_AttributeInteger___init__():
    assert becontent_AttributeInteger.__init__(becontent_AttributeInteger(True), False) == None


from python_code import becontent_AttributeVarchar

def test_becontent_AttributeVarchar___init__():
    assert becontent_AttributeVarchar.__init__(becontent_AttributeVarchar(0, False), 0, False) == None


from python_code import becontent_Checkbox

def test_becontent_Checkbox___init__():
    assert becontent_Checkbox.__init__(becontent_Checkbox('\x00\x00', '', '', True), '', '', '', False) == None


from python_code import becontent_Color

def test_becontent_Color___init__():
    assert becontent_Color.__init__(becontent_Color('', '', '\x00\x00'), '', '', '') == None


from python_code import becontent_Copy

def test_becontent_Copy___init__():
    assert becontent_Copy.__init__(becontent_Copy('', '\x00'), '\x00\x00', '') == None


from python_code import becontent_Date

def test_becontent_Date___init__():
    assert becontent_Date.__init__(becontent_Date('', '', False), '\x00', '', False) == None


from python_code import becontent_Editor

def test_becontent_Editor___init__():
    assert becontent_Editor.__init__(becontent_Editor(0, False, '', '', 0), 0, False, '', '', 0) == None


from python_code import becontent_ExtendedForm

def test_becontent_ExtendedForm___init__():
    assert becontent_ExtendedForm.__init__(becontent_ExtendedForm(''), '') == None


from python_code import becontent_File

def test_becontent_File___init__():
    assert becontent_File.__init__(becontent_File('', '', False, '', ''), '', '', False, '', '') == None


from python_code import becontent_FileToFolder

def test_becontent_FileToFolder___init__():
    assert becontent_FileToFolder.__init__(becontent_FileToFolder('', '', False, '', ''), '', '', False, '', '') == None


from python_code import becontent_AttributeFileToFolder
from python_code import becontent_FileToFolderExtension
from python_code import becontent_SystemAttributeFileToFolder

def test_becontent_FileToFolderExtension___init__():
    assert becontent_FileToFolderExtension.__init__(becontent_FileToFolderExtension('', '', '\x00\x00', becontent_FileToFolderExtension=becontent_AttributeFileToFolder(), becontent_FileToFolderExtension23=becontent_SystemAttributeFileToFolder()), '', '', '', becontent_FileToFolderExtension=becontent_AttributeFileToFolder(), becontent_FileToFolderExtension23=becontent_SystemAttributeFileToFolder()) == None


from python_code import becontent_Hidden

def test_becontent_Hidden___init__():
    assert becontent_Hidden.__init__(becontent_Hidden('', '\x00'), '\x00\x00', '') == None


from python_code import becontent_HierarchicalPosition

def test_becontent_HierarchicalPosition___init__():
    assert becontent_HierarchicalPosition.__init__(becontent_HierarchicalPosition('', '', '', '', 0), '', '', '', '', 0) == None


from python_code import becontent_Image

def test_becontent_Image___init__():
    assert becontent_Image.__init__(becontent_Image('', '', False), '\x00', '', False) == None


from python_code import becontent_Link

def test_becontent_Link___init__():
    assert becontent_Link.__init__(becontent_Link('', '', 0, False, 0), '', '', 0, False, 0) == None


from python_code import becontent_LongDate

def test_becontent_LongDate___init__():
    assert becontent_LongDate.__init__(becontent_LongDate('', '', False), '\x00', '', False) == None


from python_code import becontent_Parameter

def test_becontent_Parameter___init__():
    assert becontent_Parameter.__init__(becontent_Parameter('', '\x00'), '\x00\x00', '') == None


from python_code import becontent_Password

def test_becontent_Password___init__():
    assert becontent_Password.__init__(becontent_Password('', '', 0, False, 0), '', '', 0, False, 0) == None


from python_code import becontent_Position

def test_becontent_Position___init__():
    assert becontent_Position.__init__(becontent_Position('', '', '', 0, False), '', '', '', 0, False) == None


from python_code import becontent_Propagate

def test_becontent_Propagate___init__():
    assert becontent_Propagate.__init__(becontent_Propagate('', '\x00'), '\x00\x00', '') == None


from python_code import becontent_RadioButton

def test_becontent_RadioButton___init__():
    assert becontent_RadioButton.__init__(becontent_RadioButton('', '', '\x00\x00'), '', '', '') == None


from python_code import becontent_Relation

def test_becontent_Relation___init__():
    assert becontent_Relation.__init__(becontent_Relation('', '\x00'), '\x00\x00', '') == None


from python_code import becontent_RelationManager

def test_becontent_RelationManager___init__():
    assert becontent_RelationManager.__init__(becontent_RelationManager('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import becontent_Section

def test_becontent_Section___init__():
    assert becontent_Section.__init__(becontent_Section('', '\x00'), '\x00\x00', '') == None


from python_code import becontent_Select

def test_becontent_Select___init__():
    assert becontent_Select.__init__(becontent_Select('\x00\x00', '', '', True), '', '', '', False) == None


from python_code import becontent_Skinlet

def test_becontent_Skinlet___init__():
    assert becontent_Skinlet.__init__(becontent_Skinlet('', '\x00'), '\x00\x00', '') == None


from python_code import becontent_SystemAttributeInteger

def test_becontent_SystemAttributeInteger___init__():
    assert becontent_SystemAttributeInteger.__init__(becontent_SystemAttributeInteger(True), False) == None


from python_code import becontent_SystemAttributeVarchar

def test_becontent_SystemAttributeVarchar___init__():
    assert becontent_SystemAttributeVarchar.__init__(becontent_SystemAttributeVarchar(0, False), 0, False) == None


from python_code import becontent_SystemEntity
from python_code import becontent_SystemEntityField

def test_becontent_SystemEntityField___init__():
    assert becontent_SystemEntityField.__init__(becontent_SystemEntityField(False, False, False, False, becontent_SystemEntityField=becontent_SystemEntity()), False, False, False, True, becontent_SystemEntityField=becontent_SystemEntity()) == None


from python_code import becontent_SystemEntity
from python_code import becontent_SystemReference

def test_becontent_SystemReference___init__():
    assert becontent_SystemReference.__init__(becontent_SystemReference('', becontent_SystemReference=becontent_SystemEntity()), '', becontent_SystemReference=becontent_SystemEntity()) == None


from python_code import becontent_Template

def test_becontent_Template___init__():
    assert becontent_Template.__init__(becontent_Template('', '\x00'), '\x00\x00', '') == None


from python_code import becontent_Text

def test_becontent_Text___init__():
    assert becontent_Text.__init__(becontent_Text('', '', 0, False, 0), '', '', 0, False, 0) == None


from python_code import becontent_Textarea

def test_becontent_Textarea___init__():
    assert becontent_Textarea.__init__(becontent_Textarea('', '', 0, 0, False), '', '', 0, 0, False) == None


from python_code import becontent_Trigger

def test_becontent_Trigger___init__():
    assert becontent_Trigger.__init__(becontent_Trigger('', '\x00'), '\x00\x00', '') == None


from python_code import becontent_TypedAttribute

def test_becontent_TypedAttribute___init__():
    assert becontent_TypedAttribute.__init__(becontent_TypedAttribute('', False), '', False) == None


from python_code import becontent_TypedSystemAttribute

def test_becontent_TypedSystemAttribute___init__():
    assert becontent_TypedSystemAttribute.__init__(becontent_TypedSystemAttribute('', False), '', False) == None


from python_code import becontent_UnsetParameter

def test_becontent_UnsetParameter___init__():
    assert becontent_UnsetParameter.__init__(becontent_UnsetParameter(''), '') == None


from python_code import becontent_Year

def test_becontent_Year___init__():
    assert becontent_Year.__init__(becontent_Year('', '', 0, 0, False), '', '', 0, 0, False) == None

