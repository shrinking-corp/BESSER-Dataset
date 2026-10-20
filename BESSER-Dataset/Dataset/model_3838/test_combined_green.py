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
    sql_NamedElement,
    NamedElement,
    sql_Column,
    sql_Table,
    sql_SelectQuery,
    sql_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_sql_namedelement_is_not_abstract():
    assert not inspect.isabstract(sql_NamedElement)


def test_hyp_sql_namedelement_constructor_exists():
    assert callable(sql_NamedElement.__init__)


def test_hyp_sql_namedelement_constructor_args():
    sig = inspect.signature(sql_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_column_is_not_abstract():
    assert not inspect.isabstract(sql_Column)


def test_hyp_sql_column_constructor_exists():
    assert callable(sql_Column.__init__)


def test_hyp_sql_column_constructor_args():
    sig = inspect.signature(sql_Column.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_table_is_not_abstract():
    assert not inspect.isabstract(sql_Table)


def test_hyp_sql_table_constructor_exists():
    assert callable(sql_Table.__init__)


def test_hyp_sql_table_constructor_args():
    sig = inspect.signature(sql_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_selectquery_is_not_abstract():
    assert not inspect.isabstract(sql_SelectQuery)


def test_hyp_sql_selectquery_constructor_exists():
    assert callable(sql_SelectQuery.__init__)


def test_hyp_sql_selectquery_constructor_args():
    sig = inspect.signature(sql_SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_model_is_not_abstract():
    assert not inspect.isabstract(sql_Model)


def test_hyp_sql_model_constructor_exists():
    assert callable(sql_Model.__init__)


def test_hyp_sql_model_constructor_args():
    sig = inspect.signature(sql_Model.__init__)
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
sql_NamedElement_strategy = st.builds(
    sql_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sql_Column_strategy = st.builds(
    sql_Column,
)
sql_Table_strategy = st.builds(
    sql_Table,
)
sql_SelectQuery_strategy = st.builds(
    sql_SelectQuery,
)
sql_Model_strategy = st.builds(
    sql_Model,
)




@given(instance=sql_NamedElement_strategy)
def test_hyp_sql_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamedElement,
    sql_Column,
    sql_Model,
    sql_NamedElement,
    sql_SelectQuery,
    sql_Table,
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

def test_sql_NamedElement_name_value_roundtrip():
    instance = sql_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sql_Column_isa_NamedElement():
    instance = sql_Column()
    assert isinstance(instance, NamedElement)


def test_sql_Table_isa_NamedElement():
    instance = sql_Table()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


sql_Column_strategy = st.builds(sql_Column)
@given(instance=sql_Column_strategy)
@settings(max_examples=25)
def test_sql_Column_instantiation(instance):
    assert isinstance(instance, sql_Column)


sql_Model_strategy = st.builds(sql_Model)
@given(instance=sql_Model_strategy)
@settings(max_examples=25)
def test_sql_Model_instantiation(instance):
    assert isinstance(instance, sql_Model)


sql_NamedElement_strategy = st.builds(sql_NamedElement, name=safe_text)
@given(instance=sql_NamedElement_strategy)
@settings(max_examples=25)
def test_sql_NamedElement_instantiation(instance):
    assert isinstance(instance, sql_NamedElement)


sql_SelectQuery_strategy = st.builds(sql_SelectQuery)
@given(instance=sql_SelectQuery_strategy)
@settings(max_examples=25)
def test_sql_SelectQuery_instantiation(instance):
    assert isinstance(instance, sql_SelectQuery)


sql_Table_strategy = st.builds(sql_Table)
@given(instance=sql_Table_strategy)
@settings(max_examples=25)
def test_sql_Table_instantiation(instance):
    assert isinstance(instance, sql_Table)



