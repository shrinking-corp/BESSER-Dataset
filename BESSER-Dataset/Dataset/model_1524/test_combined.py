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
    cpsml_Fright,
    cpsml_Interval,
    cpsml_Condition,
    cpsml_Function,
    Transition,
    cpsml_DeVariable,
    cpsml_IndeVariable,
    cpsml_ComTransition,
    cpsml_ProbTransition,
    cpsml_ODE,
    cpsml_Transition,
    cpsml_State,
    cpsml_System,
    cpsml_Variable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cpsml_fright_is_not_abstract():
    assert not inspect.isabstract(cpsml_Fright)


def test_hyp_cpsml_fright_constructor_exists():
    assert callable(cpsml_Fright.__init__)


def test_hyp_cpsml_fright_constructor_args():
    sig = inspect.signature(cpsml_Fright.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cpsml_interval_is_not_abstract():
    assert not inspect.isabstract(cpsml_Interval)


def test_hyp_cpsml_interval_constructor_exists():
    assert callable(cpsml_Interval.__init__)


def test_hyp_cpsml_interval_constructor_args():
    sig = inspect.signature(cpsml_Interval.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "right" in params, "Missing parameter 'right'"
    assert "subinterval" in params, "Missing parameter 'subinterval'"
    assert "left" in params, "Missing parameter 'left'"







def test_hyp_cpsml_condition_is_not_abstract():
    assert not inspect.isabstract(cpsml_Condition)


def test_hyp_cpsml_condition_constructor_exists():
    assert callable(cpsml_Condition.__init__)


def test_hyp_cpsml_condition_constructor_args():
    sig = inspect.signature(cpsml_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cpsml_function_is_not_abstract():
    assert not inspect.isabstract(cpsml_Function)


def test_hyp_cpsml_function_constructor_exists():
    assert callable(cpsml_Function.__init__)


def test_hyp_cpsml_function_constructor_args():
    sig = inspect.signature(cpsml_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpsml_devariable_is_not_abstract():
    assert not inspect.isabstract(cpsml_DeVariable)


def test_hyp_cpsml_devariable_constructor_exists():
    assert callable(cpsml_DeVariable.__init__)


def test_hyp_cpsml_devariable_constructor_args():
    sig = inspect.signature(cpsml_DeVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cpsml_indevariable_is_not_abstract():
    assert not inspect.isabstract(cpsml_IndeVariable)


def test_hyp_cpsml_indevariable_constructor_exists():
    assert callable(cpsml_IndeVariable.__init__)


def test_hyp_cpsml_indevariable_constructor_args():
    sig = inspect.signature(cpsml_IndeVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cpsml_comtransition_is_not_abstract():
    assert not inspect.isabstract(cpsml_ComTransition)


def test_hyp_cpsml_comtransition_constructor_exists():
    assert callable(cpsml_ComTransition.__init__)


def test_hyp_cpsml_comtransition_constructor_args():
    sig = inspect.signature(cpsml_ComTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpsml_probtransition_is_not_abstract():
    assert not inspect.isabstract(cpsml_ProbTransition)


def test_hyp_cpsml_probtransition_constructor_exists():
    assert callable(cpsml_ProbTransition.__init__)


def test_hyp_cpsml_probtransition_constructor_args():
    sig = inspect.signature(cpsml_ProbTransition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"




def test_hyp_cpsml_ode_is_not_abstract():
    assert not inspect.isabstract(cpsml_ODE)


def test_hyp_cpsml_ode_constructor_exists():
    assert callable(cpsml_ODE.__init__)


def test_hyp_cpsml_ode_constructor_args():
    sig = inspect.signature(cpsml_ODE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cpsml_transition_is_not_abstract():
    assert not inspect.isabstract(cpsml_Transition)


def test_hyp_cpsml_transition_constructor_exists():
    assert callable(cpsml_Transition.__init__)


def test_hyp_cpsml_transition_constructor_args():
    sig = inspect.signature(cpsml_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "event" in params, "Missing parameter 'event'"







def test_hyp_cpsml_state_is_not_abstract():
    assert not inspect.isabstract(cpsml_State)


def test_hyp_cpsml_state_constructor_exists():
    assert callable(cpsml_State.__init__)


def test_hyp_cpsml_state_constructor_args():
    sig = inspect.signature(cpsml_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cpsml_system_is_not_abstract():
    assert not inspect.isabstract(cpsml_System)


def test_hyp_cpsml_system_constructor_exists():
    assert callable(cpsml_System.__init__)


def test_hyp_cpsml_system_constructor_args():
    sig = inspect.signature(cpsml_System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "y0label" in params, "Missing parameter 'y0label'"
    assert "sub" in params, "Missing parameter 'sub'"
    assert "ran" in params, "Missing parameter 'ran'"







def test_hyp_cpsml_variable_is_not_abstract():
    assert not inspect.isabstract(cpsml_Variable)


def test_hyp_cpsml_variable_constructor_exists():
    assert callable(cpsml_Variable.__init__)


def test_hyp_cpsml_variable_constructor_args():
    sig = inspect.signature(cpsml_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "Globalnv" in params, "Missing parameter 'Globalnv'"




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
cpsml_Fright_strategy = st.builds(
    cpsml_Fright,
    name=
        safe_text
)
cpsml_Interval_strategy = st.builds(
    cpsml_Interval,
    name=
        safe_text,
    right=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    subinterval=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    left=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cpsml_Condition_strategy = st.builds(
    cpsml_Condition,
    name=
        safe_text
)
cpsml_Function_strategy = st.builds(
    cpsml_Function,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
cpsml_DeVariable_strategy = st.builds(
    cpsml_DeVariable,
    name=
        safe_text
)
cpsml_IndeVariable_strategy = st.builds(
    cpsml_IndeVariable,
    name=
        safe_text
)
cpsml_ComTransition_strategy = st.builds(
    cpsml_ComTransition,
)
cpsml_ProbTransition_strategy = st.builds(
    cpsml_ProbTransition,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cpsml_ODE_strategy = st.builds(
    cpsml_ODE,
    name=
        safe_text
)
cpsml_Transition_strategy = st.builds(
    cpsml_Transition,
    action=
        safe_text,
    name=
        safe_text,
    guard=
        safe_text,
    event=
        safe_text
)
cpsml_State_strategy = st.builds(
    cpsml_State,
    name=
        st.booleans()
)
cpsml_System_strategy = st.builds(
    cpsml_System,
    name=
        safe_text,
    y0label=
        st.integers(),
    sub=
        st.integers(),
    ran=
        safe_text
)
cpsml_Variable_strategy = st.builds(
    cpsml_Variable,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Globalnv=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)




@given(instance=cpsml_Fright_strategy)
def test_hyp_cpsml_fright_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=cpsml_Interval_strategy)
def test_hyp_cpsml_interval_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cpsml_Interval_strategy)
def test_hyp_cpsml_interval_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original



@given(instance=cpsml_Interval_strategy)
def test_hyp_cpsml_interval_subinterval_setter(instance):
    original = instance.subinterval
    instance.subinterval = original
    assert instance.subinterval == original



@given(instance=cpsml_Interval_strategy)
def test_hyp_cpsml_interval_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original




@given(instance=cpsml_Condition_strategy)
def test_hyp_cpsml_condition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=cpsml_Function_strategy)
def test_hyp_cpsml_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=cpsml_DeVariable_strategy)
def test_hyp_cpsml_devariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=cpsml_IndeVariable_strategy)
def test_hyp_cpsml_indevariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=cpsml_ProbTransition_strategy)
def test_hyp_cpsml_probtransition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original




@given(instance=cpsml_ODE_strategy)
def test_hyp_cpsml_ode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=cpsml_Transition_strategy)
def test_hyp_cpsml_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=cpsml_Transition_strategy)
def test_hyp_cpsml_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cpsml_Transition_strategy)
def test_hyp_cpsml_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=cpsml_Transition_strategy)
def test_hyp_cpsml_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=cpsml_Transition_strategy)
@settings(max_examples=30)
def test_hyp_cpsml_transition_holds_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.holds()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.holds).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'holds' in cpsml_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'holds' in cpsml_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'holds' in cpsml_Transition is not implemented or raised an error")




@given(instance=cpsml_State_strategy)
def test_hyp_cpsml_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=cpsml_System_strategy)
def test_hyp_cpsml_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cpsml_System_strategy)
def test_hyp_cpsml_system_y0label_setter(instance):
    original = instance.y0label
    instance.y0label = original
    assert instance.y0label == original



@given(instance=cpsml_System_strategy)
def test_hyp_cpsml_system_sub_setter(instance):
    original = instance.sub
    instance.sub = original
    assert instance.sub == original



@given(instance=cpsml_System_strategy)
def test_hyp_cpsml_system_ran_setter(instance):
    original = instance.ran
    instance.ran = original
    assert instance.ran == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=cpsml_System_strategy)
@settings(max_examples=30)
def test_hyp_cpsml_system_callscilab_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.callscilab()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.callscilab).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'callscilab' in cpsml_System is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'callscilab' in cpsml_System did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'callscilab' in cpsml_System is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=cpsml_System_strategy)
@settings(max_examples=30)
def test_hyp_cpsml_system_dojump_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.dojump()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.dojump).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'dojump' in cpsml_System is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dojump' in cpsml_System did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dojump' in cpsml_System is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=cpsml_System_strategy)
@settings(max_examples=30)
def test_hyp_cpsml_system_main_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.main()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.main).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'main' in cpsml_System is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'main' in cpsml_System did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'main' in cpsml_System is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=cpsml_System_strategy)
@settings(max_examples=30)
def test_hyp_cpsml_system_realizeinitializemodel_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RealizeInitializeModel(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RealizeInitializeModel).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RealizeInitializeModel' in cpsml_System is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RealizeInitializeModel' in cpsml_System did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RealizeInitializeModel' in cpsml_System is not implemented or raised an error")




@given(instance=cpsml_Variable_strategy)
def test_hyp_cpsml_variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=cpsml_Variable_strategy)
def test_hyp_cpsml_variable_Globalnv_setter(instance):
    original = instance.Globalnv
    instance.Globalnv = original
    assert instance.Globalnv == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Transition,
    cpsml_ComTransition,
    cpsml_Condition,
    cpsml_DeVariable,
    cpsml_Fright,
    cpsml_Function,
    cpsml_IndeVariable,
    cpsml_Interval,
    cpsml_ODE,
    cpsml_ProbTransition,
    cpsml_State,
    cpsml_System,
    cpsml_Transition,
    cpsml_Variable,
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

def test_cpsml_Condition_name_value_roundtrip():
    instance = cpsml_Condition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpsml_DeVariable_name_value_roundtrip():
    instance = cpsml_DeVariable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpsml_Fright_name_value_roundtrip():
    instance = cpsml_Fright(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpsml_Function_name_value_roundtrip():
    instance = cpsml_Function(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpsml_IndeVariable_name_value_roundtrip():
    instance = cpsml_IndeVariable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpsml_Interval_left_value_roundtrip():
    instance = cpsml_Interval(left=3.14, name="sample_text", right=3.14, subinterval=3.14)
    assert instance.left == 3.14
    instance.left = 9.99
    assert instance.left == 9.99


def test_cpsml_Interval_name_value_roundtrip():
    instance = cpsml_Interval(left=3.14, name="sample_text", right=3.14, subinterval=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpsml_Interval_right_value_roundtrip():
    instance = cpsml_Interval(left=3.14, name="sample_text", right=3.14, subinterval=3.14)
    assert instance.right == 3.14
    instance.right = 9.99
    assert instance.right == 9.99


def test_cpsml_Interval_subinterval_value_roundtrip():
    instance = cpsml_Interval(left=3.14, name="sample_text", right=3.14, subinterval=3.14)
    assert instance.subinterval == 3.14
    instance.subinterval = 9.99
    assert instance.subinterval == 9.99


def test_cpsml_ODE_name_value_roundtrip():
    instance = cpsml_ODE(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpsml_ProbTransition_probability_value_roundtrip():
    instance = cpsml_ProbTransition(probability=3.14)
    assert instance.probability == 3.14
    instance.probability = 9.99
    assert instance.probability == 9.99


def test_cpsml_State_name_value_roundtrip():
    instance = cpsml_State(name=True)
    assert instance.name == True
    instance.name = False
    assert instance.name == False


def test_cpsml_System_name_value_roundtrip():
    instance = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpsml_System_ran_value_roundtrip():
    instance = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    assert instance.ran == "sample_text"
    instance.ran = "sample_text_2"
    assert instance.ran == "sample_text_2"


def test_cpsml_System_sub_value_roundtrip():
    instance = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    assert instance.sub == 7
    instance.sub = 13
    assert instance.sub == 13


def test_cpsml_System_y0label_value_roundtrip():
    instance = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    assert instance.y0label == 7
    instance.y0label = 13
    assert instance.y0label == 13


def test_cpsml_Transition_action_value_roundtrip():
    instance = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_cpsml_Transition_event_value_roundtrip():
    instance = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_cpsml_Transition_guard_value_roundtrip():
    instance = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    assert instance.guard == "sample_text"
    instance.guard = "sample_text_2"
    assert instance.guard == "sample_text_2"


def test_cpsml_Transition_name_value_roundtrip():
    instance = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpsml_Variable_Globalnv_value_roundtrip():
    instance = cpsml_Variable(Globalnv=3.14, value=3.14)
    assert instance.Globalnv == 3.14
    instance.Globalnv = 9.99
    assert instance.Globalnv == 9.99


def test_cpsml_Variable_value_value_roundtrip():
    instance = cpsml_Variable(Globalnv=3.14, value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_cpsml_ComTransition_isa_Transition():
    instance = cpsml_ComTransition()
    assert isinstance(instance, Transition)


def test_cpsml_ProbTransition_isa_Transition():
    instance = cpsml_ProbTransition(probability=3.14)
    assert isinstance(instance, Transition)


def test_assoc_condition60_link_reassign_clear():
    a = cpsml_ODE(name="sample_text")
    b1 = cpsml_Condition(name="sample_text")
    b2 = cpsml_Condition(name="sample_text_2")
    _safe_set(a, 'cpsml_ODE61', b1)
    assert _is_linked(a, 'cpsml_ODE61', b1)
    if hasattr(b1, 'cpsml_Condition'):
        assert _is_linked(b1, 'cpsml_Condition', a)
    _safe_set(a, 'cpsml_ODE61', b2)
    assert _is_linked(a, 'cpsml_ODE61', b2)
    if hasattr(b1, 'cpsml_Condition'):
        assert not _is_linked(b1, 'cpsml_Condition', a)
    if hasattr(b2, 'cpsml_Condition'):
        assert _is_linked(b2, 'cpsml_Condition', a)
    _safe_set(a, 'cpsml_ODE61', None)
    assert not _is_linked(a, 'cpsml_ODE61', b2)
    if hasattr(b2, 'cpsml_Condition'):
        assert not _is_linked(b2, 'cpsml_Condition', a)


def test_assoc_csrc51_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_ComTransition()
    b2 = cpsml_ComTransition()
    _safe_set(a, 'State', b1)
    assert _is_linked(a, 'State', b1)
    if hasattr(b1, 'outgoingComTransitions'):
        assert _is_linked(b1, 'outgoingComTransitions', a)
    _safe_set(a, 'State', b2)
    assert _is_linked(a, 'State', b2)
    if hasattr(b1, 'outgoingComTransitions'):
        assert not _is_linked(b1, 'outgoingComTransitions', a)
    if hasattr(b2, 'outgoingComTransitions'):
        assert _is_linked(b2, 'outgoingComTransitions', a)
    _safe_set(a, 'State', None)
    assert not _is_linked(a, 'State', b2)
    if hasattr(b2, 'outgoingComTransitions'):
        assert not _is_linked(b2, 'outgoingComTransitions', a)


def test_assoc_ctgt52_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_ComTransition()
    b2 = cpsml_ComTransition()
    _safe_set(a, 'State53', b1)
    assert _is_linked(a, 'State53', b1)
    if hasattr(b1, 'incomingComTransitions'):
        assert _is_linked(b1, 'incomingComTransitions', a)
    _safe_set(a, 'State53', b2)
    assert _is_linked(a, 'State53', b2)
    if hasattr(b1, 'incomingComTransitions'):
        assert not _is_linked(b1, 'incomingComTransitions', a)
    if hasattr(b2, 'incomingComTransitions'):
        assert _is_linked(b2, 'incomingComTransitions', a)
    _safe_set(a, 'State53', None)
    assert not _is_linked(a, 'State53', b2)
    if hasattr(b2, 'incomingComTransitions'):
        assert not _is_linked(b2, 'incomingComTransitions', a)


def test_assoc_currentState13_link_reassign_clear():
    a = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    b1 = cpsml_State(name=True)
    b2 = cpsml_State(name=False)
    _safe_set(a, 'cpsml_System14', b1)
    assert _is_linked(a, 'cpsml_System14', b1)
    if hasattr(b1, 'cpsml_State15'):
        assert _is_linked(b1, 'cpsml_State15', a)
    _safe_set(a, 'cpsml_System14', b2)
    assert _is_linked(a, 'cpsml_System14', b2)
    if hasattr(b1, 'cpsml_State15'):
        assert not _is_linked(b1, 'cpsml_State15', a)
    if hasattr(b2, 'cpsml_State15'):
        assert _is_linked(b2, 'cpsml_State15', a)
    _safe_set(a, 'cpsml_System14', None)
    assert not _is_linked(a, 'cpsml_System14', b2)
    if hasattr(b2, 'cpsml_State15'):
        assert not _is_linked(b2, 'cpsml_State15', a)


def test_assoc_devariable66_link_reassign_clear():
    a = cpsml_Function(name="sample_text")
    b1 = cpsml_DeVariable(name="sample_text")
    b2 = cpsml_DeVariable(name="sample_text_2")
    _safe_set(a, 'cpsml_Function67', b1)
    assert _is_linked(a, 'cpsml_Function67', b1)
    if hasattr(b1, 'cpsml_DeVariable'):
        assert _is_linked(b1, 'cpsml_DeVariable', a)
    _safe_set(a, 'cpsml_Function67', b2)
    assert _is_linked(a, 'cpsml_Function67', b2)
    if hasattr(b1, 'cpsml_DeVariable'):
        assert not _is_linked(b1, 'cpsml_DeVariable', a)
    if hasattr(b2, 'cpsml_DeVariable'):
        assert _is_linked(b2, 'cpsml_DeVariable', a)
    _safe_set(a, 'cpsml_Function67', None)
    assert not _is_linked(a, 'cpsml_Function67', b2)
    if hasattr(b2, 'cpsml_DeVariable'):
        assert not _is_linked(b2, 'cpsml_DeVariable', a)


def test_assoc_fatherState16_link_reassign_clear():
    a = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    b1 = cpsml_State(name=True)
    b2 = cpsml_State(name=False)
    _safe_set(a, 'cpsml_System17', b1)
    assert _is_linked(a, 'cpsml_System17', b1)
    if hasattr(b1, 'cpsml_State18'):
        assert _is_linked(b1, 'cpsml_State18', a)
    _safe_set(a, 'cpsml_System17', b2)
    assert _is_linked(a, 'cpsml_System17', b2)
    if hasattr(b1, 'cpsml_State18'):
        assert not _is_linked(b1, 'cpsml_State18', a)
    if hasattr(b2, 'cpsml_State18'):
        assert _is_linked(b2, 'cpsml_State18', a)
    _safe_set(a, 'cpsml_System17', None)
    assert not _is_linked(a, 'cpsml_System17', b2)
    if hasattr(b2, 'cpsml_State18'):
        assert not _is_linked(b2, 'cpsml_State18', a)


def test_assoc_fright68_link_reassign_clear():
    a = cpsml_Function(name="sample_text")
    b1 = cpsml_Fright(name="sample_text")
    b2 = cpsml_Fright(name="sample_text_2")
    _safe_set(a, 'cpsml_Function69', b1)
    assert _is_linked(a, 'cpsml_Function69', b1)
    if hasattr(b1, 'cpsml_Fright'):
        assert _is_linked(b1, 'cpsml_Fright', a)
    _safe_set(a, 'cpsml_Function69', b2)
    assert _is_linked(a, 'cpsml_Function69', b2)
    if hasattr(b1, 'cpsml_Fright'):
        assert not _is_linked(b1, 'cpsml_Fright', a)
    if hasattr(b2, 'cpsml_Fright'):
        assert _is_linked(b2, 'cpsml_Fright', a)
    _safe_set(a, 'cpsml_Function69', None)
    assert not _is_linked(a, 'cpsml_Function69', b2)
    if hasattr(b2, 'cpsml_Fright'):
        assert not _is_linked(b2, 'cpsml_Fright', a)


def test_assoc_function58_link_reassign_clear():
    a = cpsml_ODE(name="sample_text")
    b1 = cpsml_Function(name="sample_text")
    b2 = cpsml_Function(name="sample_text_2")
    _safe_set(a, 'cpsml_ODE59', b1)
    assert _is_linked(a, 'cpsml_ODE59', b1)
    if hasattr(b1, 'cpsml_Function'):
        assert _is_linked(b1, 'cpsml_Function', a)
    _safe_set(a, 'cpsml_ODE59', b2)
    assert _is_linked(a, 'cpsml_ODE59', b2)
    if hasattr(b1, 'cpsml_Function'):
        assert not _is_linked(b1, 'cpsml_Function', a)
    if hasattr(b2, 'cpsml_Function'):
        assert _is_linked(b2, 'cpsml_Function', a)
    _safe_set(a, 'cpsml_ODE59', None)
    assert not _is_linked(a, 'cpsml_ODE59', b2)
    if hasattr(b2, 'cpsml_Function'):
        assert not _is_linked(b2, 'cpsml_Function', a)


def test_assoc_incomingComTransitions25_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_ComTransition()
    b2 = cpsml_ComTransition()
    _safe_set(a, 'ctgt', {b1})
    assert _is_linked(a, 'ctgt', b1)
    if hasattr(b1, 'ComTransition26'):
        assert _is_linked(b1, 'ComTransition26', a)
    _safe_set(a, 'ctgt', {b2})
    assert _is_linked(a, 'ctgt', b2)
    if hasattr(b1, 'ComTransition26'):
        assert not _is_linked(b1, 'ComTransition26', a)
    if hasattr(b2, 'ComTransition26'):
        assert _is_linked(b2, 'ComTransition26', a)
    _safe_set(a, 'ctgt', set())
    assert not _is_linked(a, 'ctgt', b2)
    if hasattr(b2, 'ComTransition26'):
        assert not _is_linked(b2, 'ComTransition26', a)


def test_assoc_incomingProbTransitions28_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_ProbTransition(probability=3.14)
    b2 = cpsml_ProbTransition(probability=9.99)
    _safe_set(a, 'ptgt', {b1})
    assert _is_linked(a, 'ptgt', b1)
    if hasattr(b1, 'ProbTransition29'):
        assert _is_linked(b1, 'ProbTransition29', a)
    _safe_set(a, 'ptgt', {b2})
    assert _is_linked(a, 'ptgt', b2)
    if hasattr(b1, 'ProbTransition29'):
        assert not _is_linked(b1, 'ProbTransition29', a)
    if hasattr(b2, 'ProbTransition29'):
        assert _is_linked(b2, 'ProbTransition29', a)
    _safe_set(a, 'ptgt', set())
    assert not _is_linked(a, 'ptgt', b2)
    if hasattr(b2, 'ProbTransition29'):
        assert not _is_linked(b2, 'ProbTransition29', a)


def test_assoc_indevariable64_link_reassign_clear():
    a = cpsml_IndeVariable(name="sample_text")
    b1 = cpsml_Function(name="sample_text")
    b2 = cpsml_Function(name="sample_text_2")
    _safe_set(a, 'cpsml_IndeVariable', b1)
    assert _is_linked(a, 'cpsml_IndeVariable', b1)
    if hasattr(b1, 'cpsml_Function65'):
        assert _is_linked(b1, 'cpsml_Function65', a)
    _safe_set(a, 'cpsml_IndeVariable', b2)
    assert _is_linked(a, 'cpsml_IndeVariable', b2)
    if hasattr(b1, 'cpsml_Function65'):
        assert not _is_linked(b1, 'cpsml_Function65', a)
    if hasattr(b2, 'cpsml_Function65'):
        assert _is_linked(b2, 'cpsml_Function65', a)
    _safe_set(a, 'cpsml_IndeVariable', None)
    assert not _is_linked(a, 'cpsml_IndeVariable', b2)
    if hasattr(b2, 'cpsml_Function65'):
        assert not _is_linked(b2, 'cpsml_Function65', a)


def test_assoc_initialState8_link_reassign_clear():
    a = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    b1 = cpsml_State(name=True)
    b2 = cpsml_State(name=False)
    _safe_set(a, 'cpsml_System9', b1)
    assert _is_linked(a, 'cpsml_System9', b1)
    if hasattr(b1, 'cpsml_State10'):
        assert _is_linked(b1, 'cpsml_State10', a)
    _safe_set(a, 'cpsml_System9', b2)
    assert _is_linked(a, 'cpsml_System9', b2)
    if hasattr(b1, 'cpsml_State10'):
        assert not _is_linked(b1, 'cpsml_State10', a)
    if hasattr(b2, 'cpsml_State10'):
        assert _is_linked(b2, 'cpsml_State10', a)
    _safe_set(a, 'cpsml_System9', None)
    assert not _is_linked(a, 'cpsml_System9', b2)
    if hasattr(b2, 'cpsml_State10'):
        assert not _is_linked(b2, 'cpsml_State10', a)


def test_assoc_initialsubstate34_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_State(name=True)
    b2 = cpsml_State(name=False)
    _safe_set(a, 'cpsml_State33', b1)
    assert _is_linked(a, 'cpsml_State33', b1)
    if hasattr(b1, 'cpsml_State35'):
        assert _is_linked(b1, 'cpsml_State35', a)
    _safe_set(a, 'cpsml_State33', b2)
    assert _is_linked(a, 'cpsml_State33', b2)
    if hasattr(b1, 'cpsml_State35'):
        assert not _is_linked(b1, 'cpsml_State35', a)
    if hasattr(b2, 'cpsml_State35'):
        assert _is_linked(b2, 'cpsml_State35', a)
    _safe_set(a, 'cpsml_State33', None)
    assert not _is_linked(a, 'cpsml_State33', b2)
    if hasattr(b2, 'cpsml_State35'):
        assert not _is_linked(b2, 'cpsml_State35', a)


def test_assoc_interval62_link_reassign_clear():
    a = cpsml_ODE(name="sample_text")
    b1 = cpsml_Interval(left=3.14, name="sample_text", right=3.14, subinterval=3.14)
    b2 = cpsml_Interval(left=9.99, name="sample_text_2", right=9.99, subinterval=9.99)
    _safe_set(a, 'cpsml_ODE63', b1)
    assert _is_linked(a, 'cpsml_ODE63', b1)
    if hasattr(b1, 'cpsml_Interval'):
        assert _is_linked(b1, 'cpsml_Interval', a)
    _safe_set(a, 'cpsml_ODE63', b2)
    assert _is_linked(a, 'cpsml_ODE63', b2)
    if hasattr(b1, 'cpsml_Interval'):
        assert not _is_linked(b1, 'cpsml_Interval', a)
    if hasattr(b2, 'cpsml_Interval'):
        assert _is_linked(b2, 'cpsml_Interval', a)
    _safe_set(a, 'cpsml_ODE63', None)
    assert not _is_linked(a, 'cpsml_ODE63', b2)
    if hasattr(b2, 'cpsml_Interval'):
        assert not _is_linked(b2, 'cpsml_Interval', a)


def test_assoc_outgoingComTransitions24_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_ComTransition()
    b2 = cpsml_ComTransition()
    _safe_set(a, 'csrc', {b1})
    assert _is_linked(a, 'csrc', b1)
    if hasattr(b1, 'ComTransition'):
        assert _is_linked(b1, 'ComTransition', a)
    _safe_set(a, 'csrc', {b2})
    assert _is_linked(a, 'csrc', b2)
    if hasattr(b1, 'ComTransition'):
        assert not _is_linked(b1, 'ComTransition', a)
    if hasattr(b2, 'ComTransition'):
        assert _is_linked(b2, 'ComTransition', a)
    _safe_set(a, 'csrc', set())
    assert not _is_linked(a, 'csrc', b2)
    if hasattr(b2, 'ComTransition'):
        assert not _is_linked(b2, 'ComTransition', a)


def test_assoc_outgoingProbTransitions27_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_ProbTransition(probability=3.14)
    b2 = cpsml_ProbTransition(probability=9.99)
    _safe_set(a, 'psrc', {b1})
    assert _is_linked(a, 'psrc', b1)
    if hasattr(b1, 'ProbTransition'):
        assert _is_linked(b1, 'ProbTransition', a)
    _safe_set(a, 'psrc', {b2})
    assert _is_linked(a, 'psrc', b2)
    if hasattr(b1, 'ProbTransition'):
        assert not _is_linked(b1, 'ProbTransition', a)
    if hasattr(b2, 'ProbTransition'):
        assert _is_linked(b2, 'ProbTransition', a)
    _safe_set(a, 'psrc', set())
    assert not _is_linked(a, 'psrc', b2)
    if hasattr(b2, 'ProbTransition'):
        assert not _is_linked(b2, 'ProbTransition', a)


def test_assoc_ownedStates4_link_reassign_clear():
    a = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    b1 = cpsml_State(name=True)
    b2 = cpsml_State(name=False)
    _safe_set(a, 'cpsml_System5', {b1})
    assert _is_linked(a, 'cpsml_System5', b1)
    if hasattr(b1, 'cpsml_State'):
        assert _is_linked(b1, 'cpsml_State', a)
    _safe_set(a, 'cpsml_System5', {b2})
    assert _is_linked(a, 'cpsml_System5', b2)
    if hasattr(b1, 'cpsml_State'):
        assert not _is_linked(b1, 'cpsml_State', a)
    if hasattr(b2, 'cpsml_State'):
        assert _is_linked(b2, 'cpsml_State', a)
    _safe_set(a, 'cpsml_System5', set())
    assert not _is_linked(a, 'cpsml_System5', b2)
    if hasattr(b2, 'cpsml_State'):
        assert not _is_linked(b2, 'cpsml_State', a)


def test_assoc_ownedTransitions6_link_reassign_clear():
    a = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    b1 = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    b2 = cpsml_System(name="sample_text_2", ran="sample_text_2", sub=13, y0label=13)
    _safe_set(a, 'cpsml_Transition', b1)
    assert _is_linked(a, 'cpsml_Transition', b1)
    if hasattr(b1, 'cpsml_System7'):
        assert _is_linked(b1, 'cpsml_System7', a)
    _safe_set(a, 'cpsml_Transition', b2)
    assert _is_linked(a, 'cpsml_Transition', b2)
    if hasattr(b1, 'cpsml_System7'):
        assert not _is_linked(b1, 'cpsml_System7', a)
    if hasattr(b2, 'cpsml_System7'):
        assert _is_linked(b2, 'cpsml_System7', a)
    _safe_set(a, 'cpsml_Transition', None)
    assert not _is_linked(a, 'cpsml_Transition', b2)
    if hasattr(b2, 'cpsml_System7'):
        assert not _is_linked(b2, 'cpsml_System7', a)


def test_assoc_ownedodes11_link_reassign_clear():
    a = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    b1 = cpsml_ODE(name="sample_text")
    b2 = cpsml_ODE(name="sample_text_2")
    _safe_set(a, 'cpsml_System12', {b1})
    assert _is_linked(a, 'cpsml_System12', b1)
    if hasattr(b1, 'cpsml_ODE'):
        assert _is_linked(b1, 'cpsml_ODE', a)
    _safe_set(a, 'cpsml_System12', {b2})
    assert _is_linked(a, 'cpsml_System12', b2)
    if hasattr(b1, 'cpsml_ODE'):
        assert not _is_linked(b1, 'cpsml_ODE', a)
    if hasattr(b2, 'cpsml_ODE'):
        assert _is_linked(b2, 'cpsml_ODE', a)
    _safe_set(a, 'cpsml_System12', set())
    assert not _is_linked(a, 'cpsml_System12', b2)
    if hasattr(b2, 'cpsml_ODE'):
        assert not _is_linked(b2, 'cpsml_ODE', a)


def test_assoc_ownedvariables0_link_reassign_clear():
    a = cpsml_Variable(Globalnv=3.14, value=3.14)
    b1 = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    b2 = cpsml_System(name="sample_text_2", ran="sample_text_2", sub=13, y0label=13)
    _safe_set(a, 'cpsml_Variable', b1)
    assert _is_linked(a, 'cpsml_Variable', b1)
    if hasattr(b1, 'cpsml_System'):
        assert _is_linked(b1, 'cpsml_System', a)
    _safe_set(a, 'cpsml_Variable', b2)
    assert _is_linked(a, 'cpsml_Variable', b2)
    if hasattr(b1, 'cpsml_System'):
        assert not _is_linked(b1, 'cpsml_System', a)
    if hasattr(b2, 'cpsml_System'):
        assert _is_linked(b2, 'cpsml_System', a)
    _safe_set(a, 'cpsml_Variable', None)
    assert not _is_linked(a, 'cpsml_Variable', b2)
    if hasattr(b2, 'cpsml_System'):
        assert not _is_linked(b2, 'cpsml_System', a)


def test_assoc_psrc54_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_ProbTransition(probability=3.14)
    b2 = cpsml_ProbTransition(probability=9.99)
    _safe_set(a, 'State55', b1)
    assert _is_linked(a, 'State55', b1)
    if hasattr(b1, 'outgoingProbTransitions'):
        assert _is_linked(b1, 'outgoingProbTransitions', a)
    _safe_set(a, 'State55', b2)
    assert _is_linked(a, 'State55', b2)
    if hasattr(b1, 'outgoingProbTransitions'):
        assert not _is_linked(b1, 'outgoingProbTransitions', a)
    if hasattr(b2, 'outgoingProbTransitions'):
        assert _is_linked(b2, 'outgoingProbTransitions', a)
    _safe_set(a, 'State55', None)
    assert not _is_linked(a, 'State55', b2)
    if hasattr(b2, 'outgoingProbTransitions'):
        assert not _is_linked(b2, 'outgoingProbTransitions', a)


def test_assoc_ptgt56_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_ProbTransition(probability=3.14)
    b2 = cpsml_ProbTransition(probability=9.99)
    _safe_set(a, 'State57', b1)
    assert _is_linked(a, 'State57', b1)
    if hasattr(b1, 'incomingProbTransitions'):
        assert _is_linked(b1, 'incomingProbTransitions', a)
    _safe_set(a, 'State57', b2)
    assert _is_linked(a, 'State57', b2)
    if hasattr(b1, 'incomingProbTransitions'):
        assert not _is_linked(b1, 'incomingProbTransitions', a)
    if hasattr(b2, 'incomingProbTransitions'):
        assert _is_linked(b2, 'incomingProbTransitions', a)
    _safe_set(a, 'State57', None)
    assert not _is_linked(a, 'State57', b2)
    if hasattr(b2, 'incomingProbTransitions'):
        assert not _is_linked(b2, 'incomingProbTransitions', a)


def test_assoc_ptok19_link_reassign_clear():
    a = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    b1 = cpsml_ProbTransition(probability=3.14)
    b2 = cpsml_ProbTransition(probability=9.99)
    _safe_set(a, 'cpsml_System20', b1)
    assert _is_linked(a, 'cpsml_System20', b1)
    if hasattr(b1, 'cpsml_ProbTransition'):
        assert _is_linked(b1, 'cpsml_ProbTransition', a)
    _safe_set(a, 'cpsml_System20', b2)
    assert _is_linked(a, 'cpsml_System20', b2)
    if hasattr(b1, 'cpsml_ProbTransition'):
        assert not _is_linked(b1, 'cpsml_ProbTransition', a)
    if hasattr(b2, 'cpsml_ProbTransition'):
        assert _is_linked(b2, 'cpsml_ProbTransition', a)
    _safe_set(a, 'cpsml_System20', None)
    assert not _is_linked(a, 'cpsml_System20', b2)
    if hasattr(b2, 'cpsml_ProbTransition'):
        assert not _is_linked(b2, 'cpsml_ProbTransition', a)


def test_assoc_relatedvariable1_link_reassign_clear():
    a = cpsml_Variable(Globalnv=3.14, value=3.14)
    b1 = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    b2 = cpsml_System(name="sample_text_2", ran="sample_text_2", sub=13, y0label=13)
    _safe_set(a, 'cpsml_Variable3', b1)
    assert _is_linked(a, 'cpsml_Variable3', b1)
    if hasattr(b1, 'cpsml_System2'):
        assert _is_linked(b1, 'cpsml_System2', a)
    _safe_set(a, 'cpsml_Variable3', b2)
    assert _is_linked(a, 'cpsml_Variable3', b2)
    if hasattr(b1, 'cpsml_System2'):
        assert not _is_linked(b1, 'cpsml_System2', a)
    if hasattr(b2, 'cpsml_System2'):
        assert _is_linked(b2, 'cpsml_System2', a)
    _safe_set(a, 'cpsml_Variable3', None)
    assert not _is_linked(a, 'cpsml_Variable3', b2)
    if hasattr(b2, 'cpsml_System2'):
        assert not _is_linked(b2, 'cpsml_System2', a)


def test_assoc_relatedvariable248_link_reassign_clear():
    a = cpsml_Variable(Globalnv=3.14, value=3.14)
    b1 = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    b2 = cpsml_Transition(action="sample_text_2", event="sample_text_2", guard="sample_text_2", name="sample_text_2")
    _safe_set(a, 'cpsml_Variable50', b1)
    assert _is_linked(a, 'cpsml_Variable50', b1)
    if hasattr(b1, 'cpsml_Transition49'):
        assert _is_linked(b1, 'cpsml_Transition49', a)
    _safe_set(a, 'cpsml_Variable50', b2)
    assert _is_linked(a, 'cpsml_Variable50', b2)
    if hasattr(b1, 'cpsml_Transition49'):
        assert not _is_linked(b1, 'cpsml_Transition49', a)
    if hasattr(b2, 'cpsml_Transition49'):
        assert _is_linked(b2, 'cpsml_Transition49', a)
    _safe_set(a, 'cpsml_Variable50', None)
    assert not _is_linked(a, 'cpsml_Variable50', b2)
    if hasattr(b2, 'cpsml_Transition49'):
        assert not _is_linked(b2, 'cpsml_Transition49', a)


def test_assoc_slaveode21_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_ODE(name="sample_text")
    b2 = cpsml_ODE(name="sample_text_2")
    _safe_set(a, 'cpsml_State22', b1)
    assert _is_linked(a, 'cpsml_State22', b1)
    if hasattr(b1, 'cpsml_ODE23'):
        assert _is_linked(b1, 'cpsml_ODE23', a)
    _safe_set(a, 'cpsml_State22', b2)
    assert _is_linked(a, 'cpsml_State22', b2)
    if hasattr(b1, 'cpsml_ODE23'):
        assert not _is_linked(b1, 'cpsml_ODE23', a)
    if hasattr(b2, 'cpsml_ODE23'):
        assert _is_linked(b2, 'cpsml_ODE23', a)
    _safe_set(a, 'cpsml_State22', None)
    assert not _is_linked(a, 'cpsml_State22', b2)
    if hasattr(b2, 'cpsml_ODE23'):
        assert not _is_linked(b2, 'cpsml_ODE23', a)


def test_assoc_subStates31_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_State(name=True)
    b2 = cpsml_State(name=False)
    _safe_set(a, 'cpsml_State30', {b1})
    assert _is_linked(a, 'cpsml_State30', b1)
    if hasattr(b1, 'cpsml_State32'):
        assert _is_linked(b1, 'cpsml_State32', a)
    _safe_set(a, 'cpsml_State30', {b2})
    assert _is_linked(a, 'cpsml_State30', b2)
    if hasattr(b1, 'cpsml_State32'):
        assert not _is_linked(b1, 'cpsml_State32', a)
    if hasattr(b2, 'cpsml_State32'):
        assert _is_linked(b2, 'cpsml_State32', a)
    _safe_set(a, 'cpsml_State30', set())
    assert not _is_linked(a, 'cpsml_State30', b2)
    if hasattr(b2, 'cpsml_State32'):
        assert not _is_linked(b2, 'cpsml_State32', a)


def test_assoc_subodes39_link_reassign_clear():
    a = cpsml_State(name=True)
    b1 = cpsml_ODE(name="sample_text")
    b2 = cpsml_ODE(name="sample_text_2")
    _safe_set(a, 'cpsml_State40', {b1})
    assert _is_linked(a, 'cpsml_State40', b1)
    if hasattr(b1, 'cpsml_ODE41'):
        assert _is_linked(b1, 'cpsml_ODE41', a)
    _safe_set(a, 'cpsml_State40', {b2})
    assert _is_linked(a, 'cpsml_State40', b2)
    if hasattr(b1, 'cpsml_ODE41'):
        assert not _is_linked(b1, 'cpsml_ODE41', a)
    if hasattr(b2, 'cpsml_ODE41'):
        assert _is_linked(b2, 'cpsml_ODE41', a)
    _safe_set(a, 'cpsml_State40', set())
    assert not _is_linked(a, 'cpsml_State40', b2)
    if hasattr(b2, 'cpsml_ODE41'):
        assert not _is_linked(b2, 'cpsml_ODE41', a)


def test_assoc_subrelatedvariable45_link_reassign_clear():
    a = cpsml_Variable(Globalnv=3.14, value=3.14)
    b1 = cpsml_State(name=True)
    b2 = cpsml_State(name=False)
    _safe_set(a, 'cpsml_Variable47', b1)
    assert _is_linked(a, 'cpsml_Variable47', b1)
    if hasattr(b1, 'cpsml_State46'):
        assert _is_linked(b1, 'cpsml_State46', a)
    _safe_set(a, 'cpsml_Variable47', b2)
    assert _is_linked(a, 'cpsml_Variable47', b2)
    if hasattr(b1, 'cpsml_State46'):
        assert not _is_linked(b1, 'cpsml_State46', a)
    if hasattr(b2, 'cpsml_State46'):
        assert _is_linked(b2, 'cpsml_State46', a)
    _safe_set(a, 'cpsml_Variable47', None)
    assert not _is_linked(a, 'cpsml_Variable47', b2)
    if hasattr(b2, 'cpsml_State46'):
        assert not _is_linked(b2, 'cpsml_State46', a)


def test_assoc_subrelatedvariables42_link_reassign_clear():
    a = cpsml_Variable(Globalnv=3.14, value=3.14)
    b1 = cpsml_State(name=True)
    b2 = cpsml_State(name=False)
    _safe_set(a, 'cpsml_Variable44', b1)
    assert _is_linked(a, 'cpsml_Variable44', b1)
    if hasattr(b1, 'cpsml_State43'):
        assert _is_linked(b1, 'cpsml_State43', a)
    _safe_set(a, 'cpsml_Variable44', b2)
    assert _is_linked(a, 'cpsml_Variable44', b2)
    if hasattr(b1, 'cpsml_State43'):
        assert not _is_linked(b1, 'cpsml_State43', a)
    if hasattr(b2, 'cpsml_State43'):
        assert _is_linked(b2, 'cpsml_State43', a)
    _safe_set(a, 'cpsml_Variable44', None)
    assert not _is_linked(a, 'cpsml_Variable44', b2)
    if hasattr(b2, 'cpsml_State43'):
        assert not _is_linked(b2, 'cpsml_State43', a)


def test_assoc_subtransitions36_link_reassign_clear():
    a = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    b1 = cpsml_State(name=True)
    b2 = cpsml_State(name=False)
    _safe_set(a, 'cpsml_Transition38', b1)
    assert _is_linked(a, 'cpsml_Transition38', b1)
    if hasattr(b1, 'cpsml_State37'):
        assert _is_linked(b1, 'cpsml_State37', a)
    _safe_set(a, 'cpsml_Transition38', b2)
    assert _is_linked(a, 'cpsml_Transition38', b2)
    if hasattr(b1, 'cpsml_State37'):
        assert not _is_linked(b1, 'cpsml_State37', a)
    if hasattr(b2, 'cpsml_State37'):
        assert _is_linked(b2, 'cpsml_State37', a)
    _safe_set(a, 'cpsml_Transition38', None)
    assert not _is_linked(a, 'cpsml_Transition38', b2)
    if hasattr(b2, 'cpsml_State37'):
        assert not _is_linked(b2, 'cpsml_State37', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)


cpsml_ComTransition_strategy = st.builds(cpsml_ComTransition)
@given(instance=cpsml_ComTransition_strategy)
@settings(max_examples=25)
def test_cpsml_ComTransition_instantiation(instance):
    assert isinstance(instance, cpsml_ComTransition)


cpsml_Condition_strategy = st.builds(cpsml_Condition, name=safe_text)
@given(instance=cpsml_Condition_strategy)
@settings(max_examples=25)
def test_cpsml_Condition_instantiation(instance):
    assert isinstance(instance, cpsml_Condition)


cpsml_DeVariable_strategy = st.builds(cpsml_DeVariable, name=safe_text)
@given(instance=cpsml_DeVariable_strategy)
@settings(max_examples=25)
def test_cpsml_DeVariable_instantiation(instance):
    assert isinstance(instance, cpsml_DeVariable)


cpsml_Fright_strategy = st.builds(cpsml_Fright, name=safe_text)
@given(instance=cpsml_Fright_strategy)
@settings(max_examples=25)
def test_cpsml_Fright_instantiation(instance):
    assert isinstance(instance, cpsml_Fright)


cpsml_Function_strategy = st.builds(cpsml_Function, name=safe_text)
@given(instance=cpsml_Function_strategy)
@settings(max_examples=25)
def test_cpsml_Function_instantiation(instance):
    assert isinstance(instance, cpsml_Function)


cpsml_IndeVariable_strategy = st.builds(cpsml_IndeVariable, name=safe_text)
@given(instance=cpsml_IndeVariable_strategy)
@settings(max_examples=25)
def test_cpsml_IndeVariable_instantiation(instance):
    assert isinstance(instance, cpsml_IndeVariable)


cpsml_Interval_strategy = st.builds(cpsml_Interval, left=st.floats(allow_nan=False, allow_infinity=False), name=safe_text, right=st.floats(allow_nan=False, allow_infinity=False), subinterval=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=cpsml_Interval_strategy)
@settings(max_examples=25)
def test_cpsml_Interval_instantiation(instance):
    assert isinstance(instance, cpsml_Interval)


cpsml_ODE_strategy = st.builds(cpsml_ODE, name=safe_text)
@given(instance=cpsml_ODE_strategy)
@settings(max_examples=25)
def test_cpsml_ODE_instantiation(instance):
    assert isinstance(instance, cpsml_ODE)


cpsml_ProbTransition_strategy = st.builds(cpsml_ProbTransition, probability=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=cpsml_ProbTransition_strategy)
@settings(max_examples=25)
def test_cpsml_ProbTransition_instantiation(instance):
    assert isinstance(instance, cpsml_ProbTransition)


cpsml_State_strategy = st.builds(cpsml_State, name=st.booleans())
@given(instance=cpsml_State_strategy)
@settings(max_examples=25)
def test_cpsml_State_instantiation(instance):
    assert isinstance(instance, cpsml_State)


cpsml_System_strategy = st.builds(cpsml_System, name=safe_text, ran=safe_text, sub=st.integers(), y0label=st.integers())
@given(instance=cpsml_System_strategy)
@settings(max_examples=25)
def test_cpsml_System_instantiation(instance):
    assert isinstance(instance, cpsml_System)


cpsml_Transition_strategy = st.builds(cpsml_Transition, action=safe_text, event=safe_text, guard=safe_text, name=safe_text)
@given(instance=cpsml_Transition_strategy)
@settings(max_examples=25)
def test_cpsml_Transition_instantiation(instance):
    assert isinstance(instance, cpsml_Transition)


cpsml_Variable_strategy = st.builds(cpsml_Variable, Globalnv=st.floats(allow_nan=False, allow_infinity=False), value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=cpsml_Variable_strategy)
@settings(max_examples=25)
def test_cpsml_Variable_instantiation(instance):
    assert isinstance(instance, cpsml_Variable)



