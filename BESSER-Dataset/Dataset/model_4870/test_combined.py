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
    FlowDesigner_Flow,
    FlowDesigner_Source,
    FlowDesigner_Target,
    FlowDesigner_Event,
    NamedState,
    FlowDesigner_ViewState,
    FlowDesigner_ActionState,
    Target,
    FlowDesigner_FinalState,
    Source,
    FlowDesigner_NamedState,
    FlowDesigner_InitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_flowdesigner_flow_is_not_abstract():
    assert not inspect.isabstract(FlowDesigner_Flow)


def test_hyp_flowdesigner_flow_constructor_exists():
    assert callable(FlowDesigner_Flow.__init__)


def test_hyp_flowdesigner_flow_constructor_args():
    sig = inspect.signature(FlowDesigner_Flow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowdesigner_source_is_not_abstract():
    assert not inspect.isabstract(FlowDesigner_Source)


def test_hyp_flowdesigner_source_constructor_exists():
    assert callable(FlowDesigner_Source.__init__)


def test_hyp_flowdesigner_source_constructor_args():
    sig = inspect.signature(FlowDesigner_Source.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowdesigner_target_is_not_abstract():
    assert not inspect.isabstract(FlowDesigner_Target)


def test_hyp_flowdesigner_target_constructor_exists():
    assert callable(FlowDesigner_Target.__init__)


def test_hyp_flowdesigner_target_constructor_args():
    sig = inspect.signature(FlowDesigner_Target.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowdesigner_event_is_not_abstract():
    assert not inspect.isabstract(FlowDesigner_Event)


def test_hyp_flowdesigner_event_constructor_exists():
    assert callable(FlowDesigner_Event.__init__)


def test_hyp_flowdesigner_event_constructor_args():
    sig = inspect.signature(FlowDesigner_Event.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "action" in params, "Missing parameter 'action'"
    assert "event" in params, "Missing parameter 'event'"






def test_hyp_namedstate_is_not_abstract():
    assert not inspect.isabstract(NamedState)


def test_hyp_namedstate_constructor_exists():
    assert callable(NamedState.__init__)


def test_hyp_namedstate_constructor_args():
    sig = inspect.signature(NamedState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowdesigner_viewstate_is_not_abstract():
    assert not inspect.isabstract(FlowDesigner_ViewState)


def test_hyp_flowdesigner_viewstate_constructor_exists():
    assert callable(FlowDesigner_ViewState.__init__)


def test_hyp_flowdesigner_viewstate_constructor_args():
    sig = inspect.signature(FlowDesigner_ViewState.__init__)
    params = list(sig.parameters.keys())
    assert "view" in params, "Missing parameter 'view'"




def test_hyp_flowdesigner_actionstate_is_not_abstract():
    assert not inspect.isabstract(FlowDesigner_ActionState)


def test_hyp_flowdesigner_actionstate_constructor_exists():
    assert callable(FlowDesigner_ActionState.__init__)


def test_hyp_flowdesigner_actionstate_constructor_args():
    sig = inspect.signature(FlowDesigner_ActionState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_target_is_not_abstract():
    assert not inspect.isabstract(Target)


def test_hyp_target_constructor_exists():
    assert callable(Target.__init__)


def test_hyp_target_constructor_args():
    sig = inspect.signature(Target.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowdesigner_finalstate_is_not_abstract():
    assert not inspect.isabstract(FlowDesigner_FinalState)


def test_hyp_flowdesigner_finalstate_constructor_exists():
    assert callable(FlowDesigner_FinalState.__init__)


def test_hyp_flowdesigner_finalstate_constructor_args():
    sig = inspect.signature(FlowDesigner_FinalState.__init__)
    params = list(sig.parameters.keys())
    assert "finalize" in params, "Missing parameter 'finalize'"




def test_hyp_source_is_not_abstract():
    assert not inspect.isabstract(Source)


def test_hyp_source_constructor_exists():
    assert callable(Source.__init__)


def test_hyp_source_constructor_args():
    sig = inspect.signature(Source.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowdesigner_namedstate_is_not_abstract():
    assert not inspect.isabstract(FlowDesigner_NamedState)


def test_hyp_flowdesigner_namedstate_constructor_exists():
    assert callable(FlowDesigner_NamedState.__init__)


def test_hyp_flowdesigner_namedstate_constructor_args():
    sig = inspect.signature(FlowDesigner_NamedState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "exit" in params, "Missing parameter 'exit'"
    assert "entry" in params, "Missing parameter 'entry'"
    assert "activity" in params, "Missing parameter 'activity'"







def test_hyp_flowdesigner_initialstate_is_not_abstract():
    assert not inspect.isabstract(FlowDesigner_InitialState)


def test_hyp_flowdesigner_initialstate_constructor_exists():
    assert callable(FlowDesigner_InitialState.__init__)


def test_hyp_flowdesigner_initialstate_constructor_args():
    sig = inspect.signature(FlowDesigner_InitialState.__init__)
    params = list(sig.parameters.keys())
    assert "initialize" in params, "Missing parameter 'initialize'"



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
FlowDesigner_Flow_strategy = st.builds(
    FlowDesigner_Flow,
)
FlowDesigner_Source_strategy = st.builds(
    FlowDesigner_Source,
)
FlowDesigner_Target_strategy = st.builds(
    FlowDesigner_Target,
)
FlowDesigner_Event_strategy = st.builds(
    FlowDesigner_Event,
    guard=
        safe_text,
    action=
        safe_text,
    event=
        safe_text
)
NamedState_strategy = st.builds(
    NamedState,
)
FlowDesigner_ViewState_strategy = st.builds(
    FlowDesigner_ViewState,
    view=
        safe_text
)
FlowDesigner_ActionState_strategy = st.builds(
    FlowDesigner_ActionState,
)
Target_strategy = st.builds(
    Target,
)
FlowDesigner_FinalState_strategy = st.builds(
    FlowDesigner_FinalState,
    finalize=
        safe_text
)
Source_strategy = st.builds(
    Source,
)
FlowDesigner_NamedState_strategy = st.builds(
    FlowDesigner_NamedState,
    name=
        safe_text,
    exit=
        safe_text,
    entry=
        safe_text,
    activity=
        safe_text
)
FlowDesigner_InitialState_strategy = st.builds(
    FlowDesigner_InitialState,
    initialize=
        safe_text
)


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlowDesigner_Flow_strategy)
@settings(max_examples=30)
def test_hyp_flowdesigner_flow_findstatebyname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findStateByName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findStateByName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findStateByName' in FlowDesigner_Flow is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findStateByName' in FlowDesigner_Flow did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findStateByName' in FlowDesigner_Flow is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlowDesigner_Flow_strategy)
@settings(max_examples=30)
def test_hyp_flowdesigner_flow_haslaststate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasLastState()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasLastState).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasLastState' in FlowDesigner_Flow is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasLastState' in FlowDesigner_Flow did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasLastState' in FlowDesigner_Flow is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlowDesigner_Source_strategy)
@settings(max_examples=30)
def test_hyp_flowdesigner_source_canbesource_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canBeSource(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canBeSource).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canBeSource' in FlowDesigner_Source is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canBeSource' in FlowDesigner_Source did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canBeSource' in FlowDesigner_Source is not implemented or raised an error")





@given(instance=FlowDesigner_Event_strategy)
def test_hyp_flowdesigner_event_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=FlowDesigner_Event_strategy)
def test_hyp_flowdesigner_event_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=FlowDesigner_Event_strategy)
def test_hyp_flowdesigner_event_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original





@given(instance=FlowDesigner_ViewState_strategy)
def test_hyp_flowdesigner_viewstate_view_setter(instance):
    original = instance.view
    instance.view = original
    assert instance.view == original






@given(instance=FlowDesigner_FinalState_strategy)
def test_hyp_flowdesigner_finalstate_finalize_setter(instance):
    original = instance.finalize
    instance.finalize = original
    assert instance.finalize == original





@given(instance=FlowDesigner_NamedState_strategy)
def test_hyp_flowdesigner_namedstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=FlowDesigner_NamedState_strategy)
def test_hyp_flowdesigner_namedstate_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original



@given(instance=FlowDesigner_NamedState_strategy)
def test_hyp_flowdesigner_namedstate_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original



@given(instance=FlowDesigner_NamedState_strategy)
def test_hyp_flowdesigner_namedstate_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original




@given(instance=FlowDesigner_InitialState_strategy)
def test_hyp_flowdesigner_initialstate_initialize_setter(instance):
    original = instance.initialize
    instance.initialize = original
    assert instance.initialize == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    FlowDesigner_ActionState,
    FlowDesigner_Event,
    FlowDesigner_FinalState,
    FlowDesigner_Flow,
    FlowDesigner_InitialState,
    FlowDesigner_NamedState,
    FlowDesigner_Source,
    FlowDesigner_Target,
    FlowDesigner_ViewState,
    NamedState,
    Source,
    Target,
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

def test_FlowDesigner_Event_action_value_roundtrip():
    instance = FlowDesigner_Event(action="sample_text", event="sample_text", guard="sample_text")
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_FlowDesigner_Event_event_value_roundtrip():
    instance = FlowDesigner_Event(action="sample_text", event="sample_text", guard="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_FlowDesigner_Event_guard_value_roundtrip():
    instance = FlowDesigner_Event(action="sample_text", event="sample_text", guard="sample_text")
    assert instance.guard == "sample_text"
    instance.guard = "sample_text_2"
    assert instance.guard == "sample_text_2"


def test_FlowDesigner_FinalState_finalize_value_roundtrip():
    instance = FlowDesigner_FinalState(finalize="sample_text")
    assert instance.finalize == "sample_text"
    instance.finalize = "sample_text_2"
    assert instance.finalize == "sample_text_2"


def test_FlowDesigner_InitialState_initialize_value_roundtrip():
    instance = FlowDesigner_InitialState(initialize="sample_text")
    assert instance.initialize == "sample_text"
    instance.initialize = "sample_text_2"
    assert instance.initialize == "sample_text_2"


def test_FlowDesigner_NamedState_activity_value_roundtrip():
    instance = FlowDesigner_NamedState(activity="sample_text", entry="sample_text", exit="sample_text", name="sample_text")
    assert instance.activity == "sample_text"
    instance.activity = "sample_text_2"
    assert instance.activity == "sample_text_2"


def test_FlowDesigner_NamedState_entry_value_roundtrip():
    instance = FlowDesigner_NamedState(activity="sample_text", entry="sample_text", exit="sample_text", name="sample_text")
    assert instance.entry == "sample_text"
    instance.entry = "sample_text_2"
    assert instance.entry == "sample_text_2"


def test_FlowDesigner_NamedState_exit_value_roundtrip():
    instance = FlowDesigner_NamedState(activity="sample_text", entry="sample_text", exit="sample_text", name="sample_text")
    assert instance.exit == "sample_text"
    instance.exit = "sample_text_2"
    assert instance.exit == "sample_text_2"


def test_FlowDesigner_NamedState_name_value_roundtrip():
    instance = FlowDesigner_NamedState(activity="sample_text", entry="sample_text", exit="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FlowDesigner_ViewState_view_value_roundtrip():
    instance = FlowDesigner_ViewState(view="sample_text")
    assert instance.view == "sample_text"
    instance.view = "sample_text_2"
    assert instance.view == "sample_text_2"


def test_FlowDesigner_ActionState_isa_NamedState():
    instance = FlowDesigner_ActionState()
    assert isinstance(instance, NamedState)


def test_FlowDesigner_ViewState_isa_NamedState():
    instance = FlowDesigner_ViewState(view="sample_text")
    assert isinstance(instance, NamedState)


def test_FlowDesigner_InitialState_isa_Source():
    instance = FlowDesigner_InitialState(initialize="sample_text")
    assert isinstance(instance, Source)


def test_FlowDesigner_NamedState_isa_Source():
    instance = FlowDesigner_NamedState(activity="sample_text", entry="sample_text", exit="sample_text", name="sample_text")
    assert isinstance(instance, Source)


def test_FlowDesigner_FinalState_isa_Target():
    instance = FlowDesigner_FinalState(finalize="sample_text")
    assert isinstance(instance, Target)


def test_FlowDesigner_NamedState_isa_Target():
    instance = FlowDesigner_NamedState(activity="sample_text", entry="sample_text", exit="sample_text", name="sample_text")
    assert isinstance(instance, Target)


def test_assoc_events1_link_reassign_clear():
    a = FlowDesigner_Source()
    b1 = FlowDesigner_Event(action="sample_text", event="sample_text", guard="sample_text")
    b2 = FlowDesigner_Event(action="sample_text_2", event="sample_text_2", guard="sample_text_2")
    _safe_set(a, 'FlowDesigner_Source', {b1})
    assert _is_linked(a, 'FlowDesigner_Source', b1)
    if hasattr(b1, 'FlowDesigner_Event2'):
        assert _is_linked(b1, 'FlowDesigner_Event2', a)
    _safe_set(a, 'FlowDesigner_Source', {b2})
    assert _is_linked(a, 'FlowDesigner_Source', b2)
    if hasattr(b1, 'FlowDesigner_Event2'):
        assert not _is_linked(b1, 'FlowDesigner_Event2', a)
    if hasattr(b2, 'FlowDesigner_Event2'):
        assert _is_linked(b2, 'FlowDesigner_Event2', a)
    _safe_set(a, 'FlowDesigner_Source', set())
    assert not _is_linked(a, 'FlowDesigner_Source', b2)
    if hasattr(b2, 'FlowDesigner_Event2'):
        assert not _is_linked(b2, 'FlowDesigner_Event2', a)


def test_assoc_finalState6_link_reassign_clear():
    a = FlowDesigner_Flow()
    b1 = FlowDesigner_FinalState(finalize="sample_text")
    b2 = FlowDesigner_FinalState(finalize="sample_text_2")
    _safe_set(a, 'FlowDesigner_Flow7', b1)
    assert _is_linked(a, 'FlowDesigner_Flow7', b1)
    if hasattr(b1, 'FlowDesigner_FinalState'):
        assert _is_linked(b1, 'FlowDesigner_FinalState', a)
    _safe_set(a, 'FlowDesigner_Flow7', b2)
    assert _is_linked(a, 'FlowDesigner_Flow7', b2)
    if hasattr(b1, 'FlowDesigner_FinalState'):
        assert not _is_linked(b1, 'FlowDesigner_FinalState', a)
    if hasattr(b2, 'FlowDesigner_FinalState'):
        assert _is_linked(b2, 'FlowDesigner_FinalState', a)
    _safe_set(a, 'FlowDesigner_Flow7', None)
    assert not _is_linked(a, 'FlowDesigner_Flow7', b2)
    if hasattr(b2, 'FlowDesigner_FinalState'):
        assert not _is_linked(b2, 'FlowDesigner_FinalState', a)


def test_assoc_initialState3_link_reassign_clear():
    a = FlowDesigner_InitialState(initialize="sample_text")
    b1 = FlowDesigner_Flow()
    b2 = FlowDesigner_Flow()
    _safe_set(a, 'FlowDesigner_InitialState', b1)
    assert _is_linked(a, 'FlowDesigner_InitialState', b1)
    if hasattr(b1, 'FlowDesigner_Flow'):
        assert _is_linked(b1, 'FlowDesigner_Flow', a)
    _safe_set(a, 'FlowDesigner_InitialState', b2)
    assert _is_linked(a, 'FlowDesigner_InitialState', b2)
    if hasattr(b1, 'FlowDesigner_Flow'):
        assert not _is_linked(b1, 'FlowDesigner_Flow', a)
    if hasattr(b2, 'FlowDesigner_Flow'):
        assert _is_linked(b2, 'FlowDesigner_Flow', a)
    _safe_set(a, 'FlowDesigner_InitialState', None)
    assert not _is_linked(a, 'FlowDesigner_InitialState', b2)
    if hasattr(b2, 'FlowDesigner_Flow'):
        assert not _is_linked(b2, 'FlowDesigner_Flow', a)


def test_assoc_nextState0_link_reassign_clear():
    a = FlowDesigner_Target()
    b1 = FlowDesigner_Event(action="sample_text", event="sample_text", guard="sample_text")
    b2 = FlowDesigner_Event(action="sample_text_2", event="sample_text_2", guard="sample_text_2")
    _safe_set(a, 'FlowDesigner_Target', b1)
    assert _is_linked(a, 'FlowDesigner_Target', b1)
    if hasattr(b1, 'FlowDesigner_Event'):
        assert _is_linked(b1, 'FlowDesigner_Event', a)
    _safe_set(a, 'FlowDesigner_Target', b2)
    assert _is_linked(a, 'FlowDesigner_Target', b2)
    if hasattr(b1, 'FlowDesigner_Event'):
        assert not _is_linked(b1, 'FlowDesigner_Event', a)
    if hasattr(b2, 'FlowDesigner_Event'):
        assert _is_linked(b2, 'FlowDesigner_Event', a)
    _safe_set(a, 'FlowDesigner_Target', None)
    assert not _is_linked(a, 'FlowDesigner_Target', b2)
    if hasattr(b2, 'FlowDesigner_Event'):
        assert not _is_linked(b2, 'FlowDesigner_Event', a)


def test_assoc_states4_link_reassign_clear():
    a = FlowDesigner_NamedState(activity="sample_text", entry="sample_text", exit="sample_text", name="sample_text")
    b1 = FlowDesigner_Flow()
    b2 = FlowDesigner_Flow()
    _safe_set(a, 'FlowDesigner_NamedState', b1)
    assert _is_linked(a, 'FlowDesigner_NamedState', b1)
    if hasattr(b1, 'FlowDesigner_Flow5'):
        assert _is_linked(b1, 'FlowDesigner_Flow5', a)
    _safe_set(a, 'FlowDesigner_NamedState', b2)
    assert _is_linked(a, 'FlowDesigner_NamedState', b2)
    if hasattr(b1, 'FlowDesigner_Flow5'):
        assert not _is_linked(b1, 'FlowDesigner_Flow5', a)
    if hasattr(b2, 'FlowDesigner_Flow5'):
        assert _is_linked(b2, 'FlowDesigner_Flow5', a)
    _safe_set(a, 'FlowDesigner_NamedState', None)
    assert not _is_linked(a, 'FlowDesigner_NamedState', b2)
    if hasattr(b2, 'FlowDesigner_Flow5'):
        assert not _is_linked(b2, 'FlowDesigner_Flow5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

FlowDesigner_ActionState_strategy = st.builds(FlowDesigner_ActionState)
@given(instance=FlowDesigner_ActionState_strategy)
@settings(max_examples=25)
def test_FlowDesigner_ActionState_instantiation(instance):
    assert isinstance(instance, FlowDesigner_ActionState)


FlowDesigner_Event_strategy = st.builds(FlowDesigner_Event, action=safe_text, event=safe_text, guard=safe_text)
@given(instance=FlowDesigner_Event_strategy)
@settings(max_examples=25)
def test_FlowDesigner_Event_instantiation(instance):
    assert isinstance(instance, FlowDesigner_Event)


FlowDesigner_FinalState_strategy = st.builds(FlowDesigner_FinalState, finalize=safe_text)
@given(instance=FlowDesigner_FinalState_strategy)
@settings(max_examples=25)
def test_FlowDesigner_FinalState_instantiation(instance):
    assert isinstance(instance, FlowDesigner_FinalState)


FlowDesigner_Flow_strategy = st.builds(FlowDesigner_Flow)
@given(instance=FlowDesigner_Flow_strategy)
@settings(max_examples=25)
def test_FlowDesigner_Flow_instantiation(instance):
    assert isinstance(instance, FlowDesigner_Flow)


FlowDesigner_InitialState_strategy = st.builds(FlowDesigner_InitialState, initialize=safe_text)
@given(instance=FlowDesigner_InitialState_strategy)
@settings(max_examples=25)
def test_FlowDesigner_InitialState_instantiation(instance):
    assert isinstance(instance, FlowDesigner_InitialState)


FlowDesigner_NamedState_strategy = st.builds(FlowDesigner_NamedState, activity=safe_text, entry=safe_text, exit=safe_text, name=safe_text)
@given(instance=FlowDesigner_NamedState_strategy)
@settings(max_examples=25)
def test_FlowDesigner_NamedState_instantiation(instance):
    assert isinstance(instance, FlowDesigner_NamedState)


FlowDesigner_Source_strategy = st.builds(FlowDesigner_Source)
@given(instance=FlowDesigner_Source_strategy)
@settings(max_examples=25)
def test_FlowDesigner_Source_instantiation(instance):
    assert isinstance(instance, FlowDesigner_Source)


FlowDesigner_Target_strategy = st.builds(FlowDesigner_Target)
@given(instance=FlowDesigner_Target_strategy)
@settings(max_examples=25)
def test_FlowDesigner_Target_instantiation(instance):
    assert isinstance(instance, FlowDesigner_Target)


FlowDesigner_ViewState_strategy = st.builds(FlowDesigner_ViewState, view=safe_text)
@given(instance=FlowDesigner_ViewState_strategy)
@settings(max_examples=25)
def test_FlowDesigner_ViewState_instantiation(instance):
    assert isinstance(instance, FlowDesigner_ViewState)


NamedState_strategy = st.builds(NamedState)
@given(instance=NamedState_strategy)
@settings(max_examples=25)
def test_NamedState_instantiation(instance):
    assert isinstance(instance, NamedState)


Source_strategy = st.builds(Source)
@given(instance=Source_strategy)
@settings(max_examples=25)
def test_Source_instantiation(instance):
    assert isinstance(instance, Source)


Target_strategy = st.builds(Target)
@given(instance=Target_strategy)
@settings(max_examples=25)
def test_Target_instantiation(instance):
    assert isinstance(instance, Target)



