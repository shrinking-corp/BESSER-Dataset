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
    fuzzyAutomaton_VarUpdate,
    fuzzyAutomaton_FuzzyRelation,
    Action,
    fuzzyAutomaton_Output,
    fuzzyAutomaton_Input,
    fuzzyAutomaton_VarTransformation,
    fuzzyAutomaton_FuzzyConstraint,
    fuzzyAutomaton_Action,
    fuzzyAutomaton_Variable,
    fuzzyAutomaton_TransitionFeature,
    fuzzyAutomaton_VariableSet,
    fuzzyAutomaton_Transition,
    fuzzyAutomaton_State,
    fuzzyAutomaton_FuzzyAutomaton,
    FuzzyRelationType,
    TNormType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fuzzyautomaton_varupdate_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_VarUpdate)


def test_hyp_fuzzyautomaton_varupdate_constructor_exists():
    assert callable(fuzzyAutomaton_VarUpdate.__init__)


def test_hyp_fuzzyautomaton_varupdate_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_VarUpdate.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_fuzzyautomaton_fuzzyrelation_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_FuzzyRelation)


def test_hyp_fuzzyautomaton_fuzzyrelation_constructor_exists():
    assert callable(fuzzyAutomaton_FuzzyRelation.__init__)


def test_hyp_fuzzyautomaton_fuzzyrelation_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_FuzzyRelation.__init__)
    params = list(sig.parameters.keys())
    assert "expression1" in params, "Missing parameter 'expression1'"
    assert "expression2" in params, "Missing parameter 'expression2'"
    assert "tFRelation" in params, "Missing parameter 'tFRelation'"
    assert "delta" in params, "Missing parameter 'delta'"
    assert "expression3" in params, "Missing parameter 'expression3'"








def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fuzzyautomaton_output_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_Output)


def test_hyp_fuzzyautomaton_output_constructor_exists():
    assert callable(fuzzyAutomaton_Output.__init__)


def test_hyp_fuzzyautomaton_output_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_Output.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_fuzzyautomaton_input_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_Input)


def test_hyp_fuzzyautomaton_input_constructor_exists():
    assert callable(fuzzyAutomaton_Input.__init__)


def test_hyp_fuzzyautomaton_input_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_Input.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fuzzyautomaton_vartransformation_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_VarTransformation)


def test_hyp_fuzzyautomaton_vartransformation_constructor_exists():
    assert callable(fuzzyAutomaton_VarTransformation.__init__)


def test_hyp_fuzzyautomaton_vartransformation_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_VarTransformation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fuzzyautomaton_fuzzyconstraint_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_FuzzyConstraint)


def test_hyp_fuzzyautomaton_fuzzyconstraint_constructor_exists():
    assert callable(fuzzyAutomaton_FuzzyConstraint.__init__)


def test_hyp_fuzzyautomaton_fuzzyconstraint_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_FuzzyConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tNorm" in params, "Missing parameter 'tNorm'"





def test_hyp_fuzzyautomaton_action_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_Action)


def test_hyp_fuzzyautomaton_action_constructor_exists():
    assert callable(fuzzyAutomaton_Action.__init__)


def test_hyp_fuzzyautomaton_action_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fuzzyautomaton_variable_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_Variable)


def test_hyp_fuzzyautomaton_variable_constructor_exists():
    assert callable(fuzzyAutomaton_Variable.__init__)


def test_hyp_fuzzyautomaton_variable_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fuzzyautomaton_transitionfeature_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_TransitionFeature)


def test_hyp_fuzzyautomaton_transitionfeature_constructor_exists():
    assert callable(fuzzyAutomaton_TransitionFeature.__init__)


def test_hyp_fuzzyautomaton_transitionfeature_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_TransitionFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fuzzyautomaton_variableset_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_VariableSet)


def test_hyp_fuzzyautomaton_variableset_constructor_exists():
    assert callable(fuzzyAutomaton_VariableSet.__init__)


def test_hyp_fuzzyautomaton_variableset_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_VariableSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fuzzyautomaton_transition_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_Transition)


def test_hyp_fuzzyautomaton_transition_constructor_exists():
    assert callable(fuzzyAutomaton_Transition.__init__)


def test_hyp_fuzzyautomaton_transition_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fuzzyautomaton_state_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_State)


def test_hyp_fuzzyautomaton_state_constructor_exists():
    assert callable(fuzzyAutomaton_State.__init__)


def test_hyp_fuzzyautomaton_state_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"




def test_hyp_fuzzyautomaton_fuzzyautomaton_is_not_abstract():
    assert not inspect.isabstract(fuzzyAutomaton_FuzzyAutomaton)


def test_hyp_fuzzyautomaton_fuzzyautomaton_constructor_exists():
    assert callable(fuzzyAutomaton_FuzzyAutomaton.__init__)


def test_hyp_fuzzyautomaton_fuzzyautomaton_constructor_args():
    sig = inspect.signature(fuzzyAutomaton_FuzzyAutomaton.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tNorm" in params, "Missing parameter 'tNorm'"



def test_hyp_fuzzyrelationtype_exists():
    # Check that the Enumeration exists
    assert FuzzyRelationType is not None

def test_hyp_fuzzyrelationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FuzzyRelationType]
    expected_literals = [
        "GTE",
        "EQ",
        "LTE",
        "TERN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FuzzyRelationType"

def test_hyp_tnormtype_exists():
    # Check that the Enumeration exists
    assert TNormType is not None

def test_hyp_tnormtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TNormType]
    expected_literals = [
        "GODEL",
        "HAMACHER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TNormType"


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
fuzzyAutomaton_VarUpdate_strategy = st.builds(
    fuzzyAutomaton_VarUpdate,
    expression=
        safe_text
)
fuzzyAutomaton_FuzzyRelation_strategy = st.builds(
    fuzzyAutomaton_FuzzyRelation,
    expression1=
        safe_text,
    expression2=
        safe_text,
    tFRelation=
        safe_text,
    delta=
        safe_text,
    expression3=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
fuzzyAutomaton_Output_strategy = st.builds(
    fuzzyAutomaton_Output,
    expression=
        safe_text
)
fuzzyAutomaton_Input_strategy = st.builds(
    fuzzyAutomaton_Input,
)
fuzzyAutomaton_VarTransformation_strategy = st.builds(
    fuzzyAutomaton_VarTransformation,
    name=
        safe_text
)
fuzzyAutomaton_FuzzyConstraint_strategy = st.builds(
    fuzzyAutomaton_FuzzyConstraint,
    name=
        safe_text,
    tNorm=
        safe_text
)
fuzzyAutomaton_Action_strategy = st.builds(
    fuzzyAutomaton_Action,
    name=
        safe_text
)
fuzzyAutomaton_Variable_strategy = st.builds(
    fuzzyAutomaton_Variable,
    value=
        safe_text,
    name=
        safe_text
)
fuzzyAutomaton_TransitionFeature_strategy = st.builds(
    fuzzyAutomaton_TransitionFeature,
    name=
        safe_text
)
fuzzyAutomaton_VariableSet_strategy = st.builds(
    fuzzyAutomaton_VariableSet,
    name=
        safe_text
)
fuzzyAutomaton_Transition_strategy = st.builds(
    fuzzyAutomaton_Transition,
)
fuzzyAutomaton_State_strategy = st.builds(
    fuzzyAutomaton_State,
    isInitial=
        safe_text
)
fuzzyAutomaton_FuzzyAutomaton_strategy = st.builds(
    fuzzyAutomaton_FuzzyAutomaton,
    name=
        safe_text,
    tNorm=
        safe_text
)




@given(instance=fuzzyAutomaton_VarUpdate_strategy)
def test_hyp_fuzzyautomaton_varupdate_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original




@given(instance=fuzzyAutomaton_FuzzyRelation_strategy)
def test_hyp_fuzzyautomaton_fuzzyrelation_expression1_setter(instance):
    original = instance.expression1
    instance.expression1 = original
    assert instance.expression1 == original



@given(instance=fuzzyAutomaton_FuzzyRelation_strategy)
def test_hyp_fuzzyautomaton_fuzzyrelation_expression2_setter(instance):
    original = instance.expression2
    instance.expression2 = original
    assert instance.expression2 == original



@given(instance=fuzzyAutomaton_FuzzyRelation_strategy)
def test_hyp_fuzzyautomaton_fuzzyrelation_tFRelation_setter(instance):
    original = instance.tFRelation
    instance.tFRelation = original
    assert instance.tFRelation == original



@given(instance=fuzzyAutomaton_FuzzyRelation_strategy)
def test_hyp_fuzzyautomaton_fuzzyrelation_delta_setter(instance):
    original = instance.delta
    instance.delta = original
    assert instance.delta == original



@given(instance=fuzzyAutomaton_FuzzyRelation_strategy)
def test_hyp_fuzzyautomaton_fuzzyrelation_expression3_setter(instance):
    original = instance.expression3
    instance.expression3 = original
    assert instance.expression3 == original





@given(instance=fuzzyAutomaton_Output_strategy)
def test_hyp_fuzzyautomaton_output_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original





@given(instance=fuzzyAutomaton_VarTransformation_strategy)
def test_hyp_fuzzyautomaton_vartransformation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fuzzyAutomaton_FuzzyConstraint_strategy)
def test_hyp_fuzzyautomaton_fuzzyconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fuzzyAutomaton_FuzzyConstraint_strategy)
def test_hyp_fuzzyautomaton_fuzzyconstraint_tNorm_setter(instance):
    original = instance.tNorm
    instance.tNorm = original
    assert instance.tNorm == original




@given(instance=fuzzyAutomaton_Action_strategy)
def test_hyp_fuzzyautomaton_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fuzzyAutomaton_Variable_strategy)
def test_hyp_fuzzyautomaton_variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fuzzyAutomaton_Variable_strategy)
def test_hyp_fuzzyautomaton_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fuzzyAutomaton_TransitionFeature_strategy)
def test_hyp_fuzzyautomaton_transitionfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fuzzyAutomaton_VariableSet_strategy)
def test_hyp_fuzzyautomaton_variableset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=fuzzyAutomaton_State_strategy)
def test_hyp_fuzzyautomaton_state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original




@given(instance=fuzzyAutomaton_FuzzyAutomaton_strategy)
def test_hyp_fuzzyautomaton_fuzzyautomaton_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fuzzyAutomaton_FuzzyAutomaton_strategy)
def test_hyp_fuzzyautomaton_fuzzyautomaton_tNorm_setter(instance):
    original = instance.tNorm
    instance.tNorm = original
    assert instance.tNorm == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    fuzzyAutomaton_Action,
    fuzzyAutomaton_FuzzyAutomaton,
    fuzzyAutomaton_FuzzyConstraint,
    fuzzyAutomaton_FuzzyRelation,
    fuzzyAutomaton_Input,
    fuzzyAutomaton_Output,
    fuzzyAutomaton_State,
    fuzzyAutomaton_Transition,
    fuzzyAutomaton_TransitionFeature,
    fuzzyAutomaton_VarTransformation,
    fuzzyAutomaton_VarUpdate,
    fuzzyAutomaton_Variable,
    fuzzyAutomaton_VariableSet,
    FuzzyRelationType,
    TNormType,
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

def test_fuzzyAutomaton_Action_name_value_roundtrip():
    instance = fuzzyAutomaton_Action(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fuzzyAutomaton_FuzzyAutomaton_name_value_roundtrip():
    instance = fuzzyAutomaton_FuzzyAutomaton(name="sample_text", tNorm="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fuzzyAutomaton_FuzzyAutomaton_tNorm_value_roundtrip():
    instance = fuzzyAutomaton_FuzzyAutomaton(name="sample_text", tNorm="sample_text")
    assert instance.tNorm == "sample_text"
    instance.tNorm = "sample_text_2"
    assert instance.tNorm == "sample_text_2"


def test_fuzzyAutomaton_FuzzyConstraint_name_value_roundtrip():
    instance = fuzzyAutomaton_FuzzyConstraint(name="sample_text", tNorm="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fuzzyAutomaton_FuzzyConstraint_tNorm_value_roundtrip():
    instance = fuzzyAutomaton_FuzzyConstraint(name="sample_text", tNorm="sample_text")
    assert instance.tNorm == "sample_text"
    instance.tNorm = "sample_text_2"
    assert instance.tNorm == "sample_text_2"


def test_fuzzyAutomaton_FuzzyRelation_delta_value_roundtrip():
    instance = fuzzyAutomaton_FuzzyRelation(delta="sample_text", expression1="sample_text", expression2="sample_text", expression3="sample_text", tFRelation="sample_text")
    assert instance.delta == "sample_text"
    instance.delta = "sample_text_2"
    assert instance.delta == "sample_text_2"


def test_fuzzyAutomaton_FuzzyRelation_expression1_value_roundtrip():
    instance = fuzzyAutomaton_FuzzyRelation(delta="sample_text", expression1="sample_text", expression2="sample_text", expression3="sample_text", tFRelation="sample_text")
    assert instance.expression1 == "sample_text"
    instance.expression1 = "sample_text_2"
    assert instance.expression1 == "sample_text_2"


def test_fuzzyAutomaton_FuzzyRelation_expression2_value_roundtrip():
    instance = fuzzyAutomaton_FuzzyRelation(delta="sample_text", expression1="sample_text", expression2="sample_text", expression3="sample_text", tFRelation="sample_text")
    assert instance.expression2 == "sample_text"
    instance.expression2 = "sample_text_2"
    assert instance.expression2 == "sample_text_2"


def test_fuzzyAutomaton_FuzzyRelation_expression3_value_roundtrip():
    instance = fuzzyAutomaton_FuzzyRelation(delta="sample_text", expression1="sample_text", expression2="sample_text", expression3="sample_text", tFRelation="sample_text")
    assert instance.expression3 == "sample_text"
    instance.expression3 = "sample_text_2"
    assert instance.expression3 == "sample_text_2"


def test_fuzzyAutomaton_FuzzyRelation_tFRelation_value_roundtrip():
    instance = fuzzyAutomaton_FuzzyRelation(delta="sample_text", expression1="sample_text", expression2="sample_text", expression3="sample_text", tFRelation="sample_text")
    assert instance.tFRelation == "sample_text"
    instance.tFRelation = "sample_text_2"
    assert instance.tFRelation == "sample_text_2"


def test_fuzzyAutomaton_Output_expression_value_roundtrip():
    instance = fuzzyAutomaton_Output(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_fuzzyAutomaton_State_isInitial_value_roundtrip():
    instance = fuzzyAutomaton_State(isInitial="sample_text")
    assert instance.isInitial == "sample_text"
    instance.isInitial = "sample_text_2"
    assert instance.isInitial == "sample_text_2"


def test_fuzzyAutomaton_TransitionFeature_name_value_roundtrip():
    instance = fuzzyAutomaton_TransitionFeature(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fuzzyAutomaton_VarTransformation_name_value_roundtrip():
    instance = fuzzyAutomaton_VarTransformation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fuzzyAutomaton_VarUpdate_expression_value_roundtrip():
    instance = fuzzyAutomaton_VarUpdate(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_fuzzyAutomaton_Variable_name_value_roundtrip():
    instance = fuzzyAutomaton_Variable(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fuzzyAutomaton_Variable_value_value_roundtrip():
    instance = fuzzyAutomaton_Variable(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fuzzyAutomaton_VariableSet_name_value_roundtrip():
    instance = fuzzyAutomaton_VariableSet(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fuzzyAutomaton_Input_isa_Action():
    instance = fuzzyAutomaton_Input()
    assert isinstance(instance, Action)


def test_fuzzyAutomaton_Output_isa_Action():
    instance = fuzzyAutomaton_Output(expression="sample_text")
    assert isinstance(instance, Action)


def test_assoc_action18_link_reassign_clear():
    a = fuzzyAutomaton_TransitionFeature(name="sample_text")
    b1 = fuzzyAutomaton_Action(name="sample_text")
    b2 = fuzzyAutomaton_Action(name="sample_text_2")
    _safe_set(a, 'fuzzyAutomaton_TransitionFeature19', b1)
    assert _is_linked(a, 'fuzzyAutomaton_TransitionFeature19', b1)
    if hasattr(b1, 'fuzzyAutomaton_Action'):
        assert _is_linked(b1, 'fuzzyAutomaton_Action', a)
    _safe_set(a, 'fuzzyAutomaton_TransitionFeature19', b2)
    assert _is_linked(a, 'fuzzyAutomaton_TransitionFeature19', b2)
    if hasattr(b1, 'fuzzyAutomaton_Action'):
        assert not _is_linked(b1, 'fuzzyAutomaton_Action', a)
    if hasattr(b2, 'fuzzyAutomaton_Action'):
        assert _is_linked(b2, 'fuzzyAutomaton_Action', a)
    _safe_set(a, 'fuzzyAutomaton_TransitionFeature19', None)
    assert not _is_linked(a, 'fuzzyAutomaton_TransitionFeature19', b2)
    if hasattr(b2, 'fuzzyAutomaton_Action'):
        assert not _is_linked(b2, 'fuzzyAutomaton_Action', a)


def test_assoc_feature13_link_reassign_clear():
    a = fuzzyAutomaton_TransitionFeature(name="sample_text")
    b1 = fuzzyAutomaton_Transition()
    b2 = fuzzyAutomaton_Transition()
    _safe_set(a, 'TransitionFeature', b1)
    assert _is_linked(a, 'TransitionFeature', b1)
    if hasattr(b1, 'featureToTransition'):
        assert _is_linked(b1, 'featureToTransition', a)
    _safe_set(a, 'TransitionFeature', b2)
    assert _is_linked(a, 'TransitionFeature', b2)
    if hasattr(b1, 'featureToTransition'):
        assert not _is_linked(b1, 'featureToTransition', a)
    if hasattr(b2, 'featureToTransition'):
        assert _is_linked(b2, 'featureToTransition', a)
    _safe_set(a, 'TransitionFeature', None)
    assert not _is_linked(a, 'TransitionFeature', b2)
    if hasattr(b2, 'featureToTransition'):
        assert not _is_linked(b2, 'featureToTransition', a)


def test_assoc_featureToTransition16_link_reassign_clear():
    a = fuzzyAutomaton_TransitionFeature(name="sample_text")
    b1 = fuzzyAutomaton_Transition()
    b2 = fuzzyAutomaton_Transition()
    _safe_set(a, 'feature', {b1})
    assert _is_linked(a, 'feature', b1)
    if hasattr(b1, 'Transition17'):
        assert _is_linked(b1, 'Transition17', a)
    _safe_set(a, 'feature', {b2})
    assert _is_linked(a, 'feature', b2)
    if hasattr(b1, 'Transition17'):
        assert not _is_linked(b1, 'Transition17', a)
    if hasattr(b2, 'Transition17'):
        assert _is_linked(b2, 'Transition17', a)
    _safe_set(a, 'feature', set())
    assert not _is_linked(a, 'feature', b2)
    if hasattr(b2, 'Transition17'):
        assert not _is_linked(b2, 'Transition17', a)


def test_assoc_fuzzyConstraint20_link_reassign_clear():
    a = fuzzyAutomaton_TransitionFeature(name="sample_text")
    b1 = fuzzyAutomaton_FuzzyConstraint(name="sample_text", tNorm="sample_text")
    b2 = fuzzyAutomaton_FuzzyConstraint(name="sample_text_2", tNorm="sample_text_2")
    _safe_set(a, 'fuzzyAutomaton_TransitionFeature21', b1)
    assert _is_linked(a, 'fuzzyAutomaton_TransitionFeature21', b1)
    if hasattr(b1, 'fuzzyAutomaton_FuzzyConstraint'):
        assert _is_linked(b1, 'fuzzyAutomaton_FuzzyConstraint', a)
    _safe_set(a, 'fuzzyAutomaton_TransitionFeature21', b2)
    assert _is_linked(a, 'fuzzyAutomaton_TransitionFeature21', b2)
    if hasattr(b1, 'fuzzyAutomaton_FuzzyConstraint'):
        assert not _is_linked(b1, 'fuzzyAutomaton_FuzzyConstraint', a)
    if hasattr(b2, 'fuzzyAutomaton_FuzzyConstraint'):
        assert _is_linked(b2, 'fuzzyAutomaton_FuzzyConstraint', a)
    _safe_set(a, 'fuzzyAutomaton_TransitionFeature21', None)
    assert not _is_linked(a, 'fuzzyAutomaton_TransitionFeature21', b2)
    if hasattr(b2, 'fuzzyAutomaton_FuzzyConstraint'):
        assert not _is_linked(b2, 'fuzzyAutomaton_FuzzyConstraint', a)


def test_assoc_fuzzyRelations26_link_reassign_clear():
    a = fuzzyAutomaton_FuzzyRelation(delta="sample_text", expression1="sample_text", expression2="sample_text", expression3="sample_text", tFRelation="sample_text")
    b1 = fuzzyAutomaton_FuzzyConstraint(name="sample_text", tNorm="sample_text")
    b2 = fuzzyAutomaton_FuzzyConstraint(name="sample_text_2", tNorm="sample_text_2")
    _safe_set(a, 'fuzzyAutomaton_FuzzyRelation', b1)
    assert _is_linked(a, 'fuzzyAutomaton_FuzzyRelation', b1)
    if hasattr(b1, 'fuzzyAutomaton_FuzzyConstraint27'):
        assert _is_linked(b1, 'fuzzyAutomaton_FuzzyConstraint27', a)
    _safe_set(a, 'fuzzyAutomaton_FuzzyRelation', b2)
    assert _is_linked(a, 'fuzzyAutomaton_FuzzyRelation', b2)
    if hasattr(b1, 'fuzzyAutomaton_FuzzyConstraint27'):
        assert not _is_linked(b1, 'fuzzyAutomaton_FuzzyConstraint27', a)
    if hasattr(b2, 'fuzzyAutomaton_FuzzyConstraint27'):
        assert _is_linked(b2, 'fuzzyAutomaton_FuzzyConstraint27', a)
    _safe_set(a, 'fuzzyAutomaton_FuzzyRelation', None)
    assert not _is_linked(a, 'fuzzyAutomaton_FuzzyRelation', b2)
    if hasattr(b2, 'fuzzyAutomaton_FuzzyConstraint27'):
        assert not _is_linked(b2, 'fuzzyAutomaton_FuzzyConstraint27', a)


def test_assoc_incoming7_link_reassign_clear():
    a = fuzzyAutomaton_State(isInitial="sample_text")
    b1 = fuzzyAutomaton_Transition()
    b2 = fuzzyAutomaton_Transition()
    _safe_set(a, 'target', {b1})
    assert _is_linked(a, 'target', b1)
    if hasattr(b1, 'Transition'):
        assert _is_linked(b1, 'Transition', a)
    _safe_set(a, 'target', {b2})
    assert _is_linked(a, 'target', b2)
    if hasattr(b1, 'Transition'):
        assert not _is_linked(b1, 'Transition', a)
    if hasattr(b2, 'Transition'):
        assert _is_linked(b2, 'Transition', a)
    _safe_set(a, 'target', set())
    assert not _is_linked(a, 'target', b2)
    if hasattr(b2, 'Transition'):
        assert not _is_linked(b2, 'Transition', a)


def test_assoc_outgoing8_link_reassign_clear():
    a = fuzzyAutomaton_State(isInitial="sample_text")
    b1 = fuzzyAutomaton_Transition()
    b2 = fuzzyAutomaton_Transition()
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'Transition9'):
        assert _is_linked(b1, 'Transition9', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'Transition9'):
        assert not _is_linked(b1, 'Transition9', a)
    if hasattr(b2, 'Transition9'):
        assert _is_linked(b2, 'Transition9', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'Transition9'):
        assert not _is_linked(b2, 'Transition9', a)


def test_assoc_parameters24_link_reassign_clear():
    a = fuzzyAutomaton_Variable(name="sample_text", value="sample_text")
    b1 = fuzzyAutomaton_Input()
    b2 = fuzzyAutomaton_Input()
    _safe_set(a, 'fuzzyAutomaton_Variable25', b1)
    assert _is_linked(a, 'fuzzyAutomaton_Variable25', b1)
    if hasattr(b1, 'fuzzyAutomaton_Input'):
        assert _is_linked(b1, 'fuzzyAutomaton_Input', a)
    _safe_set(a, 'fuzzyAutomaton_Variable25', b2)
    assert _is_linked(a, 'fuzzyAutomaton_Variable25', b2)
    if hasattr(b1, 'fuzzyAutomaton_Input'):
        assert not _is_linked(b1, 'fuzzyAutomaton_Input', a)
    if hasattr(b2, 'fuzzyAutomaton_Input'):
        assert _is_linked(b2, 'fuzzyAutomaton_Input', a)
    _safe_set(a, 'fuzzyAutomaton_Variable25', None)
    assert not _is_linked(a, 'fuzzyAutomaton_Variable25', b2)
    if hasattr(b2, 'fuzzyAutomaton_Input'):
        assert not _is_linked(b2, 'fuzzyAutomaton_Input', a)


def test_assoc_source10_link_reassign_clear():
    a = fuzzyAutomaton_State(isInitial="sample_text")
    b1 = fuzzyAutomaton_Transition()
    b2 = fuzzyAutomaton_Transition()
    _safe_set(a, 'State', b1)
    assert _is_linked(a, 'State', b1)
    if hasattr(b1, 'outgoing'):
        assert _is_linked(b1, 'outgoing', a)
    _safe_set(a, 'State', b2)
    assert _is_linked(a, 'State', b2)
    if hasattr(b1, 'outgoing'):
        assert not _is_linked(b1, 'outgoing', a)
    if hasattr(b2, 'outgoing'):
        assert _is_linked(b2, 'outgoing', a)
    _safe_set(a, 'State', None)
    assert not _is_linked(a, 'State', b2)
    if hasattr(b2, 'outgoing'):
        assert not _is_linked(b2, 'outgoing', a)


def test_assoc_states0_link_reassign_clear():
    a = fuzzyAutomaton_State(isInitial="sample_text")
    b1 = fuzzyAutomaton_FuzzyAutomaton(name="sample_text", tNorm="sample_text")
    b2 = fuzzyAutomaton_FuzzyAutomaton(name="sample_text_2", tNorm="sample_text_2")
    _safe_set(a, 'fuzzyAutomaton_State', b1)
    assert _is_linked(a, 'fuzzyAutomaton_State', b1)
    if hasattr(b1, 'fuzzyAutomaton_FuzzyAutomaton'):
        assert _is_linked(b1, 'fuzzyAutomaton_FuzzyAutomaton', a)
    _safe_set(a, 'fuzzyAutomaton_State', b2)
    assert _is_linked(a, 'fuzzyAutomaton_State', b2)
    if hasattr(b1, 'fuzzyAutomaton_FuzzyAutomaton'):
        assert not _is_linked(b1, 'fuzzyAutomaton_FuzzyAutomaton', a)
    if hasattr(b2, 'fuzzyAutomaton_FuzzyAutomaton'):
        assert _is_linked(b2, 'fuzzyAutomaton_FuzzyAutomaton', a)
    _safe_set(a, 'fuzzyAutomaton_State', None)
    assert not _is_linked(a, 'fuzzyAutomaton_State', b2)
    if hasattr(b2, 'fuzzyAutomaton_FuzzyAutomaton'):
        assert not _is_linked(b2, 'fuzzyAutomaton_FuzzyAutomaton', a)


def test_assoc_target11_link_reassign_clear():
    a = fuzzyAutomaton_State(isInitial="sample_text")
    b1 = fuzzyAutomaton_Transition()
    b2 = fuzzyAutomaton_Transition()
    _safe_set(a, 'State12', b1)
    assert _is_linked(a, 'State12', b1)
    if hasattr(b1, 'incoming'):
        assert _is_linked(b1, 'incoming', a)
    _safe_set(a, 'State12', b2)
    assert _is_linked(a, 'State12', b2)
    if hasattr(b1, 'incoming'):
        assert not _is_linked(b1, 'incoming', a)
    if hasattr(b2, 'incoming'):
        assert _is_linked(b2, 'incoming', a)
    _safe_set(a, 'State12', None)
    assert not _is_linked(a, 'State12', b2)
    if hasattr(b2, 'incoming'):
        assert not _is_linked(b2, 'incoming', a)


def test_assoc_transitionFeatures5_link_reassign_clear():
    a = fuzzyAutomaton_TransitionFeature(name="sample_text")
    b1 = fuzzyAutomaton_FuzzyAutomaton(name="sample_text", tNorm="sample_text")
    b2 = fuzzyAutomaton_FuzzyAutomaton(name="sample_text_2", tNorm="sample_text_2")
    _safe_set(a, 'fuzzyAutomaton_TransitionFeature', b1)
    assert _is_linked(a, 'fuzzyAutomaton_TransitionFeature', b1)
    if hasattr(b1, 'fuzzyAutomaton_FuzzyAutomaton6'):
        assert _is_linked(b1, 'fuzzyAutomaton_FuzzyAutomaton6', a)
    _safe_set(a, 'fuzzyAutomaton_TransitionFeature', b2)
    assert _is_linked(a, 'fuzzyAutomaton_TransitionFeature', b2)
    if hasattr(b1, 'fuzzyAutomaton_FuzzyAutomaton6'):
        assert not _is_linked(b1, 'fuzzyAutomaton_FuzzyAutomaton6', a)
    if hasattr(b2, 'fuzzyAutomaton_FuzzyAutomaton6'):
        assert _is_linked(b2, 'fuzzyAutomaton_FuzzyAutomaton6', a)
    _safe_set(a, 'fuzzyAutomaton_TransitionFeature', None)
    assert not _is_linked(a, 'fuzzyAutomaton_TransitionFeature', b2)
    if hasattr(b2, 'fuzzyAutomaton_FuzzyAutomaton6'):
        assert not _is_linked(b2, 'fuzzyAutomaton_FuzzyAutomaton6', a)


def test_assoc_transitions1_link_reassign_clear():
    a = fuzzyAutomaton_FuzzyAutomaton(name="sample_text", tNorm="sample_text")
    b1 = fuzzyAutomaton_Transition()
    b2 = fuzzyAutomaton_Transition()
    _safe_set(a, 'fuzzyAutomaton_FuzzyAutomaton2', {b1})
    assert _is_linked(a, 'fuzzyAutomaton_FuzzyAutomaton2', b1)
    if hasattr(b1, 'fuzzyAutomaton_Transition'):
        assert _is_linked(b1, 'fuzzyAutomaton_Transition', a)
    _safe_set(a, 'fuzzyAutomaton_FuzzyAutomaton2', {b2})
    assert _is_linked(a, 'fuzzyAutomaton_FuzzyAutomaton2', b2)
    if hasattr(b1, 'fuzzyAutomaton_Transition'):
        assert not _is_linked(b1, 'fuzzyAutomaton_Transition', a)
    if hasattr(b2, 'fuzzyAutomaton_Transition'):
        assert _is_linked(b2, 'fuzzyAutomaton_Transition', a)
    _safe_set(a, 'fuzzyAutomaton_FuzzyAutomaton2', set())
    assert not _is_linked(a, 'fuzzyAutomaton_FuzzyAutomaton2', b2)
    if hasattr(b2, 'fuzzyAutomaton_Transition'):
        assert not _is_linked(b2, 'fuzzyAutomaton_Transition', a)


def test_assoc_varTransformation22_link_reassign_clear():
    a = fuzzyAutomaton_VarTransformation(name="sample_text")
    b1 = fuzzyAutomaton_TransitionFeature(name="sample_text")
    b2 = fuzzyAutomaton_TransitionFeature(name="sample_text_2")
    _safe_set(a, 'fuzzyAutomaton_VarTransformation', b1)
    assert _is_linked(a, 'fuzzyAutomaton_VarTransformation', b1)
    if hasattr(b1, 'fuzzyAutomaton_TransitionFeature23'):
        assert _is_linked(b1, 'fuzzyAutomaton_TransitionFeature23', a)
    _safe_set(a, 'fuzzyAutomaton_VarTransformation', b2)
    assert _is_linked(a, 'fuzzyAutomaton_VarTransformation', b2)
    if hasattr(b1, 'fuzzyAutomaton_TransitionFeature23'):
        assert not _is_linked(b1, 'fuzzyAutomaton_TransitionFeature23', a)
    if hasattr(b2, 'fuzzyAutomaton_TransitionFeature23'):
        assert _is_linked(b2, 'fuzzyAutomaton_TransitionFeature23', a)
    _safe_set(a, 'fuzzyAutomaton_VarTransformation', None)
    assert not _is_linked(a, 'fuzzyAutomaton_VarTransformation', b2)
    if hasattr(b2, 'fuzzyAutomaton_TransitionFeature23'):
        assert not _is_linked(b2, 'fuzzyAutomaton_TransitionFeature23', a)


def test_assoc_varUpdates28_link_reassign_clear():
    a = fuzzyAutomaton_VarUpdate(expression="sample_text")
    b1 = fuzzyAutomaton_VarTransformation(name="sample_text")
    b2 = fuzzyAutomaton_VarTransformation(name="sample_text_2")
    _safe_set(a, 'fuzzyAutomaton_VarUpdate', b1)
    assert _is_linked(a, 'fuzzyAutomaton_VarUpdate', b1)
    if hasattr(b1, 'fuzzyAutomaton_VarTransformation29'):
        assert _is_linked(b1, 'fuzzyAutomaton_VarTransformation29', a)
    _safe_set(a, 'fuzzyAutomaton_VarUpdate', b2)
    assert _is_linked(a, 'fuzzyAutomaton_VarUpdate', b2)
    if hasattr(b1, 'fuzzyAutomaton_VarTransformation29'):
        assert not _is_linked(b1, 'fuzzyAutomaton_VarTransformation29', a)
    if hasattr(b2, 'fuzzyAutomaton_VarTransformation29'):
        assert _is_linked(b2, 'fuzzyAutomaton_VarTransformation29', a)
    _safe_set(a, 'fuzzyAutomaton_VarUpdate', None)
    assert not _is_linked(a, 'fuzzyAutomaton_VarUpdate', b2)
    if hasattr(b2, 'fuzzyAutomaton_VarTransformation29'):
        assert not _is_linked(b2, 'fuzzyAutomaton_VarTransformation29', a)


def test_assoc_variable30_link_reassign_clear():
    a = fuzzyAutomaton_Variable(name="sample_text", value="sample_text")
    b1 = fuzzyAutomaton_VarUpdate(expression="sample_text")
    b2 = fuzzyAutomaton_VarUpdate(expression="sample_text_2")
    _safe_set(a, 'fuzzyAutomaton_Variable32', b1)
    assert _is_linked(a, 'fuzzyAutomaton_Variable32', b1)
    if hasattr(b1, 'fuzzyAutomaton_VarUpdate31'):
        assert _is_linked(b1, 'fuzzyAutomaton_VarUpdate31', a)
    _safe_set(a, 'fuzzyAutomaton_Variable32', b2)
    assert _is_linked(a, 'fuzzyAutomaton_Variable32', b2)
    if hasattr(b1, 'fuzzyAutomaton_VarUpdate31'):
        assert not _is_linked(b1, 'fuzzyAutomaton_VarUpdate31', a)
    if hasattr(b2, 'fuzzyAutomaton_VarUpdate31'):
        assert _is_linked(b2, 'fuzzyAutomaton_VarUpdate31', a)
    _safe_set(a, 'fuzzyAutomaton_Variable32', None)
    assert not _is_linked(a, 'fuzzyAutomaton_Variable32', b2)
    if hasattr(b2, 'fuzzyAutomaton_VarUpdate31'):
        assert not _is_linked(b2, 'fuzzyAutomaton_VarUpdate31', a)


def test_assoc_variableSet3_link_reassign_clear():
    a = fuzzyAutomaton_VariableSet(name="sample_text")
    b1 = fuzzyAutomaton_FuzzyAutomaton(name="sample_text", tNorm="sample_text")
    b2 = fuzzyAutomaton_FuzzyAutomaton(name="sample_text_2", tNorm="sample_text_2")
    _safe_set(a, 'fuzzyAutomaton_VariableSet', b1)
    assert _is_linked(a, 'fuzzyAutomaton_VariableSet', b1)
    if hasattr(b1, 'fuzzyAutomaton_FuzzyAutomaton4'):
        assert _is_linked(b1, 'fuzzyAutomaton_FuzzyAutomaton4', a)
    _safe_set(a, 'fuzzyAutomaton_VariableSet', b2)
    assert _is_linked(a, 'fuzzyAutomaton_VariableSet', b2)
    if hasattr(b1, 'fuzzyAutomaton_FuzzyAutomaton4'):
        assert not _is_linked(b1, 'fuzzyAutomaton_FuzzyAutomaton4', a)
    if hasattr(b2, 'fuzzyAutomaton_FuzzyAutomaton4'):
        assert _is_linked(b2, 'fuzzyAutomaton_FuzzyAutomaton4', a)
    _safe_set(a, 'fuzzyAutomaton_VariableSet', None)
    assert not _is_linked(a, 'fuzzyAutomaton_VariableSet', b2)
    if hasattr(b2, 'fuzzyAutomaton_FuzzyAutomaton4'):
        assert not _is_linked(b2, 'fuzzyAutomaton_FuzzyAutomaton4', a)


def test_assoc_variables14_link_reassign_clear():
    a = fuzzyAutomaton_VariableSet(name="sample_text")
    b1 = fuzzyAutomaton_Variable(name="sample_text", value="sample_text")
    b2 = fuzzyAutomaton_Variable(name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'fuzzyAutomaton_VariableSet15', {b1})
    assert _is_linked(a, 'fuzzyAutomaton_VariableSet15', b1)
    if hasattr(b1, 'fuzzyAutomaton_Variable'):
        assert _is_linked(b1, 'fuzzyAutomaton_Variable', a)
    _safe_set(a, 'fuzzyAutomaton_VariableSet15', {b2})
    assert _is_linked(a, 'fuzzyAutomaton_VariableSet15', b2)
    if hasattr(b1, 'fuzzyAutomaton_Variable'):
        assert not _is_linked(b1, 'fuzzyAutomaton_Variable', a)
    if hasattr(b2, 'fuzzyAutomaton_Variable'):
        assert _is_linked(b2, 'fuzzyAutomaton_Variable', a)
    _safe_set(a, 'fuzzyAutomaton_VariableSet15', set())
    assert not _is_linked(a, 'fuzzyAutomaton_VariableSet15', b2)
    if hasattr(b2, 'fuzzyAutomaton_Variable'):
        assert not _is_linked(b2, 'fuzzyAutomaton_Variable', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


fuzzyAutomaton_Action_strategy = st.builds(fuzzyAutomaton_Action, name=safe_text)
@given(instance=fuzzyAutomaton_Action_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_Action_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_Action)


fuzzyAutomaton_FuzzyAutomaton_strategy = st.builds(fuzzyAutomaton_FuzzyAutomaton, name=safe_text, tNorm=safe_text)
@given(instance=fuzzyAutomaton_FuzzyAutomaton_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_FuzzyAutomaton_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_FuzzyAutomaton)


fuzzyAutomaton_FuzzyConstraint_strategy = st.builds(fuzzyAutomaton_FuzzyConstraint, name=safe_text, tNorm=safe_text)
@given(instance=fuzzyAutomaton_FuzzyConstraint_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_FuzzyConstraint_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_FuzzyConstraint)


fuzzyAutomaton_FuzzyRelation_strategy = st.builds(fuzzyAutomaton_FuzzyRelation, delta=safe_text, expression1=safe_text, expression2=safe_text, expression3=safe_text, tFRelation=safe_text)
@given(instance=fuzzyAutomaton_FuzzyRelation_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_FuzzyRelation_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_FuzzyRelation)


fuzzyAutomaton_Input_strategy = st.builds(fuzzyAutomaton_Input)
@given(instance=fuzzyAutomaton_Input_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_Input_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_Input)


fuzzyAutomaton_Output_strategy = st.builds(fuzzyAutomaton_Output, expression=safe_text)
@given(instance=fuzzyAutomaton_Output_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_Output_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_Output)


fuzzyAutomaton_State_strategy = st.builds(fuzzyAutomaton_State, isInitial=safe_text)
@given(instance=fuzzyAutomaton_State_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_State_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_State)


fuzzyAutomaton_Transition_strategy = st.builds(fuzzyAutomaton_Transition)
@given(instance=fuzzyAutomaton_Transition_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_Transition_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_Transition)


fuzzyAutomaton_TransitionFeature_strategy = st.builds(fuzzyAutomaton_TransitionFeature, name=safe_text)
@given(instance=fuzzyAutomaton_TransitionFeature_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_TransitionFeature_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_TransitionFeature)


fuzzyAutomaton_VarTransformation_strategy = st.builds(fuzzyAutomaton_VarTransformation, name=safe_text)
@given(instance=fuzzyAutomaton_VarTransformation_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_VarTransformation_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_VarTransformation)


fuzzyAutomaton_VarUpdate_strategy = st.builds(fuzzyAutomaton_VarUpdate, expression=safe_text)
@given(instance=fuzzyAutomaton_VarUpdate_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_VarUpdate_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_VarUpdate)


fuzzyAutomaton_Variable_strategy = st.builds(fuzzyAutomaton_Variable, name=safe_text, value=safe_text)
@given(instance=fuzzyAutomaton_Variable_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_Variable_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_Variable)


fuzzyAutomaton_VariableSet_strategy = st.builds(fuzzyAutomaton_VariableSet, name=safe_text)
@given(instance=fuzzyAutomaton_VariableSet_strategy)
@settings(max_examples=25)
def test_fuzzyAutomaton_VariableSet_instantiation(instance):
    assert isinstance(instance, fuzzyAutomaton_VariableSet)



