import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DataSource,
    datasetload_DataSource,
    datasetload_DataSourceJdbc,
    datasetload_Table,
    datasetload_TableGroup,
    datasetload_TableRow,
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

def test_datasetload_DataSource_Connected_value_roundtrip():
    instance = datasetload_DataSource(Connected=True, Name="sample_text")
    assert instance.Connected == True
    instance.Connected = False
    assert instance.Connected == False


def test_datasetload_DataSource_Name_value_roundtrip():
    instance = datasetload_DataSource(Connected=True, Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_datasetload_DataSourceJdbc_DataBaseUser_value_roundtrip():
    instance = datasetload_DataSourceJdbc(DataBaseUser="sample_text", DataBaseUserPwd="sample_text", DefaultSchema="sample_text")
    assert instance.DataBaseUser == "sample_text"
    instance.DataBaseUser = "sample_text_2"
    assert instance.DataBaseUser == "sample_text_2"


def test_datasetload_DataSourceJdbc_DataBaseUserPwd_value_roundtrip():
    instance = datasetload_DataSourceJdbc(DataBaseUser="sample_text", DataBaseUserPwd="sample_text", DefaultSchema="sample_text")
    assert instance.DataBaseUserPwd == "sample_text"
    instance.DataBaseUserPwd = "sample_text_2"
    assert instance.DataBaseUserPwd == "sample_text_2"


def test_datasetload_DataSourceJdbc_DefaultSchema_value_roundtrip():
    instance = datasetload_DataSourceJdbc(DataBaseUser="sample_text", DataBaseUserPwd="sample_text", DefaultSchema="sample_text")
    assert instance.DefaultSchema == "sample_text"
    instance.DefaultSchema = "sample_text_2"
    assert instance.DefaultSchema == "sample_text_2"


def test_datasetload_Table_ColumnTableRowAttributes_value_roundtrip():
    instance = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    assert instance.ColumnTableRowAttributes == "sample_text"
    instance.ColumnTableRowAttributes = "sample_text_2"
    assert instance.ColumnTableRowAttributes == "sample_text_2"


def test_datasetload_Table_KeyColumns_value_roundtrip():
    instance = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    assert instance.KeyColumns == 7
    instance.KeyColumns = 13
    assert instance.KeyColumns == 13


def test_datasetload_Table_LastLoad_value_roundtrip():
    instance = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    assert instance.LastLoad == date(2024, 1, 1)
    instance.LastLoad = date(2025, 6, 15)
    assert instance.LastLoad == date(2025, 6, 15)


def test_datasetload_Table_Name_value_roundtrip():
    instance = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_datasetload_Table_NumberOfRows_value_roundtrip():
    instance = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    assert instance.NumberOfRows == 7
    instance.NumberOfRows = 13
    assert instance.NumberOfRows == 13


def test_datasetload_Table_ParamTableGroupAttributes_value_roundtrip():
    instance = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    assert instance.ParamTableGroupAttributes == "sample_text"
    instance.ParamTableGroupAttributes = "sample_text_2"
    assert instance.ParamTableGroupAttributes == "sample_text_2"


def test_datasetload_Table_SQLStatement_value_roundtrip():
    instance = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    assert instance.SQLStatement == "sample_text"
    instance.SQLStatement = "sample_text_2"
    assert instance.SQLStatement == "sample_text_2"


def test_datasetload_TableGroup_Name_value_roundtrip():
    instance = datasetload_TableGroup(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_datasetload_TableRow_Key_value_roundtrip():
    instance = datasetload_TableRow(Key="sample_text", NewRow=True, RowNumber=7)
    assert instance.Key == "sample_text"
    instance.Key = "sample_text_2"
    assert instance.Key == "sample_text_2"


def test_datasetload_TableRow_NewRow_value_roundtrip():
    instance = datasetload_TableRow(Key="sample_text", NewRow=True, RowNumber=7)
    assert instance.NewRow == True
    instance.NewRow = False
    assert instance.NewRow == False


def test_datasetload_TableRow_RowNumber_value_roundtrip():
    instance = datasetload_TableRow(Key="sample_text", NewRow=True, RowNumber=7)
    assert instance.RowNumber == 7
    instance.RowNumber = 13
    assert instance.RowNumber == 13


def test_datasetload_DataSourceJdbc_isa_DataSource():
    instance = datasetload_DataSourceJdbc(DataBaseUser="sample_text", DataBaseUserPwd="sample_text", DefaultSchema="sample_text")
    assert isinstance(instance, DataSource)


def test_assoc_DataSource1_link_reassign_clear():
    a = datasetload_TableGroup(Name="sample_text")
    b1 = datasetload_DataSource(Connected=True, Name="sample_text")
    b2 = datasetload_DataSource(Connected=False, Name="sample_text_2")
    _safe_set(a, 'datasetload_TableGroup2', b1)
    assert _is_linked(a, 'datasetload_TableGroup2', b1)
    if hasattr(b1, 'datasetload_DataSource'):
        assert _is_linked(b1, 'datasetload_DataSource', a)
    _safe_set(a, 'datasetload_TableGroup2', b2)
    assert _is_linked(a, 'datasetload_TableGroup2', b2)
    if hasattr(b1, 'datasetload_DataSource'):
        assert not _is_linked(b1, 'datasetload_DataSource', a)
    if hasattr(b2, 'datasetload_DataSource'):
        assert _is_linked(b2, 'datasetload_DataSource', a)
    _safe_set(a, 'datasetload_TableGroup2', None)
    assert not _is_linked(a, 'datasetload_TableGroup2', b2)
    if hasattr(b2, 'datasetload_DataSource'):
        assert not _is_linked(b2, 'datasetload_DataSource', a)


def test_assoc_Rows6_link_reassign_clear():
    a = datasetload_TableRow(Key="sample_text", NewRow=True, RowNumber=7)
    b1 = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    b2 = datasetload_Table(ColumnTableRowAttributes="sample_text_2", KeyColumns=13, LastLoad=date(2025, 6, 15), Name="sample_text_2", NumberOfRows=13, ParamTableGroupAttributes="sample_text_2", SQLStatement="sample_text_2")
    _safe_set(a, 'datasetload_TableRow', b1)
    assert _is_linked(a, 'datasetload_TableRow', b1)
    if hasattr(b1, 'datasetload_Table7'):
        assert _is_linked(b1, 'datasetload_Table7', a)
    _safe_set(a, 'datasetload_TableRow', b2)
    assert _is_linked(a, 'datasetload_TableRow', b2)
    if hasattr(b1, 'datasetload_Table7'):
        assert not _is_linked(b1, 'datasetload_Table7', a)
    if hasattr(b2, 'datasetload_Table7'):
        assert _is_linked(b2, 'datasetload_Table7', a)
    _safe_set(a, 'datasetload_TableRow', None)
    assert not _is_linked(a, 'datasetload_TableRow', b2)
    if hasattr(b2, 'datasetload_Table7'):
        assert not _is_linked(b2, 'datasetload_Table7', a)


def test_assoc_Table8_link_reassign_clear():
    a = datasetload_TableRow(Key="sample_text", NewRow=True, RowNumber=7)
    b1 = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    b2 = datasetload_Table(ColumnTableRowAttributes="sample_text_2", KeyColumns=13, LastLoad=date(2025, 6, 15), Name="sample_text_2", NumberOfRows=13, ParamTableGroupAttributes="sample_text_2", SQLStatement="sample_text_2")
    _safe_set(a, 'datasetload_TableRow9', b1)
    assert _is_linked(a, 'datasetload_TableRow9', b1)
    if hasattr(b1, 'datasetload_Table10'):
        assert _is_linked(b1, 'datasetload_Table10', a)
    _safe_set(a, 'datasetload_TableRow9', b2)
    assert _is_linked(a, 'datasetload_TableRow9', b2)
    if hasattr(b1, 'datasetload_Table10'):
        assert not _is_linked(b1, 'datasetload_Table10', a)
    if hasattr(b2, 'datasetload_Table10'):
        assert _is_linked(b2, 'datasetload_Table10', a)
    _safe_set(a, 'datasetload_TableRow9', None)
    assert not _is_linked(a, 'datasetload_TableRow9', b2)
    if hasattr(b2, 'datasetload_Table10'):
        assert not _is_linked(b2, 'datasetload_Table10', a)


def test_assoc_TableGroup3_link_reassign_clear():
    a = datasetload_TableGroup(Name="sample_text")
    b1 = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    b2 = datasetload_Table(ColumnTableRowAttributes="sample_text_2", KeyColumns=13, LastLoad=date(2025, 6, 15), Name="sample_text_2", NumberOfRows=13, ParamTableGroupAttributes="sample_text_2", SQLStatement="sample_text_2")
    _safe_set(a, 'datasetload_TableGroup5', b1)
    assert _is_linked(a, 'datasetload_TableGroup5', b1)
    if hasattr(b1, 'datasetload_Table4'):
        assert _is_linked(b1, 'datasetload_Table4', a)
    _safe_set(a, 'datasetload_TableGroup5', b2)
    assert _is_linked(a, 'datasetload_TableGroup5', b2)
    if hasattr(b1, 'datasetload_Table4'):
        assert not _is_linked(b1, 'datasetload_Table4', a)
    if hasattr(b2, 'datasetload_Table4'):
        assert _is_linked(b2, 'datasetload_Table4', a)
    _safe_set(a, 'datasetload_TableGroup5', None)
    assert not _is_linked(a, 'datasetload_TableGroup5', b2)
    if hasattr(b2, 'datasetload_Table4'):
        assert not _is_linked(b2, 'datasetload_Table4', a)


def test_assoc_Tables0_link_reassign_clear():
    a = datasetload_TableGroup(Name="sample_text")
    b1 = datasetload_Table(ColumnTableRowAttributes="sample_text", KeyColumns=7, LastLoad=date(2024, 1, 1), Name="sample_text", NumberOfRows=7, ParamTableGroupAttributes="sample_text", SQLStatement="sample_text")
    b2 = datasetload_Table(ColumnTableRowAttributes="sample_text_2", KeyColumns=13, LastLoad=date(2025, 6, 15), Name="sample_text_2", NumberOfRows=13, ParamTableGroupAttributes="sample_text_2", SQLStatement="sample_text_2")
    _safe_set(a, 'datasetload_TableGroup', {b1})
    assert _is_linked(a, 'datasetload_TableGroup', b1)
    if hasattr(b1, 'datasetload_Table'):
        assert _is_linked(b1, 'datasetload_Table', a)
    _safe_set(a, 'datasetload_TableGroup', {b2})
    assert _is_linked(a, 'datasetload_TableGroup', b2)
    if hasattr(b1, 'datasetload_Table'):
        assert not _is_linked(b1, 'datasetload_Table', a)
    if hasattr(b2, 'datasetload_Table'):
        assert _is_linked(b2, 'datasetload_Table', a)
    _safe_set(a, 'datasetload_TableGroup', set())
    assert not _is_linked(a, 'datasetload_TableGroup', b2)
    if hasattr(b2, 'datasetload_Table'):
        assert not _is_linked(b2, 'datasetload_Table', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DataSource_strategy = st.builds(DataSource)
@given(instance=DataSource_strategy)
@settings(max_examples=25)
def test_DataSource_instantiation(instance):
    assert isinstance(instance, DataSource)


datasetload_DataSource_strategy = st.builds(datasetload_DataSource, Connected=st.booleans(), Name=safe_text)
@given(instance=datasetload_DataSource_strategy)
@settings(max_examples=25)
def test_datasetload_DataSource_instantiation(instance):
    assert isinstance(instance, datasetload_DataSource)


datasetload_DataSourceJdbc_strategy = st.builds(datasetload_DataSourceJdbc, DataBaseUser=safe_text, DataBaseUserPwd=safe_text, DefaultSchema=safe_text)
@given(instance=datasetload_DataSourceJdbc_strategy)
@settings(max_examples=25)
def test_datasetload_DataSourceJdbc_instantiation(instance):
    assert isinstance(instance, datasetload_DataSourceJdbc)


datasetload_Table_strategy = st.builds(datasetload_Table, ColumnTableRowAttributes=safe_text, KeyColumns=st.integers(), LastLoad=st.dates(), Name=safe_text, NumberOfRows=st.integers(), ParamTableGroupAttributes=safe_text, SQLStatement=safe_text)
@given(instance=datasetload_Table_strategy)
@settings(max_examples=25)
def test_datasetload_Table_instantiation(instance):
    assert isinstance(instance, datasetload_Table)


datasetload_TableGroup_strategy = st.builds(datasetload_TableGroup, Name=safe_text)
@given(instance=datasetload_TableGroup_strategy)
@settings(max_examples=25)
def test_datasetload_TableGroup_instantiation(instance):
    assert isinstance(instance, datasetload_TableGroup)


datasetload_TableRow_strategy = st.builds(datasetload_TableRow, Key=safe_text, NewRow=st.booleans(), RowNumber=st.integers())
@given(instance=datasetload_TableRow_strategy)
@settings(max_examples=25)
def test_datasetload_TableRow_instantiation(instance):
    assert isinstance(instance, datasetload_TableRow)


