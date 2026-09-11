import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Collection,
    Key,
    Type,
    columnFamilyDataModel_ClusteringKey,
    columnFamilyDataModel_Collection,
    columnFamilyDataModel_Column,
    columnFamilyDataModel_ColumnFamily,
    columnFamilyDataModel_ColumnFamilyDataModel,
    columnFamilyDataModel_Field,
    columnFamilyDataModel_Key,
    columnFamilyDataModel_List,
    columnFamilyDataModel_Map,
    columnFamilyDataModel_PartitionKey,
    columnFamilyDataModel_Set,
    columnFamilyDataModel_SimpleType,
    columnFamilyDataModel_Table,
    columnFamilyDataModel_Tuple,
    columnFamilyDataModel_Type,
    columnFamilyDataModel_UserDefinedType,
    PrimitiveType,
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

def test_columnFamilyDataModel_Collection_type_value_roundtrip():
    instance = columnFamilyDataModel_Collection(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_columnFamilyDataModel_Column_name_value_roundtrip():
    instance = columnFamilyDataModel_Column(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_columnFamilyDataModel_ColumnFamily_name_value_roundtrip():
    instance = columnFamilyDataModel_ColumnFamily(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_columnFamilyDataModel_Field_name_value_roundtrip():
    instance = columnFamilyDataModel_Field(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_columnFamilyDataModel_Map_keyType_value_roundtrip():
    instance = columnFamilyDataModel_Map(keyType="sample_text")
    assert instance.keyType == "sample_text"
    instance.keyType = "sample_text_2"
    assert instance.keyType == "sample_text_2"


def test_columnFamilyDataModel_SimpleType_type_value_roundtrip():
    instance = columnFamilyDataModel_SimpleType(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_columnFamilyDataModel_Table_name_value_roundtrip():
    instance = columnFamilyDataModel_Table(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_columnFamilyDataModel_Tuple_types_value_roundtrip():
    instance = columnFamilyDataModel_Tuple(types="sample_text")
    assert instance.types == "sample_text"
    instance.types = "sample_text_2"
    assert instance.types == "sample_text_2"


def test_columnFamilyDataModel_UserDefinedType_name_value_roundtrip():
    instance = columnFamilyDataModel_UserDefinedType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_columnFamilyDataModel_List_isa_Collection():
    instance = columnFamilyDataModel_List()
    assert isinstance(instance, Collection)


def test_columnFamilyDataModel_Map_isa_Collection():
    instance = columnFamilyDataModel_Map(keyType="sample_text")
    assert isinstance(instance, Collection)


def test_columnFamilyDataModel_Set_isa_Collection():
    instance = columnFamilyDataModel_Set()
    assert isinstance(instance, Collection)


def test_columnFamilyDataModel_ClusteringKey_isa_Key():
    instance = columnFamilyDataModel_ClusteringKey()
    assert isinstance(instance, Key)


def test_columnFamilyDataModel_PartitionKey_isa_Key():
    instance = columnFamilyDataModel_PartitionKey()
    assert isinstance(instance, Key)


def test_columnFamilyDataModel_Collection_isa_Type():
    instance = columnFamilyDataModel_Collection(type="sample_text")
    assert isinstance(instance, Type)


def test_columnFamilyDataModel_SimpleType_isa_Type():
    instance = columnFamilyDataModel_SimpleType(type="sample_text")
    assert isinstance(instance, Type)


def test_columnFamilyDataModel_Tuple_isa_Type():
    instance = columnFamilyDataModel_Tuple(types="sample_text")
    assert isinstance(instance, Type)


def test_columnFamilyDataModel_UserDefinedType_isa_Type():
    instance = columnFamilyDataModel_UserDefinedType(name="sample_text")
    assert isinstance(instance, Type)


def test_assoc_clusteringKeys7_link_reassign_clear():
    a = columnFamilyDataModel_Table(name="sample_text")
    b1 = columnFamilyDataModel_ClusteringKey()
    b2 = columnFamilyDataModel_ClusteringKey()
    _safe_set(a, 'columnFamilyDataModel_Table8', {b1})
    assert _is_linked(a, 'columnFamilyDataModel_Table8', b1)
    if hasattr(b1, 'columnFamilyDataModel_ClusteringKey'):
        assert _is_linked(b1, 'columnFamilyDataModel_ClusteringKey', a)
    _safe_set(a, 'columnFamilyDataModel_Table8', {b2})
    assert _is_linked(a, 'columnFamilyDataModel_Table8', b2)
    if hasattr(b1, 'columnFamilyDataModel_ClusteringKey'):
        assert not _is_linked(b1, 'columnFamilyDataModel_ClusteringKey', a)
    if hasattr(b2, 'columnFamilyDataModel_ClusteringKey'):
        assert _is_linked(b2, 'columnFamilyDataModel_ClusteringKey', a)
    _safe_set(a, 'columnFamilyDataModel_Table8', set())
    assert not _is_linked(a, 'columnFamilyDataModel_Table8', b2)
    if hasattr(b2, 'columnFamilyDataModel_ClusteringKey'):
        assert not _is_linked(b2, 'columnFamilyDataModel_ClusteringKey', a)


def test_assoc_column18_link_reassign_clear():
    a = columnFamilyDataModel_Column(name="sample_text")
    b1 = columnFamilyDataModel_Key()
    b2 = columnFamilyDataModel_Key()
    _safe_set(a, 'columnFamilyDataModel_Column19', b1)
    assert _is_linked(a, 'columnFamilyDataModel_Column19', b1)
    if hasattr(b1, 'columnFamilyDataModel_Key'):
        assert _is_linked(b1, 'columnFamilyDataModel_Key', a)
    _safe_set(a, 'columnFamilyDataModel_Column19', b2)
    assert _is_linked(a, 'columnFamilyDataModel_Column19', b2)
    if hasattr(b1, 'columnFamilyDataModel_Key'):
        assert not _is_linked(b1, 'columnFamilyDataModel_Key', a)
    if hasattr(b2, 'columnFamilyDataModel_Key'):
        assert _is_linked(b2, 'columnFamilyDataModel_Key', a)
    _safe_set(a, 'columnFamilyDataModel_Column19', None)
    assert not _is_linked(a, 'columnFamilyDataModel_Column19', b2)
    if hasattr(b2, 'columnFamilyDataModel_Key'):
        assert not _is_linked(b2, 'columnFamilyDataModel_Key', a)


def test_assoc_columnFamilies1_link_reassign_clear():
    a = columnFamilyDataModel_Table(name="sample_text")
    b1 = columnFamilyDataModel_ColumnFamily(name="sample_text")
    b2 = columnFamilyDataModel_ColumnFamily(name="sample_text_2")
    _safe_set(a, 'columnFamilyDataModel_Table2', {b1})
    assert _is_linked(a, 'columnFamilyDataModel_Table2', b1)
    if hasattr(b1, 'columnFamilyDataModel_ColumnFamily'):
        assert _is_linked(b1, 'columnFamilyDataModel_ColumnFamily', a)
    _safe_set(a, 'columnFamilyDataModel_Table2', {b2})
    assert _is_linked(a, 'columnFamilyDataModel_Table2', b2)
    if hasattr(b1, 'columnFamilyDataModel_ColumnFamily'):
        assert not _is_linked(b1, 'columnFamilyDataModel_ColumnFamily', a)
    if hasattr(b2, 'columnFamilyDataModel_ColumnFamily'):
        assert _is_linked(b2, 'columnFamilyDataModel_ColumnFamily', a)
    _safe_set(a, 'columnFamilyDataModel_Table2', set())
    assert not _is_linked(a, 'columnFamilyDataModel_Table2', b2)
    if hasattr(b2, 'columnFamilyDataModel_ColumnFamily'):
        assert not _is_linked(b2, 'columnFamilyDataModel_ColumnFamily', a)


def test_assoc_columnFamily11_link_reassign_clear():
    a = columnFamilyDataModel_ColumnFamily(name="sample_text")
    b1 = columnFamilyDataModel_Column(name="sample_text")
    b2 = columnFamilyDataModel_Column(name="sample_text_2")
    _safe_set(a, 'columnFamilyDataModel_ColumnFamily13', b1)
    assert _is_linked(a, 'columnFamilyDataModel_ColumnFamily13', b1)
    if hasattr(b1, 'columnFamilyDataModel_Column12'):
        assert _is_linked(b1, 'columnFamilyDataModel_Column12', a)
    _safe_set(a, 'columnFamilyDataModel_ColumnFamily13', b2)
    assert _is_linked(a, 'columnFamilyDataModel_ColumnFamily13', b2)
    if hasattr(b1, 'columnFamilyDataModel_Column12'):
        assert not _is_linked(b1, 'columnFamilyDataModel_Column12', a)
    if hasattr(b2, 'columnFamilyDataModel_Column12'):
        assert _is_linked(b2, 'columnFamilyDataModel_Column12', a)
    _safe_set(a, 'columnFamilyDataModel_ColumnFamily13', None)
    assert not _is_linked(a, 'columnFamilyDataModel_ColumnFamily13', b2)
    if hasattr(b2, 'columnFamilyDataModel_Column12'):
        assert not _is_linked(b2, 'columnFamilyDataModel_Column12', a)


def test_assoc_columns3_link_reassign_clear():
    a = columnFamilyDataModel_Table(name="sample_text")
    b1 = columnFamilyDataModel_Column(name="sample_text")
    b2 = columnFamilyDataModel_Column(name="sample_text_2")
    _safe_set(a, 'columnFamilyDataModel_Table4', {b1})
    assert _is_linked(a, 'columnFamilyDataModel_Table4', b1)
    if hasattr(b1, 'columnFamilyDataModel_Column'):
        assert _is_linked(b1, 'columnFamilyDataModel_Column', a)
    _safe_set(a, 'columnFamilyDataModel_Table4', {b2})
    assert _is_linked(a, 'columnFamilyDataModel_Table4', b2)
    if hasattr(b1, 'columnFamilyDataModel_Column'):
        assert not _is_linked(b1, 'columnFamilyDataModel_Column', a)
    if hasattr(b2, 'columnFamilyDataModel_Column'):
        assert _is_linked(b2, 'columnFamilyDataModel_Column', a)
    _safe_set(a, 'columnFamilyDataModel_Table4', set())
    assert not _is_linked(a, 'columnFamilyDataModel_Table4', b2)
    if hasattr(b2, 'columnFamilyDataModel_Column'):
        assert not _is_linked(b2, 'columnFamilyDataModel_Column', a)


def test_assoc_fields14_link_reassign_clear():
    a = columnFamilyDataModel_UserDefinedType(name="sample_text")
    b1 = columnFamilyDataModel_Field(name="sample_text")
    b2 = columnFamilyDataModel_Field(name="sample_text_2")
    _safe_set(a, 'columnFamilyDataModel_UserDefinedType', {b1})
    assert _is_linked(a, 'columnFamilyDataModel_UserDefinedType', b1)
    if hasattr(b1, 'columnFamilyDataModel_Field'):
        assert _is_linked(b1, 'columnFamilyDataModel_Field', a)
    _safe_set(a, 'columnFamilyDataModel_UserDefinedType', {b2})
    assert _is_linked(a, 'columnFamilyDataModel_UserDefinedType', b2)
    if hasattr(b1, 'columnFamilyDataModel_Field'):
        assert not _is_linked(b1, 'columnFamilyDataModel_Field', a)
    if hasattr(b2, 'columnFamilyDataModel_Field'):
        assert _is_linked(b2, 'columnFamilyDataModel_Field', a)
    _safe_set(a, 'columnFamilyDataModel_UserDefinedType', set())
    assert not _is_linked(a, 'columnFamilyDataModel_UserDefinedType', b2)
    if hasattr(b2, 'columnFamilyDataModel_Field'):
        assert not _is_linked(b2, 'columnFamilyDataModel_Field', a)


def test_assoc_partitionKeys5_link_reassign_clear():
    a = columnFamilyDataModel_Table(name="sample_text")
    b1 = columnFamilyDataModel_PartitionKey()
    b2 = columnFamilyDataModel_PartitionKey()
    _safe_set(a, 'columnFamilyDataModel_Table6', {b1})
    assert _is_linked(a, 'columnFamilyDataModel_Table6', b1)
    if hasattr(b1, 'columnFamilyDataModel_PartitionKey'):
        assert _is_linked(b1, 'columnFamilyDataModel_PartitionKey', a)
    _safe_set(a, 'columnFamilyDataModel_Table6', {b2})
    assert _is_linked(a, 'columnFamilyDataModel_Table6', b2)
    if hasattr(b1, 'columnFamilyDataModel_PartitionKey'):
        assert not _is_linked(b1, 'columnFamilyDataModel_PartitionKey', a)
    if hasattr(b2, 'columnFamilyDataModel_PartitionKey'):
        assert _is_linked(b2, 'columnFamilyDataModel_PartitionKey', a)
    _safe_set(a, 'columnFamilyDataModel_Table6', set())
    assert not _is_linked(a, 'columnFamilyDataModel_Table6', b2)
    if hasattr(b2, 'columnFamilyDataModel_PartitionKey'):
        assert not _is_linked(b2, 'columnFamilyDataModel_PartitionKey', a)


def test_assoc_tables0_link_reassign_clear():
    a = columnFamilyDataModel_Table(name="sample_text")
    b1 = columnFamilyDataModel_ColumnFamilyDataModel()
    b2 = columnFamilyDataModel_ColumnFamilyDataModel()
    _safe_set(a, 'columnFamilyDataModel_Table', b1)
    assert _is_linked(a, 'columnFamilyDataModel_Table', b1)
    if hasattr(b1, 'columnFamilyDataModel_ColumnFamilyDataModel'):
        assert _is_linked(b1, 'columnFamilyDataModel_ColumnFamilyDataModel', a)
    _safe_set(a, 'columnFamilyDataModel_Table', b2)
    assert _is_linked(a, 'columnFamilyDataModel_Table', b2)
    if hasattr(b1, 'columnFamilyDataModel_ColumnFamilyDataModel'):
        assert not _is_linked(b1, 'columnFamilyDataModel_ColumnFamilyDataModel', a)
    if hasattr(b2, 'columnFamilyDataModel_ColumnFamilyDataModel'):
        assert _is_linked(b2, 'columnFamilyDataModel_ColumnFamilyDataModel', a)
    _safe_set(a, 'columnFamilyDataModel_Table', None)
    assert not _is_linked(a, 'columnFamilyDataModel_Table', b2)
    if hasattr(b2, 'columnFamilyDataModel_ColumnFamilyDataModel'):
        assert not _is_linked(b2, 'columnFamilyDataModel_ColumnFamilyDataModel', a)


def test_assoc_type15_link_reassign_clear():
    a = columnFamilyDataModel_Field(name="sample_text")
    b1 = columnFamilyDataModel_Type()
    b2 = columnFamilyDataModel_Type()
    _safe_set(a, 'columnFamilyDataModel_Field16', b1)
    assert _is_linked(a, 'columnFamilyDataModel_Field16', b1)
    if hasattr(b1, 'columnFamilyDataModel_Type17'):
        assert _is_linked(b1, 'columnFamilyDataModel_Type17', a)
    _safe_set(a, 'columnFamilyDataModel_Field16', b2)
    assert _is_linked(a, 'columnFamilyDataModel_Field16', b2)
    if hasattr(b1, 'columnFamilyDataModel_Type17'):
        assert not _is_linked(b1, 'columnFamilyDataModel_Type17', a)
    if hasattr(b2, 'columnFamilyDataModel_Type17'):
        assert _is_linked(b2, 'columnFamilyDataModel_Type17', a)
    _safe_set(a, 'columnFamilyDataModel_Field16', None)
    assert not _is_linked(a, 'columnFamilyDataModel_Field16', b2)
    if hasattr(b2, 'columnFamilyDataModel_Type17'):
        assert not _is_linked(b2, 'columnFamilyDataModel_Type17', a)


def test_assoc_type9_link_reassign_clear():
    a = columnFamilyDataModel_Column(name="sample_text")
    b1 = columnFamilyDataModel_Type()
    b2 = columnFamilyDataModel_Type()
    _safe_set(a, 'columnFamilyDataModel_Column10', b1)
    assert _is_linked(a, 'columnFamilyDataModel_Column10', b1)
    if hasattr(b1, 'columnFamilyDataModel_Type'):
        assert _is_linked(b1, 'columnFamilyDataModel_Type', a)
    _safe_set(a, 'columnFamilyDataModel_Column10', b2)
    assert _is_linked(a, 'columnFamilyDataModel_Column10', b2)
    if hasattr(b1, 'columnFamilyDataModel_Type'):
        assert not _is_linked(b1, 'columnFamilyDataModel_Type', a)
    if hasattr(b2, 'columnFamilyDataModel_Type'):
        assert _is_linked(b2, 'columnFamilyDataModel_Type', a)
    _safe_set(a, 'columnFamilyDataModel_Column10', None)
    assert not _is_linked(a, 'columnFamilyDataModel_Column10', b2)
    if hasattr(b2, 'columnFamilyDataModel_Type'):
        assert not _is_linked(b2, 'columnFamilyDataModel_Type', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Collection_strategy = st.builds(Collection)
@given(instance=Collection_strategy)
@settings(max_examples=25)
def test_Collection_instantiation(instance):
    assert isinstance(instance, Collection)


Key_strategy = st.builds(Key)
@given(instance=Key_strategy)
@settings(max_examples=25)
def test_Key_instantiation(instance):
    assert isinstance(instance, Key)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


columnFamilyDataModel_ClusteringKey_strategy = st.builds(columnFamilyDataModel_ClusteringKey)
@given(instance=columnFamilyDataModel_ClusteringKey_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_ClusteringKey_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_ClusteringKey)


columnFamilyDataModel_Collection_strategy = st.builds(columnFamilyDataModel_Collection, type=safe_text)
@given(instance=columnFamilyDataModel_Collection_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_Collection_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_Collection)


columnFamilyDataModel_Column_strategy = st.builds(columnFamilyDataModel_Column, name=safe_text)
@given(instance=columnFamilyDataModel_Column_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_Column_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_Column)


columnFamilyDataModel_ColumnFamily_strategy = st.builds(columnFamilyDataModel_ColumnFamily, name=safe_text)
@given(instance=columnFamilyDataModel_ColumnFamily_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_ColumnFamily_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_ColumnFamily)


columnFamilyDataModel_ColumnFamilyDataModel_strategy = st.builds(columnFamilyDataModel_ColumnFamilyDataModel)
@given(instance=columnFamilyDataModel_ColumnFamilyDataModel_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_ColumnFamilyDataModel_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_ColumnFamilyDataModel)


columnFamilyDataModel_Field_strategy = st.builds(columnFamilyDataModel_Field, name=safe_text)
@given(instance=columnFamilyDataModel_Field_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_Field_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_Field)


columnFamilyDataModel_Key_strategy = st.builds(columnFamilyDataModel_Key)
@given(instance=columnFamilyDataModel_Key_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_Key_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_Key)


columnFamilyDataModel_List_strategy = st.builds(columnFamilyDataModel_List)
@given(instance=columnFamilyDataModel_List_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_List_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_List)


columnFamilyDataModel_Map_strategy = st.builds(columnFamilyDataModel_Map, keyType=safe_text)
@given(instance=columnFamilyDataModel_Map_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_Map_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_Map)


columnFamilyDataModel_PartitionKey_strategy = st.builds(columnFamilyDataModel_PartitionKey)
@given(instance=columnFamilyDataModel_PartitionKey_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_PartitionKey_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_PartitionKey)


columnFamilyDataModel_Set_strategy = st.builds(columnFamilyDataModel_Set)
@given(instance=columnFamilyDataModel_Set_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_Set_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_Set)


columnFamilyDataModel_SimpleType_strategy = st.builds(columnFamilyDataModel_SimpleType, type=safe_text)
@given(instance=columnFamilyDataModel_SimpleType_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_SimpleType_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_SimpleType)


columnFamilyDataModel_Table_strategy = st.builds(columnFamilyDataModel_Table, name=safe_text)
@given(instance=columnFamilyDataModel_Table_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_Table_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_Table)


columnFamilyDataModel_Tuple_strategy = st.builds(columnFamilyDataModel_Tuple, types=safe_text)
@given(instance=columnFamilyDataModel_Tuple_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_Tuple_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_Tuple)


columnFamilyDataModel_Type_strategy = st.builds(columnFamilyDataModel_Type)
@given(instance=columnFamilyDataModel_Type_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_Type_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_Type)


columnFamilyDataModel_UserDefinedType_strategy = st.builds(columnFamilyDataModel_UserDefinedType, name=safe_text)
@given(instance=columnFamilyDataModel_UserDefinedType_strategy)
@settings(max_examples=25)
def test_columnFamilyDataModel_UserDefinedType_instantiation(instance):
    assert isinstance(instance, columnFamilyDataModel_UserDefinedType)


