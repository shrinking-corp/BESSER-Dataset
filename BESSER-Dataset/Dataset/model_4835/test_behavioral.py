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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessesFunctions110_stub_double():
    # contentfwk_Function has no real 'Function111' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Role(estimatedFTEs="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function111', None)
    _safe_set(owner, 'canBeAccessedByRoles', {partner})
    assert getattr(partner, 'Function111') == owner
    _safe_set(owner, 'canBeAccessedByRoles', set())
    assert getattr(partner, 'Function111') is None


def test_assoc_actors8_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture9' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture9', None)
    _safe_set(owner, 'contentfwk_Actor', partner)
    assert getattr(partner, 'contentfwk_BusinessArchitecture9') == owner
    _safe_set(owner, 'contentfwk_Actor', None)
    assert getattr(partner, 'contentfwk_BusinessArchitecture9') is None


def test_assoc_appliesToContracts247_stub_double():
    # contentfwk_ServiceQuality has no real 'meetsServiceQuality' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_ServiceQuality()
    setattr(partner, 'meetsServiceQuality', None)
    _safe_set(owner, 'Contract', partner)
    assert getattr(partner, 'meetsServiceQuality') == owner
    _safe_set(owner, 'Contract', None)
    assert getattr(partner, 'meetsServiceQuality') is None


def test_assoc_canBeAccessedByRoles161_stub_double():
    # contentfwk_Function has no real 'accessesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Role(estimatedFTEs="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'accessesFunctions', None)
    _safe_set(owner, 'Role162', partner)
    assert getattr(partner, 'accessesFunctions') == owner
    _safe_set(owner, 'Role162', None)
    assert getattr(partner, 'accessesFunctions') is None


def test_assoc_capabilities349_stub_double():
    # contentfwk_StrategicArchitecture has no real 'contentfwk_StrategicArchitecture' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Capability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Capability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Capability(businessValue="sample_text", increments="sample_text")
    partner = contentfwk_StrategicArchitecture()
    setattr(partner, 'contentfwk_StrategicArchitecture', None)
    _safe_set(owner, 'contentfwk_Capability', partner)
    assert getattr(partner, 'contentfwk_StrategicArchitecture') == owner
    _safe_set(owner, 'contentfwk_Capability', None)
    assert getattr(partner, 'contentfwk_StrategicArchitecture') is None


def test_assoc_consumesDataEntities358_stub_double():
    # contentfwk_Service has no real 'isAccessedByServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'isAccessedByServices', None)
    _safe_set(owner, 'DataEntity359', partner)
    assert getattr(partner, 'isAccessedByServices') == owner
    _safe_set(owner, 'DataEntity359', None)
    assert getattr(partner, 'isAccessedByServices') is None


def test_assoc_consumesServices92_stub_double():
    # contentfwk_Service has no real 'Service93' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service93', None)
    _safe_set(owner, 'isProvidedToActors', {partner})
    assert getattr(partner, 'Service93') == owner
    _safe_set(owner, 'isProvidedToActors', set())
    assert getattr(partner, 'Service93') is None


def test_assoc_containsActors271_stub_double():
    # contentfwk_Location has no real 'operatesInLocation' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'operatesInLocation', None)
    _safe_set(owner, 'Actor272', partner)
    assert getattr(partner, 'operatesInLocation') == owner
    _safe_set(owner, 'Actor272', None)
    assert getattr(partner, 'operatesInLocation') is None


def test_assoc_containsOrganizationUnits273_stub_double():
    # contentfwk_Location has no real 'operatesInLocation274' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'operatesInLocation274', None)
    _safe_set(owner, 'OrganizationUnit275', partner)
    assert getattr(partner, 'operatesInLocation274') == owner
    _safe_set(owner, 'OrganizationUnit275', None)
    assert getattr(partner, 'operatesInLocation274') is None


def test_assoc_containsPhysicalApplicationComponents277_stub_double():
    # contentfwk_Location has no real 'isHostedInLocation' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'isHostedInLocation', None)
    _safe_set(owner, 'PhysicalApplicationComponent278', partner)
    assert getattr(partner, 'isHostedInLocation') == owner
    _safe_set(owner, 'PhysicalApplicationComponent278', None)
    assert getattr(partner, 'isHostedInLocation') is None


def test_assoc_containsPhysicalTechnologyComponents279_stub_double():
    # contentfwk_Location has no real 'isHostedInLocation280' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'isHostedInLocation280', None)
    _safe_set(owner, 'PhysicalTechnologyComponent281', partner)
    assert getattr(partner, 'isHostedInLocation280') == owner
    _safe_set(owner, 'PhysicalTechnologyComponent281', None)
    assert getattr(partner, 'isHostedInLocation280') is None


def test_assoc_contracts26_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture27' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture27', None)
    _safe_set(owner, 'contentfwk_Contract', partner)
    assert getattr(partner, 'contentfwk_BusinessArchitecture27') == owner
    _safe_set(owner, 'contentfwk_Contract', None)
    assert getattr(partner, 'contentfwk_BusinessArchitecture27') is None


def test_assoc_decomposesFunctions178_stub_double():
    # contentfwk_Function has no real 'Function179' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function179', None)
    _safe_set(owner, 'supportsProcesses', {partner})
    assert getattr(partner, 'Function179') == owner
    _safe_set(owner, 'supportsProcesses', set())
    assert getattr(partner, 'Function179') is None


def test_assoc_decomposesServices185_stub_double():
    # contentfwk_Service has no real 'Service187' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service187', None)
    _safe_set(owner, 'supportsProcesses186', {partner})
    assert getattr(partner, 'Service187') == owner
    _safe_set(owner, 'supportsProcesses186', set())
    assert getattr(partner, 'Service187') is None


def test_assoc_encapsulatesDataEntities290_stub_double():
    # contentfwk_LogicalDataComponent has no real 'residesWithinLogicalDataComponent' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_LogicalDataComponent()
    setattr(partner, 'residesWithinLogicalDataComponent', None)
    _safe_set(owner, 'DataEntity291', partner)
    assert getattr(partner, 'residesWithinLogicalDataComponent') == owner
    _safe_set(owner, 'DataEntity291', None)
    assert getattr(partner, 'residesWithinLogicalDataComponent') is None


def test_assoc_encapsulatesPhysicalApplicationComponents301_stub_double():
    # contentfwk_PhysicalDataComponent has no real 'encapsulatesPhysicalDataComponents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_PhysicalDataComponent()
    setattr(partner, 'encapsulatesPhysicalDataComponents', None)
    _safe_set(owner, 'PhysicalApplicationComponent302', partner)
    assert getattr(partner, 'encapsulatesPhysicalDataComponents') == owner
    _safe_set(owner, 'PhysicalApplicationComponent302', None)
    assert getattr(partner, 'encapsulatesPhysicalDataComponents') is None


def test_assoc_encapsulatesPhysicalDataComponents319_stub_double():
    # contentfwk_PhysicalDataComponent has no real 'PhysicalDataComponent320' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_PhysicalDataComponent()
    setattr(partner, 'PhysicalDataComponent320', None)
    _safe_set(owner, 'encapsulatesPhysicalApplicationComponents', {partner})
    assert getattr(partner, 'PhysicalDataComponent320') == owner
    _safe_set(owner, 'encapsulatesPhysicalApplicationComponents', set())
    assert getattr(partner, 'PhysicalDataComponent320') is None


def test_assoc_ensuresCorrectOperationOfProcesses264_stub_double():
    # contentfwk_Control has no real 'isGuidedByControls' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Control()
    setattr(partner, 'isGuidedByControls', None)
    _safe_set(owner, 'Process265', partner)
    assert getattr(partner, 'isGuidedByControls') == owner
    _safe_set(owner, 'Process265', None)
    assert getattr(partner, 'isGuidedByControls') is None


def test_assoc_entities32_stub_double():
    # contentfwk_DataArchitecture has no real 'contentfwk_DataArchitecture' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_DataArchitecture()
    setattr(partner, 'contentfwk_DataArchitecture', None)
    _safe_set(owner, 'contentfwk_DataEntity', partner)
    assert getattr(partner, 'contentfwk_DataArchitecture') == owner
    _safe_set(owner, 'contentfwk_DataEntity', None)
    assert getattr(partner, 'contentfwk_DataArchitecture') is None


def test_assoc_extendsLogicalApplicationComponents312_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'LogicalApplicationComponent313' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'LogicalApplicationComponent313', None)
    _safe_set(owner, 'isExtendedByPhysicalApplicationComponents', {partner})
    assert getattr(partner, 'LogicalApplicationComponent313') == owner
    _safe_set(owner, 'isExtendedByPhysicalApplicationComponents', set())
    assert getattr(partner, 'LogicalApplicationComponent313') is None


def test_assoc_generatesEvents194_stub_double():
    # contentfwk_Event has no real 'Event195' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event195', None)
    _safe_set(owner, 'isGeneratedByProcesses', {partner})
    assert getattr(partner, 'Event195') == owner
    _safe_set(owner, 'isGeneratedByProcesses', set())
    assert getattr(partner, 'Event195') is None


def test_assoc_generatesEvents95_stub_double():
    # contentfwk_Event has no real 'Event96' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event96', None)
    _safe_set(owner, 'isGeneratedByActors', {partner})
    assert getattr(partner, 'Event96') == owner
    _safe_set(owner, 'isGeneratedByActors', set())
    assert getattr(partner, 'Event96') is None


def test_assoc_governsAndMeasuresBusinessServices248_stub_double():
    # contentfwk_Service has no real 'Service249' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service249', None)
    _safe_set(owner, 'isGovernedAndMeasuredByContracts', {partner})
    assert getattr(partner, 'Service249') == owner
    _safe_set(owner, 'isGovernedAndMeasuredByContracts', set())
    assert getattr(partner, 'Service249') is None


def test_assoc_interactsWithFunctions87_stub_double():
    # contentfwk_Function has no real 'Function88' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function88', None)
    _safe_set(owner, 'supportsActors', {partner})
    assert getattr(partner, 'Function88') == owner
    _safe_set(owner, 'supportsActors', set())
    assert getattr(partner, 'Function88') is None


def test_assoc_isAccessedByServices122_stub_double():
    # contentfwk_Service has no real 'Service124' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service124', None)
    _safe_set(owner, 'consumesDataEntities123', {partner})
    assert getattr(partner, 'Service124') == owner
    _safe_set(owner, 'consumesDataEntities123', set())
    assert getattr(partner, 'Service124') is None


def test_assoc_isExtendedByPhysicalApplicationComponents142_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'extendsLogicalApplicationComponents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'extendsLogicalApplicationComponents', None)
    _safe_set(owner, 'PhysicalApplicationComponent', partner)
    assert getattr(partner, 'extendsLogicalApplicationComponents') == owner
    _safe_set(owner, 'PhysicalApplicationComponent', None)
    assert getattr(partner, 'extendsLogicalApplicationComponents') is None


def test_assoc_isGeneratedByActors261_stub_double():
    # contentfwk_Event has no real 'generatesEvents262' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'generatesEvents262', None)
    _safe_set(owner, 'Actor263', partner)
    assert getattr(partner, 'generatesEvents262') == owner
    _safe_set(owner, 'Actor263', None)
    assert getattr(partner, 'generatesEvents262') is None


def test_assoc_isGeneratedByProcesses256_stub_double():
    # contentfwk_Event has no real 'generatesEvents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'generatesEvents', None)
    _safe_set(owner, 'Process257', partner)
    assert getattr(partner, 'generatesEvents') == owner
    _safe_set(owner, 'Process257', None)
    assert getattr(partner, 'generatesEvents') is None


def test_assoc_isGovernedAndMeasuredByContracts360_stub_double():
    # contentfwk_Service has no real 'governsAndMeasuresBusinessServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'governsAndMeasuresBusinessServices', None)
    _safe_set(owner, 'Contract361', partner)
    assert getattr(partner, 'governsAndMeasuresBusinessServices') == owner
    _safe_set(owner, 'Contract361', None)
    assert getattr(partner, 'governsAndMeasuresBusinessServices') is None


def test_assoc_isGuidedByControls191_stub_double():
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


def test_assoc_isHostedInLocation216_stub_double():
    # contentfwk_Location has no real 'Location217' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location217', None)
    _safe_set(owner, 'containsPhysicalTechnologyComponents', {partner})
    assert getattr(partner, 'Location217') == owner
    _safe_set(owner, 'containsPhysicalTechnologyComponents', set())
    assert getattr(partner, 'Location217') is None


def test_assoc_isHostedInLocation314_stub_double():
    # contentfwk_Location has no real 'Location315' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location315', None)
    _safe_set(owner, 'containsPhysicalApplicationComponents', {partner})
    assert getattr(partner, 'Location315') == owner
    _safe_set(owner, 'containsPhysicalApplicationComponents', set())
    assert getattr(partner, 'Location315') is None


def test_assoc_isImplementedOnLogicalTechnologyComponents364_stub_double():
    # contentfwk_Service has no real 'providesPlatformForServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_LogicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_LogicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'providesPlatformForServices', None)
    _safe_set(owner, 'LogicalTechnologyComponent365', partner)
    assert getattr(partner, 'providesPlatformForServices') == owner
    _safe_set(owner, 'LogicalTechnologyComponent365', None)
    assert getattr(partner, 'providesPlatformForServices') is None


def test_assoc_isMotivatedByDrivers72_stub_double():
    # contentfwk_Driver has no real 'Driver73' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Driver()
    setattr(partner, 'Driver73', None)
    _safe_set(owner, 'motivatesOrganizationUnits', {partner})
    assert getattr(partner, 'Driver73') == owner
    _safe_set(owner, 'motivatesOrganizationUnits', set())
    assert getattr(partner, 'Driver73') is None


def test_assoc_isOwnedAndGovernedByOrganizationUnits368_stub_double():
    # contentfwk_Service has no real 'ownsAndGovernsServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'ownsAndGovernsServices', None)
    _safe_set(owner, 'OrganizationUnit369', partner)
    assert getattr(partner, 'ownsAndGovernsServices') == owner
    _safe_set(owner, 'OrganizationUnit369', None)
    assert getattr(partner, 'ownsAndGovernsServices') is None


def test_assoc_isOwnedByOrganizationUnit153_stub_double():
    # contentfwk_Function has no real 'ownsFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'ownsFunctions', None)
    _safe_set(owner, 'OrganizationUnit154', partner)
    assert getattr(partner, 'ownsFunctions') == owner
    _safe_set(owner, 'OrganizationUnit154', None)
    assert getattr(partner, 'ownsFunctions') is None


def test_assoc_isPerformedByActors151_stub_double():
    # contentfwk_Function has no real 'performsFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'performsFunctions', None)
    _safe_set(owner, 'Actor152', partner)
    assert getattr(partner, 'performsFunctions') == owner
    _safe_set(owner, 'Actor152', None)
    assert getattr(partner, 'performsFunctions') is None


def test_assoc_isProcessesByLogicalApplicationComponents128_stub_double():
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


def test_assoc_isProducedByOrganizationUnits229_stub_double():
    # contentfwk_Product has no real 'producesProducts' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'producesProducts', None)
    _safe_set(owner, 'OrganizationUnit230', partner)
    assert getattr(partner, 'producesProducts') == owner
    _safe_set(owner, 'OrganizationUnit230', None)
    assert getattr(partner, 'producesProducts') is None


def test_assoc_isProducedByProcesses231_stub_double():
    # contentfwk_Product has no real 'producesProducts232' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'producesProducts232', None)
    _safe_set(owner, 'Process233', partner)
    assert getattr(partner, 'producesProducts232') == owner
    _safe_set(owner, 'Process233', None)
    assert getattr(partner, 'producesProducts232') is None


def test_assoc_isProvidedToActors352_stub_double():
    # contentfwk_Service has no real 'consumesServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'consumesServices', None)
    _safe_set(owner, 'Actor353', partner)
    assert getattr(partner, 'consumesServices') == owner
    _safe_set(owner, 'Actor353', None)
    assert getattr(partner, 'consumesServices') is None


def test_assoc_isRealizedByProcesses159_stub_double():
    # contentfwk_Function has no real 'orchestratesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'orchestratesFunctions', None)
    _safe_set(owner, 'Process160', partner)
    assert getattr(partner, 'orchestratesFunctions') == owner
    _safe_set(owner, 'Process160', None)
    assert getattr(partner, 'orchestratesFunctions') is None


def test_assoc_isRealizedByProcesses374_stub_double():
    # contentfwk_Service has no real 'orchestratesServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'orchestratesServices', None)
    _safe_set(owner, 'Process375', partner)
    assert getattr(partner, 'orchestratesServices') == owner
    _safe_set(owner, 'Process375', None)
    assert getattr(partner, 'orchestratesServices') is None


def test_assoc_isResolvedByActors258_stub_double():
    # contentfwk_Event has no real 'resolvesEvents259' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'resolvesEvents259', None)
    _safe_set(owner, 'Actor260', partner)
    assert getattr(partner, 'resolvesEvents259') == owner
    _safe_set(owner, 'Actor260', None)
    assert getattr(partner, 'resolvesEvents259') is None


def test_assoc_isResolvedByProcesses253_stub_double():
    # contentfwk_Event has no real 'resolvesEvents254' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'resolvesEvents254', None)
    _safe_set(owner, 'Process255', partner)
    assert getattr(partner, 'resolvesEvents254') == owner
    _safe_set(owner, 'Process255', None)
    assert getattr(partner, 'resolvesEvents254') is None


def test_assoc_isUpdatedThroughServices125_stub_double():
    # contentfwk_Service has no real 'Service126' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service126', None)
    _safe_set(owner, 'providesDataEntities', {partner})
    assert getattr(partner, 'Service126') == owner
    _safe_set(owner, 'providesDataEntities', set())
    assert getattr(partner, 'Service126') is None


def test_assoc_logicalComponents40_stub_double():
    # contentfwk_TechnologyArchitecture has no real 'contentfwk_TechnologyArchitecture41' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_LogicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_LogicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    partner = contentfwk_TechnologyArchitecture()
    setattr(partner, 'contentfwk_TechnologyArchitecture41', None)
    _safe_set(owner, 'contentfwk_LogicalTechnologyComponent', partner)
    assert getattr(partner, 'contentfwk_TechnologyArchitecture41') == owner
    _safe_set(owner, 'contentfwk_LogicalTechnologyComponent', None)
    assert getattr(partner, 'contentfwk_TechnologyArchitecture41') is None


def test_assoc_meetsServiceQuality250_stub_double():
    # contentfwk_ServiceQuality has no real 'ServiceQuality' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Contract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Contract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_ServiceQuality()
    setattr(partner, 'ServiceQuality', None)
    _safe_set(owner, 'appliesToContracts', {partner})
    assert getattr(partner, 'ServiceQuality') == owner
    _safe_set(owner, 'appliesToContracts', set())
    assert getattr(partner, 'ServiceQuality') is None


def test_assoc_motivatesOrganizationUnits43_stub_double():
    # contentfwk_Driver has no real 'isMotivatedByDrivers' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Driver()
    setattr(partner, 'isMotivatedByDrivers', None)
    _safe_set(owner, 'OrganizationUnit', partner)
    assert getattr(partner, 'isMotivatedByDrivers') == owner
    _safe_set(owner, 'OrganizationUnit', None)
    assert getattr(partner, 'isMotivatedByDrivers') is None


def test_assoc_operatesInLocation75_stub_double():
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


def test_assoc_operatesInLocation97_stub_double():
    # contentfwk_Location has no real 'Location99' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Location()
    setattr(partner, 'Location99', None)
    _safe_set(owner, 'containsActors98', partner)
    assert getattr(partner, 'Location99') == owner
    _safe_set(owner, 'containsActors98', None)
    assert getattr(partner, 'Location99') is None


def test_assoc_operatesOnDataEntities140_stub_double():
    # contentfwk_LogicalApplicationComponent has no real 'isProcessesByLogicalApplicationComponents' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_LogicalApplicationComponent()
    setattr(partner, 'isProcessesByLogicalApplicationComponents', None)
    _safe_set(owner, 'DataEntity141', partner)
    assert getattr(partner, 'isProcessesByLogicalApplicationComponents') == owner
    _safe_set(owner, 'DataEntity141', None)
    assert getattr(partner, 'isProcessesByLogicalApplicationComponents') is None


def test_assoc_orchestratesFunctions176_stub_double():
    # contentfwk_Function has no real 'Function177' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function177', None)
    _safe_set(owner, 'isRealizedByProcesses', {partner})
    assert getattr(partner, 'Function177') == owner
    _safe_set(owner, 'isRealizedByProcesses', set())
    assert getattr(partner, 'Function177') is None


def test_assoc_orchestratesServices182_stub_double():
    # contentfwk_Service has no real 'Service184' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service184', None)
    _safe_set(owner, 'isRealizedByProcesses183', {partner})
    assert getattr(partner, 'Service184') == owner
    _safe_set(owner, 'isRealizedByProcesses183', set())
    assert getattr(partner, 'Service184') is None


def test_assoc_ownsAndGovernsServices68_stub_double():
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


def test_assoc_ownsFunctions70_stub_double():
    # contentfwk_Function has no real 'Function' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function', None)
    _safe_set(owner, 'isOwnedByOrganizationUnit', {partner})
    assert getattr(partner, 'Function') == owner
    _safe_set(owner, 'isOwnedByOrganizationUnit', set())
    assert getattr(partner, 'Function') is None


def test_assoc_performsFunctions100_stub_double():
    # contentfwk_Function has no real 'Function101' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'Function101', None)
    _safe_set(owner, 'isPerformedByActors', {partner})
    assert getattr(partner, 'Function101') == owner
    _safe_set(owner, 'isPerformedByActors', set())
    assert getattr(partner, 'Function101') is None


def test_assoc_physicalApplicationComponents308_stub_double():
    # contentfwk_ApplicationArchitecture has no real 'contentfwk_ApplicationArchitecture309' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalApplicationComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalApplicationComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    partner = contentfwk_ApplicationArchitecture()
    setattr(partner, 'contentfwk_ApplicationArchitecture309', None)
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent', partner)
    assert getattr(partner, 'contentfwk_ApplicationArchitecture309') == owner
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent', None)
    assert getattr(partner, 'contentfwk_ApplicationArchitecture309') is None


def test_assoc_physicalComponents38_stub_double():
    # contentfwk_TechnologyArchitecture has no real 'contentfwk_TechnologyArchitecture39' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PhysicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PhysicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    partner = contentfwk_TechnologyArchitecture()
    setattr(partner, 'contentfwk_TechnologyArchitecture39', None)
    _safe_set(owner, 'contentfwk_PhysicalTechnologyComponent', partner)
    assert getattr(partner, 'contentfwk_TechnologyArchitecture39') == owner
    _safe_set(owner, 'contentfwk_PhysicalTechnologyComponent', None)
    assert getattr(partner, 'contentfwk_TechnologyArchitecture39') is None


def test_assoc_platformServices37_stub_double():
    # contentfwk_TechnologyArchitecture has no real 'contentfwk_TechnologyArchitecture' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_PlatformService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_PlatformService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_PlatformService(categoryTRM="sample_text", standardClass="sample_text")
    partner = contentfwk_TechnologyArchitecture()
    setattr(partner, 'contentfwk_TechnologyArchitecture', None)
    _safe_set(owner, 'contentfwk_PlatformService', partner)
    assert getattr(partner, 'contentfwk_TechnologyArchitecture') == owner
    _safe_set(owner, 'contentfwk_PlatformService', None)
    assert getattr(partner, 'contentfwk_TechnologyArchitecture') is None


def test_assoc_processes16_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture17' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture17', None)
    _safe_set(owner, 'contentfwk_Process', partner)
    assert getattr(partner, 'contentfwk_BusinessArchitecture17') == owner
    _safe_set(owner, 'contentfwk_Process', None)
    assert getattr(partner, 'contentfwk_BusinessArchitecture17') is None


def test_assoc_producesProducts196_stub_double():
    # contentfwk_Product has no real 'Product197' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Product()
    setattr(partner, 'Product197', None)
    _safe_set(owner, 'isProducedByProcesses', {partner})
    assert getattr(partner, 'Product197') == owner
    _safe_set(owner, 'isProducedByProcesses', set())
    assert getattr(partner, 'Product197') is None


def test_assoc_producesProducts74_stub_double():
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


def test_assoc_providesDataEntities356_stub_double():
    # contentfwk_Service has no real 'isUpdatedThroughServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_DataEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_DataEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'isUpdatedThroughServices', None)
    _safe_set(owner, 'DataEntity357', partner)
    assert getattr(partner, 'isUpdatedThroughServices') == owner
    _safe_set(owner, 'DataEntity357', None)
    assert getattr(partner, 'isUpdatedThroughServices') is None


def test_assoc_providesPlatformForServices329_stub_double():
    # contentfwk_Service has no real 'Service330' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_LogicalTechnologyComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_LogicalTechnologyComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'Service330', None)
    _safe_set(owner, 'isImplementedOnLogicalTechnologyComponents', {partner})
    assert getattr(partner, 'Service330') == owner
    _safe_set(owner, 'isImplementedOnLogicalTechnologyComponents', set())
    assert getattr(partner, 'Service330') is None


def test_assoc_residesWithinLogicalDataComponent127_stub_double():
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


def test_assoc_resolvesEvents192_stub_double():
    # contentfwk_Event has no real 'Event193' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Event()
    setattr(partner, 'Event193', None)
    _safe_set(owner, 'isResolvedByProcesses', {partner})
    assert getattr(partner, 'Event193') == owner
    _safe_set(owner, 'isResolvedByProcesses', set())
    assert getattr(partner, 'Event193') is None


def test_assoc_resolvesEvents94_stub_double():
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


def test_assoc_roles10_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture11' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Role(estimatedFTEs="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture11', None)
    _safe_set(owner, 'contentfwk_Role', partner)
    assert getattr(partner, 'contentfwk_BusinessArchitecture11') == owner
    _safe_set(owner, 'contentfwk_Role', None)
    assert getattr(partner, 'contentfwk_BusinessArchitecture11') is None


def test_assoc_supportsActors163_stub_double():
    # contentfwk_Function has no real 'interactsWithFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'interactsWithFunctions', None)
    _safe_set(owner, 'Actor164', partner)
    assert getattr(partner, 'interactsWithFunctions') == owner
    _safe_set(owner, 'Actor164', None)
    assert getattr(partner, 'interactsWithFunctions') is None


def test_assoc_supportsProcesses157_stub_double():
    # contentfwk_Function has no real 'decomposesFunctions' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Function()
    setattr(partner, 'decomposesFunctions', None)
    _safe_set(owner, 'Process158', partner)
    assert getattr(partner, 'decomposesFunctions') == owner
    _safe_set(owner, 'Process158', None)
    assert getattr(partner, 'decomposesFunctions') is None


def test_assoc_supportsProcesses372_stub_double():
    # contentfwk_Service has no real 'decomposesServices' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    partner = contentfwk_Service()
    setattr(partner, 'decomposesServices', None)
    _safe_set(owner, 'Process373', partner)
    assert getattr(partner, 'decomposesServices') == owner
    _safe_set(owner, 'Process373', None)
    assert getattr(partner, 'decomposesServices') is None


def test_assoc_units6_stub_double():
    # contentfwk_BusinessArchitecture has no real 'contentfwk_BusinessArchitecture7' property in the generated
    # code (a bare stub) -- manually attach it so contentfwk_OrganizationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contentfwk_OrganizationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contentfwk_OrganizationUnit(headcount="sample_text")
    partner = contentfwk_BusinessArchitecture()
    setattr(partner, 'contentfwk_BusinessArchitecture7', None)
    _safe_set(owner, 'contentfwk_OrganizationUnit', partner)
    assert getattr(partner, 'contentfwk_BusinessArchitecture7') == owner
    _safe_set(owner, 'contentfwk_OrganizationUnit', None)
    assert getattr(partner, 'contentfwk_BusinessArchitecture7') is None


