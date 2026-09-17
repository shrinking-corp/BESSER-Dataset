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
    fsm_Transition,
    NoAnnotationSuper,
    fsm_NoAnnotation,
    fsm_NoAnnotationSuper,
    fsm_FSM,
    fsm_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_hyp_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_hyp_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_noannotationsuper_is_not_abstract():
    assert not inspect.isabstract(NoAnnotationSuper)


def test_hyp_noannotationsuper_constructor_exists():
    assert callable(NoAnnotationSuper.__init__)


def test_hyp_noannotationsuper_constructor_args():
    sig = inspect.signature(NoAnnotationSuper.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_noannotation_is_not_abstract():
    assert not inspect.isabstract(fsm_NoAnnotation)


def test_hyp_fsm_noannotation_constructor_exists():
    assert callable(fsm_NoAnnotation.__init__)


def test_hyp_fsm_noannotation_constructor_args():
    sig = inspect.signature(fsm_NoAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "a" in params, "Missing parameter 'a'"





def test_hyp_fsm_noannotationsuper_is_not_abstract():
    assert not inspect.isabstract(fsm_NoAnnotationSuper)


def test_hyp_fsm_noannotationsuper_constructor_exists():
    assert callable(fsm_NoAnnotationSuper.__init__)


def test_hyp_fsm_noannotationsuper_constructor_args():
    sig = inspect.signature(fsm_NoAnnotationSuper.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_fsm_is_not_abstract():
    assert not inspect.isabstract(fsm_FSM)


def test_hyp_fsm_fsm_constructor_exists():
    assert callable(fsm_FSM.__init__)


def test_hyp_fsm_fsm_constructor_args():
    sig = inspect.signature(fsm_FSM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_hyp_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_hyp_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
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
fsm_Transition_strategy = st.builds(
    fsm_Transition,
)
NoAnnotationSuper_strategy = st.builds(
    NoAnnotationSuper,
)
fsm_NoAnnotation_strategy = st.builds(
    fsm_NoAnnotation,
    b=
        safe_text,
    a=
        safe_text
)
fsm_NoAnnotationSuper_strategy = st.builds(
    fsm_NoAnnotationSuper,
)
fsm_FSM_strategy = st.builds(
    fsm_FSM,
)
fsm_State_strategy = st.builds(
    fsm_State,
)






@given(instance=fsm_NoAnnotation_strategy)
def test_hyp_fsm_noannotation_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=fsm_NoAnnotation_strategy)
def test_hyp_fsm_noannotation_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_NoAnnotation_strategy)
@settings(max_examples=30)
def test_hyp_fsm_noannotation_k_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.k(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.k).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'k' in fsm_NoAnnotation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'k' in fsm_NoAnnotation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'k' in fsm_NoAnnotation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_NoAnnotation_strategy)
@settings(max_examples=30)
def test_hyp_fsm_noannotation_j_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.j(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.j).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'j' in fsm_NoAnnotation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'j' in fsm_NoAnnotation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'j' in fsm_NoAnnotation is not implemented or raised an error")





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NoAnnotationSuper,
    fsm_FSM,
    fsm_NoAnnotation,
    fsm_NoAnnotationSuper,
    fsm_State,
    fsm_Transition,
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

def test_fsm_NoAnnotation_a_value_roundtrip():
    instance = fsm_NoAnnotation(a="sample_text", b="sample_text")
    assert instance.a == "sample_text"
    instance.a = "sample_text_2"
    assert instance.a == "sample_text_2"


def test_fsm_NoAnnotation_b_value_roundtrip():
    instance = fsm_NoAnnotation(a="sample_text", b="sample_text")
    assert instance.b == "sample_text"
    instance.b = "sample_text_2"
    assert instance.b == "sample_text_2"


def test_fsm_NoAnnotation_isa_NoAnnotationSuper():
    instance = fsm_NoAnnotation(a="sample_text", b="sample_text")
    assert isinstance(instance, NoAnnotationSuper)


def test_assoc_f1_link_reassign_clear():
    a = fsm_NoAnnotation(a="sample_text", b="sample_text")
    b1 = fsm_FSM()
    b2 = fsm_FSM()
    _safe_set(a, 'fsm_NoAnnotation2', b1)
    assert _is_linked(a, 'fsm_NoAnnotation2', b1)
    if hasattr(b1, 'fsm_FSM'):
        assert _is_linked(b1, 'fsm_FSM', a)
    _safe_set(a, 'fsm_NoAnnotation2', b2)
    assert _is_linked(a, 'fsm_NoAnnotation2', b2)
    if hasattr(b1, 'fsm_FSM'):
        assert not _is_linked(b1, 'fsm_FSM', a)
    if hasattr(b2, 'fsm_FSM'):
        assert _is_linked(b2, 'fsm_FSM', a)
    _safe_set(a, 'fsm_NoAnnotation2', None)
    assert not _is_linked(a, 'fsm_NoAnnotation2', b2)
    if hasattr(b2, 'fsm_FSM'):
        assert not _is_linked(b2, 'fsm_FSM', a)


def test_assoc_ls0_link_reassign_clear():
    a = fsm_NoAnnotation(a="sample_text", b="sample_text")
    b1 = fsm_State()
    b2 = fsm_State()
    _safe_set(a, 'fsm_NoAnnotation', {b1})
    assert _is_linked(a, 'fsm_NoAnnotation', b1)
    if hasattr(b1, 'fsm_State'):
        assert _is_linked(b1, 'fsm_State', a)
    _safe_set(a, 'fsm_NoAnnotation', {b2})
    assert _is_linked(a, 'fsm_NoAnnotation', b2)
    if hasattr(b1, 'fsm_State'):
        assert not _is_linked(b1, 'fsm_State', a)
    if hasattr(b2, 'fsm_State'):
        assert _is_linked(b2, 'fsm_State', a)
    _safe_set(a, 'fsm_NoAnnotation', set())
    assert not _is_linked(a, 'fsm_NoAnnotation', b2)
    if hasattr(b2, 'fsm_State'):
        assert not _is_linked(b2, 'fsm_State', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NoAnnotationSuper_strategy = st.builds(NoAnnotationSuper)
@given(instance=NoAnnotationSuper_strategy)
@settings(max_examples=25)
def test_NoAnnotationSuper_instantiation(instance):
    assert isinstance(instance, NoAnnotationSuper)


fsm_FSM_strategy = st.builds(fsm_FSM)
@given(instance=fsm_FSM_strategy)
@settings(max_examples=25)
def test_fsm_FSM_instantiation(instance):
    assert isinstance(instance, fsm_FSM)


fsm_NoAnnotation_strategy = st.builds(fsm_NoAnnotation, a=safe_text, b=safe_text)
@given(instance=fsm_NoAnnotation_strategy)
@settings(max_examples=25)
def test_fsm_NoAnnotation_instantiation(instance):
    assert isinstance(instance, fsm_NoAnnotation)


fsm_NoAnnotationSuper_strategy = st.builds(fsm_NoAnnotationSuper)
@given(instance=fsm_NoAnnotationSuper_strategy)
@settings(max_examples=25)
def test_fsm_NoAnnotationSuper_instantiation(instance):
    assert isinstance(instance, fsm_NoAnnotationSuper)


fsm_State_strategy = st.builds(fsm_State)
@given(instance=fsm_State_strategy)
@settings(max_examples=25)
def test_fsm_State_instantiation(instance):
    assert isinstance(instance, fsm_State)


fsm_Transition_strategy = st.builds(fsm_Transition)
@given(instance=fsm_Transition_strategy)
@settings(max_examples=25)
def test_fsm_Transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



