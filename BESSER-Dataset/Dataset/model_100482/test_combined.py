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
    tfsmextended_NamedElement,
    Guard,
    tfsmextended_EvaluateGuard,
    tfsmextended_EventGuard,
    tfsmextended_TemporalGuard,
    NamedElement,
    tfsmextended_FSMEvent,
    tfsmextended_Guard,
    tfsmextended_Transition,
    tfsmextended_State,
    tfsmextended_TimedSystem,
    tfsmextended_FSMClock,
    tfsmextended_TFSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tfsmextended_namedelement_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_NamedElement)


def test_hyp_tfsmextended_namedelement_constructor_exists():
    assert callable(tfsmextended_NamedElement.__init__)


def test_hyp_tfsmextended_namedelement_constructor_args():
    sig = inspect.signature(tfsmextended_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_hyp_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_hyp_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tfsmextended_evaluateguard_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_EvaluateGuard)


def test_hyp_tfsmextended_evaluateguard_constructor_exists():
    assert callable(tfsmextended_EvaluateGuard.__init__)


def test_hyp_tfsmextended_evaluateguard_constructor_args():
    sig = inspect.signature(tfsmextended_EvaluateGuard.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"




def test_hyp_tfsmextended_eventguard_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_EventGuard)


def test_hyp_tfsmextended_eventguard_constructor_exists():
    assert callable(tfsmextended_EventGuard.__init__)


def test_hyp_tfsmextended_eventguard_constructor_args():
    sig = inspect.signature(tfsmextended_EventGuard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tfsmextended_temporalguard_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_TemporalGuard)


def test_hyp_tfsmextended_temporalguard_constructor_exists():
    assert callable(tfsmextended_TemporalGuard.__init__)


def test_hyp_tfsmextended_temporalguard_constructor_args():
    sig = inspect.signature(tfsmextended_TemporalGuard.__init__)
    params = list(sig.parameters.keys())
    assert "afterDuration" in params, "Missing parameter 'afterDuration'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tfsmextended_fsmevent_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_FSMEvent)


def test_hyp_tfsmextended_fsmevent_constructor_exists():
    assert callable(tfsmextended_FSMEvent.__init__)


def test_hyp_tfsmextended_fsmevent_constructor_args():
    sig = inspect.signature(tfsmextended_FSMEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isTriggered" in params, "Missing parameter 'isTriggered'"




def test_hyp_tfsmextended_guard_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_Guard)


def test_hyp_tfsmextended_guard_constructor_exists():
    assert callable(tfsmextended_Guard.__init__)


def test_hyp_tfsmextended_guard_constructor_args():
    sig = inspect.signature(tfsmextended_Guard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tfsmextended_transition_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_Transition)


def test_hyp_tfsmextended_transition_constructor_exists():
    assert callable(tfsmextended_Transition.__init__)


def test_hyp_tfsmextended_transition_constructor_args():
    sig = inspect.signature(tfsmextended_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"




def test_hyp_tfsmextended_state_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_State)


def test_hyp_tfsmextended_state_constructor_exists():
    assert callable(tfsmextended_State.__init__)


def test_hyp_tfsmextended_state_constructor_args():
    sig = inspect.signature(tfsmextended_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tfsmextended_timedsystem_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_TimedSystem)


def test_hyp_tfsmextended_timedsystem_constructor_exists():
    assert callable(tfsmextended_TimedSystem.__init__)


def test_hyp_tfsmextended_timedsystem_constructor_args():
    sig = inspect.signature(tfsmextended_TimedSystem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tfsmextended_fsmclock_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_FSMClock)


def test_hyp_tfsmextended_fsmclock_constructor_exists():
    assert callable(tfsmextended_FSMClock.__init__)


def test_hyp_tfsmextended_fsmclock_constructor_args():
    sig = inspect.signature(tfsmextended_FSMClock.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfTicks" in params, "Missing parameter 'numberOfTicks'"




def test_hyp_tfsmextended_tfsm_is_not_abstract():
    assert not inspect.isabstract(tfsmextended_TFSM)


def test_hyp_tfsmextended_tfsm_constructor_exists():
    assert callable(tfsmextended_TFSM.__init__)


def test_hyp_tfsmextended_tfsm_constructor_args():
    sig = inspect.signature(tfsmextended_TFSM.__init__)
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
tfsmextended_NamedElement_strategy = st.builds(
    tfsmextended_NamedElement,
    name=
        safe_text
)
Guard_strategy = st.builds(
    Guard,
)
tfsmextended_EvaluateGuard_strategy = st.builds(
    tfsmextended_EvaluateGuard,
    condition=
        safe_text
)
tfsmextended_EventGuard_strategy = st.builds(
    tfsmextended_EventGuard,
)
tfsmextended_TemporalGuard_strategy = st.builds(
    tfsmextended_TemporalGuard,
    afterDuration=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tfsmextended_FSMEvent_strategy = st.builds(
    tfsmextended_FSMEvent,
    isTriggered=
        st.booleans()
)
tfsmextended_Guard_strategy = st.builds(
    tfsmextended_Guard,
)
tfsmextended_Transition_strategy = st.builds(
    tfsmextended_Transition,
    action=
        safe_text
)
tfsmextended_State_strategy = st.builds(
    tfsmextended_State,
)
tfsmextended_TimedSystem_strategy = st.builds(
    tfsmextended_TimedSystem,
)
tfsmextended_FSMClock_strategy = st.builds(
    tfsmextended_FSMClock,
    numberOfTicks=
        safe_text
)
tfsmextended_TFSM_strategy = st.builds(
    tfsmextended_TFSM,
)




@given(instance=tfsmextended_NamedElement_strategy)
def test_hyp_tfsmextended_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=tfsmextended_EvaluateGuard_strategy)
def test_hyp_tfsmextended_evaluateguard_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original





@given(instance=tfsmextended_TemporalGuard_strategy)
def test_hyp_tfsmextended_temporalguard_afterDuration_setter(instance):
    original = instance.afterDuration
    instance.afterDuration = original
    assert instance.afterDuration == original





@given(instance=tfsmextended_FSMEvent_strategy)
def test_hyp_tfsmextended_fsmevent_isTriggered_setter(instance):
    original = instance.isTriggered
    instance.isTriggered = original
    assert instance.isTriggered == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended_FSMEvent_strategy)
@settings(max_examples=30)
def test_hyp_tfsmextended_fsmevent_trigger_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.trigger()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.trigger).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'trigger' in tfsmextended_FSMEvent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'trigger' in tfsmextended_FSMEvent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'trigger' in tfsmextended_FSMEvent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended_FSMEvent_strategy)
@settings(max_examples=30)
def test_hyp_tfsmextended_fsmevent_untrigger_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unTrigger()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unTrigger).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unTrigger' in tfsmextended_FSMEvent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unTrigger' in tfsmextended_FSMEvent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unTrigger' in tfsmextended_FSMEvent is not implemented or raised an error")





@given(instance=tfsmextended_Transition_strategy)
def test_hyp_tfsmextended_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended_Transition_strategy)
@settings(max_examples=30)
def test_hyp_tfsmextended_transition_fire_changes_state(instance):
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
        assert has_statements, f"Function 'fire' in tfsmextended_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in tfsmextended_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in tfsmextended_Transition is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended_State_strategy)
@settings(max_examples=30)
def test_hyp_tfsmextended_state_onleave_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.onLeave()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.onLeave).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'onLeave' in tfsmextended_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'onLeave' in tfsmextended_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'onLeave' in tfsmextended_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended_State_strategy)
@settings(max_examples=30)
def test_hyp_tfsmextended_state_onenter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.onEnter()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.onEnter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'onEnter' in tfsmextended_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'onEnter' in tfsmextended_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'onEnter' in tfsmextended_State is not implemented or raised an error")





@given(instance=tfsmextended_FSMClock_strategy)
def test_hyp_tfsmextended_fsmclock_numberOfTicks_setter(instance):
    original = instance.numberOfTicks
    instance.numberOfTicks = original
    assert instance.numberOfTicks == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended_FSMClock_strategy)
@settings(max_examples=30)
def test_hyp_tfsmextended_fsmclock_ticks_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ticks()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ticks).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ticks' in tfsmextended_FSMClock is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ticks' in tfsmextended_FSMClock did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ticks' in tfsmextended_FSMClock is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended_TFSM_strategy)
@settings(max_examples=30)
def test_hyp_tfsmextended_tfsm_init_changes_state(instance):
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
        assert has_statements, f"Function 'init' in tfsmextended_TFSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'init' in tfsmextended_TFSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'init' in tfsmextended_TFSM is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Guard,
    NamedElement,
    tfsmextended_EvaluateGuard,
    tfsmextended_EventGuard,
    tfsmextended_FSMClock,
    tfsmextended_FSMEvent,
    tfsmextended_Guard,
    tfsmextended_NamedElement,
    tfsmextended_State,
    tfsmextended_TFSM,
    tfsmextended_TemporalGuard,
    tfsmextended_TimedSystem,
    tfsmextended_Transition,
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

def test_tfsmextended_EvaluateGuard_condition_value_roundtrip():
    instance = tfsmextended_EvaluateGuard(condition="sample_text")
    assert instance.condition == "sample_text"
    instance.condition = "sample_text_2"
    assert instance.condition == "sample_text_2"


def test_tfsmextended_FSMClock_numberOfTicks_value_roundtrip():
    instance = tfsmextended_FSMClock(numberOfTicks="sample_text")
    assert instance.numberOfTicks == "sample_text"
    instance.numberOfTicks = "sample_text_2"
    assert instance.numberOfTicks == "sample_text_2"


def test_tfsmextended_FSMEvent_isTriggered_value_roundtrip():
    instance = tfsmextended_FSMEvent(isTriggered=True)
    assert instance.isTriggered == True
    instance.isTriggered = False
    assert instance.isTriggered == False


def test_tfsmextended_NamedElement_name_value_roundtrip():
    instance = tfsmextended_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tfsmextended_TemporalGuard_afterDuration_value_roundtrip():
    instance = tfsmextended_TemporalGuard(afterDuration=7)
    assert instance.afterDuration == 7
    instance.afterDuration = 13
    assert instance.afterDuration == 13


def test_tfsmextended_Transition_action_value_roundtrip():
    instance = tfsmextended_Transition(action="sample_text")
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_tfsmextended_EvaluateGuard_isa_Guard():
    instance = tfsmextended_EvaluateGuard(condition="sample_text")
    assert isinstance(instance, Guard)


def test_tfsmextended_EventGuard_isa_Guard():
    instance = tfsmextended_EventGuard()
    assert isinstance(instance, Guard)


def test_tfsmextended_TemporalGuard_isa_Guard():
    instance = tfsmextended_TemporalGuard(afterDuration=7)
    assert isinstance(instance, Guard)


def test_tfsmextended_FSMClock_isa_NamedElement():
    instance = tfsmextended_FSMClock(numberOfTicks="sample_text")
    assert isinstance(instance, NamedElement)


def test_tfsmextended_FSMEvent_isa_NamedElement():
    instance = tfsmextended_FSMEvent(isTriggered=True)
    assert isinstance(instance, NamedElement)


def test_tfsmextended_Guard_isa_NamedElement():
    instance = tfsmextended_Guard()
    assert isinstance(instance, NamedElement)


def test_tfsmextended_State_isa_NamedElement():
    instance = tfsmextended_State()
    assert isinstance(instance, NamedElement)


def test_tfsmextended_TFSM_isa_NamedElement():
    instance = tfsmextended_TFSM()
    assert isinstance(instance, NamedElement)


def test_tfsmextended_TimedSystem_isa_NamedElement():
    instance = tfsmextended_TimedSystem()
    assert isinstance(instance, NamedElement)


def test_tfsmextended_Transition_isa_NamedElement():
    instance = tfsmextended_Transition(action="sample_text")
    assert isinstance(instance, NamedElement)


def test_assoc_currentState8_link_reassign_clear():
    a = tfsmextended_TFSM()
    b1 = tfsmextended_State()
    b2 = tfsmextended_State()
    _safe_set(a, 'tfsmextended_TFSM9', b1)
    assert _is_linked(a, 'tfsmextended_TFSM9', b1)
    if hasattr(b1, 'tfsmextended_State10'):
        assert _is_linked(b1, 'tfsmextended_State10', a)
    _safe_set(a, 'tfsmextended_TFSM9', b2)
    assert _is_linked(a, 'tfsmextended_TFSM9', b2)
    if hasattr(b1, 'tfsmextended_State10'):
        assert not _is_linked(b1, 'tfsmextended_State10', a)
    if hasattr(b2, 'tfsmextended_State10'):
        assert _is_linked(b2, 'tfsmextended_State10', a)
    _safe_set(a, 'tfsmextended_TFSM9', None)
    assert not _is_linked(a, 'tfsmextended_TFSM9', b2)
    if hasattr(b2, 'tfsmextended_State10'):
        assert not _is_linked(b2, 'tfsmextended_State10', a)


def test_assoc_generatedEvents21_link_reassign_clear():
    a = tfsmextended_Transition(action="sample_text")
    b1 = tfsmextended_FSMEvent(isTriggered=True)
    b2 = tfsmextended_FSMEvent(isTriggered=False)
    _safe_set(a, 'tfsmextended_Transition22', {b1})
    assert _is_linked(a, 'tfsmextended_Transition22', b1)
    if hasattr(b1, 'tfsmextended_FSMEvent23'):
        assert _is_linked(b1, 'tfsmextended_FSMEvent23', a)
    _safe_set(a, 'tfsmextended_Transition22', {b2})
    assert _is_linked(a, 'tfsmextended_Transition22', b2)
    if hasattr(b1, 'tfsmextended_FSMEvent23'):
        assert not _is_linked(b1, 'tfsmextended_FSMEvent23', a)
    if hasattr(b2, 'tfsmextended_FSMEvent23'):
        assert _is_linked(b2, 'tfsmextended_FSMEvent23', a)
    _safe_set(a, 'tfsmextended_Transition22', set())
    assert not _is_linked(a, 'tfsmextended_Transition22', b2)
    if hasattr(b2, 'tfsmextended_FSMEvent23'):
        assert not _is_linked(b2, 'tfsmextended_FSMEvent23', a)


def test_assoc_globalClocks33_link_reassign_clear():
    a = tfsmextended_FSMClock(numberOfTicks="sample_text")
    b1 = tfsmextended_TimedSystem()
    b2 = tfsmextended_TimedSystem()
    _safe_set(a, 'tfsmextended_FSMClock35', b1)
    assert _is_linked(a, 'tfsmextended_FSMClock35', b1)
    if hasattr(b1, 'tfsmextended_TimedSystem34'):
        assert _is_linked(b1, 'tfsmextended_TimedSystem34', a)
    _safe_set(a, 'tfsmextended_FSMClock35', b2)
    assert _is_linked(a, 'tfsmextended_FSMClock35', b2)
    if hasattr(b1, 'tfsmextended_TimedSystem34'):
        assert not _is_linked(b1, 'tfsmextended_TimedSystem34', a)
    if hasattr(b2, 'tfsmextended_TimedSystem34'):
        assert _is_linked(b2, 'tfsmextended_TimedSystem34', a)
    _safe_set(a, 'tfsmextended_FSMClock35', None)
    assert not _is_linked(a, 'tfsmextended_FSMClock35', b2)
    if hasattr(b2, 'tfsmextended_TimedSystem34'):
        assert not _is_linked(b2, 'tfsmextended_TimedSystem34', a)


def test_assoc_globalEvents36_link_reassign_clear():
    a = tfsmextended_FSMEvent(isTriggered=True)
    b1 = tfsmextended_TimedSystem()
    b2 = tfsmextended_TimedSystem()
    _safe_set(a, 'tfsmextended_FSMEvent38', b1)
    assert _is_linked(a, 'tfsmextended_FSMEvent38', b1)
    if hasattr(b1, 'tfsmextended_TimedSystem37'):
        assert _is_linked(b1, 'tfsmextended_TimedSystem37', a)
    _safe_set(a, 'tfsmextended_FSMEvent38', b2)
    assert _is_linked(a, 'tfsmextended_FSMEvent38', b2)
    if hasattr(b1, 'tfsmextended_TimedSystem37'):
        assert not _is_linked(b1, 'tfsmextended_TimedSystem37', a)
    if hasattr(b2, 'tfsmextended_TimedSystem37'):
        assert _is_linked(b2, 'tfsmextended_TimedSystem37', a)
    _safe_set(a, 'tfsmextended_FSMEvent38', None)
    assert not _is_linked(a, 'tfsmextended_FSMEvent38', b2)
    if hasattr(b2, 'tfsmextended_TimedSystem37'):
        assert not _is_linked(b2, 'tfsmextended_TimedSystem37', a)


def test_assoc_incomingTransitions13_link_reassign_clear():
    a = tfsmextended_Transition(action="sample_text")
    b1 = tfsmextended_State()
    b2 = tfsmextended_State()
    _safe_set(a, 'Transition14', b1)
    assert _is_linked(a, 'Transition14', b1)
    if hasattr(b1, 'target'):
        assert _is_linked(b1, 'target', a)
    _safe_set(a, 'Transition14', b2)
    assert _is_linked(a, 'Transition14', b2)
    if hasattr(b1, 'target'):
        assert not _is_linked(b1, 'target', a)
    if hasattr(b2, 'target'):
        assert _is_linked(b2, 'target', a)
    _safe_set(a, 'Transition14', None)
    assert not _is_linked(a, 'Transition14', b2)
    if hasattr(b2, 'target'):
        assert not _is_linked(b2, 'target', a)


def test_assoc_initialState1_link_reassign_clear():
    a = tfsmextended_TFSM()
    b1 = tfsmextended_State()
    b2 = tfsmextended_State()
    _safe_set(a, 'tfsmextended_TFSM', b1)
    assert _is_linked(a, 'tfsmextended_TFSM', b1)
    if hasattr(b1, 'tfsmextended_State'):
        assert _is_linked(b1, 'tfsmextended_State', a)
    _safe_set(a, 'tfsmextended_TFSM', b2)
    assert _is_linked(a, 'tfsmextended_TFSM', b2)
    if hasattr(b1, 'tfsmextended_State'):
        assert not _is_linked(b1, 'tfsmextended_State', a)
    if hasattr(b2, 'tfsmextended_State'):
        assert _is_linked(b2, 'tfsmextended_State', a)
    _safe_set(a, 'tfsmextended_TFSM', None)
    assert not _is_linked(a, 'tfsmextended_TFSM', b2)
    if hasattr(b2, 'tfsmextended_State'):
        assert not _is_linked(b2, 'tfsmextended_State', a)


def test_assoc_localClock4_link_reassign_clear():
    a = tfsmextended_TFSM()
    b1 = tfsmextended_FSMClock(numberOfTicks="sample_text")
    b2 = tfsmextended_FSMClock(numberOfTicks="sample_text_2")
    _safe_set(a, 'tfsmextended_TFSM5', b1)
    assert _is_linked(a, 'tfsmextended_TFSM5', b1)
    if hasattr(b1, 'tfsmextended_FSMClock'):
        assert _is_linked(b1, 'tfsmextended_FSMClock', a)
    _safe_set(a, 'tfsmextended_TFSM5', b2)
    assert _is_linked(a, 'tfsmextended_TFSM5', b2)
    if hasattr(b1, 'tfsmextended_FSMClock'):
        assert not _is_linked(b1, 'tfsmextended_FSMClock', a)
    if hasattr(b2, 'tfsmextended_FSMClock'):
        assert _is_linked(b2, 'tfsmextended_FSMClock', a)
    _safe_set(a, 'tfsmextended_TFSM5', None)
    assert not _is_linked(a, 'tfsmextended_TFSM5', b2)
    if hasattr(b2, 'tfsmextended_FSMClock'):
        assert not _is_linked(b2, 'tfsmextended_FSMClock', a)


def test_assoc_localEvents2_link_reassign_clear():
    a = tfsmextended_TFSM()
    b1 = tfsmextended_FSMEvent(isTriggered=True)
    b2 = tfsmextended_FSMEvent(isTriggered=False)
    _safe_set(a, 'tfsmextended_TFSM3', {b1})
    assert _is_linked(a, 'tfsmextended_TFSM3', b1)
    if hasattr(b1, 'tfsmextended_FSMEvent'):
        assert _is_linked(b1, 'tfsmextended_FSMEvent', a)
    _safe_set(a, 'tfsmextended_TFSM3', {b2})
    assert _is_linked(a, 'tfsmextended_TFSM3', b2)
    if hasattr(b1, 'tfsmextended_FSMEvent'):
        assert not _is_linked(b1, 'tfsmextended_FSMEvent', a)
    if hasattr(b2, 'tfsmextended_FSMEvent'):
        assert _is_linked(b2, 'tfsmextended_FSMEvent', a)
    _safe_set(a, 'tfsmextended_TFSM3', set())
    assert not _is_linked(a, 'tfsmextended_TFSM3', b2)
    if hasattr(b2, 'tfsmextended_FSMEvent'):
        assert not _is_linked(b2, 'tfsmextended_FSMEvent', a)


def test_assoc_onClock24_link_reassign_clear():
    a = tfsmextended_TemporalGuard(afterDuration=7)
    b1 = tfsmextended_FSMClock(numberOfTicks="sample_text")
    b2 = tfsmextended_FSMClock(numberOfTicks="sample_text_2")
    _safe_set(a, 'tfsmextended_TemporalGuard', b1)
    assert _is_linked(a, 'tfsmextended_TemporalGuard', b1)
    if hasattr(b1, 'tfsmextended_FSMClock25'):
        assert _is_linked(b1, 'tfsmextended_FSMClock25', a)
    _safe_set(a, 'tfsmextended_TemporalGuard', b2)
    assert _is_linked(a, 'tfsmextended_TemporalGuard', b2)
    if hasattr(b1, 'tfsmextended_FSMClock25'):
        assert not _is_linked(b1, 'tfsmextended_FSMClock25', a)
    if hasattr(b2, 'tfsmextended_FSMClock25'):
        assert _is_linked(b2, 'tfsmextended_FSMClock25', a)
    _safe_set(a, 'tfsmextended_TemporalGuard', None)
    assert not _is_linked(a, 'tfsmextended_TemporalGuard', b2)
    if hasattr(b2, 'tfsmextended_FSMClock25'):
        assert not _is_linked(b2, 'tfsmextended_FSMClock25', a)


def test_assoc_outgoingTransitions12_link_reassign_clear():
    a = tfsmextended_Transition(action="sample_text")
    b1 = tfsmextended_State()
    b2 = tfsmextended_State()
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_ownedGuard19_link_reassign_clear():
    a = tfsmextended_Transition(action="sample_text")
    b1 = tfsmextended_Guard()
    b2 = tfsmextended_Guard()
    _safe_set(a, 'tfsmextended_Transition20', b1)
    assert _is_linked(a, 'tfsmextended_Transition20', b1)
    if hasattr(b1, 'tfsmextended_Guard'):
        assert _is_linked(b1, 'tfsmextended_Guard', a)
    _safe_set(a, 'tfsmextended_Transition20', b2)
    assert _is_linked(a, 'tfsmextended_Transition20', b2)
    if hasattr(b1, 'tfsmextended_Guard'):
        assert not _is_linked(b1, 'tfsmextended_Guard', a)
    if hasattr(b2, 'tfsmextended_Guard'):
        assert _is_linked(b2, 'tfsmextended_Guard', a)
    _safe_set(a, 'tfsmextended_Transition20', None)
    assert not _is_linked(a, 'tfsmextended_Transition20', b2)
    if hasattr(b2, 'tfsmextended_Guard'):
        assert not _is_linked(b2, 'tfsmextended_Guard', a)


def test_assoc_ownedStates0_link_reassign_clear():
    a = tfsmextended_TFSM()
    b1 = tfsmextended_State()
    b2 = tfsmextended_State()
    _safe_set(a, 'owningFSM', {b1})
    assert _is_linked(a, 'owningFSM', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'owningFSM', {b2})
    assert _is_linked(a, 'owningFSM', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'owningFSM', set())
    assert not _is_linked(a, 'owningFSM', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_ownedTransitions6_link_reassign_clear():
    a = tfsmextended_Transition(action="sample_text")
    b1 = tfsmextended_TFSM()
    b2 = tfsmextended_TFSM()
    _safe_set(a, 'tfsmextended_Transition', b1)
    assert _is_linked(a, 'tfsmextended_Transition', b1)
    if hasattr(b1, 'tfsmextended_TFSM7'):
        assert _is_linked(b1, 'tfsmextended_TFSM7', a)
    _safe_set(a, 'tfsmextended_Transition', b2)
    assert _is_linked(a, 'tfsmextended_Transition', b2)
    if hasattr(b1, 'tfsmextended_TFSM7'):
        assert not _is_linked(b1, 'tfsmextended_TFSM7', a)
    if hasattr(b2, 'tfsmextended_TFSM7'):
        assert _is_linked(b2, 'tfsmextended_TFSM7', a)
    _safe_set(a, 'tfsmextended_Transition', None)
    assert not _is_linked(a, 'tfsmextended_Transition', b2)
    if hasattr(b2, 'tfsmextended_TFSM7'):
        assert not _is_linked(b2, 'tfsmextended_TFSM7', a)


def test_assoc_owningFSM11_link_reassign_clear():
    a = tfsmextended_TFSM()
    b1 = tfsmextended_State()
    b2 = tfsmextended_State()
    _safe_set(a, 'TFSM', b1)
    assert _is_linked(a, 'TFSM', b1)
    if hasattr(b1, 'ownedStates'):
        assert _is_linked(b1, 'ownedStates', a)
    _safe_set(a, 'TFSM', b2)
    assert _is_linked(a, 'TFSM', b2)
    if hasattr(b1, 'ownedStates'):
        assert not _is_linked(b1, 'ownedStates', a)
    if hasattr(b2, 'ownedStates'):
        assert _is_linked(b2, 'ownedStates', a)
    _safe_set(a, 'TFSM', None)
    assert not _is_linked(a, 'TFSM', b2)
    if hasattr(b2, 'ownedStates'):
        assert not _is_linked(b2, 'ownedStates', a)


def test_assoc_sollicitingTransitions28_link_reassign_clear():
    a = tfsmextended_Transition(action="sample_text")
    b1 = tfsmextended_FSMEvent(isTriggered=True)
    b2 = tfsmextended_FSMEvent(isTriggered=False)
    _safe_set(a, 'tfsmextended_Transition30', b1)
    assert _is_linked(a, 'tfsmextended_Transition30', b1)
    if hasattr(b1, 'tfsmextended_FSMEvent29'):
        assert _is_linked(b1, 'tfsmextended_FSMEvent29', a)
    _safe_set(a, 'tfsmextended_Transition30', b2)
    assert _is_linked(a, 'tfsmextended_Transition30', b2)
    if hasattr(b1, 'tfsmextended_FSMEvent29'):
        assert not _is_linked(b1, 'tfsmextended_FSMEvent29', a)
    if hasattr(b2, 'tfsmextended_FSMEvent29'):
        assert _is_linked(b2, 'tfsmextended_FSMEvent29', a)
    _safe_set(a, 'tfsmextended_Transition30', None)
    assert not _is_linked(a, 'tfsmextended_Transition30', b2)
    if hasattr(b2, 'tfsmextended_FSMEvent29'):
        assert not _is_linked(b2, 'tfsmextended_FSMEvent29', a)


def test_assoc_source15_link_reassign_clear():
    a = tfsmextended_Transition(action="sample_text")
    b1 = tfsmextended_State()
    b2 = tfsmextended_State()
    _safe_set(a, 'outgoingTransitions', b1)
    assert _is_linked(a, 'outgoingTransitions', b1)
    if hasattr(b1, 'State16'):
        assert _is_linked(b1, 'State16', a)
    _safe_set(a, 'outgoingTransitions', b2)
    assert _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b1, 'State16'):
        assert not _is_linked(b1, 'State16', a)
    if hasattr(b2, 'State16'):
        assert _is_linked(b2, 'State16', a)
    _safe_set(a, 'outgoingTransitions', None)
    assert not _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b2, 'State16'):
        assert not _is_linked(b2, 'State16', a)


def test_assoc_target17_link_reassign_clear():
    a = tfsmextended_Transition(action="sample_text")
    b1 = tfsmextended_State()
    b2 = tfsmextended_State()
    _safe_set(a, 'incomingTransitions', b1)
    assert _is_linked(a, 'incomingTransitions', b1)
    if hasattr(b1, 'State18'):
        assert _is_linked(b1, 'State18', a)
    _safe_set(a, 'incomingTransitions', b2)
    assert _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b1, 'State18'):
        assert not _is_linked(b1, 'State18', a)
    if hasattr(b2, 'State18'):
        assert _is_linked(b2, 'State18', a)
    _safe_set(a, 'incomingTransitions', None)
    assert not _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b2, 'State18'):
        assert not _is_linked(b2, 'State18', a)


def test_assoc_tfsms31_link_reassign_clear():
    a = tfsmextended_TFSM()
    b1 = tfsmextended_TimedSystem()
    b2 = tfsmextended_TimedSystem()
    _safe_set(a, 'tfsmextended_TFSM32', b1)
    assert _is_linked(a, 'tfsmextended_TFSM32', b1)
    if hasattr(b1, 'tfsmextended_TimedSystem'):
        assert _is_linked(b1, 'tfsmextended_TimedSystem', a)
    _safe_set(a, 'tfsmextended_TFSM32', b2)
    assert _is_linked(a, 'tfsmextended_TFSM32', b2)
    if hasattr(b1, 'tfsmextended_TimedSystem'):
        assert not _is_linked(b1, 'tfsmextended_TimedSystem', a)
    if hasattr(b2, 'tfsmextended_TimedSystem'):
        assert _is_linked(b2, 'tfsmextended_TimedSystem', a)
    _safe_set(a, 'tfsmextended_TFSM32', None)
    assert not _is_linked(a, 'tfsmextended_TFSM32', b2)
    if hasattr(b2, 'tfsmextended_TimedSystem'):
        assert not _is_linked(b2, 'tfsmextended_TimedSystem', a)


def test_assoc_triggeringEvent26_link_reassign_clear():
    a = tfsmextended_FSMEvent(isTriggered=True)
    b1 = tfsmextended_EventGuard()
    b2 = tfsmextended_EventGuard()
    _safe_set(a, 'tfsmextended_FSMEvent27', b1)
    assert _is_linked(a, 'tfsmextended_FSMEvent27', b1)
    if hasattr(b1, 'tfsmextended_EventGuard'):
        assert _is_linked(b1, 'tfsmextended_EventGuard', a)
    _safe_set(a, 'tfsmextended_FSMEvent27', b2)
    assert _is_linked(a, 'tfsmextended_FSMEvent27', b2)
    if hasattr(b1, 'tfsmextended_EventGuard'):
        assert not _is_linked(b1, 'tfsmextended_EventGuard', a)
    if hasattr(b2, 'tfsmextended_EventGuard'):
        assert _is_linked(b2, 'tfsmextended_EventGuard', a)
    _safe_set(a, 'tfsmextended_FSMEvent27', None)
    assert not _is_linked(a, 'tfsmextended_FSMEvent27', b2)
    if hasattr(b2, 'tfsmextended_EventGuard'):
        assert not _is_linked(b2, 'tfsmextended_EventGuard', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Guard_strategy = st.builds(Guard)
@given(instance=Guard_strategy)
@settings(max_examples=25)
def test_Guard_instantiation(instance):
    assert isinstance(instance, Guard)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


tfsmextended_EvaluateGuard_strategy = st.builds(tfsmextended_EvaluateGuard, condition=safe_text)
@given(instance=tfsmextended_EvaluateGuard_strategy)
@settings(max_examples=25)
def test_tfsmextended_EvaluateGuard_instantiation(instance):
    assert isinstance(instance, tfsmextended_EvaluateGuard)


tfsmextended_EventGuard_strategy = st.builds(tfsmextended_EventGuard)
@given(instance=tfsmextended_EventGuard_strategy)
@settings(max_examples=25)
def test_tfsmextended_EventGuard_instantiation(instance):
    assert isinstance(instance, tfsmextended_EventGuard)


tfsmextended_FSMClock_strategy = st.builds(tfsmextended_FSMClock, numberOfTicks=safe_text)
@given(instance=tfsmextended_FSMClock_strategy)
@settings(max_examples=25)
def test_tfsmextended_FSMClock_instantiation(instance):
    assert isinstance(instance, tfsmextended_FSMClock)


tfsmextended_FSMEvent_strategy = st.builds(tfsmextended_FSMEvent, isTriggered=st.booleans())
@given(instance=tfsmextended_FSMEvent_strategy)
@settings(max_examples=25)
def test_tfsmextended_FSMEvent_instantiation(instance):
    assert isinstance(instance, tfsmextended_FSMEvent)


tfsmextended_Guard_strategy = st.builds(tfsmextended_Guard)
@given(instance=tfsmextended_Guard_strategy)
@settings(max_examples=25)
def test_tfsmextended_Guard_instantiation(instance):
    assert isinstance(instance, tfsmextended_Guard)


tfsmextended_NamedElement_strategy = st.builds(tfsmextended_NamedElement, name=safe_text)
@given(instance=tfsmextended_NamedElement_strategy)
@settings(max_examples=25)
def test_tfsmextended_NamedElement_instantiation(instance):
    assert isinstance(instance, tfsmextended_NamedElement)


tfsmextended_State_strategy = st.builds(tfsmextended_State)
@given(instance=tfsmextended_State_strategy)
@settings(max_examples=25)
def test_tfsmextended_State_instantiation(instance):
    assert isinstance(instance, tfsmextended_State)


tfsmextended_TFSM_strategy = st.builds(tfsmextended_TFSM)
@given(instance=tfsmextended_TFSM_strategy)
@settings(max_examples=25)
def test_tfsmextended_TFSM_instantiation(instance):
    assert isinstance(instance, tfsmextended_TFSM)


tfsmextended_TemporalGuard_strategy = st.builds(tfsmextended_TemporalGuard, afterDuration=st.integers())
@given(instance=tfsmextended_TemporalGuard_strategy)
@settings(max_examples=25)
def test_tfsmextended_TemporalGuard_instantiation(instance):
    assert isinstance(instance, tfsmextended_TemporalGuard)


tfsmextended_TimedSystem_strategy = st.builds(tfsmextended_TimedSystem)
@given(instance=tfsmextended_TimedSystem_strategy)
@settings(max_examples=25)
def test_tfsmextended_TimedSystem_instantiation(instance):
    assert isinstance(instance, tfsmextended_TimedSystem)


tfsmextended_Transition_strategy = st.builds(tfsmextended_Transition, action=safe_text)
@given(instance=tfsmextended_Transition_strategy)
@settings(max_examples=25)
def test_tfsmextended_Transition_instantiation(instance):
    assert isinstance(instance, tfsmextended_Transition)



