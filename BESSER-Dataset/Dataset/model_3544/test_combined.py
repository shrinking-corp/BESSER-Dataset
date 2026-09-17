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
    multipleinheritence_NewEClass2,
    NewEClass3,
    NewEClass2,
    multipleinheritence_NewEClass1,
    multipleinheritence_NewEClass5,
    multipleinheritence_NewEClass4,
    NewEClass5,
    NewEClass4,
    multipleinheritence_NewEClass3,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_multipleinheritence_neweclass2_is_not_abstract():
    assert not inspect.isabstract(multipleinheritence_NewEClass2)


def test_hyp_multipleinheritence_neweclass2_constructor_exists():
    assert callable(multipleinheritence_NewEClass2.__init__)


def test_hyp_multipleinheritence_neweclass2_constructor_args():
    sig = inspect.signature(multipleinheritence_NewEClass2.__init__)
    params = list(sig.parameters.keys())
    assert "f2" in params, "Missing parameter 'f2'"




def test_hyp_neweclass3_is_not_abstract():
    assert not inspect.isabstract(NewEClass3)


def test_hyp_neweclass3_constructor_exists():
    assert callable(NewEClass3.__init__)


def test_hyp_neweclass3_constructor_args():
    sig = inspect.signature(NewEClass3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_neweclass2_is_not_abstract():
    assert not inspect.isabstract(NewEClass2)


def test_hyp_neweclass2_constructor_exists():
    assert callable(NewEClass2.__init__)


def test_hyp_neweclass2_constructor_args():
    sig = inspect.signature(NewEClass2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multipleinheritence_neweclass1_is_not_abstract():
    assert not inspect.isabstract(multipleinheritence_NewEClass1)


def test_hyp_multipleinheritence_neweclass1_constructor_exists():
    assert callable(multipleinheritence_NewEClass1.__init__)


def test_hyp_multipleinheritence_neweclass1_constructor_args():
    sig = inspect.signature(multipleinheritence_NewEClass1.__init__)
    params = list(sig.parameters.keys())
    assert "f1" in params, "Missing parameter 'f1'"




def test_hyp_multipleinheritence_neweclass5_is_not_abstract():
    assert not inspect.isabstract(multipleinheritence_NewEClass5)


def test_hyp_multipleinheritence_neweclass5_constructor_exists():
    assert callable(multipleinheritence_NewEClass5.__init__)


def test_hyp_multipleinheritence_neweclass5_constructor_args():
    sig = inspect.signature(multipleinheritence_NewEClass5.__init__)
    params = list(sig.parameters.keys())
    assert "f5" in params, "Missing parameter 'f5'"




def test_hyp_multipleinheritence_neweclass4_is_not_abstract():
    assert not inspect.isabstract(multipleinheritence_NewEClass4)


def test_hyp_multipleinheritence_neweclass4_constructor_exists():
    assert callable(multipleinheritence_NewEClass4.__init__)


def test_hyp_multipleinheritence_neweclass4_constructor_args():
    sig = inspect.signature(multipleinheritence_NewEClass4.__init__)
    params = list(sig.parameters.keys())
    assert "f4" in params, "Missing parameter 'f4'"




def test_hyp_neweclass5_is_not_abstract():
    assert not inspect.isabstract(NewEClass5)


def test_hyp_neweclass5_constructor_exists():
    assert callable(NewEClass5.__init__)


def test_hyp_neweclass5_constructor_args():
    sig = inspect.signature(NewEClass5.__init__)
    params = list(sig.parameters.keys())



def test_hyp_neweclass4_is_not_abstract():
    assert not inspect.isabstract(NewEClass4)


def test_hyp_neweclass4_constructor_exists():
    assert callable(NewEClass4.__init__)


def test_hyp_neweclass4_constructor_args():
    sig = inspect.signature(NewEClass4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multipleinheritence_neweclass3_is_not_abstract():
    assert not inspect.isabstract(multipleinheritence_NewEClass3)


def test_hyp_multipleinheritence_neweclass3_constructor_exists():
    assert callable(multipleinheritence_NewEClass3.__init__)


def test_hyp_multipleinheritence_neweclass3_constructor_args():
    sig = inspect.signature(multipleinheritence_NewEClass3.__init__)
    params = list(sig.parameters.keys())
    assert "f3" in params, "Missing parameter 'f3'"



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
multipleinheritence_NewEClass2_strategy = st.builds(
    multipleinheritence_NewEClass2,
    f2=
        st.integers()
)
NewEClass3_strategy = st.builds(
    NewEClass3,
)
NewEClass2_strategy = st.builds(
    NewEClass2,
)
multipleinheritence_NewEClass1_strategy = st.builds(
    multipleinheritence_NewEClass1,
    f1=
        st.integers()
)
multipleinheritence_NewEClass5_strategy = st.builds(
    multipleinheritence_NewEClass5,
    f5=
        st.integers()
)
multipleinheritence_NewEClass4_strategy = st.builds(
    multipleinheritence_NewEClass4,
    f4=
        st.integers()
)
NewEClass5_strategy = st.builds(
    NewEClass5,
)
NewEClass4_strategy = st.builds(
    NewEClass4,
)
multipleinheritence_NewEClass3_strategy = st.builds(
    multipleinheritence_NewEClass3,
    f3=
        st.integers()
)




@given(instance=multipleinheritence_NewEClass2_strategy)
def test_hyp_multipleinheritence_neweclass2_f2_setter(instance):
    original = instance.f2
    instance.f2 = original
    assert instance.f2 == original






@given(instance=multipleinheritence_NewEClass1_strategy)
def test_hyp_multipleinheritence_neweclass1_f1_setter(instance):
    original = instance.f1
    instance.f1 = original
    assert instance.f1 == original




@given(instance=multipleinheritence_NewEClass5_strategy)
def test_hyp_multipleinheritence_neweclass5_f5_setter(instance):
    original = instance.f5
    instance.f5 = original
    assert instance.f5 == original




@given(instance=multipleinheritence_NewEClass4_strategy)
def test_hyp_multipleinheritence_neweclass4_f4_setter(instance):
    original = instance.f4
    instance.f4 = original
    assert instance.f4 == original






@given(instance=multipleinheritence_NewEClass3_strategy)
def test_hyp_multipleinheritence_neweclass3_f3_setter(instance):
    original = instance.f3
    instance.f3 = original
    assert instance.f3 == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NewEClass2,
    NewEClass3,
    NewEClass4,
    NewEClass5,
    multipleinheritence_NewEClass1,
    multipleinheritence_NewEClass2,
    multipleinheritence_NewEClass3,
    multipleinheritence_NewEClass4,
    multipleinheritence_NewEClass5,
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

def test_multipleinheritence_NewEClass1_f1_value_roundtrip():
    instance = multipleinheritence_NewEClass1(f1=7)
    assert instance.f1 == 7
    instance.f1 = 13
    assert instance.f1 == 13


def test_multipleinheritence_NewEClass2_f2_value_roundtrip():
    instance = multipleinheritence_NewEClass2(f2=7)
    assert instance.f2 == 7
    instance.f2 = 13
    assert instance.f2 == 13


def test_multipleinheritence_NewEClass3_f3_value_roundtrip():
    instance = multipleinheritence_NewEClass3(f3=7)
    assert instance.f3 == 7
    instance.f3 = 13
    assert instance.f3 == 13


def test_multipleinheritence_NewEClass4_f4_value_roundtrip():
    instance = multipleinheritence_NewEClass4(f4=7)
    assert instance.f4 == 7
    instance.f4 = 13
    assert instance.f4 == 13


def test_multipleinheritence_NewEClass5_f5_value_roundtrip():
    instance = multipleinheritence_NewEClass5(f5=7)
    assert instance.f5 == 7
    instance.f5 = 13
    assert instance.f5 == 13


def test_multipleinheritence_NewEClass1_isa_NewEClass2():
    instance = multipleinheritence_NewEClass1(f1=7)
    assert isinstance(instance, NewEClass2)


def test_multipleinheritence_NewEClass1_isa_NewEClass3():
    instance = multipleinheritence_NewEClass1(f1=7)
    assert isinstance(instance, NewEClass3)


def test_multipleinheritence_NewEClass3_isa_NewEClass4():
    instance = multipleinheritence_NewEClass3(f3=7)
    assert isinstance(instance, NewEClass4)


def test_multipleinheritence_NewEClass3_isa_NewEClass5():
    instance = multipleinheritence_NewEClass3(f3=7)
    assert isinstance(instance, NewEClass5)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NewEClass2_strategy = st.builds(NewEClass2)
@given(instance=NewEClass2_strategy)
@settings(max_examples=25)
def test_NewEClass2_instantiation(instance):
    assert isinstance(instance, NewEClass2)


NewEClass3_strategy = st.builds(NewEClass3)
@given(instance=NewEClass3_strategy)
@settings(max_examples=25)
def test_NewEClass3_instantiation(instance):
    assert isinstance(instance, NewEClass3)


NewEClass4_strategy = st.builds(NewEClass4)
@given(instance=NewEClass4_strategy)
@settings(max_examples=25)
def test_NewEClass4_instantiation(instance):
    assert isinstance(instance, NewEClass4)


NewEClass5_strategy = st.builds(NewEClass5)
@given(instance=NewEClass5_strategy)
@settings(max_examples=25)
def test_NewEClass5_instantiation(instance):
    assert isinstance(instance, NewEClass5)


multipleinheritence_NewEClass1_strategy = st.builds(multipleinheritence_NewEClass1, f1=st.integers())
@given(instance=multipleinheritence_NewEClass1_strategy)
@settings(max_examples=25)
def test_multipleinheritence_NewEClass1_instantiation(instance):
    assert isinstance(instance, multipleinheritence_NewEClass1)


multipleinheritence_NewEClass2_strategy = st.builds(multipleinheritence_NewEClass2, f2=st.integers())
@given(instance=multipleinheritence_NewEClass2_strategy)
@settings(max_examples=25)
def test_multipleinheritence_NewEClass2_instantiation(instance):
    assert isinstance(instance, multipleinheritence_NewEClass2)


multipleinheritence_NewEClass3_strategy = st.builds(multipleinheritence_NewEClass3, f3=st.integers())
@given(instance=multipleinheritence_NewEClass3_strategy)
@settings(max_examples=25)
def test_multipleinheritence_NewEClass3_instantiation(instance):
    assert isinstance(instance, multipleinheritence_NewEClass3)


multipleinheritence_NewEClass4_strategy = st.builds(multipleinheritence_NewEClass4, f4=st.integers())
@given(instance=multipleinheritence_NewEClass4_strategy)
@settings(max_examples=25)
def test_multipleinheritence_NewEClass4_instantiation(instance):
    assert isinstance(instance, multipleinheritence_NewEClass4)


multipleinheritence_NewEClass5_strategy = st.builds(multipleinheritence_NewEClass5, f5=st.integers())
@given(instance=multipleinheritence_NewEClass5_strategy)
@settings(max_examples=25)
def test_multipleinheritence_NewEClass5_instantiation(instance):
    assert isinstance(instance, multipleinheritence_NewEClass5)



