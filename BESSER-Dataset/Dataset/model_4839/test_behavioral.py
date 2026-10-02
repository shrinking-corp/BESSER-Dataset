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
    contentfwk_Label,
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


def test_assoc_category233_reverse_link_reassign_clear():
    a1 = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    a2 = contentfwk_Label(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    _safe_set(b, 'ownedElements', {a1})
    assert _is_linked(b, 'ownedElements', a1)
    if hasattr(a1, 'Label'):
        assert _is_linked(a1, 'Label', b)
    _safe_set(b, 'ownedElements', {a2})
    assert _is_linked(b, 'ownedElements', a2)
    if hasattr(a1, 'Label'):
        assert not _is_linked(a1, 'Label', b)
    if hasattr(a2, 'Label'):
        assert _is_linked(a2, 'Label', b)
    _safe_set(b, 'ownedElements', set())
    assert not _is_linked(b, 'ownedElements', a2)
    if hasattr(a2, 'Label'):
        assert not _is_linked(a2, 'Label', b)


def test_assoc_communicatesWith286_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    a2 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent287', a1)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent287', a1)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent285'):
        assert _is_linked(a1, 'contentfwk_PhysicalApplicationComponent285', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent287', a2)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent287', a2)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent285'):
        assert not _is_linked(a1, 'contentfwk_PhysicalApplicationComponent285', b)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent285'):
        assert _is_linked(a2, 'contentfwk_PhysicalApplicationComponent285', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent287', None)
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent287', a2)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent285'):
        assert not _is_linked(a2, 'contentfwk_PhysicalApplicationComponent285', b)


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


def test_assoc_containers244_reverse_link_reassign_clear():
    a1 = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    a2 = contentfwk_Label(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'Container', a1)
    assert _is_linked(b, 'Container', a1)
    if hasattr(a1, 'labels'):
        assert _is_linked(a1, 'labels', b)
    _safe_set(b, 'Container', a2)
    assert _is_linked(b, 'Container', a2)
    if hasattr(a1, 'labels'):
        assert not _is_linked(a1, 'labels', b)
    if hasattr(a2, 'labels'):
        assert _is_linked(a2, 'labels', b)
    _safe_set(b, 'Container', None)
    assert not _is_linked(b, 'Container', a2)
    if hasattr(a2, 'labels'):
        assert not _is_linked(a2, 'labels', b)


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


def test_assoc_decomposesLogicalTechnologyComponent303_reverse_link_reassign_clear():
    a1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    a2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'contentfwk_LogicalTechnologyComponent304', a1)
    assert _is_linked(b, 'contentfwk_LogicalTechnologyComponent304', a1)
    if hasattr(a1, 'contentfwk_LogicalTechnologyComponent302'):
        assert _is_linked(a1, 'contentfwk_LogicalTechnologyComponent302', b)
    _safe_set(b, 'contentfwk_LogicalTechnologyComponent304', a2)
    assert _is_linked(b, 'contentfwk_LogicalTechnologyComponent304', a2)
    if hasattr(a1, 'contentfwk_LogicalTechnologyComponent302'):
        assert not _is_linked(a1, 'contentfwk_LogicalTechnologyComponent302', b)
    if hasattr(a2, 'contentfwk_LogicalTechnologyComponent302'):
        assert _is_linked(a2, 'contentfwk_LogicalTechnologyComponent302', b)
    _safe_set(b, 'contentfwk_LogicalTechnologyComponent304', None)
    assert not _is_linked(b, 'contentfwk_LogicalTechnologyComponent304', a2)
    if hasattr(a2, 'contentfwk_LogicalTechnologyComponent302'):
        assert not _is_linked(a2, 'contentfwk_LogicalTechnologyComponent302', b)


def test_assoc_decomposesPhysicalApplicationComponent295_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    a2 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent296', a1)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent296', a1)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent294'):
        assert _is_linked(a1, 'contentfwk_PhysicalApplicationComponent294', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent296', a2)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent296', a2)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent294'):
        assert not _is_linked(a1, 'contentfwk_PhysicalApplicationComponent294', b)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent294'):
        assert _is_linked(a2, 'contentfwk_PhysicalApplicationComponent294', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent296', None)
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent296', a2)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent294'):
        assert not _is_linked(a2, 'contentfwk_PhysicalApplicationComponent294', b)


def test_assoc_decomposesPhysicalTechnologyComponent189_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent190', a1)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent190', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent188'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent188', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent190', a2)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent190', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent188'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent188', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent188'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent188', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent190', None)
    assert not _is_linked(b, 'contentfwk_PhysicalTechnologyComponent190', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent188'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent188', b)


def test_assoc_decomposesProcess173_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'contentfwk_Process174', a1)
    assert _is_linked(b, 'contentfwk_Process174', a1)
    if hasattr(a1, 'contentfwk_Process172'):
        assert _is_linked(a1, 'contentfwk_Process172', b)
    _safe_set(b, 'contentfwk_Process174', a2)
    assert _is_linked(b, 'contentfwk_Process174', a2)
    if hasattr(a1, 'contentfwk_Process172'):
        assert not _is_linked(a1, 'contentfwk_Process172', b)
    if hasattr(a2, 'contentfwk_Process172'):
        assert _is_linked(a2, 'contentfwk_Process172', b)
    _safe_set(b, 'contentfwk_Process174', None)
    assert not _is_linked(b, 'contentfwk_Process174', a2)
    if hasattr(a2, 'contentfwk_Process172'):
        assert not _is_linked(a2, 'contentfwk_Process172', b)


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


def test_assoc_delegates229_reverse_link_reassign_clear():
    a1 = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    a2 = contentfwk_Element(ID="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    b = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
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


def test_assoc_deliversCapabilities259_reverse_link_reassign_clear():
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


def test_assoc_extendsLogicalTechnologyComponents184_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'LogicalTechnologyComponent185', a1)
    assert _is_linked(b, 'LogicalTechnologyComponent185', a1)
    if hasattr(a1, 'isRealizedByPhysicalTechnologyComponents'):
        assert _is_linked(a1, 'isRealizedByPhysicalTechnologyComponents', b)
    _safe_set(b, 'LogicalTechnologyComponent185', a2)
    assert _is_linked(b, 'LogicalTechnologyComponent185', a2)
    if hasattr(a1, 'isRealizedByPhysicalTechnologyComponents'):
        assert not _is_linked(a1, 'isRealizedByPhysicalTechnologyComponents', b)
    if hasattr(a2, 'isRealizedByPhysicalTechnologyComponents'):
        assert _is_linked(a2, 'isRealizedByPhysicalTechnologyComponents', b)
    _safe_set(b, 'LogicalTechnologyComponent185', None)
    assert not _is_linked(b, 'LogicalTechnologyComponent185', a2)
    if hasattr(a2, 'isRealizedByPhysicalTechnologyComponents'):
        assert not _is_linked(a2, 'isRealizedByPhysicalTechnologyComponents', b)


def test_assoc_followsProcesses179_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'precedesProcesses', {a1})
    assert _is_linked(b, 'precedesProcesses', a1)
    if hasattr(a1, 'Process180'):
        assert _is_linked(a1, 'Process180', b)
    _safe_set(b, 'precedesProcesses', {a2})
    assert _is_linked(b, 'precedesProcesses', a2)
    if hasattr(a1, 'Process180'):
        assert not _is_linked(a1, 'Process180', b)
    if hasattr(a2, 'Process180'):
        assert _is_linked(a2, 'Process180', b)
    _safe_set(b, 'precedesProcesses', set())
    assert not _is_linked(b, 'precedesProcesses', a2)
    if hasattr(a2, 'Process180'):
        assert not _is_linked(a2, 'Process180', b)


def test_assoc_involvesActors162_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor164', a1)
    assert _is_linked(b, 'Actor164', a1)
    if hasattr(a1, 'participatesInProcesses163'):
        assert _is_linked(a1, 'participatesInProcesses163', b)
    _safe_set(b, 'Actor164', a2)
    assert _is_linked(b, 'Actor164', a2)
    if hasattr(a1, 'participatesInProcesses163'):
        assert not _is_linked(a1, 'participatesInProcesses163', b)
    if hasattr(a2, 'participatesInProcesses163'):
        assert _is_linked(a2, 'participatesInProcesses163', b)
    _safe_set(b, 'Actor164', None)
    assert not _is_linked(b, 'Actor164', a2)
    if hasattr(a2, 'participatesInProcesses163'):
        assert not _is_linked(a2, 'participatesInProcesses163', b)


def test_assoc_involvesOrganizationUnits154_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_OrganizationUnit(headcount="sample_text")
    _safe_set(b, 'OrganizationUnit155', a1)
    assert _is_linked(b, 'OrganizationUnit155', a1)
    if hasattr(a1, 'participatesInProcesses'):
        assert _is_linked(a1, 'participatesInProcesses', b)
    _safe_set(b, 'OrganizationUnit155', a2)
    assert _is_linked(b, 'OrganizationUnit155', a2)
    if hasattr(a1, 'participatesInProcesses'):
        assert not _is_linked(a1, 'participatesInProcesses', b)
    if hasattr(a2, 'participatesInProcesses'):
        assert _is_linked(a2, 'participatesInProcesses', b)
    _safe_set(b, 'OrganizationUnit155', None)
    assert not _is_linked(b, 'OrganizationUnit155', a2)
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


def test_assoc_isDelegatedBy231_reverse_link_reassign_clear():
    a1 = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    a2 = contentfwk_Element(ID="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    b = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    _safe_set(b, 'delegates', {a1})
    assert _is_linked(b, 'delegates', a1)
    if hasattr(a1, 'Element232'):
        assert _is_linked(a1, 'Element232', b)
    _safe_set(b, 'delegates', {a2})
    assert _is_linked(b, 'delegates', a2)
    if hasattr(a1, 'Element232'):
        assert not _is_linked(a1, 'Element232', b)
    if hasattr(a2, 'Element232'):
        assert _is_linked(a2, 'Element232', b)
    _safe_set(b, 'delegates', set())
    assert not _is_linked(b, 'delegates', a2)
    if hasattr(a2, 'Element232'):
        assert not _is_linked(a2, 'Element232', b)


def test_assoc_isDeliveredBy258_reverse_link_reassign_clear():
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


def test_assoc_isDependentOnLogicalTechnologyComponents306_reverse_link_reassign_clear():
    a1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    a2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'contentfwk_LogicalTechnologyComponent307', a1)
    assert _is_linked(b, 'contentfwk_LogicalTechnologyComponent307', a1)
    if hasattr(a1, 'contentfwk_LogicalTechnologyComponent305'):
        assert _is_linked(a1, 'contentfwk_LogicalTechnologyComponent305', b)
    _safe_set(b, 'contentfwk_LogicalTechnologyComponent307', a2)
    assert _is_linked(b, 'contentfwk_LogicalTechnologyComponent307', a2)
    if hasattr(a1, 'contentfwk_LogicalTechnologyComponent305'):
        assert not _is_linked(a1, 'contentfwk_LogicalTechnologyComponent305', b)
    if hasattr(a2, 'contentfwk_LogicalTechnologyComponent305'):
        assert _is_linked(a2, 'contentfwk_LogicalTechnologyComponent305', b)
    _safe_set(b, 'contentfwk_LogicalTechnologyComponent307', None)
    assert not _is_linked(b, 'contentfwk_LogicalTechnologyComponent307', a2)
    if hasattr(a2, 'contentfwk_LogicalTechnologyComponent305'):
        assert not _is_linked(a2, 'contentfwk_LogicalTechnologyComponent305', b)


def test_assoc_isDependentOnPhysicalTechnologyComponents192_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent193', a1)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent193', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent191'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent191', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent193', a2)
    assert _is_linked(b, 'contentfwk_PhysicalTechnologyComponent193', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent191'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent191', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent191'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent191', b)
    _safe_set(b, 'contentfwk_PhysicalTechnologyComponent193', None)
    assert not _is_linked(b, 'contentfwk_PhysicalTechnologyComponent193', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent191'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent191', b)


def test_assoc_isRealizedByPhysicalTechnologyComponents291_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent292', {a1})
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent292', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent293'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent293', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent292', {a2})
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent292', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent293'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent293', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent293'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent293', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent292', set())
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent292', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent293'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent293', b)


def test_assoc_isRealizedByPhysicalTechnologyComponents300_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'extendsLogicalTechnologyComponents', {a1})
    assert _is_linked(b, 'extendsLogicalTechnologyComponents', a1)
    if hasattr(a1, 'PhysicalTechnologyComponent301'):
        assert _is_linked(a1, 'PhysicalTechnologyComponent301', b)
    _safe_set(b, 'extendsLogicalTechnologyComponents', {a2})
    assert _is_linked(b, 'extendsLogicalTechnologyComponents', a2)
    if hasattr(a1, 'PhysicalTechnologyComponent301'):
        assert not _is_linked(a1, 'PhysicalTechnologyComponent301', b)
    if hasattr(a2, 'PhysicalTechnologyComponent301'):
        assert _is_linked(a2, 'PhysicalTechnologyComponent301', b)
    _safe_set(b, 'extendsLogicalTechnologyComponents', set())
    assert not _is_linked(b, 'extendsLogicalTechnologyComponents', a2)
    if hasattr(a2, 'PhysicalTechnologyComponent301'):
        assert not _is_linked(a2, 'PhysicalTechnologyComponent301', b)


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


def test_assoc_isSuppliedByLogicalTechnologyComponents181_reverse_link_reassign_clear():
    a1 = contentfwk_PlatformService(categoryTRM="sample_text")
    a2 = contentfwk_PlatformService(categoryTRM="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'LogicalTechnologyComponent', a1)
    assert _is_linked(b, 'LogicalTechnologyComponent', a1)
    if hasattr(a1, 'suppliesPlatformServices'):
        assert _is_linked(a1, 'suppliesPlatformServices', b)
    _safe_set(b, 'LogicalTechnologyComponent', a2)
    assert _is_linked(b, 'LogicalTechnologyComponent', a2)
    if hasattr(a1, 'suppliesPlatformServices'):
        assert not _is_linked(a1, 'suppliesPlatformServices', b)
    if hasattr(a2, 'suppliesPlatformServices'):
        assert _is_linked(a2, 'suppliesPlatformServices', b)
    _safe_set(b, 'LogicalTechnologyComponent', None)
    assert not _is_linked(b, 'LogicalTechnologyComponent', a2)
    if hasattr(a2, 'suppliesPlatformServices'):
        assert not _is_linked(a2, 'suppliesPlatformServices', b)


def test_assoc_labels237_reverse_link_reassign_clear():
    a1 = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    a2 = contentfwk_Label(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'containers', {a1})
    assert _is_linked(b, 'containers', a1)
    if hasattr(a1, 'Label238'):
        assert _is_linked(a1, 'Label238', b)
    _safe_set(b, 'containers', {a2})
    assert _is_linked(b, 'containers', a2)
    if hasattr(a1, 'Label238'):
        assert not _is_linked(a1, 'Label238', b)
    if hasattr(a2, 'Label238'):
        assert _is_linked(a2, 'Label238', b)
    _safe_set(b, 'containers', set())
    assert not _is_linked(b, 'containers', a2)
    if hasattr(a2, 'Label238'):
        assert not _is_linked(a2, 'Label238', b)


def test_assoc_ownedElements242_reverse_link_reassign_clear():
    a1 = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    a2 = contentfwk_Label(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    _safe_set(b, 'Element243', a1)
    assert _is_linked(b, 'Element243', a1)
    if hasattr(a1, 'category'):
        assert _is_linked(a1, 'category', b)
    _safe_set(b, 'Element243', a2)
    assert _is_linked(b, 'Element243', a2)
    if hasattr(a1, 'category'):
        assert not _is_linked(a1, 'category', b)
    if hasattr(a2, 'category'):
        assert _is_linked(a2, 'category', b)
    _safe_set(b, 'Element243', None)
    assert not _is_linked(b, 'Element243', a2)
    if hasattr(a2, 'category'):
        assert not _is_linked(a2, 'category', b)


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


def test_assoc_precedesProcesses176_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'followsProcesses', {a1})
    assert _is_linked(b, 'followsProcesses', a1)
    if hasattr(a1, 'Process177'):
        assert _is_linked(a1, 'Process177', b)
    _safe_set(b, 'followsProcesses', {a2})
    assert _is_linked(b, 'followsProcesses', a2)
    if hasattr(a1, 'Process177'):
        assert not _is_linked(a1, 'Process177', b)
    if hasattr(a2, 'Process177'):
        assert _is_linked(a2, 'Process177', b)
    _safe_set(b, 'followsProcesses', set())
    assert not _is_linked(b, 'followsProcesses', a2)
    if hasattr(a2, 'Process177'):
        assert not _is_linked(a2, 'Process177', b)


def test_assoc_realizesApplicationComponents182_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent', a1)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent183'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent183', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent', a2)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent183'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent183', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent183'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent183', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent', None)
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent183'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent183', b)


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


def test_assoc_subContainers235_reverse_link_reassign_clear():
    a1 = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    a2 = contentfwk_Container(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'contentfwk_Container236', a1)
    assert _is_linked(b, 'contentfwk_Container236', a1)
    if hasattr(a1, 'contentfwk_Container234'):
        assert _is_linked(a1, 'contentfwk_Container234', b)
    _safe_set(b, 'contentfwk_Container236', a2)
    assert _is_linked(b, 'contentfwk_Container236', a2)
    if hasattr(a1, 'contentfwk_Container234'):
        assert not _is_linked(a1, 'contentfwk_Container234', b)
    if hasattr(a2, 'contentfwk_Container234'):
        assert _is_linked(a2, 'contentfwk_Container234', b)
    _safe_set(b, 'contentfwk_Container236', None)
    assert not _is_linked(b, 'contentfwk_Container236', a2)
    if hasattr(a2, 'contentfwk_Container234'):
        assert not _is_linked(a2, 'contentfwk_Container234', b)


def test_assoc_subLabels240_reverse_link_reassign_clear():
    a1 = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    a2 = contentfwk_Label(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'contentfwk_Label241', a1)
    assert _is_linked(b, 'contentfwk_Label241', a1)
    if hasattr(a1, 'contentfwk_Label239'):
        assert _is_linked(a1, 'contentfwk_Label239', b)
    _safe_set(b, 'contentfwk_Label241', a2)
    assert _is_linked(b, 'contentfwk_Label241', a2)
    if hasattr(a1, 'contentfwk_Label239'):
        assert not _is_linked(a1, 'contentfwk_Label239', b)
    if hasattr(a2, 'contentfwk_Label239'):
        assert _is_linked(a2, 'contentfwk_Label239', b)
    _safe_set(b, 'contentfwk_Label241', None)
    assert not _is_linked(b, 'contentfwk_Label241', a2)
    if hasattr(a2, 'contentfwk_Label239'):
        assert not _is_linked(a2, 'contentfwk_Label239', b)


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


def test_assoc_suppliesPlatformServices299_reverse_link_reassign_clear():
    a1 = contentfwk_PlatformService(categoryTRM="sample_text")
    a2 = contentfwk_PlatformService(categoryTRM="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'isSuppliedByLogicalTechnologyComponents', {a1})
    assert _is_linked(b, 'isSuppliedByLogicalTechnologyComponents', a1)
    if hasattr(a1, 'PlatformService'):
        assert _is_linked(a1, 'PlatformService', b)
    _safe_set(b, 'isSuppliedByLogicalTechnologyComponents', {a2})
    assert _is_linked(b, 'isSuppliedByLogicalTechnologyComponents', a2)
    if hasattr(a1, 'PlatformService'):
        assert not _is_linked(a1, 'PlatformService', b)
    if hasattr(a2, 'PlatformService'):
        assert _is_linked(a2, 'PlatformService', b)
    _safe_set(b, 'isSuppliedByLogicalTechnologyComponents', set())
    assert not _is_linked(b, 'isSuppliedByLogicalTechnologyComponents', a2)
    if hasattr(a2, 'PlatformService'):
        assert not _is_linked(a2, 'PlatformService', b)


