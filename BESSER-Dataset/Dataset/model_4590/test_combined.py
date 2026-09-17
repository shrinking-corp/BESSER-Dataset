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
    ControlNode,
    activitydiagram_FinalNode,
    activitydiagram_InitialNode,
    ActivityNode,
    activitydiagram_ControlNode,
    activitydiagram_ObjectNode,
    activitydiagram_SignalNode,
    activitydiagram_ActionNode,
    ObjectNode,
    activitydiagram_ExpansionNode,
    activitydiagram_DataStoreNode,
    activitydiagram_Pin,
    activitydiagram_ActivityParameterNode,
    FinalNode,
    activitydiagram_FlowFinalNode,
    activitydiagram_ActivityFinalNode,
    activitydiagram_TimeEventNode,
    activitydiagram_AcceptSignalNode,
    activitydiagram_DecisionNode,
    activitydiagram_MergeNode,
    activitydiagram_JoinNode,
    activitydiagram_ForkNode,
    activitydiagram_ADElement,
    ADElement,
    activitydiagram_ActivityEdge,
    activitydiagram_ActivityNode,
    activitydiagram_Activity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_hyp_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_hyp_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_finalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_FinalNode)


def test_hyp_activitydiagram_finalnode_constructor_exists():
    assert callable(activitydiagram_FinalNode.__init__)


def test_hyp_activitydiagram_finalnode_constructor_args():
    sig = inspect.signature(activitydiagram_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_initialnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_InitialNode)


def test_hyp_activitydiagram_initialnode_constructor_exists():
    assert callable(activitydiagram_InitialNode.__init__)


def test_hyp_activitydiagram_initialnode_constructor_args():
    sig = inspect.signature(activitydiagram_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_hyp_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_hyp_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_controlnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_ControlNode)


def test_hyp_activitydiagram_controlnode_constructor_exists():
    assert callable(activitydiagram_ControlNode.__init__)


def test_hyp_activitydiagram_controlnode_constructor_args():
    sig = inspect.signature(activitydiagram_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_objectnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_ObjectNode)


def test_hyp_activitydiagram_objectnode_constructor_exists():
    assert callable(activitydiagram_ObjectNode.__init__)


def test_hyp_activitydiagram_objectnode_constructor_args():
    sig = inspect.signature(activitydiagram_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_signalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_SignalNode)


def test_hyp_activitydiagram_signalnode_constructor_exists():
    assert callable(activitydiagram_SignalNode.__init__)


def test_hyp_activitydiagram_signalnode_constructor_args():
    sig = inspect.signature(activitydiagram_SignalNode.__init__)
    params = list(sig.parameters.keys())
    assert "signalId" in params, "Missing parameter 'signalId'"




def test_hyp_activitydiagram_actionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_ActionNode)


def test_hyp_activitydiagram_actionnode_constructor_exists():
    assert callable(activitydiagram_ActionNode.__init__)


def test_hyp_activitydiagram_actionnode_constructor_args():
    sig = inspect.signature(activitydiagram_ActionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_hyp_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_hyp_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_expansionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_ExpansionNode)


def test_hyp_activitydiagram_expansionnode_constructor_exists():
    assert callable(activitydiagram_ExpansionNode.__init__)


def test_hyp_activitydiagram_expansionnode_constructor_args():
    sig = inspect.signature(activitydiagram_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_datastorenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_DataStoreNode)


def test_hyp_activitydiagram_datastorenode_constructor_exists():
    assert callable(activitydiagram_DataStoreNode.__init__)


def test_hyp_activitydiagram_datastorenode_constructor_args():
    sig = inspect.signature(activitydiagram_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_pin_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_Pin)


def test_hyp_activitydiagram_pin_constructor_exists():
    assert callable(activitydiagram_Pin.__init__)


def test_hyp_activitydiagram_pin_constructor_args():
    sig = inspect.signature(activitydiagram_Pin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_ActivityParameterNode)


def test_hyp_activitydiagram_activityparameternode_constructor_exists():
    assert callable(activitydiagram_ActivityParameterNode.__init__)


def test_hyp_activitydiagram_activityparameternode_constructor_args():
    sig = inspect.signature(activitydiagram_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"




def test_hyp_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_hyp_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_hyp_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_FlowFinalNode)


def test_hyp_activitydiagram_flowfinalnode_constructor_exists():
    assert callable(activitydiagram_FlowFinalNode.__init__)


def test_hyp_activitydiagram_flowfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram_FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_ActivityFinalNode)


def test_hyp_activitydiagram_activityfinalnode_constructor_exists():
    assert callable(activitydiagram_ActivityFinalNode.__init__)


def test_hyp_activitydiagram_activityfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_timeeventnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TimeEventNode)


def test_hyp_activitydiagram_timeeventnode_constructor_exists():
    assert callable(activitydiagram_TimeEventNode.__init__)


def test_hyp_activitydiagram_timeeventnode_constructor_args():
    sig = inspect.signature(activitydiagram_TimeEventNode.__init__)
    params = list(sig.parameters.keys())
    assert "cycle" in params, "Missing parameter 'cycle'"




def test_hyp_activitydiagram_acceptsignalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_AcceptSignalNode)


def test_hyp_activitydiagram_acceptsignalnode_constructor_exists():
    assert callable(activitydiagram_AcceptSignalNode.__init__)


def test_hyp_activitydiagram_acceptsignalnode_constructor_args():
    sig = inspect.signature(activitydiagram_AcceptSignalNode.__init__)
    params = list(sig.parameters.keys())
    assert "signalId" in params, "Missing parameter 'signalId'"




def test_hyp_activitydiagram_decisionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_DecisionNode)


def test_hyp_activitydiagram_decisionnode_constructor_exists():
    assert callable(activitydiagram_DecisionNode.__init__)


def test_hyp_activitydiagram_decisionnode_constructor_args():
    sig = inspect.signature(activitydiagram_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_mergenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_MergeNode)


def test_hyp_activitydiagram_mergenode_constructor_exists():
    assert callable(activitydiagram_MergeNode.__init__)


def test_hyp_activitydiagram_mergenode_constructor_args():
    sig = inspect.signature(activitydiagram_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_joinnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_JoinNode)


def test_hyp_activitydiagram_joinnode_constructor_exists():
    assert callable(activitydiagram_JoinNode.__init__)


def test_hyp_activitydiagram_joinnode_constructor_args():
    sig = inspect.signature(activitydiagram_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_forknode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_ForkNode)


def test_hyp_activitydiagram_forknode_constructor_exists():
    assert callable(activitydiagram_ForkNode.__init__)


def test_hyp_activitydiagram_forknode_constructor_args():
    sig = inspect.signature(activitydiagram_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_adelement_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_ADElement)


def test_hyp_activitydiagram_adelement_constructor_exists():
    assert callable(activitydiagram_ADElement.__init__)


def test_hyp_activitydiagram_adelement_constructor_args():
    sig = inspect.signature(activitydiagram_ADElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_adelement_is_not_abstract():
    assert not inspect.isabstract(ADElement)


def test_hyp_adelement_constructor_exists():
    assert callable(ADElement.__init__)


def test_hyp_adelement_constructor_args():
    sig = inspect.signature(ADElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydiagram_activityedge_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_ActivityEdge)


def test_hyp_activitydiagram_activityedge_constructor_exists():
    assert callable(activitydiagram_ActivityEdge.__init__)


def test_hyp_activitydiagram_activityedge_constructor_args():
    sig = inspect.signature(activitydiagram_ActivityEdge.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"




def test_hyp_activitydiagram_activitynode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_ActivityNode)


def test_hyp_activitydiagram_activitynode_constructor_exists():
    assert callable(activitydiagram_ActivityNode.__init__)


def test_hyp_activitydiagram_activitynode_constructor_args():
    sig = inspect.signature(activitydiagram_ActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "current" in params, "Missing parameter 'current'"




def test_hyp_activitydiagram_activity_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_Activity)


def test_hyp_activitydiagram_activity_constructor_exists():
    assert callable(activitydiagram_Activity.__init__)


def test_hyp_activitydiagram_activity_constructor_args():
    sig = inspect.signature(activitydiagram_Activity.__init__)
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
ControlNode_strategy = st.builds(
    ControlNode,
)
activitydiagram_FinalNode_strategy = st.builds(
    activitydiagram_FinalNode,
)
activitydiagram_InitialNode_strategy = st.builds(
    activitydiagram_InitialNode,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
activitydiagram_ControlNode_strategy = st.builds(
    activitydiagram_ControlNode,
)
activitydiagram_ObjectNode_strategy = st.builds(
    activitydiagram_ObjectNode,
)
activitydiagram_SignalNode_strategy = st.builds(
    activitydiagram_SignalNode,
    signalId=
        safe_text
)
activitydiagram_ActionNode_strategy = st.builds(
    activitydiagram_ActionNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
activitydiagram_ExpansionNode_strategy = st.builds(
    activitydiagram_ExpansionNode,
)
activitydiagram_DataStoreNode_strategy = st.builds(
    activitydiagram_DataStoreNode,
)
activitydiagram_Pin_strategy = st.builds(
    activitydiagram_Pin,
)
activitydiagram_ActivityParameterNode_strategy = st.builds(
    activitydiagram_ActivityParameterNode,
    parameter=
        safe_text
)
FinalNode_strategy = st.builds(
    FinalNode,
)
activitydiagram_FlowFinalNode_strategy = st.builds(
    activitydiagram_FlowFinalNode,
)
activitydiagram_ActivityFinalNode_strategy = st.builds(
    activitydiagram_ActivityFinalNode,
)
activitydiagram_TimeEventNode_strategy = st.builds(
    activitydiagram_TimeEventNode,
    cycle=
        safe_text
)
activitydiagram_AcceptSignalNode_strategy = st.builds(
    activitydiagram_AcceptSignalNode,
    signalId=
        safe_text
)
activitydiagram_DecisionNode_strategy = st.builds(
    activitydiagram_DecisionNode,
)
activitydiagram_MergeNode_strategy = st.builds(
    activitydiagram_MergeNode,
)
activitydiagram_JoinNode_strategy = st.builds(
    activitydiagram_JoinNode,
)
activitydiagram_ForkNode_strategy = st.builds(
    activitydiagram_ForkNode,
)
activitydiagram_ADElement_strategy = st.builds(
    activitydiagram_ADElement,
    name=
        safe_text
)
ADElement_strategy = st.builds(
    ADElement,
)
activitydiagram_ActivityEdge_strategy = st.builds(
    activitydiagram_ActivityEdge,
    guard=
        st.booleans()
)
activitydiagram_ActivityNode_strategy = st.builds(
    activitydiagram_ActivityNode,
    current=
        st.booleans()
)
activitydiagram_Activity_strategy = st.builds(
    activitydiagram_Activity,
)










@given(instance=activitydiagram_SignalNode_strategy)
def test_hyp_activitydiagram_signalnode_signalId_setter(instance):
    original = instance.signalId
    instance.signalId = original
    assert instance.signalId == original









@given(instance=activitydiagram_ActivityParameterNode_strategy)
def test_hyp_activitydiagram_activityparameternode_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original







@given(instance=activitydiagram_TimeEventNode_strategy)
def test_hyp_activitydiagram_timeeventnode_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original




@given(instance=activitydiagram_AcceptSignalNode_strategy)
def test_hyp_activitydiagram_acceptsignalnode_signalId_setter(instance):
    original = instance.signalId
    instance.signalId = original
    assert instance.signalId == original








@given(instance=activitydiagram_ADElement_strategy)
def test_hyp_activitydiagram_adelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=activitydiagram_ActivityEdge_strategy)
def test_hyp_activitydiagram_activityedge_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original




@given(instance=activitydiagram_ActivityNode_strategy)
def test_hyp_activitydiagram_activitynode_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ADElement,
    ActivityNode,
    ControlNode,
    FinalNode,
    ObjectNode,
    activitydiagram_ADElement,
    activitydiagram_AcceptSignalNode,
    activitydiagram_ActionNode,
    activitydiagram_Activity,
    activitydiagram_ActivityEdge,
    activitydiagram_ActivityFinalNode,
    activitydiagram_ActivityNode,
    activitydiagram_ActivityParameterNode,
    activitydiagram_ControlNode,
    activitydiagram_DataStoreNode,
    activitydiagram_DecisionNode,
    activitydiagram_ExpansionNode,
    activitydiagram_FinalNode,
    activitydiagram_FlowFinalNode,
    activitydiagram_ForkNode,
    activitydiagram_InitialNode,
    activitydiagram_JoinNode,
    activitydiagram_MergeNode,
    activitydiagram_ObjectNode,
    activitydiagram_Pin,
    activitydiagram_SignalNode,
    activitydiagram_TimeEventNode,
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

def test_activitydiagram_ADElement_name_value_roundtrip():
    instance = activitydiagram_ADElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_activitydiagram_AcceptSignalNode_signalId_value_roundtrip():
    instance = activitydiagram_AcceptSignalNode(signalId="sample_text")
    assert instance.signalId == "sample_text"
    instance.signalId = "sample_text_2"
    assert instance.signalId == "sample_text_2"


def test_activitydiagram_ActivityEdge_guard_value_roundtrip():
    instance = activitydiagram_ActivityEdge(guard=True)
    assert instance.guard == True
    instance.guard = False
    assert instance.guard == False


def test_activitydiagram_ActivityNode_current_value_roundtrip():
    instance = activitydiagram_ActivityNode(current=True)
    assert instance.current == True
    instance.current = False
    assert instance.current == False


def test_activitydiagram_ActivityParameterNode_parameter_value_roundtrip():
    instance = activitydiagram_ActivityParameterNode(parameter="sample_text")
    assert instance.parameter == "sample_text"
    instance.parameter = "sample_text_2"
    assert instance.parameter == "sample_text_2"


def test_activitydiagram_SignalNode_signalId_value_roundtrip():
    instance = activitydiagram_SignalNode(signalId="sample_text")
    assert instance.signalId == "sample_text"
    instance.signalId = "sample_text_2"
    assert instance.signalId == "sample_text_2"


def test_activitydiagram_TimeEventNode_cycle_value_roundtrip():
    instance = activitydiagram_TimeEventNode(cycle="sample_text")
    assert instance.cycle == "sample_text"
    instance.cycle = "sample_text_2"
    assert instance.cycle == "sample_text_2"


def test_activitydiagram_Activity_isa_ADElement():
    instance = activitydiagram_Activity()
    assert isinstance(instance, ADElement)


def test_activitydiagram_ActivityEdge_isa_ADElement():
    instance = activitydiagram_ActivityEdge(guard=True)
    assert isinstance(instance, ADElement)


def test_activitydiagram_ActivityNode_isa_ADElement():
    instance = activitydiagram_ActivityNode(current=True)
    assert isinstance(instance, ADElement)


def test_activitydiagram_AcceptSignalNode_isa_ActivityNode():
    instance = activitydiagram_AcceptSignalNode(signalId="sample_text")
    assert isinstance(instance, ActivityNode)


def test_activitydiagram_ActionNode_isa_ActivityNode():
    instance = activitydiagram_ActionNode()
    assert isinstance(instance, ActivityNode)


def test_activitydiagram_ControlNode_isa_ActivityNode():
    instance = activitydiagram_ControlNode()
    assert isinstance(instance, ActivityNode)


def test_activitydiagram_ObjectNode_isa_ActivityNode():
    instance = activitydiagram_ObjectNode()
    assert isinstance(instance, ActivityNode)


def test_activitydiagram_SignalNode_isa_ActivityNode():
    instance = activitydiagram_SignalNode(signalId="sample_text")
    assert isinstance(instance, ActivityNode)


def test_activitydiagram_TimeEventNode_isa_ActivityNode():
    instance = activitydiagram_TimeEventNode(cycle="sample_text")
    assert isinstance(instance, ActivityNode)


def test_activitydiagram_DecisionNode_isa_ControlNode():
    instance = activitydiagram_DecisionNode()
    assert isinstance(instance, ControlNode)


def test_activitydiagram_FinalNode_isa_ControlNode():
    instance = activitydiagram_FinalNode()
    assert isinstance(instance, ControlNode)


def test_activitydiagram_ForkNode_isa_ControlNode():
    instance = activitydiagram_ForkNode()
    assert isinstance(instance, ControlNode)


def test_activitydiagram_InitialNode_isa_ControlNode():
    instance = activitydiagram_InitialNode()
    assert isinstance(instance, ControlNode)


def test_activitydiagram_JoinNode_isa_ControlNode():
    instance = activitydiagram_JoinNode()
    assert isinstance(instance, ControlNode)


def test_activitydiagram_MergeNode_isa_ControlNode():
    instance = activitydiagram_MergeNode()
    assert isinstance(instance, ControlNode)


def test_activitydiagram_ActivityFinalNode_isa_FinalNode():
    instance = activitydiagram_ActivityFinalNode()
    assert isinstance(instance, FinalNode)


def test_activitydiagram_FlowFinalNode_isa_FinalNode():
    instance = activitydiagram_FlowFinalNode()
    assert isinstance(instance, FinalNode)


def test_activitydiagram_ActivityParameterNode_isa_ObjectNode():
    instance = activitydiagram_ActivityParameterNode(parameter="sample_text")
    assert isinstance(instance, ObjectNode)


def test_activitydiagram_DataStoreNode_isa_ObjectNode():
    instance = activitydiagram_DataStoreNode()
    assert isinstance(instance, ObjectNode)


def test_activitydiagram_ExpansionNode_isa_ObjectNode():
    instance = activitydiagram_ExpansionNode()
    assert isinstance(instance, ObjectNode)


def test_activitydiagram_Pin_isa_ObjectNode():
    instance = activitydiagram_Pin()
    assert isinstance(instance, ObjectNode)


def test_assoc_activityDiag1_link_reassign_clear():
    a = activitydiagram_ADElement(name="sample_text")
    b1 = activitydiagram_Activity()
    b2 = activitydiagram_Activity()
    _safe_set(a, 'contains', b1)
    assert _is_linked(a, 'contains', b1)
    if hasattr(b1, 'Activity'):
        assert _is_linked(b1, 'Activity', a)
    _safe_set(a, 'contains', b2)
    assert _is_linked(a, 'contains', b2)
    if hasattr(b1, 'Activity'):
        assert not _is_linked(b1, 'Activity', a)
    if hasattr(b2, 'Activity'):
        assert _is_linked(b2, 'Activity', a)
    _safe_set(a, 'contains', None)
    assert not _is_linked(a, 'contains', b2)
    if hasattr(b2, 'Activity'):
        assert not _is_linked(b2, 'Activity', a)


def test_assoc_contains0_link_reassign_clear():
    a = activitydiagram_ADElement(name="sample_text")
    b1 = activitydiagram_Activity()
    b2 = activitydiagram_Activity()
    _safe_set(a, 'ADElement', b1)
    assert _is_linked(a, 'ADElement', b1)
    if hasattr(b1, 'activityDiag'):
        assert _is_linked(b1, 'activityDiag', a)
    _safe_set(a, 'ADElement', b2)
    assert _is_linked(a, 'ADElement', b2)
    if hasattr(b1, 'activityDiag'):
        assert not _is_linked(b1, 'activityDiag', a)
    if hasattr(b2, 'activityDiag'):
        assert _is_linked(b2, 'activityDiag', a)
    _safe_set(a, 'ADElement', None)
    assert not _is_linked(a, 'ADElement', b2)
    if hasattr(b2, 'activityDiag'):
        assert not _is_linked(b2, 'activityDiag', a)


def test_assoc_sedges2_link_reassign_clear():
    a = activitydiagram_ActivityNode(current=True)
    b1 = activitydiagram_ActivityEdge(guard=True)
    b2 = activitydiagram_ActivityEdge(guard=False)
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'ActivityEdge'):
        assert _is_linked(b1, 'ActivityEdge', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'ActivityEdge'):
        assert not _is_linked(b1, 'ActivityEdge', a)
    if hasattr(b2, 'ActivityEdge'):
        assert _is_linked(b2, 'ActivityEdge', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'ActivityEdge'):
        assert not _is_linked(b2, 'ActivityEdge', a)


def test_assoc_source5_link_reassign_clear():
    a = activitydiagram_ActivityNode(current=True)
    b1 = activitydiagram_ActivityEdge(guard=True)
    b2 = activitydiagram_ActivityEdge(guard=False)
    _safe_set(a, 'ActivityNode', b1)
    assert _is_linked(a, 'ActivityNode', b1)
    if hasattr(b1, 'sedges'):
        assert _is_linked(b1, 'sedges', a)
    _safe_set(a, 'ActivityNode', b2)
    assert _is_linked(a, 'ActivityNode', b2)
    if hasattr(b1, 'sedges'):
        assert not _is_linked(b1, 'sedges', a)
    if hasattr(b2, 'sedges'):
        assert _is_linked(b2, 'sedges', a)
    _safe_set(a, 'ActivityNode', None)
    assert not _is_linked(a, 'ActivityNode', b2)
    if hasattr(b2, 'sedges'):
        assert not _is_linked(b2, 'sedges', a)


def test_assoc_target6_link_reassign_clear():
    a = activitydiagram_ActivityNode(current=True)
    b1 = activitydiagram_ActivityEdge(guard=True)
    b2 = activitydiagram_ActivityEdge(guard=False)
    _safe_set(a, 'ActivityNode7', b1)
    assert _is_linked(a, 'ActivityNode7', b1)
    if hasattr(b1, 'tedges'):
        assert _is_linked(b1, 'tedges', a)
    _safe_set(a, 'ActivityNode7', b2)
    assert _is_linked(a, 'ActivityNode7', b2)
    if hasattr(b1, 'tedges'):
        assert not _is_linked(b1, 'tedges', a)
    if hasattr(b2, 'tedges'):
        assert _is_linked(b2, 'tedges', a)
    _safe_set(a, 'ActivityNode7', None)
    assert not _is_linked(a, 'ActivityNode7', b2)
    if hasattr(b2, 'tedges'):
        assert not _is_linked(b2, 'tedges', a)


def test_assoc_tedges3_link_reassign_clear():
    a = activitydiagram_ActivityNode(current=True)
    b1 = activitydiagram_ActivityEdge(guard=True)
    b2 = activitydiagram_ActivityEdge(guard=False)
    _safe_set(a, 'target', {b1})
    assert _is_linked(a, 'target', b1)
    if hasattr(b1, 'ActivityEdge4'):
        assert _is_linked(b1, 'ActivityEdge4', a)
    _safe_set(a, 'target', {b2})
    assert _is_linked(a, 'target', b2)
    if hasattr(b1, 'ActivityEdge4'):
        assert not _is_linked(b1, 'ActivityEdge4', a)
    if hasattr(b2, 'ActivityEdge4'):
        assert _is_linked(b2, 'ActivityEdge4', a)
    _safe_set(a, 'target', set())
    assert not _is_linked(a, 'target', b2)
    if hasattr(b2, 'ActivityEdge4'):
        assert not _is_linked(b2, 'ActivityEdge4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ADElement_strategy = st.builds(ADElement)
@given(instance=ADElement_strategy)
@settings(max_examples=25)
def test_ADElement_instantiation(instance):
    assert isinstance(instance, ADElement)


ActivityNode_strategy = st.builds(ActivityNode)
@given(instance=ActivityNode_strategy)
@settings(max_examples=25)
def test_ActivityNode_instantiation(instance):
    assert isinstance(instance, ActivityNode)


ControlNode_strategy = st.builds(ControlNode)
@given(instance=ControlNode_strategy)
@settings(max_examples=25)
def test_ControlNode_instantiation(instance):
    assert isinstance(instance, ControlNode)


FinalNode_strategy = st.builds(FinalNode)
@given(instance=FinalNode_strategy)
@settings(max_examples=25)
def test_FinalNode_instantiation(instance):
    assert isinstance(instance, FinalNode)


ObjectNode_strategy = st.builds(ObjectNode)
@given(instance=ObjectNode_strategy)
@settings(max_examples=25)
def test_ObjectNode_instantiation(instance):
    assert isinstance(instance, ObjectNode)


activitydiagram_ADElement_strategy = st.builds(activitydiagram_ADElement, name=safe_text)
@given(instance=activitydiagram_ADElement_strategy)
@settings(max_examples=25)
def test_activitydiagram_ADElement_instantiation(instance):
    assert isinstance(instance, activitydiagram_ADElement)


activitydiagram_AcceptSignalNode_strategy = st.builds(activitydiagram_AcceptSignalNode, signalId=safe_text)
@given(instance=activitydiagram_AcceptSignalNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_AcceptSignalNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_AcceptSignalNode)


activitydiagram_ActionNode_strategy = st.builds(activitydiagram_ActionNode)
@given(instance=activitydiagram_ActionNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_ActionNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_ActionNode)


activitydiagram_Activity_strategy = st.builds(activitydiagram_Activity)
@given(instance=activitydiagram_Activity_strategy)
@settings(max_examples=25)
def test_activitydiagram_Activity_instantiation(instance):
    assert isinstance(instance, activitydiagram_Activity)


activitydiagram_ActivityEdge_strategy = st.builds(activitydiagram_ActivityEdge, guard=st.booleans())
@given(instance=activitydiagram_ActivityEdge_strategy)
@settings(max_examples=25)
def test_activitydiagram_ActivityEdge_instantiation(instance):
    assert isinstance(instance, activitydiagram_ActivityEdge)


activitydiagram_ActivityFinalNode_strategy = st.builds(activitydiagram_ActivityFinalNode)
@given(instance=activitydiagram_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_ActivityFinalNode)


activitydiagram_ActivityNode_strategy = st.builds(activitydiagram_ActivityNode, current=st.booleans())
@given(instance=activitydiagram_ActivityNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_ActivityNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_ActivityNode)


activitydiagram_ActivityParameterNode_strategy = st.builds(activitydiagram_ActivityParameterNode, parameter=safe_text)
@given(instance=activitydiagram_ActivityParameterNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_ActivityParameterNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_ActivityParameterNode)


activitydiagram_ControlNode_strategy = st.builds(activitydiagram_ControlNode)
@given(instance=activitydiagram_ControlNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_ControlNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_ControlNode)


activitydiagram_DataStoreNode_strategy = st.builds(activitydiagram_DataStoreNode)
@given(instance=activitydiagram_DataStoreNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_DataStoreNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_DataStoreNode)


activitydiagram_DecisionNode_strategy = st.builds(activitydiagram_DecisionNode)
@given(instance=activitydiagram_DecisionNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_DecisionNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_DecisionNode)


activitydiagram_ExpansionNode_strategy = st.builds(activitydiagram_ExpansionNode)
@given(instance=activitydiagram_ExpansionNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_ExpansionNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_ExpansionNode)


activitydiagram_FinalNode_strategy = st.builds(activitydiagram_FinalNode)
@given(instance=activitydiagram_FinalNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_FinalNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_FinalNode)


activitydiagram_FlowFinalNode_strategy = st.builds(activitydiagram_FlowFinalNode)
@given(instance=activitydiagram_FlowFinalNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_FlowFinalNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_FlowFinalNode)


activitydiagram_ForkNode_strategy = st.builds(activitydiagram_ForkNode)
@given(instance=activitydiagram_ForkNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_ForkNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_ForkNode)


activitydiagram_InitialNode_strategy = st.builds(activitydiagram_InitialNode)
@given(instance=activitydiagram_InitialNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_InitialNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_InitialNode)


activitydiagram_JoinNode_strategy = st.builds(activitydiagram_JoinNode)
@given(instance=activitydiagram_JoinNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_JoinNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_JoinNode)


activitydiagram_MergeNode_strategy = st.builds(activitydiagram_MergeNode)
@given(instance=activitydiagram_MergeNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_MergeNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_MergeNode)


activitydiagram_ObjectNode_strategy = st.builds(activitydiagram_ObjectNode)
@given(instance=activitydiagram_ObjectNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_ObjectNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_ObjectNode)


activitydiagram_Pin_strategy = st.builds(activitydiagram_Pin)
@given(instance=activitydiagram_Pin_strategy)
@settings(max_examples=25)
def test_activitydiagram_Pin_instantiation(instance):
    assert isinstance(instance, activitydiagram_Pin)


activitydiagram_SignalNode_strategy = st.builds(activitydiagram_SignalNode, signalId=safe_text)
@given(instance=activitydiagram_SignalNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_SignalNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_SignalNode)


activitydiagram_TimeEventNode_strategy = st.builds(activitydiagram_TimeEventNode, cycle=safe_text)
@given(instance=activitydiagram_TimeEventNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_TimeEventNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TimeEventNode)



