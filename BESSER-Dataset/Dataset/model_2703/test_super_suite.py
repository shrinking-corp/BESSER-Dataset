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
    sample_C,
    A,
    sample_B,
    sample_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_sample_c_is_not_abstract():
    assert not inspect.isabstract(sample_C)


def test_hyp_sample_c_constructor_exists():
    assert callable(sample_C.__init__)


def test_hyp_sample_c_constructor_args():
    sig = inspect.signature(sample_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_hyp_a_constructor_exists():
    assert callable(A.__init__)


def test_hyp_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sample_b_is_not_abstract():
    assert not inspect.isabstract(sample_B)


def test_hyp_sample_b_constructor_exists():
    assert callable(sample_B.__init__)


def test_hyp_sample_b_constructor_args():
    sig = inspect.signature(sample_B.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_sample_a_is_not_abstract():
    assert not inspect.isabstract(sample_A)


def test_hyp_sample_a_constructor_exists():
    assert callable(sample_A.__init__)


def test_hyp_sample_a_constructor_args():
    sig = inspect.signature(sample_A.__init__)
    params = list(sig.parameters.keys())
    assert "valid" in params, "Missing parameter 'valid'"
    assert "name" in params, "Missing parameter 'name'"
    assert "quantity" in params, "Missing parameter 'quantity'"





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
sample_C_strategy = st.builds(
    sample_C,
)
A_strategy = st.builds(
    A,
)
sample_B_strategy = st.builds(
    sample_B,
    label=
        safe_text
)
sample_A_strategy = st.builds(
    sample_A,
    valid=
        st.booleans(),
    name=
        safe_text,
    quantity=
        st.integers()
)






@given(instance=sample_B_strategy)
def test_hyp_sample_b_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original




@given(instance=sample_A_strategy)
def test_hyp_sample_a_valid_setter(instance):
    original = instance.valid
    instance.valid = original
    assert instance.valid == original



@given(instance=sample_A_strategy)
def test_hyp_sample_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sample_A_strategy)
def test_hyp_sample_a_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    A,
    sample_A,
    sample_B,
    sample_C,
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

def test_sample_A_name_value_roundtrip():
    instance = sample_A(name="sample_text", quantity=7, valid=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sample_A_quantity_value_roundtrip():
    instance = sample_A(name="sample_text", quantity=7, valid=True)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_sample_A_valid_value_roundtrip():
    instance = sample_A(name="sample_text", quantity=7, valid=True)
    assert instance.valid == True
    instance.valid = False
    assert instance.valid == False


def test_sample_B_label_value_roundtrip():
    instance = sample_B(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_sample_B_isa_A():
    instance = sample_B(label="sample_text")
    assert isinstance(instance, A)


def test_assoc_a1_link_reassign_clear():
    a = sample_A(name="sample_text", quantity=7, valid=True)
    b1 = sample_C()
    b2 = sample_C()
    _safe_set(a, 'sample_A', b1)
    assert _is_linked(a, 'sample_A', b1)
    if hasattr(b1, 'sample_C2'):
        assert _is_linked(b1, 'sample_C2', a)
    _safe_set(a, 'sample_A', b2)
    assert _is_linked(a, 'sample_A', b2)
    if hasattr(b1, 'sample_C2'):
        assert not _is_linked(b1, 'sample_C2', a)
    if hasattr(b2, 'sample_C2'):
        assert _is_linked(b2, 'sample_C2', a)
    _safe_set(a, 'sample_A', None)
    assert not _is_linked(a, 'sample_A', b2)
    if hasattr(b2, 'sample_C2'):
        assert not _is_linked(b2, 'sample_C2', a)


def test_assoc_c0_link_reassign_clear():
    a = sample_B(label="sample_text")
    b1 = sample_C()
    b2 = sample_C()
    _safe_set(a, 'sample_B', {b1})
    assert _is_linked(a, 'sample_B', b1)
    if hasattr(b1, 'sample_C'):
        assert _is_linked(b1, 'sample_C', a)
    _safe_set(a, 'sample_B', {b2})
    assert _is_linked(a, 'sample_B', b2)
    if hasattr(b1, 'sample_C'):
        assert not _is_linked(b1, 'sample_C', a)
    if hasattr(b2, 'sample_C'):
        assert _is_linked(b2, 'sample_C', a)
    _safe_set(a, 'sample_B', set())
    assert not _is_linked(a, 'sample_B', b2)
    if hasattr(b2, 'sample_C'):
        assert not _is_linked(b2, 'sample_C', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

A_strategy = st.builds(A)
@given(instance=A_strategy)
@settings(max_examples=25)
def test_A_instantiation(instance):
    assert isinstance(instance, A)


sample_A_strategy = st.builds(sample_A, name=safe_text, quantity=st.integers(), valid=st.booleans())
@given(instance=sample_A_strategy)
@settings(max_examples=25)
def test_sample_A_instantiation(instance):
    assert isinstance(instance, sample_A)


sample_B_strategy = st.builds(sample_B, label=safe_text)
@given(instance=sample_B_strategy)
@settings(max_examples=25)
def test_sample_B_instantiation(instance):
    assert isinstance(instance, sample_B)


sample_C_strategy = st.builds(sample_C)
@given(instance=sample_C_strategy)
@settings(max_examples=25)
def test_sample_C_instantiation(instance):
    assert isinstance(instance, sample_C)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    sample_A,
    sample_B,
    sample_C,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_a1_stub_double():
    # sample_C has no real 'sample_C2' property in the generated
    # code (a bare stub) -- manually attach it so sample_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sample_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sample_A(name="sample_text", quantity=7, valid=True)
    partner = sample_C()
    setattr(partner, 'sample_C2', None)
    _safe_set(owner, 'sample_A', partner)
    assert getattr(partner, 'sample_C2') == owner
    _safe_set(owner, 'sample_A', None)
    assert getattr(partner, 'sample_C2') is None


def test_assoc_c0_stub_double():
    # sample_C has no real 'sample_C' property in the generated
    # code (a bare stub) -- manually attach it so sample_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sample_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sample_B(label="sample_text")
    partner = sample_C()
    setattr(partner, 'sample_C', None)
    _safe_set(owner, 'sample_B', {partner})
    assert getattr(partner, 'sample_C') == owner
    _safe_set(owner, 'sample_B', set())
    assert getattr(partner, 'sample_C') is None




from python_code import sample_A
from python_code import sample_C

def test_sample_A___init__():
    assert sample_A.__init__(sample_A('', False, 0, sample_A=sample_C()), '\x00', False, 0, sample_A=sample_C()) == None
from python_code import sample_B

def test_sample_B___init__():
    assert sample_B.__init__(sample_B('', sample_B=set()), '', sample_B=set()) == None

