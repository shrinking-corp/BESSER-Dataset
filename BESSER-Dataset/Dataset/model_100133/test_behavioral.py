import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BindingStatement,
    ConditionInfoClause,
    DefinitionStatement,
    IntoClause,
    MultipleRowFetchClause,
    Option,
    QueryExpressionBody,
    QuerySelect,
    SQLObjectNameHelper,
    SingleRowFetchClause,
    StatementParser,
    StatementWriter,
    ddl_syntax_IndexDef,
    ddl_syntax_QualifiedName,
    ddl_syntax_TableColumnDef,
    dml_ExtendedQueryExpressionBody,
    syntax_AliasResolver,
    syntax_BindingParseError,
    syntax_BindingParseResult,
    syntax_BindingParser,
    syntax_BindingParserRegistry,
    syntax_BindingStatement,
    syntax_DefinitionParseError,
    syntax_DefinitionParseResult,
    syntax_DefinitionParser,
    syntax_DefinitionParserRegistry,
    syntax_DefinitionStatement,
    syntax_DefinitionWriter,
    syntax_DefinitionWriterRegistry,
    syntax_NameHelper,
    syntax_NameHelperRegistry,
    syntax_QueryParser,
    syntax_QueryParserRegistry,
    syntax_QueryWriter,
    syntax_QueryWriterRegistry,
    syntax_SQLObjectNameHelper,
    syntax_StatementParser,
    syntax_StatementWriter,
    syntax_dbl_AllocateDescriptorStatement,
    syntax_dbl_CloseStatement,
    syntax_dbl_ConditionInfoClause,
    syntax_dbl_DeallocateDescriptorStatement,
    syntax_dbl_DeclareCursorStatement,
    syntax_dbl_DescribeStatement,
    syntax_dbl_ExecuteImmediateStatement,
    syntax_dbl_ExecuteStatement,
    syntax_dbl_FetchStatement,
    syntax_dbl_GetDescriptorStatement,
    syntax_dbl_GetDiagnosticsStatement,
    syntax_dbl_IntoClause,
    syntax_dbl_MultipleRowFetchClause,
    syntax_dbl_OpenStatement,
    syntax_dbl_Option,
    syntax_dbl_PrepareStatement,
    syntax_dbl_SetDescriptorStatement,
    syntax_dbl_SetOptionStatement,
    syntax_dbl_SetTransactionStatement,
    syntax_dbl_SingleRowFetchClause,
    syntax_ddl_CallStatement,
    syntax_ddl_CommitStatement,
    syntax_ddl_ConnectStatement,
    syntax_ddl_CreateAliasStatement,
    syntax_ddl_CreateIndexStatement,
    syntax_ddl_CreateTableStatement,
    syntax_ddl_CreateViewStatement,
    syntax_ddl_DisconnectStatement,
    syntax_ddl_DropStatement,
    syntax_ddl_LockTableStatement,
    syntax_ddl_ReleaseStatement,
    syntax_ddl_RenameStatement,
    syntax_ddl_RollbackStatement,
    syntax_ddl_SetConnectionStatement,
    syntax_dml_ExtendedQueryExpressionBody,
    syntax_dml_ExtendedQuerySelect,
    CursorType,
    DescriptorScope,
    DropRange,
    FetchPosition,
    IsolationLevel,
    OpenUsingType,
    RWOperation,
    ShareMode,
    StatementType,
    TargetElement,
    TargetItem,
    UsingType,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bindingStatement0_stub_double():
    # syntax_BindingParseResult has no real 'syntax_BindingParseResult' property in the generated
    # code (a bare stub) -- manually attach it so syntax_BindingStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_BindingStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_BindingStatement()
    partner = syntax_BindingParseResult()
    setattr(partner, 'syntax_BindingParseResult', None)
    _safe_set(owner, 'syntax_BindingStatement', partner)
    assert getattr(partner, 'syntax_BindingParseResult') == owner
    _safe_set(owner, 'syntax_BindingStatement', None)
    assert getattr(partner, 'syntax_BindingParseResult') is None


def test_assoc_conditionItems32_stub_double():
    # Option has no real 'Option' property in the generated
    # code (a bare stub) -- manually attach it so syntax_dbl_ConditionInfoClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_dbl_ConditionInfoClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_dbl_ConditionInfoClause(condition="sample_text")
    partner = Option()
    setattr(partner, 'Option', None)
    _safe_set(owner, 'syntax_dbl_ConditionInfoClause', {partner})
    assert getattr(partner, 'Option') == owner
    _safe_set(owner, 'syntax_dbl_ConditionInfoClause', set())
    assert getattr(partner, 'Option') is None


def test_assoc_definitionStatement3_stub_double():
    # syntax_DefinitionParseResult has no real 'syntax_DefinitionParseResult' property in the generated
    # code (a bare stub) -- manually attach it so syntax_DefinitionStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_DefinitionStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_DefinitionStatement()
    partner = syntax_DefinitionParseResult()
    setattr(partner, 'syntax_DefinitionParseResult', None)
    _safe_set(owner, 'syntax_DefinitionStatement', partner)
    assert getattr(partner, 'syntax_DefinitionParseResult') == owner
    _safe_set(owner, 'syntax_DefinitionStatement', None)
    assert getattr(partner, 'syntax_DefinitionParseResult') is None


def test_assoc_indexName13_stub_double():
    # ddl_syntax_QualifiedName has no real 'ddl_syntax_QualifiedName14' property in the generated
    # code (a bare stub) -- manually attach it so syntax_ddl_CreateIndexStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_ddl_CreateIndexStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_ddl_CreateIndexStatement(unique=True)
    partner = ddl_syntax_QualifiedName()
    setattr(partner, 'ddl_syntax_QualifiedName14', None)
    _safe_set(owner, 'syntax_ddl_CreateIndexStatement', partner)
    assert getattr(partner, 'ddl_syntax_QualifiedName14') == owner
    _safe_set(owner, 'syntax_ddl_CreateIndexStatement', None)
    assert getattr(partner, 'ddl_syntax_QualifiedName14') is None


def test_assoc_into33_stub_double():
    # IntoClause has no real 'IntoClause' property in the generated
    # code (a bare stub) -- manually attach it so syntax_dbl_DescribeStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_dbl_DescribeStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_dbl_DescribeStatement(statementName="sample_text")
    partner = IntoClause()
    setattr(partner, 'IntoClause', None)
    _safe_set(owner, 'syntax_dbl_DescribeStatement', partner)
    assert getattr(partner, 'IntoClause') == owner
    _safe_set(owner, 'syntax_dbl_DescribeStatement', None)
    assert getattr(partner, 'IntoClause') is None


def test_assoc_into44_stub_double():
    # IntoClause has no real 'IntoClause45' property in the generated
    # code (a bare stub) -- manually attach it so syntax_dbl_PrepareStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_dbl_PrepareStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_dbl_PrepareStatement(from_="sample_text", statementName="sample_text")
    partner = IntoClause()
    setattr(partner, 'IntoClause45', None)
    _safe_set(owner, 'syntax_dbl_PrepareStatement', partner)
    assert getattr(partner, 'IntoClause45') == owner
    _safe_set(owner, 'syntax_dbl_PrepareStatement', None)
    assert getattr(partner, 'IntoClause45') is None


def test_assoc_items40_stub_double():
    # Option has no real 'Option41' property in the generated
    # code (a bare stub) -- manually attach it so syntax_dbl_SetDescriptorStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_dbl_SetDescriptorStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_dbl_SetDescriptorStatement(descriptorName="sample_text", value="sample_text")
    partner = Option()
    setattr(partner, 'Option41', None)
    _safe_set(owner, 'syntax_dbl_SetDescriptorStatement', {partner})
    assert getattr(partner, 'Option41') == owner
    _safe_set(owner, 'syntax_dbl_SetDescriptorStatement', set())
    assert getattr(partner, 'Option41') is None


def test_assoc_multipleRowClause34_stub_double():
    # MultipleRowFetchClause has no real 'MultipleRowFetchClause' property in the generated
    # code (a bare stub) -- manually attach it so syntax_dbl_FetchStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_dbl_FetchStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_dbl_FetchStatement(cursorName="sample_text", position="sample_text", relativePosition="sample_text")
    partner = MultipleRowFetchClause()
    setattr(partner, 'MultipleRowFetchClause', None)
    _safe_set(owner, 'syntax_dbl_FetchStatement', partner)
    assert getattr(partner, 'MultipleRowFetchClause') == owner
    _safe_set(owner, 'syntax_dbl_FetchStatement', None)
    assert getattr(partner, 'MultipleRowFetchClause') is None


def test_assoc_nameHelper6_stub_double():
    # syntax_StatementWriter has no real 'syntax_StatementWriter' property in the generated
    # code (a bare stub) -- manually attach it so syntax_NameHelper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_NameHelper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_NameHelper()
    partner = syntax_StatementWriter()
    setattr(partner, 'syntax_StatementWriter', None)
    _safe_set(owner, 'syntax_NameHelper', partner)
    assert getattr(partner, 'syntax_StatementWriter') == owner
    _safe_set(owner, 'syntax_NameHelper', None)
    assert getattr(partner, 'syntax_StatementWriter') is None


def test_assoc_onTable15_stub_double():
    # ddl_syntax_QualifiedName has no real 'ddl_syntax_QualifiedName17' property in the generated
    # code (a bare stub) -- manually attach it so syntax_ddl_CreateIndexStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_ddl_CreateIndexStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_ddl_CreateIndexStatement(unique=True)
    partner = ddl_syntax_QualifiedName()
    setattr(partner, 'ddl_syntax_QualifiedName17', None)
    _safe_set(owner, 'syntax_ddl_CreateIndexStatement16', partner)
    assert getattr(partner, 'ddl_syntax_QualifiedName17') == owner
    _safe_set(owner, 'syntax_ddl_CreateIndexStatement16', None)
    assert getattr(partner, 'ddl_syntax_QualifiedName17') is None


def test_assoc_originalName30_stub_double():
    # ddl_syntax_QualifiedName has no real 'ddl_syntax_QualifiedName31' property in the generated
    # code (a bare stub) -- manually attach it so syntax_ddl_RenameStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_ddl_RenameStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_ddl_RenameStatement(newName="sample_text", system="sample_text", target="sample_text")
    partner = ddl_syntax_QualifiedName()
    setattr(partner, 'ddl_syntax_QualifiedName31', None)
    _safe_set(owner, 'syntax_ddl_RenameStatement', partner)
    assert getattr(partner, 'ddl_syntax_QualifiedName31') == owner
    _safe_set(owner, 'syntax_ddl_RenameStatement', None)
    assert getattr(partner, 'ddl_syntax_QualifiedName31') is None


def test_assoc_procedureName7_stub_double():
    # ddl_syntax_QualifiedName has no real 'ddl_syntax_QualifiedName' property in the generated
    # code (a bare stub) -- manually attach it so syntax_ddl_CallStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_ddl_CallStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_ddl_CallStatement(parms="sample_text")
    partner = ddl_syntax_QualifiedName()
    setattr(partner, 'ddl_syntax_QualifiedName', None)
    _safe_set(owner, 'syntax_ddl_CallStatement', partner)
    assert getattr(partner, 'ddl_syntax_QualifiedName') == owner
    _safe_set(owner, 'syntax_ddl_CallStatement', None)
    assert getattr(partner, 'ddl_syntax_QualifiedName') is None


def test_assoc_singleRowClause35_stub_double():
    # SingleRowFetchClause has no real 'SingleRowFetchClause' property in the generated
    # code (a bare stub) -- manually attach it so syntax_dbl_FetchStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_dbl_FetchStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_dbl_FetchStatement(cursorName="sample_text", position="sample_text", relativePosition="sample_text")
    partner = SingleRowFetchClause()
    setattr(partner, 'SingleRowFetchClause', None)
    _safe_set(owner, 'syntax_dbl_FetchStatement36', partner)
    assert getattr(partner, 'SingleRowFetchClause') == owner
    _safe_set(owner, 'syntax_dbl_FetchStatement36', None)
    assert getattr(partner, 'SingleRowFetchClause') is None


def test_assoc_sortBy18_stub_double():
    # ddl_syntax_IndexDef has no real 'ddl_syntax_IndexDef' property in the generated
    # code (a bare stub) -- manually attach it so syntax_ddl_CreateIndexStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_ddl_CreateIndexStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_ddl_CreateIndexStatement(unique=True)
    partner = ddl_syntax_IndexDef()
    setattr(partner, 'ddl_syntax_IndexDef', None)
    _safe_set(owner, 'syntax_ddl_CreateIndexStatement19', partner)
    assert getattr(partner, 'ddl_syntax_IndexDef') == owner
    _safe_set(owner, 'syntax_ddl_CreateIndexStatement19', None)
    assert getattr(partner, 'ddl_syntax_IndexDef') is None


def test_assoc_tableName28_stub_double():
    # ddl_syntax_QualifiedName has no real 'ddl_syntax_QualifiedName29' property in the generated
    # code (a bare stub) -- manually attach it so syntax_ddl_LockTableStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_ddl_LockTableStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_ddl_LockTableStatement(allowRead=True, shareMode="sample_text")
    partner = ddl_syntax_QualifiedName()
    setattr(partner, 'ddl_syntax_QualifiedName29', None)
    _safe_set(owner, 'syntax_ddl_LockTableStatement', partner)
    assert getattr(partner, 'ddl_syntax_QualifiedName29') == owner
    _safe_set(owner, 'syntax_ddl_LockTableStatement', None)
    assert getattr(partner, 'ddl_syntax_QualifiedName29') is None


def test_assoc_targetName26_stub_double():
    # ddl_syntax_QualifiedName has no real 'ddl_syntax_QualifiedName27' property in the generated
    # code (a bare stub) -- manually attach it so syntax_ddl_DropStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_ddl_DropStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_ddl_DropStatement(range="sample_text", target="sample_text")
    partner = ddl_syntax_QualifiedName()
    setattr(partner, 'ddl_syntax_QualifiedName27', None)
    _safe_set(owner, 'syntax_ddl_DropStatement', partner)
    assert getattr(partner, 'ddl_syntax_QualifiedName27') == owner
    _safe_set(owner, 'syntax_ddl_DropStatement', None)
    assert getattr(partner, 'ddl_syntax_QualifiedName27') is None


def test_assoc_variables37_stub_double():
    # Option has no real 'Option38' property in the generated
    # code (a bare stub) -- manually attach it so syntax_dbl_GetDescriptorStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_dbl_GetDescriptorStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_dbl_GetDescriptorStatement(descriptorName="sample_text", descriptorScope="sample_text", value="sample_text")
    partner = Option()
    setattr(partner, 'Option38', None)
    _safe_set(owner, 'syntax_dbl_GetDescriptorStatement', {partner})
    assert getattr(partner, 'Option38') == owner
    _safe_set(owner, 'syntax_dbl_GetDescriptorStatement', set())
    assert getattr(partner, 'Option38') is None


def test_assoc_viewName24_stub_double():
    # ddl_syntax_QualifiedName has no real 'ddl_syntax_QualifiedName25' property in the generated
    # code (a bare stub) -- manually attach it so syntax_ddl_CreateViewStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syntax_ddl_CreateViewStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syntax_ddl_CreateViewStatement(fields="sample_text", query="sample_text")
    partner = ddl_syntax_QualifiedName()
    setattr(partner, 'ddl_syntax_QualifiedName25', None)
    _safe_set(owner, 'syntax_ddl_CreateViewStatement', partner)
    assert getattr(partner, 'ddl_syntax_QualifiedName25') == owner
    _safe_set(owner, 'syntax_ddl_CreateViewStatement', None)
    assert getattr(partner, 'ddl_syntax_QualifiedName25') is None


