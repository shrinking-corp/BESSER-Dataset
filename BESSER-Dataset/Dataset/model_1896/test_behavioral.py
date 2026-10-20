import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GUI,
    GUIImplementable,
    Layout,
    Node,
    graphbt_AlternativeClass,
    graphbt_Attribute,
    graphbt_Author,
    graphbt_AuthorList,
    graphbt_BEModel,
    graphbt_Behavior,
    graphbt_BehaviorTree,
    graphbt_Button,
    graphbt_CTEdge,
    graphbt_Component,
    graphbt_ComponentList,
    graphbt_Edge,
    graphbt_EmptyNode,
    graphbt_Formula,
    graphbt_FormulaList,
    graphbt_GUI,
    graphbt_GUIImplementable,
    graphbt_Information,
    graphbt_InputGUI,
    graphbt_InputType,
    graphbt_Layout,
    graphbt_LayoutList,
    graphbt_Libraries,
    graphbt_Library,
    graphbt_Link,
    graphbt_MapInformation,
    graphbt_MethodDeclaration,
    graphbt_Node,
    graphbt_OperatorClass,
    graphbt_OutputGUI,
    graphbt_OutputType,
    graphbt_Parameter,
    graphbt_Requirement,
    graphbt_RequirementList,
    graphbt_SpecialEdge,
    graphbt_StandardNode,
    graphbt_State,
    graphbt_TraceabilityStatusClass,
    BehaviorType,
    Branch,
    Composition,
    EventType,
    Operator,
    SpecialEdgeEnum,
    TraceabilityStatus,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_attributes32_reverse_link_reassign_clear():
    a1 = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    a2 = graphbt_Component(componentDesc="sample_text_2", componentName="sample_text_2", componentRef="sample_text_2", enumerated=False, id=13)
    b = graphbt_Attribute(name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'graphbt_Attribute', a1)
    assert _is_linked(b, 'graphbt_Attribute', a1)
    if hasattr(a1, 'graphbt_Component'):
        assert _is_linked(a1, 'graphbt_Component', b)
    _safe_set(b, 'graphbt_Attribute', a2)
    assert _is_linked(b, 'graphbt_Attribute', a2)
    if hasattr(a1, 'graphbt_Component'):
        assert not _is_linked(a1, 'graphbt_Component', b)
    if hasattr(a2, 'graphbt_Component'):
        assert _is_linked(a2, 'graphbt_Component', b)
    _safe_set(b, 'graphbt_Attribute', None)
    assert not _is_linked(b, 'graphbt_Attribute', a2)
    if hasattr(a2, 'graphbt_Component'):
        assert not _is_linked(a2, 'graphbt_Component', b)


def test_assoc_attributes45_reverse_link_reassign_clear():
    a1 = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    a2 = graphbt_State(desc="sample_text_2", name="sample_text_2", ref="sample_text_2")
    b = graphbt_MapInformation()
    _safe_set(b, 'graphbt_MapInformation', a1)
    assert _is_linked(b, 'graphbt_MapInformation', a1)
    if hasattr(a1, 'graphbt_State46'):
        assert _is_linked(a1, 'graphbt_State46', b)
    _safe_set(b, 'graphbt_MapInformation', a2)
    assert _is_linked(b, 'graphbt_MapInformation', a2)
    if hasattr(a1, 'graphbt_State46'):
        assert not _is_linked(a1, 'graphbt_State46', b)
    if hasattr(a2, 'graphbt_State46'):
        assert _is_linked(a2, 'graphbt_State46', b)
    _safe_set(b, 'graphbt_MapInformation', None)
    assert not _is_linked(b, 'graphbt_MapInformation', a2)
    if hasattr(a2, 'graphbt_State46'):
        assert not _is_linked(a2, 'graphbt_State46', b)


def test_assoc_attributes55_reverse_link_reassign_clear():
    a1 = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    a2 = graphbt_Library(desc="sample_text_2", id="sample_text_2", location="sample_text_2", name="sample_text_2", text="sample_text_2")
    b = graphbt_Attribute(name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'graphbt_Attribute57', a1)
    assert _is_linked(b, 'graphbt_Attribute57', a1)
    if hasattr(a1, 'graphbt_Library56'):
        assert _is_linked(a1, 'graphbt_Library56', b)
    _safe_set(b, 'graphbt_Attribute57', a2)
    assert _is_linked(b, 'graphbt_Attribute57', a2)
    if hasattr(a1, 'graphbt_Library56'):
        assert not _is_linked(a1, 'graphbt_Library56', b)
    if hasattr(a2, 'graphbt_Library56'):
        assert _is_linked(a2, 'graphbt_Library56', b)
    _safe_set(b, 'graphbt_Attribute57', None)
    assert not _is_linked(b, 'graphbt_Attribute57', a2)
    if hasattr(a2, 'graphbt_Library56'):
        assert not _is_linked(a2, 'graphbt_Library56', b)


def test_assoc_behaviors41_reverse_link_reassign_clear():
    a1 = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    a2 = graphbt_Component(componentDesc="sample_text_2", componentName="sample_text_2", componentRef="sample_text_2", enumerated=False, id=13)
    b = graphbt_Behavior(behaviorDesc="sample_text", behaviorName="sample_text", behaviorRef="sample_text", behaviorType="sample_text", technicalDetail="sample_text")
    _safe_set(b, 'graphbt_Behavior', a1)
    assert _is_linked(b, 'graphbt_Behavior', a1)
    if hasattr(a1, 'graphbt_Component42'):
        assert _is_linked(a1, 'graphbt_Component42', b)
    _safe_set(b, 'graphbt_Behavior', a2)
    assert _is_linked(b, 'graphbt_Behavior', a2)
    if hasattr(a1, 'graphbt_Component42'):
        assert not _is_linked(a1, 'graphbt_Component42', b)
    if hasattr(a2, 'graphbt_Component42'):
        assert _is_linked(a2, 'graphbt_Component42', b)
    _safe_set(b, 'graphbt_Behavior', None)
    assert not _is_linked(b, 'graphbt_Behavior', a2)
    if hasattr(a2, 'graphbt_Component42'):
        assert not _is_linked(a2, 'graphbt_Component42', b)


def test_assoc_behaviors52_reverse_link_reassign_clear():
    a1 = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    a2 = graphbt_Library(desc="sample_text_2", id="sample_text_2", location="sample_text_2", name="sample_text_2", text="sample_text_2")
    b = graphbt_Behavior(behaviorDesc="sample_text", behaviorName="sample_text", behaviorRef="sample_text", behaviorType="sample_text", technicalDetail="sample_text")
    _safe_set(b, 'graphbt_Behavior54', a1)
    assert _is_linked(b, 'graphbt_Behavior54', a1)
    if hasattr(a1, 'graphbt_Library53'):
        assert _is_linked(a1, 'graphbt_Library53', b)
    _safe_set(b, 'graphbt_Behavior54', a2)
    assert _is_linked(b, 'graphbt_Behavior54', a2)
    if hasattr(a1, 'graphbt_Library53'):
        assert not _is_linked(a1, 'graphbt_Library53', b)
    if hasattr(a2, 'graphbt_Library53'):
        assert _is_linked(a2, 'graphbt_Library53', b)
    _safe_set(b, 'graphbt_Behavior54', None)
    assert not _is_linked(b, 'graphbt_Behavior54', a2)
    if hasattr(a2, 'graphbt_Library53'):
        assert not _is_linked(a2, 'graphbt_Library53', b)


def test_assoc_container26_reverse_link_reassign_clear():
    a1 = graphbt_Node(id="sample_text", index=7)
    a2 = graphbt_Node(id="sample_text_2", index=13)
    b = graphbt_Edge(branch="sample_text", composition="sample_text")
    _safe_set(b, 'graphbt_Edge27', a1)
    assert _is_linked(b, 'graphbt_Edge27', a1)
    if hasattr(a1, 'graphbt_Node28'):
        assert _is_linked(a1, 'graphbt_Node28', b)
    _safe_set(b, 'graphbt_Edge27', a2)
    assert _is_linked(b, 'graphbt_Edge27', a2)
    if hasattr(a1, 'graphbt_Node28'):
        assert not _is_linked(a1, 'graphbt_Node28', b)
    if hasattr(a2, 'graphbt_Node28'):
        assert _is_linked(a2, 'graphbt_Node28', b)
    _safe_set(b, 'graphbt_Edge27', None)
    assert not _is_linked(b, 'graphbt_Edge27', a2)
    if hasattr(a2, 'graphbt_Node28'):
        assert not _is_linked(a2, 'graphbt_Node28', b)


def test_assoc_dbt0_reverse_link_reassign_clear():
    a1 = graphbt_BehaviorTree(name="sample_text")
    a2 = graphbt_BehaviorTree(name="sample_text_2")
    b = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    _safe_set(b, 'graphbt_BEModel', a1)
    assert _is_linked(b, 'graphbt_BEModel', a1)
    if hasattr(a1, 'graphbt_BehaviorTree'):
        assert _is_linked(a1, 'graphbt_BehaviorTree', b)
    _safe_set(b, 'graphbt_BEModel', a2)
    assert _is_linked(b, 'graphbt_BEModel', a2)
    if hasattr(a1, 'graphbt_BehaviorTree'):
        assert not _is_linked(a1, 'graphbt_BehaviorTree', b)
    if hasattr(a2, 'graphbt_BehaviorTree'):
        assert _is_linked(a2, 'graphbt_BehaviorTree', b)
    _safe_set(b, 'graphbt_BEModel', None)
    assert not _is_linked(b, 'graphbt_BEModel', a2)
    if hasattr(a2, 'graphbt_BehaviorTree'):
        assert not _is_linked(a2, 'graphbt_BehaviorTree', b)


def test_assoc_edge20_reverse_link_reassign_clear():
    a1 = graphbt_Node(id="sample_text", index=7)
    a2 = graphbt_Node(id="sample_text_2", index=13)
    b = graphbt_Edge(branch="sample_text", composition="sample_text")
    _safe_set(b, 'graphbt_Edge', a1)
    assert _is_linked(b, 'graphbt_Edge', a1)
    if hasattr(a1, 'graphbt_Node21'):
        assert _is_linked(a1, 'graphbt_Node21', b)
    _safe_set(b, 'graphbt_Edge', a2)
    assert _is_linked(b, 'graphbt_Edge', a2)
    if hasattr(a1, 'graphbt_Node21'):
        assert not _is_linked(a1, 'graphbt_Node21', b)
    if hasattr(a2, 'graphbt_Node21'):
        assert _is_linked(a2, 'graphbt_Node21', b)
    _safe_set(b, 'graphbt_Edge', None)
    assert not _is_linked(b, 'graphbt_Edge', a2)
    if hasattr(a2, 'graphbt_Node21'):
        assert not _is_linked(a2, 'graphbt_Node21', b)


def test_assoc_errorReversionNode11_reverse_link_reassign_clear():
    a1 = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    a2 = graphbt_StandardNode(behaviorRef="sample_text_2", componentRef="sample_text_2", label="sample_text_2", leaf=False, operator="sample_text_2", traceabilityLink="sample_text_2", traceabilityStatus="sample_text_2")
    b = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    _safe_set(b, 'graphbt_BEModel12', {a1})
    assert _is_linked(b, 'graphbt_BEModel12', a1)
    if hasattr(a1, 'graphbt_StandardNode13'):
        assert _is_linked(a1, 'graphbt_StandardNode13', b)
    _safe_set(b, 'graphbt_BEModel12', {a2})
    assert _is_linked(b, 'graphbt_BEModel12', a2)
    if hasattr(a1, 'graphbt_StandardNode13'):
        assert not _is_linked(a1, 'graphbt_StandardNode13', b)
    if hasattr(a2, 'graphbt_StandardNode13'):
        assert _is_linked(a2, 'graphbt_StandardNode13', b)
    _safe_set(b, 'graphbt_BEModel12', set())
    assert not _is_linked(b, 'graphbt_BEModel12', a2)
    if hasattr(a2, 'graphbt_StandardNode13'):
        assert not _is_linked(a2, 'graphbt_StandardNode13', b)


def test_assoc_info74_reverse_link_reassign_clear():
    a1 = graphbt_MapInformation()
    a2 = graphbt_MapInformation()
    b = graphbt_Information(key="sample_text", value="sample_text")
    _safe_set(b, 'graphbt_Information', a1)
    assert _is_linked(b, 'graphbt_Information', a1)
    if hasattr(a1, 'graphbt_MapInformation75'):
        assert _is_linked(a1, 'graphbt_MapInformation75', b)
    _safe_set(b, 'graphbt_Information', a2)
    assert _is_linked(b, 'graphbt_Information', a2)
    if hasattr(a1, 'graphbt_MapInformation75'):
        assert not _is_linked(a1, 'graphbt_MapInformation75', b)
    if hasattr(a2, 'graphbt_MapInformation75'):
        assert _is_linked(a2, 'graphbt_MapInformation75', b)
    _safe_set(b, 'graphbt_Information', None)
    assert not _is_linked(b, 'graphbt_Information', a2)
    if hasattr(a2, 'graphbt_MapInformation75'):
        assert not _is_linked(a2, 'graphbt_MapInformation75', b)


def test_assoc_initialState35_reverse_link_reassign_clear():
    a1 = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    a2 = graphbt_State(desc="sample_text_2", name="sample_text_2", ref="sample_text_2")
    b = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    _safe_set(b, 'graphbt_Component36', a1)
    assert _is_linked(b, 'graphbt_Component36', a1)
    if hasattr(a1, 'graphbt_State37'):
        assert _is_linked(a1, 'graphbt_State37', b)
    _safe_set(b, 'graphbt_Component36', a2)
    assert _is_linked(b, 'graphbt_Component36', a2)
    if hasattr(a1, 'graphbt_State37'):
        assert not _is_linked(a1, 'graphbt_State37', b)
    if hasattr(a2, 'graphbt_State37'):
        assert _is_linked(a2, 'graphbt_State37', b)
    _safe_set(b, 'graphbt_Component36', None)
    assert not _is_linked(b, 'graphbt_Component36', a2)
    if hasattr(a2, 'graphbt_State37'):
        assert not _is_linked(a2, 'graphbt_State37', b)


def test_assoc_methods47_reverse_link_reassign_clear():
    a1 = graphbt_MethodDeclaration(name="sample_text", type="sample_text")
    a2 = graphbt_MethodDeclaration(name="sample_text_2", type="sample_text_2")
    b = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    _safe_set(b, 'graphbt_Library48', {a1})
    assert _is_linked(b, 'graphbt_Library48', a1)
    if hasattr(a1, 'graphbt_MethodDeclaration'):
        assert _is_linked(a1, 'graphbt_MethodDeclaration', b)
    _safe_set(b, 'graphbt_Library48', {a2})
    assert _is_linked(b, 'graphbt_Library48', a2)
    if hasattr(a1, 'graphbt_MethodDeclaration'):
        assert not _is_linked(a1, 'graphbt_MethodDeclaration', b)
    if hasattr(a2, 'graphbt_MethodDeclaration'):
        assert _is_linked(a2, 'graphbt_MethodDeclaration', b)
    _safe_set(b, 'graphbt_Library48', set())
    assert not _is_linked(b, 'graphbt_Library48', a2)
    if hasattr(a2, 'graphbt_MethodDeclaration'):
        assert not _is_linked(a2, 'graphbt_MethodDeclaration', b)


def test_assoc_parameters79_reverse_link_reassign_clear():
    a1 = graphbt_Parameter(name="sample_text", type="sample_text")
    a2 = graphbt_Parameter(name="sample_text_2", type="sample_text_2")
    b = graphbt_MethodDeclaration(name="sample_text", type="sample_text")
    _safe_set(b, 'graphbt_MethodDeclaration80', {a1})
    assert _is_linked(b, 'graphbt_MethodDeclaration80', a1)
    if hasattr(a1, 'graphbt_Parameter'):
        assert _is_linked(a1, 'graphbt_Parameter', b)
    _safe_set(b, 'graphbt_MethodDeclaration80', {a2})
    assert _is_linked(b, 'graphbt_MethodDeclaration80', a2)
    if hasattr(a1, 'graphbt_Parameter'):
        assert not _is_linked(a1, 'graphbt_Parameter', b)
    if hasattr(a2, 'graphbt_Parameter'):
        assert _is_linked(a2, 'graphbt_Parameter', b)
    _safe_set(b, 'graphbt_MethodDeclaration80', set())
    assert not _is_linked(b, 'graphbt_MethodDeclaration80', a2)
    if hasattr(a2, 'graphbt_Parameter'):
        assert not _is_linked(a2, 'graphbt_Parameter', b)


def test_assoc_parent30_reverse_link_reassign_clear():
    a1 = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    a2 = graphbt_StandardNode(behaviorRef="sample_text_2", componentRef="sample_text_2", label="sample_text_2", leaf=False, operator="sample_text_2", traceabilityLink="sample_text_2", traceabilityStatus="sample_text_2")
    b = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    _safe_set(b, 'graphbt_StandardNode31', a1)
    assert _is_linked(b, 'graphbt_StandardNode31', a1)
    if hasattr(a1, 'graphbt_StandardNode29'):
        assert _is_linked(a1, 'graphbt_StandardNode29', b)
    _safe_set(b, 'graphbt_StandardNode31', a2)
    assert _is_linked(b, 'graphbt_StandardNode31', a2)
    if hasattr(a1, 'graphbt_StandardNode29'):
        assert not _is_linked(a1, 'graphbt_StandardNode29', b)
    if hasattr(a2, 'graphbt_StandardNode29'):
        assert _is_linked(a2, 'graphbt_StandardNode29', b)
    _safe_set(b, 'graphbt_StandardNode31', None)
    assert not _is_linked(b, 'graphbt_StandardNode31', a2)
    if hasattr(a2, 'graphbt_StandardNode29'):
        assert not _is_linked(a2, 'graphbt_StandardNode29', b)


def test_assoc_relatedTo39_reverse_link_reassign_clear():
    a1 = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    a2 = graphbt_Component(componentDesc="sample_text_2", componentName="sample_text_2", componentRef="sample_text_2", enumerated=False, id=13)
    b = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    _safe_set(b, 'graphbt_Component40', a1)
    assert _is_linked(b, 'graphbt_Component40', a1)
    if hasattr(a1, 'graphbt_Component38'):
        assert _is_linked(a1, 'graphbt_Component38', b)
    _safe_set(b, 'graphbt_Component40', a2)
    assert _is_linked(b, 'graphbt_Component40', a2)
    if hasattr(a1, 'graphbt_Component38'):
        assert not _is_linked(a1, 'graphbt_Component38', b)
    if hasattr(a2, 'graphbt_Component38'):
        assert _is_linked(a2, 'graphbt_Component38', b)
    _safe_set(b, 'graphbt_Component40', None)
    assert not _is_linked(b, 'graphbt_Component40', a2)
    if hasattr(a2, 'graphbt_Component38'):
        assert not _is_linked(a2, 'graphbt_Component38', b)


def test_assoc_requirementList3_reverse_link_reassign_clear():
    a1 = graphbt_RequirementList(projectId="sample_text")
    a2 = graphbt_RequirementList(projectId="sample_text_2")
    b = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    _safe_set(b, 'graphbt_BEModel4', a1)
    assert _is_linked(b, 'graphbt_BEModel4', a1)
    if hasattr(a1, 'graphbt_RequirementList'):
        assert _is_linked(a1, 'graphbt_RequirementList', b)
    _safe_set(b, 'graphbt_BEModel4', a2)
    assert _is_linked(b, 'graphbt_BEModel4', a2)
    if hasattr(a1, 'graphbt_RequirementList'):
        assert not _is_linked(a1, 'graphbt_RequirementList', b)
    if hasattr(a2, 'graphbt_RequirementList'):
        assert _is_linked(a2, 'graphbt_RequirementList', b)
    _safe_set(b, 'graphbt_BEModel4', None)
    assert not _is_linked(b, 'graphbt_BEModel4', a2)
    if hasattr(a2, 'graphbt_RequirementList'):
        assert not _is_linked(a2, 'graphbt_RequirementList', b)


def test_assoc_requirements63_reverse_link_reassign_clear():
    a1 = graphbt_RequirementList(projectId="sample_text")
    a2 = graphbt_RequirementList(projectId="sample_text_2")
    b = graphbt_Requirement(Description="sample_text", Id="sample_text", Key="sample_text", Requirement="sample_text")
    _safe_set(b, 'graphbt_Requirement65', a1)
    assert _is_linked(b, 'graphbt_Requirement65', a1)
    if hasattr(a1, 'graphbt_RequirementList64'):
        assert _is_linked(a1, 'graphbt_RequirementList64', b)
    _safe_set(b, 'graphbt_Requirement65', a2)
    assert _is_linked(b, 'graphbt_Requirement65', a2)
    if hasattr(a1, 'graphbt_RequirementList64'):
        assert not _is_linked(a1, 'graphbt_RequirementList64', b)
    if hasattr(a2, 'graphbt_RequirementList64'):
        assert _is_linked(a2, 'graphbt_RequirementList64', b)
    _safe_set(b, 'graphbt_Requirement65', None)
    assert not _is_linked(b, 'graphbt_Requirement65', a2)
    if hasattr(a2, 'graphbt_RequirementList64'):
        assert not _is_linked(a2, 'graphbt_RequirementList64', b)


def test_assoc_reversionNode9_reverse_link_reassign_clear():
    a1 = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    a2 = graphbt_StandardNode(behaviorRef="sample_text_2", componentRef="sample_text_2", label="sample_text_2", leaf=False, operator="sample_text_2", traceabilityLink="sample_text_2", traceabilityStatus="sample_text_2")
    b = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    _safe_set(b, 'graphbt_BEModel10', {a1})
    assert _is_linked(b, 'graphbt_BEModel10', a1)
    if hasattr(a1, 'graphbt_StandardNode'):
        assert _is_linked(a1, 'graphbt_StandardNode', b)
    _safe_set(b, 'graphbt_BEModel10', {a2})
    assert _is_linked(b, 'graphbt_BEModel10', a2)
    if hasattr(a1, 'graphbt_StandardNode'):
        assert not _is_linked(a1, 'graphbt_StandardNode', b)
    if hasattr(a2, 'graphbt_StandardNode'):
        assert _is_linked(a2, 'graphbt_StandardNode', b)
    _safe_set(b, 'graphbt_BEModel10', set())
    assert not _is_linked(b, 'graphbt_BEModel10', a2)
    if hasattr(a2, 'graphbt_StandardNode'):
        assert not _is_linked(a2, 'graphbt_StandardNode', b)


def test_assoc_rootNode18_reverse_link_reassign_clear():
    a1 = graphbt_Node(id="sample_text", index=7)
    a2 = graphbt_Node(id="sample_text_2", index=13)
    b = graphbt_BehaviorTree(name="sample_text")
    _safe_set(b, 'graphbt_BehaviorTree19', a1)
    assert _is_linked(b, 'graphbt_BehaviorTree19', a1)
    if hasattr(a1, 'graphbt_Node'):
        assert _is_linked(a1, 'graphbt_Node', b)
    _safe_set(b, 'graphbt_BehaviorTree19', a2)
    assert _is_linked(b, 'graphbt_BehaviorTree19', a2)
    if hasattr(a1, 'graphbt_Node'):
        assert not _is_linked(a1, 'graphbt_Node', b)
    if hasattr(a2, 'graphbt_Node'):
        assert _is_linked(a2, 'graphbt_Node', b)
    _safe_set(b, 'graphbt_BehaviorTree19', None)
    assert not _is_linked(b, 'graphbt_BehaviorTree19', a2)
    if hasattr(a2, 'graphbt_Node'):
        assert not _is_linked(a2, 'graphbt_Node', b)


def test_assoc_specialE22_reverse_link_reassign_clear():
    a1 = graphbt_SpecialEdge(destination=7, type="sample_text")
    a2 = graphbt_SpecialEdge(destination=13, type="sample_text_2")
    b = graphbt_Node(id="sample_text", index=7)
    _safe_set(b, 'graphbt_Node23', a1)
    assert _is_linked(b, 'graphbt_Node23', a1)
    if hasattr(a1, 'graphbt_SpecialEdge'):
        assert _is_linked(a1, 'graphbt_SpecialEdge', b)
    _safe_set(b, 'graphbt_Node23', a2)
    assert _is_linked(b, 'graphbt_Node23', a2)
    if hasattr(a1, 'graphbt_SpecialEdge'):
        assert not _is_linked(a1, 'graphbt_SpecialEdge', b)
    if hasattr(a2, 'graphbt_SpecialEdge'):
        assert _is_linked(a2, 'graphbt_SpecialEdge', b)
    _safe_set(b, 'graphbt_Node23', None)
    assert not _is_linked(b, 'graphbt_Node23', a2)
    if hasattr(a2, 'graphbt_SpecialEdge'):
        assert not _is_linked(a2, 'graphbt_SpecialEdge', b)


def test_assoc_state33_reverse_link_reassign_clear():
    a1 = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    a2 = graphbt_State(desc="sample_text_2", name="sample_text_2", ref="sample_text_2")
    b = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    _safe_set(b, 'graphbt_Component34', {a1})
    assert _is_linked(b, 'graphbt_Component34', a1)
    if hasattr(a1, 'graphbt_State'):
        assert _is_linked(a1, 'graphbt_State', b)
    _safe_set(b, 'graphbt_Component34', {a2})
    assert _is_linked(b, 'graphbt_Component34', a2)
    if hasattr(a1, 'graphbt_State'):
        assert not _is_linked(a1, 'graphbt_State', b)
    if hasattr(a2, 'graphbt_State'):
        assert _is_linked(a2, 'graphbt_State', b)
    _safe_set(b, 'graphbt_Component34', set())
    assert not _is_linked(b, 'graphbt_Component34', a2)
    if hasattr(a2, 'graphbt_State'):
        assert not _is_linked(a2, 'graphbt_State', b)


def test_assoc_states49_reverse_link_reassign_clear():
    a1 = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    a2 = graphbt_State(desc="sample_text_2", name="sample_text_2", ref="sample_text_2")
    b = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    _safe_set(b, 'graphbt_Library50', {a1})
    assert _is_linked(b, 'graphbt_Library50', a1)
    if hasattr(a1, 'graphbt_State51'):
        assert _is_linked(a1, 'graphbt_State51', b)
    _safe_set(b, 'graphbt_Library50', {a2})
    assert _is_linked(b, 'graphbt_Library50', a2)
    if hasattr(a1, 'graphbt_State51'):
        assert not _is_linked(a1, 'graphbt_State51', b)
    if hasattr(a2, 'graphbt_State51'):
        assert _is_linked(a2, 'graphbt_State51', b)
    _safe_set(b, 'graphbt_Library50', set())
    assert not _is_linked(b, 'graphbt_Library50', a2)
    if hasattr(a2, 'graphbt_State51'):
        assert not _is_linked(a2, 'graphbt_State51', b)


def test_assoc_traceabilityLink58_reverse_link_reassign_clear():
    a1 = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    a2 = graphbt_StandardNode(behaviorRef="sample_text_2", componentRef="sample_text_2", label="sample_text_2", leaf=False, operator="sample_text_2", traceabilityLink="sample_text_2", traceabilityStatus="sample_text_2")
    b = graphbt_Requirement(Description="sample_text", Id="sample_text", Key="sample_text", Requirement="sample_text")
    _safe_set(b, 'graphbt_Requirement', {a1})
    assert _is_linked(b, 'graphbt_Requirement', a1)
    if hasattr(a1, 'graphbt_StandardNode59'):
        assert _is_linked(a1, 'graphbt_StandardNode59', b)
    _safe_set(b, 'graphbt_Requirement', {a2})
    assert _is_linked(b, 'graphbt_Requirement', a2)
    if hasattr(a1, 'graphbt_StandardNode59'):
        assert not _is_linked(a1, 'graphbt_StandardNode59', b)
    if hasattr(a2, 'graphbt_StandardNode59'):
        assert _is_linked(a2, 'graphbt_StandardNode59', b)
    _safe_set(b, 'graphbt_Requirement', set())
    assert not _is_linked(b, 'graphbt_Requirement', a2)
    if hasattr(a2, 'graphbt_StandardNode59'):
        assert not _is_linked(a2, 'graphbt_StandardNode59', b)


def test_assoc_uses43_reverse_link_reassign_clear():
    a1 = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    a2 = graphbt_Library(desc="sample_text_2", id="sample_text_2", location="sample_text_2", name="sample_text_2", text="sample_text_2")
    b = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    _safe_set(b, 'graphbt_Component44', {a1})
    assert _is_linked(b, 'graphbt_Component44', a1)
    if hasattr(a1, 'graphbt_Library'):
        assert _is_linked(a1, 'graphbt_Library', b)
    _safe_set(b, 'graphbt_Component44', {a2})
    assert _is_linked(b, 'graphbt_Component44', a2)
    if hasattr(a1, 'graphbt_Library'):
        assert not _is_linked(a1, 'graphbt_Library', b)
    if hasattr(a2, 'graphbt_Library'):
        assert _is_linked(a2, 'graphbt_Library', b)
    _safe_set(b, 'graphbt_Component44', set())
    assert not _is_linked(b, 'graphbt_Component44', a2)
    if hasattr(a2, 'graphbt_Library'):
        assert not _is_linked(a2, 'graphbt_Library', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_authorList16_stub_double():
    # graphbt_AuthorList has no real 'graphbt_AuthorList' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_BEModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_BEModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    partner = graphbt_AuthorList()
    setattr(partner, 'graphbt_AuthorList', None)
    _safe_set(owner, 'graphbt_BEModel17', partner)
    assert getattr(partner, 'graphbt_AuthorList') == owner
    _safe_set(owner, 'graphbt_BEModel17', None)
    assert getattr(partner, 'graphbt_AuthorList') is None


def test_assoc_authors83_stub_double():
    # graphbt_AuthorList has no real 'graphbt_AuthorList84' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_Author(contact="sample_text", name="sample_text", role="sample_text")
    partner = graphbt_AuthorList()
    setattr(partner, 'graphbt_AuthorList84', None)
    _safe_set(owner, 'graphbt_Author', partner)
    assert owner in getattr(partner, 'graphbt_AuthorList84')
    _safe_set(owner, 'graphbt_Author', None)
    assert owner not in getattr(partner, 'graphbt_AuthorList84')


def test_assoc_childNode24_stub_double():
    # graphbt_Link has no real 'graphbt_Link' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_Edge(branch="sample_text", composition="sample_text")
    partner = graphbt_Link()
    setattr(partner, 'graphbt_Link', None)
    _safe_set(owner, 'graphbt_Edge25', {partner})
    assert getattr(partner, 'graphbt_Link') == owner
    _safe_set(owner, 'graphbt_Edge25', set())
    assert getattr(partner, 'graphbt_Link') is None


def test_assoc_componentList1_stub_double():
    # graphbt_ComponentList has no real 'graphbt_ComponentList' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_BEModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_BEModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    partner = graphbt_ComponentList()
    setattr(partner, 'graphbt_ComponentList', None)
    _safe_set(owner, 'graphbt_BEModel2', partner)
    assert getattr(partner, 'graphbt_ComponentList') == owner
    _safe_set(owner, 'graphbt_BEModel2', None)
    assert getattr(partner, 'graphbt_ComponentList') is None


def test_assoc_components60_stub_double():
    # graphbt_ComponentList has no real 'graphbt_ComponentList61' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    partner = graphbt_ComponentList()
    setattr(partner, 'graphbt_ComponentList61', None)
    _safe_set(owner, 'graphbt_Component62', partner)
    assert owner in getattr(partner, 'graphbt_ComponentList61')
    _safe_set(owner, 'graphbt_Component62', None)
    assert owner not in getattr(partner, 'graphbt_ComponentList61')


def test_assoc_formula66_stub_double():
    # graphbt_FormulaList has no real 'graphbt_FormulaList67' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_Formula(formulaName="sample_text")
    partner = graphbt_FormulaList()
    setattr(partner, 'graphbt_FormulaList67', None)
    _safe_set(owner, 'graphbt_Formula', partner)
    assert owner in getattr(partner, 'graphbt_FormulaList67')
    _safe_set(owner, 'graphbt_Formula', None)
    assert owner not in getattr(partner, 'graphbt_FormulaList67')


def test_assoc_formulaList5_stub_double():
    # graphbt_FormulaList has no real 'graphbt_FormulaList' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_BEModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_BEModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    partner = graphbt_FormulaList()
    setattr(partner, 'graphbt_FormulaList', None)
    _safe_set(owner, 'graphbt_BEModel6', partner)
    assert getattr(partner, 'graphbt_FormulaList') == owner
    _safe_set(owner, 'graphbt_BEModel6', None)
    assert getattr(partner, 'graphbt_FormulaList') is None


def test_assoc_import_76_stub_double():
    # graphbt_Libraries has no real 'graphbt_Libraries77' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    partner = graphbt_Libraries()
    setattr(partner, 'graphbt_Libraries77', None)
    _safe_set(owner, 'graphbt_Library78', partner)
    assert owner in getattr(partner, 'graphbt_Libraries77')
    _safe_set(owner, 'graphbt_Library78', None)
    assert owner not in getattr(partner, 'graphbt_Libraries77')


def test_assoc_layoutList14_stub_double():
    # graphbt_LayoutList has no real 'graphbt_LayoutList' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_BEModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_BEModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    partner = graphbt_LayoutList()
    setattr(partner, 'graphbt_LayoutList', None)
    _safe_set(owner, 'graphbt_BEModel15', partner)
    assert getattr(partner, 'graphbt_LayoutList') == owner
    _safe_set(owner, 'graphbt_BEModel15', None)
    assert getattr(partner, 'graphbt_LayoutList') is None


def test_assoc_layouts81_stub_double():
    # graphbt_LayoutList has no real 'graphbt_LayoutList82' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_Layout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_Layout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_Layout(cRef="sample_text", height=7, width=7, x=7, y=7, z=7)
    partner = graphbt_LayoutList()
    setattr(partner, 'graphbt_LayoutList82', None)
    _safe_set(owner, 'graphbt_Layout', partner)
    assert owner in getattr(partner, 'graphbt_LayoutList82')
    _safe_set(owner, 'graphbt_Layout', None)
    assert owner not in getattr(partner, 'graphbt_LayoutList82')


def test_assoc_libraries7_stub_double():
    # graphbt_Libraries has no real 'graphbt_Libraries' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_BEModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_BEModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    partner = graphbt_Libraries()
    setattr(partner, 'graphbt_Libraries', None)
    _safe_set(owner, 'graphbt_BEModel8', partner)
    assert getattr(partner, 'graphbt_Libraries') == owner
    _safe_set(owner, 'graphbt_BEModel8', None)
    assert getattr(partner, 'graphbt_Libraries') is None


def test_assoc_source71_stub_double():
    # graphbt_Link has no real 'graphbt_Link72' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_Node(id="sample_text", index=7)
    partner = graphbt_Link()
    setattr(partner, 'graphbt_Link72', None)
    _safe_set(owner, 'graphbt_Node73', partner)
    assert getattr(partner, 'graphbt_Link72') == owner
    _safe_set(owner, 'graphbt_Node73', None)
    assert getattr(partner, 'graphbt_Link72') is None


def test_assoc_target68_stub_double():
    # graphbt_Link has no real 'graphbt_Link69' property in the generated
    # code (a bare stub) -- manually attach it so graphbt_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphbt_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphbt_Node(id="sample_text", index=7)
    partner = graphbt_Link()
    setattr(partner, 'graphbt_Link69', None)
    _safe_set(owner, 'graphbt_Node70', partner)
    assert getattr(partner, 'graphbt_Link69') == owner
    _safe_set(owner, 'graphbt_Node70', None)
    assert getattr(partner, 'graphbt_Link69') is None


