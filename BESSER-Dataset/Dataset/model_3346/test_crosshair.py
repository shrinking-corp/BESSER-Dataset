from python_code import MOFScriptModel_CreateStatement

def test_MOFScriptModel_CreateStatement___init__():
    assert MOFScriptModel_CreateStatement.__init__(MOFScriptModel_CreateStatement('', '\x00'), '\x00\x00', '') == None


from python_code import MOFScriptModel_DebugStatement

def test_MOFScriptModel_DebugStatement___init__():
    assert MOFScriptModel_DebugStatement.__init__(MOFScriptModel_DebugStatement('', '\x00'), '\x00\x00', '') == None


from python_code import MOFScriptModel_Expression
from python_code import MOFScriptModel_GeneralAssignment

def test_MOFScriptModel_GeneralAssignment___init__():
    assert MOFScriptModel_GeneralAssignment.__init__(MOFScriptModel_GeneralAssignment('', '\x00', MOFScriptModel_GeneralAssignment=MOFScriptModel_Expression()), '\x00\x00', '', MOFScriptModel_GeneralAssignment=MOFScriptModel_Expression()) == None


from python_code import MOFScriptModel_Literal

def test_MOFScriptModel_Literal___init__():
    assert MOFScriptModel_Literal.__init__(MOFScriptModel_Literal('', '\x00'), '\x00\x00', '') == None


from python_code import MOFScriptModel_Expression
from python_code import MOFScriptModel_LogicalExpression

def test_MOFScriptModel_LogicalExpression___init__():
    assert MOFScriptModel_LogicalExpression.__init__(MOFScriptModel_LogicalExpression('', MOFScriptModel_LogicalExpression=MOFScriptModel_Expression(), MOFScriptModel_LogicalExpression46=MOFScriptModel_Expression()), '', MOFScriptModel_LogicalExpression=MOFScriptModel_Expression(), MOFScriptModel_LogicalExpression46=MOFScriptModel_Expression()) == None


from python_code import MOFScriptModel_MOFScriptImport
from python_code import MOFScriptModel_MOFScriptSpecification

def test_MOFScriptModel_MOFScriptImport___init__():
    assert MOFScriptModel_MOFScriptImport.__init__(MOFScriptModel_MOFScriptImport('\x00\x00', '', '', '', MOFScriptModel_MOFScriptImport=MOFScriptModel_MOFScriptSpecification()), '', '', '', '', MOFScriptModel_MOFScriptImport=MOFScriptModel_MOFScriptSpecification()) == None


from python_code import MOFScriptModel_MOFScriptObject

def test_MOFScriptModel_MOFScriptObject___init__():
    assert MOFScriptModel_MOFScriptObject.__init__(MOFScriptModel_MOFScriptObject(0, 0, MOFScriptModel_MOFScriptObject=set()), 0, 0, MOFScriptModel_MOFScriptObject=set()) == None


from python_code import MOFScriptModel_Expression
from python_code import MOFScriptModel_ResultAssignment

def test_MOFScriptModel_ResultAssignment___init__():
    assert MOFScriptModel_ResultAssignment.__init__(MOFScriptModel_ResultAssignment('', '\x00', MOFScriptModel_ResultAssignment=MOFScriptModel_Expression()), '\x00\x00', '', MOFScriptModel_ResultAssignment=MOFScriptModel_Expression()) == None


from python_code import MOFScriptModel_MOFScriptStatementOwner
from python_code import MOFScriptModel_StatementBlock

def test_MOFScriptModel_StatementBlock___init__():
    assert MOFScriptModel_StatementBlock.__init__(MOFScriptModel_StatementBlock(False, '', '', MOFScriptModel_StatementBlock17=set(), MOFScriptModel_StatementBlock=MOFScriptModel_MOFScriptStatementOwner()), False, '', '', MOFScriptModel_StatementBlock17=set(), MOFScriptModel_StatementBlock=MOFScriptModel_MOFScriptStatementOwner()) == None

