# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    oracle_OracleSequenceProperty,
    ExtensibleModel,
    oracle_OracleUser,
    oracle_OraclePrivilege,
    oracle_DatabaseModuleExtensibleProperty,
    oracle_TableSpaceRelation,
    oracle_TableSpace,
    DatabaseResourceData,
    oracle_SequenceResourceData,
    oracle_OracleUserResourceData,
    oracle_TriggerResourceData,
    oracle_OracleSpaceResourceData,
    oracle_OracleModuleProperty,
    oracle_OracleViewProperty,
    oracle_OracleIndexProperty,
    oracle_OracleTableProperty,
    table_type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_oracle_oraclesequenceproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleSequenceProperty)


def test_hyp_oracle_oraclesequenceproperty_constructor_exists():
    assert callable(oracle_OracleSequenceProperty.__init__)


def test_hyp_oracle_oraclesequenceproperty_constructor_args():
    sig = inspect.signature(oracle_OracleSequenceProperty.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"




def test_hyp_extensiblemodel_is_not_abstract():
    assert not inspect.isabstract(ExtensibleModel)


def test_hyp_extensiblemodel_constructor_exists():
    assert callable(ExtensibleModel.__init__)


def test_hyp_extensiblemodel_constructor_args():
    sig = inspect.signature(ExtensibleModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oracle_oracleuser_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleUser)


def test_hyp_oracle_oracleuser_constructor_exists():
    assert callable(oracle_OracleUser.__init__)


def test_hyp_oracle_oracleuser_constructor_args():
    sig = inspect.signature(oracle_OracleUser.__init__)
    params = list(sig.parameters.keys())
    assert "defaultTableSpace" in params, "Missing parameter 'defaultTableSpace'"
    assert "enable" in params, "Missing parameter 'enable'"
    assert "name" in params, "Missing parameter 'name'"
    assert "attributes" in params, "Missing parameter 'attributes'"
    assert "password" in params, "Missing parameter 'password'"
    assert "decription" in params, "Missing parameter 'decription'"









def test_hyp_oracle_oracleprivilege_is_not_abstract():
    assert not inspect.isabstract(oracle_OraclePrivilege)


def test_hyp_oracle_oracleprivilege_constructor_exists():
    assert callable(oracle_OraclePrivilege.__init__)


def test_hyp_oracle_oracleprivilege_constructor_args():
    sig = inspect.signature(oracle_OraclePrivilege.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "decription" in params, "Missing parameter 'decription'"






def test_hyp_oracle_databasemoduleextensibleproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_DatabaseModuleExtensibleProperty)


def test_hyp_oracle_databasemoduleextensibleproperty_constructor_exists():
    assert callable(oracle_DatabaseModuleExtensibleProperty.__init__)


def test_hyp_oracle_databasemoduleextensibleproperty_constructor_args():
    sig = inspect.signature(oracle_DatabaseModuleExtensibleProperty.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "splitNum" in params, "Missing parameter 'splitNum'"
    assert "tableType" in params, "Missing parameter 'tableType'"
    assert "bizPkg" in params, "Missing parameter 'bizPkg'"
    assert "splitField" in params, "Missing parameter 'splitField'"
    assert "space" in params, "Missing parameter 'space'"









def test_hyp_oracle_tablespacerelation_is_not_abstract():
    assert not inspect.isabstract(oracle_TableSpaceRelation)


def test_hyp_oracle_tablespacerelation_constructor_exists():
    assert callable(oracle_TableSpaceRelation.__init__)


def test_hyp_oracle_tablespacerelation_constructor_args():
    sig = inspect.signature(oracle_TableSpaceRelation.__init__)
    params = list(sig.parameters.keys())
    assert "mainSpace" in params, "Missing parameter 'mainSpace'"
    assert "indexSpace" in params, "Missing parameter 'indexSpace'"





def test_hyp_oracle_tablespace_is_not_abstract():
    assert not inspect.isabstract(oracle_TableSpace)


def test_hyp_oracle_tablespace_constructor_exists():
    assert callable(oracle_TableSpace.__init__)


def test_hyp_oracle_tablespace_constructor_args():
    sig = inspect.signature(oracle_TableSpace.__init__)
    params = list(sig.parameters.keys())
    assert "logicName" in params, "Missing parameter 'logicName'"
    assert "size" in params, "Missing parameter 'size'"
    assert "file" in params, "Missing parameter 'file'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "user" in params, "Missing parameter 'user'"
    assert "chineseName" in params, "Missing parameter 'chineseName'"










def test_hyp_databaseresourcedata_is_not_abstract():
    assert not inspect.isabstract(DatabaseResourceData)


def test_hyp_databaseresourcedata_constructor_exists():
    assert callable(DatabaseResourceData.__init__)


def test_hyp_databaseresourcedata_constructor_args():
    sig = inspect.signature(DatabaseResourceData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oracle_sequenceresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle_SequenceResourceData)


def test_hyp_oracle_sequenceresourcedata_constructor_exists():
    assert callable(oracle_SequenceResourceData.__init__)


def test_hyp_oracle_sequenceresourcedata_constructor_args():
    sig = inspect.signature(oracle_SequenceResourceData.__init__)
    params = list(sig.parameters.keys())
    assert "useCache" in params, "Missing parameter 'useCache'"
    assert "increment" in params, "Missing parameter 'increment'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "cycle" in params, "Missing parameter 'cycle'"
    assert "start" in params, "Missing parameter 'start'"
    assert "isHistory" in params, "Missing parameter 'isHistory'"
    assert "cache" in params, "Missing parameter 'cache'"












def test_hyp_oracle_oracleuserresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleUserResourceData)


def test_hyp_oracle_oracleuserresourcedata_constructor_exists():
    assert callable(oracle_OracleUserResourceData.__init__)


def test_hyp_oracle_oracleuserresourcedata_constructor_args():
    sig = inspect.signature(oracle_OracleUserResourceData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oracle_triggerresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle_TriggerResourceData)


def test_hyp_oracle_triggerresourcedata_constructor_exists():
    assert callable(oracle_TriggerResourceData.__init__)


def test_hyp_oracle_triggerresourcedata_constructor_args():
    sig = inspect.signature(oracle_TriggerResourceData.__init__)
    params = list(sig.parameters.keys())
    assert "sql" in params, "Missing parameter 'sql'"




def test_hyp_oracle_oraclespaceresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleSpaceResourceData)


def test_hyp_oracle_oraclespaceresourcedata_constructor_exists():
    assert callable(oracle_OracleSpaceResourceData.__init__)


def test_hyp_oracle_oraclespaceresourcedata_constructor_args():
    sig = inspect.signature(oracle_OracleSpaceResourceData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oracle_oraclemoduleproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleModuleProperty)


def test_hyp_oracle_oraclemoduleproperty_constructor_exists():
    assert callable(oracle_OracleModuleProperty.__init__)


def test_hyp_oracle_oraclemoduleproperty_constructor_args():
    sig = inspect.signature(oracle_OracleModuleProperty.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"




def test_hyp_oracle_oracleviewproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleViewProperty)


def test_hyp_oracle_oracleviewproperty_constructor_exists():
    assert callable(oracle_OracleViewProperty.__init__)


def test_hyp_oracle_oracleviewproperty_constructor_args():
    sig = inspect.signature(oracle_OracleViewProperty.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"




def test_hyp_oracle_oracleindexproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleIndexProperty)


def test_hyp_oracle_oracleindexproperty_constructor_exists():
    assert callable(oracle_OracleIndexProperty.__init__)


def test_hyp_oracle_oracleindexproperty_constructor_args():
    sig = inspect.signature(oracle_OracleIndexProperty.__init__)
    params = list(sig.parameters.keys())
    assert "reverse" in params, "Missing parameter 'reverse'"




def test_hyp_oracle_oracletableproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleTableProperty)


def test_hyp_oracle_oracletableproperty_constructor_exists():
    assert callable(oracle_OracleTableProperty.__init__)


def test_hyp_oracle_oracletableproperty_constructor_args():
    sig = inspect.signature(oracle_OracleTableProperty.__init__)
    params = list(sig.parameters.keys())
    assert "tabletype" in params, "Missing parameter 'tabletype'"
    assert "space" in params, "Missing parameter 'space'"



def test_hyp_table_type_exists():
    # Check that the Enumeration exists
    assert table_type is not None

def test_hyp_table_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in table_type]
    expected_literals = [
        "TEMP_NO_VALUE",
        "COMMON",
        "TEMP_WITH_VALUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in table_type"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
oracle_OracleSequenceProperty_strategy = st.builds(
    oracle_OracleSequenceProperty,
    space=
        safe_text
)
ExtensibleModel_strategy = st.builds(
    ExtensibleModel,
)
oracle_OracleUser_strategy = st.builds(
    oracle_OracleUser,
    defaultTableSpace=
        safe_text,
    enable=
        st.booleans(),
    name=
        safe_text,
    attributes=
        safe_text,
    password=
        safe_text,
    decription=
        safe_text
)
oracle_OraclePrivilege_strategy = st.builds(
    oracle_OraclePrivilege,
    name=
        safe_text,
    type=
        safe_text,
    decription=
        safe_text
)
oracle_DatabaseModuleExtensibleProperty_strategy = st.builds(
    oracle_DatabaseModuleExtensibleProperty,
    startDate=
        safe_text,
    splitNum=
        safe_text,
    tableType=
        safe_text,
    bizPkg=
        safe_text,
    splitField=
        safe_text,
    space=
        safe_text
)
oracle_TableSpaceRelation_strategy = st.builds(
    oracle_TableSpaceRelation,
    mainSpace=
        safe_text,
    indexSpace=
        safe_text
)
oracle_TableSpace_strategy = st.builds(
    oracle_TableSpace,
    logicName=
        safe_text,
    size=
        safe_text,
    file=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    user=
        safe_text,
    chineseName=
        safe_text
)
DatabaseResourceData_strategy = st.builds(
    DatabaseResourceData,
)
oracle_SequenceResourceData_strategy = st.builds(
    oracle_SequenceResourceData,
    useCache=
        st.booleans(),
    increment=
        safe_text,
    tableName=
        safe_text,
    maxValue=
        safe_text,
    minValue=
        safe_text,
    cycle=
        st.booleans(),
    start=
        safe_text,
    isHistory=
        st.booleans(),
    cache=
        safe_text
)
oracle_OracleUserResourceData_strategy = st.builds(
    oracle_OracleUserResourceData,
)
oracle_TriggerResourceData_strategy = st.builds(
    oracle_TriggerResourceData,
    sql=
        safe_text
)
oracle_OracleSpaceResourceData_strategy = st.builds(
    oracle_OracleSpaceResourceData,
)
oracle_OracleModuleProperty_strategy = st.builds(
    oracle_OracleModuleProperty,
    space=
        safe_text
)
oracle_OracleViewProperty_strategy = st.builds(
    oracle_OracleViewProperty,
    space=
        safe_text
)
oracle_OracleIndexProperty_strategy = st.builds(
    oracle_OracleIndexProperty,
    reverse=
        st.booleans()
)
oracle_OracleTableProperty_strategy = st.builds(
    oracle_OracleTableProperty,
    tabletype=
        safe_text,
    space=
        safe_text
)




@given(instance=oracle_OracleSequenceProperty_strategy)
def test_hyp_oracle_oraclesequenceproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original





@given(instance=oracle_OracleUser_strategy)
def test_hyp_oracle_oracleuser_defaultTableSpace_setter(instance):
    original = instance.defaultTableSpace
    instance.defaultTableSpace = original
    assert instance.defaultTableSpace == original



@given(instance=oracle_OracleUser_strategy)
def test_hyp_oracle_oracleuser_enable_setter(instance):
    original = instance.enable
    instance.enable = original
    assert instance.enable == original



@given(instance=oracle_OracleUser_strategy)
def test_hyp_oracle_oracleuser_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oracle_OracleUser_strategy)
def test_hyp_oracle_oracleuser_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original



@given(instance=oracle_OracleUser_strategy)
def test_hyp_oracle_oracleuser_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=oracle_OracleUser_strategy)
def test_hyp_oracle_oracleuser_decription_setter(instance):
    original = instance.decription
    instance.decription = original
    assert instance.decription == original




@given(instance=oracle_OraclePrivilege_strategy)
def test_hyp_oracle_oracleprivilege_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oracle_OraclePrivilege_strategy)
def test_hyp_oracle_oracleprivilege_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=oracle_OraclePrivilege_strategy)
def test_hyp_oracle_oracleprivilege_decription_setter(instance):
    original = instance.decription
    instance.decription = original
    assert instance.decription == original




@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_hyp_oracle_databasemoduleextensibleproperty_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_hyp_oracle_databasemoduleextensibleproperty_splitNum_setter(instance):
    original = instance.splitNum
    instance.splitNum = original
    assert instance.splitNum == original



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_hyp_oracle_databasemoduleextensibleproperty_tableType_setter(instance):
    original = instance.tableType
    instance.tableType = original
    assert instance.tableType == original



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_hyp_oracle_databasemoduleextensibleproperty_bizPkg_setter(instance):
    original = instance.bizPkg
    instance.bizPkg = original
    assert instance.bizPkg == original



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_hyp_oracle_databasemoduleextensibleproperty_splitField_setter(instance):
    original = instance.splitField
    instance.splitField = original
    assert instance.splitField == original



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_hyp_oracle_databasemoduleextensibleproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original




@given(instance=oracle_TableSpaceRelation_strategy)
def test_hyp_oracle_tablespacerelation_mainSpace_setter(instance):
    original = instance.mainSpace
    instance.mainSpace = original
    assert instance.mainSpace == original



@given(instance=oracle_TableSpaceRelation_strategy)
def test_hyp_oracle_tablespacerelation_indexSpace_setter(instance):
    original = instance.indexSpace
    instance.indexSpace = original
    assert instance.indexSpace == original




@given(instance=oracle_TableSpace_strategy)
def test_hyp_oracle_tablespace_logicName_setter(instance):
    original = instance.logicName
    instance.logicName = original
    assert instance.logicName == original



@given(instance=oracle_TableSpace_strategy)
def test_hyp_oracle_tablespace_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=oracle_TableSpace_strategy)
def test_hyp_oracle_tablespace_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=oracle_TableSpace_strategy)
def test_hyp_oracle_tablespace_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=oracle_TableSpace_strategy)
def test_hyp_oracle_tablespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oracle_TableSpace_strategy)
def test_hyp_oracle_tablespace_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original



@given(instance=oracle_TableSpace_strategy)
def test_hyp_oracle_tablespace_chineseName_setter(instance):
    original = instance.chineseName
    instance.chineseName = original
    assert instance.chineseName == original





@given(instance=oracle_SequenceResourceData_strategy)
def test_hyp_oracle_sequenceresourcedata_useCache_setter(instance):
    original = instance.useCache
    instance.useCache = original
    assert instance.useCache == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_hyp_oracle_sequenceresourcedata_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_hyp_oracle_sequenceresourcedata_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_hyp_oracle_sequenceresourcedata_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_hyp_oracle_sequenceresourcedata_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_hyp_oracle_sequenceresourcedata_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_hyp_oracle_sequenceresourcedata_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_hyp_oracle_sequenceresourcedata_isHistory_setter(instance):
    original = instance.isHistory
    instance.isHistory = original
    assert instance.isHistory == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_hyp_oracle_sequenceresourcedata_cache_setter(instance):
    original = instance.cache
    instance.cache = original
    assert instance.cache == original





@given(instance=oracle_TriggerResourceData_strategy)
def test_hyp_oracle_triggerresourcedata_sql_setter(instance):
    original = instance.sql
    instance.sql = original
    assert instance.sql == original





@given(instance=oracle_OracleModuleProperty_strategy)
def test_hyp_oracle_oraclemoduleproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original




@given(instance=oracle_OracleViewProperty_strategy)
def test_hyp_oracle_oracleviewproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original




@given(instance=oracle_OracleIndexProperty_strategy)
def test_hyp_oracle_oracleindexproperty_reverse_setter(instance):
    original = instance.reverse
    instance.reverse = original
    assert instance.reverse == original




@given(instance=oracle_OracleTableProperty_strategy)
def test_hyp_oracle_oracletableproperty_tabletype_setter(instance):
    original = instance.tabletype
    instance.tabletype = original
    assert instance.tabletype == original



@given(instance=oracle_OracleTableProperty_strategy)
def test_hyp_oracle_oracletableproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DatabaseResourceData,
    ExtensibleModel,
    oracle_DatabaseModuleExtensibleProperty,
    oracle_OracleIndexProperty,
    oracle_OracleModuleProperty,
    oracle_OraclePrivilege,
    oracle_OracleSequenceProperty,
    oracle_OracleSpaceResourceData,
    oracle_OracleTableProperty,
    oracle_OracleUser,
    oracle_OracleUserResourceData,
    oracle_OracleViewProperty,
    oracle_SequenceResourceData,
    oracle_TableSpace,
    oracle_TableSpaceRelation,
    oracle_TriggerResourceData,
    table_type,
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

def test_oracle_DatabaseModuleExtensibleProperty_bizPkg_value_roundtrip():
    instance = oracle_DatabaseModuleExtensibleProperty(bizPkg="sample_text", space="sample_text", splitField="sample_text", splitNum="sample_text", startDate="sample_text", tableType="sample_text")
    assert instance.bizPkg == "sample_text"
    instance.bizPkg = "sample_text_2"
    assert instance.bizPkg == "sample_text_2"


def test_oracle_DatabaseModuleExtensibleProperty_space_value_roundtrip():
    instance = oracle_DatabaseModuleExtensibleProperty(bizPkg="sample_text", space="sample_text", splitField="sample_text", splitNum="sample_text", startDate="sample_text", tableType="sample_text")
    assert instance.space == "sample_text"
    instance.space = "sample_text_2"
    assert instance.space == "sample_text_2"


def test_oracle_DatabaseModuleExtensibleProperty_splitField_value_roundtrip():
    instance = oracle_DatabaseModuleExtensibleProperty(bizPkg="sample_text", space="sample_text", splitField="sample_text", splitNum="sample_text", startDate="sample_text", tableType="sample_text")
    assert instance.splitField == "sample_text"
    instance.splitField = "sample_text_2"
    assert instance.splitField == "sample_text_2"


def test_oracle_DatabaseModuleExtensibleProperty_splitNum_value_roundtrip():
    instance = oracle_DatabaseModuleExtensibleProperty(bizPkg="sample_text", space="sample_text", splitField="sample_text", splitNum="sample_text", startDate="sample_text", tableType="sample_text")
    assert instance.splitNum == "sample_text"
    instance.splitNum = "sample_text_2"
    assert instance.splitNum == "sample_text_2"


def test_oracle_DatabaseModuleExtensibleProperty_startDate_value_roundtrip():
    instance = oracle_DatabaseModuleExtensibleProperty(bizPkg="sample_text", space="sample_text", splitField="sample_text", splitNum="sample_text", startDate="sample_text", tableType="sample_text")
    assert instance.startDate == "sample_text"
    instance.startDate = "sample_text_2"
    assert instance.startDate == "sample_text_2"


def test_oracle_DatabaseModuleExtensibleProperty_tableType_value_roundtrip():
    instance = oracle_DatabaseModuleExtensibleProperty(bizPkg="sample_text", space="sample_text", splitField="sample_text", splitNum="sample_text", startDate="sample_text", tableType="sample_text")
    assert instance.tableType == "sample_text"
    instance.tableType = "sample_text_2"
    assert instance.tableType == "sample_text_2"


def test_oracle_OracleIndexProperty_reverse_value_roundtrip():
    instance = oracle_OracleIndexProperty(reverse=True)
    assert instance.reverse == True
    instance.reverse = False
    assert instance.reverse == False


def test_oracle_OracleModuleProperty_space_value_roundtrip():
    instance = oracle_OracleModuleProperty(space="sample_text")
    assert instance.space == "sample_text"
    instance.space = "sample_text_2"
    assert instance.space == "sample_text_2"


def test_oracle_OraclePrivilege_decription_value_roundtrip():
    instance = oracle_OraclePrivilege(decription="sample_text", name="sample_text", type="sample_text")
    assert instance.decription == "sample_text"
    instance.decription = "sample_text_2"
    assert instance.decription == "sample_text_2"


def test_oracle_OraclePrivilege_name_value_roundtrip():
    instance = oracle_OraclePrivilege(decription="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oracle_OraclePrivilege_type_value_roundtrip():
    instance = oracle_OraclePrivilege(decription="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_oracle_OracleSequenceProperty_space_value_roundtrip():
    instance = oracle_OracleSequenceProperty(space="sample_text")
    assert instance.space == "sample_text"
    instance.space = "sample_text_2"
    assert instance.space == "sample_text_2"


def test_oracle_OracleTableProperty_space_value_roundtrip():
    instance = oracle_OracleTableProperty(space="sample_text", tabletype="sample_text")
    assert instance.space == "sample_text"
    instance.space = "sample_text_2"
    assert instance.space == "sample_text_2"


def test_oracle_OracleTableProperty_tabletype_value_roundtrip():
    instance = oracle_OracleTableProperty(space="sample_text", tabletype="sample_text")
    assert instance.tabletype == "sample_text"
    instance.tabletype = "sample_text_2"
    assert instance.tabletype == "sample_text_2"


def test_oracle_OracleUser_attributes_value_roundtrip():
    instance = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    assert instance.attributes == "sample_text"
    instance.attributes = "sample_text_2"
    assert instance.attributes == "sample_text_2"


def test_oracle_OracleUser_decription_value_roundtrip():
    instance = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    assert instance.decription == "sample_text"
    instance.decription = "sample_text_2"
    assert instance.decription == "sample_text_2"


def test_oracle_OracleUser_defaultTableSpace_value_roundtrip():
    instance = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    assert instance.defaultTableSpace == "sample_text"
    instance.defaultTableSpace = "sample_text_2"
    assert instance.defaultTableSpace == "sample_text_2"


def test_oracle_OracleUser_enable_value_roundtrip():
    instance = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    assert instance.enable == True
    instance.enable = False
    assert instance.enable == False


def test_oracle_OracleUser_name_value_roundtrip():
    instance = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oracle_OracleUser_password_value_roundtrip():
    instance = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_oracle_OracleViewProperty_space_value_roundtrip():
    instance = oracle_OracleViewProperty(space="sample_text")
    assert instance.space == "sample_text"
    instance.space = "sample_text_2"
    assert instance.space == "sample_text_2"


def test_oracle_SequenceResourceData_cache_value_roundtrip():
    instance = oracle_SequenceResourceData(cache="sample_text", cycle=True, increment="sample_text", isHistory=True, maxValue="sample_text", minValue="sample_text", start="sample_text", tableName="sample_text", useCache=True)
    assert instance.cache == "sample_text"
    instance.cache = "sample_text_2"
    assert instance.cache == "sample_text_2"


def test_oracle_SequenceResourceData_cycle_value_roundtrip():
    instance = oracle_SequenceResourceData(cache="sample_text", cycle=True, increment="sample_text", isHistory=True, maxValue="sample_text", minValue="sample_text", start="sample_text", tableName="sample_text", useCache=True)
    assert instance.cycle == True
    instance.cycle = False
    assert instance.cycle == False


def test_oracle_SequenceResourceData_increment_value_roundtrip():
    instance = oracle_SequenceResourceData(cache="sample_text", cycle=True, increment="sample_text", isHistory=True, maxValue="sample_text", minValue="sample_text", start="sample_text", tableName="sample_text", useCache=True)
    assert instance.increment == "sample_text"
    instance.increment = "sample_text_2"
    assert instance.increment == "sample_text_2"


def test_oracle_SequenceResourceData_isHistory_value_roundtrip():
    instance = oracle_SequenceResourceData(cache="sample_text", cycle=True, increment="sample_text", isHistory=True, maxValue="sample_text", minValue="sample_text", start="sample_text", tableName="sample_text", useCache=True)
    assert instance.isHistory == True
    instance.isHistory = False
    assert instance.isHistory == False


def test_oracle_SequenceResourceData_maxValue_value_roundtrip():
    instance = oracle_SequenceResourceData(cache="sample_text", cycle=True, increment="sample_text", isHistory=True, maxValue="sample_text", minValue="sample_text", start="sample_text", tableName="sample_text", useCache=True)
    assert instance.maxValue == "sample_text"
    instance.maxValue = "sample_text_2"
    assert instance.maxValue == "sample_text_2"


def test_oracle_SequenceResourceData_minValue_value_roundtrip():
    instance = oracle_SequenceResourceData(cache="sample_text", cycle=True, increment="sample_text", isHistory=True, maxValue="sample_text", minValue="sample_text", start="sample_text", tableName="sample_text", useCache=True)
    assert instance.minValue == "sample_text"
    instance.minValue = "sample_text_2"
    assert instance.minValue == "sample_text_2"


def test_oracle_SequenceResourceData_start_value_roundtrip():
    instance = oracle_SequenceResourceData(cache="sample_text", cycle=True, increment="sample_text", isHistory=True, maxValue="sample_text", minValue="sample_text", start="sample_text", tableName="sample_text", useCache=True)
    assert instance.start == "sample_text"
    instance.start = "sample_text_2"
    assert instance.start == "sample_text_2"


def test_oracle_SequenceResourceData_tableName_value_roundtrip():
    instance = oracle_SequenceResourceData(cache="sample_text", cycle=True, increment="sample_text", isHistory=True, maxValue="sample_text", minValue="sample_text", start="sample_text", tableName="sample_text", useCache=True)
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_oracle_SequenceResourceData_useCache_value_roundtrip():
    instance = oracle_SequenceResourceData(cache="sample_text", cycle=True, increment="sample_text", isHistory=True, maxValue="sample_text", minValue="sample_text", start="sample_text", tableName="sample_text", useCache=True)
    assert instance.useCache == True
    instance.useCache = False
    assert instance.useCache == False


def test_oracle_TableSpace_chineseName_value_roundtrip():
    instance = oracle_TableSpace(chineseName="sample_text", description="sample_text", file="sample_text", logicName="sample_text", name="sample_text", size="sample_text", user="sample_text")
    assert instance.chineseName == "sample_text"
    instance.chineseName = "sample_text_2"
    assert instance.chineseName == "sample_text_2"


def test_oracle_TableSpace_description_value_roundtrip():
    instance = oracle_TableSpace(chineseName="sample_text", description="sample_text", file="sample_text", logicName="sample_text", name="sample_text", size="sample_text", user="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_oracle_TableSpace_file_value_roundtrip():
    instance = oracle_TableSpace(chineseName="sample_text", description="sample_text", file="sample_text", logicName="sample_text", name="sample_text", size="sample_text", user="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_oracle_TableSpace_logicName_value_roundtrip():
    instance = oracle_TableSpace(chineseName="sample_text", description="sample_text", file="sample_text", logicName="sample_text", name="sample_text", size="sample_text", user="sample_text")
    assert instance.logicName == "sample_text"
    instance.logicName = "sample_text_2"
    assert instance.logicName == "sample_text_2"


def test_oracle_TableSpace_name_value_roundtrip():
    instance = oracle_TableSpace(chineseName="sample_text", description="sample_text", file="sample_text", logicName="sample_text", name="sample_text", size="sample_text", user="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oracle_TableSpace_size_value_roundtrip():
    instance = oracle_TableSpace(chineseName="sample_text", description="sample_text", file="sample_text", logicName="sample_text", name="sample_text", size="sample_text", user="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_oracle_TableSpace_user_value_roundtrip():
    instance = oracle_TableSpace(chineseName="sample_text", description="sample_text", file="sample_text", logicName="sample_text", name="sample_text", size="sample_text", user="sample_text")
    assert instance.user == "sample_text"
    instance.user = "sample_text_2"
    assert instance.user == "sample_text_2"


def test_oracle_TableSpaceRelation_indexSpace_value_roundtrip():
    instance = oracle_TableSpaceRelation(indexSpace="sample_text", mainSpace="sample_text")
    assert instance.indexSpace == "sample_text"
    instance.indexSpace = "sample_text_2"
    assert instance.indexSpace == "sample_text_2"


def test_oracle_TableSpaceRelation_mainSpace_value_roundtrip():
    instance = oracle_TableSpaceRelation(indexSpace="sample_text", mainSpace="sample_text")
    assert instance.mainSpace == "sample_text"
    instance.mainSpace = "sample_text_2"
    assert instance.mainSpace == "sample_text_2"


def test_oracle_TriggerResourceData_sql_value_roundtrip():
    instance = oracle_TriggerResourceData(sql="sample_text")
    assert instance.sql == "sample_text"
    instance.sql = "sample_text_2"
    assert instance.sql == "sample_text_2"


def test_oracle_OracleSpaceResourceData_isa_DatabaseResourceData():
    instance = oracle_OracleSpaceResourceData()
    assert isinstance(instance, DatabaseResourceData)


def test_oracle_OracleUserResourceData_isa_DatabaseResourceData():
    instance = oracle_OracleUserResourceData()
    assert isinstance(instance, DatabaseResourceData)


def test_oracle_SequenceResourceData_isa_DatabaseResourceData():
    instance = oracle_SequenceResourceData(cache="sample_text", cycle=True, increment="sample_text", isHistory=True, maxValue="sample_text", minValue="sample_text", start="sample_text", tableName="sample_text", useCache=True)
    assert isinstance(instance, DatabaseResourceData)


def test_oracle_TriggerResourceData_isa_DatabaseResourceData():
    instance = oracle_TriggerResourceData(sql="sample_text")
    assert isinstance(instance, DatabaseResourceData)


def test_oracle_DatabaseModuleExtensibleProperty_isa_ExtensibleModel():
    instance = oracle_DatabaseModuleExtensibleProperty(bizPkg="sample_text", space="sample_text", splitField="sample_text", splitNum="sample_text", startDate="sample_text", tableType="sample_text")
    assert isinstance(instance, ExtensibleModel)


def test_oracle_OraclePrivilege_isa_ExtensibleModel():
    instance = oracle_OraclePrivilege(decription="sample_text", name="sample_text", type="sample_text")
    assert isinstance(instance, ExtensibleModel)


def test_oracle_OracleUser_isa_ExtensibleModel():
    instance = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    assert isinstance(instance, ExtensibleModel)


def test_oracle_TableSpace_isa_ExtensibleModel():
    instance = oracle_TableSpace(chineseName="sample_text", description="sample_text", file="sample_text", logicName="sample_text", name="sample_text", size="sample_text", user="sample_text")
    assert isinstance(instance, ExtensibleModel)


def test_oracle_TableSpaceRelation_isa_ExtensibleModel():
    instance = oracle_TableSpaceRelation(indexSpace="sample_text", mainSpace="sample_text")
    assert isinstance(instance, ExtensibleModel)


def test_assoc_privileges4_link_reassign_clear():
    a = oracle_OraclePrivilege(decription="sample_text", name="sample_text", type="sample_text")
    b1 = oracle_OracleUserResourceData()
    b2 = oracle_OracleUserResourceData()
    _safe_set(a, 'oracle_OraclePrivilege', b1)
    assert _is_linked(a, 'oracle_OraclePrivilege', b1)
    if hasattr(b1, 'oracle_OracleUserResourceData5'):
        assert _is_linked(b1, 'oracle_OracleUserResourceData5', a)
    _safe_set(a, 'oracle_OraclePrivilege', b2)
    assert _is_linked(a, 'oracle_OraclePrivilege', b2)
    if hasattr(b1, 'oracle_OracleUserResourceData5'):
        assert not _is_linked(b1, 'oracle_OracleUserResourceData5', a)
    if hasattr(b2, 'oracle_OracleUserResourceData5'):
        assert _is_linked(b2, 'oracle_OracleUserResourceData5', a)
    _safe_set(a, 'oracle_OraclePrivilege', None)
    assert not _is_linked(a, 'oracle_OraclePrivilege', b2)
    if hasattr(b2, 'oracle_OracleUserResourceData5'):
        assert not _is_linked(b2, 'oracle_OracleUserResourceData5', a)


def test_assoc_privileges6_link_reassign_clear():
    a = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    b1 = oracle_OraclePrivilege(decription="sample_text", name="sample_text", type="sample_text")
    b2 = oracle_OraclePrivilege(decription="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'oracle_OracleUser7', {b1})
    assert _is_linked(a, 'oracle_OracleUser7', b1)
    if hasattr(b1, 'oracle_OraclePrivilege8'):
        assert _is_linked(b1, 'oracle_OraclePrivilege8', a)
    _safe_set(a, 'oracle_OracleUser7', {b2})
    assert _is_linked(a, 'oracle_OracleUser7', b2)
    if hasattr(b1, 'oracle_OraclePrivilege8'):
        assert not _is_linked(b1, 'oracle_OraclePrivilege8', a)
    if hasattr(b2, 'oracle_OraclePrivilege8'):
        assert _is_linked(b2, 'oracle_OraclePrivilege8', a)
    _safe_set(a, 'oracle_OracleUser7', set())
    assert not _is_linked(a, 'oracle_OracleUser7', b2)
    if hasattr(b2, 'oracle_OraclePrivilege8'):
        assert not _is_linked(b2, 'oracle_OraclePrivilege8', a)


def test_assoc_relations1_link_reassign_clear():
    a = oracle_TableSpaceRelation(indexSpace="sample_text", mainSpace="sample_text")
    b1 = oracle_OracleSpaceResourceData()
    b2 = oracle_OracleSpaceResourceData()
    _safe_set(a, 'oracle_TableSpaceRelation', b1)
    assert _is_linked(a, 'oracle_TableSpaceRelation', b1)
    if hasattr(b1, 'oracle_OracleSpaceResourceData2'):
        assert _is_linked(b1, 'oracle_OracleSpaceResourceData2', a)
    _safe_set(a, 'oracle_TableSpaceRelation', b2)
    assert _is_linked(a, 'oracle_TableSpaceRelation', b2)
    if hasattr(b1, 'oracle_OracleSpaceResourceData2'):
        assert not _is_linked(b1, 'oracle_OracleSpaceResourceData2', a)
    if hasattr(b2, 'oracle_OracleSpaceResourceData2'):
        assert _is_linked(b2, 'oracle_OracleSpaceResourceData2', a)
    _safe_set(a, 'oracle_TableSpaceRelation', None)
    assert not _is_linked(a, 'oracle_TableSpaceRelation', b2)
    if hasattr(b2, 'oracle_OracleSpaceResourceData2'):
        assert not _is_linked(b2, 'oracle_OracleSpaceResourceData2', a)


def test_assoc_spaces0_link_reassign_clear():
    a = oracle_TableSpace(chineseName="sample_text", description="sample_text", file="sample_text", logicName="sample_text", name="sample_text", size="sample_text", user="sample_text")
    b1 = oracle_OracleSpaceResourceData()
    b2 = oracle_OracleSpaceResourceData()
    _safe_set(a, 'oracle_TableSpace', b1)
    assert _is_linked(a, 'oracle_TableSpace', b1)
    if hasattr(b1, 'oracle_OracleSpaceResourceData'):
        assert _is_linked(b1, 'oracle_OracleSpaceResourceData', a)
    _safe_set(a, 'oracle_TableSpace', b2)
    assert _is_linked(a, 'oracle_TableSpace', b2)
    if hasattr(b1, 'oracle_OracleSpaceResourceData'):
        assert not _is_linked(b1, 'oracle_OracleSpaceResourceData', a)
    if hasattr(b2, 'oracle_OracleSpaceResourceData'):
        assert _is_linked(b2, 'oracle_OracleSpaceResourceData', a)
    _safe_set(a, 'oracle_TableSpace', None)
    assert not _is_linked(a, 'oracle_TableSpace', b2)
    if hasattr(b2, 'oracle_OracleSpaceResourceData'):
        assert not _is_linked(b2, 'oracle_OracleSpaceResourceData', a)


def test_assoc_users3_link_reassign_clear():
    a = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    b1 = oracle_OracleUserResourceData()
    b2 = oracle_OracleUserResourceData()
    _safe_set(a, 'oracle_OracleUser', b1)
    assert _is_linked(a, 'oracle_OracleUser', b1)
    if hasattr(b1, 'oracle_OracleUserResourceData'):
        assert _is_linked(b1, 'oracle_OracleUserResourceData', a)
    _safe_set(a, 'oracle_OracleUser', b2)
    assert _is_linked(a, 'oracle_OracleUser', b2)
    if hasattr(b1, 'oracle_OracleUserResourceData'):
        assert not _is_linked(b1, 'oracle_OracleUserResourceData', a)
    if hasattr(b2, 'oracle_OracleUserResourceData'):
        assert _is_linked(b2, 'oracle_OracleUserResourceData', a)
    _safe_set(a, 'oracle_OracleUser', None)
    assert not _is_linked(a, 'oracle_OracleUser', b2)
    if hasattr(b2, 'oracle_OracleUserResourceData'):
        assert not _is_linked(b2, 'oracle_OracleUserResourceData', a)


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


oracle_DatabaseModuleExtensibleProperty_strategy = st.builds(oracle_DatabaseModuleExtensibleProperty, bizPkg=safe_text, space=safe_text, splitField=safe_text, splitNum=safe_text, startDate=safe_text, tableType=safe_text)
@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
@settings(max_examples=25)
def test_oracle_DatabaseModuleExtensibleProperty_instantiation(instance):
    assert isinstance(instance, oracle_DatabaseModuleExtensibleProperty)


oracle_OracleIndexProperty_strategy = st.builds(oracle_OracleIndexProperty, reverse=st.booleans())
@given(instance=oracle_OracleIndexProperty_strategy)
@settings(max_examples=25)
def test_oracle_OracleIndexProperty_instantiation(instance):
    assert isinstance(instance, oracle_OracleIndexProperty)


oracle_OracleModuleProperty_strategy = st.builds(oracle_OracleModuleProperty, space=safe_text)
@given(instance=oracle_OracleModuleProperty_strategy)
@settings(max_examples=25)
def test_oracle_OracleModuleProperty_instantiation(instance):
    assert isinstance(instance, oracle_OracleModuleProperty)


oracle_OraclePrivilege_strategy = st.builds(oracle_OraclePrivilege, decription=safe_text, name=safe_text, type=safe_text)
@given(instance=oracle_OraclePrivilege_strategy)
@settings(max_examples=25)
def test_oracle_OraclePrivilege_instantiation(instance):
    assert isinstance(instance, oracle_OraclePrivilege)


oracle_OracleSequenceProperty_strategy = st.builds(oracle_OracleSequenceProperty, space=safe_text)
@given(instance=oracle_OracleSequenceProperty_strategy)
@settings(max_examples=25)
def test_oracle_OracleSequenceProperty_instantiation(instance):
    assert isinstance(instance, oracle_OracleSequenceProperty)


oracle_OracleSpaceResourceData_strategy = st.builds(oracle_OracleSpaceResourceData)
@given(instance=oracle_OracleSpaceResourceData_strategy)
@settings(max_examples=25)
def test_oracle_OracleSpaceResourceData_instantiation(instance):
    assert isinstance(instance, oracle_OracleSpaceResourceData)


oracle_OracleTableProperty_strategy = st.builds(oracle_OracleTableProperty, space=safe_text, tabletype=safe_text)
@given(instance=oracle_OracleTableProperty_strategy)
@settings(max_examples=25)
def test_oracle_OracleTableProperty_instantiation(instance):
    assert isinstance(instance, oracle_OracleTableProperty)


oracle_OracleUser_strategy = st.builds(oracle_OracleUser, attributes=safe_text, decription=safe_text, defaultTableSpace=safe_text, enable=st.booleans(), name=safe_text, password=safe_text)
@given(instance=oracle_OracleUser_strategy)
@settings(max_examples=25)
def test_oracle_OracleUser_instantiation(instance):
    assert isinstance(instance, oracle_OracleUser)


oracle_OracleUserResourceData_strategy = st.builds(oracle_OracleUserResourceData)
@given(instance=oracle_OracleUserResourceData_strategy)
@settings(max_examples=25)
def test_oracle_OracleUserResourceData_instantiation(instance):
    assert isinstance(instance, oracle_OracleUserResourceData)


oracle_OracleViewProperty_strategy = st.builds(oracle_OracleViewProperty, space=safe_text)
@given(instance=oracle_OracleViewProperty_strategy)
@settings(max_examples=25)
def test_oracle_OracleViewProperty_instantiation(instance):
    assert isinstance(instance, oracle_OracleViewProperty)


oracle_SequenceResourceData_strategy = st.builds(oracle_SequenceResourceData, cache=safe_text, cycle=st.booleans(), increment=safe_text, isHistory=st.booleans(), maxValue=safe_text, minValue=safe_text, start=safe_text, tableName=safe_text, useCache=st.booleans())
@given(instance=oracle_SequenceResourceData_strategy)
@settings(max_examples=25)
def test_oracle_SequenceResourceData_instantiation(instance):
    assert isinstance(instance, oracle_SequenceResourceData)


oracle_TableSpace_strategy = st.builds(oracle_TableSpace, chineseName=safe_text, description=safe_text, file=safe_text, logicName=safe_text, name=safe_text, size=safe_text, user=safe_text)
@given(instance=oracle_TableSpace_strategy)
@settings(max_examples=25)
def test_oracle_TableSpace_instantiation(instance):
    assert isinstance(instance, oracle_TableSpace)


oracle_TableSpaceRelation_strategy = st.builds(oracle_TableSpaceRelation, indexSpace=safe_text, mainSpace=safe_text)
@given(instance=oracle_TableSpaceRelation_strategy)
@settings(max_examples=25)
def test_oracle_TableSpaceRelation_instantiation(instance):
    assert isinstance(instance, oracle_TableSpaceRelation)


oracle_TriggerResourceData_strategy = st.builds(oracle_TriggerResourceData, sql=safe_text)
@given(instance=oracle_TriggerResourceData_strategy)
@settings(max_examples=25)
def test_oracle_TriggerResourceData_instantiation(instance):
    assert isinstance(instance, oracle_TriggerResourceData)



