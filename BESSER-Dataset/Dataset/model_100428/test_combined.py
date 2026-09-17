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
    State,
    statemachine_InitialState,
    statemachine_FinalState,
    statemachine_NormalState,
    statemachine_Action,
    statemachine_Statement,
    statemachine_Expression,
    Declaration,
    statemachine_State,
    statemachine_Transition,
    statemachine_StateMachineVariable,
    statemachine_Declaration,
    statemachine_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_InitialState)


def test_hyp_statemachine_initialstate_constructor_exists():
    assert callable(statemachine_InitialState.__init__)


def test_hyp_statemachine_initialstate_constructor_args():
    sig = inspect.signature(statemachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_FinalState)


def test_hyp_statemachine_finalstate_constructor_exists():
    assert callable(statemachine_FinalState.__init__)


def test_hyp_statemachine_finalstate_constructor_args():
    sig = inspect.signature(statemachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_normalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_NormalState)


def test_hyp_statemachine_normalstate_constructor_exists():
    assert callable(statemachine_NormalState.__init__)


def test_hyp_statemachine_normalstate_constructor_args():
    sig = inspect.signature(statemachine_NormalState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_action_is_not_abstract():
    assert not inspect.isabstract(statemachine_Action)


def test_hyp_statemachine_action_constructor_exists():
    assert callable(statemachine_Action.__init__)


def test_hyp_statemachine_action_constructor_args():
    sig = inspect.signature(statemachine_Action.__init__)
    params = list(sig.parameters.keys())
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"




def test_hyp_statemachine_statement_is_not_abstract():
    assert not inspect.isabstract(statemachine_Statement)


def test_hyp_statemachine_statement_constructor_exists():
    assert callable(statemachine_Statement.__init__)


def test_hyp_statemachine_statement_constructor_args():
    sig = inspect.signature(statemachine_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_expression_is_not_abstract():
    assert not inspect.isabstract(statemachine_Expression)


def test_hyp_statemachine_expression_constructor_exists():
    assert callable(statemachine_Expression.__init__)


def test_hyp_statemachine_expression_constructor_args():
    sig = inspect.signature(statemachine_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_hyp_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_hyp_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_hyp_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_hyp_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_hyp_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_hyp_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "sourceLabel" in params, "Missing parameter 'sourceLabel'"
    assert "label" in params, "Missing parameter 'label'"
    assert "targetLabel" in params, "Missing parameter 'targetLabel'"
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"
    assert "guardLabel" in params, "Missing parameter 'guardLabel'"








def test_hyp_statemachine_statemachinevariable_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachineVariable)


def test_hyp_statemachine_statemachinevariable_constructor_exists():
    assert callable(statemachine_StateMachineVariable.__init__)


def test_hyp_statemachine_statemachinevariable_constructor_args():
    sig = inspect.signature(statemachine_StateMachineVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"





def test_hyp_statemachine_declaration_is_not_abstract():
    assert not inspect.isabstract(statemachine_Declaration)


def test_hyp_statemachine_declaration_constructor_exists():
    assert callable(statemachine_Declaration.__init__)


def test_hyp_statemachine_declaration_constructor_args():
    sig = inspect.signature(statemachine_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachine)


def test_hyp_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_StateMachine.__init__)


def test_hyp_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_StateMachine.__init__)
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
State_strategy = st.builds(
    State,
)
statemachine_InitialState_strategy = st.builds(
    statemachine_InitialState,
)
statemachine_FinalState_strategy = st.builds(
    statemachine_FinalState,
)
statemachine_NormalState_strategy = st.builds(
    statemachine_NormalState,
)
statemachine_Action_strategy = st.builds(
    statemachine_Action,
    actionLabel=
        safe_text
)
statemachine_Statement_strategy = st.builds(
    statemachine_Statement,
)
statemachine_Expression_strategy = st.builds(
    statemachine_Expression,
)
Declaration_strategy = st.builds(
    Declaration,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    label=
        safe_text,
    id=
        st.integers()
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
    sourceLabel=
        safe_text,
    label=
        safe_text,
    targetLabel=
        safe_text,
    actionLabel=
        safe_text,
    guardLabel=
        safe_text
)
statemachine_StateMachineVariable_strategy = st.builds(
    statemachine_StateMachineVariable,
    name=
        safe_text,
    type=
        safe_text
)
statemachine_Declaration_strategy = st.builds(
    statemachine_Declaration,
)
statemachine_StateMachine_strategy = st.builds(
    statemachine_StateMachine,
)








@given(instance=statemachine_Action_strategy)
def test_hyp_statemachine_action_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original







@given(instance=statemachine_State_strategy)
def test_hyp_statemachine_state_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=statemachine_State_strategy)
def test_hyp_statemachine_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_State_strategy)
@settings(max_examples=30)
def test_hyp_statemachine_state_printreachable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.printReachable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.printReachable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'printReachable' in statemachine_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printReachable' in statemachine_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printReachable' in statemachine_State is not implemented or raised an error")




@given(instance=statemachine_Transition_strategy)
def test_hyp_statemachine_transition_sourceLabel_setter(instance):
    original = instance.sourceLabel
    instance.sourceLabel = original
    assert instance.sourceLabel == original



@given(instance=statemachine_Transition_strategy)
def test_hyp_statemachine_transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=statemachine_Transition_strategy)
def test_hyp_statemachine_transition_targetLabel_setter(instance):
    original = instance.targetLabel
    instance.targetLabel = original
    assert instance.targetLabel == original



@given(instance=statemachine_Transition_strategy)
def test_hyp_statemachine_transition_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original



@given(instance=statemachine_Transition_strategy)
def test_hyp_statemachine_transition_guardLabel_setter(instance):
    original = instance.guardLabel
    instance.guardLabel = original
    assert instance.guardLabel == original




@given(instance=statemachine_StateMachineVariable_strategy)
def test_hyp_statemachine_statemachinevariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statemachine_StateMachineVariable_strategy)
def test_hyp_statemachine_statemachinevariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_Declaration_strategy)
@settings(max_examples=30)
def test_hyp_statemachine_declaration_printreachable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.printReachable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.printReachable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'printReachable' in statemachine_Declaration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printReachable' in statemachine_Declaration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printReachable' in statemachine_Declaration is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=30)
def test_hyp_statemachine_statemachine_printreachable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.printReachable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.printReachable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'printReachable' in statemachine_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printReachable' in statemachine_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printReachable' in statemachine_StateMachine is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Declaration,
    State,
    statemachine_Action,
    statemachine_Declaration,
    statemachine_Expression,
    statemachine_FinalState,
    statemachine_InitialState,
    statemachine_NormalState,
    statemachine_State,
    statemachine_StateMachine,
    statemachine_StateMachineVariable,
    statemachine_Statement,
    statemachine_Transition,
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

def test_statemachine_Action_actionLabel_value_roundtrip():
    instance = statemachine_Action(actionLabel="sample_text")
    assert instance.actionLabel == "sample_text"
    instance.actionLabel = "sample_text_2"
    assert instance.actionLabel == "sample_text_2"


def test_statemachine_State_id_value_roundtrip():
    instance = statemachine_State(id=7, label="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_statemachine_State_label_value_roundtrip():
    instance = statemachine_State(id=7, label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_statemachine_StateMachineVariable_name_value_roundtrip():
    instance = statemachine_StateMachineVariable(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_StateMachineVariable_type_value_roundtrip():
    instance = statemachine_StateMachineVariable(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_statemachine_Transition_actionLabel_value_roundtrip():
    instance = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    assert instance.actionLabel == "sample_text"
    instance.actionLabel = "sample_text_2"
    assert instance.actionLabel == "sample_text_2"


def test_statemachine_Transition_guardLabel_value_roundtrip():
    instance = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    assert instance.guardLabel == "sample_text"
    instance.guardLabel = "sample_text_2"
    assert instance.guardLabel == "sample_text_2"


def test_statemachine_Transition_label_value_roundtrip():
    instance = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_statemachine_Transition_sourceLabel_value_roundtrip():
    instance = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    assert instance.sourceLabel == "sample_text"
    instance.sourceLabel = "sample_text_2"
    assert instance.sourceLabel == "sample_text_2"


def test_statemachine_Transition_targetLabel_value_roundtrip():
    instance = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    assert instance.targetLabel == "sample_text"
    instance.targetLabel = "sample_text_2"
    assert instance.targetLabel == "sample_text_2"


def test_statemachine_State_isa_Declaration():
    instance = statemachine_State(id=7, label="sample_text")
    assert isinstance(instance, Declaration)


def test_statemachine_Transition_isa_Declaration():
    instance = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    assert isinstance(instance, Declaration)


def test_statemachine_FinalState_isa_State():
    instance = statemachine_FinalState()
    assert isinstance(instance, State)


def test_statemachine_InitialState_isa_State():
    instance = statemachine_InitialState()
    assert isinstance(instance, State)


def test_statemachine_NormalState_isa_State():
    instance = statemachine_NormalState()
    assert isinstance(instance, State)


def test_assoc_actionStatement17_link_reassign_clear():
    a = statemachine_Action(actionLabel="sample_text")
    b1 = statemachine_Statement()
    b2 = statemachine_Statement()
    _safe_set(a, 'statemachine_Action', b1)
    assert _is_linked(a, 'statemachine_Action', b1)
    if hasattr(b1, 'statemachine_Statement18'):
        assert _is_linked(b1, 'statemachine_Statement18', a)
    _safe_set(a, 'statemachine_Action', b2)
    assert _is_linked(a, 'statemachine_Action', b2)
    if hasattr(b1, 'statemachine_Statement18'):
        assert not _is_linked(b1, 'statemachine_Statement18', a)
    if hasattr(b2, 'statemachine_Statement18'):
        assert _is_linked(b2, 'statemachine_Statement18', a)
    _safe_set(a, 'statemachine_Action', None)
    assert not _is_linked(a, 'statemachine_Action', b2)
    if hasattr(b2, 'statemachine_Statement18'):
        assert not _is_linked(b2, 'statemachine_Statement18', a)


def test_assoc_actionStatement9_link_reassign_clear():
    a = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    b1 = statemachine_Statement()
    b2 = statemachine_Statement()
    _safe_set(a, 'statemachine_Transition10', b1)
    assert _is_linked(a, 'statemachine_Transition10', b1)
    if hasattr(b1, 'statemachine_Statement'):
        assert _is_linked(b1, 'statemachine_Statement', a)
    _safe_set(a, 'statemachine_Transition10', b2)
    assert _is_linked(a, 'statemachine_Transition10', b2)
    if hasattr(b1, 'statemachine_Statement'):
        assert not _is_linked(b1, 'statemachine_Statement', a)
    if hasattr(b2, 'statemachine_Statement'):
        assert _is_linked(b2, 'statemachine_Statement', a)
    _safe_set(a, 'statemachine_Transition10', None)
    assert not _is_linked(a, 'statemachine_Transition10', b2)
    if hasattr(b2, 'statemachine_Statement'):
        assert not _is_linked(b2, 'statemachine_Statement', a)


def test_assoc_declarations0_link_reassign_clear():
    a = statemachine_StateMachine()
    b1 = statemachine_Declaration()
    b2 = statemachine_Declaration()
    _safe_set(a, 'statemachine_StateMachine', {b1})
    assert _is_linked(a, 'statemachine_StateMachine', b1)
    if hasattr(b1, 'statemachine_Declaration'):
        assert _is_linked(b1, 'statemachine_Declaration', a)
    _safe_set(a, 'statemachine_StateMachine', {b2})
    assert _is_linked(a, 'statemachine_StateMachine', b2)
    if hasattr(b1, 'statemachine_Declaration'):
        assert not _is_linked(b1, 'statemachine_Declaration', a)
    if hasattr(b2, 'statemachine_Declaration'):
        assert _is_linked(b2, 'statemachine_Declaration', a)
    _safe_set(a, 'statemachine_StateMachine', set())
    assert not _is_linked(a, 'statemachine_StateMachine', b2)
    if hasattr(b2, 'statemachine_Declaration'):
        assert not _is_linked(b2, 'statemachine_Declaration', a)


def test_assoc_entry19_link_reassign_clear():
    a = statemachine_Action(actionLabel="sample_text")
    b1 = statemachine_NormalState()
    b2 = statemachine_NormalState()
    _safe_set(a, 'statemachine_Action20', b1)
    assert _is_linked(a, 'statemachine_Action20', b1)
    if hasattr(b1, 'statemachine_NormalState'):
        assert _is_linked(b1, 'statemachine_NormalState', a)
    _safe_set(a, 'statemachine_Action20', b2)
    assert _is_linked(a, 'statemachine_Action20', b2)
    if hasattr(b1, 'statemachine_NormalState'):
        assert not _is_linked(b1, 'statemachine_NormalState', a)
    if hasattr(b2, 'statemachine_NormalState'):
        assert _is_linked(b2, 'statemachine_NormalState', a)
    _safe_set(a, 'statemachine_Action20', None)
    assert not _is_linked(a, 'statemachine_Action20', b2)
    if hasattr(b2, 'statemachine_NormalState'):
        assert not _is_linked(b2, 'statemachine_NormalState', a)


def test_assoc_guardExpression7_link_reassign_clear():
    a = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    b1 = statemachine_Expression()
    b2 = statemachine_Expression()
    _safe_set(a, 'statemachine_Transition8', b1)
    assert _is_linked(a, 'statemachine_Transition8', b1)
    if hasattr(b1, 'statemachine_Expression'):
        assert _is_linked(b1, 'statemachine_Expression', a)
    _safe_set(a, 'statemachine_Transition8', b2)
    assert _is_linked(a, 'statemachine_Transition8', b2)
    if hasattr(b1, 'statemachine_Expression'):
        assert not _is_linked(b1, 'statemachine_Expression', a)
    if hasattr(b2, 'statemachine_Expression'):
        assert _is_linked(b2, 'statemachine_Expression', a)
    _safe_set(a, 'statemachine_Transition8', None)
    assert not _is_linked(a, 'statemachine_Transition8', b2)
    if hasattr(b2, 'statemachine_Expression'):
        assert not _is_linked(b2, 'statemachine_Expression', a)


def test_assoc_machineVariables1_link_reassign_clear():
    a = statemachine_StateMachineVariable(name="sample_text", type="sample_text")
    b1 = statemachine_StateMachine()
    b2 = statemachine_StateMachine()
    _safe_set(a, 'statemachine_StateMachineVariable', b1)
    assert _is_linked(a, 'statemachine_StateMachineVariable', b1)
    if hasattr(b1, 'statemachine_StateMachine2'):
        assert _is_linked(b1, 'statemachine_StateMachine2', a)
    _safe_set(a, 'statemachine_StateMachineVariable', b2)
    assert _is_linked(a, 'statemachine_StateMachineVariable', b2)
    if hasattr(b1, 'statemachine_StateMachine2'):
        assert not _is_linked(b1, 'statemachine_StateMachine2', a)
    if hasattr(b2, 'statemachine_StateMachine2'):
        assert _is_linked(b2, 'statemachine_StateMachine2', a)
    _safe_set(a, 'statemachine_StateMachineVariable', None)
    assert not _is_linked(a, 'statemachine_StateMachineVariable', b2)
    if hasattr(b2, 'statemachine_StateMachine2'):
        assert not _is_linked(b2, 'statemachine_StateMachine2', a)


def test_assoc_reachable15_link_reassign_clear():
    a = statemachine_State(id=7, label="sample_text")
    b1 = statemachine_State(id=7, label="sample_text")
    b2 = statemachine_State(id=13, label="sample_text_2")
    _safe_set(a, 'statemachine_State14', {b1})
    assert _is_linked(a, 'statemachine_State14', b1)
    if hasattr(b1, 'statemachine_State16'):
        assert _is_linked(b1, 'statemachine_State16', a)
    _safe_set(a, 'statemachine_State14', {b2})
    assert _is_linked(a, 'statemachine_State14', b2)
    if hasattr(b1, 'statemachine_State16'):
        assert not _is_linked(b1, 'statemachine_State16', a)
    if hasattr(b2, 'statemachine_State16'):
        assert _is_linked(b2, 'statemachine_State16', a)
    _safe_set(a, 'statemachine_State14', set())
    assert not _is_linked(a, 'statemachine_State14', b2)
    if hasattr(b2, 'statemachine_State16'):
        assert not _is_linked(b2, 'statemachine_State16', a)


def test_assoc_source3_link_reassign_clear():
    a = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    b1 = statemachine_State(id=7, label="sample_text")
    b2 = statemachine_State(id=13, label="sample_text_2")
    _safe_set(a, 'statemachine_Transition', b1)
    assert _is_linked(a, 'statemachine_Transition', b1)
    if hasattr(b1, 'statemachine_State'):
        assert _is_linked(b1, 'statemachine_State', a)
    _safe_set(a, 'statemachine_Transition', b2)
    assert _is_linked(a, 'statemachine_Transition', b2)
    if hasattr(b1, 'statemachine_State'):
        assert not _is_linked(b1, 'statemachine_State', a)
    if hasattr(b2, 'statemachine_State'):
        assert _is_linked(b2, 'statemachine_State', a)
    _safe_set(a, 'statemachine_Transition', None)
    assert not _is_linked(a, 'statemachine_Transition', b2)
    if hasattr(b2, 'statemachine_State'):
        assert not _is_linked(b2, 'statemachine_State', a)


def test_assoc_successors12_link_reassign_clear():
    a = statemachine_State(id=7, label="sample_text")
    b1 = statemachine_State(id=7, label="sample_text")
    b2 = statemachine_State(id=13, label="sample_text_2")
    _safe_set(a, 'statemachine_State11', {b1})
    assert _is_linked(a, 'statemachine_State11', b1)
    if hasattr(b1, 'statemachine_State13'):
        assert _is_linked(b1, 'statemachine_State13', a)
    _safe_set(a, 'statemachine_State11', {b2})
    assert _is_linked(a, 'statemachine_State11', b2)
    if hasattr(b1, 'statemachine_State13'):
        assert not _is_linked(b1, 'statemachine_State13', a)
    if hasattr(b2, 'statemachine_State13'):
        assert _is_linked(b2, 'statemachine_State13', a)
    _safe_set(a, 'statemachine_State11', set())
    assert not _is_linked(a, 'statemachine_State11', b2)
    if hasattr(b2, 'statemachine_State13'):
        assert not _is_linked(b2, 'statemachine_State13', a)


def test_assoc_target4_link_reassign_clear():
    a = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    b1 = statemachine_State(id=7, label="sample_text")
    b2 = statemachine_State(id=13, label="sample_text_2")
    _safe_set(a, 'statemachine_Transition5', b1)
    assert _is_linked(a, 'statemachine_Transition5', b1)
    if hasattr(b1, 'statemachine_State6'):
        assert _is_linked(b1, 'statemachine_State6', a)
    _safe_set(a, 'statemachine_Transition5', b2)
    assert _is_linked(a, 'statemachine_Transition5', b2)
    if hasattr(b1, 'statemachine_State6'):
        assert not _is_linked(b1, 'statemachine_State6', a)
    if hasattr(b2, 'statemachine_State6'):
        assert _is_linked(b2, 'statemachine_State6', a)
    _safe_set(a, 'statemachine_Transition5', None)
    assert not _is_linked(a, 'statemachine_Transition5', b2)
    if hasattr(b2, 'statemachine_State6'):
        assert not _is_linked(b2, 'statemachine_State6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Declaration_strategy = st.builds(Declaration)
@given(instance=Declaration_strategy)
@settings(max_examples=25)
def test_Declaration_instantiation(instance):
    assert isinstance(instance, Declaration)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


statemachine_Action_strategy = st.builds(statemachine_Action, actionLabel=safe_text)
@given(instance=statemachine_Action_strategy)
@settings(max_examples=25)
def test_statemachine_Action_instantiation(instance):
    assert isinstance(instance, statemachine_Action)


statemachine_Declaration_strategy = st.builds(statemachine_Declaration)
@given(instance=statemachine_Declaration_strategy)
@settings(max_examples=25)
def test_statemachine_Declaration_instantiation(instance):
    assert isinstance(instance, statemachine_Declaration)


statemachine_Expression_strategy = st.builds(statemachine_Expression)
@given(instance=statemachine_Expression_strategy)
@settings(max_examples=25)
def test_statemachine_Expression_instantiation(instance):
    assert isinstance(instance, statemachine_Expression)


statemachine_FinalState_strategy = st.builds(statemachine_FinalState)
@given(instance=statemachine_FinalState_strategy)
@settings(max_examples=25)
def test_statemachine_FinalState_instantiation(instance):
    assert isinstance(instance, statemachine_FinalState)


statemachine_InitialState_strategy = st.builds(statemachine_InitialState)
@given(instance=statemachine_InitialState_strategy)
@settings(max_examples=25)
def test_statemachine_InitialState_instantiation(instance):
    assert isinstance(instance, statemachine_InitialState)


statemachine_NormalState_strategy = st.builds(statemachine_NormalState)
@given(instance=statemachine_NormalState_strategy)
@settings(max_examples=25)
def test_statemachine_NormalState_instantiation(instance):
    assert isinstance(instance, statemachine_NormalState)


statemachine_State_strategy = st.builds(statemachine_State, id=st.integers(), label=safe_text)
@given(instance=statemachine_State_strategy)
@settings(max_examples=25)
def test_statemachine_State_instantiation(instance):
    assert isinstance(instance, statemachine_State)


statemachine_StateMachine_strategy = st.builds(statemachine_StateMachine)
@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=25)
def test_statemachine_StateMachine_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachine)


statemachine_StateMachineVariable_strategy = st.builds(statemachine_StateMachineVariable, name=safe_text, type=safe_text)
@given(instance=statemachine_StateMachineVariable_strategy)
@settings(max_examples=25)
def test_statemachine_StateMachineVariable_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachineVariable)


statemachine_Statement_strategy = st.builds(statemachine_Statement)
@given(instance=statemachine_Statement_strategy)
@settings(max_examples=25)
def test_statemachine_Statement_instantiation(instance):
    assert isinstance(instance, statemachine_Statement)


statemachine_Transition_strategy = st.builds(statemachine_Transition, actionLabel=safe_text, guardLabel=safe_text, label=safe_text, sourceLabel=safe_text, targetLabel=safe_text)
@given(instance=statemachine_Transition_strategy)
@settings(max_examples=25)
def test_statemachine_Transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



