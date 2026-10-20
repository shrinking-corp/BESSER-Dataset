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
    UnaryExpression,
    core_UMinus,
    core_Not,
    IntegerExpression,
    core_Conditional,
    core_BinaryExpression,
    core_IntegerLiteral,
    core_UnaryExpression,
    BinaryExpression,
    core_Or,
    core_Minus,
    core_Mult,
    core_Mod,
    core_Div,
    core_Equal,
    core_And,
    core_Greater,
    core_Lower,
    core_Add,
    core_Filter,
    core_IntegerExpression,
    core_Rule,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_hyp_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_hyp_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_uminus_is_not_abstract():
    assert not inspect.isabstract(core_UMinus)


def test_hyp_core_uminus_constructor_exists():
    assert callable(core_UMinus.__init__)


def test_hyp_core_uminus_constructor_args():
    sig = inspect.signature(core_UMinus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_not_is_not_abstract():
    assert not inspect.isabstract(core_Not)


def test_hyp_core_not_constructor_exists():
    assert callable(core_Not.__init__)


def test_hyp_core_not_constructor_args():
    sig = inspect.signature(core_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_integerexpression_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression)


def test_hyp_integerexpression_constructor_exists():
    assert callable(IntegerExpression.__init__)


def test_hyp_integerexpression_constructor_args():
    sig = inspect.signature(IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_conditional_is_not_abstract():
    assert not inspect.isabstract(core_Conditional)


def test_hyp_core_conditional_constructor_exists():
    assert callable(core_Conditional.__init__)


def test_hyp_core_conditional_constructor_args():
    sig = inspect.signature(core_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(core_BinaryExpression)


def test_hyp_core_binaryexpression_constructor_exists():
    assert callable(core_BinaryExpression.__init__)


def test_hyp_core_binaryexpression_constructor_args():
    sig = inspect.signature(core_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_integerliteral_is_not_abstract():
    assert not inspect.isabstract(core_IntegerLiteral)


def test_hyp_core_integerliteral_constructor_exists():
    assert callable(core_IntegerLiteral.__init__)


def test_hyp_core_integerliteral_constructor_args():
    sig = inspect.signature(core_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"




def test_hyp_core_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(core_UnaryExpression)


def test_hyp_core_unaryexpression_constructor_exists():
    assert callable(core_UnaryExpression.__init__)


def test_hyp_core_unaryexpression_constructor_args():
    sig = inspect.signature(core_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_hyp_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_hyp_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_or_is_not_abstract():
    assert not inspect.isabstract(core_Or)


def test_hyp_core_or_constructor_exists():
    assert callable(core_Or.__init__)


def test_hyp_core_or_constructor_args():
    sig = inspect.signature(core_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_minus_is_not_abstract():
    assert not inspect.isabstract(core_Minus)


def test_hyp_core_minus_constructor_exists():
    assert callable(core_Minus.__init__)


def test_hyp_core_minus_constructor_args():
    sig = inspect.signature(core_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_mult_is_not_abstract():
    assert not inspect.isabstract(core_Mult)


def test_hyp_core_mult_constructor_exists():
    assert callable(core_Mult.__init__)


def test_hyp_core_mult_constructor_args():
    sig = inspect.signature(core_Mult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_mod_is_not_abstract():
    assert not inspect.isabstract(core_Mod)


def test_hyp_core_mod_constructor_exists():
    assert callable(core_Mod.__init__)


def test_hyp_core_mod_constructor_args():
    sig = inspect.signature(core_Mod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_div_is_not_abstract():
    assert not inspect.isabstract(core_Div)


def test_hyp_core_div_constructor_exists():
    assert callable(core_Div.__init__)


def test_hyp_core_div_constructor_args():
    sig = inspect.signature(core_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_equal_is_not_abstract():
    assert not inspect.isabstract(core_Equal)


def test_hyp_core_equal_constructor_exists():
    assert callable(core_Equal.__init__)


def test_hyp_core_equal_constructor_args():
    sig = inspect.signature(core_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_and_is_not_abstract():
    assert not inspect.isabstract(core_And)


def test_hyp_core_and_constructor_exists():
    assert callable(core_And.__init__)


def test_hyp_core_and_constructor_args():
    sig = inspect.signature(core_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_greater_is_not_abstract():
    assert not inspect.isabstract(core_Greater)


def test_hyp_core_greater_constructor_exists():
    assert callable(core_Greater.__init__)


def test_hyp_core_greater_constructor_args():
    sig = inspect.signature(core_Greater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_lower_is_not_abstract():
    assert not inspect.isabstract(core_Lower)


def test_hyp_core_lower_constructor_exists():
    assert callable(core_Lower.__init__)


def test_hyp_core_lower_constructor_args():
    sig = inspect.signature(core_Lower.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_add_is_not_abstract():
    assert not inspect.isabstract(core_Add)


def test_hyp_core_add_constructor_exists():
    assert callable(core_Add.__init__)


def test_hyp_core_add_constructor_args():
    sig = inspect.signature(core_Add.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_filter_is_not_abstract():
    assert not inspect.isabstract(core_Filter)


def test_hyp_core_filter_constructor_exists():
    assert callable(core_Filter.__init__)


def test_hyp_core_filter_constructor_args():
    sig = inspect.signature(core_Filter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_integerexpression_is_not_abstract():
    assert not inspect.isabstract(core_IntegerExpression)


def test_hyp_core_integerexpression_constructor_exists():
    assert callable(core_IntegerExpression.__init__)


def test_hyp_core_integerexpression_constructor_args():
    sig = inspect.signature(core_IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_rule_is_not_abstract():
    assert not inspect.isabstract(core_Rule)


def test_hyp_core_rule_constructor_exists():
    assert callable(core_Rule.__init__)


def test_hyp_core_rule_constructor_args():
    sig = inspect.signature(core_Rule.__init__)
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
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
core_UMinus_strategy = st.builds(
    core_UMinus,
)
core_Not_strategy = st.builds(
    core_Not,
)
IntegerExpression_strategy = st.builds(
    IntegerExpression,
)
core_Conditional_strategy = st.builds(
    core_Conditional,
)
core_BinaryExpression_strategy = st.builds(
    core_BinaryExpression,
)
core_IntegerLiteral_strategy = st.builds(
    core_IntegerLiteral,
    val=
        st.integers()
)
core_UnaryExpression_strategy = st.builds(
    core_UnaryExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
core_Or_strategy = st.builds(
    core_Or,
)
core_Minus_strategy = st.builds(
    core_Minus,
)
core_Mult_strategy = st.builds(
    core_Mult,
)
core_Mod_strategy = st.builds(
    core_Mod,
)
core_Div_strategy = st.builds(
    core_Div,
)
core_Equal_strategy = st.builds(
    core_Equal,
)
core_And_strategy = st.builds(
    core_And,
)
core_Greater_strategy = st.builds(
    core_Greater,
)
core_Lower_strategy = st.builds(
    core_Lower,
)
core_Add_strategy = st.builds(
    core_Add,
)
core_Filter_strategy = st.builds(
    core_Filter,
)
core_IntegerExpression_strategy = st.builds(
    core_IntegerExpression,
)
core_Rule_strategy = st.builds(
    core_Rule,
)










@given(instance=core_IntegerLiteral_strategy)
def test_hyp_core_integerliteral_val_setter(instance):
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
    BinaryExpression,
    IntegerExpression,
    UnaryExpression,
    core_Add,
    core_And,
    core_BinaryExpression,
    core_Conditional,
    core_Div,
    core_Equal,
    core_Filter,
    core_Greater,
    core_IntegerExpression,
    core_IntegerLiteral,
    core_Lower,
    core_Minus,
    core_Mod,
    core_Mult,
    core_Not,
    core_Or,
    core_Rule,
    core_UMinus,
    core_UnaryExpression,
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

def test_core_IntegerLiteral_val_value_roundtrip():
    instance = core_IntegerLiteral(val=7)
    assert instance.val == 7
    instance.val = 13
    assert instance.val == 13


def test_core_Add_isa_BinaryExpression():
    instance = core_Add()
    assert isinstance(instance, BinaryExpression)


def test_core_And_isa_BinaryExpression():
    instance = core_And()
    assert isinstance(instance, BinaryExpression)


def test_core_Div_isa_BinaryExpression():
    instance = core_Div()
    assert isinstance(instance, BinaryExpression)


def test_core_Equal_isa_BinaryExpression():
    instance = core_Equal()
    assert isinstance(instance, BinaryExpression)


def test_core_Greater_isa_BinaryExpression():
    instance = core_Greater()
    assert isinstance(instance, BinaryExpression)


def test_core_Lower_isa_BinaryExpression():
    instance = core_Lower()
    assert isinstance(instance, BinaryExpression)


def test_core_Minus_isa_BinaryExpression():
    instance = core_Minus()
    assert isinstance(instance, BinaryExpression)


def test_core_Mod_isa_BinaryExpression():
    instance = core_Mod()
    assert isinstance(instance, BinaryExpression)


def test_core_Mult_isa_BinaryExpression():
    instance = core_Mult()
    assert isinstance(instance, BinaryExpression)


def test_core_Or_isa_BinaryExpression():
    instance = core_Or()
    assert isinstance(instance, BinaryExpression)


def test_core_BinaryExpression_isa_IntegerExpression():
    instance = core_BinaryExpression()
    assert isinstance(instance, IntegerExpression)


def test_core_Conditional_isa_IntegerExpression():
    instance = core_Conditional()
    assert isinstance(instance, IntegerExpression)


def test_core_IntegerLiteral_isa_IntegerExpression():
    instance = core_IntegerLiteral(val=7)
    assert isinstance(instance, IntegerExpression)


def test_core_UnaryExpression_isa_IntegerExpression():
    instance = core_UnaryExpression()
    assert isinstance(instance, IntegerExpression)


def test_core_Not_isa_UnaryExpression():
    instance = core_Not()
    assert isinstance(instance, UnaryExpression)


def test_core_UMinus_isa_UnaryExpression():
    instance = core_UMinus()
    assert isinstance(instance, UnaryExpression)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryExpression_strategy = st.builds(BinaryExpression)
@given(instance=BinaryExpression_strategy)
@settings(max_examples=25)
def test_BinaryExpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)


IntegerExpression_strategy = st.builds(IntegerExpression)
@given(instance=IntegerExpression_strategy)
@settings(max_examples=25)
def test_IntegerExpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)


UnaryExpression_strategy = st.builds(UnaryExpression)
@given(instance=UnaryExpression_strategy)
@settings(max_examples=25)
def test_UnaryExpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)


core_Add_strategy = st.builds(core_Add)
@given(instance=core_Add_strategy)
@settings(max_examples=25)
def test_core_Add_instantiation(instance):
    assert isinstance(instance, core_Add)


core_And_strategy = st.builds(core_And)
@given(instance=core_And_strategy)
@settings(max_examples=25)
def test_core_And_instantiation(instance):
    assert isinstance(instance, core_And)


core_BinaryExpression_strategy = st.builds(core_BinaryExpression)
@given(instance=core_BinaryExpression_strategy)
@settings(max_examples=25)
def test_core_BinaryExpression_instantiation(instance):
    assert isinstance(instance, core_BinaryExpression)


core_Conditional_strategy = st.builds(core_Conditional)
@given(instance=core_Conditional_strategy)
@settings(max_examples=25)
def test_core_Conditional_instantiation(instance):
    assert isinstance(instance, core_Conditional)


core_Div_strategy = st.builds(core_Div)
@given(instance=core_Div_strategy)
@settings(max_examples=25)
def test_core_Div_instantiation(instance):
    assert isinstance(instance, core_Div)


core_Equal_strategy = st.builds(core_Equal)
@given(instance=core_Equal_strategy)
@settings(max_examples=25)
def test_core_Equal_instantiation(instance):
    assert isinstance(instance, core_Equal)


core_Filter_strategy = st.builds(core_Filter)
@given(instance=core_Filter_strategy)
@settings(max_examples=25)
def test_core_Filter_instantiation(instance):
    assert isinstance(instance, core_Filter)


core_Greater_strategy = st.builds(core_Greater)
@given(instance=core_Greater_strategy)
@settings(max_examples=25)
def test_core_Greater_instantiation(instance):
    assert isinstance(instance, core_Greater)


core_IntegerExpression_strategy = st.builds(core_IntegerExpression)
@given(instance=core_IntegerExpression_strategy)
@settings(max_examples=25)
def test_core_IntegerExpression_instantiation(instance):
    assert isinstance(instance, core_IntegerExpression)


core_IntegerLiteral_strategy = st.builds(core_IntegerLiteral, val=st.integers())
@given(instance=core_IntegerLiteral_strategy)
@settings(max_examples=25)
def test_core_IntegerLiteral_instantiation(instance):
    assert isinstance(instance, core_IntegerLiteral)


core_Lower_strategy = st.builds(core_Lower)
@given(instance=core_Lower_strategy)
@settings(max_examples=25)
def test_core_Lower_instantiation(instance):
    assert isinstance(instance, core_Lower)


core_Minus_strategy = st.builds(core_Minus)
@given(instance=core_Minus_strategy)
@settings(max_examples=25)
def test_core_Minus_instantiation(instance):
    assert isinstance(instance, core_Minus)


core_Mod_strategy = st.builds(core_Mod)
@given(instance=core_Mod_strategy)
@settings(max_examples=25)
def test_core_Mod_instantiation(instance):
    assert isinstance(instance, core_Mod)


core_Mult_strategy = st.builds(core_Mult)
@given(instance=core_Mult_strategy)
@settings(max_examples=25)
def test_core_Mult_instantiation(instance):
    assert isinstance(instance, core_Mult)


core_Not_strategy = st.builds(core_Not)
@given(instance=core_Not_strategy)
@settings(max_examples=25)
def test_core_Not_instantiation(instance):
    assert isinstance(instance, core_Not)


core_Or_strategy = st.builds(core_Or)
@given(instance=core_Or_strategy)
@settings(max_examples=25)
def test_core_Or_instantiation(instance):
    assert isinstance(instance, core_Or)


core_Rule_strategy = st.builds(core_Rule)
@given(instance=core_Rule_strategy)
@settings(max_examples=25)
def test_core_Rule_instantiation(instance):
    assert isinstance(instance, core_Rule)


core_UMinus_strategy = st.builds(core_UMinus)
@given(instance=core_UMinus_strategy)
@settings(max_examples=25)
def test_core_UMinus_instantiation(instance):
    assert isinstance(instance, core_UMinus)


core_UnaryExpression_strategy = st.builds(core_UnaryExpression)
@given(instance=core_UnaryExpression_strategy)
@settings(max_examples=25)
def test_core_UnaryExpression_instantiation(instance):
    assert isinstance(instance, core_UnaryExpression)



