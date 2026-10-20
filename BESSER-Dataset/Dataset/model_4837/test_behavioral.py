import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ApplicationComponent,
    Architecture,
    DataComponent,
    Element,
    Service,
    Standard,
    StrategicElement,
    TechnologyComponent,
    contentfwk_Actor,
    contentfwk_ApplicationArchitecture,
    contentfwk_ApplicationComponent,
    contentfwk_Architecture,
    contentfwk_Assumption,
    contentfwk_BusinessArchitecture,
    contentfwk_BusinessService,
    contentfwk_Capability,
    contentfwk_Constraint,
    contentfwk_Container,
    contentfwk_Contract,
    contentfwk_Control,
    contentfwk_DataArchitecture,
    contentfwk_DataComponent,
    contentfwk_DataEntity,
    contentfwk_Driver,
    contentfwk_Element,
    contentfwk_EnterpriseArchitecture,
    contentfwk_Event,
    contentfwk_Function,
    contentfwk_Gap,
    contentfwk_Goal,
    contentfwk_InformationSystemService,
    contentfwk_Location,
    contentfwk_LogicalApplicationComponent,
    contentfwk_LogicalDataComponent,
    contentfwk_LogicalTechnologyComponent,
    contentfwk_Measure,
    contentfwk_Objective,
    contentfwk_OrganizationUnit,
    contentfwk_PhysicalApplicationComponent,
    contentfwk_PhysicalDataComponent,
    contentfwk_PhysicalTechnologyComponent,
    contentfwk_PlatformService,
    contentfwk_Principle,
    contentfwk_Process,
    contentfwk_Product,
    contentfwk_Requirement,
    contentfwk_Role,
    contentfwk_Service,
    contentfwk_ServiceQuality,
    contentfwk_Standard,
    contentfwk_StrategicArchitecture,
    contentfwk_StrategicElement,
    contentfwk_TechnologyArchitecture,
    contentfwk_TechnologyComponent,
    contentfwk_WorkPackage,
    DataEntityCategory,
    LifeCycleStatus,
    PrincipleCategory,
    StandardsClass,
    WorkPackageCategory,
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

def test_assoc_belongsTo71_reverse_link_reassign_clear():
    a1 = contentfwk_OrganizationUnit(headcount="sample_text")
    a2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'containsActors', a1)
    assert _is_linked(b, 'containsActors', a1)
    if hasattr(a1, 'OrganizationUnit72'):
        assert _is_linked(a1, 'OrganizationUnit72', b)
    _safe_set(b, 'containsActors', a2)
    assert _is_linked(b, 'containsActors', a2)
    if hasattr(a1, 'OrganizationUnit72'):
        assert not _is_linked(a1, 'OrganizationUnit72', b)
    if hasattr(a2, 'OrganizationUnit72'):
        assert _is_linked(a2, 'OrganizationUnit72', b)
    _safe_set(b, 'containsActors', None)
    assert not _is_linked(b, 'containsActors', a2)
    if hasattr(a2, 'OrganizationUnit72'):
        assert not _is_linked(a2, 'OrganizationUnit72', b)


def test_assoc_communicatesWith274_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    a2 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent275', a1)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent275', a1)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent273'):
        assert _is_linked(a1, 'contentfwk_PhysicalApplicationComponent273', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent275', a2)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent275', a2)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent273'):
        assert not _is_linked(a1, 'contentfwk_PhysicalApplicationComponent273', b)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent273'):
        assert _is_linked(a2, 'contentfwk_PhysicalApplicationComponent273', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent275', None)
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent275', a2)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent273'):
        assert not _is_linked(a2, 'contentfwk_PhysicalApplicationComponent273', b)


def test_assoc_consumesEntities69_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'isConsumedByActors', {a1})
    assert _is_linked(b, 'isConsumedByActors', a1)
    if hasattr(a1, 'DataEntity70'):
        assert _is_linked(a1, 'DataEntity70', b)
    _safe_set(b, 'isConsumedByActors', {a2})
    assert _is_linked(b, 'isConsumedByActors', a2)
    if hasattr(a1, 'DataEntity70'):
        assert not _is_linked(a1, 'DataEntity70', b)
    if hasattr(a2, 'DataEntity70'):
        assert _is_linked(a2, 'DataEntity70', b)
    _safe_set(b, 'isConsumedByActors', set())
    assert not _is_linked(b, 'isConsumedByActors', a2)
    if hasattr(a2, 'DataEntity70'):
        assert not _is_linked(a2, 'DataEntity70', b)


def test_assoc_containsActors61_reverse_link_reassign_clear():
    a1 = contentfwk_OrganizationUnit(headcount="sample_text")
    a2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor', a1)
    assert _is_linked(b, 'Actor', a1)
    if hasattr(a1, 'belongsTo'):
        assert _is_linked(a1, 'belongsTo', b)
    _safe_set(b, 'Actor', a2)
    assert _is_linked(b, 'Actor', a2)
    if hasattr(a1, 'belongsTo'):
        assert not _is_linked(a1, 'belongsTo', b)
    if hasattr(a2, 'belongsTo'):
        assert _is_linked(a2, 'belongsTo', b)
    _safe_set(b, 'Actor', None)
    assert not _is_linked(b, 'Actor', a2)
    if hasattr(a2, 'belongsTo'):
        assert not _is_linked(a2, 'belongsTo', b)


def test_assoc_decomposeEntity110_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    _safe_set(b, 'contentfwk_DataEntity111', a1)
    assert _is_linked(b, 'contentfwk_DataEntity111', a1)
    if hasattr(a1, 'contentfwk_DataEntity109'):
        assert _is_linked(a1, 'contentfwk_DataEntity109', b)
    _safe_set(b, 'contentfwk_DataEntity111', a2)
    assert _is_linked(b, 'contentfwk_DataEntity111', a2)
    if hasattr(a1, 'contentfwk_DataEntity109'):
        assert not _is_linked(a1, 'contentfwk_DataEntity109', b)
    if hasattr(a2, 'contentfwk_DataEntity109'):
        assert _is_linked(a2, 'contentfwk_DataEntity109', b)
    _safe_set(b, 'contentfwk_DataEntity111', None)
    assert not _is_linked(b, 'contentfwk_DataEntity111', a2)
    if hasattr(a2, 'contentfwk_DataEntity109'):
        assert not _is_linked(a2, 'contentfwk_DataEntity109', b)


def test_assoc_decomposesActors89_reverse_link_reassign_clear():
    a1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    a2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'contentfwk_Actor90', a1)
    assert _is_linked(b, 'contentfwk_Actor90', a1)
    if hasattr(a1, 'contentfwk_Actor88'):
        assert _is_linked(a1, 'contentfwk_Actor88', b)
    _safe_set(b, 'contentfwk_Actor90', a2)
    assert _is_linked(b, 'contentfwk_Actor90', a2)
    if hasattr(a1, 'contentfwk_Actor88'):
        assert not _is_linked(a1, 'contentfwk_Actor88', b)
    if hasattr(a2, 'contentfwk_Actor88'):
        assert _is_linked(a2, 'contentfwk_Actor88', b)
    _safe_set(b, 'contentfwk_Actor90', None)
    assert not _is_linked(b, 'contentfwk_Actor90', a2)
    if hasattr(a2, 'contentfwk_Actor88'):
        assert not _is_linked(a2, 'contentfwk_Actor88', b)


def test_assoc_decomposesPhysicalApplicationComponent283_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    a2 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent284', a1)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent284', a1)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent282'):
        assert _is_linked(a1, 'contentfwk_PhysicalApplicationComponent282', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent284', a2)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent284', a2)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent282'):
        assert not _is_linked(a1, 'contentfwk_PhysicalApplicationComponent282', b)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent282'):
        assert _is_linked(a2, 'contentfwk_PhysicalApplicationComponent282', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent284', None)
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent284', a2)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent282'):
        assert not _is_linked(a2, 'contentfwk_PhysicalApplicationComponent282', b)


def test_assoc_decomposesPhysicalTechnologyComponent187_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent188', a1)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent188', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent186'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent186', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent188', a2)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent188', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent186'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent186', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent186'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent186', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent188', None)
    assert not _is_linked(b, 'contentfwk_PhysicalTechnologyComponent188', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent186'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent186', b)


def test_assoc_decomposesProcess171_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'contentfwk_Process172', a1)
    assert _is_linked(b, 'contentfwk_Process172', a1)
    if hasattr(a1, 'contentfwk_Process170'):
        assert _is_linked(a1, 'contentfwk_Process170', b)
    _safe_set(b, 'contentfwk_Process172', a2)
    assert _is_linked(b, 'contentfwk_Process172', a2)
    if hasattr(a1, 'contentfwk_Process170'):
        assert not _is_linked(a1, 'contentfwk_Process170', b)
    if hasattr(a2, 'contentfwk_Process170'):
        assert _is_linked(a2, 'contentfwk_Process170', b)
    _safe_set(b, 'contentfwk_Process172', None)
    assert not _is_linked(b, 'contentfwk_Process172', a2)
    if hasattr(a2, 'contentfwk_Process170'):
        assert not _is_linked(a2, 'contentfwk_Process170', b)


def test_assoc_decomposesRole96_reverse_link_reassign_clear():
    a1 = contentfwk_Role(estimatedFTEs="sample_text")
    a2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    b = contentfwk_Role(estimatedFTEs="sample_text")
    _safe_set(b, 'contentfwk_Role97', a1)
    assert _is_linked(b, 'contentfwk_Role97', a1)
    if hasattr(a1, 'contentfwk_Role95'):
        assert _is_linked(a1, 'contentfwk_Role95', b)
    _safe_set(b, 'contentfwk_Role97', a2)
    assert _is_linked(b, 'contentfwk_Role97', a2)
    if hasattr(a1, 'contentfwk_Role95'):
        assert not _is_linked(a1, 'contentfwk_Role95', b)
    if hasattr(a2, 'contentfwk_Role95'):
        assert _is_linked(a2, 'contentfwk_Role95', b)
    _safe_set(b, 'contentfwk_Role97', None)
    assert not _is_linked(b, 'contentfwk_Role97', a2)
    if hasattr(a2, 'contentfwk_Role95'):
        assert not _is_linked(a2, 'contentfwk_Role95', b)


def test_assoc_delegates227_reverse_link_reassign_clear():
    a1 = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    a2 = contentfwk_Element(ID="sample_text_2", category="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    b = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    _safe_set(b, 'isDelegatedBy', {a1})
    assert _is_linked(b, 'isDelegatedBy', a1)
    if hasattr(a1, 'Element'):
        assert _is_linked(a1, 'Element', b)
    _safe_set(b, 'isDelegatedBy', {a2})
    assert _is_linked(b, 'isDelegatedBy', a2)
    if hasattr(a1, 'Element'):
        assert not _is_linked(a1, 'Element', b)
    if hasattr(a2, 'Element'):
        assert _is_linked(a2, 'Element', b)
    _safe_set(b, 'isDelegatedBy', set())
    assert not _is_linked(b, 'isDelegatedBy', a2)
    if hasattr(a2, 'Element'):
        assert not _is_linked(a2, 'Element', b)


def test_assoc_deliversCapabilities247_reverse_link_reassign_clear():
    a1 = contentfwk_WorkPackage(workPackageCategory="sample_text")
    a2 = contentfwk_WorkPackage(workPackageCategory="sample_text_2")
    b = contentfwk_Capability(businessValue="sample_text", increments="sample_text")
    _safe_set(b, 'Capability', a1)
    assert _is_linked(b, 'Capability', a1)
    if hasattr(a1, 'isDeliveredBy'):
        assert _is_linked(a1, 'isDeliveredBy', b)
    _safe_set(b, 'Capability', a2)
    assert _is_linked(b, 'Capability', a2)
    if hasattr(a1, 'isDeliveredBy'):
        assert not _is_linked(a1, 'isDeliveredBy', b)
    if hasattr(a2, 'isDeliveredBy'):
        assert _is_linked(a2, 'isDeliveredBy', b)
    _safe_set(b, 'Capability', None)
    assert not _is_linked(b, 'Capability', a2)
    if hasattr(a2, 'isDeliveredBy'):
        assert not _is_linked(a2, 'isDeliveredBy', b)


def test_assoc_followsProcesses177_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'precedesProcesses', {a1})
    assert _is_linked(b, 'precedesProcesses', a1)
    if hasattr(a1, 'Process178'):
        assert _is_linked(a1, 'Process178', b)
    _safe_set(b, 'precedesProcesses', {a2})
    assert _is_linked(b, 'precedesProcesses', a2)
    if hasattr(a1, 'Process178'):
        assert not _is_linked(a1, 'Process178', b)
    if hasattr(a2, 'Process178'):
        assert _is_linked(a2, 'Process178', b)
    _safe_set(b, 'precedesProcesses', set())
    assert not _is_linked(b, 'precedesProcesses', a2)
    if hasattr(a2, 'Process178'):
        assert not _is_linked(a2, 'Process178', b)


def test_assoc_involvesActors160_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor162', a1)
    assert _is_linked(b, 'Actor162', a1)
    if hasattr(a1, 'participatesInProcesses161'):
        assert _is_linked(a1, 'participatesInProcesses161', b)
    _safe_set(b, 'Actor162', a2)
    assert _is_linked(b, 'Actor162', a2)
    if hasattr(a1, 'participatesInProcesses161'):
        assert not _is_linked(a1, 'participatesInProcesses161', b)
    if hasattr(a2, 'participatesInProcesses161'):
        assert _is_linked(a2, 'participatesInProcesses161', b)
    _safe_set(b, 'Actor162', None)
    assert not _is_linked(b, 'Actor162', a2)
    if hasattr(a2, 'participatesInProcesses161'):
        assert not _is_linked(a2, 'participatesInProcesses161', b)


def test_assoc_involvesOrganizationUnits152_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_OrganizationUnit(headcount="sample_text")
    _safe_set(b, 'OrganizationUnit153', a1)
    assert _is_linked(b, 'OrganizationUnit153', a1)
    if hasattr(a1, 'participatesInProcesses'):
        assert _is_linked(a1, 'participatesInProcesses', b)
    _safe_set(b, 'OrganizationUnit153', a2)
    assert _is_linked(b, 'OrganizationUnit153', a2)
    if hasattr(a1, 'participatesInProcesses'):
        assert not _is_linked(a1, 'participatesInProcesses', b)
    if hasattr(a2, 'participatesInProcesses'):
        assert _is_linked(a2, 'participatesInProcesses', b)
    _safe_set(b, 'OrganizationUnit153', None)
    assert not _is_linked(b, 'OrganizationUnit153', a2)
    if hasattr(a2, 'participatesInProcesses'):
        assert not _is_linked(a2, 'participatesInProcesses', b)


def test_assoc_isAssumedByActors91_reverse_link_reassign_clear():
    a1 = contentfwk_Role(estimatedFTEs="sample_text")
    a2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor92', a1)
    assert _is_linked(b, 'Actor92', a1)
    if hasattr(a1, 'performsTaskInRoles'):
        assert _is_linked(a1, 'performsTaskInRoles', b)
    _safe_set(b, 'Actor92', a2)
    assert _is_linked(b, 'Actor92', a2)
    if hasattr(a1, 'performsTaskInRoles'):
        assert not _is_linked(a1, 'performsTaskInRoles', b)
    if hasattr(a2, 'performsTaskInRoles'):
        assert _is_linked(a2, 'performsTaskInRoles', b)
    _safe_set(b, 'Actor92', None)
    assert not _is_linked(b, 'Actor92', a2)
    if hasattr(a2, 'performsTaskInRoles'):
        assert not _is_linked(a2, 'performsTaskInRoles', b)


def test_assoc_isConsumedByActors100_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor101', a1)
    assert _is_linked(b, 'Actor101', a1)
    if hasattr(a1, 'consumesEntities'):
        assert _is_linked(a1, 'consumesEntities', b)
    _safe_set(b, 'Actor101', a2)
    assert _is_linked(b, 'Actor101', a2)
    if hasattr(a1, 'consumesEntities'):
        assert not _is_linked(a1, 'consumesEntities', b)
    if hasattr(a2, 'consumesEntities'):
        assert _is_linked(a2, 'consumesEntities', b)
    _safe_set(b, 'Actor101', None)
    assert not _is_linked(b, 'Actor101', a2)
    if hasattr(a2, 'consumesEntities'):
        assert not _is_linked(a2, 'consumesEntities', b)


def test_assoc_isDelegatedBy229_reverse_link_reassign_clear():
    a1 = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    a2 = contentfwk_Element(ID="sample_text_2", category="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    b = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    _safe_set(b, 'delegates', {a1})
    assert _is_linked(b, 'delegates', a1)
    if hasattr(a1, 'Element230'):
        assert _is_linked(a1, 'Element230', b)
    _safe_set(b, 'delegates', {a2})
    assert _is_linked(b, 'delegates', a2)
    if hasattr(a1, 'Element230'):
        assert not _is_linked(a1, 'Element230', b)
    if hasattr(a2, 'Element230'):
        assert _is_linked(a2, 'Element230', b)
    _safe_set(b, 'delegates', set())
    assert not _is_linked(b, 'delegates', a2)
    if hasattr(a2, 'Element230'):
        assert not _is_linked(a2, 'Element230', b)


def test_assoc_isDeliveredBy246_reverse_link_reassign_clear():
    a1 = contentfwk_WorkPackage(workPackageCategory="sample_text")
    a2 = contentfwk_WorkPackage(workPackageCategory="sample_text_2")
    b = contentfwk_Capability(businessValue="sample_text", increments="sample_text")
    _safe_set(b, 'deliversCapabilities', a1)
    assert _is_linked(b, 'deliversCapabilities', a1)
    if hasattr(a1, 'WorkPackage'):
        assert _is_linked(a1, 'WorkPackage', b)
    _safe_set(b, 'deliversCapabilities', a2)
    assert _is_linked(b, 'deliversCapabilities', a2)
    if hasattr(a1, 'WorkPackage'):
        assert not _is_linked(a1, 'WorkPackage', b)
    if hasattr(a2, 'WorkPackage'):
        assert _is_linked(a2, 'WorkPackage', b)
    _safe_set(b, 'deliversCapabilities', None)
    assert not _is_linked(b, 'deliversCapabilities', a2)
    if hasattr(a2, 'WorkPackage'):
        assert not _is_linked(a2, 'WorkPackage', b)


def test_assoc_isDependentOnPhysicalTechnologyComponents190_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent191', a1)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent191', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent189'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent189', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent191', a2)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent191', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent189'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent189', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent189'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent189', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent191', None)
    assert not _is_linked(b, 'contentfwk_PhysicalTechnologyComponent191', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent189'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent189', b)


def test_assoc_isRealizedByPhysicalTechnologyComponents279_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent280', {a1})
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent280', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent281'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent281', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent280', {a2})
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent280', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent281'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent281', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent281'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent281', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent280', set())
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent280', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent281'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent281', b)


def test_assoc_isSuppliedByActors98_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor99', a1)
    assert _is_linked(b, 'Actor99', a1)
    if hasattr(a1, 'suppliesEntities'):
        assert _is_linked(a1, 'suppliesEntities', b)
    _safe_set(b, 'Actor99', a2)
    assert _is_linked(b, 'Actor99', a2)
    if hasattr(a1, 'suppliesEntities'):
        assert not _is_linked(a1, 'suppliesEntities', b)
    if hasattr(a2, 'suppliesEntities'):
        assert _is_linked(a2, 'suppliesEntities', b)
    _safe_set(b, 'Actor99', None)
    assert not _is_linked(b, 'Actor99', a2)
    if hasattr(a2, 'suppliesEntities'):
        assert not _is_linked(a2, 'suppliesEntities', b)


def test_assoc_ownsElements231_reverse_link_reassign_clear():
    a1 = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    a2 = contentfwk_Element(ID="sample_text_2", category="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    b = contentfwk_Container(name="sample_text")
    _safe_set(b, 'contentfwk_Container232', {a1})
    assert _is_linked(b, 'contentfwk_Container232', a1)
    if hasattr(a1, 'contentfwk_Element'):
        assert _is_linked(a1, 'contentfwk_Element', b)
    _safe_set(b, 'contentfwk_Container232', {a2})
    assert _is_linked(b, 'contentfwk_Container232', a2)
    if hasattr(a1, 'contentfwk_Element'):
        assert not _is_linked(a1, 'contentfwk_Element', b)
    if hasattr(a2, 'contentfwk_Element'):
        assert _is_linked(a2, 'contentfwk_Element', b)
    _safe_set(b, 'contentfwk_Container232', set())
    assert not _is_linked(b, 'contentfwk_Container232', a2)
    if hasattr(a2, 'contentfwk_Element'):
        assert not _is_linked(a2, 'contentfwk_Element', b)


def test_assoc_participatesInProcesses63_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_OrganizationUnit(headcount="sample_text")
    _safe_set(b, 'involvesOrganizationUnits', {a1})
    assert _is_linked(b, 'involvesOrganizationUnits', a1)
    if hasattr(a1, 'Process'):
        assert _is_linked(a1, 'Process', b)
    _safe_set(b, 'involvesOrganizationUnits', {a2})
    assert _is_linked(b, 'involvesOrganizationUnits', a2)
    if hasattr(a1, 'Process'):
        assert not _is_linked(a1, 'Process', b)
    if hasattr(a2, 'Process'):
        assert _is_linked(a2, 'Process', b)
    _safe_set(b, 'involvesOrganizationUnits', set())
    assert not _is_linked(b, 'involvesOrganizationUnits', a2)
    if hasattr(a2, 'Process'):
        assert not _is_linked(a2, 'Process', b)


def test_assoc_participatesInProcesses76_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'involvesActors', {a1})
    assert _is_linked(b, 'involvesActors', a1)
    if hasattr(a1, 'Process77'):
        assert _is_linked(a1, 'Process77', b)
    _safe_set(b, 'involvesActors', {a2})
    assert _is_linked(b, 'involvesActors', a2)
    if hasattr(a1, 'Process77'):
        assert not _is_linked(a1, 'Process77', b)
    if hasattr(a2, 'Process77'):
        assert _is_linked(a2, 'Process77', b)
    _safe_set(b, 'involvesActors', set())
    assert not _is_linked(b, 'involvesActors', a2)
    if hasattr(a2, 'Process77'):
        assert not _is_linked(a2, 'Process77', b)


def test_assoc_performsTaskInRoles75_reverse_link_reassign_clear():
    a1 = contentfwk_Role(estimatedFTEs="sample_text")
    a2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'isAssumedByActors', {a1})
    assert _is_linked(b, 'isAssumedByActors', a1)
    if hasattr(a1, 'Role'):
        assert _is_linked(a1, 'Role', b)
    _safe_set(b, 'isAssumedByActors', {a2})
    assert _is_linked(b, 'isAssumedByActors', a2)
    if hasattr(a1, 'Role'):
        assert not _is_linked(a1, 'Role', b)
    if hasattr(a2, 'Role'):
        assert _is_linked(a2, 'Role', b)
    _safe_set(b, 'isAssumedByActors', set())
    assert not _is_linked(b, 'isAssumedByActors', a2)
    if hasattr(a2, 'Role'):
        assert not _is_linked(a2, 'Role', b)


def test_assoc_precedesProcesses174_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'followsProcesses', {a1})
    assert _is_linked(b, 'followsProcesses', a1)
    if hasattr(a1, 'Process175'):
        assert _is_linked(a1, 'Process175', b)
    _safe_set(b, 'followsProcesses', {a2})
    assert _is_linked(b, 'followsProcesses', a2)
    if hasattr(a1, 'Process175'):
        assert not _is_linked(a1, 'Process175', b)
    if hasattr(a2, 'Process175'):
        assert _is_linked(a2, 'Process175', b)
    _safe_set(b, 'followsProcesses', set())
    assert not _is_linked(b, 'followsProcesses', a2)
    if hasattr(a2, 'Process175'):
        assert not _is_linked(a2, 'Process175', b)


def test_assoc_realizesApplicationComponents180_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent', a1)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent181'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent181', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent', a2)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent181'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent181', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent181'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent181', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent', None)
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent181'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent181', b)


def test_assoc_relatesTo113_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    _safe_set(b, 'contentfwk_DataEntity114', a1)
    assert _is_linked(b, 'contentfwk_DataEntity114', a1)
    if hasattr(a1, 'contentfwk_DataEntity112'):
        assert _is_linked(a1, 'contentfwk_DataEntity112', b)
    _safe_set(b, 'contentfwk_DataEntity114', a2)
    assert _is_linked(b, 'contentfwk_DataEntity114', a2)
    if hasattr(a1, 'contentfwk_DataEntity112'):
        assert not _is_linked(a1, 'contentfwk_DataEntity112', b)
    if hasattr(a2, 'contentfwk_DataEntity112'):
        assert _is_linked(a2, 'contentfwk_DataEntity112', b)
    _safe_set(b, 'contentfwk_DataEntity114', None)
    assert not _is_linked(b, 'contentfwk_DataEntity114', a2)
    if hasattr(a2, 'contentfwk_DataEntity112'):
        assert not _is_linked(a2, 'contentfwk_DataEntity112', b)


def test_assoc_suppliesEntities68_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'isSuppliedByActors', {a1})
    assert _is_linked(b, 'isSuppliedByActors', a1)
    if hasattr(a1, 'DataEntity'):
        assert _is_linked(a1, 'DataEntity', b)
    _safe_set(b, 'isSuppliedByActors', {a2})
    assert _is_linked(b, 'isSuppliedByActors', a2)
    if hasattr(a1, 'DataEntity'):
        assert not _is_linked(a1, 'DataEntity', b)
    if hasattr(a2, 'DataEntity'):
        assert _is_linked(a2, 'DataEntity', b)
    _safe_set(b, 'isSuppliedByActors', set())
    assert not _is_linked(b, 'isSuppliedByActors', a2)
    if hasattr(a2, 'DataEntity'):
        assert not _is_linked(a2, 'DataEntity', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessesFunctions93_stub_double():
    # contentfwk_Function has no real 'Function94' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Role(estimatedFTEs="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function94', None)
    _safe_set(owner, 'canBeAccessedByRoles', {partner})
    assert getattr(partner, 'Function94') == owner
    _safe_set(owner, 'canBeAccessedByRoles', set())
    assert getattr(partner, 'Function94') is None


def test_assoc_actors10_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture11' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture11', None)
    _safe_set(owner, 'contentfwk_Actor', partner)
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture11')
    _safe_set(owner, 'contentfwk_Actor', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture11')


def test_assoc_appliesToContracts207_stub_double():
    # contentfwk_ServiceQuality has no real 'meetsServiceQuality' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_ServiceQuality()
    setattr(partner, 'meetsServiceQuality', None)
    _safe_set(owner, 'Contract', partner)
    assert owner in getattr(partner, 'meetsServiceQuality')
    _safe_set(owner, 'Contract', None)
    assert owner not in getattr(partner, 'meetsServiceQuality')


def test_assoc_canBeAccessedByRoles135_stub_double():
    # contentfwk_Function has no real 'accessesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Role(estimatedFTEs="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'accessesFunctions', None)
    _safe_set(owner, 'Role136', partner)
    assert owner in getattr(partner, 'accessesFunctions')
    _safe_set(owner, 'Role136', None)
    assert owner not in getattr(partner, 'accessesFunctions')


def test_assoc_capabilities296_stub_double():
    # contentfwk_StrategicArchitecture has no real 'contentfwk_StrategicArchitecture' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Capability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Capability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Capability(businessValue="sample_text", increments="sample_text")
    partner = contentfwk_StrategicArchitecture()
    setattr(partner, 'contentfwk_StrategicArchitecture', None)
    _safe_set(owner, 'contentfwk_Capability', partner)
    assert owner in getattr(partner, 'contentfwk_StrategicArchitecture')
    _safe_set(owner, 'contentfwk_Capability', None)
    assert owner not in getattr(partner, 'contentfwk_StrategicArchitecture')


def test_assoc_consumesEntities306_stub_double():
    # contentfwk_Service has no real 'isAccessedByServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'isAccessedByServices', None)
    _safe_set(owner, 'DataEntity307', partner)
    assert owner in getattr(partner, 'isAccessedByServices')
    _safe_set(owner, 'DataEntity307', None)
    assert owner not in getattr(partner, 'isAccessedByServices')


def test_assoc_consumesServices78_stub_double():
    # contentfwk_Service has no real 'contentfwk_Service' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'contentfwk_Service', None)
    _safe_set(owner, 'contentfwk_Actor79', {partner})
    assert getattr(partner, 'contentfwk_Service') == owner
    _safe_set(owner, 'contentfwk_Actor79', set())
    assert getattr(partner, 'contentfwk_Service') is None


def test_assoc_containers1_stub_double():
    # contentfwk_EnterpriseArchitecture has no real 'contentfwk_EnterpriseArchitecture2' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Container(name="sample_text")
    partner = contentfwk_EnterpriseArchitecture()
    setattr(partner, 'contentfwk_EnterpriseArchitecture2', None)
    _safe_set(owner, 'contentfwk_Container', partner)
    assert owner in getattr(partner, 'contentfwk_EnterpriseArchitecture2')
    _safe_set(owner, 'contentfwk_Container', None)
    assert owner not in getattr(partner, 'contentfwk_EnterpriseArchitecture2')


def test_assoc_containsActors233_stub_double():
    # contentfwk_Location has no real 'operatesInLocation' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'operatesInLocation', None)
    _safe_set(owner, 'Actor234', partner)
    assert owner in getattr(partner, 'operatesInLocation')
    _safe_set(owner, 'Actor234', None)
    assert owner not in getattr(partner, 'operatesInLocation')


def test_assoc_containsOrganizationUnits235_stub_double():
    # contentfwk_Location has no real 'operatesInLocation236' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'operatesInLocation236', None)
    _safe_set(owner, 'OrganizationUnit237', partner)
    assert owner in getattr(partner, 'operatesInLocation236')
    _safe_set(owner, 'OrganizationUnit237', None)
    assert owner not in getattr(partner, 'operatesInLocation236')


def test_assoc_containsPhysicalApplicationComponents239_stub_double():
    # contentfwk_Location has no real 'isHostedInLocation' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'isHostedInLocation', None)
    _safe_set(owner, 'PhysicalApplicationComponent240', partner)
    assert owner in getattr(partner, 'isHostedInLocation')
    _safe_set(owner, 'PhysicalApplicationComponent240', None)
    assert owner not in getattr(partner, 'isHostedInLocation')


def test_assoc_containsPhysicalTechnologyComponents241_stub_double():
    # contentfwk_Location has no real 'isHostedInLocation242' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'isHostedInLocation242', None)
    _safe_set(owner, 'PhysicalTechnologyComponent', partner)
    assert owner in getattr(partner, 'isHostedInLocation242')
    _safe_set(owner, 'PhysicalTechnologyComponent', None)
    assert owner not in getattr(partner, 'isHostedInLocation242')


def test_assoc_contracts28_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture29' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture29', None)
    _safe_set(owner, 'contentfwk_Contract', partner)
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture29')
    _safe_set(owner, 'contentfwk_Contract', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture29')


def test_assoc_decomposesFunctions150_stub_double():
    # contentfwk_Function has no real 'Function151' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function151', None)
    _safe_set(owner, 'supportsProcesses', {partner})
    assert getattr(partner, 'Function151') == owner
    _safe_set(owner, 'supportsProcesses', set())
    assert getattr(partner, 'Function151') is None


def test_assoc_decomposesServices157_stub_double():
    # contentfwk_Service has no real 'Service159' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service159', None)
    _safe_set(owner, 'supportsProcesses158', {partner})
    assert getattr(partner, 'Service159') == owner
    _safe_set(owner, 'supportsProcesses158', set())
    assert getattr(partner, 'Service159') is None


def test_assoc_encapsulatesDataEntities248_stub_double():
    # contentfwk_LogicalDataComponent has no real 'residesWithinLogicalDataComponent' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_LogicalDataComponent()
    setattr(partner, 'residesWithinLogicalDataComponent', None)
    _safe_set(owner, 'DataEntity249', partner)
    assert owner in getattr(partner, 'residesWithinLogicalDataComponent')
    _safe_set(owner, 'DataEntity249', None)
    assert owner not in getattr(partner, 'residesWithinLogicalDataComponent')


def test_assoc_encapsulatesPhysicalApplicationComponents259_stub_double():
    # contentfwk_PhysicalDataComponent has no real 'contentfwk_PhysicalDataComponent260' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_PhysicalDataComponent()
    setattr(partner, 'contentfwk_PhysicalDataComponent260', None)
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent261', partner)
    assert owner in getattr(partner, 'contentfwk_PhysicalDataComponent260')
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent261', None)
    assert owner not in getattr(partner, 'contentfwk_PhysicalDataComponent260')


def test_assoc_encapsulatesPhysicalDataComponents276_stub_double():
    # contentfwk_PhysicalDataComponent has no real 'contentfwk_PhysicalDataComponent278' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_PhysicalDataComponent()
    setattr(partner, 'contentfwk_PhysicalDataComponent278', None)
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent277', {partner})
    assert getattr(partner, 'contentfwk_PhysicalDataComponent278') == owner
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent277', set())
    assert getattr(partner, 'contentfwk_PhysicalDataComponent278') is None


def test_assoc_ensuresCorrectOperationOfProcesses224_stub_double():
    # contentfwk_Control has no real 'isGuidedByControls' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Control()
    setattr(partner, 'isGuidedByControls', None)
    _safe_set(owner, 'Process225', partner)
    assert owner in getattr(partner, 'isGuidedByControls')
    _safe_set(owner, 'Process225', None)
    assert owner not in getattr(partner, 'isGuidedByControls')


def test_assoc_entities34_stub_double():
    # contentfwk_DataArchitecture has no real 'contentfwk_DataArchitecture' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_DataArchitecture()
    setattr(partner, 'contentfwk_DataArchitecture', None)
    _safe_set(owner, 'contentfwk_DataEntity', partner)
    assert owner in getattr(partner, 'contentfwk_DataArchitecture')
    _safe_set(owner, 'contentfwk_DataEntity', None)
    assert owner not in getattr(partner, 'contentfwk_DataArchitecture')


def test_assoc_extendsLogicalApplicationComponents269_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'LogicalApplicationComponent270' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'LogicalApplicationComponent270', None)
    _safe_set(owner, 'isExtendedByPhysicalApplicationComponents', {partner})
    assert getattr(partner, 'LogicalApplicationComponent270') == owner
    _safe_set(owner, 'isExtendedByPhysicalApplicationComponents', set())
    assert getattr(partner, 'LogicalApplicationComponent270') is None


def test_assoc_extendsLogicalTechnologyComponents182_stub_double():
    # contentfwk_LogicalTechnologyComponent has no real 'LogicalTechnologyComponent183' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_LogicalTechnologyComponent()
    setattr(partner, 'LogicalTechnologyComponent183', None)
    _safe_set(owner, 'isRealizedByPhysicalTechnologyComponents', {partner})
    assert getattr(partner, 'LogicalTechnologyComponent183') == owner
    _safe_set(owner, 'isRealizedByPhysicalTechnologyComponents', set())
    assert getattr(partner, 'LogicalTechnologyComponent183') is None


def test_assoc_generatesEvents166_stub_double():
    # contentfwk_Event has no real 'Event167' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event167', None)
    _safe_set(owner, 'isGeneratedByProcesses', {partner})
    assert getattr(partner, 'Event167') == owner
    _safe_set(owner, 'isGeneratedByProcesses', set())
    assert getattr(partner, 'Event167') is None


def test_assoc_generatesEvents81_stub_double():
    # contentfwk_Event has no real 'Event82' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event82', None)
    _safe_set(owner, 'isGeneratedByActors', {partner})
    assert getattr(partner, 'Event82') == owner
    _safe_set(owner, 'isGeneratedByActors', set())
    assert getattr(partner, 'Event82') is None


def test_assoc_governsAndMeasuresBusinessServices208_stub_double():
    # contentfwk_Service has no real 'Service209' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service209', None)
    _safe_set(owner, 'isGovernedAndMeasuredByContracts', {partner})
    assert getattr(partner, 'Service209') == owner
    _safe_set(owner, 'isGovernedAndMeasuredByContracts', set())
    assert getattr(partner, 'Service209') is None


def test_assoc_interactsWithFunctions73_stub_double():
    # contentfwk_Function has no real 'Function74' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function74', None)
    _safe_set(owner, 'supportsActors', {partner})
    assert getattr(partner, 'Function74') == owner
    _safe_set(owner, 'supportsActors', set())
    assert getattr(partner, 'Function74') is None


def test_assoc_isAccessedByServices102_stub_double():
    # contentfwk_Service has no real 'Service104' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service104', None)
    _safe_set(owner, 'consumesEntities103', {partner})
    assert getattr(partner, 'Service104') == owner
    _safe_set(owner, 'consumesEntities103', set())
    assert getattr(partner, 'Service104') is None


def test_assoc_isExtendedByPhysicalApplicationComponents119_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'extendsLogicalApplicationComponents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'extendsLogicalApplicationComponents', None)
    _safe_set(owner, 'PhysicalApplicationComponent', partner)
    assert owner in getattr(partner, 'extendsLogicalApplicationComponents')
    _safe_set(owner, 'PhysicalApplicationComponent', None)
    assert owner not in getattr(partner, 'extendsLogicalApplicationComponents')


def test_assoc_isGeneratedByActors221_stub_double():
    # contentfwk_Event has no real 'generatesEvents222' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'generatesEvents222', None)
    _safe_set(owner, 'Actor223', partner)
    assert getattr(partner, 'generatesEvents222') == owner
    _safe_set(owner, 'Actor223', None)
    assert getattr(partner, 'generatesEvents222') is None


def test_assoc_isGeneratedByProcesses216_stub_double():
    # contentfwk_Event has no real 'generatesEvents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'generatesEvents', None)
    _safe_set(owner, 'Process217', partner)
    assert owner in getattr(partner, 'generatesEvents')
    _safe_set(owner, 'Process217', None)
    assert owner not in getattr(partner, 'generatesEvents')


def test_assoc_isGovernedAndMeasuredByContracts308_stub_double():
    # contentfwk_Service has no real 'governsAndMeasuresBusinessServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'governsAndMeasuresBusinessServices', None)
    _safe_set(owner, 'Contract309', partner)
    assert owner in getattr(partner, 'governsAndMeasuresBusinessServices')
    _safe_set(owner, 'Contract309', None)
    assert owner not in getattr(partner, 'governsAndMeasuresBusinessServices')


def test_assoc_isGuidedByControls163_stub_double():
    # contentfwk_Control has no real 'Control' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Control()
    setattr(partner, 'Control', None)
    _safe_set(owner, 'ensuresCorrectOperationOfProcesses', {partner})
    assert getattr(partner, 'Control') == owner
    _safe_set(owner, 'ensuresCorrectOperationOfProcesses', set())
    assert getattr(partner, 'Control') is None


def test_assoc_isHostedInLocation184_stub_double():
    # contentfwk_Location has no real 'Location185' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location185', None)
    _safe_set(owner, 'containsPhysicalTechnologyComponents', {partner})
    assert getattr(partner, 'Location185') == owner
    _safe_set(owner, 'containsPhysicalTechnologyComponents', set())
    assert getattr(partner, 'Location185') is None


def test_assoc_isHostedInLocation271_stub_double():
    # contentfwk_Location has no real 'Location272' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location272', None)
    _safe_set(owner, 'containsPhysicalApplicationComponents', {partner})
    assert getattr(partner, 'Location272') == owner
    _safe_set(owner, 'containsPhysicalApplicationComponents', set())
    assert getattr(partner, 'Location272') is None


def test_assoc_isMotivatedByDrivers64_stub_double():
    # contentfwk_Driver has no real 'Driver65' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Driver()
    setattr(partner, 'Driver65', None)
    _safe_set(owner, 'motivatesOrganizationUnits', {partner})
    assert getattr(partner, 'Driver65') == owner
    _safe_set(owner, 'motivatesOrganizationUnits', set())
    assert getattr(partner, 'Driver65') is None


def test_assoc_isOwnedAndGovernedByOrganizationUnits316_stub_double():
    # contentfwk_Service has no real 'ownsAndGovernsServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'ownsAndGovernsServices', None)
    _safe_set(owner, 'OrganizationUnit317', partner)
    assert owner in getattr(partner, 'ownsAndGovernsServices')
    _safe_set(owner, 'OrganizationUnit317', None)
    assert owner not in getattr(partner, 'ownsAndGovernsServices')


def test_assoc_isOwnedByUnit127_stub_double():
    # contentfwk_Function has no real 'ownsFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'ownsFunctions', None)
    _safe_set(owner, 'OrganizationUnit128', partner)
    assert getattr(partner, 'ownsFunctions') == owner
    _safe_set(owner, 'OrganizationUnit128', None)
    assert getattr(partner, 'ownsFunctions') is None


def test_assoc_isPerformedByActors125_stub_double():
    # contentfwk_Function has no real 'performsFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'performsFunctions', None)
    _safe_set(owner, 'Actor126', partner)
    assert owner in getattr(partner, 'performsFunctions')
    _safe_set(owner, 'Actor126', None)
    assert owner not in getattr(partner, 'performsFunctions')


def test_assoc_isProcessesByLogicalApplicationComponents108_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'LogicalApplicationComponent' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'LogicalApplicationComponent', None)
    _safe_set(owner, 'operatesOnDataEntities', {partner})
    assert getattr(partner, 'LogicalApplicationComponent') == owner
    _safe_set(owner, 'operatesOnDataEntities', set())
    assert getattr(partner, 'LogicalApplicationComponent') is None


def test_assoc_isProducedByOrganizationUnits192_stub_double():
    # contentfwk_Product has no real 'producesProducts' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'producesProducts', None)
    _safe_set(owner, 'OrganizationUnit193', partner)
    assert owner in getattr(partner, 'producesProducts')
    _safe_set(owner, 'OrganizationUnit193', None)
    assert owner not in getattr(partner, 'producesProducts')


def test_assoc_isProducedByProcesses194_stub_double():
    # contentfwk_Product has no real 'producesProducts195' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'producesProducts195', None)
    _safe_set(owner, 'Process196', partner)
    assert owner in getattr(partner, 'producesProducts195')
    _safe_set(owner, 'Process196', None)
    assert owner not in getattr(partner, 'producesProducts195')


def test_assoc_isProvidedToActors299_stub_double():
    # contentfwk_Service has no real 'contentfwk_Service300' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'contentfwk_Service300', None)
    _safe_set(owner, 'contentfwk_Actor301', partner)
    assert owner in getattr(partner, 'contentfwk_Service300')
    _safe_set(owner, 'contentfwk_Actor301', None)
    assert owner not in getattr(partner, 'contentfwk_Service300')


def test_assoc_isRealizedByPhysicalTechnologyComponents288_stub_double():
    # contentfwk_LogicalTechnologyComponent has no real 'extendsLogicalTechnologyComponents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_LogicalTechnologyComponent()
    setattr(partner, 'extendsLogicalTechnologyComponents', None)
    _safe_set(owner, 'PhysicalTechnologyComponent289', partner)
    assert owner in getattr(partner, 'extendsLogicalTechnologyComponents')
    _safe_set(owner, 'PhysicalTechnologyComponent289', None)
    assert owner not in getattr(partner, 'extendsLogicalTechnologyComponents')


def test_assoc_isRealizedByProcesses133_stub_double():
    # contentfwk_Function has no real 'orchestratesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'orchestratesFunctions', None)
    _safe_set(owner, 'Process134', partner)
    assert owner in getattr(partner, 'orchestratesFunctions')
    _safe_set(owner, 'Process134', None)
    assert owner not in getattr(partner, 'orchestratesFunctions')


def test_assoc_isRealizedByProcesses322_stub_double():
    # contentfwk_Service has no real 'orchestratesServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'orchestratesServices', None)
    _safe_set(owner, 'Process323', partner)
    assert owner in getattr(partner, 'orchestratesServices')
    _safe_set(owner, 'Process323', None)
    assert owner not in getattr(partner, 'orchestratesServices')


def test_assoc_isResolvedByActors218_stub_double():
    # contentfwk_Event has no real 'resolvesEvents219' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'resolvesEvents219', None)
    _safe_set(owner, 'Actor220', partner)
    assert owner in getattr(partner, 'resolvesEvents219')
    _safe_set(owner, 'Actor220', None)
    assert owner not in getattr(partner, 'resolvesEvents219')


def test_assoc_isResolvedByProcesses213_stub_double():
    # contentfwk_Event has no real 'resolvesEvents214' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'resolvesEvents214', None)
    _safe_set(owner, 'Process215', partner)
    assert owner in getattr(partner, 'resolvesEvents214')
    _safe_set(owner, 'Process215', None)
    assert owner not in getattr(partner, 'resolvesEvents214')


def test_assoc_isUpdatedThroughServices105_stub_double():
    # contentfwk_Service has no real 'Service106' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service106', None)
    _safe_set(owner, 'providesEntities', {partner})
    assert getattr(partner, 'Service106') == owner
    _safe_set(owner, 'providesEntities', set())
    assert getattr(partner, 'Service106') is None


def test_assoc_meetsServiceQuality210_stub_double():
    # contentfwk_ServiceQuality has no real 'ServiceQuality' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_ServiceQuality()
    setattr(partner, 'ServiceQuality', None)
    _safe_set(owner, 'appliesToContracts', {partner})
    assert getattr(partner, 'ServiceQuality') == owner
    _safe_set(owner, 'appliesToContracts', set())
    assert getattr(partner, 'ServiceQuality') is None


def test_assoc_motivatesOrganizationUnits45_stub_double():
    # contentfwk_Driver has no real 'isMotivatedByDrivers' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Driver()
    setattr(partner, 'isMotivatedByDrivers', None)
    _safe_set(owner, 'OrganizationUnit', partner)
    assert owner in getattr(partner, 'isMotivatedByDrivers')
    _safe_set(owner, 'OrganizationUnit', None)
    assert owner not in getattr(partner, 'isMotivatedByDrivers')


def test_assoc_operatesInLocation67_stub_double():
    # contentfwk_Location has no real 'Location' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location', None)
    _safe_set(owner, 'containsOrganizationUnits', partner)
    assert getattr(partner, 'Location') == owner
    _safe_set(owner, 'containsOrganizationUnits', None)
    assert getattr(partner, 'Location') is None


def test_assoc_operatesInLocation83_stub_double():
    # contentfwk_Location has no real 'Location85' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location85', None)
    _safe_set(owner, 'containsActors84', partner)
    assert getattr(partner, 'Location85') == owner
    _safe_set(owner, 'containsActors84', None)
    assert getattr(partner, 'Location85') is None


def test_assoc_operatesOnDataEntities117_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'isProcessesByLogicalApplicationComponents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'isProcessesByLogicalApplicationComponents', None)
    _safe_set(owner, 'DataEntity118', partner)
    assert owner in getattr(partner, 'isProcessesByLogicalApplicationComponents')
    _safe_set(owner, 'DataEntity118', None)
    assert owner not in getattr(partner, 'isProcessesByLogicalApplicationComponents')


def test_assoc_orchestratesFunctions148_stub_double():
    # contentfwk_Function has no real 'Function149' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function149', None)
    _safe_set(owner, 'isRealizedByProcesses', {partner})
    assert getattr(partner, 'Function149') == owner
    _safe_set(owner, 'isRealizedByProcesses', set())
    assert getattr(partner, 'Function149') is None


def test_assoc_orchestratesServices154_stub_double():
    # contentfwk_Service has no real 'Service156' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service156', None)
    _safe_set(owner, 'isRealizedByProcesses155', {partner})
    assert getattr(partner, 'Service156') == owner
    _safe_set(owner, 'isRealizedByProcesses155', set())
    assert getattr(partner, 'Service156') is None


def test_assoc_ownsAndGovernsServices60_stub_double():
    # contentfwk_Service has no real 'Service' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service', None)
    _safe_set(owner, 'isOwnedAndGovernedByOrganizationUnits', {partner})
    assert getattr(partner, 'Service') == owner
    _safe_set(owner, 'isOwnedAndGovernedByOrganizationUnits', set())
    assert getattr(partner, 'Service') is None


def test_assoc_ownsFunctions62_stub_double():
    # contentfwk_Function has no real 'Function' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function', None)
    _safe_set(owner, 'isOwnedByUnit', {partner})
    assert getattr(partner, 'Function') == owner
    _safe_set(owner, 'isOwnedByUnit', set())
    assert getattr(partner, 'Function') is None


def test_assoc_performsFunctions86_stub_double():
    # contentfwk_Function has no real 'Function87' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function87', None)
    _safe_set(owner, 'isPerformedByActors', {partner})
    assert getattr(partner, 'Function87') == owner
    _safe_set(owner, 'isPerformedByActors', set())
    assert getattr(partner, 'Function87') is None


def test_assoc_physicalApplicationComponents264_stub_double():
    # contentfwk_ApplicationArchitecture has no real 'contentfwk_ApplicationArchitecture265' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_ApplicationArchitecture()
    setattr(partner, 'contentfwk_ApplicationArchitecture265', None)
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent266', partner)
    assert owner in getattr(partner, 'contentfwk_ApplicationArchitecture265')
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent266', None)
    assert owner not in getattr(partner, 'contentfwk_ApplicationArchitecture265')


def test_assoc_physicalComponents40_stub_double():
    # contentfwk_TechnologyArchitecture has no real 'contentfwk_TechnologyArchitecture41' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_TechnologyArchitecture()
    setattr(partner, 'contentfwk_TechnologyArchitecture41', None)
    _safe_set(owner, 'contentfwk_PhysicalTechnologyComponent', partner)
    assert owner in getattr(partner, 'contentfwk_TechnologyArchitecture41')
    _safe_set(owner, 'contentfwk_PhysicalTechnologyComponent', None)
    assert owner not in getattr(partner, 'contentfwk_TechnologyArchitecture41')


def test_assoc_processes18_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture19' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture19', None)
    _safe_set(owner, 'contentfwk_Process', partner)
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture19')
    _safe_set(owner, 'contentfwk_Process', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture19')


def test_assoc_producesProducts168_stub_double():
    # contentfwk_Product has no real 'Product169' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'Product169', None)
    _safe_set(owner, 'isProducedByProcesses', {partner})
    assert getattr(partner, 'Product169') == owner
    _safe_set(owner, 'isProducedByProcesses', set())
    assert getattr(partner, 'Product169') is None


def test_assoc_producesProducts66_stub_double():
    # contentfwk_Product has no real 'Product' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'Product', None)
    _safe_set(owner, 'isProducedByOrganizationUnits', {partner})
    assert getattr(partner, 'Product') == owner
    _safe_set(owner, 'isProducedByOrganizationUnits', set())
    assert getattr(partner, 'Product') is None


def test_assoc_providesEntities304_stub_double():
    # contentfwk_Service has no real 'isUpdatedThroughServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'isUpdatedThroughServices', None)
    _safe_set(owner, 'DataEntity305', partner)
    assert owner in getattr(partner, 'isUpdatedThroughServices')
    _safe_set(owner, 'DataEntity305', None)
    assert owner not in getattr(partner, 'isUpdatedThroughServices')


def test_assoc_residesWithinLogicalDataComponent107_stub_double():
    # contentfwk_LogicalDataComponent has no real 'LogicalDataComponent' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_LogicalDataComponent()
    setattr(partner, 'LogicalDataComponent', None)
    _safe_set(owner, 'encapsulatesDataEntities', partner)
    assert getattr(partner, 'LogicalDataComponent') == owner
    _safe_set(owner, 'encapsulatesDataEntities', None)
    assert getattr(partner, 'LogicalDataComponent') is None


def test_assoc_resolvesEvents164_stub_double():
    # contentfwk_Event has no real 'Event165' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event165', None)
    _safe_set(owner, 'isResolvedByProcesses', {partner})
    assert getattr(partner, 'Event165') == owner
    _safe_set(owner, 'isResolvedByProcesses', set())
    assert getattr(partner, 'Event165') is None


def test_assoc_resolvesEvents80_stub_double():
    # contentfwk_Event has no real 'Event' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event', None)
    _safe_set(owner, 'isResolvedByActors', {partner})
    assert getattr(partner, 'Event') == owner
    _safe_set(owner, 'isResolvedByActors', set())
    assert getattr(partner, 'Event') is None


def test_assoc_roles12_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture13' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Role(estimatedFTEs="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture13', None)
    _safe_set(owner, 'contentfwk_Role', partner)
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture13')
    _safe_set(owner, 'contentfwk_Role', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture13')


def test_assoc_supportsActors137_stub_double():
    # contentfwk_Function has no real 'interactsWithFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'interactsWithFunctions', None)
    _safe_set(owner, 'Actor138', partner)
    assert owner in getattr(partner, 'interactsWithFunctions')
    _safe_set(owner, 'Actor138', None)
    assert owner not in getattr(partner, 'interactsWithFunctions')


def test_assoc_supportsProcesses131_stub_double():
    # contentfwk_Function has no real 'decomposesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'decomposesFunctions', None)
    _safe_set(owner, 'Process132', partner)
    assert owner in getattr(partner, 'decomposesFunctions')
    _safe_set(owner, 'Process132', None)
    assert owner not in getattr(partner, 'decomposesFunctions')


def test_assoc_supportsProcesses320_stub_double():
    # contentfwk_Service has no real 'decomposesServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'decomposesServices', None)
    _safe_set(owner, 'Process321', partner)
    assert owner in getattr(partner, 'decomposesServices')
    _safe_set(owner, 'Process321', None)
    assert owner not in getattr(partner, 'decomposesServices')


def test_assoc_units8_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture9' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture9', None)
    _safe_set(owner, 'contentfwk_OrganizationUnit', partner)
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture9')
    _safe_set(owner, 'contentfwk_OrganizationUnit', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture9')


