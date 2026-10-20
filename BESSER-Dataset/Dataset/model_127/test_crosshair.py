from python_code import astm_gastm_Comment
from python_code import astm_gastm_GASTMSyntaxObject

def test_astm_gastm_Comment___init__():
    assert astm_gastm_Comment.__init__(astm_gastm_Comment('', PreprocessorElement=astm_gastm_GASTMSyntaxObject()), '', PreprocessorElement=astm_gastm_GASTMSyntaxObject()) == None


from python_code import Expression
from python_code import astm_gastm_DataDefinition
from python_code import astm_gastm_Declaration

def test_astm_gastm_DataDefinition___init__():
    assert astm_gastm_DataDefinition.__init__(astm_gastm_DataDefinition(True, astm_gastm_DataDefinition=Expression(), Definition=astm_gastm_Declaration()), False, astm_gastm_DataDefinition=Expression(), Definition=astm_gastm_Declaration()) == None


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
from python_code import astm_sastm_RDBColumnReference
from python_code import astm_sastm_RDBCursorStatement
from python_code import astm_sastm_RDBHostVariableReference
from python_code import astm_sastm_RDBInsertStatement
from python_code import astm_sastm_RDBModifyStatement
from python_code import astm_sastm_RDBOpenCursorStatement
from python_code import astm_sastm_RDBSelectExpression
from python_code import astm_sastm_RDBUpdateStatement

def test_astm_gastm_Literal___init__():
    assert astm_gastm_Literal.__init__(astm_gastm_Literal('', Expression225=astm_gastm_ActualParameterExpression(), Expression293=astm_sastm_RDBModifyStatement(), Expression299=astm_sastm_RDBOpenCursorStatement(), Expression141=astm_gastm_ReturnStatement(), Expression151=astm_gastm_ForStatement(), Expression219=astm_gastm_RangeExpression(), Expression179=astm_gastm_QualifiedIdentifierReference(), Expression112=astm_gastm_JumpStatement(), Expression54=astm_gastm_EnumLiteralDefinition(), Expression139=astm_gastm_CaseBlock(), Expression295=astm_sastm_RDBUpdateStatement(), Expression=astm_gastm_DataDefinition(False, astm_gastm_DataDefinition=Expression(), Definition=astm_gastm_Declaration()), Expression318=astm_sastm_RDBColumnReference(), Expression297=astm_sastm_RDBCursorStatement(), Expression174=astm_gastm_ArrayAccess(), Expression143=astm_gastm_LoopStatement(), Expression214=astm_gastm_ConditionalExpression(), Expression85=astm_gastm_Dimension(), Expression196=astm_gastm_UnaryExpression(), Expression204=astm_gastm_BinaryExpression(), Expression177=astm_gastm_ArrayAccess(), Expression191=astm_gastm_CastExpression(), Expression216=astm_gastm_RangeExpression(), Expression133=astm_gastm_SwitchStatement(), Expression240=astm_gastm_AnnotationExpression(), Expression110=astm_gastm_ExpressionStatement(), Expression106=astm_gastm_DeleteStatement(), Expression303=astm_sastm_RDBHostVariableReference(), Expression221=astm_gastm_FunctionCallExpression(), Expression52=astm_gastm_BitFieldDefinition(), Expression148=astm_gastm_ForStatement(), Expression288=astm_sastm_RDBInsertStatement(), Expression314=astm_sastm_RDBSelectExpression(), Expression208=astm_gastm_ConditionalExpression(), Expression165=astm_gastm_ThrowStatement(), Expression306=astm_sastm_RDBHostVariableReference(), Expression201=astm_gastm_BinaryExpression(), Expression211=astm_gastm_ConditionalExpression(), Expression125=astm_gastm_IfStatement(), Expression82=astm_gastm_Dimension()), '', Expression225=astm_gastm_ActualParameterExpression(), Expression293=astm_sastm_RDBModifyStatement(), Expression299=astm_sastm_RDBOpenCursorStatement(), Expression141=astm_gastm_ReturnStatement(), Expression151=astm_gastm_ForStatement(), Expression219=astm_gastm_RangeExpression(), Expression179=astm_gastm_QualifiedIdentifierReference(), Expression112=astm_gastm_JumpStatement(), Expression54=astm_gastm_EnumLiteralDefinition(), Expression139=astm_gastm_CaseBlock(), Expression295=astm_sastm_RDBUpdateStatement(), Expression=astm_gastm_DataDefinition(False, astm_gastm_DataDefinition=Expression(), Definition=astm_gastm_Declaration()), Expression318=astm_sastm_RDBColumnReference(), Expression297=astm_sastm_RDBCursorStatement(), Expression174=astm_gastm_ArrayAccess(), Expression143=astm_gastm_LoopStatement(), Expression214=astm_gastm_ConditionalExpression(), Expression85=astm_gastm_Dimension(), Expression196=astm_gastm_UnaryExpression(), Expression204=astm_gastm_BinaryExpression(), Expression177=astm_gastm_ArrayAccess(), Expression191=astm_gastm_CastExpression(), Expression216=astm_gastm_RangeExpression(), Expression133=astm_gastm_SwitchStatement(), Expression240=astm_gastm_AnnotationExpression(), Expression110=astm_gastm_ExpressionStatement(), Expression106=astm_gastm_DeleteStatement(), Expression303=astm_sastm_RDBHostVariableReference(), Expression221=astm_gastm_FunctionCallExpression(), Expression52=astm_gastm_BitFieldDefinition(), Expression148=astm_gastm_ForStatement(), Expression288=astm_sastm_RDBInsertStatement(), Expression314=astm_sastm_RDBSelectExpression(), Expression208=astm_gastm_ConditionalExpression(), Expression165=astm_gastm_ThrowStatement(), Expression306=astm_sastm_RDBHostVariableReference(), Expression201=astm_gastm_BinaryExpression(), Expression211=astm_gastm_ConditionalExpression(), Expression125=astm_gastm_IfStatement(), Expression82=astm_gastm_Dimension()) == None


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


from python_code import astm_sastm_RDBCheckConstraint
from python_code import astm_sastm_RDBTableDefinition

def test_astm_sastm_RDBCheckConstraint___init__():
    assert astm_sastm_RDBCheckConstraint.__init__(astm_sastm_RDBCheckConstraint('', '\x00', RDBConstraint=astm_sastm_RDBTableDefinition()), '\x00\x00', '', RDBConstraint=astm_sastm_RDBTableDefinition()) == None


from python_code import Name
from python_code import RDBColumnType
from python_code import astm_gastm_Declaration
from python_code import astm_sastm_RDBColumnDefinition

def test_astm_sastm_RDBColumnDefinition___init__():
    assert astm_sastm_RDBColumnDefinition.__init__(astm_sastm_RDBColumnDefinition(True, astm_sastm_RDBColumnDefinition=Name(), astm_sastm_RDBColumnDefinition259=RDBColumnType(), Definition=astm_gastm_Declaration()), False, astm_sastm_RDBColumnDefinition=Name(), astm_sastm_RDBColumnDefinition259=RDBColumnType(), Definition=astm_gastm_Declaration()) == None

