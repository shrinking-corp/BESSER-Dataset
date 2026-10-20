from python_code import plSql_BooleanLiteralExpression

def test_plSql_BooleanLiteralExpression___init__():
    assert plSql_BooleanLiteralExpression.__init__(plSql_BooleanLiteralExpression(''), '') == None


from python_code import plSql_CaseStatement
from python_code import plSql_CaseStatementElseBranch
from python_code import plSql_Expression

def test_plSql_CaseStatement___init__():
    assert plSql_CaseStatement.__init__(plSql_CaseStatement('', plSql_CaseStatement=plSql_Expression(), plSql_CaseStatement62=set(), plSql_CaseStatement64=plSql_CaseStatementElseBranch()), '', plSql_CaseStatement=plSql_Expression(), plSql_CaseStatement62=set(), plSql_CaseStatement64=plSql_CaseStatementElseBranch()) == None


from python_code import plSql_ContinueStatement
from python_code import plSql_Expression

def test_plSql_ContinueStatement___init__():
    assert plSql_ContinueStatement.__init__(plSql_ContinueStatement('', plSql_ContinueStatement=plSql_Expression()), '', plSql_ContinueStatement=plSql_Expression()) == None


from python_code import plSql_ExitStatement
from python_code import plSql_Expression

def test_plSql_ExitStatement___init__():
    assert plSql_ExitStatement.__init__(plSql_ExitStatement('', plSql_ExitStatement=plSql_Expression()), '', plSql_ExitStatement=plSql_Expression()) == None


from python_code import plSql_Function
from python_code import plSql_FunctionContent
from python_code import plSql_ParameterSequence

def test_plSql_Function___init__():
    assert plSql_Function.__init__(plSql_Function('\x00\x00', '', plSql_Function18=set(), plSql_Function20=plSql_FunctionContent(), plSql_Function=plSql_ParameterSequence()), '', '', plSql_Function18=set(), plSql_Function20=plSql_FunctionContent(), plSql_Function=plSql_ParameterSequence()) == None


from python_code import plSql_FunctionInvokerRightsClause

def test_plSql_FunctionInvokerRightsClause___init__():
    assert plSql_FunctionInvokerRightsClause.__init__(plSql_FunctionInvokerRightsClause(''), '') == None


from python_code import plSql_IntLiteralExpression

def test_plSql_IntLiteralExpression___init__():
    assert plSql_IntLiteralExpression.__init__(plSql_IntLiteralExpression(0), 0) == None


from python_code import plSql_GotoStatement
from python_code import plSql_Label
from python_code import plSql_Statement

def test_plSql_Label___init__():
    assert plSql_Label.__init__(plSql_Label('', plSql_Label=plSql_Statement(), plSql_Label90=plSql_GotoStatement()), '', plSql_Label=plSql_Statement(), plSql_Label90=plSql_GotoStatement()) == None


from python_code import plSql_LoopStatement

def test_plSql_LoopStatement___init__():
    assert plSql_LoopStatement.__init__(plSql_LoopStatement('', plSql_LoopStatement=set()), '', plSql_LoopStatement=set()) == None


from python_code import plSql_Name
from python_code import plSql_NameDeclaration

def test_plSql_NameDeclaration___init__():
    assert plSql_NameDeclaration.__init__(plSql_NameDeclaration('', plSql_NameDeclaration=plSql_Name()), '', plSql_NameDeclaration=plSql_Name()) == None


from python_code import plSql_ParameterDeclaration
from python_code import plSql_ParameterSequence
from python_code import plSql_ParameterValue

def test_plSql_ParameterDeclaration___init__():
    assert plSql_ParameterDeclaration.__init__(plSql_ParameterDeclaration('', '\x00', plSql_ParameterDeclaration24=plSql_ParameterValue(), plSql_ParameterDeclaration=plSql_ParameterSequence()), '\x00\x00', '', plSql_ParameterDeclaration24=plSql_ParameterValue(), plSql_ParameterDeclaration=plSql_ParameterSequence()) == None


from python_code import plSql_PragmaRestrictReferences

def test_plSql_PragmaRestrictReferences___init__():
    assert plSql_PragmaRestrictReferences.__init__(plSql_PragmaRestrictReferences(''), '') == None


from python_code import plSql_PragmaTimestamp

def test_plSql_PragmaTimestamp___init__():
    assert plSql_PragmaTimestamp.__init__(plSql_PragmaTimestamp(''), '') == None


from python_code import plSql_ParameterSequence
from python_code import plSql_ProcedureDeclaration

def test_plSql_ProcedureDeclaration___init__():
    assert plSql_ProcedureDeclaration.__init__(plSql_ProcedureDeclaration('', plSql_ProcedureDeclaration=plSql_ParameterSequence()), '', plSql_ProcedureDeclaration=plSql_ParameterSequence()) == None


from python_code import plSql_RaiseStatement

def test_plSql_RaiseStatement___init__():
    assert plSql_RaiseStatement.__init__(plSql_RaiseStatement(''), '') == None


from python_code import plSql_ResultCacheClause

def test_plSql_ResultCacheClause___init__():
    assert plSql_ResultCacheClause.__init__(plSql_ResultCacheClause(''), '') == None


from python_code import plSql_BlockStatement
from python_code import plSql_FunctionImplementation
from python_code import plSql_ProcedureImplementation
from python_code import plSql_StatementBody

def test_plSql_StatementBody___init__():
    assert plSql_StatementBody.__init__(plSql_StatementBody('', plSql_StatementBody=plSql_ProcedureImplementation(), plSql_StatementBody35=plSql_FunctionImplementation(), plSql_StatementBody37=set(), plSql_StatementBody58=plSql_BlockStatement()), '', plSql_StatementBody=plSql_ProcedureImplementation(), plSql_StatementBody35=plSql_FunctionImplementation(), plSql_StatementBody37=set(), plSql_StatementBody58=plSql_BlockStatement()) == None


from python_code import plSql_StringLiteralExpression

def test_plSql_StringLiteralExpression___init__():
    assert plSql_StringLiteralExpression.__init__(plSql_StringLiteralExpression(''), '') == None


from python_code import plSql_VariableDeclaration
from python_code import plSql_VariableValue

def test_plSql_VariableDeclaration___init__():
    assert plSql_VariableDeclaration.__init__(plSql_VariableDeclaration(False, '', False, plSql_VariableDeclaration=plSql_VariableValue()), False, '', False, plSql_VariableDeclaration=plSql_VariableValue()) == None


from python_code import plSql_CloseStatement
from python_code import plSql_FetchStatement
from python_code import plSql_FetchStatementIntoClause
from python_code import plSql_QualifiedName
from python_code import plSql_VariableAssignmentTarget
from python_code import plSql_VariableRef
from python_code import plSql_VariableRefExpression

def test_plSql_VariableRef___init__():
    assert plSql_VariableRef.__init__(plSql_VariableRef(True, plSql_VariableRef=plSql_VariableRefExpression(), plSql_VariableRef53=plSql_VariableAssignmentTarget(), plSql_VariableRef75=plSql_CloseStatement(), plSql_VariableRef81=plSql_FetchStatement(), plSql_VariableRef86=plSql_FetchStatementIntoClause(), plSql_VariableRef123=plSql_QualifiedName()), False, plSql_VariableRef=plSql_VariableRefExpression(), plSql_VariableRef53=plSql_VariableAssignmentTarget(), plSql_VariableRef75=plSql_CloseStatement(), plSql_VariableRef81=plSql_FetchStatement(), plSql_VariableRef86=plSql_FetchStatementIntoClause(), plSql_VariableRef123=plSql_QualifiedName()) == None

