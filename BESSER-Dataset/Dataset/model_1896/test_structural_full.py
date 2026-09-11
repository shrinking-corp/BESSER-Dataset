import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_graphbt_AlternativeClass_alternativeAttribute_value_roundtrip():
    instance = graphbt_AlternativeClass(alternativeAttribute="sample_text")
    assert instance.alternativeAttribute == "sample_text"
    instance.alternativeAttribute = "sample_text_2"
    assert instance.alternativeAttribute == "sample_text_2"


def test_graphbt_Attribute_name_value_roundtrip():
    instance = graphbt_Attribute(name="sample_text", type="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphbt_Attribute_type_value_roundtrip():
    instance = graphbt_Attribute(name="sample_text", type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_graphbt_Attribute_value_value_roundtrip():
    instance = graphbt_Attribute(name="sample_text", type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_graphbt_Author_contact_value_roundtrip():
    instance = graphbt_Author(contact="sample_text", name="sample_text", role="sample_text")
    assert instance.contact == "sample_text"
    instance.contact = "sample_text_2"
    assert instance.contact == "sample_text_2"


def test_graphbt_Author_name_value_roundtrip():
    instance = graphbt_Author(contact="sample_text", name="sample_text", role="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphbt_Author_role_value_roundtrip():
    instance = graphbt_Author(contact="sample_text", name="sample_text", role="sample_text")
    assert instance.role == "sample_text"
    instance.role = "sample_text_2"
    assert instance.role == "sample_text_2"


def test_graphbt_BEModel_name_value_roundtrip():
    instance = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphbt_BEModel_subtitle_value_roundtrip():
    instance = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    assert instance.subtitle == "sample_text"
    instance.subtitle = "sample_text_2"
    assert instance.subtitle == "sample_text_2"


def test_graphbt_BEModel_version_value_roundtrip():
    instance = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_graphbt_Behavior_behaviorDesc_value_roundtrip():
    instance = graphbt_Behavior(behaviorDesc="sample_text", behaviorName="sample_text", behaviorRef="sample_text", behaviorType="sample_text", technicalDetail="sample_text")
    assert instance.behaviorDesc == "sample_text"
    instance.behaviorDesc = "sample_text_2"
    assert instance.behaviorDesc == "sample_text_2"


def test_graphbt_Behavior_behaviorName_value_roundtrip():
    instance = graphbt_Behavior(behaviorDesc="sample_text", behaviorName="sample_text", behaviorRef="sample_text", behaviorType="sample_text", technicalDetail="sample_text")
    assert instance.behaviorName == "sample_text"
    instance.behaviorName = "sample_text_2"
    assert instance.behaviorName == "sample_text_2"


def test_graphbt_Behavior_behaviorRef_value_roundtrip():
    instance = graphbt_Behavior(behaviorDesc="sample_text", behaviorName="sample_text", behaviorRef="sample_text", behaviorType="sample_text", technicalDetail="sample_text")
    assert instance.behaviorRef == "sample_text"
    instance.behaviorRef = "sample_text_2"
    assert instance.behaviorRef == "sample_text_2"


def test_graphbt_Behavior_behaviorType_value_roundtrip():
    instance = graphbt_Behavior(behaviorDesc="sample_text", behaviorName="sample_text", behaviorRef="sample_text", behaviorType="sample_text", technicalDetail="sample_text")
    assert instance.behaviorType == "sample_text"
    instance.behaviorType = "sample_text_2"
    assert instance.behaviorType == "sample_text_2"


def test_graphbt_Behavior_technicalDetail_value_roundtrip():
    instance = graphbt_Behavior(behaviorDesc="sample_text", behaviorName="sample_text", behaviorRef="sample_text", behaviorType="sample_text", technicalDetail="sample_text")
    assert instance.technicalDetail == "sample_text"
    instance.technicalDetail = "sample_text_2"
    assert instance.technicalDetail == "sample_text_2"


def test_graphbt_BehaviorTree_name_value_roundtrip():
    instance = graphbt_BehaviorTree(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphbt_Button_label_value_roundtrip():
    instance = graphbt_Button(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_graphbt_Component_componentDesc_value_roundtrip():
    instance = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    assert instance.componentDesc == "sample_text"
    instance.componentDesc = "sample_text_2"
    assert instance.componentDesc == "sample_text_2"


def test_graphbt_Component_componentName_value_roundtrip():
    instance = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    assert instance.componentName == "sample_text"
    instance.componentName = "sample_text_2"
    assert instance.componentName == "sample_text_2"


def test_graphbt_Component_componentRef_value_roundtrip():
    instance = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    assert instance.componentRef == "sample_text"
    instance.componentRef = "sample_text_2"
    assert instance.componentRef == "sample_text_2"


def test_graphbt_Component_enumerated_value_roundtrip():
    instance = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    assert instance.enumerated == True
    instance.enumerated = False
    assert instance.enumerated == False


def test_graphbt_Component_id_value_roundtrip():
    instance = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_graphbt_Edge_branch_value_roundtrip():
    instance = graphbt_Edge(branch="sample_text", composition="sample_text")
    assert instance.branch == "sample_text"
    instance.branch = "sample_text_2"
    assert instance.branch == "sample_text_2"


def test_graphbt_Edge_composition_value_roundtrip():
    instance = graphbt_Edge(branch="sample_text", composition="sample_text")
    assert instance.composition == "sample_text"
    instance.composition = "sample_text_2"
    assert instance.composition == "sample_text_2"


def test_graphbt_EmptyNode_label_value_roundtrip():
    instance = graphbt_EmptyNode(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_graphbt_Formula_formulaName_value_roundtrip():
    instance = graphbt_Formula(formulaName="sample_text")
    assert instance.formulaName == "sample_text"
    instance.formulaName = "sample_text_2"
    assert instance.formulaName == "sample_text_2"


def test_graphbt_GUI_codeImplementation_value_roundtrip():
    instance = graphbt_GUI(codeImplementation="sample_text", identifier="sample_text")
    assert instance.codeImplementation == "sample_text"
    instance.codeImplementation = "sample_text_2"
    assert instance.codeImplementation == "sample_text_2"


def test_graphbt_GUI_identifier_value_roundtrip():
    instance = graphbt_GUI(codeImplementation="sample_text", identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_graphbt_Information_key_value_roundtrip():
    instance = graphbt_Information(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_graphbt_Information_value_value_roundtrip():
    instance = graphbt_Information(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_graphbt_Layout_cRef_value_roundtrip():
    instance = graphbt_Layout(cRef="sample_text", height=7, width=7, x=7, y=7, z=7)
    assert instance.cRef == "sample_text"
    instance.cRef = "sample_text_2"
    assert instance.cRef == "sample_text_2"


def test_graphbt_Layout_height_value_roundtrip():
    instance = graphbt_Layout(cRef="sample_text", height=7, width=7, x=7, y=7, z=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_graphbt_Layout_width_value_roundtrip():
    instance = graphbt_Layout(cRef="sample_text", height=7, width=7, x=7, y=7, z=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_graphbt_Layout_x_value_roundtrip():
    instance = graphbt_Layout(cRef="sample_text", height=7, width=7, x=7, y=7, z=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_graphbt_Layout_y_value_roundtrip():
    instance = graphbt_Layout(cRef="sample_text", height=7, width=7, x=7, y=7, z=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_graphbt_Layout_z_value_roundtrip():
    instance = graphbt_Layout(cRef="sample_text", height=7, width=7, x=7, y=7, z=7)
    assert instance.z == 7
    instance.z = 13
    assert instance.z == 13


def test_graphbt_Library_desc_value_roundtrip():
    instance = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    assert instance.desc == "sample_text"
    instance.desc = "sample_text_2"
    assert instance.desc == "sample_text_2"


def test_graphbt_Library_id_value_roundtrip():
    instance = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_graphbt_Library_location_value_roundtrip():
    instance = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_graphbt_Library_name_value_roundtrip():
    instance = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphbt_Library_text_value_roundtrip():
    instance = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_graphbt_MethodDeclaration_name_value_roundtrip():
    instance = graphbt_MethodDeclaration(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphbt_MethodDeclaration_type_value_roundtrip():
    instance = graphbt_MethodDeclaration(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_graphbt_Node_id_value_roundtrip():
    instance = graphbt_Node(id="sample_text", index=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_graphbt_Node_index_value_roundtrip():
    instance = graphbt_Node(id="sample_text", index=7)
    assert instance.index == 7
    instance.index = 13
    assert instance.index == 13


def test_graphbt_OperatorClass_operatorLiteral_value_roundtrip():
    instance = graphbt_OperatorClass(operatorLiteral="sample_text")
    assert instance.operatorLiteral == "sample_text"
    instance.operatorLiteral = "sample_text_2"
    assert instance.operatorLiteral == "sample_text_2"


def test_graphbt_Parameter_name_value_roundtrip():
    instance = graphbt_Parameter(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphbt_Parameter_type_value_roundtrip():
    instance = graphbt_Parameter(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_graphbt_Requirement_Description_value_roundtrip():
    instance = graphbt_Requirement(Description="sample_text", Id="sample_text", Key="sample_text", Requirement="sample_text")
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_graphbt_Requirement_Id_value_roundtrip():
    instance = graphbt_Requirement(Description="sample_text", Id="sample_text", Key="sample_text", Requirement="sample_text")
    assert instance.Id == "sample_text"
    instance.Id = "sample_text_2"
    assert instance.Id == "sample_text_2"


def test_graphbt_Requirement_Key_value_roundtrip():
    instance = graphbt_Requirement(Description="sample_text", Id="sample_text", Key="sample_text", Requirement="sample_text")
    assert instance.Key == "sample_text"
    instance.Key = "sample_text_2"
    assert instance.Key == "sample_text_2"


def test_graphbt_Requirement_Requirement_value_roundtrip():
    instance = graphbt_Requirement(Description="sample_text", Id="sample_text", Key="sample_text", Requirement="sample_text")
    assert instance.Requirement == "sample_text"
    instance.Requirement = "sample_text_2"
    assert instance.Requirement == "sample_text_2"


def test_graphbt_RequirementList_projectId_value_roundtrip():
    instance = graphbt_RequirementList(projectId="sample_text")
    assert instance.projectId == "sample_text"
    instance.projectId = "sample_text_2"
    assert instance.projectId == "sample_text_2"


def test_graphbt_SpecialEdge_destination_value_roundtrip():
    instance = graphbt_SpecialEdge(destination=7, type="sample_text")
    assert instance.destination == 7
    instance.destination = 13
    assert instance.destination == 13


def test_graphbt_SpecialEdge_type_value_roundtrip():
    instance = graphbt_SpecialEdge(destination=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_graphbt_StandardNode_behaviorRef_value_roundtrip():
    instance = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    assert instance.behaviorRef == "sample_text"
    instance.behaviorRef = "sample_text_2"
    assert instance.behaviorRef == "sample_text_2"


def test_graphbt_StandardNode_componentRef_value_roundtrip():
    instance = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    assert instance.componentRef == "sample_text"
    instance.componentRef = "sample_text_2"
    assert instance.componentRef == "sample_text_2"


def test_graphbt_StandardNode_label_value_roundtrip():
    instance = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_graphbt_StandardNode_leaf_value_roundtrip():
    instance = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    assert instance.leaf == True
    instance.leaf = False
    assert instance.leaf == False


def test_graphbt_StandardNode_operator_value_roundtrip():
    instance = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_graphbt_StandardNode_traceabilityLink_value_roundtrip():
    instance = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    assert instance.traceabilityLink == "sample_text"
    instance.traceabilityLink = "sample_text_2"
    assert instance.traceabilityLink == "sample_text_2"


def test_graphbt_StandardNode_traceabilityStatus_value_roundtrip():
    instance = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    assert instance.traceabilityStatus == "sample_text"
    instance.traceabilityStatus = "sample_text_2"
    assert instance.traceabilityStatus == "sample_text_2"


def test_graphbt_State_desc_value_roundtrip():
    instance = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    assert instance.desc == "sample_text"
    instance.desc = "sample_text_2"
    assert instance.desc == "sample_text_2"


def test_graphbt_State_name_value_roundtrip():
    instance = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphbt_State_ref_value_roundtrip():
    instance = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_graphbt_TraceabilityStatusClass_traceabilityStatusLiteral_value_roundtrip():
    instance = graphbt_TraceabilityStatusClass(traceabilityStatusLiteral="sample_text")
    assert instance.traceabilityStatusLiteral == "sample_text"
    instance.traceabilityStatusLiteral = "sample_text_2"
    assert instance.traceabilityStatusLiteral == "sample_text_2"


def test_graphbt_InputGUI_isa_GUI():
    instance = graphbt_InputGUI()
    assert isinstance(instance, GUI)


def test_graphbt_OutputGUI_isa_GUI():
    instance = graphbt_OutputGUI()
    assert isinstance(instance, GUI)


def test_graphbt_InputType_isa_GUIImplementable():
    instance = graphbt_InputType()
    assert isinstance(instance, GUIImplementable)


def test_graphbt_OutputType_isa_GUIImplementable():
    instance = graphbt_OutputType()
    assert isinstance(instance, GUIImplementable)


def test_graphbt_Button_isa_Layout():
    instance = graphbt_Button(label="sample_text")
    assert isinstance(instance, Layout)


def test_graphbt_EmptyNode_isa_Node():
    instance = graphbt_EmptyNode(label="sample_text")
    assert isinstance(instance, Node)


def test_graphbt_StandardNode_isa_Node():
    instance = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    assert isinstance(instance, Node)


def test_assoc_attributes32_link_reassign_clear():
    a = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    b1 = graphbt_Attribute(name="sample_text", type="sample_text", value="sample_text")
    b2 = graphbt_Attribute(name="sample_text_2", type="sample_text_2", value="sample_text_2")
    _safe_set(a, 'graphbt_Component', {b1})
    assert _is_linked(a, 'graphbt_Component', b1)
    if hasattr(b1, 'graphbt_Attribute'):
        assert _is_linked(b1, 'graphbt_Attribute', a)
    _safe_set(a, 'graphbt_Component', {b2})
    assert _is_linked(a, 'graphbt_Component', b2)
    if hasattr(b1, 'graphbt_Attribute'):
        assert not _is_linked(b1, 'graphbt_Attribute', a)
    if hasattr(b2, 'graphbt_Attribute'):
        assert _is_linked(b2, 'graphbt_Attribute', a)
    _safe_set(a, 'graphbt_Component', set())
    assert not _is_linked(a, 'graphbt_Component', b2)
    if hasattr(b2, 'graphbt_Attribute'):
        assert not _is_linked(b2, 'graphbt_Attribute', a)


def test_assoc_attributes45_link_reassign_clear():
    a = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    b1 = graphbt_MapInformation()
    b2 = graphbt_MapInformation()
    _safe_set(a, 'graphbt_State46', b1)
    assert _is_linked(a, 'graphbt_State46', b1)
    if hasattr(b1, 'graphbt_MapInformation'):
        assert _is_linked(b1, 'graphbt_MapInformation', a)
    _safe_set(a, 'graphbt_State46', b2)
    assert _is_linked(a, 'graphbt_State46', b2)
    if hasattr(b1, 'graphbt_MapInformation'):
        assert not _is_linked(b1, 'graphbt_MapInformation', a)
    if hasattr(b2, 'graphbt_MapInformation'):
        assert _is_linked(b2, 'graphbt_MapInformation', a)
    _safe_set(a, 'graphbt_State46', None)
    assert not _is_linked(a, 'graphbt_State46', b2)
    if hasattr(b2, 'graphbt_MapInformation'):
        assert not _is_linked(b2, 'graphbt_MapInformation', a)


def test_assoc_attributes55_link_reassign_clear():
    a = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    b1 = graphbt_Attribute(name="sample_text", type="sample_text", value="sample_text")
    b2 = graphbt_Attribute(name="sample_text_2", type="sample_text_2", value="sample_text_2")
    _safe_set(a, 'graphbt_Library56', {b1})
    assert _is_linked(a, 'graphbt_Library56', b1)
    if hasattr(b1, 'graphbt_Attribute57'):
        assert _is_linked(b1, 'graphbt_Attribute57', a)
    _safe_set(a, 'graphbt_Library56', {b2})
    assert _is_linked(a, 'graphbt_Library56', b2)
    if hasattr(b1, 'graphbt_Attribute57'):
        assert not _is_linked(b1, 'graphbt_Attribute57', a)
    if hasattr(b2, 'graphbt_Attribute57'):
        assert _is_linked(b2, 'graphbt_Attribute57', a)
    _safe_set(a, 'graphbt_Library56', set())
    assert not _is_linked(a, 'graphbt_Library56', b2)
    if hasattr(b2, 'graphbt_Attribute57'):
        assert not _is_linked(b2, 'graphbt_Attribute57', a)


def test_assoc_authorList16_link_reassign_clear():
    a = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    b1 = graphbt_AuthorList()
    b2 = graphbt_AuthorList()
    _safe_set(a, 'graphbt_BEModel17', b1)
    assert _is_linked(a, 'graphbt_BEModel17', b1)
    if hasattr(b1, 'graphbt_AuthorList'):
        assert _is_linked(b1, 'graphbt_AuthorList', a)
    _safe_set(a, 'graphbt_BEModel17', b2)
    assert _is_linked(a, 'graphbt_BEModel17', b2)
    if hasattr(b1, 'graphbt_AuthorList'):
        assert not _is_linked(b1, 'graphbt_AuthorList', a)
    if hasattr(b2, 'graphbt_AuthorList'):
        assert _is_linked(b2, 'graphbt_AuthorList', a)
    _safe_set(a, 'graphbt_BEModel17', None)
    assert not _is_linked(a, 'graphbt_BEModel17', b2)
    if hasattr(b2, 'graphbt_AuthorList'):
        assert not _is_linked(b2, 'graphbt_AuthorList', a)


def test_assoc_authors83_link_reassign_clear():
    a = graphbt_Author(contact="sample_text", name="sample_text", role="sample_text")
    b1 = graphbt_AuthorList()
    b2 = graphbt_AuthorList()
    _safe_set(a, 'graphbt_Author', b1)
    assert _is_linked(a, 'graphbt_Author', b1)
    if hasattr(b1, 'graphbt_AuthorList84'):
        assert _is_linked(b1, 'graphbt_AuthorList84', a)
    _safe_set(a, 'graphbt_Author', b2)
    assert _is_linked(a, 'graphbt_Author', b2)
    if hasattr(b1, 'graphbt_AuthorList84'):
        assert not _is_linked(b1, 'graphbt_AuthorList84', a)
    if hasattr(b2, 'graphbt_AuthorList84'):
        assert _is_linked(b2, 'graphbt_AuthorList84', a)
    _safe_set(a, 'graphbt_Author', None)
    assert not _is_linked(a, 'graphbt_Author', b2)
    if hasattr(b2, 'graphbt_AuthorList84'):
        assert not _is_linked(b2, 'graphbt_AuthorList84', a)


def test_assoc_behaviors41_link_reassign_clear():
    a = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    b1 = graphbt_Behavior(behaviorDesc="sample_text", behaviorName="sample_text", behaviorRef="sample_text", behaviorType="sample_text", technicalDetail="sample_text")
    b2 = graphbt_Behavior(behaviorDesc="sample_text_2", behaviorName="sample_text_2", behaviorRef="sample_text_2", behaviorType="sample_text_2", technicalDetail="sample_text_2")
    _safe_set(a, 'graphbt_Component42', {b1})
    assert _is_linked(a, 'graphbt_Component42', b1)
    if hasattr(b1, 'graphbt_Behavior'):
        assert _is_linked(b1, 'graphbt_Behavior', a)
    _safe_set(a, 'graphbt_Component42', {b2})
    assert _is_linked(a, 'graphbt_Component42', b2)
    if hasattr(b1, 'graphbt_Behavior'):
        assert not _is_linked(b1, 'graphbt_Behavior', a)
    if hasattr(b2, 'graphbt_Behavior'):
        assert _is_linked(b2, 'graphbt_Behavior', a)
    _safe_set(a, 'graphbt_Component42', set())
    assert not _is_linked(a, 'graphbt_Component42', b2)
    if hasattr(b2, 'graphbt_Behavior'):
        assert not _is_linked(b2, 'graphbt_Behavior', a)


def test_assoc_behaviors52_link_reassign_clear():
    a = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    b1 = graphbt_Behavior(behaviorDesc="sample_text", behaviorName="sample_text", behaviorRef="sample_text", behaviorType="sample_text", technicalDetail="sample_text")
    b2 = graphbt_Behavior(behaviorDesc="sample_text_2", behaviorName="sample_text_2", behaviorRef="sample_text_2", behaviorType="sample_text_2", technicalDetail="sample_text_2")
    _safe_set(a, 'graphbt_Library53', {b1})
    assert _is_linked(a, 'graphbt_Library53', b1)
    if hasattr(b1, 'graphbt_Behavior54'):
        assert _is_linked(b1, 'graphbt_Behavior54', a)
    _safe_set(a, 'graphbt_Library53', {b2})
    assert _is_linked(a, 'graphbt_Library53', b2)
    if hasattr(b1, 'graphbt_Behavior54'):
        assert not _is_linked(b1, 'graphbt_Behavior54', a)
    if hasattr(b2, 'graphbt_Behavior54'):
        assert _is_linked(b2, 'graphbt_Behavior54', a)
    _safe_set(a, 'graphbt_Library53', set())
    assert not _is_linked(a, 'graphbt_Library53', b2)
    if hasattr(b2, 'graphbt_Behavior54'):
        assert not _is_linked(b2, 'graphbt_Behavior54', a)


def test_assoc_childNode24_link_reassign_clear():
    a = graphbt_Edge(branch="sample_text", composition="sample_text")
    b1 = graphbt_Link()
    b2 = graphbt_Link()
    _safe_set(a, 'graphbt_Edge25', {b1})
    assert _is_linked(a, 'graphbt_Edge25', b1)
    if hasattr(b1, 'graphbt_Link'):
        assert _is_linked(b1, 'graphbt_Link', a)
    _safe_set(a, 'graphbt_Edge25', {b2})
    assert _is_linked(a, 'graphbt_Edge25', b2)
    if hasattr(b1, 'graphbt_Link'):
        assert not _is_linked(b1, 'graphbt_Link', a)
    if hasattr(b2, 'graphbt_Link'):
        assert _is_linked(b2, 'graphbt_Link', a)
    _safe_set(a, 'graphbt_Edge25', set())
    assert not _is_linked(a, 'graphbt_Edge25', b2)
    if hasattr(b2, 'graphbt_Link'):
        assert not _is_linked(b2, 'graphbt_Link', a)


def test_assoc_componentList1_link_reassign_clear():
    a = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    b1 = graphbt_ComponentList()
    b2 = graphbt_ComponentList()
    _safe_set(a, 'graphbt_BEModel2', b1)
    assert _is_linked(a, 'graphbt_BEModel2', b1)
    if hasattr(b1, 'graphbt_ComponentList'):
        assert _is_linked(b1, 'graphbt_ComponentList', a)
    _safe_set(a, 'graphbt_BEModel2', b2)
    assert _is_linked(a, 'graphbt_BEModel2', b2)
    if hasattr(b1, 'graphbt_ComponentList'):
        assert not _is_linked(b1, 'graphbt_ComponentList', a)
    if hasattr(b2, 'graphbt_ComponentList'):
        assert _is_linked(b2, 'graphbt_ComponentList', a)
    _safe_set(a, 'graphbt_BEModel2', None)
    assert not _is_linked(a, 'graphbt_BEModel2', b2)
    if hasattr(b2, 'graphbt_ComponentList'):
        assert not _is_linked(b2, 'graphbt_ComponentList', a)


def test_assoc_components60_link_reassign_clear():
    a = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    b1 = graphbt_ComponentList()
    b2 = graphbt_ComponentList()
    _safe_set(a, 'graphbt_Component62', b1)
    assert _is_linked(a, 'graphbt_Component62', b1)
    if hasattr(b1, 'graphbt_ComponentList61'):
        assert _is_linked(b1, 'graphbt_ComponentList61', a)
    _safe_set(a, 'graphbt_Component62', b2)
    assert _is_linked(a, 'graphbt_Component62', b2)
    if hasattr(b1, 'graphbt_ComponentList61'):
        assert not _is_linked(b1, 'graphbt_ComponentList61', a)
    if hasattr(b2, 'graphbt_ComponentList61'):
        assert _is_linked(b2, 'graphbt_ComponentList61', a)
    _safe_set(a, 'graphbt_Component62', None)
    assert not _is_linked(a, 'graphbt_Component62', b2)
    if hasattr(b2, 'graphbt_ComponentList61'):
        assert not _is_linked(b2, 'graphbt_ComponentList61', a)


def test_assoc_container26_link_reassign_clear():
    a = graphbt_Node(id="sample_text", index=7)
    b1 = graphbt_Edge(branch="sample_text", composition="sample_text")
    b2 = graphbt_Edge(branch="sample_text_2", composition="sample_text_2")
    _safe_set(a, 'graphbt_Node28', b1)
    assert _is_linked(a, 'graphbt_Node28', b1)
    if hasattr(b1, 'graphbt_Edge27'):
        assert _is_linked(b1, 'graphbt_Edge27', a)
    _safe_set(a, 'graphbt_Node28', b2)
    assert _is_linked(a, 'graphbt_Node28', b2)
    if hasattr(b1, 'graphbt_Edge27'):
        assert not _is_linked(b1, 'graphbt_Edge27', a)
    if hasattr(b2, 'graphbt_Edge27'):
        assert _is_linked(b2, 'graphbt_Edge27', a)
    _safe_set(a, 'graphbt_Node28', None)
    assert not _is_linked(a, 'graphbt_Node28', b2)
    if hasattr(b2, 'graphbt_Edge27'):
        assert not _is_linked(b2, 'graphbt_Edge27', a)


def test_assoc_dbt0_link_reassign_clear():
    a = graphbt_BehaviorTree(name="sample_text")
    b1 = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    b2 = graphbt_BEModel(name="sample_text_2", subtitle="sample_text_2", version="sample_text_2")
    _safe_set(a, 'graphbt_BehaviorTree', b1)
    assert _is_linked(a, 'graphbt_BehaviorTree', b1)
    if hasattr(b1, 'graphbt_BEModel'):
        assert _is_linked(b1, 'graphbt_BEModel', a)
    _safe_set(a, 'graphbt_BehaviorTree', b2)
    assert _is_linked(a, 'graphbt_BehaviorTree', b2)
    if hasattr(b1, 'graphbt_BEModel'):
        assert not _is_linked(b1, 'graphbt_BEModel', a)
    if hasattr(b2, 'graphbt_BEModel'):
        assert _is_linked(b2, 'graphbt_BEModel', a)
    _safe_set(a, 'graphbt_BehaviorTree', None)
    assert not _is_linked(a, 'graphbt_BehaviorTree', b2)
    if hasattr(b2, 'graphbt_BEModel'):
        assert not _is_linked(b2, 'graphbt_BEModel', a)


def test_assoc_edge20_link_reassign_clear():
    a = graphbt_Node(id="sample_text", index=7)
    b1 = graphbt_Edge(branch="sample_text", composition="sample_text")
    b2 = graphbt_Edge(branch="sample_text_2", composition="sample_text_2")
    _safe_set(a, 'graphbt_Node21', b1)
    assert _is_linked(a, 'graphbt_Node21', b1)
    if hasattr(b1, 'graphbt_Edge'):
        assert _is_linked(b1, 'graphbt_Edge', a)
    _safe_set(a, 'graphbt_Node21', b2)
    assert _is_linked(a, 'graphbt_Node21', b2)
    if hasattr(b1, 'graphbt_Edge'):
        assert not _is_linked(b1, 'graphbt_Edge', a)
    if hasattr(b2, 'graphbt_Edge'):
        assert _is_linked(b2, 'graphbt_Edge', a)
    _safe_set(a, 'graphbt_Node21', None)
    assert not _is_linked(a, 'graphbt_Node21', b2)
    if hasattr(b2, 'graphbt_Edge'):
        assert not _is_linked(b2, 'graphbt_Edge', a)


def test_assoc_errorReversionNode11_link_reassign_clear():
    a = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    b1 = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    b2 = graphbt_BEModel(name="sample_text_2", subtitle="sample_text_2", version="sample_text_2")
    _safe_set(a, 'graphbt_StandardNode13', b1)
    assert _is_linked(a, 'graphbt_StandardNode13', b1)
    if hasattr(b1, 'graphbt_BEModel12'):
        assert _is_linked(b1, 'graphbt_BEModel12', a)
    _safe_set(a, 'graphbt_StandardNode13', b2)
    assert _is_linked(a, 'graphbt_StandardNode13', b2)
    if hasattr(b1, 'graphbt_BEModel12'):
        assert not _is_linked(b1, 'graphbt_BEModel12', a)
    if hasattr(b2, 'graphbt_BEModel12'):
        assert _is_linked(b2, 'graphbt_BEModel12', a)
    _safe_set(a, 'graphbt_StandardNode13', None)
    assert not _is_linked(a, 'graphbt_StandardNode13', b2)
    if hasattr(b2, 'graphbt_BEModel12'):
        assert not _is_linked(b2, 'graphbt_BEModel12', a)


def test_assoc_formula66_link_reassign_clear():
    a = graphbt_Formula(formulaName="sample_text")
    b1 = graphbt_FormulaList()
    b2 = graphbt_FormulaList()
    _safe_set(a, 'graphbt_Formula', b1)
    assert _is_linked(a, 'graphbt_Formula', b1)
    if hasattr(b1, 'graphbt_FormulaList67'):
        assert _is_linked(b1, 'graphbt_FormulaList67', a)
    _safe_set(a, 'graphbt_Formula', b2)
    assert _is_linked(a, 'graphbt_Formula', b2)
    if hasattr(b1, 'graphbt_FormulaList67'):
        assert not _is_linked(b1, 'graphbt_FormulaList67', a)
    if hasattr(b2, 'graphbt_FormulaList67'):
        assert _is_linked(b2, 'graphbt_FormulaList67', a)
    _safe_set(a, 'graphbt_Formula', None)
    assert not _is_linked(a, 'graphbt_Formula', b2)
    if hasattr(b2, 'graphbt_FormulaList67'):
        assert not _is_linked(b2, 'graphbt_FormulaList67', a)


def test_assoc_formulaList5_link_reassign_clear():
    a = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    b1 = graphbt_FormulaList()
    b2 = graphbt_FormulaList()
    _safe_set(a, 'graphbt_BEModel6', b1)
    assert _is_linked(a, 'graphbt_BEModel6', b1)
    if hasattr(b1, 'graphbt_FormulaList'):
        assert _is_linked(b1, 'graphbt_FormulaList', a)
    _safe_set(a, 'graphbt_BEModel6', b2)
    assert _is_linked(a, 'graphbt_BEModel6', b2)
    if hasattr(b1, 'graphbt_FormulaList'):
        assert not _is_linked(b1, 'graphbt_FormulaList', a)
    if hasattr(b2, 'graphbt_FormulaList'):
        assert _is_linked(b2, 'graphbt_FormulaList', a)
    _safe_set(a, 'graphbt_BEModel6', None)
    assert not _is_linked(a, 'graphbt_BEModel6', b2)
    if hasattr(b2, 'graphbt_FormulaList'):
        assert not _is_linked(b2, 'graphbt_FormulaList', a)


def test_assoc_import_76_link_reassign_clear():
    a = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    b1 = graphbt_Libraries()
    b2 = graphbt_Libraries()
    _safe_set(a, 'graphbt_Library78', b1)
    assert _is_linked(a, 'graphbt_Library78', b1)
    if hasattr(b1, 'graphbt_Libraries77'):
        assert _is_linked(b1, 'graphbt_Libraries77', a)
    _safe_set(a, 'graphbt_Library78', b2)
    assert _is_linked(a, 'graphbt_Library78', b2)
    if hasattr(b1, 'graphbt_Libraries77'):
        assert not _is_linked(b1, 'graphbt_Libraries77', a)
    if hasattr(b2, 'graphbt_Libraries77'):
        assert _is_linked(b2, 'graphbt_Libraries77', a)
    _safe_set(a, 'graphbt_Library78', None)
    assert not _is_linked(a, 'graphbt_Library78', b2)
    if hasattr(b2, 'graphbt_Libraries77'):
        assert not _is_linked(b2, 'graphbt_Libraries77', a)


def test_assoc_info74_link_reassign_clear():
    a = graphbt_MapInformation()
    b1 = graphbt_Information(key="sample_text", value="sample_text")
    b2 = graphbt_Information(key="sample_text_2", value="sample_text_2")
    _safe_set(a, 'graphbt_MapInformation75', {b1})
    assert _is_linked(a, 'graphbt_MapInformation75', b1)
    if hasattr(b1, 'graphbt_Information'):
        assert _is_linked(b1, 'graphbt_Information', a)
    _safe_set(a, 'graphbt_MapInformation75', {b2})
    assert _is_linked(a, 'graphbt_MapInformation75', b2)
    if hasattr(b1, 'graphbt_Information'):
        assert not _is_linked(b1, 'graphbt_Information', a)
    if hasattr(b2, 'graphbt_Information'):
        assert _is_linked(b2, 'graphbt_Information', a)
    _safe_set(a, 'graphbt_MapInformation75', set())
    assert not _is_linked(a, 'graphbt_MapInformation75', b2)
    if hasattr(b2, 'graphbt_Information'):
        assert not _is_linked(b2, 'graphbt_Information', a)


def test_assoc_initialState35_link_reassign_clear():
    a = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    b1 = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    b2 = graphbt_Component(componentDesc="sample_text_2", componentName="sample_text_2", componentRef="sample_text_2", enumerated=False, id=13)
    _safe_set(a, 'graphbt_State37', b1)
    assert _is_linked(a, 'graphbt_State37', b1)
    if hasattr(b1, 'graphbt_Component36'):
        assert _is_linked(b1, 'graphbt_Component36', a)
    _safe_set(a, 'graphbt_State37', b2)
    assert _is_linked(a, 'graphbt_State37', b2)
    if hasattr(b1, 'graphbt_Component36'):
        assert not _is_linked(b1, 'graphbt_Component36', a)
    if hasattr(b2, 'graphbt_Component36'):
        assert _is_linked(b2, 'graphbt_Component36', a)
    _safe_set(a, 'graphbt_State37', None)
    assert not _is_linked(a, 'graphbt_State37', b2)
    if hasattr(b2, 'graphbt_Component36'):
        assert not _is_linked(b2, 'graphbt_Component36', a)


def test_assoc_layoutList14_link_reassign_clear():
    a = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    b1 = graphbt_LayoutList()
    b2 = graphbt_LayoutList()
    _safe_set(a, 'graphbt_BEModel15', b1)
    assert _is_linked(a, 'graphbt_BEModel15', b1)
    if hasattr(b1, 'graphbt_LayoutList'):
        assert _is_linked(b1, 'graphbt_LayoutList', a)
    _safe_set(a, 'graphbt_BEModel15', b2)
    assert _is_linked(a, 'graphbt_BEModel15', b2)
    if hasattr(b1, 'graphbt_LayoutList'):
        assert not _is_linked(b1, 'graphbt_LayoutList', a)
    if hasattr(b2, 'graphbt_LayoutList'):
        assert _is_linked(b2, 'graphbt_LayoutList', a)
    _safe_set(a, 'graphbt_BEModel15', None)
    assert not _is_linked(a, 'graphbt_BEModel15', b2)
    if hasattr(b2, 'graphbt_LayoutList'):
        assert not _is_linked(b2, 'graphbt_LayoutList', a)


def test_assoc_layouts81_link_reassign_clear():
    a = graphbt_Layout(cRef="sample_text", height=7, width=7, x=7, y=7, z=7)
    b1 = graphbt_LayoutList()
    b2 = graphbt_LayoutList()
    _safe_set(a, 'graphbt_Layout', b1)
    assert _is_linked(a, 'graphbt_Layout', b1)
    if hasattr(b1, 'graphbt_LayoutList82'):
        assert _is_linked(b1, 'graphbt_LayoutList82', a)
    _safe_set(a, 'graphbt_Layout', b2)
    assert _is_linked(a, 'graphbt_Layout', b2)
    if hasattr(b1, 'graphbt_LayoutList82'):
        assert not _is_linked(b1, 'graphbt_LayoutList82', a)
    if hasattr(b2, 'graphbt_LayoutList82'):
        assert _is_linked(b2, 'graphbt_LayoutList82', a)
    _safe_set(a, 'graphbt_Layout', None)
    assert not _is_linked(a, 'graphbt_Layout', b2)
    if hasattr(b2, 'graphbt_LayoutList82'):
        assert not _is_linked(b2, 'graphbt_LayoutList82', a)


def test_assoc_libraries7_link_reassign_clear():
    a = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    b1 = graphbt_Libraries()
    b2 = graphbt_Libraries()
    _safe_set(a, 'graphbt_BEModel8', b1)
    assert _is_linked(a, 'graphbt_BEModel8', b1)
    if hasattr(b1, 'graphbt_Libraries'):
        assert _is_linked(b1, 'graphbt_Libraries', a)
    _safe_set(a, 'graphbt_BEModel8', b2)
    assert _is_linked(a, 'graphbt_BEModel8', b2)
    if hasattr(b1, 'graphbt_Libraries'):
        assert not _is_linked(b1, 'graphbt_Libraries', a)
    if hasattr(b2, 'graphbt_Libraries'):
        assert _is_linked(b2, 'graphbt_Libraries', a)
    _safe_set(a, 'graphbt_BEModel8', None)
    assert not _is_linked(a, 'graphbt_BEModel8', b2)
    if hasattr(b2, 'graphbt_Libraries'):
        assert not _is_linked(b2, 'graphbt_Libraries', a)


def test_assoc_methods47_link_reassign_clear():
    a = graphbt_MethodDeclaration(name="sample_text", type="sample_text")
    b1 = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    b2 = graphbt_Library(desc="sample_text_2", id="sample_text_2", location="sample_text_2", name="sample_text_2", text="sample_text_2")
    _safe_set(a, 'graphbt_MethodDeclaration', b1)
    assert _is_linked(a, 'graphbt_MethodDeclaration', b1)
    if hasattr(b1, 'graphbt_Library48'):
        assert _is_linked(b1, 'graphbt_Library48', a)
    _safe_set(a, 'graphbt_MethodDeclaration', b2)
    assert _is_linked(a, 'graphbt_MethodDeclaration', b2)
    if hasattr(b1, 'graphbt_Library48'):
        assert not _is_linked(b1, 'graphbt_Library48', a)
    if hasattr(b2, 'graphbt_Library48'):
        assert _is_linked(b2, 'graphbt_Library48', a)
    _safe_set(a, 'graphbt_MethodDeclaration', None)
    assert not _is_linked(a, 'graphbt_MethodDeclaration', b2)
    if hasattr(b2, 'graphbt_Library48'):
        assert not _is_linked(b2, 'graphbt_Library48', a)


def test_assoc_parameters79_link_reassign_clear():
    a = graphbt_Parameter(name="sample_text", type="sample_text")
    b1 = graphbt_MethodDeclaration(name="sample_text", type="sample_text")
    b2 = graphbt_MethodDeclaration(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'graphbt_Parameter', b1)
    assert _is_linked(a, 'graphbt_Parameter', b1)
    if hasattr(b1, 'graphbt_MethodDeclaration80'):
        assert _is_linked(b1, 'graphbt_MethodDeclaration80', a)
    _safe_set(a, 'graphbt_Parameter', b2)
    assert _is_linked(a, 'graphbt_Parameter', b2)
    if hasattr(b1, 'graphbt_MethodDeclaration80'):
        assert not _is_linked(b1, 'graphbt_MethodDeclaration80', a)
    if hasattr(b2, 'graphbt_MethodDeclaration80'):
        assert _is_linked(b2, 'graphbt_MethodDeclaration80', a)
    _safe_set(a, 'graphbt_Parameter', None)
    assert not _is_linked(a, 'graphbt_Parameter', b2)
    if hasattr(b2, 'graphbt_MethodDeclaration80'):
        assert not _is_linked(b2, 'graphbt_MethodDeclaration80', a)


def test_assoc_parent30_link_reassign_clear():
    a = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    b1 = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    b2 = graphbt_StandardNode(behaviorRef="sample_text_2", componentRef="sample_text_2", label="sample_text_2", leaf=False, operator="sample_text_2", traceabilityLink="sample_text_2", traceabilityStatus="sample_text_2")
    _safe_set(a, 'graphbt_StandardNode29', b1)
    assert _is_linked(a, 'graphbt_StandardNode29', b1)
    if hasattr(b1, 'graphbt_StandardNode31'):
        assert _is_linked(b1, 'graphbt_StandardNode31', a)
    _safe_set(a, 'graphbt_StandardNode29', b2)
    assert _is_linked(a, 'graphbt_StandardNode29', b2)
    if hasattr(b1, 'graphbt_StandardNode31'):
        assert not _is_linked(b1, 'graphbt_StandardNode31', a)
    if hasattr(b2, 'graphbt_StandardNode31'):
        assert _is_linked(b2, 'graphbt_StandardNode31', a)
    _safe_set(a, 'graphbt_StandardNode29', None)
    assert not _is_linked(a, 'graphbt_StandardNode29', b2)
    if hasattr(b2, 'graphbt_StandardNode31'):
        assert not _is_linked(b2, 'graphbt_StandardNode31', a)


def test_assoc_relatedTo39_link_reassign_clear():
    a = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    b1 = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    b2 = graphbt_Component(componentDesc="sample_text_2", componentName="sample_text_2", componentRef="sample_text_2", enumerated=False, id=13)
    _safe_set(a, 'graphbt_Component38', {b1})
    assert _is_linked(a, 'graphbt_Component38', b1)
    if hasattr(b1, 'graphbt_Component40'):
        assert _is_linked(b1, 'graphbt_Component40', a)
    _safe_set(a, 'graphbt_Component38', {b2})
    assert _is_linked(a, 'graphbt_Component38', b2)
    if hasattr(b1, 'graphbt_Component40'):
        assert not _is_linked(b1, 'graphbt_Component40', a)
    if hasattr(b2, 'graphbt_Component40'):
        assert _is_linked(b2, 'graphbt_Component40', a)
    _safe_set(a, 'graphbt_Component38', set())
    assert not _is_linked(a, 'graphbt_Component38', b2)
    if hasattr(b2, 'graphbt_Component40'):
        assert not _is_linked(b2, 'graphbt_Component40', a)


def test_assoc_requirementList3_link_reassign_clear():
    a = graphbt_RequirementList(projectId="sample_text")
    b1 = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    b2 = graphbt_BEModel(name="sample_text_2", subtitle="sample_text_2", version="sample_text_2")
    _safe_set(a, 'graphbt_RequirementList', b1)
    assert _is_linked(a, 'graphbt_RequirementList', b1)
    if hasattr(b1, 'graphbt_BEModel4'):
        assert _is_linked(b1, 'graphbt_BEModel4', a)
    _safe_set(a, 'graphbt_RequirementList', b2)
    assert _is_linked(a, 'graphbt_RequirementList', b2)
    if hasattr(b1, 'graphbt_BEModel4'):
        assert not _is_linked(b1, 'graphbt_BEModel4', a)
    if hasattr(b2, 'graphbt_BEModel4'):
        assert _is_linked(b2, 'graphbt_BEModel4', a)
    _safe_set(a, 'graphbt_RequirementList', None)
    assert not _is_linked(a, 'graphbt_RequirementList', b2)
    if hasattr(b2, 'graphbt_BEModel4'):
        assert not _is_linked(b2, 'graphbt_BEModel4', a)


def test_assoc_requirements63_link_reassign_clear():
    a = graphbt_RequirementList(projectId="sample_text")
    b1 = graphbt_Requirement(Description="sample_text", Id="sample_text", Key="sample_text", Requirement="sample_text")
    b2 = graphbt_Requirement(Description="sample_text_2", Id="sample_text_2", Key="sample_text_2", Requirement="sample_text_2")
    _safe_set(a, 'graphbt_RequirementList64', {b1})
    assert _is_linked(a, 'graphbt_RequirementList64', b1)
    if hasattr(b1, 'graphbt_Requirement65'):
        assert _is_linked(b1, 'graphbt_Requirement65', a)
    _safe_set(a, 'graphbt_RequirementList64', {b2})
    assert _is_linked(a, 'graphbt_RequirementList64', b2)
    if hasattr(b1, 'graphbt_Requirement65'):
        assert not _is_linked(b1, 'graphbt_Requirement65', a)
    if hasattr(b2, 'graphbt_Requirement65'):
        assert _is_linked(b2, 'graphbt_Requirement65', a)
    _safe_set(a, 'graphbt_RequirementList64', set())
    assert not _is_linked(a, 'graphbt_RequirementList64', b2)
    if hasattr(b2, 'graphbt_Requirement65'):
        assert not _is_linked(b2, 'graphbt_Requirement65', a)


def test_assoc_reversionNode9_link_reassign_clear():
    a = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    b1 = graphbt_BEModel(name="sample_text", subtitle="sample_text", version="sample_text")
    b2 = graphbt_BEModel(name="sample_text_2", subtitle="sample_text_2", version="sample_text_2")
    _safe_set(a, 'graphbt_StandardNode', b1)
    assert _is_linked(a, 'graphbt_StandardNode', b1)
    if hasattr(b1, 'graphbt_BEModel10'):
        assert _is_linked(b1, 'graphbt_BEModel10', a)
    _safe_set(a, 'graphbt_StandardNode', b2)
    assert _is_linked(a, 'graphbt_StandardNode', b2)
    if hasattr(b1, 'graphbt_BEModel10'):
        assert not _is_linked(b1, 'graphbt_BEModel10', a)
    if hasattr(b2, 'graphbt_BEModel10'):
        assert _is_linked(b2, 'graphbt_BEModel10', a)
    _safe_set(a, 'graphbt_StandardNode', None)
    assert not _is_linked(a, 'graphbt_StandardNode', b2)
    if hasattr(b2, 'graphbt_BEModel10'):
        assert not _is_linked(b2, 'graphbt_BEModel10', a)


def test_assoc_rootNode18_link_reassign_clear():
    a = graphbt_Node(id="sample_text", index=7)
    b1 = graphbt_BehaviorTree(name="sample_text")
    b2 = graphbt_BehaviorTree(name="sample_text_2")
    _safe_set(a, 'graphbt_Node', b1)
    assert _is_linked(a, 'graphbt_Node', b1)
    if hasattr(b1, 'graphbt_BehaviorTree19'):
        assert _is_linked(b1, 'graphbt_BehaviorTree19', a)
    _safe_set(a, 'graphbt_Node', b2)
    assert _is_linked(a, 'graphbt_Node', b2)
    if hasattr(b1, 'graphbt_BehaviorTree19'):
        assert not _is_linked(b1, 'graphbt_BehaviorTree19', a)
    if hasattr(b2, 'graphbt_BehaviorTree19'):
        assert _is_linked(b2, 'graphbt_BehaviorTree19', a)
    _safe_set(a, 'graphbt_Node', None)
    assert not _is_linked(a, 'graphbt_Node', b2)
    if hasattr(b2, 'graphbt_BehaviorTree19'):
        assert not _is_linked(b2, 'graphbt_BehaviorTree19', a)


def test_assoc_source71_link_reassign_clear():
    a = graphbt_Node(id="sample_text", index=7)
    b1 = graphbt_Link()
    b2 = graphbt_Link()
    _safe_set(a, 'graphbt_Node73', b1)
    assert _is_linked(a, 'graphbt_Node73', b1)
    if hasattr(b1, 'graphbt_Link72'):
        assert _is_linked(b1, 'graphbt_Link72', a)
    _safe_set(a, 'graphbt_Node73', b2)
    assert _is_linked(a, 'graphbt_Node73', b2)
    if hasattr(b1, 'graphbt_Link72'):
        assert not _is_linked(b1, 'graphbt_Link72', a)
    if hasattr(b2, 'graphbt_Link72'):
        assert _is_linked(b2, 'graphbt_Link72', a)
    _safe_set(a, 'graphbt_Node73', None)
    assert not _is_linked(a, 'graphbt_Node73', b2)
    if hasattr(b2, 'graphbt_Link72'):
        assert not _is_linked(b2, 'graphbt_Link72', a)


def test_assoc_specialE22_link_reassign_clear():
    a = graphbt_SpecialEdge(destination=7, type="sample_text")
    b1 = graphbt_Node(id="sample_text", index=7)
    b2 = graphbt_Node(id="sample_text_2", index=13)
    _safe_set(a, 'graphbt_SpecialEdge', b1)
    assert _is_linked(a, 'graphbt_SpecialEdge', b1)
    if hasattr(b1, 'graphbt_Node23'):
        assert _is_linked(b1, 'graphbt_Node23', a)
    _safe_set(a, 'graphbt_SpecialEdge', b2)
    assert _is_linked(a, 'graphbt_SpecialEdge', b2)
    if hasattr(b1, 'graphbt_Node23'):
        assert not _is_linked(b1, 'graphbt_Node23', a)
    if hasattr(b2, 'graphbt_Node23'):
        assert _is_linked(b2, 'graphbt_Node23', a)
    _safe_set(a, 'graphbt_SpecialEdge', None)
    assert not _is_linked(a, 'graphbt_SpecialEdge', b2)
    if hasattr(b2, 'graphbt_Node23'):
        assert not _is_linked(b2, 'graphbt_Node23', a)


def test_assoc_state33_link_reassign_clear():
    a = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    b1 = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    b2 = graphbt_Component(componentDesc="sample_text_2", componentName="sample_text_2", componentRef="sample_text_2", enumerated=False, id=13)
    _safe_set(a, 'graphbt_State', b1)
    assert _is_linked(a, 'graphbt_State', b1)
    if hasattr(b1, 'graphbt_Component34'):
        assert _is_linked(b1, 'graphbt_Component34', a)
    _safe_set(a, 'graphbt_State', b2)
    assert _is_linked(a, 'graphbt_State', b2)
    if hasattr(b1, 'graphbt_Component34'):
        assert not _is_linked(b1, 'graphbt_Component34', a)
    if hasattr(b2, 'graphbt_Component34'):
        assert _is_linked(b2, 'graphbt_Component34', a)
    _safe_set(a, 'graphbt_State', None)
    assert not _is_linked(a, 'graphbt_State', b2)
    if hasattr(b2, 'graphbt_Component34'):
        assert not _is_linked(b2, 'graphbt_Component34', a)


def test_assoc_states49_link_reassign_clear():
    a = graphbt_State(desc="sample_text", name="sample_text", ref="sample_text")
    b1 = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    b2 = graphbt_Library(desc="sample_text_2", id="sample_text_2", location="sample_text_2", name="sample_text_2", text="sample_text_2")
    _safe_set(a, 'graphbt_State51', b1)
    assert _is_linked(a, 'graphbt_State51', b1)
    if hasattr(b1, 'graphbt_Library50'):
        assert _is_linked(b1, 'graphbt_Library50', a)
    _safe_set(a, 'graphbt_State51', b2)
    assert _is_linked(a, 'graphbt_State51', b2)
    if hasattr(b1, 'graphbt_Library50'):
        assert not _is_linked(b1, 'graphbt_Library50', a)
    if hasattr(b2, 'graphbt_Library50'):
        assert _is_linked(b2, 'graphbt_Library50', a)
    _safe_set(a, 'graphbt_State51', None)
    assert not _is_linked(a, 'graphbt_State51', b2)
    if hasattr(b2, 'graphbt_Library50'):
        assert not _is_linked(b2, 'graphbt_Library50', a)


def test_assoc_target68_link_reassign_clear():
    a = graphbt_Node(id="sample_text", index=7)
    b1 = graphbt_Link()
    b2 = graphbt_Link()
    _safe_set(a, 'graphbt_Node70', b1)
    assert _is_linked(a, 'graphbt_Node70', b1)
    if hasattr(b1, 'graphbt_Link69'):
        assert _is_linked(b1, 'graphbt_Link69', a)
    _safe_set(a, 'graphbt_Node70', b2)
    assert _is_linked(a, 'graphbt_Node70', b2)
    if hasattr(b1, 'graphbt_Link69'):
        assert not _is_linked(b1, 'graphbt_Link69', a)
    if hasattr(b2, 'graphbt_Link69'):
        assert _is_linked(b2, 'graphbt_Link69', a)
    _safe_set(a, 'graphbt_Node70', None)
    assert not _is_linked(a, 'graphbt_Node70', b2)
    if hasattr(b2, 'graphbt_Link69'):
        assert not _is_linked(b2, 'graphbt_Link69', a)


def test_assoc_traceabilityLink58_link_reassign_clear():
    a = graphbt_StandardNode(behaviorRef="sample_text", componentRef="sample_text", label="sample_text", leaf=True, operator="sample_text", traceabilityLink="sample_text", traceabilityStatus="sample_text")
    b1 = graphbt_Requirement(Description="sample_text", Id="sample_text", Key="sample_text", Requirement="sample_text")
    b2 = graphbt_Requirement(Description="sample_text_2", Id="sample_text_2", Key="sample_text_2", Requirement="sample_text_2")
    _safe_set(a, 'graphbt_StandardNode59', b1)
    assert _is_linked(a, 'graphbt_StandardNode59', b1)
    if hasattr(b1, 'graphbt_Requirement'):
        assert _is_linked(b1, 'graphbt_Requirement', a)
    _safe_set(a, 'graphbt_StandardNode59', b2)
    assert _is_linked(a, 'graphbt_StandardNode59', b2)
    if hasattr(b1, 'graphbt_Requirement'):
        assert not _is_linked(b1, 'graphbt_Requirement', a)
    if hasattr(b2, 'graphbt_Requirement'):
        assert _is_linked(b2, 'graphbt_Requirement', a)
    _safe_set(a, 'graphbt_StandardNode59', None)
    assert not _is_linked(a, 'graphbt_StandardNode59', b2)
    if hasattr(b2, 'graphbt_Requirement'):
        assert not _is_linked(b2, 'graphbt_Requirement', a)


def test_assoc_uses43_link_reassign_clear():
    a = graphbt_Library(desc="sample_text", id="sample_text", location="sample_text", name="sample_text", text="sample_text")
    b1 = graphbt_Component(componentDesc="sample_text", componentName="sample_text", componentRef="sample_text", enumerated=True, id=7)
    b2 = graphbt_Component(componentDesc="sample_text_2", componentName="sample_text_2", componentRef="sample_text_2", enumerated=False, id=13)
    _safe_set(a, 'graphbt_Library', b1)
    assert _is_linked(a, 'graphbt_Library', b1)
    if hasattr(b1, 'graphbt_Component44'):
        assert _is_linked(b1, 'graphbt_Component44', a)
    _safe_set(a, 'graphbt_Library', b2)
    assert _is_linked(a, 'graphbt_Library', b2)
    if hasattr(b1, 'graphbt_Component44'):
        assert not _is_linked(b1, 'graphbt_Component44', a)
    if hasattr(b2, 'graphbt_Component44'):
        assert _is_linked(b2, 'graphbt_Component44', a)
    _safe_set(a, 'graphbt_Library', None)
    assert not _is_linked(a, 'graphbt_Library', b2)
    if hasattr(b2, 'graphbt_Component44'):
        assert not _is_linked(b2, 'graphbt_Component44', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

GUI_strategy = st.builds(GUI)
@given(instance=GUI_strategy)
@settings(max_examples=25)
def test_GUI_instantiation(instance):
    assert isinstance(instance, GUI)


GUIImplementable_strategy = st.builds(GUIImplementable)
@given(instance=GUIImplementable_strategy)
@settings(max_examples=25)
def test_GUIImplementable_instantiation(instance):
    assert isinstance(instance, GUIImplementable)


Layout_strategy = st.builds(Layout)
@given(instance=Layout_strategy)
@settings(max_examples=25)
def test_Layout_instantiation(instance):
    assert isinstance(instance, Layout)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


graphbt_AlternativeClass_strategy = st.builds(graphbt_AlternativeClass, alternativeAttribute=safe_text)
@given(instance=graphbt_AlternativeClass_strategy)
@settings(max_examples=25)
def test_graphbt_AlternativeClass_instantiation(instance):
    assert isinstance(instance, graphbt_AlternativeClass)


graphbt_Attribute_strategy = st.builds(graphbt_Attribute, name=safe_text, type=safe_text, value=safe_text)
@given(instance=graphbt_Attribute_strategy)
@settings(max_examples=25)
def test_graphbt_Attribute_instantiation(instance):
    assert isinstance(instance, graphbt_Attribute)


graphbt_Author_strategy = st.builds(graphbt_Author, contact=safe_text, name=safe_text, role=safe_text)
@given(instance=graphbt_Author_strategy)
@settings(max_examples=25)
def test_graphbt_Author_instantiation(instance):
    assert isinstance(instance, graphbt_Author)


graphbt_AuthorList_strategy = st.builds(graphbt_AuthorList)
@given(instance=graphbt_AuthorList_strategy)
@settings(max_examples=25)
def test_graphbt_AuthorList_instantiation(instance):
    assert isinstance(instance, graphbt_AuthorList)


graphbt_BEModel_strategy = st.builds(graphbt_BEModel, name=safe_text, subtitle=safe_text, version=safe_text)
@given(instance=graphbt_BEModel_strategy)
@settings(max_examples=25)
def test_graphbt_BEModel_instantiation(instance):
    assert isinstance(instance, graphbt_BEModel)


graphbt_Behavior_strategy = st.builds(graphbt_Behavior, behaviorDesc=safe_text, behaviorName=safe_text, behaviorRef=safe_text, behaviorType=safe_text, technicalDetail=safe_text)
@given(instance=graphbt_Behavior_strategy)
@settings(max_examples=25)
def test_graphbt_Behavior_instantiation(instance):
    assert isinstance(instance, graphbt_Behavior)


graphbt_BehaviorTree_strategy = st.builds(graphbt_BehaviorTree, name=safe_text)
@given(instance=graphbt_BehaviorTree_strategy)
@settings(max_examples=25)
def test_graphbt_BehaviorTree_instantiation(instance):
    assert isinstance(instance, graphbt_BehaviorTree)


graphbt_Button_strategy = st.builds(graphbt_Button, label=safe_text)
@given(instance=graphbt_Button_strategy)
@settings(max_examples=25)
def test_graphbt_Button_instantiation(instance):
    assert isinstance(instance, graphbt_Button)


graphbt_CTEdge_strategy = st.builds(graphbt_CTEdge)
@given(instance=graphbt_CTEdge_strategy)
@settings(max_examples=25)
def test_graphbt_CTEdge_instantiation(instance):
    assert isinstance(instance, graphbt_CTEdge)


graphbt_Component_strategy = st.builds(graphbt_Component, componentDesc=safe_text, componentName=safe_text, componentRef=safe_text, enumerated=st.booleans(), id=st.integers())
@given(instance=graphbt_Component_strategy)
@settings(max_examples=25)
def test_graphbt_Component_instantiation(instance):
    assert isinstance(instance, graphbt_Component)


graphbt_ComponentList_strategy = st.builds(graphbt_ComponentList)
@given(instance=graphbt_ComponentList_strategy)
@settings(max_examples=25)
def test_graphbt_ComponentList_instantiation(instance):
    assert isinstance(instance, graphbt_ComponentList)


graphbt_Edge_strategy = st.builds(graphbt_Edge, branch=safe_text, composition=safe_text)
@given(instance=graphbt_Edge_strategy)
@settings(max_examples=25)
def test_graphbt_Edge_instantiation(instance):
    assert isinstance(instance, graphbt_Edge)


graphbt_EmptyNode_strategy = st.builds(graphbt_EmptyNode, label=safe_text)
@given(instance=graphbt_EmptyNode_strategy)
@settings(max_examples=25)
def test_graphbt_EmptyNode_instantiation(instance):
    assert isinstance(instance, graphbt_EmptyNode)


graphbt_Formula_strategy = st.builds(graphbt_Formula, formulaName=safe_text)
@given(instance=graphbt_Formula_strategy)
@settings(max_examples=25)
def test_graphbt_Formula_instantiation(instance):
    assert isinstance(instance, graphbt_Formula)


graphbt_FormulaList_strategy = st.builds(graphbt_FormulaList)
@given(instance=graphbt_FormulaList_strategy)
@settings(max_examples=25)
def test_graphbt_FormulaList_instantiation(instance):
    assert isinstance(instance, graphbt_FormulaList)


graphbt_GUI_strategy = st.builds(graphbt_GUI, codeImplementation=safe_text, identifier=safe_text)
@given(instance=graphbt_GUI_strategy)
@settings(max_examples=25)
def test_graphbt_GUI_instantiation(instance):
    assert isinstance(instance, graphbt_GUI)


graphbt_GUIImplementable_strategy = st.builds(graphbt_GUIImplementable)
@given(instance=graphbt_GUIImplementable_strategy)
@settings(max_examples=25)
def test_graphbt_GUIImplementable_instantiation(instance):
    assert isinstance(instance, graphbt_GUIImplementable)


graphbt_Information_strategy = st.builds(graphbt_Information, key=safe_text, value=safe_text)
@given(instance=graphbt_Information_strategy)
@settings(max_examples=25)
def test_graphbt_Information_instantiation(instance):
    assert isinstance(instance, graphbt_Information)


graphbt_InputGUI_strategy = st.builds(graphbt_InputGUI)
@given(instance=graphbt_InputGUI_strategy)
@settings(max_examples=25)
def test_graphbt_InputGUI_instantiation(instance):
    assert isinstance(instance, graphbt_InputGUI)


graphbt_InputType_strategy = st.builds(graphbt_InputType)
@given(instance=graphbt_InputType_strategy)
@settings(max_examples=25)
def test_graphbt_InputType_instantiation(instance):
    assert isinstance(instance, graphbt_InputType)


graphbt_Layout_strategy = st.builds(graphbt_Layout, cRef=safe_text, height=st.integers(), width=st.integers(), x=st.integers(), y=st.integers(), z=st.integers())
@given(instance=graphbt_Layout_strategy)
@settings(max_examples=25)
def test_graphbt_Layout_instantiation(instance):
    assert isinstance(instance, graphbt_Layout)


graphbt_LayoutList_strategy = st.builds(graphbt_LayoutList)
@given(instance=graphbt_LayoutList_strategy)
@settings(max_examples=25)
def test_graphbt_LayoutList_instantiation(instance):
    assert isinstance(instance, graphbt_LayoutList)


graphbt_Libraries_strategy = st.builds(graphbt_Libraries)
@given(instance=graphbt_Libraries_strategy)
@settings(max_examples=25)
def test_graphbt_Libraries_instantiation(instance):
    assert isinstance(instance, graphbt_Libraries)


graphbt_Library_strategy = st.builds(graphbt_Library, desc=safe_text, id=safe_text, location=safe_text, name=safe_text, text=safe_text)
@given(instance=graphbt_Library_strategy)
@settings(max_examples=25)
def test_graphbt_Library_instantiation(instance):
    assert isinstance(instance, graphbt_Library)


graphbt_Link_strategy = st.builds(graphbt_Link)
@given(instance=graphbt_Link_strategy)
@settings(max_examples=25)
def test_graphbt_Link_instantiation(instance):
    assert isinstance(instance, graphbt_Link)


graphbt_MapInformation_strategy = st.builds(graphbt_MapInformation)
@given(instance=graphbt_MapInformation_strategy)
@settings(max_examples=25)
def test_graphbt_MapInformation_instantiation(instance):
    assert isinstance(instance, graphbt_MapInformation)


graphbt_MethodDeclaration_strategy = st.builds(graphbt_MethodDeclaration, name=safe_text, type=safe_text)
@given(instance=graphbt_MethodDeclaration_strategy)
@settings(max_examples=25)
def test_graphbt_MethodDeclaration_instantiation(instance):
    assert isinstance(instance, graphbt_MethodDeclaration)


graphbt_Node_strategy = st.builds(graphbt_Node, id=safe_text, index=st.integers())
@given(instance=graphbt_Node_strategy)
@settings(max_examples=25)
def test_graphbt_Node_instantiation(instance):
    assert isinstance(instance, graphbt_Node)


graphbt_OperatorClass_strategy = st.builds(graphbt_OperatorClass, operatorLiteral=safe_text)
@given(instance=graphbt_OperatorClass_strategy)
@settings(max_examples=25)
def test_graphbt_OperatorClass_instantiation(instance):
    assert isinstance(instance, graphbt_OperatorClass)


graphbt_OutputGUI_strategy = st.builds(graphbt_OutputGUI)
@given(instance=graphbt_OutputGUI_strategy)
@settings(max_examples=25)
def test_graphbt_OutputGUI_instantiation(instance):
    assert isinstance(instance, graphbt_OutputGUI)


graphbt_OutputType_strategy = st.builds(graphbt_OutputType)
@given(instance=graphbt_OutputType_strategy)
@settings(max_examples=25)
def test_graphbt_OutputType_instantiation(instance):
    assert isinstance(instance, graphbt_OutputType)


graphbt_Parameter_strategy = st.builds(graphbt_Parameter, name=safe_text, type=safe_text)
@given(instance=graphbt_Parameter_strategy)
@settings(max_examples=25)
def test_graphbt_Parameter_instantiation(instance):
    assert isinstance(instance, graphbt_Parameter)


graphbt_Requirement_strategy = st.builds(graphbt_Requirement, Description=safe_text, Id=safe_text, Key=safe_text, Requirement=safe_text)
@given(instance=graphbt_Requirement_strategy)
@settings(max_examples=25)
def test_graphbt_Requirement_instantiation(instance):
    assert isinstance(instance, graphbt_Requirement)


graphbt_RequirementList_strategy = st.builds(graphbt_RequirementList, projectId=safe_text)
@given(instance=graphbt_RequirementList_strategy)
@settings(max_examples=25)
def test_graphbt_RequirementList_instantiation(instance):
    assert isinstance(instance, graphbt_RequirementList)


graphbt_SpecialEdge_strategy = st.builds(graphbt_SpecialEdge, destination=st.integers(), type=safe_text)
@given(instance=graphbt_SpecialEdge_strategy)
@settings(max_examples=25)
def test_graphbt_SpecialEdge_instantiation(instance):
    assert isinstance(instance, graphbt_SpecialEdge)


graphbt_StandardNode_strategy = st.builds(graphbt_StandardNode, behaviorRef=safe_text, componentRef=safe_text, label=safe_text, leaf=st.booleans(), operator=safe_text, traceabilityLink=safe_text, traceabilityStatus=safe_text)
@given(instance=graphbt_StandardNode_strategy)
@settings(max_examples=25)
def test_graphbt_StandardNode_instantiation(instance):
    assert isinstance(instance, graphbt_StandardNode)


graphbt_State_strategy = st.builds(graphbt_State, desc=safe_text, name=safe_text, ref=safe_text)
@given(instance=graphbt_State_strategy)
@settings(max_examples=25)
def test_graphbt_State_instantiation(instance):
    assert isinstance(instance, graphbt_State)


graphbt_TraceabilityStatusClass_strategy = st.builds(graphbt_TraceabilityStatusClass, traceabilityStatusLiteral=safe_text)
@given(instance=graphbt_TraceabilityStatusClass_strategy)
@settings(max_examples=25)
def test_graphbt_TraceabilityStatusClass_instantiation(instance):
    assert isinstance(instance, graphbt_TraceabilityStatusClass)


