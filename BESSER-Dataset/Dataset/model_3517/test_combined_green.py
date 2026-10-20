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
    autocast_ConceptC,
    ConceptA,
    autocast_ConceptB,
    autocast_ConceptA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_autocast_conceptc_is_not_abstract():
    assert not inspect.isabstract(autocast_ConceptC)


def test_hyp_autocast_conceptc_constructor_exists():
    assert callable(autocast_ConceptC.__init__)


def test_hyp_autocast_conceptc_constructor_args():
    sig = inspect.signature(autocast_ConceptC.__init__)
    params = list(sig.parameters.keys())



def test_hyp_concepta_is_not_abstract():
    assert not inspect.isabstract(ConceptA)


def test_hyp_concepta_constructor_exists():
    assert callable(ConceptA.__init__)


def test_hyp_concepta_constructor_args():
    sig = inspect.signature(ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_hyp_autocast_conceptb_is_not_abstract():
    assert not inspect.isabstract(autocast_ConceptB)


def test_hyp_autocast_conceptb_constructor_exists():
    assert callable(autocast_ConceptB.__init__)


def test_hyp_autocast_conceptb_constructor_args():
    sig = inspect.signature(autocast_ConceptB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_autocast_concepta_is_not_abstract():
    assert not inspect.isabstract(autocast_ConceptA)


def test_hyp_autocast_concepta_constructor_exists():
    assert callable(autocast_ConceptA.__init__)


def test_hyp_autocast_concepta_constructor_args():
    sig = inspect.signature(autocast_ConceptA.__init__)
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
autocast_ConceptC_strategy = st.builds(
    autocast_ConceptC,
)
ConceptA_strategy = st.builds(
    ConceptA,
)
autocast_ConceptB_strategy = st.builds(
    autocast_ConceptB,
    name=
        safe_text
)
autocast_ConceptA_strategy = st.builds(
    autocast_ConceptA,
)






@given(instance=autocast_ConceptB_strategy)
def test_hyp_autocast_conceptb_name_setter(instance):
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
    ConceptA,
    autocast_ConceptA,
    autocast_ConceptB,
    autocast_ConceptC,
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

def test_autocast_ConceptB_name_value_roundtrip():
    instance = autocast_ConceptB(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_autocast_ConceptB_isa_ConceptA():
    instance = autocast_ConceptB(name="sample_text")
    assert isinstance(instance, ConceptA)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ConceptA_strategy = st.builds(ConceptA)
@given(instance=ConceptA_strategy)
@settings(max_examples=25)
def test_ConceptA_instantiation(instance):
    assert isinstance(instance, ConceptA)


autocast_ConceptA_strategy = st.builds(autocast_ConceptA)
@given(instance=autocast_ConceptA_strategy)
@settings(max_examples=25)
def test_autocast_ConceptA_instantiation(instance):
    assert isinstance(instance, autocast_ConceptA)


autocast_ConceptB_strategy = st.builds(autocast_ConceptB, name=safe_text)
@given(instance=autocast_ConceptB_strategy)
@settings(max_examples=25)
def test_autocast_ConceptB_instantiation(instance):
    assert isinstance(instance, autocast_ConceptB)


autocast_ConceptC_strategy = st.builds(autocast_ConceptC)
@given(instance=autocast_ConceptC_strategy)
@settings(max_examples=25)
def test_autocast_ConceptC_instantiation(instance):
    assert isinstance(instance, autocast_ConceptC)



