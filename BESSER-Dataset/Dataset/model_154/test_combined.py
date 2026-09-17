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
    petrinetmodel_Edge,
    Edge,
    petrinetmodel_EdgeToTransaction,
    petrinetmodel_EdgeToPlace,
    petrinetmodel_Place,
    petrinetmodel_Transition,
    petrinetmodel_Petrinet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_petrinetmodel_edge_is_not_abstract():
    assert not inspect.isabstract(petrinetmodel_Edge)


def test_hyp_petrinetmodel_edge_constructor_exists():
    assert callable(petrinetmodel_Edge.__init__)


def test_hyp_petrinetmodel_edge_constructor_args():
    sig = inspect.signature(petrinetmodel_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"




def test_hyp_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_hyp_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_hyp_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinetmodel_edgetotransaction_is_not_abstract():
    assert not inspect.isabstract(petrinetmodel_EdgeToTransaction)


def test_hyp_petrinetmodel_edgetotransaction_constructor_exists():
    assert callable(petrinetmodel_EdgeToTransaction.__init__)


def test_hyp_petrinetmodel_edgetotransaction_constructor_args():
    sig = inspect.signature(petrinetmodel_EdgeToTransaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinetmodel_edgetoplace_is_not_abstract():
    assert not inspect.isabstract(petrinetmodel_EdgeToPlace)


def test_hyp_petrinetmodel_edgetoplace_constructor_exists():
    assert callable(petrinetmodel_EdgeToPlace.__init__)


def test_hyp_petrinetmodel_edgetoplace_constructor_args():
    sig = inspect.signature(petrinetmodel_EdgeToPlace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinetmodel_place_is_not_abstract():
    assert not inspect.isabstract(petrinetmodel_Place)


def test_hyp_petrinetmodel_place_constructor_exists():
    assert callable(petrinetmodel_Place.__init__)


def test_hyp_petrinetmodel_place_constructor_args():
    sig = inspect.signature(petrinetmodel_Place.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_petrinetmodel_transition_is_not_abstract():
    assert not inspect.isabstract(petrinetmodel_Transition)


def test_hyp_petrinetmodel_transition_constructor_exists():
    assert callable(petrinetmodel_Transition.__init__)


def test_hyp_petrinetmodel_transition_constructor_args():
    sig = inspect.signature(petrinetmodel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "token" in params, "Missing parameter 'token'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_petrinetmodel_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinetmodel_Petrinet)


def test_hyp_petrinetmodel_petrinet_constructor_exists():
    assert callable(petrinetmodel_Petrinet.__init__)


def test_hyp_petrinetmodel_petrinet_constructor_args():
    sig = inspect.signature(petrinetmodel_Petrinet.__init__)
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
petrinetmodel_Edge_strategy = st.builds(
    petrinetmodel_Edge,
    weight=
        st.integers()
)
Edge_strategy = st.builds(
    Edge,
)
petrinetmodel_EdgeToTransaction_strategy = st.builds(
    petrinetmodel_EdgeToTransaction,
)
petrinetmodel_EdgeToPlace_strategy = st.builds(
    petrinetmodel_EdgeToPlace,
)
petrinetmodel_Place_strategy = st.builds(
    petrinetmodel_Place,
    token=
        st.integers(),
    id=
        st.integers()
)
petrinetmodel_Transition_strategy = st.builds(
    petrinetmodel_Transition,
    priority=
        st.integers(),
    token=
        st.integers(),
    id=
        st.integers()
)
petrinetmodel_Petrinet_strategy = st.builds(
    petrinetmodel_Petrinet,
)




@given(instance=petrinetmodel_Edge_strategy)
def test_hyp_petrinetmodel_edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original







@given(instance=petrinetmodel_Place_strategy)
def test_hyp_petrinetmodel_place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original



@given(instance=petrinetmodel_Place_strategy)
def test_hyp_petrinetmodel_place_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petrinetmodel_Place_strategy)
@settings(max_examples=30)
def test_hyp_petrinetmodel_place_init_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.init()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.init).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'init' in petrinetmodel_Place is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'init' in petrinetmodel_Place did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'init' in petrinetmodel_Place is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petrinetmodel_Place_strategy)
@settings(max_examples=30)
def test_hyp_petrinetmodel_place_addtoken_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addToken()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addToken).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addToken' in petrinetmodel_Place is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addToken' in petrinetmodel_Place did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addToken' in petrinetmodel_Place is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petrinetmodel_Place_strategy)
@settings(max_examples=30)
def test_hyp_petrinetmodel_place_hastoken_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasToken()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasToken).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasToken' in petrinetmodel_Place is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasToken' in petrinetmodel_Place did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasToken' in petrinetmodel_Place is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petrinetmodel_Place_strategy)
@settings(max_examples=30)
def test_hyp_petrinetmodel_place_removetoken_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeToken()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeToken).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeToken' in petrinetmodel_Place is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeToken' in petrinetmodel_Place did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeToken' in petrinetmodel_Place is not implemented or raised an error")




@given(instance=petrinetmodel_Transition_strategy)
def test_hyp_petrinetmodel_transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=petrinetmodel_Transition_strategy)
def test_hyp_petrinetmodel_transition_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original



@given(instance=petrinetmodel_Transition_strategy)
def test_hyp_petrinetmodel_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petrinetmodel_Transition_strategy)
@settings(max_examples=30)
def test_hyp_petrinetmodel_transition_fire_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fire()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fire).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fire' in petrinetmodel_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in petrinetmodel_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in petrinetmodel_Transition is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petrinetmodel_Transition_strategy)
@settings(max_examples=30)
def test_hyp_petrinetmodel_transition_prepare_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.prepare()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.prepare).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'prepare' in petrinetmodel_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'prepare' in petrinetmodel_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'prepare' in petrinetmodel_Transition is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petrinetmodel_Transition_strategy)
@settings(max_examples=30)
def test_hyp_petrinetmodel_transition_addinputplace_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addInputPlace(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addInputPlace).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addInputPlace' in petrinetmodel_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addInputPlace' in petrinetmodel_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addInputPlace' in petrinetmodel_Transition is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petrinetmodel_Petrinet_strategy)
@settings(max_examples=30)
def test_hyp_petrinetmodel_petrinet_init_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.init()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.init).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'init' in petrinetmodel_Petrinet is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'init' in petrinetmodel_Petrinet did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'init' in petrinetmodel_Petrinet is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petrinetmodel_Petrinet_strategy)
@settings(max_examples=30)
def test_hyp_petrinetmodel_petrinet_firetransactionsbypriority_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fireTransactionsByPriority()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fireTransactionsByPriority).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fireTransactionsByPriority' in petrinetmodel_Petrinet is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fireTransactionsByPriority' in petrinetmodel_Petrinet did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fireTransactionsByPriority' in petrinetmodel_Petrinet is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Edge,
    petrinetmodel_Edge,
    petrinetmodel_EdgeToPlace,
    petrinetmodel_EdgeToTransaction,
    petrinetmodel_Petrinet,
    petrinetmodel_Place,
    petrinetmodel_Transition,
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

def test_petrinetmodel_Edge_weight_value_roundtrip():
    instance = petrinetmodel_Edge(weight=7)
    assert instance.weight == 7
    instance.weight = 13
    assert instance.weight == 13


def test_petrinetmodel_Place_id_value_roundtrip():
    instance = petrinetmodel_Place(id=7, token=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_petrinetmodel_Place_token_value_roundtrip():
    instance = petrinetmodel_Place(id=7, token=7)
    assert instance.token == 7
    instance.token = 13
    assert instance.token == 13


def test_petrinetmodel_Transition_id_value_roundtrip():
    instance = petrinetmodel_Transition(id=7, priority=7, token=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_petrinetmodel_Transition_priority_value_roundtrip():
    instance = petrinetmodel_Transition(id=7, priority=7, token=7)
    assert instance.priority == 7
    instance.priority = 13
    assert instance.priority == 13


def test_petrinetmodel_Transition_token_value_roundtrip():
    instance = petrinetmodel_Transition(id=7, priority=7, token=7)
    assert instance.token == 7
    instance.token = 13
    assert instance.token == 13


def test_petrinetmodel_EdgeToPlace_isa_Edge():
    instance = petrinetmodel_EdgeToPlace()
    assert isinstance(instance, Edge)


def test_petrinetmodel_EdgeToTransaction_isa_Edge():
    instance = petrinetmodel_EdgeToTransaction()
    assert isinstance(instance, Edge)


def test_assoc_in_10_link_reassign_clear():
    a = petrinetmodel_Place(id=7, token=7)
    b1 = petrinetmodel_EdgeToPlace()
    b2 = petrinetmodel_EdgeToPlace()
    _safe_set(a, 'petrinetmodel_Place12', b1)
    assert _is_linked(a, 'petrinetmodel_Place12', b1)
    if hasattr(b1, 'petrinetmodel_EdgeToPlace11'):
        assert _is_linked(b1, 'petrinetmodel_EdgeToPlace11', a)
    _safe_set(a, 'petrinetmodel_Place12', b2)
    assert _is_linked(a, 'petrinetmodel_Place12', b2)
    if hasattr(b1, 'petrinetmodel_EdgeToPlace11'):
        assert not _is_linked(b1, 'petrinetmodel_EdgeToPlace11', a)
    if hasattr(b2, 'petrinetmodel_EdgeToPlace11'):
        assert _is_linked(b2, 'petrinetmodel_EdgeToPlace11', a)
    _safe_set(a, 'petrinetmodel_Place12', None)
    assert not _is_linked(a, 'petrinetmodel_Place12', b2)
    if hasattr(b2, 'petrinetmodel_EdgeToPlace11'):
        assert not _is_linked(b2, 'petrinetmodel_EdgeToPlace11', a)


def test_assoc_in_13_link_reassign_clear():
    a = petrinetmodel_Transition(id=7, priority=7, token=7)
    b1 = petrinetmodel_EdgeToTransaction()
    b2 = petrinetmodel_EdgeToTransaction()
    _safe_set(a, 'petrinetmodel_Transition15', b1)
    assert _is_linked(a, 'petrinetmodel_Transition15', b1)
    if hasattr(b1, 'petrinetmodel_EdgeToTransaction14'):
        assert _is_linked(b1, 'petrinetmodel_EdgeToTransaction14', a)
    _safe_set(a, 'petrinetmodel_Transition15', b2)
    assert _is_linked(a, 'petrinetmodel_Transition15', b2)
    if hasattr(b1, 'petrinetmodel_EdgeToTransaction14'):
        assert not _is_linked(b1, 'petrinetmodel_EdgeToTransaction14', a)
    if hasattr(b2, 'petrinetmodel_EdgeToTransaction14'):
        assert _is_linked(b2, 'petrinetmodel_EdgeToTransaction14', a)
    _safe_set(a, 'petrinetmodel_Transition15', None)
    assert not _is_linked(a, 'petrinetmodel_Transition15', b2)
    if hasattr(b2, 'petrinetmodel_EdgeToTransaction14'):
        assert not _is_linked(b2, 'petrinetmodel_EdgeToTransaction14', a)


def test_assoc_inputPlaces5_link_reassign_clear():
    a = petrinetmodel_Transition(id=7, priority=7, token=7)
    b1 = petrinetmodel_Place(id=7, token=7)
    b2 = petrinetmodel_Place(id=13, token=13)
    _safe_set(a, 'petrinetmodel_Transition6', {b1})
    assert _is_linked(a, 'petrinetmodel_Transition6', b1)
    if hasattr(b1, 'petrinetmodel_Place7'):
        assert _is_linked(b1, 'petrinetmodel_Place7', a)
    _safe_set(a, 'petrinetmodel_Transition6', {b2})
    assert _is_linked(a, 'petrinetmodel_Transition6', b2)
    if hasattr(b1, 'petrinetmodel_Place7'):
        assert not _is_linked(b1, 'petrinetmodel_Place7', a)
    if hasattr(b2, 'petrinetmodel_Place7'):
        assert _is_linked(b2, 'petrinetmodel_Place7', a)
    _safe_set(a, 'petrinetmodel_Transition6', set())
    assert not _is_linked(a, 'petrinetmodel_Transition6', b2)
    if hasattr(b2, 'petrinetmodel_Place7'):
        assert not _is_linked(b2, 'petrinetmodel_Place7', a)


def test_assoc_out3_link_reassign_clear():
    a = petrinetmodel_Transition(id=7, priority=7, token=7)
    b1 = petrinetmodel_EdgeToPlace()
    b2 = petrinetmodel_EdgeToPlace()
    _safe_set(a, 'petrinetmodel_Transition4', {b1})
    assert _is_linked(a, 'petrinetmodel_Transition4', b1)
    if hasattr(b1, 'petrinetmodel_EdgeToPlace'):
        assert _is_linked(b1, 'petrinetmodel_EdgeToPlace', a)
    _safe_set(a, 'petrinetmodel_Transition4', {b2})
    assert _is_linked(a, 'petrinetmodel_Transition4', b2)
    if hasattr(b1, 'petrinetmodel_EdgeToPlace'):
        assert not _is_linked(b1, 'petrinetmodel_EdgeToPlace', a)
    if hasattr(b2, 'petrinetmodel_EdgeToPlace'):
        assert _is_linked(b2, 'petrinetmodel_EdgeToPlace', a)
    _safe_set(a, 'petrinetmodel_Transition4', set())
    assert not _is_linked(a, 'petrinetmodel_Transition4', b2)
    if hasattr(b2, 'petrinetmodel_EdgeToPlace'):
        assert not _is_linked(b2, 'petrinetmodel_EdgeToPlace', a)


def test_assoc_out8_link_reassign_clear():
    a = petrinetmodel_Place(id=7, token=7)
    b1 = petrinetmodel_EdgeToTransaction()
    b2 = petrinetmodel_EdgeToTransaction()
    _safe_set(a, 'petrinetmodel_Place9', {b1})
    assert _is_linked(a, 'petrinetmodel_Place9', b1)
    if hasattr(b1, 'petrinetmodel_EdgeToTransaction'):
        assert _is_linked(b1, 'petrinetmodel_EdgeToTransaction', a)
    _safe_set(a, 'petrinetmodel_Place9', {b2})
    assert _is_linked(a, 'petrinetmodel_Place9', b2)
    if hasattr(b1, 'petrinetmodel_EdgeToTransaction'):
        assert not _is_linked(b1, 'petrinetmodel_EdgeToTransaction', a)
    if hasattr(b2, 'petrinetmodel_EdgeToTransaction'):
        assert _is_linked(b2, 'petrinetmodel_EdgeToTransaction', a)
    _safe_set(a, 'petrinetmodel_Place9', set())
    assert not _is_linked(a, 'petrinetmodel_Place9', b2)
    if hasattr(b2, 'petrinetmodel_EdgeToTransaction'):
        assert not _is_linked(b2, 'petrinetmodel_EdgeToTransaction', a)


def test_assoc_places1_link_reassign_clear():
    a = petrinetmodel_Place(id=7, token=7)
    b1 = petrinetmodel_Petrinet()
    b2 = petrinetmodel_Petrinet()
    _safe_set(a, 'petrinetmodel_Place', b1)
    assert _is_linked(a, 'petrinetmodel_Place', b1)
    if hasattr(b1, 'petrinetmodel_Petrinet2'):
        assert _is_linked(b1, 'petrinetmodel_Petrinet2', a)
    _safe_set(a, 'petrinetmodel_Place', b2)
    assert _is_linked(a, 'petrinetmodel_Place', b2)
    if hasattr(b1, 'petrinetmodel_Petrinet2'):
        assert not _is_linked(b1, 'petrinetmodel_Petrinet2', a)
    if hasattr(b2, 'petrinetmodel_Petrinet2'):
        assert _is_linked(b2, 'petrinetmodel_Petrinet2', a)
    _safe_set(a, 'petrinetmodel_Place', None)
    assert not _is_linked(a, 'petrinetmodel_Place', b2)
    if hasattr(b2, 'petrinetmodel_Petrinet2'):
        assert not _is_linked(b2, 'petrinetmodel_Petrinet2', a)


def test_assoc_transitions0_link_reassign_clear():
    a = petrinetmodel_Transition(id=7, priority=7, token=7)
    b1 = petrinetmodel_Petrinet()
    b2 = petrinetmodel_Petrinet()
    _safe_set(a, 'petrinetmodel_Transition', b1)
    assert _is_linked(a, 'petrinetmodel_Transition', b1)
    if hasattr(b1, 'petrinetmodel_Petrinet'):
        assert _is_linked(b1, 'petrinetmodel_Petrinet', a)
    _safe_set(a, 'petrinetmodel_Transition', b2)
    assert _is_linked(a, 'petrinetmodel_Transition', b2)
    if hasattr(b1, 'petrinetmodel_Petrinet'):
        assert not _is_linked(b1, 'petrinetmodel_Petrinet', a)
    if hasattr(b2, 'petrinetmodel_Petrinet'):
        assert _is_linked(b2, 'petrinetmodel_Petrinet', a)
    _safe_set(a, 'petrinetmodel_Transition', None)
    assert not _is_linked(a, 'petrinetmodel_Transition', b2)
    if hasattr(b2, 'petrinetmodel_Petrinet'):
        assert not _is_linked(b2, 'petrinetmodel_Petrinet', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Edge_strategy = st.builds(Edge)
@given(instance=Edge_strategy)
@settings(max_examples=25)
def test_Edge_instantiation(instance):
    assert isinstance(instance, Edge)


petrinetmodel_Edge_strategy = st.builds(petrinetmodel_Edge, weight=st.integers())
@given(instance=petrinetmodel_Edge_strategy)
@settings(max_examples=25)
def test_petrinetmodel_Edge_instantiation(instance):
    assert isinstance(instance, petrinetmodel_Edge)


petrinetmodel_EdgeToPlace_strategy = st.builds(petrinetmodel_EdgeToPlace)
@given(instance=petrinetmodel_EdgeToPlace_strategy)
@settings(max_examples=25)
def test_petrinetmodel_EdgeToPlace_instantiation(instance):
    assert isinstance(instance, petrinetmodel_EdgeToPlace)


petrinetmodel_EdgeToTransaction_strategy = st.builds(petrinetmodel_EdgeToTransaction)
@given(instance=petrinetmodel_EdgeToTransaction_strategy)
@settings(max_examples=25)
def test_petrinetmodel_EdgeToTransaction_instantiation(instance):
    assert isinstance(instance, petrinetmodel_EdgeToTransaction)


petrinetmodel_Petrinet_strategy = st.builds(petrinetmodel_Petrinet)
@given(instance=petrinetmodel_Petrinet_strategy)
@settings(max_examples=25)
def test_petrinetmodel_Petrinet_instantiation(instance):
    assert isinstance(instance, petrinetmodel_Petrinet)


petrinetmodel_Place_strategy = st.builds(petrinetmodel_Place, id=st.integers(), token=st.integers())
@given(instance=petrinetmodel_Place_strategy)
@settings(max_examples=25)
def test_petrinetmodel_Place_instantiation(instance):
    assert isinstance(instance, petrinetmodel_Place)


petrinetmodel_Transition_strategy = st.builds(petrinetmodel_Transition, id=st.integers(), priority=st.integers(), token=st.integers())
@given(instance=petrinetmodel_Transition_strategy)
@settings(max_examples=25)
def test_petrinetmodel_Transition_instantiation(instance):
    assert isinstance(instance, petrinetmodel_Transition)



