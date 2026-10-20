from python_code import ir_ArgOrVar
from python_code import ir_ArgOrVarRef

def test_ir_ArgOrVar___init__():
    assert ir_ArgOrVar.__init__(ir_ArgOrVar('', ir_ArgOrVar=ir_ArgOrVarRef()), '', ir_ArgOrVar=ir_ArgOrVarRef()) == None


from python_code import ir_BinaryExpression
from python_code import ir_Expression

def test_ir_BinaryExpression___init__():
    assert ir_BinaryExpression.__init__(ir_BinaryExpression('', ir_BinaryExpression=ir_Expression(), ir_BinaryExpression164=ir_Expression()), '', ir_BinaryExpression=ir_Expression(), ir_BinaryExpression164=ir_Expression()) == None


from python_code import ir_BoolConstant

def test_ir_BoolConstant___init__():
    assert ir_BoolConstant.__init__(ir_BoolConstant(True), False) == None


from python_code import ir_Exit

def test_ir_Exit___init__():
    assert ir_Exit.__init__(ir_Exit(''), '') == None


from python_code import ir_IntConstant

def test_ir_IntConstant___init__():
    assert ir_IntConstant.__init__(ir_IntConstant(0), 0) == None


from python_code import ir_IrAnnotable
from python_code import ir_IrAnnotation

def test_ir_IrAnnotation___init__():
    assert ir_IrAnnotation.__init__(ir_IrAnnotation('', ir_IrAnnotation=ir_IrAnnotable(), ir_IrAnnotation2=set()), '', ir_IrAnnotation=ir_IrAnnotable(), ir_IrAnnotation2=set()) == None


from python_code import ir_ConnectivityCall
from python_code import ir_ItemId
from python_code import ir_ItemIdDefinition
from python_code import ir_ItemIndexValue

def test_ir_ItemId___init__():
    assert ir_ItemId.__init__(ir_ItemId('', '\x00', ir_ItemId=ir_ItemIdDefinition(), ir_ItemId212=ir_ConnectivityCall(), ir_ItemId221=ir_ItemIndexValue()), '\x00\x00', '', ir_ItemId=ir_ItemIdDefinition(), ir_ItemId212=ir_ConnectivityCall(), ir_ItemId221=ir_ItemIndexValue()) == None


from python_code import ir_ItemIdValueIterator
from python_code import ir_Iterator

def test_ir_ItemIdValueIterator___init__():
    assert ir_ItemIdValueIterator.__init__(ir_ItemIdValueIterator(0, ir_ItemIdValueIterator=ir_Iterator()), 0, ir_ItemIdValueIterator=ir_Iterator()) == None


from python_code import ir_ArgOrVarRef
from python_code import ir_ItemIndex
from python_code import ir_ItemIndexDefinition
from python_code import ir_Iterator

def test_ir_ItemIndex___init__():
    assert ir_ItemIndex.__init__(ir_ItemIndex('', '\x00', ir_ItemIndex=ir_ItemIndexDefinition(), ir_ItemIndex140=ir_Iterator(), ir_ItemIndex185=ir_ArgOrVarRef()), '\x00\x00', '', ir_ItemIndex=ir_ItemIndexDefinition(), ir_ItemIndex140=ir_Iterator(), ir_ItemIndex185=ir_ArgOrVarRef()) == None


from python_code import ir_Instruction
from python_code import ir_Loop

def test_ir_Loop___init__():
    assert ir_Loop.__init__(ir_Loop(True, ir_Loop=ir_Instruction()), False, ir_Loop=ir_Instruction()) == None


from python_code import ir_RealConstant

def test_ir_RealConstant___init__():
    assert ir_RealConstant.__init__(ir_RealConstant(0.0), 0.0) == None


from python_code import ir_ConnectivityCall
from python_code import ir_SetDefinition
from python_code import ir_SetRef

def test_ir_SetDefinition___init__():
    assert ir_SetDefinition.__init__(ir_SetDefinition('', ir_SetDefinition=ir_ConnectivityCall(), ir_SetDefinition214=ir_SetRef()), '', ir_SetDefinition=ir_ConnectivityCall(), ir_SetDefinition214=ir_SetRef()) == None


from python_code import ir_Expression
from python_code import ir_UnaryExpression

def test_ir_UnaryExpression___init__():
    assert ir_UnaryExpression.__init__(ir_UnaryExpression('', ir_UnaryExpression=ir_Expression()), '', ir_UnaryExpression=ir_Expression()) == None

