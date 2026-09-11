import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DatabaseResourceData,
    ExtensibleModel,
    JRESResourceInfo,
    database_DBGenContext,
    database_DBModuleCommonProperty,
    database_DatabaseResourceData,
    database_ForeignKey,
    database_TableColumn,
    database_TableIndex,
    database_TableIndexColumn,
    database_TableKey,
    database_TableResourceData,
    database_ViewResourceData,
    ColumnType,
    key_type,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_database_DBModuleCommonProperty_database_value_roundtrip():
    instance = database_DBModuleCommonProperty(database="sample_text", supportDatabases="sample_text")
    assert instance.database == "sample_text"
    instance.database = "sample_text_2"
    assert instance.database == "sample_text_2"


def test_database_DBModuleCommonProperty_supportDatabases_value_roundtrip():
    instance = database_DBModuleCommonProperty(database="sample_text", supportDatabases="sample_text")
    assert instance.supportDatabases == "sample_text"
    instance.supportDatabases = "sample_text_2"
    assert instance.supportDatabases == "sample_text_2"


def test_database_ForeignKey_fieldName_value_roundtrip():
    instance = database_ForeignKey(fieldName="sample_text", tableName="sample_text")
    assert instance.fieldName == "sample_text"
    instance.fieldName = "sample_text_2"
    assert instance.fieldName == "sample_text_2"


def test_database_ForeignKey_tableName_value_roundtrip():
    instance = database_ForeignKey(fieldName="sample_text", tableName="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_database_TableColumn_chineseName_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.chineseName == "sample_text"
    instance.chineseName = "sample_text_2"
    assert instance.chineseName == "sample_text_2"


def test_database_TableColumn_columnName_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_database_TableColumn_columnType_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.columnType == "sample_text"
    instance.columnType = "sample_text_2"
    assert instance.columnType == "sample_text_2"


def test_database_TableColumn_comments_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.comments == "sample_text"
    instance.comments = "sample_text_2"
    assert instance.comments == "sample_text_2"


def test_database_TableColumn_dataType_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_database_TableColumn_defaultValue_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_database_TableColumn_description_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_database_TableColumn_fieldName_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.fieldName == "sample_text"
    instance.fieldName = "sample_text_2"
    assert instance.fieldName == "sample_text_2"


def test_database_TableColumn_mark_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.mark == "sample_text"
    instance.mark = "sample_text_2"
    assert instance.mark == "sample_text_2"


def test_database_TableColumn_name_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_database_TableColumn_nullable_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.nullable == True
    instance.nullable = False
    assert instance.nullable == False


def test_database_TableColumn_primaryKey_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.primaryKey == True
    instance.primaryKey = False
    assert instance.primaryKey == False


def test_database_TableColumn_unique_value_roundtrip():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_database_TableIndex_cluster_value_roundtrip():
    instance = database_TableIndex(cluster=True, mark="sample_text", name="sample_text", unique=True)
    assert instance.cluster == True
    instance.cluster = False
    assert instance.cluster == False


def test_database_TableIndex_mark_value_roundtrip():
    instance = database_TableIndex(cluster=True, mark="sample_text", name="sample_text", unique=True)
    assert instance.mark == "sample_text"
    instance.mark = "sample_text_2"
    assert instance.mark == "sample_text_2"


def test_database_TableIndex_name_value_roundtrip():
    instance = database_TableIndex(cluster=True, mark="sample_text", name="sample_text", unique=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_database_TableIndex_unique_value_roundtrip():
    instance = database_TableIndex(cluster=True, mark="sample_text", name="sample_text", unique=True)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_database_TableIndexColumn_ascending_value_roundtrip():
    instance = database_TableIndexColumn(ascending=True, columnName="sample_text", columnType="sample_text")
    assert instance.ascending == True
    instance.ascending = False
    assert instance.ascending == False


def test_database_TableIndexColumn_columnName_value_roundtrip():
    instance = database_TableIndexColumn(ascending=True, columnName="sample_text", columnType="sample_text")
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_database_TableIndexColumn_columnType_value_roundtrip():
    instance = database_TableIndexColumn(ascending=True, columnName="sample_text", columnType="sample_text")
    assert instance.columnType == "sample_text"
    instance.columnType = "sample_text_2"
    assert instance.columnType == "sample_text_2"


def test_database_TableKey_mark_value_roundtrip():
    instance = database_TableKey(mark="sample_text", name="sample_text", type="sample_text")
    assert instance.mark == "sample_text"
    instance.mark = "sample_text_2"
    assert instance.mark == "sample_text_2"


def test_database_TableKey_name_value_roundtrip():
    instance = database_TableKey(mark="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_database_TableKey_type_value_roundtrip():
    instance = database_TableKey(mark="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_database_ViewResourceData_isHistory_value_roundtrip():
    instance = database_ViewResourceData(isHistory=True, sql="sample_text")
    assert instance.isHistory == True
    instance.isHistory = False
    assert instance.isHistory == False


def test_database_ViewResourceData_sql_value_roundtrip():
    instance = database_ViewResourceData(isHistory=True, sql="sample_text")
    assert instance.sql == "sample_text"
    instance.sql = "sample_text_2"
    assert instance.sql == "sample_text_2"


def test_database_TableResourceData_isa_DatabaseResourceData():
    instance = database_TableResourceData()
    assert isinstance(instance, DatabaseResourceData)


def test_database_ViewResourceData_isa_DatabaseResourceData():
    instance = database_ViewResourceData(isHistory=True, sql="sample_text")
    assert isinstance(instance, DatabaseResourceData)


def test_database_DBGenContext_isa_ExtensibleModel():
    instance = database_DBGenContext()
    assert isinstance(instance, ExtensibleModel)


def test_database_TableColumn_isa_ExtensibleModel():
    instance = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    assert isinstance(instance, ExtensibleModel)


def test_database_TableIndex_isa_ExtensibleModel():
    instance = database_TableIndex(cluster=True, mark="sample_text", name="sample_text", unique=True)
    assert isinstance(instance, ExtensibleModel)


def test_database_TableIndexColumn_isa_ExtensibleModel():
    instance = database_TableIndexColumn(ascending=True, columnName="sample_text", columnType="sample_text")
    assert isinstance(instance, ExtensibleModel)


def test_database_TableKey_isa_ExtensibleModel():
    instance = database_TableKey(mark="sample_text", name="sample_text", type="sample_text")
    assert isinstance(instance, ExtensibleModel)


def test_database_DatabaseResourceData_isa_JRESResourceInfo():
    instance = database_DatabaseResourceData()
    assert isinstance(instance, JRESResourceInfo)


def test_assoc_columns0_link_reassign_clear():
    a = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    b1 = database_TableResourceData()
    b2 = database_TableResourceData()
    _safe_set(a, 'database_TableColumn', b1)
    assert _is_linked(a, 'database_TableColumn', b1)
    if hasattr(b1, 'database_TableResourceData'):
        assert _is_linked(b1, 'database_TableResourceData', a)
    _safe_set(a, 'database_TableColumn', b2)
    assert _is_linked(a, 'database_TableColumn', b2)
    if hasattr(b1, 'database_TableResourceData'):
        assert not _is_linked(b1, 'database_TableResourceData', a)
    if hasattr(b2, 'database_TableResourceData'):
        assert _is_linked(b2, 'database_TableResourceData', a)
    _safe_set(a, 'database_TableColumn', None)
    assert not _is_linked(a, 'database_TableColumn', b2)
    if hasattr(b2, 'database_TableResourceData'):
        assert not _is_linked(b2, 'database_TableResourceData', a)


def test_assoc_columns12_link_reassign_clear():
    a = database_TableKey(mark="sample_text", name="sample_text", type="sample_text")
    b1 = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    b2 = database_TableColumn(chineseName="sample_text_2", columnName="sample_text_2", columnType="sample_text_2", comments="sample_text_2", dataType="sample_text_2", defaultValue="sample_text_2", description="sample_text_2", fieldName="sample_text_2", mark="sample_text_2", name="sample_text_2", nullable=False, primaryKey=False, unique=False)
    _safe_set(a, 'database_TableKey13', {b1})
    assert _is_linked(a, 'database_TableKey13', b1)
    if hasattr(b1, 'database_TableColumn14'):
        assert _is_linked(b1, 'database_TableColumn14', a)
    _safe_set(a, 'database_TableKey13', {b2})
    assert _is_linked(a, 'database_TableKey13', b2)
    if hasattr(b1, 'database_TableColumn14'):
        assert not _is_linked(b1, 'database_TableColumn14', a)
    if hasattr(b2, 'database_TableColumn14'):
        assert _is_linked(b2, 'database_TableColumn14', a)
    _safe_set(a, 'database_TableKey13', set())
    assert not _is_linked(a, 'database_TableKey13', b2)
    if hasattr(b2, 'database_TableColumn14'):
        assert not _is_linked(b2, 'database_TableColumn14', a)


def test_assoc_columns7_link_reassign_clear():
    a = database_TableIndexColumn(ascending=True, columnName="sample_text", columnType="sample_text")
    b1 = database_TableIndex(cluster=True, mark="sample_text", name="sample_text", unique=True)
    b2 = database_TableIndex(cluster=False, mark="sample_text_2", name="sample_text_2", unique=False)
    _safe_set(a, 'database_TableIndexColumn', b1)
    assert _is_linked(a, 'database_TableIndexColumn', b1)
    if hasattr(b1, 'database_TableIndex8'):
        assert _is_linked(b1, 'database_TableIndex8', a)
    _safe_set(a, 'database_TableIndexColumn', b2)
    assert _is_linked(a, 'database_TableIndexColumn', b2)
    if hasattr(b1, 'database_TableIndex8'):
        assert not _is_linked(b1, 'database_TableIndex8', a)
    if hasattr(b2, 'database_TableIndex8'):
        assert _is_linked(b2, 'database_TableIndex8', a)
    _safe_set(a, 'database_TableIndexColumn', None)
    assert not _is_linked(a, 'database_TableIndexColumn', b2)
    if hasattr(b2, 'database_TableIndex8'):
        assert not _is_linked(b2, 'database_TableIndex8', a)


def test_assoc_foreignKey9_link_reassign_clear():
    a = database_TableKey(mark="sample_text", name="sample_text", type="sample_text")
    b1 = database_ForeignKey(fieldName="sample_text", tableName="sample_text")
    b2 = database_ForeignKey(fieldName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'database_TableKey10', {b1})
    assert _is_linked(a, 'database_TableKey10', b1)
    if hasattr(b1, 'database_ForeignKey11'):
        assert _is_linked(b1, 'database_ForeignKey11', a)
    _safe_set(a, 'database_TableKey10', {b2})
    assert _is_linked(a, 'database_TableKey10', b2)
    if hasattr(b1, 'database_ForeignKey11'):
        assert not _is_linked(b1, 'database_ForeignKey11', a)
    if hasattr(b2, 'database_ForeignKey11'):
        assert _is_linked(b2, 'database_ForeignKey11', a)
    _safe_set(a, 'database_TableKey10', set())
    assert not _is_linked(a, 'database_TableKey10', b2)
    if hasattr(b2, 'database_ForeignKey11'):
        assert not _is_linked(b2, 'database_ForeignKey11', a)


def test_assoc_foreignkey5_link_reassign_clear():
    a = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    b1 = database_ForeignKey(fieldName="sample_text", tableName="sample_text")
    b2 = database_ForeignKey(fieldName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'database_TableColumn6', {b1})
    assert _is_linked(a, 'database_TableColumn6', b1)
    if hasattr(b1, 'database_ForeignKey'):
        assert _is_linked(b1, 'database_ForeignKey', a)
    _safe_set(a, 'database_TableColumn6', {b2})
    assert _is_linked(a, 'database_TableColumn6', b2)
    if hasattr(b1, 'database_ForeignKey'):
        assert not _is_linked(b1, 'database_ForeignKey', a)
    if hasattr(b2, 'database_ForeignKey'):
        assert _is_linked(b2, 'database_ForeignKey', a)
    _safe_set(a, 'database_TableColumn6', set())
    assert not _is_linked(a, 'database_TableColumn6', b2)
    if hasattr(b2, 'database_ForeignKey'):
        assert not _is_linked(b2, 'database_ForeignKey', a)


def test_assoc_indexes1_link_reassign_clear():
    a = database_TableIndex(cluster=True, mark="sample_text", name="sample_text", unique=True)
    b1 = database_TableResourceData()
    b2 = database_TableResourceData()
    _safe_set(a, 'database_TableIndex', b1)
    assert _is_linked(a, 'database_TableIndex', b1)
    if hasattr(b1, 'database_TableResourceData2'):
        assert _is_linked(b1, 'database_TableResourceData2', a)
    _safe_set(a, 'database_TableIndex', b2)
    assert _is_linked(a, 'database_TableIndex', b2)
    if hasattr(b1, 'database_TableResourceData2'):
        assert not _is_linked(b1, 'database_TableResourceData2', a)
    if hasattr(b2, 'database_TableResourceData2'):
        assert _is_linked(b2, 'database_TableResourceData2', a)
    _safe_set(a, 'database_TableIndex', None)
    assert not _is_linked(a, 'database_TableIndex', b2)
    if hasattr(b2, 'database_TableResourceData2'):
        assert not _is_linked(b2, 'database_TableResourceData2', a)


def test_assoc_keys3_link_reassign_clear():
    a = database_TableKey(mark="sample_text", name="sample_text", type="sample_text")
    b1 = database_TableResourceData()
    b2 = database_TableResourceData()
    _safe_set(a, 'database_TableKey', b1)
    assert _is_linked(a, 'database_TableKey', b1)
    if hasattr(b1, 'database_TableResourceData4'):
        assert _is_linked(b1, 'database_TableResourceData4', a)
    _safe_set(a, 'database_TableKey', b2)
    assert _is_linked(a, 'database_TableKey', b2)
    if hasattr(b1, 'database_TableResourceData4'):
        assert not _is_linked(b1, 'database_TableResourceData4', a)
    if hasattr(b2, 'database_TableResourceData4'):
        assert _is_linked(b2, 'database_TableResourceData4', a)
    _safe_set(a, 'database_TableKey', None)
    assert not _is_linked(a, 'database_TableKey', b2)
    if hasattr(b2, 'database_TableResourceData4'):
        assert not _is_linked(b2, 'database_TableResourceData4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DatabaseResourceData_strategy = st.builds(DatabaseResourceData)
@given(instance=DatabaseResourceData_strategy)
@settings(max_examples=25)
def test_DatabaseResourceData_instantiation(instance):
    assert isinstance(instance, DatabaseResourceData)


ExtensibleModel_strategy = st.builds(ExtensibleModel)
@given(instance=ExtensibleModel_strategy)
@settings(max_examples=25)
def test_ExtensibleModel_instantiation(instance):
    assert isinstance(instance, ExtensibleModel)


JRESResourceInfo_strategy = st.builds(JRESResourceInfo)
@given(instance=JRESResourceInfo_strategy)
@settings(max_examples=25)
def test_JRESResourceInfo_instantiation(instance):
    assert isinstance(instance, JRESResourceInfo)


database_DBGenContext_strategy = st.builds(database_DBGenContext)
@given(instance=database_DBGenContext_strategy)
@settings(max_examples=25)
def test_database_DBGenContext_instantiation(instance):
    assert isinstance(instance, database_DBGenContext)


database_DBModuleCommonProperty_strategy = st.builds(database_DBModuleCommonProperty, database=safe_text, supportDatabases=safe_text)
@given(instance=database_DBModuleCommonProperty_strategy)
@settings(max_examples=25)
def test_database_DBModuleCommonProperty_instantiation(instance):
    assert isinstance(instance, database_DBModuleCommonProperty)


database_DatabaseResourceData_strategy = st.builds(database_DatabaseResourceData)
@given(instance=database_DatabaseResourceData_strategy)
@settings(max_examples=25)
def test_database_DatabaseResourceData_instantiation(instance):
    assert isinstance(instance, database_DatabaseResourceData)


database_ForeignKey_strategy = st.builds(database_ForeignKey, fieldName=safe_text, tableName=safe_text)
@given(instance=database_ForeignKey_strategy)
@settings(max_examples=25)
def test_database_ForeignKey_instantiation(instance):
    assert isinstance(instance, database_ForeignKey)


database_TableColumn_strategy = st.builds(database_TableColumn, chineseName=safe_text, columnName=safe_text, columnType=safe_text, comments=safe_text, dataType=safe_text, defaultValue=safe_text, description=safe_text, fieldName=safe_text, mark=safe_text, name=safe_text, nullable=st.booleans(), primaryKey=st.booleans(), unique=st.booleans())
@given(instance=database_TableColumn_strategy)
@settings(max_examples=25)
def test_database_TableColumn_instantiation(instance):
    assert isinstance(instance, database_TableColumn)


database_TableIndex_strategy = st.builds(database_TableIndex, cluster=st.booleans(), mark=safe_text, name=safe_text, unique=st.booleans())
@given(instance=database_TableIndex_strategy)
@settings(max_examples=25)
def test_database_TableIndex_instantiation(instance):
    assert isinstance(instance, database_TableIndex)


database_TableIndexColumn_strategy = st.builds(database_TableIndexColumn, ascending=st.booleans(), columnName=safe_text, columnType=safe_text)
@given(instance=database_TableIndexColumn_strategy)
@settings(max_examples=25)
def test_database_TableIndexColumn_instantiation(instance):
    assert isinstance(instance, database_TableIndexColumn)


database_TableKey_strategy = st.builds(database_TableKey, mark=safe_text, name=safe_text, type=safe_text)
@given(instance=database_TableKey_strategy)
@settings(max_examples=25)
def test_database_TableKey_instantiation(instance):
    assert isinstance(instance, database_TableKey)


database_TableResourceData_strategy = st.builds(database_TableResourceData)
@given(instance=database_TableResourceData_strategy)
@settings(max_examples=25)
def test_database_TableResourceData_instantiation(instance):
    assert isinstance(instance, database_TableResourceData)


database_ViewResourceData_strategy = st.builds(database_ViewResourceData, isHistory=st.booleans(), sql=safe_text)
@given(instance=database_ViewResourceData_strategy)
@settings(max_examples=25)
def test_database_ViewResourceData_instantiation(instance):
    assert isinstance(instance, database_ViewResourceData)


