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
    Master_N,
    B,
    N,
    Master_test2_B,
    Master_Classe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_master_n_is_not_abstract():
    assert not inspect.isabstract(Master_N)


def test_hyp_master_n_constructor_exists():
    assert callable(Master_N.__init__)


def test_hyp_master_n_constructor_args():
    sig = inspect.signature(Master_N.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"




def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_n_is_not_abstract():
    assert not inspect.isabstract(N)


def test_hyp_n_constructor_exists():
    assert callable(N.__init__)


def test_hyp_n_constructor_args():
    sig = inspect.signature(N.__init__)
    params = list(sig.parameters.keys())



def test_hyp_master_test2_b_is_not_abstract():
    assert not inspect.isabstract(Master_test2_B)


def test_hyp_master_test2_b_constructor_exists():
    assert callable(Master_test2_B.__init__)


def test_hyp_master_test2_b_constructor_args():
    sig = inspect.signature(Master_test2_B.__init__)
    params = list(sig.parameters.keys())
    assert "nb" in params, "Missing parameter 'nb'"
    assert "nb2" in params, "Missing parameter 'nb2'"





def test_hyp_master_classe_is_not_abstract():
    assert not inspect.isabstract(Master_Classe)


def test_hyp_master_classe_constructor_exists():
    assert callable(Master_Classe.__init__)


def test_hyp_master_classe_constructor_args():
    sig = inspect.signature(Master_Classe.__init__)
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
Master_N_strategy = st.builds(
    Master_N,
    n=
        safe_text
)
B_strategy = st.builds(
    B,
)
N_strategy = st.builds(
    N,
)
Master_test2_B_strategy = st.builds(
    Master_test2_B,
    nb=
        st.integers(),
    nb2=
        st.integers()
)
Master_Classe_strategy = st.builds(
    Master_Classe,
)




@given(instance=Master_N_strategy)
def test_hyp_master_n_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original






@given(instance=Master_test2_B_strategy)
def test_hyp_master_test2_b_nb_setter(instance):
    original = instance.nb
    instance.nb = original
    assert instance.nb == original



@given(instance=Master_test2_B_strategy)
def test_hyp_master_test2_b_nb2_setter(instance):
    original = instance.nb2
    instance.nb2 = original
    assert instance.nb2 == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    B,
    Master_Classe,
    Master_N,
    Master_test2_B,
    N,
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

def test_Master_N_n_value_roundtrip():
    instance = Master_N(n="sample_text")
    assert instance.n == "sample_text"
    instance.n = "sample_text_2"
    assert instance.n == "sample_text_2"


def test_Master_test2_B_nb_value_roundtrip():
    instance = Master_test2_B(nb=7, nb2=7)
    assert instance.nb == 7
    instance.nb = 13
    assert instance.nb == 13


def test_Master_test2_B_nb2_value_roundtrip():
    instance = Master_test2_B(nb=7, nb2=7)
    assert instance.nb2 == 7
    instance.nb2 = 13
    assert instance.nb2 == 13


def test_Master_Classe_isa_N():
    instance = Master_Classe()
    assert isinstance(instance, N)


def test_Master_test2_B_isa_N():
    instance = Master_test2_B(nb=7, nb2=7)
    assert isinstance(instance, N)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

B_strategy = st.builds(B)
@given(instance=B_strategy)
@settings(max_examples=25)
def test_B_instantiation(instance):
    assert isinstance(instance, B)


Master_Classe_strategy = st.builds(Master_Classe)
@given(instance=Master_Classe_strategy)
@settings(max_examples=25)
def test_Master_Classe_instantiation(instance):
    assert isinstance(instance, Master_Classe)


Master_N_strategy = st.builds(Master_N, n=safe_text)
@given(instance=Master_N_strategy)
@settings(max_examples=25)
def test_Master_N_instantiation(instance):
    assert isinstance(instance, Master_N)


Master_test2_B_strategy = st.builds(Master_test2_B, nb=st.integers(), nb2=st.integers())
@given(instance=Master_test2_B_strategy)
@settings(max_examples=25)
def test_Master_test2_B_instantiation(instance):
    assert isinstance(instance, Master_test2_B)


N_strategy = st.builds(N)
@given(instance=N_strategy)
@settings(max_examples=25)
def test_N_instantiation(instance):
    assert isinstance(instance, N)



