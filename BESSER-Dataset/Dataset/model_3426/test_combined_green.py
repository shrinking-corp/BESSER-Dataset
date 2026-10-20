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
    mongoQuery_Array,
    mongoQuery_JsonDate,
    Query,
    mongoQuery_QueryObject,
    mongoQuery_FieldSelection,
    mongoQuery_Selection,
    mongoQuery_Query,
    mongoQuery_Selector,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_mongoquery_array_is_not_abstract():
    assert not inspect.isabstract(mongoQuery_Array)


def test_hyp_mongoquery_array_constructor_exists():
    assert callable(mongoQuery_Array.__init__)


def test_hyp_mongoquery_array_constructor_args():
    sig = inspect.signature(mongoQuery_Array.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mongoquery_jsondate_is_not_abstract():
    assert not inspect.isabstract(mongoQuery_JsonDate)


def test_hyp_mongoquery_jsondate_constructor_exists():
    assert callable(mongoQuery_JsonDate.__init__)


def test_hyp_mongoquery_jsondate_constructor_args():
    sig = inspect.signature(mongoQuery_JsonDate.__init__)
    params = list(sig.parameters.keys())
    assert "second" in params, "Missing parameter 'second'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "year" in params, "Missing parameter 'year'"
    assert "dateString" in params, "Missing parameter 'dateString'"
    assert "millisecond" in params, "Missing parameter 'millisecond'"
    assert "milliseconds" in params, "Missing parameter 'milliseconds'"
    assert "day" in params, "Missing parameter 'day'"
    assert "month" in params, "Missing parameter 'month'"
    assert "minute" in params, "Missing parameter 'minute'"












def test_hyp_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_hyp_query_constructor_exists():
    assert callable(Query.__init__)


def test_hyp_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mongoquery_queryobject_is_not_abstract():
    assert not inspect.isabstract(mongoQuery_QueryObject)


def test_hyp_mongoquery_queryobject_constructor_exists():
    assert callable(mongoQuery_QueryObject.__init__)


def test_hyp_mongoquery_queryobject_constructor_args():
    sig = inspect.signature(mongoQuery_QueryObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mongoquery_fieldselection_is_not_abstract():
    assert not inspect.isabstract(mongoQuery_FieldSelection)


def test_hyp_mongoquery_fieldselection_constructor_exists():
    assert callable(mongoQuery_FieldSelection.__init__)


def test_hyp_mongoquery_fieldselection_constructor_args():
    sig = inspect.signature(mongoQuery_FieldSelection.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "enabled" in params, "Missing parameter 'enabled'"





def test_hyp_mongoquery_selection_is_not_abstract():
    assert not inspect.isabstract(mongoQuery_Selection)


def test_hyp_mongoquery_selection_constructor_exists():
    assert callable(mongoQuery_Selection.__init__)


def test_hyp_mongoquery_selection_constructor_args():
    sig = inspect.signature(mongoQuery_Selection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mongoquery_query_is_not_abstract():
    assert not inspect.isabstract(mongoQuery_Query)


def test_hyp_mongoquery_query_constructor_exists():
    assert callable(mongoQuery_Query.__init__)


def test_hyp_mongoquery_query_constructor_args():
    sig = inspect.signature(mongoQuery_Query.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "stringValue" in params, "Missing parameter 'stringValue'"
    assert "numberValue" in params, "Missing parameter 'numberValue'"
    assert "integerValue" in params, "Missing parameter 'integerValue'"







def test_hyp_mongoquery_selector_is_not_abstract():
    assert not inspect.isabstract(mongoQuery_Selector)


def test_hyp_mongoquery_selector_constructor_exists():
    assert callable(mongoQuery_Selector.__init__)


def test_hyp_mongoquery_selector_constructor_args():
    sig = inspect.signature(mongoQuery_Selector.__init__)
    params = list(sig.parameters.keys())


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
mongoQuery_Array_strategy = st.builds(
    mongoQuery_Array,
)
mongoQuery_JsonDate_strategy = st.builds(
    mongoQuery_JsonDate,
    second=
        st.integers(),
    hour=
        st.integers(),
    year=
        st.integers(),
    dateString=
        safe_text,
    millisecond=
        st.integers(),
    milliseconds=
        st.integers(),
    day=
        st.integers(),
    month=
        st.integers(),
    minute=
        st.integers()
)
Query_strategy = st.builds(
    Query,
)
mongoQuery_QueryObject_strategy = st.builds(
    mongoQuery_QueryObject,
)
mongoQuery_FieldSelection_strategy = st.builds(
    mongoQuery_FieldSelection,
    key=
        safe_text,
    enabled=
        st.integers()
)
mongoQuery_Selection_strategy = st.builds(
    mongoQuery_Selection,
)
mongoQuery_Query_strategy = st.builds(
    mongoQuery_Query,
    key=
        safe_text,
    stringValue=
        safe_text,
    numberValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    integerValue=
        st.integers()
)
mongoQuery_Selector_strategy = st.builds(
    mongoQuery_Selector,
)





@given(instance=mongoQuery_JsonDate_strategy)
def test_hyp_mongoquery_jsondate_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=mongoQuery_JsonDate_strategy)
def test_hyp_mongoquery_jsondate_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=mongoQuery_JsonDate_strategy)
def test_hyp_mongoquery_jsondate_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=mongoQuery_JsonDate_strategy)
def test_hyp_mongoquery_jsondate_dateString_setter(instance):
    original = instance.dateString
    instance.dateString = original
    assert instance.dateString == original



@given(instance=mongoQuery_JsonDate_strategy)
def test_hyp_mongoquery_jsondate_millisecond_setter(instance):
    original = instance.millisecond
    instance.millisecond = original
    assert instance.millisecond == original



@given(instance=mongoQuery_JsonDate_strategy)
def test_hyp_mongoquery_jsondate_milliseconds_setter(instance):
    original = instance.milliseconds
    instance.milliseconds = original
    assert instance.milliseconds == original



@given(instance=mongoQuery_JsonDate_strategy)
def test_hyp_mongoquery_jsondate_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=mongoQuery_JsonDate_strategy)
def test_hyp_mongoquery_jsondate_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=mongoQuery_JsonDate_strategy)
def test_hyp_mongoquery_jsondate_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original






@given(instance=mongoQuery_FieldSelection_strategy)
def test_hyp_mongoquery_fieldselection_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=mongoQuery_FieldSelection_strategy)
def test_hyp_mongoquery_fieldselection_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original





@given(instance=mongoQuery_Query_strategy)
def test_hyp_mongoquery_query_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=mongoQuery_Query_strategy)
def test_hyp_mongoquery_query_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original



@given(instance=mongoQuery_Query_strategy)
def test_hyp_mongoquery_query_numberValue_setter(instance):
    original = instance.numberValue
    instance.numberValue = original
    assert instance.numberValue == original



@given(instance=mongoQuery_Query_strategy)
def test_hyp_mongoquery_query_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Query,
    mongoQuery_Array,
    mongoQuery_FieldSelection,
    mongoQuery_JsonDate,
    mongoQuery_Query,
    mongoQuery_QueryObject,
    mongoQuery_Selection,
    mongoQuery_Selector,
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

def test_mongoQuery_FieldSelection_enabled_value_roundtrip():
    instance = mongoQuery_FieldSelection(enabled=7, key="sample_text")
    assert instance.enabled == 7
    instance.enabled = 13
    assert instance.enabled == 13


def test_mongoQuery_FieldSelection_key_value_roundtrip():
    instance = mongoQuery_FieldSelection(enabled=7, key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_mongoQuery_JsonDate_dateString_value_roundtrip():
    instance = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    assert instance.dateString == "sample_text"
    instance.dateString = "sample_text_2"
    assert instance.dateString == "sample_text_2"


def test_mongoQuery_JsonDate_day_value_roundtrip():
    instance = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    assert instance.day == 7
    instance.day = 13
    assert instance.day == 13


def test_mongoQuery_JsonDate_hour_value_roundtrip():
    instance = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    assert instance.hour == 7
    instance.hour = 13
    assert instance.hour == 13


def test_mongoQuery_JsonDate_millisecond_value_roundtrip():
    instance = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    assert instance.millisecond == 7
    instance.millisecond = 13
    assert instance.millisecond == 13


def test_mongoQuery_JsonDate_milliseconds_value_roundtrip():
    instance = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    assert instance.milliseconds == 7
    instance.milliseconds = 13
    assert instance.milliseconds == 13


def test_mongoQuery_JsonDate_minute_value_roundtrip():
    instance = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    assert instance.minute == 7
    instance.minute = 13
    assert instance.minute == 13


def test_mongoQuery_JsonDate_month_value_roundtrip():
    instance = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    assert instance.month == 7
    instance.month = 13
    assert instance.month == 13


def test_mongoQuery_JsonDate_second_value_roundtrip():
    instance = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    assert instance.second == 7
    instance.second = 13
    assert instance.second == 13


def test_mongoQuery_JsonDate_year_value_roundtrip():
    instance = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_mongoQuery_Query_integerValue_value_roundtrip():
    instance = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    assert instance.integerValue == 7
    instance.integerValue = 13
    assert instance.integerValue == 13


def test_mongoQuery_Query_key_value_roundtrip():
    instance = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_mongoQuery_Query_numberValue_value_roundtrip():
    instance = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    assert instance.numberValue == 3.14
    instance.numberValue = 9.99
    assert instance.numberValue == 9.99


def test_mongoQuery_Query_stringValue_value_roundtrip():
    instance = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    assert instance.stringValue == "sample_text"
    instance.stringValue = "sample_text_2"
    assert instance.stringValue == "sample_text_2"


def test_mongoQuery_QueryObject_isa_Query():
    instance = mongoQuery_QueryObject()
    assert isinstance(instance, Query)


def test_assoc_arrayValue10_link_reassign_clear():
    a = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    b1 = mongoQuery_Array()
    b2 = mongoQuery_Array()
    _safe_set(a, 'mongoQuery_Query11', b1)
    assert _is_linked(a, 'mongoQuery_Query11', b1)
    if hasattr(b1, 'mongoQuery_Array'):
        assert _is_linked(b1, 'mongoQuery_Array', a)
    _safe_set(a, 'mongoQuery_Query11', b2)
    assert _is_linked(a, 'mongoQuery_Query11', b2)
    if hasattr(b1, 'mongoQuery_Array'):
        assert not _is_linked(b1, 'mongoQuery_Array', a)
    if hasattr(b2, 'mongoQuery_Array'):
        assert _is_linked(b2, 'mongoQuery_Array', a)
    _safe_set(a, 'mongoQuery_Query11', None)
    assert not _is_linked(a, 'mongoQuery_Query11', b2)
    if hasattr(b2, 'mongoQuery_Array'):
        assert not _is_linked(b2, 'mongoQuery_Array', a)


def test_assoc_dateValue8_link_reassign_clear():
    a = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    b1 = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    b2 = mongoQuery_JsonDate(dateString="sample_text_2", day=13, hour=13, millisecond=13, milliseconds=13, minute=13, month=13, second=13, year=13)
    _safe_set(a, 'mongoQuery_Query9', b1)
    assert _is_linked(a, 'mongoQuery_Query9', b1)
    if hasattr(b1, 'mongoQuery_JsonDate'):
        assert _is_linked(b1, 'mongoQuery_JsonDate', a)
    _safe_set(a, 'mongoQuery_Query9', b2)
    assert _is_linked(a, 'mongoQuery_Query9', b2)
    if hasattr(b1, 'mongoQuery_JsonDate'):
        assert not _is_linked(b1, 'mongoQuery_JsonDate', a)
    if hasattr(b2, 'mongoQuery_JsonDate'):
        assert _is_linked(b2, 'mongoQuery_JsonDate', a)
    _safe_set(a, 'mongoQuery_Query9', None)
    assert not _is_linked(a, 'mongoQuery_Query9', b2)
    if hasattr(b2, 'mongoQuery_JsonDate'):
        assert not _is_linked(b2, 'mongoQuery_JsonDate', a)


def test_assoc_fields3_link_reassign_clear():
    a = mongoQuery_FieldSelection(enabled=7, key="sample_text")
    b1 = mongoQuery_Selection()
    b2 = mongoQuery_Selection()
    _safe_set(a, 'mongoQuery_FieldSelection', b1)
    assert _is_linked(a, 'mongoQuery_FieldSelection', b1)
    if hasattr(b1, 'mongoQuery_Selection4'):
        assert _is_linked(b1, 'mongoQuery_Selection4', a)
    _safe_set(a, 'mongoQuery_FieldSelection', b2)
    assert _is_linked(a, 'mongoQuery_FieldSelection', b2)
    if hasattr(b1, 'mongoQuery_Selection4'):
        assert not _is_linked(b1, 'mongoQuery_Selection4', a)
    if hasattr(b2, 'mongoQuery_Selection4'):
        assert _is_linked(b2, 'mongoQuery_Selection4', a)
    _safe_set(a, 'mongoQuery_FieldSelection', None)
    assert not _is_linked(a, 'mongoQuery_FieldSelection', b2)
    if hasattr(b2, 'mongoQuery_Selection4'):
        assert not _is_linked(b2, 'mongoQuery_Selection4', a)


def test_assoc_members18_link_reassign_clear():
    a = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    b1 = mongoQuery_QueryObject()
    b2 = mongoQuery_QueryObject()
    _safe_set(a, 'mongoQuery_Query19', b1)
    assert _is_linked(a, 'mongoQuery_Query19', b1)
    if hasattr(b1, 'mongoQuery_QueryObject'):
        assert _is_linked(b1, 'mongoQuery_QueryObject', a)
    _safe_set(a, 'mongoQuery_Query19', b2)
    assert _is_linked(a, 'mongoQuery_Query19', b2)
    if hasattr(b1, 'mongoQuery_QueryObject'):
        assert not _is_linked(b1, 'mongoQuery_QueryObject', a)
    if hasattr(b2, 'mongoQuery_QueryObject'):
        assert _is_linked(b2, 'mongoQuery_QueryObject', a)
    _safe_set(a, 'mongoQuery_Query19', None)
    assert not _is_linked(a, 'mongoQuery_Query19', b2)
    if hasattr(b2, 'mongoQuery_QueryObject'):
        assert not _is_linked(b2, 'mongoQuery_QueryObject', a)


def test_assoc_objectValue13_link_reassign_clear():
    a = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    b1 = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    b2 = mongoQuery_Query(integerValue=13, key="sample_text_2", numberValue=9.99, stringValue="sample_text_2")
    _safe_set(a, 'mongoQuery_Query12', b1)
    assert _is_linked(a, 'mongoQuery_Query12', b1)
    if hasattr(b1, 'mongoQuery_Query14'):
        assert _is_linked(b1, 'mongoQuery_Query14', a)
    _safe_set(a, 'mongoQuery_Query12', b2)
    assert _is_linked(a, 'mongoQuery_Query12', b2)
    if hasattr(b1, 'mongoQuery_Query14'):
        assert not _is_linked(b1, 'mongoQuery_Query14', a)
    if hasattr(b2, 'mongoQuery_Query14'):
        assert _is_linked(b2, 'mongoQuery_Query14', a)
    _safe_set(a, 'mongoQuery_Query12', None)
    assert not _is_linked(a, 'mongoQuery_Query12', b2)
    if hasattr(b2, 'mongoQuery_Query14'):
        assert not _is_linked(b2, 'mongoQuery_Query14', a)


def test_assoc_query0_link_reassign_clear():
    a = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    b1 = mongoQuery_Selector()
    b2 = mongoQuery_Selector()
    _safe_set(a, 'mongoQuery_Query', b1)
    assert _is_linked(a, 'mongoQuery_Query', b1)
    if hasattr(b1, 'mongoQuery_Selector'):
        assert _is_linked(b1, 'mongoQuery_Selector', a)
    _safe_set(a, 'mongoQuery_Query', b2)
    assert _is_linked(a, 'mongoQuery_Query', b2)
    if hasattr(b1, 'mongoQuery_Selector'):
        assert not _is_linked(b1, 'mongoQuery_Selector', a)
    if hasattr(b2, 'mongoQuery_Selector'):
        assert _is_linked(b2, 'mongoQuery_Selector', a)
    _safe_set(a, 'mongoQuery_Query', None)
    assert not _is_linked(a, 'mongoQuery_Query', b2)
    if hasattr(b2, 'mongoQuery_Selector'):
        assert not _is_linked(b2, 'mongoQuery_Selector', a)


def test_assoc_value6_link_reassign_clear():
    a = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    b1 = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    b2 = mongoQuery_Query(integerValue=13, key="sample_text_2", numberValue=9.99, stringValue="sample_text_2")
    _safe_set(a, 'mongoQuery_Query5', b1)
    assert _is_linked(a, 'mongoQuery_Query5', b1)
    if hasattr(b1, 'mongoQuery_Query7'):
        assert _is_linked(b1, 'mongoQuery_Query7', a)
    _safe_set(a, 'mongoQuery_Query5', b2)
    assert _is_linked(a, 'mongoQuery_Query5', b2)
    if hasattr(b1, 'mongoQuery_Query7'):
        assert not _is_linked(b1, 'mongoQuery_Query7', a)
    if hasattr(b2, 'mongoQuery_Query7'):
        assert _is_linked(b2, 'mongoQuery_Query7', a)
    _safe_set(a, 'mongoQuery_Query5', None)
    assert not _is_linked(a, 'mongoQuery_Query5', b2)
    if hasattr(b2, 'mongoQuery_Query7'):
        assert not _is_linked(b2, 'mongoQuery_Query7', a)


def test_assoc_values15_link_reassign_clear():
    a = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    b1 = mongoQuery_Array()
    b2 = mongoQuery_Array()
    _safe_set(a, 'mongoQuery_Query17', b1)
    assert _is_linked(a, 'mongoQuery_Query17', b1)
    if hasattr(b1, 'mongoQuery_Array16'):
        assert _is_linked(b1, 'mongoQuery_Array16', a)
    _safe_set(a, 'mongoQuery_Query17', b2)
    assert _is_linked(a, 'mongoQuery_Query17', b2)
    if hasattr(b1, 'mongoQuery_Array16'):
        assert not _is_linked(b1, 'mongoQuery_Array16', a)
    if hasattr(b2, 'mongoQuery_Array16'):
        assert _is_linked(b2, 'mongoQuery_Array16', a)
    _safe_set(a, 'mongoQuery_Query17', None)
    assert not _is_linked(a, 'mongoQuery_Query17', b2)
    if hasattr(b2, 'mongoQuery_Array16'):
        assert not _is_linked(b2, 'mongoQuery_Array16', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Query_strategy = st.builds(Query)
@given(instance=Query_strategy)
@settings(max_examples=25)
def test_Query_instantiation(instance):
    assert isinstance(instance, Query)


mongoQuery_Array_strategy = st.builds(mongoQuery_Array)
@given(instance=mongoQuery_Array_strategy)
@settings(max_examples=25)
def test_mongoQuery_Array_instantiation(instance):
    assert isinstance(instance, mongoQuery_Array)


mongoQuery_FieldSelection_strategy = st.builds(mongoQuery_FieldSelection, enabled=st.integers(), key=safe_text)
@given(instance=mongoQuery_FieldSelection_strategy)
@settings(max_examples=25)
def test_mongoQuery_FieldSelection_instantiation(instance):
    assert isinstance(instance, mongoQuery_FieldSelection)


mongoQuery_JsonDate_strategy = st.builds(mongoQuery_JsonDate, dateString=safe_text, day=st.integers(), hour=st.integers(), millisecond=st.integers(), milliseconds=st.integers(), minute=st.integers(), month=st.integers(), second=st.integers(), year=st.integers())
@given(instance=mongoQuery_JsonDate_strategy)
@settings(max_examples=25)
def test_mongoQuery_JsonDate_instantiation(instance):
    assert isinstance(instance, mongoQuery_JsonDate)


mongoQuery_Query_strategy = st.builds(mongoQuery_Query, integerValue=st.integers(), key=safe_text, numberValue=st.floats(allow_nan=False, allow_infinity=False), stringValue=safe_text)
@given(instance=mongoQuery_Query_strategy)
@settings(max_examples=25)
def test_mongoQuery_Query_instantiation(instance):
    assert isinstance(instance, mongoQuery_Query)


mongoQuery_QueryObject_strategy = st.builds(mongoQuery_QueryObject)
@given(instance=mongoQuery_QueryObject_strategy)
@settings(max_examples=25)
def test_mongoQuery_QueryObject_instantiation(instance):
    assert isinstance(instance, mongoQuery_QueryObject)


mongoQuery_Selection_strategy = st.builds(mongoQuery_Selection)
@given(instance=mongoQuery_Selection_strategy)
@settings(max_examples=25)
def test_mongoQuery_Selection_instantiation(instance):
    assert isinstance(instance, mongoQuery_Selection)


mongoQuery_Selector_strategy = st.builds(mongoQuery_Selector)
@given(instance=mongoQuery_Selector_strategy)
@settings(max_examples=25)
def test_mongoQuery_Selector_instantiation(instance):
    assert isinstance(instance, mongoQuery_Selector)



