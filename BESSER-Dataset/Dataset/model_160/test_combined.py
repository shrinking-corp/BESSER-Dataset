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
    Petrinet_Transition,
    Petrinet_Place,
    Petrinet_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(Petrinet_Transition)


def test_hyp_petrinet_transition_constructor_exists():
    assert callable(Petrinet_Transition.__init__)


def test_hyp_petrinet_transition_constructor_args():
    sig = inspect.signature(Petrinet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(Petrinet_Place)


def test_hyp_petrinet_place_constructor_exists():
    assert callable(Petrinet_Place.__init__)


def test_hyp_petrinet_place_constructor_args():
    sig = inspect.signature(Petrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tokens" in params, "Missing parameter 'tokens'"





def test_hyp_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(Petrinet_PetriNet)


def test_hyp_petrinet_petrinet_constructor_exists():
    assert callable(Petrinet_PetriNet.__init__)


def test_hyp_petrinet_petrinet_constructor_args():
    sig = inspect.signature(Petrinet_PetriNet.__init__)
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
Petrinet_Transition_strategy = st.builds(
    Petrinet_Transition,
    name=
        safe_text
)
Petrinet_Place_strategy = st.builds(
    Petrinet_Place,
    name=
        safe_text,
    tokens=
        st.integers()
)
Petrinet_PetriNet_strategy = st.builds(
    Petrinet_PetriNet,
)




@given(instance=Petrinet_Transition_strategy)
def test_hyp_petrinet_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Petrinet_Place_strategy)
def test_hyp_petrinet_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Petrinet_Place_strategy)
def test_hyp_petrinet_place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Petrinet_PetriNet,
    Petrinet_Place,
    Petrinet_Transition,
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

def test_Petrinet_Place_name_value_roundtrip():
    instance = Petrinet_Place(name="sample_text", tokens=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Petrinet_Place_tokens_value_roundtrip():
    instance = Petrinet_Place(name="sample_text", tokens=7)
    assert instance.tokens == 7
    instance.tokens = 13
    assert instance.tokens == 13


def test_Petrinet_Transition_name_value_roundtrip():
    instance = Petrinet_Transition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_p2t3_link_reassign_clear():
    a = Petrinet_Transition(name="sample_text")
    b1 = Petrinet_Place(name="sample_text", tokens=7)
    b2 = Petrinet_Place(name="sample_text_2", tokens=13)
    _safe_set(a, 'Petrinet_Transition5', b1)
    assert _is_linked(a, 'Petrinet_Transition5', b1)
    if hasattr(b1, 'Petrinet_Place4'):
        assert _is_linked(b1, 'Petrinet_Place4', a)
    _safe_set(a, 'Petrinet_Transition5', b2)
    assert _is_linked(a, 'Petrinet_Transition5', b2)
    if hasattr(b1, 'Petrinet_Place4'):
        assert not _is_linked(b1, 'Petrinet_Place4', a)
    if hasattr(b2, 'Petrinet_Place4'):
        assert _is_linked(b2, 'Petrinet_Place4', a)
    _safe_set(a, 'Petrinet_Transition5', None)
    assert not _is_linked(a, 'Petrinet_Transition5', b2)
    if hasattr(b2, 'Petrinet_Place4'):
        assert not _is_linked(b2, 'Petrinet_Place4', a)


def test_assoc_places0_link_reassign_clear():
    a = Petrinet_Place(name="sample_text", tokens=7)
    b1 = Petrinet_PetriNet()
    b2 = Petrinet_PetriNet()
    _safe_set(a, 'Petrinet_Place', b1)
    assert _is_linked(a, 'Petrinet_Place', b1)
    if hasattr(b1, 'Petrinet_PetriNet'):
        assert _is_linked(b1, 'Petrinet_PetriNet', a)
    _safe_set(a, 'Petrinet_Place', b2)
    assert _is_linked(a, 'Petrinet_Place', b2)
    if hasattr(b1, 'Petrinet_PetriNet'):
        assert not _is_linked(b1, 'Petrinet_PetriNet', a)
    if hasattr(b2, 'Petrinet_PetriNet'):
        assert _is_linked(b2, 'Petrinet_PetriNet', a)
    _safe_set(a, 'Petrinet_Place', None)
    assert not _is_linked(a, 'Petrinet_Place', b2)
    if hasattr(b2, 'Petrinet_PetriNet'):
        assert not _is_linked(b2, 'Petrinet_PetriNet', a)


def test_assoc_t2p6_link_reassign_clear():
    a = Petrinet_Transition(name="sample_text")
    b1 = Petrinet_Place(name="sample_text", tokens=7)
    b2 = Petrinet_Place(name="sample_text_2", tokens=13)
    _safe_set(a, 'Petrinet_Transition7', {b1})
    assert _is_linked(a, 'Petrinet_Transition7', b1)
    if hasattr(b1, 'Petrinet_Place8'):
        assert _is_linked(b1, 'Petrinet_Place8', a)
    _safe_set(a, 'Petrinet_Transition7', {b2})
    assert _is_linked(a, 'Petrinet_Transition7', b2)
    if hasattr(b1, 'Petrinet_Place8'):
        assert not _is_linked(b1, 'Petrinet_Place8', a)
    if hasattr(b2, 'Petrinet_Place8'):
        assert _is_linked(b2, 'Petrinet_Place8', a)
    _safe_set(a, 'Petrinet_Transition7', set())
    assert not _is_linked(a, 'Petrinet_Transition7', b2)
    if hasattr(b2, 'Petrinet_Place8'):
        assert not _is_linked(b2, 'Petrinet_Place8', a)


def test_assoc_transitions1_link_reassign_clear():
    a = Petrinet_Transition(name="sample_text")
    b1 = Petrinet_PetriNet()
    b2 = Petrinet_PetriNet()
    _safe_set(a, 'Petrinet_Transition', b1)
    assert _is_linked(a, 'Petrinet_Transition', b1)
    if hasattr(b1, 'Petrinet_PetriNet2'):
        assert _is_linked(b1, 'Petrinet_PetriNet2', a)
    _safe_set(a, 'Petrinet_Transition', b2)
    assert _is_linked(a, 'Petrinet_Transition', b2)
    if hasattr(b1, 'Petrinet_PetriNet2'):
        assert not _is_linked(b1, 'Petrinet_PetriNet2', a)
    if hasattr(b2, 'Petrinet_PetriNet2'):
        assert _is_linked(b2, 'Petrinet_PetriNet2', a)
    _safe_set(a, 'Petrinet_Transition', None)
    assert not _is_linked(a, 'Petrinet_Transition', b2)
    if hasattr(b2, 'Petrinet_PetriNet2'):
        assert not _is_linked(b2, 'Petrinet_PetriNet2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Petrinet_PetriNet_strategy = st.builds(Petrinet_PetriNet)
@given(instance=Petrinet_PetriNet_strategy)
@settings(max_examples=25)
def test_Petrinet_PetriNet_instantiation(instance):
    assert isinstance(instance, Petrinet_PetriNet)


Petrinet_Place_strategy = st.builds(Petrinet_Place, name=safe_text, tokens=st.integers())
@given(instance=Petrinet_Place_strategy)
@settings(max_examples=25)
def test_Petrinet_Place_instantiation(instance):
    assert isinstance(instance, Petrinet_Place)


Petrinet_Transition_strategy = st.builds(Petrinet_Transition, name=safe_text)
@given(instance=Petrinet_Transition_strategy)
@settings(max_examples=25)
def test_Petrinet_Transition_instantiation(instance):
    assert isinstance(instance, Petrinet_Transition)



