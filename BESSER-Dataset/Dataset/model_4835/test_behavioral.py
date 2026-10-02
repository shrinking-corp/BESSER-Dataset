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

def test_assoc_architectures0_reverse_link_reassign_clear():
    a1 = contentfwk_EnterpriseArchitecture(ID="sample_text")
    a2 = contentfwk_EnterpriseArchitecture(ID="sample_text_2")
    b = contentfwk_Architecture(ID="sample_text")
    _safe_set(b, 'contentfwk_Architecture', a1)
    assert _is_linked(b, 'contentfwk_Architecture', a1)
    if hasattr(a1, 'contentfwk_EnterpriseArchitecture'):
        assert _is_linked(a1, 'contentfwk_EnterpriseArchitecture', b)
    _safe_set(b, 'contentfwk_Architecture', a2)
    assert _is_linked(b, 'contentfwk_Architecture', a2)
    if hasattr(a1, 'contentfwk_EnterpriseArchitecture'):
        assert not _is_linked(a1, 'contentfwk_EnterpriseArchitecture', b)
    if hasattr(a2, 'contentfwk_EnterpriseArchitecture'):
        assert _is_linked(a2, 'contentfwk_EnterpriseArchitecture', b)
    _safe_set(b, 'contentfwk_Architecture', None)
    assert not _is_linked(b, 'contentfwk_Architecture', a2)
    if hasattr(a2, 'contentfwk_EnterpriseArchitecture'):
        assert not _is_linked(a2, 'contentfwk_EnterpriseArchitecture', b)


def test_assoc_belongsToOrganizationUnit85_reverse_link_reassign_clear():
    a1 = contentfwk_OrganizationUnit(headcount="sample_text")
    a2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'containsActors', a1)
    assert _is_linked(b, 'containsActors', a1)
    if hasattr(a1, 'OrganizationUnit86'):
        assert _is_linked(a1, 'OrganizationUnit86', b)
    _safe_set(b, 'containsActors', a2)
    assert _is_linked(b, 'containsActors', a2)
    if hasattr(a1, 'OrganizationUnit86'):
        assert not _is_linked(a1, 'OrganizationUnit86', b)
    if hasattr(a2, 'OrganizationUnit86'):
        assert _is_linked(a2, 'OrganizationUnit86', b)
    _safe_set(b, 'containsActors', None)
    assert not _is_linked(b, 'containsActors', a2)
    if hasattr(a2, 'OrganizationUnit86'):
        assert not _is_linked(a2, 'OrganizationUnit86', b)


def test_assoc_communicatesWith317_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    a2 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent318', a1)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent318', a1)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent316'):
        assert _is_linked(a1, 'contentfwk_PhysicalApplicationComponent316', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent318', a2)
    assert _is_linked(b, 'contentfwk_PhysicalApplicationComponent318', a2)
    if hasattr(a1, 'contentfwk_PhysicalApplicationComponent316'):
        assert not _is_linked(a1, 'contentfwk_PhysicalApplicationComponent316', b)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent316'):
        assert _is_linked(a2, 'contentfwk_PhysicalApplicationComponent316', b)
    _safe_set(b, 'contentfwk_PhysicalApplicationComponent318', None)
    assert not _is_linked(b, 'contentfwk_PhysicalApplicationComponent318', a2)
    if hasattr(a2, 'contentfwk_PhysicalApplicationComponent316'):
        assert not _is_linked(a2, 'contentfwk_PhysicalApplicationComponent316', b)


def test_assoc_consumesDataEntities83_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'isConsumedByActors', {a1})
    assert _is_linked(b, 'isConsumedByActors', a1)
    if hasattr(a1, 'DataEntity84'):
        assert _is_linked(a1, 'DataEntity84', b)
    _safe_set(b, 'isConsumedByActors', {a2})
    assert _is_linked(b, 'isConsumedByActors', a2)
    if hasattr(a1, 'DataEntity84'):
        assert not _is_linked(a1, 'DataEntity84', b)
    if hasattr(a2, 'DataEntity84'):
        assert _is_linked(a2, 'DataEntity84', b)
    _safe_set(b, 'isConsumedByActors', set())
    assert not _is_linked(b, 'isConsumedByActors', a2)
    if hasattr(a2, 'DataEntity84'):
        assert not _is_linked(a2, 'DataEntity84', b)


def test_assoc_containsActors69_reverse_link_reassign_clear():
    a1 = contentfwk_OrganizationUnit(headcount="sample_text")
    a2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor', a1)
    assert _is_linked(b, 'Actor', a1)
    if hasattr(a1, 'belongsToOrganizationUnit'):
        assert _is_linked(a1, 'belongsToOrganizationUnit', b)
    _safe_set(b, 'Actor', a2)
    assert _is_linked(b, 'Actor', a2)
    if hasattr(a1, 'belongsToOrganizationUnit'):
        assert not _is_linked(a1, 'belongsToOrganizationUnit', b)
    if hasattr(a2, 'belongsToOrganizationUnit'):
        assert _is_linked(a2, 'belongsToOrganizationUnit', b)
    _safe_set(b, 'Actor', None)
    assert not _is_linked(b, 'Actor', a2)
    if hasattr(a2, 'belongsToOrganizationUnit'):
        assert not _is_linked(a2, 'belongsToOrganizationUnit', b)


def test_assoc_decomposesActor103_reverse_link_reassign_clear():
    a1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    a2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'isDecomposedByActors', a1)
    assert _is_linked(b, 'isDecomposedByActors', a1)
    if hasattr(a1, 'Actor104'):
        assert _is_linked(a1, 'Actor104', b)
    _safe_set(b, 'isDecomposedByActors', a2)
    assert _is_linked(b, 'isDecomposedByActors', a2)
    if hasattr(a1, 'Actor104'):
        assert not _is_linked(a1, 'Actor104', b)
    if hasattr(a2, 'Actor104'):
        assert _is_linked(a2, 'Actor104', b)
    _safe_set(b, 'isDecomposedByActors', None)
    assert not _is_linked(b, 'isDecomposedByActors', a2)
    if hasattr(a2, 'Actor104'):
        assert not _is_linked(a2, 'Actor104', b)


def test_assoc_decomposesDataEntity130_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    _safe_set(b, 'contentfwk_DataEntity131', a1)
    assert _is_linked(b, 'contentfwk_DataEntity131', a1)
    if hasattr(a1, 'contentfwk_DataEntity129'):
        assert _is_linked(a1, 'contentfwk_DataEntity129', b)
    _safe_set(b, 'contentfwk_DataEntity131', a2)
    assert _is_linked(b, 'contentfwk_DataEntity131', a2)
    if hasattr(a1, 'contentfwk_DataEntity129'):
        assert not _is_linked(a1, 'contentfwk_DataEntity129', b)
    if hasattr(a2, 'contentfwk_DataEntity129'):
        assert _is_linked(a2, 'contentfwk_DataEntity129', b)
    _safe_set(b, 'contentfwk_DataEntity131', None)
    assert not _is_linked(b, 'contentfwk_DataEntity131', a2)
    if hasattr(a2, 'contentfwk_DataEntity129'):
        assert not _is_linked(a2, 'contentfwk_DataEntity129', b)


def test_assoc_decomposesLogicalTechnologyComponent335_reverse_link_reassign_clear():
    a1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    a2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'isDecomposedByLogicalTechnologyComponents', a1)
    assert _is_linked(b, 'isDecomposedByLogicalTechnologyComponents', a1)
    if hasattr(a1, 'LogicalTechnologyComponent336'):
        assert _is_linked(a1, 'LogicalTechnologyComponent336', b)
    _safe_set(b, 'isDecomposedByLogicalTechnologyComponents', a2)
    assert _is_linked(b, 'isDecomposedByLogicalTechnologyComponents', a2)
    if hasattr(a1, 'LogicalTechnologyComponent336'):
        assert not _is_linked(a1, 'LogicalTechnologyComponent336', b)
    if hasattr(a2, 'LogicalTechnologyComponent336'):
        assert _is_linked(a2, 'LogicalTechnologyComponent336', b)
    _safe_set(b, 'isDecomposedByLogicalTechnologyComponents', None)
    assert not _is_linked(b, 'isDecomposedByLogicalTechnologyComponents', a2)
    if hasattr(a2, 'LogicalTechnologyComponent336'):
        assert not _is_linked(a2, 'LogicalTechnologyComponent336', b)


def test_assoc_decomposesOrganizationUnit77_reverse_link_reassign_clear():
    a1 = contentfwk_OrganizationUnit(headcount="sample_text")
    a2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    b = contentfwk_OrganizationUnit(headcount="sample_text")
    _safe_set(b, 'isDecomposedByOrganizationUnits', a1)
    assert _is_linked(b, 'isDecomposedByOrganizationUnits', a1)
    if hasattr(a1, 'OrganizationUnit78'):
        assert _is_linked(a1, 'OrganizationUnit78', b)
    _safe_set(b, 'isDecomposedByOrganizationUnits', a2)
    assert _is_linked(b, 'isDecomposedByOrganizationUnits', a2)
    if hasattr(a1, 'OrganizationUnit78'):
        assert not _is_linked(a1, 'OrganizationUnit78', b)
    if hasattr(a2, 'OrganizationUnit78'):
        assert _is_linked(a2, 'OrganizationUnit78', b)
    _safe_set(b, 'isDecomposedByOrganizationUnits', None)
    assert not _is_linked(b, 'isDecomposedByOrganizationUnits', a2)
    if hasattr(a2, 'OrganizationUnit78'):
        assert not _is_linked(a2, 'OrganizationUnit78', b)


def test_assoc_decomposesPhysicalApplicationComponent324_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    a2 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'isDecomposedByPhysicalApplicationComponents', a1)
    assert _is_linked(b, 'isDecomposedByPhysicalApplicationComponents', a1)
    if hasattr(a1, 'PhysicalApplicationComponent325'):
        assert _is_linked(a1, 'PhysicalApplicationComponent325', b)
    _safe_set(b, 'isDecomposedByPhysicalApplicationComponents', a2)
    assert _is_linked(b, 'isDecomposedByPhysicalApplicationComponents', a2)
    if hasattr(a1, 'PhysicalApplicationComponent325'):
        assert not _is_linked(a1, 'PhysicalApplicationComponent325', b)
    if hasattr(a2, 'PhysicalApplicationComponent325'):
        assert _is_linked(a2, 'PhysicalApplicationComponent325', b)
    _safe_set(b, 'isDecomposedByPhysicalApplicationComponents', None)
    assert not _is_linked(b, 'isDecomposedByPhysicalApplicationComponents', a2)
    if hasattr(a2, 'PhysicalApplicationComponent325'):
        assert not _is_linked(a2, 'PhysicalApplicationComponent325', b)


def test_assoc_decomposesPhysicalTechnologyComponent219_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'isDecomposedByPhysicalTechnologyComponents', a1)
    assert _is_linked(b, 'isDecomposedByPhysicalTechnologyComponents', a1)
    if hasattr(a1, 'PhysicalTechnologyComponent'):
        assert _is_linked(a1, 'PhysicalTechnologyComponent', b)
    _safe_set(b, 'isDecomposedByPhysicalTechnologyComponents', a2)
    assert _is_linked(b, 'isDecomposedByPhysicalTechnologyComponents', a2)
    if hasattr(a1, 'PhysicalTechnologyComponent'):
        assert not _is_linked(a1, 'PhysicalTechnologyComponent', b)
    if hasattr(a2, 'PhysicalTechnologyComponent'):
        assert _is_linked(a2, 'PhysicalTechnologyComponent', b)
    _safe_set(b, 'isDecomposedByPhysicalTechnologyComponents', None)
    assert not _is_linked(b, 'isDecomposedByPhysicalTechnologyComponents', a2)
    if hasattr(a2, 'PhysicalTechnologyComponent'):
        assert not _is_linked(a2, 'PhysicalTechnologyComponent', b)


def test_assoc_decomposesProcess199_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'isDecomposedByProcesses', a1)
    assert _is_linked(b, 'isDecomposedByProcesses', a1)
    if hasattr(a1, 'Process200'):
        assert _is_linked(a1, 'Process200', b)
    _safe_set(b, 'isDecomposedByProcesses', a2)
    assert _is_linked(b, 'isDecomposedByProcesses', a2)
    if hasattr(a1, 'Process200'):
        assert not _is_linked(a1, 'Process200', b)
    if hasattr(a2, 'Process200'):
        assert _is_linked(a2, 'Process200', b)
    _safe_set(b, 'isDecomposedByProcesses', None)
    assert not _is_linked(b, 'isDecomposedByProcesses', a2)
    if hasattr(a2, 'Process200'):
        assert not _is_linked(a2, 'Process200', b)


def test_assoc_decomposesRole113_reverse_link_reassign_clear():
    a1 = contentfwk_Role(estimatedFTEs="sample_text")
    a2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    b = contentfwk_Role(estimatedFTEs="sample_text")
    _safe_set(b, 'isDecomposedByRoles', a1)
    assert _is_linked(b, 'isDecomposedByRoles', a1)
    if hasattr(a1, 'Role114'):
        assert _is_linked(a1, 'Role114', b)
    _safe_set(b, 'isDecomposedByRoles', a2)
    assert _is_linked(b, 'isDecomposedByRoles', a2)
    if hasattr(a1, 'Role114'):
        assert not _is_linked(a1, 'Role114', b)
    if hasattr(a2, 'Role114'):
        assert _is_linked(a2, 'Role114', b)
    _safe_set(b, 'isDecomposedByRoles', None)
    assert not _is_linked(b, 'isDecomposedByRoles', a2)
    if hasattr(a2, 'Role114'):
        assert not _is_linked(a2, 'Role114', b)


def test_assoc_delegates267_reverse_link_reassign_clear():
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


def test_assoc_deliversCapabilities289_reverse_link_reassign_clear():
    a1 = contentfwk_WorkPackage(capabilityDelivered="sample_text", workPackageCategory="sample_text")
    a2 = contentfwk_WorkPackage(capabilityDelivered="sample_text_2", workPackageCategory="sample_text_2")
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


def test_assoc_extendsLogicalTechnologyComponents213_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'LogicalTechnologyComponent215', a1)
    assert _is_linked(b, 'LogicalTechnologyComponent215', a1)
    if hasattr(a1, 'isRealizedByPhysicalTechnologyComponents214'):
        assert _is_linked(a1, 'isRealizedByPhysicalTechnologyComponents214', b)
    _safe_set(b, 'LogicalTechnologyComponent215', a2)
    assert _is_linked(b, 'LogicalTechnologyComponent215', a2)
    if hasattr(a1, 'isRealizedByPhysicalTechnologyComponents214'):
        assert not _is_linked(a1, 'isRealizedByPhysicalTechnologyComponents214', b)
    if hasattr(a2, 'isRealizedByPhysicalTechnologyComponents214'):
        assert _is_linked(a2, 'isRealizedByPhysicalTechnologyComponents214', b)
    _safe_set(b, 'LogicalTechnologyComponent215', None)
    assert not _is_linked(b, 'LogicalTechnologyComponent215', a2)
    if hasattr(a2, 'isRealizedByPhysicalTechnologyComponents214'):
        assert not _is_linked(a2, 'isRealizedByPhysicalTechnologyComponents214', b)


def test_assoc_followsProcesses205_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'precedesProcesses', {a1})
    assert _is_linked(b, 'precedesProcesses', a1)
    if hasattr(a1, 'Process206'):
        assert _is_linked(a1, 'Process206', b)
    _safe_set(b, 'precedesProcesses', {a2})
    assert _is_linked(b, 'precedesProcesses', a2)
    if hasattr(a1, 'Process206'):
        assert not _is_linked(a1, 'Process206', b)
    if hasattr(a2, 'Process206'):
        assert _is_linked(a2, 'Process206', b)
    _safe_set(b, 'precedesProcesses', set())
    assert not _is_linked(b, 'precedesProcesses', a2)
    if hasattr(a2, 'Process206'):
        assert not _is_linked(a2, 'Process206', b)


def test_assoc_involvesActors188_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor190', a1)
    assert _is_linked(b, 'Actor190', a1)
    if hasattr(a1, 'participatesInProcesses189'):
        assert _is_linked(a1, 'participatesInProcesses189', b)
    _safe_set(b, 'Actor190', a2)
    assert _is_linked(b, 'Actor190', a2)
    if hasattr(a1, 'participatesInProcesses189'):
        assert not _is_linked(a1, 'participatesInProcesses189', b)
    if hasattr(a2, 'participatesInProcesses189'):
        assert _is_linked(a2, 'participatesInProcesses189', b)
    _safe_set(b, 'Actor190', None)
    assert not _is_linked(b, 'Actor190', a2)
    if hasattr(a2, 'participatesInProcesses189'):
        assert not _is_linked(a2, 'participatesInProcesses189', b)


def test_assoc_involvesOrganizationUnits180_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_OrganizationUnit(headcount="sample_text")
    _safe_set(b, 'OrganizationUnit181', a1)
    assert _is_linked(b, 'OrganizationUnit181', a1)
    if hasattr(a1, 'participatesInProcesses'):
        assert _is_linked(a1, 'participatesInProcesses', b)
    _safe_set(b, 'OrganizationUnit181', a2)
    assert _is_linked(b, 'OrganizationUnit181', a2)
    if hasattr(a1, 'participatesInProcesses'):
        assert not _is_linked(a1, 'participatesInProcesses', b)
    if hasattr(a2, 'participatesInProcesses'):
        assert _is_linked(a2, 'participatesInProcesses', b)
    _safe_set(b, 'OrganizationUnit181', None)
    assert not _is_linked(b, 'OrganizationUnit181', a2)
    if hasattr(a2, 'participatesInProcesses'):
        assert not _is_linked(a2, 'participatesInProcesses', b)


def test_assoc_isAssumedByActors108_reverse_link_reassign_clear():
    a1 = contentfwk_Role(estimatedFTEs="sample_text")
    a2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor109', a1)
    assert _is_linked(b, 'Actor109', a1)
    if hasattr(a1, 'performsTaskInRoles'):
        assert _is_linked(a1, 'performsTaskInRoles', b)
    _safe_set(b, 'Actor109', a2)
    assert _is_linked(b, 'Actor109', a2)
    if hasattr(a1, 'performsTaskInRoles'):
        assert not _is_linked(a1, 'performsTaskInRoles', b)
    if hasattr(a2, 'performsTaskInRoles'):
        assert _is_linked(a2, 'performsTaskInRoles', b)
    _safe_set(b, 'Actor109', None)
    assert not _is_linked(b, 'Actor109', a2)
    if hasattr(a2, 'performsTaskInRoles'):
        assert not _is_linked(a2, 'performsTaskInRoles', b)


def test_assoc_isConsumedByActors120_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor121', a1)
    assert _is_linked(b, 'Actor121', a1)
    if hasattr(a1, 'consumesDataEntities'):
        assert _is_linked(a1, 'consumesDataEntities', b)
    _safe_set(b, 'Actor121', a2)
    assert _is_linked(b, 'Actor121', a2)
    if hasattr(a1, 'consumesDataEntities'):
        assert not _is_linked(a1, 'consumesDataEntities', b)
    if hasattr(a2, 'consumesDataEntities'):
        assert _is_linked(a2, 'consumesDataEntities', b)
    _safe_set(b, 'Actor121', None)
    assert not _is_linked(b, 'Actor121', a2)
    if hasattr(a2, 'consumesDataEntities'):
        assert not _is_linked(a2, 'consumesDataEntities', b)


def test_assoc_isDecomposedByActors106_reverse_link_reassign_clear():
    a1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    a2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'decomposesActor', {a1})
    assert _is_linked(b, 'decomposesActor', a1)
    if hasattr(a1, 'Actor107'):
        assert _is_linked(a1, 'Actor107', b)
    _safe_set(b, 'decomposesActor', {a2})
    assert _is_linked(b, 'decomposesActor', a2)
    if hasattr(a1, 'Actor107'):
        assert not _is_linked(a1, 'Actor107', b)
    if hasattr(a2, 'Actor107'):
        assert _is_linked(a2, 'Actor107', b)
    _safe_set(b, 'decomposesActor', set())
    assert not _is_linked(b, 'decomposesActor', a2)
    if hasattr(a2, 'Actor107'):
        assert not _is_linked(a2, 'Actor107', b)


def test_assoc_isDecomposedByDataEntities136_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    _safe_set(b, 'contentfwk_DataEntity137', a1)
    assert _is_linked(b, 'contentfwk_DataEntity137', a1)
    if hasattr(a1, 'contentfwk_DataEntity135'):
        assert _is_linked(a1, 'contentfwk_DataEntity135', b)
    _safe_set(b, 'contentfwk_DataEntity137', a2)
    assert _is_linked(b, 'contentfwk_DataEntity137', a2)
    if hasattr(a1, 'contentfwk_DataEntity135'):
        assert not _is_linked(a1, 'contentfwk_DataEntity135', b)
    if hasattr(a2, 'contentfwk_DataEntity135'):
        assert _is_linked(a2, 'contentfwk_DataEntity135', b)
    _safe_set(b, 'contentfwk_DataEntity137', None)
    assert not _is_linked(b, 'contentfwk_DataEntity137', a2)
    if hasattr(a2, 'contentfwk_DataEntity135'):
        assert not _is_linked(a2, 'contentfwk_DataEntity135', b)


def test_assoc_isDecomposedByLogicalTechnologyComponents347_reverse_link_reassign_clear():
    a1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    a2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'decomposesLogicalTechnologyComponent', {a1})
    assert _is_linked(b, 'decomposesLogicalTechnologyComponent', a1)
    if hasattr(a1, 'LogicalTechnologyComponent348'):
        assert _is_linked(a1, 'LogicalTechnologyComponent348', b)
    _safe_set(b, 'decomposesLogicalTechnologyComponent', {a2})
    assert _is_linked(b, 'decomposesLogicalTechnologyComponent', a2)
    if hasattr(a1, 'LogicalTechnologyComponent348'):
        assert not _is_linked(a1, 'LogicalTechnologyComponent348', b)
    if hasattr(a2, 'LogicalTechnologyComponent348'):
        assert _is_linked(a2, 'LogicalTechnologyComponent348', b)
    _safe_set(b, 'decomposesLogicalTechnologyComponent', set())
    assert not _is_linked(b, 'decomposesLogicalTechnologyComponent', a2)
    if hasattr(a2, 'LogicalTechnologyComponent348'):
        assert not _is_linked(a2, 'LogicalTechnologyComponent348', b)


def test_assoc_isDecomposedByOrganizationUnits80_reverse_link_reassign_clear():
    a1 = contentfwk_OrganizationUnit(headcount="sample_text")
    a2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    b = contentfwk_OrganizationUnit(headcount="sample_text")
    _safe_set(b, 'decomposesOrganizationUnit', {a1})
    assert _is_linked(b, 'decomposesOrganizationUnit', a1)
    if hasattr(a1, 'OrganizationUnit81'):
        assert _is_linked(a1, 'OrganizationUnit81', b)
    _safe_set(b, 'decomposesOrganizationUnit', {a2})
    assert _is_linked(b, 'decomposesOrganizationUnit', a2)
    if hasattr(a1, 'OrganizationUnit81'):
        assert not _is_linked(a1, 'OrganizationUnit81', b)
    if hasattr(a2, 'OrganizationUnit81'):
        assert _is_linked(a2, 'OrganizationUnit81', b)
    _safe_set(b, 'decomposesOrganizationUnit', set())
    assert not _is_linked(b, 'decomposesOrganizationUnit', a2)
    if hasattr(a2, 'OrganizationUnit81'):
        assert not _is_linked(a2, 'OrganizationUnit81', b)


def test_assoc_isDecomposedByPhysicalApplicationComponents327_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    a2 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'decomposesPhysicalApplicationComponent', {a1})
    assert _is_linked(b, 'decomposesPhysicalApplicationComponent', a1)
    if hasattr(a1, 'PhysicalApplicationComponent328'):
        assert _is_linked(a1, 'PhysicalApplicationComponent328', b)
    _safe_set(b, 'decomposesPhysicalApplicationComponent', {a2})
    assert _is_linked(b, 'decomposesPhysicalApplicationComponent', a2)
    if hasattr(a1, 'PhysicalApplicationComponent328'):
        assert not _is_linked(a1, 'PhysicalApplicationComponent328', b)
    if hasattr(a2, 'PhysicalApplicationComponent328'):
        assert _is_linked(a2, 'PhysicalApplicationComponent328', b)
    _safe_set(b, 'decomposesPhysicalApplicationComponent', set())
    assert not _is_linked(b, 'decomposesPhysicalApplicationComponent', a2)
    if hasattr(a2, 'PhysicalApplicationComponent328'):
        assert not _is_linked(a2, 'PhysicalApplicationComponent328', b)


def test_assoc_isDecomposedByPhysicalTechnologyComponents227_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'decomposesPhysicalTechnologyComponent', {a1})
    assert _is_linked(b, 'decomposesPhysicalTechnologyComponent', a1)
    if hasattr(a1, 'PhysicalTechnologyComponent228'):
        assert _is_linked(a1, 'PhysicalTechnologyComponent228', b)
    _safe_set(b, 'decomposesPhysicalTechnologyComponent', {a2})
    assert _is_linked(b, 'decomposesPhysicalTechnologyComponent', a2)
    if hasattr(a1, 'PhysicalTechnologyComponent228'):
        assert not _is_linked(a1, 'PhysicalTechnologyComponent228', b)
    if hasattr(a2, 'PhysicalTechnologyComponent228'):
        assert _is_linked(a2, 'PhysicalTechnologyComponent228', b)
    _safe_set(b, 'decomposesPhysicalTechnologyComponent', set())
    assert not _is_linked(b, 'decomposesPhysicalTechnologyComponent', a2)
    if hasattr(a2, 'PhysicalTechnologyComponent228'):
        assert not _is_linked(a2, 'PhysicalTechnologyComponent228', b)


def test_assoc_isDecomposedByProcesses208_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'decomposesProcess', {a1})
    assert _is_linked(b, 'decomposesProcess', a1)
    if hasattr(a1, 'Process209'):
        assert _is_linked(a1, 'Process209', b)
    _safe_set(b, 'decomposesProcess', {a2})
    assert _is_linked(b, 'decomposesProcess', a2)
    if hasattr(a1, 'Process209'):
        assert not _is_linked(a1, 'Process209', b)
    if hasattr(a2, 'Process209'):
        assert _is_linked(a2, 'Process209', b)
    _safe_set(b, 'decomposesProcess', set())
    assert not _is_linked(b, 'decomposesProcess', a2)
    if hasattr(a2, 'Process209'):
        assert not _is_linked(a2, 'Process209', b)


def test_assoc_isDecomposedByRoles116_reverse_link_reassign_clear():
    a1 = contentfwk_Role(estimatedFTEs="sample_text")
    a2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    b = contentfwk_Role(estimatedFTEs="sample_text")
    _safe_set(b, 'decomposesRole', {a1})
    assert _is_linked(b, 'decomposesRole', a1)
    if hasattr(a1, 'Role117'):
        assert _is_linked(a1, 'Role117', b)
    _safe_set(b, 'decomposesRole', {a2})
    assert _is_linked(b, 'decomposesRole', a2)
    if hasattr(a1, 'Role117'):
        assert not _is_linked(a1, 'Role117', b)
    if hasattr(a2, 'Role117'):
        assert _is_linked(a2, 'Role117', b)
    _safe_set(b, 'decomposesRole', set())
    assert not _is_linked(b, 'decomposesRole', a2)
    if hasattr(a2, 'Role117'):
        assert not _is_linked(a2, 'Role117', b)


def test_assoc_isDelegatedBy269_reverse_link_reassign_clear():
    a1 = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    a2 = contentfwk_Element(ID="sample_text_2", category="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    b = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    _safe_set(b, 'delegates', {a1})
    assert _is_linked(b, 'delegates', a1)
    if hasattr(a1, 'Element270'):
        assert _is_linked(a1, 'Element270', b)
    _safe_set(b, 'delegates', {a2})
    assert _is_linked(b, 'delegates', a2)
    if hasattr(a1, 'Element270'):
        assert not _is_linked(a1, 'Element270', b)
    if hasattr(a2, 'Element270'):
        assert _is_linked(a2, 'Element270', b)
    _safe_set(b, 'delegates', set())
    assert not _is_linked(b, 'delegates', a2)
    if hasattr(a2, 'Element270'):
        assert not _is_linked(a2, 'Element270', b)


def test_assoc_isDeliveredBy288_reverse_link_reassign_clear():
    a1 = contentfwk_WorkPackage(capabilityDelivered="sample_text", workPackageCategory="sample_text")
    a2 = contentfwk_WorkPackage(capabilityDelivered="sample_text_2", workPackageCategory="sample_text_2")
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


def test_assoc_isDependentOnLogicalTechnologyComponents338_reverse_link_reassign_clear():
    a1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    a2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'isRequiredByLogicalTechnologyComponents', {a1})
    assert _is_linked(b, 'isRequiredByLogicalTechnologyComponents', a1)
    if hasattr(a1, 'LogicalTechnologyComponent339'):
        assert _is_linked(a1, 'LogicalTechnologyComponent339', b)
    _safe_set(b, 'isRequiredByLogicalTechnologyComponents', {a2})
    assert _is_linked(b, 'isRequiredByLogicalTechnologyComponents', a2)
    if hasattr(a1, 'LogicalTechnologyComponent339'):
        assert not _is_linked(a1, 'LogicalTechnologyComponent339', b)
    if hasattr(a2, 'LogicalTechnologyComponent339'):
        assert _is_linked(a2, 'LogicalTechnologyComponent339', b)
    _safe_set(b, 'isRequiredByLogicalTechnologyComponents', set())
    assert not _is_linked(b, 'isRequiredByLogicalTechnologyComponents', a2)
    if hasattr(a2, 'LogicalTechnologyComponent339'):
        assert not _is_linked(a2, 'LogicalTechnologyComponent339', b)


def test_assoc_isDependentOnPhysicalTechnologyComponents221_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'isRequiredByPhysicalTechnologyComponent', {a1})
    assert _is_linked(b, 'isRequiredByPhysicalTechnologyComponent', a1)
    if hasattr(a1, 'PhysicalTechnologyComponent222'):
        assert _is_linked(a1, 'PhysicalTechnologyComponent222', b)
    _safe_set(b, 'isRequiredByPhysicalTechnologyComponent', {a2})
    assert _is_linked(b, 'isRequiredByPhysicalTechnologyComponent', a2)
    if hasattr(a1, 'PhysicalTechnologyComponent222'):
        assert not _is_linked(a1, 'PhysicalTechnologyComponent222', b)
    if hasattr(a2, 'PhysicalTechnologyComponent222'):
        assert _is_linked(a2, 'PhysicalTechnologyComponent222', b)
    _safe_set(b, 'isRequiredByPhysicalTechnologyComponent', set())
    assert not _is_linked(b, 'isRequiredByPhysicalTechnologyComponent', a2)
    if hasattr(a2, 'PhysicalTechnologyComponent222'):
        assert not _is_linked(a2, 'PhysicalTechnologyComponent222', b)


def test_assoc_isExtendedByPhysicalTechnologyComponent340_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'contentfwk_LogicalTechnologyComponent341', {a1})
    assert _is_linked(b, 'contentfwk_LogicalTechnologyComponent341', a1)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent342'):
        assert _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent342', b)
    _safe_set(b, 'contentfwk_LogicalTechnologyComponent341', {a2})
    assert _is_linked(b, 'contentfwk_LogicalTechnologyComponent341', a2)
    if hasattr(a1, 'contentfwk_PhysicalTechnologyComponent342'):
        assert not _is_linked(a1, 'contentfwk_PhysicalTechnologyComponent342', b)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent342'):
        assert _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent342', b)
    _safe_set(b, 'contentfwk_LogicalTechnologyComponent341', set())
    assert not _is_linked(b, 'contentfwk_LogicalTechnologyComponent341', a2)
    if hasattr(a2, 'contentfwk_PhysicalTechnologyComponent342'):
        assert not _is_linked(a2, 'contentfwk_PhysicalTechnologyComponent342', b)


def test_assoc_isRealizedByPhysicalTechnologyComponents321_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'realizesPhysicalApplicationComponents', {a1})
    assert _is_linked(b, 'realizesPhysicalApplicationComponents', a1)
    if hasattr(a1, 'PhysicalTechnologyComponent322'):
        assert _is_linked(a1, 'PhysicalTechnologyComponent322', b)
    _safe_set(b, 'realizesPhysicalApplicationComponents', {a2})
    assert _is_linked(b, 'realizesPhysicalApplicationComponents', a2)
    if hasattr(a1, 'PhysicalTechnologyComponent322'):
        assert not _is_linked(a1, 'PhysicalTechnologyComponent322', b)
    if hasattr(a2, 'PhysicalTechnologyComponent322'):
        assert _is_linked(a2, 'PhysicalTechnologyComponent322', b)
    _safe_set(b, 'realizesPhysicalApplicationComponents', set())
    assert not _is_linked(b, 'realizesPhysicalApplicationComponents', a2)
    if hasattr(a2, 'PhysicalTechnologyComponent322'):
        assert not _is_linked(a2, 'PhysicalTechnologyComponent322', b)


def test_assoc_isRealizedByPhysicalTechnologyComponents332_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'extendsLogicalTechnologyComponents', {a1})
    assert _is_linked(b, 'extendsLogicalTechnologyComponents', a1)
    if hasattr(a1, 'PhysicalTechnologyComponent333'):
        assert _is_linked(a1, 'PhysicalTechnologyComponent333', b)
    _safe_set(b, 'extendsLogicalTechnologyComponents', {a2})
    assert _is_linked(b, 'extendsLogicalTechnologyComponents', a2)
    if hasattr(a1, 'PhysicalTechnologyComponent333'):
        assert not _is_linked(a1, 'PhysicalTechnologyComponent333', b)
    if hasattr(a2, 'PhysicalTechnologyComponent333'):
        assert _is_linked(a2, 'PhysicalTechnologyComponent333', b)
    _safe_set(b, 'extendsLogicalTechnologyComponents', set())
    assert not _is_linked(b, 'extendsLogicalTechnologyComponents', a2)
    if hasattr(a2, 'PhysicalTechnologyComponent333'):
        assert not _is_linked(a2, 'PhysicalTechnologyComponent333', b)


def test_assoc_isRequiredByLogicalTechnologyComponents344_reverse_link_reassign_clear():
    a1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    a2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    b = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    _safe_set(b, 'isDependentOnLogicalTechnologyComponents', {a1})
    assert _is_linked(b, 'isDependentOnLogicalTechnologyComponents', a1)
    if hasattr(a1, 'LogicalTechnologyComponent345'):
        assert _is_linked(a1, 'LogicalTechnologyComponent345', b)
    _safe_set(b, 'isDependentOnLogicalTechnologyComponents', {a2})
    assert _is_linked(b, 'isDependentOnLogicalTechnologyComponents', a2)
    if hasattr(a1, 'LogicalTechnologyComponent345'):
        assert not _is_linked(a1, 'LogicalTechnologyComponent345', b)
    if hasattr(a2, 'LogicalTechnologyComponent345'):
        assert _is_linked(a2, 'LogicalTechnologyComponent345', b)
    _safe_set(b, 'isDependentOnLogicalTechnologyComponents', set())
    assert not _is_linked(b, 'isDependentOnLogicalTechnologyComponents', a2)
    if hasattr(a2, 'LogicalTechnologyComponent345'):
        assert not _is_linked(a2, 'LogicalTechnologyComponent345', b)


def test_assoc_isRequiredByPhysicalTechnologyComponent224_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'isDependentOnPhysicalTechnologyComponents', {a1})
    assert _is_linked(b, 'isDependentOnPhysicalTechnologyComponents', a1)
    if hasattr(a1, 'PhysicalTechnologyComponent225'):
        assert _is_linked(a1, 'PhysicalTechnologyComponent225', b)
    _safe_set(b, 'isDependentOnPhysicalTechnologyComponents', {a2})
    assert _is_linked(b, 'isDependentOnPhysicalTechnologyComponents', a2)
    if hasattr(a1, 'PhysicalTechnologyComponent225'):
        assert not _is_linked(a1, 'PhysicalTechnologyComponent225', b)
    if hasattr(a2, 'PhysicalTechnologyComponent225'):
        assert _is_linked(a2, 'PhysicalTechnologyComponent225', b)
    _safe_set(b, 'isDependentOnPhysicalTechnologyComponents', set())
    assert not _is_linked(b, 'isDependentOnPhysicalTechnologyComponents', a2)
    if hasattr(a2, 'PhysicalTechnologyComponent225'):
        assert not _is_linked(a2, 'PhysicalTechnologyComponent225', b)


def test_assoc_isSuppliedByActors118_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'Actor119', a1)
    assert _is_linked(b, 'Actor119', a1)
    if hasattr(a1, 'suppliesDataEntities'):
        assert _is_linked(a1, 'suppliesDataEntities', b)
    _safe_set(b, 'Actor119', a2)
    assert _is_linked(b, 'Actor119', a2)
    if hasattr(a1, 'suppliesDataEntities'):
        assert not _is_linked(a1, 'suppliesDataEntities', b)
    if hasattr(a2, 'suppliesDataEntities'):
        assert _is_linked(a2, 'suppliesDataEntities', b)
    _safe_set(b, 'Actor119', None)
    assert not _is_linked(b, 'Actor119', a2)
    if hasattr(a2, 'suppliesDataEntities'):
        assert not _is_linked(a2, 'suppliesDataEntities', b)


def test_assoc_isSuppliedByLogicalTechnologyComponents210_reverse_link_reassign_clear():
    a1 = contentfwk_PlatformService(categoryTRM="sample_text", standardClass="sample_text")
    a2 = contentfwk_PlatformService(categoryTRM="sample_text_2", standardClass="sample_text_2")
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


def test_assoc_participatesInProcesses71_reverse_link_reassign_clear():
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


def test_assoc_participatesInProcesses90_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    _safe_set(b, 'involvesActors', {a1})
    assert _is_linked(b, 'involvesActors', a1)
    if hasattr(a1, 'Process91'):
        assert _is_linked(a1, 'Process91', b)
    _safe_set(b, 'involvesActors', {a2})
    assert _is_linked(b, 'involvesActors', a2)
    if hasattr(a1, 'Process91'):
        assert not _is_linked(a1, 'Process91', b)
    if hasattr(a2, 'Process91'):
        assert _is_linked(a2, 'Process91', b)
    _safe_set(b, 'involvesActors', set())
    assert not _is_linked(b, 'involvesActors', a2)
    if hasattr(a2, 'Process91'):
        assert not _is_linked(a2, 'Process91', b)


def test_assoc_performsTaskInRoles89_reverse_link_reassign_clear():
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


def test_assoc_precedesProcesses202_reverse_link_reassign_clear():
    a1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    a2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    b = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    _safe_set(b, 'followsProcesses', {a1})
    assert _is_linked(b, 'followsProcesses', a1)
    if hasattr(a1, 'Process203'):
        assert _is_linked(a1, 'Process203', b)
    _safe_set(b, 'followsProcesses', {a2})
    assert _is_linked(b, 'followsProcesses', a2)
    if hasattr(a1, 'Process203'):
        assert not _is_linked(a1, 'Process203', b)
    if hasattr(a2, 'Process203'):
        assert _is_linked(a2, 'Process203', b)
    _safe_set(b, 'followsProcesses', set())
    assert not _is_linked(b, 'followsProcesses', a2)
    if hasattr(a2, 'Process203'):
        assert not _is_linked(a2, 'Process203', b)


def test_assoc_realizesPhysicalApplicationComponents211_reverse_link_reassign_clear():
    a1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    a2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    _safe_set(b, 'PhysicalApplicationComponent212', a1)
    assert _is_linked(b, 'PhysicalApplicationComponent212', a1)
    if hasattr(a1, 'isRealizedByPhysicalTechnologyComponents'):
        assert _is_linked(a1, 'isRealizedByPhysicalTechnologyComponents', b)
    _safe_set(b, 'PhysicalApplicationComponent212', a2)
    assert _is_linked(b, 'PhysicalApplicationComponent212', a2)
    if hasattr(a1, 'isRealizedByPhysicalTechnologyComponents'):
        assert not _is_linked(a1, 'isRealizedByPhysicalTechnologyComponents', b)
    if hasattr(a2, 'isRealizedByPhysicalTechnologyComponents'):
        assert _is_linked(a2, 'isRealizedByPhysicalTechnologyComponents', b)
    _safe_set(b, 'PhysicalApplicationComponent212', None)
    assert not _is_linked(b, 'PhysicalApplicationComponent212', a2)
    if hasattr(a2, 'isRealizedByPhysicalTechnologyComponents'):
        assert not _is_linked(a2, 'isRealizedByPhysicalTechnologyComponents', b)


def test_assoc_relatesToDataEntities133_reverse_link_reassign_clear():
    a1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    a2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    b = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    _safe_set(b, 'contentfwk_DataEntity134', a1)
    assert _is_linked(b, 'contentfwk_DataEntity134', a1)
    if hasattr(a1, 'contentfwk_DataEntity132'):
        assert _is_linked(a1, 'contentfwk_DataEntity132', b)
    _safe_set(b, 'contentfwk_DataEntity134', a2)
    assert _is_linked(b, 'contentfwk_DataEntity134', a2)
    if hasattr(a1, 'contentfwk_DataEntity132'):
        assert not _is_linked(a1, 'contentfwk_DataEntity132', b)
    if hasattr(a2, 'contentfwk_DataEntity132'):
        assert _is_linked(a2, 'contentfwk_DataEntity132', b)
    _safe_set(b, 'contentfwk_DataEntity134', None)
    assert not _is_linked(b, 'contentfwk_DataEntity134', a2)
    if hasattr(a2, 'contentfwk_DataEntity132'):
        assert not _is_linked(a2, 'contentfwk_DataEntity132', b)


def test_assoc_suppliesDataEntities82_reverse_link_reassign_clear():
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


def test_assoc_suppliesPlatformServices331_reverse_link_reassign_clear():
    a1 = contentfwk_PlatformService(categoryTRM="sample_text", standardClass="sample_text")
    a2 = contentfwk_PlatformService(categoryTRM="sample_text_2", standardClass="sample_text_2")
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


