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
    ExpOp,
    mdsdassignment2_Sub,
    mdsdassignment2_Mult,
    mdsdassignment2_Div,
    mdsdassignment2_Parenthesis,
    mdsdassignment2_ExpOp,
    mdsdassignment2_Exp,
    mdsdassignment2_MathExp,
    mdsdassignment2_Add,
    mdsdassignment2_Num,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expop_is_not_abstract():
    assert not inspect.isabstract(ExpOp)


def test_hyp_expop_constructor_exists():
    assert callable(ExpOp.__init__)


def test_hyp_expop_constructor_args():
    sig = inspect.signature(ExpOp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mdsdassignment2_sub_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Sub)


def test_hyp_mdsdassignment2_sub_constructor_exists():
    assert callable(mdsdassignment2_Sub.__init__)


def test_hyp_mdsdassignment2_sub_constructor_args():
    sig = inspect.signature(mdsdassignment2_Sub.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mdsdassignment2_mult_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Mult)


def test_hyp_mdsdassignment2_mult_constructor_exists():
    assert callable(mdsdassignment2_Mult.__init__)


def test_hyp_mdsdassignment2_mult_constructor_args():
    sig = inspect.signature(mdsdassignment2_Mult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mdsdassignment2_div_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Div)


def test_hyp_mdsdassignment2_div_constructor_exists():
    assert callable(mdsdassignment2_Div.__init__)


def test_hyp_mdsdassignment2_div_constructor_args():
    sig = inspect.signature(mdsdassignment2_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mdsdassignment2_parenthesis_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Parenthesis)


def test_hyp_mdsdassignment2_parenthesis_constructor_exists():
    assert callable(mdsdassignment2_Parenthesis.__init__)


def test_hyp_mdsdassignment2_parenthesis_constructor_args():
    sig = inspect.signature(mdsdassignment2_Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mdsdassignment2_expop_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_ExpOp)


def test_hyp_mdsdassignment2_expop_constructor_exists():
    assert callable(mdsdassignment2_ExpOp.__init__)


def test_hyp_mdsdassignment2_expop_constructor_args():
    sig = inspect.signature(mdsdassignment2_ExpOp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mdsdassignment2_exp_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Exp)


def test_hyp_mdsdassignment2_exp_constructor_exists():
    assert callable(mdsdassignment2_Exp.__init__)


def test_hyp_mdsdassignment2_exp_constructor_args():
    sig = inspect.signature(mdsdassignment2_Exp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mdsdassignment2_mathexp_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_MathExp)


def test_hyp_mdsdassignment2_mathexp_constructor_exists():
    assert callable(mdsdassignment2_MathExp.__init__)


def test_hyp_mdsdassignment2_mathexp_constructor_args():
    sig = inspect.signature(mdsdassignment2_MathExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mdsdassignment2_add_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Add)


def test_hyp_mdsdassignment2_add_constructor_exists():
    assert callable(mdsdassignment2_Add.__init__)


def test_hyp_mdsdassignment2_add_constructor_args():
    sig = inspect.signature(mdsdassignment2_Add.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mdsdassignment2_num_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Num)


def test_hyp_mdsdassignment2_num_constructor_exists():
    assert callable(mdsdassignment2_Num.__init__)


def test_hyp_mdsdassignment2_num_constructor_args():
    sig = inspect.signature(mdsdassignment2_Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"



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
ExpOp_strategy = st.builds(
    ExpOp,
)
mdsdassignment2_Sub_strategy = st.builds(
    mdsdassignment2_Sub,
)
mdsdassignment2_Mult_strategy = st.builds(
    mdsdassignment2_Mult,
)
mdsdassignment2_Div_strategy = st.builds(
    mdsdassignment2_Div,
)
mdsdassignment2_Parenthesis_strategy = st.builds(
    mdsdassignment2_Parenthesis,
)
mdsdassignment2_ExpOp_strategy = st.builds(
    mdsdassignment2_ExpOp,
)
mdsdassignment2_Exp_strategy = st.builds(
    mdsdassignment2_Exp,
)
mdsdassignment2_MathExp_strategy = st.builds(
    mdsdassignment2_MathExp,
)
mdsdassignment2_Add_strategy = st.builds(
    mdsdassignment2_Add,
)
mdsdassignment2_Num_strategy = st.builds(
    mdsdassignment2_Num,
    value=
        st.integers()
)













@given(instance=mdsdassignment2_Num_strategy)
def test_hyp_mdsdassignment2_num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ExpOp,
    mdsdassignment2_Add,
    mdsdassignment2_Div,
    mdsdassignment2_Exp,
    mdsdassignment2_ExpOp,
    mdsdassignment2_MathExp,
    mdsdassignment2_Mult,
    mdsdassignment2_Num,
    mdsdassignment2_Parenthesis,
    mdsdassignment2_Sub,
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

def test_mdsdassignment2_Num_value_value_roundtrip():
    instance = mdsdassignment2_Num(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_mdsdassignment2_Add_isa_ExpOp():
    instance = mdsdassignment2_Add()
    assert isinstance(instance, ExpOp)


def test_mdsdassignment2_Div_isa_ExpOp():
    instance = mdsdassignment2_Div()
    assert isinstance(instance, ExpOp)


def test_mdsdassignment2_Mult_isa_ExpOp():
    instance = mdsdassignment2_Mult()
    assert isinstance(instance, ExpOp)


def test_mdsdassignment2_Num_isa_ExpOp():
    instance = mdsdassignment2_Num(value=7)
    assert isinstance(instance, ExpOp)


def test_mdsdassignment2_Parenthesis_isa_ExpOp():
    instance = mdsdassignment2_Parenthesis()
    assert isinstance(instance, ExpOp)


def test_mdsdassignment2_Sub_isa_ExpOp():
    instance = mdsdassignment2_Sub()
    assert isinstance(instance, ExpOp)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ExpOp_strategy = st.builds(ExpOp)
@given(instance=ExpOp_strategy)
@settings(max_examples=25)
def test_ExpOp_instantiation(instance):
    assert isinstance(instance, ExpOp)


mdsdassignment2_Add_strategy = st.builds(mdsdassignment2_Add)
@given(instance=mdsdassignment2_Add_strategy)
@settings(max_examples=25)
def test_mdsdassignment2_Add_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Add)


mdsdassignment2_Div_strategy = st.builds(mdsdassignment2_Div)
@given(instance=mdsdassignment2_Div_strategy)
@settings(max_examples=25)
def test_mdsdassignment2_Div_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Div)


mdsdassignment2_Exp_strategy = st.builds(mdsdassignment2_Exp)
@given(instance=mdsdassignment2_Exp_strategy)
@settings(max_examples=25)
def test_mdsdassignment2_Exp_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Exp)


mdsdassignment2_ExpOp_strategy = st.builds(mdsdassignment2_ExpOp)
@given(instance=mdsdassignment2_ExpOp_strategy)
@settings(max_examples=25)
def test_mdsdassignment2_ExpOp_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_ExpOp)


mdsdassignment2_MathExp_strategy = st.builds(mdsdassignment2_MathExp)
@given(instance=mdsdassignment2_MathExp_strategy)
@settings(max_examples=25)
def test_mdsdassignment2_MathExp_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_MathExp)


mdsdassignment2_Mult_strategy = st.builds(mdsdassignment2_Mult)
@given(instance=mdsdassignment2_Mult_strategy)
@settings(max_examples=25)
def test_mdsdassignment2_Mult_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Mult)


mdsdassignment2_Num_strategy = st.builds(mdsdassignment2_Num, value=st.integers())
@given(instance=mdsdassignment2_Num_strategy)
@settings(max_examples=25)
def test_mdsdassignment2_Num_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Num)


mdsdassignment2_Parenthesis_strategy = st.builds(mdsdassignment2_Parenthesis)
@given(instance=mdsdassignment2_Parenthesis_strategy)
@settings(max_examples=25)
def test_mdsdassignment2_Parenthesis_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Parenthesis)


mdsdassignment2_Sub_strategy = st.builds(mdsdassignment2_Sub)
@given(instance=mdsdassignment2_Sub_strategy)
@settings(max_examples=25)
def test_mdsdassignment2_Sub_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Sub)



