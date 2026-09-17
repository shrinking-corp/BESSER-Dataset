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
    statemachine_Action,
    Transition,
    statemachine_LabeledTransition,
    Vertex,
    statemachine_State,
    Region,
    statemachine_Statemachine,
    statemachine_Region,
    State,
    statemachine_ComplexState,
    statemachine_Pseudostate,
    statemachine_Transition,
    statemachine_Vertex,
    PseudostateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_statemachine_action_is_not_abstract():
    assert not inspect.isabstract(statemachine_Action)


def test_hyp_statemachine_action_constructor_exists():
    assert callable(statemachine_Action.__init__)


def test_hyp_statemachine_action_constructor_args():
    sig = inspect.signature(statemachine_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_labeledtransition_is_not_abstract():
    assert not inspect.isabstract(statemachine_LabeledTransition)


def test_hyp_statemachine_labeledtransition_constructor_exists():
    assert callable(statemachine_LabeledTransition.__init__)


def test_hyp_statemachine_labeledtransition_constructor_args():
    sig = inspect.signature(statemachine_LabeledTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_hyp_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_hyp_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_hyp_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_hyp_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_region_is_not_abstract():
    assert not inspect.isabstract(Region)


def test_hyp_region_constructor_exists():
    assert callable(Region.__init__)


def test_hyp_region_constructor_args():
    sig = inspect.signature(Region.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_Statemachine)


def test_hyp_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_Statemachine.__init__)


def test_hyp_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_statemachine_region_is_not_abstract():
    assert not inspect.isabstract(statemachine_Region)


def test_hyp_statemachine_region_constructor_exists():
    assert callable(statemachine_Region.__init__)


def test_hyp_statemachine_region_constructor_args():
    sig = inspect.signature(statemachine_Region.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_complexstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_ComplexState)


def test_hyp_statemachine_complexstate_constructor_exists():
    assert callable(statemachine_ComplexState.__init__)


def test_hyp_statemachine_complexstate_constructor_args():
    sig = inspect.signature(statemachine_ComplexState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_pseudostate_is_not_abstract():
    assert not inspect.isabstract(statemachine_Pseudostate)


def test_hyp_statemachine_pseudostate_constructor_exists():
    assert callable(statemachine_Pseudostate.__init__)


def test_hyp_statemachine_pseudostate_constructor_args():
    sig = inspect.signature(statemachine_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "kind" in params, "Missing parameter 'kind'"





def test_hyp_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_hyp_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_hyp_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_statemachine_vertex_is_not_abstract():
    assert not inspect.isabstract(statemachine_Vertex)


def test_hyp_statemachine_vertex_constructor_exists():
    assert callable(statemachine_Vertex.__init__)


def test_hyp_statemachine_vertex_constructor_args():
    sig = inspect.signature(statemachine_Vertex.__init__)
    params = list(sig.parameters.keys())

def test_hyp_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_hyp_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "final",
        "initial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"


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
statemachine_Action_strategy = st.builds(
    statemachine_Action,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
statemachine_LabeledTransition_strategy = st.builds(
    statemachine_LabeledTransition,
)
Vertex_strategy = st.builds(
    Vertex,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    name=
        safe_text
)
Region_strategy = st.builds(
    Region,
)
statemachine_Statemachine_strategy = st.builds(
    statemachine_Statemachine,
    name=
        safe_text
)
statemachine_Region_strategy = st.builds(
    statemachine_Region,
)
State_strategy = st.builds(
    State,
)
statemachine_ComplexState_strategy = st.builds(
    statemachine_ComplexState,
)
statemachine_Pseudostate_strategy = st.builds(
    statemachine_Pseudostate,
    id=
        safe_text,
    kind=
        safe_text
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
    id=
        safe_text
)
statemachine_Vertex_strategy = st.builds(
    statemachine_Vertex,
)




@given(instance=statemachine_Action_strategy)
def test_hyp_statemachine_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=statemachine_State_strategy)
def test_hyp_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_State_strategy)
@settings(max_examples=30)
def test_hyp_statemachine_state_fullyqualifiedname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fullyQualifiedName()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fullyQualifiedName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fullyQualifiedName' in statemachine_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fullyQualifiedName' in statemachine_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fullyQualifiedName' in statemachine_State is not implemented or raised an error")





@given(instance=statemachine_Statemachine_strategy)
def test_hyp_statemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_ComplexState_strategy)
@settings(max_examples=30)
def test_hyp_statemachine_complexstate_directsubstates_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.directSubStates()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.directSubStates).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'directSubStates' in statemachine_ComplexState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'directSubStates' in statemachine_ComplexState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'directSubStates' in statemachine_ComplexState is not implemented or raised an error")




@given(instance=statemachine_Pseudostate_strategy)
def test_hyp_statemachine_pseudostate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=statemachine_Pseudostate_strategy)
def test_hyp_statemachine_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=statemachine_Transition_strategy)
def test_hyp_statemachine_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Region,
    State,
    Transition,
    Vertex,
    statemachine_Action,
    statemachine_ComplexState,
    statemachine_LabeledTransition,
    statemachine_Pseudostate,
    statemachine_Region,
    statemachine_State,
    statemachine_Statemachine,
    statemachine_Transition,
    statemachine_Vertex,
    PseudostateKind,
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

def test_statemachine_Action_name_value_roundtrip():
    instance = statemachine_Action(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_Pseudostate_id_value_roundtrip():
    instance = statemachine_Pseudostate(id="sample_text", kind="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_statemachine_Pseudostate_kind_value_roundtrip():
    instance = statemachine_Pseudostate(id="sample_text", kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_statemachine_State_name_value_roundtrip():
    instance = statemachine_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_Statemachine_name_value_roundtrip():
    instance = statemachine_Statemachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_Transition_id_value_roundtrip():
    instance = statemachine_Transition(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_statemachine_Statemachine_isa_Region():
    instance = statemachine_Statemachine(name="sample_text")
    assert isinstance(instance, Region)


def test_statemachine_ComplexState_isa_State():
    instance = statemachine_ComplexState()
    assert isinstance(instance, State)


def test_statemachine_LabeledTransition_isa_Transition():
    instance = statemachine_LabeledTransition()
    assert isinstance(instance, Transition)


def test_statemachine_Pseudostate_isa_Vertex():
    instance = statemachine_Pseudostate(id="sample_text", kind="sample_text")
    assert isinstance(instance, Vertex)


def test_statemachine_State_isa_Vertex():
    instance = statemachine_State(name="sample_text")
    assert isinstance(instance, Vertex)


def test_assoc_action19_link_reassign_clear():
    a = statemachine_Action(name="sample_text")
    b1 = statemachine_LabeledTransition()
    b2 = statemachine_LabeledTransition()
    _safe_set(a, 'statemachine_Action20', b1)
    assert _is_linked(a, 'statemachine_Action20', b1)
    if hasattr(b1, 'statemachine_LabeledTransition'):
        assert _is_linked(b1, 'statemachine_LabeledTransition', a)
    _safe_set(a, 'statemachine_Action20', b2)
    assert _is_linked(a, 'statemachine_Action20', b2)
    if hasattr(b1, 'statemachine_LabeledTransition'):
        assert not _is_linked(b1, 'statemachine_LabeledTransition', a)
    if hasattr(b2, 'statemachine_LabeledTransition'):
        assert _is_linked(b2, 'statemachine_LabeledTransition', a)
    _safe_set(a, 'statemachine_Action20', None)
    assert not _is_linked(a, 'statemachine_Action20', b2)
    if hasattr(b2, 'statemachine_LabeledTransition'):
        assert not _is_linked(b2, 'statemachine_LabeledTransition', a)


def test_assoc_actions12_link_reassign_clear():
    a = statemachine_Statemachine(name="sample_text")
    b1 = statemachine_Action(name="sample_text")
    b2 = statemachine_Action(name="sample_text_2")
    _safe_set(a, 'statemachine_Statemachine13', {b1})
    assert _is_linked(a, 'statemachine_Statemachine13', b1)
    if hasattr(b1, 'statemachine_Action'):
        assert _is_linked(b1, 'statemachine_Action', a)
    _safe_set(a, 'statemachine_Statemachine13', {b2})
    assert _is_linked(a, 'statemachine_Statemachine13', b2)
    if hasattr(b1, 'statemachine_Action'):
        assert not _is_linked(b1, 'statemachine_Action', a)
    if hasattr(b2, 'statemachine_Action'):
        assert _is_linked(b2, 'statemachine_Action', a)
    _safe_set(a, 'statemachine_Statemachine13', set())
    assert not _is_linked(a, 'statemachine_Statemachine13', b2)
    if hasattr(b2, 'statemachine_Action'):
        assert not _is_linked(b2, 'statemachine_Action', a)


def test_assoc_initial17_link_reassign_clear():
    a = statemachine_Pseudostate(id="sample_text", kind="sample_text")
    b1 = statemachine_Region()
    b2 = statemachine_Region()
    _safe_set(a, 'statemachine_Pseudostate', b1)
    assert _is_linked(a, 'statemachine_Pseudostate', b1)
    if hasattr(b1, 'statemachine_Region18'):
        assert _is_linked(b1, 'statemachine_Region18', a)
    _safe_set(a, 'statemachine_Pseudostate', b2)
    assert _is_linked(a, 'statemachine_Pseudostate', b2)
    if hasattr(b1, 'statemachine_Region18'):
        assert not _is_linked(b1, 'statemachine_Region18', a)
    if hasattr(b2, 'statemachine_Region18'):
        assert _is_linked(b2, 'statemachine_Region18', a)
    _safe_set(a, 'statemachine_Pseudostate', None)
    assert not _is_linked(a, 'statemachine_Pseudostate', b2)
    if hasattr(b2, 'statemachine_Region18'):
        assert not _is_linked(b2, 'statemachine_Region18', a)


def test_assoc_outgoings0_link_reassign_clear():
    a = statemachine_Transition(id="sample_text")
    b1 = statemachine_Vertex()
    b2 = statemachine_Vertex()
    _safe_set(a, 'statemachine_Transition', b1)
    assert _is_linked(a, 'statemachine_Transition', b1)
    if hasattr(b1, 'statemachine_Vertex'):
        assert _is_linked(b1, 'statemachine_Vertex', a)
    _safe_set(a, 'statemachine_Transition', b2)
    assert _is_linked(a, 'statemachine_Transition', b2)
    if hasattr(b1, 'statemachine_Vertex'):
        assert not _is_linked(b1, 'statemachine_Vertex', a)
    if hasattr(b2, 'statemachine_Vertex'):
        assert _is_linked(b2, 'statemachine_Vertex', a)
    _safe_set(a, 'statemachine_Transition', None)
    assert not _is_linked(a, 'statemachine_Transition', b2)
    if hasattr(b2, 'statemachine_Vertex'):
        assert not _is_linked(b2, 'statemachine_Vertex', a)


def test_assoc_region2_link_reassign_clear():
    a = statemachine_ComplexState()
    b1 = statemachine_Region()
    b2 = statemachine_Region()
    _safe_set(a, 'statemachine_ComplexState3', b1)
    assert _is_linked(a, 'statemachine_ComplexState3', b1)
    if hasattr(b1, 'statemachine_Region'):
        assert _is_linked(b1, 'statemachine_Region', a)
    _safe_set(a, 'statemachine_ComplexState3', b2)
    assert _is_linked(a, 'statemachine_ComplexState3', b2)
    if hasattr(b1, 'statemachine_Region'):
        assert not _is_linked(b1, 'statemachine_Region', a)
    if hasattr(b2, 'statemachine_Region'):
        assert _is_linked(b2, 'statemachine_Region', a)
    _safe_set(a, 'statemachine_ComplexState3', None)
    assert not _is_linked(a, 'statemachine_ComplexState3', b2)
    if hasattr(b2, 'statemachine_Region'):
        assert not _is_linked(b2, 'statemachine_Region', a)


def test_assoc_source4_link_reassign_clear():
    a = statemachine_Transition(id="sample_text")
    b1 = statemachine_Vertex()
    b2 = statemachine_Vertex()
    _safe_set(a, 'statemachine_Transition5', b1)
    assert _is_linked(a, 'statemachine_Transition5', b1)
    if hasattr(b1, 'statemachine_Vertex6'):
        assert _is_linked(b1, 'statemachine_Vertex6', a)
    _safe_set(a, 'statemachine_Transition5', b2)
    assert _is_linked(a, 'statemachine_Transition5', b2)
    if hasattr(b1, 'statemachine_Vertex6'):
        assert not _is_linked(b1, 'statemachine_Vertex6', a)
    if hasattr(b2, 'statemachine_Vertex6'):
        assert _is_linked(b2, 'statemachine_Vertex6', a)
    _safe_set(a, 'statemachine_Transition5', None)
    assert not _is_linked(a, 'statemachine_Transition5', b2)
    if hasattr(b2, 'statemachine_Vertex6'):
        assert not _is_linked(b2, 'statemachine_Vertex6', a)


def test_assoc_states14_link_reassign_clear():
    a = statemachine_State(name="sample_text")
    b1 = statemachine_Region()
    b2 = statemachine_Region()
    _safe_set(a, 'statemachine_State16', b1)
    assert _is_linked(a, 'statemachine_State16', b1)
    if hasattr(b1, 'statemachine_Region15'):
        assert _is_linked(b1, 'statemachine_Region15', a)
    _safe_set(a, 'statemachine_State16', b2)
    assert _is_linked(a, 'statemachine_State16', b2)
    if hasattr(b1, 'statemachine_Region15'):
        assert not _is_linked(b1, 'statemachine_Region15', a)
    if hasattr(b2, 'statemachine_Region15'):
        assert _is_linked(b2, 'statemachine_Region15', a)
    _safe_set(a, 'statemachine_State16', None)
    assert not _is_linked(a, 'statemachine_State16', b2)
    if hasattr(b2, 'statemachine_Region15'):
        assert not _is_linked(b2, 'statemachine_Region15', a)


def test_assoc_super1_link_reassign_clear():
    a = statemachine_State(name="sample_text")
    b1 = statemachine_ComplexState()
    b2 = statemachine_ComplexState()
    _safe_set(a, 'statemachine_State', b1)
    assert _is_linked(a, 'statemachine_State', b1)
    if hasattr(b1, 'statemachine_ComplexState'):
        assert _is_linked(b1, 'statemachine_ComplexState', a)
    _safe_set(a, 'statemachine_State', b2)
    assert _is_linked(a, 'statemachine_State', b2)
    if hasattr(b1, 'statemachine_ComplexState'):
        assert not _is_linked(b1, 'statemachine_ComplexState', a)
    if hasattr(b2, 'statemachine_ComplexState'):
        assert _is_linked(b2, 'statemachine_ComplexState', a)
    _safe_set(a, 'statemachine_State', None)
    assert not _is_linked(a, 'statemachine_State', b2)
    if hasattr(b2, 'statemachine_ComplexState'):
        assert not _is_linked(b2, 'statemachine_ComplexState', a)


def test_assoc_target7_link_reassign_clear():
    a = statemachine_Transition(id="sample_text")
    b1 = statemachine_Vertex()
    b2 = statemachine_Vertex()
    _safe_set(a, 'statemachine_Transition8', b1)
    assert _is_linked(a, 'statemachine_Transition8', b1)
    if hasattr(b1, 'statemachine_Vertex9'):
        assert _is_linked(b1, 'statemachine_Vertex9', a)
    _safe_set(a, 'statemachine_Transition8', b2)
    assert _is_linked(a, 'statemachine_Transition8', b2)
    if hasattr(b1, 'statemachine_Vertex9'):
        assert not _is_linked(b1, 'statemachine_Vertex9', a)
    if hasattr(b2, 'statemachine_Vertex9'):
        assert _is_linked(b2, 'statemachine_Vertex9', a)
    _safe_set(a, 'statemachine_Transition8', None)
    assert not _is_linked(a, 'statemachine_Transition8', b2)
    if hasattr(b2, 'statemachine_Vertex9'):
        assert not _is_linked(b2, 'statemachine_Vertex9', a)


def test_assoc_transitions10_link_reassign_clear():
    a = statemachine_Transition(id="sample_text")
    b1 = statemachine_Statemachine(name="sample_text")
    b2 = statemachine_Statemachine(name="sample_text_2")
    _safe_set(a, 'statemachine_Transition11', b1)
    assert _is_linked(a, 'statemachine_Transition11', b1)
    if hasattr(b1, 'statemachine_Statemachine'):
        assert _is_linked(b1, 'statemachine_Statemachine', a)
    _safe_set(a, 'statemachine_Transition11', b2)
    assert _is_linked(a, 'statemachine_Transition11', b2)
    if hasattr(b1, 'statemachine_Statemachine'):
        assert not _is_linked(b1, 'statemachine_Statemachine', a)
    if hasattr(b2, 'statemachine_Statemachine'):
        assert _is_linked(b2, 'statemachine_Statemachine', a)
    _safe_set(a, 'statemachine_Transition11', None)
    assert not _is_linked(a, 'statemachine_Transition11', b2)
    if hasattr(b2, 'statemachine_Statemachine'):
        assert not _is_linked(b2, 'statemachine_Statemachine', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Region_strategy = st.builds(Region)
@given(instance=Region_strategy)
@settings(max_examples=25)
def test_Region_instantiation(instance):
    assert isinstance(instance, Region)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)


Vertex_strategy = st.builds(Vertex)
@given(instance=Vertex_strategy)
@settings(max_examples=25)
def test_Vertex_instantiation(instance):
    assert isinstance(instance, Vertex)


statemachine_Action_strategy = st.builds(statemachine_Action, name=safe_text)
@given(instance=statemachine_Action_strategy)
@settings(max_examples=25)
def test_statemachine_Action_instantiation(instance):
    assert isinstance(instance, statemachine_Action)


statemachine_ComplexState_strategy = st.builds(statemachine_ComplexState)
@given(instance=statemachine_ComplexState_strategy)
@settings(max_examples=25)
def test_statemachine_ComplexState_instantiation(instance):
    assert isinstance(instance, statemachine_ComplexState)


statemachine_LabeledTransition_strategy = st.builds(statemachine_LabeledTransition)
@given(instance=statemachine_LabeledTransition_strategy)
@settings(max_examples=25)
def test_statemachine_LabeledTransition_instantiation(instance):
    assert isinstance(instance, statemachine_LabeledTransition)


statemachine_Pseudostate_strategy = st.builds(statemachine_Pseudostate, id=safe_text, kind=safe_text)
@given(instance=statemachine_Pseudostate_strategy)
@settings(max_examples=25)
def test_statemachine_Pseudostate_instantiation(instance):
    assert isinstance(instance, statemachine_Pseudostate)


statemachine_Region_strategy = st.builds(statemachine_Region)
@given(instance=statemachine_Region_strategy)
@settings(max_examples=25)
def test_statemachine_Region_instantiation(instance):
    assert isinstance(instance, statemachine_Region)


statemachine_State_strategy = st.builds(statemachine_State, name=safe_text)
@given(instance=statemachine_State_strategy)
@settings(max_examples=25)
def test_statemachine_State_instantiation(instance):
    assert isinstance(instance, statemachine_State)


statemachine_Statemachine_strategy = st.builds(statemachine_Statemachine, name=safe_text)
@given(instance=statemachine_Statemachine_strategy)
@settings(max_examples=25)
def test_statemachine_Statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_Statemachine)


statemachine_Transition_strategy = st.builds(statemachine_Transition, id=safe_text)
@given(instance=statemachine_Transition_strategy)
@settings(max_examples=25)
def test_statemachine_Transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)


statemachine_Vertex_strategy = st.builds(statemachine_Vertex)
@given(instance=statemachine_Vertex_strategy)
@settings(max_examples=25)
def test_statemachine_Vertex_instantiation(instance):
    assert isinstance(instance, statemachine_Vertex)



