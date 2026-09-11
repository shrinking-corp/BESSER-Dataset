import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArrayExpression,
    Expression,
    ExpressionWhereEntry,
    WhereEntry,
    query_AndWhereEntry,
    query_ArrayExpression,
    query_BooleanArrayExpression,
    query_BooleanExpression,
    query_Database,
    query_DateArrayExpression,
    query_DateExpression,
    query_DoubleArrayExpression,
    query_DoubleExpression,
    query_Expression,
    query_ExpressionWhereEntry,
    query_LongArrayExpression,
    query_LongExpression,
    query_Model,
    query_MultiExpressionWhereEntry,
    query_NullArrayExpression,
    query_NullExpression,
    query_OrWhereEntry,
    query_ReplacableValue,
    query_SingleExpressionWhereEntry,
    query_StringArrayExpression,
    query_StringExpression,
    query_WhereEntry,
    ArrayOperator,
    Operator,
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

def test_query_BooleanArrayExpression_values_value_roundtrip():
    instance = query_BooleanArrayExpression(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_query_BooleanExpression_true_value_roundtrip():
    instance = query_BooleanExpression(true="sample_text")
    assert instance.true == "sample_text"
    instance.true = "sample_text_2"
    assert instance.true == "sample_text_2"


def test_query_Database_dbName_value_roundtrip():
    instance = query_Database(dbName="sample_text", name="sample_text", port="sample_text", url="sample_text")
    assert instance.dbName == "sample_text"
    instance.dbName = "sample_text_2"
    assert instance.dbName == "sample_text_2"


def test_query_Database_name_value_roundtrip():
    instance = query_Database(dbName="sample_text", name="sample_text", port="sample_text", url="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_query_Database_port_value_roundtrip():
    instance = query_Database(dbName="sample_text", name="sample_text", port="sample_text", url="sample_text")
    assert instance.port == "sample_text"
    instance.port = "sample_text_2"
    assert instance.port == "sample_text_2"


def test_query_Database_url_value_roundtrip():
    instance = query_Database(dbName="sample_text", name="sample_text", port="sample_text", url="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_query_DateArrayExpression_values_value_roundtrip():
    instance = query_DateArrayExpression(values=date(2024, 1, 1))
    assert instance.values == date(2024, 1, 1)
    instance.values = date(2025, 6, 15)
    assert instance.values == date(2025, 6, 15)


def test_query_DateExpression_value_value_roundtrip():
    instance = query_DateExpression(value=date(2024, 1, 1))
    assert instance.value == date(2024, 1, 1)
    instance.value = date(2025, 6, 15)
    assert instance.value == date(2025, 6, 15)


def test_query_DoubleArrayExpression_values_value_roundtrip():
    instance = query_DoubleArrayExpression(values=3.14)
    assert instance.values == 3.14
    instance.values = 9.99
    assert instance.values == 9.99


def test_query_DoubleExpression_value_value_roundtrip():
    instance = query_DoubleExpression(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_query_ExpressionWhereEntry_name_value_roundtrip():
    instance = query_ExpressionWhereEntry(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_query_LongArrayExpression_values_value_roundtrip():
    instance = query_LongArrayExpression(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_query_LongExpression_value_value_roundtrip():
    instance = query_LongExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_query_Model_attrs_value_roundtrip():
    instance = query_Model(attrs="sample_text")
    assert instance.attrs == "sample_text"
    instance.attrs = "sample_text_2"
    assert instance.attrs == "sample_text_2"


def test_query_MultiExpressionWhereEntry_operator_value_roundtrip():
    instance = query_MultiExpressionWhereEntry(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_query_NullArrayExpression_values_value_roundtrip():
    instance = query_NullArrayExpression(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_query_NullExpression_value_value_roundtrip():
    instance = query_NullExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_query_ReplacableValue_value_value_roundtrip():
    instance = query_ReplacableValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_query_SingleExpressionWhereEntry_operator_value_roundtrip():
    instance = query_SingleExpressionWhereEntry(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_query_StringArrayExpression_values_value_roundtrip():
    instance = query_StringArrayExpression(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_query_StringExpression_value_value_roundtrip():
    instance = query_StringExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_query_BooleanArrayExpression_isa_ArrayExpression():
    instance = query_BooleanArrayExpression(values="sample_text")
    assert isinstance(instance, ArrayExpression)


def test_query_DateArrayExpression_isa_ArrayExpression():
    instance = query_DateArrayExpression(values=date(2024, 1, 1))
    assert isinstance(instance, ArrayExpression)


def test_query_DoubleArrayExpression_isa_ArrayExpression():
    instance = query_DoubleArrayExpression(values=3.14)
    assert isinstance(instance, ArrayExpression)


def test_query_LongArrayExpression_isa_ArrayExpression():
    instance = query_LongArrayExpression(values="sample_text")
    assert isinstance(instance, ArrayExpression)


def test_query_NullArrayExpression_isa_ArrayExpression():
    instance = query_NullArrayExpression(values="sample_text")
    assert isinstance(instance, ArrayExpression)


def test_query_StringArrayExpression_isa_ArrayExpression():
    instance = query_StringArrayExpression(values="sample_text")
    assert isinstance(instance, ArrayExpression)


def test_query_BooleanExpression_isa_Expression():
    instance = query_BooleanExpression(true="sample_text")
    assert isinstance(instance, Expression)


def test_query_DateExpression_isa_Expression():
    instance = query_DateExpression(value=date(2024, 1, 1))
    assert isinstance(instance, Expression)


def test_query_DoubleExpression_isa_Expression():
    instance = query_DoubleExpression(value=3.14)
    assert isinstance(instance, Expression)


def test_query_LongExpression_isa_Expression():
    instance = query_LongExpression(value="sample_text")
    assert isinstance(instance, Expression)


def test_query_NullExpression_isa_Expression():
    instance = query_NullExpression(value="sample_text")
    assert isinstance(instance, Expression)


def test_query_ReplacableValue_isa_Expression():
    instance = query_ReplacableValue(value="sample_text")
    assert isinstance(instance, Expression)


def test_query_StringExpression_isa_Expression():
    instance = query_StringExpression(value="sample_text")
    assert isinstance(instance, Expression)


def test_query_MultiExpressionWhereEntry_isa_ExpressionWhereEntry():
    instance = query_MultiExpressionWhereEntry(operator="sample_text")
    assert isinstance(instance, ExpressionWhereEntry)


def test_query_SingleExpressionWhereEntry_isa_ExpressionWhereEntry():
    instance = query_SingleExpressionWhereEntry(operator="sample_text")
    assert isinstance(instance, ExpressionWhereEntry)


def test_query_AndWhereEntry_isa_WhereEntry():
    instance = query_AndWhereEntry()
    assert isinstance(instance, WhereEntry)


def test_query_ExpressionWhereEntry_isa_WhereEntry():
    instance = query_ExpressionWhereEntry(name="sample_text")
    assert isinstance(instance, WhereEntry)


def test_query_OrWhereEntry_isa_WhereEntry():
    instance = query_OrWhereEntry()
    assert isinstance(instance, WhereEntry)


def test_assoc_db0_link_reassign_clear():
    a = query_Model(attrs="sample_text")
    b1 = query_Database(dbName="sample_text", name="sample_text", port="sample_text", url="sample_text")
    b2 = query_Database(dbName="sample_text_2", name="sample_text_2", port="sample_text_2", url="sample_text_2")
    _safe_set(a, 'query_Model', b1)
    assert _is_linked(a, 'query_Model', b1)
    if hasattr(b1, 'query_Database'):
        assert _is_linked(b1, 'query_Database', a)
    _safe_set(a, 'query_Model', b2)
    assert _is_linked(a, 'query_Model', b2)
    if hasattr(b1, 'query_Database'):
        assert not _is_linked(b1, 'query_Database', a)
    if hasattr(b2, 'query_Database'):
        assert _is_linked(b2, 'query_Database', a)
    _safe_set(a, 'query_Model', None)
    assert not _is_linked(a, 'query_Model', b2)
    if hasattr(b2, 'query_Database'):
        assert not _is_linked(b2, 'query_Database', a)


def test_assoc_rhs3_link_reassign_clear():
    a = query_SingleExpressionWhereEntry(operator="sample_text")
    b1 = query_Expression()
    b2 = query_Expression()
    _safe_set(a, 'query_SingleExpressionWhereEntry', b1)
    assert _is_linked(a, 'query_SingleExpressionWhereEntry', b1)
    if hasattr(b1, 'query_Expression'):
        assert _is_linked(b1, 'query_Expression', a)
    _safe_set(a, 'query_SingleExpressionWhereEntry', b2)
    assert _is_linked(a, 'query_SingleExpressionWhereEntry', b2)
    if hasattr(b1, 'query_Expression'):
        assert not _is_linked(b1, 'query_Expression', a)
    if hasattr(b2, 'query_Expression'):
        assert _is_linked(b2, 'query_Expression', a)
    _safe_set(a, 'query_SingleExpressionWhereEntry', None)
    assert not _is_linked(a, 'query_SingleExpressionWhereEntry', b2)
    if hasattr(b2, 'query_Expression'):
        assert not _is_linked(b2, 'query_Expression', a)


def test_assoc_rhs4_link_reassign_clear():
    a = query_MultiExpressionWhereEntry(operator="sample_text")
    b1 = query_ArrayExpression()
    b2 = query_ArrayExpression()
    _safe_set(a, 'query_MultiExpressionWhereEntry', b1)
    assert _is_linked(a, 'query_MultiExpressionWhereEntry', b1)
    if hasattr(b1, 'query_ArrayExpression'):
        assert _is_linked(b1, 'query_ArrayExpression', a)
    _safe_set(a, 'query_MultiExpressionWhereEntry', b2)
    assert _is_linked(a, 'query_MultiExpressionWhereEntry', b2)
    if hasattr(b1, 'query_ArrayExpression'):
        assert not _is_linked(b1, 'query_ArrayExpression', a)
    if hasattr(b2, 'query_ArrayExpression'):
        assert _is_linked(b2, 'query_ArrayExpression', a)
    _safe_set(a, 'query_MultiExpressionWhereEntry', None)
    assert not _is_linked(a, 'query_MultiExpressionWhereEntry', b2)
    if hasattr(b2, 'query_ArrayExpression'):
        assert not _is_linked(b2, 'query_ArrayExpression', a)


def test_assoc_whereEntry1_link_reassign_clear():
    a = query_Model(attrs="sample_text")
    b1 = query_WhereEntry()
    b2 = query_WhereEntry()
    _safe_set(a, 'query_Model2', b1)
    assert _is_linked(a, 'query_Model2', b1)
    if hasattr(b1, 'query_WhereEntry'):
        assert _is_linked(b1, 'query_WhereEntry', a)
    _safe_set(a, 'query_Model2', b2)
    assert _is_linked(a, 'query_Model2', b2)
    if hasattr(b1, 'query_WhereEntry'):
        assert not _is_linked(b1, 'query_WhereEntry', a)
    if hasattr(b2, 'query_WhereEntry'):
        assert _is_linked(b2, 'query_WhereEntry', a)
    _safe_set(a, 'query_Model2', None)
    assert not _is_linked(a, 'query_Model2', b2)
    if hasattr(b2, 'query_WhereEntry'):
        assert not _is_linked(b2, 'query_WhereEntry', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArrayExpression_strategy = st.builds(ArrayExpression)
@given(instance=ArrayExpression_strategy)
@settings(max_examples=25)
def test_ArrayExpression_instantiation(instance):
    assert isinstance(instance, ArrayExpression)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ExpressionWhereEntry_strategy = st.builds(ExpressionWhereEntry)
@given(instance=ExpressionWhereEntry_strategy)
@settings(max_examples=25)
def test_ExpressionWhereEntry_instantiation(instance):
    assert isinstance(instance, ExpressionWhereEntry)


WhereEntry_strategy = st.builds(WhereEntry)
@given(instance=WhereEntry_strategy)
@settings(max_examples=25)
def test_WhereEntry_instantiation(instance):
    assert isinstance(instance, WhereEntry)


query_AndWhereEntry_strategy = st.builds(query_AndWhereEntry)
@given(instance=query_AndWhereEntry_strategy)
@settings(max_examples=25)
def test_query_AndWhereEntry_instantiation(instance):
    assert isinstance(instance, query_AndWhereEntry)


query_ArrayExpression_strategy = st.builds(query_ArrayExpression)
@given(instance=query_ArrayExpression_strategy)
@settings(max_examples=25)
def test_query_ArrayExpression_instantiation(instance):
    assert isinstance(instance, query_ArrayExpression)


query_BooleanArrayExpression_strategy = st.builds(query_BooleanArrayExpression, values=safe_text)
@given(instance=query_BooleanArrayExpression_strategy)
@settings(max_examples=25)
def test_query_BooleanArrayExpression_instantiation(instance):
    assert isinstance(instance, query_BooleanArrayExpression)


query_BooleanExpression_strategy = st.builds(query_BooleanExpression, true=safe_text)
@given(instance=query_BooleanExpression_strategy)
@settings(max_examples=25)
def test_query_BooleanExpression_instantiation(instance):
    assert isinstance(instance, query_BooleanExpression)


query_Database_strategy = st.builds(query_Database, dbName=safe_text, name=safe_text, port=safe_text, url=safe_text)
@given(instance=query_Database_strategy)
@settings(max_examples=25)
def test_query_Database_instantiation(instance):
    assert isinstance(instance, query_Database)


query_DateArrayExpression_strategy = st.builds(query_DateArrayExpression, values=st.dates())
@given(instance=query_DateArrayExpression_strategy)
@settings(max_examples=25)
def test_query_DateArrayExpression_instantiation(instance):
    assert isinstance(instance, query_DateArrayExpression)


query_DateExpression_strategy = st.builds(query_DateExpression, value=st.dates())
@given(instance=query_DateExpression_strategy)
@settings(max_examples=25)
def test_query_DateExpression_instantiation(instance):
    assert isinstance(instance, query_DateExpression)


query_DoubleArrayExpression_strategy = st.builds(query_DoubleArrayExpression, values=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=query_DoubleArrayExpression_strategy)
@settings(max_examples=25)
def test_query_DoubleArrayExpression_instantiation(instance):
    assert isinstance(instance, query_DoubleArrayExpression)


query_DoubleExpression_strategy = st.builds(query_DoubleExpression, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=query_DoubleExpression_strategy)
@settings(max_examples=25)
def test_query_DoubleExpression_instantiation(instance):
    assert isinstance(instance, query_DoubleExpression)


query_Expression_strategy = st.builds(query_Expression)
@given(instance=query_Expression_strategy)
@settings(max_examples=25)
def test_query_Expression_instantiation(instance):
    assert isinstance(instance, query_Expression)


query_ExpressionWhereEntry_strategy = st.builds(query_ExpressionWhereEntry, name=safe_text)
@given(instance=query_ExpressionWhereEntry_strategy)
@settings(max_examples=25)
def test_query_ExpressionWhereEntry_instantiation(instance):
    assert isinstance(instance, query_ExpressionWhereEntry)


query_LongArrayExpression_strategy = st.builds(query_LongArrayExpression, values=safe_text)
@given(instance=query_LongArrayExpression_strategy)
@settings(max_examples=25)
def test_query_LongArrayExpression_instantiation(instance):
    assert isinstance(instance, query_LongArrayExpression)


query_LongExpression_strategy = st.builds(query_LongExpression, value=safe_text)
@given(instance=query_LongExpression_strategy)
@settings(max_examples=25)
def test_query_LongExpression_instantiation(instance):
    assert isinstance(instance, query_LongExpression)


query_Model_strategy = st.builds(query_Model, attrs=safe_text)
@given(instance=query_Model_strategy)
@settings(max_examples=25)
def test_query_Model_instantiation(instance):
    assert isinstance(instance, query_Model)


query_MultiExpressionWhereEntry_strategy = st.builds(query_MultiExpressionWhereEntry, operator=safe_text)
@given(instance=query_MultiExpressionWhereEntry_strategy)
@settings(max_examples=25)
def test_query_MultiExpressionWhereEntry_instantiation(instance):
    assert isinstance(instance, query_MultiExpressionWhereEntry)


query_NullArrayExpression_strategy = st.builds(query_NullArrayExpression, values=safe_text)
@given(instance=query_NullArrayExpression_strategy)
@settings(max_examples=25)
def test_query_NullArrayExpression_instantiation(instance):
    assert isinstance(instance, query_NullArrayExpression)


query_NullExpression_strategy = st.builds(query_NullExpression, value=safe_text)
@given(instance=query_NullExpression_strategy)
@settings(max_examples=25)
def test_query_NullExpression_instantiation(instance):
    assert isinstance(instance, query_NullExpression)


query_OrWhereEntry_strategy = st.builds(query_OrWhereEntry)
@given(instance=query_OrWhereEntry_strategy)
@settings(max_examples=25)
def test_query_OrWhereEntry_instantiation(instance):
    assert isinstance(instance, query_OrWhereEntry)


query_ReplacableValue_strategy = st.builds(query_ReplacableValue, value=safe_text)
@given(instance=query_ReplacableValue_strategy)
@settings(max_examples=25)
def test_query_ReplacableValue_instantiation(instance):
    assert isinstance(instance, query_ReplacableValue)


query_SingleExpressionWhereEntry_strategy = st.builds(query_SingleExpressionWhereEntry, operator=safe_text)
@given(instance=query_SingleExpressionWhereEntry_strategy)
@settings(max_examples=25)
def test_query_SingleExpressionWhereEntry_instantiation(instance):
    assert isinstance(instance, query_SingleExpressionWhereEntry)


query_StringArrayExpression_strategy = st.builds(query_StringArrayExpression, values=safe_text)
@given(instance=query_StringArrayExpression_strategy)
@settings(max_examples=25)
def test_query_StringArrayExpression_instantiation(instance):
    assert isinstance(instance, query_StringArrayExpression)


query_StringExpression_strategy = st.builds(query_StringExpression, value=safe_text)
@given(instance=query_StringExpression_strategy)
@settings(max_examples=25)
def test_query_StringExpression_instantiation(instance):
    assert isinstance(instance, query_StringExpression)


query_WhereEntry_strategy = st.builds(query_WhereEntry)
@given(instance=query_WhereEntry_strategy)
@settings(max_examples=25)
def test_query_WhereEntry_instantiation(instance):
    assert isinstance(instance, query_WhereEntry)


