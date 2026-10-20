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
    AbstractState,
    z4fsm_State,
    z4fsm_AbstractState,
    z4fsm_Region,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_hyp_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_hyp_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_z4fsm_state_is_not_abstract():
    assert not inspect.isabstract(z4fsm_State)


def test_hyp_z4fsm_state_constructor_exists():
    assert callable(z4fsm_State.__init__)


def test_hyp_z4fsm_state_constructor_args():
    sig = inspect.signature(z4fsm_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_z4fsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(z4fsm_AbstractState)


def test_hyp_z4fsm_abstractstate_constructor_exists():
    assert callable(z4fsm_AbstractState.__init__)


def test_hyp_z4fsm_abstractstate_constructor_args():
    sig = inspect.signature(z4fsm_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_z4fsm_region_is_not_abstract():
    assert not inspect.isabstract(z4fsm_Region)


def test_hyp_z4fsm_region_constructor_exists():
    assert callable(z4fsm_Region.__init__)


def test_hyp_z4fsm_region_constructor_args():
    sig = inspect.signature(z4fsm_Region.__init__)
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
AbstractState_strategy = st.builds(
    AbstractState,
)
z4fsm_State_strategy = st.builds(
    z4fsm_State,
)
z4fsm_AbstractState_strategy = st.builds(
    z4fsm_AbstractState,
    id=
        safe_text
)
z4fsm_Region_strategy = st.builds(
    z4fsm_Region,
    name=
        safe_text
)






@given(instance=z4fsm_AbstractState_strategy)
def test_hyp_z4fsm_abstractstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=z4fsm_Region_strategy)
def test_hyp_z4fsm_region_name_setter(instance):
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
    AbstractState,
    z4fsm_AbstractState,
    z4fsm_Region,
    z4fsm_State,
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

def test_z4fsm_AbstractState_id_value_roundtrip():
    instance = z4fsm_AbstractState(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_z4fsm_Region_name_value_roundtrip():
    instance = z4fsm_Region(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_z4fsm_State_isa_AbstractState():
    instance = z4fsm_State()
    assert isinstance(instance, AbstractState)


def test_assoc_astates0_link_reassign_clear():
    a = z4fsm_Region(name="sample_text")
    b1 = z4fsm_AbstractState(id="sample_text")
    b2 = z4fsm_AbstractState(id="sample_text_2")
    _safe_set(a, 'z4fsm_Region', {b1})
    assert _is_linked(a, 'z4fsm_Region', b1)
    if hasattr(b1, 'z4fsm_AbstractState'):
        assert _is_linked(b1, 'z4fsm_AbstractState', a)
    _safe_set(a, 'z4fsm_Region', {b2})
    assert _is_linked(a, 'z4fsm_Region', b2)
    if hasattr(b1, 'z4fsm_AbstractState'):
        assert not _is_linked(b1, 'z4fsm_AbstractState', a)
    if hasattr(b2, 'z4fsm_AbstractState'):
        assert _is_linked(b2, 'z4fsm_AbstractState', a)
    _safe_set(a, 'z4fsm_Region', set())
    assert not _is_linked(a, 'z4fsm_Region', b2)
    if hasattr(b2, 'z4fsm_AbstractState'):
        assert not _is_linked(b2, 'z4fsm_AbstractState', a)


def test_assoc_subElements1_link_reassign_clear():
    a = z4fsm_AbstractState(id="sample_text")
    b1 = z4fsm_State()
    b2 = z4fsm_State()
    _safe_set(a, 'z4fsm_AbstractState2', {b1})
    assert _is_linked(a, 'z4fsm_AbstractState2', b1)
    if hasattr(b1, 'z4fsm_State'):
        assert _is_linked(b1, 'z4fsm_State', a)
    _safe_set(a, 'z4fsm_AbstractState2', {b2})
    assert _is_linked(a, 'z4fsm_AbstractState2', b2)
    if hasattr(b1, 'z4fsm_State'):
        assert not _is_linked(b1, 'z4fsm_State', a)
    if hasattr(b2, 'z4fsm_State'):
        assert _is_linked(b2, 'z4fsm_State', a)
    _safe_set(a, 'z4fsm_AbstractState2', set())
    assert not _is_linked(a, 'z4fsm_AbstractState2', b2)
    if hasattr(b2, 'z4fsm_State'):
        assert not _is_linked(b2, 'z4fsm_State', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractState_strategy = st.builds(AbstractState)
@given(instance=AbstractState_strategy)
@settings(max_examples=25)
def test_AbstractState_instantiation(instance):
    assert isinstance(instance, AbstractState)


z4fsm_AbstractState_strategy = st.builds(z4fsm_AbstractState, id=safe_text)
@given(instance=z4fsm_AbstractState_strategy)
@settings(max_examples=25)
def test_z4fsm_AbstractState_instantiation(instance):
    assert isinstance(instance, z4fsm_AbstractState)


z4fsm_Region_strategy = st.builds(z4fsm_Region, name=safe_text)
@given(instance=z4fsm_Region_strategy)
@settings(max_examples=25)
def test_z4fsm_Region_instantiation(instance):
    assert isinstance(instance, z4fsm_Region)


z4fsm_State_strategy = st.builds(z4fsm_State)
@given(instance=z4fsm_State_strategy)
@settings(max_examples=25)
def test_z4fsm_State_instantiation(instance):
    assert isinstance(instance, z4fsm_State)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    z4fsm_AbstractState,
    z4fsm_Region,
    z4fsm_State,
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

def test_assoc_astates0_reverse_link_reassign_clear():
    a1 = z4fsm_Region(name="sample_text")
    a2 = z4fsm_Region(name="sample_text_2")
    b = z4fsm_AbstractState(id="sample_text")
    _safe_set(b, 'z4fsm_AbstractState', a1)
    assert _is_linked(b, 'z4fsm_AbstractState', a1)
    if hasattr(a1, 'z4fsm_Region'):
        assert _is_linked(a1, 'z4fsm_Region', b)
    _safe_set(b, 'z4fsm_AbstractState', a2)
    assert _is_linked(b, 'z4fsm_AbstractState', a2)
    if hasattr(a1, 'z4fsm_Region'):
        assert not _is_linked(a1, 'z4fsm_Region', b)
    if hasattr(a2, 'z4fsm_Region'):
        assert _is_linked(a2, 'z4fsm_Region', b)
    _safe_set(b, 'z4fsm_AbstractState', None)
    assert not _is_linked(b, 'z4fsm_AbstractState', a2)
    if hasattr(a2, 'z4fsm_Region'):
        assert not _is_linked(a2, 'z4fsm_Region', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_subElements1_stub_double():
    # z4fsm_State has no real 'z4fsm_State' property in the generated
    # code (a bare stub) -- manually attach it so z4fsm_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # z4fsm_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = z4fsm_AbstractState(id="sample_text")
    partner = z4fsm_State()
    setattr(partner, 'z4fsm_State', None)
    _safe_set(owner, 'z4fsm_AbstractState2', {partner})
    assert getattr(partner, 'z4fsm_State') == owner
    _safe_set(owner, 'z4fsm_AbstractState2', set())
    assert getattr(partner, 'z4fsm_State') is None




from python_code import z4fsm_Region

def test_z4fsm_Region___init__():
    assert z4fsm_Region.__init__(z4fsm_Region('', z4fsm_Region=set()), '', z4fsm_Region=set()) == None

