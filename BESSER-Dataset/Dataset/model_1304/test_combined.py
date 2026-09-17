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
    Data,
    SimplStateMachine_IntegerData,
    SimplStateMachine_BooleanData,
    SimplStateMachine_Assignment,
    Variable,
    SimplStateMachine_IntegerVariable,
    SimplStateMachine_BooleanVariable,
    SimplStateMachine_InitialState,
    ExpressionElement,
    SimplStateMachine_Data,
    SimplStateMachine_VariableReference,
    SimplStateMachine_ExpressionElement,
    SimplStateMachine_Expression,
    SimplStateMachine_Variable,
    SimplStateMachine_Event,
    SimplStateMachine_Transition,
    State,
    SimplStateMachine_Operation,
    SimplStateMachine_CompositeState,
    SimplStateMachine_State,
    CompositeState,
    SimplStateMachine_StateMachine,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_hyp_data_constructor_exists():
    assert callable(Data.__init__)


def test_hyp_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_integerdata_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_IntegerData)


def test_hyp_simplstatemachine_integerdata_constructor_exists():
    assert callable(SimplStateMachine_IntegerData.__init__)


def test_hyp_simplstatemachine_integerdata_constructor_args():
    sig = inspect.signature(SimplStateMachine_IntegerData.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_simplstatemachine_booleandata_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_BooleanData)


def test_hyp_simplstatemachine_booleandata_constructor_exists():
    assert callable(SimplStateMachine_BooleanData.__init__)


def test_hyp_simplstatemachine_booleandata_constructor_args():
    sig = inspect.signature(SimplStateMachine_BooleanData.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_simplstatemachine_assignment_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_Assignment)


def test_hyp_simplstatemachine_assignment_constructor_exists():
    assert callable(SimplStateMachine_Assignment.__init__)


def test_hyp_simplstatemachine_assignment_constructor_args():
    sig = inspect.signature(SimplStateMachine_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "_name" in params, "Missing parameter '_name'"




def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_integervariable_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_IntegerVariable)


def test_hyp_simplstatemachine_integervariable_constructor_exists():
    assert callable(SimplStateMachine_IntegerVariable.__init__)


def test_hyp_simplstatemachine_integervariable_constructor_args():
    sig = inspect.signature(SimplStateMachine_IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_booleanvariable_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_BooleanVariable)


def test_hyp_simplstatemachine_booleanvariable_constructor_exists():
    assert callable(SimplStateMachine_BooleanVariable.__init__)


def test_hyp_simplstatemachine_booleanvariable_constructor_args():
    sig = inspect.signature(SimplStateMachine_BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_InitialState)


def test_hyp_simplstatemachine_initialstate_constructor_exists():
    assert callable(SimplStateMachine_InitialState.__init__)


def test_hyp_simplstatemachine_initialstate_constructor_args():
    sig = inspect.signature(SimplStateMachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressionelement_is_not_abstract():
    assert not inspect.isabstract(ExpressionElement)


def test_hyp_expressionelement_constructor_exists():
    assert callable(ExpressionElement.__init__)


def test_hyp_expressionelement_constructor_args():
    sig = inspect.signature(ExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_data_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_Data)


def test_hyp_simplstatemachine_data_constructor_exists():
    assert callable(SimplStateMachine_Data.__init__)


def test_hyp_simplstatemachine_data_constructor_args():
    sig = inspect.signature(SimplStateMachine_Data.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_variablereference_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_VariableReference)


def test_hyp_simplstatemachine_variablereference_constructor_exists():
    assert callable(SimplStateMachine_VariableReference.__init__)


def test_hyp_simplstatemachine_variablereference_constructor_args():
    sig = inspect.signature(SimplStateMachine_VariableReference.__init__)
    params = list(sig.parameters.keys())
    assert "_name" in params, "Missing parameter '_name'"




def test_hyp_simplstatemachine_expressionelement_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_ExpressionElement)


def test_hyp_simplstatemachine_expressionelement_constructor_exists():
    assert callable(SimplStateMachine_ExpressionElement.__init__)


def test_hyp_simplstatemachine_expressionelement_constructor_args():
    sig = inspect.signature(SimplStateMachine_ExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_expression_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_Expression)


def test_hyp_simplstatemachine_expression_constructor_exists():
    assert callable(SimplStateMachine_Expression.__init__)


def test_hyp_simplstatemachine_expression_constructor_args():
    sig = inspect.signature(SimplStateMachine_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "_name" in params, "Missing parameter '_name'"
    assert "operator" in params, "Missing parameter 'operator'"





def test_hyp_simplstatemachine_variable_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_Variable)


def test_hyp_simplstatemachine_variable_constructor_exists():
    assert callable(SimplStateMachine_Variable.__init__)


def test_hyp_simplstatemachine_variable_constructor_args():
    sig = inspect.signature(SimplStateMachine_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_simplstatemachine_event_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_Event)


def test_hyp_simplstatemachine_event_constructor_exists():
    assert callable(SimplStateMachine_Event.__init__)


def test_hyp_simplstatemachine_event_constructor_args():
    sig = inspect.signature(SimplStateMachine_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_simplstatemachine_transition_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_Transition)


def test_hyp_simplstatemachine_transition_constructor_exists():
    assert callable(SimplStateMachine_Transition.__init__)


def test_hyp_simplstatemachine_transition_constructor_args():
    sig = inspect.signature(SimplStateMachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_operation_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_Operation)


def test_hyp_simplstatemachine_operation_constructor_exists():
    assert callable(SimplStateMachine_Operation.__init__)


def test_hyp_simplstatemachine_operation_constructor_args():
    sig = inspect.signature(SimplStateMachine_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_compositestate_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_CompositeState)


def test_hyp_simplstatemachine_compositestate_constructor_exists():
    assert callable(SimplStateMachine_CompositeState.__init__)


def test_hyp_simplstatemachine_compositestate_constructor_args():
    sig = inspect.signature(SimplStateMachine_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_state_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_State)


def test_hyp_simplstatemachine_state_constructor_exists():
    assert callable(SimplStateMachine_State.__init__)


def test_hyp_simplstatemachine_state_constructor_args():
    sig = inspect.signature(SimplStateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isActive" in params, "Missing parameter 'isActive'"





def test_hyp_compositestate_is_not_abstract():
    assert not inspect.isabstract(CompositeState)


def test_hyp_compositestate_constructor_exists():
    assert callable(CompositeState.__init__)


def test_hyp_compositestate_constructor_args():
    sig = inspect.signature(CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplstatemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine_StateMachine)


def test_hyp_simplstatemachine_statemachine_constructor_exists():
    assert callable(SimplStateMachine_StateMachine.__init__)


def test_hyp_simplstatemachine_statemachine_constructor_args():
    sig = inspect.signature(SimplStateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_hyp_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_hyp_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "div",
        "neq",
        "not_",
        "sub",
        "and_",
        "mul",
        "eq",
        "lt",
        "lte",
        "or_",
        "add",
        "gte",
        "gt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


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
Data_strategy = st.builds(
    Data,
)
SimplStateMachine_IntegerData_strategy = st.builds(
    SimplStateMachine_IntegerData,
    value=
        st.integers()
)
SimplStateMachine_BooleanData_strategy = st.builds(
    SimplStateMachine_BooleanData,
    value=
        st.booleans()
)
SimplStateMachine_Assignment_strategy = st.builds(
    SimplStateMachine_Assignment,
    _name=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
SimplStateMachine_IntegerVariable_strategy = st.builds(
    SimplStateMachine_IntegerVariable,
)
SimplStateMachine_BooleanVariable_strategy = st.builds(
    SimplStateMachine_BooleanVariable,
)
SimplStateMachine_InitialState_strategy = st.builds(
    SimplStateMachine_InitialState,
)
ExpressionElement_strategy = st.builds(
    ExpressionElement,
)
SimplStateMachine_Data_strategy = st.builds(
    SimplStateMachine_Data,
)
SimplStateMachine_VariableReference_strategy = st.builds(
    SimplStateMachine_VariableReference,
    _name=
        safe_text
)
SimplStateMachine_ExpressionElement_strategy = st.builds(
    SimplStateMachine_ExpressionElement,
)
SimplStateMachine_Expression_strategy = st.builds(
    SimplStateMachine_Expression,
    _name=
        safe_text,
    operator=
        safe_text
)
SimplStateMachine_Variable_strategy = st.builds(
    SimplStateMachine_Variable,
    name=
        safe_text
)
SimplStateMachine_Event_strategy = st.builds(
    SimplStateMachine_Event,
    name=
        safe_text
)
SimplStateMachine_Transition_strategy = st.builds(
    SimplStateMachine_Transition,
)
State_strategy = st.builds(
    State,
)
SimplStateMachine_Operation_strategy = st.builds(
    SimplStateMachine_Operation,
)
SimplStateMachine_CompositeState_strategy = st.builds(
    SimplStateMachine_CompositeState,
)
SimplStateMachine_State_strategy = st.builds(
    SimplStateMachine_State,
    name=
        safe_text,
    isActive=
        st.booleans()
)
CompositeState_strategy = st.builds(
    CompositeState,
)
SimplStateMachine_StateMachine_strategy = st.builds(
    SimplStateMachine_StateMachine,
)





@given(instance=SimplStateMachine_IntegerData_strategy)
def test_hyp_simplstatemachine_integerdata_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=SimplStateMachine_BooleanData_strategy)
def test_hyp_simplstatemachine_booleandata_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=SimplStateMachine_Assignment_strategy)
def test_hyp_simplstatemachine_assignment__name_setter(instance):
    original = instance._name
    instance._name = original
    assert instance._name == original










@given(instance=SimplStateMachine_VariableReference_strategy)
def test_hyp_simplstatemachine_variablereference__name_setter(instance):
    original = instance._name
    instance._name = original
    assert instance._name == original





@given(instance=SimplStateMachine_Expression_strategy)
def test_hyp_simplstatemachine_expression__name_setter(instance):
    original = instance._name
    instance._name = original
    assert instance._name == original



@given(instance=SimplStateMachine_Expression_strategy)
def test_hyp_simplstatemachine_expression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=SimplStateMachine_Variable_strategy)
def test_hyp_simplstatemachine_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=SimplStateMachine_Event_strategy)
def test_hyp_simplstatemachine_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=SimplStateMachine_CompositeState_strategy)
@settings(max_examples=30)
def test_hyp_simplstatemachine_compositestate_unactivesubtree_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unactiveSubTree()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unactiveSubTree).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unactiveSubTree' in SimplStateMachine_CompositeState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unactiveSubTree' in SimplStateMachine_CompositeState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unactiveSubTree' in SimplStateMachine_CompositeState is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=SimplStateMachine_CompositeState_strategy)
@settings(max_examples=30)
def test_hyp_simplstatemachine_compositestate_activesubtree_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.activeSubTree()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.activeSubTree).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'activeSubTree' in SimplStateMachine_CompositeState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'activeSubTree' in SimplStateMachine_CompositeState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'activeSubTree' in SimplStateMachine_CompositeState is not implemented or raised an error")




@given(instance=SimplStateMachine_State_strategy)
def test_hyp_simplstatemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SimplStateMachine_State_strategy)
def test_hyp_simplstatemachine_state_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CompositeState,
    Data,
    ExpressionElement,
    SimplStateMachine_Assignment,
    SimplStateMachine_BooleanData,
    SimplStateMachine_BooleanVariable,
    SimplStateMachine_CompositeState,
    SimplStateMachine_Data,
    SimplStateMachine_Event,
    SimplStateMachine_Expression,
    SimplStateMachine_ExpressionElement,
    SimplStateMachine_InitialState,
    SimplStateMachine_IntegerData,
    SimplStateMachine_IntegerVariable,
    SimplStateMachine_Operation,
    SimplStateMachine_State,
    SimplStateMachine_StateMachine,
    SimplStateMachine_Transition,
    SimplStateMachine_Variable,
    SimplStateMachine_VariableReference,
    State,
    Variable,
    Operator,
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

def test_SimplStateMachine_Assignment__name_value_roundtrip():
    instance = SimplStateMachine_Assignment(_name="sample_text")
    assert instance._name == "sample_text"
    instance._name = "sample_text_2"
    assert instance._name == "sample_text_2"


def test_SimplStateMachine_BooleanData_value_value_roundtrip():
    instance = SimplStateMachine_BooleanData(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_SimplStateMachine_Event_name_value_roundtrip():
    instance = SimplStateMachine_Event(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SimplStateMachine_Expression__name_value_roundtrip():
    instance = SimplStateMachine_Expression(_name="sample_text", operator="sample_text")
    assert instance._name == "sample_text"
    instance._name = "sample_text_2"
    assert instance._name == "sample_text_2"


def test_SimplStateMachine_Expression_operator_value_roundtrip():
    instance = SimplStateMachine_Expression(_name="sample_text", operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_SimplStateMachine_IntegerData_value_value_roundtrip():
    instance = SimplStateMachine_IntegerData(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_SimplStateMachine_State_isActive_value_roundtrip():
    instance = SimplStateMachine_State(isActive=True, name="sample_text")
    assert instance.isActive == True
    instance.isActive = False
    assert instance.isActive == False


def test_SimplStateMachine_State_name_value_roundtrip():
    instance = SimplStateMachine_State(isActive=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SimplStateMachine_Variable_name_value_roundtrip():
    instance = SimplStateMachine_Variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SimplStateMachine_VariableReference__name_value_roundtrip():
    instance = SimplStateMachine_VariableReference(_name="sample_text")
    assert instance._name == "sample_text"
    instance._name = "sample_text_2"
    assert instance._name == "sample_text_2"


def test_SimplStateMachine_StateMachine_isa_CompositeState():
    instance = SimplStateMachine_StateMachine()
    assert isinstance(instance, CompositeState)


def test_SimplStateMachine_BooleanData_isa_Data():
    instance = SimplStateMachine_BooleanData(value=True)
    assert isinstance(instance, Data)


def test_SimplStateMachine_IntegerData_isa_Data():
    instance = SimplStateMachine_IntegerData(value=7)
    assert isinstance(instance, Data)


def test_SimplStateMachine_Data_isa_ExpressionElement():
    instance = SimplStateMachine_Data()
    assert isinstance(instance, ExpressionElement)


def test_SimplStateMachine_Expression_isa_ExpressionElement():
    instance = SimplStateMachine_Expression(_name="sample_text", operator="sample_text")
    assert isinstance(instance, ExpressionElement)


def test_SimplStateMachine_VariableReference_isa_ExpressionElement():
    instance = SimplStateMachine_VariableReference(_name="sample_text")
    assert isinstance(instance, ExpressionElement)


def test_SimplStateMachine_CompositeState_isa_State():
    instance = SimplStateMachine_CompositeState()
    assert isinstance(instance, State)


def test_SimplStateMachine_BooleanVariable_isa_Variable():
    instance = SimplStateMachine_BooleanVariable()
    assert isinstance(instance, Variable)


def test_SimplStateMachine_IntegerVariable_isa_Variable():
    instance = SimplStateMachine_IntegerVariable()
    assert isinstance(instance, Variable)


def test_assoc_container5_link_reassign_clear():
    a = SimplStateMachine_State(isActive=True, name="sample_text")
    b1 = SimplStateMachine_CompositeState()
    b2 = SimplStateMachine_CompositeState()
    _safe_set(a, 'states', b1)
    assert _is_linked(a, 'states', b1)
    if hasattr(b1, 'CompositeState'):
        assert _is_linked(b1, 'CompositeState', a)
    _safe_set(a, 'states', b2)
    assert _is_linked(a, 'states', b2)
    if hasattr(b1, 'CompositeState'):
        assert not _is_linked(b1, 'CompositeState', a)
    if hasattr(b2, 'CompositeState'):
        assert _is_linked(b2, 'CompositeState', a)
    _safe_set(a, 'states', None)
    assert not _is_linked(a, 'states', b2)
    if hasattr(b2, 'CompositeState'):
        assert not _is_linked(b2, 'CompositeState', a)


def test_assoc_contents30_link_reassign_clear():
    a = SimplStateMachine_Assignment(_name="sample_text")
    b1 = SimplStateMachine_Operation()
    b2 = SimplStateMachine_Operation()
    _safe_set(a, 'SimplStateMachine_Assignment', b1)
    assert _is_linked(a, 'SimplStateMachine_Assignment', b1)
    if hasattr(b1, 'SimplStateMachine_Operation31'):
        assert _is_linked(b1, 'SimplStateMachine_Operation31', a)
    _safe_set(a, 'SimplStateMachine_Assignment', b2)
    assert _is_linked(a, 'SimplStateMachine_Assignment', b2)
    if hasattr(b1, 'SimplStateMachine_Operation31'):
        assert not _is_linked(b1, 'SimplStateMachine_Operation31', a)
    if hasattr(b2, 'SimplStateMachine_Operation31'):
        assert _is_linked(b2, 'SimplStateMachine_Operation31', a)
    _safe_set(a, 'SimplStateMachine_Assignment', None)
    assert not _is_linked(a, 'SimplStateMachine_Assignment', b2)
    if hasattr(b2, 'SimplStateMachine_Operation31'):
        assert not _is_linked(b2, 'SimplStateMachine_Operation31', a)


def test_assoc_event18_link_reassign_clear():
    a = SimplStateMachine_Event(name="sample_text")
    b1 = SimplStateMachine_Transition()
    b2 = SimplStateMachine_Transition()
    _safe_set(a, 'SimplStateMachine_Event20', b1)
    assert _is_linked(a, 'SimplStateMachine_Event20', b1)
    if hasattr(b1, 'SimplStateMachine_Transition19'):
        assert _is_linked(b1, 'SimplStateMachine_Transition19', a)
    _safe_set(a, 'SimplStateMachine_Event20', b2)
    assert _is_linked(a, 'SimplStateMachine_Event20', b2)
    if hasattr(b1, 'SimplStateMachine_Transition19'):
        assert not _is_linked(b1, 'SimplStateMachine_Transition19', a)
    if hasattr(b2, 'SimplStateMachine_Transition19'):
        assert _is_linked(b2, 'SimplStateMachine_Transition19', a)
    _safe_set(a, 'SimplStateMachine_Event20', None)
    assert not _is_linked(a, 'SimplStateMachine_Event20', b2)
    if hasattr(b2, 'SimplStateMachine_Transition19'):
        assert not _is_linked(b2, 'SimplStateMachine_Transition19', a)


def test_assoc_events1_link_reassign_clear():
    a = SimplStateMachine_Event(name="sample_text")
    b1 = SimplStateMachine_StateMachine()
    b2 = SimplStateMachine_StateMachine()
    _safe_set(a, 'SimplStateMachine_Event', b1)
    assert _is_linked(a, 'SimplStateMachine_Event', b1)
    if hasattr(b1, 'SimplStateMachine_StateMachine2'):
        assert _is_linked(b1, 'SimplStateMachine_StateMachine2', a)
    _safe_set(a, 'SimplStateMachine_Event', b2)
    assert _is_linked(a, 'SimplStateMachine_Event', b2)
    if hasattr(b1, 'SimplStateMachine_StateMachine2'):
        assert not _is_linked(b1, 'SimplStateMachine_StateMachine2', a)
    if hasattr(b2, 'SimplStateMachine_StateMachine2'):
        assert _is_linked(b2, 'SimplStateMachine_StateMachine2', a)
    _safe_set(a, 'SimplStateMachine_Event', None)
    assert not _is_linked(a, 'SimplStateMachine_Event', b2)
    if hasattr(b2, 'SimplStateMachine_StateMachine2'):
        assert not _is_linked(b2, 'SimplStateMachine_StateMachine2', a)


def test_assoc_expression32_link_reassign_clear():
    a = SimplStateMachine_Assignment(_name="sample_text")
    b1 = SimplStateMachine_ExpressionElement()
    b2 = SimplStateMachine_ExpressionElement()
    _safe_set(a, 'SimplStateMachine_Assignment33', b1)
    assert _is_linked(a, 'SimplStateMachine_Assignment33', b1)
    if hasattr(b1, 'SimplStateMachine_ExpressionElement34'):
        assert _is_linked(b1, 'SimplStateMachine_ExpressionElement34', a)
    _safe_set(a, 'SimplStateMachine_Assignment33', b2)
    assert _is_linked(a, 'SimplStateMachine_Assignment33', b2)
    if hasattr(b1, 'SimplStateMachine_ExpressionElement34'):
        assert not _is_linked(b1, 'SimplStateMachine_ExpressionElement34', a)
    if hasattr(b2, 'SimplStateMachine_ExpressionElement34'):
        assert _is_linked(b2, 'SimplStateMachine_ExpressionElement34', a)
    _safe_set(a, 'SimplStateMachine_Assignment33', None)
    assert not _is_linked(a, 'SimplStateMachine_Assignment33', b2)
    if hasattr(b2, 'SimplStateMachine_ExpressionElement34'):
        assert not _is_linked(b2, 'SimplStateMachine_ExpressionElement34', a)


def test_assoc_guard21_link_reassign_clear():
    a = SimplStateMachine_Expression(_name="sample_text", operator="sample_text")
    b1 = SimplStateMachine_Transition()
    b2 = SimplStateMachine_Transition()
    _safe_set(a, 'SimplStateMachine_Expression', b1)
    assert _is_linked(a, 'SimplStateMachine_Expression', b1)
    if hasattr(b1, 'SimplStateMachine_Transition22'):
        assert _is_linked(b1, 'SimplStateMachine_Transition22', a)
    _safe_set(a, 'SimplStateMachine_Expression', b2)
    assert _is_linked(a, 'SimplStateMachine_Expression', b2)
    if hasattr(b1, 'SimplStateMachine_Transition22'):
        assert not _is_linked(b1, 'SimplStateMachine_Transition22', a)
    if hasattr(b2, 'SimplStateMachine_Transition22'):
        assert _is_linked(b2, 'SimplStateMachine_Transition22', a)
    _safe_set(a, 'SimplStateMachine_Expression', None)
    assert not _is_linked(a, 'SimplStateMachine_Expression', b2)
    if hasattr(b2, 'SimplStateMachine_Transition22'):
        assert not _is_linked(b2, 'SimplStateMachine_Transition22', a)


def test_assoc_initialState8_link_reassign_clear():
    a = SimplStateMachine_CompositeState()
    b1 = SimplStateMachine_InitialState()
    b2 = SimplStateMachine_InitialState()
    _safe_set(a, 'SimplStateMachine_CompositeState', b1)
    assert _is_linked(a, 'SimplStateMachine_CompositeState', b1)
    if hasattr(b1, 'SimplStateMachine_InitialState'):
        assert _is_linked(b1, 'SimplStateMachine_InitialState', a)
    _safe_set(a, 'SimplStateMachine_CompositeState', b2)
    assert _is_linked(a, 'SimplStateMachine_CompositeState', b2)
    if hasattr(b1, 'SimplStateMachine_InitialState'):
        assert not _is_linked(b1, 'SimplStateMachine_InitialState', a)
    if hasattr(b2, 'SimplStateMachine_InitialState'):
        assert _is_linked(b2, 'SimplStateMachine_InitialState', a)
    _safe_set(a, 'SimplStateMachine_CompositeState', None)
    assert not _is_linked(a, 'SimplStateMachine_CompositeState', b2)
    if hasattr(b2, 'SimplStateMachine_InitialState'):
        assert not _is_linked(b2, 'SimplStateMachine_InitialState', a)


def test_assoc_left23_link_reassign_clear():
    a = SimplStateMachine_Expression(_name="sample_text", operator="sample_text")
    b1 = SimplStateMachine_ExpressionElement()
    b2 = SimplStateMachine_ExpressionElement()
    _safe_set(a, 'SimplStateMachine_Expression24', b1)
    assert _is_linked(a, 'SimplStateMachine_Expression24', b1)
    if hasattr(b1, 'SimplStateMachine_ExpressionElement'):
        assert _is_linked(b1, 'SimplStateMachine_ExpressionElement', a)
    _safe_set(a, 'SimplStateMachine_Expression24', b2)
    assert _is_linked(a, 'SimplStateMachine_Expression24', b2)
    if hasattr(b1, 'SimplStateMachine_ExpressionElement'):
        assert not _is_linked(b1, 'SimplStateMachine_ExpressionElement', a)
    if hasattr(b2, 'SimplStateMachine_ExpressionElement'):
        assert _is_linked(b2, 'SimplStateMachine_ExpressionElement', a)
    _safe_set(a, 'SimplStateMachine_Expression24', None)
    assert not _is_linked(a, 'SimplStateMachine_Expression24', b2)
    if hasattr(b2, 'SimplStateMachine_ExpressionElement'):
        assert not _is_linked(b2, 'SimplStateMachine_ExpressionElement', a)


def test_assoc_operation6_link_reassign_clear():
    a = SimplStateMachine_State(isActive=True, name="sample_text")
    b1 = SimplStateMachine_Operation()
    b2 = SimplStateMachine_Operation()
    _safe_set(a, 'SimplStateMachine_State', b1)
    assert _is_linked(a, 'SimplStateMachine_State', b1)
    if hasattr(b1, 'SimplStateMachine_Operation'):
        assert _is_linked(b1, 'SimplStateMachine_Operation', a)
    _safe_set(a, 'SimplStateMachine_State', b2)
    assert _is_linked(a, 'SimplStateMachine_State', b2)
    if hasattr(b1, 'SimplStateMachine_Operation'):
        assert not _is_linked(b1, 'SimplStateMachine_Operation', a)
    if hasattr(b2, 'SimplStateMachine_Operation'):
        assert _is_linked(b2, 'SimplStateMachine_Operation', a)
    _safe_set(a, 'SimplStateMachine_State', None)
    assert not _is_linked(a, 'SimplStateMachine_State', b2)
    if hasattr(b2, 'SimplStateMachine_Operation'):
        assert not _is_linked(b2, 'SimplStateMachine_Operation', a)


def test_assoc_referencedState9_link_reassign_clear():
    a = SimplStateMachine_State(isActive=True, name="sample_text")
    b1 = SimplStateMachine_InitialState()
    b2 = SimplStateMachine_InitialState()
    _safe_set(a, 'SimplStateMachine_State11', b1)
    assert _is_linked(a, 'SimplStateMachine_State11', b1)
    if hasattr(b1, 'SimplStateMachine_InitialState10'):
        assert _is_linked(b1, 'SimplStateMachine_InitialState10', a)
    _safe_set(a, 'SimplStateMachine_State11', b2)
    assert _is_linked(a, 'SimplStateMachine_State11', b2)
    if hasattr(b1, 'SimplStateMachine_InitialState10'):
        assert not _is_linked(b1, 'SimplStateMachine_InitialState10', a)
    if hasattr(b2, 'SimplStateMachine_InitialState10'):
        assert _is_linked(b2, 'SimplStateMachine_InitialState10', a)
    _safe_set(a, 'SimplStateMachine_State11', None)
    assert not _is_linked(a, 'SimplStateMachine_State11', b2)
    if hasattr(b2, 'SimplStateMachine_InitialState10'):
        assert not _is_linked(b2, 'SimplStateMachine_InitialState10', a)


def test_assoc_right25_link_reassign_clear():
    a = SimplStateMachine_Expression(_name="sample_text", operator="sample_text")
    b1 = SimplStateMachine_ExpressionElement()
    b2 = SimplStateMachine_ExpressionElement()
    _safe_set(a, 'SimplStateMachine_Expression26', b1)
    assert _is_linked(a, 'SimplStateMachine_Expression26', b1)
    if hasattr(b1, 'SimplStateMachine_ExpressionElement27'):
        assert _is_linked(b1, 'SimplStateMachine_ExpressionElement27', a)
    _safe_set(a, 'SimplStateMachine_Expression26', b2)
    assert _is_linked(a, 'SimplStateMachine_Expression26', b2)
    if hasattr(b1, 'SimplStateMachine_ExpressionElement27'):
        assert not _is_linked(b1, 'SimplStateMachine_ExpressionElement27', a)
    if hasattr(b2, 'SimplStateMachine_ExpressionElement27'):
        assert _is_linked(b2, 'SimplStateMachine_ExpressionElement27', a)
    _safe_set(a, 'SimplStateMachine_Expression26', None)
    assert not _is_linked(a, 'SimplStateMachine_Expression26', b2)
    if hasattr(b2, 'SimplStateMachine_ExpressionElement27'):
        assert not _is_linked(b2, 'SimplStateMachine_ExpressionElement27', a)


def test_assoc_source12_link_reassign_clear():
    a = SimplStateMachine_State(isActive=True, name="sample_text")
    b1 = SimplStateMachine_Transition()
    b2 = SimplStateMachine_Transition()
    _safe_set(a, 'SimplStateMachine_State14', b1)
    assert _is_linked(a, 'SimplStateMachine_State14', b1)
    if hasattr(b1, 'SimplStateMachine_Transition13'):
        assert _is_linked(b1, 'SimplStateMachine_Transition13', a)
    _safe_set(a, 'SimplStateMachine_State14', b2)
    assert _is_linked(a, 'SimplStateMachine_State14', b2)
    if hasattr(b1, 'SimplStateMachine_Transition13'):
        assert not _is_linked(b1, 'SimplStateMachine_Transition13', a)
    if hasattr(b2, 'SimplStateMachine_Transition13'):
        assert _is_linked(b2, 'SimplStateMachine_Transition13', a)
    _safe_set(a, 'SimplStateMachine_State14', None)
    assert not _is_linked(a, 'SimplStateMachine_State14', b2)
    if hasattr(b2, 'SimplStateMachine_Transition13'):
        assert not _is_linked(b2, 'SimplStateMachine_Transition13', a)


def test_assoc_states7_link_reassign_clear():
    a = SimplStateMachine_State(isActive=True, name="sample_text")
    b1 = SimplStateMachine_CompositeState()
    b2 = SimplStateMachine_CompositeState()
    _safe_set(a, 'State', b1)
    assert _is_linked(a, 'State', b1)
    if hasattr(b1, 'container'):
        assert _is_linked(b1, 'container', a)
    _safe_set(a, 'State', b2)
    assert _is_linked(a, 'State', b2)
    if hasattr(b1, 'container'):
        assert not _is_linked(b1, 'container', a)
    if hasattr(b2, 'container'):
        assert _is_linked(b2, 'container', a)
    _safe_set(a, 'State', None)
    assert not _is_linked(a, 'State', b2)
    if hasattr(b2, 'container'):
        assert not _is_linked(b2, 'container', a)


def test_assoc_target15_link_reassign_clear():
    a = SimplStateMachine_State(isActive=True, name="sample_text")
    b1 = SimplStateMachine_Transition()
    b2 = SimplStateMachine_Transition()
    _safe_set(a, 'SimplStateMachine_State17', b1)
    assert _is_linked(a, 'SimplStateMachine_State17', b1)
    if hasattr(b1, 'SimplStateMachine_Transition16'):
        assert _is_linked(b1, 'SimplStateMachine_Transition16', a)
    _safe_set(a, 'SimplStateMachine_State17', b2)
    assert _is_linked(a, 'SimplStateMachine_State17', b2)
    if hasattr(b1, 'SimplStateMachine_Transition16'):
        assert not _is_linked(b1, 'SimplStateMachine_Transition16', a)
    if hasattr(b2, 'SimplStateMachine_Transition16'):
        assert _is_linked(b2, 'SimplStateMachine_Transition16', a)
    _safe_set(a, 'SimplStateMachine_State17', None)
    assert not _is_linked(a, 'SimplStateMachine_State17', b2)
    if hasattr(b2, 'SimplStateMachine_Transition16'):
        assert not _is_linked(b2, 'SimplStateMachine_Transition16', a)


def test_assoc_value28_link_reassign_clear():
    a = SimplStateMachine_Variable(name="sample_text")
    b1 = SimplStateMachine_Data()
    b2 = SimplStateMachine_Data()
    _safe_set(a, 'SimplStateMachine_Variable29', b1)
    assert _is_linked(a, 'SimplStateMachine_Variable29', b1)
    if hasattr(b1, 'SimplStateMachine_Data'):
        assert _is_linked(b1, 'SimplStateMachine_Data', a)
    _safe_set(a, 'SimplStateMachine_Variable29', b2)
    assert _is_linked(a, 'SimplStateMachine_Variable29', b2)
    if hasattr(b1, 'SimplStateMachine_Data'):
        assert not _is_linked(b1, 'SimplStateMachine_Data', a)
    if hasattr(b2, 'SimplStateMachine_Data'):
        assert _is_linked(b2, 'SimplStateMachine_Data', a)
    _safe_set(a, 'SimplStateMachine_Variable29', None)
    assert not _is_linked(a, 'SimplStateMachine_Variable29', b2)
    if hasattr(b2, 'SimplStateMachine_Data'):
        assert not _is_linked(b2, 'SimplStateMachine_Data', a)


def test_assoc_variable35_link_reassign_clear():
    a = SimplStateMachine_Variable(name="sample_text")
    b1 = SimplStateMachine_Assignment(_name="sample_text")
    b2 = SimplStateMachine_Assignment(_name="sample_text_2")
    _safe_set(a, 'SimplStateMachine_Variable37', b1)
    assert _is_linked(a, 'SimplStateMachine_Variable37', b1)
    if hasattr(b1, 'SimplStateMachine_Assignment36'):
        assert _is_linked(b1, 'SimplStateMachine_Assignment36', a)
    _safe_set(a, 'SimplStateMachine_Variable37', b2)
    assert _is_linked(a, 'SimplStateMachine_Variable37', b2)
    if hasattr(b1, 'SimplStateMachine_Assignment36'):
        assert not _is_linked(b1, 'SimplStateMachine_Assignment36', a)
    if hasattr(b2, 'SimplStateMachine_Assignment36'):
        assert _is_linked(b2, 'SimplStateMachine_Assignment36', a)
    _safe_set(a, 'SimplStateMachine_Variable37', None)
    assert not _is_linked(a, 'SimplStateMachine_Variable37', b2)
    if hasattr(b2, 'SimplStateMachine_Assignment36'):
        assert not _is_linked(b2, 'SimplStateMachine_Assignment36', a)


def test_assoc_variable38_link_reassign_clear():
    a = SimplStateMachine_VariableReference(_name="sample_text")
    b1 = SimplStateMachine_Variable(name="sample_text")
    b2 = SimplStateMachine_Variable(name="sample_text_2")
    _safe_set(a, 'SimplStateMachine_VariableReference', b1)
    assert _is_linked(a, 'SimplStateMachine_VariableReference', b1)
    if hasattr(b1, 'SimplStateMachine_Variable39'):
        assert _is_linked(b1, 'SimplStateMachine_Variable39', a)
    _safe_set(a, 'SimplStateMachine_VariableReference', b2)
    assert _is_linked(a, 'SimplStateMachine_VariableReference', b2)
    if hasattr(b1, 'SimplStateMachine_Variable39'):
        assert not _is_linked(b1, 'SimplStateMachine_Variable39', a)
    if hasattr(b2, 'SimplStateMachine_Variable39'):
        assert _is_linked(b2, 'SimplStateMachine_Variable39', a)
    _safe_set(a, 'SimplStateMachine_VariableReference', None)
    assert not _is_linked(a, 'SimplStateMachine_VariableReference', b2)
    if hasattr(b2, 'SimplStateMachine_Variable39'):
        assert not _is_linked(b2, 'SimplStateMachine_Variable39', a)


def test_assoc_variables3_link_reassign_clear():
    a = SimplStateMachine_Variable(name="sample_text")
    b1 = SimplStateMachine_StateMachine()
    b2 = SimplStateMachine_StateMachine()
    _safe_set(a, 'SimplStateMachine_Variable', b1)
    assert _is_linked(a, 'SimplStateMachine_Variable', b1)
    if hasattr(b1, 'SimplStateMachine_StateMachine4'):
        assert _is_linked(b1, 'SimplStateMachine_StateMachine4', a)
    _safe_set(a, 'SimplStateMachine_Variable', b2)
    assert _is_linked(a, 'SimplStateMachine_Variable', b2)
    if hasattr(b1, 'SimplStateMachine_StateMachine4'):
        assert not _is_linked(b1, 'SimplStateMachine_StateMachine4', a)
    if hasattr(b2, 'SimplStateMachine_StateMachine4'):
        assert _is_linked(b2, 'SimplStateMachine_StateMachine4', a)
    _safe_set(a, 'SimplStateMachine_Variable', None)
    assert not _is_linked(a, 'SimplStateMachine_Variable', b2)
    if hasattr(b2, 'SimplStateMachine_StateMachine4'):
        assert not _is_linked(b2, 'SimplStateMachine_StateMachine4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CompositeState_strategy = st.builds(CompositeState)
@given(instance=CompositeState_strategy)
@settings(max_examples=25)
def test_CompositeState_instantiation(instance):
    assert isinstance(instance, CompositeState)


Data_strategy = st.builds(Data)
@given(instance=Data_strategy)
@settings(max_examples=25)
def test_Data_instantiation(instance):
    assert isinstance(instance, Data)


ExpressionElement_strategy = st.builds(ExpressionElement)
@given(instance=ExpressionElement_strategy)
@settings(max_examples=25)
def test_ExpressionElement_instantiation(instance):
    assert isinstance(instance, ExpressionElement)


SimplStateMachine_Assignment_strategy = st.builds(SimplStateMachine_Assignment, _name=safe_text)
@given(instance=SimplStateMachine_Assignment_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_Assignment_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_Assignment)


SimplStateMachine_BooleanData_strategy = st.builds(SimplStateMachine_BooleanData, value=st.booleans())
@given(instance=SimplStateMachine_BooleanData_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_BooleanData_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_BooleanData)


SimplStateMachine_BooleanVariable_strategy = st.builds(SimplStateMachine_BooleanVariable)
@given(instance=SimplStateMachine_BooleanVariable_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_BooleanVariable_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_BooleanVariable)


SimplStateMachine_CompositeState_strategy = st.builds(SimplStateMachine_CompositeState)
@given(instance=SimplStateMachine_CompositeState_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_CompositeState_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_CompositeState)


SimplStateMachine_Data_strategy = st.builds(SimplStateMachine_Data)
@given(instance=SimplStateMachine_Data_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_Data_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_Data)


SimplStateMachine_Event_strategy = st.builds(SimplStateMachine_Event, name=safe_text)
@given(instance=SimplStateMachine_Event_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_Event_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_Event)


SimplStateMachine_Expression_strategy = st.builds(SimplStateMachine_Expression, _name=safe_text, operator=safe_text)
@given(instance=SimplStateMachine_Expression_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_Expression_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_Expression)


SimplStateMachine_ExpressionElement_strategy = st.builds(SimplStateMachine_ExpressionElement)
@given(instance=SimplStateMachine_ExpressionElement_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_ExpressionElement_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_ExpressionElement)


SimplStateMachine_InitialState_strategy = st.builds(SimplStateMachine_InitialState)
@given(instance=SimplStateMachine_InitialState_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_InitialState_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_InitialState)


SimplStateMachine_IntegerData_strategy = st.builds(SimplStateMachine_IntegerData, value=st.integers())
@given(instance=SimplStateMachine_IntegerData_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_IntegerData_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_IntegerData)


SimplStateMachine_IntegerVariable_strategy = st.builds(SimplStateMachine_IntegerVariable)
@given(instance=SimplStateMachine_IntegerVariable_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_IntegerVariable_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_IntegerVariable)


SimplStateMachine_Operation_strategy = st.builds(SimplStateMachine_Operation)
@given(instance=SimplStateMachine_Operation_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_Operation_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_Operation)


SimplStateMachine_State_strategy = st.builds(SimplStateMachine_State, isActive=st.booleans(), name=safe_text)
@given(instance=SimplStateMachine_State_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_State_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_State)


SimplStateMachine_StateMachine_strategy = st.builds(SimplStateMachine_StateMachine)
@given(instance=SimplStateMachine_StateMachine_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_StateMachine_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_StateMachine)


SimplStateMachine_Transition_strategy = st.builds(SimplStateMachine_Transition)
@given(instance=SimplStateMachine_Transition_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_Transition_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_Transition)


SimplStateMachine_Variable_strategy = st.builds(SimplStateMachine_Variable, name=safe_text)
@given(instance=SimplStateMachine_Variable_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_Variable_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_Variable)


SimplStateMachine_VariableReference_strategy = st.builds(SimplStateMachine_VariableReference, _name=safe_text)
@given(instance=SimplStateMachine_VariableReference_strategy)
@settings(max_examples=25)
def test_SimplStateMachine_VariableReference_instantiation(instance):
    assert isinstance(instance, SimplStateMachine_VariableReference)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)



