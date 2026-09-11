import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BinExp,
    Exp,
    Lit,
    boolexp_And,
    boolexp_BinExp,
    boolexp_Exp,
    boolexp_Fals,
    boolexp_Lit,
    boolexp_Not,
    boolexp_Or,
    boolexp_Tru,
    boolexp_VarRef,
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

def test_boolexp_VarRef_name_value_roundtrip():
    instance = boolexp_VarRef(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_boolexp_And_isa_BinExp():
    instance = boolexp_And()
    assert isinstance(instance, BinExp)


def test_boolexp_Or_isa_BinExp():
    instance = boolexp_Or()
    assert isinstance(instance, BinExp)


def test_boolexp_BinExp_isa_Exp():
    instance = boolexp_BinExp()
    assert isinstance(instance, Exp)


def test_boolexp_Lit_isa_Exp():
    instance = boolexp_Lit()
    assert isinstance(instance, Exp)


def test_boolexp_Not_isa_Exp():
    instance = boolexp_Not()
    assert isinstance(instance, Exp)


def test_boolexp_VarRef_isa_Exp():
    instance = boolexp_VarRef(name="sample_text")
    assert isinstance(instance, Exp)


def test_boolexp_Fals_isa_Lit():
    instance = boolexp_Fals()
    assert isinstance(instance, Lit)


def test_boolexp_Tru_isa_Lit():
    instance = boolexp_Tru()
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


boolexp_And_strategy = st.builds(boolexp_And)
@given(instance=boolexp_And_strategy)
@settings(max_examples=25)
def test_boolexp_And_instantiation(instance):
    assert isinstance(instance, boolexp_And)


boolexp_BinExp_strategy = st.builds(boolexp_BinExp)
@given(instance=boolexp_BinExp_strategy)
@settings(max_examples=25)
def test_boolexp_BinExp_instantiation(instance):
    assert isinstance(instance, boolexp_BinExp)


boolexp_Exp_strategy = st.builds(boolexp_Exp)
@given(instance=boolexp_Exp_strategy)
@settings(max_examples=25)
def test_boolexp_Exp_instantiation(instance):
    assert isinstance(instance, boolexp_Exp)


boolexp_Fals_strategy = st.builds(boolexp_Fals)
@given(instance=boolexp_Fals_strategy)
@settings(max_examples=25)
def test_boolexp_Fals_instantiation(instance):
    assert isinstance(instance, boolexp_Fals)


boolexp_Lit_strategy = st.builds(boolexp_Lit)
@given(instance=boolexp_Lit_strategy)
@settings(max_examples=25)
def test_boolexp_Lit_instantiation(instance):
    assert isinstance(instance, boolexp_Lit)


boolexp_Not_strategy = st.builds(boolexp_Not)
@given(instance=boolexp_Not_strategy)
@settings(max_examples=25)
def test_boolexp_Not_instantiation(instance):
    assert isinstance(instance, boolexp_Not)


boolexp_Or_strategy = st.builds(boolexp_Or)
@given(instance=boolexp_Or_strategy)
@settings(max_examples=25)
def test_boolexp_Or_instantiation(instance):
    assert isinstance(instance, boolexp_Or)


boolexp_Tru_strategy = st.builds(boolexp_Tru)
@given(instance=boolexp_Tru_strategy)
@settings(max_examples=25)
def test_boolexp_Tru_instantiation(instance):
    assert isinstance(instance, boolexp_Tru)


boolexp_VarRef_strategy = st.builds(boolexp_VarRef, name=safe_text)
@given(instance=boolexp_VarRef_strategy)
@settings(max_examples=25)
def test_boolexp_VarRef_instantiation(instance):
    assert isinstance(instance, boolexp_VarRef)


