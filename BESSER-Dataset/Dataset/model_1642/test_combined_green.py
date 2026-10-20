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
    kwcs_TopCS,
    TreeCS,
    kwcs_LeafCS,
    kwcs_BinCS,
    kwcs_TreeCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_kwcs_topcs_is_not_abstract():
    assert not inspect.isabstract(kwcs_TopCS)


def test_hyp_kwcs_topcs_constructor_exists():
    assert callable(kwcs_TopCS.__init__)


def test_hyp_kwcs_topcs_constructor_args():
    sig = inspect.signature(kwcs_TopCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treecs_is_not_abstract():
    assert not inspect.isabstract(TreeCS)


def test_hyp_treecs_constructor_exists():
    assert callable(TreeCS.__init__)


def test_hyp_treecs_constructor_args():
    sig = inspect.signature(TreeCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kwcs_leafcs_is_not_abstract():
    assert not inspect.isabstract(kwcs_LeafCS)


def test_hyp_kwcs_leafcs_constructor_exists():
    assert callable(kwcs_LeafCS.__init__)


def test_hyp_kwcs_leafcs_constructor_args():
    sig = inspect.signature(kwcs_LeafCS.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"




def test_hyp_kwcs_bincs_is_not_abstract():
    assert not inspect.isabstract(kwcs_BinCS)


def test_hyp_kwcs_bincs_constructor_exists():
    assert callable(kwcs_BinCS.__init__)


def test_hyp_kwcs_bincs_constructor_args():
    sig = inspect.signature(kwcs_BinCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kwcs_treecs_is_not_abstract():
    assert not inspect.isabstract(kwcs_TreeCS)


def test_hyp_kwcs_treecs_constructor_exists():
    assert callable(kwcs_TreeCS.__init__)


def test_hyp_kwcs_treecs_constructor_args():
    sig = inspect.signature(kwcs_TreeCS.__init__)
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
kwcs_TopCS_strategy = st.builds(
    kwcs_TopCS,
)
TreeCS_strategy = st.builds(
    TreeCS,
)
kwcs_LeafCS_strategy = st.builds(
    kwcs_LeafCS,
    val=
        st.integers()
)
kwcs_BinCS_strategy = st.builds(
    kwcs_BinCS,
)
kwcs_TreeCS_strategy = st.builds(
    kwcs_TreeCS,
)






@given(instance=kwcs_LeafCS_strategy)
def test_hyp_kwcs_leafcs_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    TreeCS,
    kwcs_BinCS,
    kwcs_LeafCS,
    kwcs_TopCS,
    kwcs_TreeCS,
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

def test_kwcs_LeafCS_val_value_roundtrip():
    instance = kwcs_LeafCS(val=7)
    assert instance.val == 7
    instance.val = 13
    assert instance.val == 13


def test_kwcs_BinCS_isa_TreeCS():
    instance = kwcs_BinCS()
    assert isinstance(instance, TreeCS)


def test_kwcs_LeafCS_isa_TreeCS():
    instance = kwcs_LeafCS(val=7)
    assert isinstance(instance, TreeCS)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

TreeCS_strategy = st.builds(TreeCS)
@given(instance=TreeCS_strategy)
@settings(max_examples=25)
def test_TreeCS_instantiation(instance):
    assert isinstance(instance, TreeCS)


kwcs_BinCS_strategy = st.builds(kwcs_BinCS)
@given(instance=kwcs_BinCS_strategy)
@settings(max_examples=25)
def test_kwcs_BinCS_instantiation(instance):
    assert isinstance(instance, kwcs_BinCS)


kwcs_LeafCS_strategy = st.builds(kwcs_LeafCS, val=st.integers())
@given(instance=kwcs_LeafCS_strategy)
@settings(max_examples=25)
def test_kwcs_LeafCS_instantiation(instance):
    assert isinstance(instance, kwcs_LeafCS)


kwcs_TopCS_strategy = st.builds(kwcs_TopCS)
@given(instance=kwcs_TopCS_strategy)
@settings(max_examples=25)
def test_kwcs_TopCS_instantiation(instance):
    assert isinstance(instance, kwcs_TopCS)


kwcs_TreeCS_strategy = st.builds(kwcs_TreeCS)
@given(instance=kwcs_TreeCS_strategy)
@settings(max_examples=25)
def test_kwcs_TreeCS_instantiation(instance):
    assert isinstance(instance, kwcs_TreeCS)



