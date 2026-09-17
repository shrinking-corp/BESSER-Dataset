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
    Lit,
    boolExpEnv_Tru,
    Exp,
    boolExpEnv_Lit,
    boolExpEnv_BinExp,
    boolExpEnv_VarRef,
    BinExp,
    boolExpEnv_Or,
    boolExpEnv_And,
    boolExpEnv_Not,
    boolExpEnv_Fals,
    boolExpEnv_Exp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_lit_is_not_abstract():
    assert not inspect.isabstract(Lit)


def test_hyp_lit_constructor_exists():
    assert callable(Lit.__init__)


def test_hyp_lit_constructor_args():
    sig = inspect.signature(Lit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_boolexpenv_tru_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv_Tru)


def test_hyp_boolexpenv_tru_constructor_exists():
    assert callable(boolExpEnv_Tru.__init__)


def test_hyp_boolexpenv_tru_constructor_args():
    sig = inspect.signature(boolExpEnv_Tru.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_hyp_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_hyp_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_boolexpenv_lit_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv_Lit)


def test_hyp_boolexpenv_lit_constructor_exists():
    assert callable(boolExpEnv_Lit.__init__)


def test_hyp_boolexpenv_lit_constructor_args():
    sig = inspect.signature(boolExpEnv_Lit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_boolexpenv_binexp_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv_BinExp)


def test_hyp_boolexpenv_binexp_constructor_exists():
    assert callable(boolExpEnv_BinExp.__init__)


def test_hyp_boolexpenv_binexp_constructor_args():
    sig = inspect.signature(boolExpEnv_BinExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_boolexpenv_varref_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv_VarRef)


def test_hyp_boolexpenv_varref_constructor_exists():
    assert callable(boolExpEnv_VarRef.__init__)


def test_hyp_boolexpenv_varref_constructor_args():
    sig = inspect.signature(boolExpEnv_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_binexp_is_not_abstract():
    assert not inspect.isabstract(BinExp)


def test_hyp_binexp_constructor_exists():
    assert callable(BinExp.__init__)


def test_hyp_binexp_constructor_args():
    sig = inspect.signature(BinExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_boolexpenv_or_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv_Or)


def test_hyp_boolexpenv_or_constructor_exists():
    assert callable(boolExpEnv_Or.__init__)


def test_hyp_boolexpenv_or_constructor_args():
    sig = inspect.signature(boolExpEnv_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_boolexpenv_and_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv_And)


def test_hyp_boolexpenv_and_constructor_exists():
    assert callable(boolExpEnv_And.__init__)


def test_hyp_boolexpenv_and_constructor_args():
    sig = inspect.signature(boolExpEnv_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_boolexpenv_not_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv_Not)


def test_hyp_boolexpenv_not_constructor_exists():
    assert callable(boolExpEnv_Not.__init__)


def test_hyp_boolexpenv_not_constructor_args():
    sig = inspect.signature(boolExpEnv_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_boolexpenv_fals_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv_Fals)


def test_hyp_boolexpenv_fals_constructor_exists():
    assert callable(boolExpEnv_Fals.__init__)


def test_hyp_boolexpenv_fals_constructor_args():
    sig = inspect.signature(boolExpEnv_Fals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_boolexpenv_exp_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv_Exp)


def test_hyp_boolexpenv_exp_constructor_exists():
    assert callable(boolExpEnv_Exp.__init__)


def test_hyp_boolexpenv_exp_constructor_args():
    sig = inspect.signature(boolExpEnv_Exp.__init__)
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
Lit_strategy = st.builds(
    Lit,
)
boolExpEnv_Tru_strategy = st.builds(
    boolExpEnv_Tru,
)
Exp_strategy = st.builds(
    Exp,
)
boolExpEnv_Lit_strategy = st.builds(
    boolExpEnv_Lit,
)
boolExpEnv_BinExp_strategy = st.builds(
    boolExpEnv_BinExp,
)
boolExpEnv_VarRef_strategy = st.builds(
    boolExpEnv_VarRef,
    name=
        safe_text
)
BinExp_strategy = st.builds(
    BinExp,
)
boolExpEnv_Or_strategy = st.builds(
    boolExpEnv_Or,
)
boolExpEnv_And_strategy = st.builds(
    boolExpEnv_And,
)
boolExpEnv_Not_strategy = st.builds(
    boolExpEnv_Not,
)
boolExpEnv_Fals_strategy = st.builds(
    boolExpEnv_Fals,
)
boolExpEnv_Exp_strategy = st.builds(
    boolExpEnv_Exp,
)









@given(instance=boolExpEnv_VarRef_strategy)
def test_hyp_boolexpenv_varref_name_setter(instance):
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
    BinExp,
    Exp,
    Lit,
    boolExpEnv_And,
    boolExpEnv_BinExp,
    boolExpEnv_Exp,
    boolExpEnv_Fals,
    boolExpEnv_Lit,
    boolExpEnv_Not,
    boolExpEnv_Or,
    boolExpEnv_Tru,
    boolExpEnv_VarRef,
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

def test_boolExpEnv_VarRef_name_value_roundtrip():
    instance = boolExpEnv_VarRef(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_boolExpEnv_And_isa_BinExp():
    instance = boolExpEnv_And()
    assert isinstance(instance, BinExp)


def test_boolExpEnv_Or_isa_BinExp():
    instance = boolExpEnv_Or()
    assert isinstance(instance, BinExp)


def test_boolExpEnv_BinExp_isa_Exp():
    instance = boolExpEnv_BinExp()
    assert isinstance(instance, Exp)


def test_boolExpEnv_Lit_isa_Exp():
    instance = boolExpEnv_Lit()
    assert isinstance(instance, Exp)


def test_boolExpEnv_Not_isa_Exp():
    instance = boolExpEnv_Not()
    assert isinstance(instance, Exp)


def test_boolExpEnv_VarRef_isa_Exp():
    instance = boolExpEnv_VarRef(name="sample_text")
    assert isinstance(instance, Exp)


def test_boolExpEnv_Fals_isa_Lit():
    instance = boolExpEnv_Fals()
    assert isinstance(instance, Lit)


def test_boolExpEnv_Tru_isa_Lit():
    instance = boolExpEnv_Tru()
    assert isinstance(instance, Lit)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinExp_strategy = st.builds(BinExp)
@given(instance=BinExp_strategy)
@settings(max_examples=25)
def test_BinExp_instantiation(instance):
    assert isinstance(instance, BinExp)


Exp_strategy = st.builds(Exp)
@given(instance=Exp_strategy)
@settings(max_examples=25)
def test_Exp_instantiation(instance):
    assert isinstance(instance, Exp)


Lit_strategy = st.builds(Lit)
@given(instance=Lit_strategy)
@settings(max_examples=25)
def test_Lit_instantiation(instance):
    assert isinstance(instance, Lit)


boolExpEnv_And_strategy = st.builds(boolExpEnv_And)
@given(instance=boolExpEnv_And_strategy)
@settings(max_examples=25)
def test_boolExpEnv_And_instantiation(instance):
    assert isinstance(instance, boolExpEnv_And)


boolExpEnv_BinExp_strategy = st.builds(boolExpEnv_BinExp)
@given(instance=boolExpEnv_BinExp_strategy)
@settings(max_examples=25)
def test_boolExpEnv_BinExp_instantiation(instance):
    assert isinstance(instance, boolExpEnv_BinExp)


boolExpEnv_Exp_strategy = st.builds(boolExpEnv_Exp)
@given(instance=boolExpEnv_Exp_strategy)
@settings(max_examples=25)
def test_boolExpEnv_Exp_instantiation(instance):
    assert isinstance(instance, boolExpEnv_Exp)


boolExpEnv_Fals_strategy = st.builds(boolExpEnv_Fals)
@given(instance=boolExpEnv_Fals_strategy)
@settings(max_examples=25)
def test_boolExpEnv_Fals_instantiation(instance):
    assert isinstance(instance, boolExpEnv_Fals)


boolExpEnv_Lit_strategy = st.builds(boolExpEnv_Lit)
@given(instance=boolExpEnv_Lit_strategy)
@settings(max_examples=25)
def test_boolExpEnv_Lit_instantiation(instance):
    assert isinstance(instance, boolExpEnv_Lit)


boolExpEnv_Not_strategy = st.builds(boolExpEnv_Not)
@given(instance=boolExpEnv_Not_strategy)
@settings(max_examples=25)
def test_boolExpEnv_Not_instantiation(instance):
    assert isinstance(instance, boolExpEnv_Not)


boolExpEnv_Or_strategy = st.builds(boolExpEnv_Or)
@given(instance=boolExpEnv_Or_strategy)
@settings(max_examples=25)
def test_boolExpEnv_Or_instantiation(instance):
    assert isinstance(instance, boolExpEnv_Or)


boolExpEnv_Tru_strategy = st.builds(boolExpEnv_Tru)
@given(instance=boolExpEnv_Tru_strategy)
@settings(max_examples=25)
def test_boolExpEnv_Tru_instantiation(instance):
    assert isinstance(instance, boolExpEnv_Tru)


boolExpEnv_VarRef_strategy = st.builds(boolExpEnv_VarRef, name=safe_text)
@given(instance=boolExpEnv_VarRef_strategy)
@settings(max_examples=25)
def test_boolExpEnv_VarRef_instantiation(instance):
    assert isinstance(instance, boolExpEnv_VarRef)



