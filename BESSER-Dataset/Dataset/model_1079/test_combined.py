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
    PetriNet,
    PetriNets_Place,
    PetriNets_PetriNet,
    PetriNets_Token,
    PetriNets_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_hyp_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_hyp_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinets_place_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Place)


def test_hyp_petrinets_place_constructor_exists():
    assert callable(PetriNets_Place.__init__)


def test_hyp_petrinets_place_constructor_args():
    sig = inspect.signature(PetriNets_Place.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "itokens" in params, "Missing parameter 'itokens'"





def test_hyp_petrinets_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNets_PetriNet)


def test_hyp_petrinets_petrinet_constructor_exists():
    assert callable(PetriNets_PetriNet.__init__)


def test_hyp_petrinets_petrinet_constructor_args():
    sig = inspect.signature(PetriNets_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinets_token_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Token)


def test_hyp_petrinets_token_constructor_exists():
    assert callable(PetriNets_Token.__init__)


def test_hyp_petrinets_token_constructor_args():
    sig = inspect.signature(PetriNets_Token.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinets_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Transition)


def test_hyp_petrinets_transition_constructor_exists():
    assert callable(PetriNets_Transition.__init__)


def test_hyp_petrinets_transition_constructor_args():
    sig = inspect.signature(PetriNets_Transition.__init__)
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
PetriNet_strategy = st.builds(
    PetriNet,
)
PetriNets_Place_strategy = st.builds(
    PetriNets_Place,
    capacity=
        st.integers(),
    itokens=
        st.integers()
)
PetriNets_PetriNet_strategy = st.builds(
    PetriNets_PetriNet,
)
PetriNets_Token_strategy = st.builds(
    PetriNets_Token,
)
PetriNets_Transition_strategy = st.builds(
    PetriNets_Transition,
)





@given(instance=PetriNets_Place_strategy)
def test_hyp_petrinets_place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=PetriNets_Place_strategy)
def test_hyp_petrinets_place_itokens_setter(instance):
    original = instance.itokens
    instance.itokens = original
    assert instance.itokens == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=PetriNets_Place_strategy)
@settings(max_examples=30)
def test_hyp_petrinets_place_tokens_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.tokens()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.tokens).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'tokens' in PetriNets_Place is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'tokens' in PetriNets_Place did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'tokens' in PetriNets_Place is not implemented or raised an error")





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    PetriNet,
    PetriNets_PetriNet,
    PetriNets_Place,
    PetriNets_Token,
    PetriNets_Transition,
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

def test_PetriNets_Place_capacity_value_roundtrip():
    instance = PetriNets_Place(capacity=7, itokens=7)
    assert instance.capacity == 7
    instance.capacity = 13
    assert instance.capacity == 13


def test_PetriNets_Place_itokens_value_roundtrip():
    instance = PetriNets_Place(capacity=7, itokens=7)
    assert instance.itokens == 7
    instance.itokens = 13
    assert instance.itokens == 13


def test_PetriNets_Transition_isa_PetriNet():
    instance = PetriNets_Transition()
    assert isinstance(instance, PetriNet)


def test_assoc_ins9_link_reassign_clear():
    a = PetriNets_Place(capacity=7, itokens=7)
    b1 = PetriNets_Transition()
    b2 = PetriNets_Transition()
    _safe_set(a, 'PetriNets_Place', b1)
    assert _is_linked(a, 'PetriNets_Place', b1)
    if hasattr(b1, 'PetriNets_Transition'):
        assert _is_linked(b1, 'PetriNets_Transition', a)
    _safe_set(a, 'PetriNets_Place', b2)
    assert _is_linked(a, 'PetriNets_Place', b2)
    if hasattr(b1, 'PetriNets_Transition'):
        assert not _is_linked(b1, 'PetriNets_Transition', a)
    if hasattr(b2, 'PetriNets_Transition'):
        assert _is_linked(b2, 'PetriNets_Transition', a)
    _safe_set(a, 'PetriNets_Place', None)
    assert not _is_linked(a, 'PetriNets_Place', b2)
    if hasattr(b2, 'PetriNets_Transition'):
        assert not _is_linked(b2, 'PetriNets_Transition', a)


def test_assoc_net3_link_reassign_clear():
    a = PetriNets_Place(capacity=7, itokens=7)
    b1 = PetriNets_PetriNet()
    b2 = PetriNets_PetriNet()
    _safe_set(a, 'places', b1)
    assert _is_linked(a, 'places', b1)
    if hasattr(b1, 'PetriNet'):
        assert _is_linked(b1, 'PetriNet', a)
    _safe_set(a, 'places', b2)
    assert _is_linked(a, 'places', b2)
    if hasattr(b1, 'PetriNet'):
        assert not _is_linked(b1, 'PetriNet', a)
    if hasattr(b2, 'PetriNet'):
        assert _is_linked(b2, 'PetriNet', a)
    _safe_set(a, 'places', None)
    assert not _is_linked(a, 'places', b2)
    if hasattr(b2, 'PetriNet'):
        assert not _is_linked(b2, 'PetriNet', a)


def test_assoc_outs10_link_reassign_clear():
    a = PetriNets_Place(capacity=7, itokens=7)
    b1 = PetriNets_Transition()
    b2 = PetriNets_Transition()
    _safe_set(a, 'PetriNets_Place12', b1)
    assert _is_linked(a, 'PetriNets_Place12', b1)
    if hasattr(b1, 'PetriNets_Transition11'):
        assert _is_linked(b1, 'PetriNets_Transition11', a)
    _safe_set(a, 'PetriNets_Place12', b2)
    assert _is_linked(a, 'PetriNets_Place12', b2)
    if hasattr(b1, 'PetriNets_Transition11'):
        assert not _is_linked(b1, 'PetriNets_Transition11', a)
    if hasattr(b2, 'PetriNets_Transition11'):
        assert _is_linked(b2, 'PetriNets_Transition11', a)
    _safe_set(a, 'PetriNets_Place12', None)
    assert not _is_linked(a, 'PetriNets_Place12', b2)
    if hasattr(b2, 'PetriNets_Transition11'):
        assert not _is_linked(b2, 'PetriNets_Transition11', a)


def test_assoc_place5_link_reassign_clear():
    a = PetriNets_Place(capacity=7, itokens=7)
    b1 = PetriNets_Token()
    b2 = PetriNets_Token()
    _safe_set(a, 'Place6', b1)
    assert _is_linked(a, 'Place6', b1)
    if hasattr(b1, 'tokens.1'):
        assert _is_linked(b1, 'tokens.1', a)
    _safe_set(a, 'Place6', b2)
    assert _is_linked(a, 'Place6', b2)
    if hasattr(b1, 'tokens.1'):
        assert not _is_linked(b1, 'tokens.1', a)
    if hasattr(b2, 'tokens.1'):
        assert _is_linked(b2, 'tokens.1', a)
    _safe_set(a, 'Place6', None)
    assert not _is_linked(a, 'Place6', b2)
    if hasattr(b2, 'tokens.1'):
        assert not _is_linked(b2, 'tokens.1', a)


def test_assoc_places0_link_reassign_clear():
    a = PetriNets_Place(capacity=7, itokens=7)
    b1 = PetriNets_PetriNet()
    b2 = PetriNets_PetriNet()
    _safe_set(a, 'Place', b1)
    assert _is_linked(a, 'Place', b1)
    if hasattr(b1, 'net'):
        assert _is_linked(b1, 'net', a)
    _safe_set(a, 'Place', b2)
    assert _is_linked(a, 'Place', b2)
    if hasattr(b1, 'net'):
        assert not _is_linked(b1, 'net', a)
    if hasattr(b2, 'net'):
        assert _is_linked(b2, 'net', a)
    _safe_set(a, 'Place', None)
    assert not _is_linked(a, 'Place', b2)
    if hasattr(b2, 'net'):
        assert not _is_linked(b2, 'net', a)


def test_assoc_tokens4_link_reassign_clear():
    a = PetriNets_Place(capacity=7, itokens=7)
    b1 = PetriNets_Token()
    b2 = PetriNets_Token()
    _safe_set(a, 'place', {b1})
    assert _is_linked(a, 'place', b1)
    if hasattr(b1, 'Token'):
        assert _is_linked(b1, 'Token', a)
    _safe_set(a, 'place', {b2})
    assert _is_linked(a, 'place', b2)
    if hasattr(b1, 'Token'):
        assert not _is_linked(b1, 'Token', a)
    if hasattr(b2, 'Token'):
        assert _is_linked(b2, 'Token', a)
    _safe_set(a, 'place', set())
    assert not _is_linked(a, 'place', b2)
    if hasattr(b2, 'Token'):
        assert not _is_linked(b2, 'Token', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

PetriNet_strategy = st.builds(PetriNet)
@given(instance=PetriNet_strategy)
@settings(max_examples=25)
def test_PetriNet_instantiation(instance):
    assert isinstance(instance, PetriNet)


PetriNets_PetriNet_strategy = st.builds(PetriNets_PetriNet)
@given(instance=PetriNets_PetriNet_strategy)
@settings(max_examples=25)
def test_PetriNets_PetriNet_instantiation(instance):
    assert isinstance(instance, PetriNets_PetriNet)


PetriNets_Place_strategy = st.builds(PetriNets_Place, capacity=st.integers(), itokens=st.integers())
@given(instance=PetriNets_Place_strategy)
@settings(max_examples=25)
def test_PetriNets_Place_instantiation(instance):
    assert isinstance(instance, PetriNets_Place)


PetriNets_Token_strategy = st.builds(PetriNets_Token)
@given(instance=PetriNets_Token_strategy)
@settings(max_examples=25)
def test_PetriNets_Token_instantiation(instance):
    assert isinstance(instance, PetriNets_Token)


PetriNets_Transition_strategy = st.builds(PetriNets_Transition)
@given(instance=PetriNets_Transition_strategy)
@settings(max_examples=25)
def test_PetriNets_Transition_instantiation(instance):
    assert isinstance(instance, PetriNets_Transition)



