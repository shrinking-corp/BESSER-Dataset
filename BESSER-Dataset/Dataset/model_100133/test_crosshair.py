from python_code import syntax_AliasResolver

def test_syntax_AliasResolver___init__():
    assert syntax_AliasResolver.__init__(syntax_AliasResolver()) == None

def test_syntax_AliasResolver_resolveQuery():
    assert syntax_AliasResolver.resolveQuery(syntax_AliasResolver(), '', '') == None


from python_code import syntax_BindingParser

def test_syntax_BindingParser___init__():
    assert syntax_BindingParser.__init__(syntax_BindingParser()) == None

def test_syntax_BindingParser_parseBinding():
    assert syntax_BindingParser.parseBinding(syntax_BindingParser(), '') == None


from python_code import syntax_BindingParserRegistry

def test_syntax_BindingParserRegistry___init__():
    assert syntax_BindingParserRegistry.__init__(syntax_BindingParserRegistry()) == None

def test_syntax_BindingParserRegistry_lookup():
    assert syntax_BindingParserRegistry.lookup(syntax_BindingParserRegistry(), '') == None


from python_code import syntax_BindingParseResult
from python_code import syntax_BindingStatement

def test_syntax_BindingStatement___init__():
    assert syntax_BindingStatement.__init__(syntax_BindingStatement(syntax_BindingStatement=syntax_BindingParseResult()), syntax_BindingStatement=syntax_BindingParseResult()) == None

def test_syntax_BindingStatement_getStatementType():
    assert syntax_BindingStatement.getStatementType(syntax_BindingStatement(syntax_BindingStatement=syntax_BindingParseResult())) == None


from python_code import syntax_DefinitionParser

def test_syntax_DefinitionParser___init__():
    assert syntax_DefinitionParser.__init__(syntax_DefinitionParser()) == None

def test_syntax_DefinitionParser_parseDefinition():
    assert syntax_DefinitionParser.parseDefinition(syntax_DefinitionParser(), '') == None


from python_code import syntax_DefinitionParserRegistry

def test_syntax_DefinitionParserRegistry___init__():
    assert syntax_DefinitionParserRegistry.__init__(syntax_DefinitionParserRegistry()) == None

def test_syntax_DefinitionParserRegistry_lookup():
    assert syntax_DefinitionParserRegistry.lookup(syntax_DefinitionParserRegistry(), '') == None


from python_code import syntax_DefinitionParseResult
from python_code import syntax_DefinitionStatement

def test_syntax_DefinitionStatement___init__():
    assert syntax_DefinitionStatement.__init__(syntax_DefinitionStatement(syntax_DefinitionStatement=syntax_DefinitionParseResult()), syntax_DefinitionStatement=syntax_DefinitionParseResult()) == None

def test_syntax_DefinitionStatement_getStatementType():
    assert syntax_DefinitionStatement.getStatementType(syntax_DefinitionStatement(syntax_DefinitionStatement=syntax_DefinitionParseResult())) == None


from python_code import syntax_DefinitionWriter

def test_syntax_DefinitionWriter___init__():
    assert syntax_DefinitionWriter.__init__(syntax_DefinitionWriter()) == None

def test_syntax_DefinitionWriter_hasLogicals():
    assert syntax_DefinitionWriter.hasLogicals(syntax_DefinitionWriter(), '') == None

def test_syntax_DefinitionWriter_renameTable():
    assert syntax_DefinitionWriter.renameTable(syntax_DefinitionWriter(), '', '') == None

def test_syntax_DefinitionWriter_dropTable():
    assert syntax_DefinitionWriter.dropTable(syntax_DefinitionWriter(), '') == None

def test_syntax_DefinitionWriter_createTable():
    assert syntax_DefinitionWriter.createTable(syntax_DefinitionWriter(), '', '', '') == None

def test_syntax_DefinitionWriter_countRecords():
    assert syntax_DefinitionWriter.countRecords(syntax_DefinitionWriter(), '') == None

def test_syntax_DefinitionWriter_createView():
    assert syntax_DefinitionWriter.createView(syntax_DefinitionWriter(), '', '', '') == None

def test_syntax_DefinitionWriter_createSchema():
    assert syntax_DefinitionWriter.createSchema(syntax_DefinitionWriter(), '', '') == None

def test_syntax_DefinitionWriter_insertData():
    assert syntax_DefinitionWriter.insertData(syntax_DefinitionWriter(), '', '') == None

def test_syntax_DefinitionWriter_renameIndex():
    assert syntax_DefinitionWriter.renameIndex(syntax_DefinitionWriter(), '', '') == None

def test_syntax_DefinitionWriter_createIndex():
    assert syntax_DefinitionWriter.createIndex(syntax_DefinitionWriter(), '', '', '') == None

def test_syntax_DefinitionWriter_dropIndex():
    assert syntax_DefinitionWriter.dropIndex(syntax_DefinitionWriter(), '') == None

def test_syntax_DefinitionWriter_selectData():
    assert syntax_DefinitionWriter.selectData(syntax_DefinitionWriter(), '') == None

def test_syntax_DefinitionWriter_copyTableData():
    assert syntax_DefinitionWriter.copyTableData(syntax_DefinitionWriter(), '', '', '') == None

def test_syntax_DefinitionWriter_dropView():
    assert syntax_DefinitionWriter.dropView(syntax_DefinitionWriter(), '') == None

def test_syntax_DefinitionWriter_deleteData():
    assert syntax_DefinitionWriter.deleteData(syntax_DefinitionWriter(), '') == None

def test_syntax_DefinitionWriter_createLabelForFields():
    assert syntax_DefinitionWriter.createLabelForFields(syntax_DefinitionWriter(), '', '', '') == None

def test_syntax_DefinitionWriter_truncateTable():
    assert syntax_DefinitionWriter.truncateTable(syntax_DefinitionWriter(), '') == None

def test_syntax_DefinitionWriter_createLabel():
    assert syntax_DefinitionWriter.createLabel(syntax_DefinitionWriter(), '', '', '') == None

def test_syntax_DefinitionWriter_dropSchema():
    assert syntax_DefinitionWriter.dropSchema(syntax_DefinitionWriter(), '', '') == None


from python_code import syntax_DefinitionWriterRegistry

def test_syntax_DefinitionWriterRegistry___init__():
    assert syntax_DefinitionWriterRegistry.__init__(syntax_DefinitionWriterRegistry()) == None

def test_syntax_DefinitionWriterRegistry_lookup():
    assert syntax_DefinitionWriterRegistry.lookup(syntax_DefinitionWriterRegistry(), '') == None


from python_code import syntax_NameHelper
from python_code import syntax_StatementWriter

def test_syntax_NameHelper___init__():
    assert syntax_NameHelper.__init__(syntax_NameHelper(syntax_NameHelper=syntax_StatementWriter()), syntax_NameHelper=syntax_StatementWriter()) == None

def test_syntax_NameHelper_resolveContainers():
    assert syntax_NameHelper.resolveContainers(syntax_NameHelper(syntax_NameHelper=syntax_StatementWriter()), '') == None


from python_code import syntax_NameHelperRegistry

def test_syntax_NameHelperRegistry___init__():
    assert syntax_NameHelperRegistry.__init__(syntax_NameHelperRegistry()) == None

def test_syntax_NameHelperRegistry_lookup():
    assert syntax_NameHelperRegistry.lookup(syntax_NameHelperRegistry(), '') == None


from python_code import syntax_QueryParser

def test_syntax_QueryParser___init__():
    assert syntax_QueryParser.__init__(syntax_QueryParser()) == None

def test_syntax_QueryParser_parseQuery():
    assert syntax_QueryParser.parseQuery(syntax_QueryParser(), '') == None


from python_code import syntax_QueryParserRegistry

def test_syntax_QueryParserRegistry___init__():
    assert syntax_QueryParserRegistry.__init__(syntax_QueryParserRegistry()) == None

def test_syntax_QueryParserRegistry_lookup():
    assert syntax_QueryParserRegistry.lookup(syntax_QueryParserRegistry(), '') == None


from python_code import syntax_QueryWriter

def test_syntax_QueryWriter___init__():
    assert syntax_QueryWriter.__init__(syntax_QueryWriter()) == None

def test_syntax_QueryWriter_writeQuery():
    assert syntax_QueryWriter.writeQuery(syntax_QueryWriter(), '') == None


from python_code import syntax_QueryWriterRegistry

def test_syntax_QueryWriterRegistry___init__():
    assert syntax_QueryWriterRegistry.__init__(syntax_QueryWriterRegistry()) == None

def test_syntax_QueryWriterRegistry_lookup():
    assert syntax_QueryWriterRegistry.lookup(syntax_QueryWriterRegistry(), '') == None


from python_code import syntax_dbl_AllocateDescriptorStatement

def test_syntax_dbl_AllocateDescriptorStatement___init__():
    assert syntax_dbl_AllocateDescriptorStatement.__init__(syntax_dbl_AllocateDescriptorStatement('', '', '\x00\x00'), '', '', '') == None


from python_code import syntax_dbl_CloseStatement

def test_syntax_dbl_CloseStatement___init__():
    assert syntax_dbl_CloseStatement.__init__(syntax_dbl_CloseStatement(''), '') == None


from python_code import syntax_dbl_ConditionInfoClause

def test_syntax_dbl_ConditionInfoClause___init__():
    assert syntax_dbl_ConditionInfoClause.__init__(syntax_dbl_ConditionInfoClause('', syntax_dbl_ConditionInfoClause=set()), '', syntax_dbl_ConditionInfoClause=set()) == None


from python_code import syntax_dbl_DeallocateDescriptorStatement

def test_syntax_dbl_DeallocateDescriptorStatement___init__():
    assert syntax_dbl_DeallocateDescriptorStatement.__init__(syntax_dbl_DeallocateDescriptorStatement('', '\x00'), '\x00\x00', '') == None


from python_code import syntax_dbl_DeclareCursorStatement

def test_syntax_dbl_DeclareCursorStatement___init__():
    assert syntax_dbl_DeclareCursorStatement.__init__(syntax_dbl_DeclareCursorStatement('', '', '', '', False), '', '', '', '', False) == None


from python_code import IntoClause
from python_code import syntax_dbl_DescribeStatement

def test_syntax_dbl_DescribeStatement___init__():
    assert syntax_dbl_DescribeStatement.__init__(syntax_dbl_DescribeStatement('', syntax_dbl_DescribeStatement=IntoClause()), '', syntax_dbl_DescribeStatement=IntoClause()) == None


from python_code import syntax_dbl_ExecuteImmediateStatement

def test_syntax_dbl_ExecuteImmediateStatement___init__():
    assert syntax_dbl_ExecuteImmediateStatement.__init__(syntax_dbl_ExecuteImmediateStatement(''), '') == None


from python_code import syntax_dbl_ExecuteStatement

def test_syntax_dbl_ExecuteStatement___init__():
    assert syntax_dbl_ExecuteStatement.__init__(syntax_dbl_ExecuteStatement(''), '') == None


from python_code import MultipleRowFetchClause
from python_code import SingleRowFetchClause
from python_code import syntax_dbl_FetchStatement

def test_syntax_dbl_FetchStatement___init__():
    assert syntax_dbl_FetchStatement.__init__(syntax_dbl_FetchStatement('', '', '\x00\x00', syntax_dbl_FetchStatement=MultipleRowFetchClause(), syntax_dbl_FetchStatement36=SingleRowFetchClause()), '', '', '', syntax_dbl_FetchStatement=MultipleRowFetchClause(), syntax_dbl_FetchStatement36=SingleRowFetchClause()) == None


from python_code import syntax_dbl_GetDescriptorStatement

def test_syntax_dbl_GetDescriptorStatement___init__():
    assert syntax_dbl_GetDescriptorStatement.__init__(syntax_dbl_GetDescriptorStatement('', '', '', syntax_dbl_GetDescriptorStatement=set()), '', '', '', syntax_dbl_GetDescriptorStatement=set()) == None


from python_code import syntax_dbl_IntoClause

def test_syntax_dbl_IntoClause___init__():
    assert syntax_dbl_IntoClause.__init__(syntax_dbl_IntoClause('', '\x00'), '\x00\x00', '') == None


from python_code import syntax_dbl_MultipleRowFetchClause

def test_syntax_dbl_MultipleRowFetchClause___init__():
    assert syntax_dbl_MultipleRowFetchClause.__init__(syntax_dbl_MultipleRowFetchClause('\x00\x00', '', False, ''), '', '', False, '') == None


from python_code import syntax_dbl_OpenStatement

def test_syntax_dbl_OpenStatement___init__():
    assert syntax_dbl_OpenStatement.__init__(syntax_dbl_OpenStatement('', '', '\x00\x00'), '', '', '') == None


from python_code import syntax_dbl_Option

def test_syntax_dbl_Option___init__():
    assert syntax_dbl_Option.__init__(syntax_dbl_Option('', '\x00'), '\x00\x00', '') == None


from python_code import IntoClause
from python_code import syntax_dbl_PrepareStatement

def test_syntax_dbl_PrepareStatement___init__():
    assert syntax_dbl_PrepareStatement.__init__(syntax_dbl_PrepareStatement('', '\x00', syntax_dbl_PrepareStatement=IntoClause()), '\x00\x00', '', syntax_dbl_PrepareStatement=IntoClause()) == None


from python_code import syntax_dbl_SetDescriptorStatement

def test_syntax_dbl_SetDescriptorStatement___init__():
    assert syntax_dbl_SetDescriptorStatement.__init__(syntax_dbl_SetDescriptorStatement('\x00\x00', '', syntax_dbl_SetDescriptorStatement=set()), '', '', syntax_dbl_SetDescriptorStatement=set()) == None


from python_code import syntax_dbl_SetTransactionStatement

def test_syntax_dbl_SetTransactionStatement___init__():
    assert syntax_dbl_SetTransactionStatement.__init__(syntax_dbl_SetTransactionStatement('', '\x00'), '\x00\x00', '') == None


from python_code import syntax_dbl_SingleRowFetchClause

def test_syntax_dbl_SingleRowFetchClause___init__():
    assert syntax_dbl_SingleRowFetchClause.__init__(syntax_dbl_SingleRowFetchClause('', False), '', False) == None


from python_code import ddl_syntax_QualifiedName
from python_code import syntax_ddl_CallStatement

def test_syntax_ddl_CallStatement___init__():
    assert syntax_ddl_CallStatement.__init__(syntax_ddl_CallStatement('', syntax_ddl_CallStatement=ddl_syntax_QualifiedName()), '', syntax_ddl_CallStatement=ddl_syntax_QualifiedName()) == None


from python_code import syntax_ddl_CommitStatement

def test_syntax_ddl_CommitStatement___init__():
    assert syntax_ddl_CommitStatement.__init__(syntax_ddl_CommitStatement(True), False) == None


from python_code import syntax_ddl_ConnectStatement

def test_syntax_ddl_ConnectStatement___init__():
    assert syntax_ddl_ConnectStatement.__init__(syntax_ddl_ConnectStatement('\x00\x00', False, '', ''), '', False, '', '') == None


from python_code import ddl_syntax_IndexDef
from python_code import ddl_syntax_QualifiedName
from python_code import syntax_ddl_CreateIndexStatement

def test_syntax_ddl_CreateIndexStatement___init__():
    assert syntax_ddl_CreateIndexStatement.__init__(syntax_ddl_CreateIndexStatement(True, syntax_ddl_CreateIndexStatement=ddl_syntax_QualifiedName(), syntax_ddl_CreateIndexStatement16=ddl_syntax_QualifiedName(), syntax_ddl_CreateIndexStatement19=ddl_syntax_IndexDef()), False, syntax_ddl_CreateIndexStatement=ddl_syntax_QualifiedName(), syntax_ddl_CreateIndexStatement16=ddl_syntax_QualifiedName(), syntax_ddl_CreateIndexStatement19=ddl_syntax_IndexDef()) == None


from python_code import ddl_syntax_QualifiedName
from python_code import syntax_ddl_CreateViewStatement

def test_syntax_ddl_CreateViewStatement___init__():
    assert syntax_ddl_CreateViewStatement.__init__(syntax_ddl_CreateViewStatement('', '\x00', syntax_ddl_CreateViewStatement=ddl_syntax_QualifiedName()), '\x00\x00', '', syntax_ddl_CreateViewStatement=ddl_syntax_QualifiedName()) == None


from python_code import syntax_ddl_DisconnectStatement

def test_syntax_ddl_DisconnectStatement___init__():
    assert syntax_ddl_DisconnectStatement.__init__(syntax_ddl_DisconnectStatement(''), '') == None


from python_code import ddl_syntax_QualifiedName
from python_code import syntax_ddl_DropStatement

def test_syntax_ddl_DropStatement___init__():
    assert syntax_ddl_DropStatement.__init__(syntax_ddl_DropStatement('', '\x00', syntax_ddl_DropStatement=ddl_syntax_QualifiedName()), '\x00\x00', '', syntax_ddl_DropStatement=ddl_syntax_QualifiedName()) == None


from python_code import ddl_syntax_QualifiedName
from python_code import syntax_ddl_LockTableStatement

def test_syntax_ddl_LockTableStatement___init__():
    assert syntax_ddl_LockTableStatement.__init__(syntax_ddl_LockTableStatement(False, '\x00', syntax_ddl_LockTableStatement=ddl_syntax_QualifiedName()), False, '\x00', syntax_ddl_LockTableStatement=ddl_syntax_QualifiedName()) == None


from python_code import syntax_ddl_ReleaseStatement

def test_syntax_ddl_ReleaseStatement___init__():
    assert syntax_ddl_ReleaseStatement.__init__(syntax_ddl_ReleaseStatement(''), '') == None


from python_code import ddl_syntax_QualifiedName
from python_code import syntax_ddl_RenameStatement

def test_syntax_ddl_RenameStatement___init__():
    assert syntax_ddl_RenameStatement.__init__(syntax_ddl_RenameStatement('', '', '\x00\x00', syntax_ddl_RenameStatement=ddl_syntax_QualifiedName()), '', '', '', syntax_ddl_RenameStatement=ddl_syntax_QualifiedName()) == None


from python_code import syntax_ddl_RollbackStatement

def test_syntax_ddl_RollbackStatement___init__():
    assert syntax_ddl_RollbackStatement.__init__(syntax_ddl_RollbackStatement(True), False) == None


from python_code import syntax_ddl_SetConnectionStatement

def test_syntax_ddl_SetConnectionStatement___init__():
    assert syntax_ddl_SetConnectionStatement.__init__(syntax_ddl_SetConnectionStatement(''), '') == None


from python_code import syntax_dml_ExtendedQueryExpressionBody

def test_syntax_dml_ExtendedQueryExpressionBody___init__():
    assert syntax_dml_ExtendedQueryExpressionBody.__init__(syntax_dml_ExtendedQueryExpressionBody(0), 0) == None

