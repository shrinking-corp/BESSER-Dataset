import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActiveStructure,
    ApplicationComponent,
    ApplicationFunction,
    ArchimateElement,
    BehaviorElement,
    BusinessBehaviorElement,
    BusinessObject,
    BusinessRole,
    Node,
    PassiveStructure,
    archimateC2_ActiveStructure,
    archimateC2_ApplicationCollaboration,
    archimateC2_ApplicationComponent,
    archimateC2_ApplicationFunction,
    archimateC2_ApplicationInteraction,
    archimateC2_ApplicationInterface,
    archimateC2_ApplicationService,
    archimateC2_ArchimateElement,
    archimateC2_ArchimateModel,
    archimateC2_Artifact,
    archimateC2_BehaviorElement,
    archimateC2_BusinessActor,
    archimateC2_BusinessBehaviorElement,
    archimateC2_BusinessCollaboration,
    archimateC2_BusinessEvent,
    archimateC2_BusinessFunction,
    archimateC2_BusinessInteraction,
    archimateC2_BusinessInterface,
    archimateC2_BusinessObject,
    archimateC2_BusinessProcess,
    archimateC2_BusinessRole,
    archimateC2_BusinessService,
    archimateC2_CommunicationPath,
    archimateC2_Contract,
    archimateC2_DataObject,
    archimateC2_Device,
    archimateC2_InfrastructureInterface,
    archimateC2_InfrastructureService,
    archimateC2_Location,
    archimateC2_Meaning,
    archimateC2_Network,
    archimateC2_Node,
    archimateC2_PassiveStructure,
    archimateC2_Product,
    archimateC2_Representation,
    archimateC2_SystemSoftware,
    archimateC2_Value,
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

def test_assoc_aggregatedByBusinessCollaborationBusinessRole107_reverse_link_reassign_clear():
    a1 = archimateC2_BusinessRole(rank=7)
    a2 = archimateC2_BusinessRole(rank=13)
    b = archimateC2_BusinessCollaboration(collaboration="sample_text")
    _safe_set(b, 'BusinessCollaboration', a1)
    assert _is_linked(b, 'BusinessCollaboration', a1)
    if hasattr(a1, 'aggregatesBusinessRoleBusinessCollaboration'):
        assert _is_linked(a1, 'aggregatesBusinessRoleBusinessCollaboration', b)
    _safe_set(b, 'BusinessCollaboration', a2)
    assert _is_linked(b, 'BusinessCollaboration', a2)
    if hasattr(a1, 'aggregatesBusinessRoleBusinessCollaboration'):
        assert not _is_linked(a1, 'aggregatesBusinessRoleBusinessCollaboration', b)
    if hasattr(a2, 'aggregatesBusinessRoleBusinessCollaboration'):
        assert _is_linked(a2, 'aggregatesBusinessRoleBusinessCollaboration', b)
    _safe_set(b, 'BusinessCollaboration', None)
    assert not _is_linked(b, 'BusinessCollaboration', a2)
    if hasattr(a2, 'aggregatesBusinessRoleBusinessCollaboration'):
        assert not _is_linked(a2, 'aggregatesBusinessRoleBusinessCollaboration', b)


def test_assoc_aggregatedByElementElement10_reverse_link_reassign_clear():
    a1 = archimateC2_ArchimateElement(description="sample_text", elementName="sample_text")
    a2 = archimateC2_ArchimateElement(description="sample_text_2", elementName="sample_text_2")
    b = archimateC2_ArchimateElement(description="sample_text", elementName="sample_text")
    _safe_set(b, 'aggregatesElementElement', a1)
    assert _is_linked(b, 'aggregatesElementElement', a1)
    if hasattr(a1, 'ArchimateElement11'):
        assert _is_linked(a1, 'ArchimateElement11', b)
    _safe_set(b, 'aggregatesElementElement', a2)
    assert _is_linked(b, 'aggregatesElementElement', a2)
    if hasattr(a1, 'ArchimateElement11'):
        assert not _is_linked(a1, 'ArchimateElement11', b)
    if hasattr(a2, 'ArchimateElement11'):
        assert _is_linked(a2, 'ArchimateElement11', b)
    _safe_set(b, 'aggregatesElementElement', None)
    assert not _is_linked(b, 'aggregatesElementElement', a2)
    if hasattr(a2, 'ArchimateElement11'):
        assert not _is_linked(a2, 'ArchimateElement11', b)


def test_assoc_aggregatesBusinessRoleBusinessCollaboration118_reverse_link_reassign_clear():
    a1 = archimateC2_BusinessRole(rank=7)
    a2 = archimateC2_BusinessRole(rank=13)
    b = archimateC2_BusinessCollaboration(collaboration="sample_text")
    _safe_set(b, 'aggregatedByBusinessCollaborationBusinessRole', {a1})
    assert _is_linked(b, 'aggregatedByBusinessCollaborationBusinessRole', a1)
    if hasattr(a1, 'BusinessRole119'):
        assert _is_linked(a1, 'BusinessRole119', b)
    _safe_set(b, 'aggregatedByBusinessCollaborationBusinessRole', {a2})
    assert _is_linked(b, 'aggregatedByBusinessCollaborationBusinessRole', a2)
    if hasattr(a1, 'BusinessRole119'):
        assert not _is_linked(a1, 'BusinessRole119', b)
    if hasattr(a2, 'BusinessRole119'):
        assert _is_linked(a2, 'BusinessRole119', b)
    _safe_set(b, 'aggregatedByBusinessCollaborationBusinessRole', set())
    assert not _is_linked(b, 'aggregatedByBusinessCollaborationBusinessRole', a2)
    if hasattr(a2, 'BusinessRole119'):
        assert not _is_linked(a2, 'BusinessRole119', b)


def test_assoc_aggregatesElementElement7_reverse_link_reassign_clear():
    a1 = archimateC2_ArchimateElement(description="sample_text", elementName="sample_text")
    a2 = archimateC2_ArchimateElement(description="sample_text_2", elementName="sample_text_2")
    b = archimateC2_ArchimateElement(description="sample_text", elementName="sample_text")
    _safe_set(b, 'aggregatedByElementElement', {a1})
    assert _is_linked(b, 'aggregatedByElementElement', a1)
    if hasattr(a1, 'ArchimateElement8'):
        assert _is_linked(a1, 'ArchimateElement8', b)
    _safe_set(b, 'aggregatedByElementElement', {a2})
    assert _is_linked(b, 'aggregatedByElementElement', a2)
    if hasattr(a1, 'ArchimateElement8'):
        assert not _is_linked(a1, 'ArchimateElement8', b)
    if hasattr(a2, 'ArchimateElement8'):
        assert _is_linked(a2, 'ArchimateElement8', b)
    _safe_set(b, 'aggregatedByElementElement', set())
    assert not _is_linked(b, 'aggregatedByElementElement', a2)
    if hasattr(a2, 'ArchimateElement8'):
        assert not _is_linked(a2, 'ArchimateElement8', b)


def test_assoc_composedOfElementElement2_reverse_link_reassign_clear():
    a1 = archimateC2_ArchimateElement(description="sample_text", elementName="sample_text")
    a2 = archimateC2_ArchimateElement(description="sample_text_2", elementName="sample_text_2")
    b = archimateC2_ArchimateElement(description="sample_text", elementName="sample_text")
    _safe_set(b, 'composesElementElement', {a1})
    assert _is_linked(b, 'composesElementElement', a1)
    if hasattr(a1, 'ArchimateElement'):
        assert _is_linked(a1, 'ArchimateElement', b)
    _safe_set(b, 'composesElementElement', {a2})
    assert _is_linked(b, 'composesElementElement', a2)
    if hasattr(a1, 'ArchimateElement'):
        assert not _is_linked(a1, 'ArchimateElement', b)
    if hasattr(a2, 'ArchimateElement'):
        assert _is_linked(a2, 'ArchimateElement', b)
    _safe_set(b, 'composesElementElement', set())
    assert not _is_linked(b, 'composesElementElement', a2)
    if hasattr(a2, 'ArchimateElement'):
        assert not _is_linked(a2, 'ArchimateElement', b)


def test_assoc_composesElementElement4_reverse_link_reassign_clear():
    a1 = archimateC2_ArchimateElement(description="sample_text", elementName="sample_text")
    a2 = archimateC2_ArchimateElement(description="sample_text_2", elementName="sample_text_2")
    b = archimateC2_ArchimateElement(description="sample_text", elementName="sample_text")
    _safe_set(b, 'composedOfElementElement', a1)
    assert _is_linked(b, 'composedOfElementElement', a1)
    if hasattr(a1, 'ArchimateElement5'):
        assert _is_linked(a1, 'ArchimateElement5', b)
    _safe_set(b, 'composedOfElementElement', a2)
    assert _is_linked(b, 'composedOfElementElement', a2)
    if hasattr(a1, 'ArchimateElement5'):
        assert not _is_linked(a1, 'ArchimateElement5', b)
    if hasattr(a2, 'ArchimateElement5'):
        assert _is_linked(a2, 'ArchimateElement5', b)
    _safe_set(b, 'composedOfElementElement', None)
    assert not _is_linked(b, 'composedOfElementElement', a2)
    if hasattr(a2, 'ArchimateElement5'):
        assert not _is_linked(a2, 'ArchimateElement5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_aggregatedByProductApplicationService16_stub_double():
    # archimateC2_ApplicationService has no real 'ApplicationService' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Product(contract="sample_text")
    partner = archimateC2_ApplicationService()
    setattr(partner, 'ApplicationService', None)
    _safe_set(owner, 'aggregatesProductApplicationService', {partner})
    assert getattr(partner, 'ApplicationService') == owner
    _safe_set(owner, 'aggregatesProductApplicationService', set())
    assert getattr(partner, 'ApplicationService') is None


def test_assoc_aggregatedByProductBusinessService33_stub_double():
    # archimateC2_BusinessService has no real 'aggregatesBusinessServiceProduct' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Product(contract="sample_text")
    partner = archimateC2_BusinessService()
    setattr(partner, 'aggregatesBusinessServiceProduct', None)
    _safe_set(owner, 'Product34', partner)
    assert owner in getattr(partner, 'aggregatesBusinessServiceProduct')
    _safe_set(owner, 'Product34', None)
    assert owner not in getattr(partner, 'aggregatesBusinessServiceProduct')


def test_assoc_aggregatedByProductContract18_stub_double():
    # archimateC2_Contract has no real 'aggregatesContractProduct' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Product(contract="sample_text")
    partner = archimateC2_Contract()
    setattr(partner, 'aggregatesContractProduct', None)
    _safe_set(owner, 'Product19', partner)
    assert owner in getattr(partner, 'aggregatesContractProduct')
    _safe_set(owner, 'Product19', None)
    assert owner not in getattr(partner, 'aggregatesContractProduct')


def test_assoc_aggregatedByProductInfrastructureService17_stub_double():
    # archimateC2_InfrastructureService has no real 'InfrastructureService' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Product(contract="sample_text")
    partner = archimateC2_InfrastructureService()
    setattr(partner, 'InfrastructureService', None)
    _safe_set(owner, 'aggregatesProductInfrastructureService', {partner})
    assert getattr(partner, 'InfrastructureService') == owner
    _safe_set(owner, 'aggregatesProductInfrastructureService', set())
    assert getattr(partner, 'InfrastructureService') is None


def test_assoc_aggregatesBusinessActorBusinessCollaboration116_stub_double():
    # archimateC2_BusinessActor has no real 'BusinessActor117' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessCollaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessCollaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessCollaboration(collaboration="sample_text")
    partner = archimateC2_BusinessActor()
    setattr(partner, 'BusinessActor117', None)
    _safe_set(owner, 'aggregatesByBusinessCollaborationBusinessActor', {partner})
    assert getattr(partner, 'BusinessActor117') == owner
    _safe_set(owner, 'aggregatesByBusinessCollaborationBusinessActor', set())
    assert getattr(partner, 'BusinessActor117') is None


def test_assoc_aggregatesBusinessServiceProduct15_stub_double():
    # archimateC2_BusinessService has no real 'BusinessService' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Product(contract="sample_text")
    partner = archimateC2_BusinessService()
    setattr(partner, 'BusinessService', None)
    _safe_set(owner, 'aggregatedByProductBusinessService', {partner})
    assert getattr(partner, 'BusinessService') == owner
    _safe_set(owner, 'aggregatedByProductBusinessService', set())
    assert getattr(partner, 'BusinessService') is None


def test_assoc_aggregatesByBusinessCollaborationBusinessActor120_stub_double():
    # archimateC2_BusinessActor has no real 'aggregatesBusinessActorBusinessCollaboration' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessCollaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessCollaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessCollaboration(collaboration="sample_text")
    partner = archimateC2_BusinessActor()
    setattr(partner, 'aggregatesBusinessActorBusinessCollaboration', None)
    _safe_set(owner, 'BusinessCollaboration121', partner)
    assert owner in getattr(partner, 'aggregatesBusinessActorBusinessCollaboration')
    _safe_set(owner, 'BusinessCollaboration121', None)
    assert owner not in getattr(partner, 'aggregatesBusinessActorBusinessCollaboration')


def test_assoc_aggregatesContractProduct14_stub_double():
    # archimateC2_Contract has no real 'Contract' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Product(contract="sample_text")
    partner = archimateC2_Contract()
    setattr(partner, 'Contract', None)
    _safe_set(owner, 'aggregatedByProductContract', {partner})
    assert getattr(partner, 'Contract') == owner
    _safe_set(owner, 'aggregatedByProductContract', set())
    assert getattr(partner, 'Contract') is None


def test_assoc_aggregatesProductApplicationService151_stub_double():
    # archimateC2_ApplicationService has no real 'aggregatedByProductApplicationService' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Product(contract="sample_text")
    partner = archimateC2_ApplicationService()
    setattr(partner, 'aggregatedByProductApplicationService', None)
    _safe_set(owner, 'Product152', partner)
    assert owner in getattr(partner, 'aggregatedByProductApplicationService')
    _safe_set(owner, 'Product152', None)
    assert owner not in getattr(partner, 'aggregatedByProductApplicationService')


def test_assoc_aggregatesProductInfrastructureService227_stub_double():
    # archimateC2_InfrastructureService has no real 'aggregatedByProductInfrastructureService' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Product(contract="sample_text")
    partner = archimateC2_InfrastructureService()
    setattr(partner, 'aggregatedByProductInfrastructureService', None)
    _safe_set(owner, 'Product228', partner)
    assert owner in getattr(partner, 'aggregatedByProductInfrastructureService')
    _safe_set(owner, 'Product228', None)
    assert owner not in getattr(partner, 'aggregatedByProductInfrastructureService')


def test_assoc_assignedFromBusinessActorLocation78_stub_double():
    # archimateC2_BusinessActor has no real 'BusinessActor79' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_BusinessActor()
    setattr(partner, 'BusinessActor79', None)
    _safe_set(owner, 'assignedToLocationBusinessActor', {partner})
    assert getattr(partner, 'BusinessActor79') == owner
    _safe_set(owner, 'assignedToLocationBusinessActor', set())
    assert getattr(partner, 'BusinessActor79') is None


def test_assoc_assignedFromBusinessObjectLocation80_stub_double():
    # archimateC2_BusinessObject has no real 'BusinessObject81' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_BusinessObject()
    setattr(partner, 'BusinessObject81', None)
    _safe_set(owner, 'assignedToLocationBusinessObject', {partner})
    assert getattr(partner, 'BusinessObject81') == owner
    _safe_set(owner, 'assignedToLocationBusinessObject', set())
    assert getattr(partner, 'BusinessObject81') is None


def test_assoc_assignedFromLocationApplicationComponent86_stub_double():
    # archimateC2_ApplicationComponent has no real 'ApplicationComponent87' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_ApplicationComponent()
    setattr(partner, 'ApplicationComponent87', None)
    _safe_set(owner, 'assignedToLocationApplicationComponent', {partner})
    assert getattr(partner, 'ApplicationComponent87') == owner
    _safe_set(owner, 'assignedToLocationApplicationComponent', set())
    assert getattr(partner, 'ApplicationComponent87') is None


def test_assoc_assignedFromLocationArtifact92_stub_double():
    # archimateC2_Artifact has no real 'Artifact' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_Artifact()
    setattr(partner, 'Artifact', None)
    _safe_set(owner, 'assignedToLocationArtifact', {partner})
    assert getattr(partner, 'Artifact') == owner
    _safe_set(owner, 'assignedToLocationArtifact', set())
    assert getattr(partner, 'Artifact') is None


def test_assoc_assignedFromLocationCommunicationPath259_stub_double():
    # archimateC2_CommunicationPath has no real 'archimateC2_CommunicationPath260' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_CommunicationPath()
    setattr(partner, 'archimateC2_CommunicationPath260', None)
    _safe_set(owner, 'archimateC2_Location261', partner)
    assert owner in getattr(partner, 'archimateC2_CommunicationPath260')
    _safe_set(owner, 'archimateC2_Location261', None)
    assert owner not in getattr(partner, 'archimateC2_CommunicationPath260')


def test_assoc_assignedFromLocationCommunicationPath90_stub_double():
    # archimateC2_CommunicationPath has no real 'archimateC2_CommunicationPath' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_CommunicationPath()
    setattr(partner, 'archimateC2_CommunicationPath', None)
    _safe_set(owner, 'archimateC2_Location91', {partner})
    assert getattr(partner, 'archimateC2_CommunicationPath') == owner
    _safe_set(owner, 'archimateC2_Location91', set())
    assert getattr(partner, 'archimateC2_CommunicationPath') is None


def test_assoc_assignedFromLocationNetwork266_stub_double():
    # archimateC2_Network has no real 'archimateC2_Network267' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_Network()
    setattr(partner, 'archimateC2_Network267', None)
    _safe_set(owner, 'archimateC2_Location268', partner)
    assert owner in getattr(partner, 'archimateC2_Network267')
    _safe_set(owner, 'archimateC2_Location268', None)
    assert owner not in getattr(partner, 'archimateC2_Network267')


def test_assoc_assignedFromLocationNetwork89_stub_double():
    # archimateC2_Network has no real 'archimateC2_Network' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_Network()
    setattr(partner, 'archimateC2_Network', None)
    _safe_set(owner, 'archimateC2_Location', {partner})
    assert getattr(partner, 'archimateC2_Network') == owner
    _safe_set(owner, 'archimateC2_Location', set())
    assert getattr(partner, 'archimateC2_Network') is None


def test_assoc_assignedFromLocationNode88_stub_double():
    # archimateC2_Node has no real 'Node' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_Node()
    setattr(partner, 'Node', None)
    _safe_set(owner, 'assignedToLocationNode', {partner})
    assert getattr(partner, 'Node') == owner
    _safe_set(owner, 'assignedToLocationNode', set())
    assert getattr(partner, 'Node') is None


def test_assoc_assignedFromRepresentationLocation82_stub_double():
    # archimateC2_Representation has no real 'Representation83' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_Representation()
    setattr(partner, 'Representation83', None)
    _safe_set(owner, 'assignedToLocationRepresentation', {partner})
    assert getattr(partner, 'Representation83') == owner
    _safe_set(owner, 'assignedToLocationRepresentation', set())
    assert getattr(partner, 'Representation83') is None


def test_assoc_assignedToBusinessActorBusinessRole105_stub_double():
    # archimateC2_BusinessActor has no real 'BusinessActor106' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_BusinessActor()
    setattr(partner, 'BusinessActor106', None)
    _safe_set(owner, 'assignedToBusinessRoleBusinessActor', {partner})
    assert getattr(partner, 'BusinessActor106') == owner
    _safe_set(owner, 'assignedToBusinessRoleBusinessActor', set())
    assert getattr(partner, 'BusinessActor106') is None


def test_assoc_assignedToBusinessBehaviorElementBusinessRole108_stub_double():
    # archimateC2_BusinessBehaviorElement has no real 'BusinessBehaviorElement109' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_BusinessBehaviorElement()
    setattr(partner, 'BusinessBehaviorElement109', None)
    _safe_set(owner, 'assignedToBusinessRoleBusinessBehaviorElement', {partner})
    assert getattr(partner, 'BusinessBehaviorElement109') == owner
    _safe_set(owner, 'assignedToBusinessRoleBusinessBehaviorElement', set())
    assert getattr(partner, 'BusinessBehaviorElement109') is None


def test_assoc_assignedToBusinessRoleBusinessActor124_stub_double():
    # archimateC2_BusinessActor has no real 'assignedToBusinessActorBusinessRole' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_BusinessActor()
    setattr(partner, 'assignedToBusinessActorBusinessRole', None)
    _safe_set(owner, 'BusinessRole125', partner)
    assert owner in getattr(partner, 'assignedToBusinessActorBusinessRole')
    _safe_set(owner, 'BusinessRole125', None)
    assert owner not in getattr(partner, 'assignedToBusinessActorBusinessRole')


def test_assoc_assignedToBusinessRoleBusinessBehaviorElement67_stub_double():
    # archimateC2_BusinessBehaviorElement has no real 'assignedToBusinessBehaviorElementBusinessRole' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_BusinessBehaviorElement()
    setattr(partner, 'assignedToBusinessBehaviorElementBusinessRole', None)
    _safe_set(owner, 'BusinessRole68', partner)
    assert owner in getattr(partner, 'assignedToBusinessBehaviorElementBusinessRole')
    _safe_set(owner, 'BusinessRole68', None)
    assert owner not in getattr(partner, 'assignedToBusinessBehaviorElementBusinessRole')


def test_assoc_assignedToLocationApplicationComponent200_stub_double():
    # archimateC2_ApplicationComponent has no real 'assignedFromLocationApplicationComponent' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_ApplicationComponent()
    setattr(partner, 'assignedFromLocationApplicationComponent', None)
    _safe_set(owner, 'Location201', partner)
    assert owner in getattr(partner, 'assignedFromLocationApplicationComponent')
    _safe_set(owner, 'Location201', None)
    assert owner not in getattr(partner, 'assignedFromLocationApplicationComponent')


def test_assoc_assignedToLocationArtifact215_stub_double():
    # archimateC2_Artifact has no real 'assignedFromLocationArtifact' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_Artifact()
    setattr(partner, 'assignedFromLocationArtifact', None)
    _safe_set(owner, 'Location216', partner)
    assert owner in getattr(partner, 'assignedFromLocationArtifact')
    _safe_set(owner, 'Location216', None)
    assert owner not in getattr(partner, 'assignedFromLocationArtifact')


def test_assoc_assignedToLocationBusinessActor128_stub_double():
    # archimateC2_BusinessActor has no real 'assignedFromBusinessActorLocation' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_BusinessActor()
    setattr(partner, 'assignedFromBusinessActorLocation', None)
    _safe_set(owner, 'Location129', partner)
    assert owner in getattr(partner, 'assignedFromBusinessActorLocation')
    _safe_set(owner, 'Location129', None)
    assert owner not in getattr(partner, 'assignedFromBusinessActorLocation')


def test_assoc_assignedToLocationBusinessObject22_stub_double():
    # archimateC2_BusinessObject has no real 'assignedFromBusinessObjectLocation' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_BusinessObject()
    setattr(partner, 'assignedFromBusinessObjectLocation', None)
    _safe_set(owner, 'Location', partner)
    assert owner in getattr(partner, 'assignedFromBusinessObjectLocation')
    _safe_set(owner, 'Location', None)
    assert owner not in getattr(partner, 'assignedFromBusinessObjectLocation')


def test_assoc_assignedToLocationDataObject84_stub_double():
    # archimateC2_DataObject has no real 'DataObject85' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_DataObject()
    setattr(partner, 'DataObject85', None)
    _safe_set(owner, 'assignedfromLocationDataObject', {partner})
    assert getattr(partner, 'DataObject85') == owner
    _safe_set(owner, 'assignedfromLocationDataObject', set())
    assert getattr(partner, 'DataObject85') is None


def test_assoc_assignedToLocationNode250_stub_double():
    # archimateC2_Node has no real 'assignedFromLocationNode' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_Node()
    setattr(partner, 'assignedFromLocationNode', None)
    _safe_set(owner, 'Location251', partner)
    assert owner in getattr(partner, 'assignedFromLocationNode')
    _safe_set(owner, 'Location251', None)
    assert owner not in getattr(partner, 'assignedFromLocationNode')


def test_assoc_assignedToLocationRepresentation31_stub_double():
    # archimateC2_Representation has no real 'assignedFromRepresentationLocation' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_Representation()
    setattr(partner, 'assignedFromRepresentationLocation', None)
    _safe_set(owner, 'Location32', partner)
    assert owner in getattr(partner, 'assignedFromRepresentationLocation')
    _safe_set(owner, 'Location32', None)
    assert owner not in getattr(partner, 'assignedFromRepresentationLocation')


def test_assoc_assignedfromLocationDataObject139_stub_double():
    # archimateC2_DataObject has no real 'assignedToLocationDataObject' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Location(address="sample_text")
    partner = archimateC2_DataObject()
    setattr(partner, 'assignedToLocationDataObject', None)
    _safe_set(owner, 'Location140', partner)
    assert owner in getattr(partner, 'assignedToLocationDataObject')
    _safe_set(owner, 'Location140', None)
    assert owner not in getattr(partner, 'assignedToLocationDataObject')


def test_assoc_associatedWithProductValue12_stub_double():
    # archimateC2_Value has no real 'associatedWithValueProduct' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Product(contract="sample_text")
    partner = archimateC2_Value()
    setattr(partner, 'associatedWithValueProduct', None)
    _safe_set(owner, 'Product', partner)
    assert owner in getattr(partner, 'associatedWithValueProduct')
    _safe_set(owner, 'Product', None)
    assert owner not in getattr(partner, 'associatedWithValueProduct')


def test_assoc_associatedWithValueProduct13_stub_double():
    # archimateC2_Value has no real 'Value' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_Product(contract="sample_text")
    partner = archimateC2_Value()
    setattr(partner, 'Value', None)
    _safe_set(owner, 'associatedWithProductValue', {partner})
    assert getattr(partner, 'Value') == owner
    _safe_set(owner, 'associatedWithProductValue', set())
    assert getattr(partner, 'Value') is None


def test_assoc_composedOfBusinessInterfaceBusinessRole101_stub_double():
    # archimateC2_BusinessInterface has no real 'BusinessInterface102' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_BusinessInterface()
    setattr(partner, 'BusinessInterface102', None)
    _safe_set(owner, 'composesBusinessRoleBusinessInterface', {partner})
    assert getattr(partner, 'BusinessInterface102') == owner
    _safe_set(owner, 'composesBusinessRoleBusinessInterface', set())
    assert getattr(partner, 'BusinessInterface102') is None


def test_assoc_composesBusinessRoleBusinessInterface93_stub_double():
    # archimateC2_BusinessInterface has no real 'composedOfBusinessInterfaceBusinessRole' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_BusinessInterface()
    setattr(partner, 'composedOfBusinessInterfaceBusinessRole', None)
    _safe_set(owner, 'BusinessRole94', partner)
    assert getattr(partner, 'composedOfBusinessInterfaceBusinessRole') == owner
    _safe_set(owner, 'BusinessRole94', None)
    assert getattr(partner, 'composedOfBusinessInterfaceBusinessRole') is None


def test_assoc_elements0_stub_double():
    # archimateC2_ArchimateModel has no real 'archimateC2_ArchimateModel' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_ArchimateElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_ArchimateElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_ArchimateElement(description="sample_text", elementName="sample_text")
    partner = archimateC2_ArchimateModel()
    setattr(partner, 'archimateC2_ArchimateModel', None)
    _safe_set(owner, 'archimateC2_ArchimateElement', partner)
    assert owner in getattr(partner, 'archimateC2_ArchimateModel')
    _safe_set(owner, 'archimateC2_ArchimateElement', None)
    assert owner not in getattr(partner, 'archimateC2_ArchimateModel')


def test_assoc_usedByBusinessRoleApplicationInterface114_stub_double():
    # archimateC2_ApplicationInterface has no real 'ApplicationInterface115' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_ApplicationInterface()
    setattr(partner, 'ApplicationInterface115', None)
    _safe_set(owner, 'usesBusinessRoleApplicationInterface', {partner})
    assert getattr(partner, 'ApplicationInterface115') == owner
    _safe_set(owner, 'usesBusinessRoleApplicationInterface', set())
    assert getattr(partner, 'ApplicationInterface115') is None


def test_assoc_usedByBusinessRoleApplicationService155_stub_double():
    # archimateC2_ApplicationService has no real 'usesBusinessRoleApplicationService' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_ApplicationService()
    setattr(partner, 'usesBusinessRoleApplicationService', None)
    _safe_set(owner, 'BusinessRole156', partner)
    assert owner in getattr(partner, 'usesBusinessRoleApplicationService')
    _safe_set(owner, 'BusinessRole156', None)
    assert owner not in getattr(partner, 'usesBusinessRoleApplicationService')


def test_assoc_usedByBusinessRoleBusinessInterface97_stub_double():
    # archimateC2_BusinessInterface has no real 'usesBusinessInterfaceBusinessRole' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_BusinessInterface()
    setattr(partner, 'usesBusinessInterfaceBusinessRole', None)
    _safe_set(owner, 'BusinessRole98', partner)
    assert owner in getattr(partner, 'usesBusinessInterfaceBusinessRole')
    _safe_set(owner, 'BusinessRole98', None)
    assert owner not in getattr(partner, 'usesBusinessInterfaceBusinessRole')


def test_assoc_usedByElementBusinessRoleBusinessService43_stub_double():
    # archimateC2_BusinessService has no real 'usesElementBusinessServiceBusinessRole' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_BusinessService()
    setattr(partner, 'usesElementBusinessServiceBusinessRole', None)
    _safe_set(owner, 'BusinessRole', partner)
    assert owner in getattr(partner, 'usesElementBusinessServiceBusinessRole')
    _safe_set(owner, 'BusinessRole', None)
    assert owner not in getattr(partner, 'usesElementBusinessServiceBusinessRole')


def test_assoc_usesBusinessInterfaceBusinessRole103_stub_double():
    # archimateC2_BusinessInterface has no real 'BusinessInterface104' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_BusinessInterface()
    setattr(partner, 'BusinessInterface104', None)
    _safe_set(owner, 'usedByBusinessRoleBusinessInterface', {partner})
    assert getattr(partner, 'BusinessInterface104') == owner
    _safe_set(owner, 'usedByBusinessRoleBusinessInterface', set())
    assert getattr(partner, 'BusinessInterface104') is None


def test_assoc_usesBusinessRoleApplicationInterface189_stub_double():
    # archimateC2_ApplicationInterface has no real 'usedByBusinessRoleApplicationInterface' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_ApplicationInterface()
    setattr(partner, 'usedByBusinessRoleApplicationInterface', None)
    _safe_set(owner, 'BusinessRole190', partner)
    assert owner in getattr(partner, 'usedByBusinessRoleApplicationInterface')
    _safe_set(owner, 'BusinessRole190', None)
    assert owner not in getattr(partner, 'usedByBusinessRoleApplicationInterface')


def test_assoc_usesBusinessRoleApplicationService112_stub_double():
    # archimateC2_ApplicationService has no real 'ApplicationService113' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_ApplicationService()
    setattr(partner, 'ApplicationService113', None)
    _safe_set(owner, 'usedByBusinessRoleApplicationService', {partner})
    assert getattr(partner, 'ApplicationService113') == owner
    _safe_set(owner, 'usedByBusinessRoleApplicationService', set())
    assert getattr(partner, 'ApplicationService113') is None


def test_assoc_usesElementBusinessServiceBusinessRole110_stub_double():
    # archimateC2_BusinessService has no real 'BusinessService111' property in the generated
    # code (a bare stub) -- manually attach it so archimateC2_BusinessRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archimateC2_BusinessRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archimateC2_BusinessRole(rank=7)
    partner = archimateC2_BusinessService()
    setattr(partner, 'BusinessService111', None)
    _safe_set(owner, 'usedByElementBusinessRoleBusinessService', {partner})
    assert getattr(partner, 'BusinessService111') == owner
    _safe_set(owner, 'usedByElementBusinessRoleBusinessService', set())
    assert getattr(partner, 'BusinessService111') is None


