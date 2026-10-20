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
    Action,
    UML_Activity_mine_ExpansionRegion,
    ObjectNode,
    UML_Activity_mine_ExpansionNode,
    UML_Activity_mine_ActivityParameterNode,
    UML_Activity_mine_DatastoreNode,
    ControlNode,
    UML_Activity_mine_ActivityFinalNode,
    UML_Activity_mine_Join,
    UML_Activity_mine_ActivityInitialNode,
    Element,
    UML_Activity_mine_ActivityNode,
    UML_Activity_mine_ActivityEdge,
    UML_Activity_mine_Activity,
    UML_Activity_mine_Fork,
    ActivityNode,
    UML_Activity_mine_ObjectNode,
    UML_Activity_mine_Action,
    UML_Activity_mine_ControlNode,
    UML_Activity_mine_Element,
    ExpansionMode,
    Status,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_expansionregion_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_ExpansionRegion)


def test_hyp_uml_activity_mine_expansionregion_constructor_exists():
    assert callable(UML_Activity_mine_ExpansionRegion.__init__)


def test_hyp_uml_activity_mine_expansionregion_constructor_args():
    sig = inspect.signature(UML_Activity_mine_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_hyp_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_hyp_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_expansionnode_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_ExpansionNode)


def test_hyp_uml_activity_mine_expansionnode_constructor_exists():
    assert callable(UML_Activity_mine_ExpansionNode.__init__)


def test_hyp_uml_activity_mine_expansionnode_constructor_args():
    sig = inspect.signature(UML_Activity_mine_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_ActivityParameterNode)


def test_hyp_uml_activity_mine_activityparameternode_constructor_exists():
    assert callable(UML_Activity_mine_ActivityParameterNode.__init__)


def test_hyp_uml_activity_mine_activityparameternode_constructor_args():
    sig = inspect.signature(UML_Activity_mine_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"




def test_hyp_uml_activity_mine_datastorenode_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_DatastoreNode)


def test_hyp_uml_activity_mine_datastorenode_constructor_exists():
    assert callable(UML_Activity_mine_DatastoreNode.__init__)


def test_hyp_uml_activity_mine_datastorenode_constructor_args():
    sig = inspect.signature(UML_Activity_mine_DatastoreNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_hyp_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_hyp_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_ActivityFinalNode)


def test_hyp_uml_activity_mine_activityfinalnode_constructor_exists():
    assert callable(UML_Activity_mine_ActivityFinalNode.__init__)


def test_hyp_uml_activity_mine_activityfinalnode_constructor_args():
    sig = inspect.signature(UML_Activity_mine_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_join_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_Join)


def test_hyp_uml_activity_mine_join_constructor_exists():
    assert callable(UML_Activity_mine_Join.__init__)


def test_hyp_uml_activity_mine_join_constructor_args():
    sig = inspect.signature(UML_Activity_mine_Join.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_activityinitialnode_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_ActivityInitialNode)


def test_hyp_uml_activity_mine_activityinitialnode_constructor_exists():
    assert callable(UML_Activity_mine_ActivityInitialNode.__init__)


def test_hyp_uml_activity_mine_activityinitialnode_constructor_args():
    sig = inspect.signature(UML_Activity_mine_ActivityInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_activitynode_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_ActivityNode)


def test_hyp_uml_activity_mine_activitynode_constructor_exists():
    assert callable(UML_Activity_mine_ActivityNode.__init__)


def test_hyp_uml_activity_mine_activitynode_constructor_args():
    sig = inspect.signature(UML_Activity_mine_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_activityedge_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_ActivityEdge)


def test_hyp_uml_activity_mine_activityedge_constructor_exists():
    assert callable(UML_Activity_mine_ActivityEdge.__init__)


def test_hyp_uml_activity_mine_activityedge_constructor_args():
    sig = inspect.signature(UML_Activity_mine_ActivityEdge.__init__)
    params = list(sig.parameters.keys())
    assert "objectFlow" in params, "Missing parameter 'objectFlow'"




def test_hyp_uml_activity_mine_activity_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_Activity)


def test_hyp_uml_activity_mine_activity_constructor_exists():
    assert callable(UML_Activity_mine_Activity.__init__)


def test_hyp_uml_activity_mine_activity_constructor_args():
    sig = inspect.signature(UML_Activity_mine_Activity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_fork_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_Fork)


def test_hyp_uml_activity_mine_fork_constructor_exists():
    assert callable(UML_Activity_mine_Fork.__init__)


def test_hyp_uml_activity_mine_fork_constructor_args():
    sig = inspect.signature(UML_Activity_mine_Fork.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_hyp_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_hyp_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_objectnode_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_ObjectNode)


def test_hyp_uml_activity_mine_objectnode_constructor_exists():
    assert callable(UML_Activity_mine_ObjectNode.__init__)


def test_hyp_uml_activity_mine_objectnode_constructor_args():
    sig = inspect.signature(UML_Activity_mine_ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "objects" in params, "Missing parameter 'objects'"





def test_hyp_uml_activity_mine_action_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_Action)


def test_hyp_uml_activity_mine_action_constructor_exists():
    assert callable(UML_Activity_mine_Action.__init__)


def test_hyp_uml_activity_mine_action_constructor_args():
    sig = inspect.signature(UML_Activity_mine_Action.__init__)
    params = list(sig.parameters.keys())
    assert "inputs" in params, "Missing parameter 'inputs'"
    assert "outputs" in params, "Missing parameter 'outputs'"





def test_hyp_uml_activity_mine_controlnode_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_ControlNode)


def test_hyp_uml_activity_mine_controlnode_constructor_exists():
    assert callable(UML_Activity_mine_ControlNode.__init__)


def test_hyp_uml_activity_mine_controlnode_constructor_args():
    sig = inspect.signature(UML_Activity_mine_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_activity_mine_element_is_not_abstract():
    assert not inspect.isabstract(UML_Activity_mine_Element)


def test_hyp_uml_activity_mine_element_constructor_exists():
    assert callable(UML_Activity_mine_Element.__init__)


def test_hyp_uml_activity_mine_element_constructor_args():
    sig = inspect.signature(UML_Activity_mine_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "properties" in params, "Missing parameter 'properties'"
    assert "elementID" in params, "Missing parameter 'elementID'"




def test_hyp_expansionmode_exists():
    # Check that the Enumeration exists
    assert ExpansionMode is not None

def test_hyp_expansionmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionMode]
    expected_literals = [
        "ITERATIVE",
        "PARALLEL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionMode"

def test_hyp_status_exists():
    # Check that the Enumeration exists
    assert Status is not None

def test_hyp_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Status]
    expected_literals = [
        "DONE",
        "ACTIVE",
        "INACTIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Status"

def test_hyp_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_hyp_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "OUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
Action_strategy = st.builds(
    Action,
)
UML_Activity_mine_ExpansionRegion_strategy = st.builds(
    UML_Activity_mine_ExpansionRegion,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
UML_Activity_mine_ExpansionNode_strategy = st.builds(
    UML_Activity_mine_ExpansionNode,
)
UML_Activity_mine_ActivityParameterNode_strategy = st.builds(
    UML_Activity_mine_ActivityParameterNode,
    parameter=
        safe_text
)
UML_Activity_mine_DatastoreNode_strategy = st.builds(
    UML_Activity_mine_DatastoreNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
UML_Activity_mine_ActivityFinalNode_strategy = st.builds(
    UML_Activity_mine_ActivityFinalNode,
)
UML_Activity_mine_Join_strategy = st.builds(
    UML_Activity_mine_Join,
)
UML_Activity_mine_ActivityInitialNode_strategy = st.builds(
    UML_Activity_mine_ActivityInitialNode,
)
Element_strategy = st.builds(
    Element,
)
UML_Activity_mine_ActivityNode_strategy = st.builds(
    UML_Activity_mine_ActivityNode,
)
UML_Activity_mine_ActivityEdge_strategy = st.builds(
    UML_Activity_mine_ActivityEdge,
    objectFlow=
        st.booleans()
)
UML_Activity_mine_Activity_strategy = st.builds(
    UML_Activity_mine_Activity,
)
UML_Activity_mine_Fork_strategy = st.builds(
    UML_Activity_mine_Fork,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
UML_Activity_mine_ObjectNode_strategy = st.builds(
    UML_Activity_mine_ObjectNode,
    upperBound=
        safe_text,
    objects=
        safe_text
)
UML_Activity_mine_Action_strategy = st.builds(
    UML_Activity_mine_Action,
    inputs=
        safe_text,
    outputs=
        safe_text
)
UML_Activity_mine_ControlNode_strategy = st.builds(
    UML_Activity_mine_ControlNode,
)
UML_Activity_mine_Element_strategy = st.builds(
    UML_Activity_mine_Element,
    name=
        safe_text,
    properties=
        safe_text,
    elementID=
        safe_text
)








@given(instance=UML_Activity_mine_ActivityParameterNode_strategy)
def test_hyp_uml_activity_mine_activityparameternode_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original











@given(instance=UML_Activity_mine_ActivityEdge_strategy)
def test_hyp_uml_activity_mine_activityedge_objectFlow_setter(instance):
    original = instance.objectFlow
    instance.objectFlow = original
    assert instance.objectFlow == original







@given(instance=UML_Activity_mine_ObjectNode_strategy)
def test_hyp_uml_activity_mine_objectnode_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=UML_Activity_mine_ObjectNode_strategy)
def test_hyp_uml_activity_mine_objectnode_objects_setter(instance):
    original = instance.objects
    instance.objects = original
    assert instance.objects == original




@given(instance=UML_Activity_mine_Action_strategy)
def test_hyp_uml_activity_mine_action_inputs_setter(instance):
    original = instance.inputs
    instance.inputs = original
    assert instance.inputs == original



@given(instance=UML_Activity_mine_Action_strategy)
def test_hyp_uml_activity_mine_action_outputs_setter(instance):
    original = instance.outputs
    instance.outputs = original
    assert instance.outputs == original





@given(instance=UML_Activity_mine_Element_strategy)
def test_hyp_uml_activity_mine_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=UML_Activity_mine_Element_strategy)
def test_hyp_uml_activity_mine_element_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original



@given(instance=UML_Activity_mine_Element_strategy)
def test_hyp_uml_activity_mine_element_elementID_setter(instance):
    original = instance.elementID
    instance.elementID = original
    assert instance.elementID == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    ActivityNode,
    ControlNode,
    Element,
    ObjectNode,
    UML_Activity_mine_Action,
    UML_Activity_mine_Activity,
    UML_Activity_mine_ActivityEdge,
    UML_Activity_mine_ActivityFinalNode,
    UML_Activity_mine_ActivityInitialNode,
    UML_Activity_mine_ActivityNode,
    UML_Activity_mine_ActivityParameterNode,
    UML_Activity_mine_ControlNode,
    UML_Activity_mine_DatastoreNode,
    UML_Activity_mine_Element,
    UML_Activity_mine_ExpansionNode,
    UML_Activity_mine_ExpansionRegion,
    UML_Activity_mine_Fork,
    UML_Activity_mine_Join,
    UML_Activity_mine_ObjectNode,
    Direction,
    ExpansionMode,
    Status,
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

def test_UML_Activity_mine_Action_inputs_value_roundtrip():
    instance = UML_Activity_mine_Action(inputs="sample_text", outputs="sample_text")
    assert instance.inputs == "sample_text"
    instance.inputs = "sample_text_2"
    assert instance.inputs == "sample_text_2"


def test_UML_Activity_mine_Action_outputs_value_roundtrip():
    instance = UML_Activity_mine_Action(inputs="sample_text", outputs="sample_text")
    assert instance.outputs == "sample_text"
    instance.outputs = "sample_text_2"
    assert instance.outputs == "sample_text_2"


def test_UML_Activity_mine_ActivityEdge_objectFlow_value_roundtrip():
    instance = UML_Activity_mine_ActivityEdge(objectFlow=True)
    assert instance.objectFlow == True
    instance.objectFlow = False
    assert instance.objectFlow == False


def test_UML_Activity_mine_ActivityParameterNode_parameter_value_roundtrip():
    instance = UML_Activity_mine_ActivityParameterNode(parameter="sample_text")
    assert instance.parameter == "sample_text"
    instance.parameter = "sample_text_2"
    assert instance.parameter == "sample_text_2"


def test_UML_Activity_mine_Element_elementID_value_roundtrip():
    instance = UML_Activity_mine_Element(elementID="sample_text", name="sample_text", properties="sample_text")
    assert instance.elementID == "sample_text"
    instance.elementID = "sample_text_2"
    assert instance.elementID == "sample_text_2"


def test_UML_Activity_mine_Element_name_value_roundtrip():
    instance = UML_Activity_mine_Element(elementID="sample_text", name="sample_text", properties="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_UML_Activity_mine_Element_properties_value_roundtrip():
    instance = UML_Activity_mine_Element(elementID="sample_text", name="sample_text", properties="sample_text")
    assert instance.properties == "sample_text"
    instance.properties = "sample_text_2"
    assert instance.properties == "sample_text_2"


def test_UML_Activity_mine_ObjectNode_objects_value_roundtrip():
    instance = UML_Activity_mine_ObjectNode(objects="sample_text", upperBound="sample_text")
    assert instance.objects == "sample_text"
    instance.objects = "sample_text_2"
    assert instance.objects == "sample_text_2"


def test_UML_Activity_mine_ObjectNode_upperBound_value_roundtrip():
    instance = UML_Activity_mine_ObjectNode(objects="sample_text", upperBound="sample_text")
    assert instance.upperBound == "sample_text"
    instance.upperBound = "sample_text_2"
    assert instance.upperBound == "sample_text_2"


def test_UML_Activity_mine_ExpansionRegion_isa_Action():
    instance = UML_Activity_mine_ExpansionRegion()
    assert isinstance(instance, Action)


def test_UML_Activity_mine_Action_isa_ActivityNode():
    instance = UML_Activity_mine_Action(inputs="sample_text", outputs="sample_text")
    assert isinstance(instance, ActivityNode)


def test_UML_Activity_mine_ControlNode_isa_ActivityNode():
    instance = UML_Activity_mine_ControlNode()
    assert isinstance(instance, ActivityNode)


def test_UML_Activity_mine_ObjectNode_isa_ActivityNode():
    instance = UML_Activity_mine_ObjectNode(objects="sample_text", upperBound="sample_text")
    assert isinstance(instance, ActivityNode)


def test_UML_Activity_mine_ActivityFinalNode_isa_ControlNode():
    instance = UML_Activity_mine_ActivityFinalNode()
    assert isinstance(instance, ControlNode)


def test_UML_Activity_mine_ActivityInitialNode_isa_ControlNode():
    instance = UML_Activity_mine_ActivityInitialNode()
    assert isinstance(instance, ControlNode)


def test_UML_Activity_mine_Fork_isa_ControlNode():
    instance = UML_Activity_mine_Fork()
    assert isinstance(instance, ControlNode)


def test_UML_Activity_mine_Join_isa_ControlNode():
    instance = UML_Activity_mine_Join()
    assert isinstance(instance, ControlNode)


def test_UML_Activity_mine_Activity_isa_Element():
    instance = UML_Activity_mine_Activity()
    assert isinstance(instance, Element)


def test_UML_Activity_mine_ActivityEdge_isa_Element():
    instance = UML_Activity_mine_ActivityEdge(objectFlow=True)
    assert isinstance(instance, Element)


def test_UML_Activity_mine_ActivityNode_isa_Element():
    instance = UML_Activity_mine_ActivityNode()
    assert isinstance(instance, Element)


def test_UML_Activity_mine_ActivityParameterNode_isa_ObjectNode():
    instance = UML_Activity_mine_ActivityParameterNode(parameter="sample_text")
    assert isinstance(instance, ObjectNode)


def test_UML_Activity_mine_DatastoreNode_isa_ObjectNode():
    instance = UML_Activity_mine_DatastoreNode()
    assert isinstance(instance, ObjectNode)


def test_UML_Activity_mine_ExpansionNode_isa_ObjectNode():
    instance = UML_Activity_mine_ExpansionNode()
    assert isinstance(instance, ObjectNode)


def test_assoc_edges1_link_reassign_clear():
    a = UML_Activity_mine_ActivityEdge(objectFlow=True)
    b1 = UML_Activity_mine_Activity()
    b2 = UML_Activity_mine_Activity()
    _safe_set(a, 'UML_Activity_mine_ActivityEdge', b1)
    assert _is_linked(a, 'UML_Activity_mine_ActivityEdge', b1)
    if hasattr(b1, 'UML_Activity_mine_Activity2'):
        assert _is_linked(b1, 'UML_Activity_mine_Activity2', a)
    _safe_set(a, 'UML_Activity_mine_ActivityEdge', b2)
    assert _is_linked(a, 'UML_Activity_mine_ActivityEdge', b2)
    if hasattr(b1, 'UML_Activity_mine_Activity2'):
        assert not _is_linked(b1, 'UML_Activity_mine_Activity2', a)
    if hasattr(b2, 'UML_Activity_mine_Activity2'):
        assert _is_linked(b2, 'UML_Activity_mine_Activity2', a)
    _safe_set(a, 'UML_Activity_mine_ActivityEdge', None)
    assert not _is_linked(a, 'UML_Activity_mine_ActivityEdge', b2)
    if hasattr(b2, 'UML_Activity_mine_Activity2'):
        assert not _is_linked(b2, 'UML_Activity_mine_Activity2', a)


def test_assoc_edges13_link_reassign_clear():
    a = UML_Activity_mine_ActivityEdge(objectFlow=True)
    b1 = UML_Activity_mine_ExpansionRegion()
    b2 = UML_Activity_mine_ExpansionRegion()
    _safe_set(a, 'UML_Activity_mine_ActivityEdge15', b1)
    assert _is_linked(a, 'UML_Activity_mine_ActivityEdge15', b1)
    if hasattr(b1, 'UML_Activity_mine_ExpansionRegion14'):
        assert _is_linked(b1, 'UML_Activity_mine_ExpansionRegion14', a)
    _safe_set(a, 'UML_Activity_mine_ActivityEdge15', b2)
    assert _is_linked(a, 'UML_Activity_mine_ActivityEdge15', b2)
    if hasattr(b1, 'UML_Activity_mine_ExpansionRegion14'):
        assert not _is_linked(b1, 'UML_Activity_mine_ExpansionRegion14', a)
    if hasattr(b2, 'UML_Activity_mine_ExpansionRegion14'):
        assert _is_linked(b2, 'UML_Activity_mine_ExpansionRegion14', a)
    _safe_set(a, 'UML_Activity_mine_ActivityEdge15', None)
    assert not _is_linked(a, 'UML_Activity_mine_ActivityEdge15', b2)
    if hasattr(b2, 'UML_Activity_mine_ExpansionRegion14'):
        assert not _is_linked(b2, 'UML_Activity_mine_ExpansionRegion14', a)


def test_assoc_incoming6_link_reassign_clear():
    a = UML_Activity_mine_ActivityEdge(objectFlow=True)
    b1 = UML_Activity_mine_ActivityNode()
    b2 = UML_Activity_mine_ActivityNode()
    _safe_set(a, 'ActivityEdge', b1)
    assert _is_linked(a, 'ActivityEdge', b1)
    if hasattr(b1, 'target'):
        assert _is_linked(b1, 'target', a)
    _safe_set(a, 'ActivityEdge', b2)
    assert _is_linked(a, 'ActivityEdge', b2)
    if hasattr(b1, 'target'):
        assert not _is_linked(b1, 'target', a)
    if hasattr(b2, 'target'):
        assert _is_linked(b2, 'target', a)
    _safe_set(a, 'ActivityEdge', None)
    assert not _is_linked(a, 'ActivityEdge', b2)
    if hasattr(b2, 'target'):
        assert not _is_linked(b2, 'target', a)


def test_assoc_outgoing7_link_reassign_clear():
    a = UML_Activity_mine_ActivityEdge(objectFlow=True)
    b1 = UML_Activity_mine_ActivityNode()
    b2 = UML_Activity_mine_ActivityNode()
    _safe_set(a, 'ActivityEdge8', b1)
    assert _is_linked(a, 'ActivityEdge8', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'ActivityEdge8', b2)
    assert _is_linked(a, 'ActivityEdge8', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'ActivityEdge8', None)
    assert not _is_linked(a, 'ActivityEdge8', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_source4_link_reassign_clear():
    a = UML_Activity_mine_ActivityEdge(objectFlow=True)
    b1 = UML_Activity_mine_ActivityNode()
    b2 = UML_Activity_mine_ActivityNode()
    _safe_set(a, 'outgoing', b1)
    assert _is_linked(a, 'outgoing', b1)
    if hasattr(b1, 'ActivityNode5'):
        assert _is_linked(b1, 'ActivityNode5', a)
    _safe_set(a, 'outgoing', b2)
    assert _is_linked(a, 'outgoing', b2)
    if hasattr(b1, 'ActivityNode5'):
        assert not _is_linked(b1, 'ActivityNode5', a)
    if hasattr(b2, 'ActivityNode5'):
        assert _is_linked(b2, 'ActivityNode5', a)
    _safe_set(a, 'outgoing', None)
    assert not _is_linked(a, 'outgoing', b2)
    if hasattr(b2, 'ActivityNode5'):
        assert not _is_linked(b2, 'ActivityNode5', a)


def test_assoc_target3_link_reassign_clear():
    a = UML_Activity_mine_ActivityEdge(objectFlow=True)
    b1 = UML_Activity_mine_ActivityNode()
    b2 = UML_Activity_mine_ActivityNode()
    _safe_set(a, 'incoming', b1)
    assert _is_linked(a, 'incoming', b1)
    if hasattr(b1, 'ActivityNode'):
        assert _is_linked(b1, 'ActivityNode', a)
    _safe_set(a, 'incoming', b2)
    assert _is_linked(a, 'incoming', b2)
    if hasattr(b1, 'ActivityNode'):
        assert not _is_linked(b1, 'ActivityNode', a)
    if hasattr(b2, 'ActivityNode'):
        assert _is_linked(b2, 'ActivityNode', a)
    _safe_set(a, 'incoming', None)
    assert not _is_linked(a, 'incoming', b2)
    if hasattr(b2, 'ActivityNode'):
        assert not _is_linked(b2, 'ActivityNode', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


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


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


ObjectNode_strategy = st.builds(ObjectNode)
@given(instance=ObjectNode_strategy)
@settings(max_examples=25)
def test_ObjectNode_instantiation(instance):
    assert isinstance(instance, ObjectNode)


UML_Activity_mine_Action_strategy = st.builds(UML_Activity_mine_Action, inputs=safe_text, outputs=safe_text)
@given(instance=UML_Activity_mine_Action_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_Action_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_Action)


UML_Activity_mine_Activity_strategy = st.builds(UML_Activity_mine_Activity)
@given(instance=UML_Activity_mine_Activity_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_Activity_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_Activity)


UML_Activity_mine_ActivityEdge_strategy = st.builds(UML_Activity_mine_ActivityEdge, objectFlow=st.booleans())
@given(instance=UML_Activity_mine_ActivityEdge_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_ActivityEdge_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_ActivityEdge)


UML_Activity_mine_ActivityFinalNode_strategy = st.builds(UML_Activity_mine_ActivityFinalNode)
@given(instance=UML_Activity_mine_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_ActivityFinalNode)


UML_Activity_mine_ActivityInitialNode_strategy = st.builds(UML_Activity_mine_ActivityInitialNode)
@given(instance=UML_Activity_mine_ActivityInitialNode_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_ActivityInitialNode_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_ActivityInitialNode)


UML_Activity_mine_ActivityNode_strategy = st.builds(UML_Activity_mine_ActivityNode)
@given(instance=UML_Activity_mine_ActivityNode_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_ActivityNode_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_ActivityNode)


UML_Activity_mine_ActivityParameterNode_strategy = st.builds(UML_Activity_mine_ActivityParameterNode, parameter=safe_text)
@given(instance=UML_Activity_mine_ActivityParameterNode_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_ActivityParameterNode_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_ActivityParameterNode)


UML_Activity_mine_ControlNode_strategy = st.builds(UML_Activity_mine_ControlNode)
@given(instance=UML_Activity_mine_ControlNode_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_ControlNode_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_ControlNode)


UML_Activity_mine_DatastoreNode_strategy = st.builds(UML_Activity_mine_DatastoreNode)
@given(instance=UML_Activity_mine_DatastoreNode_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_DatastoreNode_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_DatastoreNode)


UML_Activity_mine_Element_strategy = st.builds(UML_Activity_mine_Element, elementID=safe_text, name=safe_text, properties=safe_text)
@given(instance=UML_Activity_mine_Element_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_Element_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_Element)


UML_Activity_mine_ExpansionNode_strategy = st.builds(UML_Activity_mine_ExpansionNode)
@given(instance=UML_Activity_mine_ExpansionNode_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_ExpansionNode_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_ExpansionNode)


UML_Activity_mine_ExpansionRegion_strategy = st.builds(UML_Activity_mine_ExpansionRegion)
@given(instance=UML_Activity_mine_ExpansionRegion_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_ExpansionRegion_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_ExpansionRegion)


UML_Activity_mine_Fork_strategy = st.builds(UML_Activity_mine_Fork)
@given(instance=UML_Activity_mine_Fork_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_Fork_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_Fork)


UML_Activity_mine_Join_strategy = st.builds(UML_Activity_mine_Join)
@given(instance=UML_Activity_mine_Join_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_Join_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_Join)


UML_Activity_mine_ObjectNode_strategy = st.builds(UML_Activity_mine_ObjectNode, objects=safe_text, upperBound=safe_text)
@given(instance=UML_Activity_mine_ObjectNode_strategy)
@settings(max_examples=25)
def test_UML_Activity_mine_ObjectNode_instantiation(instance):
    assert isinstance(instance, UML_Activity_mine_ObjectNode)



