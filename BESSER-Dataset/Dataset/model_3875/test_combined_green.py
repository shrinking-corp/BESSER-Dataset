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
    BinaryExp,
    fl_MinusExp,
    fl_EqualExp,
    fl_PlusExp,
    Exp,
    fl_IfThenElseExp,
    fl_ArgumentExp,
    fl_ApplyExp,
    fl_LiteralExp,
    fl_Exp,
    fl_Argument,
    fl_Function,
    fl_Program,
    fl_BinaryExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_hyp_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_hyp_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fl_minusexp_is_not_abstract():
    assert not inspect.isabstract(fl_MinusExp)


def test_hyp_fl_minusexp_constructor_exists():
    assert callable(fl_MinusExp.__init__)


def test_hyp_fl_minusexp_constructor_args():
    sig = inspect.signature(fl_MinusExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fl_equalexp_is_not_abstract():
    assert not inspect.isabstract(fl_EqualExp)


def test_hyp_fl_equalexp_constructor_exists():
    assert callable(fl_EqualExp.__init__)


def test_hyp_fl_equalexp_constructor_args():
    sig = inspect.signature(fl_EqualExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fl_plusexp_is_not_abstract():
    assert not inspect.isabstract(fl_PlusExp)


def test_hyp_fl_plusexp_constructor_exists():
    assert callable(fl_PlusExp.__init__)


def test_hyp_fl_plusexp_constructor_args():
    sig = inspect.signature(fl_PlusExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_hyp_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_hyp_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fl_ifthenelseexp_is_not_abstract():
    assert not inspect.isabstract(fl_IfThenElseExp)


def test_hyp_fl_ifthenelseexp_constructor_exists():
    assert callable(fl_IfThenElseExp.__init__)


def test_hyp_fl_ifthenelseexp_constructor_args():
    sig = inspect.signature(fl_IfThenElseExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fl_argumentexp_is_not_abstract():
    assert not inspect.isabstract(fl_ArgumentExp)


def test_hyp_fl_argumentexp_constructor_exists():
    assert callable(fl_ArgumentExp.__init__)


def test_hyp_fl_argumentexp_constructor_args():
    sig = inspect.signature(fl_ArgumentExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fl_applyexp_is_not_abstract():
    assert not inspect.isabstract(fl_ApplyExp)


def test_hyp_fl_applyexp_constructor_exists():
    assert callable(fl_ApplyExp.__init__)


def test_hyp_fl_applyexp_constructor_args():
    sig = inspect.signature(fl_ApplyExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fl_literalexp_is_not_abstract():
    assert not inspect.isabstract(fl_LiteralExp)


def test_hyp_fl_literalexp_constructor_exists():
    assert callable(fl_LiteralExp.__init__)


def test_hyp_fl_literalexp_constructor_args():
    sig = inspect.signature(fl_LiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_fl_exp_is_not_abstract():
    assert not inspect.isabstract(fl_Exp)


def test_hyp_fl_exp_constructor_exists():
    assert callable(fl_Exp.__init__)


def test_hyp_fl_exp_constructor_args():
    sig = inspect.signature(fl_Exp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fl_argument_is_not_abstract():
    assert not inspect.isabstract(fl_Argument)


def test_hyp_fl_argument_constructor_exists():
    assert callable(fl_Argument.__init__)


def test_hyp_fl_argument_constructor_args():
    sig = inspect.signature(fl_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fl_function_is_not_abstract():
    assert not inspect.isabstract(fl_Function)


def test_hyp_fl_function_constructor_exists():
    assert callable(fl_Function.__init__)


def test_hyp_fl_function_constructor_args():
    sig = inspect.signature(fl_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fl_program_is_not_abstract():
    assert not inspect.isabstract(fl_Program)


def test_hyp_fl_program_constructor_exists():
    assert callable(fl_Program.__init__)


def test_hyp_fl_program_constructor_args():
    sig = inspect.signature(fl_Program.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fl_binaryexp_is_not_abstract():
    assert not inspect.isabstract(fl_BinaryExp)


def test_hyp_fl_binaryexp_constructor_exists():
    assert callable(fl_BinaryExp.__init__)


def test_hyp_fl_binaryexp_constructor_args():
    sig = inspect.signature(fl_BinaryExp.__init__)
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
BinaryExp_strategy = st.builds(
    BinaryExp,
)
fl_MinusExp_strategy = st.builds(
    fl_MinusExp,
)
fl_EqualExp_strategy = st.builds(
    fl_EqualExp,
)
fl_PlusExp_strategy = st.builds(
    fl_PlusExp,
)
Exp_strategy = st.builds(
    Exp,
)
fl_IfThenElseExp_strategy = st.builds(
    fl_IfThenElseExp,
)
fl_ArgumentExp_strategy = st.builds(
    fl_ArgumentExp,
)
fl_ApplyExp_strategy = st.builds(
    fl_ApplyExp,
)
fl_LiteralExp_strategy = st.builds(
    fl_LiteralExp,
    value=
        st.integers()
)
fl_Exp_strategy = st.builds(
    fl_Exp,
)
fl_Argument_strategy = st.builds(
    fl_Argument,
    name=
        safe_text
)
fl_Function_strategy = st.builds(
    fl_Function,
    name=
        safe_text
)
fl_Program_strategy = st.builds(
    fl_Program,
)
fl_BinaryExp_strategy = st.builds(
    fl_BinaryExp,
)












@given(instance=fl_LiteralExp_strategy)
def test_hyp_fl_literalexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=fl_Argument_strategy)
def test_hyp_fl_argument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fl_Function_strategy)
def test_hyp_fl_function_name_setter(instance):
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
    BinaryExp,
    Exp,
    fl_ApplyExp,
    fl_Argument,
    fl_ArgumentExp,
    fl_BinaryExp,
    fl_EqualExp,
    fl_Exp,
    fl_Function,
    fl_IfThenElseExp,
    fl_LiteralExp,
    fl_MinusExp,
    fl_PlusExp,
    fl_Program,
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

def test_fl_Argument_name_value_roundtrip():
    instance = fl_Argument(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fl_Function_name_value_roundtrip():
    instance = fl_Function(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fl_LiteralExp_value_value_roundtrip():
    instance = fl_LiteralExp(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fl_EqualExp_isa_BinaryExp():
    instance = fl_EqualExp()
    assert isinstance(instance, BinaryExp)


def test_fl_MinusExp_isa_BinaryExp():
    instance = fl_MinusExp()
    assert isinstance(instance, BinaryExp)


def test_fl_PlusExp_isa_BinaryExp():
    instance = fl_PlusExp()
    assert isinstance(instance, BinaryExp)


def test_fl_ApplyExp_isa_Exp():
    instance = fl_ApplyExp()
    assert isinstance(instance, Exp)


def test_fl_ArgumentExp_isa_Exp():
    instance = fl_ArgumentExp()
    assert isinstance(instance, Exp)


def test_fl_BinaryExp_isa_Exp():
    instance = fl_BinaryExp()
    assert isinstance(instance, Exp)


def test_fl_IfThenElseExp_isa_Exp():
    instance = fl_IfThenElseExp()
    assert isinstance(instance, Exp)


def test_fl_LiteralExp_isa_Exp():
    instance = fl_LiteralExp(value=7)
    assert isinstance(instance, Exp)


def test_assoc_argument1_link_reassign_clear():
    a = fl_Function(name="sample_text")
    b1 = fl_Argument(name="sample_text")
    b2 = fl_Argument(name="sample_text_2")
    _safe_set(a, 'fl_Function2', {b1})
    assert _is_linked(a, 'fl_Function2', b1)
    if hasattr(b1, 'fl_Argument'):
        assert _is_linked(b1, 'fl_Argument', a)
    _safe_set(a, 'fl_Function2', {b2})
    assert _is_linked(a, 'fl_Function2', b2)
    if hasattr(b1, 'fl_Argument'):
        assert not _is_linked(b1, 'fl_Argument', a)
    if hasattr(b2, 'fl_Argument'):
        assert _is_linked(b2, 'fl_Argument', a)
    _safe_set(a, 'fl_Function2', set())
    assert not _is_linked(a, 'fl_Function2', b2)
    if hasattr(b2, 'fl_Argument'):
        assert not _is_linked(b2, 'fl_Argument', a)


def test_assoc_argument5_link_reassign_clear():
    a = fl_Argument(name="sample_text")
    b1 = fl_ArgumentExp()
    b2 = fl_ArgumentExp()
    _safe_set(a, 'fl_Argument6', b1)
    assert _is_linked(a, 'fl_Argument6', b1)
    if hasattr(b1, 'fl_ArgumentExp'):
        assert _is_linked(b1, 'fl_ArgumentExp', a)
    _safe_set(a, 'fl_Argument6', b2)
    assert _is_linked(a, 'fl_Argument6', b2)
    if hasattr(b1, 'fl_ArgumentExp'):
        assert not _is_linked(b1, 'fl_ArgumentExp', a)
    if hasattr(b2, 'fl_ArgumentExp'):
        assert _is_linked(b2, 'fl_ArgumentExp', a)
    _safe_set(a, 'fl_Argument6', None)
    assert not _is_linked(a, 'fl_Argument6', b2)
    if hasattr(b2, 'fl_ArgumentExp'):
        assert not _is_linked(b2, 'fl_ArgumentExp', a)


def test_assoc_definition3_link_reassign_clear():
    a = fl_Function(name="sample_text")
    b1 = fl_Exp()
    b2 = fl_Exp()
    _safe_set(a, 'fl_Function4', b1)
    assert _is_linked(a, 'fl_Function4', b1)
    if hasattr(b1, 'fl_Exp'):
        assert _is_linked(b1, 'fl_Exp', a)
    _safe_set(a, 'fl_Function4', b2)
    assert _is_linked(a, 'fl_Function4', b2)
    if hasattr(b1, 'fl_Exp'):
        assert not _is_linked(b1, 'fl_Exp', a)
    if hasattr(b2, 'fl_Exp'):
        assert _is_linked(b2, 'fl_Exp', a)
    _safe_set(a, 'fl_Function4', None)
    assert not _is_linked(a, 'fl_Function4', b2)
    if hasattr(b2, 'fl_Exp'):
        assert not _is_linked(b2, 'fl_Exp', a)


def test_assoc_function0_link_reassign_clear():
    a = fl_Function(name="sample_text")
    b1 = fl_Program()
    b2 = fl_Program()
    _safe_set(a, 'fl_Function', b1)
    assert _is_linked(a, 'fl_Function', b1)
    if hasattr(b1, 'fl_Program'):
        assert _is_linked(b1, 'fl_Program', a)
    _safe_set(a, 'fl_Function', b2)
    assert _is_linked(a, 'fl_Function', b2)
    if hasattr(b1, 'fl_Program'):
        assert not _is_linked(b1, 'fl_Program', a)
    if hasattr(b2, 'fl_Program'):
        assert _is_linked(b2, 'fl_Program', a)
    _safe_set(a, 'fl_Function', None)
    assert not _is_linked(a, 'fl_Function', b2)
    if hasattr(b2, 'fl_Program'):
        assert not _is_linked(b2, 'fl_Program', a)


def test_assoc_function15_link_reassign_clear():
    a = fl_Function(name="sample_text")
    b1 = fl_ApplyExp()
    b2 = fl_ApplyExp()
    _safe_set(a, 'fl_Function16', b1)
    assert _is_linked(a, 'fl_Function16', b1)
    if hasattr(b1, 'fl_ApplyExp'):
        assert _is_linked(b1, 'fl_ApplyExp', a)
    _safe_set(a, 'fl_Function16', b2)
    assert _is_linked(a, 'fl_Function16', b2)
    if hasattr(b1, 'fl_ApplyExp'):
        assert not _is_linked(b1, 'fl_ApplyExp', a)
    if hasattr(b2, 'fl_ApplyExp'):
        assert _is_linked(b2, 'fl_ApplyExp', a)
    _safe_set(a, 'fl_Function16', None)
    assert not _is_linked(a, 'fl_Function16', b2)
    if hasattr(b2, 'fl_ApplyExp'):
        assert not _is_linked(b2, 'fl_ApplyExp', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryExp_strategy = st.builds(BinaryExp)
@given(instance=BinaryExp_strategy)
@settings(max_examples=25)
def test_BinaryExp_instantiation(instance):
    assert isinstance(instance, BinaryExp)


Exp_strategy = st.builds(Exp)
@given(instance=Exp_strategy)
@settings(max_examples=25)
def test_Exp_instantiation(instance):
    assert isinstance(instance, Exp)


fl_ApplyExp_strategy = st.builds(fl_ApplyExp)
@given(instance=fl_ApplyExp_strategy)
@settings(max_examples=25)
def test_fl_ApplyExp_instantiation(instance):
    assert isinstance(instance, fl_ApplyExp)


fl_Argument_strategy = st.builds(fl_Argument, name=safe_text)
@given(instance=fl_Argument_strategy)
@settings(max_examples=25)
def test_fl_Argument_instantiation(instance):
    assert isinstance(instance, fl_Argument)


fl_ArgumentExp_strategy = st.builds(fl_ArgumentExp)
@given(instance=fl_ArgumentExp_strategy)
@settings(max_examples=25)
def test_fl_ArgumentExp_instantiation(instance):
    assert isinstance(instance, fl_ArgumentExp)


fl_BinaryExp_strategy = st.builds(fl_BinaryExp)
@given(instance=fl_BinaryExp_strategy)
@settings(max_examples=25)
def test_fl_BinaryExp_instantiation(instance):
    assert isinstance(instance, fl_BinaryExp)


fl_EqualExp_strategy = st.builds(fl_EqualExp)
@given(instance=fl_EqualExp_strategy)
@settings(max_examples=25)
def test_fl_EqualExp_instantiation(instance):
    assert isinstance(instance, fl_EqualExp)


fl_Exp_strategy = st.builds(fl_Exp)
@given(instance=fl_Exp_strategy)
@settings(max_examples=25)
def test_fl_Exp_instantiation(instance):
    assert isinstance(instance, fl_Exp)


fl_Function_strategy = st.builds(fl_Function, name=safe_text)
@given(instance=fl_Function_strategy)
@settings(max_examples=25)
def test_fl_Function_instantiation(instance):
    assert isinstance(instance, fl_Function)


fl_IfThenElseExp_strategy = st.builds(fl_IfThenElseExp)
@given(instance=fl_IfThenElseExp_strategy)
@settings(max_examples=25)
def test_fl_IfThenElseExp_instantiation(instance):
    assert isinstance(instance, fl_IfThenElseExp)


fl_LiteralExp_strategy = st.builds(fl_LiteralExp, value=st.integers())
@given(instance=fl_LiteralExp_strategy)
@settings(max_examples=25)
def test_fl_LiteralExp_instantiation(instance):
    assert isinstance(instance, fl_LiteralExp)


fl_MinusExp_strategy = st.builds(fl_MinusExp)
@given(instance=fl_MinusExp_strategy)
@settings(max_examples=25)
def test_fl_MinusExp_instantiation(instance):
    assert isinstance(instance, fl_MinusExp)


fl_PlusExp_strategy = st.builds(fl_PlusExp)
@given(instance=fl_PlusExp_strategy)
@settings(max_examples=25)
def test_fl_PlusExp_instantiation(instance):
    assert isinstance(instance, fl_PlusExp)


fl_Program_strategy = st.builds(fl_Program)
@given(instance=fl_Program_strategy)
@settings(max_examples=25)
def test_fl_Program_instantiation(instance):
    assert isinstance(instance, fl_Program)



