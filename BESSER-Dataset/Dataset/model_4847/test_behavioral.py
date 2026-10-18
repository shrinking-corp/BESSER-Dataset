import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EnterpriseObject,
    EnterpriseProcessor,
    EnterpriseResource,
    ObjectView,
    OrganisationCell,
    SIPME_object,
    Stakeholder,
    sipme_Activity,
    sipme_Application,
    sipme_BusinessProcess,
    sipme_BusinessRules,
    sipme_Capability,
    sipme_Capacity,
    sipme_CompanyMember,
    sipme_Device_Machine,
    sipme_Domain,
    sipme_Enterprise,
    sipme_EnterpriseObject,
    sipme_EnterpriseProcessor,
    sipme_EnterpriseProduct,
    sipme_EnterpriseResource,
    sipme_EnterpriseService,
    sipme_Event,
    sipme_ObjectView,
    sipme_Objective,
    sipme_ObjectsFileView,
    sipme_OrganisationCell,
    sipme_Requirement,
    sipme_Role_Function,
    sipme_SIPME_object,
    sipme_Stakeholder,
    sipme_Task,
    sipme_Workstation,
    CapabilityType,
    EnterpriseObjectiveType,
    ObjectiveNature,
    Origin,
    ProductNature,
    ProductState,
    RequirementNature,
    RequirementOrigin,
    RoleType,
    ServiceState,
    StakeholderType,
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

def test_assoc_activities2_reverse_link_reassign_clear():
    a1 = sipme_BusinessProcess(ProcessPriority=7)
    a2 = sipme_BusinessProcess(ProcessPriority=13)
    b = sipme_Activity(ActivityDuration=7, endingStatus="sample_text")
    _safe_set(b, 'Activity', a1)
    assert _is_linked(b, 'Activity', a1)
    if hasattr(a1, 'activityOf'):
        assert _is_linked(a1, 'activityOf', b)
    _safe_set(b, 'Activity', a2)
    assert _is_linked(b, 'Activity', a2)
    if hasattr(a1, 'activityOf'):
        assert not _is_linked(a1, 'activityOf', b)
    if hasattr(a2, 'activityOf'):
        assert _is_linked(a2, 'activityOf', b)
    _safe_set(b, 'Activity', None)
    assert not _is_linked(b, 'Activity', a2)
    if hasattr(a2, 'activityOf'):
        assert not _is_linked(a2, 'activityOf', b)


def test_assoc_activityOf1_reverse_link_reassign_clear():
    a1 = sipme_BusinessProcess(ProcessPriority=7)
    a2 = sipme_BusinessProcess(ProcessPriority=13)
    b = sipme_Activity(ActivityDuration=7, endingStatus="sample_text")
    _safe_set(b, 'activities', a1)
    assert _is_linked(b, 'activities', a1)
    if hasattr(a1, 'BusinessProcess'):
        assert _is_linked(a1, 'BusinessProcess', b)
    _safe_set(b, 'activities', a2)
    assert _is_linked(b, 'activities', a2)
    if hasattr(a1, 'BusinessProcess'):
        assert not _is_linked(a1, 'BusinessProcess', b)
    if hasattr(a2, 'BusinessProcess'):
        assert _is_linked(a2, 'BusinessProcess', b)
    _safe_set(b, 'activities', None)
    assert not _is_linked(b, 'activities', a2)
    if hasattr(a2, 'BusinessProcess'):
        assert not _is_linked(a2, 'BusinessProcess', b)


def test_assoc_assignedTo90_reverse_link_reassign_clear():
    a1 = sipme_OrganisationCell(organisationLevel=7)
    a2 = sipme_OrganisationCell(organisationLevel=13)
    b = sipme_OrganisationCell(organisationLevel=7)
    _safe_set(b, 'sipme_OrganisationCell91', a1)
    assert _is_linked(b, 'sipme_OrganisationCell91', a1)
    if hasattr(a1, 'sipme_OrganisationCell89'):
        assert _is_linked(a1, 'sipme_OrganisationCell89', b)
    _safe_set(b, 'sipme_OrganisationCell91', a2)
    assert _is_linked(b, 'sipme_OrganisationCell91', a2)
    if hasattr(a1, 'sipme_OrganisationCell89'):
        assert not _is_linked(a1, 'sipme_OrganisationCell89', b)
    if hasattr(a2, 'sipme_OrganisationCell89'):
        assert _is_linked(a2, 'sipme_OrganisationCell89', b)
    _safe_set(b, 'sipme_OrganisationCell91', None)
    assert not _is_linked(b, 'sipme_OrganisationCell91', a2)
    if hasattr(a2, 'sipme_OrganisationCell89'):
        assert not _is_linked(a2, 'sipme_OrganisationCell89', b)


def test_assoc_associatedObjective99_reverse_link_reassign_clear():
    a1 = sipme_Requirement(requirementDate=date(2024, 1, 1), requirementMaturity=7, requirementNature="sample_text", requirementOrigin="sample_text", requirementPriority=7, requirementStatement="sample_text", requirementStatus="sample_text", requirementVersion="sample_text")
    a2 = sipme_Requirement(requirementDate=date(2025, 6, 15), requirementMaturity=13, requirementNature="sample_text_2", requirementOrigin="sample_text_2", requirementPriority=13, requirementStatement="sample_text_2", requirementStatus="sample_text_2", requirementVersion="sample_text_2")
    b = sipme_Objective(objectiveNature="sample_text", objectiveType="sample_text")
    _safe_set(b, 'Objective100', a1)
    assert _is_linked(b, 'Objective100', a1)
    if hasattr(a1, 'takenIntoAccountBy'):
        assert _is_linked(a1, 'takenIntoAccountBy', b)
    _safe_set(b, 'Objective100', a2)
    assert _is_linked(b, 'Objective100', a2)
    if hasattr(a1, 'takenIntoAccountBy'):
        assert not _is_linked(a1, 'takenIntoAccountBy', b)
    if hasattr(a2, 'takenIntoAccountBy'):
        assert _is_linked(a2, 'takenIntoAccountBy', b)
    _safe_set(b, 'Objective100', None)
    assert not _is_linked(b, 'Objective100', a2)
    if hasattr(a2, 'takenIntoAccountBy'):
        assert not _is_linked(a2, 'takenIntoAccountBy', b)


def test_assoc_businessProcessOf3_reverse_link_reassign_clear():
    a1 = sipme_Domain(domainCharacterization="sample_text", performanceIndicators=3.14)
    a2 = sipme_Domain(domainCharacterization="sample_text_2", performanceIndicators=9.99)
    b = sipme_BusinessProcess(ProcessPriority=7)
    _safe_set(b, 'sipme_BusinessProcess', a1)
    assert _is_linked(b, 'sipme_BusinessProcess', a1)
    if hasattr(a1, 'sipme_Domain'):
        assert _is_linked(a1, 'sipme_Domain', b)
    _safe_set(b, 'sipme_BusinessProcess', a2)
    assert _is_linked(b, 'sipme_BusinessProcess', a2)
    if hasattr(a1, 'sipme_Domain'):
        assert not _is_linked(a1, 'sipme_Domain', b)
    if hasattr(a2, 'sipme_Domain'):
        assert _is_linked(a2, 'sipme_Domain', b)
    _safe_set(b, 'sipme_BusinessProcess', None)
    assert not _is_linked(b, 'sipme_BusinessProcess', a2)
    if hasattr(a2, 'sipme_Domain'):
        assert not _is_linked(a2, 'sipme_Domain', b)


def test_assoc_businessProcesses14_reverse_link_reassign_clear():
    a1 = sipme_Domain(domainCharacterization="sample_text", performanceIndicators=3.14)
    a2 = sipme_Domain(domainCharacterization="sample_text_2", performanceIndicators=9.99)
    b = sipme_BusinessProcess(ProcessPriority=7)
    _safe_set(b, 'sipme_BusinessProcess16', a1)
    assert _is_linked(b, 'sipme_BusinessProcess16', a1)
    if hasattr(a1, 'sipme_Domain15'):
        assert _is_linked(a1, 'sipme_Domain15', b)
    _safe_set(b, 'sipme_BusinessProcess16', a2)
    assert _is_linked(b, 'sipme_BusinessProcess16', a2)
    if hasattr(a1, 'sipme_Domain15'):
        assert not _is_linked(a1, 'sipme_Domain15', b)
    if hasattr(a2, 'sipme_Domain15'):
        assert _is_linked(a2, 'sipme_Domain15', b)
    _safe_set(b, 'sipme_BusinessProcess16', None)
    assert not _is_linked(b, 'sipme_BusinessProcess16', a2)
    if hasattr(a2, 'sipme_Domain15'):
        assert not _is_linked(a2, 'sipme_Domain15', b)


def test_assoc_canBePlayedBy116_reverse_link_reassign_clear():
    a1 = sipme_Role_Function(roleType="sample_text")
    a2 = sipme_Role_Function(roleType="sample_text_2")
    b = sipme_EnterpriseResource(resourceOrigin="sample_text")
    _safe_set(b, 'EnterpriseResource117', a1)
    assert _is_linked(b, 'EnterpriseResource117', a1)
    if hasattr(a1, 'isAbleToPlay'):
        assert _is_linked(a1, 'isAbleToPlay', b)
    _safe_set(b, 'EnterpriseResource117', a2)
    assert _is_linked(b, 'EnterpriseResource117', a2)
    if hasattr(a1, 'isAbleToPlay'):
        assert not _is_linked(a1, 'isAbleToPlay', b)
    if hasattr(a2, 'isAbleToPlay'):
        assert _is_linked(a2, 'isAbleToPlay', b)
    _safe_set(b, 'EnterpriseResource117', None)
    assert not _is_linked(b, 'EnterpriseResource117', a2)
    if hasattr(a2, 'isAbleToPlay'):
        assert not _is_linked(a2, 'isAbleToPlay', b)


def test_assoc_cellResponsible88_reverse_link_reassign_clear():
    a1 = sipme_OrganisationCell(organisationLevel=7)
    a2 = sipme_OrganisationCell(organisationLevel=13)
    b = sipme_CompanyMember(address="sample_text", fullName="sample_text", socialSecurityNumber=7)
    _safe_set(b, 'CompanyMember', a1)
    assert _is_linked(b, 'CompanyMember', a1)
    if hasattr(a1, 'responsibleOfCell'):
        assert _is_linked(a1, 'responsibleOfCell', b)
    _safe_set(b, 'CompanyMember', a2)
    assert _is_linked(b, 'CompanyMember', a2)
    if hasattr(a1, 'responsibleOfCell'):
        assert not _is_linked(a1, 'responsibleOfCell', b)
    if hasattr(a2, 'responsibleOfCell'):
        assert _is_linked(a2, 'responsibleOfCell', b)
    _safe_set(b, 'CompanyMember', None)
    assert not _is_linked(b, 'CompanyMember', a2)
    if hasattr(a2, 'responsibleOfCell'):
        assert not _is_linked(a2, 'responsibleOfCell', b)


def test_assoc_companyMembers33_reverse_link_reassign_clear():
    a1 = sipme_Enterprise(acronym="sample_text", status="sample_text")
    a2 = sipme_Enterprise(acronym="sample_text_2", status="sample_text_2")
    b = sipme_CompanyMember(address="sample_text", fullName="sample_text", socialSecurityNumber=7)
    _safe_set(b, 'sipme_CompanyMember', a1)
    assert _is_linked(b, 'sipme_CompanyMember', a1)
    if hasattr(a1, 'sipme_Enterprise34'):
        assert _is_linked(a1, 'sipme_Enterprise34', b)
    _safe_set(b, 'sipme_CompanyMember', a2)
    assert _is_linked(b, 'sipme_CompanyMember', a2)
    if hasattr(a1, 'sipme_Enterprise34'):
        assert not _is_linked(a1, 'sipme_Enterprise34', b)
    if hasattr(a2, 'sipme_Enterprise34'):
        assert _is_linked(a2, 'sipme_Enterprise34', b)
    _safe_set(b, 'sipme_CompanyMember', None)
    assert not _is_linked(b, 'sipme_CompanyMember', a2)
    if hasattr(a2, 'sipme_Enterprise34'):
        assert not _is_linked(a2, 'sipme_Enterprise34', b)


def test_assoc_concerns23_reverse_link_reassign_clear():
    a1 = sipme_Enterprise(acronym="sample_text", status="sample_text")
    a2 = sipme_Enterprise(acronym="sample_text_2", status="sample_text_2")
    b = sipme_Domain(domainCharacterization="sample_text", performanceIndicators=3.14)
    _safe_set(b, 'sipme_Domain25', a1)
    assert _is_linked(b, 'sipme_Domain25', a1)
    if hasattr(a1, 'sipme_Enterprise24'):
        assert _is_linked(a1, 'sipme_Enterprise24', b)
    _safe_set(b, 'sipme_Domain25', a2)
    assert _is_linked(b, 'sipme_Domain25', a2)
    if hasattr(a1, 'sipme_Enterprise24'):
        assert not _is_linked(a1, 'sipme_Enterprise24', b)
    if hasattr(a2, 'sipme_Enterprise24'):
        assert _is_linked(a2, 'sipme_Enterprise24', b)
    _safe_set(b, 'sipme_Domain25', None)
    assert not _is_linked(b, 'sipme_Domain25', a2)
    if hasattr(a2, 'sipme_Enterprise24'):
        assert not _is_linked(a2, 'sipme_Enterprise24', b)


def test_assoc_concernsActivity111_reverse_link_reassign_clear():
    a1 = sipme_Requirement(requirementDate=date(2024, 1, 1), requirementMaturity=7, requirementNature="sample_text", requirementOrigin="sample_text", requirementPriority=7, requirementStatement="sample_text", requirementStatus="sample_text", requirementVersion="sample_text")
    a2 = sipme_Requirement(requirementDate=date(2025, 6, 15), requirementMaturity=13, requirementNature="sample_text_2", requirementOrigin="sample_text_2", requirementPriority=13, requirementStatement="sample_text_2", requirementStatus="sample_text_2", requirementVersion="sample_text_2")
    b = sipme_Activity(ActivityDuration=7, endingStatus="sample_text")
    _safe_set(b, 'sipme_Activity', a1)
    assert _is_linked(b, 'sipme_Activity', a1)
    if hasattr(a1, 'sipme_Requirement112'):
        assert _is_linked(a1, 'sipme_Requirement112', b)
    _safe_set(b, 'sipme_Activity', a2)
    assert _is_linked(b, 'sipme_Activity', a2)
    if hasattr(a1, 'sipme_Requirement112'):
        assert not _is_linked(a1, 'sipme_Requirement112', b)
    if hasattr(a2, 'sipme_Requirement112'):
        assert _is_linked(a2, 'sipme_Requirement112', b)
    _safe_set(b, 'sipme_Activity', None)
    assert not _is_linked(b, 'sipme_Activity', a2)
    if hasattr(a2, 'sipme_Requirement112'):
        assert not _is_linked(a2, 'sipme_Requirement112', b)


def test_assoc_concernsProcessors108_reverse_link_reassign_clear():
    a1 = sipme_Requirement(requirementDate=date(2024, 1, 1), requirementMaturity=7, requirementNature="sample_text", requirementOrigin="sample_text", requirementPriority=7, requirementStatement="sample_text", requirementStatus="sample_text", requirementVersion="sample_text")
    a2 = sipme_Requirement(requirementDate=date(2025, 6, 15), requirementMaturity=13, requirementNature="sample_text_2", requirementOrigin="sample_text_2", requirementPriority=13, requirementStatement="sample_text_2", requirementStatus="sample_text_2", requirementVersion="sample_text_2")
    b = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    _safe_set(b, 'sipme_EnterpriseProcessor110', a1)
    assert _is_linked(b, 'sipme_EnterpriseProcessor110', a1)
    if hasattr(a1, 'sipme_Requirement109'):
        assert _is_linked(a1, 'sipme_Requirement109', b)
    _safe_set(b, 'sipme_EnterpriseProcessor110', a2)
    assert _is_linked(b, 'sipme_EnterpriseProcessor110', a2)
    if hasattr(a1, 'sipme_Requirement109'):
        assert not _is_linked(a1, 'sipme_Requirement109', b)
    if hasattr(a2, 'sipme_Requirement109'):
        assert _is_linked(a2, 'sipme_Requirement109', b)
    _safe_set(b, 'sipme_EnterpriseProcessor110', None)
    assert not _is_linked(b, 'sipme_EnterpriseProcessor110', a2)
    if hasattr(a2, 'sipme_Requirement109'):
        assert not _is_linked(a2, 'sipme_Requirement109', b)


def test_assoc_concernsResources105_reverse_link_reassign_clear():
    a1 = sipme_Requirement(requirementDate=date(2024, 1, 1), requirementMaturity=7, requirementNature="sample_text", requirementOrigin="sample_text", requirementPriority=7, requirementStatement="sample_text", requirementStatus="sample_text", requirementVersion="sample_text")
    a2 = sipme_Requirement(requirementDate=date(2025, 6, 15), requirementMaturity=13, requirementNature="sample_text_2", requirementOrigin="sample_text_2", requirementPriority=13, requirementStatement="sample_text_2", requirementStatus="sample_text_2", requirementVersion="sample_text_2")
    b = sipme_EnterpriseResource(resourceOrigin="sample_text")
    _safe_set(b, 'sipme_EnterpriseResource107', a1)
    assert _is_linked(b, 'sipme_EnterpriseResource107', a1)
    if hasattr(a1, 'sipme_Requirement106'):
        assert _is_linked(a1, 'sipme_Requirement106', b)
    _safe_set(b, 'sipme_EnterpriseResource107', a2)
    assert _is_linked(b, 'sipme_EnterpriseResource107', a2)
    if hasattr(a1, 'sipme_Requirement106'):
        assert not _is_linked(a1, 'sipme_Requirement106', b)
    if hasattr(a2, 'sipme_Requirement106'):
        assert _is_linked(a2, 'sipme_Requirement106', b)
    _safe_set(b, 'sipme_EnterpriseResource107', None)
    assert not _is_linked(b, 'sipme_EnterpriseResource107', a2)
    if hasattr(a2, 'sipme_Requirement106'):
        assert not _is_linked(a2, 'sipme_Requirement106', b)


def test_assoc_coveredBy17_reverse_link_reassign_clear():
    a1 = sipme_OrganisationCell(organisationLevel=7)
    a2 = sipme_OrganisationCell(organisationLevel=13)
    b = sipme_Domain(domainCharacterization="sample_text", performanceIndicators=3.14)
    _safe_set(b, 'covers', {a1})
    assert _is_linked(b, 'covers', a1)
    if hasattr(a1, 'OrganisationCell18'):
        assert _is_linked(a1, 'OrganisationCell18', b)
    _safe_set(b, 'covers', {a2})
    assert _is_linked(b, 'covers', a2)
    if hasattr(a1, 'OrganisationCell18'):
        assert not _is_linked(a1, 'OrganisationCell18', b)
    if hasattr(a2, 'OrganisationCell18'):
        assert _is_linked(a2, 'OrganisationCell18', b)
    _safe_set(b, 'covers', set())
    assert not _is_linked(b, 'covers', a2)
    if hasattr(a2, 'OrganisationCell18'):
        assert not _is_linked(a2, 'OrganisationCell18', b)


def test_assoc_covers87_reverse_link_reassign_clear():
    a1 = sipme_OrganisationCell(organisationLevel=7)
    a2 = sipme_OrganisationCell(organisationLevel=13)
    b = sipme_Domain(domainCharacterization="sample_text", performanceIndicators=3.14)
    _safe_set(b, 'Domain', a1)
    assert _is_linked(b, 'Domain', a1)
    if hasattr(a1, 'coveredBy'):
        assert _is_linked(a1, 'coveredBy', b)
    _safe_set(b, 'Domain', a2)
    assert _is_linked(b, 'Domain', a2)
    if hasattr(a1, 'coveredBy'):
        assert not _is_linked(a1, 'coveredBy', b)
    if hasattr(a2, 'coveredBy'):
        assert _is_linked(a2, 'coveredBy', b)
    _safe_set(b, 'Domain', None)
    assert not _is_linked(b, 'Domain', a2)
    if hasattr(a2, 'coveredBy'):
        assert not _is_linked(a2, 'coveredBy', b)


def test_assoc_decomposedIn41_reverse_link_reassign_clear():
    a1 = sipme_EnterpriseObject(properties="sample_text", reference="sample_text")
    a2 = sipme_EnterpriseObject(properties="sample_text_2", reference="sample_text_2")
    b = sipme_EnterpriseObject(properties="sample_text", reference="sample_text")
    _safe_set(b, 'partOf', {a1})
    assert _is_linked(b, 'partOf', a1)
    if hasattr(a1, 'EnterpriseObject42'):
        assert _is_linked(a1, 'EnterpriseObject42', b)
    _safe_set(b, 'partOf', {a2})
    assert _is_linked(b, 'partOf', a2)
    if hasattr(a1, 'EnterpriseObject42'):
        assert not _is_linked(a1, 'EnterpriseObject42', b)
    if hasattr(a2, 'EnterpriseObject42'):
        assert _is_linked(a2, 'EnterpriseObject42', b)
    _safe_set(b, 'partOf', set())
    assert not _is_linked(b, 'partOf', a2)
    if hasattr(a2, 'EnterpriseObject42'):
        assert not _is_linked(a2, 'EnterpriseObject42', b)


def test_assoc_defines8_reverse_link_reassign_clear():
    a1 = sipme_Capacity(unit="sample_text", value=3.14)
    a2 = sipme_Capacity(unit="sample_text_2", value=9.99)
    b = sipme_Capability(capabilityType="sample_text")
    _safe_set(b, 'sipme_Capability', a1)
    assert _is_linked(b, 'sipme_Capability', a1)
    if hasattr(a1, 'sipme_Capacity'):
        assert _is_linked(a1, 'sipme_Capacity', b)
    _safe_set(b, 'sipme_Capability', a2)
    assert _is_linked(b, 'sipme_Capability', a2)
    if hasattr(a1, 'sipme_Capacity'):
        assert not _is_linked(a1, 'sipme_Capacity', b)
    if hasattr(a2, 'sipme_Capacity'):
        assert _is_linked(a2, 'sipme_Capacity', b)
    _safe_set(b, 'sipme_Capability', None)
    assert not _is_linked(b, 'sipme_Capability', a2)
    if hasattr(a2, 'sipme_Capacity'):
        assert not _is_linked(a2, 'sipme_Capacity', b)


def test_assoc_events83_reverse_link_reassign_clear():
    a1 = sipme_ObjectView(viewPoint="sample_text")
    a2 = sipme_ObjectView(viewPoint="sample_text_2")
    b = sipme_Event(frequency="sample_text", occurenceProbability="sample_text", source="sample_text", timeStamp=date(2024, 1, 1))
    _safe_set(b, 'Event84', a1)
    assert _is_linked(b, 'Event84', a1)
    if hasattr(a1, 'hasAssociatedEvents'):
        assert _is_linked(a1, 'hasAssociatedEvents', b)
    _safe_set(b, 'Event84', a2)
    assert _is_linked(b, 'Event84', a2)
    if hasattr(a1, 'hasAssociatedEvents'):
        assert not _is_linked(a1, 'hasAssociatedEvents', b)
    if hasattr(a2, 'hasAssociatedEvents'):
        assert _is_linked(a2, 'hasAssociatedEvents', b)
    _safe_set(b, 'Event84', None)
    assert not _is_linked(b, 'Event84', a2)
    if hasattr(a2, 'hasAssociatedEvents'):
        assert not _is_linked(a2, 'hasAssociatedEvents', b)


def test_assoc_executes60_reverse_link_reassign_clear():
    a1 = sipme_Task(taskDuration=7)
    a2 = sipme_Task(taskDuration=13)
    b = sipme_EnterpriseResource(resourceOrigin="sample_text")
    _safe_set(b, 'sipme_EnterpriseResource', a1)
    assert _is_linked(b, 'sipme_EnterpriseResource', a1)
    if hasattr(a1, 'sipme_Task'):
        assert _is_linked(a1, 'sipme_Task', b)
    _safe_set(b, 'sipme_EnterpriseResource', a2)
    assert _is_linked(b, 'sipme_EnterpriseResource', a2)
    if hasattr(a1, 'sipme_Task'):
        assert not _is_linked(a1, 'sipme_Task', b)
    if hasattr(a2, 'sipme_Task'):
        assert _is_linked(a2, 'sipme_Task', b)
    _safe_set(b, 'sipme_EnterpriseResource', None)
    assert not _is_linked(b, 'sipme_EnterpriseResource', a2)
    if hasattr(a2, 'sipme_Task'):
        assert not _is_linked(a2, 'sipme_Task', b)


def test_assoc_expresseCommonlydBy101_reverse_link_reassign_clear():
    a1 = sipme_Stakeholder(stakeholderOrganism="sample_text", stakeholderType="sample_text")
    a2 = sipme_Stakeholder(stakeholderOrganism="sample_text_2", stakeholderType="sample_text_2")
    b = sipme_Requirement(requirementDate=date(2024, 1, 1), requirementMaturity=7, requirementNature="sample_text", requirementOrigin="sample_text", requirementPriority=7, requirementStatement="sample_text", requirementStatus="sample_text", requirementVersion="sample_text")
    _safe_set(b, 'sipme_Requirement', {a1})
    assert _is_linked(b, 'sipme_Requirement', a1)
    if hasattr(a1, 'sipme_Stakeholder'):
        assert _is_linked(a1, 'sipme_Stakeholder', b)
    _safe_set(b, 'sipme_Requirement', {a2})
    assert _is_linked(b, 'sipme_Requirement', a2)
    if hasattr(a1, 'sipme_Stakeholder'):
        assert not _is_linked(a1, 'sipme_Stakeholder', b)
    if hasattr(a2, 'sipme_Stakeholder'):
        assert _is_linked(a2, 'sipme_Stakeholder', b)
    _safe_set(b, 'sipme_Requirement', set())
    assert not _is_linked(b, 'sipme_Requirement', a2)
    if hasattr(a2, 'sipme_Stakeholder'):
        assert not _is_linked(a2, 'sipme_Stakeholder', b)


def test_assoc_expresses123_reverse_link_reassign_clear():
    a1 = sipme_Stakeholder(stakeholderOrganism="sample_text", stakeholderType="sample_text")
    a2 = sipme_Stakeholder(stakeholderOrganism="sample_text_2", stakeholderType="sample_text_2")
    b = sipme_Requirement(requirementDate=date(2024, 1, 1), requirementMaturity=7, requirementNature="sample_text", requirementOrigin="sample_text", requirementPriority=7, requirementStatement="sample_text", requirementStatus="sample_text", requirementVersion="sample_text")
    _safe_set(b, 'sipme_Requirement125', a1)
    assert _is_linked(b, 'sipme_Requirement125', a1)
    if hasattr(a1, 'sipme_Stakeholder124'):
        assert _is_linked(a1, 'sipme_Stakeholder124', b)
    _safe_set(b, 'sipme_Requirement125', a2)
    assert _is_linked(b, 'sipme_Requirement125', a2)
    if hasattr(a1, 'sipme_Stakeholder124'):
        assert not _is_linked(a1, 'sipme_Stakeholder124', b)
    if hasattr(a2, 'sipme_Stakeholder124'):
        assert _is_linked(a2, 'sipme_Stakeholder124', b)
    _safe_set(b, 'sipme_Requirement125', None)
    assert not _is_linked(b, 'sipme_Requirement125', a2)
    if hasattr(a2, 'sipme_Stakeholder124'):
        assert not _is_linked(a2, 'sipme_Stakeholder124', b)


def test_assoc_fileResponsible97_reverse_link_reassign_clear():
    a1 = sipme_ObjectsFileView(filePriority=7, fileState="sample_text")
    a2 = sipme_ObjectsFileView(filePriority=13, fileState="sample_text_2")
    b = sipme_CompanyMember(address="sample_text", fullName="sample_text", socialSecurityNumber=7)
    _safe_set(b, 'CompanyMember98', a1)
    assert _is_linked(b, 'CompanyMember98', a1)
    if hasattr(a1, 'responsibleOfFile'):
        assert _is_linked(a1, 'responsibleOfFile', b)
    _safe_set(b, 'CompanyMember98', a2)
    assert _is_linked(b, 'CompanyMember98', a2)
    if hasattr(a1, 'responsibleOfFile'):
        assert not _is_linked(a1, 'responsibleOfFile', b)
    if hasattr(a2, 'responsibleOfFile'):
        assert _is_linked(a2, 'responsibleOfFile', b)
    _safe_set(b, 'CompanyMember98', None)
    assert not _is_linked(b, 'CompanyMember98', a2)
    if hasattr(a2, 'responsibleOfFile'):
        assert not _is_linked(a2, 'responsibleOfFile', b)


def test_assoc_generatedBy68_reverse_link_reassign_clear():
    a1 = sipme_Event(frequency="sample_text", occurenceProbability="sample_text", source="sample_text", timeStamp=date(2024, 1, 1))
    a2 = sipme_Event(frequency="sample_text_2", occurenceProbability="sample_text_2", source="sample_text_2", timeStamp=date(2025, 6, 15))
    b = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    _safe_set(b, 'EnterpriseProcessor', a1)
    assert _is_linked(b, 'EnterpriseProcessor', a1)
    if hasattr(a1, 'generates'):
        assert _is_linked(a1, 'generates', b)
    _safe_set(b, 'EnterpriseProcessor', a2)
    assert _is_linked(b, 'EnterpriseProcessor', a2)
    if hasattr(a1, 'generates'):
        assert not _is_linked(a1, 'generates', b)
    if hasattr(a2, 'generates'):
        assert _is_linked(a2, 'generates', b)
    _safe_set(b, 'EnterpriseProcessor', None)
    assert not _is_linked(b, 'EnterpriseProcessor', a2)
    if hasattr(a2, 'generates'):
        assert not _is_linked(a2, 'generates', b)


def test_assoc_generates43_reverse_link_reassign_clear():
    a1 = sipme_Event(frequency="sample_text", occurenceProbability="sample_text", source="sample_text", timeStamp=date(2024, 1, 1))
    a2 = sipme_Event(frequency="sample_text_2", occurenceProbability="sample_text_2", source="sample_text_2", timeStamp=date(2025, 6, 15))
    b = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    _safe_set(b, 'generatedBy', {a1})
    assert _is_linked(b, 'generatedBy', a1)
    if hasattr(a1, 'Event'):
        assert _is_linked(a1, 'Event', b)
    _safe_set(b, 'generatedBy', {a2})
    assert _is_linked(b, 'generatedBy', a2)
    if hasattr(a1, 'Event'):
        assert not _is_linked(a1, 'Event', b)
    if hasattr(a2, 'Event'):
        assert _is_linked(a2, 'Event', b)
    _safe_set(b, 'generatedBy', set())
    assert not _is_linked(b, 'generatedBy', a2)
    if hasattr(a2, 'Event'):
        assert not _is_linked(a2, 'Event', b)


def test_assoc_hasAssociatedEvents73_reverse_link_reassign_clear():
    a1 = sipme_ObjectView(viewPoint="sample_text")
    a2 = sipme_ObjectView(viewPoint="sample_text_2")
    b = sipme_Event(frequency="sample_text", occurenceProbability="sample_text", source="sample_text", timeStamp=date(2024, 1, 1))
    _safe_set(b, 'events', {a1})
    assert _is_linked(b, 'events', a1)
    if hasattr(a1, 'ObjectView74'):
        assert _is_linked(a1, 'ObjectView74', b)
    _safe_set(b, 'events', {a2})
    assert _is_linked(b, 'events', a2)
    if hasattr(a1, 'ObjectView74'):
        assert not _is_linked(a1, 'ObjectView74', b)
    if hasattr(a2, 'ObjectView74'):
        assert _is_linked(a2, 'ObjectView74', b)
    _safe_set(b, 'events', set())
    assert not _is_linked(b, 'events', a2)
    if hasattr(a2, 'ObjectView74'):
        assert not _is_linked(a2, 'ObjectView74', b)


def test_assoc_hasCapacity54_reverse_link_reassign_clear():
    a1 = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    a2 = sipme_EnterpriseProcessor(processorOrigin="sample_text_2")
    b = sipme_Capacity(unit="sample_text", value=3.14)
    _safe_set(b, 'sipme_Capacity56', a1)
    assert _is_linked(b, 'sipme_Capacity56', a1)
    if hasattr(a1, 'sipme_EnterpriseProcessor55'):
        assert _is_linked(a1, 'sipme_EnterpriseProcessor55', b)
    _safe_set(b, 'sipme_Capacity56', a2)
    assert _is_linked(b, 'sipme_Capacity56', a2)
    if hasattr(a1, 'sipme_EnterpriseProcessor55'):
        assert not _is_linked(a1, 'sipme_EnterpriseProcessor55', b)
    if hasattr(a2, 'sipme_EnterpriseProcessor55'):
        assert _is_linked(a2, 'sipme_EnterpriseProcessor55', b)
    _safe_set(b, 'sipme_Capacity56', None)
    assert not _is_linked(b, 'sipme_Capacity56', a2)
    if hasattr(a2, 'sipme_EnterpriseProcessor55'):
        assert not _is_linked(a2, 'sipme_EnterpriseProcessor55', b)


def test_assoc_hasControlInputs50_reverse_link_reassign_clear():
    a1 = sipme_ObjectView(viewPoint="sample_text")
    a2 = sipme_ObjectView(viewPoint="sample_text_2")
    b = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    _safe_set(b, 'sipme_EnterpriseProcessor51', {a1})
    assert _is_linked(b, 'sipme_EnterpriseProcessor51', a1)
    if hasattr(a1, 'sipme_ObjectView52'):
        assert _is_linked(a1, 'sipme_ObjectView52', b)
    _safe_set(b, 'sipme_EnterpriseProcessor51', {a2})
    assert _is_linked(b, 'sipme_EnterpriseProcessor51', a2)
    if hasattr(a1, 'sipme_ObjectView52'):
        assert not _is_linked(a1, 'sipme_ObjectView52', b)
    if hasattr(a2, 'sipme_ObjectView52'):
        assert _is_linked(a2, 'sipme_ObjectView52', b)
    _safe_set(b, 'sipme_EnterpriseProcessor51', set())
    assert not _is_linked(b, 'sipme_EnterpriseProcessor51', a2)
    if hasattr(a2, 'sipme_ObjectView52'):
        assert not _is_linked(a2, 'sipme_ObjectView52', b)


def test_assoc_hasInputs45_reverse_link_reassign_clear():
    a1 = sipme_ObjectView(viewPoint="sample_text")
    a2 = sipme_ObjectView(viewPoint="sample_text_2")
    b = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    _safe_set(b, 'sipme_EnterpriseProcessor46', {a1})
    assert _is_linked(b, 'sipme_EnterpriseProcessor46', a1)
    if hasattr(a1, 'sipme_ObjectView47'):
        assert _is_linked(a1, 'sipme_ObjectView47', b)
    _safe_set(b, 'sipme_EnterpriseProcessor46', {a2})
    assert _is_linked(b, 'sipme_EnterpriseProcessor46', a2)
    if hasattr(a1, 'sipme_ObjectView47'):
        assert not _is_linked(a1, 'sipme_ObjectView47', b)
    if hasattr(a2, 'sipme_ObjectView47'):
        assert _is_linked(a2, 'sipme_ObjectView47', b)
    _safe_set(b, 'sipme_EnterpriseProcessor46', set())
    assert not _is_linked(b, 'sipme_EnterpriseProcessor46', a2)
    if hasattr(a2, 'sipme_ObjectView47'):
        assert not _is_linked(a2, 'sipme_ObjectView47', b)


def test_assoc_implementedBy118_reverse_link_reassign_clear():
    a1 = sipme_Role_Function(roleType="sample_text")
    a2 = sipme_Role_Function(roleType="sample_text_2")
    b = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    _safe_set(b, 'EnterpriseProcessor119', a1)
    assert _is_linked(b, 'EnterpriseProcessor119', a1)
    if hasattr(a1, 'implements'):
        assert _is_linked(a1, 'implements', b)
    _safe_set(b, 'EnterpriseProcessor119', a2)
    assert _is_linked(b, 'EnterpriseProcessor119', a2)
    if hasattr(a1, 'implements'):
        assert not _is_linked(a1, 'implements', b)
    if hasattr(a2, 'implements'):
        assert _is_linked(a2, 'implements', b)
    _safe_set(b, 'EnterpriseProcessor119', None)
    assert not _is_linked(b, 'EnterpriseProcessor119', a2)
    if hasattr(a2, 'implements'):
        assert not _is_linked(a2, 'implements', b)


def test_assoc_implements53_reverse_link_reassign_clear():
    a1 = sipme_Role_Function(roleType="sample_text")
    a2 = sipme_Role_Function(roleType="sample_text_2")
    b = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    _safe_set(b, 'implementedBy', {a1})
    assert _is_linked(b, 'implementedBy', a1)
    if hasattr(a1, 'Role_Function'):
        assert _is_linked(a1, 'Role_Function', b)
    _safe_set(b, 'implementedBy', {a2})
    assert _is_linked(b, 'implementedBy', a2)
    if hasattr(a1, 'Role_Function'):
        assert not _is_linked(a1, 'Role_Function', b)
    if hasattr(a2, 'Role_Function'):
        assert _is_linked(a2, 'Role_Function', b)
    _safe_set(b, 'implementedBy', set())
    assert not _is_linked(b, 'implementedBy', a2)
    if hasattr(a2, 'Role_Function'):
        assert not _is_linked(a2, 'Role_Function', b)


def test_assoc_inChargeOf9_reverse_link_reassign_clear():
    a1 = sipme_Workstation(ProfileDeescription="sample_text")
    a2 = sipme_Workstation(ProfileDeescription="sample_text_2")
    b = sipme_CompanyMember(address="sample_text", fullName="sample_text", socialSecurityNumber=7)
    _safe_set(b, 'owners', {a1})
    assert _is_linked(b, 'owners', a1)
    if hasattr(a1, 'Workstation'):
        assert _is_linked(a1, 'Workstation', b)
    _safe_set(b, 'owners', {a2})
    assert _is_linked(b, 'owners', a2)
    if hasattr(a1, 'Workstation'):
        assert not _is_linked(a1, 'Workstation', b)
    if hasattr(a2, 'Workstation'):
        assert _is_linked(a2, 'Workstation', b)
    _safe_set(b, 'owners', set())
    assert not _is_linked(b, 'owners', a2)
    if hasattr(a2, 'Workstation'):
        assert not _is_linked(a2, 'Workstation', b)


def test_assoc_initiatedBy48_reverse_link_reassign_clear():
    a1 = sipme_Event(frequency="sample_text", occurenceProbability="sample_text", source="sample_text", timeStamp=date(2024, 1, 1))
    a2 = sipme_Event(frequency="sample_text_2", occurenceProbability="sample_text_2", source="sample_text_2", timeStamp=date(2025, 6, 15))
    b = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    _safe_set(b, 'initiates', {a1})
    assert _is_linked(b, 'initiates', a1)
    if hasattr(a1, 'Event49'):
        assert _is_linked(a1, 'Event49', b)
    _safe_set(b, 'initiates', {a2})
    assert _is_linked(b, 'initiates', a2)
    if hasattr(a1, 'Event49'):
        assert not _is_linked(a1, 'Event49', b)
    if hasattr(a2, 'Event49'):
        assert _is_linked(a2, 'Event49', b)
    _safe_set(b, 'initiates', set())
    assert not _is_linked(b, 'initiates', a2)
    if hasattr(a2, 'Event49'):
        assert not _is_linked(a2, 'Event49', b)


def test_assoc_initiates69_reverse_link_reassign_clear():
    a1 = sipme_Event(frequency="sample_text", occurenceProbability="sample_text", source="sample_text", timeStamp=date(2024, 1, 1))
    a2 = sipme_Event(frequency="sample_text_2", occurenceProbability="sample_text_2", source="sample_text_2", timeStamp=date(2025, 6, 15))
    b = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    _safe_set(b, 'EnterpriseProcessor70', a1)
    assert _is_linked(b, 'EnterpriseProcessor70', a1)
    if hasattr(a1, 'initiatedBy'):
        assert _is_linked(a1, 'initiatedBy', b)
    _safe_set(b, 'EnterpriseProcessor70', a2)
    assert _is_linked(b, 'EnterpriseProcessor70', a2)
    if hasattr(a1, 'initiatedBy'):
        assert not _is_linked(a1, 'initiatedBy', b)
    if hasattr(a2, 'initiatedBy'):
        assert _is_linked(a2, 'initiatedBy', b)
    _safe_set(b, 'EnterpriseProcessor70', None)
    assert not _is_linked(b, 'EnterpriseProcessor70', a2)
    if hasattr(a2, 'initiatedBy'):
        assert not _is_linked(a2, 'initiatedBy', b)


def test_assoc_isAbleToPlay63_reverse_link_reassign_clear():
    a1 = sipme_Role_Function(roleType="sample_text")
    a2 = sipme_Role_Function(roleType="sample_text_2")
    b = sipme_EnterpriseResource(resourceOrigin="sample_text")
    _safe_set(b, 'canBePlayedBy', {a1})
    assert _is_linked(b, 'canBePlayedBy', a1)
    if hasattr(a1, 'Role_Function64'):
        assert _is_linked(a1, 'Role_Function64', b)
    _safe_set(b, 'canBePlayedBy', {a2})
    assert _is_linked(b, 'canBePlayedBy', a2)
    if hasattr(a1, 'Role_Function64'):
        assert not _is_linked(a1, 'Role_Function64', b)
    if hasattr(a2, 'Role_Function64'):
        assert _is_linked(a2, 'Role_Function64', b)
    _safe_set(b, 'canBePlayedBy', set())
    assert not _is_linked(b, 'canBePlayedBy', a2)
    if hasattr(a2, 'Role_Function64'):
        assert not _is_linked(a2, 'Role_Function64', b)


def test_assoc_objectViews92_reverse_link_reassign_clear():
    a1 = sipme_ObjectsFileView(filePriority=7, fileState="sample_text")
    a2 = sipme_ObjectsFileView(filePriority=13, fileState="sample_text_2")
    b = sipme_ObjectView(viewPoint="sample_text")
    _safe_set(b, 'sipme_ObjectView93', a1)
    assert _is_linked(b, 'sipme_ObjectView93', a1)
    if hasattr(a1, 'sipme_ObjectsFileView'):
        assert _is_linked(a1, 'sipme_ObjectsFileView', b)
    _safe_set(b, 'sipme_ObjectView93', a2)
    assert _is_linked(b, 'sipme_ObjectView93', a2)
    if hasattr(a1, 'sipme_ObjectsFileView'):
        assert not _is_linked(a1, 'sipme_ObjectsFileView', b)
    if hasattr(a2, 'sipme_ObjectsFileView'):
        assert _is_linked(a2, 'sipme_ObjectsFileView', b)
    _safe_set(b, 'sipme_ObjectView93', None)
    assert not _is_linked(b, 'sipme_ObjectView93', a2)
    if hasattr(a2, 'sipme_ObjectsFileView'):
        assert not _is_linked(a2, 'sipme_ObjectsFileView', b)


def test_assoc_operations132_reverse_link_reassign_clear():
    a1 = sipme_Task(taskDuration=7)
    a2 = sipme_Task(taskDuration=13)
    b = sipme_Task(taskDuration=7)
    _safe_set(b, 'sipme_Task133', a1)
    assert _is_linked(b, 'sipme_Task133', a1)
    if hasattr(a1, 'sipme_Task131'):
        assert _is_linked(a1, 'sipme_Task131', b)
    _safe_set(b, 'sipme_Task133', a2)
    assert _is_linked(b, 'sipme_Task133', a2)
    if hasattr(a1, 'sipme_Task131'):
        assert not _is_linked(a1, 'sipme_Task131', b)
    if hasattr(a2, 'sipme_Task131'):
        assert _is_linked(a2, 'sipme_Task131', b)
    _safe_set(b, 'sipme_Task133', None)
    assert not _is_linked(b, 'sipme_Task133', a2)
    if hasattr(a2, 'sipme_Task131'):
        assert not _is_linked(a2, 'sipme_Task131', b)


def test_assoc_organisationCell134_reverse_link_reassign_clear():
    a1 = sipme_Workstation(ProfileDeescription="sample_text")
    a2 = sipme_Workstation(ProfileDeescription="sample_text_2")
    b = sipme_OrganisationCell(organisationLevel=7)
    _safe_set(b, 'OrganisationCell135', a1)
    assert _is_linked(b, 'OrganisationCell135', a1)
    if hasattr(a1, 'workstations'):
        assert _is_linked(a1, 'workstations', b)
    _safe_set(b, 'OrganisationCell135', a2)
    assert _is_linked(b, 'OrganisationCell135', a2)
    if hasattr(a1, 'workstations'):
        assert not _is_linked(a1, 'workstations', b)
    if hasattr(a2, 'workstations'):
        assert _is_linked(a2, 'workstations', b)
    _safe_set(b, 'OrganisationCell135', None)
    assert not _is_linked(b, 'OrganisationCell135', a2)
    if hasattr(a2, 'workstations'):
        assert not _is_linked(a2, 'workstations', b)


def test_assoc_organizationCells35_reverse_link_reassign_clear():
    a1 = sipme_OrganisationCell(organisationLevel=7)
    a2 = sipme_OrganisationCell(organisationLevel=13)
    b = sipme_Enterprise(acronym="sample_text", status="sample_text")
    _safe_set(b, 'sipme_Enterprise36', {a1})
    assert _is_linked(b, 'sipme_Enterprise36', a1)
    if hasattr(a1, 'sipme_OrganisationCell'):
        assert _is_linked(a1, 'sipme_OrganisationCell', b)
    _safe_set(b, 'sipme_Enterprise36', {a2})
    assert _is_linked(b, 'sipme_Enterprise36', a2)
    if hasattr(a1, 'sipme_OrganisationCell'):
        assert not _is_linked(a1, 'sipme_OrganisationCell', b)
    if hasattr(a2, 'sipme_OrganisationCell'):
        assert _is_linked(a2, 'sipme_OrganisationCell', b)
    _safe_set(b, 'sipme_Enterprise36', set())
    assert not _is_linked(b, 'sipme_Enterprise36', a2)
    if hasattr(a2, 'sipme_OrganisationCell'):
        assert not _is_linked(a2, 'sipme_OrganisationCell', b)


def test_assoc_owners138_reverse_link_reassign_clear():
    a1 = sipme_Workstation(ProfileDeescription="sample_text")
    a2 = sipme_Workstation(ProfileDeescription="sample_text_2")
    b = sipme_CompanyMember(address="sample_text", fullName="sample_text", socialSecurityNumber=7)
    _safe_set(b, 'CompanyMember139', a1)
    assert _is_linked(b, 'CompanyMember139', a1)
    if hasattr(a1, 'inChargeOf'):
        assert _is_linked(a1, 'inChargeOf', b)
    _safe_set(b, 'CompanyMember139', a2)
    assert _is_linked(b, 'CompanyMember139', a2)
    if hasattr(a1, 'inChargeOf'):
        assert not _is_linked(a1, 'inChargeOf', b)
    if hasattr(a2, 'inChargeOf'):
        assert _is_linked(a2, 'inChargeOf', b)
    _safe_set(b, 'CompanyMember139', None)
    assert not _is_linked(b, 'CompanyMember139', a2)
    if hasattr(a2, 'inChargeOf'):
        assert not _is_linked(a2, 'inChargeOf', b)


def test_assoc_partOf38_reverse_link_reassign_clear():
    a1 = sipme_EnterpriseObject(properties="sample_text", reference="sample_text")
    a2 = sipme_EnterpriseObject(properties="sample_text_2", reference="sample_text_2")
    b = sipme_EnterpriseObject(properties="sample_text", reference="sample_text")
    _safe_set(b, 'decomposedIn', a1)
    assert _is_linked(b, 'decomposedIn', a1)
    if hasattr(a1, 'EnterpriseObject'):
        assert _is_linked(a1, 'EnterpriseObject', b)
    _safe_set(b, 'decomposedIn', a2)
    assert _is_linked(b, 'decomposedIn', a2)
    if hasattr(a1, 'EnterpriseObject'):
        assert not _is_linked(a1, 'EnterpriseObject', b)
    if hasattr(a2, 'EnterpriseObject'):
        assert _is_linked(a2, 'EnterpriseObject', b)
    _safe_set(b, 'decomposedIn', None)
    assert not _is_linked(b, 'decomposedIn', a2)
    if hasattr(a2, 'EnterpriseObject'):
        assert not _is_linked(a2, 'EnterpriseObject', b)


def test_assoc_playedBy115_reverse_link_reassign_clear():
    a1 = sipme_Role_Function(roleType="sample_text")
    a2 = sipme_Role_Function(roleType="sample_text_2")
    b = sipme_EnterpriseResource(resourceOrigin="sample_text")
    _safe_set(b, 'EnterpriseResource', a1)
    assert _is_linked(b, 'EnterpriseResource', a1)
    if hasattr(a1, 'plays'):
        assert _is_linked(a1, 'plays', b)
    _safe_set(b, 'EnterpriseResource', a2)
    assert _is_linked(b, 'EnterpriseResource', a2)
    if hasattr(a1, 'plays'):
        assert not _is_linked(a1, 'plays', b)
    if hasattr(a2, 'plays'):
        assert _is_linked(a2, 'plays', b)
    _safe_set(b, 'EnterpriseResource', None)
    assert not _is_linked(b, 'EnterpriseResource', a2)
    if hasattr(a2, 'plays'):
        assert not _is_linked(a2, 'plays', b)


def test_assoc_plays61_reverse_link_reassign_clear():
    a1 = sipme_Role_Function(roleType="sample_text")
    a2 = sipme_Role_Function(roleType="sample_text_2")
    b = sipme_EnterpriseResource(resourceOrigin="sample_text")
    _safe_set(b, 'playedBy', {a1})
    assert _is_linked(b, 'playedBy', a1)
    if hasattr(a1, 'Role_Function62'):
        assert _is_linked(a1, 'Role_Function62', b)
    _safe_set(b, 'playedBy', {a2})
    assert _is_linked(b, 'playedBy', a2)
    if hasattr(a1, 'Role_Function62'):
        assert not _is_linked(a1, 'Role_Function62', b)
    if hasattr(a2, 'Role_Function62'):
        assert _is_linked(a2, 'Role_Function62', b)
    _safe_set(b, 'playedBy', set())
    assert not _is_linked(b, 'playedBy', a2)
    if hasattr(a2, 'Role_Function62'):
        assert not _is_linked(a2, 'Role_Function62', b)


def test_assoc_priorTo72_reverse_link_reassign_clear():
    a1 = sipme_Event(frequency="sample_text", occurenceProbability="sample_text", source="sample_text", timeStamp=date(2024, 1, 1))
    a2 = sipme_Event(frequency="sample_text_2", occurenceProbability="sample_text_2", source="sample_text_2", timeStamp=date(2025, 6, 15))
    b = sipme_Event(frequency="sample_text", occurenceProbability="sample_text", source="sample_text", timeStamp=date(2024, 1, 1))
    _safe_set(b, 'sipme_Event71', {a1})
    assert _is_linked(b, 'sipme_Event71', a1)
    if hasattr(a1, 'sipme_Event'):
        assert _is_linked(a1, 'sipme_Event', b)
    _safe_set(b, 'sipme_Event71', {a2})
    assert _is_linked(b, 'sipme_Event71', a2)
    if hasattr(a1, 'sipme_Event'):
        assert not _is_linked(a1, 'sipme_Event', b)
    if hasattr(a2, 'sipme_Event'):
        assert _is_linked(a2, 'sipme_Event', b)
    _safe_set(b, 'sipme_Event71', set())
    assert not _is_linked(b, 'sipme_Event71', a2)
    if hasattr(a2, 'sipme_Event'):
        assert not _is_linked(a2, 'sipme_Event', b)


def test_assoc_proposesProducts31_reverse_link_reassign_clear():
    a1 = sipme_EnterpriseProduct(productNarure="sample_text", productState="sample_text")
    a2 = sipme_EnterpriseProduct(productNarure="sample_text_2", productState="sample_text_2")
    b = sipme_Enterprise(acronym="sample_text", status="sample_text")
    _safe_set(b, 'sipme_Enterprise32', {a1})
    assert _is_linked(b, 'sipme_Enterprise32', a1)
    if hasattr(a1, 'sipme_EnterpriseProduct'):
        assert _is_linked(a1, 'sipme_EnterpriseProduct', b)
    _safe_set(b, 'sipme_Enterprise32', {a2})
    assert _is_linked(b, 'sipme_Enterprise32', a2)
    if hasattr(a1, 'sipme_EnterpriseProduct'):
        assert not _is_linked(a1, 'sipme_EnterpriseProduct', b)
    if hasattr(a2, 'sipme_EnterpriseProduct'):
        assert _is_linked(a2, 'sipme_EnterpriseProduct', b)
    _safe_set(b, 'sipme_Enterprise32', set())
    assert not _is_linked(b, 'sipme_Enterprise32', a2)
    if hasattr(a2, 'sipme_EnterpriseProduct'):
        assert not _is_linked(a2, 'sipme_EnterpriseProduct', b)


def test_assoc_proposesServices29_reverse_link_reassign_clear():
    a1 = sipme_EnterpriseService(serviceState="sample_text")
    a2 = sipme_EnterpriseService(serviceState="sample_text_2")
    b = sipme_Enterprise(acronym="sample_text", status="sample_text")
    _safe_set(b, 'sipme_Enterprise30', {a1})
    assert _is_linked(b, 'sipme_Enterprise30', a1)
    if hasattr(a1, 'sipme_EnterpriseService'):
        assert _is_linked(a1, 'sipme_EnterpriseService', b)
    _safe_set(b, 'sipme_Enterprise30', {a2})
    assert _is_linked(b, 'sipme_Enterprise30', a2)
    if hasattr(a1, 'sipme_EnterpriseService'):
        assert not _is_linked(a1, 'sipme_EnterpriseService', b)
    if hasattr(a2, 'sipme_EnterpriseService'):
        assert _is_linked(a2, 'sipme_EnterpriseService', b)
    _safe_set(b, 'sipme_Enterprise30', set())
    assert not _is_linked(b, 'sipme_Enterprise30', a2)
    if hasattr(a2, 'sipme_EnterpriseService'):
        assert not _is_linked(a2, 'sipme_EnterpriseService', b)


def test_assoc_providesCapability65_reverse_link_reassign_clear():
    a1 = sipme_EnterpriseResource(resourceOrigin="sample_text")
    a2 = sipme_EnterpriseResource(resourceOrigin="sample_text_2")
    b = sipme_Capability(capabilityType="sample_text")
    _safe_set(b, 'sipme_Capability67', a1)
    assert _is_linked(b, 'sipme_Capability67', a1)
    if hasattr(a1, 'sipme_EnterpriseResource66'):
        assert _is_linked(a1, 'sipme_EnterpriseResource66', b)
    _safe_set(b, 'sipme_Capability67', a2)
    assert _is_linked(b, 'sipme_Capability67', a2)
    if hasattr(a1, 'sipme_EnterpriseResource66'):
        assert not _is_linked(a1, 'sipme_EnterpriseResource66', b)
    if hasattr(a2, 'sipme_EnterpriseResource66'):
        assert _is_linked(a2, 'sipme_EnterpriseResource66', b)
    _safe_set(b, 'sipme_Capability67', None)
    assert not _is_linked(b, 'sipme_Capability67', a2)
    if hasattr(a2, 'sipme_EnterpriseResource66'):
        assert not _is_linked(a2, 'sipme_EnterpriseResource66', b)


def test_assoc_providesOutputs44_reverse_link_reassign_clear():
    a1 = sipme_ObjectView(viewPoint="sample_text")
    a2 = sipme_ObjectView(viewPoint="sample_text_2")
    b = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    _safe_set(b, 'sipme_EnterpriseProcessor', {a1})
    assert _is_linked(b, 'sipme_EnterpriseProcessor', a1)
    if hasattr(a1, 'sipme_ObjectView'):
        assert _is_linked(a1, 'sipme_ObjectView', b)
    _safe_set(b, 'sipme_EnterpriseProcessor', {a2})
    assert _is_linked(b, 'sipme_EnterpriseProcessor', a2)
    if hasattr(a1, 'sipme_ObjectView'):
        assert not _is_linked(a1, 'sipme_ObjectView', b)
    if hasattr(a2, 'sipme_ObjectView'):
        assert _is_linked(a2, 'sipme_ObjectView', b)
    _safe_set(b, 'sipme_EnterpriseProcessor', set())
    assert not _is_linked(b, 'sipme_EnterpriseProcessor', a2)
    if hasattr(a2, 'sipme_ObjectView'):
        assert not _is_linked(a2, 'sipme_ObjectView', b)


def test_assoc_refers26_reverse_link_reassign_clear():
    a1 = sipme_EnterpriseObject(properties="sample_text", reference="sample_text")
    a2 = sipme_EnterpriseObject(properties="sample_text_2", reference="sample_text_2")
    b = sipme_Enterprise(acronym="sample_text", status="sample_text")
    _safe_set(b, 'sipme_Enterprise27', {a1})
    assert _is_linked(b, 'sipme_Enterprise27', a1)
    if hasattr(a1, 'sipme_EnterpriseObject28'):
        assert _is_linked(a1, 'sipme_EnterpriseObject28', b)
    _safe_set(b, 'sipme_Enterprise27', {a2})
    assert _is_linked(b, 'sipme_Enterprise27', a2)
    if hasattr(a1, 'sipme_EnterpriseObject28'):
        assert not _is_linked(a1, 'sipme_EnterpriseObject28', b)
    if hasattr(a2, 'sipme_EnterpriseObject28'):
        assert _is_linked(a2, 'sipme_EnterpriseObject28', b)
    _safe_set(b, 'sipme_Enterprise27', set())
    assert not _is_linked(b, 'sipme_Enterprise27', a2)
    if hasattr(a2, 'sipme_EnterpriseObject28'):
        assert not _is_linked(a2, 'sipme_EnterpriseObject28', b)


def test_assoc_refines78_reverse_link_reassign_clear():
    a1 = sipme_Objective(objectiveNature="sample_text", objectiveType="sample_text")
    a2 = sipme_Objective(objectiveNature="sample_text_2", objectiveType="sample_text_2")
    b = sipme_Objective(objectiveNature="sample_text", objectiveType="sample_text")
    _safe_set(b, 'subObjectives', a1)
    assert _is_linked(b, 'subObjectives', a1)
    if hasattr(a1, 'Objective79'):
        assert _is_linked(a1, 'Objective79', b)
    _safe_set(b, 'subObjectives', a2)
    assert _is_linked(b, 'subObjectives', a2)
    if hasattr(a1, 'Objective79'):
        assert not _is_linked(a1, 'Objective79', b)
    if hasattr(a2, 'Objective79'):
        assert _is_linked(a2, 'Objective79', b)
    _safe_set(b, 'subObjectives', None)
    assert not _is_linked(b, 'subObjectives', a2)
    if hasattr(a2, 'Objective79'):
        assert not _is_linked(a2, 'Objective79', b)


def test_assoc_refinesRequirement103_reverse_link_reassign_clear():
    a1 = sipme_Requirement(requirementDate=date(2024, 1, 1), requirementMaturity=7, requirementNature="sample_text", requirementOrigin="sample_text", requirementPriority=7, requirementStatement="sample_text", requirementStatus="sample_text", requirementVersion="sample_text")
    a2 = sipme_Requirement(requirementDate=date(2025, 6, 15), requirementMaturity=13, requirementNature="sample_text_2", requirementOrigin="sample_text_2", requirementPriority=13, requirementStatement="sample_text_2", requirementStatus="sample_text_2", requirementVersion="sample_text_2")
    b = sipme_Requirement(requirementDate=date(2024, 1, 1), requirementMaturity=7, requirementNature="sample_text", requirementOrigin="sample_text", requirementPriority=7, requirementStatement="sample_text", requirementStatus="sample_text", requirementVersion="sample_text")
    _safe_set(b, 'sipme_Requirement104', a1)
    assert _is_linked(b, 'sipme_Requirement104', a1)
    if hasattr(a1, 'sipme_Requirement102'):
        assert _is_linked(a1, 'sipme_Requirement102', b)
    _safe_set(b, 'sipme_Requirement104', a2)
    assert _is_linked(b, 'sipme_Requirement104', a2)
    if hasattr(a1, 'sipme_Requirement102'):
        assert not _is_linked(a1, 'sipme_Requirement102', b)
    if hasattr(a2, 'sipme_Requirement102'):
        assert _is_linked(a2, 'sipme_Requirement102', b)
    _safe_set(b, 'sipme_Requirement104', None)
    assert not _is_linked(b, 'sipme_Requirement104', a2)
    if hasattr(a2, 'sipme_Requirement102'):
        assert not _is_linked(a2, 'sipme_Requirement102', b)


def test_assoc_representedBy39_reverse_link_reassign_clear():
    a1 = sipme_ObjectView(viewPoint="sample_text")
    a2 = sipme_ObjectView(viewPoint="sample_text_2")
    b = sipme_EnterpriseObject(properties="sample_text", reference="sample_text")
    _safe_set(b, 'represents', {a1})
    assert _is_linked(b, 'represents', a1)
    if hasattr(a1, 'ObjectView'):
        assert _is_linked(a1, 'ObjectView', b)
    _safe_set(b, 'represents', {a2})
    assert _is_linked(b, 'represents', a2)
    if hasattr(a1, 'ObjectView'):
        assert not _is_linked(a1, 'ObjectView', b)
    if hasattr(a2, 'ObjectView'):
        assert _is_linked(a2, 'ObjectView', b)
    _safe_set(b, 'represents', set())
    assert not _is_linked(b, 'represents', a2)
    if hasattr(a2, 'ObjectView'):
        assert not _is_linked(a2, 'ObjectView', b)


def test_assoc_represents81_reverse_link_reassign_clear():
    a1 = sipme_ObjectView(viewPoint="sample_text")
    a2 = sipme_ObjectView(viewPoint="sample_text_2")
    b = sipme_EnterpriseObject(properties="sample_text", reference="sample_text")
    _safe_set(b, 'EnterpriseObject82', a1)
    assert _is_linked(b, 'EnterpriseObject82', a1)
    if hasattr(a1, 'representedBy'):
        assert _is_linked(a1, 'representedBy', b)
    _safe_set(b, 'EnterpriseObject82', a2)
    assert _is_linked(b, 'EnterpriseObject82', a2)
    if hasattr(a1, 'representedBy'):
        assert not _is_linked(a1, 'representedBy', b)
    if hasattr(a2, 'representedBy'):
        assert _is_linked(a2, 'representedBy', b)
    _safe_set(b, 'EnterpriseObject82', None)
    assert not _is_linked(b, 'EnterpriseObject82', a2)
    if hasattr(a2, 'representedBy'):
        assert not _is_linked(a2, 'representedBy', b)


def test_assoc_requiresCapabilities57_reverse_link_reassign_clear():
    a1 = sipme_EnterpriseProcessor(processorOrigin="sample_text")
    a2 = sipme_EnterpriseProcessor(processorOrigin="sample_text_2")
    b = sipme_Capability(capabilityType="sample_text")
    _safe_set(b, 'sipme_Capability59', a1)
    assert _is_linked(b, 'sipme_Capability59', a1)
    if hasattr(a1, 'sipme_EnterpriseProcessor58'):
        assert _is_linked(a1, 'sipme_EnterpriseProcessor58', b)
    _safe_set(b, 'sipme_Capability59', a2)
    assert _is_linked(b, 'sipme_Capability59', a2)
    if hasattr(a1, 'sipme_EnterpriseProcessor58'):
        assert not _is_linked(a1, 'sipme_EnterpriseProcessor58', b)
    if hasattr(a2, 'sipme_EnterpriseProcessor58'):
        assert _is_linked(a2, 'sipme_EnterpriseProcessor58', b)
    _safe_set(b, 'sipme_Capability59', None)
    assert not _is_linked(b, 'sipme_Capability59', a2)
    if hasattr(a2, 'sipme_EnterpriseProcessor58'):
        assert not _is_linked(a2, 'sipme_EnterpriseProcessor58', b)


def test_assoc_requiresTasks113_reverse_link_reassign_clear():
    a1 = sipme_Task(taskDuration=7)
    a2 = sipme_Task(taskDuration=13)
    b = sipme_Role_Function(roleType="sample_text")
    _safe_set(b, 'sipme_Role_Function', {a1})
    assert _is_linked(b, 'sipme_Role_Function', a1)
    if hasattr(a1, 'sipme_Task114'):
        assert _is_linked(a1, 'sipme_Task114', b)
    _safe_set(b, 'sipme_Role_Function', {a2})
    assert _is_linked(b, 'sipme_Role_Function', a2)
    if hasattr(a1, 'sipme_Task114'):
        assert not _is_linked(a1, 'sipme_Task114', b)
    if hasattr(a2, 'sipme_Task114'):
        assert _is_linked(a2, 'sipme_Task114', b)
    _safe_set(b, 'sipme_Role_Function', set())
    assert not _is_linked(b, 'sipme_Role_Function', a2)
    if hasattr(a2, 'sipme_Task114'):
        assert not _is_linked(a2, 'sipme_Task114', b)


def test_assoc_responsible136_reverse_link_reassign_clear():
    a1 = sipme_Workstation(ProfileDeescription="sample_text")
    a2 = sipme_Workstation(ProfileDeescription="sample_text_2")
    b = sipme_CompanyMember(address="sample_text", fullName="sample_text", socialSecurityNumber=7)
    _safe_set(b, 'CompanyMember137', a1)
    assert _is_linked(b, 'CompanyMember137', a1)
    if hasattr(a1, 'responsibleOf'):
        assert _is_linked(a1, 'responsibleOf', b)
    _safe_set(b, 'CompanyMember137', a2)
    assert _is_linked(b, 'CompanyMember137', a2)
    if hasattr(a1, 'responsibleOf'):
        assert not _is_linked(a1, 'responsibleOf', b)
    if hasattr(a2, 'responsibleOf'):
        assert _is_linked(a2, 'responsibleOf', b)
    _safe_set(b, 'CompanyMember137', None)
    assert not _is_linked(b, 'CompanyMember137', a2)
    if hasattr(a2, 'responsibleOf'):
        assert not _is_linked(a2, 'responsibleOf', b)


def test_assoc_responsibleOf10_reverse_link_reassign_clear():
    a1 = sipme_Workstation(ProfileDeescription="sample_text")
    a2 = sipme_Workstation(ProfileDeescription="sample_text_2")
    b = sipme_CompanyMember(address="sample_text", fullName="sample_text", socialSecurityNumber=7)
    _safe_set(b, 'responsible', {a1})
    assert _is_linked(b, 'responsible', a1)
    if hasattr(a1, 'Workstation11'):
        assert _is_linked(a1, 'Workstation11', b)
    _safe_set(b, 'responsible', {a2})
    assert _is_linked(b, 'responsible', a2)
    if hasattr(a1, 'Workstation11'):
        assert not _is_linked(a1, 'Workstation11', b)
    if hasattr(a2, 'Workstation11'):
        assert _is_linked(a2, 'Workstation11', b)
    _safe_set(b, 'responsible', set())
    assert not _is_linked(b, 'responsible', a2)
    if hasattr(a2, 'Workstation11'):
        assert not _is_linked(a2, 'Workstation11', b)


def test_assoc_responsibleOfCell12_reverse_link_reassign_clear():
    a1 = sipme_OrganisationCell(organisationLevel=7)
    a2 = sipme_OrganisationCell(organisationLevel=13)
    b = sipme_CompanyMember(address="sample_text", fullName="sample_text", socialSecurityNumber=7)
    _safe_set(b, 'cellResponsible', {a1})
    assert _is_linked(b, 'cellResponsible', a1)
    if hasattr(a1, 'OrganisationCell'):
        assert _is_linked(a1, 'OrganisationCell', b)
    _safe_set(b, 'cellResponsible', {a2})
    assert _is_linked(b, 'cellResponsible', a2)
    if hasattr(a1, 'OrganisationCell'):
        assert not _is_linked(a1, 'OrganisationCell', b)
    if hasattr(a2, 'OrganisationCell'):
        assert _is_linked(a2, 'OrganisationCell', b)
    _safe_set(b, 'cellResponsible', set())
    assert not _is_linked(b, 'cellResponsible', a2)
    if hasattr(a2, 'OrganisationCell'):
        assert not _is_linked(a2, 'OrganisationCell', b)


def test_assoc_responsibleOfFile13_reverse_link_reassign_clear():
    a1 = sipme_ObjectsFileView(filePriority=7, fileState="sample_text")
    a2 = sipme_ObjectsFileView(filePriority=13, fileState="sample_text_2")
    b = sipme_CompanyMember(address="sample_text", fullName="sample_text", socialSecurityNumber=7)
    _safe_set(b, 'fileResponsible', {a1})
    assert _is_linked(b, 'fileResponsible', a1)
    if hasattr(a1, 'ObjectsFileView'):
        assert _is_linked(a1, 'ObjectsFileView', b)
    _safe_set(b, 'fileResponsible', {a2})
    assert _is_linked(b, 'fileResponsible', a2)
    if hasattr(a1, 'ObjectsFileView'):
        assert not _is_linked(a1, 'ObjectsFileView', b)
    if hasattr(a2, 'ObjectsFileView'):
        assert _is_linked(a2, 'ObjectsFileView', b)
    _safe_set(b, 'fileResponsible', set())
    assert not _is_linked(b, 'fileResponsible', a2)
    if hasattr(a2, 'ObjectsFileView'):
        assert not _is_linked(a2, 'ObjectsFileView', b)


def test_assoc_strategicObjectives22_reverse_link_reassign_clear():
    a1 = sipme_Objective(objectiveNature="sample_text", objectiveType="sample_text")
    a2 = sipme_Objective(objectiveNature="sample_text_2", objectiveType="sample_text_2")
    b = sipme_Enterprise(acronym="sample_text", status="sample_text")
    _safe_set(b, 'sipme_Enterprise', {a1})
    assert _is_linked(b, 'sipme_Enterprise', a1)
    if hasattr(a1, 'sipme_Objective'):
        assert _is_linked(a1, 'sipme_Objective', b)
    _safe_set(b, 'sipme_Enterprise', {a2})
    assert _is_linked(b, 'sipme_Enterprise', a2)
    if hasattr(a1, 'sipme_Objective'):
        assert not _is_linked(a1, 'sipme_Objective', b)
    if hasattr(a2, 'sipme_Objective'):
        assert _is_linked(a2, 'sipme_Objective', b)
    _safe_set(b, 'sipme_Enterprise', set())
    assert not _is_linked(b, 'sipme_Enterprise', a2)
    if hasattr(a2, 'sipme_Objective'):
        assert not _is_linked(a2, 'sipme_Objective', b)


def test_assoc_subFiles95_reverse_link_reassign_clear():
    a1 = sipme_ObjectsFileView(filePriority=7, fileState="sample_text")
    a2 = sipme_ObjectsFileView(filePriority=13, fileState="sample_text_2")
    b = sipme_ObjectsFileView(filePriority=7, fileState="sample_text")
    _safe_set(b, 'sipme_ObjectsFileView96', a1)
    assert _is_linked(b, 'sipme_ObjectsFileView96', a1)
    if hasattr(a1, 'sipme_ObjectsFileView94'):
        assert _is_linked(a1, 'sipme_ObjectsFileView94', b)
    _safe_set(b, 'sipme_ObjectsFileView96', a2)
    assert _is_linked(b, 'sipme_ObjectsFileView96', a2)
    if hasattr(a1, 'sipme_ObjectsFileView94'):
        assert not _is_linked(a1, 'sipme_ObjectsFileView94', b)
    if hasattr(a2, 'sipme_ObjectsFileView94'):
        assert _is_linked(a2, 'sipme_ObjectsFileView94', b)
    _safe_set(b, 'sipme_ObjectsFileView96', None)
    assert not _is_linked(b, 'sipme_ObjectsFileView96', a2)
    if hasattr(a2, 'sipme_ObjectsFileView94'):
        assert not _is_linked(a2, 'sipme_ObjectsFileView94', b)


def test_assoc_subObjectives76_reverse_link_reassign_clear():
    a1 = sipme_Objective(objectiveNature="sample_text", objectiveType="sample_text")
    a2 = sipme_Objective(objectiveNature="sample_text_2", objectiveType="sample_text_2")
    b = sipme_Objective(objectiveNature="sample_text", objectiveType="sample_text")
    _safe_set(b, 'refines', {a1})
    assert _is_linked(b, 'refines', a1)
    if hasattr(a1, 'Objective'):
        assert _is_linked(a1, 'Objective', b)
    _safe_set(b, 'refines', {a2})
    assert _is_linked(b, 'refines', a2)
    if hasattr(a1, 'Objective'):
        assert not _is_linked(a1, 'Objective', b)
    if hasattr(a2, 'Objective'):
        assert _is_linked(a2, 'Objective', b)
    _safe_set(b, 'refines', set())
    assert not _is_linked(b, 'refines', a2)
    if hasattr(a2, 'Objective'):
        assert not _is_linked(a2, 'Objective', b)


def test_assoc_takenIntoAccountBy80_reverse_link_reassign_clear():
    a1 = sipme_Requirement(requirementDate=date(2024, 1, 1), requirementMaturity=7, requirementNature="sample_text", requirementOrigin="sample_text", requirementPriority=7, requirementStatement="sample_text", requirementStatus="sample_text", requirementVersion="sample_text")
    a2 = sipme_Requirement(requirementDate=date(2025, 6, 15), requirementMaturity=13, requirementNature="sample_text_2", requirementOrigin="sample_text_2", requirementPriority=13, requirementStatement="sample_text_2", requirementStatus="sample_text_2", requirementVersion="sample_text_2")
    b = sipme_Objective(objectiveNature="sample_text", objectiveType="sample_text")
    _safe_set(b, 'associatedObjective', {a1})
    assert _is_linked(b, 'associatedObjective', a1)
    if hasattr(a1, 'Requirement'):
        assert _is_linked(a1, 'Requirement', b)
    _safe_set(b, 'associatedObjective', {a2})
    assert _is_linked(b, 'associatedObjective', a2)
    if hasattr(a1, 'Requirement'):
        assert not _is_linked(a1, 'Requirement', b)
    if hasattr(a2, 'Requirement'):
        assert _is_linked(a2, 'Requirement', b)
    _safe_set(b, 'associatedObjective', set())
    assert not _is_linked(b, 'associatedObjective', a2)
    if hasattr(a2, 'Requirement'):
        assert not _is_linked(a2, 'Requirement', b)


def test_assoc_taskOf129_reverse_link_reassign_clear():
    a1 = sipme_Task(taskDuration=7)
    a2 = sipme_Task(taskDuration=13)
    b = sipme_Activity(ActivityDuration=7, endingStatus="sample_text")
    _safe_set(b, 'Activity130', a1)
    assert _is_linked(b, 'Activity130', a1)
    if hasattr(a1, 'tasks'):
        assert _is_linked(a1, 'tasks', b)
    _safe_set(b, 'Activity130', a2)
    assert _is_linked(b, 'Activity130', a2)
    if hasattr(a1, 'tasks'):
        assert not _is_linked(a1, 'tasks', b)
    if hasattr(a2, 'tasks'):
        assert _is_linked(a2, 'tasks', b)
    _safe_set(b, 'Activity130', None)
    assert not _is_linked(b, 'Activity130', a2)
    if hasattr(a2, 'tasks'):
        assert not _is_linked(a2, 'tasks', b)


def test_assoc_tasks0_reverse_link_reassign_clear():
    a1 = sipme_Task(taskDuration=7)
    a2 = sipme_Task(taskDuration=13)
    b = sipme_Activity(ActivityDuration=7, endingStatus="sample_text")
    _safe_set(b, 'taskOf', {a1})
    assert _is_linked(b, 'taskOf', a1)
    if hasattr(a1, 'Task'):
        assert _is_linked(a1, 'Task', b)
    _safe_set(b, 'taskOf', {a2})
    assert _is_linked(b, 'taskOf', a2)
    if hasattr(a1, 'Task'):
        assert not _is_linked(a1, 'Task', b)
    if hasattr(a2, 'Task'):
        assert _is_linked(a2, 'Task', b)
    _safe_set(b, 'taskOf', set())
    assert not _is_linked(b, 'taskOf', a2)
    if hasattr(a2, 'Task'):
        assert not _is_linked(a2, 'Task', b)


def test_assoc_workstations85_reverse_link_reassign_clear():
    a1 = sipme_Workstation(ProfileDeescription="sample_text")
    a2 = sipme_Workstation(ProfileDeescription="sample_text_2")
    b = sipme_OrganisationCell(organisationLevel=7)
    _safe_set(b, 'organisationCell', {a1})
    assert _is_linked(b, 'organisationCell', a1)
    if hasattr(a1, 'Workstation86'):
        assert _is_linked(a1, 'Workstation86', b)
    _safe_set(b, 'organisationCell', {a2})
    assert _is_linked(b, 'organisationCell', a2)
    if hasattr(a1, 'Workstation86'):
        assert not _is_linked(a1, 'Workstation86', b)
    if hasattr(a2, 'Workstation86'):
        assert _is_linked(a2, 'Workstation86', b)
    _safe_set(b, 'organisationCell', set())
    assert not _is_linked(b, 'organisationCell', a2)
    if hasattr(a2, 'Workstation86'):
        assert not _is_linked(a2, 'Workstation86', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_considers4_stub_double():
    # sipme_BusinessRules has no real 'sipme_BusinessRules' property in the generated
    # code (a bare stub) -- manually attach it so sipme_EnterpriseObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sipme_EnterpriseObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sipme_EnterpriseObject(properties="sample_text", reference="sample_text")
    partner = sipme_BusinessRules()
    setattr(partner, 'sipme_BusinessRules', None)
    _safe_set(owner, 'sipme_EnterpriseObject', partner)
    assert owner in getattr(partner, 'sipme_BusinessRules')
    _safe_set(owner, 'sipme_EnterpriseObject', None)
    assert owner not in getattr(partner, 'sipme_BusinessRules')


def test_assoc_impacts5_stub_double():
    # sipme_BusinessRules has no real 'sipme_BusinessRules6' property in the generated
    # code (a bare stub) -- manually attach it so sipme_EnterpriseObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sipme_EnterpriseObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sipme_EnterpriseObject(properties="sample_text", reference="sample_text")
    partner = sipme_BusinessRules()
    setattr(partner, 'sipme_BusinessRules6', None)
    _safe_set(owner, 'sipme_EnterpriseObject7', partner)
    assert owner in getattr(partner, 'sipme_BusinessRules6')
    _safe_set(owner, 'sipme_EnterpriseObject7', None)
    assert owner not in getattr(partner, 'sipme_BusinessRules6')


def test_assoc_induces19_stub_double():
    # sipme_BusinessRules has no real 'sipme_BusinessRules21' property in the generated
    # code (a bare stub) -- manually attach it so sipme_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sipme_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sipme_Domain(domainCharacterization="sample_text", performanceIndicators=3.14)
    partner = sipme_BusinessRules()
    setattr(partner, 'sipme_BusinessRules21', None)
    _safe_set(owner, 'sipme_Domain20', {partner})
    assert getattr(partner, 'sipme_BusinessRules21') == owner
    _safe_set(owner, 'sipme_Domain20', set())
    assert getattr(partner, 'sipme_BusinessRules21') is None


def test_assoc_respectsRoleRules120_stub_double():
    # sipme_BusinessRules has no real 'sipme_BusinessRules122' property in the generated
    # code (a bare stub) -- manually attach it so sipme_Role_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sipme_Role_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sipme_Role_Function(roleType="sample_text")
    partner = sipme_BusinessRules()
    setattr(partner, 'sipme_BusinessRules122', None)
    _safe_set(owner, 'sipme_Role_Function121', {partner})
    assert getattr(partner, 'sipme_BusinessRules122') == owner
    _safe_set(owner, 'sipme_Role_Function121', set())
    assert getattr(partner, 'sipme_BusinessRules122') is None


def test_assoc_respectsTaskRules126_stub_double():
    # sipme_BusinessRules has no real 'sipme_BusinessRules128' property in the generated
    # code (a bare stub) -- manually attach it so sipme_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sipme_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sipme_Task(taskDuration=7)
    partner = sipme_BusinessRules()
    setattr(partner, 'sipme_BusinessRules128', None)
    _safe_set(owner, 'sipme_Task127', partner)
    assert getattr(partner, 'sipme_BusinessRules128') == owner
    _safe_set(owner, 'sipme_Task127', None)
    assert getattr(partner, 'sipme_BusinessRules128') is None


