from python_code import ast_AdditiveExpression
from python_code import ast_Expression

def test_ast_AdditiveExpression___init__():
    assert ast_AdditiveExpression.__init__(ast_AdditiveExpression('', ast_AdditiveExpression=ast_Expression(), ast_AdditiveExpression153=ast_Expression()), '', ast_AdditiveExpression=ast_Expression(), ast_AdditiveExpression153=ast_Expression()) == None


from python_code import ast_AdditiveStepExpression
from python_code import ast_StepExpression

def test_ast_AdditiveStepExpression___init__():
    assert ast_AdditiveStepExpression.__init__(ast_AdditiveStepExpression('', ast_AdditiveStepExpression=ast_StepExpression(), ast_AdditiveStepExpression180=ast_StepExpression()), '', ast_AdditiveStepExpression=ast_StepExpression(), ast_AdditiveStepExpression180=ast_StepExpression()) == None


from python_code import ast_ArrayConstructionIterationClause
from python_code import ast_ArrayConstructionOperator
from python_code import ast_Expression

def test_ast_ArrayConstructionIterationClause___init__():
    assert ast_ArrayConstructionIterationClause.__init__(ast_ArrayConstructionIterationClause('', ast_ArrayConstructionIterationClause=ast_ArrayConstructionOperator(), ast_ArrayConstructionIterationClause109=ast_Expression()), '', ast_ArrayConstructionIterationClause=ast_ArrayConstructionOperator(), ast_ArrayConstructionIterationClause109=ast_Expression()) == None


from python_code import ast_ArrayElementAccess
from python_code import ast_ArraySubscript
from python_code import ast_Expression

def test_ast_ArraySubscript___init__():
    assert ast_ArraySubscript.__init__(ast_ArraySubscript(True, ast_ArraySubscript=ast_ArrayElementAccess(), ast_ArraySubscript86=ast_Expression()), False, ast_ArraySubscript=ast_ArrayElementAccess(), ast_ArraySubscript86=ast_Expression()) == None


from python_code import ast_CallableElement
from python_code import ast_DerivativeOperator
from python_code import ast_FeatureCall
from python_code import ast_ForStatement
from python_code import ast_MemberVariableAccess

def test_ast_CallableElement___init__():
    assert ast_CallableElement.__init__(ast_CallableElement(ast_CallableElement=ast_DerivativeOperator(), ast_CallableElement170=ast_FeatureCall(), ast_CallableElement223=ast_ForStatement(), ast_CallableElement190=ast_MemberVariableAccess()), ast_CallableElement=ast_DerivativeOperator(), ast_CallableElement170=ast_FeatureCall(), ast_CallableElement223=ast_ForStatement(), ast_CallableElement190=ast_MemberVariableAccess()) == None

def test_ast_CallableElement_getQualifiedName():
    assert ast_CallableElement.getQualifiedName(ast_CallableElement(ast_CallableElement=ast_DerivativeOperator(), ast_CallableElement170=ast_FeatureCall(), ast_CallableElement223=ast_ForStatement(), ast_CallableElement190=ast_MemberVariableAccess())) == None

def test_ast_CallableElement_getName():
    assert ast_CallableElement.getName(ast_CallableElement(ast_CallableElement=ast_DerivativeOperator(), ast_CallableElement170=ast_FeatureCall(), ast_CallableElement223=ast_ForStatement(), ast_CallableElement190=ast_MemberVariableAccess())) == None


from python_code import ast_Definition
from python_code import ast_Module

def test_ast_Definition___init__():
    assert ast_Definition.__init__(ast_Definition('', ast_Definition=ast_Module()), '', ast_Definition=ast_Module()) == None


from python_code import ast_EnumerationDefinition
from python_code import ast_EnumerationLiteralDeclaration

def test_ast_EnumerationLiteralDeclaration___init__():
    assert ast_EnumerationLiteralDeclaration.__init__(ast_EnumerationLiteralDeclaration('', ast_EnumerationLiteralDeclaration=ast_EnumerationDefinition()), '', ast_EnumerationLiteralDeclaration=ast_EnumerationDefinition()) == None


from python_code import ast_EqualityExpression
from python_code import ast_Expression

def test_ast_EqualityExpression___init__():
    assert ast_EqualityExpression.__init__(ast_EqualityExpression('', ast_EqualityExpression=ast_Expression(), ast_EqualityExpression138=ast_Expression()), '', ast_EqualityExpression=ast_Expression(), ast_EqualityExpression138=ast_Expression()) == None


from python_code import ast_Expression
from python_code import ast_IfExpression

def test_ast_IfExpression___init__():
    assert ast_IfExpression.__init__(ast_IfExpression(True, ast_IfExpression=ast_Expression(), ast_IfExpression63=ast_Expression(), ast_IfExpression66=ast_Expression()), False, ast_IfExpression=ast_Expression(), ast_IfExpression63=ast_Expression(), ast_IfExpression66=ast_Expression()) == None


from python_code import ast_LetExpressionVariableDeclaration
from python_code import ast_LetExpressionVariableDeclarationPart

def test_ast_LetExpressionVariableDeclarationPart___init__():
    assert ast_LetExpressionVariableDeclarationPart.__init__(ast_LetExpressionVariableDeclarationPart('', ast_LetExpressionVariableDeclarationPart=ast_LetExpressionVariableDeclaration()), '', ast_LetExpressionVariableDeclarationPart=ast_LetExpressionVariableDeclaration()) == None


from python_code import ast_Expression
from python_code import ast_MultiplicativeExpression

def test_ast_MultiplicativeExpression___init__():
    assert ast_MultiplicativeExpression.__init__(ast_MultiplicativeExpression('', ast_MultiplicativeExpression=ast_Expression(), ast_MultiplicativeExpression158=ast_Expression()), '', ast_MultiplicativeExpression=ast_Expression(), ast_MultiplicativeExpression158=ast_Expression()) == None


from python_code import ast_ParameterDeclaration

def test_ast_ParameterDeclaration___init__():
    assert ast_ParameterDeclaration.__init__(ast_ParameterDeclaration(''), '') == None


from python_code import ast_Expression
from python_code import ast_PostfixExpression

def test_ast_PostfixExpression___init__():
    assert ast_PostfixExpression.__init__(ast_PostfixExpression('', ast_PostfixExpression=ast_Expression()), '', ast_PostfixExpression=ast_Expression()) == None


from python_code import ast_Expression
from python_code import ast_PowerExpression

def test_ast_PowerExpression___init__():
    assert ast_PowerExpression.__init__(ast_PowerExpression('', ast_PowerExpression=ast_Expression(), ast_PowerExpression163=ast_Expression()), '', ast_PowerExpression=ast_Expression(), ast_PowerExpression163=ast_Expression()) == None


from python_code import ast_DataTypeSpecifier
from python_code import ast_RecordDefinition
from python_code import ast_RecordFieldDeclaration

def test_ast_RecordFieldDeclaration___init__():
    assert ast_RecordFieldDeclaration.__init__(ast_RecordFieldDeclaration('', ast_RecordFieldDeclaration5=ast_DataTypeSpecifier(), ast_RecordFieldDeclaration=ast_RecordDefinition()), '', ast_RecordFieldDeclaration5=ast_DataTypeSpecifier(), ast_RecordFieldDeclaration=ast_RecordDefinition()) == None


from python_code import ast_Expression
from python_code import ast_RelationalExpression

def test_ast_RelationalExpression___init__():
    assert ast_RelationalExpression.__init__(ast_RelationalExpression('', ast_RelationalExpression143=ast_Expression(), ast_RelationalExpression=ast_Expression()), '', ast_RelationalExpression143=ast_Expression(), ast_RelationalExpression=ast_Expression()) == None


from python_code import ast_StepLiteral

def test_ast_StepLiteral___init__():
    assert ast_StepLiteral.__init__(ast_StepLiteral(0), 0) == None


from python_code import ast_Expression
from python_code import ast_SwitchExpression

def test_ast_SwitchExpression___init__():
    assert ast_SwitchExpression.__init__(ast_SwitchExpression(False, ast_SwitchExpression=ast_Expression(), ast_SwitchExpression71=set(), ast_SwitchExpression73=ast_Expression()), False, ast_SwitchExpression=ast_Expression(), ast_SwitchExpression71=set(), ast_SwitchExpression73=ast_Expression()) == None


from python_code import ast_Expression
from python_code import ast_UnaryExpression

def test_ast_UnaryExpression___init__():
    assert ast_UnaryExpression.__init__(ast_UnaryExpression('', ast_UnaryExpression=ast_Expression()), '', ast_UnaryExpression=ast_Expression()) == None


from python_code import ast_StepExpression
from python_code import ast_VariableAccess

def test_ast_VariableAccess___init__():
    assert ast_VariableAccess.__init__(ast_VariableAccess(ast_VariableAccess=ast_StepExpression()), ast_VariableAccess=ast_StepExpression()) == None

def test_ast_VariableAccess_isInitial():
    assert ast_VariableAccess.isInitial(ast_VariableAccess(ast_VariableAccess=ast_StepExpression())) == None


from python_code import ast_Expression
from python_code import ast_VariableDeclaration

def test_ast_VariableDeclaration___init__():
    assert ast_VariableDeclaration.__init__(ast_VariableDeclaration('', ast_VariableDeclaration=ast_Expression()), '', ast_VariableDeclaration=ast_Expression()) == None

