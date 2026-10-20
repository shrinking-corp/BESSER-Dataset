from python_code import gastm_Comment
from python_code import gastm_GASTMSyntaxObject

def test_gastm_Comment___init__():
    assert gastm_Comment.__init__(gastm_Comment('', PreprocessorElement=gastm_GASTMSyntaxObject()), '', PreprocessorElement=gastm_GASTMSyntaxObject()) == None


from python_code import Expression
from python_code import gastm_DataDefinition
from python_code import gastm_Declaration

def test_gastm_DataDefinition___init__():
    assert gastm_DataDefinition.__init__(gastm_DataDefinition(True, gastm_DataDefinition=Expression(), Definition=gastm_Declaration()), False, gastm_DataDefinition=Expression(), Definition=gastm_Declaration()) == None


from python_code import gastm_FunctionMemberAttributes
from python_code import gastm_Virtual

def test_gastm_FunctionMemberAttributes___init__():
    assert gastm_FunctionMemberAttributes.__init__(gastm_FunctionMemberAttributes(True, True, True, gastm_FunctionMemberAttributes=gastm_Virtual()), False, True, False, gastm_FunctionMemberAttributes=gastm_Virtual()) == None


from python_code import Expression
from python_code import gastm_ActualParameterExpression
from python_code import gastm_AnnotationExpression
from python_code import gastm_ArrayAccess
from python_code import gastm_BinaryExpression
from python_code import gastm_BitFieldDefinition
from python_code import gastm_CaseBlock
from python_code import gastm_CastExpression
from python_code import gastm_ConditionalExpression
from python_code import gastm_DataDefinition
from python_code import gastm_Declaration
from python_code import gastm_DeleteStatement
from python_code import gastm_Dimension
from python_code import gastm_EnumLiteralDefinition
from python_code import gastm_ExpressionStatement
from python_code import gastm_ForStatement
from python_code import gastm_FunctionCallExpression
from python_code import gastm_IfStatement
from python_code import gastm_JumpStatement
from python_code import gastm_Literal
from python_code import gastm_LoopStatement
from python_code import gastm_QualifiedIdentifierReference
from python_code import gastm_RangeExpression
from python_code import gastm_ReturnStatement
from python_code import gastm_SwitchStatement
from python_code import gastm_ThrowStatement
from python_code import gastm_UnaryExpression
from python_code import sastm_RDBColumnReference
from python_code import sastm_RDBCursorStatement
from python_code import sastm_RDBHostVariableReference
from python_code import sastm_RDBInsertStatement
from python_code import sastm_RDBModifyStatement
from python_code import sastm_RDBOpenCursorStatement
from python_code import sastm_RDBSelectExpression
from python_code import sastm_RDBUpdateStatement

def test_gastm_Literal___init__():
    assert gastm_Literal.__init__(gastm_Literal('', Expression148=gastm_ForStatement(), Expression292=sastm_RDBModifyStatement(), Expression179=gastm_QualifiedIdentifierReference(), Expression240=gastm_AnnotationExpression(), Expression133=gastm_SwitchStatement(), Expression=gastm_DataDefinition(False, gastm_DataDefinition=Expression(), Definition=gastm_Declaration()), Expression151=gastm_ForStatement(), Expression304=sastm_RDBHostVariableReference(), Expression143=gastm_LoopStatement(), Expression141=gastm_ReturnStatement(), Expression219=gastm_RangeExpression(), Expression165=gastm_ThrowStatement(), Expression52=gastm_BitFieldDefinition(), Expression112=gastm_JumpStatement(), Expression177=gastm_ArrayAccess(), Expression298=sastm_RDBOpenCursorStatement(), Expression287=sastm_RDBInsertStatement(), Expression216=gastm_RangeExpression(), Expression316=sastm_RDBColumnReference(), Expression201=gastm_BinaryExpression(), Expression294=sastm_RDBUpdateStatement(), Expression204=gastm_BinaryExpression(), Expression208=gastm_ConditionalExpression(), Expression214=gastm_ConditionalExpression(), Expression191=gastm_CastExpression(), Expression85=gastm_Dimension(), Expression125=gastm_IfStatement(), Expression312=sastm_RDBSelectExpression(), Expression301=sastm_RDBHostVariableReference(), Expression110=gastm_ExpressionStatement(), Expression211=gastm_ConditionalExpression(), Expression82=gastm_Dimension(), Expression54=gastm_EnumLiteralDefinition(), Expression221=gastm_FunctionCallExpression(), Expression196=gastm_UnaryExpression(), Expression225=gastm_ActualParameterExpression(), Expression174=gastm_ArrayAccess(), Expression139=gastm_CaseBlock(), Expression106=gastm_DeleteStatement(), Expression296=sastm_RDBCursorStatement()), '', Expression148=gastm_ForStatement(), Expression292=sastm_RDBModifyStatement(), Expression179=gastm_QualifiedIdentifierReference(), Expression240=gastm_AnnotationExpression(), Expression133=gastm_SwitchStatement(), Expression=gastm_DataDefinition(False, gastm_DataDefinition=Expression(), Definition=gastm_Declaration()), Expression151=gastm_ForStatement(), Expression304=sastm_RDBHostVariableReference(), Expression143=gastm_LoopStatement(), Expression141=gastm_ReturnStatement(), Expression219=gastm_RangeExpression(), Expression165=gastm_ThrowStatement(), Expression52=gastm_BitFieldDefinition(), Expression112=gastm_JumpStatement(), Expression177=gastm_ArrayAccess(), Expression298=sastm_RDBOpenCursorStatement(), Expression287=sastm_RDBInsertStatement(), Expression216=gastm_RangeExpression(), Expression316=sastm_RDBColumnReference(), Expression201=gastm_BinaryExpression(), Expression294=sastm_RDBUpdateStatement(), Expression204=gastm_BinaryExpression(), Expression208=gastm_ConditionalExpression(), Expression214=gastm_ConditionalExpression(), Expression191=gastm_CastExpression(), Expression85=gastm_Dimension(), Expression125=gastm_IfStatement(), Expression312=sastm_RDBSelectExpression(), Expression301=sastm_RDBHostVariableReference(), Expression110=gastm_ExpressionStatement(), Expression211=gastm_ConditionalExpression(), Expression82=gastm_Dimension(), Expression54=gastm_EnumLiteralDefinition(), Expression221=gastm_FunctionCallExpression(), Expression196=gastm_UnaryExpression(), Expression225=gastm_ActualParameterExpression(), Expression174=gastm_ArrayAccess(), Expression139=gastm_CaseBlock(), Expression106=gastm_DeleteStatement(), Expression296=sastm_RDBCursorStatement()) == None


from python_code import gastm_GASTMSyntaxObject
from python_code import gastm_MacroDefinition

def test_gastm_MacroDefinition___init__():
    assert gastm_MacroDefinition.__init__(gastm_MacroDefinition('', '\x00', PreprocessorElement=gastm_GASTMSyntaxObject()), '\x00\x00', '', PreprocessorElement=gastm_GASTMSyntaxObject()) == None


from python_code import gastm_PrimitiveType

def test_gastm_PrimitiveType___init__():
    assert gastm_PrimitiveType.__init__(gastm_PrimitiveType(True), False) == None


from python_code import gastm_SourceFile

def test_gastm_SourceFile___init__():
    assert gastm_SourceFile.__init__(gastm_SourceFile(''), '') == None


from python_code import SourceFile
from python_code import gastm_SourceLocation

def test_gastm_SourceLocation___init__():
    assert gastm_SourceLocation.__init__(gastm_SourceLocation(0, 0, 0, 0, gastm_SourceLocation=SourceFile()), 0, 0, 0, 0, gastm_SourceLocation=SourceFile()) == None


from python_code import gastm_Type

def test_gastm_Type___init__():
    assert gastm_Type.__init__(gastm_Type(False, False), False, False) == None


from python_code import gastm_VariableDeclaration

def test_gastm_VariableDeclaration___init__():
    assert gastm_VariableDeclaration.__init__(gastm_VariableDeclaration(True), False) == None


from python_code import sastm_RDBCheckConstraint

def test_sastm_RDBCheckConstraint___init__():
    assert sastm_RDBCheckConstraint.__init__(sastm_RDBCheckConstraint('', '\x00'), '\x00\x00', '') == None


from python_code import gastm_Declaration
from python_code import sastm_RDBColumnDefinition

def test_sastm_RDBColumnDefinition___init__():
    assert sastm_RDBColumnDefinition.__init__(sastm_RDBColumnDefinition(True, Definition=gastm_Declaration()), False, Definition=gastm_Declaration()) == None

