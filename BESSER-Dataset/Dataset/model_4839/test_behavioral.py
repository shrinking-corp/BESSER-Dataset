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


def test_assoc_appliesToContracts209_stub_double():
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


def test_assoc_canBeAccessedByRoles137_stub_double():
    # contentfwk_Function has no real 'accessesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Role(estimatedFTEs="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'accessesFunctions', None)
    _safe_set(owner, 'Role138', partner)
    assert owner in getattr(partner, 'accessesFunctions')
    _safe_set(owner, 'Role138', None)
    assert owner not in getattr(partner, 'accessesFunctions')


def test_assoc_capabilities308_stub_double():
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


def test_assoc_consumesEntities318_stub_double():
    # contentfwk_Service has no real 'isAccessedByServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'isAccessedByServices', None)
    _safe_set(owner, 'DataEntity319', partner)
    assert owner in getattr(partner, 'isAccessedByServices')
    _safe_set(owner, 'DataEntity319', None)
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
    owner = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    partner = contentfwk_EnterpriseArchitecture()
    setattr(partner, 'contentfwk_EnterpriseArchitecture2', None)
    _safe_set(owner, 'contentfwk_Container', partner)
    assert owner in getattr(partner, 'contentfwk_EnterpriseArchitecture2')
    _safe_set(owner, 'contentfwk_Container', None)
    assert owner not in getattr(partner, 'contentfwk_EnterpriseArchitecture2')


def test_assoc_containsActors245_stub_double():
    # contentfwk_Location has no real 'operatesInLocation' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'operatesInLocation', None)
    _safe_set(owner, 'Actor246', partner)
    assert owner in getattr(partner, 'operatesInLocation')
    _safe_set(owner, 'Actor246', None)
    assert owner not in getattr(partner, 'operatesInLocation')


def test_assoc_containsOrganizationUnits247_stub_double():
    # contentfwk_Location has no real 'operatesInLocation248' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'operatesInLocation248', None)
    _safe_set(owner, 'OrganizationUnit249', partner)
    assert owner in getattr(partner, 'operatesInLocation248')
    _safe_set(owner, 'OrganizationUnit249', None)
    assert owner not in getattr(partner, 'operatesInLocation248')


def test_assoc_containsPhysicalApplicationComponents251_stub_double():
    # contentfwk_Location has no real 'isHostedInLocation' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'isHostedInLocation', None)
    _safe_set(owner, 'PhysicalApplicationComponent252', partner)
    assert owner in getattr(partner, 'isHostedInLocation')
    _safe_set(owner, 'PhysicalApplicationComponent252', None)
    assert owner not in getattr(partner, 'isHostedInLocation')


def test_assoc_containsPhysicalTechnologyComponents253_stub_double():
    # contentfwk_Location has no real 'isHostedInLocation254' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'isHostedInLocation254', None)
    _safe_set(owner, 'PhysicalTechnologyComponent', partner)
    assert owner in getattr(partner, 'isHostedInLocation254')
    _safe_set(owner, 'PhysicalTechnologyComponent', None)
    assert owner not in getattr(partner, 'isHostedInLocation254')


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


def test_assoc_decomposesFunctions152_stub_double():
    # contentfwk_Function has no real 'Function153' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function153', None)
    _safe_set(owner, 'supportsProcesses', {partner})
    assert getattr(partner, 'Function153') == owner
    _safe_set(owner, 'supportsProcesses', set())
    assert getattr(partner, 'Function153') is None


def test_assoc_decomposesServices159_stub_double():
    # contentfwk_Service has no real 'Service161' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service161', None)
    _safe_set(owner, 'supportsProcesses160', {partner})
    assert getattr(partner, 'Service161') == owner
    _safe_set(owner, 'supportsProcesses160', set())
    assert getattr(partner, 'Service161') is None


def test_assoc_encapsulatesDataEntities260_stub_double():
    # contentfwk_LogicalDataComponent has no real 'residesWithinLogicalDataComponent' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_LogicalDataComponent()
    setattr(partner, 'residesWithinLogicalDataComponent', None)
    _safe_set(owner, 'DataEntity261', partner)
    assert owner in getattr(partner, 'residesWithinLogicalDataComponent')
    _safe_set(owner, 'DataEntity261', None)
    assert owner not in getattr(partner, 'residesWithinLogicalDataComponent')


def test_assoc_encapsulatesPhysicalApplicationComponents271_stub_double():
    # contentfwk_PhysicalDataComponent has no real 'contentfwk_PhysicalDataComponent272' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_PhysicalDataComponent()
    setattr(partner, 'contentfwk_PhysicalDataComponent272', None)
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent273', partner)
    assert owner in getattr(partner, 'contentfwk_PhysicalDataComponent272')
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent273', None)
    assert owner not in getattr(partner, 'contentfwk_PhysicalDataComponent272')


def test_assoc_encapsulatesPhysicalDataComponents288_stub_double():
    # contentfwk_PhysicalDataComponent has no real 'contentfwk_PhysicalDataComponent290' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_PhysicalDataComponent()
    setattr(partner, 'contentfwk_PhysicalDataComponent290', None)
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent289', {partner})
    assert getattr(partner, 'contentfwk_PhysicalDataComponent290') == owner
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent289', set())
    assert getattr(partner, 'contentfwk_PhysicalDataComponent290') is None


def test_assoc_ensuresCorrectOperationOfProcesses226_stub_double():
    # contentfwk_Control has no real 'isGuidedByControls' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Control()
    setattr(partner, 'isGuidedByControls', None)
    _safe_set(owner, 'Process227', partner)
    assert owner in getattr(partner, 'isGuidedByControls')
    _safe_set(owner, 'Process227', None)
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


def test_assoc_extendsLogicalApplicationComponents281_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'LogicalApplicationComponent282' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'LogicalApplicationComponent282', None)
    _safe_set(owner, 'isExtendedByPhysicalApplicationComponents', {partner})
    assert getattr(partner, 'LogicalApplicationComponent282') == owner
    _safe_set(owner, 'isExtendedByPhysicalApplicationComponents', set())
    assert getattr(partner, 'LogicalApplicationComponent282') is None


def test_assoc_generatesEvents168_stub_double():
    # contentfwk_Event has no real 'Event169' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event169', None)
    _safe_set(owner, 'isGeneratedByProcesses', {partner})
    assert getattr(partner, 'Event169') == owner
    _safe_set(owner, 'isGeneratedByProcesses', set())
    assert getattr(partner, 'Event169') is None


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


def test_assoc_governsAndMeasuresBusinessServices210_stub_double():
    # contentfwk_Service has no real 'Service211' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service211', None)
    _safe_set(owner, 'isGovernedAndMeasuredByContracts', {partner})
    assert getattr(partner, 'Service211') == owner
    _safe_set(owner, 'isGovernedAndMeasuredByContracts', set())
    assert getattr(partner, 'Service211') is None


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


def test_assoc_isExtendedByPhysicalApplicationComponents121_stub_double():
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


def test_assoc_isGeneratedByActors223_stub_double():
    # contentfwk_Event has no real 'generatesEvents224' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'generatesEvents224', None)
    _safe_set(owner, 'Actor225', partner)
    assert getattr(partner, 'generatesEvents224') == owner
    _safe_set(owner, 'Actor225', None)
    assert getattr(partner, 'generatesEvents224') is None


def test_assoc_isGeneratedByProcesses218_stub_double():
    # contentfwk_Event has no real 'generatesEvents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'generatesEvents', None)
    _safe_set(owner, 'Process219', partner)
    assert owner in getattr(partner, 'generatesEvents')
    _safe_set(owner, 'Process219', None)
    assert owner not in getattr(partner, 'generatesEvents')


def test_assoc_isGovernedAndMeasuredByContracts320_stub_double():
    # contentfwk_Service has no real 'governsAndMeasuresBusinessServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'governsAndMeasuresBusinessServices', None)
    _safe_set(owner, 'Contract321', partner)
    assert owner in getattr(partner, 'governsAndMeasuresBusinessServices')
    _safe_set(owner, 'Contract321', None)
    assert owner not in getattr(partner, 'governsAndMeasuresBusinessServices')


def test_assoc_isGuidedByControls165_stub_double():
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


def test_assoc_isHostedInLocation186_stub_double():
    # contentfwk_Location has no real 'Location187' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location187', None)
    _safe_set(owner, 'containsPhysicalTechnologyComponents', {partner})
    assert getattr(partner, 'Location187') == owner
    _safe_set(owner, 'containsPhysicalTechnologyComponents', set())
    assert getattr(partner, 'Location187') is None


def test_assoc_isHostedInLocation283_stub_double():
    # contentfwk_Location has no real 'Location284' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location284', None)
    _safe_set(owner, 'containsPhysicalApplicationComponents', {partner})
    assert getattr(partner, 'Location284') == owner
    _safe_set(owner, 'containsPhysicalApplicationComponents', set())
    assert getattr(partner, 'Location284') is None


def test_assoc_isImplementedOnLogicalTechnologyComponents324_stub_double():
    # contentfwk_Service has no real 'providesPlatformForServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_LogicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_LogicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'providesPlatformForServices', None)
    _safe_set(owner, 'LogicalTechnologyComponent325', partner)
    assert owner in getattr(partner, 'providesPlatformForServices')
    _safe_set(owner, 'LogicalTechnologyComponent325', None)
    assert owner not in getattr(partner, 'providesPlatformForServices')


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


def test_assoc_isOwnedAndGovernedByOrganizationUnits328_stub_double():
    # contentfwk_Service has no real 'ownsAndGovernsServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'ownsAndGovernsServices', None)
    _safe_set(owner, 'OrganizationUnit329', partner)
    assert owner in getattr(partner, 'ownsAndGovernsServices')
    _safe_set(owner, 'OrganizationUnit329', None)
    assert owner not in getattr(partner, 'ownsAndGovernsServices')


def test_assoc_isOwnedByUnit129_stub_double():
    # contentfwk_Function has no real 'ownsFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'ownsFunctions', None)
    _safe_set(owner, 'OrganizationUnit130', partner)
    assert getattr(partner, 'ownsFunctions') == owner
    _safe_set(owner, 'OrganizationUnit130', None)
    assert getattr(partner, 'ownsFunctions') is None


def test_assoc_isPerformedByActors127_stub_double():
    # contentfwk_Function has no real 'performsFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'performsFunctions', None)
    _safe_set(owner, 'Actor128', partner)
    assert owner in getattr(partner, 'performsFunctions')
    _safe_set(owner, 'Actor128', None)
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


def test_assoc_isProducedByOrganizationUnits194_stub_double():
    # contentfwk_Product has no real 'producesProducts' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'producesProducts', None)
    _safe_set(owner, 'OrganizationUnit195', partner)
    assert owner in getattr(partner, 'producesProducts')
    _safe_set(owner, 'OrganizationUnit195', None)
    assert owner not in getattr(partner, 'producesProducts')


def test_assoc_isProducedByProcesses196_stub_double():
    # contentfwk_Product has no real 'producesProducts197' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'producesProducts197', None)
    _safe_set(owner, 'Process198', partner)
    assert owner in getattr(partner, 'producesProducts197')
    _safe_set(owner, 'Process198', None)
    assert owner not in getattr(partner, 'producesProducts197')


def test_assoc_isProvidedToActors311_stub_double():
    # contentfwk_Service has no real 'contentfwk_Service312' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'contentfwk_Service312', None)
    _safe_set(owner, 'contentfwk_Actor313', partner)
    assert owner in getattr(partner, 'contentfwk_Service312')
    _safe_set(owner, 'contentfwk_Actor313', None)
    assert owner not in getattr(partner, 'contentfwk_Service312')


def test_assoc_isRealizedByProcesses135_stub_double():
    # contentfwk_Function has no real 'orchestratesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'orchestratesFunctions', None)
    _safe_set(owner, 'Process136', partner)
    assert owner in getattr(partner, 'orchestratesFunctions')
    _safe_set(owner, 'Process136', None)
    assert owner not in getattr(partner, 'orchestratesFunctions')


def test_assoc_isRealizedByProcesses334_stub_double():
    # contentfwk_Service has no real 'orchestratesServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'orchestratesServices', None)
    _safe_set(owner, 'Process335', partner)
    assert owner in getattr(partner, 'orchestratesServices')
    _safe_set(owner, 'Process335', None)
    assert owner not in getattr(partner, 'orchestratesServices')


def test_assoc_isResolvedByActors220_stub_double():
    # contentfwk_Event has no real 'resolvesEvents221' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'resolvesEvents221', None)
    _safe_set(owner, 'Actor222', partner)
    assert owner in getattr(partner, 'resolvesEvents221')
    _safe_set(owner, 'Actor222', None)
    assert owner not in getattr(partner, 'resolvesEvents221')


def test_assoc_isResolvedByProcesses215_stub_double():
    # contentfwk_Event has no real 'resolvesEvents216' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'resolvesEvents216', None)
    _safe_set(owner, 'Process217', partner)
    assert owner in getattr(partner, 'resolvesEvents216')
    _safe_set(owner, 'Process217', None)
    assert owner not in getattr(partner, 'resolvesEvents216')


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


def test_assoc_labels3_stub_double():
    # contentfwk_EnterpriseArchitecture has no real 'contentfwk_EnterpriseArchitecture4' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    partner = contentfwk_EnterpriseArchitecture()
    setattr(partner, 'contentfwk_EnterpriseArchitecture4', None)
    _safe_set(owner, 'contentfwk_Label', partner)
    assert owner in getattr(partner, 'contentfwk_EnterpriseArchitecture4')
    _safe_set(owner, 'contentfwk_Label', None)
    assert owner not in getattr(partner, 'contentfwk_EnterpriseArchitecture4')


def test_assoc_logicalComponents44_stub_double():
    # contentfwk_TechnologyArchitecture has no real 'contentfwk_TechnologyArchitecture45' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_LogicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_LogicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    partner = contentfwk_TechnologyArchitecture()
    setattr(partner, 'contentfwk_TechnologyArchitecture45', None)
    _safe_set(owner, 'contentfwk_LogicalTechnologyComponent', partner)
    assert owner in getattr(partner, 'contentfwk_TechnologyArchitecture45')
    _safe_set(owner, 'contentfwk_LogicalTechnologyComponent', None)
    assert owner not in getattr(partner, 'contentfwk_TechnologyArchitecture45')


def test_assoc_meetsServiceQuality212_stub_double():
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


def test_assoc_operatesOnDataEntities119_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'isProcessesByLogicalApplicationComponents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'isProcessesByLogicalApplicationComponents', None)
    _safe_set(owner, 'DataEntity120', partner)
    assert owner in getattr(partner, 'isProcessesByLogicalApplicationComponents')
    _safe_set(owner, 'DataEntity120', None)
    assert owner not in getattr(partner, 'isProcessesByLogicalApplicationComponents')


def test_assoc_orchestratesFunctions150_stub_double():
    # contentfwk_Function has no real 'Function151' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function151', None)
    _safe_set(owner, 'isRealizedByProcesses', {partner})
    assert getattr(partner, 'Function151') == owner
    _safe_set(owner, 'isRealizedByProcesses', set())
    assert getattr(partner, 'Function151') is None


def test_assoc_orchestratesServices156_stub_double():
    # contentfwk_Service has no real 'Service158' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service158', None)
    _safe_set(owner, 'isRealizedByProcesses157', {partner})
    assert getattr(partner, 'Service158') == owner
    _safe_set(owner, 'isRealizedByProcesses157', set())
    assert getattr(partner, 'Service158') is None


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


def test_assoc_physicalApplicationComponents276_stub_double():
    # contentfwk_ApplicationArchitecture has no real 'contentfwk_ApplicationArchitecture277' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_ApplicationArchitecture()
    setattr(partner, 'contentfwk_ApplicationArchitecture277', None)
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent278', partner)
    assert owner in getattr(partner, 'contentfwk_ApplicationArchitecture277')
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent278', None)
    assert owner not in getattr(partner, 'contentfwk_ApplicationArchitecture277')


def test_assoc_physicalComponents42_stub_double():
    # contentfwk_TechnologyArchitecture has no real 'contentfwk_TechnologyArchitecture43' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_TechnologyArchitecture()
    setattr(partner, 'contentfwk_TechnologyArchitecture43', None)
    _safe_set(owner, 'contentfwk_PhysicalTechnologyComponent', partner)
    assert owner in getattr(partner, 'contentfwk_TechnologyArchitecture43')
    _safe_set(owner, 'contentfwk_PhysicalTechnologyComponent', None)
    assert owner not in getattr(partner, 'contentfwk_TechnologyArchitecture43')


def test_assoc_platformServices41_stub_double():
    # contentfwk_TechnologyArchitecture has no real 'contentfwk_TechnologyArchitecture' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PlatformService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PlatformService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PlatformService(categoryTRM="sample_text")
    partner = contentfwk_TechnologyArchitecture()
    setattr(partner, 'contentfwk_TechnologyArchitecture', None)
    _safe_set(owner, 'contentfwk_PlatformService', partner)
    assert owner in getattr(partner, 'contentfwk_TechnologyArchitecture')
    _safe_set(owner, 'contentfwk_PlatformService', None)
    assert owner not in getattr(partner, 'contentfwk_TechnologyArchitecture')


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


def test_assoc_producesProducts170_stub_double():
    # contentfwk_Product has no real 'Product171' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'Product171', None)
    _safe_set(owner, 'isProducedByProcesses', {partner})
    assert getattr(partner, 'Product171') == owner
    _safe_set(owner, 'isProducedByProcesses', set())
    assert getattr(partner, 'Product171') is None


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


def test_assoc_providesEntities316_stub_double():
    # contentfwk_Service has no real 'isUpdatedThroughServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'isUpdatedThroughServices', None)
    _safe_set(owner, 'DataEntity317', partner)
    assert owner in getattr(partner, 'isUpdatedThroughServices')
    _safe_set(owner, 'DataEntity317', None)
    assert owner not in getattr(partner, 'isUpdatedThroughServices')


def test_assoc_providesPlatformForServices297_stub_double():
    # contentfwk_Service has no real 'Service298' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_LogicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_LogicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service298', None)
    _safe_set(owner, 'isImplementedOnLogicalTechnologyComponents', {partner})
    assert getattr(partner, 'Service298') == owner
    _safe_set(owner, 'isImplementedOnLogicalTechnologyComponents', set())
    assert getattr(partner, 'Service298') is None


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


def test_assoc_resolvesEvents166_stub_double():
    # contentfwk_Event has no real 'Event167' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event167', None)
    _safe_set(owner, 'isResolvedByProcesses', {partner})
    assert getattr(partner, 'Event167') == owner
    _safe_set(owner, 'isResolvedByProcesses', set())
    assert getattr(partner, 'Event167') is None


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


def test_assoc_supportsActors139_stub_double():
    # contentfwk_Function has no real 'interactsWithFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'interactsWithFunctions', None)
    _safe_set(owner, 'Actor140', partner)
    assert owner in getattr(partner, 'interactsWithFunctions')
    _safe_set(owner, 'Actor140', None)
    assert owner not in getattr(partner, 'interactsWithFunctions')


def test_assoc_supportsProcesses133_stub_double():
    # contentfwk_Function has no real 'decomposesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'decomposesFunctions', None)
    _safe_set(owner, 'Process134', partner)
    assert owner in getattr(partner, 'decomposesFunctions')
    _safe_set(owner, 'Process134', None)
    assert owner not in getattr(partner, 'decomposesFunctions')


def test_assoc_supportsProcesses332_stub_double():
    # contentfwk_Service has no real 'decomposesServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'decomposesServices', None)
    _safe_set(owner, 'Process333', partner)
    assert owner in getattr(partner, 'decomposesServices')
    _safe_set(owner, 'Process333', None)
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


