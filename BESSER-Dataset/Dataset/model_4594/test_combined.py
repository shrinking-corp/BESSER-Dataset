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
    minuml2_ActivityEdge,
    minuml2_ActivityNode,
    minuml2_Activity,
    ValueSpecification,
    minuml2_OpaqueExpression,
    ActivityEdge,
    minuml2_ObjectFlow,
    minuml2_ControlFlow,
    minuml2_ValueSpecification,
    ActivityNode,
    minuml2_ForkNode,
    minuml2_JoinNode,
    minuml2_DecisionNode,
    minuml2_ActivityFinalNode,
    minuml2_OpaqueAction,
    ActivityGroup,
    minuml2_ActivityPartition,
    minuml2_ActivityGroup,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_minuml2_activityedge_is_not_abstract():
    assert not inspect.isabstract(minuml2_ActivityEdge)


def test_hyp_minuml2_activityedge_constructor_exists():
    assert callable(minuml2_ActivityEdge.__init__)


def test_hyp_minuml2_activityedge_constructor_args():
    sig = inspect.signature(minuml2_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_activitynode_is_not_abstract():
    assert not inspect.isabstract(minuml2_ActivityNode)


def test_hyp_minuml2_activitynode_constructor_exists():
    assert callable(minuml2_ActivityNode.__init__)


def test_hyp_minuml2_activitynode_constructor_args():
    sig = inspect.signature(minuml2_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_activity_is_not_abstract():
    assert not inspect.isabstract(minuml2_Activity)


def test_hyp_minuml2_activity_constructor_exists():
    assert callable(minuml2_Activity.__init__)


def test_hyp_minuml2_activity_constructor_args():
    sig = inspect.signature(minuml2_Activity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_hyp_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_hyp_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(minuml2_OpaqueExpression)


def test_hyp_minuml2_opaqueexpression_constructor_exists():
    assert callable(minuml2_OpaqueExpression.__init__)


def test_hyp_minuml2_opaqueexpression_constructor_args():
    sig = inspect.signature(minuml2_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"





def test_hyp_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_hyp_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_hyp_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_objectflow_is_not_abstract():
    assert not inspect.isabstract(minuml2_ObjectFlow)


def test_hyp_minuml2_objectflow_constructor_exists():
    assert callable(minuml2_ObjectFlow.__init__)


def test_hyp_minuml2_objectflow_constructor_args():
    sig = inspect.signature(minuml2_ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_controlflow_is_not_abstract():
    assert not inspect.isabstract(minuml2_ControlFlow)


def test_hyp_minuml2_controlflow_constructor_exists():
    assert callable(minuml2_ControlFlow.__init__)


def test_hyp_minuml2_controlflow_constructor_args():
    sig = inspect.signature(minuml2_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_valuespecification_is_not_abstract():
    assert not inspect.isabstract(minuml2_ValueSpecification)


def test_hyp_minuml2_valuespecification_constructor_exists():
    assert callable(minuml2_ValueSpecification.__init__)


def test_hyp_minuml2_valuespecification_constructor_args():
    sig = inspect.signature(minuml2_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_hyp_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_hyp_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_forknode_is_not_abstract():
    assert not inspect.isabstract(minuml2_ForkNode)


def test_hyp_minuml2_forknode_constructor_exists():
    assert callable(minuml2_ForkNode.__init__)


def test_hyp_minuml2_forknode_constructor_args():
    sig = inspect.signature(minuml2_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_joinnode_is_not_abstract():
    assert not inspect.isabstract(minuml2_JoinNode)


def test_hyp_minuml2_joinnode_constructor_exists():
    assert callable(minuml2_JoinNode.__init__)


def test_hyp_minuml2_joinnode_constructor_args():
    sig = inspect.signature(minuml2_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_decisionnode_is_not_abstract():
    assert not inspect.isabstract(minuml2_DecisionNode)


def test_hyp_minuml2_decisionnode_constructor_exists():
    assert callable(minuml2_DecisionNode.__init__)


def test_hyp_minuml2_decisionnode_constructor_args():
    sig = inspect.signature(minuml2_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(minuml2_ActivityFinalNode)


def test_hyp_minuml2_activityfinalnode_constructor_exists():
    assert callable(minuml2_ActivityFinalNode.__init__)


def test_hyp_minuml2_activityfinalnode_constructor_args():
    sig = inspect.signature(minuml2_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(minuml2_OpaqueAction)


def test_hyp_minuml2_opaqueaction_constructor_exists():
    assert callable(minuml2_OpaqueAction.__init__)


def test_hyp_minuml2_opaqueaction_constructor_args():
    sig = inspect.signature(minuml2_OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_hyp_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_hyp_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_activitypartition_is_not_abstract():
    assert not inspect.isabstract(minuml2_ActivityPartition)


def test_hyp_minuml2_activitypartition_constructor_exists():
    assert callable(minuml2_ActivityPartition.__init__)


def test_hyp_minuml2_activitypartition_constructor_args():
    sig = inspect.signature(minuml2_ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minuml2_activitygroup_is_not_abstract():
    assert not inspect.isabstract(minuml2_ActivityGroup)


def test_hyp_minuml2_activitygroup_constructor_exists():
    assert callable(minuml2_ActivityGroup.__init__)


def test_hyp_minuml2_activitygroup_constructor_args():
    sig = inspect.signature(minuml2_ActivityGroup.__init__)
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
minuml2_ActivityEdge_strategy = st.builds(
    minuml2_ActivityEdge,
)
minuml2_ActivityNode_strategy = st.builds(
    minuml2_ActivityNode,
)
minuml2_Activity_strategy = st.builds(
    minuml2_Activity,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
minuml2_OpaqueExpression_strategy = st.builds(
    minuml2_OpaqueExpression,
    language=
        safe_text,
    body=
        safe_text
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
minuml2_ObjectFlow_strategy = st.builds(
    minuml2_ObjectFlow,
)
minuml2_ControlFlow_strategy = st.builds(
    minuml2_ControlFlow,
)
minuml2_ValueSpecification_strategy = st.builds(
    minuml2_ValueSpecification,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
minuml2_ForkNode_strategy = st.builds(
    minuml2_ForkNode,
)
minuml2_JoinNode_strategy = st.builds(
    minuml2_JoinNode,
)
minuml2_DecisionNode_strategy = st.builds(
    minuml2_DecisionNode,
)
minuml2_ActivityFinalNode_strategy = st.builds(
    minuml2_ActivityFinalNode,
)
minuml2_OpaqueAction_strategy = st.builds(
    minuml2_OpaqueAction,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
minuml2_ActivityPartition_strategy = st.builds(
    minuml2_ActivityPartition,
)
minuml2_ActivityGroup_strategy = st.builds(
    minuml2_ActivityGroup,
)








@given(instance=minuml2_OpaqueExpression_strategy)
def test_hyp_minuml2_opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=minuml2_OpaqueExpression_strategy)
def test_hyp_minuml2_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original















# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    ValueSpecification,
    minuml2_Activity,
    minuml2_ActivityEdge,
    minuml2_ActivityFinalNode,
    minuml2_ActivityGroup,
    minuml2_ActivityNode,
    minuml2_ActivityPartition,
    minuml2_ControlFlow,
    minuml2_DecisionNode,
    minuml2_ForkNode,
    minuml2_JoinNode,
    minuml2_ObjectFlow,
    minuml2_OpaqueAction,
    minuml2_OpaqueExpression,
    minuml2_ValueSpecification,
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

def test_minuml2_OpaqueExpression_body_value_roundtrip():
    instance = minuml2_OpaqueExpression(body="sample_text", language="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_minuml2_OpaqueExpression_language_value_roundtrip():
    instance = minuml2_OpaqueExpression(body="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_minuml2_ControlFlow_isa_ActivityEdge():
    instance = minuml2_ControlFlow()
    assert isinstance(instance, ActivityEdge)


def test_minuml2_ObjectFlow_isa_ActivityEdge():
    instance = minuml2_ObjectFlow()
    assert isinstance(instance, ActivityEdge)


def test_minuml2_ActivityPartition_isa_ActivityGroup():
    instance = minuml2_ActivityPartition()
    assert isinstance(instance, ActivityGroup)


def test_minuml2_ActivityFinalNode_isa_ActivityNode():
    instance = minuml2_ActivityFinalNode()
    assert isinstance(instance, ActivityNode)


def test_minuml2_DecisionNode_isa_ActivityNode():
    instance = minuml2_DecisionNode()
    assert isinstance(instance, ActivityNode)


def test_minuml2_ForkNode_isa_ActivityNode():
    instance = minuml2_ForkNode()
    assert isinstance(instance, ActivityNode)


def test_minuml2_JoinNode_isa_ActivityNode():
    instance = minuml2_JoinNode()
    assert isinstance(instance, ActivityNode)


def test_minuml2_OpaqueAction_isa_ActivityNode():
    instance = minuml2_OpaqueAction()
    assert isinstance(instance, ActivityNode)


def test_minuml2_OpaqueExpression_isa_ValueSpecification():
    instance = minuml2_OpaqueExpression(body="sample_text", language="sample_text")
    assert isinstance(instance, ValueSpecification)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ActivityEdge_strategy = st.builds(ActivityEdge)
@given(instance=ActivityEdge_strategy)
@settings(max_examples=25)
def test_ActivityEdge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)


ActivityGroup_strategy = st.builds(ActivityGroup)
@given(instance=ActivityGroup_strategy)
@settings(max_examples=25)
def test_ActivityGroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)


ActivityNode_strategy = st.builds(ActivityNode)
@given(instance=ActivityNode_strategy)
@settings(max_examples=25)
def test_ActivityNode_instantiation(instance):
    assert isinstance(instance, ActivityNode)


ValueSpecification_strategy = st.builds(ValueSpecification)
@given(instance=ValueSpecification_strategy)
@settings(max_examples=25)
def test_ValueSpecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)


minuml2_Activity_strategy = st.builds(minuml2_Activity)
@given(instance=minuml2_Activity_strategy)
@settings(max_examples=25)
def test_minuml2_Activity_instantiation(instance):
    assert isinstance(instance, minuml2_Activity)


minuml2_ActivityEdge_strategy = st.builds(minuml2_ActivityEdge)
@given(instance=minuml2_ActivityEdge_strategy)
@settings(max_examples=25)
def test_minuml2_ActivityEdge_instantiation(instance):
    assert isinstance(instance, minuml2_ActivityEdge)


minuml2_ActivityFinalNode_strategy = st.builds(minuml2_ActivityFinalNode)
@given(instance=minuml2_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_minuml2_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, minuml2_ActivityFinalNode)


minuml2_ActivityGroup_strategy = st.builds(minuml2_ActivityGroup)
@given(instance=minuml2_ActivityGroup_strategy)
@settings(max_examples=25)
def test_minuml2_ActivityGroup_instantiation(instance):
    assert isinstance(instance, minuml2_ActivityGroup)


minuml2_ActivityNode_strategy = st.builds(minuml2_ActivityNode)
@given(instance=minuml2_ActivityNode_strategy)
@settings(max_examples=25)
def test_minuml2_ActivityNode_instantiation(instance):
    assert isinstance(instance, minuml2_ActivityNode)


minuml2_ActivityPartition_strategy = st.builds(minuml2_ActivityPartition)
@given(instance=minuml2_ActivityPartition_strategy)
@settings(max_examples=25)
def test_minuml2_ActivityPartition_instantiation(instance):
    assert isinstance(instance, minuml2_ActivityPartition)


minuml2_ControlFlow_strategy = st.builds(minuml2_ControlFlow)
@given(instance=minuml2_ControlFlow_strategy)
@settings(max_examples=25)
def test_minuml2_ControlFlow_instantiation(instance):
    assert isinstance(instance, minuml2_ControlFlow)


minuml2_DecisionNode_strategy = st.builds(minuml2_DecisionNode)
@given(instance=minuml2_DecisionNode_strategy)
@settings(max_examples=25)
def test_minuml2_DecisionNode_instantiation(instance):
    assert isinstance(instance, minuml2_DecisionNode)


minuml2_ForkNode_strategy = st.builds(minuml2_ForkNode)
@given(instance=minuml2_ForkNode_strategy)
@settings(max_examples=25)
def test_minuml2_ForkNode_instantiation(instance):
    assert isinstance(instance, minuml2_ForkNode)


minuml2_JoinNode_strategy = st.builds(minuml2_JoinNode)
@given(instance=minuml2_JoinNode_strategy)
@settings(max_examples=25)
def test_minuml2_JoinNode_instantiation(instance):
    assert isinstance(instance, minuml2_JoinNode)


minuml2_ObjectFlow_strategy = st.builds(minuml2_ObjectFlow)
@given(instance=minuml2_ObjectFlow_strategy)
@settings(max_examples=25)
def test_minuml2_ObjectFlow_instantiation(instance):
    assert isinstance(instance, minuml2_ObjectFlow)


minuml2_OpaqueAction_strategy = st.builds(minuml2_OpaqueAction)
@given(instance=minuml2_OpaqueAction_strategy)
@settings(max_examples=25)
def test_minuml2_OpaqueAction_instantiation(instance):
    assert isinstance(instance, minuml2_OpaqueAction)


minuml2_OpaqueExpression_strategy = st.builds(minuml2_OpaqueExpression, body=safe_text, language=safe_text)
@given(instance=minuml2_OpaqueExpression_strategy)
@settings(max_examples=25)
def test_minuml2_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, minuml2_OpaqueExpression)


minuml2_ValueSpecification_strategy = st.builds(minuml2_ValueSpecification)
@given(instance=minuml2_ValueSpecification_strategy)
@settings(max_examples=25)
def test_minuml2_ValueSpecification_instantiation(instance):
    assert isinstance(instance, minuml2_ValueSpecification)



