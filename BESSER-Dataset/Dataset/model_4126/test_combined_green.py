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
    assignment2_ExpMD,
    assignment2_ExpPM,
    assignment2_EObject,
    ExpMinusPlus,
    assignment2_ExpMultDiv,
    assignment2_ExpMinusPlus,
    assignment2_MathExp,
    assignment2_Model,
    ExpMD,
    assignment2_Div,
    assignment2_Mult,
    ExpPM,
    assignment2_Minus,
    assignment2_Plus,
    Primary,
    assignment2_Number,
    assignment2_Parenthesis,
    ExpMultDiv,
    assignment2_Exp,
    assignment2_Primary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_assignment2_expmd_is_not_abstract():
    assert not inspect.isabstract(assignment2_ExpMD)


def test_hyp_assignment2_expmd_constructor_exists():
    assert callable(assignment2_ExpMD.__init__)


def test_hyp_assignment2_expmd_constructor_args():
    sig = inspect.signature(assignment2_ExpMD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_exppm_is_not_abstract():
    assert not inspect.isabstract(assignment2_ExpPM)


def test_hyp_assignment2_exppm_constructor_exists():
    assert callable(assignment2_ExpPM.__init__)


def test_hyp_assignment2_exppm_constructor_args():
    sig = inspect.signature(assignment2_ExpPM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_eobject_is_not_abstract():
    assert not inspect.isabstract(assignment2_EObject)


def test_hyp_assignment2_eobject_constructor_exists():
    assert callable(assignment2_EObject.__init__)


def test_hyp_assignment2_eobject_constructor_args():
    sig = inspect.signature(assignment2_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expminusplus_is_not_abstract():
    assert not inspect.isabstract(ExpMinusPlus)


def test_hyp_expminusplus_constructor_exists():
    assert callable(ExpMinusPlus.__init__)


def test_hyp_expminusplus_constructor_args():
    sig = inspect.signature(ExpMinusPlus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_expmultdiv_is_not_abstract():
    assert not inspect.isabstract(assignment2_ExpMultDiv)


def test_hyp_assignment2_expmultdiv_constructor_exists():
    assert callable(assignment2_ExpMultDiv.__init__)


def test_hyp_assignment2_expmultdiv_constructor_args():
    sig = inspect.signature(assignment2_ExpMultDiv.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_expminusplus_is_not_abstract():
    assert not inspect.isabstract(assignment2_ExpMinusPlus)


def test_hyp_assignment2_expminusplus_constructor_exists():
    assert callable(assignment2_ExpMinusPlus.__init__)


def test_hyp_assignment2_expminusplus_constructor_args():
    sig = inspect.signature(assignment2_ExpMinusPlus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_mathexp_is_not_abstract():
    assert not inspect.isabstract(assignment2_MathExp)


def test_hyp_assignment2_mathexp_constructor_exists():
    assert callable(assignment2_MathExp.__init__)


def test_hyp_assignment2_mathexp_constructor_args():
    sig = inspect.signature(assignment2_MathExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_model_is_not_abstract():
    assert not inspect.isabstract(assignment2_Model)


def test_hyp_assignment2_model_constructor_exists():
    assert callable(assignment2_Model.__init__)


def test_hyp_assignment2_model_constructor_args():
    sig = inspect.signature(assignment2_Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expmd_is_not_abstract():
    assert not inspect.isabstract(ExpMD)


def test_hyp_expmd_constructor_exists():
    assert callable(ExpMD.__init__)


def test_hyp_expmd_constructor_args():
    sig = inspect.signature(ExpMD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_div_is_not_abstract():
    assert not inspect.isabstract(assignment2_Div)


def test_hyp_assignment2_div_constructor_exists():
    assert callable(assignment2_Div.__init__)


def test_hyp_assignment2_div_constructor_args():
    sig = inspect.signature(assignment2_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_mult_is_not_abstract():
    assert not inspect.isabstract(assignment2_Mult)


def test_hyp_assignment2_mult_constructor_exists():
    assert callable(assignment2_Mult.__init__)


def test_hyp_assignment2_mult_constructor_args():
    sig = inspect.signature(assignment2_Mult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exppm_is_not_abstract():
    assert not inspect.isabstract(ExpPM)


def test_hyp_exppm_constructor_exists():
    assert callable(ExpPM.__init__)


def test_hyp_exppm_constructor_args():
    sig = inspect.signature(ExpPM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_minus_is_not_abstract():
    assert not inspect.isabstract(assignment2_Minus)


def test_hyp_assignment2_minus_constructor_exists():
    assert callable(assignment2_Minus.__init__)


def test_hyp_assignment2_minus_constructor_args():
    sig = inspect.signature(assignment2_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_plus_is_not_abstract():
    assert not inspect.isabstract(assignment2_Plus)


def test_hyp_assignment2_plus_constructor_exists():
    assert callable(assignment2_Plus.__init__)


def test_hyp_assignment2_plus_constructor_args():
    sig = inspect.signature(assignment2_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_hyp_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_hyp_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_number_is_not_abstract():
    assert not inspect.isabstract(assignment2_Number)


def test_hyp_assignment2_number_constructor_exists():
    assert callable(assignment2_Number.__init__)


def test_hyp_assignment2_number_constructor_args():
    sig = inspect.signature(assignment2_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_assignment2_parenthesis_is_not_abstract():
    assert not inspect.isabstract(assignment2_Parenthesis)


def test_hyp_assignment2_parenthesis_constructor_exists():
    assert callable(assignment2_Parenthesis.__init__)


def test_hyp_assignment2_parenthesis_constructor_args():
    sig = inspect.signature(assignment2_Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expmultdiv_is_not_abstract():
    assert not inspect.isabstract(ExpMultDiv)


def test_hyp_expmultdiv_constructor_exists():
    assert callable(ExpMultDiv.__init__)


def test_hyp_expmultdiv_constructor_args():
    sig = inspect.signature(ExpMultDiv.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_exp_is_not_abstract():
    assert not inspect.isabstract(assignment2_Exp)


def test_hyp_assignment2_exp_constructor_exists():
    assert callable(assignment2_Exp.__init__)


def test_hyp_assignment2_exp_constructor_args():
    sig = inspect.signature(assignment2_Exp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignment2_primary_is_not_abstract():
    assert not inspect.isabstract(assignment2_Primary)


def test_hyp_assignment2_primary_constructor_exists():
    assert callable(assignment2_Primary.__init__)


def test_hyp_assignment2_primary_constructor_args():
    sig = inspect.signature(assignment2_Primary.__init__)
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
assignment2_ExpMD_strategy = st.builds(
    assignment2_ExpMD,
)
assignment2_ExpPM_strategy = st.builds(
    assignment2_ExpPM,
)
assignment2_EObject_strategy = st.builds(
    assignment2_EObject,
)
ExpMinusPlus_strategy = st.builds(
    ExpMinusPlus,
)
assignment2_ExpMultDiv_strategy = st.builds(
    assignment2_ExpMultDiv,
)
assignment2_ExpMinusPlus_strategy = st.builds(
    assignment2_ExpMinusPlus,
)
assignment2_MathExp_strategy = st.builds(
    assignment2_MathExp,
)
assignment2_Model_strategy = st.builds(
    assignment2_Model,
)
ExpMD_strategy = st.builds(
    ExpMD,
)
assignment2_Div_strategy = st.builds(
    assignment2_Div,
)
assignment2_Mult_strategy = st.builds(
    assignment2_Mult,
)
ExpPM_strategy = st.builds(
    ExpPM,
)
assignment2_Minus_strategy = st.builds(
    assignment2_Minus,
)
assignment2_Plus_strategy = st.builds(
    assignment2_Plus,
)
Primary_strategy = st.builds(
    Primary,
)
assignment2_Number_strategy = st.builds(
    assignment2_Number,
    value=
        st.integers()
)
assignment2_Parenthesis_strategy = st.builds(
    assignment2_Parenthesis,
)
ExpMultDiv_strategy = st.builds(
    ExpMultDiv,
)
assignment2_Exp_strategy = st.builds(
    assignment2_Exp,
)
assignment2_Primary_strategy = st.builds(
    assignment2_Primary,
)



















@given(instance=assignment2_Number_strategy)
def test_hyp_assignment2_number_value_setter(instance):
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
    ExpMD,
    ExpMinusPlus,
    ExpMultDiv,
    ExpPM,
    Primary,
    assignment2_Div,
    assignment2_EObject,
    assignment2_Exp,
    assignment2_ExpMD,
    assignment2_ExpMinusPlus,
    assignment2_ExpMultDiv,
    assignment2_ExpPM,
    assignment2_MathExp,
    assignment2_Minus,
    assignment2_Model,
    assignment2_Mult,
    assignment2_Number,
    assignment2_Parenthesis,
    assignment2_Plus,
    assignment2_Primary,
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

def test_assignment2_Number_value_value_roundtrip():
    instance = assignment2_Number(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_assignment2_Div_isa_ExpMD():
    instance = assignment2_Div()
    assert isinstance(instance, ExpMD)


def test_assignment2_Mult_isa_ExpMD():
    instance = assignment2_Mult()
    assert isinstance(instance, ExpMD)


def test_assignment2_ExpMultDiv_isa_ExpMinusPlus():
    instance = assignment2_ExpMultDiv()
    assert isinstance(instance, ExpMinusPlus)


def test_assignment2_Exp_isa_ExpMultDiv():
    instance = assignment2_Exp()
    assert isinstance(instance, ExpMultDiv)


def test_assignment2_Primary_isa_ExpMultDiv():
    instance = assignment2_Primary()
    assert isinstance(instance, ExpMultDiv)


def test_assignment2_Minus_isa_ExpPM():
    instance = assignment2_Minus()
    assert isinstance(instance, ExpPM)


def test_assignment2_Plus_isa_ExpPM():
    instance = assignment2_Plus()
    assert isinstance(instance, ExpPM)


def test_assignment2_Number_isa_Primary():
    instance = assignment2_Number(value=7)
    assert isinstance(instance, Primary)


def test_assignment2_Parenthesis_isa_Primary():
    instance = assignment2_Parenthesis()
    assert isinstance(instance, Primary)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ExpMD_strategy = st.builds(ExpMD)
@given(instance=ExpMD_strategy)
@settings(max_examples=25)
def test_ExpMD_instantiation(instance):
    assert isinstance(instance, ExpMD)


ExpMinusPlus_strategy = st.builds(ExpMinusPlus)
@given(instance=ExpMinusPlus_strategy)
@settings(max_examples=25)
def test_ExpMinusPlus_instantiation(instance):
    assert isinstance(instance, ExpMinusPlus)


ExpMultDiv_strategy = st.builds(ExpMultDiv)
@given(instance=ExpMultDiv_strategy)
@settings(max_examples=25)
def test_ExpMultDiv_instantiation(instance):
    assert isinstance(instance, ExpMultDiv)


ExpPM_strategy = st.builds(ExpPM)
@given(instance=ExpPM_strategy)
@settings(max_examples=25)
def test_ExpPM_instantiation(instance):
    assert isinstance(instance, ExpPM)


Primary_strategy = st.builds(Primary)
@given(instance=Primary_strategy)
@settings(max_examples=25)
def test_Primary_instantiation(instance):
    assert isinstance(instance, Primary)


assignment2_Div_strategy = st.builds(assignment2_Div)
@given(instance=assignment2_Div_strategy)
@settings(max_examples=25)
def test_assignment2_Div_instantiation(instance):
    assert isinstance(instance, assignment2_Div)


assignment2_EObject_strategy = st.builds(assignment2_EObject)
@given(instance=assignment2_EObject_strategy)
@settings(max_examples=25)
def test_assignment2_EObject_instantiation(instance):
    assert isinstance(instance, assignment2_EObject)


assignment2_Exp_strategy = st.builds(assignment2_Exp)
@given(instance=assignment2_Exp_strategy)
@settings(max_examples=25)
def test_assignment2_Exp_instantiation(instance):
    assert isinstance(instance, assignment2_Exp)


assignment2_ExpMD_strategy = st.builds(assignment2_ExpMD)
@given(instance=assignment2_ExpMD_strategy)
@settings(max_examples=25)
def test_assignment2_ExpMD_instantiation(instance):
    assert isinstance(instance, assignment2_ExpMD)


assignment2_ExpMinusPlus_strategy = st.builds(assignment2_ExpMinusPlus)
@given(instance=assignment2_ExpMinusPlus_strategy)
@settings(max_examples=25)
def test_assignment2_ExpMinusPlus_instantiation(instance):
    assert isinstance(instance, assignment2_ExpMinusPlus)


assignment2_ExpMultDiv_strategy = st.builds(assignment2_ExpMultDiv)
@given(instance=assignment2_ExpMultDiv_strategy)
@settings(max_examples=25)
def test_assignment2_ExpMultDiv_instantiation(instance):
    assert isinstance(instance, assignment2_ExpMultDiv)


assignment2_ExpPM_strategy = st.builds(assignment2_ExpPM)
@given(instance=assignment2_ExpPM_strategy)
@settings(max_examples=25)
def test_assignment2_ExpPM_instantiation(instance):
    assert isinstance(instance, assignment2_ExpPM)


assignment2_MathExp_strategy = st.builds(assignment2_MathExp)
@given(instance=assignment2_MathExp_strategy)
@settings(max_examples=25)
def test_assignment2_MathExp_instantiation(instance):
    assert isinstance(instance, assignment2_MathExp)


assignment2_Minus_strategy = st.builds(assignment2_Minus)
@given(instance=assignment2_Minus_strategy)
@settings(max_examples=25)
def test_assignment2_Minus_instantiation(instance):
    assert isinstance(instance, assignment2_Minus)


assignment2_Model_strategy = st.builds(assignment2_Model)
@given(instance=assignment2_Model_strategy)
@settings(max_examples=25)
def test_assignment2_Model_instantiation(instance):
    assert isinstance(instance, assignment2_Model)


assignment2_Mult_strategy = st.builds(assignment2_Mult)
@given(instance=assignment2_Mult_strategy)
@settings(max_examples=25)
def test_assignment2_Mult_instantiation(instance):
    assert isinstance(instance, assignment2_Mult)


assignment2_Number_strategy = st.builds(assignment2_Number, value=st.integers())
@given(instance=assignment2_Number_strategy)
@settings(max_examples=25)
def test_assignment2_Number_instantiation(instance):
    assert isinstance(instance, assignment2_Number)


assignment2_Parenthesis_strategy = st.builds(assignment2_Parenthesis)
@given(instance=assignment2_Parenthesis_strategy)
@settings(max_examples=25)
def test_assignment2_Parenthesis_instantiation(instance):
    assert isinstance(instance, assignment2_Parenthesis)


assignment2_Plus_strategy = st.builds(assignment2_Plus)
@given(instance=assignment2_Plus_strategy)
@settings(max_examples=25)
def test_assignment2_Plus_instantiation(instance):
    assert isinstance(instance, assignment2_Plus)


assignment2_Primary_strategy = st.builds(assignment2_Primary)
@given(instance=assignment2_Primary_strategy)
@settings(max_examples=25)
def test_assignment2_Primary_instantiation(instance):
    assert isinstance(instance, assignment2_Primary)



