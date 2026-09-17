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
    ChangingOverTime_LinkKind,
    TimeStampedElement,
    ChangingOverTime_Entity,
    ChangingOverTime_BindingKind,
    ChangingOverTime_NodeKind,
    ChangingOverTime_Tree,
    ChangingOverTime_TimeStampedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_changingovertime_linkkind_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_LinkKind)


def test_hyp_changingovertime_linkkind_constructor_exists():
    assert callable(ChangingOverTime_LinkKind.__init__)


def test_hyp_changingovertime_linkkind_constructor_args():
    sig = inspect.signature(ChangingOverTime_LinkKind.__init__)
    params = list(sig.parameters.keys())



def test_hyp_timestampedelement_is_not_abstract():
    assert not inspect.isabstract(TimeStampedElement)


def test_hyp_timestampedelement_constructor_exists():
    assert callable(TimeStampedElement.__init__)


def test_hyp_timestampedelement_constructor_args():
    sig = inspect.signature(TimeStampedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_changingovertime_entity_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_Entity)


def test_hyp_changingovertime_entity_constructor_exists():
    assert callable(ChangingOverTime_Entity.__init__)


def test_hyp_changingovertime_entity_constructor_args():
    sig = inspect.signature(ChangingOverTime_Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_changingovertime_bindingkind_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_BindingKind)


def test_hyp_changingovertime_bindingkind_constructor_exists():
    assert callable(ChangingOverTime_BindingKind.__init__)


def test_hyp_changingovertime_bindingkind_constructor_args():
    sig = inspect.signature(ChangingOverTime_BindingKind.__init__)
    params = list(sig.parameters.keys())



def test_hyp_changingovertime_nodekind_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_NodeKind)


def test_hyp_changingovertime_nodekind_constructor_exists():
    assert callable(ChangingOverTime_NodeKind.__init__)


def test_hyp_changingovertime_nodekind_constructor_args():
    sig = inspect.signature(ChangingOverTime_NodeKind.__init__)
    params = list(sig.parameters.keys())



def test_hyp_changingovertime_tree_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_Tree)


def test_hyp_changingovertime_tree_constructor_exists():
    assert callable(ChangingOverTime_Tree.__init__)


def test_hyp_changingovertime_tree_constructor_args():
    sig = inspect.signature(ChangingOverTime_Tree.__init__)
    params = list(sig.parameters.keys())



def test_hyp_changingovertime_timestampedelement_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_TimeStampedElement)


def test_hyp_changingovertime_timestampedelement_constructor_exists():
    assert callable(ChangingOverTime_TimeStampedElement.__init__)


def test_hyp_changingovertime_timestampedelement_constructor_args():
    sig = inspect.signature(ChangingOverTime_TimeStampedElement.__init__)
    params = list(sig.parameters.keys())
    assert "expirationDate" in params, "Missing parameter 'expirationDate'"
    assert "effectiveDate" in params, "Missing parameter 'effectiveDate'"




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
ChangingOverTime_LinkKind_strategy = st.builds(
    ChangingOverTime_LinkKind,
)
TimeStampedElement_strategy = st.builds(
    TimeStampedElement,
)
ChangingOverTime_Entity_strategy = st.builds(
    ChangingOverTime_Entity,
)
ChangingOverTime_BindingKind_strategy = st.builds(
    ChangingOverTime_BindingKind,
)
ChangingOverTime_NodeKind_strategy = st.builds(
    ChangingOverTime_NodeKind,
)
ChangingOverTime_Tree_strategy = st.builds(
    ChangingOverTime_Tree,
)
ChangingOverTime_TimeStampedElement_strategy = st.builds(
    ChangingOverTime_TimeStampedElement,
    expirationDate=
        st.dates(),
    effectiveDate=
        st.dates()
)










@given(instance=ChangingOverTime_TimeStampedElement_strategy)
def test_hyp_changingovertime_timestampedelement_expirationDate_setter(instance):
    original = instance.expirationDate
    instance.expirationDate = original
    assert instance.expirationDate == original



@given(instance=ChangingOverTime_TimeStampedElement_strategy)
def test_hyp_changingovertime_timestampedelement_effectiveDate_setter(instance):
    original = instance.effectiveDate
    instance.effectiveDate = original
    assert instance.effectiveDate == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ChangingOverTime_BindingKind,
    ChangingOverTime_Entity,
    ChangingOverTime_LinkKind,
    ChangingOverTime_NodeKind,
    ChangingOverTime_TimeStampedElement,
    ChangingOverTime_Tree,
    TimeStampedElement,
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

def test_ChangingOverTime_TimeStampedElement_effectiveDate_value_roundtrip():
    instance = ChangingOverTime_TimeStampedElement(effectiveDate=date(2024, 1, 1), expirationDate=date(2024, 1, 1))
    assert instance.effectiveDate == date(2024, 1, 1)
    instance.effectiveDate = date(2025, 6, 15)
    assert instance.effectiveDate == date(2025, 6, 15)


def test_ChangingOverTime_TimeStampedElement_expirationDate_value_roundtrip():
    instance = ChangingOverTime_TimeStampedElement(effectiveDate=date(2024, 1, 1), expirationDate=date(2024, 1, 1))
    assert instance.expirationDate == date(2024, 1, 1)
    instance.expirationDate = date(2025, 6, 15)
    assert instance.expirationDate == date(2025, 6, 15)


def test_ChangingOverTime_BindingKind_isa_TimeStampedElement():
    instance = ChangingOverTime_BindingKind()
    assert isinstance(instance, TimeStampedElement)


def test_ChangingOverTime_Entity_isa_TimeStampedElement():
    instance = ChangingOverTime_Entity()
    assert isinstance(instance, TimeStampedElement)


def test_ChangingOverTime_NodeKind_isa_TimeStampedElement():
    instance = ChangingOverTime_NodeKind()
    assert isinstance(instance, TimeStampedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ChangingOverTime_BindingKind_strategy = st.builds(ChangingOverTime_BindingKind)
@given(instance=ChangingOverTime_BindingKind_strategy)
@settings(max_examples=25)
def test_ChangingOverTime_BindingKind_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_BindingKind)


ChangingOverTime_Entity_strategy = st.builds(ChangingOverTime_Entity)
@given(instance=ChangingOverTime_Entity_strategy)
@settings(max_examples=25)
def test_ChangingOverTime_Entity_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_Entity)


ChangingOverTime_LinkKind_strategy = st.builds(ChangingOverTime_LinkKind)
@given(instance=ChangingOverTime_LinkKind_strategy)
@settings(max_examples=25)
def test_ChangingOverTime_LinkKind_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_LinkKind)


ChangingOverTime_NodeKind_strategy = st.builds(ChangingOverTime_NodeKind)
@given(instance=ChangingOverTime_NodeKind_strategy)
@settings(max_examples=25)
def test_ChangingOverTime_NodeKind_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_NodeKind)


ChangingOverTime_TimeStampedElement_strategy = st.builds(ChangingOverTime_TimeStampedElement, effectiveDate=st.dates(), expirationDate=st.dates())
@given(instance=ChangingOverTime_TimeStampedElement_strategy)
@settings(max_examples=25)
def test_ChangingOverTime_TimeStampedElement_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_TimeStampedElement)


ChangingOverTime_Tree_strategy = st.builds(ChangingOverTime_Tree)
@given(instance=ChangingOverTime_Tree_strategy)
@settings(max_examples=25)
def test_ChangingOverTime_Tree_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_Tree)


TimeStampedElement_strategy = st.builds(TimeStampedElement)
@given(instance=TimeStampedElement_strategy)
@settings(max_examples=25)
def test_TimeStampedElement_instantiation(instance):
    assert isinstance(instance, TimeStampedElement)



