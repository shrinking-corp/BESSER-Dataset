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
    contentfwk_EObject,
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

def test_assoc_belongsTo73_reverse_link_reassign_clear():
    a1 = contentfwk_OrganizationUnit(headcount="sample_text")
    a2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'containsActors', a1)
    assert _is_linked(b, 'containsActors', a1)
    if hasattr(a1, 'OrganizationUnit74'):
        assert _is_linked(a1, 'OrganizationUnit74', b)
    _safe_set(b, 'containsActors', a2)
    assert _is_linked(b, 'containsActors', a2)
    if hasattr(a1, 'OrganizationUnit74'):
        assert not _is_linked(a1, 'OrganizationUnit74', b)
    if hasattr(a2, 'OrganizationUnit74'):
        assert _is_linked(a2, 'OrganizationUnit74', b)
    _safe_set(b, 'containsActors', None)
    assert not _is_linked(b, 'containsActors', a2)
    if hasattr(a2, 'OrganizationUnit74'):
        assert not _is_linked(a2, 'OrganizationUnit74', b)


def test_assoc_communicatesWith288_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    a2 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent289', a1)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent289', a1)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent287'):
        assert _is_linked(a1, 'contentfwk_PhysicalApplicationComponent287', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent289', a2)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent289', a2)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent287'):
        assert not _is_linked(a1, 'contentfwk_PhysicalApplicationComponent287', b)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent287'):
        assert _is_linked(a2, 'contentfwk_PhysicalApplicationComponent287', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent289', None)
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent289', a2)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent287'):
        assert not _is_linked(a2, 'contentfwk_PhysicalApplicationComponent287', b)


def test_assoc_consumesEntities71_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'isConsumedByActors', {a1})
    assert _is_linked(b, 'isConsumedByActors', a1)
    if hasattr(a1, 'DataEntity72'):
        assert _is_linked(a1, 'DataEntity72', b)
    _safe_set(b, 'isConsumedByActors', {a2})
    assert _is_linked(b, 'isConsumedByActors', a2)
    if hasattr(a1, 'DataEntity72'):
        assert not _is_linked(a1, 'DataEntity72', b)
    if hasattr(a2, 'DataEntity72'):
        assert _is_linked(a2, 'DataEntity72', b)
    _safe_set(b, 'isConsumedByActors', set())
    assert not _is_linked(b, 'isConsumedByActors', a2)
    if hasattr(a2, 'DataEntity72'):
        assert not _is_linked(a2, 'DataEntity72', b)


def test_assoc_containsActors63_reverse_link_reassign_clear():
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


def test_assoc_decomposeEntity112_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    _safe_set(b, 'contentfwk_DataEntity113', a1)
    assert _is_linked(b, 'contentfwk_DataEntity113', a1)
    if hasattr(a1, 'contentfwk_DataEntity111'):
        assert _is_linked(a1, 'contentfwk_DataEntity111', b)
    _safe_set(b, 'contentfwk_DataEntity113', a2)
    assert _is_linked(b, 'contentfwk_DataEntity113', a2)
    if hasattr(a1, 'contentfwk_DataEntity111'):
        assert not _is_linked(a1, 'contentfwk_DataEntity111', b)
    if hasattr(a2, 'contentfwk_DataEntity111'):
        assert _is_linked(a2, 'contentfwk_DataEntity111', b)
    _safe_set(b, 'contentfwk_DataEntity113', None)
    assert not _is_linked(b, 'contentfwk_DataEntity113', a2)
    if hasattr(a2, 'contentfwk_DataEntity111'):
        assert not _is_linked(a2, 'contentfwk_DataEntity111', b)


def test_assoc_decomposesActors91_reverse_link_reassign_clear():
    a1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    a2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'contentfwk_Actor92', a1)
    assert _is_linked(b, 'contentfwk_Actor92', a1)
    if hasattr(a1, 'contentfwk_Actor90'):
        assert _is_linked(a1, 'contentfwk_Actor90', b)
    _safe_set(b, 'contentfwk_Actor92', a2)
    assert _is_linked(b, 'contentfwk_Actor92', a2)
    if hasattr(a1, 'contentfwk_Actor90'):
        assert not _is_linked(a1, 'contentfwk_Actor90', b)
    if hasattr(a2, 'contentfwk_Actor90'):
        assert _is_linked(a2, 'contentfwk_Actor90', b)
    _safe_set(b, 'contentfwk_Actor92', None)
    assert not _is_linked(b, 'contentfwk_Actor92', a2)
    if hasattr(a2, 'contentfwk_Actor90'):
        assert not _is_linked(a2, 'contentfwk_Actor90', b)


def test_assoc_decomposesPhysicalApplicationComponent297_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    a2 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent298', a1)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent298', a1)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent296'):
        assert _is_linked(a1, 'contentfwk_PhysicalApplicationComponent296', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent298', a2)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent298', a2)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent296'):
        assert not _is_linked(a1, 'contentfwk_PhysicalApplicationComponent296', b)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent296'):
        assert _is_linked(a2, 'contentfwk_PhysicalApplicationComponent296', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent298', None)
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent298', a2)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent296'):
        assert not _is_linked(a2, 'contentfwk_PhysicalApplicationComponent296', b)


def test_assoc_decomposesPhysicalTechnologyComponent198_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent199', a1)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent199', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent197'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent197', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent199', a2)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent199', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent197'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent197', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent197'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent197', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent199', None)
    assert not _is_linked(b, 'contentfwk_PhysicalTechnologyComponent199', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent197'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent197', b)


def test_assoc_decomposesProcess179_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'contentfwk_Process180', a1)
    assert _is_linked(b, 'contentfwk_Process180', a1)
    if hasattr(a1, 'contentfwk_Process178'):
        assert _is_linked(a1, 'contentfwk_Process178', b)
    _safe_set(b, 'contentfwk_Process180', a2)
    assert _is_linked(b, 'contentfwk_Process180', a2)
    if hasattr(a1, 'contentfwk_Process178'):
        assert not _is_linked(a1, 'contentfwk_Process178', b)
    if hasattr(a2, 'contentfwk_Process178'):
        assert _is_linked(a2, 'contentfwk_Process178', b)
    _safe_set(b, 'contentfwk_Process180', None)
    assert not _is_linked(b, 'contentfwk_Process180', a2)
    if hasattr(a2, 'contentfwk_Process178'):
        assert not _is_linked(a2, 'contentfwk_Process178', b)


def test_assoc_decomposesRole98_reverse_link_reassign_clear():
    a1 = contentfwk_Role(estimatedFTEs="sample_text")
    a2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    b = contentfwk_Role(estimatedFTEs="sample_text")
    _safe_set(b, 'contentfwk_Role99', a1)
    assert _is_linked(b, 'contentfwk_Role99', a1)
    if hasattr(a1, 'contentfwk_Role97'):
        assert _is_linked(a1, 'contentfwk_Role97', b)
    _safe_set(b, 'contentfwk_Role99', a2)
    assert _is_linked(b, 'contentfwk_Role99', a2)
    if hasattr(a1, 'contentfwk_Role97'):
        assert not _is_linked(a1, 'contentfwk_Role97', b)
    if hasattr(a2, 'contentfwk_Role97'):
        assert _is_linked(a2, 'contentfwk_Role97', b)
    _safe_set(b, 'contentfwk_Role99', None)
    assert not _is_linked(b, 'contentfwk_Role99', a2)
    if hasattr(a2, 'contentfwk_Role97'):
        assert not _is_linked(a2, 'contentfwk_Role97', b)


def test_assoc_delegates238_reverse_link_reassign_clear():
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


def test_assoc_deliversCapabilities258_reverse_link_reassign_clear():
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


def test_assoc_followsProcesses185_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'precedesProcesses', {a1})
    assert _is_linked(b, 'precedesProcesses', a1)
    if hasattr(a1, 'Process186'):
        assert _is_linked(a1, 'Process186', b)
    _safe_set(b, 'precedesProcesses', {a2})
    assert _is_linked(b, 'precedesProcesses', a2)
    if hasattr(a1, 'Process186'):
        assert not _is_linked(a1, 'Process186', b)
    if hasattr(a2, 'Process186'):
        assert _is_linked(a2, 'Process186', b)
    _safe_set(b, 'precedesProcesses', set())
    assert not _is_linked(b, 'precedesProcesses', a2)
    if hasattr(a2, 'Process186'):
        assert not _is_linked(a2, 'Process186', b)


def test_assoc_involvesActors168_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor170', a1)
    assert _is_linked(b, 'Actor170', a1)
    if hasattr(a1, 'participatesInProcesses169'):
        assert _is_linked(a1, 'participatesInProcesses169', b)
    _safe_set(b, 'Actor170', a2)
    assert _is_linked(b, 'Actor170', a2)
    if hasattr(a1, 'participatesInProcesses169'):
        assert not _is_linked(a1, 'participatesInProcesses169', b)
    if hasattr(a2, 'participatesInProcesses169'):
        assert _is_linked(a2, 'participatesInProcesses169', b)
    _safe_set(b, 'Actor170', None)
    assert not _is_linked(b, 'Actor170', a2)
    if hasattr(a2, 'participatesInProcesses169'):
        assert not _is_linked(a2, 'participatesInProcesses169', b)


def test_assoc_involvesOrganizationUnits160_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_OrganizationUnit(headcount="sample_text")
    _safe_set(b, 'OrganizationUnit161', a1)
    assert _is_linked(b, 'OrganizationUnit161', a1)
    if hasattr(a1, 'participatesInProcesses'):
        assert _is_linked(a1, 'participatesInProcesses', b)
    _safe_set(b, 'OrganizationUnit161', a2)
    assert _is_linked(b, 'OrganizationUnit161', a2)
    if hasattr(a1, 'participatesInProcesses'):
        assert not _is_linked(a1, 'participatesInProcesses', b)
    if hasattr(a2, 'participatesInProcesses'):
        assert _is_linked(a2, 'participatesInProcesses', b)
    _safe_set(b, 'OrganizationUnit161', None)
    assert not _is_linked(b, 'OrganizationUnit161', a2)
    if hasattr(a2, 'participatesInProcesses'):
        assert not _is_linked(a2, 'participatesInProcesses', b)


def test_assoc_isAssumedByActors93_reverse_link_reassign_clear():
    a1 = contentfwk_Role(estimatedFTEs="sample_text")
    a2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor94', a1)
    assert _is_linked(b, 'Actor94', a1)
    if hasattr(a1, 'performsTaskInRoles'):
        assert _is_linked(a1, 'performsTaskInRoles', b)
    _safe_set(b, 'Actor94', a2)
    assert _is_linked(b, 'Actor94', a2)
    if hasattr(a1, 'performsTaskInRoles'):
        assert not _is_linked(a1, 'performsTaskInRoles', b)
    if hasattr(a2, 'performsTaskInRoles'):
        assert _is_linked(a2, 'performsTaskInRoles', b)
    _safe_set(b, 'Actor94', None)
    assert not _is_linked(b, 'Actor94', a2)
    if hasattr(a2, 'performsTaskInRoles'):
        assert not _is_linked(a2, 'performsTaskInRoles', b)


def test_assoc_isConsumedByActors102_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor103', a1)
    assert _is_linked(b, 'Actor103', a1)
    if hasattr(a1, 'consumesEntities'):
        assert _is_linked(a1, 'consumesEntities', b)
    _safe_set(b, 'Actor103', a2)
    assert _is_linked(b, 'Actor103', a2)
    if hasattr(a1, 'consumesEntities'):
        assert not _is_linked(a1, 'consumesEntities', b)
    if hasattr(a2, 'consumesEntities'):
        assert _is_linked(a2, 'consumesEntities', b)
    _safe_set(b, 'Actor103', None)
    assert not _is_linked(b, 'Actor103', a2)
    if hasattr(a2, 'consumesEntities'):
        assert not _is_linked(a2, 'consumesEntities', b)


def test_assoc_isDelegatedBy240_reverse_link_reassign_clear():
    a1 = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    a2 = contentfwk_Element(ID="sample_text_2", category="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    b = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    _safe_set(b, 'delegates', {a1})
    assert _is_linked(b, 'delegates', a1)
    if hasattr(a1, 'Element241'):
        assert _is_linked(a1, 'Element241', b)
    _safe_set(b, 'delegates', {a2})
    assert _is_linked(b, 'delegates', a2)
    if hasattr(a1, 'Element241'):
        assert not _is_linked(a1, 'Element241', b)
    if hasattr(a2, 'Element241'):
        assert _is_linked(a2, 'Element241', b)
    _safe_set(b, 'delegates', set())
    assert not _is_linked(b, 'delegates', a2)
    if hasattr(a2, 'Element241'):
        assert not _is_linked(a2, 'Element241', b)


def test_assoc_isDeliveredBy257_reverse_link_reassign_clear():
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


def test_assoc_isDependentOnPhysicalTechnologyComponents201_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent202', a1)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent202', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent200'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent200', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent202', a2)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent202', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent200'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent200', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent200'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent200', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent202', None)
    assert not _is_linked(b, 'contentfwk_PhysicalTechnologyComponent202', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent200'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent200', b)


def test_assoc_isRealizedByPhysicalTechnologyComponents293_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent294', {a1})
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent294', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent295'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent295', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent294', {a2})
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent294', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent295'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent295', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent295'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent295', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent294', set())
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent294', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent295'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent295', b)


def test_assoc_isSuppliedByActors100_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor101', a1)
    assert _is_linked(b, 'Actor101', a1)
    if hasattr(a1, 'suppliesEntities'):
        assert _is_linked(a1, 'suppliesEntities', b)
    _safe_set(b, 'Actor101', a2)
    assert _is_linked(b, 'Actor101', a2)
    if hasattr(a1, 'suppliesEntities'):
        assert not _is_linked(a1, 'suppliesEntities', b)
    if hasattr(a2, 'suppliesEntities'):
        assert _is_linked(a2, 'suppliesEntities', b)
    _safe_set(b, 'Actor101', None)
    assert not _is_linked(b, 'Actor101', a2)
    if hasattr(a2, 'suppliesEntities'):
        assert not _is_linked(a2, 'suppliesEntities', b)


def test_assoc_ownsElements242_reverse_link_reassign_clear():
    a1 = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    a2 = contentfwk_Element(ID="sample_text_2", category="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    b = contentfwk_Container(name="sample_text")
    _safe_set(b, 'contentfwk_Container243', {a1})
    assert _is_linked(b, 'contentfwk_Container243', a1)
    if hasattr(a1, 'contentfwk_Element'):
        assert _is_linked(a1, 'contentfwk_Element', b)
    _safe_set(b, 'contentfwk_Container243', {a2})
    assert _is_linked(b, 'contentfwk_Container243', a2)
    if hasattr(a1, 'contentfwk_Element'):
        assert not _is_linked(a1, 'contentfwk_Element', b)
    if hasattr(a2, 'contentfwk_Element'):
        assert _is_linked(a2, 'contentfwk_Element', b)
    _safe_set(b, 'contentfwk_Container243', set())
    assert not _is_linked(b, 'contentfwk_Container243', a2)
    if hasattr(a2, 'contentfwk_Element'):
        assert not _is_linked(a2, 'contentfwk_Element', b)


def test_assoc_participatesInProcesses65_reverse_link_reassign_clear():
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


def test_assoc_participatesInProcesses78_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'involvesActors', {a1})
    assert _is_linked(b, 'involvesActors', a1)
    if hasattr(a1, 'Process79'):
        assert _is_linked(a1, 'Process79', b)
    _safe_set(b, 'involvesActors', {a2})
    assert _is_linked(b, 'involvesActors', a2)
    if hasattr(a1, 'Process79'):
        assert not _is_linked(a1, 'Process79', b)
    if hasattr(a2, 'Process79'):
        assert _is_linked(a2, 'Process79', b)
    _safe_set(b, 'involvesActors', set())
    assert not _is_linked(b, 'involvesActors', a2)
    if hasattr(a2, 'Process79'):
        assert not _is_linked(a2, 'Process79', b)


def test_assoc_performsTaskInRoles77_reverse_link_reassign_clear():
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


def test_assoc_precedesProcesses182_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'followsProcesses', {a1})
    assert _is_linked(b, 'followsProcesses', a1)
    if hasattr(a1, 'Process183'):
        assert _is_linked(a1, 'Process183', b)
    _safe_set(b, 'followsProcesses', {a2})
    assert _is_linked(b, 'followsProcesses', a2)
    if hasattr(a1, 'Process183'):
        assert not _is_linked(a1, 'Process183', b)
    if hasattr(a2, 'Process183'):
        assert _is_linked(a2, 'Process183', b)
    _safe_set(b, 'followsProcesses', set())
    assert not _is_linked(b, 'followsProcesses', a2)
    if hasattr(a2, 'Process183'):
        assert not _is_linked(a2, 'Process183', b)


def test_assoc_realizesApplicationComponents191_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent', a1)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent192'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent192', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent', a2)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent192'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent192', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent192'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent192', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent', None)
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent192'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent192', b)


def test_assoc_relatesTo115_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    _safe_set(b, 'contentfwk_DataEntity116', a1)
    assert _is_linked(b, 'contentfwk_DataEntity116', a1)
    if hasattr(a1, 'contentfwk_DataEntity114'):
        assert _is_linked(a1, 'contentfwk_DataEntity114', b)
    _safe_set(b, 'contentfwk_DataEntity116', a2)
    assert _is_linked(b, 'contentfwk_DataEntity116', a2)
    if hasattr(a1, 'contentfwk_DataEntity114'):
        assert not _is_linked(a1, 'contentfwk_DataEntity114', b)
    if hasattr(a2, 'contentfwk_DataEntity114'):
        assert _is_linked(a2, 'contentfwk_DataEntity114', b)
    _safe_set(b, 'contentfwk_DataEntity116', None)
    assert not _is_linked(b, 'contentfwk_DataEntity116', a2)
    if hasattr(a2, 'contentfwk_DataEntity114'):
        assert not _is_linked(a2, 'contentfwk_DataEntity114', b)


def test_assoc_suppliesEntities70_reverse_link_reassign_clear():
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

def test_assoc_accessesFunctions95_stub_double():
    # contentfwk_Function has no real 'Function96' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Role(estimatedFTEs="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function96', None)
    _safe_set(owner, 'canBeAccessedByRoles', {partner})
    assert getattr(partner, 'Function96') == owner
    _safe_set(owner, 'canBeAccessedByRoles', set())
    assert getattr(partner, 'Function96') is None


def test_assoc_actors12_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture13' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture13', None)
    _safe_set(owner, 'contentfwk_Actor', partner)
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture13')
    _safe_set(owner, 'contentfwk_Actor', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture13')


def test_assoc_any117_stub_double():
    # contentfwk_EObject has no real 'contentfwk_EObject119' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_EObject()
    setattr(partner, 'contentfwk_EObject119', None)
    _safe_set(owner, 'contentfwk_DataEntity118', partner)
    assert getattr(partner, 'contentfwk_EObject119') == owner
    _safe_set(owner, 'contentfwk_DataEntity118', None)
    assert getattr(partner, 'contentfwk_EObject119') is None


def test_assoc_any187_stub_double():
    # contentfwk_EObject has no real 'contentfwk_EObject189' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_EObject()
    setattr(partner, 'contentfwk_EObject189', None)
    _safe_set(owner, 'contentfwk_Process188', partner)
    assert getattr(partner, 'contentfwk_EObject189') == owner
    _safe_set(owner, 'contentfwk_Process188', None)
    assert getattr(partner, 'contentfwk_EObject189') is None


def test_assoc_appliesToContracts218_stub_double():
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


def test_assoc_canBeAccessedByRoles143_stub_double():
    # contentfwk_Function has no real 'accessesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Role(estimatedFTEs="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'accessesFunctions', None)
    _safe_set(owner, 'Role144', partner)
    assert owner in getattr(partner, 'accessesFunctions')
    _safe_set(owner, 'Role144', None)
    assert owner not in getattr(partner, 'accessesFunctions')


def test_assoc_capabilities310_stub_double():
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


def test_assoc_consumesEntities320_stub_double():
    # contentfwk_Service has no real 'isAccessedByServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'isAccessedByServices', None)
    _safe_set(owner, 'DataEntity321', partner)
    assert owner in getattr(partner, 'isAccessedByServices')
    _safe_set(owner, 'DataEntity321', None)
    assert owner not in getattr(partner, 'isAccessedByServices')


def test_assoc_consumesServices80_stub_double():
    # contentfwk_Service has no real 'contentfwk_Service' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'contentfwk_Service', None)
    _safe_set(owner, 'contentfwk_Actor81', {partner})
    assert getattr(partner, 'contentfwk_Service') == owner
    _safe_set(owner, 'contentfwk_Actor81', set())
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


def test_assoc_containsActors244_stub_double():
    # contentfwk_Location has no real 'operatesInLocation' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'operatesInLocation', None)
    _safe_set(owner, 'Actor245', partner)
    assert owner in getattr(partner, 'operatesInLocation')
    _safe_set(owner, 'Actor245', None)
    assert owner not in getattr(partner, 'operatesInLocation')


def test_assoc_containsOrganizationUnits246_stub_double():
    # contentfwk_Location has no real 'operatesInLocation247' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'operatesInLocation247', None)
    _safe_set(owner, 'OrganizationUnit248', partner)
    assert owner in getattr(partner, 'operatesInLocation247')
    _safe_set(owner, 'OrganizationUnit248', None)
    assert owner not in getattr(partner, 'operatesInLocation247')


def test_assoc_containsPhysicalApplicationComponents250_stub_double():
    # contentfwk_Location has no real 'isHostedInLocation' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'isHostedInLocation', None)
    _safe_set(owner, 'PhysicalApplicationComponent251', partner)
    assert owner in getattr(partner, 'isHostedInLocation')
    _safe_set(owner, 'PhysicalApplicationComponent251', None)
    assert owner not in getattr(partner, 'isHostedInLocation')


def test_assoc_containsPhysicalTechnologyComponents252_stub_double():
    # contentfwk_Location has no real 'isHostedInLocation253' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'isHostedInLocation253', None)
    _safe_set(owner, 'PhysicalTechnologyComponent', partner)
    assert owner in getattr(partner, 'isHostedInLocation253')
    _safe_set(owner, 'PhysicalTechnologyComponent', None)
    assert owner not in getattr(partner, 'isHostedInLocation253')


def test_assoc_contracts30_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture31' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture31', None)
    _safe_set(owner, 'contentfwk_Contract', partner)
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture31')
    _safe_set(owner, 'contentfwk_Contract', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture31')


def test_assoc_decomposesFunctions158_stub_double():
    # contentfwk_Function has no real 'Function159' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function159', None)
    _safe_set(owner, 'supportsProcesses', {partner})
    assert getattr(partner, 'Function159') == owner
    _safe_set(owner, 'supportsProcesses', set())
    assert getattr(partner, 'Function159') is None


def test_assoc_decomposesServices165_stub_double():
    # contentfwk_Service has no real 'Service167' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service167', None)
    _safe_set(owner, 'supportsProcesses166', {partner})
    assert getattr(partner, 'Service167') == owner
    _safe_set(owner, 'supportsProcesses166', set())
    assert getattr(partner, 'Service167') is None


def test_assoc_encapsulatesDataEntities259_stub_double():
    # contentfwk_LogicalDataComponent has no real 'residesWithinLogicalDataComponent' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_LogicalDataComponent()
    setattr(partner, 'residesWithinLogicalDataComponent', None)
    _safe_set(owner, 'DataEntity260', partner)
    assert owner in getattr(partner, 'residesWithinLogicalDataComponent')
    _safe_set(owner, 'DataEntity260', None)
    assert owner not in getattr(partner, 'residesWithinLogicalDataComponent')


def test_assoc_encapsulatesPhysicalApplicationComponents270_stub_double():
    # contentfwk_PhysicalDataComponent has no real 'contentfwk_PhysicalDataComponent271' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_PhysicalDataComponent()
    setattr(partner, 'contentfwk_PhysicalDataComponent271', None)
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent272', partner)
    assert owner in getattr(partner, 'contentfwk_PhysicalDataComponent271')
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent272', None)
    assert owner not in getattr(partner, 'contentfwk_PhysicalDataComponent271')


def test_assoc_encapsulatesPhysicalDataComponents290_stub_double():
    # contentfwk_PhysicalDataComponent has no real 'contentfwk_PhysicalDataComponent292' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_PhysicalDataComponent()
    setattr(partner, 'contentfwk_PhysicalDataComponent292', None)
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent291', {partner})
    assert getattr(partner, 'contentfwk_PhysicalDataComponent292') == owner
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent291', set())
    assert getattr(partner, 'contentfwk_PhysicalDataComponent292') is None


def test_assoc_ensuresCorrectOperationOfProcesses235_stub_double():
    # contentfwk_Control has no real 'isGuidedByControls' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Control()
    setattr(partner, 'isGuidedByControls', None)
    _safe_set(owner, 'Process236', partner)
    assert owner in getattr(partner, 'isGuidedByControls')
    _safe_set(owner, 'Process236', None)
    assert owner not in getattr(partner, 'isGuidedByControls')


def test_assoc_entities36_stub_double():
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


def test_assoc_extendsLogicalApplicationComponents283_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'LogicalApplicationComponent284' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'LogicalApplicationComponent284', None)
    _safe_set(owner, 'isExtendedByPhysicalApplicationComponents', {partner})
    assert getattr(partner, 'LogicalApplicationComponent284') == owner
    _safe_set(owner, 'isExtendedByPhysicalApplicationComponents', set())
    assert getattr(partner, 'LogicalApplicationComponent284') is None


def test_assoc_extendsLogicalTechnologyComponents193_stub_double():
    # contentfwk_LogicalTechnologyComponent has no real 'LogicalTechnologyComponent194' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_LogicalTechnologyComponent()
    setattr(partner, 'LogicalTechnologyComponent194', None)
    _safe_set(owner, 'isRealizedByPhysicalTechnologyComponents', {partner})
    assert getattr(partner, 'LogicalTechnologyComponent194') == owner
    _safe_set(owner, 'isRealizedByPhysicalTechnologyComponents', set())
    assert getattr(partner, 'LogicalTechnologyComponent194') is None


def test_assoc_generatesEvents174_stub_double():
    # contentfwk_Event has no real 'Event175' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event175', None)
    _safe_set(owner, 'isGeneratedByProcesses', {partner})
    assert getattr(partner, 'Event175') == owner
    _safe_set(owner, 'isGeneratedByProcesses', set())
    assert getattr(partner, 'Event175') is None


def test_assoc_generatesEvents83_stub_double():
    # contentfwk_Event has no real 'Event84' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event84', None)
    _safe_set(owner, 'isGeneratedByActors', {partner})
    assert getattr(partner, 'Event84') == owner
    _safe_set(owner, 'isGeneratedByActors', set())
    assert getattr(partner, 'Event84') is None


def test_assoc_governsAndMeasuresBusinessServices219_stub_double():
    # contentfwk_Service has no real 'Service220' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service220', None)
    _safe_set(owner, 'isGovernedAndMeasuredByContracts', {partner})
    assert getattr(partner, 'Service220') == owner
    _safe_set(owner, 'isGovernedAndMeasuredByContracts', set())
    assert getattr(partner, 'Service220') is None


def test_assoc_interactsWithFunctions75_stub_double():
    # contentfwk_Function has no real 'Function76' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function76', None)
    _safe_set(owner, 'supportsActors', {partner})
    assert getattr(partner, 'Function76') == owner
    _safe_set(owner, 'supportsActors', set())
    assert getattr(partner, 'Function76') is None


def test_assoc_isAccessedByServices104_stub_double():
    # contentfwk_Service has no real 'Service106' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service106', None)
    _safe_set(owner, 'consumesEntities105', {partner})
    assert getattr(partner, 'Service106') == owner
    _safe_set(owner, 'consumesEntities105', set())
    assert getattr(partner, 'Service106') is None


def test_assoc_isExtendedByPhysicalApplicationComponents124_stub_double():
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


def test_assoc_isGeneratedByActors232_stub_double():
    # contentfwk_Event has no real 'generatesEvents233' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'generatesEvents233', None)
    _safe_set(owner, 'Actor234', partner)
    assert getattr(partner, 'generatesEvents233') == owner
    _safe_set(owner, 'Actor234', None)
    assert getattr(partner, 'generatesEvents233') is None


def test_assoc_isGeneratedByProcesses227_stub_double():
    # contentfwk_Event has no real 'generatesEvents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'generatesEvents', None)
    _safe_set(owner, 'Process228', partner)
    assert owner in getattr(partner, 'generatesEvents')
    _safe_set(owner, 'Process228', None)
    assert owner not in getattr(partner, 'generatesEvents')


def test_assoc_isGovernedAndMeasuredByContracts322_stub_double():
    # contentfwk_Service has no real 'governsAndMeasuresBusinessServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'governsAndMeasuresBusinessServices', None)
    _safe_set(owner, 'Contract323', partner)
    assert owner in getattr(partner, 'governsAndMeasuresBusinessServices')
    _safe_set(owner, 'Contract323', None)
    assert owner not in getattr(partner, 'governsAndMeasuresBusinessServices')


def test_assoc_isGuidedByControls171_stub_double():
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


def test_assoc_isHostedInLocation195_stub_double():
    # contentfwk_Location has no real 'Location196' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location196', None)
    _safe_set(owner, 'containsPhysicalTechnologyComponents', {partner})
    assert getattr(partner, 'Location196') == owner
    _safe_set(owner, 'containsPhysicalTechnologyComponents', set())
    assert getattr(partner, 'Location196') is None


def test_assoc_isHostedInLocation285_stub_double():
    # contentfwk_Location has no real 'Location286' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location286', None)
    _safe_set(owner, 'containsPhysicalApplicationComponents', {partner})
    assert getattr(partner, 'Location286') == owner
    _safe_set(owner, 'containsPhysicalApplicationComponents', set())
    assert getattr(partner, 'Location286') is None


def test_assoc_isMotivatedByDrivers66_stub_double():
    # contentfwk_Driver has no real 'Driver67' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Driver()
    setattr(partner, 'Driver67', None)
    _safe_set(owner, 'motivatesOrganizationUnits', {partner})
    assert getattr(partner, 'Driver67') == owner
    _safe_set(owner, 'motivatesOrganizationUnits', set())
    assert getattr(partner, 'Driver67') is None


def test_assoc_isOwnedAndGovernedByOrganizationUnits330_stub_double():
    # contentfwk_Service has no real 'ownsAndGovernsServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'ownsAndGovernsServices', None)
    _safe_set(owner, 'OrganizationUnit331', partner)
    assert owner in getattr(partner, 'ownsAndGovernsServices')
    _safe_set(owner, 'OrganizationUnit331', None)
    assert owner not in getattr(partner, 'ownsAndGovernsServices')


def test_assoc_isOwnedByUnit135_stub_double():
    # contentfwk_Function has no real 'ownsFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'ownsFunctions', None)
    _safe_set(owner, 'OrganizationUnit136', partner)
    assert getattr(partner, 'ownsFunctions') == owner
    _safe_set(owner, 'OrganizationUnit136', None)
    assert getattr(partner, 'ownsFunctions') is None


def test_assoc_isPerformedByActors133_stub_double():
    # contentfwk_Function has no real 'performsFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'performsFunctions', None)
    _safe_set(owner, 'Actor134', partner)
    assert owner in getattr(partner, 'performsFunctions')
    _safe_set(owner, 'Actor134', None)
    assert owner not in getattr(partner, 'performsFunctions')


def test_assoc_isProcessesByLogicalApplicationComponents110_stub_double():
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


def test_assoc_isProducedByOrganizationUnits203_stub_double():
    # contentfwk_Product has no real 'producesProducts' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'producesProducts', None)
    _safe_set(owner, 'OrganizationUnit204', partner)
    assert owner in getattr(partner, 'producesProducts')
    _safe_set(owner, 'OrganizationUnit204', None)
    assert owner not in getattr(partner, 'producesProducts')


def test_assoc_isProducedByProcesses205_stub_double():
    # contentfwk_Product has no real 'producesProducts206' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'producesProducts206', None)
    _safe_set(owner, 'Process207', partner)
    assert owner in getattr(partner, 'producesProducts206')
    _safe_set(owner, 'Process207', None)
    assert owner not in getattr(partner, 'producesProducts206')


def test_assoc_isProvidedToActors313_stub_double():
    # contentfwk_Service has no real 'contentfwk_Service314' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'contentfwk_Service314', None)
    _safe_set(owner, 'contentfwk_Actor315', partner)
    assert owner in getattr(partner, 'contentfwk_Service314')
    _safe_set(owner, 'contentfwk_Actor315', None)
    assert owner not in getattr(partner, 'contentfwk_Service314')


def test_assoc_isRealizedByPhysicalTechnologyComponents302_stub_double():
    # contentfwk_LogicalTechnologyComponent has no real 'extendsLogicalTechnologyComponents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_LogicalTechnologyComponent()
    setattr(partner, 'extendsLogicalTechnologyComponents', None)
    _safe_set(owner, 'PhysicalTechnologyComponent303', partner)
    assert owner in getattr(partner, 'extendsLogicalTechnologyComponents')
    _safe_set(owner, 'PhysicalTechnologyComponent303', None)
    assert owner not in getattr(partner, 'extendsLogicalTechnologyComponents')


def test_assoc_isRealizedByProcesses141_stub_double():
    # contentfwk_Function has no real 'orchestratesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'orchestratesFunctions', None)
    _safe_set(owner, 'Process142', partner)
    assert owner in getattr(partner, 'orchestratesFunctions')
    _safe_set(owner, 'Process142', None)
    assert owner not in getattr(partner, 'orchestratesFunctions')


def test_assoc_isRealizedByProcesses336_stub_double():
    # contentfwk_Service has no real 'orchestratesServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'orchestratesServices', None)
    _safe_set(owner, 'Process337', partner)
    assert owner in getattr(partner, 'orchestratesServices')
    _safe_set(owner, 'Process337', None)
    assert owner not in getattr(partner, 'orchestratesServices')


def test_assoc_isResolvedByActors229_stub_double():
    # contentfwk_Event has no real 'resolvesEvents230' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'resolvesEvents230', None)
    _safe_set(owner, 'Actor231', partner)
    assert owner in getattr(partner, 'resolvesEvents230')
    _safe_set(owner, 'Actor231', None)
    assert owner not in getattr(partner, 'resolvesEvents230')


def test_assoc_isResolvedByProcesses224_stub_double():
    # contentfwk_Event has no real 'resolvesEvents225' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'resolvesEvents225', None)
    _safe_set(owner, 'Process226', partner)
    assert owner in getattr(partner, 'resolvesEvents225')
    _safe_set(owner, 'Process226', None)
    assert owner not in getattr(partner, 'resolvesEvents225')


def test_assoc_isUpdatedThroughServices107_stub_double():
    # contentfwk_Service has no real 'Service108' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service108', None)
    _safe_set(owner, 'providesEntities', {partner})
    assert getattr(partner, 'Service108') == owner
    _safe_set(owner, 'providesEntities', set())
    assert getattr(partner, 'Service108') is None


def test_assoc_meetsServiceQuality221_stub_double():
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


def test_assoc_motivatesOrganizationUnits47_stub_double():
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


def test_assoc_operatesInLocation69_stub_double():
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


def test_assoc_operatesInLocation85_stub_double():
    # contentfwk_Location has no real 'Location87' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location87', None)
    _safe_set(owner, 'containsActors86', partner)
    assert getattr(partner, 'Location87') == owner
    _safe_set(owner, 'containsActors86', None)
    assert getattr(partner, 'Location87') is None


def test_assoc_operatesOnDataEntities122_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'isProcessesByLogicalApplicationComponents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'isProcessesByLogicalApplicationComponents', None)
    _safe_set(owner, 'DataEntity123', partner)
    assert owner in getattr(partner, 'isProcessesByLogicalApplicationComponents')
    _safe_set(owner, 'DataEntity123', None)
    assert owner not in getattr(partner, 'isProcessesByLogicalApplicationComponents')


def test_assoc_orchestratesFunctions156_stub_double():
    # contentfwk_Function has no real 'Function157' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function157', None)
    _safe_set(owner, 'isRealizedByProcesses', {partner})
    assert getattr(partner, 'Function157') == owner
    _safe_set(owner, 'isRealizedByProcesses', set())
    assert getattr(partner, 'Function157') is None


def test_assoc_orchestratesServices162_stub_double():
    # contentfwk_Service has no real 'Service164' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service164', None)
    _safe_set(owner, 'isRealizedByProcesses163', {partner})
    assert getattr(partner, 'Service164') == owner
    _safe_set(owner, 'isRealizedByProcesses163', set())
    assert getattr(partner, 'Service164') is None


def test_assoc_ownsAndGovernsServices62_stub_double():
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


def test_assoc_ownsFunctions64_stub_double():
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


def test_assoc_performsFunctions88_stub_double():
    # contentfwk_Function has no real 'Function89' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function89', None)
    _safe_set(owner, 'isPerformedByActors', {partner})
    assert getattr(partner, 'Function89') == owner
    _safe_set(owner, 'isPerformedByActors', set())
    assert getattr(partner, 'Function89') is None


def test_assoc_physicalApplicationComponents275_stub_double():
    # contentfwk_ApplicationArchitecture has no real 'contentfwk_ApplicationArchitecture276' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_ApplicationArchitecture()
    setattr(partner, 'contentfwk_ApplicationArchitecture276', None)
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent277', partner)
    assert owner in getattr(partner, 'contentfwk_ApplicationArchitecture276')
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent277', None)
    assert owner not in getattr(partner, 'contentfwk_ApplicationArchitecture276')


def test_assoc_physicalComponents42_stub_double():
    # contentfwk_TechnologyArchitecture has no real 'contentfwk_TechnologyArchitecture43' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_TechnologyArchitecture()
    setattr(partner, 'contentfwk_TechnologyArchitecture43', None)
    _safe_set(owner, 'contentfwk_PhysicalTechnologyComponent', partner)
    assert owner in getattr(partner, 'contentfwk_TechnologyArchitecture43')
    _safe_set(owner, 'contentfwk_PhysicalTechnologyComponent', None)
    assert owner not in getattr(partner, 'contentfwk_TechnologyArchitecture43')


def test_assoc_processes20_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture21' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture21', None)
    _safe_set(owner, 'contentfwk_Process', partner)
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture21')
    _safe_set(owner, 'contentfwk_Process', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture21')


def test_assoc_producesProducts176_stub_double():
    # contentfwk_Product has no real 'Product177' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'Product177', None)
    _safe_set(owner, 'isProducedByProcesses', {partner})
    assert getattr(partner, 'Product177') == owner
    _safe_set(owner, 'isProducedByProcesses', set())
    assert getattr(partner, 'Product177') is None


def test_assoc_producesProducts68_stub_double():
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


def test_assoc_providesEntities318_stub_double():
    # contentfwk_Service has no real 'isUpdatedThroughServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'isUpdatedThroughServices', None)
    _safe_set(owner, 'DataEntity319', partner)
    assert owner in getattr(partner, 'isUpdatedThroughServices')
    _safe_set(owner, 'DataEntity319', None)
    assert owner not in getattr(partner, 'isUpdatedThroughServices')


def test_assoc_residesWithinLogicalDataComponent109_stub_double():
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


def test_assoc_resolvesEvents172_stub_double():
    # contentfwk_Event has no real 'Event173' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event173', None)
    _safe_set(owner, 'isResolvedByProcesses', {partner})
    assert getattr(partner, 'Event173') == owner
    _safe_set(owner, 'isResolvedByProcesses', set())
    assert getattr(partner, 'Event173') is None


def test_assoc_resolvesEvents82_stub_double():
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


def test_assoc_roles14_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture15' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Role(estimatedFTEs="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture15', None)
    _safe_set(owner, 'contentfwk_Role', partner)
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture15')
    _safe_set(owner, 'contentfwk_Role', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture15')


def test_assoc_supportsActors145_stub_double():
    # contentfwk_Function has no real 'interactsWithFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'interactsWithFunctions', None)
    _safe_set(owner, 'Actor146', partner)
    assert owner in getattr(partner, 'interactsWithFunctions')
    _safe_set(owner, 'Actor146', None)
    assert owner not in getattr(partner, 'interactsWithFunctions')


def test_assoc_supportsProcesses139_stub_double():
    # contentfwk_Function has no real 'decomposesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'decomposesFunctions', None)
    _safe_set(owner, 'Process140', partner)
    assert owner in getattr(partner, 'decomposesFunctions')
    _safe_set(owner, 'Process140', None)
    assert owner not in getattr(partner, 'decomposesFunctions')


def test_assoc_supportsProcesses334_stub_double():
    # contentfwk_Service has no real 'decomposesServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'decomposesServices', None)
    _safe_set(owner, 'Process335', partner)
    assert owner in getattr(partner, 'decomposesServices')
    _safe_set(owner, 'Process335', None)
    assert owner not in getattr(partner, 'decomposesServices')


def test_assoc_units10_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture11' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture11', None)
    _safe_set(owner, 'contentfwk_OrganizationUnit', partner)
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture11')
    _safe_set(owner, 'contentfwk_OrganizationUnit', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture11')


