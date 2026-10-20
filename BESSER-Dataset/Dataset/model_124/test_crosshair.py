from python_code import astm_gastm_Comment
from python_code import astm_gastm_GASTMSyntaxObject

def test_astm_gastm_Comment___init__():
    assert astm_gastm_Comment.__init__(astm_gastm_Comment('', PreprocessorElement=astm_gastm_GASTMSyntaxObject()), '', PreprocessorElement=astm_gastm_GASTMSyntaxObject()) == None


from python_code import Expression
from python_code import astm_gastm_DataDefinition
from python_code import astm_gastm_Declaration

def test_astm_gastm_DataDefinition___init__():
    assert astm_gastm_DataDefinition.__init__(astm_gastm_DataDefinition(False, astm_gastm_DataDefinition=Expression(), Definition=astm_gastm_Declaration()), False, astm_gastm_DataDefinition=Expression(), Definition=astm_gastm_Declaration()) == None


from python_code import VirtualSpecification
from python_code import astm_gastm_FunctionMemberAttributes
from python_code import astm_gastm_Virtual

def test_astm_gastm_FunctionMemberAttributes___init__():
    assert astm_gastm_FunctionMemberAttributes.__init__(astm_gastm_FunctionMemberAttributes(True, True, False, astm_gastm_FunctionMemberAttributes=astm_gastm_Virtual()), False, True, False, astm_gastm_FunctionMemberAttributes=VirtualSpecification()) == None


from python_code import Expression
from python_code import astm_gastm_ActualParameterExpression
from python_code import astm_gastm_AnnotationExpression
from python_code import astm_gastm_ArrayAccess
from python_code import astm_gastm_BinaryExpression
from python_code import astm_gastm_BitFieldDefinition
from python_code import astm_gastm_CaseBlock
from python_code import astm_gastm_CastExpression
from python_code import astm_gastm_ConditionalExpression
from python_code import astm_gastm_DataDefinition
from python_code import astm_gastm_Declaration
from python_code import astm_gastm_DeleteStatement
from python_code import astm_gastm_Dimension
from python_code import astm_gastm_EnumLiteralDefinition
from python_code import astm_gastm_ExpressionStatement
from python_code import astm_gastm_ForStatement
from python_code import astm_gastm_FunctionCallExpression
from python_code import astm_gastm_IfStatement
from python_code import astm_gastm_JumpStatement
from python_code import astm_gastm_Literal
from python_code import astm_gastm_LoopStatement
from python_code import astm_gastm_QualifiedIdentifierReference
from python_code import astm_gastm_RangeExpression
from python_code import astm_gastm_ReturnStatement
from python_code import astm_gastm_SwitchStatement
from python_code import astm_gastm_ThrowStatement
from python_code import astm_gastm_UnaryExpression

def test_astm_gastm_Literal___init__():
    assert astm_gastm_Literal.__init__(astm_gastm_Literal('\x00', Expression115=astm_gastm_JumpStatement(), Expression243=astm_gastm_AnnotationExpression(), Expression128=astm_gastm_IfStatement(), Expression88=astm_gastm_Dimension(), Expression144=astm_gastm_ReturnStatement(), Expression142=astm_gastm_CaseBlock(), Expression217=astm_gastm_ConditionalExpression(), Expression168=astm_gastm_ThrowStatement(), Expression211=astm_gastm_ConditionalExpression(), Expression180=astm_gastm_ArrayAccess(), Expression136=astm_gastm_SwitchStatement(), Expression109=astm_gastm_DeleteStatement(), Expression151=astm_gastm_ForStatement(), Expression207=astm_gastm_BinaryExpression(), Expression55=astm_gastm_BitFieldDefinition(), Expression177=astm_gastm_ArrayAccess(), Expression154=astm_gastm_ForStatement(), Expression204=astm_gastm_BinaryExpression(), Expression199=astm_gastm_UnaryExpression(), Expression113=astm_gastm_ExpressionStatement(), Expression222=astm_gastm_RangeExpression(), Expression228=astm_gastm_ActualParameterExpression(), Expression=astm_gastm_DataDefinition(False, astm_gastm_DataDefinition=Expression(), Definition=astm_gastm_Declaration()), Expression182=astm_gastm_QualifiedIdentifierReference(), Expression146=astm_gastm_LoopStatement(), Expression214=astm_gastm_ConditionalExpression(), Expression57=astm_gastm_EnumLiteralDefinition(), Expression219=astm_gastm_RangeExpression(), Expression194=astm_gastm_CastExpression(), Expression224=astm_gastm_FunctionCallExpression(), Expression85=astm_gastm_Dimension()), '', Expression115=astm_gastm_JumpStatement(), Expression243=astm_gastm_AnnotationExpression(), Expression128=astm_gastm_IfStatement(), Expression88=astm_gastm_Dimension(), Expression144=astm_gastm_ReturnStatement(), Expression142=astm_gastm_CaseBlock(), Expression217=astm_gastm_ConditionalExpression(), Expression168=astm_gastm_ThrowStatement(), Expression211=astm_gastm_ConditionalExpression(), Expression180=astm_gastm_ArrayAccess(), Expression136=astm_gastm_SwitchStatement(), Expression109=astm_gastm_DeleteStatement(), Expression151=astm_gastm_ForStatement(), Expression207=astm_gastm_BinaryExpression(), Expression55=astm_gastm_BitFieldDefinition(), Expression177=astm_gastm_ArrayAccess(), Expression154=astm_gastm_ForStatement(), Expression204=astm_gastm_BinaryExpression(), Expression199=astm_gastm_UnaryExpression(), Expression113=astm_gastm_ExpressionStatement(), Expression222=astm_gastm_RangeExpression(), Expression228=astm_gastm_ActualParameterExpression(), Expression=astm_gastm_DataDefinition(False, astm_gastm_DataDefinition=Expression(), Definition=astm_gastm_Declaration()), Expression182=astm_gastm_QualifiedIdentifierReference(), Expression146=astm_gastm_LoopStatement(), Expression214=astm_gastm_ConditionalExpression(), Expression57=astm_gastm_EnumLiteralDefinition(), Expression219=astm_gastm_RangeExpression(), Expression194=astm_gastm_CastExpression(), Expression224=astm_gastm_FunctionCallExpression(), Expression85=astm_gastm_Dimension()) == None


from python_code import astm_gastm_GASTMSyntaxObject
from python_code import astm_gastm_MacroDefinition

def test_astm_gastm_MacroDefinition___init__():
    assert astm_gastm_MacroDefinition.__init__(astm_gastm_MacroDefinition('', '\x00', PreprocessorElement=astm_gastm_GASTMSyntaxObject()), '\x00\x00', '', PreprocessorElement=astm_gastm_GASTMSyntaxObject()) == None


from python_code import astm_gastm_PrimitiveType

def test_astm_gastm_PrimitiveType___init__():
    assert astm_gastm_PrimitiveType.__init__(astm_gastm_PrimitiveType(True), False) == None


from python_code import astm_gastm_SourceFile

def test_astm_gastm_SourceFile___init__():
    assert astm_gastm_SourceFile.__init__(astm_gastm_SourceFile(''), '') == None


from python_code import SourceFile
from python_code import astm_gastm_SourceLocation

def test_astm_gastm_SourceLocation___init__():
    assert astm_gastm_SourceLocation.__init__(astm_gastm_SourceLocation(0, 0, 0, 0, astm_gastm_SourceLocation=SourceFile()), 0, 0, 0, 0, astm_gastm_SourceLocation=SourceFile()) == None


from python_code import astm_gastm_Type

def test_astm_gastm_Type___init__():
    assert astm_gastm_Type.__init__(astm_gastm_Type(False, False), False, False) == None


from python_code import astm_gastm_VariableDeclaration

def test_astm_gastm_VariableDeclaration___init__():
    assert astm_gastm_VariableDeclaration.__init__(astm_gastm_VariableDeclaration(True), False) == None

