from python_code import swrtj_Args

def test_swrtj_Args___init__():
    assert swrtj_Args.__init__(swrtj_Args(True), False) == None


from python_code import swrtj_AtomicBooleanExpression
from python_code import swrtj_BooleanExpression

def test_swrtj_AtomicBooleanExpression___init__():
    assert swrtj_AtomicBooleanExpression.__init__(swrtj_AtomicBooleanExpression(True, swrtj_AtomicBooleanExpression=swrtj_BooleanExpression()), False, swrtj_AtomicBooleanExpression=swrtj_BooleanExpression()) == None


from python_code import swrtj_BooleanConstant

def test_swrtj_BooleanConstant___init__():
    assert swrtj_BooleanConstant.__init__(swrtj_BooleanConstant(''), '') == None


from python_code import swrtj_BooleanExpression
from python_code import swrtj_BooleanOperator

def test_swrtj_BooleanOperator___init__():
    assert swrtj_BooleanOperator.__init__(swrtj_BooleanOperator('', swrtj_BooleanOperator=swrtj_BooleanExpression()), '', swrtj_BooleanOperator=swrtj_BooleanExpression()) == None


from python_code import swrtj_CompareOperator
from python_code import swrtj_SimpleComparation

def test_swrtj_CompareOperator___init__():
    assert swrtj_CompareOperator.__init__(swrtj_CompareOperator('', swrtj_CompareOperator=swrtj_SimpleComparation()), '', swrtj_CompareOperator=swrtj_SimpleComparation()) == None


from python_code import swrtj_Block
from python_code import swrtj_Class
from python_code import swrtj_Constructor

def test_swrtj_Constructor___init__():
    assert swrtj_Constructor.__init__(swrtj_Constructor('', swrtj_Constructor=swrtj_Class(), swrtj_Constructor50=set(), swrtj_Constructor53=swrtj_Block()), '', swrtj_Constructor=swrtj_Class(), swrtj_Constructor50=set(), swrtj_Constructor53=swrtj_Block()) == None


from python_code import swrtj_Element
from python_code import swrtj_File

def test_swrtj_Element___init__():
    assert swrtj_Element.__init__(swrtj_Element('', '\x00', swrtj_Element=swrtj_File()), '\x00\x00', '', swrtj_Element=swrtj_File()) == None


from python_code import swrtj_Expression

def test_swrtj_Expression___init__():
    assert swrtj_Expression.__init__(swrtj_Expression('\x00\x00', '', swrtj_Expression=set()), '', '', swrtj_Expression=set()) == None


from python_code import swrtj_FieldDeclaration

def test_swrtj_FieldDeclaration___init__():
    assert swrtj_FieldDeclaration.__init__(swrtj_FieldDeclaration(''), '') == None


from python_code import swrtj_Field
from python_code import swrtj_FieldAccess
from python_code import swrtj_FieldName
from python_code import swrtj_RecordExclude
from python_code import swrtj_RecordRename
from python_code import swrtj_TraitFieldRename

def test_swrtj_FieldName___init__():
    assert swrtj_FieldName.__init__(swrtj_FieldName('', swrtj_FieldName120=swrtj_FieldAccess(), swrtj_FieldName127=swrtj_RecordExclude(), swrtj_FieldName129=swrtj_RecordRename(), swrtj_FieldName132=swrtj_RecordRename(), swrtj_FieldName146=swrtj_TraitFieldRename(), swrtj_FieldName149=swrtj_TraitFieldRename(), swrtj_FieldName=swrtj_Field()), '', swrtj_FieldName120=swrtj_FieldAccess(), swrtj_FieldName127=swrtj_RecordExclude(), swrtj_FieldName129=swrtj_RecordRename(), swrtj_FieldName132=swrtj_RecordRename(), swrtj_FieldName146=swrtj_TraitFieldRename(), swrtj_FieldName149=swrtj_TraitFieldRename(), swrtj_FieldName=swrtj_Field()) == None


from python_code import swrtj_File
from python_code import swrtj_Import

def test_swrtj_Import___init__():
    assert swrtj_Import.__init__(swrtj_Import('', swrtj_Import=swrtj_File()), '', swrtj_Import=swrtj_File()) == None


from python_code import swrtj_Input

def test_swrtj_Input___init__():
    assert swrtj_Input.__init__(swrtj_Input(True), False) == None


from python_code import swrtj_Method
from python_code import swrtj_MethodInvocation
from python_code import swrtj_MethodName
from python_code import swrtj_TraitAlias
from python_code import swrtj_TraitExclude
from python_code import swrtj_TraitMethodRename

def test_swrtj_MethodName___init__():
    assert swrtj_MethodName.__init__(swrtj_MethodName('', swrtj_MethodName=swrtj_Method(), swrtj_MethodName115=swrtj_MethodInvocation(), swrtj_MethodName134=swrtj_TraitExclude(), swrtj_MethodName136=swrtj_TraitAlias(), swrtj_MethodName139=swrtj_TraitAlias(), swrtj_MethodName141=swrtj_TraitMethodRename(), swrtj_MethodName144=swrtj_TraitMethodRename()), '', swrtj_MethodName=swrtj_Method(), swrtj_MethodName115=swrtj_MethodInvocation(), swrtj_MethodName134=swrtj_TraitExclude(), swrtj_MethodName136=swrtj_TraitAlias(), swrtj_MethodName139=swrtj_TraitAlias(), swrtj_MethodName141=swrtj_TraitMethodRename(), swrtj_MethodName144=swrtj_TraitMethodRename()) == None


from python_code import swrtj_Null

def test_swrtj_Null___init__():
    assert swrtj_Null.__init__(swrtj_Null(True), False) == None


from python_code import swrtj_Number

def test_swrtj_Number___init__():
    assert swrtj_Number.__init__(swrtj_Number(0), 0) == None


from python_code import swrtj_Output

def test_swrtj_Output___init__():
    assert swrtj_Output.__init__(swrtj_Output(True), False) == None


from python_code import swrtj_Block
from python_code import swrtj_ProvidedMethod
from python_code import swrtj_ReturnStatement

def test_swrtj_ProvidedMethod___init__():
    assert swrtj_ProvidedMethod.__init__(swrtj_ProvidedMethod(True, swrtj_ProvidedMethod153=swrtj_ReturnStatement(), swrtj_ProvidedMethod=swrtj_Block()), False, swrtj_ProvidedMethod153=swrtj_ReturnStatement(), swrtj_ProvidedMethod=swrtj_Block()) == None


from python_code import swrtj_StringConstant

def test_swrtj_StringConstant___init__():
    assert swrtj_StringConstant.__init__(swrtj_StringConstant(''), '') == None


from python_code import swrtj_This

def test_swrtj_This___init__():
    assert swrtj_This.__init__(swrtj_This(True), False) == None

