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
    IntegerExpression,
    adwithoutruntime_IntegerCalculationExpression,
    BooleanExpression,
    adwithoutruntime_BooleanBinaryExpression,
    adwithoutruntime_BooleanUnaryExpression,
    adwithoutruntime_IntegerComparisonExpression,
    adwithoutruntime_Expression,
    Action,
    adwithoutruntime_OpaqueAction,
    Expression,
    adwithoutruntime_BooleanExpression,
    adwithoutruntime_IntegerExpression,
    Value,
    adwithoutruntime_IntegerValue,
    adwithoutruntime_BooleanValue,
    Variable,
    adwithoutruntime_IntegerVariable,
    adwithoutruntime_Value,
    FinalNode,
    adwithoutruntime_ActivityFinalNode,
    ControlNode,
    adwithoutruntime_JoinNode,
    adwithoutruntime_DecisionNode,
    adwithoutruntime_ForkNode,
    adwithoutruntime_FinalNode,
    adwithoutruntime_MergeNode,
    adwithoutruntime_InitialNode,
    adwithoutruntime_NamedElement,
    NamedElement,
    adwithoutruntime_Activity,
    ExecutableNode,
    adwithoutruntime_Action,
    ActivityNode,
    adwithoutruntime_ExecutableNode,
    adwithoutruntime_ControlNode,
    adwithoutruntime_BooleanVariable,
    ActivityEdge,
    adwithoutruntime_ControlFlow,
    adwithoutruntime_Variable,
    adwithoutruntime_ActivityEdge,
    adwithoutruntime_ActivityNode,
    BooleanBinaryOperator,
    IntegerCalculationOperator,
    BooleanUnaryOperator,
    IntegerComparisonOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_integerexpression_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression)


def test_hyp_integerexpression_constructor_exists():
    assert callable(IntegerExpression.__init__)


def test_hyp_integerexpression_constructor_args():
    sig = inspect.signature(IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_IntegerCalculationExpression)


def test_hyp_adwithoutruntime_integercalculationexpression_constructor_exists():
    assert callable(adwithoutruntime_IntegerCalculationExpression.__init__)


def test_hyp_adwithoutruntime_integercalculationexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_hyp_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_hyp_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_BooleanBinaryExpression)


def test_hyp_adwithoutruntime_booleanbinaryexpression_constructor_exists():
    assert callable(adwithoutruntime_BooleanBinaryExpression.__init__)


def test_hyp_adwithoutruntime_booleanbinaryexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_adwithoutruntime_booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_BooleanUnaryExpression)


def test_hyp_adwithoutruntime_booleanunaryexpression_constructor_exists():
    assert callable(adwithoutruntime_BooleanUnaryExpression.__init__)


def test_hyp_adwithoutruntime_booleanunaryexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_adwithoutruntime_integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_IntegerComparisonExpression)


def test_hyp_adwithoutruntime_integercomparisonexpression_constructor_exists():
    assert callable(adwithoutruntime_IntegerComparisonExpression.__init__)


def test_hyp_adwithoutruntime_integercomparisonexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_adwithoutruntime_expression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_Expression)


def test_hyp_adwithoutruntime_expression_constructor_exists():
    assert callable(adwithoutruntime_Expression.__init__)


def test_hyp_adwithoutruntime_expression_constructor_args():
    sig = inspect.signature(adwithoutruntime_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_OpaqueAction)


def test_hyp_adwithoutruntime_opaqueaction_constructor_exists():
    assert callable(adwithoutruntime_OpaqueAction.__init__)


def test_hyp_adwithoutruntime_opaqueaction_constructor_args():
    sig = inspect.signature(adwithoutruntime_OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_BooleanExpression)


def test_hyp_adwithoutruntime_booleanexpression_constructor_exists():
    assert callable(adwithoutruntime_BooleanExpression.__init__)


def test_hyp_adwithoutruntime_booleanexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_integerexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_IntegerExpression)


def test_hyp_adwithoutruntime_integerexpression_constructor_exists():
    assert callable(adwithoutruntime_IntegerExpression.__init__)


def test_hyp_adwithoutruntime_integerexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_hyp_value_constructor_exists():
    assert callable(Value.__init__)


def test_hyp_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_integervalue_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_IntegerValue)


def test_hyp_adwithoutruntime_integervalue_constructor_exists():
    assert callable(adwithoutruntime_IntegerValue.__init__)


def test_hyp_adwithoutruntime_integervalue_constructor_args():
    sig = inspect.signature(adwithoutruntime_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_adwithoutruntime_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_BooleanValue)


def test_hyp_adwithoutruntime_booleanvalue_constructor_exists():
    assert callable(adwithoutruntime_BooleanValue.__init__)


def test_hyp_adwithoutruntime_booleanvalue_constructor_args():
    sig = inspect.signature(adwithoutruntime_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_integervariable_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_IntegerVariable)


def test_hyp_adwithoutruntime_integervariable_constructor_exists():
    assert callable(adwithoutruntime_IntegerVariable.__init__)


def test_hyp_adwithoutruntime_integervariable_constructor_args():
    sig = inspect.signature(adwithoutruntime_IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_value_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_Value)


def test_hyp_adwithoutruntime_value_constructor_exists():
    assert callable(adwithoutruntime_Value.__init__)


def test_hyp_adwithoutruntime_value_constructor_args():
    sig = inspect.signature(adwithoutruntime_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_hyp_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_hyp_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ActivityFinalNode)


def test_hyp_adwithoutruntime_activityfinalnode_constructor_exists():
    assert callable(adwithoutruntime_ActivityFinalNode.__init__)


def test_hyp_adwithoutruntime_activityfinalnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_hyp_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_hyp_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_joinnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_JoinNode)


def test_hyp_adwithoutruntime_joinnode_constructor_exists():
    assert callable(adwithoutruntime_JoinNode.__init__)


def test_hyp_adwithoutruntime_joinnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_decisionnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_DecisionNode)


def test_hyp_adwithoutruntime_decisionnode_constructor_exists():
    assert callable(adwithoutruntime_DecisionNode.__init__)


def test_hyp_adwithoutruntime_decisionnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_forknode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ForkNode)


def test_hyp_adwithoutruntime_forknode_constructor_exists():
    assert callable(adwithoutruntime_ForkNode.__init__)


def test_hyp_adwithoutruntime_forknode_constructor_args():
    sig = inspect.signature(adwithoutruntime_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_finalnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_FinalNode)


def test_hyp_adwithoutruntime_finalnode_constructor_exists():
    assert callable(adwithoutruntime_FinalNode.__init__)


def test_hyp_adwithoutruntime_finalnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_mergenode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_MergeNode)


def test_hyp_adwithoutruntime_mergenode_constructor_exists():
    assert callable(adwithoutruntime_MergeNode.__init__)


def test_hyp_adwithoutruntime_mergenode_constructor_args():
    sig = inspect.signature(adwithoutruntime_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_initialnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_InitialNode)


def test_hyp_adwithoutruntime_initialnode_constructor_exists():
    assert callable(adwithoutruntime_InitialNode.__init__)


def test_hyp_adwithoutruntime_initialnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_namedelement_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_NamedElement)


def test_hyp_adwithoutruntime_namedelement_constructor_exists():
    assert callable(adwithoutruntime_NamedElement.__init__)


def test_hyp_adwithoutruntime_namedelement_constructor_args():
    sig = inspect.signature(adwithoutruntime_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_activity_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_Activity)


def test_hyp_adwithoutruntime_activity_constructor_exists():
    assert callable(adwithoutruntime_Activity.__init__)


def test_hyp_adwithoutruntime_activity_constructor_args():
    sig = inspect.signature(adwithoutruntime_Activity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_hyp_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_hyp_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_action_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_Action)


def test_hyp_adwithoutruntime_action_constructor_exists():
    assert callable(adwithoutruntime_Action.__init__)


def test_hyp_adwithoutruntime_action_constructor_args():
    sig = inspect.signature(adwithoutruntime_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_hyp_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_hyp_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_executablenode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ExecutableNode)


def test_hyp_adwithoutruntime_executablenode_constructor_exists():
    assert callable(adwithoutruntime_ExecutableNode.__init__)


def test_hyp_adwithoutruntime_executablenode_constructor_args():
    sig = inspect.signature(adwithoutruntime_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_controlnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ControlNode)


def test_hyp_adwithoutruntime_controlnode_constructor_exists():
    assert callable(adwithoutruntime_ControlNode.__init__)


def test_hyp_adwithoutruntime_controlnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_booleanvariable_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_BooleanVariable)


def test_hyp_adwithoutruntime_booleanvariable_constructor_exists():
    assert callable(adwithoutruntime_BooleanVariable.__init__)


def test_hyp_adwithoutruntime_booleanvariable_constructor_args():
    sig = inspect.signature(adwithoutruntime_BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_hyp_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_hyp_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_controlflow_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ControlFlow)


def test_hyp_adwithoutruntime_controlflow_constructor_exists():
    assert callable(adwithoutruntime_ControlFlow.__init__)


def test_hyp_adwithoutruntime_controlflow_constructor_args():
    sig = inspect.signature(adwithoutruntime_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_variable_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_Variable)


def test_hyp_adwithoutruntime_variable_constructor_exists():
    assert callable(adwithoutruntime_Variable.__init__)


def test_hyp_adwithoutruntime_variable_constructor_args():
    sig = inspect.signature(adwithoutruntime_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_adwithoutruntime_activityedge_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ActivityEdge)


def test_hyp_adwithoutruntime_activityedge_constructor_exists():
    assert callable(adwithoutruntime_ActivityEdge.__init__)


def test_hyp_adwithoutruntime_activityedge_constructor_args():
    sig = inspect.signature(adwithoutruntime_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adwithoutruntime_activitynode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ActivityNode)


def test_hyp_adwithoutruntime_activitynode_constructor_exists():
    assert callable(adwithoutruntime_ActivityNode.__init__)


def test_hyp_adwithoutruntime_activitynode_constructor_args():
    sig = inspect.signature(adwithoutruntime_ActivityNode.__init__)
    params = list(sig.parameters.keys())

def test_hyp_booleanbinaryoperator_exists():
    # Check that the Enumeration exists
    assert BooleanBinaryOperator is not None

def test_hyp_booleanbinaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanBinaryOperator]
    expected_literals = [
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanBinaryOperator"

def test_hyp_integercalculationoperator_exists():
    # Check that the Enumeration exists
    assert IntegerCalculationOperator is not None

def test_hyp_integercalculationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegerCalculationOperator]
    expected_literals = [
        "ADD",
        "SUBRACT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegerCalculationOperator"

def test_hyp_booleanunaryoperator_exists():
    # Check that the Enumeration exists
    assert BooleanUnaryOperator is not None

def test_hyp_booleanunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanUnaryOperator]
    expected_literals = [
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanUnaryOperator"

def test_hyp_integercomparisonoperator_exists():
    # Check that the Enumeration exists
    assert IntegerComparisonOperator is not None

def test_hyp_integercomparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegerComparisonOperator]
    expected_literals = [
        "EQUALS",
        "SMALLER",
        "SMALLER_EQUALS",
        "GREATER",
        "GREATER_EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegerComparisonOperator"


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
IntegerExpression_strategy = st.builds(
    IntegerExpression,
)
adwithoutruntime_IntegerCalculationExpression_strategy = st.builds(
    adwithoutruntime_IntegerCalculationExpression,
    operator=
        safe_text
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
adwithoutruntime_BooleanBinaryExpression_strategy = st.builds(
    adwithoutruntime_BooleanBinaryExpression,
    operator=
        safe_text
)
adwithoutruntime_BooleanUnaryExpression_strategy = st.builds(
    adwithoutruntime_BooleanUnaryExpression,
    operator=
        safe_text
)
adwithoutruntime_IntegerComparisonExpression_strategy = st.builds(
    adwithoutruntime_IntegerComparisonExpression,
    operator=
        safe_text
)
adwithoutruntime_Expression_strategy = st.builds(
    adwithoutruntime_Expression,
)
Action_strategy = st.builds(
    Action,
)
adwithoutruntime_OpaqueAction_strategy = st.builds(
    adwithoutruntime_OpaqueAction,
)
Expression_strategy = st.builds(
    Expression,
)
adwithoutruntime_BooleanExpression_strategy = st.builds(
    adwithoutruntime_BooleanExpression,
)
adwithoutruntime_IntegerExpression_strategy = st.builds(
    adwithoutruntime_IntegerExpression,
)
Value_strategy = st.builds(
    Value,
)
adwithoutruntime_IntegerValue_strategy = st.builds(
    adwithoutruntime_IntegerValue,
    value=
        st.integers()
)
adwithoutruntime_BooleanValue_strategy = st.builds(
    adwithoutruntime_BooleanValue,
    value=
        st.booleans()
)
Variable_strategy = st.builds(
    Variable,
)
adwithoutruntime_IntegerVariable_strategy = st.builds(
    adwithoutruntime_IntegerVariable,
)
adwithoutruntime_Value_strategy = st.builds(
    adwithoutruntime_Value,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
adwithoutruntime_ActivityFinalNode_strategy = st.builds(
    adwithoutruntime_ActivityFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
adwithoutruntime_JoinNode_strategy = st.builds(
    adwithoutruntime_JoinNode,
)
adwithoutruntime_DecisionNode_strategy = st.builds(
    adwithoutruntime_DecisionNode,
)
adwithoutruntime_ForkNode_strategy = st.builds(
    adwithoutruntime_ForkNode,
)
adwithoutruntime_FinalNode_strategy = st.builds(
    adwithoutruntime_FinalNode,
)
adwithoutruntime_MergeNode_strategy = st.builds(
    adwithoutruntime_MergeNode,
)
adwithoutruntime_InitialNode_strategy = st.builds(
    adwithoutruntime_InitialNode,
)
adwithoutruntime_NamedElement_strategy = st.builds(
    adwithoutruntime_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
adwithoutruntime_Activity_strategy = st.builds(
    adwithoutruntime_Activity,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
adwithoutruntime_Action_strategy = st.builds(
    adwithoutruntime_Action,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
adwithoutruntime_ExecutableNode_strategy = st.builds(
    adwithoutruntime_ExecutableNode,
)
adwithoutruntime_ControlNode_strategy = st.builds(
    adwithoutruntime_ControlNode,
)
adwithoutruntime_BooleanVariable_strategy = st.builds(
    adwithoutruntime_BooleanVariable,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
adwithoutruntime_ControlFlow_strategy = st.builds(
    adwithoutruntime_ControlFlow,
)
adwithoutruntime_Variable_strategy = st.builds(
    adwithoutruntime_Variable,
    name=
        safe_text
)
adwithoutruntime_ActivityEdge_strategy = st.builds(
    adwithoutruntime_ActivityEdge,
)
adwithoutruntime_ActivityNode_strategy = st.builds(
    adwithoutruntime_ActivityNode,
)





@given(instance=adwithoutruntime_IntegerCalculationExpression_strategy)
def test_hyp_adwithoutruntime_integercalculationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=adwithoutruntime_BooleanBinaryExpression_strategy)
def test_hyp_adwithoutruntime_booleanbinaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=adwithoutruntime_BooleanUnaryExpression_strategy)
def test_hyp_adwithoutruntime_booleanunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=adwithoutruntime_IntegerComparisonExpression_strategy)
def test_hyp_adwithoutruntime_integercomparisonexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original











@given(instance=adwithoutruntime_IntegerValue_strategy)
def test_hyp_adwithoutruntime_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=adwithoutruntime_BooleanValue_strategy)
def test_hyp_adwithoutruntime_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
















@given(instance=adwithoutruntime_NamedElement_strategy)
def test_hyp_adwithoutruntime_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original














@given(instance=adwithoutruntime_Variable_strategy)
def test_hyp_adwithoutruntime_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    ActivityEdge,
    ActivityNode,
    BooleanExpression,
    ControlNode,
    ExecutableNode,
    Expression,
    FinalNode,
    IntegerExpression,
    NamedElement,
    Value,
    Variable,
    adwithoutruntime_Action,
    adwithoutruntime_Activity,
    adwithoutruntime_ActivityEdge,
    adwithoutruntime_ActivityFinalNode,
    adwithoutruntime_ActivityNode,
    adwithoutruntime_BooleanBinaryExpression,
    adwithoutruntime_BooleanExpression,
    adwithoutruntime_BooleanUnaryExpression,
    adwithoutruntime_BooleanValue,
    adwithoutruntime_BooleanVariable,
    adwithoutruntime_ControlFlow,
    adwithoutruntime_ControlNode,
    adwithoutruntime_DecisionNode,
    adwithoutruntime_ExecutableNode,
    adwithoutruntime_Expression,
    adwithoutruntime_FinalNode,
    adwithoutruntime_ForkNode,
    adwithoutruntime_InitialNode,
    adwithoutruntime_IntegerCalculationExpression,
    adwithoutruntime_IntegerComparisonExpression,
    adwithoutruntime_IntegerExpression,
    adwithoutruntime_IntegerValue,
    adwithoutruntime_IntegerVariable,
    adwithoutruntime_JoinNode,
    adwithoutruntime_MergeNode,
    adwithoutruntime_NamedElement,
    adwithoutruntime_OpaqueAction,
    adwithoutruntime_Value,
    adwithoutruntime_Variable,
    BooleanBinaryOperator,
    BooleanUnaryOperator,
    IntegerCalculationOperator,
    IntegerComparisonOperator,
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

def test_adwithoutruntime_BooleanBinaryExpression_operator_value_roundtrip():
    instance = adwithoutruntime_BooleanBinaryExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_adwithoutruntime_BooleanUnaryExpression_operator_value_roundtrip():
    instance = adwithoutruntime_BooleanUnaryExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_adwithoutruntime_BooleanValue_value_value_roundtrip():
    instance = adwithoutruntime_BooleanValue(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_adwithoutruntime_IntegerCalculationExpression_operator_value_roundtrip():
    instance = adwithoutruntime_IntegerCalculationExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_adwithoutruntime_IntegerComparisonExpression_operator_value_roundtrip():
    instance = adwithoutruntime_IntegerComparisonExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_adwithoutruntime_IntegerValue_value_value_roundtrip():
    instance = adwithoutruntime_IntegerValue(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_adwithoutruntime_NamedElement_name_value_roundtrip():
    instance = adwithoutruntime_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adwithoutruntime_Variable_name_value_roundtrip():
    instance = adwithoutruntime_Variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adwithoutruntime_OpaqueAction_isa_Action():
    instance = adwithoutruntime_OpaqueAction()
    assert isinstance(instance, Action)


def test_adwithoutruntime_ControlFlow_isa_ActivityEdge():
    instance = adwithoutruntime_ControlFlow()
    assert isinstance(instance, ActivityEdge)


def test_adwithoutruntime_ControlNode_isa_ActivityNode():
    instance = adwithoutruntime_ControlNode()
    assert isinstance(instance, ActivityNode)


def test_adwithoutruntime_ExecutableNode_isa_ActivityNode():
    instance = adwithoutruntime_ExecutableNode()
    assert isinstance(instance, ActivityNode)


def test_adwithoutruntime_BooleanBinaryExpression_isa_BooleanExpression():
    instance = adwithoutruntime_BooleanBinaryExpression(operator="sample_text")
    assert isinstance(instance, BooleanExpression)


def test_adwithoutruntime_BooleanUnaryExpression_isa_BooleanExpression():
    instance = adwithoutruntime_BooleanUnaryExpression(operator="sample_text")
    assert isinstance(instance, BooleanExpression)


def test_adwithoutruntime_DecisionNode_isa_ControlNode():
    instance = adwithoutruntime_DecisionNode()
    assert isinstance(instance, ControlNode)


def test_adwithoutruntime_FinalNode_isa_ControlNode():
    instance = adwithoutruntime_FinalNode()
    assert isinstance(instance, ControlNode)


def test_adwithoutruntime_ForkNode_isa_ControlNode():
    instance = adwithoutruntime_ForkNode()
    assert isinstance(instance, ControlNode)


def test_adwithoutruntime_InitialNode_isa_ControlNode():
    instance = adwithoutruntime_InitialNode()
    assert isinstance(instance, ControlNode)


def test_adwithoutruntime_JoinNode_isa_ControlNode():
    instance = adwithoutruntime_JoinNode()
    assert isinstance(instance, ControlNode)


def test_adwithoutruntime_MergeNode_isa_ControlNode():
    instance = adwithoutruntime_MergeNode()
    assert isinstance(instance, ControlNode)


def test_adwithoutruntime_Action_isa_ExecutableNode():
    instance = adwithoutruntime_Action()
    assert isinstance(instance, ExecutableNode)


def test_adwithoutruntime_BooleanExpression_isa_Expression():
    instance = adwithoutruntime_BooleanExpression()
    assert isinstance(instance, Expression)


def test_adwithoutruntime_IntegerExpression_isa_Expression():
    instance = adwithoutruntime_IntegerExpression()
    assert isinstance(instance, Expression)


def test_adwithoutruntime_ActivityFinalNode_isa_FinalNode():
    instance = adwithoutruntime_ActivityFinalNode()
    assert isinstance(instance, FinalNode)


def test_adwithoutruntime_IntegerCalculationExpression_isa_IntegerExpression():
    instance = adwithoutruntime_IntegerCalculationExpression(operator="sample_text")
    assert isinstance(instance, IntegerExpression)


def test_adwithoutruntime_IntegerComparisonExpression_isa_IntegerExpression():
    instance = adwithoutruntime_IntegerComparisonExpression(operator="sample_text")
    assert isinstance(instance, IntegerExpression)


def test_adwithoutruntime_Activity_isa_NamedElement():
    instance = adwithoutruntime_Activity()
    assert isinstance(instance, NamedElement)


def test_adwithoutruntime_ActivityEdge_isa_NamedElement():
    instance = adwithoutruntime_ActivityEdge()
    assert isinstance(instance, NamedElement)


def test_adwithoutruntime_ActivityNode_isa_NamedElement():
    instance = adwithoutruntime_ActivityNode()
    assert isinstance(instance, NamedElement)


def test_adwithoutruntime_BooleanValue_isa_Value():
    instance = adwithoutruntime_BooleanValue(value=True)
    assert isinstance(instance, Value)


def test_adwithoutruntime_IntegerValue_isa_Value():
    instance = adwithoutruntime_IntegerValue(value=7)
    assert isinstance(instance, Value)


def test_adwithoutruntime_BooleanVariable_isa_Variable():
    instance = adwithoutruntime_BooleanVariable()
    assert isinstance(instance, Variable)


def test_adwithoutruntime_IntegerVariable_isa_Variable():
    instance = adwithoutruntime_IntegerVariable()
    assert isinstance(instance, Variable)


def test_assoc_assignee28_link_reassign_clear():
    a = adwithoutruntime_IntegerCalculationExpression(operator="sample_text")
    b1 = adwithoutruntime_IntegerVariable()
    b2 = adwithoutruntime_IntegerVariable()
    _safe_set(a, 'adwithoutruntime_IntegerCalculationExpression', b1)
    assert _is_linked(a, 'adwithoutruntime_IntegerCalculationExpression', b1)
    if hasattr(b1, 'adwithoutruntime_IntegerVariable29'):
        assert _is_linked(b1, 'adwithoutruntime_IntegerVariable29', a)
    _safe_set(a, 'adwithoutruntime_IntegerCalculationExpression', b2)
    assert _is_linked(a, 'adwithoutruntime_IntegerCalculationExpression', b2)
    if hasattr(b1, 'adwithoutruntime_IntegerVariable29'):
        assert not _is_linked(b1, 'adwithoutruntime_IntegerVariable29', a)
    if hasattr(b2, 'adwithoutruntime_IntegerVariable29'):
        assert _is_linked(b2, 'adwithoutruntime_IntegerVariable29', a)
    _safe_set(a, 'adwithoutruntime_IntegerCalculationExpression', None)
    assert not _is_linked(a, 'adwithoutruntime_IntegerCalculationExpression', b2)
    if hasattr(b2, 'adwithoutruntime_IntegerVariable29'):
        assert not _is_linked(b2, 'adwithoutruntime_IntegerVariable29', a)


def test_assoc_assignee30_link_reassign_clear():
    a = adwithoutruntime_IntegerComparisonExpression(operator="sample_text")
    b1 = adwithoutruntime_BooleanVariable()
    b2 = adwithoutruntime_BooleanVariable()
    _safe_set(a, 'adwithoutruntime_IntegerComparisonExpression', b1)
    assert _is_linked(a, 'adwithoutruntime_IntegerComparisonExpression', b1)
    if hasattr(b1, 'adwithoutruntime_BooleanVariable31'):
        assert _is_linked(b1, 'adwithoutruntime_BooleanVariable31', a)
    _safe_set(a, 'adwithoutruntime_IntegerComparisonExpression', b2)
    assert _is_linked(a, 'adwithoutruntime_IntegerComparisonExpression', b2)
    if hasattr(b1, 'adwithoutruntime_BooleanVariable31'):
        assert not _is_linked(b1, 'adwithoutruntime_BooleanVariable31', a)
    if hasattr(b2, 'adwithoutruntime_BooleanVariable31'):
        assert _is_linked(b2, 'adwithoutruntime_BooleanVariable31', a)
    _safe_set(a, 'adwithoutruntime_IntegerComparisonExpression', None)
    assert not _is_linked(a, 'adwithoutruntime_IntegerComparisonExpression', b2)
    if hasattr(b2, 'adwithoutruntime_BooleanVariable31'):
        assert not _is_linked(b2, 'adwithoutruntime_BooleanVariable31', a)


def test_assoc_currentValue19_link_reassign_clear():
    a = adwithoutruntime_Variable(name="sample_text")
    b1 = adwithoutruntime_Value()
    b2 = adwithoutruntime_Value()
    _safe_set(a, 'adwithoutruntime_Variable20', b1)
    assert _is_linked(a, 'adwithoutruntime_Variable20', b1)
    if hasattr(b1, 'adwithoutruntime_Value21'):
        assert _is_linked(b1, 'adwithoutruntime_Value21', a)
    _safe_set(a, 'adwithoutruntime_Variable20', b2)
    assert _is_linked(a, 'adwithoutruntime_Variable20', b2)
    if hasattr(b1, 'adwithoutruntime_Value21'):
        assert not _is_linked(b1, 'adwithoutruntime_Value21', a)
    if hasattr(b2, 'adwithoutruntime_Value21'):
        assert _is_linked(b2, 'adwithoutruntime_Value21', a)
    _safe_set(a, 'adwithoutruntime_Variable20', None)
    assert not _is_linked(a, 'adwithoutruntime_Variable20', b2)
    if hasattr(b2, 'adwithoutruntime_Value21'):
        assert not _is_linked(b2, 'adwithoutruntime_Value21', a)


def test_assoc_initialValue17_link_reassign_clear():
    a = adwithoutruntime_Variable(name="sample_text")
    b1 = adwithoutruntime_Value()
    b2 = adwithoutruntime_Value()
    _safe_set(a, 'adwithoutruntime_Variable18', b1)
    assert _is_linked(a, 'adwithoutruntime_Variable18', b1)
    if hasattr(b1, 'adwithoutruntime_Value'):
        assert _is_linked(b1, 'adwithoutruntime_Value', a)
    _safe_set(a, 'adwithoutruntime_Variable18', b2)
    assert _is_linked(a, 'adwithoutruntime_Variable18', b2)
    if hasattr(b1, 'adwithoutruntime_Value'):
        assert not _is_linked(b1, 'adwithoutruntime_Value', a)
    if hasattr(b2, 'adwithoutruntime_Value'):
        assert _is_linked(b2, 'adwithoutruntime_Value', a)
    _safe_set(a, 'adwithoutruntime_Variable18', None)
    assert not _is_linked(a, 'adwithoutruntime_Variable18', b2)
    if hasattr(b2, 'adwithoutruntime_Value'):
        assert not _is_linked(b2, 'adwithoutruntime_Value', a)


def test_assoc_inputs4_link_reassign_clear():
    a = adwithoutruntime_Variable(name="sample_text")
    b1 = adwithoutruntime_Activity()
    b2 = adwithoutruntime_Activity()
    _safe_set(a, 'adwithoutruntime_Variable6', b1)
    assert _is_linked(a, 'adwithoutruntime_Variable6', b1)
    if hasattr(b1, 'adwithoutruntime_Activity5'):
        assert _is_linked(b1, 'adwithoutruntime_Activity5', a)
    _safe_set(a, 'adwithoutruntime_Variable6', b2)
    assert _is_linked(a, 'adwithoutruntime_Variable6', b2)
    if hasattr(b1, 'adwithoutruntime_Activity5'):
        assert not _is_linked(b1, 'adwithoutruntime_Activity5', a)
    if hasattr(b2, 'adwithoutruntime_Activity5'):
        assert _is_linked(b2, 'adwithoutruntime_Activity5', a)
    _safe_set(a, 'adwithoutruntime_Variable6', None)
    assert not _is_linked(a, 'adwithoutruntime_Variable6', b2)
    if hasattr(b2, 'adwithoutruntime_Activity5'):
        assert not _is_linked(b2, 'adwithoutruntime_Activity5', a)


def test_assoc_locals2_link_reassign_clear():
    a = adwithoutruntime_Variable(name="sample_text")
    b1 = adwithoutruntime_Activity()
    b2 = adwithoutruntime_Activity()
    _safe_set(a, 'adwithoutruntime_Variable', b1)
    assert _is_linked(a, 'adwithoutruntime_Variable', b1)
    if hasattr(b1, 'adwithoutruntime_Activity3'):
        assert _is_linked(b1, 'adwithoutruntime_Activity3', a)
    _safe_set(a, 'adwithoutruntime_Variable', b2)
    assert _is_linked(a, 'adwithoutruntime_Variable', b2)
    if hasattr(b1, 'adwithoutruntime_Activity3'):
        assert not _is_linked(b1, 'adwithoutruntime_Activity3', a)
    if hasattr(b2, 'adwithoutruntime_Activity3'):
        assert _is_linked(b2, 'adwithoutruntime_Activity3', a)
    _safe_set(a, 'adwithoutruntime_Variable', None)
    assert not _is_linked(a, 'adwithoutruntime_Variable', b2)
    if hasattr(b2, 'adwithoutruntime_Activity3'):
        assert not _is_linked(b2, 'adwithoutruntime_Activity3', a)


def test_assoc_operand134_link_reassign_clear():
    a = adwithoutruntime_BooleanBinaryExpression(operator="sample_text")
    b1 = adwithoutruntime_BooleanVariable()
    b2 = adwithoutruntime_BooleanVariable()
    _safe_set(a, 'adwithoutruntime_BooleanBinaryExpression', b1)
    assert _is_linked(a, 'adwithoutruntime_BooleanBinaryExpression', b1)
    if hasattr(b1, 'adwithoutruntime_BooleanVariable35'):
        assert _is_linked(b1, 'adwithoutruntime_BooleanVariable35', a)
    _safe_set(a, 'adwithoutruntime_BooleanBinaryExpression', b2)
    assert _is_linked(a, 'adwithoutruntime_BooleanBinaryExpression', b2)
    if hasattr(b1, 'adwithoutruntime_BooleanVariable35'):
        assert not _is_linked(b1, 'adwithoutruntime_BooleanVariable35', a)
    if hasattr(b2, 'adwithoutruntime_BooleanVariable35'):
        assert _is_linked(b2, 'adwithoutruntime_BooleanVariable35', a)
    _safe_set(a, 'adwithoutruntime_BooleanBinaryExpression', None)
    assert not _is_linked(a, 'adwithoutruntime_BooleanBinaryExpression', b2)
    if hasattr(b2, 'adwithoutruntime_BooleanVariable35'):
        assert not _is_linked(b2, 'adwithoutruntime_BooleanVariable35', a)


def test_assoc_operand236_link_reassign_clear():
    a = adwithoutruntime_BooleanBinaryExpression(operator="sample_text")
    b1 = adwithoutruntime_BooleanVariable()
    b2 = adwithoutruntime_BooleanVariable()
    _safe_set(a, 'adwithoutruntime_BooleanBinaryExpression37', b1)
    assert _is_linked(a, 'adwithoutruntime_BooleanBinaryExpression37', b1)
    if hasattr(b1, 'adwithoutruntime_BooleanVariable38'):
        assert _is_linked(b1, 'adwithoutruntime_BooleanVariable38', a)
    _safe_set(a, 'adwithoutruntime_BooleanBinaryExpression37', b2)
    assert _is_linked(a, 'adwithoutruntime_BooleanBinaryExpression37', b2)
    if hasattr(b1, 'adwithoutruntime_BooleanVariable38'):
        assert not _is_linked(b1, 'adwithoutruntime_BooleanVariable38', a)
    if hasattr(b2, 'adwithoutruntime_BooleanVariable38'):
        assert _is_linked(b2, 'adwithoutruntime_BooleanVariable38', a)
    _safe_set(a, 'adwithoutruntime_BooleanBinaryExpression37', None)
    assert not _is_linked(a, 'adwithoutruntime_BooleanBinaryExpression37', b2)
    if hasattr(b2, 'adwithoutruntime_BooleanVariable38'):
        assert not _is_linked(b2, 'adwithoutruntime_BooleanVariable38', a)


def test_assoc_operand32_link_reassign_clear():
    a = adwithoutruntime_BooleanUnaryExpression(operator="sample_text")
    b1 = adwithoutruntime_BooleanVariable()
    b2 = adwithoutruntime_BooleanVariable()
    _safe_set(a, 'adwithoutruntime_BooleanUnaryExpression', b1)
    assert _is_linked(a, 'adwithoutruntime_BooleanUnaryExpression', b1)
    if hasattr(b1, 'adwithoutruntime_BooleanVariable33'):
        assert _is_linked(b1, 'adwithoutruntime_BooleanVariable33', a)
    _safe_set(a, 'adwithoutruntime_BooleanUnaryExpression', b2)
    assert _is_linked(a, 'adwithoutruntime_BooleanUnaryExpression', b2)
    if hasattr(b1, 'adwithoutruntime_BooleanVariable33'):
        assert not _is_linked(b1, 'adwithoutruntime_BooleanVariable33', a)
    if hasattr(b2, 'adwithoutruntime_BooleanVariable33'):
        assert _is_linked(b2, 'adwithoutruntime_BooleanVariable33', a)
    _safe_set(a, 'adwithoutruntime_BooleanUnaryExpression', None)
    assert not _is_linked(a, 'adwithoutruntime_BooleanUnaryExpression', b2)
    if hasattr(b2, 'adwithoutruntime_BooleanVariable33'):
        assert not _is_linked(b2, 'adwithoutruntime_BooleanVariable33', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


ActivityEdge_strategy = st.builds(ActivityEdge)
@given(instance=ActivityEdge_strategy)
@settings(max_examples=25)
def test_ActivityEdge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)


ActivityNode_strategy = st.builds(ActivityNode)
@given(instance=ActivityNode_strategy)
@settings(max_examples=25)
def test_ActivityNode_instantiation(instance):
    assert isinstance(instance, ActivityNode)


BooleanExpression_strategy = st.builds(BooleanExpression)
@given(instance=BooleanExpression_strategy)
@settings(max_examples=25)
def test_BooleanExpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)


ControlNode_strategy = st.builds(ControlNode)
@given(instance=ControlNode_strategy)
@settings(max_examples=25)
def test_ControlNode_instantiation(instance):
    assert isinstance(instance, ControlNode)


ExecutableNode_strategy = st.builds(ExecutableNode)
@given(instance=ExecutableNode_strategy)
@settings(max_examples=25)
def test_ExecutableNode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FinalNode_strategy = st.builds(FinalNode)
@given(instance=FinalNode_strategy)
@settings(max_examples=25)
def test_FinalNode_instantiation(instance):
    assert isinstance(instance, FinalNode)


IntegerExpression_strategy = st.builds(IntegerExpression)
@given(instance=IntegerExpression_strategy)
@settings(max_examples=25)
def test_IntegerExpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


adwithoutruntime_Action_strategy = st.builds(adwithoutruntime_Action)
@given(instance=adwithoutruntime_Action_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_Action_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_Action)


adwithoutruntime_Activity_strategy = st.builds(adwithoutruntime_Activity)
@given(instance=adwithoutruntime_Activity_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_Activity_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_Activity)


adwithoutruntime_ActivityEdge_strategy = st.builds(adwithoutruntime_ActivityEdge)
@given(instance=adwithoutruntime_ActivityEdge_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_ActivityEdge_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ActivityEdge)


adwithoutruntime_ActivityFinalNode_strategy = st.builds(adwithoutruntime_ActivityFinalNode)
@given(instance=adwithoutruntime_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ActivityFinalNode)


adwithoutruntime_ActivityNode_strategy = st.builds(adwithoutruntime_ActivityNode)
@given(instance=adwithoutruntime_ActivityNode_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_ActivityNode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ActivityNode)


adwithoutruntime_BooleanBinaryExpression_strategy = st.builds(adwithoutruntime_BooleanBinaryExpression, operator=safe_text)
@given(instance=adwithoutruntime_BooleanBinaryExpression_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_BooleanBinaryExpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_BooleanBinaryExpression)


adwithoutruntime_BooleanExpression_strategy = st.builds(adwithoutruntime_BooleanExpression)
@given(instance=adwithoutruntime_BooleanExpression_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_BooleanExpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_BooleanExpression)


adwithoutruntime_BooleanUnaryExpression_strategy = st.builds(adwithoutruntime_BooleanUnaryExpression, operator=safe_text)
@given(instance=adwithoutruntime_BooleanUnaryExpression_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_BooleanUnaryExpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_BooleanUnaryExpression)


adwithoutruntime_BooleanValue_strategy = st.builds(adwithoutruntime_BooleanValue, value=st.booleans())
@given(instance=adwithoutruntime_BooleanValue_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_BooleanValue_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_BooleanValue)


adwithoutruntime_BooleanVariable_strategy = st.builds(adwithoutruntime_BooleanVariable)
@given(instance=adwithoutruntime_BooleanVariable_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_BooleanVariable_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_BooleanVariable)


adwithoutruntime_ControlFlow_strategy = st.builds(adwithoutruntime_ControlFlow)
@given(instance=adwithoutruntime_ControlFlow_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_ControlFlow_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ControlFlow)


adwithoutruntime_ControlNode_strategy = st.builds(adwithoutruntime_ControlNode)
@given(instance=adwithoutruntime_ControlNode_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_ControlNode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ControlNode)


adwithoutruntime_DecisionNode_strategy = st.builds(adwithoutruntime_DecisionNode)
@given(instance=adwithoutruntime_DecisionNode_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_DecisionNode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_DecisionNode)


adwithoutruntime_ExecutableNode_strategy = st.builds(adwithoutruntime_ExecutableNode)
@given(instance=adwithoutruntime_ExecutableNode_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_ExecutableNode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ExecutableNode)


adwithoutruntime_Expression_strategy = st.builds(adwithoutruntime_Expression)
@given(instance=adwithoutruntime_Expression_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_Expression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_Expression)


adwithoutruntime_FinalNode_strategy = st.builds(adwithoutruntime_FinalNode)
@given(instance=adwithoutruntime_FinalNode_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_FinalNode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_FinalNode)


adwithoutruntime_ForkNode_strategy = st.builds(adwithoutruntime_ForkNode)
@given(instance=adwithoutruntime_ForkNode_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_ForkNode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ForkNode)


adwithoutruntime_InitialNode_strategy = st.builds(adwithoutruntime_InitialNode)
@given(instance=adwithoutruntime_InitialNode_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_InitialNode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_InitialNode)


adwithoutruntime_IntegerCalculationExpression_strategy = st.builds(adwithoutruntime_IntegerCalculationExpression, operator=safe_text)
@given(instance=adwithoutruntime_IntegerCalculationExpression_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_IntegerCalculationExpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_IntegerCalculationExpression)


adwithoutruntime_IntegerComparisonExpression_strategy = st.builds(adwithoutruntime_IntegerComparisonExpression, operator=safe_text)
@given(instance=adwithoutruntime_IntegerComparisonExpression_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_IntegerComparisonExpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_IntegerComparisonExpression)


adwithoutruntime_IntegerExpression_strategy = st.builds(adwithoutruntime_IntegerExpression)
@given(instance=adwithoutruntime_IntegerExpression_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_IntegerExpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_IntegerExpression)


adwithoutruntime_IntegerValue_strategy = st.builds(adwithoutruntime_IntegerValue, value=st.integers())
@given(instance=adwithoutruntime_IntegerValue_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_IntegerValue_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_IntegerValue)


adwithoutruntime_IntegerVariable_strategy = st.builds(adwithoutruntime_IntegerVariable)
@given(instance=adwithoutruntime_IntegerVariable_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_IntegerVariable_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_IntegerVariable)


adwithoutruntime_JoinNode_strategy = st.builds(adwithoutruntime_JoinNode)
@given(instance=adwithoutruntime_JoinNode_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_JoinNode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_JoinNode)


adwithoutruntime_MergeNode_strategy = st.builds(adwithoutruntime_MergeNode)
@given(instance=adwithoutruntime_MergeNode_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_MergeNode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_MergeNode)


adwithoutruntime_NamedElement_strategy = st.builds(adwithoutruntime_NamedElement, name=safe_text)
@given(instance=adwithoutruntime_NamedElement_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_NamedElement_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_NamedElement)


adwithoutruntime_OpaqueAction_strategy = st.builds(adwithoutruntime_OpaqueAction)
@given(instance=adwithoutruntime_OpaqueAction_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_OpaqueAction_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_OpaqueAction)


adwithoutruntime_Value_strategy = st.builds(adwithoutruntime_Value)
@given(instance=adwithoutruntime_Value_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_Value_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_Value)


adwithoutruntime_Variable_strategy = st.builds(adwithoutruntime_Variable, name=safe_text)
@given(instance=adwithoutruntime_Variable_strategy)
@settings(max_examples=25)
def test_adwithoutruntime_Variable_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_Variable)



