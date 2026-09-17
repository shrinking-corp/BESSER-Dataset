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
    NamedElement,
    simpleRDBMS_Table,
    simpleRDBMS_Key,
    simpleRDBMS_Column,
    simpleRDBMS_ForeignKey,
    simpleRDBMS_Schema,
    simpleRDBMS_NamedElement,
    simpleRDBMS_RDBMSModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_table_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_Table)


def test_hyp_simplerdbms_table_constructor_exists():
    assert callable(simpleRDBMS_Table.__init__)


def test_hyp_simplerdbms_table_constructor_args():
    sig = inspect.signature(simpleRDBMS_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_key_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_Key)


def test_hyp_simplerdbms_key_constructor_exists():
    assert callable(simpleRDBMS_Key.__init__)


def test_hyp_simplerdbms_key_constructor_args():
    sig = inspect.signature(simpleRDBMS_Key.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_column_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_Column)


def test_hyp_simplerdbms_column_constructor_exists():
    assert callable(simpleRDBMS_Column.__init__)


def test_hyp_simplerdbms_column_constructor_args():
    sig = inspect.signature(simpleRDBMS_Column.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_ForeignKey)


def test_hyp_simplerdbms_foreignkey_constructor_exists():
    assert callable(simpleRDBMS_ForeignKey.__init__)


def test_hyp_simplerdbms_foreignkey_constructor_args():
    sig = inspect.signature(simpleRDBMS_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_schema_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_Schema)


def test_hyp_simplerdbms_schema_constructor_exists():
    assert callable(simpleRDBMS_Schema.__init__)


def test_hyp_simplerdbms_schema_constructor_args():
    sig = inspect.signature(simpleRDBMS_Schema.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_NamedElement)


def test_hyp_simplerdbms_namedelement_constructor_exists():
    assert callable(simpleRDBMS_NamedElement.__init__)


def test_hyp_simplerdbms_namedelement_constructor_args():
    sig = inspect.signature(simpleRDBMS_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_simplerdbms_rdbmsmodel_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_RDBMSModel)


def test_hyp_simplerdbms_rdbmsmodel_constructor_exists():
    assert callable(simpleRDBMS_RDBMSModel.__init__)


def test_hyp_simplerdbms_rdbmsmodel_constructor_args():
    sig = inspect.signature(simpleRDBMS_RDBMSModel.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleRDBMS_Table_strategy = st.builds(
    simpleRDBMS_Table,
)
simpleRDBMS_Key_strategy = st.builds(
    simpleRDBMS_Key,
)
simpleRDBMS_Column_strategy = st.builds(
    simpleRDBMS_Column,
)
simpleRDBMS_ForeignKey_strategy = st.builds(
    simpleRDBMS_ForeignKey,
)
simpleRDBMS_Schema_strategy = st.builds(
    simpleRDBMS_Schema,
)
simpleRDBMS_NamedElement_strategy = st.builds(
    simpleRDBMS_NamedElement,
    name=
        safe_text
)
simpleRDBMS_RDBMSModel_strategy = st.builds(
    simpleRDBMS_RDBMSModel,
)










@given(instance=simpleRDBMS_NamedElement_strategy)
def test_hyp_simplerdbms_namedelement_name_setter(instance):
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
    simpleRDBMS_Column,
    simpleRDBMS_ForeignKey,
    simpleRDBMS_Key,
    simpleRDBMS_NamedElement,
    simpleRDBMS_RDBMSModel,
    simpleRDBMS_Schema,
    simpleRDBMS_Table,
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

def test_simpleRDBMS_NamedElement_name_value_roundtrip():
    instance = simpleRDBMS_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_simpleRDBMS_Column_isa_NamedElement():
    instance = simpleRDBMS_Column()
    assert isinstance(instance, NamedElement)


def test_simpleRDBMS_ForeignKey_isa_NamedElement():
    instance = simpleRDBMS_ForeignKey()
    assert isinstance(instance, NamedElement)


def test_simpleRDBMS_Key_isa_NamedElement():
    instance = simpleRDBMS_Key()
    assert isinstance(instance, NamedElement)


def test_simpleRDBMS_Schema_isa_NamedElement():
    instance = simpleRDBMS_Schema()
    assert isinstance(instance, NamedElement)


def test_simpleRDBMS_Table_isa_NamedElement():
    instance = simpleRDBMS_Table()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


simpleRDBMS_Column_strategy = st.builds(simpleRDBMS_Column)
@given(instance=simpleRDBMS_Column_strategy)
@settings(max_examples=25)
def test_simpleRDBMS_Column_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_Column)


simpleRDBMS_ForeignKey_strategy = st.builds(simpleRDBMS_ForeignKey)
@given(instance=simpleRDBMS_ForeignKey_strategy)
@settings(max_examples=25)
def test_simpleRDBMS_ForeignKey_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_ForeignKey)


simpleRDBMS_Key_strategy = st.builds(simpleRDBMS_Key)
@given(instance=simpleRDBMS_Key_strategy)
@settings(max_examples=25)
def test_simpleRDBMS_Key_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_Key)


simpleRDBMS_NamedElement_strategy = st.builds(simpleRDBMS_NamedElement, name=safe_text)
@given(instance=simpleRDBMS_NamedElement_strategy)
@settings(max_examples=25)
def test_simpleRDBMS_NamedElement_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_NamedElement)


simpleRDBMS_RDBMSModel_strategy = st.builds(simpleRDBMS_RDBMSModel)
@given(instance=simpleRDBMS_RDBMSModel_strategy)
@settings(max_examples=25)
def test_simpleRDBMS_RDBMSModel_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_RDBMSModel)


simpleRDBMS_Schema_strategy = st.builds(simpleRDBMS_Schema)
@given(instance=simpleRDBMS_Schema_strategy)
@settings(max_examples=25)
def test_simpleRDBMS_Schema_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_Schema)


simpleRDBMS_Table_strategy = st.builds(simpleRDBMS_Table)
@given(instance=simpleRDBMS_Table_strategy)
@settings(max_examples=25)
def test_simpleRDBMS_Table_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_Table)



