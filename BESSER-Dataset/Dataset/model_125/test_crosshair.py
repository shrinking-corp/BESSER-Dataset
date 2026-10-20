from python_code import astm_Comment
from python_code import astm_GASTMSyntaxObject

def test_astm_Comment___init__():
    assert astm_Comment.__init__(astm_Comment('', PreprocessorElement=astm_GASTMSyntaxObject()), '', PreprocessorElement=astm_GASTMSyntaxObject()) == None


from python_code import Expression
from python_code import astm_DataDefinition
from python_code import astm_Declaration

def test_astm_DataDefinition___init__():
    assert astm_DataDefinition.__init__(astm_DataDefinition(False, astm_DataDefinition=Expression(), Definition=astm_Declaration()), False, astm_DataDefinition=Expression(), Definition=astm_Declaration()) == None


from python_code import astm_FunctionMemberAttributes
from python_code import astm_Virtual

def test_astm_FunctionMemberAttributes___init__():
    assert astm_FunctionMemberAttributes.__init__(astm_FunctionMemberAttributes(False, False, False, astm_FunctionMemberAttributes=astm_Virtual()), False, True, False, astm_FunctionMemberAttributes=astm_Virtual()) == None


from python_code import Expression
from python_code import astm_ActualParameterExpression
from python_code import astm_AnnotationExpression
from python_code import astm_ArrayAccess
from python_code import astm_BinaryExpression
from python_code import astm_BitFieldDefinition
from python_code import astm_CaseBlock
from python_code import astm_CastExpression
from python_code import astm_ConditionalExpression
from python_code import astm_DataDefinition
from python_code import astm_Declaration
from python_code import astm_DeleteStatement
from python_code import astm_Dimension
from python_code import astm_EnumLiteralDefinition
from python_code import astm_ExpressionStatement
from python_code import astm_ForStatement
from python_code import astm_FunctionCallExpression
from python_code import astm_IfStatement
from python_code import astm_JumpStatement
from python_code import astm_Literal
from python_code import astm_LoopStatement
from python_code import astm_QualifiedIdentifierReference
from python_code import astm_RangeExpression
from python_code import astm_ReturnStatement
from python_code import astm_SwitchStatement
from python_code import astm_ThrowStatement
from python_code import astm_UnaryExpression

def test_astm_Literal___init__():
    assert astm_Literal.__init__(astm_Literal('', Expression141=astm_ReturnStatement(), Expression208=astm_ConditionalExpression(), Expression196=astm_UnaryExpression(), Expression211=astm_ConditionalExpression(), Expression225=astm_ActualParameterExpression(), Expression165=astm_ThrowStatement(), Expression133=astm_SwitchStatement(), Expression82=astm_Dimension(), Expression214=astm_ConditionalExpression(), Expression177=astm_ArrayAccess(), Expression112=astm_JumpStatement(), Expression204=astm_BinaryExpression(), Expression191=astm_CastExpression(), Expression240=astm_AnnotationExpression(), Expression143=astm_LoopStatement(), Expression221=astm_FunctionCallExpression(), Expression139=astm_CaseBlock(), Expression110=astm_ExpressionStatement(), Expression54=astm_EnumLiteralDefinition(), Expression174=astm_ArrayAccess(), Expression106=astm_DeleteStatement(), Expression179=astm_QualifiedIdentifierReference(), Expression219=astm_RangeExpression(), Expression=astm_DataDefinition(False, astm_DataDefinition=Expression(), Definition=astm_Declaration()), Expression125=astm_IfStatement(), Expression201=astm_BinaryExpression(), Expression216=astm_RangeExpression(), Expression148=astm_ForStatement(), Expression151=astm_ForStatement(), Expression52=astm_BitFieldDefinition(), Expression85=astm_Dimension()), '', Expression141=astm_ReturnStatement(), Expression208=astm_ConditionalExpression(), Expression196=astm_UnaryExpression(), Expression211=astm_ConditionalExpression(), Expression225=astm_ActualParameterExpression(), Expression165=astm_ThrowStatement(), Expression133=astm_SwitchStatement(), Expression82=astm_Dimension(), Expression214=astm_ConditionalExpression(), Expression177=astm_ArrayAccess(), Expression112=astm_JumpStatement(), Expression204=astm_BinaryExpression(), Expression191=astm_CastExpression(), Expression240=astm_AnnotationExpression(), Expression143=astm_LoopStatement(), Expression221=astm_FunctionCallExpression(), Expression139=astm_CaseBlock(), Expression110=astm_ExpressionStatement(), Expression54=astm_EnumLiteralDefinition(), Expression174=astm_ArrayAccess(), Expression106=astm_DeleteStatement(), Expression179=astm_QualifiedIdentifierReference(), Expression219=astm_RangeExpression(), Expression=astm_DataDefinition(True, astm_DataDefinition=Expression(), Definition=astm_Declaration()), Expression125=astm_IfStatement(), Expression201=astm_BinaryExpression(), Expression216=astm_RangeExpression(), Expression148=astm_ForStatement(), Expression151=astm_ForStatement(), Expression52=astm_BitFieldDefinition(), Expression85=astm_Dimension()) == None


from python_code import astm_GASTMSyntaxObject
from python_code import astm_MacroDefinition

def test_astm_MacroDefinition___init__():
    assert astm_MacroDefinition.__init__(astm_MacroDefinition('', '\x00', PreprocessorElement=astm_GASTMSyntaxObject()), '\x00\x00', '', PreprocessorElement=astm_GASTMSyntaxObject()) == None


from python_code import astm_PrimitiveType

def test_astm_PrimitiveType___init__():
    assert astm_PrimitiveType.__init__(astm_PrimitiveType(True), False) == None


from python_code import astm_SourceFile

def test_astm_SourceFile___init__():
    assert astm_SourceFile.__init__(astm_SourceFile(''), '') == None


from python_code import SourceFile
from python_code import astm_SourceLocation

def test_astm_SourceLocation___init__():
    assert astm_SourceLocation.__init__(astm_SourceLocation(0, 0, 0, 0, astm_SourceLocation=SourceFile()), 0, 0, 0, 0, astm_SourceLocation=SourceFile()) == None


from python_code import astm_Type

def test_astm_Type___init__():
    assert astm_Type.__init__(astm_Type(False, False), False, False) == None


from python_code import astm_VariableDeclaration

def test_astm_VariableDeclaration___init__():
    assert astm_VariableDeclaration.__init__(astm_VariableDeclaration(True), False) == None

