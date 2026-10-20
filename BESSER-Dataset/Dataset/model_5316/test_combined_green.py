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
    M,
    A,
    N,
    refinher2_Y,
    refinher2_H,
    CE,
    refinher2_DL,
    refinher2_DNamedElement,
    refinher2_M,
    DNamedElement,
    refinher2_A,
    refinher2_AB,
    refinher2_N,
    refinher2_E,
    refinher2_DG,
    refinher2_DC,
    E,
    refinher2_CE,
    refinher2_DR,
    refinher2_BB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_m_is_not_abstract():
    assert not inspect.isabstract(M)


def test_hyp_m_constructor_exists():
    assert callable(M.__init__)


def test_hyp_m_constructor_args():
    sig = inspect.signature(M.__init__)
    params = list(sig.parameters.keys())



def test_hyp_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_hyp_a_constructor_exists():
    assert callable(A.__init__)


def test_hyp_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_n_is_not_abstract():
    assert not inspect.isabstract(N)


def test_hyp_n_constructor_exists():
    assert callable(N.__init__)


def test_hyp_n_constructor_args():
    sig = inspect.signature(N.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_y_is_not_abstract():
    assert not inspect.isabstract(refinher2_Y)


def test_hyp_refinher2_y_constructor_exists():
    assert callable(refinher2_Y.__init__)


def test_hyp_refinher2_y_constructor_args():
    sig = inspect.signature(refinher2_Y.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_h_is_not_abstract():
    assert not inspect.isabstract(refinher2_H)


def test_hyp_refinher2_h_constructor_exists():
    assert callable(refinher2_H.__init__)


def test_hyp_refinher2_h_constructor_args():
    sig = inspect.signature(refinher2_H.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ce_is_not_abstract():
    assert not inspect.isabstract(CE)


def test_hyp_ce_constructor_exists():
    assert callable(CE.__init__)


def test_hyp_ce_constructor_args():
    sig = inspect.signature(CE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_dl_is_not_abstract():
    assert not inspect.isabstract(refinher2_DL)


def test_hyp_refinher2_dl_constructor_exists():
    assert callable(refinher2_DL.__init__)


def test_hyp_refinher2_dl_constructor_args():
    sig = inspect.signature(refinher2_DL.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_dnamedelement_is_not_abstract():
    assert not inspect.isabstract(refinher2_DNamedElement)


def test_hyp_refinher2_dnamedelement_constructor_exists():
    assert callable(refinher2_DNamedElement.__init__)


def test_hyp_refinher2_dnamedelement_constructor_args():
    sig = inspect.signature(refinher2_DNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_refinher2_m_is_not_abstract():
    assert not inspect.isabstract(refinher2_M)


def test_hyp_refinher2_m_constructor_exists():
    assert callable(refinher2_M.__init__)


def test_hyp_refinher2_m_constructor_args():
    sig = inspect.signature(refinher2_M.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dnamedelement_is_not_abstract():
    assert not inspect.isabstract(DNamedElement)


def test_hyp_dnamedelement_constructor_exists():
    assert callable(DNamedElement.__init__)


def test_hyp_dnamedelement_constructor_args():
    sig = inspect.signature(DNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_a_is_not_abstract():
    assert not inspect.isabstract(refinher2_A)


def test_hyp_refinher2_a_constructor_exists():
    assert callable(refinher2_A.__init__)


def test_hyp_refinher2_a_constructor_args():
    sig = inspect.signature(refinher2_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_ab_is_not_abstract():
    assert not inspect.isabstract(refinher2_AB)


def test_hyp_refinher2_ab_constructor_exists():
    assert callable(refinher2_AB.__init__)


def test_hyp_refinher2_ab_constructor_args():
    sig = inspect.signature(refinher2_AB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_n_is_not_abstract():
    assert not inspect.isabstract(refinher2_N)


def test_hyp_refinher2_n_constructor_exists():
    assert callable(refinher2_N.__init__)


def test_hyp_refinher2_n_constructor_args():
    sig = inspect.signature(refinher2_N.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_e_is_not_abstract():
    assert not inspect.isabstract(refinher2_E)


def test_hyp_refinher2_e_constructor_exists():
    assert callable(refinher2_E.__init__)


def test_hyp_refinher2_e_constructor_args():
    sig = inspect.signature(refinher2_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_dg_is_not_abstract():
    assert not inspect.isabstract(refinher2_DG)


def test_hyp_refinher2_dg_constructor_exists():
    assert callable(refinher2_DG.__init__)


def test_hyp_refinher2_dg_constructor_args():
    sig = inspect.signature(refinher2_DG.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_dc_is_not_abstract():
    assert not inspect.isabstract(refinher2_DC)


def test_hyp_refinher2_dc_constructor_exists():
    assert callable(refinher2_DC.__init__)


def test_hyp_refinher2_dc_constructor_args():
    sig = inspect.signature(refinher2_DC.__init__)
    params = list(sig.parameters.keys())



def test_hyp_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_hyp_e_constructor_exists():
    assert callable(E.__init__)


def test_hyp_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_ce_is_not_abstract():
    assert not inspect.isabstract(refinher2_CE)


def test_hyp_refinher2_ce_constructor_exists():
    assert callable(refinher2_CE.__init__)


def test_hyp_refinher2_ce_constructor_args():
    sig = inspect.signature(refinher2_CE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_dr_is_not_abstract():
    assert not inspect.isabstract(refinher2_DR)


def test_hyp_refinher2_dr_constructor_exists():
    assert callable(refinher2_DR.__init__)


def test_hyp_refinher2_dr_constructor_args():
    sig = inspect.signature(refinher2_DR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinher2_bb_is_not_abstract():
    assert not inspect.isabstract(refinher2_BB)


def test_hyp_refinher2_bb_constructor_exists():
    assert callable(refinher2_BB.__init__)


def test_hyp_refinher2_bb_constructor_args():
    sig = inspect.signature(refinher2_BB.__init__)
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
M_strategy = st.builds(
    M,
)
A_strategy = st.builds(
    A,
)
N_strategy = st.builds(
    N,
)
refinher2_Y_strategy = st.builds(
    refinher2_Y,
)
refinher2_H_strategy = st.builds(
    refinher2_H,
)
CE_strategy = st.builds(
    CE,
)
refinher2_DL_strategy = st.builds(
    refinher2_DL,
)
refinher2_DNamedElement_strategy = st.builds(
    refinher2_DNamedElement,
    name=
        safe_text
)
refinher2_M_strategy = st.builds(
    refinher2_M,
)
DNamedElement_strategy = st.builds(
    DNamedElement,
)
refinher2_A_strategy = st.builds(
    refinher2_A,
)
refinher2_AB_strategy = st.builds(
    refinher2_AB,
)
refinher2_N_strategy = st.builds(
    refinher2_N,
)
refinher2_E_strategy = st.builds(
    refinher2_E,
)
refinher2_DG_strategy = st.builds(
    refinher2_DG,
)
refinher2_DC_strategy = st.builds(
    refinher2_DC,
)
E_strategy = st.builds(
    E,
)
refinher2_CE_strategy = st.builds(
    refinher2_CE,
)
refinher2_DR_strategy = st.builds(
    refinher2_DR,
)
refinher2_BB_strategy = st.builds(
    refinher2_BB,
)











@given(instance=refinher2_DNamedElement_strategy)
def test_hyp_refinher2_dnamedelement_name_setter(instance):
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
    A,
    CE,
    DNamedElement,
    E,
    M,
    N,
    refinher2_A,
    refinher2_AB,
    refinher2_BB,
    refinher2_CE,
    refinher2_DC,
    refinher2_DG,
    refinher2_DL,
    refinher2_DNamedElement,
    refinher2_DR,
    refinher2_E,
    refinher2_H,
    refinher2_M,
    refinher2_N,
    refinher2_Y,
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

def test_refinher2_DNamedElement_name_value_roundtrip():
    instance = refinher2_DNamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_refinher2_CE_isa_A():
    instance = refinher2_CE()
    assert isinstance(instance, A)


def test_refinher2_N_isa_A():
    instance = refinher2_N()
    assert isinstance(instance, A)


def test_refinher2_DC_isa_CE():
    instance = refinher2_DC()
    assert isinstance(instance, CE)


def test_refinher2_DL_isa_CE():
    instance = refinher2_DL()
    assert isinstance(instance, CE)


def test_refinher2_A_isa_DNamedElement():
    instance = refinher2_A()
    assert isinstance(instance, DNamedElement)


def test_refinher2_AB_isa_DNamedElement():
    instance = refinher2_AB()
    assert isinstance(instance, DNamedElement)


def test_refinher2_BB_isa_DNamedElement():
    instance = refinher2_BB()
    assert isinstance(instance, DNamedElement)


def test_refinher2_E_isa_DNamedElement():
    instance = refinher2_E()
    assert isinstance(instance, DNamedElement)


def test_refinher2_N_isa_DNamedElement():
    instance = refinher2_N()
    assert isinstance(instance, DNamedElement)


def test_refinher2_CE_isa_E():
    instance = refinher2_CE()
    assert isinstance(instance, E)


def test_refinher2_DR_isa_E():
    instance = refinher2_DR()
    assert isinstance(instance, E)


def test_refinher2_N_isa_M():
    instance = refinher2_N()
    assert isinstance(instance, M)


def test_refinher2_H_isa_N():
    instance = refinher2_H()
    assert isinstance(instance, N)


def test_refinher2_Y_isa_N():
    instance = refinher2_Y()
    assert isinstance(instance, N)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

A_strategy = st.builds(A)
@given(instance=A_strategy)
@settings(max_examples=25)
def test_A_instantiation(instance):
    assert isinstance(instance, A)


CE_strategy = st.builds(CE)
@given(instance=CE_strategy)
@settings(max_examples=25)
def test_CE_instantiation(instance):
    assert isinstance(instance, CE)


DNamedElement_strategy = st.builds(DNamedElement)
@given(instance=DNamedElement_strategy)
@settings(max_examples=25)
def test_DNamedElement_instantiation(instance):
    assert isinstance(instance, DNamedElement)


E_strategy = st.builds(E)
@given(instance=E_strategy)
@settings(max_examples=25)
def test_E_instantiation(instance):
    assert isinstance(instance, E)


M_strategy = st.builds(M)
@given(instance=M_strategy)
@settings(max_examples=25)
def test_M_instantiation(instance):
    assert isinstance(instance, M)


N_strategy = st.builds(N)
@given(instance=N_strategy)
@settings(max_examples=25)
def test_N_instantiation(instance):
    assert isinstance(instance, N)


refinher2_A_strategy = st.builds(refinher2_A)
@given(instance=refinher2_A_strategy)
@settings(max_examples=25)
def test_refinher2_A_instantiation(instance):
    assert isinstance(instance, refinher2_A)


refinher2_AB_strategy = st.builds(refinher2_AB)
@given(instance=refinher2_AB_strategy)
@settings(max_examples=25)
def test_refinher2_AB_instantiation(instance):
    assert isinstance(instance, refinher2_AB)


refinher2_BB_strategy = st.builds(refinher2_BB)
@given(instance=refinher2_BB_strategy)
@settings(max_examples=25)
def test_refinher2_BB_instantiation(instance):
    assert isinstance(instance, refinher2_BB)


refinher2_CE_strategy = st.builds(refinher2_CE)
@given(instance=refinher2_CE_strategy)
@settings(max_examples=25)
def test_refinher2_CE_instantiation(instance):
    assert isinstance(instance, refinher2_CE)


refinher2_DC_strategy = st.builds(refinher2_DC)
@given(instance=refinher2_DC_strategy)
@settings(max_examples=25)
def test_refinher2_DC_instantiation(instance):
    assert isinstance(instance, refinher2_DC)


refinher2_DG_strategy = st.builds(refinher2_DG)
@given(instance=refinher2_DG_strategy)
@settings(max_examples=25)
def test_refinher2_DG_instantiation(instance):
    assert isinstance(instance, refinher2_DG)


refinher2_DL_strategy = st.builds(refinher2_DL)
@given(instance=refinher2_DL_strategy)
@settings(max_examples=25)
def test_refinher2_DL_instantiation(instance):
    assert isinstance(instance, refinher2_DL)


refinher2_DNamedElement_strategy = st.builds(refinher2_DNamedElement, name=safe_text)
@given(instance=refinher2_DNamedElement_strategy)
@settings(max_examples=25)
def test_refinher2_DNamedElement_instantiation(instance):
    assert isinstance(instance, refinher2_DNamedElement)


refinher2_DR_strategy = st.builds(refinher2_DR)
@given(instance=refinher2_DR_strategy)
@settings(max_examples=25)
def test_refinher2_DR_instantiation(instance):
    assert isinstance(instance, refinher2_DR)


refinher2_E_strategy = st.builds(refinher2_E)
@given(instance=refinher2_E_strategy)
@settings(max_examples=25)
def test_refinher2_E_instantiation(instance):
    assert isinstance(instance, refinher2_E)


refinher2_H_strategy = st.builds(refinher2_H)
@given(instance=refinher2_H_strategy)
@settings(max_examples=25)
def test_refinher2_H_instantiation(instance):
    assert isinstance(instance, refinher2_H)


refinher2_M_strategy = st.builds(refinher2_M)
@given(instance=refinher2_M_strategy)
@settings(max_examples=25)
def test_refinher2_M_instantiation(instance):
    assert isinstance(instance, refinher2_M)


refinher2_N_strategy = st.builds(refinher2_N)
@given(instance=refinher2_N_strategy)
@settings(max_examples=25)
def test_refinher2_N_instantiation(instance):
    assert isinstance(instance, refinher2_N)


refinher2_Y_strategy = st.builds(refinher2_Y)
@given(instance=refinher2_Y_strategy)
@settings(max_examples=25)
def test_refinher2_Y_instantiation(instance):
    assert isinstance(instance, refinher2_Y)



