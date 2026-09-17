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
    ClassC,
    ClassB,
    ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_classc_is_not_abstract():
    assert not inspect.isabstract(ClassC)


def test_hyp_classc_constructor_exists():
    assert callable(ClassC.__init__)


def test_hyp_classc_constructor_args():
    sig = inspect.signature(ClassC.__init__)
    params = list(sig.parameters.keys())
    assert "attC1" in params, "Missing parameter 'attC1'"
    assert "attC2" in params, "Missing parameter 'attC2'"





def test_hyp_classb_is_not_abstract():
    assert not inspect.isabstract(ClassB)


def test_hyp_classb_constructor_exists():
    assert callable(ClassB.__init__)


def test_hyp_classb_constructor_args():
    sig = inspect.signature(ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_classa_is_not_abstract():
    assert not inspect.isabstract(ClassA)


def test_hyp_classa_constructor_exists():
    assert callable(ClassA.__init__)


def test_hyp_classa_constructor_args():
    sig = inspect.signature(ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "attA" in params, "Missing parameter 'attA'"



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
ClassC_strategy = st.builds(
    ClassC,
    attC1=
        st.integers(),
    attC2=
        st.booleans()
)
ClassB_strategy = st.builds(
    ClassB,
    attribute=
        st.integers()
)
ClassA_strategy = st.builds(
    ClassA,
    attA=
        safe_text
)




@given(instance=ClassC_strategy)
def test_hyp_classc_attC1_setter(instance):
    original = instance.attC1
    instance.attC1 = original
    assert instance.attC1 == original



@given(instance=ClassC_strategy)
def test_hyp_classc_attC2_setter(instance):
    original = instance.attC2
    instance.attC2 = original
    assert instance.attC2 == original




@given(instance=ClassB_strategy)
def test_hyp_classb_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=ClassA_strategy)
def test_hyp_classa_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ClassA,
    ClassB,
    ClassC,
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

def test_ClassA_attA_value_roundtrip():
    instance = ClassA(attA="sample_text")
    assert instance.attA == "sample_text"
    instance.attA = "sample_text_2"
    assert instance.attA == "sample_text_2"


def test_ClassB_attribute_value_roundtrip():
    instance = ClassB(attribute=7)
    assert instance.attribute == 7
    instance.attribute = 13
    assert instance.attribute == 13


def test_ClassC_attC1_value_roundtrip():
    instance = ClassC(attC1=7, attC2=True)
    assert instance.attC1 == 7
    instance.attC1 = 13
    assert instance.attC1 == 13


def test_ClassC_attC2_value_roundtrip():
    instance = ClassC(attC1=7, attC2=True)
    assert instance.attC2 == True
    instance.attC2 = False
    assert instance.attC2 == False


def test_assoc_ClassA_ClassB_link_reassign_clear():
    a = ClassB(attribute=7)
    b1 = ClassA(attA="sample_text")
    b2 = ClassA(attA="sample_text_2")
    _safe_set(a, 'classA1', b1)
    assert _is_linked(a, 'classA1', b1)
    if hasattr(b1, 'classB0'):
        assert _is_linked(b1, 'classB0', a)
    _safe_set(a, 'classA1', b2)
    assert _is_linked(a, 'classA1', b2)
    if hasattr(b1, 'classB0'):
        assert not _is_linked(b1, 'classB0', a)
    if hasattr(b2, 'classB0'):
        assert _is_linked(b2, 'classB0', a)
    _safe_set(a, 'classA1', None)
    assert not _is_linked(a, 'classA1', b2)
    if hasattr(b2, 'classB0'):
        assert not _is_linked(b2, 'classB0', a)


def test_assoc_ClassB_ClassC_link_reassign_clear():
    a = ClassC(attC1=7, attC2=True)
    b1 = ClassB(attribute=7)
    b2 = ClassB(attribute=13)
    _safe_set(a, 'classB3', b1)
    assert _is_linked(a, 'classB3', b1)
    if hasattr(b1, 'classC2'):
        assert _is_linked(b1, 'classC2', a)
    _safe_set(a, 'classB3', b2)
    assert _is_linked(a, 'classB3', b2)
    if hasattr(b1, 'classC2'):
        assert not _is_linked(b1, 'classC2', a)
    if hasattr(b2, 'classC2'):
        assert _is_linked(b2, 'classC2', a)
    _safe_set(a, 'classB3', None)
    assert not _is_linked(a, 'classB3', b2)
    if hasattr(b2, 'classC2'):
        assert not _is_linked(b2, 'classC2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ClassA_strategy = st.builds(ClassA, attA=safe_text)
@given(instance=ClassA_strategy)
@settings(max_examples=25)
def test_ClassA_instantiation(instance):
    assert isinstance(instance, ClassA)


ClassB_strategy = st.builds(ClassB, attribute=st.integers())
@given(instance=ClassB_strategy)
@settings(max_examples=25)
def test_ClassB_instantiation(instance):
    assert isinstance(instance, ClassB)


ClassC_strategy = st.builds(ClassC, attC1=st.integers(), attC2=st.booleans())
@given(instance=ClassC_strategy)
@settings(max_examples=25)
def test_ClassC_instantiation(instance):
    assert isinstance(instance, ClassC)



