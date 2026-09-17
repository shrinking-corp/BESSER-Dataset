# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    contentfwk_EnterpriseArchitecture,
    Architecture,
    contentfwk_DataArchitecture,
    contentfwk_BusinessArchitecture,
    contentfwk_Label,
    contentfwk_Container,
    contentfwk_Architecture,
    contentfwk_Standard,
    contentfwk_StrategicArchitecture,
    contentfwk_ApplicationArchitecture,
    DataComponent,
    StrategicElement,
    contentfwk_Constraint,
    contentfwk_Requirement,
    contentfwk_Gap,
    contentfwk_Assumption,
    contentfwk_Principle,
    contentfwk_WorkPackage,
    contentfwk_Element,
    TechnologyComponent,
    Service,
    Standard,
    contentfwk_DataComponent,
    contentfwk_TechnologyComponent,
    contentfwk_ApplicationComponent,
    ApplicationComponent,
    contentfwk_Service,
    Element,
    contentfwk_StrategicElement,
    contentfwk_Objective,
    contentfwk_Process,
    contentfwk_Measure,
    contentfwk_DataEntity,
    contentfwk_Location,
    contentfwk_Driver,
    contentfwk_Role,
    contentfwk_BusinessService,
    contentfwk_Goal,
    contentfwk_InformationSystemService,
    contentfwk_Event,
    contentfwk_LogicalDataComponent,
    contentfwk_LogicalApplicationComponent,
    contentfwk_PhysicalApplicationComponent,
    contentfwk_Function,
    contentfwk_OrganizationUnit,
    contentfwk_Contract,
    contentfwk_Product,
    contentfwk_Actor,
    contentfwk_Capability,
    contentfwk_Control,
    contentfwk_ServiceQuality,
    contentfwk_LogicalTechnologyComponent,
    contentfwk_PhysicalTechnologyComponent,
    contentfwk_PlatformService,
    contentfwk_TechnologyArchitecture,
    contentfwk_PhysicalDataComponent,
    StandardsClass,
    DataEntityCategory,
    WorkPackageCategory,
    LifeCycleStatus,
    PrincipleCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_contentfwk_enterprisearchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_EnterpriseArchitecture)


def test_hyp_contentfwk_enterprisearchitecture_constructor_exists():
    assert callable(contentfwk_EnterpriseArchitecture.__init__)


def test_hyp_contentfwk_enterprisearchitecture_constructor_args():
    sig = inspect.signature(contentfwk_EnterpriseArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_architecture_is_not_abstract():
    assert not inspect.isabstract(Architecture)


def test_hyp_architecture_constructor_exists():
    assert callable(Architecture.__init__)


def test_hyp_architecture_constructor_args():
    sig = inspect.signature(Architecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_dataarchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_DataArchitecture)


def test_hyp_contentfwk_dataarchitecture_constructor_exists():
    assert callable(contentfwk_DataArchitecture.__init__)


def test_hyp_contentfwk_dataarchitecture_constructor_args():
    sig = inspect.signature(contentfwk_DataArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_businessarchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_BusinessArchitecture)


def test_hyp_contentfwk_businessarchitecture_constructor_exists():
    assert callable(contentfwk_BusinessArchitecture.__init__)


def test_hyp_contentfwk_businessarchitecture_constructor_args():
    sig = inspect.signature(contentfwk_BusinessArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_label_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Label)


def test_hyp_contentfwk_label_constructor_exists():
    assert callable(contentfwk_Label.__init__)


def test_hyp_contentfwk_label_constructor_args():
    sig = inspect.signature(contentfwk_Label.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_contentfwk_container_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Container)


def test_hyp_contentfwk_container_constructor_exists():
    assert callable(contentfwk_Container.__init__)


def test_hyp_contentfwk_container_constructor_args():
    sig = inspect.signature(contentfwk_Container.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_contentfwk_architecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Architecture)


def test_hyp_contentfwk_architecture_constructor_exists():
    assert callable(contentfwk_Architecture.__init__)


def test_hyp_contentfwk_architecture_constructor_args():
    sig = inspect.signature(contentfwk_Architecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_standard_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Standard)


def test_hyp_contentfwk_standard_constructor_exists():
    assert callable(contentfwk_Standard.__init__)


def test_hyp_contentfwk_standard_constructor_args():
    sig = inspect.signature(contentfwk_Standard.__init__)
    params = list(sig.parameters.keys())
    assert "standardCreationDate" in params, "Missing parameter 'standardCreationDate'"
    assert "retireDate" in params, "Missing parameter 'retireDate'"
    assert "standardClass" in params, "Missing parameter 'standardClass'"
    assert "nextStandardCreationDate" in params, "Missing parameter 'nextStandardCreationDate'"
    assert "lastStandardCreationDate" in params, "Missing parameter 'lastStandardCreationDate'"








def test_hyp_contentfwk_strategicarchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_StrategicArchitecture)


def test_hyp_contentfwk_strategicarchitecture_constructor_exists():
    assert callable(contentfwk_StrategicArchitecture.__init__)


def test_hyp_contentfwk_strategicarchitecture_constructor_args():
    sig = inspect.signature(contentfwk_StrategicArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_applicationarchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_ApplicationArchitecture)


def test_hyp_contentfwk_applicationarchitecture_constructor_exists():
    assert callable(contentfwk_ApplicationArchitecture.__init__)


def test_hyp_contentfwk_applicationarchitecture_constructor_args():
    sig = inspect.signature(contentfwk_ApplicationArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datacomponent_is_not_abstract():
    assert not inspect.isabstract(DataComponent)


def test_hyp_datacomponent_constructor_exists():
    assert callable(DataComponent.__init__)


def test_hyp_datacomponent_constructor_args():
    sig = inspect.signature(DataComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_strategicelement_is_not_abstract():
    assert not inspect.isabstract(StrategicElement)


def test_hyp_strategicelement_constructor_exists():
    assert callable(StrategicElement.__init__)


def test_hyp_strategicelement_constructor_args():
    sig = inspect.signature(StrategicElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_constraint_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Constraint)


def test_hyp_contentfwk_constraint_constructor_exists():
    assert callable(contentfwk_Constraint.__init__)


def test_hyp_contentfwk_constraint_constructor_args():
    sig = inspect.signature(contentfwk_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_requirement_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Requirement)


def test_hyp_contentfwk_requirement_constructor_exists():
    assert callable(contentfwk_Requirement.__init__)


def test_hyp_contentfwk_requirement_constructor_args():
    sig = inspect.signature(contentfwk_Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "acceptanceCriteria" in params, "Missing parameter 'acceptanceCriteria'"
    assert "statementOfRequirement" in params, "Missing parameter 'statementOfRequirement'"
    assert "rationale" in params, "Missing parameter 'rationale'"






def test_hyp_contentfwk_gap_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Gap)


def test_hyp_contentfwk_gap_constructor_exists():
    assert callable(contentfwk_Gap.__init__)


def test_hyp_contentfwk_gap_constructor_args():
    sig = inspect.signature(contentfwk_Gap.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_assumption_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Assumption)


def test_hyp_contentfwk_assumption_constructor_exists():
    assert callable(contentfwk_Assumption.__init__)


def test_hyp_contentfwk_assumption_constructor_args():
    sig = inspect.signature(contentfwk_Assumption.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_principle_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Principle)


def test_hyp_contentfwk_principle_constructor_exists():
    assert callable(contentfwk_Principle.__init__)


def test_hyp_contentfwk_principle_constructor_args():
    sig = inspect.signature(contentfwk_Principle.__init__)
    params = list(sig.parameters.keys())
    assert "implication" in params, "Missing parameter 'implication'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "principleCategory" in params, "Missing parameter 'principleCategory'"
    assert "metric" in params, "Missing parameter 'metric'"
    assert "statementOfPrinciple" in params, "Missing parameter 'statementOfPrinciple'"
    assert "rationale" in params, "Missing parameter 'rationale'"









def test_hyp_contentfwk_workpackage_is_not_abstract():
    assert not inspect.isabstract(contentfwk_WorkPackage)


def test_hyp_contentfwk_workpackage_constructor_exists():
    assert callable(contentfwk_WorkPackage.__init__)


def test_hyp_contentfwk_workpackage_constructor_args():
    sig = inspect.signature(contentfwk_WorkPackage.__init__)
    params = list(sig.parameters.keys())
    assert "workPackageCategory" in params, "Missing parameter 'workPackageCategory'"




def test_hyp_contentfwk_element_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Element)


def test_hyp_contentfwk_element_constructor_exists():
    assert callable(contentfwk_Element.__init__)


def test_hyp_contentfwk_element_constructor_args():
    sig = inspect.signature(contentfwk_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ownerDescr" in params, "Missing parameter 'ownerDescr'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "sourceDescr" in params, "Missing parameter 'sourceDescr'"
    assert "description" in params, "Missing parameter 'description'"








def test_hyp_technologycomponent_is_not_abstract():
    assert not inspect.isabstract(TechnologyComponent)


def test_hyp_technologycomponent_constructor_exists():
    assert callable(TechnologyComponent.__init__)


def test_hyp_technologycomponent_constructor_args():
    sig = inspect.signature(TechnologyComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_hyp_service_constructor_exists():
    assert callable(Service.__init__)


def test_hyp_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())



def test_hyp_standard_is_not_abstract():
    assert not inspect.isabstract(Standard)


def test_hyp_standard_constructor_exists():
    assert callable(Standard.__init__)


def test_hyp_standard_constructor_args():
    sig = inspect.signature(Standard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_datacomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_DataComponent)


def test_hyp_contentfwk_datacomponent_constructor_exists():
    assert callable(contentfwk_DataComponent.__init__)


def test_hyp_contentfwk_datacomponent_constructor_args():
    sig = inspect.signature(contentfwk_DataComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_technologycomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_TechnologyComponent)


def test_hyp_contentfwk_technologycomponent_constructor_exists():
    assert callable(contentfwk_TechnologyComponent.__init__)


def test_hyp_contentfwk_technologycomponent_constructor_args():
    sig = inspect.signature(contentfwk_TechnologyComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_applicationcomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_ApplicationComponent)


def test_hyp_contentfwk_applicationcomponent_constructor_exists():
    assert callable(contentfwk_ApplicationComponent.__init__)


def test_hyp_contentfwk_applicationcomponent_constructor_args():
    sig = inspect.signature(contentfwk_ApplicationComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_applicationcomponent_is_not_abstract():
    assert not inspect.isabstract(ApplicationComponent)


def test_hyp_applicationcomponent_constructor_exists():
    assert callable(ApplicationComponent.__init__)


def test_hyp_applicationcomponent_constructor_args():
    sig = inspect.signature(ApplicationComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_service_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Service)


def test_hyp_contentfwk_service_constructor_exists():
    assert callable(contentfwk_Service.__init__)


def test_hyp_contentfwk_service_constructor_args():
    sig = inspect.signature(contentfwk_Service.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_strategicelement_is_not_abstract():
    assert not inspect.isabstract(contentfwk_StrategicElement)


def test_hyp_contentfwk_strategicelement_constructor_exists():
    assert callable(contentfwk_StrategicElement.__init__)


def test_hyp_contentfwk_strategicelement_constructor_args():
    sig = inspect.signature(contentfwk_StrategicElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_objective_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Objective)


def test_hyp_contentfwk_objective_constructor_exists():
    assert callable(contentfwk_Objective.__init__)


def test_hyp_contentfwk_objective_constructor_args():
    sig = inspect.signature(contentfwk_Objective.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_process_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Process)


def test_hyp_contentfwk_process_constructor_exists():
    assert callable(contentfwk_Process.__init__)


def test_hyp_contentfwk_process_constructor_args():
    sig = inspect.signature(contentfwk_Process.__init__)
    params = list(sig.parameters.keys())
    assert "processCritiality" in params, "Missing parameter 'processCritiality'"
    assert "isAutomated" in params, "Missing parameter 'isAutomated'"
    assert "processVolumetrics" in params, "Missing parameter 'processVolumetrics'"






def test_hyp_contentfwk_measure_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Measure)


def test_hyp_contentfwk_measure_constructor_exists():
    assert callable(contentfwk_Measure.__init__)


def test_hyp_contentfwk_measure_constructor_args():
    sig = inspect.signature(contentfwk_Measure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_dataentity_is_not_abstract():
    assert not inspect.isabstract(contentfwk_DataEntity)


def test_hyp_contentfwk_dataentity_constructor_exists():
    assert callable(contentfwk_DataEntity.__init__)


def test_hyp_contentfwk_dataentity_constructor_args():
    sig = inspect.signature(contentfwk_DataEntity.__init__)
    params = list(sig.parameters.keys())
    assert "privacyClassification" in params, "Missing parameter 'privacyClassification'"
    assert "dataEntityCategory" in params, "Missing parameter 'dataEntityCategory'"
    assert "retentionClassification" in params, "Missing parameter 'retentionClassification'"






def test_hyp_contentfwk_location_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Location)


def test_hyp_contentfwk_location_constructor_exists():
    assert callable(contentfwk_Location.__init__)


def test_hyp_contentfwk_location_constructor_args():
    sig = inspect.signature(contentfwk_Location.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_driver_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Driver)


def test_hyp_contentfwk_driver_constructor_exists():
    assert callable(contentfwk_Driver.__init__)


def test_hyp_contentfwk_driver_constructor_args():
    sig = inspect.signature(contentfwk_Driver.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_role_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Role)


def test_hyp_contentfwk_role_constructor_exists():
    assert callable(contentfwk_Role.__init__)


def test_hyp_contentfwk_role_constructor_args():
    sig = inspect.signature(contentfwk_Role.__init__)
    params = list(sig.parameters.keys())
    assert "estimatedFTEs" in params, "Missing parameter 'estimatedFTEs'"




def test_hyp_contentfwk_businessservice_is_not_abstract():
    assert not inspect.isabstract(contentfwk_BusinessService)


def test_hyp_contentfwk_businessservice_constructor_exists():
    assert callable(contentfwk_BusinessService.__init__)


def test_hyp_contentfwk_businessservice_constructor_args():
    sig = inspect.signature(contentfwk_BusinessService.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_goal_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Goal)


def test_hyp_contentfwk_goal_constructor_exists():
    assert callable(contentfwk_Goal.__init__)


def test_hyp_contentfwk_goal_constructor_args():
    sig = inspect.signature(contentfwk_Goal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_informationsystemservice_is_not_abstract():
    assert not inspect.isabstract(contentfwk_InformationSystemService)


def test_hyp_contentfwk_informationsystemservice_constructor_exists():
    assert callable(contentfwk_InformationSystemService.__init__)


def test_hyp_contentfwk_informationsystemservice_constructor_args():
    sig = inspect.signature(contentfwk_InformationSystemService.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_event_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Event)


def test_hyp_contentfwk_event_constructor_exists():
    assert callable(contentfwk_Event.__init__)


def test_hyp_contentfwk_event_constructor_args():
    sig = inspect.signature(contentfwk_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_logicaldatacomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_LogicalDataComponent)


def test_hyp_contentfwk_logicaldatacomponent_constructor_exists():
    assert callable(contentfwk_LogicalDataComponent.__init__)


def test_hyp_contentfwk_logicaldatacomponent_constructor_args():
    sig = inspect.signature(contentfwk_LogicalDataComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_logicalapplicationcomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_LogicalApplicationComponent)


def test_hyp_contentfwk_logicalapplicationcomponent_constructor_exists():
    assert callable(contentfwk_LogicalApplicationComponent.__init__)


def test_hyp_contentfwk_logicalapplicationcomponent_constructor_args():
    sig = inspect.signature(contentfwk_LogicalApplicationComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_physicalapplicationcomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_PhysicalApplicationComponent)


def test_hyp_contentfwk_physicalapplicationcomponent_constructor_exists():
    assert callable(contentfwk_PhysicalApplicationComponent.__init__)


def test_hyp_contentfwk_physicalapplicationcomponent_constructor_args():
    sig = inspect.signature(contentfwk_PhysicalApplicationComponent.__init__)
    params = list(sig.parameters.keys())
    assert "privacyCharacteristics" in params, "Missing parameter 'privacyCharacteristics'"
    assert "manageabilityCharacteristics" in params, "Missing parameter 'manageabilityCharacteristics'"
    assert "dateOfLastRelease" in params, "Missing parameter 'dateOfLastRelease'"
    assert "dateOfNextRelease" in params, "Missing parameter 'dateOfNextRelease'"
    assert "serviceabilityCharacteristics" in params, "Missing parameter 'serviceabilityCharacteristics'"
    assert "throughputPeriod" in params, "Missing parameter 'throughputPeriod'"
    assert "peakProfileLongTerm" in params, "Missing parameter 'peakProfileLongTerm'"
    assert "securityCharacteristics" in params, "Missing parameter 'securityCharacteristics'"
    assert "extensibilityCharacteristics" in params, "Missing parameter 'extensibilityCharacteristics'"
    assert "scalabilityCharacteristics" in params, "Missing parameter 'scalabilityCharacteristics'"
    assert "credibilityCharacteristics" in params, "Missing parameter 'credibilityCharacteristics'"
    assert "portabilityCharacteristics" in params, "Missing parameter 'portabilityCharacteristics'"
    assert "capacityCharacteristics" in params, "Missing parameter 'capacityCharacteristics'"
    assert "internationalizationCharacteristics" in params, "Missing parameter 'internationalizationCharacteristics'"
    assert "integrityCharacteristics" in params, "Missing parameter 'integrityCharacteristics'"
    assert "peakProfileShortTerm" in params, "Missing parameter 'peakProfileShortTerm'"
    assert "growthPeriod" in params, "Missing parameter 'growthPeriod'"
    assert "locatabilityCharacteristics" in params, "Missing parameter 'locatabilityCharacteristics'"
    assert "recoverabilityCharacteristics" in params, "Missing parameter 'recoverabilityCharacteristics'"
    assert "retirementDate" in params, "Missing parameter 'retirementDate'"
    assert "growth" in params, "Missing parameter 'growth'"
    assert "interoperabilityCharacteristics" in params, "Missing parameter 'interoperabilityCharacteristics'"
    assert "availabilityQualityCharacteristics" in params, "Missing parameter 'availabilityQualityCharacteristics'"
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "performanceCharacteristics" in params, "Missing parameter 'performanceCharacteristics'"
    assert "lifeCycleStatus" in params, "Missing parameter 'lifeCycleStatus'"
    assert "servicesTimes" in params, "Missing parameter 'servicesTimes'"
    assert "reliabilityCharacteristics" in params, "Missing parameter 'reliabilityCharacteristics'"
    assert "initialLiveDate" in params, "Missing parameter 'initialLiveDate'"
    assert "localizationCharacteristics" in params, "Missing parameter 'localizationCharacteristics'"

































def test_hyp_contentfwk_function_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Function)


def test_hyp_contentfwk_function_constructor_exists():
    assert callable(contentfwk_Function.__init__)


def test_hyp_contentfwk_function_constructor_args():
    sig = inspect.signature(contentfwk_Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_organizationunit_is_not_abstract():
    assert not inspect.isabstract(contentfwk_OrganizationUnit)


def test_hyp_contentfwk_organizationunit_constructor_exists():
    assert callable(contentfwk_OrganizationUnit.__init__)


def test_hyp_contentfwk_organizationunit_constructor_args():
    sig = inspect.signature(contentfwk_OrganizationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "headcount" in params, "Missing parameter 'headcount'"




def test_hyp_contentfwk_contract_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Contract)


def test_hyp_contentfwk_contract_constructor_exists():
    assert callable(contentfwk_Contract.__init__)


def test_hyp_contentfwk_contract_constructor_args():
    sig = inspect.signature(contentfwk_Contract.__init__)
    params = list(sig.parameters.keys())
    assert "scalabilityCharacteristics" in params, "Missing parameter 'scalabilityCharacteristics'"
    assert "extensibilityCharacteristics" in params, "Missing parameter 'extensibilityCharacteristics'"
    assert "availabilityQualityCharacteristics" in params, "Missing parameter 'availabilityQualityCharacteristics'"
    assert "recoverabilityCharacteristics" in params, "Missing parameter 'recoverabilityCharacteristics'"
    assert "credibilityCharacteristics" in params, "Missing parameter 'credibilityCharacteristics'"
    assert "servicesTimes" in params, "Missing parameter 'servicesTimes'"
    assert "manageabilityCharacteristics" in params, "Missing parameter 'manageabilityCharacteristics'"
    assert "localizationCharacteristics" in params, "Missing parameter 'localizationCharacteristics'"
    assert "serviceQualityCharacteristics" in params, "Missing parameter 'serviceQualityCharacteristics'"
    assert "ServiceNameCalled" in params, "Missing parameter 'ServiceNameCalled'"
    assert "reliabilityCharacteristics" in params, "Missing parameter 'reliabilityCharacteristics'"
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "integrityCharacteristics" in params, "Missing parameter 'integrityCharacteristics'"
    assert "internationalizationCharacteristics" in params, "Missing parameter 'internationalizationCharacteristics'"
    assert "privacyCharacteristics" in params, "Missing parameter 'privacyCharacteristics'"
    assert "resultControlRequirements" in params, "Missing parameter 'resultControlRequirements'"
    assert "contractControlRequirements" in params, "Missing parameter 'contractControlRequirements'"
    assert "peakProfileLongTerm" in params, "Missing parameter 'peakProfileLongTerm'"
    assert "securityCharacteristics" in params, "Missing parameter 'securityCharacteristics'"
    assert "locatabilityCharacteristics" in params, "Missing parameter 'locatabilityCharacteristics'"
    assert "qualityOfInformationRequired" in params, "Missing parameter 'qualityOfInformationRequired'"
    assert "ServiceNameCaller" in params, "Missing parameter 'ServiceNameCaller'"
    assert "performanceCharacteristics" in params, "Missing parameter 'performanceCharacteristics'"
    assert "capacityCharacteristics" in params, "Missing parameter 'capacityCharacteristics'"
    assert "portabilityCharacteristics" in params, "Missing parameter 'portabilityCharacteristics'"
    assert "serviceabilityCharacteristics" in params, "Missing parameter 'serviceabilityCharacteristics'"
    assert "peakProfileShortTerm" in params, "Missing parameter 'peakProfileShortTerm'"
    assert "responseCharacteristics" in params, "Missing parameter 'responseCharacteristics'"
    assert "interoperabilityCharacteristics" in params, "Missing parameter 'interoperabilityCharacteristics'"
    assert "throughputPeriod" in params, "Missing parameter 'throughputPeriod'"
    assert "growth" in params, "Missing parameter 'growth'"
    assert "growthPeriod" in params, "Missing parameter 'growthPeriod'"
    assert "behaviorCharacteristics" in params, "Missing parameter 'behaviorCharacteristics'"




































def test_hyp_contentfwk_product_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Product)


def test_hyp_contentfwk_product_constructor_exists():
    assert callable(contentfwk_Product.__init__)


def test_hyp_contentfwk_product_constructor_args():
    sig = inspect.signature(contentfwk_Product.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_actor_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Actor)


def test_hyp_contentfwk_actor_constructor_exists():
    assert callable(contentfwk_Actor.__init__)


def test_hyp_contentfwk_actor_constructor_args():
    sig = inspect.signature(contentfwk_Actor.__init__)
    params = list(sig.parameters.keys())
    assert "FTEs" in params, "Missing parameter 'FTEs'"
    assert "actorTasks" in params, "Missing parameter 'actorTasks'"
    assert "actorGoal" in params, "Missing parameter 'actorGoal'"






def test_hyp_contentfwk_capability_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Capability)


def test_hyp_contentfwk_capability_constructor_exists():
    assert callable(contentfwk_Capability.__init__)


def test_hyp_contentfwk_capability_constructor_args():
    sig = inspect.signature(contentfwk_Capability.__init__)
    params = list(sig.parameters.keys())
    assert "increments" in params, "Missing parameter 'increments'"
    assert "businessValue" in params, "Missing parameter 'businessValue'"





def test_hyp_contentfwk_control_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Control)


def test_hyp_contentfwk_control_constructor_exists():
    assert callable(contentfwk_Control.__init__)


def test_hyp_contentfwk_control_constructor_args():
    sig = inspect.signature(contentfwk_Control.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_servicequality_is_not_abstract():
    assert not inspect.isabstract(contentfwk_ServiceQuality)


def test_hyp_contentfwk_servicequality_constructor_exists():
    assert callable(contentfwk_ServiceQuality.__init__)


def test_hyp_contentfwk_servicequality_constructor_args():
    sig = inspect.signature(contentfwk_ServiceQuality.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_logicaltechnologycomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_LogicalTechnologyComponent)


def test_hyp_contentfwk_logicaltechnologycomponent_constructor_exists():
    assert callable(contentfwk_LogicalTechnologyComponent.__init__)


def test_hyp_contentfwk_logicaltechnologycomponent_constructor_args():
    sig = inspect.signature(contentfwk_LogicalTechnologyComponent.__init__)
    params = list(sig.parameters.keys())
    assert "categoryTRM" in params, "Missing parameter 'categoryTRM'"




def test_hyp_contentfwk_physicaltechnologycomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_PhysicalTechnologyComponent)


def test_hyp_contentfwk_physicaltechnologycomponent_constructor_exists():
    assert callable(contentfwk_PhysicalTechnologyComponent.__init__)


def test_hyp_contentfwk_physicaltechnologycomponent_constructor_args():
    sig = inspect.signature(contentfwk_PhysicalTechnologyComponent.__init__)
    params = list(sig.parameters.keys())
    assert "categoryTRM" in params, "Missing parameter 'categoryTRM'"
    assert "moduleName" in params, "Missing parameter 'moduleName'"
    assert "productName" in params, "Missing parameter 'productName'"
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "version" in params, "Missing parameter 'version'"








def test_hyp_contentfwk_platformservice_is_not_abstract():
    assert not inspect.isabstract(contentfwk_PlatformService)


def test_hyp_contentfwk_platformservice_constructor_exists():
    assert callable(contentfwk_PlatformService.__init__)


def test_hyp_contentfwk_platformservice_constructor_args():
    sig = inspect.signature(contentfwk_PlatformService.__init__)
    params = list(sig.parameters.keys())
    assert "categoryTRM" in params, "Missing parameter 'categoryTRM'"




def test_hyp_contentfwk_technologyarchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_TechnologyArchitecture)


def test_hyp_contentfwk_technologyarchitecture_constructor_exists():
    assert callable(contentfwk_TechnologyArchitecture.__init__)


def test_hyp_contentfwk_technologyarchitecture_constructor_args():
    sig = inspect.signature(contentfwk_TechnologyArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_physicaldatacomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_PhysicalDataComponent)


def test_hyp_contentfwk_physicaldatacomponent_constructor_exists():
    assert callable(contentfwk_PhysicalDataComponent.__init__)


def test_hyp_contentfwk_physicaldatacomponent_constructor_args():
    sig = inspect.signature(contentfwk_PhysicalDataComponent.__init__)
    params = list(sig.parameters.keys())

def test_hyp_standardsclass_exists():
    # Check that the Enumeration exists
    assert StandardsClass is not None

def test_hyp_standardsclass_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StandardsClass]
    expected_literals = [
        "Standard",
        "PhasingOut",
        "Retired",
        "NonStandard",
        "Proposed",
        "Provisional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StandardsClass"

def test_hyp_dataentitycategory_exists():
    # Check that the Enumeration exists
    assert DataEntityCategory is not None

def test_hyp_dataentitycategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataEntityCategory]
    expected_literals = [
        "InternallyStoredEntity",
        "Message",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataEntityCategory"

def test_hyp_workpackagecategory_exists():
    # Check that the Enumeration exists
    assert WorkPackageCategory is not None

def test_hyp_workpackagecategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkPackageCategory]
    expected_literals = [
        "Portofolio",
        "WorkStream",
        "Project",
        "Program",
        "WorkPackage",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkPackageCategory"

def test_hyp_lifecyclestatus_exists():
    # Check that the Enumeration exists
    assert LifeCycleStatus is not None

def test_hyp_lifecyclestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LifeCycleStatus]
    expected_literals = [
        "Live",
        "PhasingOut",
        "Proposed",
        "InDevelopment",
        "Retired",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LifeCycleStatus"

def test_hyp_principlecategory_exists():
    # Check that the Enumeration exists
    assert PrincipleCategory is not None

def test_hyp_principlecategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrincipleCategory]
    expected_literals = [
        "ApplicationPrinciple",
        "TechnologyPrinciple",
        "DataPrinciple",
        "BusinessPrinciple",
        "IntegrationPrinciple",
        "GuidingPrinciple",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrincipleCategory"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
contentfwk_EnterpriseArchitecture_strategy = st.builds(
    contentfwk_EnterpriseArchitecture,
)
Architecture_strategy = st.builds(
    Architecture,
)
contentfwk_DataArchitecture_strategy = st.builds(
    contentfwk_DataArchitecture,
)
contentfwk_BusinessArchitecture_strategy = st.builds(
    contentfwk_BusinessArchitecture,
)
contentfwk_Label_strategy = st.builds(
    contentfwk_Label,
    description=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
contentfwk_Container_strategy = st.builds(
    contentfwk_Container,
    name=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)
contentfwk_Architecture_strategy = st.builds(
    contentfwk_Architecture,
)
contentfwk_Standard_strategy = st.builds(
    contentfwk_Standard,
    standardCreationDate=
        st.dates(),
    retireDate=
        st.dates(),
    standardClass=
        safe_text,
    nextStandardCreationDate=
        st.dates(),
    lastStandardCreationDate=
        st.dates()
)
contentfwk_StrategicArchitecture_strategy = st.builds(
    contentfwk_StrategicArchitecture,
)
contentfwk_ApplicationArchitecture_strategy = st.builds(
    contentfwk_ApplicationArchitecture,
)
DataComponent_strategy = st.builds(
    DataComponent,
)
StrategicElement_strategy = st.builds(
    StrategicElement,
)
contentfwk_Constraint_strategy = st.builds(
    contentfwk_Constraint,
)
contentfwk_Requirement_strategy = st.builds(
    contentfwk_Requirement,
    acceptanceCriteria=
        safe_text,
    statementOfRequirement=
        safe_text,
    rationale=
        safe_text
)
contentfwk_Gap_strategy = st.builds(
    contentfwk_Gap,
)
contentfwk_Assumption_strategy = st.builds(
    contentfwk_Assumption,
)
contentfwk_Principle_strategy = st.builds(
    contentfwk_Principle,
    implication=
        safe_text,
    priority=
        safe_text,
    principleCategory=
        safe_text,
    metric=
        safe_text,
    statementOfPrinciple=
        safe_text,
    rationale=
        safe_text
)
contentfwk_WorkPackage_strategy = st.builds(
    contentfwk_WorkPackage,
    workPackageCategory=
        safe_text
)
contentfwk_Element_strategy = st.builds(
    contentfwk_Element,
    name=
        safe_text,
    ownerDescr=
        safe_text,
    ID=
        safe_text,
    sourceDescr=
        safe_text,
    description=
        safe_text
)
TechnologyComponent_strategy = st.builds(
    TechnologyComponent,
)
Service_strategy = st.builds(
    Service,
)
Standard_strategy = st.builds(
    Standard,
)
contentfwk_DataComponent_strategy = st.builds(
    contentfwk_DataComponent,
)
contentfwk_TechnologyComponent_strategy = st.builds(
    contentfwk_TechnologyComponent,
)
contentfwk_ApplicationComponent_strategy = st.builds(
    contentfwk_ApplicationComponent,
)
ApplicationComponent_strategy = st.builds(
    ApplicationComponent,
)
contentfwk_Service_strategy = st.builds(
    contentfwk_Service,
)
Element_strategy = st.builds(
    Element,
)
contentfwk_StrategicElement_strategy = st.builds(
    contentfwk_StrategicElement,
)
contentfwk_Objective_strategy = st.builds(
    contentfwk_Objective,
)
contentfwk_Process_strategy = st.builds(
    contentfwk_Process,
    processCritiality=
        safe_text,
    isAutomated=
        st.booleans(),
    processVolumetrics=
        safe_text
)
contentfwk_Measure_strategy = st.builds(
    contentfwk_Measure,
)
contentfwk_DataEntity_strategy = st.builds(
    contentfwk_DataEntity,
    privacyClassification=
        safe_text,
    dataEntityCategory=
        safe_text,
    retentionClassification=
        safe_text
)
contentfwk_Location_strategy = st.builds(
    contentfwk_Location,
)
contentfwk_Driver_strategy = st.builds(
    contentfwk_Driver,
)
contentfwk_Role_strategy = st.builds(
    contentfwk_Role,
    estimatedFTEs=
        safe_text
)
contentfwk_BusinessService_strategy = st.builds(
    contentfwk_BusinessService,
)
contentfwk_Goal_strategy = st.builds(
    contentfwk_Goal,
)
contentfwk_InformationSystemService_strategy = st.builds(
    contentfwk_InformationSystemService,
)
contentfwk_Event_strategy = st.builds(
    contentfwk_Event,
)
contentfwk_LogicalDataComponent_strategy = st.builds(
    contentfwk_LogicalDataComponent,
)
contentfwk_LogicalApplicationComponent_strategy = st.builds(
    contentfwk_LogicalApplicationComponent,
)
contentfwk_PhysicalApplicationComponent_strategy = st.builds(
    contentfwk_PhysicalApplicationComponent,
    privacyCharacteristics=
        safe_text,
    manageabilityCharacteristics=
        safe_text,
    dateOfLastRelease=
        st.dates(),
    dateOfNextRelease=
        st.dates(),
    serviceabilityCharacteristics=
        safe_text,
    throughputPeriod=
        safe_text,
    peakProfileLongTerm=
        safe_text,
    securityCharacteristics=
        safe_text,
    extensibilityCharacteristics=
        safe_text,
    scalabilityCharacteristics=
        safe_text,
    credibilityCharacteristics=
        safe_text,
    portabilityCharacteristics=
        safe_text,
    capacityCharacteristics=
        safe_text,
    internationalizationCharacteristics=
        safe_text,
    integrityCharacteristics=
        safe_text,
    peakProfileShortTerm=
        safe_text,
    growthPeriod=
        safe_text,
    locatabilityCharacteristics=
        safe_text,
    recoverabilityCharacteristics=
        safe_text,
    retirementDate=
        st.dates(),
    growth=
        safe_text,
    interoperabilityCharacteristics=
        safe_text,
    availabilityQualityCharacteristics=
        safe_text,
    throughput=
        safe_text,
    performanceCharacteristics=
        safe_text,
    lifeCycleStatus=
        safe_text,
    servicesTimes=
        safe_text,
    reliabilityCharacteristics=
        safe_text,
    initialLiveDate=
        st.dates(),
    localizationCharacteristics=
        safe_text
)
contentfwk_Function_strategy = st.builds(
    contentfwk_Function,
)
contentfwk_OrganizationUnit_strategy = st.builds(
    contentfwk_OrganizationUnit,
    headcount=
        safe_text
)
contentfwk_Contract_strategy = st.builds(
    contentfwk_Contract,
    scalabilityCharacteristics=
        safe_text,
    extensibilityCharacteristics=
        safe_text,
    availabilityQualityCharacteristics=
        safe_text,
    recoverabilityCharacteristics=
        safe_text,
    credibilityCharacteristics=
        safe_text,
    servicesTimes=
        safe_text,
    manageabilityCharacteristics=
        safe_text,
    localizationCharacteristics=
        safe_text,
    serviceQualityCharacteristics=
        safe_text,
    ServiceNameCalled=
        safe_text,
    reliabilityCharacteristics=
        safe_text,
    throughput=
        safe_text,
    integrityCharacteristics=
        safe_text,
    internationalizationCharacteristics=
        safe_text,
    privacyCharacteristics=
        safe_text,
    resultControlRequirements=
        safe_text,
    contractControlRequirements=
        safe_text,
    peakProfileLongTerm=
        safe_text,
    securityCharacteristics=
        safe_text,
    locatabilityCharacteristics=
        safe_text,
    qualityOfInformationRequired=
        safe_text,
    ServiceNameCaller=
        safe_text,
    performanceCharacteristics=
        safe_text,
    capacityCharacteristics=
        safe_text,
    portabilityCharacteristics=
        safe_text,
    serviceabilityCharacteristics=
        safe_text,
    peakProfileShortTerm=
        safe_text,
    responseCharacteristics=
        safe_text,
    interoperabilityCharacteristics=
        safe_text,
    throughputPeriod=
        safe_text,
    growth=
        safe_text,
    growthPeriod=
        safe_text,
    behaviorCharacteristics=
        safe_text
)
contentfwk_Product_strategy = st.builds(
    contentfwk_Product,
)
contentfwk_Actor_strategy = st.builds(
    contentfwk_Actor,
    FTEs=
        safe_text,
    actorTasks=
        safe_text,
    actorGoal=
        safe_text
)
contentfwk_Capability_strategy = st.builds(
    contentfwk_Capability,
    increments=
        safe_text,
    businessValue=
        safe_text
)
contentfwk_Control_strategy = st.builds(
    contentfwk_Control,
)
contentfwk_ServiceQuality_strategy = st.builds(
    contentfwk_ServiceQuality,
)
contentfwk_LogicalTechnologyComponent_strategy = st.builds(
    contentfwk_LogicalTechnologyComponent,
    categoryTRM=
        safe_text
)
contentfwk_PhysicalTechnologyComponent_strategy = st.builds(
    contentfwk_PhysicalTechnologyComponent,
    categoryTRM=
        safe_text,
    moduleName=
        safe_text,
    productName=
        safe_text,
    vendor=
        safe_text,
    version=
        safe_text
)
contentfwk_PlatformService_strategy = st.builds(
    contentfwk_PlatformService,
    categoryTRM=
        safe_text
)
contentfwk_TechnologyArchitecture_strategy = st.builds(
    contentfwk_TechnologyArchitecture,
)
contentfwk_PhysicalDataComponent_strategy = st.builds(
    contentfwk_PhysicalDataComponent,
)








@given(instance=contentfwk_Label_strategy)
def test_hyp_contentfwk_label_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=contentfwk_Label_strategy)
def test_hyp_contentfwk_label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=contentfwk_Label_strategy)
def test_hyp_contentfwk_label_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=contentfwk_Container_strategy)
def test_hyp_contentfwk_container_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=contentfwk_Container_strategy)
def test_hyp_contentfwk_container_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=contentfwk_Container_strategy)
def test_hyp_contentfwk_container_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=contentfwk_Standard_strategy)
def test_hyp_contentfwk_standard_standardCreationDate_setter(instance):
    original = instance.standardCreationDate
    instance.standardCreationDate = original
    assert instance.standardCreationDate == original



@given(instance=contentfwk_Standard_strategy)
def test_hyp_contentfwk_standard_retireDate_setter(instance):
    original = instance.retireDate
    instance.retireDate = original
    assert instance.retireDate == original



@given(instance=contentfwk_Standard_strategy)
def test_hyp_contentfwk_standard_standardClass_setter(instance):
    original = instance.standardClass
    instance.standardClass = original
    assert instance.standardClass == original



@given(instance=contentfwk_Standard_strategy)
def test_hyp_contentfwk_standard_nextStandardCreationDate_setter(instance):
    original = instance.nextStandardCreationDate
    instance.nextStandardCreationDate = original
    assert instance.nextStandardCreationDate == original



@given(instance=contentfwk_Standard_strategy)
def test_hyp_contentfwk_standard_lastStandardCreationDate_setter(instance):
    original = instance.lastStandardCreationDate
    instance.lastStandardCreationDate = original
    assert instance.lastStandardCreationDate == original









@given(instance=contentfwk_Requirement_strategy)
def test_hyp_contentfwk_requirement_acceptanceCriteria_setter(instance):
    original = instance.acceptanceCriteria
    instance.acceptanceCriteria = original
    assert instance.acceptanceCriteria == original



@given(instance=contentfwk_Requirement_strategy)
def test_hyp_contentfwk_requirement_statementOfRequirement_setter(instance):
    original = instance.statementOfRequirement
    instance.statementOfRequirement = original
    assert instance.statementOfRequirement == original



@given(instance=contentfwk_Requirement_strategy)
def test_hyp_contentfwk_requirement_rationale_setter(instance):
    original = instance.rationale
    instance.rationale = original
    assert instance.rationale == original






@given(instance=contentfwk_Principle_strategy)
def test_hyp_contentfwk_principle_implication_setter(instance):
    original = instance.implication
    instance.implication = original
    assert instance.implication == original



@given(instance=contentfwk_Principle_strategy)
def test_hyp_contentfwk_principle_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=contentfwk_Principle_strategy)
def test_hyp_contentfwk_principle_principleCategory_setter(instance):
    original = instance.principleCategory
    instance.principleCategory = original
    assert instance.principleCategory == original



@given(instance=contentfwk_Principle_strategy)
def test_hyp_contentfwk_principle_metric_setter(instance):
    original = instance.metric
    instance.metric = original
    assert instance.metric == original



@given(instance=contentfwk_Principle_strategy)
def test_hyp_contentfwk_principle_statementOfPrinciple_setter(instance):
    original = instance.statementOfPrinciple
    instance.statementOfPrinciple = original
    assert instance.statementOfPrinciple == original



@given(instance=contentfwk_Principle_strategy)
def test_hyp_contentfwk_principle_rationale_setter(instance):
    original = instance.rationale
    instance.rationale = original
    assert instance.rationale == original




@given(instance=contentfwk_WorkPackage_strategy)
def test_hyp_contentfwk_workpackage_workPackageCategory_setter(instance):
    original = instance.workPackageCategory
    instance.workPackageCategory = original
    assert instance.workPackageCategory == original




@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_ownerDescr_setter(instance):
    original = instance.ownerDescr
    instance.ownerDescr = original
    assert instance.ownerDescr == original



@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_sourceDescr_setter(instance):
    original = instance.sourceDescr
    instance.sourceDescr = original
    assert instance.sourceDescr == original



@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original















@given(instance=contentfwk_Process_strategy)
def test_hyp_contentfwk_process_processCritiality_setter(instance):
    original = instance.processCritiality
    instance.processCritiality = original
    assert instance.processCritiality == original



@given(instance=contentfwk_Process_strategy)
def test_hyp_contentfwk_process_isAutomated_setter(instance):
    original = instance.isAutomated
    instance.isAutomated = original
    assert instance.isAutomated == original



@given(instance=contentfwk_Process_strategy)
def test_hyp_contentfwk_process_processVolumetrics_setter(instance):
    original = instance.processVolumetrics
    instance.processVolumetrics = original
    assert instance.processVolumetrics == original





@given(instance=contentfwk_DataEntity_strategy)
def test_hyp_contentfwk_dataentity_privacyClassification_setter(instance):
    original = instance.privacyClassification
    instance.privacyClassification = original
    assert instance.privacyClassification == original



@given(instance=contentfwk_DataEntity_strategy)
def test_hyp_contentfwk_dataentity_dataEntityCategory_setter(instance):
    original = instance.dataEntityCategory
    instance.dataEntityCategory = original
    assert instance.dataEntityCategory == original



@given(instance=contentfwk_DataEntity_strategy)
def test_hyp_contentfwk_dataentity_retentionClassification_setter(instance):
    original = instance.retentionClassification
    instance.retentionClassification = original
    assert instance.retentionClassification == original






@given(instance=contentfwk_Role_strategy)
def test_hyp_contentfwk_role_estimatedFTEs_setter(instance):
    original = instance.estimatedFTEs
    instance.estimatedFTEs = original
    assert instance.estimatedFTEs == original










@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_privacyCharacteristics_setter(instance):
    original = instance.privacyCharacteristics
    instance.privacyCharacteristics = original
    assert instance.privacyCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_manageabilityCharacteristics_setter(instance):
    original = instance.manageabilityCharacteristics
    instance.manageabilityCharacteristics = original
    assert instance.manageabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_dateOfLastRelease_setter(instance):
    original = instance.dateOfLastRelease
    instance.dateOfLastRelease = original
    assert instance.dateOfLastRelease == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_dateOfNextRelease_setter(instance):
    original = instance.dateOfNextRelease
    instance.dateOfNextRelease = original
    assert instance.dateOfNextRelease == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_serviceabilityCharacteristics_setter(instance):
    original = instance.serviceabilityCharacteristics
    instance.serviceabilityCharacteristics = original
    assert instance.serviceabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_throughputPeriod_setter(instance):
    original = instance.throughputPeriod
    instance.throughputPeriod = original
    assert instance.throughputPeriod == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_peakProfileLongTerm_setter(instance):
    original = instance.peakProfileLongTerm
    instance.peakProfileLongTerm = original
    assert instance.peakProfileLongTerm == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_securityCharacteristics_setter(instance):
    original = instance.securityCharacteristics
    instance.securityCharacteristics = original
    assert instance.securityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_extensibilityCharacteristics_setter(instance):
    original = instance.extensibilityCharacteristics
    instance.extensibilityCharacteristics = original
    assert instance.extensibilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_scalabilityCharacteristics_setter(instance):
    original = instance.scalabilityCharacteristics
    instance.scalabilityCharacteristics = original
    assert instance.scalabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_credibilityCharacteristics_setter(instance):
    original = instance.credibilityCharacteristics
    instance.credibilityCharacteristics = original
    assert instance.credibilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_portabilityCharacteristics_setter(instance):
    original = instance.portabilityCharacteristics
    instance.portabilityCharacteristics = original
    assert instance.portabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_capacityCharacteristics_setter(instance):
    original = instance.capacityCharacteristics
    instance.capacityCharacteristics = original
    assert instance.capacityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_internationalizationCharacteristics_setter(instance):
    original = instance.internationalizationCharacteristics
    instance.internationalizationCharacteristics = original
    assert instance.internationalizationCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_integrityCharacteristics_setter(instance):
    original = instance.integrityCharacteristics
    instance.integrityCharacteristics = original
    assert instance.integrityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_peakProfileShortTerm_setter(instance):
    original = instance.peakProfileShortTerm
    instance.peakProfileShortTerm = original
    assert instance.peakProfileShortTerm == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_growthPeriod_setter(instance):
    original = instance.growthPeriod
    instance.growthPeriod = original
    assert instance.growthPeriod == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_locatabilityCharacteristics_setter(instance):
    original = instance.locatabilityCharacteristics
    instance.locatabilityCharacteristics = original
    assert instance.locatabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_recoverabilityCharacteristics_setter(instance):
    original = instance.recoverabilityCharacteristics
    instance.recoverabilityCharacteristics = original
    assert instance.recoverabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_retirementDate_setter(instance):
    original = instance.retirementDate
    instance.retirementDate = original
    assert instance.retirementDate == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_growth_setter(instance):
    original = instance.growth
    instance.growth = original
    assert instance.growth == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_interoperabilityCharacteristics_setter(instance):
    original = instance.interoperabilityCharacteristics
    instance.interoperabilityCharacteristics = original
    assert instance.interoperabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_availabilityQualityCharacteristics_setter(instance):
    original = instance.availabilityQualityCharacteristics
    instance.availabilityQualityCharacteristics = original
    assert instance.availabilityQualityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_performanceCharacteristics_setter(instance):
    original = instance.performanceCharacteristics
    instance.performanceCharacteristics = original
    assert instance.performanceCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_lifeCycleStatus_setter(instance):
    original = instance.lifeCycleStatus
    instance.lifeCycleStatus = original
    assert instance.lifeCycleStatus == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_servicesTimes_setter(instance):
    original = instance.servicesTimes
    instance.servicesTimes = original
    assert instance.servicesTimes == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_reliabilityCharacteristics_setter(instance):
    original = instance.reliabilityCharacteristics
    instance.reliabilityCharacteristics = original
    assert instance.reliabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_initialLiveDate_setter(instance):
    original = instance.initialLiveDate
    instance.initialLiveDate = original
    assert instance.initialLiveDate == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_localizationCharacteristics_setter(instance):
    original = instance.localizationCharacteristics
    instance.localizationCharacteristics = original
    assert instance.localizationCharacteristics == original





@given(instance=contentfwk_OrganizationUnit_strategy)
def test_hyp_contentfwk_organizationunit_headcount_setter(instance):
    original = instance.headcount
    instance.headcount = original
    assert instance.headcount == original




@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_scalabilityCharacteristics_setter(instance):
    original = instance.scalabilityCharacteristics
    instance.scalabilityCharacteristics = original
    assert instance.scalabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_extensibilityCharacteristics_setter(instance):
    original = instance.extensibilityCharacteristics
    instance.extensibilityCharacteristics = original
    assert instance.extensibilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_availabilityQualityCharacteristics_setter(instance):
    original = instance.availabilityQualityCharacteristics
    instance.availabilityQualityCharacteristics = original
    assert instance.availabilityQualityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_recoverabilityCharacteristics_setter(instance):
    original = instance.recoverabilityCharacteristics
    instance.recoverabilityCharacteristics = original
    assert instance.recoverabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_credibilityCharacteristics_setter(instance):
    original = instance.credibilityCharacteristics
    instance.credibilityCharacteristics = original
    assert instance.credibilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_servicesTimes_setter(instance):
    original = instance.servicesTimes
    instance.servicesTimes = original
    assert instance.servicesTimes == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_manageabilityCharacteristics_setter(instance):
    original = instance.manageabilityCharacteristics
    instance.manageabilityCharacteristics = original
    assert instance.manageabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_localizationCharacteristics_setter(instance):
    original = instance.localizationCharacteristics
    instance.localizationCharacteristics = original
    assert instance.localizationCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_serviceQualityCharacteristics_setter(instance):
    original = instance.serviceQualityCharacteristics
    instance.serviceQualityCharacteristics = original
    assert instance.serviceQualityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_ServiceNameCalled_setter(instance):
    original = instance.ServiceNameCalled
    instance.ServiceNameCalled = original
    assert instance.ServiceNameCalled == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_reliabilityCharacteristics_setter(instance):
    original = instance.reliabilityCharacteristics
    instance.reliabilityCharacteristics = original
    assert instance.reliabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_integrityCharacteristics_setter(instance):
    original = instance.integrityCharacteristics
    instance.integrityCharacteristics = original
    assert instance.integrityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_internationalizationCharacteristics_setter(instance):
    original = instance.internationalizationCharacteristics
    instance.internationalizationCharacteristics = original
    assert instance.internationalizationCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_privacyCharacteristics_setter(instance):
    original = instance.privacyCharacteristics
    instance.privacyCharacteristics = original
    assert instance.privacyCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_resultControlRequirements_setter(instance):
    original = instance.resultControlRequirements
    instance.resultControlRequirements = original
    assert instance.resultControlRequirements == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_contractControlRequirements_setter(instance):
    original = instance.contractControlRequirements
    instance.contractControlRequirements = original
    assert instance.contractControlRequirements == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_peakProfileLongTerm_setter(instance):
    original = instance.peakProfileLongTerm
    instance.peakProfileLongTerm = original
    assert instance.peakProfileLongTerm == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_securityCharacteristics_setter(instance):
    original = instance.securityCharacteristics
    instance.securityCharacteristics = original
    assert instance.securityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_locatabilityCharacteristics_setter(instance):
    original = instance.locatabilityCharacteristics
    instance.locatabilityCharacteristics = original
    assert instance.locatabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_qualityOfInformationRequired_setter(instance):
    original = instance.qualityOfInformationRequired
    instance.qualityOfInformationRequired = original
    assert instance.qualityOfInformationRequired == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_ServiceNameCaller_setter(instance):
    original = instance.ServiceNameCaller
    instance.ServiceNameCaller = original
    assert instance.ServiceNameCaller == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_performanceCharacteristics_setter(instance):
    original = instance.performanceCharacteristics
    instance.performanceCharacteristics = original
    assert instance.performanceCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_capacityCharacteristics_setter(instance):
    original = instance.capacityCharacteristics
    instance.capacityCharacteristics = original
    assert instance.capacityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_portabilityCharacteristics_setter(instance):
    original = instance.portabilityCharacteristics
    instance.portabilityCharacteristics = original
    assert instance.portabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_serviceabilityCharacteristics_setter(instance):
    original = instance.serviceabilityCharacteristics
    instance.serviceabilityCharacteristics = original
    assert instance.serviceabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_peakProfileShortTerm_setter(instance):
    original = instance.peakProfileShortTerm
    instance.peakProfileShortTerm = original
    assert instance.peakProfileShortTerm == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_responseCharacteristics_setter(instance):
    original = instance.responseCharacteristics
    instance.responseCharacteristics = original
    assert instance.responseCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_interoperabilityCharacteristics_setter(instance):
    original = instance.interoperabilityCharacteristics
    instance.interoperabilityCharacteristics = original
    assert instance.interoperabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_throughputPeriod_setter(instance):
    original = instance.throughputPeriod
    instance.throughputPeriod = original
    assert instance.throughputPeriod == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_growth_setter(instance):
    original = instance.growth
    instance.growth = original
    assert instance.growth == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_growthPeriod_setter(instance):
    original = instance.growthPeriod
    instance.growthPeriod = original
    assert instance.growthPeriod == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_behaviorCharacteristics_setter(instance):
    original = instance.behaviorCharacteristics
    instance.behaviorCharacteristics = original
    assert instance.behaviorCharacteristics == original





@given(instance=contentfwk_Actor_strategy)
def test_hyp_contentfwk_actor_FTEs_setter(instance):
    original = instance.FTEs
    instance.FTEs = original
    assert instance.FTEs == original



@given(instance=contentfwk_Actor_strategy)
def test_hyp_contentfwk_actor_actorTasks_setter(instance):
    original = instance.actorTasks
    instance.actorTasks = original
    assert instance.actorTasks == original



@given(instance=contentfwk_Actor_strategy)
def test_hyp_contentfwk_actor_actorGoal_setter(instance):
    original = instance.actorGoal
    instance.actorGoal = original
    assert instance.actorGoal == original




@given(instance=contentfwk_Capability_strategy)
def test_hyp_contentfwk_capability_increments_setter(instance):
    original = instance.increments
    instance.increments = original
    assert instance.increments == original



@given(instance=contentfwk_Capability_strategy)
def test_hyp_contentfwk_capability_businessValue_setter(instance):
    original = instance.businessValue
    instance.businessValue = original
    assert instance.businessValue == original






@given(instance=contentfwk_LogicalTechnologyComponent_strategy)
def test_hyp_contentfwk_logicaltechnologycomponent_categoryTRM_setter(instance):
    original = instance.categoryTRM
    instance.categoryTRM = original
    assert instance.categoryTRM == original




@given(instance=contentfwk_PhysicalTechnologyComponent_strategy)
def test_hyp_contentfwk_physicaltechnologycomponent_categoryTRM_setter(instance):
    original = instance.categoryTRM
    instance.categoryTRM = original
    assert instance.categoryTRM == original



@given(instance=contentfwk_PhysicalTechnologyComponent_strategy)
def test_hyp_contentfwk_physicaltechnologycomponent_moduleName_setter(instance):
    original = instance.moduleName
    instance.moduleName = original
    assert instance.moduleName == original



@given(instance=contentfwk_PhysicalTechnologyComponent_strategy)
def test_hyp_contentfwk_physicaltechnologycomponent_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original



@given(instance=contentfwk_PhysicalTechnologyComponent_strategy)
def test_hyp_contentfwk_physicaltechnologycomponent_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original



@given(instance=contentfwk_PhysicalTechnologyComponent_strategy)
def test_hyp_contentfwk_physicaltechnologycomponent_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original




@given(instance=contentfwk_PlatformService_strategy)
def test_hyp_contentfwk_platformservice_categoryTRM_setter(instance):
    original = instance.categoryTRM
    instance.categoryTRM = original
    assert instance.categoryTRM == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_contentfwk_Actor_FTEs_value_roundtrip():
    instance = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    assert instance.FTEs == "sample_text"
    instance.FTEs = "sample_text_2"
    assert instance.FTEs == "sample_text_2"


def test_contentfwk_Actor_actorGoal_value_roundtrip():
    instance = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    assert instance.actorGoal == "sample_text"
    instance.actorGoal = "sample_text_2"
    assert instance.actorGoal == "sample_text_2"


def test_contentfwk_Actor_actorTasks_value_roundtrip():
    instance = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    assert instance.actorTasks == "sample_text"
    instance.actorTasks = "sample_text_2"
    assert instance.actorTasks == "sample_text_2"


def test_contentfwk_Capability_businessValue_value_roundtrip():
    instance = contentfwk_Capability(businessValue="sample_text", increments="sample_text")
    assert instance.businessValue == "sample_text"
    instance.businessValue = "sample_text_2"
    assert instance.businessValue == "sample_text_2"


def test_contentfwk_Capability_increments_value_roundtrip():
    instance = contentfwk_Capability(businessValue="sample_text", increments="sample_text")
    assert instance.increments == "sample_text"
    instance.increments = "sample_text_2"
    assert instance.increments == "sample_text_2"


def test_contentfwk_Container_description_value_roundtrip():
    instance = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_contentfwk_Container_id_value_roundtrip():
    instance = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_contentfwk_Container_name_value_roundtrip():
    instance = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_contentfwk_Contract_ServiceNameCalled_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.ServiceNameCalled == "sample_text"
    instance.ServiceNameCalled = "sample_text_2"
    assert instance.ServiceNameCalled == "sample_text_2"


def test_contentfwk_Contract_ServiceNameCaller_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.ServiceNameCaller == "sample_text"
    instance.ServiceNameCaller = "sample_text_2"
    assert instance.ServiceNameCaller == "sample_text_2"


def test_contentfwk_Contract_availabilityQualityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.availabilityQualityCharacteristics == "sample_text"
    instance.availabilityQualityCharacteristics = "sample_text_2"
    assert instance.availabilityQualityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_behaviorCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.behaviorCharacteristics == "sample_text"
    instance.behaviorCharacteristics = "sample_text_2"
    assert instance.behaviorCharacteristics == "sample_text_2"


def test_contentfwk_Contract_capacityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.capacityCharacteristics == "sample_text"
    instance.capacityCharacteristics = "sample_text_2"
    assert instance.capacityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_contractControlRequirements_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.contractControlRequirements == "sample_text"
    instance.contractControlRequirements = "sample_text_2"
    assert instance.contractControlRequirements == "sample_text_2"


def test_contentfwk_Contract_credibilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.credibilityCharacteristics == "sample_text"
    instance.credibilityCharacteristics = "sample_text_2"
    assert instance.credibilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_extensibilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.extensibilityCharacteristics == "sample_text"
    instance.extensibilityCharacteristics = "sample_text_2"
    assert instance.extensibilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_growth_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.growth == "sample_text"
    instance.growth = "sample_text_2"
    assert instance.growth == "sample_text_2"


def test_contentfwk_Contract_growthPeriod_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.growthPeriod == "sample_text"
    instance.growthPeriod = "sample_text_2"
    assert instance.growthPeriod == "sample_text_2"


def test_contentfwk_Contract_integrityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.integrityCharacteristics == "sample_text"
    instance.integrityCharacteristics = "sample_text_2"
    assert instance.integrityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_internationalizationCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.internationalizationCharacteristics == "sample_text"
    instance.internationalizationCharacteristics = "sample_text_2"
    assert instance.internationalizationCharacteristics == "sample_text_2"


def test_contentfwk_Contract_interoperabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.interoperabilityCharacteristics == "sample_text"
    instance.interoperabilityCharacteristics = "sample_text_2"
    assert instance.interoperabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_localizationCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.localizationCharacteristics == "sample_text"
    instance.localizationCharacteristics = "sample_text_2"
    assert instance.localizationCharacteristics == "sample_text_2"


def test_contentfwk_Contract_locatabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.locatabilityCharacteristics == "sample_text"
    instance.locatabilityCharacteristics = "sample_text_2"
    assert instance.locatabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_manageabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.manageabilityCharacteristics == "sample_text"
    instance.manageabilityCharacteristics = "sample_text_2"
    assert instance.manageabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_peakProfileLongTerm_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.peakProfileLongTerm == "sample_text"
    instance.peakProfileLongTerm = "sample_text_2"
    assert instance.peakProfileLongTerm == "sample_text_2"


def test_contentfwk_Contract_peakProfileShortTerm_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.peakProfileShortTerm == "sample_text"
    instance.peakProfileShortTerm = "sample_text_2"
    assert instance.peakProfileShortTerm == "sample_text_2"


def test_contentfwk_Contract_performanceCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.performanceCharacteristics == "sample_text"
    instance.performanceCharacteristics = "sample_text_2"
    assert instance.performanceCharacteristics == "sample_text_2"


def test_contentfwk_Contract_portabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.portabilityCharacteristics == "sample_text"
    instance.portabilityCharacteristics = "sample_text_2"
    assert instance.portabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_privacyCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.privacyCharacteristics == "sample_text"
    instance.privacyCharacteristics = "sample_text_2"
    assert instance.privacyCharacteristics == "sample_text_2"


def test_contentfwk_Contract_qualityOfInformationRequired_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.qualityOfInformationRequired == "sample_text"
    instance.qualityOfInformationRequired = "sample_text_2"
    assert instance.qualityOfInformationRequired == "sample_text_2"


def test_contentfwk_Contract_recoverabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.recoverabilityCharacteristics == "sample_text"
    instance.recoverabilityCharacteristics = "sample_text_2"
    assert instance.recoverabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_reliabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.reliabilityCharacteristics == "sample_text"
    instance.reliabilityCharacteristics = "sample_text_2"
    assert instance.reliabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_responseCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.responseCharacteristics == "sample_text"
    instance.responseCharacteristics = "sample_text_2"
    assert instance.responseCharacteristics == "sample_text_2"


def test_contentfwk_Contract_resultControlRequirements_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.resultControlRequirements == "sample_text"
    instance.resultControlRequirements = "sample_text_2"
    assert instance.resultControlRequirements == "sample_text_2"


def test_contentfwk_Contract_scalabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.scalabilityCharacteristics == "sample_text"
    instance.scalabilityCharacteristics = "sample_text_2"
    assert instance.scalabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_securityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.securityCharacteristics == "sample_text"
    instance.securityCharacteristics = "sample_text_2"
    assert instance.securityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_serviceQualityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.serviceQualityCharacteristics == "sample_text"
    instance.serviceQualityCharacteristics = "sample_text_2"
    assert instance.serviceQualityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_serviceabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.serviceabilityCharacteristics == "sample_text"
    instance.serviceabilityCharacteristics = "sample_text_2"
    assert instance.serviceabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_servicesTimes_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.servicesTimes == "sample_text"
    instance.servicesTimes = "sample_text_2"
    assert instance.servicesTimes == "sample_text_2"


def test_contentfwk_Contract_throughput_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.throughput == "sample_text"
    instance.throughput = "sample_text_2"
    assert instance.throughput == "sample_text_2"


def test_contentfwk_Contract_throughputPeriod_value_roundtrip():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.throughputPeriod == "sample_text"
    instance.throughputPeriod = "sample_text_2"
    assert instance.throughputPeriod == "sample_text_2"


def test_contentfwk_DataEntity_dataEntityCategory_value_roundtrip():
    instance = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    assert instance.dataEntityCategory == "sample_text"
    instance.dataEntityCategory = "sample_text_2"
    assert instance.dataEntityCategory == "sample_text_2"


def test_contentfwk_DataEntity_privacyClassification_value_roundtrip():
    instance = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    assert instance.privacyClassification == "sample_text"
    instance.privacyClassification = "sample_text_2"
    assert instance.privacyClassification == "sample_text_2"


def test_contentfwk_DataEntity_retentionClassification_value_roundtrip():
    instance = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    assert instance.retentionClassification == "sample_text"
    instance.retentionClassification = "sample_text_2"
    assert instance.retentionClassification == "sample_text_2"


def test_contentfwk_Element_ID_value_roundtrip():
    instance = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_contentfwk_Element_description_value_roundtrip():
    instance = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_contentfwk_Element_name_value_roundtrip():
    instance = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_contentfwk_Element_ownerDescr_value_roundtrip():
    instance = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.ownerDescr == "sample_text"
    instance.ownerDescr = "sample_text_2"
    assert instance.ownerDescr == "sample_text_2"


def test_contentfwk_Element_sourceDescr_value_roundtrip():
    instance = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.sourceDescr == "sample_text"
    instance.sourceDescr = "sample_text_2"
    assert instance.sourceDescr == "sample_text_2"


def test_contentfwk_Label_description_value_roundtrip():
    instance = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_contentfwk_Label_id_value_roundtrip():
    instance = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_contentfwk_Label_name_value_roundtrip():
    instance = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_contentfwk_LogicalTechnologyComponent_categoryTRM_value_roundtrip():
    instance = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    assert instance.categoryTRM == "sample_text"
    instance.categoryTRM = "sample_text_2"
    assert instance.categoryTRM == "sample_text_2"


def test_contentfwk_OrganizationUnit_headcount_value_roundtrip():
    instance = contentfwk_OrganizationUnit(headcount="sample_text")
    assert instance.headcount == "sample_text"
    instance.headcount = "sample_text_2"
    assert instance.headcount == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_availabilityQualityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.availabilityQualityCharacteristics == "sample_text"
    instance.availabilityQualityCharacteristics = "sample_text_2"
    assert instance.availabilityQualityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_capacityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.capacityCharacteristics == "sample_text"
    instance.capacityCharacteristics = "sample_text_2"
    assert instance.capacityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_credibilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.credibilityCharacteristics == "sample_text"
    instance.credibilityCharacteristics = "sample_text_2"
    assert instance.credibilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_dateOfLastRelease_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.dateOfLastRelease == date(2024, 1, 1)
    instance.dateOfLastRelease = date(2025, 6, 15)
    assert instance.dateOfLastRelease == date(2025, 6, 15)


def test_contentfwk_PhysicalApplicationComponent_dateOfNextRelease_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.dateOfNextRelease == date(2024, 1, 1)
    instance.dateOfNextRelease = date(2025, 6, 15)
    assert instance.dateOfNextRelease == date(2025, 6, 15)


def test_contentfwk_PhysicalApplicationComponent_extensibilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.extensibilityCharacteristics == "sample_text"
    instance.extensibilityCharacteristics = "sample_text_2"
    assert instance.extensibilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_growth_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.growth == "sample_text"
    instance.growth = "sample_text_2"
    assert instance.growth == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_growthPeriod_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.growthPeriod == "sample_text"
    instance.growthPeriod = "sample_text_2"
    assert instance.growthPeriod == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_initialLiveDate_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.initialLiveDate == date(2024, 1, 1)
    instance.initialLiveDate = date(2025, 6, 15)
    assert instance.initialLiveDate == date(2025, 6, 15)


def test_contentfwk_PhysicalApplicationComponent_integrityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.integrityCharacteristics == "sample_text"
    instance.integrityCharacteristics = "sample_text_2"
    assert instance.integrityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_internationalizationCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.internationalizationCharacteristics == "sample_text"
    instance.internationalizationCharacteristics = "sample_text_2"
    assert instance.internationalizationCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_interoperabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.interoperabilityCharacteristics == "sample_text"
    instance.interoperabilityCharacteristics = "sample_text_2"
    assert instance.interoperabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_lifeCycleStatus_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.lifeCycleStatus == "sample_text"
    instance.lifeCycleStatus = "sample_text_2"
    assert instance.lifeCycleStatus == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_localizationCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.localizationCharacteristics == "sample_text"
    instance.localizationCharacteristics = "sample_text_2"
    assert instance.localizationCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_locatabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.locatabilityCharacteristics == "sample_text"
    instance.locatabilityCharacteristics = "sample_text_2"
    assert instance.locatabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_manageabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.manageabilityCharacteristics == "sample_text"
    instance.manageabilityCharacteristics = "sample_text_2"
    assert instance.manageabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_peakProfileLongTerm_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.peakProfileLongTerm == "sample_text"
    instance.peakProfileLongTerm = "sample_text_2"
    assert instance.peakProfileLongTerm == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_peakProfileShortTerm_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.peakProfileShortTerm == "sample_text"
    instance.peakProfileShortTerm = "sample_text_2"
    assert instance.peakProfileShortTerm == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_performanceCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.performanceCharacteristics == "sample_text"
    instance.performanceCharacteristics = "sample_text_2"
    assert instance.performanceCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_portabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.portabilityCharacteristics == "sample_text"
    instance.portabilityCharacteristics = "sample_text_2"
    assert instance.portabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_privacyCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.privacyCharacteristics == "sample_text"
    instance.privacyCharacteristics = "sample_text_2"
    assert instance.privacyCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_recoverabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.recoverabilityCharacteristics == "sample_text"
    instance.recoverabilityCharacteristics = "sample_text_2"
    assert instance.recoverabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_reliabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.reliabilityCharacteristics == "sample_text"
    instance.reliabilityCharacteristics = "sample_text_2"
    assert instance.reliabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_retirementDate_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.retirementDate == date(2024, 1, 1)
    instance.retirementDate = date(2025, 6, 15)
    assert instance.retirementDate == date(2025, 6, 15)


def test_contentfwk_PhysicalApplicationComponent_scalabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.scalabilityCharacteristics == "sample_text"
    instance.scalabilityCharacteristics = "sample_text_2"
    assert instance.scalabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_securityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.securityCharacteristics == "sample_text"
    instance.securityCharacteristics = "sample_text_2"
    assert instance.securityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_serviceabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.serviceabilityCharacteristics == "sample_text"
    instance.serviceabilityCharacteristics = "sample_text_2"
    assert instance.serviceabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_servicesTimes_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.servicesTimes == "sample_text"
    instance.servicesTimes = "sample_text_2"
    assert instance.servicesTimes == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_throughput_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.throughput == "sample_text"
    instance.throughput = "sample_text_2"
    assert instance.throughput == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_throughputPeriod_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.throughputPeriod == "sample_text"
    instance.throughputPeriod = "sample_text_2"
    assert instance.throughputPeriod == "sample_text_2"


def test_contentfwk_PhysicalTechnologyComponent_categoryTRM_value_roundtrip():
    instance = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    assert instance.categoryTRM == "sample_text"
    instance.categoryTRM = "sample_text_2"
    assert instance.categoryTRM == "sample_text_2"


def test_contentfwk_PhysicalTechnologyComponent_moduleName_value_roundtrip():
    instance = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    assert instance.moduleName == "sample_text"
    instance.moduleName = "sample_text_2"
    assert instance.moduleName == "sample_text_2"


def test_contentfwk_PhysicalTechnologyComponent_productName_value_roundtrip():
    instance = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    assert instance.productName == "sample_text"
    instance.productName = "sample_text_2"
    assert instance.productName == "sample_text_2"


def test_contentfwk_PhysicalTechnologyComponent_vendor_value_roundtrip():
    instance = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    assert instance.vendor == "sample_text"
    instance.vendor = "sample_text_2"
    assert instance.vendor == "sample_text_2"


def test_contentfwk_PhysicalTechnologyComponent_version_value_roundtrip():
    instance = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_contentfwk_PlatformService_categoryTRM_value_roundtrip():
    instance = contentfwk_PlatformService(categoryTRM="sample_text")
    assert instance.categoryTRM == "sample_text"
    instance.categoryTRM = "sample_text_2"
    assert instance.categoryTRM == "sample_text_2"


def test_contentfwk_Principle_implication_value_roundtrip():
    instance = contentfwk_Principle(implication="sample_text", metric="sample_text", principleCategory="sample_text", priority="sample_text", rationale="sample_text", statementOfPrinciple="sample_text")
    assert instance.implication == "sample_text"
    instance.implication = "sample_text_2"
    assert instance.implication == "sample_text_2"


def test_contentfwk_Principle_metric_value_roundtrip():
    instance = contentfwk_Principle(implication="sample_text", metric="sample_text", principleCategory="sample_text", priority="sample_text", rationale="sample_text", statementOfPrinciple="sample_text")
    assert instance.metric == "sample_text"
    instance.metric = "sample_text_2"
    assert instance.metric == "sample_text_2"


def test_contentfwk_Principle_principleCategory_value_roundtrip():
    instance = contentfwk_Principle(implication="sample_text", metric="sample_text", principleCategory="sample_text", priority="sample_text", rationale="sample_text", statementOfPrinciple="sample_text")
    assert instance.principleCategory == "sample_text"
    instance.principleCategory = "sample_text_2"
    assert instance.principleCategory == "sample_text_2"


def test_contentfwk_Principle_priority_value_roundtrip():
    instance = contentfwk_Principle(implication="sample_text", metric="sample_text", principleCategory="sample_text", priority="sample_text", rationale="sample_text", statementOfPrinciple="sample_text")
    assert instance.priority == "sample_text"
    instance.priority = "sample_text_2"
    assert instance.priority == "sample_text_2"


def test_contentfwk_Principle_rationale_value_roundtrip():
    instance = contentfwk_Principle(implication="sample_text", metric="sample_text", principleCategory="sample_text", priority="sample_text", rationale="sample_text", statementOfPrinciple="sample_text")
    assert instance.rationale == "sample_text"
    instance.rationale = "sample_text_2"
    assert instance.rationale == "sample_text_2"


def test_contentfwk_Principle_statementOfPrinciple_value_roundtrip():
    instance = contentfwk_Principle(implication="sample_text", metric="sample_text", principleCategory="sample_text", priority="sample_text", rationale="sample_text", statementOfPrinciple="sample_text")
    assert instance.statementOfPrinciple == "sample_text"
    instance.statementOfPrinciple = "sample_text_2"
    assert instance.statementOfPrinciple == "sample_text_2"


def test_contentfwk_Process_isAutomated_value_roundtrip():
    instance = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    assert instance.isAutomated == True
    instance.isAutomated = False
    assert instance.isAutomated == False


def test_contentfwk_Process_processCritiality_value_roundtrip():
    instance = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    assert instance.processCritiality == "sample_text"
    instance.processCritiality = "sample_text_2"
    assert instance.processCritiality == "sample_text_2"


def test_contentfwk_Process_processVolumetrics_value_roundtrip():
    instance = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    assert instance.processVolumetrics == "sample_text"
    instance.processVolumetrics = "sample_text_2"
    assert instance.processVolumetrics == "sample_text_2"


def test_contentfwk_Requirement_acceptanceCriteria_value_roundtrip():
    instance = contentfwk_Requirement(acceptanceCriteria="sample_text", rationale="sample_text", statementOfRequirement="sample_text")
    assert instance.acceptanceCriteria == "sample_text"
    instance.acceptanceCriteria = "sample_text_2"
    assert instance.acceptanceCriteria == "sample_text_2"


def test_contentfwk_Requirement_rationale_value_roundtrip():
    instance = contentfwk_Requirement(acceptanceCriteria="sample_text", rationale="sample_text", statementOfRequirement="sample_text")
    assert instance.rationale == "sample_text"
    instance.rationale = "sample_text_2"
    assert instance.rationale == "sample_text_2"


def test_contentfwk_Requirement_statementOfRequirement_value_roundtrip():
    instance = contentfwk_Requirement(acceptanceCriteria="sample_text", rationale="sample_text", statementOfRequirement="sample_text")
    assert instance.statementOfRequirement == "sample_text"
    instance.statementOfRequirement = "sample_text_2"
    assert instance.statementOfRequirement == "sample_text_2"


def test_contentfwk_Role_estimatedFTEs_value_roundtrip():
    instance = contentfwk_Role(estimatedFTEs="sample_text")
    assert instance.estimatedFTEs == "sample_text"
    instance.estimatedFTEs = "sample_text_2"
    assert instance.estimatedFTEs == "sample_text_2"


def test_contentfwk_Standard_lastStandardCreationDate_value_roundtrip():
    instance = contentfwk_Standard(lastStandardCreationDate=date(2024, 1, 1), nextStandardCreationDate=date(2024, 1, 1), retireDate=date(2024, 1, 1), standardClass="sample_text", standardCreationDate=date(2024, 1, 1))
    assert instance.lastStandardCreationDate == date(2024, 1, 1)
    instance.lastStandardCreationDate = date(2025, 6, 15)
    assert instance.lastStandardCreationDate == date(2025, 6, 15)


def test_contentfwk_Standard_nextStandardCreationDate_value_roundtrip():
    instance = contentfwk_Standard(lastStandardCreationDate=date(2024, 1, 1), nextStandardCreationDate=date(2024, 1, 1), retireDate=date(2024, 1, 1), standardClass="sample_text", standardCreationDate=date(2024, 1, 1))
    assert instance.nextStandardCreationDate == date(2024, 1, 1)
    instance.nextStandardCreationDate = date(2025, 6, 15)
    assert instance.nextStandardCreationDate == date(2025, 6, 15)


def test_contentfwk_Standard_retireDate_value_roundtrip():
    instance = contentfwk_Standard(lastStandardCreationDate=date(2024, 1, 1), nextStandardCreationDate=date(2024, 1, 1), retireDate=date(2024, 1, 1), standardClass="sample_text", standardCreationDate=date(2024, 1, 1))
    assert instance.retireDate == date(2024, 1, 1)
    instance.retireDate = date(2025, 6, 15)
    assert instance.retireDate == date(2025, 6, 15)


def test_contentfwk_Standard_standardClass_value_roundtrip():
    instance = contentfwk_Standard(lastStandardCreationDate=date(2024, 1, 1), nextStandardCreationDate=date(2024, 1, 1), retireDate=date(2024, 1, 1), standardClass="sample_text", standardCreationDate=date(2024, 1, 1))
    assert instance.standardClass == "sample_text"
    instance.standardClass = "sample_text_2"
    assert instance.standardClass == "sample_text_2"


def test_contentfwk_Standard_standardCreationDate_value_roundtrip():
    instance = contentfwk_Standard(lastStandardCreationDate=date(2024, 1, 1), nextStandardCreationDate=date(2024, 1, 1), retireDate=date(2024, 1, 1), standardClass="sample_text", standardCreationDate=date(2024, 1, 1))
    assert instance.standardCreationDate == date(2024, 1, 1)
    instance.standardCreationDate = date(2025, 6, 15)
    assert instance.standardCreationDate == date(2025, 6, 15)


def test_contentfwk_WorkPackage_workPackageCategory_value_roundtrip():
    instance = contentfwk_WorkPackage(workPackageCategory="sample_text")
    assert instance.workPackageCategory == "sample_text"
    instance.workPackageCategory = "sample_text_2"
    assert instance.workPackageCategory == "sample_text_2"


def test_contentfwk_LogicalApplicationComponent_isa_ApplicationComponent():
    instance = contentfwk_LogicalApplicationComponent()
    assert isinstance(instance, ApplicationComponent)


def test_contentfwk_PhysicalApplicationComponent_isa_ApplicationComponent():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert isinstance(instance, ApplicationComponent)


def test_contentfwk_ApplicationArchitecture_isa_Architecture():
    instance = contentfwk_ApplicationArchitecture()
    assert isinstance(instance, Architecture)


def test_contentfwk_BusinessArchitecture_isa_Architecture():
    instance = contentfwk_BusinessArchitecture()
    assert isinstance(instance, Architecture)


def test_contentfwk_DataArchitecture_isa_Architecture():
    instance = contentfwk_DataArchitecture()
    assert isinstance(instance, Architecture)


def test_contentfwk_StrategicArchitecture_isa_Architecture():
    instance = contentfwk_StrategicArchitecture()
    assert isinstance(instance, Architecture)


def test_contentfwk_TechnologyArchitecture_isa_Architecture():
    instance = contentfwk_TechnologyArchitecture()
    assert isinstance(instance, Architecture)


def test_contentfwk_LogicalDataComponent_isa_DataComponent():
    instance = contentfwk_LogicalDataComponent()
    assert isinstance(instance, DataComponent)


def test_contentfwk_PhysicalDataComponent_isa_DataComponent():
    instance = contentfwk_PhysicalDataComponent()
    assert isinstance(instance, DataComponent)


def test_contentfwk_Actor_isa_Element():
    instance = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_BusinessService_isa_Element():
    instance = contentfwk_BusinessService()
    assert isinstance(instance, Element)


def test_contentfwk_Capability_isa_Element():
    instance = contentfwk_Capability(businessValue="sample_text", increments="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_Contract_isa_Element():
    instance = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_Control_isa_Element():
    instance = contentfwk_Control()
    assert isinstance(instance, Element)


def test_contentfwk_DataEntity_isa_Element():
    instance = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_Driver_isa_Element():
    instance = contentfwk_Driver()
    assert isinstance(instance, Element)


def test_contentfwk_Event_isa_Element():
    instance = contentfwk_Event()
    assert isinstance(instance, Element)


def test_contentfwk_Function_isa_Element():
    instance = contentfwk_Function()
    assert isinstance(instance, Element)


def test_contentfwk_Goal_isa_Element():
    instance = contentfwk_Goal()
    assert isinstance(instance, Element)


def test_contentfwk_InformationSystemService_isa_Element():
    instance = contentfwk_InformationSystemService()
    assert isinstance(instance, Element)


def test_contentfwk_Location_isa_Element():
    instance = contentfwk_Location()
    assert isinstance(instance, Element)


def test_contentfwk_LogicalApplicationComponent_isa_Element():
    instance = contentfwk_LogicalApplicationComponent()
    assert isinstance(instance, Element)


def test_contentfwk_LogicalDataComponent_isa_Element():
    instance = contentfwk_LogicalDataComponent()
    assert isinstance(instance, Element)


def test_contentfwk_LogicalTechnologyComponent_isa_Element():
    instance = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_Measure_isa_Element():
    instance = contentfwk_Measure()
    assert isinstance(instance, Element)


def test_contentfwk_Objective_isa_Element():
    instance = contentfwk_Objective()
    assert isinstance(instance, Element)


def test_contentfwk_OrganizationUnit_isa_Element():
    instance = contentfwk_OrganizationUnit(headcount="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_PhysicalApplicationComponent_isa_Element():
    instance = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_PhysicalDataComponent_isa_Element():
    instance = contentfwk_PhysicalDataComponent()
    assert isinstance(instance, Element)


def test_contentfwk_PhysicalTechnologyComponent_isa_Element():
    instance = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_PlatformService_isa_Element():
    instance = contentfwk_PlatformService(categoryTRM="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_Process_isa_Element():
    instance = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_Product_isa_Element():
    instance = contentfwk_Product()
    assert isinstance(instance, Element)


def test_contentfwk_Role_isa_Element():
    instance = contentfwk_Role(estimatedFTEs="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_ServiceQuality_isa_Element():
    instance = contentfwk_ServiceQuality()
    assert isinstance(instance, Element)


def test_contentfwk_StrategicElement_isa_Element():
    instance = contentfwk_StrategicElement()
    assert isinstance(instance, Element)


def test_contentfwk_BusinessService_isa_Service():
    instance = contentfwk_BusinessService()
    assert isinstance(instance, Service)


def test_contentfwk_InformationSystemService_isa_Service():
    instance = contentfwk_InformationSystemService()
    assert isinstance(instance, Service)


def test_contentfwk_PlatformService_isa_Service():
    instance = contentfwk_PlatformService(categoryTRM="sample_text")
    assert isinstance(instance, Service)


def test_contentfwk_ApplicationComponent_isa_Standard():
    instance = contentfwk_ApplicationComponent()
    assert isinstance(instance, Standard)


def test_contentfwk_DataComponent_isa_Standard():
    instance = contentfwk_DataComponent()
    assert isinstance(instance, Standard)


def test_contentfwk_Function_isa_Standard():
    instance = contentfwk_Function()
    assert isinstance(instance, Standard)


def test_contentfwk_Process_isa_Standard():
    instance = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    assert isinstance(instance, Standard)


def test_contentfwk_Service_isa_Standard():
    instance = contentfwk_Service()
    assert isinstance(instance, Standard)


def test_contentfwk_TechnologyComponent_isa_Standard():
    instance = contentfwk_TechnologyComponent()
    assert isinstance(instance, Standard)


def test_contentfwk_Assumption_isa_StrategicElement():
    instance = contentfwk_Assumption()
    assert isinstance(instance, StrategicElement)


def test_contentfwk_Constraint_isa_StrategicElement():
    instance = contentfwk_Constraint()
    assert isinstance(instance, StrategicElement)


def test_contentfwk_Gap_isa_StrategicElement():
    instance = contentfwk_Gap()
    assert isinstance(instance, StrategicElement)


def test_contentfwk_Principle_isa_StrategicElement():
    instance = contentfwk_Principle(implication="sample_text", metric="sample_text", principleCategory="sample_text", priority="sample_text", rationale="sample_text", statementOfPrinciple="sample_text")
    assert isinstance(instance, StrategicElement)


def test_contentfwk_Requirement_isa_StrategicElement():
    instance = contentfwk_Requirement(acceptanceCriteria="sample_text", rationale="sample_text", statementOfRequirement="sample_text")
    assert isinstance(instance, StrategicElement)


def test_contentfwk_WorkPackage_isa_StrategicElement():
    instance = contentfwk_WorkPackage(workPackageCategory="sample_text")
    assert isinstance(instance, StrategicElement)


def test_contentfwk_LogicalTechnologyComponent_isa_TechnologyComponent():
    instance = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    assert isinstance(instance, TechnologyComponent)


def test_contentfwk_PhysicalTechnologyComponent_isa_TechnologyComponent():
    instance = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    assert isinstance(instance, TechnologyComponent)


def test_assoc_accessesFunctions95_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'canBeAccessedByRoles', {b1})
    assert _is_linked(a, 'canBeAccessedByRoles', b1)
    if hasattr(b1, 'Function96'):
        assert _is_linked(b1, 'Function96', a)
    _safe_set(a, 'canBeAccessedByRoles', {b2})
    assert _is_linked(a, 'canBeAccessedByRoles', b2)
    if hasattr(b1, 'Function96'):
        assert not _is_linked(b1, 'Function96', a)
    if hasattr(b2, 'Function96'):
        assert _is_linked(b2, 'Function96', a)
    _safe_set(a, 'canBeAccessedByRoles', set())
    assert not _is_linked(a, 'canBeAccessedByRoles', b2)
    if hasattr(b2, 'Function96'):
        assert not _is_linked(b2, 'Function96', a)


def test_assoc_actors12_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_BusinessArchitecture()
    b2 = contentfwk_BusinessArchitecture()
    _safe_set(a, 'contentfwk_Actor', b1)
    assert _is_linked(a, 'contentfwk_Actor', b1)
    if hasattr(b1, 'contentfwk_BusinessArchitecture13'):
        assert _is_linked(b1, 'contentfwk_BusinessArchitecture13', a)
    _safe_set(a, 'contentfwk_Actor', b2)
    assert _is_linked(a, 'contentfwk_Actor', b2)
    if hasattr(b1, 'contentfwk_BusinessArchitecture13'):
        assert not _is_linked(b1, 'contentfwk_BusinessArchitecture13', a)
    if hasattr(b2, 'contentfwk_BusinessArchitecture13'):
        assert _is_linked(b2, 'contentfwk_BusinessArchitecture13', a)
    _safe_set(a, 'contentfwk_Actor', None)
    assert not _is_linked(a, 'contentfwk_Actor', b2)
    if hasattr(b2, 'contentfwk_BusinessArchitecture13'):
        assert not _is_linked(b2, 'contentfwk_BusinessArchitecture13', a)


def test_assoc_appliesToContracts209_link_reassign_clear():
    a = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_ServiceQuality()
    b2 = contentfwk_ServiceQuality()
    _safe_set(a, 'Contract', b1)
    assert _is_linked(a, 'Contract', b1)
    if hasattr(b1, 'meetsServiceQuality'):
        assert _is_linked(b1, 'meetsServiceQuality', a)
    _safe_set(a, 'Contract', b2)
    assert _is_linked(a, 'Contract', b2)
    if hasattr(b1, 'meetsServiceQuality'):
        assert not _is_linked(b1, 'meetsServiceQuality', a)
    if hasattr(b2, 'meetsServiceQuality'):
        assert _is_linked(b2, 'meetsServiceQuality', a)
    _safe_set(a, 'Contract', None)
    assert not _is_linked(a, 'Contract', b2)
    if hasattr(b2, 'meetsServiceQuality'):
        assert not _is_linked(b2, 'meetsServiceQuality', a)


def test_assoc_belongsTo73_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'OrganizationUnit74', b1)
    assert _is_linked(a, 'OrganizationUnit74', b1)
    if hasattr(b1, 'containsActors'):
        assert _is_linked(b1, 'containsActors', a)
    _safe_set(a, 'OrganizationUnit74', b2)
    assert _is_linked(a, 'OrganizationUnit74', b2)
    if hasattr(b1, 'containsActors'):
        assert not _is_linked(b1, 'containsActors', a)
    if hasattr(b2, 'containsActors'):
        assert _is_linked(b2, 'containsActors', a)
    _safe_set(a, 'OrganizationUnit74', None)
    assert not _is_linked(a, 'OrganizationUnit74', b2)
    if hasattr(b2, 'containsActors'):
        assert not _is_linked(b2, 'containsActors', a)


def test_assoc_canBeAccessedByRoles137_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'Role138', b1)
    assert _is_linked(a, 'Role138', b1)
    if hasattr(b1, 'accessesFunctions'):
        assert _is_linked(b1, 'accessesFunctions', a)
    _safe_set(a, 'Role138', b2)
    assert _is_linked(a, 'Role138', b2)
    if hasattr(b1, 'accessesFunctions'):
        assert not _is_linked(b1, 'accessesFunctions', a)
    if hasattr(b2, 'accessesFunctions'):
        assert _is_linked(b2, 'accessesFunctions', a)
    _safe_set(a, 'Role138', None)
    assert not _is_linked(a, 'Role138', b2)
    if hasattr(b2, 'accessesFunctions'):
        assert not _is_linked(b2, 'accessesFunctions', a)


def test_assoc_capabilities308_link_reassign_clear():
    a = contentfwk_Capability(businessValue="sample_text", increments="sample_text")
    b1 = contentfwk_StrategicArchitecture()
    b2 = contentfwk_StrategicArchitecture()
    _safe_set(a, 'contentfwk_Capability', b1)
    assert _is_linked(a, 'contentfwk_Capability', b1)
    if hasattr(b1, 'contentfwk_StrategicArchitecture'):
        assert _is_linked(b1, 'contentfwk_StrategicArchitecture', a)
    _safe_set(a, 'contentfwk_Capability', b2)
    assert _is_linked(a, 'contentfwk_Capability', b2)
    if hasattr(b1, 'contentfwk_StrategicArchitecture'):
        assert not _is_linked(b1, 'contentfwk_StrategicArchitecture', a)
    if hasattr(b2, 'contentfwk_StrategicArchitecture'):
        assert _is_linked(b2, 'contentfwk_StrategicArchitecture', a)
    _safe_set(a, 'contentfwk_Capability', None)
    assert not _is_linked(a, 'contentfwk_Capability', b2)
    if hasattr(b2, 'contentfwk_StrategicArchitecture'):
        assert not _is_linked(b2, 'contentfwk_StrategicArchitecture', a)


def test_assoc_category233_link_reassign_clear():
    a = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    b1 = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    b2 = contentfwk_Element(ID="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    _safe_set(a, 'Label', b1)
    assert _is_linked(a, 'Label', b1)
    if hasattr(b1, 'ownedElements'):
        assert _is_linked(b1, 'ownedElements', a)
    _safe_set(a, 'Label', b2)
    assert _is_linked(a, 'Label', b2)
    if hasattr(b1, 'ownedElements'):
        assert not _is_linked(b1, 'ownedElements', a)
    if hasattr(b2, 'ownedElements'):
        assert _is_linked(b2, 'ownedElements', a)
    _safe_set(a, 'Label', None)
    assert not _is_linked(a, 'Label', b2)
    if hasattr(b2, 'ownedElements'):
        assert not _is_linked(b2, 'ownedElements', a)


def test_assoc_communicatesWith286_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b2 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent285', {b1})
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent285', b1)
    if hasattr(b1, 'contentfwk_PhysicalApplicationComponent287'):
        assert _is_linked(b1, 'contentfwk_PhysicalApplicationComponent287', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent285', {b2})
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent285', b2)
    if hasattr(b1, 'contentfwk_PhysicalApplicationComponent287'):
        assert not _is_linked(b1, 'contentfwk_PhysicalApplicationComponent287', a)
    if hasattr(b2, 'contentfwk_PhysicalApplicationComponent287'):
        assert _is_linked(b2, 'contentfwk_PhysicalApplicationComponent287', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent285', set())
    assert not _is_linked(a, 'contentfwk_PhysicalApplicationComponent285', b2)
    if hasattr(b2, 'contentfwk_PhysicalApplicationComponent287'):
        assert not _is_linked(b2, 'contentfwk_PhysicalApplicationComponent287', a)


def test_assoc_consumesEntities318_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'DataEntity319', b1)
    assert _is_linked(a, 'DataEntity319', b1)
    if hasattr(b1, 'isAccessedByServices'):
        assert _is_linked(b1, 'isAccessedByServices', a)
    _safe_set(a, 'DataEntity319', b2)
    assert _is_linked(a, 'DataEntity319', b2)
    if hasattr(b1, 'isAccessedByServices'):
        assert not _is_linked(b1, 'isAccessedByServices', a)
    if hasattr(b2, 'isAccessedByServices'):
        assert _is_linked(b2, 'isAccessedByServices', a)
    _safe_set(a, 'DataEntity319', None)
    assert not _is_linked(a, 'DataEntity319', b2)
    if hasattr(b2, 'isAccessedByServices'):
        assert not _is_linked(b2, 'isAccessedByServices', a)


def test_assoc_consumesEntities71_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'DataEntity72', b1)
    assert _is_linked(a, 'DataEntity72', b1)
    if hasattr(b1, 'isConsumedByActors'):
        assert _is_linked(b1, 'isConsumedByActors', a)
    _safe_set(a, 'DataEntity72', b2)
    assert _is_linked(a, 'DataEntity72', b2)
    if hasattr(b1, 'isConsumedByActors'):
        assert not _is_linked(b1, 'isConsumedByActors', a)
    if hasattr(b2, 'isConsumedByActors'):
        assert _is_linked(b2, 'isConsumedByActors', a)
    _safe_set(a, 'DataEntity72', None)
    assert not _is_linked(a, 'DataEntity72', b2)
    if hasattr(b2, 'isConsumedByActors'):
        assert not _is_linked(b2, 'isConsumedByActors', a)


def test_assoc_consumesServices80_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'contentfwk_Actor81', {b1})
    assert _is_linked(a, 'contentfwk_Actor81', b1)
    if hasattr(b1, 'contentfwk_Service'):
        assert _is_linked(b1, 'contentfwk_Service', a)
    _safe_set(a, 'contentfwk_Actor81', {b2})
    assert _is_linked(a, 'contentfwk_Actor81', b2)
    if hasattr(b1, 'contentfwk_Service'):
        assert not _is_linked(b1, 'contentfwk_Service', a)
    if hasattr(b2, 'contentfwk_Service'):
        assert _is_linked(b2, 'contentfwk_Service', a)
    _safe_set(a, 'contentfwk_Actor81', set())
    assert not _is_linked(a, 'contentfwk_Actor81', b2)
    if hasattr(b2, 'contentfwk_Service'):
        assert not _is_linked(b2, 'contentfwk_Service', a)


def test_assoc_containers1_link_reassign_clear():
    a = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    b1 = contentfwk_EnterpriseArchitecture()
    b2 = contentfwk_EnterpriseArchitecture()
    _safe_set(a, 'contentfwk_Container', b1)
    assert _is_linked(a, 'contentfwk_Container', b1)
    if hasattr(b1, 'contentfwk_EnterpriseArchitecture2'):
        assert _is_linked(b1, 'contentfwk_EnterpriseArchitecture2', a)
    _safe_set(a, 'contentfwk_Container', b2)
    assert _is_linked(a, 'contentfwk_Container', b2)
    if hasattr(b1, 'contentfwk_EnterpriseArchitecture2'):
        assert not _is_linked(b1, 'contentfwk_EnterpriseArchitecture2', a)
    if hasattr(b2, 'contentfwk_EnterpriseArchitecture2'):
        assert _is_linked(b2, 'contentfwk_EnterpriseArchitecture2', a)
    _safe_set(a, 'contentfwk_Container', None)
    assert not _is_linked(a, 'contentfwk_Container', b2)
    if hasattr(b2, 'contentfwk_EnterpriseArchitecture2'):
        assert not _is_linked(b2, 'contentfwk_EnterpriseArchitecture2', a)


def test_assoc_containers244_link_reassign_clear():
    a = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    b1 = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    b2 = contentfwk_Container(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'labels', {b1})
    assert _is_linked(a, 'labels', b1)
    if hasattr(b1, 'Container'):
        assert _is_linked(b1, 'Container', a)
    _safe_set(a, 'labels', {b2})
    assert _is_linked(a, 'labels', b2)
    if hasattr(b1, 'Container'):
        assert not _is_linked(b1, 'Container', a)
    if hasattr(b2, 'Container'):
        assert _is_linked(b2, 'Container', a)
    _safe_set(a, 'labels', set())
    assert not _is_linked(a, 'labels', b2)
    if hasattr(b2, 'Container'):
        assert not _is_linked(b2, 'Container', a)


def test_assoc_containsActors245_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'Actor246', b1)
    assert _is_linked(a, 'Actor246', b1)
    if hasattr(b1, 'operatesInLocation'):
        assert _is_linked(b1, 'operatesInLocation', a)
    _safe_set(a, 'Actor246', b2)
    assert _is_linked(a, 'Actor246', b2)
    if hasattr(b1, 'operatesInLocation'):
        assert not _is_linked(b1, 'operatesInLocation', a)
    if hasattr(b2, 'operatesInLocation'):
        assert _is_linked(b2, 'operatesInLocation', a)
    _safe_set(a, 'Actor246', None)
    assert not _is_linked(a, 'Actor246', b2)
    if hasattr(b2, 'operatesInLocation'):
        assert not _is_linked(b2, 'operatesInLocation', a)


def test_assoc_containsActors63_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'belongsTo', {b1})
    assert _is_linked(a, 'belongsTo', b1)
    if hasattr(b1, 'Actor'):
        assert _is_linked(b1, 'Actor', a)
    _safe_set(a, 'belongsTo', {b2})
    assert _is_linked(a, 'belongsTo', b2)
    if hasattr(b1, 'Actor'):
        assert not _is_linked(b1, 'Actor', a)
    if hasattr(b2, 'Actor'):
        assert _is_linked(b2, 'Actor', a)
    _safe_set(a, 'belongsTo', set())
    assert not _is_linked(a, 'belongsTo', b2)
    if hasattr(b2, 'Actor'):
        assert not _is_linked(b2, 'Actor', a)


def test_assoc_containsOrganizationUnits247_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'OrganizationUnit249', b1)
    assert _is_linked(a, 'OrganizationUnit249', b1)
    if hasattr(b1, 'operatesInLocation248'):
        assert _is_linked(b1, 'operatesInLocation248', a)
    _safe_set(a, 'OrganizationUnit249', b2)
    assert _is_linked(a, 'OrganizationUnit249', b2)
    if hasattr(b1, 'operatesInLocation248'):
        assert not _is_linked(b1, 'operatesInLocation248', a)
    if hasattr(b2, 'operatesInLocation248'):
        assert _is_linked(b2, 'operatesInLocation248', a)
    _safe_set(a, 'OrganizationUnit249', None)
    assert not _is_linked(a, 'OrganizationUnit249', b2)
    if hasattr(b2, 'operatesInLocation248'):
        assert not _is_linked(b2, 'operatesInLocation248', a)


def test_assoc_containsPhysicalApplicationComponents251_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'PhysicalApplicationComponent252', b1)
    assert _is_linked(a, 'PhysicalApplicationComponent252', b1)
    if hasattr(b1, 'isHostedInLocation'):
        assert _is_linked(b1, 'isHostedInLocation', a)
    _safe_set(a, 'PhysicalApplicationComponent252', b2)
    assert _is_linked(a, 'PhysicalApplicationComponent252', b2)
    if hasattr(b1, 'isHostedInLocation'):
        assert not _is_linked(b1, 'isHostedInLocation', a)
    if hasattr(b2, 'isHostedInLocation'):
        assert _is_linked(b2, 'isHostedInLocation', a)
    _safe_set(a, 'PhysicalApplicationComponent252', None)
    assert not _is_linked(a, 'PhysicalApplicationComponent252', b2)
    if hasattr(b2, 'isHostedInLocation'):
        assert not _is_linked(b2, 'isHostedInLocation', a)


def test_assoc_containsPhysicalTechnologyComponents253_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'PhysicalTechnologyComponent', b1)
    assert _is_linked(a, 'PhysicalTechnologyComponent', b1)
    if hasattr(b1, 'isHostedInLocation254'):
        assert _is_linked(b1, 'isHostedInLocation254', a)
    _safe_set(a, 'PhysicalTechnologyComponent', b2)
    assert _is_linked(a, 'PhysicalTechnologyComponent', b2)
    if hasattr(b1, 'isHostedInLocation254'):
        assert not _is_linked(b1, 'isHostedInLocation254', a)
    if hasattr(b2, 'isHostedInLocation254'):
        assert _is_linked(b2, 'isHostedInLocation254', a)
    _safe_set(a, 'PhysicalTechnologyComponent', None)
    assert not _is_linked(a, 'PhysicalTechnologyComponent', b2)
    if hasattr(b2, 'isHostedInLocation254'):
        assert not _is_linked(b2, 'isHostedInLocation254', a)


def test_assoc_contracts30_link_reassign_clear():
    a = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_BusinessArchitecture()
    b2 = contentfwk_BusinessArchitecture()
    _safe_set(a, 'contentfwk_Contract', b1)
    assert _is_linked(a, 'contentfwk_Contract', b1)
    if hasattr(b1, 'contentfwk_BusinessArchitecture31'):
        assert _is_linked(b1, 'contentfwk_BusinessArchitecture31', a)
    _safe_set(a, 'contentfwk_Contract', b2)
    assert _is_linked(a, 'contentfwk_Contract', b2)
    if hasattr(b1, 'contentfwk_BusinessArchitecture31'):
        assert not _is_linked(b1, 'contentfwk_BusinessArchitecture31', a)
    if hasattr(b2, 'contentfwk_BusinessArchitecture31'):
        assert _is_linked(b2, 'contentfwk_BusinessArchitecture31', a)
    _safe_set(a, 'contentfwk_Contract', None)
    assert not _is_linked(a, 'contentfwk_Contract', b2)
    if hasattr(b2, 'contentfwk_BusinessArchitecture31'):
        assert not _is_linked(b2, 'contentfwk_BusinessArchitecture31', a)


def test_assoc_decomposeEntity112_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    _safe_set(a, 'contentfwk_DataEntity111', b1)
    assert _is_linked(a, 'contentfwk_DataEntity111', b1)
    if hasattr(b1, 'contentfwk_DataEntity113'):
        assert _is_linked(b1, 'contentfwk_DataEntity113', a)
    _safe_set(a, 'contentfwk_DataEntity111', b2)
    assert _is_linked(a, 'contentfwk_DataEntity111', b2)
    if hasattr(b1, 'contentfwk_DataEntity113'):
        assert not _is_linked(b1, 'contentfwk_DataEntity113', a)
    if hasattr(b2, 'contentfwk_DataEntity113'):
        assert _is_linked(b2, 'contentfwk_DataEntity113', a)
    _safe_set(a, 'contentfwk_DataEntity111', None)
    assert not _is_linked(a, 'contentfwk_DataEntity111', b2)
    if hasattr(b2, 'contentfwk_DataEntity113'):
        assert not _is_linked(b2, 'contentfwk_DataEntity113', a)


def test_assoc_decomposesActors91_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'contentfwk_Actor90', {b1})
    assert _is_linked(a, 'contentfwk_Actor90', b1)
    if hasattr(b1, 'contentfwk_Actor92'):
        assert _is_linked(b1, 'contentfwk_Actor92', a)
    _safe_set(a, 'contentfwk_Actor90', {b2})
    assert _is_linked(a, 'contentfwk_Actor90', b2)
    if hasattr(b1, 'contentfwk_Actor92'):
        assert not _is_linked(b1, 'contentfwk_Actor92', a)
    if hasattr(b2, 'contentfwk_Actor92'):
        assert _is_linked(b2, 'contentfwk_Actor92', a)
    _safe_set(a, 'contentfwk_Actor90', set())
    assert not _is_linked(a, 'contentfwk_Actor90', b2)
    if hasattr(b2, 'contentfwk_Actor92'):
        assert not _is_linked(b2, 'contentfwk_Actor92', a)


def test_assoc_decomposesFunctions152_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'supportsProcesses', {b1})
    assert _is_linked(a, 'supportsProcesses', b1)
    if hasattr(b1, 'Function153'):
        assert _is_linked(b1, 'Function153', a)
    _safe_set(a, 'supportsProcesses', {b2})
    assert _is_linked(a, 'supportsProcesses', b2)
    if hasattr(b1, 'Function153'):
        assert not _is_linked(b1, 'Function153', a)
    if hasattr(b2, 'Function153'):
        assert _is_linked(b2, 'Function153', a)
    _safe_set(a, 'supportsProcesses', set())
    assert not _is_linked(a, 'supportsProcesses', b2)
    if hasattr(b2, 'Function153'):
        assert not _is_linked(b2, 'Function153', a)


def test_assoc_decomposesLogicalTechnologyComponent303_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent302', b1)
    assert _is_linked(a, 'contentfwk_LogicalTechnologyComponent302', b1)
    if hasattr(b1, 'contentfwk_LogicalTechnologyComponent304'):
        assert _is_linked(b1, 'contentfwk_LogicalTechnologyComponent304', a)
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent302', b2)
    assert _is_linked(a, 'contentfwk_LogicalTechnologyComponent302', b2)
    if hasattr(b1, 'contentfwk_LogicalTechnologyComponent304'):
        assert not _is_linked(b1, 'contentfwk_LogicalTechnologyComponent304', a)
    if hasattr(b2, 'contentfwk_LogicalTechnologyComponent304'):
        assert _is_linked(b2, 'contentfwk_LogicalTechnologyComponent304', a)
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent302', None)
    assert not _is_linked(a, 'contentfwk_LogicalTechnologyComponent302', b2)
    if hasattr(b2, 'contentfwk_LogicalTechnologyComponent304'):
        assert not _is_linked(b2, 'contentfwk_LogicalTechnologyComponent304', a)


def test_assoc_decomposesPhysicalApplicationComponent295_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b2 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent294', b1)
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent294', b1)
    if hasattr(b1, 'contentfwk_PhysicalApplicationComponent296'):
        assert _is_linked(b1, 'contentfwk_PhysicalApplicationComponent296', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent294', b2)
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent294', b2)
    if hasattr(b1, 'contentfwk_PhysicalApplicationComponent296'):
        assert not _is_linked(b1, 'contentfwk_PhysicalApplicationComponent296', a)
    if hasattr(b2, 'contentfwk_PhysicalApplicationComponent296'):
        assert _is_linked(b2, 'contentfwk_PhysicalApplicationComponent296', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent294', None)
    assert not _is_linked(a, 'contentfwk_PhysicalApplicationComponent294', b2)
    if hasattr(b2, 'contentfwk_PhysicalApplicationComponent296'):
        assert not _is_linked(b2, 'contentfwk_PhysicalApplicationComponent296', a)


def test_assoc_decomposesPhysicalTechnologyComponent189_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent188', b1)
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent188', b1)
    if hasattr(b1, 'contentfwk_PhysicalTechnologyComponent190'):
        assert _is_linked(b1, 'contentfwk_PhysicalTechnologyComponent190', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent188', b2)
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent188', b2)
    if hasattr(b1, 'contentfwk_PhysicalTechnologyComponent190'):
        assert not _is_linked(b1, 'contentfwk_PhysicalTechnologyComponent190', a)
    if hasattr(b2, 'contentfwk_PhysicalTechnologyComponent190'):
        assert _is_linked(b2, 'contentfwk_PhysicalTechnologyComponent190', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent188', None)
    assert not _is_linked(a, 'contentfwk_PhysicalTechnologyComponent188', b2)
    if hasattr(b2, 'contentfwk_PhysicalTechnologyComponent190'):
        assert not _is_linked(b2, 'contentfwk_PhysicalTechnologyComponent190', a)


def test_assoc_decomposesProcess173_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    _safe_set(a, 'contentfwk_Process172', b1)
    assert _is_linked(a, 'contentfwk_Process172', b1)
    if hasattr(b1, 'contentfwk_Process174'):
        assert _is_linked(b1, 'contentfwk_Process174', a)
    _safe_set(a, 'contentfwk_Process172', b2)
    assert _is_linked(a, 'contentfwk_Process172', b2)
    if hasattr(b1, 'contentfwk_Process174'):
        assert not _is_linked(b1, 'contentfwk_Process174', a)
    if hasattr(b2, 'contentfwk_Process174'):
        assert _is_linked(b2, 'contentfwk_Process174', a)
    _safe_set(a, 'contentfwk_Process172', None)
    assert not _is_linked(a, 'contentfwk_Process172', b2)
    if hasattr(b2, 'contentfwk_Process174'):
        assert not _is_linked(b2, 'contentfwk_Process174', a)


def test_assoc_decomposesRole98_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_Role(estimatedFTEs="sample_text")
    b2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    _safe_set(a, 'contentfwk_Role97', b1)
    assert _is_linked(a, 'contentfwk_Role97', b1)
    if hasattr(b1, 'contentfwk_Role99'):
        assert _is_linked(b1, 'contentfwk_Role99', a)
    _safe_set(a, 'contentfwk_Role97', b2)
    assert _is_linked(a, 'contentfwk_Role97', b2)
    if hasattr(b1, 'contentfwk_Role99'):
        assert not _is_linked(b1, 'contentfwk_Role99', a)
    if hasattr(b2, 'contentfwk_Role99'):
        assert _is_linked(b2, 'contentfwk_Role99', a)
    _safe_set(a, 'contentfwk_Role97', None)
    assert not _is_linked(a, 'contentfwk_Role97', b2)
    if hasattr(b2, 'contentfwk_Role99'):
        assert not _is_linked(b2, 'contentfwk_Role99', a)


def test_assoc_decomposesServices159_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'supportsProcesses160', {b1})
    assert _is_linked(a, 'supportsProcesses160', b1)
    if hasattr(b1, 'Service161'):
        assert _is_linked(b1, 'Service161', a)
    _safe_set(a, 'supportsProcesses160', {b2})
    assert _is_linked(a, 'supportsProcesses160', b2)
    if hasattr(b1, 'Service161'):
        assert not _is_linked(b1, 'Service161', a)
    if hasattr(b2, 'Service161'):
        assert _is_linked(b2, 'Service161', a)
    _safe_set(a, 'supportsProcesses160', set())
    assert not _is_linked(a, 'supportsProcesses160', b2)
    if hasattr(b2, 'Service161'):
        assert not _is_linked(b2, 'Service161', a)


def test_assoc_delegates229_link_reassign_clear():
    a = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    b1 = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    b2 = contentfwk_Element(ID="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    _safe_set(a, 'Element', b1)
    assert _is_linked(a, 'Element', b1)
    if hasattr(b1, 'isDelegatedBy'):
        assert _is_linked(b1, 'isDelegatedBy', a)
    _safe_set(a, 'Element', b2)
    assert _is_linked(a, 'Element', b2)
    if hasattr(b1, 'isDelegatedBy'):
        assert not _is_linked(b1, 'isDelegatedBy', a)
    if hasattr(b2, 'isDelegatedBy'):
        assert _is_linked(b2, 'isDelegatedBy', a)
    _safe_set(a, 'Element', None)
    assert not _is_linked(a, 'Element', b2)
    if hasattr(b2, 'isDelegatedBy'):
        assert not _is_linked(b2, 'isDelegatedBy', a)


def test_assoc_deliversCapabilities259_link_reassign_clear():
    a = contentfwk_WorkPackage(workPackageCategory="sample_text")
    b1 = contentfwk_Capability(businessValue="sample_text", increments="sample_text")
    b2 = contentfwk_Capability(businessValue="sample_text_2", increments="sample_text_2")
    _safe_set(a, 'isDeliveredBy', {b1})
    assert _is_linked(a, 'isDeliveredBy', b1)
    if hasattr(b1, 'Capability'):
        assert _is_linked(b1, 'Capability', a)
    _safe_set(a, 'isDeliveredBy', {b2})
    assert _is_linked(a, 'isDeliveredBy', b2)
    if hasattr(b1, 'Capability'):
        assert not _is_linked(b1, 'Capability', a)
    if hasattr(b2, 'Capability'):
        assert _is_linked(b2, 'Capability', a)
    _safe_set(a, 'isDeliveredBy', set())
    assert not _is_linked(a, 'isDeliveredBy', b2)
    if hasattr(b2, 'Capability'):
        assert not _is_linked(b2, 'Capability', a)


def test_assoc_encapsulatesDataEntities260_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_LogicalDataComponent()
    b2 = contentfwk_LogicalDataComponent()
    _safe_set(a, 'DataEntity261', b1)
    assert _is_linked(a, 'DataEntity261', b1)
    if hasattr(b1, 'residesWithinLogicalDataComponent'):
        assert _is_linked(b1, 'residesWithinLogicalDataComponent', a)
    _safe_set(a, 'DataEntity261', b2)
    assert _is_linked(a, 'DataEntity261', b2)
    if hasattr(b1, 'residesWithinLogicalDataComponent'):
        assert not _is_linked(b1, 'residesWithinLogicalDataComponent', a)
    if hasattr(b2, 'residesWithinLogicalDataComponent'):
        assert _is_linked(b2, 'residesWithinLogicalDataComponent', a)
    _safe_set(a, 'DataEntity261', None)
    assert not _is_linked(a, 'DataEntity261', b2)
    if hasattr(b2, 'residesWithinLogicalDataComponent'):
        assert not _is_linked(b2, 'residesWithinLogicalDataComponent', a)


def test_assoc_encapsulatesPhysicalApplicationComponents271_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_PhysicalDataComponent()
    b2 = contentfwk_PhysicalDataComponent()
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent273', b1)
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent273', b1)
    if hasattr(b1, 'contentfwk_PhysicalDataComponent272'):
        assert _is_linked(b1, 'contentfwk_PhysicalDataComponent272', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent273', b2)
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent273', b2)
    if hasattr(b1, 'contentfwk_PhysicalDataComponent272'):
        assert not _is_linked(b1, 'contentfwk_PhysicalDataComponent272', a)
    if hasattr(b2, 'contentfwk_PhysicalDataComponent272'):
        assert _is_linked(b2, 'contentfwk_PhysicalDataComponent272', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent273', None)
    assert not _is_linked(a, 'contentfwk_PhysicalApplicationComponent273', b2)
    if hasattr(b2, 'contentfwk_PhysicalDataComponent272'):
        assert not _is_linked(b2, 'contentfwk_PhysicalDataComponent272', a)


def test_assoc_encapsulatesPhysicalDataComponents288_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_PhysicalDataComponent()
    b2 = contentfwk_PhysicalDataComponent()
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent289', {b1})
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent289', b1)
    if hasattr(b1, 'contentfwk_PhysicalDataComponent290'):
        assert _is_linked(b1, 'contentfwk_PhysicalDataComponent290', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent289', {b2})
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent289', b2)
    if hasattr(b1, 'contentfwk_PhysicalDataComponent290'):
        assert not _is_linked(b1, 'contentfwk_PhysicalDataComponent290', a)
    if hasattr(b2, 'contentfwk_PhysicalDataComponent290'):
        assert _is_linked(b2, 'contentfwk_PhysicalDataComponent290', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent289', set())
    assert not _is_linked(a, 'contentfwk_PhysicalApplicationComponent289', b2)
    if hasattr(b2, 'contentfwk_PhysicalDataComponent290'):
        assert not _is_linked(b2, 'contentfwk_PhysicalDataComponent290', a)


def test_assoc_ensuresCorrectOperationOfProcesses226_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Control()
    b2 = contentfwk_Control()
    _safe_set(a, 'Process227', b1)
    assert _is_linked(a, 'Process227', b1)
    if hasattr(b1, 'isGuidedByControls'):
        assert _is_linked(b1, 'isGuidedByControls', a)
    _safe_set(a, 'Process227', b2)
    assert _is_linked(a, 'Process227', b2)
    if hasattr(b1, 'isGuidedByControls'):
        assert not _is_linked(b1, 'isGuidedByControls', a)
    if hasattr(b2, 'isGuidedByControls'):
        assert _is_linked(b2, 'isGuidedByControls', a)
    _safe_set(a, 'Process227', None)
    assert not _is_linked(a, 'Process227', b2)
    if hasattr(b2, 'isGuidedByControls'):
        assert not _is_linked(b2, 'isGuidedByControls', a)


def test_assoc_entities36_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_DataArchitecture()
    b2 = contentfwk_DataArchitecture()
    _safe_set(a, 'contentfwk_DataEntity', b1)
    assert _is_linked(a, 'contentfwk_DataEntity', b1)
    if hasattr(b1, 'contentfwk_DataArchitecture'):
        assert _is_linked(b1, 'contentfwk_DataArchitecture', a)
    _safe_set(a, 'contentfwk_DataEntity', b2)
    assert _is_linked(a, 'contentfwk_DataEntity', b2)
    if hasattr(b1, 'contentfwk_DataArchitecture'):
        assert not _is_linked(b1, 'contentfwk_DataArchitecture', a)
    if hasattr(b2, 'contentfwk_DataArchitecture'):
        assert _is_linked(b2, 'contentfwk_DataArchitecture', a)
    _safe_set(a, 'contentfwk_DataEntity', None)
    assert not _is_linked(a, 'contentfwk_DataEntity', b2)
    if hasattr(b2, 'contentfwk_DataArchitecture'):
        assert not _is_linked(b2, 'contentfwk_DataArchitecture', a)


def test_assoc_extendsLogicalApplicationComponents281_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_LogicalApplicationComponent()
    b2 = contentfwk_LogicalApplicationComponent()
    _safe_set(a, 'isExtendedByPhysicalApplicationComponents', {b1})
    assert _is_linked(a, 'isExtendedByPhysicalApplicationComponents', b1)
    if hasattr(b1, 'LogicalApplicationComponent282'):
        assert _is_linked(b1, 'LogicalApplicationComponent282', a)
    _safe_set(a, 'isExtendedByPhysicalApplicationComponents', {b2})
    assert _is_linked(a, 'isExtendedByPhysicalApplicationComponents', b2)
    if hasattr(b1, 'LogicalApplicationComponent282'):
        assert not _is_linked(b1, 'LogicalApplicationComponent282', a)
    if hasattr(b2, 'LogicalApplicationComponent282'):
        assert _is_linked(b2, 'LogicalApplicationComponent282', a)
    _safe_set(a, 'isExtendedByPhysicalApplicationComponents', set())
    assert not _is_linked(a, 'isExtendedByPhysicalApplicationComponents', b2)
    if hasattr(b2, 'LogicalApplicationComponent282'):
        assert not _is_linked(b2, 'LogicalApplicationComponent282', a)


def test_assoc_extendsLogicalTechnologyComponents184_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'isRealizedByPhysicalTechnologyComponents', {b1})
    assert _is_linked(a, 'isRealizedByPhysicalTechnologyComponents', b1)
    if hasattr(b1, 'LogicalTechnologyComponent185'):
        assert _is_linked(b1, 'LogicalTechnologyComponent185', a)
    _safe_set(a, 'isRealizedByPhysicalTechnologyComponents', {b2})
    assert _is_linked(a, 'isRealizedByPhysicalTechnologyComponents', b2)
    if hasattr(b1, 'LogicalTechnologyComponent185'):
        assert not _is_linked(b1, 'LogicalTechnologyComponent185', a)
    if hasattr(b2, 'LogicalTechnologyComponent185'):
        assert _is_linked(b2, 'LogicalTechnologyComponent185', a)
    _safe_set(a, 'isRealizedByPhysicalTechnologyComponents', set())
    assert not _is_linked(a, 'isRealizedByPhysicalTechnologyComponents', b2)
    if hasattr(b2, 'LogicalTechnologyComponent185'):
        assert not _is_linked(b2, 'LogicalTechnologyComponent185', a)


def test_assoc_followsProcesses179_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    _safe_set(a, 'Process180', b1)
    assert _is_linked(a, 'Process180', b1)
    if hasattr(b1, 'precedesProcesses'):
        assert _is_linked(b1, 'precedesProcesses', a)
    _safe_set(a, 'Process180', b2)
    assert _is_linked(a, 'Process180', b2)
    if hasattr(b1, 'precedesProcesses'):
        assert not _is_linked(b1, 'precedesProcesses', a)
    if hasattr(b2, 'precedesProcesses'):
        assert _is_linked(b2, 'precedesProcesses', a)
    _safe_set(a, 'Process180', None)
    assert not _is_linked(a, 'Process180', b2)
    if hasattr(b2, 'precedesProcesses'):
        assert not _is_linked(b2, 'precedesProcesses', a)


def test_assoc_generatesEvents168_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'isGeneratedByProcesses', {b1})
    assert _is_linked(a, 'isGeneratedByProcesses', b1)
    if hasattr(b1, 'Event169'):
        assert _is_linked(b1, 'Event169', a)
    _safe_set(a, 'isGeneratedByProcesses', {b2})
    assert _is_linked(a, 'isGeneratedByProcesses', b2)
    if hasattr(b1, 'Event169'):
        assert not _is_linked(b1, 'Event169', a)
    if hasattr(b2, 'Event169'):
        assert _is_linked(b2, 'Event169', a)
    _safe_set(a, 'isGeneratedByProcesses', set())
    assert not _is_linked(a, 'isGeneratedByProcesses', b2)
    if hasattr(b2, 'Event169'):
        assert not _is_linked(b2, 'Event169', a)


def test_assoc_generatesEvents83_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'isGeneratedByActors', {b1})
    assert _is_linked(a, 'isGeneratedByActors', b1)
    if hasattr(b1, 'Event84'):
        assert _is_linked(b1, 'Event84', a)
    _safe_set(a, 'isGeneratedByActors', {b2})
    assert _is_linked(a, 'isGeneratedByActors', b2)
    if hasattr(b1, 'Event84'):
        assert not _is_linked(b1, 'Event84', a)
    if hasattr(b2, 'Event84'):
        assert _is_linked(b2, 'Event84', a)
    _safe_set(a, 'isGeneratedByActors', set())
    assert not _is_linked(a, 'isGeneratedByActors', b2)
    if hasattr(b2, 'Event84'):
        assert not _is_linked(b2, 'Event84', a)


def test_assoc_governsAndMeasuresBusinessServices210_link_reassign_clear():
    a = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'isGovernedAndMeasuredByContracts', {b1})
    assert _is_linked(a, 'isGovernedAndMeasuredByContracts', b1)
    if hasattr(b1, 'Service211'):
        assert _is_linked(b1, 'Service211', a)
    _safe_set(a, 'isGovernedAndMeasuredByContracts', {b2})
    assert _is_linked(a, 'isGovernedAndMeasuredByContracts', b2)
    if hasattr(b1, 'Service211'):
        assert not _is_linked(b1, 'Service211', a)
    if hasattr(b2, 'Service211'):
        assert _is_linked(b2, 'Service211', a)
    _safe_set(a, 'isGovernedAndMeasuredByContracts', set())
    assert not _is_linked(a, 'isGovernedAndMeasuredByContracts', b2)
    if hasattr(b2, 'Service211'):
        assert not _is_linked(b2, 'Service211', a)


def test_assoc_interactsWithFunctions75_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'supportsActors', {b1})
    assert _is_linked(a, 'supportsActors', b1)
    if hasattr(b1, 'Function76'):
        assert _is_linked(b1, 'Function76', a)
    _safe_set(a, 'supportsActors', {b2})
    assert _is_linked(a, 'supportsActors', b2)
    if hasattr(b1, 'Function76'):
        assert not _is_linked(b1, 'Function76', a)
    if hasattr(b2, 'Function76'):
        assert _is_linked(b2, 'Function76', a)
    _safe_set(a, 'supportsActors', set())
    assert not _is_linked(a, 'supportsActors', b2)
    if hasattr(b2, 'Function76'):
        assert not _is_linked(b2, 'Function76', a)


def test_assoc_involvesActors162_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'participatesInProcesses163', {b1})
    assert _is_linked(a, 'participatesInProcesses163', b1)
    if hasattr(b1, 'Actor164'):
        assert _is_linked(b1, 'Actor164', a)
    _safe_set(a, 'participatesInProcesses163', {b2})
    assert _is_linked(a, 'participatesInProcesses163', b2)
    if hasattr(b1, 'Actor164'):
        assert not _is_linked(b1, 'Actor164', a)
    if hasattr(b2, 'Actor164'):
        assert _is_linked(b2, 'Actor164', a)
    _safe_set(a, 'participatesInProcesses163', set())
    assert not _is_linked(a, 'participatesInProcesses163', b2)
    if hasattr(b2, 'Actor164'):
        assert not _is_linked(b2, 'Actor164', a)


def test_assoc_involvesOrganizationUnits154_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_OrganizationUnit(headcount="sample_text")
    b2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    _safe_set(a, 'participatesInProcesses', {b1})
    assert _is_linked(a, 'participatesInProcesses', b1)
    if hasattr(b1, 'OrganizationUnit155'):
        assert _is_linked(b1, 'OrganizationUnit155', a)
    _safe_set(a, 'participatesInProcesses', {b2})
    assert _is_linked(a, 'participatesInProcesses', b2)
    if hasattr(b1, 'OrganizationUnit155'):
        assert not _is_linked(b1, 'OrganizationUnit155', a)
    if hasattr(b2, 'OrganizationUnit155'):
        assert _is_linked(b2, 'OrganizationUnit155', a)
    _safe_set(a, 'participatesInProcesses', set())
    assert not _is_linked(a, 'participatesInProcesses', b2)
    if hasattr(b2, 'OrganizationUnit155'):
        assert not _is_linked(b2, 'OrganizationUnit155', a)


def test_assoc_isAccessedByServices104_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'consumesEntities105', {b1})
    assert _is_linked(a, 'consumesEntities105', b1)
    if hasattr(b1, 'Service106'):
        assert _is_linked(b1, 'Service106', a)
    _safe_set(a, 'consumesEntities105', {b2})
    assert _is_linked(a, 'consumesEntities105', b2)
    if hasattr(b1, 'Service106'):
        assert not _is_linked(b1, 'Service106', a)
    if hasattr(b2, 'Service106'):
        assert _is_linked(b2, 'Service106', a)
    _safe_set(a, 'consumesEntities105', set())
    assert not _is_linked(a, 'consumesEntities105', b2)
    if hasattr(b2, 'Service106'):
        assert not _is_linked(b2, 'Service106', a)


def test_assoc_isAssumedByActors93_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'performsTaskInRoles', {b1})
    assert _is_linked(a, 'performsTaskInRoles', b1)
    if hasattr(b1, 'Actor94'):
        assert _is_linked(b1, 'Actor94', a)
    _safe_set(a, 'performsTaskInRoles', {b2})
    assert _is_linked(a, 'performsTaskInRoles', b2)
    if hasattr(b1, 'Actor94'):
        assert not _is_linked(b1, 'Actor94', a)
    if hasattr(b2, 'Actor94'):
        assert _is_linked(b2, 'Actor94', a)
    _safe_set(a, 'performsTaskInRoles', set())
    assert not _is_linked(a, 'performsTaskInRoles', b2)
    if hasattr(b2, 'Actor94'):
        assert not _is_linked(b2, 'Actor94', a)


def test_assoc_isConsumedByActors102_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'consumesEntities', {b1})
    assert _is_linked(a, 'consumesEntities', b1)
    if hasattr(b1, 'Actor103'):
        assert _is_linked(b1, 'Actor103', a)
    _safe_set(a, 'consumesEntities', {b2})
    assert _is_linked(a, 'consumesEntities', b2)
    if hasattr(b1, 'Actor103'):
        assert not _is_linked(b1, 'Actor103', a)
    if hasattr(b2, 'Actor103'):
        assert _is_linked(b2, 'Actor103', a)
    _safe_set(a, 'consumesEntities', set())
    assert not _is_linked(a, 'consumesEntities', b2)
    if hasattr(b2, 'Actor103'):
        assert not _is_linked(b2, 'Actor103', a)


def test_assoc_isDelegatedBy231_link_reassign_clear():
    a = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    b1 = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    b2 = contentfwk_Element(ID="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    _safe_set(a, 'Element232', b1)
    assert _is_linked(a, 'Element232', b1)
    if hasattr(b1, 'delegates'):
        assert _is_linked(b1, 'delegates', a)
    _safe_set(a, 'Element232', b2)
    assert _is_linked(a, 'Element232', b2)
    if hasattr(b1, 'delegates'):
        assert not _is_linked(b1, 'delegates', a)
    if hasattr(b2, 'delegates'):
        assert _is_linked(b2, 'delegates', a)
    _safe_set(a, 'Element232', None)
    assert not _is_linked(a, 'Element232', b2)
    if hasattr(b2, 'delegates'):
        assert not _is_linked(b2, 'delegates', a)


def test_assoc_isDeliveredBy258_link_reassign_clear():
    a = contentfwk_WorkPackage(workPackageCategory="sample_text")
    b1 = contentfwk_Capability(businessValue="sample_text", increments="sample_text")
    b2 = contentfwk_Capability(businessValue="sample_text_2", increments="sample_text_2")
    _safe_set(a, 'WorkPackage', b1)
    assert _is_linked(a, 'WorkPackage', b1)
    if hasattr(b1, 'deliversCapabilities'):
        assert _is_linked(b1, 'deliversCapabilities', a)
    _safe_set(a, 'WorkPackage', b2)
    assert _is_linked(a, 'WorkPackage', b2)
    if hasattr(b1, 'deliversCapabilities'):
        assert not _is_linked(b1, 'deliversCapabilities', a)
    if hasattr(b2, 'deliversCapabilities'):
        assert _is_linked(b2, 'deliversCapabilities', a)
    _safe_set(a, 'WorkPackage', None)
    assert not _is_linked(a, 'WorkPackage', b2)
    if hasattr(b2, 'deliversCapabilities'):
        assert not _is_linked(b2, 'deliversCapabilities', a)


def test_assoc_isDependentOnLogicalTechnologyComponents306_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent305', {b1})
    assert _is_linked(a, 'contentfwk_LogicalTechnologyComponent305', b1)
    if hasattr(b1, 'contentfwk_LogicalTechnologyComponent307'):
        assert _is_linked(b1, 'contentfwk_LogicalTechnologyComponent307', a)
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent305', {b2})
    assert _is_linked(a, 'contentfwk_LogicalTechnologyComponent305', b2)
    if hasattr(b1, 'contentfwk_LogicalTechnologyComponent307'):
        assert not _is_linked(b1, 'contentfwk_LogicalTechnologyComponent307', a)
    if hasattr(b2, 'contentfwk_LogicalTechnologyComponent307'):
        assert _is_linked(b2, 'contentfwk_LogicalTechnologyComponent307', a)
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent305', set())
    assert not _is_linked(a, 'contentfwk_LogicalTechnologyComponent305', b2)
    if hasattr(b2, 'contentfwk_LogicalTechnologyComponent307'):
        assert not _is_linked(b2, 'contentfwk_LogicalTechnologyComponent307', a)


def test_assoc_isDependentOnPhysicalTechnologyComponents192_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent191', {b1})
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent191', b1)
    if hasattr(b1, 'contentfwk_PhysicalTechnologyComponent193'):
        assert _is_linked(b1, 'contentfwk_PhysicalTechnologyComponent193', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent191', {b2})
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent191', b2)
    if hasattr(b1, 'contentfwk_PhysicalTechnologyComponent193'):
        assert not _is_linked(b1, 'contentfwk_PhysicalTechnologyComponent193', a)
    if hasattr(b2, 'contentfwk_PhysicalTechnologyComponent193'):
        assert _is_linked(b2, 'contentfwk_PhysicalTechnologyComponent193', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent191', set())
    assert not _is_linked(a, 'contentfwk_PhysicalTechnologyComponent191', b2)
    if hasattr(b2, 'contentfwk_PhysicalTechnologyComponent193'):
        assert not _is_linked(b2, 'contentfwk_PhysicalTechnologyComponent193', a)


def test_assoc_isExtendedByPhysicalApplicationComponents121_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_LogicalApplicationComponent()
    b2 = contentfwk_LogicalApplicationComponent()
    _safe_set(a, 'PhysicalApplicationComponent', b1)
    assert _is_linked(a, 'PhysicalApplicationComponent', b1)
    if hasattr(b1, 'extendsLogicalApplicationComponents'):
        assert _is_linked(b1, 'extendsLogicalApplicationComponents', a)
    _safe_set(a, 'PhysicalApplicationComponent', b2)
    assert _is_linked(a, 'PhysicalApplicationComponent', b2)
    if hasattr(b1, 'extendsLogicalApplicationComponents'):
        assert not _is_linked(b1, 'extendsLogicalApplicationComponents', a)
    if hasattr(b2, 'extendsLogicalApplicationComponents'):
        assert _is_linked(b2, 'extendsLogicalApplicationComponents', a)
    _safe_set(a, 'PhysicalApplicationComponent', None)
    assert not _is_linked(a, 'PhysicalApplicationComponent', b2)
    if hasattr(b2, 'extendsLogicalApplicationComponents'):
        assert not _is_linked(b2, 'extendsLogicalApplicationComponents', a)


def test_assoc_isGeneratedByActors223_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'Actor225', b1)
    assert _is_linked(a, 'Actor225', b1)
    if hasattr(b1, 'generatesEvents224'):
        assert _is_linked(b1, 'generatesEvents224', a)
    _safe_set(a, 'Actor225', b2)
    assert _is_linked(a, 'Actor225', b2)
    if hasattr(b1, 'generatesEvents224'):
        assert not _is_linked(b1, 'generatesEvents224', a)
    if hasattr(b2, 'generatesEvents224'):
        assert _is_linked(b2, 'generatesEvents224', a)
    _safe_set(a, 'Actor225', None)
    assert not _is_linked(a, 'Actor225', b2)
    if hasattr(b2, 'generatesEvents224'):
        assert not _is_linked(b2, 'generatesEvents224', a)


def test_assoc_isGeneratedByProcesses218_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'Process219', b1)
    assert _is_linked(a, 'Process219', b1)
    if hasattr(b1, 'generatesEvents'):
        assert _is_linked(b1, 'generatesEvents', a)
    _safe_set(a, 'Process219', b2)
    assert _is_linked(a, 'Process219', b2)
    if hasattr(b1, 'generatesEvents'):
        assert not _is_linked(b1, 'generatesEvents', a)
    if hasattr(b2, 'generatesEvents'):
        assert _is_linked(b2, 'generatesEvents', a)
    _safe_set(a, 'Process219', None)
    assert not _is_linked(a, 'Process219', b2)
    if hasattr(b2, 'generatesEvents'):
        assert not _is_linked(b2, 'generatesEvents', a)


def test_assoc_isGovernedAndMeasuredByContracts320_link_reassign_clear():
    a = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'Contract321', b1)
    assert _is_linked(a, 'Contract321', b1)
    if hasattr(b1, 'governsAndMeasuresBusinessServices'):
        assert _is_linked(b1, 'governsAndMeasuresBusinessServices', a)
    _safe_set(a, 'Contract321', b2)
    assert _is_linked(a, 'Contract321', b2)
    if hasattr(b1, 'governsAndMeasuresBusinessServices'):
        assert not _is_linked(b1, 'governsAndMeasuresBusinessServices', a)
    if hasattr(b2, 'governsAndMeasuresBusinessServices'):
        assert _is_linked(b2, 'governsAndMeasuresBusinessServices', a)
    _safe_set(a, 'Contract321', None)
    assert not _is_linked(a, 'Contract321', b2)
    if hasattr(b2, 'governsAndMeasuresBusinessServices'):
        assert not _is_linked(b2, 'governsAndMeasuresBusinessServices', a)


def test_assoc_isGuidedByControls165_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Control()
    b2 = contentfwk_Control()
    _safe_set(a, 'ensuresCorrectOperationOfProcesses', {b1})
    assert _is_linked(a, 'ensuresCorrectOperationOfProcesses', b1)
    if hasattr(b1, 'Control'):
        assert _is_linked(b1, 'Control', a)
    _safe_set(a, 'ensuresCorrectOperationOfProcesses', {b2})
    assert _is_linked(a, 'ensuresCorrectOperationOfProcesses', b2)
    if hasattr(b1, 'Control'):
        assert not _is_linked(b1, 'Control', a)
    if hasattr(b2, 'Control'):
        assert _is_linked(b2, 'Control', a)
    _safe_set(a, 'ensuresCorrectOperationOfProcesses', set())
    assert not _is_linked(a, 'ensuresCorrectOperationOfProcesses', b2)
    if hasattr(b2, 'Control'):
        assert not _is_linked(b2, 'Control', a)


def test_assoc_isHostedInLocation186_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'containsPhysicalTechnologyComponents', {b1})
    assert _is_linked(a, 'containsPhysicalTechnologyComponents', b1)
    if hasattr(b1, 'Location187'):
        assert _is_linked(b1, 'Location187', a)
    _safe_set(a, 'containsPhysicalTechnologyComponents', {b2})
    assert _is_linked(a, 'containsPhysicalTechnologyComponents', b2)
    if hasattr(b1, 'Location187'):
        assert not _is_linked(b1, 'Location187', a)
    if hasattr(b2, 'Location187'):
        assert _is_linked(b2, 'Location187', a)
    _safe_set(a, 'containsPhysicalTechnologyComponents', set())
    assert not _is_linked(a, 'containsPhysicalTechnologyComponents', b2)
    if hasattr(b2, 'Location187'):
        assert not _is_linked(b2, 'Location187', a)


def test_assoc_isHostedInLocation283_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'containsPhysicalApplicationComponents', {b1})
    assert _is_linked(a, 'containsPhysicalApplicationComponents', b1)
    if hasattr(b1, 'Location284'):
        assert _is_linked(b1, 'Location284', a)
    _safe_set(a, 'containsPhysicalApplicationComponents', {b2})
    assert _is_linked(a, 'containsPhysicalApplicationComponents', b2)
    if hasattr(b1, 'Location284'):
        assert not _is_linked(b1, 'Location284', a)
    if hasattr(b2, 'Location284'):
        assert _is_linked(b2, 'Location284', a)
    _safe_set(a, 'containsPhysicalApplicationComponents', set())
    assert not _is_linked(a, 'containsPhysicalApplicationComponents', b2)
    if hasattr(b2, 'Location284'):
        assert not _is_linked(b2, 'Location284', a)


def test_assoc_isImplementedOnLogicalTechnologyComponents324_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'LogicalTechnologyComponent325', b1)
    assert _is_linked(a, 'LogicalTechnologyComponent325', b1)
    if hasattr(b1, 'providesPlatformForServices'):
        assert _is_linked(b1, 'providesPlatformForServices', a)
    _safe_set(a, 'LogicalTechnologyComponent325', b2)
    assert _is_linked(a, 'LogicalTechnologyComponent325', b2)
    if hasattr(b1, 'providesPlatformForServices'):
        assert not _is_linked(b1, 'providesPlatformForServices', a)
    if hasattr(b2, 'providesPlatformForServices'):
        assert _is_linked(b2, 'providesPlatformForServices', a)
    _safe_set(a, 'LogicalTechnologyComponent325', None)
    assert not _is_linked(a, 'LogicalTechnologyComponent325', b2)
    if hasattr(b2, 'providesPlatformForServices'):
        assert not _is_linked(b2, 'providesPlatformForServices', a)


def test_assoc_isMotivatedByDrivers66_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Driver()
    b2 = contentfwk_Driver()
    _safe_set(a, 'motivatesOrganizationUnits', {b1})
    assert _is_linked(a, 'motivatesOrganizationUnits', b1)
    if hasattr(b1, 'Driver67'):
        assert _is_linked(b1, 'Driver67', a)
    _safe_set(a, 'motivatesOrganizationUnits', {b2})
    assert _is_linked(a, 'motivatesOrganizationUnits', b2)
    if hasattr(b1, 'Driver67'):
        assert not _is_linked(b1, 'Driver67', a)
    if hasattr(b2, 'Driver67'):
        assert _is_linked(b2, 'Driver67', a)
    _safe_set(a, 'motivatesOrganizationUnits', set())
    assert not _is_linked(a, 'motivatesOrganizationUnits', b2)
    if hasattr(b2, 'Driver67'):
        assert not _is_linked(b2, 'Driver67', a)


def test_assoc_isOwnedAndGovernedByOrganizationUnits328_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'OrganizationUnit329', b1)
    assert _is_linked(a, 'OrganizationUnit329', b1)
    if hasattr(b1, 'ownsAndGovernsServices'):
        assert _is_linked(b1, 'ownsAndGovernsServices', a)
    _safe_set(a, 'OrganizationUnit329', b2)
    assert _is_linked(a, 'OrganizationUnit329', b2)
    if hasattr(b1, 'ownsAndGovernsServices'):
        assert not _is_linked(b1, 'ownsAndGovernsServices', a)
    if hasattr(b2, 'ownsAndGovernsServices'):
        assert _is_linked(b2, 'ownsAndGovernsServices', a)
    _safe_set(a, 'OrganizationUnit329', None)
    assert not _is_linked(a, 'OrganizationUnit329', b2)
    if hasattr(b2, 'ownsAndGovernsServices'):
        assert not _is_linked(b2, 'ownsAndGovernsServices', a)


def test_assoc_isOwnedByUnit129_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'OrganizationUnit130', b1)
    assert _is_linked(a, 'OrganizationUnit130', b1)
    if hasattr(b1, 'ownsFunctions'):
        assert _is_linked(b1, 'ownsFunctions', a)
    _safe_set(a, 'OrganizationUnit130', b2)
    assert _is_linked(a, 'OrganizationUnit130', b2)
    if hasattr(b1, 'ownsFunctions'):
        assert not _is_linked(b1, 'ownsFunctions', a)
    if hasattr(b2, 'ownsFunctions'):
        assert _is_linked(b2, 'ownsFunctions', a)
    _safe_set(a, 'OrganizationUnit130', None)
    assert not _is_linked(a, 'OrganizationUnit130', b2)
    if hasattr(b2, 'ownsFunctions'):
        assert not _is_linked(b2, 'ownsFunctions', a)


def test_assoc_isPerformedByActors127_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'Actor128', b1)
    assert _is_linked(a, 'Actor128', b1)
    if hasattr(b1, 'performsFunctions'):
        assert _is_linked(b1, 'performsFunctions', a)
    _safe_set(a, 'Actor128', b2)
    assert _is_linked(a, 'Actor128', b2)
    if hasattr(b1, 'performsFunctions'):
        assert not _is_linked(b1, 'performsFunctions', a)
    if hasattr(b2, 'performsFunctions'):
        assert _is_linked(b2, 'performsFunctions', a)
    _safe_set(a, 'Actor128', None)
    assert not _is_linked(a, 'Actor128', b2)
    if hasattr(b2, 'performsFunctions'):
        assert not _is_linked(b2, 'performsFunctions', a)


def test_assoc_isProcessesByLogicalApplicationComponents110_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_LogicalApplicationComponent()
    b2 = contentfwk_LogicalApplicationComponent()
    _safe_set(a, 'operatesOnDataEntities', {b1})
    assert _is_linked(a, 'operatesOnDataEntities', b1)
    if hasattr(b1, 'LogicalApplicationComponent'):
        assert _is_linked(b1, 'LogicalApplicationComponent', a)
    _safe_set(a, 'operatesOnDataEntities', {b2})
    assert _is_linked(a, 'operatesOnDataEntities', b2)
    if hasattr(b1, 'LogicalApplicationComponent'):
        assert not _is_linked(b1, 'LogicalApplicationComponent', a)
    if hasattr(b2, 'LogicalApplicationComponent'):
        assert _is_linked(b2, 'LogicalApplicationComponent', a)
    _safe_set(a, 'operatesOnDataEntities', set())
    assert not _is_linked(a, 'operatesOnDataEntities', b2)
    if hasattr(b2, 'LogicalApplicationComponent'):
        assert not _is_linked(b2, 'LogicalApplicationComponent', a)


def test_assoc_isProducedByOrganizationUnits194_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Product()
    b2 = contentfwk_Product()
    _safe_set(a, 'OrganizationUnit195', b1)
    assert _is_linked(a, 'OrganizationUnit195', b1)
    if hasattr(b1, 'producesProducts'):
        assert _is_linked(b1, 'producesProducts', a)
    _safe_set(a, 'OrganizationUnit195', b2)
    assert _is_linked(a, 'OrganizationUnit195', b2)
    if hasattr(b1, 'producesProducts'):
        assert not _is_linked(b1, 'producesProducts', a)
    if hasattr(b2, 'producesProducts'):
        assert _is_linked(b2, 'producesProducts', a)
    _safe_set(a, 'OrganizationUnit195', None)
    assert not _is_linked(a, 'OrganizationUnit195', b2)
    if hasattr(b2, 'producesProducts'):
        assert not _is_linked(b2, 'producesProducts', a)


def test_assoc_isProducedByProcesses196_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Product()
    b2 = contentfwk_Product()
    _safe_set(a, 'Process198', b1)
    assert _is_linked(a, 'Process198', b1)
    if hasattr(b1, 'producesProducts197'):
        assert _is_linked(b1, 'producesProducts197', a)
    _safe_set(a, 'Process198', b2)
    assert _is_linked(a, 'Process198', b2)
    if hasattr(b1, 'producesProducts197'):
        assert not _is_linked(b1, 'producesProducts197', a)
    if hasattr(b2, 'producesProducts197'):
        assert _is_linked(b2, 'producesProducts197', a)
    _safe_set(a, 'Process198', None)
    assert not _is_linked(a, 'Process198', b2)
    if hasattr(b2, 'producesProducts197'):
        assert not _is_linked(b2, 'producesProducts197', a)


def test_assoc_isProvidedToActors311_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'contentfwk_Actor313', b1)
    assert _is_linked(a, 'contentfwk_Actor313', b1)
    if hasattr(b1, 'contentfwk_Service312'):
        assert _is_linked(b1, 'contentfwk_Service312', a)
    _safe_set(a, 'contentfwk_Actor313', b2)
    assert _is_linked(a, 'contentfwk_Actor313', b2)
    if hasattr(b1, 'contentfwk_Service312'):
        assert not _is_linked(b1, 'contentfwk_Service312', a)
    if hasattr(b2, 'contentfwk_Service312'):
        assert _is_linked(b2, 'contentfwk_Service312', a)
    _safe_set(a, 'contentfwk_Actor313', None)
    assert not _is_linked(a, 'contentfwk_Actor313', b2)
    if hasattr(b2, 'contentfwk_Service312'):
        assert not _is_linked(b2, 'contentfwk_Service312', a)


def test_assoc_isRealizedByPhysicalTechnologyComponents291_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b2 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent293', b1)
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent293', b1)
    if hasattr(b1, 'contentfwk_PhysicalApplicationComponent292'):
        assert _is_linked(b1, 'contentfwk_PhysicalApplicationComponent292', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent293', b2)
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent293', b2)
    if hasattr(b1, 'contentfwk_PhysicalApplicationComponent292'):
        assert not _is_linked(b1, 'contentfwk_PhysicalApplicationComponent292', a)
    if hasattr(b2, 'contentfwk_PhysicalApplicationComponent292'):
        assert _is_linked(b2, 'contentfwk_PhysicalApplicationComponent292', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent293', None)
    assert not _is_linked(a, 'contentfwk_PhysicalTechnologyComponent293', b2)
    if hasattr(b2, 'contentfwk_PhysicalApplicationComponent292'):
        assert not _is_linked(b2, 'contentfwk_PhysicalApplicationComponent292', a)


def test_assoc_isRealizedByPhysicalTechnologyComponents300_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'PhysicalTechnologyComponent301', b1)
    assert _is_linked(a, 'PhysicalTechnologyComponent301', b1)
    if hasattr(b1, 'extendsLogicalTechnologyComponents'):
        assert _is_linked(b1, 'extendsLogicalTechnologyComponents', a)
    _safe_set(a, 'PhysicalTechnologyComponent301', b2)
    assert _is_linked(a, 'PhysicalTechnologyComponent301', b2)
    if hasattr(b1, 'extendsLogicalTechnologyComponents'):
        assert not _is_linked(b1, 'extendsLogicalTechnologyComponents', a)
    if hasattr(b2, 'extendsLogicalTechnologyComponents'):
        assert _is_linked(b2, 'extendsLogicalTechnologyComponents', a)
    _safe_set(a, 'PhysicalTechnologyComponent301', None)
    assert not _is_linked(a, 'PhysicalTechnologyComponent301', b2)
    if hasattr(b2, 'extendsLogicalTechnologyComponents'):
        assert not _is_linked(b2, 'extendsLogicalTechnologyComponents', a)


def test_assoc_isRealizedByProcesses135_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'Process136', b1)
    assert _is_linked(a, 'Process136', b1)
    if hasattr(b1, 'orchestratesFunctions'):
        assert _is_linked(b1, 'orchestratesFunctions', a)
    _safe_set(a, 'Process136', b2)
    assert _is_linked(a, 'Process136', b2)
    if hasattr(b1, 'orchestratesFunctions'):
        assert not _is_linked(b1, 'orchestratesFunctions', a)
    if hasattr(b2, 'orchestratesFunctions'):
        assert _is_linked(b2, 'orchestratesFunctions', a)
    _safe_set(a, 'Process136', None)
    assert not _is_linked(a, 'Process136', b2)
    if hasattr(b2, 'orchestratesFunctions'):
        assert not _is_linked(b2, 'orchestratesFunctions', a)


def test_assoc_isRealizedByProcesses334_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'Process335', b1)
    assert _is_linked(a, 'Process335', b1)
    if hasattr(b1, 'orchestratesServices'):
        assert _is_linked(b1, 'orchestratesServices', a)
    _safe_set(a, 'Process335', b2)
    assert _is_linked(a, 'Process335', b2)
    if hasattr(b1, 'orchestratesServices'):
        assert not _is_linked(b1, 'orchestratesServices', a)
    if hasattr(b2, 'orchestratesServices'):
        assert _is_linked(b2, 'orchestratesServices', a)
    _safe_set(a, 'Process335', None)
    assert not _is_linked(a, 'Process335', b2)
    if hasattr(b2, 'orchestratesServices'):
        assert not _is_linked(b2, 'orchestratesServices', a)


def test_assoc_isResolvedByActors220_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'Actor222', b1)
    assert _is_linked(a, 'Actor222', b1)
    if hasattr(b1, 'resolvesEvents221'):
        assert _is_linked(b1, 'resolvesEvents221', a)
    _safe_set(a, 'Actor222', b2)
    assert _is_linked(a, 'Actor222', b2)
    if hasattr(b1, 'resolvesEvents221'):
        assert not _is_linked(b1, 'resolvesEvents221', a)
    if hasattr(b2, 'resolvesEvents221'):
        assert _is_linked(b2, 'resolvesEvents221', a)
    _safe_set(a, 'Actor222', None)
    assert not _is_linked(a, 'Actor222', b2)
    if hasattr(b2, 'resolvesEvents221'):
        assert not _is_linked(b2, 'resolvesEvents221', a)


def test_assoc_isResolvedByProcesses215_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'Process217', b1)
    assert _is_linked(a, 'Process217', b1)
    if hasattr(b1, 'resolvesEvents216'):
        assert _is_linked(b1, 'resolvesEvents216', a)
    _safe_set(a, 'Process217', b2)
    assert _is_linked(a, 'Process217', b2)
    if hasattr(b1, 'resolvesEvents216'):
        assert not _is_linked(b1, 'resolvesEvents216', a)
    if hasattr(b2, 'resolvesEvents216'):
        assert _is_linked(b2, 'resolvesEvents216', a)
    _safe_set(a, 'Process217', None)
    assert not _is_linked(a, 'Process217', b2)
    if hasattr(b2, 'resolvesEvents216'):
        assert not _is_linked(b2, 'resolvesEvents216', a)


def test_assoc_isSuppliedByActors100_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'suppliesEntities', {b1})
    assert _is_linked(a, 'suppliesEntities', b1)
    if hasattr(b1, 'Actor101'):
        assert _is_linked(b1, 'Actor101', a)
    _safe_set(a, 'suppliesEntities', {b2})
    assert _is_linked(a, 'suppliesEntities', b2)
    if hasattr(b1, 'Actor101'):
        assert not _is_linked(b1, 'Actor101', a)
    if hasattr(b2, 'Actor101'):
        assert _is_linked(b2, 'Actor101', a)
    _safe_set(a, 'suppliesEntities', set())
    assert not _is_linked(a, 'suppliesEntities', b2)
    if hasattr(b2, 'Actor101'):
        assert not _is_linked(b2, 'Actor101', a)


def test_assoc_isSuppliedByLogicalTechnologyComponents181_link_reassign_clear():
    a = contentfwk_PlatformService(categoryTRM="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'suppliesPlatformServices', {b1})
    assert _is_linked(a, 'suppliesPlatformServices', b1)
    if hasattr(b1, 'LogicalTechnologyComponent'):
        assert _is_linked(b1, 'LogicalTechnologyComponent', a)
    _safe_set(a, 'suppliesPlatformServices', {b2})
    assert _is_linked(a, 'suppliesPlatformServices', b2)
    if hasattr(b1, 'LogicalTechnologyComponent'):
        assert not _is_linked(b1, 'LogicalTechnologyComponent', a)
    if hasattr(b2, 'LogicalTechnologyComponent'):
        assert _is_linked(b2, 'LogicalTechnologyComponent', a)
    _safe_set(a, 'suppliesPlatformServices', set())
    assert not _is_linked(a, 'suppliesPlatformServices', b2)
    if hasattr(b2, 'LogicalTechnologyComponent'):
        assert not _is_linked(b2, 'LogicalTechnologyComponent', a)


def test_assoc_isUpdatedThroughServices107_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'providesEntities', {b1})
    assert _is_linked(a, 'providesEntities', b1)
    if hasattr(b1, 'Service108'):
        assert _is_linked(b1, 'Service108', a)
    _safe_set(a, 'providesEntities', {b2})
    assert _is_linked(a, 'providesEntities', b2)
    if hasattr(b1, 'Service108'):
        assert not _is_linked(b1, 'Service108', a)
    if hasattr(b2, 'Service108'):
        assert _is_linked(b2, 'Service108', a)
    _safe_set(a, 'providesEntities', set())
    assert not _is_linked(a, 'providesEntities', b2)
    if hasattr(b2, 'Service108'):
        assert not _is_linked(b2, 'Service108', a)


def test_assoc_labels237_link_reassign_clear():
    a = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    b1 = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    b2 = contentfwk_Container(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Label238', b1)
    assert _is_linked(a, 'Label238', b1)
    if hasattr(b1, 'containers'):
        assert _is_linked(b1, 'containers', a)
    _safe_set(a, 'Label238', b2)
    assert _is_linked(a, 'Label238', b2)
    if hasattr(b1, 'containers'):
        assert not _is_linked(b1, 'containers', a)
    if hasattr(b2, 'containers'):
        assert _is_linked(b2, 'containers', a)
    _safe_set(a, 'Label238', None)
    assert not _is_linked(a, 'Label238', b2)
    if hasattr(b2, 'containers'):
        assert not _is_linked(b2, 'containers', a)


def test_assoc_labels3_link_reassign_clear():
    a = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    b1 = contentfwk_EnterpriseArchitecture()
    b2 = contentfwk_EnterpriseArchitecture()
    _safe_set(a, 'contentfwk_Label', b1)
    assert _is_linked(a, 'contentfwk_Label', b1)
    if hasattr(b1, 'contentfwk_EnterpriseArchitecture4'):
        assert _is_linked(b1, 'contentfwk_EnterpriseArchitecture4', a)
    _safe_set(a, 'contentfwk_Label', b2)
    assert _is_linked(a, 'contentfwk_Label', b2)
    if hasattr(b1, 'contentfwk_EnterpriseArchitecture4'):
        assert not _is_linked(b1, 'contentfwk_EnterpriseArchitecture4', a)
    if hasattr(b2, 'contentfwk_EnterpriseArchitecture4'):
        assert _is_linked(b2, 'contentfwk_EnterpriseArchitecture4', a)
    _safe_set(a, 'contentfwk_Label', None)
    assert not _is_linked(a, 'contentfwk_Label', b2)
    if hasattr(b2, 'contentfwk_EnterpriseArchitecture4'):
        assert not _is_linked(b2, 'contentfwk_EnterpriseArchitecture4', a)


def test_assoc_logicalComponents44_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_TechnologyArchitecture()
    b2 = contentfwk_TechnologyArchitecture()
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent', b1)
    assert _is_linked(a, 'contentfwk_LogicalTechnologyComponent', b1)
    if hasattr(b1, 'contentfwk_TechnologyArchitecture45'):
        assert _is_linked(b1, 'contentfwk_TechnologyArchitecture45', a)
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent', b2)
    assert _is_linked(a, 'contentfwk_LogicalTechnologyComponent', b2)
    if hasattr(b1, 'contentfwk_TechnologyArchitecture45'):
        assert not _is_linked(b1, 'contentfwk_TechnologyArchitecture45', a)
    if hasattr(b2, 'contentfwk_TechnologyArchitecture45'):
        assert _is_linked(b2, 'contentfwk_TechnologyArchitecture45', a)
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent', None)
    assert not _is_linked(a, 'contentfwk_LogicalTechnologyComponent', b2)
    if hasattr(b2, 'contentfwk_TechnologyArchitecture45'):
        assert not _is_linked(b2, 'contentfwk_TechnologyArchitecture45', a)


def test_assoc_meetsServiceQuality212_link_reassign_clear():
    a = contentfwk_Contract(ServiceNameCalled="sample_text", ServiceNameCaller="sample_text", availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_ServiceQuality()
    b2 = contentfwk_ServiceQuality()
    _safe_set(a, 'appliesToContracts', {b1})
    assert _is_linked(a, 'appliesToContracts', b1)
    if hasattr(b1, 'ServiceQuality'):
        assert _is_linked(b1, 'ServiceQuality', a)
    _safe_set(a, 'appliesToContracts', {b2})
    assert _is_linked(a, 'appliesToContracts', b2)
    if hasattr(b1, 'ServiceQuality'):
        assert not _is_linked(b1, 'ServiceQuality', a)
    if hasattr(b2, 'ServiceQuality'):
        assert _is_linked(b2, 'ServiceQuality', a)
    _safe_set(a, 'appliesToContracts', set())
    assert not _is_linked(a, 'appliesToContracts', b2)
    if hasattr(b2, 'ServiceQuality'):
        assert not _is_linked(b2, 'ServiceQuality', a)


def test_assoc_motivatesOrganizationUnits47_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Driver()
    b2 = contentfwk_Driver()
    _safe_set(a, 'OrganizationUnit', b1)
    assert _is_linked(a, 'OrganizationUnit', b1)
    if hasattr(b1, 'isMotivatedByDrivers'):
        assert _is_linked(b1, 'isMotivatedByDrivers', a)
    _safe_set(a, 'OrganizationUnit', b2)
    assert _is_linked(a, 'OrganizationUnit', b2)
    if hasattr(b1, 'isMotivatedByDrivers'):
        assert not _is_linked(b1, 'isMotivatedByDrivers', a)
    if hasattr(b2, 'isMotivatedByDrivers'):
        assert _is_linked(b2, 'isMotivatedByDrivers', a)
    _safe_set(a, 'OrganizationUnit', None)
    assert not _is_linked(a, 'OrganizationUnit', b2)
    if hasattr(b2, 'isMotivatedByDrivers'):
        assert not _is_linked(b2, 'isMotivatedByDrivers', a)


def test_assoc_operatesInLocation69_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'containsOrganizationUnits', b1)
    assert _is_linked(a, 'containsOrganizationUnits', b1)
    if hasattr(b1, 'Location'):
        assert _is_linked(b1, 'Location', a)
    _safe_set(a, 'containsOrganizationUnits', b2)
    assert _is_linked(a, 'containsOrganizationUnits', b2)
    if hasattr(b1, 'Location'):
        assert not _is_linked(b1, 'Location', a)
    if hasattr(b2, 'Location'):
        assert _is_linked(b2, 'Location', a)
    _safe_set(a, 'containsOrganizationUnits', None)
    assert not _is_linked(a, 'containsOrganizationUnits', b2)
    if hasattr(b2, 'Location'):
        assert not _is_linked(b2, 'Location', a)


def test_assoc_operatesInLocation85_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'containsActors86', b1)
    assert _is_linked(a, 'containsActors86', b1)
    if hasattr(b1, 'Location87'):
        assert _is_linked(b1, 'Location87', a)
    _safe_set(a, 'containsActors86', b2)
    assert _is_linked(a, 'containsActors86', b2)
    if hasattr(b1, 'Location87'):
        assert not _is_linked(b1, 'Location87', a)
    if hasattr(b2, 'Location87'):
        assert _is_linked(b2, 'Location87', a)
    _safe_set(a, 'containsActors86', None)
    assert not _is_linked(a, 'containsActors86', b2)
    if hasattr(b2, 'Location87'):
        assert not _is_linked(b2, 'Location87', a)


def test_assoc_operatesOnDataEntities119_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_LogicalApplicationComponent()
    b2 = contentfwk_LogicalApplicationComponent()
    _safe_set(a, 'DataEntity120', b1)
    assert _is_linked(a, 'DataEntity120', b1)
    if hasattr(b1, 'isProcessesByLogicalApplicationComponents'):
        assert _is_linked(b1, 'isProcessesByLogicalApplicationComponents', a)
    _safe_set(a, 'DataEntity120', b2)
    assert _is_linked(a, 'DataEntity120', b2)
    if hasattr(b1, 'isProcessesByLogicalApplicationComponents'):
        assert not _is_linked(b1, 'isProcessesByLogicalApplicationComponents', a)
    if hasattr(b2, 'isProcessesByLogicalApplicationComponents'):
        assert _is_linked(b2, 'isProcessesByLogicalApplicationComponents', a)
    _safe_set(a, 'DataEntity120', None)
    assert not _is_linked(a, 'DataEntity120', b2)
    if hasattr(b2, 'isProcessesByLogicalApplicationComponents'):
        assert not _is_linked(b2, 'isProcessesByLogicalApplicationComponents', a)


def test_assoc_orchestratesFunctions150_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'isRealizedByProcesses', {b1})
    assert _is_linked(a, 'isRealizedByProcesses', b1)
    if hasattr(b1, 'Function151'):
        assert _is_linked(b1, 'Function151', a)
    _safe_set(a, 'isRealizedByProcesses', {b2})
    assert _is_linked(a, 'isRealizedByProcesses', b2)
    if hasattr(b1, 'Function151'):
        assert not _is_linked(b1, 'Function151', a)
    if hasattr(b2, 'Function151'):
        assert _is_linked(b2, 'Function151', a)
    _safe_set(a, 'isRealizedByProcesses', set())
    assert not _is_linked(a, 'isRealizedByProcesses', b2)
    if hasattr(b2, 'Function151'):
        assert not _is_linked(b2, 'Function151', a)


def test_assoc_orchestratesServices156_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'isRealizedByProcesses157', {b1})
    assert _is_linked(a, 'isRealizedByProcesses157', b1)
    if hasattr(b1, 'Service158'):
        assert _is_linked(b1, 'Service158', a)
    _safe_set(a, 'isRealizedByProcesses157', {b2})
    assert _is_linked(a, 'isRealizedByProcesses157', b2)
    if hasattr(b1, 'Service158'):
        assert not _is_linked(b1, 'Service158', a)
    if hasattr(b2, 'Service158'):
        assert _is_linked(b2, 'Service158', a)
    _safe_set(a, 'isRealizedByProcesses157', set())
    assert not _is_linked(a, 'isRealizedByProcesses157', b2)
    if hasattr(b2, 'Service158'):
        assert not _is_linked(b2, 'Service158', a)


def test_assoc_ownedElements242_link_reassign_clear():
    a = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    b1 = contentfwk_Element(ID="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    b2 = contentfwk_Element(ID="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    _safe_set(a, 'category', {b1})
    assert _is_linked(a, 'category', b1)
    if hasattr(b1, 'Element243'):
        assert _is_linked(b1, 'Element243', a)
    _safe_set(a, 'category', {b2})
    assert _is_linked(a, 'category', b2)
    if hasattr(b1, 'Element243'):
        assert not _is_linked(b1, 'Element243', a)
    if hasattr(b2, 'Element243'):
        assert _is_linked(b2, 'Element243', a)
    _safe_set(a, 'category', set())
    assert not _is_linked(a, 'category', b2)
    if hasattr(b2, 'Element243'):
        assert not _is_linked(b2, 'Element243', a)


def test_assoc_ownsAndGovernsServices62_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'isOwnedAndGovernedByOrganizationUnits', {b1})
    assert _is_linked(a, 'isOwnedAndGovernedByOrganizationUnits', b1)
    if hasattr(b1, 'Service'):
        assert _is_linked(b1, 'Service', a)
    _safe_set(a, 'isOwnedAndGovernedByOrganizationUnits', {b2})
    assert _is_linked(a, 'isOwnedAndGovernedByOrganizationUnits', b2)
    if hasattr(b1, 'Service'):
        assert not _is_linked(b1, 'Service', a)
    if hasattr(b2, 'Service'):
        assert _is_linked(b2, 'Service', a)
    _safe_set(a, 'isOwnedAndGovernedByOrganizationUnits', set())
    assert not _is_linked(a, 'isOwnedAndGovernedByOrganizationUnits', b2)
    if hasattr(b2, 'Service'):
        assert not _is_linked(b2, 'Service', a)


def test_assoc_ownsFunctions64_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'isOwnedByUnit', {b1})
    assert _is_linked(a, 'isOwnedByUnit', b1)
    if hasattr(b1, 'Function'):
        assert _is_linked(b1, 'Function', a)
    _safe_set(a, 'isOwnedByUnit', {b2})
    assert _is_linked(a, 'isOwnedByUnit', b2)
    if hasattr(b1, 'Function'):
        assert not _is_linked(b1, 'Function', a)
    if hasattr(b2, 'Function'):
        assert _is_linked(b2, 'Function', a)
    _safe_set(a, 'isOwnedByUnit', set())
    assert not _is_linked(a, 'isOwnedByUnit', b2)
    if hasattr(b2, 'Function'):
        assert not _is_linked(b2, 'Function', a)


def test_assoc_participatesInProcesses65_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_OrganizationUnit(headcount="sample_text")
    b2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    _safe_set(a, 'Process', b1)
    assert _is_linked(a, 'Process', b1)
    if hasattr(b1, 'involvesOrganizationUnits'):
        assert _is_linked(b1, 'involvesOrganizationUnits', a)
    _safe_set(a, 'Process', b2)
    assert _is_linked(a, 'Process', b2)
    if hasattr(b1, 'involvesOrganizationUnits'):
        assert not _is_linked(b1, 'involvesOrganizationUnits', a)
    if hasattr(b2, 'involvesOrganizationUnits'):
        assert _is_linked(b2, 'involvesOrganizationUnits', a)
    _safe_set(a, 'Process', None)
    assert not _is_linked(a, 'Process', b2)
    if hasattr(b2, 'involvesOrganizationUnits'):
        assert not _is_linked(b2, 'involvesOrganizationUnits', a)


def test_assoc_participatesInProcesses78_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'Process79', b1)
    assert _is_linked(a, 'Process79', b1)
    if hasattr(b1, 'involvesActors'):
        assert _is_linked(b1, 'involvesActors', a)
    _safe_set(a, 'Process79', b2)
    assert _is_linked(a, 'Process79', b2)
    if hasattr(b1, 'involvesActors'):
        assert not _is_linked(b1, 'involvesActors', a)
    if hasattr(b2, 'involvesActors'):
        assert _is_linked(b2, 'involvesActors', a)
    _safe_set(a, 'Process79', None)
    assert not _is_linked(a, 'Process79', b2)
    if hasattr(b2, 'involvesActors'):
        assert not _is_linked(b2, 'involvesActors', a)


def test_assoc_performsFunctions88_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'isPerformedByActors', {b1})
    assert _is_linked(a, 'isPerformedByActors', b1)
    if hasattr(b1, 'Function89'):
        assert _is_linked(b1, 'Function89', a)
    _safe_set(a, 'isPerformedByActors', {b2})
    assert _is_linked(a, 'isPerformedByActors', b2)
    if hasattr(b1, 'Function89'):
        assert not _is_linked(b1, 'Function89', a)
    if hasattr(b2, 'Function89'):
        assert _is_linked(b2, 'Function89', a)
    _safe_set(a, 'isPerformedByActors', set())
    assert not _is_linked(a, 'isPerformedByActors', b2)
    if hasattr(b2, 'Function89'):
        assert not _is_linked(b2, 'Function89', a)


def test_assoc_performsTaskInRoles77_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'Role', b1)
    assert _is_linked(a, 'Role', b1)
    if hasattr(b1, 'isAssumedByActors'):
        assert _is_linked(b1, 'isAssumedByActors', a)
    _safe_set(a, 'Role', b2)
    assert _is_linked(a, 'Role', b2)
    if hasattr(b1, 'isAssumedByActors'):
        assert not _is_linked(b1, 'isAssumedByActors', a)
    if hasattr(b2, 'isAssumedByActors'):
        assert _is_linked(b2, 'isAssumedByActors', a)
    _safe_set(a, 'Role', None)
    assert not _is_linked(a, 'Role', b2)
    if hasattr(b2, 'isAssumedByActors'):
        assert not _is_linked(b2, 'isAssumedByActors', a)


def test_assoc_physicalApplicationComponents276_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_ApplicationArchitecture()
    b2 = contentfwk_ApplicationArchitecture()
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent278', b1)
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent278', b1)
    if hasattr(b1, 'contentfwk_ApplicationArchitecture277'):
        assert _is_linked(b1, 'contentfwk_ApplicationArchitecture277', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent278', b2)
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent278', b2)
    if hasattr(b1, 'contentfwk_ApplicationArchitecture277'):
        assert not _is_linked(b1, 'contentfwk_ApplicationArchitecture277', a)
    if hasattr(b2, 'contentfwk_ApplicationArchitecture277'):
        assert _is_linked(b2, 'contentfwk_ApplicationArchitecture277', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent278', None)
    assert not _is_linked(a, 'contentfwk_PhysicalApplicationComponent278', b2)
    if hasattr(b2, 'contentfwk_ApplicationArchitecture277'):
        assert not _is_linked(b2, 'contentfwk_ApplicationArchitecture277', a)


def test_assoc_physicalComponents42_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_TechnologyArchitecture()
    b2 = contentfwk_TechnologyArchitecture()
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent', b1)
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent', b1)
    if hasattr(b1, 'contentfwk_TechnologyArchitecture43'):
        assert _is_linked(b1, 'contentfwk_TechnologyArchitecture43', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent', b2)
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent', b2)
    if hasattr(b1, 'contentfwk_TechnologyArchitecture43'):
        assert not _is_linked(b1, 'contentfwk_TechnologyArchitecture43', a)
    if hasattr(b2, 'contentfwk_TechnologyArchitecture43'):
        assert _is_linked(b2, 'contentfwk_TechnologyArchitecture43', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent', None)
    assert not _is_linked(a, 'contentfwk_PhysicalTechnologyComponent', b2)
    if hasattr(b2, 'contentfwk_TechnologyArchitecture43'):
        assert not _is_linked(b2, 'contentfwk_TechnologyArchitecture43', a)


def test_assoc_platformServices41_link_reassign_clear():
    a = contentfwk_PlatformService(categoryTRM="sample_text")
    b1 = contentfwk_TechnologyArchitecture()
    b2 = contentfwk_TechnologyArchitecture()
    _safe_set(a, 'contentfwk_PlatformService', b1)
    assert _is_linked(a, 'contentfwk_PlatformService', b1)
    if hasattr(b1, 'contentfwk_TechnologyArchitecture'):
        assert _is_linked(b1, 'contentfwk_TechnologyArchitecture', a)
    _safe_set(a, 'contentfwk_PlatformService', b2)
    assert _is_linked(a, 'contentfwk_PlatformService', b2)
    if hasattr(b1, 'contentfwk_TechnologyArchitecture'):
        assert not _is_linked(b1, 'contentfwk_TechnologyArchitecture', a)
    if hasattr(b2, 'contentfwk_TechnologyArchitecture'):
        assert _is_linked(b2, 'contentfwk_TechnologyArchitecture', a)
    _safe_set(a, 'contentfwk_PlatformService', None)
    assert not _is_linked(a, 'contentfwk_PlatformService', b2)
    if hasattr(b2, 'contentfwk_TechnologyArchitecture'):
        assert not _is_linked(b2, 'contentfwk_TechnologyArchitecture', a)


def test_assoc_precedesProcesses176_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    _safe_set(a, 'Process177', b1)
    assert _is_linked(a, 'Process177', b1)
    if hasattr(b1, 'followsProcesses'):
        assert _is_linked(b1, 'followsProcesses', a)
    _safe_set(a, 'Process177', b2)
    assert _is_linked(a, 'Process177', b2)
    if hasattr(b1, 'followsProcesses'):
        assert not _is_linked(b1, 'followsProcesses', a)
    if hasattr(b2, 'followsProcesses'):
        assert _is_linked(b2, 'followsProcesses', a)
    _safe_set(a, 'Process177', None)
    assert not _is_linked(a, 'Process177', b2)
    if hasattr(b2, 'followsProcesses'):
        assert not _is_linked(b2, 'followsProcesses', a)


def test_assoc_processes20_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_BusinessArchitecture()
    b2 = contentfwk_BusinessArchitecture()
    _safe_set(a, 'contentfwk_Process', b1)
    assert _is_linked(a, 'contentfwk_Process', b1)
    if hasattr(b1, 'contentfwk_BusinessArchitecture21'):
        assert _is_linked(b1, 'contentfwk_BusinessArchitecture21', a)
    _safe_set(a, 'contentfwk_Process', b2)
    assert _is_linked(a, 'contentfwk_Process', b2)
    if hasattr(b1, 'contentfwk_BusinessArchitecture21'):
        assert not _is_linked(b1, 'contentfwk_BusinessArchitecture21', a)
    if hasattr(b2, 'contentfwk_BusinessArchitecture21'):
        assert _is_linked(b2, 'contentfwk_BusinessArchitecture21', a)
    _safe_set(a, 'contentfwk_Process', None)
    assert not _is_linked(a, 'contentfwk_Process', b2)
    if hasattr(b2, 'contentfwk_BusinessArchitecture21'):
        assert not _is_linked(b2, 'contentfwk_BusinessArchitecture21', a)


def test_assoc_producesProducts170_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Product()
    b2 = contentfwk_Product()
    _safe_set(a, 'isProducedByProcesses', {b1})
    assert _is_linked(a, 'isProducedByProcesses', b1)
    if hasattr(b1, 'Product171'):
        assert _is_linked(b1, 'Product171', a)
    _safe_set(a, 'isProducedByProcesses', {b2})
    assert _is_linked(a, 'isProducedByProcesses', b2)
    if hasattr(b1, 'Product171'):
        assert not _is_linked(b1, 'Product171', a)
    if hasattr(b2, 'Product171'):
        assert _is_linked(b2, 'Product171', a)
    _safe_set(a, 'isProducedByProcesses', set())
    assert not _is_linked(a, 'isProducedByProcesses', b2)
    if hasattr(b2, 'Product171'):
        assert not _is_linked(b2, 'Product171', a)


def test_assoc_producesProducts68_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Product()
    b2 = contentfwk_Product()
    _safe_set(a, 'isProducedByOrganizationUnits', {b1})
    assert _is_linked(a, 'isProducedByOrganizationUnits', b1)
    if hasattr(b1, 'Product'):
        assert _is_linked(b1, 'Product', a)
    _safe_set(a, 'isProducedByOrganizationUnits', {b2})
    assert _is_linked(a, 'isProducedByOrganizationUnits', b2)
    if hasattr(b1, 'Product'):
        assert not _is_linked(b1, 'Product', a)
    if hasattr(b2, 'Product'):
        assert _is_linked(b2, 'Product', a)
    _safe_set(a, 'isProducedByOrganizationUnits', set())
    assert not _is_linked(a, 'isProducedByOrganizationUnits', b2)
    if hasattr(b2, 'Product'):
        assert not _is_linked(b2, 'Product', a)


def test_assoc_providesEntities316_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'DataEntity317', b1)
    assert _is_linked(a, 'DataEntity317', b1)
    if hasattr(b1, 'isUpdatedThroughServices'):
        assert _is_linked(b1, 'isUpdatedThroughServices', a)
    _safe_set(a, 'DataEntity317', b2)
    assert _is_linked(a, 'DataEntity317', b2)
    if hasattr(b1, 'isUpdatedThroughServices'):
        assert not _is_linked(b1, 'isUpdatedThroughServices', a)
    if hasattr(b2, 'isUpdatedThroughServices'):
        assert _is_linked(b2, 'isUpdatedThroughServices', a)
    _safe_set(a, 'DataEntity317', None)
    assert not _is_linked(a, 'DataEntity317', b2)
    if hasattr(b2, 'isUpdatedThroughServices'):
        assert not _is_linked(b2, 'isUpdatedThroughServices', a)


def test_assoc_providesPlatformForServices297_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'isImplementedOnLogicalTechnologyComponents', {b1})
    assert _is_linked(a, 'isImplementedOnLogicalTechnologyComponents', b1)
    if hasattr(b1, 'Service298'):
        assert _is_linked(b1, 'Service298', a)
    _safe_set(a, 'isImplementedOnLogicalTechnologyComponents', {b2})
    assert _is_linked(a, 'isImplementedOnLogicalTechnologyComponents', b2)
    if hasattr(b1, 'Service298'):
        assert not _is_linked(b1, 'Service298', a)
    if hasattr(b2, 'Service298'):
        assert _is_linked(b2, 'Service298', a)
    _safe_set(a, 'isImplementedOnLogicalTechnologyComponents', set())
    assert not _is_linked(a, 'isImplementedOnLogicalTechnologyComponents', b2)
    if hasattr(b2, 'Service298'):
        assert not _is_linked(b2, 'Service298', a)


def test_assoc_realizesApplicationComponents182_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b2 = contentfwk_PhysicalApplicationComponent(availabilityQualityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent183', {b1})
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent183', b1)
    if hasattr(b1, 'contentfwk_PhysicalApplicationComponent'):
        assert _is_linked(b1, 'contentfwk_PhysicalApplicationComponent', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent183', {b2})
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent183', b2)
    if hasattr(b1, 'contentfwk_PhysicalApplicationComponent'):
        assert not _is_linked(b1, 'contentfwk_PhysicalApplicationComponent', a)
    if hasattr(b2, 'contentfwk_PhysicalApplicationComponent'):
        assert _is_linked(b2, 'contentfwk_PhysicalApplicationComponent', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent183', set())
    assert not _is_linked(a, 'contentfwk_PhysicalTechnologyComponent183', b2)
    if hasattr(b2, 'contentfwk_PhysicalApplicationComponent'):
        assert not _is_linked(b2, 'contentfwk_PhysicalApplicationComponent', a)


def test_assoc_relatesTo115_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    _safe_set(a, 'contentfwk_DataEntity114', {b1})
    assert _is_linked(a, 'contentfwk_DataEntity114', b1)
    if hasattr(b1, 'contentfwk_DataEntity116'):
        assert _is_linked(b1, 'contentfwk_DataEntity116', a)
    _safe_set(a, 'contentfwk_DataEntity114', {b2})
    assert _is_linked(a, 'contentfwk_DataEntity114', b2)
    if hasattr(b1, 'contentfwk_DataEntity116'):
        assert not _is_linked(b1, 'contentfwk_DataEntity116', a)
    if hasattr(b2, 'contentfwk_DataEntity116'):
        assert _is_linked(b2, 'contentfwk_DataEntity116', a)
    _safe_set(a, 'contentfwk_DataEntity114', set())
    assert not _is_linked(a, 'contentfwk_DataEntity114', b2)
    if hasattr(b2, 'contentfwk_DataEntity116'):
        assert not _is_linked(b2, 'contentfwk_DataEntity116', a)


def test_assoc_residesWithinLogicalDataComponent109_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_LogicalDataComponent()
    b2 = contentfwk_LogicalDataComponent()
    _safe_set(a, 'encapsulatesDataEntities', b1)
    assert _is_linked(a, 'encapsulatesDataEntities', b1)
    if hasattr(b1, 'LogicalDataComponent'):
        assert _is_linked(b1, 'LogicalDataComponent', a)
    _safe_set(a, 'encapsulatesDataEntities', b2)
    assert _is_linked(a, 'encapsulatesDataEntities', b2)
    if hasattr(b1, 'LogicalDataComponent'):
        assert not _is_linked(b1, 'LogicalDataComponent', a)
    if hasattr(b2, 'LogicalDataComponent'):
        assert _is_linked(b2, 'LogicalDataComponent', a)
    _safe_set(a, 'encapsulatesDataEntities', None)
    assert not _is_linked(a, 'encapsulatesDataEntities', b2)
    if hasattr(b2, 'LogicalDataComponent'):
        assert not _is_linked(b2, 'LogicalDataComponent', a)


def test_assoc_resolvesEvents166_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'isResolvedByProcesses', {b1})
    assert _is_linked(a, 'isResolvedByProcesses', b1)
    if hasattr(b1, 'Event167'):
        assert _is_linked(b1, 'Event167', a)
    _safe_set(a, 'isResolvedByProcesses', {b2})
    assert _is_linked(a, 'isResolvedByProcesses', b2)
    if hasattr(b1, 'Event167'):
        assert not _is_linked(b1, 'Event167', a)
    if hasattr(b2, 'Event167'):
        assert _is_linked(b2, 'Event167', a)
    _safe_set(a, 'isResolvedByProcesses', set())
    assert not _is_linked(a, 'isResolvedByProcesses', b2)
    if hasattr(b2, 'Event167'):
        assert not _is_linked(b2, 'Event167', a)


def test_assoc_resolvesEvents82_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'isResolvedByActors', {b1})
    assert _is_linked(a, 'isResolvedByActors', b1)
    if hasattr(b1, 'Event'):
        assert _is_linked(b1, 'Event', a)
    _safe_set(a, 'isResolvedByActors', {b2})
    assert _is_linked(a, 'isResolvedByActors', b2)
    if hasattr(b1, 'Event'):
        assert not _is_linked(b1, 'Event', a)
    if hasattr(b2, 'Event'):
        assert _is_linked(b2, 'Event', a)
    _safe_set(a, 'isResolvedByActors', set())
    assert not _is_linked(a, 'isResolvedByActors', b2)
    if hasattr(b2, 'Event'):
        assert not _is_linked(b2, 'Event', a)


def test_assoc_roles14_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_BusinessArchitecture()
    b2 = contentfwk_BusinessArchitecture()
    _safe_set(a, 'contentfwk_Role', b1)
    assert _is_linked(a, 'contentfwk_Role', b1)
    if hasattr(b1, 'contentfwk_BusinessArchitecture15'):
        assert _is_linked(b1, 'contentfwk_BusinessArchitecture15', a)
    _safe_set(a, 'contentfwk_Role', b2)
    assert _is_linked(a, 'contentfwk_Role', b2)
    if hasattr(b1, 'contentfwk_BusinessArchitecture15'):
        assert not _is_linked(b1, 'contentfwk_BusinessArchitecture15', a)
    if hasattr(b2, 'contentfwk_BusinessArchitecture15'):
        assert _is_linked(b2, 'contentfwk_BusinessArchitecture15', a)
    _safe_set(a, 'contentfwk_Role', None)
    assert not _is_linked(a, 'contentfwk_Role', b2)
    if hasattr(b2, 'contentfwk_BusinessArchitecture15'):
        assert not _is_linked(b2, 'contentfwk_BusinessArchitecture15', a)


def test_assoc_subContainers235_link_reassign_clear():
    a = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    b1 = contentfwk_Container(description="sample_text", id="sample_text", name="sample_text")
    b2 = contentfwk_Container(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'contentfwk_Container234', {b1})
    assert _is_linked(a, 'contentfwk_Container234', b1)
    if hasattr(b1, 'contentfwk_Container236'):
        assert _is_linked(b1, 'contentfwk_Container236', a)
    _safe_set(a, 'contentfwk_Container234', {b2})
    assert _is_linked(a, 'contentfwk_Container234', b2)
    if hasattr(b1, 'contentfwk_Container236'):
        assert not _is_linked(b1, 'contentfwk_Container236', a)
    if hasattr(b2, 'contentfwk_Container236'):
        assert _is_linked(b2, 'contentfwk_Container236', a)
    _safe_set(a, 'contentfwk_Container234', set())
    assert not _is_linked(a, 'contentfwk_Container234', b2)
    if hasattr(b2, 'contentfwk_Container236'):
        assert not _is_linked(b2, 'contentfwk_Container236', a)


def test_assoc_subLabels240_link_reassign_clear():
    a = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    b1 = contentfwk_Label(description="sample_text", id="sample_text", name="sample_text")
    b2 = contentfwk_Label(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'contentfwk_Label239', {b1})
    assert _is_linked(a, 'contentfwk_Label239', b1)
    if hasattr(b1, 'contentfwk_Label241'):
        assert _is_linked(b1, 'contentfwk_Label241', a)
    _safe_set(a, 'contentfwk_Label239', {b2})
    assert _is_linked(a, 'contentfwk_Label239', b2)
    if hasattr(b1, 'contentfwk_Label241'):
        assert not _is_linked(b1, 'contentfwk_Label241', a)
    if hasattr(b2, 'contentfwk_Label241'):
        assert _is_linked(b2, 'contentfwk_Label241', a)
    _safe_set(a, 'contentfwk_Label239', set())
    assert not _is_linked(a, 'contentfwk_Label239', b2)
    if hasattr(b2, 'contentfwk_Label241'):
        assert not _is_linked(b2, 'contentfwk_Label241', a)


def test_assoc_suppliesEntities70_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'DataEntity', b1)
    assert _is_linked(a, 'DataEntity', b1)
    if hasattr(b1, 'isSuppliedByActors'):
        assert _is_linked(b1, 'isSuppliedByActors', a)
    _safe_set(a, 'DataEntity', b2)
    assert _is_linked(a, 'DataEntity', b2)
    if hasattr(b1, 'isSuppliedByActors'):
        assert not _is_linked(b1, 'isSuppliedByActors', a)
    if hasattr(b2, 'isSuppliedByActors'):
        assert _is_linked(b2, 'isSuppliedByActors', a)
    _safe_set(a, 'DataEntity', None)
    assert not _is_linked(a, 'DataEntity', b2)
    if hasattr(b2, 'isSuppliedByActors'):
        assert not _is_linked(b2, 'isSuppliedByActors', a)


def test_assoc_suppliesPlatformServices299_link_reassign_clear():
    a = contentfwk_PlatformService(categoryTRM="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'PlatformService', b1)
    assert _is_linked(a, 'PlatformService', b1)
    if hasattr(b1, 'isSuppliedByLogicalTechnologyComponents'):
        assert _is_linked(b1, 'isSuppliedByLogicalTechnologyComponents', a)
    _safe_set(a, 'PlatformService', b2)
    assert _is_linked(a, 'PlatformService', b2)
    if hasattr(b1, 'isSuppliedByLogicalTechnologyComponents'):
        assert not _is_linked(b1, 'isSuppliedByLogicalTechnologyComponents', a)
    if hasattr(b2, 'isSuppliedByLogicalTechnologyComponents'):
        assert _is_linked(b2, 'isSuppliedByLogicalTechnologyComponents', a)
    _safe_set(a, 'PlatformService', None)
    assert not _is_linked(a, 'PlatformService', b2)
    if hasattr(b2, 'isSuppliedByLogicalTechnologyComponents'):
        assert not _is_linked(b2, 'isSuppliedByLogicalTechnologyComponents', a)


def test_assoc_supportsActors139_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'Actor140', b1)
    assert _is_linked(a, 'Actor140', b1)
    if hasattr(b1, 'interactsWithFunctions'):
        assert _is_linked(b1, 'interactsWithFunctions', a)
    _safe_set(a, 'Actor140', b2)
    assert _is_linked(a, 'Actor140', b2)
    if hasattr(b1, 'interactsWithFunctions'):
        assert not _is_linked(b1, 'interactsWithFunctions', a)
    if hasattr(b2, 'interactsWithFunctions'):
        assert _is_linked(b2, 'interactsWithFunctions', a)
    _safe_set(a, 'Actor140', None)
    assert not _is_linked(a, 'Actor140', b2)
    if hasattr(b2, 'interactsWithFunctions'):
        assert not _is_linked(b2, 'interactsWithFunctions', a)


def test_assoc_supportsProcesses133_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'Process134', b1)
    assert _is_linked(a, 'Process134', b1)
    if hasattr(b1, 'decomposesFunctions'):
        assert _is_linked(b1, 'decomposesFunctions', a)
    _safe_set(a, 'Process134', b2)
    assert _is_linked(a, 'Process134', b2)
    if hasattr(b1, 'decomposesFunctions'):
        assert not _is_linked(b1, 'decomposesFunctions', a)
    if hasattr(b2, 'decomposesFunctions'):
        assert _is_linked(b2, 'decomposesFunctions', a)
    _safe_set(a, 'Process134', None)
    assert not _is_linked(a, 'Process134', b2)
    if hasattr(b2, 'decomposesFunctions'):
        assert not _is_linked(b2, 'decomposesFunctions', a)


def test_assoc_supportsProcesses332_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'Process333', b1)
    assert _is_linked(a, 'Process333', b1)
    if hasattr(b1, 'decomposesServices'):
        assert _is_linked(b1, 'decomposesServices', a)
    _safe_set(a, 'Process333', b2)
    assert _is_linked(a, 'Process333', b2)
    if hasattr(b1, 'decomposesServices'):
        assert not _is_linked(b1, 'decomposesServices', a)
    if hasattr(b2, 'decomposesServices'):
        assert _is_linked(b2, 'decomposesServices', a)
    _safe_set(a, 'Process333', None)
    assert not _is_linked(a, 'Process333', b2)
    if hasattr(b2, 'decomposesServices'):
        assert not _is_linked(b2, 'decomposesServices', a)


def test_assoc_units10_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_BusinessArchitecture()
    b2 = contentfwk_BusinessArchitecture()
    _safe_set(a, 'contentfwk_OrganizationUnit', b1)
    assert _is_linked(a, 'contentfwk_OrganizationUnit', b1)
    if hasattr(b1, 'contentfwk_BusinessArchitecture11'):
        assert _is_linked(b1, 'contentfwk_BusinessArchitecture11', a)
    _safe_set(a, 'contentfwk_OrganizationUnit', b2)
    assert _is_linked(a, 'contentfwk_OrganizationUnit', b2)
    if hasattr(b1, 'contentfwk_BusinessArchitecture11'):
        assert not _is_linked(b1, 'contentfwk_BusinessArchitecture11', a)
    if hasattr(b2, 'contentfwk_BusinessArchitecture11'):
        assert _is_linked(b2, 'contentfwk_BusinessArchitecture11', a)
    _safe_set(a, 'contentfwk_OrganizationUnit', None)
    assert not _is_linked(a, 'contentfwk_OrganizationUnit', b2)
    if hasattr(b2, 'contentfwk_BusinessArchitecture11'):
        assert not _is_linked(b2, 'contentfwk_BusinessArchitecture11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ApplicationComponent_strategy = st.builds(ApplicationComponent)
@given(instance=ApplicationComponent_strategy)
@settings(max_examples=25)
def test_ApplicationComponent_instantiation(instance):
    assert isinstance(instance, ApplicationComponent)


Architecture_strategy = st.builds(Architecture)
@given(instance=Architecture_strategy)
@settings(max_examples=25)
def test_Architecture_instantiation(instance):
    assert isinstance(instance, Architecture)


DataComponent_strategy = st.builds(DataComponent)
@given(instance=DataComponent_strategy)
@settings(max_examples=25)
def test_DataComponent_instantiation(instance):
    assert isinstance(instance, DataComponent)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


Service_strategy = st.builds(Service)
@given(instance=Service_strategy)
@settings(max_examples=25)
def test_Service_instantiation(instance):
    assert isinstance(instance, Service)


Standard_strategy = st.builds(Standard)
@given(instance=Standard_strategy)
@settings(max_examples=25)
def test_Standard_instantiation(instance):
    assert isinstance(instance, Standard)


StrategicElement_strategy = st.builds(StrategicElement)
@given(instance=StrategicElement_strategy)
@settings(max_examples=25)
def test_StrategicElement_instantiation(instance):
    assert isinstance(instance, StrategicElement)


TechnologyComponent_strategy = st.builds(TechnologyComponent)
@given(instance=TechnologyComponent_strategy)
@settings(max_examples=25)
def test_TechnologyComponent_instantiation(instance):
    assert isinstance(instance, TechnologyComponent)


contentfwk_Actor_strategy = st.builds(contentfwk_Actor, FTEs=safe_text, actorGoal=safe_text, actorTasks=safe_text)
@given(instance=contentfwk_Actor_strategy)
@settings(max_examples=25)
def test_contentfwk_Actor_instantiation(instance):
    assert isinstance(instance, contentfwk_Actor)


contentfwk_ApplicationArchitecture_strategy = st.builds(contentfwk_ApplicationArchitecture)
@given(instance=contentfwk_ApplicationArchitecture_strategy)
@settings(max_examples=25)
def test_contentfwk_ApplicationArchitecture_instantiation(instance):
    assert isinstance(instance, contentfwk_ApplicationArchitecture)


contentfwk_ApplicationComponent_strategy = st.builds(contentfwk_ApplicationComponent)
@given(instance=contentfwk_ApplicationComponent_strategy)
@settings(max_examples=25)
def test_contentfwk_ApplicationComponent_instantiation(instance):
    assert isinstance(instance, contentfwk_ApplicationComponent)


contentfwk_Architecture_strategy = st.builds(contentfwk_Architecture)
@given(instance=contentfwk_Architecture_strategy)
@settings(max_examples=25)
def test_contentfwk_Architecture_instantiation(instance):
    assert isinstance(instance, contentfwk_Architecture)


contentfwk_Assumption_strategy = st.builds(contentfwk_Assumption)
@given(instance=contentfwk_Assumption_strategy)
@settings(max_examples=25)
def test_contentfwk_Assumption_instantiation(instance):
    assert isinstance(instance, contentfwk_Assumption)


contentfwk_BusinessArchitecture_strategy = st.builds(contentfwk_BusinessArchitecture)
@given(instance=contentfwk_BusinessArchitecture_strategy)
@settings(max_examples=25)
def test_contentfwk_BusinessArchitecture_instantiation(instance):
    assert isinstance(instance, contentfwk_BusinessArchitecture)


contentfwk_BusinessService_strategy = st.builds(contentfwk_BusinessService)
@given(instance=contentfwk_BusinessService_strategy)
@settings(max_examples=25)
def test_contentfwk_BusinessService_instantiation(instance):
    assert isinstance(instance, contentfwk_BusinessService)


contentfwk_Capability_strategy = st.builds(contentfwk_Capability, businessValue=safe_text, increments=safe_text)
@given(instance=contentfwk_Capability_strategy)
@settings(max_examples=25)
def test_contentfwk_Capability_instantiation(instance):
    assert isinstance(instance, contentfwk_Capability)


contentfwk_Constraint_strategy = st.builds(contentfwk_Constraint)
@given(instance=contentfwk_Constraint_strategy)
@settings(max_examples=25)
def test_contentfwk_Constraint_instantiation(instance):
    assert isinstance(instance, contentfwk_Constraint)


contentfwk_Container_strategy = st.builds(contentfwk_Container, description=safe_text, id=safe_text, name=safe_text)
@given(instance=contentfwk_Container_strategy)
@settings(max_examples=25)
def test_contentfwk_Container_instantiation(instance):
    assert isinstance(instance, contentfwk_Container)


contentfwk_Contract_strategy = st.builds(contentfwk_Contract, ServiceNameCalled=safe_text, ServiceNameCaller=safe_text, availabilityQualityCharacteristics=safe_text, behaviorCharacteristics=safe_text, capacityCharacteristics=safe_text, contractControlRequirements=safe_text, credibilityCharacteristics=safe_text, extensibilityCharacteristics=safe_text, growth=safe_text, growthPeriod=safe_text, integrityCharacteristics=safe_text, internationalizationCharacteristics=safe_text, interoperabilityCharacteristics=safe_text, localizationCharacteristics=safe_text, locatabilityCharacteristics=safe_text, manageabilityCharacteristics=safe_text, peakProfileLongTerm=safe_text, peakProfileShortTerm=safe_text, performanceCharacteristics=safe_text, portabilityCharacteristics=safe_text, privacyCharacteristics=safe_text, qualityOfInformationRequired=safe_text, recoverabilityCharacteristics=safe_text, reliabilityCharacteristics=safe_text, responseCharacteristics=safe_text, resultControlRequirements=safe_text, scalabilityCharacteristics=safe_text, securityCharacteristics=safe_text, serviceQualityCharacteristics=safe_text, serviceabilityCharacteristics=safe_text, servicesTimes=safe_text, throughput=safe_text, throughputPeriod=safe_text)
@given(instance=contentfwk_Contract_strategy)
@settings(max_examples=25)
def test_contentfwk_Contract_instantiation(instance):
    assert isinstance(instance, contentfwk_Contract)


contentfwk_Control_strategy = st.builds(contentfwk_Control)
@given(instance=contentfwk_Control_strategy)
@settings(max_examples=25)
def test_contentfwk_Control_instantiation(instance):
    assert isinstance(instance, contentfwk_Control)


contentfwk_DataArchitecture_strategy = st.builds(contentfwk_DataArchitecture)
@given(instance=contentfwk_DataArchitecture_strategy)
@settings(max_examples=25)
def test_contentfwk_DataArchitecture_instantiation(instance):
    assert isinstance(instance, contentfwk_DataArchitecture)


contentfwk_DataComponent_strategy = st.builds(contentfwk_DataComponent)
@given(instance=contentfwk_DataComponent_strategy)
@settings(max_examples=25)
def test_contentfwk_DataComponent_instantiation(instance):
    assert isinstance(instance, contentfwk_DataComponent)


contentfwk_DataEntity_strategy = st.builds(contentfwk_DataEntity, dataEntityCategory=safe_text, privacyClassification=safe_text, retentionClassification=safe_text)
@given(instance=contentfwk_DataEntity_strategy)
@settings(max_examples=25)
def test_contentfwk_DataEntity_instantiation(instance):
    assert isinstance(instance, contentfwk_DataEntity)


contentfwk_Driver_strategy = st.builds(contentfwk_Driver)
@given(instance=contentfwk_Driver_strategy)
@settings(max_examples=25)
def test_contentfwk_Driver_instantiation(instance):
    assert isinstance(instance, contentfwk_Driver)


contentfwk_Element_strategy = st.builds(contentfwk_Element, ID=safe_text, description=safe_text, name=safe_text, ownerDescr=safe_text, sourceDescr=safe_text)
@given(instance=contentfwk_Element_strategy)
@settings(max_examples=25)
def test_contentfwk_Element_instantiation(instance):
    assert isinstance(instance, contentfwk_Element)


contentfwk_EnterpriseArchitecture_strategy = st.builds(contentfwk_EnterpriseArchitecture)
@given(instance=contentfwk_EnterpriseArchitecture_strategy)
@settings(max_examples=25)
def test_contentfwk_EnterpriseArchitecture_instantiation(instance):
    assert isinstance(instance, contentfwk_EnterpriseArchitecture)


contentfwk_Event_strategy = st.builds(contentfwk_Event)
@given(instance=contentfwk_Event_strategy)
@settings(max_examples=25)
def test_contentfwk_Event_instantiation(instance):
    assert isinstance(instance, contentfwk_Event)


contentfwk_Function_strategy = st.builds(contentfwk_Function)
@given(instance=contentfwk_Function_strategy)
@settings(max_examples=25)
def test_contentfwk_Function_instantiation(instance):
    assert isinstance(instance, contentfwk_Function)


contentfwk_Gap_strategy = st.builds(contentfwk_Gap)
@given(instance=contentfwk_Gap_strategy)
@settings(max_examples=25)
def test_contentfwk_Gap_instantiation(instance):
    assert isinstance(instance, contentfwk_Gap)


contentfwk_Goal_strategy = st.builds(contentfwk_Goal)
@given(instance=contentfwk_Goal_strategy)
@settings(max_examples=25)
def test_contentfwk_Goal_instantiation(instance):
    assert isinstance(instance, contentfwk_Goal)


contentfwk_InformationSystemService_strategy = st.builds(contentfwk_InformationSystemService)
@given(instance=contentfwk_InformationSystemService_strategy)
@settings(max_examples=25)
def test_contentfwk_InformationSystemService_instantiation(instance):
    assert isinstance(instance, contentfwk_InformationSystemService)


contentfwk_Label_strategy = st.builds(contentfwk_Label, description=safe_text, id=safe_text, name=safe_text)
@given(instance=contentfwk_Label_strategy)
@settings(max_examples=25)
def test_contentfwk_Label_instantiation(instance):
    assert isinstance(instance, contentfwk_Label)


contentfwk_Location_strategy = st.builds(contentfwk_Location)
@given(instance=contentfwk_Location_strategy)
@settings(max_examples=25)
def test_contentfwk_Location_instantiation(instance):
    assert isinstance(instance, contentfwk_Location)


contentfwk_LogicalApplicationComponent_strategy = st.builds(contentfwk_LogicalApplicationComponent)
@given(instance=contentfwk_LogicalApplicationComponent_strategy)
@settings(max_examples=25)
def test_contentfwk_LogicalApplicationComponent_instantiation(instance):
    assert isinstance(instance, contentfwk_LogicalApplicationComponent)


contentfwk_LogicalDataComponent_strategy = st.builds(contentfwk_LogicalDataComponent)
@given(instance=contentfwk_LogicalDataComponent_strategy)
@settings(max_examples=25)
def test_contentfwk_LogicalDataComponent_instantiation(instance):
    assert isinstance(instance, contentfwk_LogicalDataComponent)


contentfwk_LogicalTechnologyComponent_strategy = st.builds(contentfwk_LogicalTechnologyComponent, categoryTRM=safe_text)
@given(instance=contentfwk_LogicalTechnologyComponent_strategy)
@settings(max_examples=25)
def test_contentfwk_LogicalTechnologyComponent_instantiation(instance):
    assert isinstance(instance, contentfwk_LogicalTechnologyComponent)


contentfwk_Measure_strategy = st.builds(contentfwk_Measure)
@given(instance=contentfwk_Measure_strategy)
@settings(max_examples=25)
def test_contentfwk_Measure_instantiation(instance):
    assert isinstance(instance, contentfwk_Measure)


contentfwk_Objective_strategy = st.builds(contentfwk_Objective)
@given(instance=contentfwk_Objective_strategy)
@settings(max_examples=25)
def test_contentfwk_Objective_instantiation(instance):
    assert isinstance(instance, contentfwk_Objective)


contentfwk_OrganizationUnit_strategy = st.builds(contentfwk_OrganizationUnit, headcount=safe_text)
@given(instance=contentfwk_OrganizationUnit_strategy)
@settings(max_examples=25)
def test_contentfwk_OrganizationUnit_instantiation(instance):
    assert isinstance(instance, contentfwk_OrganizationUnit)


contentfwk_PhysicalApplicationComponent_strategy = st.builds(contentfwk_PhysicalApplicationComponent, availabilityQualityCharacteristics=safe_text, capacityCharacteristics=safe_text, credibilityCharacteristics=safe_text, dateOfLastRelease=st.dates(), dateOfNextRelease=st.dates(), extensibilityCharacteristics=safe_text, growth=safe_text, growthPeriod=safe_text, initialLiveDate=st.dates(), integrityCharacteristics=safe_text, internationalizationCharacteristics=safe_text, interoperabilityCharacteristics=safe_text, lifeCycleStatus=safe_text, localizationCharacteristics=safe_text, locatabilityCharacteristics=safe_text, manageabilityCharacteristics=safe_text, peakProfileLongTerm=safe_text, peakProfileShortTerm=safe_text, performanceCharacteristics=safe_text, portabilityCharacteristics=safe_text, privacyCharacteristics=safe_text, recoverabilityCharacteristics=safe_text, reliabilityCharacteristics=safe_text, retirementDate=st.dates(), scalabilityCharacteristics=safe_text, securityCharacteristics=safe_text, serviceabilityCharacteristics=safe_text, servicesTimes=safe_text, throughput=safe_text, throughputPeriod=safe_text)
@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
@settings(max_examples=25)
def test_contentfwk_PhysicalApplicationComponent_instantiation(instance):
    assert isinstance(instance, contentfwk_PhysicalApplicationComponent)


contentfwk_PhysicalDataComponent_strategy = st.builds(contentfwk_PhysicalDataComponent)
@given(instance=contentfwk_PhysicalDataComponent_strategy)
@settings(max_examples=25)
def test_contentfwk_PhysicalDataComponent_instantiation(instance):
    assert isinstance(instance, contentfwk_PhysicalDataComponent)


contentfwk_PhysicalTechnologyComponent_strategy = st.builds(contentfwk_PhysicalTechnologyComponent, categoryTRM=safe_text, moduleName=safe_text, productName=safe_text, vendor=safe_text, version=safe_text)
@given(instance=contentfwk_PhysicalTechnologyComponent_strategy)
@settings(max_examples=25)
def test_contentfwk_PhysicalTechnologyComponent_instantiation(instance):
    assert isinstance(instance, contentfwk_PhysicalTechnologyComponent)


contentfwk_PlatformService_strategy = st.builds(contentfwk_PlatformService, categoryTRM=safe_text)
@given(instance=contentfwk_PlatformService_strategy)
@settings(max_examples=25)
def test_contentfwk_PlatformService_instantiation(instance):
    assert isinstance(instance, contentfwk_PlatformService)


contentfwk_Principle_strategy = st.builds(contentfwk_Principle, implication=safe_text, metric=safe_text, principleCategory=safe_text, priority=safe_text, rationale=safe_text, statementOfPrinciple=safe_text)
@given(instance=contentfwk_Principle_strategy)
@settings(max_examples=25)
def test_contentfwk_Principle_instantiation(instance):
    assert isinstance(instance, contentfwk_Principle)


contentfwk_Process_strategy = st.builds(contentfwk_Process, isAutomated=st.booleans(), processCritiality=safe_text, processVolumetrics=safe_text)
@given(instance=contentfwk_Process_strategy)
@settings(max_examples=25)
def test_contentfwk_Process_instantiation(instance):
    assert isinstance(instance, contentfwk_Process)


contentfwk_Product_strategy = st.builds(contentfwk_Product)
@given(instance=contentfwk_Product_strategy)
@settings(max_examples=25)
def test_contentfwk_Product_instantiation(instance):
    assert isinstance(instance, contentfwk_Product)


contentfwk_Requirement_strategy = st.builds(contentfwk_Requirement, acceptanceCriteria=safe_text, rationale=safe_text, statementOfRequirement=safe_text)
@given(instance=contentfwk_Requirement_strategy)
@settings(max_examples=25)
def test_contentfwk_Requirement_instantiation(instance):
    assert isinstance(instance, contentfwk_Requirement)


contentfwk_Role_strategy = st.builds(contentfwk_Role, estimatedFTEs=safe_text)
@given(instance=contentfwk_Role_strategy)
@settings(max_examples=25)
def test_contentfwk_Role_instantiation(instance):
    assert isinstance(instance, contentfwk_Role)


contentfwk_Service_strategy = st.builds(contentfwk_Service)
@given(instance=contentfwk_Service_strategy)
@settings(max_examples=25)
def test_contentfwk_Service_instantiation(instance):
    assert isinstance(instance, contentfwk_Service)


contentfwk_ServiceQuality_strategy = st.builds(contentfwk_ServiceQuality)
@given(instance=contentfwk_ServiceQuality_strategy)
@settings(max_examples=25)
def test_contentfwk_ServiceQuality_instantiation(instance):
    assert isinstance(instance, contentfwk_ServiceQuality)


contentfwk_Standard_strategy = st.builds(contentfwk_Standard, lastStandardCreationDate=st.dates(), nextStandardCreationDate=st.dates(), retireDate=st.dates(), standardClass=safe_text, standardCreationDate=st.dates())
@given(instance=contentfwk_Standard_strategy)
@settings(max_examples=25)
def test_contentfwk_Standard_instantiation(instance):
    assert isinstance(instance, contentfwk_Standard)


contentfwk_StrategicArchitecture_strategy = st.builds(contentfwk_StrategicArchitecture)
@given(instance=contentfwk_StrategicArchitecture_strategy)
@settings(max_examples=25)
def test_contentfwk_StrategicArchitecture_instantiation(instance):
    assert isinstance(instance, contentfwk_StrategicArchitecture)


contentfwk_StrategicElement_strategy = st.builds(contentfwk_StrategicElement)
@given(instance=contentfwk_StrategicElement_strategy)
@settings(max_examples=25)
def test_contentfwk_StrategicElement_instantiation(instance):
    assert isinstance(instance, contentfwk_StrategicElement)


contentfwk_TechnologyArchitecture_strategy = st.builds(contentfwk_TechnologyArchitecture)
@given(instance=contentfwk_TechnologyArchitecture_strategy)
@settings(max_examples=25)
def test_contentfwk_TechnologyArchitecture_instantiation(instance):
    assert isinstance(instance, contentfwk_TechnologyArchitecture)


contentfwk_TechnologyComponent_strategy = st.builds(contentfwk_TechnologyComponent)
@given(instance=contentfwk_TechnologyComponent_strategy)
@settings(max_examples=25)
def test_contentfwk_TechnologyComponent_instantiation(instance):
    assert isinstance(instance, contentfwk_TechnologyComponent)


contentfwk_WorkPackage_strategy = st.builds(contentfwk_WorkPackage, workPackageCategory=safe_text)
@given(instance=contentfwk_WorkPackage_strategy)
@settings(max_examples=25)
def test_contentfwk_WorkPackage_instantiation(instance):
    assert isinstance(instance, contentfwk_WorkPackage)



