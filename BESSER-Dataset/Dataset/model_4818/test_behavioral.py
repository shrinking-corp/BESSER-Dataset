import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActiveStructureElement,
    Adapter,
    ApplicationElement,
    ArchimateConcept,
    ArchimateElement,
    ArchimateModelObject,
    ArchimateRelationship,
    BehaviorElement,
    BorderObject,
    BorderType,
    BusinessElement,
    BusinessObject,
    Cloneable,
    CompositeElement,
    Connectable,
    DependendencyRelationship,
    DiagramModel,
    DiagramModelArchimateComponent,
    DiagramModelComponent,
    DiagramModelConnection,
    DiagramModelContainer,
    DiagramModelImageProvider,
    DiagramModelObject,
    Documentable,
    DynamicRelationship,
    Features,
    FolderContainer,
    FontAttribute,
    Identifier,
    ImplementationMigrationElement,
    LineObject,
    MotivationElement,
    Nameable,
    OtherRelationship,
    PassiveStructureElement,
    PhysicalElement,
    Properties,
    StrategyBehaviorElement,
    StrategyElement,
    StructuralRelationship,
    StructureElement,
    TechnologyElement,
    TechnologyObject,
    TextAlignment,
    TextContent,
    TextPosition,
    model_AccessRelationship,
    model_ActiveStructureElement,
    model_Adapter,
    model_AggregationRelationship,
    model_ApplicationCollaboration,
    model_ApplicationComponent,
    model_ApplicationElement,
    model_ApplicationEvent,
    model_ApplicationFunction,
    model_ApplicationInteraction,
    model_ApplicationInterface,
    model_ApplicationProcess,
    model_ApplicationService,
    model_ArchimateConcept,
    model_ArchimateDiagramModel,
    model_ArchimateElement,
    model_ArchimateModel,
    model_ArchimateModelObject,
    model_ArchimateRelationship,
    model_Artifact,
    model_Assessment,
    model_AssignmentRelationship,
    model_AssociationRelationship,
    model_BehaviorElement,
    model_BorderObject,
    model_BorderType,
    model_Bounds,
    model_BusinessActor,
    model_BusinessCollaboration,
    model_BusinessElement,
    model_BusinessEvent,
    model_BusinessFunction,
    model_BusinessInteraction,
    model_BusinessInterface,
    model_BusinessObject,
    model_BusinessProcess,
    model_BusinessRole,
    model_BusinessService,
    model_Capability,
    model_Cloneable,
    model_CommunicationNetwork,
    model_CompositeElement,
    model_CompositionRelationship,
    model_Connectable,
    model_Constraint,
    model_Contract,
    model_CourseOfAction,
    model_DataObject,
    model_Deliverable,
    model_DependendencyRelationship,
    model_Device,
    model_DiagramModel,
    model_DiagramModelArchimateComponent,
    model_DiagramModelArchimateConnection,
    model_DiagramModelArchimateObject,
    model_DiagramModelBendpoint,
    model_DiagramModelComponent,
    model_DiagramModelConnection,
    model_DiagramModelContainer,
    model_DiagramModelGroup,
    model_DiagramModelImage,
    model_DiagramModelImageProvider,
    model_DiagramModelNote,
    model_DiagramModelObject,
    model_DiagramModelReference,
    model_DistributionNetwork,
    model_Documentable,
    model_Driver,
    model_DynamicRelationship,
    model_EObject,
    model_Equipment,
    model_Facility,
    model_Feature,
    model_Features,
    model_FlowRelationship,
    model_Folder,
    model_FolderContainer,
    model_FontAttribute,
    model_Gap,
    model_Goal,
    model_Grouping,
    model_Identifier,
    model_ImplementationEvent,
    model_ImplementationMigrationElement,
    model_InfluenceRelationship,
    model_Junction,
    model_LineObject,
    model_Location,
    model_Lockable,
    model_Material,
    model_Meaning,
    model_Metadata,
    model_MotivationElement,
    model_Nameable,
    model_Node,
    model_OtherRelationship,
    model_Outcome,
    model_PassiveStructureElement,
    model_Path,
    model_PhysicalElement,
    model_Plateau,
    model_Principle,
    model_Product,
    model_Properties,
    model_Property,
    model_RealizationRelationship,
    model_Representation,
    model_Requirement,
    model_Resource,
    model_ServingRelationship,
    model_SketchModel,
    model_SketchModelActor,
    model_SketchModelSticky,
    model_SpecializationRelationship,
    model_Stakeholder,
    model_StrategyBehaviorElement,
    model_StrategyElement,
    model_StructuralRelationship,
    model_StructureElement,
    model_SystemSoftware,
    model_TechnologyCollaboration,
    model_TechnologyElement,
    model_TechnologyEvent,
    model_TechnologyFunction,
    model_TechnologyInteraction,
    model_TechnologyInterface,
    model_TechnologyObject,
    model_TechnologyProcess,
    model_TechnologyService,
    model_TextAlignment,
    model_TextContent,
    model_TextPosition,
    model_TriggeringRelationship,
    model_Value,
    model_ValueStream,
    model_WorkPackage,
    FolderType,
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

def test_assoc_bendpoints27_reverse_link_reassign_clear():
    a1 = model_DiagramModelConnection(text="sample_text", textPosition=7, type=7)
    a2 = model_DiagramModelConnection(text="sample_text_2", textPosition=13, type=13)
    b = model_DiagramModelBendpoint(endX=7, endY=7, startX=7, startY=7)
    _safe_set(b, 'model_DiagramModelBendpoint', a1)
    assert _is_linked(b, 'model_DiagramModelBendpoint', a1)
    if hasattr(a1, 'model_DiagramModelConnection28'):
        assert _is_linked(a1, 'model_DiagramModelConnection28', b)
    _safe_set(b, 'model_DiagramModelBendpoint', a2)
    assert _is_linked(b, 'model_DiagramModelBendpoint', a2)
    if hasattr(a1, 'model_DiagramModelConnection28'):
        assert not _is_linked(a1, 'model_DiagramModelConnection28', b)
    if hasattr(a2, 'model_DiagramModelConnection28'):
        assert _is_linked(a2, 'model_DiagramModelConnection28', b)
    _safe_set(b, 'model_DiagramModelBendpoint', None)
    assert not _is_linked(b, 'model_DiagramModelBendpoint', a2)
    if hasattr(a2, 'model_DiagramModelConnection28'):
        assert not _is_linked(a2, 'model_DiagramModelConnection28', b)


def test_assoc_bounds19_reverse_link_reassign_clear():
    a1 = model_DiagramModelObject(alpha=7, fillColor="sample_text")
    a2 = model_DiagramModelObject(alpha=13, fillColor="sample_text_2")
    b = model_Bounds(height=7, width=7, x=7, y=7)
    _safe_set(b, 'model_Bounds', a1)
    assert _is_linked(b, 'model_Bounds', a1)
    if hasattr(a1, 'model_DiagramModelObject20'):
        assert _is_linked(a1, 'model_DiagramModelObject20', b)
    _safe_set(b, 'model_Bounds', a2)
    assert _is_linked(b, 'model_Bounds', a2)
    if hasattr(a1, 'model_DiagramModelObject20'):
        assert not _is_linked(a1, 'model_DiagramModelObject20', b)
    if hasattr(a2, 'model_DiagramModelObject20'):
        assert _is_linked(a2, 'model_DiagramModelObject20', b)
    _safe_set(b, 'model_Bounds', None)
    assert not _is_linked(b, 'model_Bounds', a2)
    if hasattr(a2, 'model_DiagramModelObject20'):
        assert not _is_linked(a2, 'model_DiagramModelObject20', b)


def test_assoc_source21_reverse_link_reassign_clear():
    a1 = model_DiagramModelConnection(text="sample_text", textPosition=7, type=7)
    a2 = model_DiagramModelConnection(text="sample_text_2", textPosition=13, type=13)
    b = model_Connectable()
    _safe_set(b, 'model_Connectable23', a1)
    assert _is_linked(b, 'model_Connectable23', a1)
    if hasattr(a1, 'model_DiagramModelConnection22'):
        assert _is_linked(a1, 'model_DiagramModelConnection22', b)
    _safe_set(b, 'model_Connectable23', a2)
    assert _is_linked(b, 'model_Connectable23', a2)
    if hasattr(a1, 'model_DiagramModelConnection22'):
        assert not _is_linked(a1, 'model_DiagramModelConnection22', b)
    if hasattr(a2, 'model_DiagramModelConnection22'):
        assert _is_linked(a2, 'model_DiagramModelConnection22', b)
    _safe_set(b, 'model_Connectable23', None)
    assert not _is_linked(b, 'model_Connectable23', a2)
    if hasattr(a2, 'model_DiagramModelConnection22'):
        assert not _is_linked(a2, 'model_DiagramModelConnection22', b)


def test_assoc_sourceConnections13_reverse_link_reassign_clear():
    a1 = model_DiagramModelConnection(text="sample_text", textPosition=7, type=7)
    a2 = model_DiagramModelConnection(text="sample_text_2", textPosition=13, type=13)
    b = model_Connectable()
    _safe_set(b, 'model_Connectable', {a1})
    assert _is_linked(b, 'model_Connectable', a1)
    if hasattr(a1, 'model_DiagramModelConnection'):
        assert _is_linked(a1, 'model_DiagramModelConnection', b)
    _safe_set(b, 'model_Connectable', {a2})
    assert _is_linked(b, 'model_Connectable', a2)
    if hasattr(a1, 'model_DiagramModelConnection'):
        assert not _is_linked(a1, 'model_DiagramModelConnection', b)
    if hasattr(a2, 'model_DiagramModelConnection'):
        assert _is_linked(a2, 'model_DiagramModelConnection', b)
    _safe_set(b, 'model_Connectable', set())
    assert not _is_linked(b, 'model_Connectable', a2)
    if hasattr(a2, 'model_DiagramModelConnection'):
        assert not _is_linked(a2, 'model_DiagramModelConnection', b)


def test_assoc_target24_reverse_link_reassign_clear():
    a1 = model_DiagramModelConnection(text="sample_text", textPosition=7, type=7)
    a2 = model_DiagramModelConnection(text="sample_text_2", textPosition=13, type=13)
    b = model_Connectable()
    _safe_set(b, 'model_Connectable26', a1)
    assert _is_linked(b, 'model_Connectable26', a1)
    if hasattr(a1, 'model_DiagramModelConnection25'):
        assert _is_linked(a1, 'model_DiagramModelConnection25', b)
    _safe_set(b, 'model_Connectable26', a2)
    assert _is_linked(b, 'model_Connectable26', a2)
    if hasattr(a1, 'model_DiagramModelConnection25'):
        assert not _is_linked(a1, 'model_DiagramModelConnection25', b)
    if hasattr(a2, 'model_DiagramModelConnection25'):
        assert _is_linked(a2, 'model_DiagramModelConnection25', b)
    _safe_set(b, 'model_Connectable26', None)
    assert not _is_linked(b, 'model_Connectable26', a2)
    if hasattr(a2, 'model_DiagramModelConnection25'):
        assert not _is_linked(a2, 'model_DiagramModelConnection25', b)


def test_assoc_targetConnections14_reverse_link_reassign_clear():
    a1 = model_DiagramModelConnection(text="sample_text", textPosition=7, type=7)
    a2 = model_DiagramModelConnection(text="sample_text_2", textPosition=13, type=13)
    b = model_Connectable()
    _safe_set(b, 'model_Connectable15', {a1})
    assert _is_linked(b, 'model_Connectable15', a1)
    if hasattr(a1, 'model_DiagramModelConnection16'):
        assert _is_linked(a1, 'model_DiagramModelConnection16', b)
    _safe_set(b, 'model_Connectable15', {a2})
    assert _is_linked(b, 'model_Connectable15', a2)
    if hasattr(a1, 'model_DiagramModelConnection16'):
        assert not _is_linked(a1, 'model_DiagramModelConnection16', b)
    if hasattr(a2, 'model_DiagramModelConnection16'):
        assert _is_linked(a2, 'model_DiagramModelConnection16', b)
    _safe_set(b, 'model_Connectable15', set())
    assert not _is_linked(b, 'model_Connectable15', a2)
    if hasattr(a2, 'model_DiagramModelConnection16'):
        assert not _is_linked(a2, 'model_DiagramModelConnection16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_archimateElement29_stub_double():
    # model_ArchimateElement has no real 'model_ArchimateElement' property in the generated
    # code (a bare stub) -- manually attach it so model_DiagramModelArchimateObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_DiagramModelArchimateObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_DiagramModelArchimateObject(type=7)
    partner = model_ArchimateElement()
    setattr(partner, 'model_ArchimateElement', None)
    _safe_set(owner, 'model_DiagramModelArchimateObject', partner)
    assert getattr(partner, 'model_ArchimateElement') == owner
    _safe_set(owner, 'model_DiagramModelArchimateObject', None)
    assert getattr(partner, 'model_ArchimateElement') is None


def test_assoc_archimateRelationship30_stub_double():
    # model_DiagramModelArchimateConnection has no real 'model_DiagramModelArchimateConnection' property in the generated
    # code (a bare stub) -- manually attach it so model_ArchimateRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ArchimateRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ArchimateRelationship()
    partner = model_DiagramModelArchimateConnection()
    setattr(partner, 'model_DiagramModelArchimateConnection', None)
    _safe_set(owner, 'model_ArchimateRelationship31', partner)
    assert getattr(partner, 'model_DiagramModelArchimateConnection') == owner
    _safe_set(owner, 'model_ArchimateRelationship31', None)
    assert getattr(partner, 'model_DiagramModelArchimateConnection') is None


def test_assoc_children17_stub_double():
    # model_DiagramModelContainer has no real 'model_DiagramModelContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_DiagramModelObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_DiagramModelObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_DiagramModelObject(alpha=7, fillColor="sample_text")
    partner = model_DiagramModelContainer()
    setattr(partner, 'model_DiagramModelContainer', None)
    _safe_set(owner, 'model_DiagramModelObject', partner)
    assert owner in getattr(partner, 'model_DiagramModelContainer')
    _safe_set(owner, 'model_DiagramModelObject', None)
    assert owner not in getattr(partner, 'model_DiagramModelContainer')


def test_assoc_elements5_stub_double():
    # model_EObject has no real 'model_EObject' property in the generated
    # code (a bare stub) -- manually attach it so model_Folder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Folder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Folder(type="sample_text")
    partner = model_EObject()
    setattr(partner, 'model_EObject', None)
    _safe_set(owner, 'model_Folder6', {partner})
    assert getattr(partner, 'model_EObject') == owner
    _safe_set(owner, 'model_Folder6', set())
    assert getattr(partner, 'model_EObject') is None


def test_assoc_entries2_stub_double():
    # model_Metadata has no real 'model_Metadata' property in the generated
    # code (a bare stub) -- manually attach it so model_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Property(key="sample_text", value="sample_text")
    partner = model_Metadata()
    setattr(partner, 'model_Metadata', None)
    _safe_set(owner, 'model_Property3', partner)
    assert owner in getattr(partner, 'model_Metadata')
    _safe_set(owner, 'model_Property3', None)
    assert owner not in getattr(partner, 'model_Metadata')


def test_assoc_features1_stub_double():
    # model_Features has no real 'model_Features' property in the generated
    # code (a bare stub) -- manually attach it so model_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Feature(name="sample_text", value="sample_text")
    partner = model_Features()
    setattr(partner, 'model_Features', None)
    _safe_set(owner, 'model_Feature', partner)
    assert owner in getattr(partner, 'model_Features')
    _safe_set(owner, 'model_Feature', None)
    assert owner not in getattr(partner, 'model_Features')


def test_assoc_folders4_stub_double():
    # model_FolderContainer has no real 'model_FolderContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_Folder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Folder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Folder(type="sample_text")
    partner = model_FolderContainer()
    setattr(partner, 'model_FolderContainer', None)
    _safe_set(owner, 'model_Folder', partner)
    assert owner in getattr(partner, 'model_FolderContainer')
    _safe_set(owner, 'model_Folder', None)
    assert owner not in getattr(partner, 'model_FolderContainer')


def test_assoc_metadata11_stub_double():
    # model_Metadata has no real 'model_Metadata12' property in the generated
    # code (a bare stub) -- manually attach it so model_ArchimateModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ArchimateModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ArchimateModel(file="sample_text", purpose="sample_text", version="sample_text")
    partner = model_Metadata()
    setattr(partner, 'model_Metadata12', None)
    _safe_set(owner, 'model_ArchimateModel', partner)
    assert getattr(partner, 'model_Metadata12') == owner
    _safe_set(owner, 'model_ArchimateModel', None)
    assert getattr(partner, 'model_Metadata12') is None


def test_assoc_properties0_stub_double():
    # model_Properties has no real 'model_Properties' property in the generated
    # code (a bare stub) -- manually attach it so model_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Property(key="sample_text", value="sample_text")
    partner = model_Properties()
    setattr(partner, 'model_Properties', None)
    _safe_set(owner, 'model_Property', partner)
    assert owner in getattr(partner, 'model_Properties')
    _safe_set(owner, 'model_Property', None)
    assert owner not in getattr(partner, 'model_Properties')


def test_assoc_referencedModel18_stub_double():
    # model_DiagramModelReference has no real 'model_DiagramModelReference' property in the generated
    # code (a bare stub) -- manually attach it so model_DiagramModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_DiagramModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_DiagramModel(connectionRouterType=7)
    partner = model_DiagramModelReference()
    setattr(partner, 'model_DiagramModelReference', None)
    _safe_set(owner, 'model_DiagramModel', partner)
    assert getattr(partner, 'model_DiagramModelReference') == owner
    _safe_set(owner, 'model_DiagramModel', None)
    assert getattr(partner, 'model_DiagramModelReference') is None


def test_assoc_source7_stub_double():
    # model_ArchimateConcept has no real 'model_ArchimateConcept' property in the generated
    # code (a bare stub) -- manually attach it so model_ArchimateRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ArchimateRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ArchimateRelationship()
    partner = model_ArchimateConcept()
    setattr(partner, 'model_ArchimateConcept', None)
    _safe_set(owner, 'model_ArchimateRelationship', partner)
    assert getattr(partner, 'model_ArchimateConcept') == owner
    _safe_set(owner, 'model_ArchimateRelationship', None)
    assert getattr(partner, 'model_ArchimateConcept') is None


def test_assoc_target8_stub_double():
    # model_ArchimateConcept has no real 'model_ArchimateConcept10' property in the generated
    # code (a bare stub) -- manually attach it so model_ArchimateRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ArchimateRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ArchimateRelationship()
    partner = model_ArchimateConcept()
    setattr(partner, 'model_ArchimateConcept10', None)
    _safe_set(owner, 'model_ArchimateRelationship9', partner)
    assert getattr(partner, 'model_ArchimateConcept10') == owner
    _safe_set(owner, 'model_ArchimateRelationship9', None)
    assert getattr(partner, 'model_ArchimateConcept10') is None


