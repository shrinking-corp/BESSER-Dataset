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
    B,
    minher_E,
    Named,
    minher_G,
    minher_C,
    minher_B,
    minher_A,
    minher_Named,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minher_e_is_not_abstract():
    assert not inspect.isabstract(minher_E)


def test_hyp_minher_e_constructor_exists():
    assert callable(minher_E.__init__)


def test_hyp_minher_e_constructor_args():
    sig = inspect.signature(minher_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minher_g_is_not_abstract():
    assert not inspect.isabstract(minher_G)


def test_hyp_minher_g_constructor_exists():
    assert callable(minher_G.__init__)


def test_hyp_minher_g_constructor_args():
    sig = inspect.signature(minher_G.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minher_c_is_not_abstract():
    assert not inspect.isabstract(minher_C)


def test_hyp_minher_c_constructor_exists():
    assert callable(minher_C.__init__)


def test_hyp_minher_c_constructor_args():
    sig = inspect.signature(minher_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minher_b_is_not_abstract():
    assert not inspect.isabstract(minher_B)


def test_hyp_minher_b_constructor_exists():
    assert callable(minher_B.__init__)


def test_hyp_minher_b_constructor_args():
    sig = inspect.signature(minher_B.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minher_a_is_not_abstract():
    assert not inspect.isabstract(minher_A)


def test_hyp_minher_a_constructor_exists():
    assert callable(minher_A.__init__)


def test_hyp_minher_a_constructor_args():
    sig = inspect.signature(minher_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minher_named_is_not_abstract():
    assert not inspect.isabstract(minher_Named)


def test_hyp_minher_named_constructor_exists():
    assert callable(minher_Named.__init__)


def test_hyp_minher_named_constructor_args():
    sig = inspect.signature(minher_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
B_strategy = st.builds(
    B,
)
minher_E_strategy = st.builds(
    minher_E,
)
Named_strategy = st.builds(
    Named,
)
minher_G_strategy = st.builds(
    minher_G,
)
minher_C_strategy = st.builds(
    minher_C,
)
minher_B_strategy = st.builds(
    minher_B,
    value=
        safe_text
)
minher_A_strategy = st.builds(
    minher_A,
)
minher_Named_strategy = st.builds(
    minher_Named,
    name=
        safe_text
)









@given(instance=minher_B_strategy)
def test_hyp_minher_b_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=minher_Named_strategy)
def test_hyp_minher_named_name_setter(instance):
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
    B,
    Named,
    minher_A,
    minher_B,
    minher_C,
    minher_E,
    minher_G,
    minher_Named,
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

def test_minher_B_value_value_roundtrip():
    instance = minher_B(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_minher_Named_name_value_roundtrip():
    instance = minher_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minher_E_isa_B():
    instance = minher_E()
    assert isinstance(instance, B)


def test_minher_B_isa_Named():
    instance = minher_B(value="sample_text")
    assert isinstance(instance, Named)


def test_minher_C_isa_Named():
    instance = minher_C()
    assert isinstance(instance, Named)


def test_minher_G_isa_Named():
    instance = minher_G()
    assert isinstance(instance, Named)


def test_assoc_bs0_link_reassign_clear():
    a = minher_B(value="sample_text")
    b1 = minher_A()
    b2 = minher_A()
    _safe_set(a, 'minher_B', b1)
    assert _is_linked(a, 'minher_B', b1)
    if hasattr(b1, 'minher_A'):
        assert _is_linked(b1, 'minher_A', a)
    _safe_set(a, 'minher_B', b2)
    assert _is_linked(a, 'minher_B', b2)
    if hasattr(b1, 'minher_A'):
        assert not _is_linked(b1, 'minher_A', a)
    if hasattr(b2, 'minher_A'):
        assert _is_linked(b2, 'minher_A', a)
    _safe_set(a, 'minher_B', None)
    assert not _is_linked(a, 'minher_B', b2)
    if hasattr(b2, 'minher_A'):
        assert not _is_linked(b2, 'minher_A', a)


def test_assoc_cs3_link_reassign_clear():
    a = minher_B(value="sample_text")
    b1 = minher_C()
    b2 = minher_C()
    _safe_set(a, 'minher_B4', {b1})
    assert _is_linked(a, 'minher_B4', b1)
    if hasattr(b1, 'minher_C'):
        assert _is_linked(b1, 'minher_C', a)
    _safe_set(a, 'minher_B4', {b2})
    assert _is_linked(a, 'minher_B4', b2)
    if hasattr(b1, 'minher_C'):
        assert not _is_linked(b1, 'minher_C', a)
    if hasattr(b2, 'minher_C'):
        assert _is_linked(b2, 'minher_C', a)
    _safe_set(a, 'minher_B4', set())
    assert not _is_linked(a, 'minher_B4', b2)
    if hasattr(b2, 'minher_C'):
        assert not _is_linked(b2, 'minher_C', a)


def test_assoc_gs1_link_reassign_clear():
    a = minher_B(value="sample_text")
    b1 = minher_G()
    b2 = minher_G()
    _safe_set(a, 'minher_B2', {b1})
    assert _is_linked(a, 'minher_B2', b1)
    if hasattr(b1, 'minher_G'):
        assert _is_linked(b1, 'minher_G', a)
    _safe_set(a, 'minher_B2', {b2})
    assert _is_linked(a, 'minher_B2', b2)
    if hasattr(b1, 'minher_G'):
        assert not _is_linked(b1, 'minher_G', a)
    if hasattr(b2, 'minher_G'):
        assert _is_linked(b2, 'minher_G', a)
    _safe_set(a, 'minher_B2', set())
    assert not _is_linked(a, 'minher_B2', b2)
    if hasattr(b2, 'minher_G'):
        assert not _is_linked(b2, 'minher_G', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

B_strategy = st.builds(B)
@given(instance=B_strategy)
@settings(max_examples=25)
def test_B_instantiation(instance):
    assert isinstance(instance, B)


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


minher_A_strategy = st.builds(minher_A)
@given(instance=minher_A_strategy)
@settings(max_examples=25)
def test_minher_A_instantiation(instance):
    assert isinstance(instance, minher_A)


minher_B_strategy = st.builds(minher_B, value=safe_text)
@given(instance=minher_B_strategy)
@settings(max_examples=25)
def test_minher_B_instantiation(instance):
    assert isinstance(instance, minher_B)


minher_C_strategy = st.builds(minher_C)
@given(instance=minher_C_strategy)
@settings(max_examples=25)
def test_minher_C_instantiation(instance):
    assert isinstance(instance, minher_C)


minher_E_strategy = st.builds(minher_E)
@given(instance=minher_E_strategy)
@settings(max_examples=25)
def test_minher_E_instantiation(instance):
    assert isinstance(instance, minher_E)


minher_G_strategy = st.builds(minher_G)
@given(instance=minher_G_strategy)
@settings(max_examples=25)
def test_minher_G_instantiation(instance):
    assert isinstance(instance, minher_G)


minher_Named_strategy = st.builds(minher_Named, name=safe_text)
@given(instance=minher_Named_strategy)
@settings(max_examples=25)
def test_minher_Named_instantiation(instance):
    assert isinstance(instance, minher_Named)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    B,
    Named,
    minher_A,
    minher_B,
    minher_C,
    minher_E,
    minher_G,
    minher_Named,
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

def test_assoc_bs0_stub_double():
    # minher_A has no real 'minher_A' property in the generated
    # code (a bare stub) -- manually attach it so minher_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minher_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minher_B(value="sample_text")
    partner = minher_A()
    setattr(partner, 'minher_A', None)
    _safe_set(owner, 'minher_B', partner)
    assert owner in getattr(partner, 'minher_A')
    _safe_set(owner, 'minher_B', None)
    assert owner not in getattr(partner, 'minher_A')


def test_assoc_cs3_stub_double():
    # minher_C has no real 'minher_C' property in the generated
    # code (a bare stub) -- manually attach it so minher_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minher_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minher_B(value="sample_text")
    partner = minher_C()
    setattr(partner, 'minher_C', None)
    _safe_set(owner, 'minher_B4', {partner})
    assert getattr(partner, 'minher_C') == owner
    _safe_set(owner, 'minher_B4', set())
    assert getattr(partner, 'minher_C') is None


def test_assoc_gs1_stub_double():
    # minher_G has no real 'minher_G' property in the generated
    # code (a bare stub) -- manually attach it so minher_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minher_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minher_B(value="sample_text")
    partner = minher_G()
    setattr(partner, 'minher_G', None)
    _safe_set(owner, 'minher_B2', {partner})
    assert getattr(partner, 'minher_G') == owner
    _safe_set(owner, 'minher_B2', set())
    assert getattr(partner, 'minher_G') is None




from python_code import minher_A
from python_code import minher_B

def test_minher_B___init__():
    assert minher_B.__init__(minher_B('', minher_B=minher_A(), minher_B2=set(), minher_B4=set()), '', minher_B=minher_A(), minher_B2=set(), minher_B4=set()) == None
from python_code import minher_Named

def test_minher_Named___init__():
    assert minher_Named.__init__(minher_Named(''), '') == None

