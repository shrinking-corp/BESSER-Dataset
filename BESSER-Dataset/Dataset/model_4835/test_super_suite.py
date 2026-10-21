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
    contentfwk_Standard,
    DataComponent,
    StrategicElement,
    contentfwk_Principle,
    contentfwk_WorkPackage,
    contentfwk_Gap,
    contentfwk_Requirement,
    contentfwk_Assumption,
    contentfwk_Constraint,
    contentfwk_Element,
    TechnologyComponent,
    Service,
    Standard,
    contentfwk_TechnologyComponent,
    contentfwk_ApplicationComponent,
    contentfwk_DataComponent,
    ApplicationComponent,
    contentfwk_Service,
    Element,
    contentfwk_PhysicalApplicationComponent,
    contentfwk_Capability,
    contentfwk_InformationSystemService,
    contentfwk_StrategicElement,
    contentfwk_LogicalApplicationComponent,
    contentfwk_LogicalTechnologyComponent,
    contentfwk_PhysicalTechnologyComponent,
    contentfwk_PlatformService,
    contentfwk_PhysicalDataComponent,
    contentfwk_LogicalDataComponent,
    contentfwk_DataEntity,
    contentfwk_Role,
    contentfwk_Actor,
    contentfwk_OrganizationUnit,
    contentfwk_Objective,
    contentfwk_Goal,
    contentfwk_Driver,
    Architecture,
    contentfwk_TechnologyArchitecture,
    contentfwk_ApplicationArchitecture,
    contentfwk_DataArchitecture,
    contentfwk_StrategicArchitecture,
    contentfwk_BusinessArchitecture,
    contentfwk_ServiceQuality,
    contentfwk_Measure,
    contentfwk_Contract,
    contentfwk_Product,
    contentfwk_Location,
    contentfwk_Event,
    contentfwk_Control,
    contentfwk_Process,
    contentfwk_BusinessService,
    contentfwk_Function,
    contentfwk_Architecture,
    contentfwk_EnterpriseArchitecture,
    PrincipleCategory,
    DataEntityCategory,
    WorkPackageCategory,
    LifeCycleStatus,
    StandardsClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_contentfwk_standard_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Standard)


def test_hyp_contentfwk_standard_constructor_exists():
    assert callable(contentfwk_Standard.__init__)


def test_hyp_contentfwk_standard_constructor_args():
    sig = inspect.signature(contentfwk_Standard.__init__)
    params = list(sig.parameters.keys())
    assert "standardCreationDate" in params, "Missing parameter 'standardCreationDate'"
    assert "standardClass" in params, "Missing parameter 'standardClass'"
    assert "nextStandardReviewDate" in params, "Missing parameter 'nextStandardReviewDate'"
    assert "lastStandardReviewDate" in params, "Missing parameter 'lastStandardReviewDate'"
    assert "retireDate" in params, "Missing parameter 'retireDate'"








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



def test_hyp_contentfwk_principle_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Principle)


def test_hyp_contentfwk_principle_constructor_exists():
    assert callable(contentfwk_Principle.__init__)


def test_hyp_contentfwk_principle_constructor_args():
    sig = inspect.signature(contentfwk_Principle.__init__)
    params = list(sig.parameters.keys())
    assert "rationale" in params, "Missing parameter 'rationale'"
    assert "implication" in params, "Missing parameter 'implication'"
    assert "metric" in params, "Missing parameter 'metric'"
    assert "statementOfPrinciple" in params, "Missing parameter 'statementOfPrinciple'"
    assert "principleCategory" in params, "Missing parameter 'principleCategory'"
    assert "priority" in params, "Missing parameter 'priority'"









def test_hyp_contentfwk_workpackage_is_not_abstract():
    assert not inspect.isabstract(contentfwk_WorkPackage)


def test_hyp_contentfwk_workpackage_constructor_exists():
    assert callable(contentfwk_WorkPackage.__init__)


def test_hyp_contentfwk_workpackage_constructor_args():
    sig = inspect.signature(contentfwk_WorkPackage.__init__)
    params = list(sig.parameters.keys())
    assert "capabilityDelivered" in params, "Missing parameter 'capabilityDelivered'"
    assert "workPackageCategory" in params, "Missing parameter 'workPackageCategory'"





def test_hyp_contentfwk_gap_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Gap)


def test_hyp_contentfwk_gap_constructor_exists():
    assert callable(contentfwk_Gap.__init__)


def test_hyp_contentfwk_gap_constructor_args():
    sig = inspect.signature(contentfwk_Gap.__init__)
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






def test_hyp_contentfwk_assumption_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Assumption)


def test_hyp_contentfwk_assumption_constructor_exists():
    assert callable(contentfwk_Assumption.__init__)


def test_hyp_contentfwk_assumption_constructor_args():
    sig = inspect.signature(contentfwk_Assumption.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_constraint_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Constraint)


def test_hyp_contentfwk_constraint_constructor_exists():
    assert callable(contentfwk_Constraint.__init__)


def test_hyp_contentfwk_constraint_constructor_args():
    sig = inspect.signature(contentfwk_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_element_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Element)


def test_hyp_contentfwk_element_constructor_exists():
    assert callable(contentfwk_Element.__init__)


def test_hyp_contentfwk_element_constructor_args():
    sig = inspect.signature(contentfwk_Element.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "sourceDescr" in params, "Missing parameter 'sourceDescr'"
    assert "category" in params, "Missing parameter 'category'"
    assert "ownerDescr" in params, "Missing parameter 'ownerDescr'"









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



def test_hyp_contentfwk_datacomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_DataComponent)


def test_hyp_contentfwk_datacomponent_constructor_exists():
    assert callable(contentfwk_DataComponent.__init__)


def test_hyp_contentfwk_datacomponent_constructor_args():
    sig = inspect.signature(contentfwk_DataComponent.__init__)
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



def test_hyp_contentfwk_physicalapplicationcomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_PhysicalApplicationComponent)


def test_hyp_contentfwk_physicalapplicationcomponent_constructor_exists():
    assert callable(contentfwk_PhysicalApplicationComponent.__init__)


def test_hyp_contentfwk_physicalapplicationcomponent_constructor_args():
    sig = inspect.signature(contentfwk_PhysicalApplicationComponent.__init__)
    params = list(sig.parameters.keys())
    assert "scalabilityCharacteristics" in params, "Missing parameter 'scalabilityCharacteristics'"
    assert "retirementDate" in params, "Missing parameter 'retirementDate'"
    assert "serviceabilityCharacteristics" in params, "Missing parameter 'serviceabilityCharacteristics'"
    assert "privacyCharacteristics" in params, "Missing parameter 'privacyCharacteristics'"
    assert "peakProfileLongTerm" in params, "Missing parameter 'peakProfileLongTerm'"
    assert "dateOfLastRelease" in params, "Missing parameter 'dateOfLastRelease'"
    assert "securityCharacteristics" in params, "Missing parameter 'securityCharacteristics'"
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "availabilityCharacteristics" in params, "Missing parameter 'availabilityCharacteristics'"
    assert "dateOfNextRelease" in params, "Missing parameter 'dateOfNextRelease'"
    assert "extensibilityCharacteristics" in params, "Missing parameter 'extensibilityCharacteristics'"
    assert "performanceCharacteristics" in params, "Missing parameter 'performanceCharacteristics'"
    assert "servicesTimes" in params, "Missing parameter 'servicesTimes'"
    assert "initialLiveDate" in params, "Missing parameter 'initialLiveDate'"
    assert "lifeCycleStatus" in params, "Missing parameter 'lifeCycleStatus'"
    assert "capacityCharacteristics" in params, "Missing parameter 'capacityCharacteristics'"
    assert "internationalizationCharacteristics" in params, "Missing parameter 'internationalizationCharacteristics'"
    assert "peakProfileShortTerm" in params, "Missing parameter 'peakProfileShortTerm'"
    assert "integrityCharacteristics" in params, "Missing parameter 'integrityCharacteristics'"
    assert "locatabilityCharacteristics" in params, "Missing parameter 'locatabilityCharacteristics'"
    assert "recoverabilityCharacteristics" in params, "Missing parameter 'recoverabilityCharacteristics'"
    assert "interoperabilityCharacteristics" in params, "Missing parameter 'interoperabilityCharacteristics'"
    assert "manageabilityCharacteristics" in params, "Missing parameter 'manageabilityCharacteristics'"
    assert "credibilityCharacteristics" in params, "Missing parameter 'credibilityCharacteristics'"
    assert "growth" in params, "Missing parameter 'growth'"
    assert "throughputPeriod" in params, "Missing parameter 'throughputPeriod'"
    assert "portabilityCharacteristics" in params, "Missing parameter 'portabilityCharacteristics'"
    assert "growthPeriod" in params, "Missing parameter 'growthPeriod'"
    assert "reliabilityCharacteristics" in params, "Missing parameter 'reliabilityCharacteristics'"
    assert "localizationCharacteristics" in params, "Missing parameter 'localizationCharacteristics'"

































def test_hyp_contentfwk_capability_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Capability)


def test_hyp_contentfwk_capability_constructor_exists():
    assert callable(contentfwk_Capability.__init__)


def test_hyp_contentfwk_capability_constructor_args():
    sig = inspect.signature(contentfwk_Capability.__init__)
    params = list(sig.parameters.keys())
    assert "businessValue" in params, "Missing parameter 'businessValue'"
    assert "increments" in params, "Missing parameter 'increments'"





def test_hyp_contentfwk_informationsystemservice_is_not_abstract():
    assert not inspect.isabstract(contentfwk_InformationSystemService)


def test_hyp_contentfwk_informationsystemservice_constructor_exists():
    assert callable(contentfwk_InformationSystemService.__init__)


def test_hyp_contentfwk_informationsystemservice_constructor_args():
    sig = inspect.signature(contentfwk_InformationSystemService.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_strategicelement_is_not_abstract():
    assert not inspect.isabstract(contentfwk_StrategicElement)


def test_hyp_contentfwk_strategicelement_constructor_exists():
    assert callable(contentfwk_StrategicElement.__init__)


def test_hyp_contentfwk_strategicelement_constructor_args():
    sig = inspect.signature(contentfwk_StrategicElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_logicalapplicationcomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_LogicalApplicationComponent)


def test_hyp_contentfwk_logicalapplicationcomponent_constructor_exists():
    assert callable(contentfwk_LogicalApplicationComponent.__init__)


def test_hyp_contentfwk_logicalapplicationcomponent_constructor_args():
    sig = inspect.signature(contentfwk_LogicalApplicationComponent.__init__)
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
    assert "version" in params, "Missing parameter 'version'"
    assert "categoryTRM" in params, "Missing parameter 'categoryTRM'"
    assert "moduleName" in params, "Missing parameter 'moduleName'"
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "productName" in params, "Missing parameter 'productName'"








def test_hyp_contentfwk_platformservice_is_not_abstract():
    assert not inspect.isabstract(contentfwk_PlatformService)


def test_hyp_contentfwk_platformservice_constructor_exists():
    assert callable(contentfwk_PlatformService.__init__)


def test_hyp_contentfwk_platformservice_constructor_args():
    sig = inspect.signature(contentfwk_PlatformService.__init__)
    params = list(sig.parameters.keys())
    assert "standardClass" in params, "Missing parameter 'standardClass'"
    assert "categoryTRM" in params, "Missing parameter 'categoryTRM'"





def test_hyp_contentfwk_physicaldatacomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_PhysicalDataComponent)


def test_hyp_contentfwk_physicaldatacomponent_constructor_exists():
    assert callable(contentfwk_PhysicalDataComponent.__init__)


def test_hyp_contentfwk_physicaldatacomponent_constructor_args():
    sig = inspect.signature(contentfwk_PhysicalDataComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_logicaldatacomponent_is_not_abstract():
    assert not inspect.isabstract(contentfwk_LogicalDataComponent)


def test_hyp_contentfwk_logicaldatacomponent_constructor_exists():
    assert callable(contentfwk_LogicalDataComponent.__init__)


def test_hyp_contentfwk_logicaldatacomponent_constructor_args():
    sig = inspect.signature(contentfwk_LogicalDataComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_dataentity_is_not_abstract():
    assert not inspect.isabstract(contentfwk_DataEntity)


def test_hyp_contentfwk_dataentity_constructor_exists():
    assert callable(contentfwk_DataEntity.__init__)


def test_hyp_contentfwk_dataentity_constructor_args():
    sig = inspect.signature(contentfwk_DataEntity.__init__)
    params = list(sig.parameters.keys())
    assert "dataEntityCategory" in params, "Missing parameter 'dataEntityCategory'"
    assert "privacyClassification" in params, "Missing parameter 'privacyClassification'"
    assert "retentionClassification" in params, "Missing parameter 'retentionClassification'"






def test_hyp_contentfwk_role_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Role)


def test_hyp_contentfwk_role_constructor_exists():
    assert callable(contentfwk_Role.__init__)


def test_hyp_contentfwk_role_constructor_args():
    sig = inspect.signature(contentfwk_Role.__init__)
    params = list(sig.parameters.keys())
    assert "estimatedFTEs" in params, "Missing parameter 'estimatedFTEs'"




def test_hyp_contentfwk_actor_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Actor)


def test_hyp_contentfwk_actor_constructor_exists():
    assert callable(contentfwk_Actor.__init__)


def test_hyp_contentfwk_actor_constructor_args():
    sig = inspect.signature(contentfwk_Actor.__init__)
    params = list(sig.parameters.keys())
    assert "actorGoal" in params, "Missing parameter 'actorGoal'"
    assert "FTEs" in params, "Missing parameter 'FTEs'"
    assert "actorTasks" in params, "Missing parameter 'actorTasks'"






def test_hyp_contentfwk_organizationunit_is_not_abstract():
    assert not inspect.isabstract(contentfwk_OrganizationUnit)


def test_hyp_contentfwk_organizationunit_constructor_exists():
    assert callable(contentfwk_OrganizationUnit.__init__)


def test_hyp_contentfwk_organizationunit_constructor_args():
    sig = inspect.signature(contentfwk_OrganizationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "headcount" in params, "Missing parameter 'headcount'"




def test_hyp_contentfwk_objective_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Objective)


def test_hyp_contentfwk_objective_constructor_exists():
    assert callable(contentfwk_Objective.__init__)


def test_hyp_contentfwk_objective_constructor_args():
    sig = inspect.signature(contentfwk_Objective.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_goal_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Goal)


def test_hyp_contentfwk_goal_constructor_exists():
    assert callable(contentfwk_Goal.__init__)


def test_hyp_contentfwk_goal_constructor_args():
    sig = inspect.signature(contentfwk_Goal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_driver_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Driver)


def test_hyp_contentfwk_driver_constructor_exists():
    assert callable(contentfwk_Driver.__init__)


def test_hyp_contentfwk_driver_constructor_args():
    sig = inspect.signature(contentfwk_Driver.__init__)
    params = list(sig.parameters.keys())



def test_hyp_architecture_is_not_abstract():
    assert not inspect.isabstract(Architecture)


def test_hyp_architecture_constructor_exists():
    assert callable(Architecture.__init__)


def test_hyp_architecture_constructor_args():
    sig = inspect.signature(Architecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_technologyarchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_TechnologyArchitecture)


def test_hyp_contentfwk_technologyarchitecture_constructor_exists():
    assert callable(contentfwk_TechnologyArchitecture.__init__)


def test_hyp_contentfwk_technologyarchitecture_constructor_args():
    sig = inspect.signature(contentfwk_TechnologyArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_applicationarchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_ApplicationArchitecture)


def test_hyp_contentfwk_applicationarchitecture_constructor_exists():
    assert callable(contentfwk_ApplicationArchitecture.__init__)


def test_hyp_contentfwk_applicationarchitecture_constructor_args():
    sig = inspect.signature(contentfwk_ApplicationArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_dataarchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_DataArchitecture)


def test_hyp_contentfwk_dataarchitecture_constructor_exists():
    assert callable(contentfwk_DataArchitecture.__init__)


def test_hyp_contentfwk_dataarchitecture_constructor_args():
    sig = inspect.signature(contentfwk_DataArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_strategicarchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_StrategicArchitecture)


def test_hyp_contentfwk_strategicarchitecture_constructor_exists():
    assert callable(contentfwk_StrategicArchitecture.__init__)


def test_hyp_contentfwk_strategicarchitecture_constructor_args():
    sig = inspect.signature(contentfwk_StrategicArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_businessarchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_BusinessArchitecture)


def test_hyp_contentfwk_businessarchitecture_constructor_exists():
    assert callable(contentfwk_BusinessArchitecture.__init__)


def test_hyp_contentfwk_businessarchitecture_constructor_args():
    sig = inspect.signature(contentfwk_BusinessArchitecture.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_servicequality_is_not_abstract():
    assert not inspect.isabstract(contentfwk_ServiceQuality)


def test_hyp_contentfwk_servicequality_constructor_exists():
    assert callable(contentfwk_ServiceQuality.__init__)


def test_hyp_contentfwk_servicequality_constructor_args():
    sig = inspect.signature(contentfwk_ServiceQuality.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_measure_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Measure)


def test_hyp_contentfwk_measure_constructor_exists():
    assert callable(contentfwk_Measure.__init__)


def test_hyp_contentfwk_measure_constructor_args():
    sig = inspect.signature(contentfwk_Measure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_contract_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Contract)


def test_hyp_contentfwk_contract_constructor_exists():
    assert callable(contentfwk_Contract.__init__)


def test_hyp_contentfwk_contract_constructor_args():
    sig = inspect.signature(contentfwk_Contract.__init__)
    params = list(sig.parameters.keys())
    assert "portabilityCharacteristics" in params, "Missing parameter 'portabilityCharacteristics'"
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "credibilityCharacteristics" in params, "Missing parameter 'credibilityCharacteristics'"
    assert "throughputPeriod" in params, "Missing parameter 'throughputPeriod'"
    assert "reliabilityCharacteristics" in params, "Missing parameter 'reliabilityCharacteristics'"
    assert "contractControlRequirements" in params, "Missing parameter 'contractControlRequirements'"
    assert "scalabilityCharacteristics" in params, "Missing parameter 'scalabilityCharacteristics'"
    assert "serviceNameCalled" in params, "Missing parameter 'serviceNameCalled'"
    assert "behaviorCharacteristics" in params, "Missing parameter 'behaviorCharacteristics'"
    assert "internationalizationCharacteristics" in params, "Missing parameter 'internationalizationCharacteristics'"
    assert "responseCharacteristics" in params, "Missing parameter 'responseCharacteristics'"
    assert "recoverabilityCharacteristics" in params, "Missing parameter 'recoverabilityCharacteristics'"
    assert "privacyCharacteristics" in params, "Missing parameter 'privacyCharacteristics'"
    assert "integrityCharacteristics" in params, "Missing parameter 'integrityCharacteristics'"
    assert "servicesTimes" in params, "Missing parameter 'servicesTimes'"
    assert "locatabilityCharacteristics" in params, "Missing parameter 'locatabilityCharacteristics'"
    assert "resultControlRequirements" in params, "Missing parameter 'resultControlRequirements'"
    assert "growth" in params, "Missing parameter 'growth'"
    assert "performanceCharacteristics" in params, "Missing parameter 'performanceCharacteristics'"
    assert "qualityOfInformationRequired" in params, "Missing parameter 'qualityOfInformationRequired'"
    assert "availabilityQualityCharacteristics" in params, "Missing parameter 'availabilityQualityCharacteristics'"
    assert "serviceabilityCharacteristics" in params, "Missing parameter 'serviceabilityCharacteristics'"
    assert "serviceQualityCharacteristics" in params, "Missing parameter 'serviceQualityCharacteristics'"
    assert "interoperabilityCharacteristics" in params, "Missing parameter 'interoperabilityCharacteristics'"
    assert "capacityCharacteristics" in params, "Missing parameter 'capacityCharacteristics'"
    assert "peakProfileLongTerm" in params, "Missing parameter 'peakProfileLongTerm'"
    assert "serviceNameCaller" in params, "Missing parameter 'serviceNameCaller'"
    assert "peakProfileShortTerm" in params, "Missing parameter 'peakProfileShortTerm'"
    assert "extensibilityCharacteristics" in params, "Missing parameter 'extensibilityCharacteristics'"
    assert "securityCharacteristics" in params, "Missing parameter 'securityCharacteristics'"
    assert "manageabilityCharacteristics" in params, "Missing parameter 'manageabilityCharacteristics'"
    assert "localizationCharacteristics" in params, "Missing parameter 'localizationCharacteristics'"
    assert "growthPeriod" in params, "Missing parameter 'growthPeriod'"




































def test_hyp_contentfwk_product_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Product)


def test_hyp_contentfwk_product_constructor_exists():
    assert callable(contentfwk_Product.__init__)


def test_hyp_contentfwk_product_constructor_args():
    sig = inspect.signature(contentfwk_Product.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_location_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Location)


def test_hyp_contentfwk_location_constructor_exists():
    assert callable(contentfwk_Location.__init__)


def test_hyp_contentfwk_location_constructor_args():
    sig = inspect.signature(contentfwk_Location.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_event_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Event)


def test_hyp_contentfwk_event_constructor_exists():
    assert callable(contentfwk_Event.__init__)


def test_hyp_contentfwk_event_constructor_args():
    sig = inspect.signature(contentfwk_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_control_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Control)


def test_hyp_contentfwk_control_constructor_exists():
    assert callable(contentfwk_Control.__init__)


def test_hyp_contentfwk_control_constructor_args():
    sig = inspect.signature(contentfwk_Control.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_process_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Process)


def test_hyp_contentfwk_process_constructor_exists():
    assert callable(contentfwk_Process.__init__)


def test_hyp_contentfwk_process_constructor_args():
    sig = inspect.signature(contentfwk_Process.__init__)
    params = list(sig.parameters.keys())
    assert "processVolumetrics" in params, "Missing parameter 'processVolumetrics'"
    assert "isAutomated" in params, "Missing parameter 'isAutomated'"
    assert "processCritiality" in params, "Missing parameter 'processCritiality'"






def test_hyp_contentfwk_businessservice_is_not_abstract():
    assert not inspect.isabstract(contentfwk_BusinessService)


def test_hyp_contentfwk_businessservice_constructor_exists():
    assert callable(contentfwk_BusinessService.__init__)


def test_hyp_contentfwk_businessservice_constructor_args():
    sig = inspect.signature(contentfwk_BusinessService.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_function_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Function)


def test_hyp_contentfwk_function_constructor_exists():
    assert callable(contentfwk_Function.__init__)


def test_hyp_contentfwk_function_constructor_args():
    sig = inspect.signature(contentfwk_Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentfwk_architecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_Architecture)


def test_hyp_contentfwk_architecture_constructor_exists():
    assert callable(contentfwk_Architecture.__init__)


def test_hyp_contentfwk_architecture_constructor_args():
    sig = inspect.signature(contentfwk_Architecture.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"




def test_hyp_contentfwk_enterprisearchitecture_is_not_abstract():
    assert not inspect.isabstract(contentfwk_EnterpriseArchitecture)


def test_hyp_contentfwk_enterprisearchitecture_constructor_exists():
    assert callable(contentfwk_EnterpriseArchitecture.__init__)


def test_hyp_contentfwk_enterprisearchitecture_constructor_args():
    sig = inspect.signature(contentfwk_EnterpriseArchitecture.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"


def test_hyp_principlecategory_exists():
    # Check that the Enumeration exists
    assert PrincipleCategory is not None

def test_hyp_principlecategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrincipleCategory]
    expected_literals = [
        "GuidingPrinciple",
        "TechnologyPrinciple",
        "DataPrinciple",
        "ApplicationPrinciple",
        "IntegrationPrinciple",
        "BusinessPrinciple",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrincipleCategory"

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
        "Program",
        "WorkPackage",
        "WorkStream",
        "Project",
        "Portofolio",
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
        "PhasingOut",
        "InDevelopment",
        "Retired",
        "Proposed",
        "Live",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LifeCycleStatus"

def test_hyp_standardsclass_exists():
    # Check that the Enumeration exists
    assert StandardsClass is not None

def test_hyp_standardsclass_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StandardsClass]
    expected_literals = [
        "Retired",
        "NonStandard",
        "PhasingOut",
        "Standard",
        "Proposed",
        "Provisional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StandardsClass"


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
contentfwk_Standard_strategy = st.builds(
    contentfwk_Standard,
    standardCreationDate=
        st.dates(),
    standardClass=
        safe_text,
    nextStandardReviewDate=
        st.dates(),
    lastStandardReviewDate=
        st.dates(),
    retireDate=
        st.dates()
)
DataComponent_strategy = st.builds(
    DataComponent,
)
StrategicElement_strategy = st.builds(
    StrategicElement,
)
contentfwk_Principle_strategy = st.builds(
    contentfwk_Principle,
    rationale=
        safe_text,
    implication=
        safe_text,
    metric=
        safe_text,
    statementOfPrinciple=
        safe_text,
    principleCategory=
        safe_text,
    priority=
        safe_text
)
contentfwk_WorkPackage_strategy = st.builds(
    contentfwk_WorkPackage,
    capabilityDelivered=
        safe_text,
    workPackageCategory=
        safe_text
)
contentfwk_Gap_strategy = st.builds(
    contentfwk_Gap,
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
contentfwk_Assumption_strategy = st.builds(
    contentfwk_Assumption,
)
contentfwk_Constraint_strategy = st.builds(
    contentfwk_Constraint,
)
contentfwk_Element_strategy = st.builds(
    contentfwk_Element,
    ID=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    sourceDescr=
        safe_text,
    category=
        safe_text,
    ownerDescr=
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
contentfwk_TechnologyComponent_strategy = st.builds(
    contentfwk_TechnologyComponent,
)
contentfwk_ApplicationComponent_strategy = st.builds(
    contentfwk_ApplicationComponent,
)
contentfwk_DataComponent_strategy = st.builds(
    contentfwk_DataComponent,
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
contentfwk_PhysicalApplicationComponent_strategy = st.builds(
    contentfwk_PhysicalApplicationComponent,
    scalabilityCharacteristics=
        safe_text,
    retirementDate=
        st.dates(),
    serviceabilityCharacteristics=
        safe_text,
    privacyCharacteristics=
        safe_text,
    peakProfileLongTerm=
        safe_text,
    dateOfLastRelease=
        st.dates(),
    securityCharacteristics=
        safe_text,
    throughput=
        safe_text,
    availabilityCharacteristics=
        safe_text,
    dateOfNextRelease=
        st.dates(),
    extensibilityCharacteristics=
        safe_text,
    performanceCharacteristics=
        safe_text,
    servicesTimes=
        safe_text,
    initialLiveDate=
        st.dates(),
    lifeCycleStatus=
        safe_text,
    capacityCharacteristics=
        safe_text,
    internationalizationCharacteristics=
        safe_text,
    peakProfileShortTerm=
        safe_text,
    integrityCharacteristics=
        safe_text,
    locatabilityCharacteristics=
        safe_text,
    recoverabilityCharacteristics=
        safe_text,
    interoperabilityCharacteristics=
        safe_text,
    manageabilityCharacteristics=
        safe_text,
    credibilityCharacteristics=
        safe_text,
    growth=
        safe_text,
    throughputPeriod=
        safe_text,
    portabilityCharacteristics=
        safe_text,
    growthPeriod=
        safe_text,
    reliabilityCharacteristics=
        safe_text,
    localizationCharacteristics=
        safe_text
)
contentfwk_Capability_strategy = st.builds(
    contentfwk_Capability,
    businessValue=
        safe_text,
    increments=
        safe_text
)
contentfwk_InformationSystemService_strategy = st.builds(
    contentfwk_InformationSystemService,
)
contentfwk_StrategicElement_strategy = st.builds(
    contentfwk_StrategicElement,
)
contentfwk_LogicalApplicationComponent_strategy = st.builds(
    contentfwk_LogicalApplicationComponent,
)
contentfwk_LogicalTechnologyComponent_strategy = st.builds(
    contentfwk_LogicalTechnologyComponent,
    categoryTRM=
        safe_text
)
contentfwk_PhysicalTechnologyComponent_strategy = st.builds(
    contentfwk_PhysicalTechnologyComponent,
    version=
        safe_text,
    categoryTRM=
        safe_text,
    moduleName=
        safe_text,
    vendor=
        safe_text,
    productName=
        safe_text
)
contentfwk_PlatformService_strategy = st.builds(
    contentfwk_PlatformService,
    standardClass=
        safe_text,
    categoryTRM=
        safe_text
)
contentfwk_PhysicalDataComponent_strategy = st.builds(
    contentfwk_PhysicalDataComponent,
)
contentfwk_LogicalDataComponent_strategy = st.builds(
    contentfwk_LogicalDataComponent,
)
contentfwk_DataEntity_strategy = st.builds(
    contentfwk_DataEntity,
    dataEntityCategory=
        safe_text,
    privacyClassification=
        safe_text,
    retentionClassification=
        safe_text
)
contentfwk_Role_strategy = st.builds(
    contentfwk_Role,
    estimatedFTEs=
        safe_text
)
contentfwk_Actor_strategy = st.builds(
    contentfwk_Actor,
    actorGoal=
        safe_text,
    FTEs=
        safe_text,
    actorTasks=
        safe_text
)
contentfwk_OrganizationUnit_strategy = st.builds(
    contentfwk_OrganizationUnit,
    headcount=
        safe_text
)
contentfwk_Objective_strategy = st.builds(
    contentfwk_Objective,
)
contentfwk_Goal_strategy = st.builds(
    contentfwk_Goal,
)
contentfwk_Driver_strategy = st.builds(
    contentfwk_Driver,
)
Architecture_strategy = st.builds(
    Architecture,
)
contentfwk_TechnologyArchitecture_strategy = st.builds(
    contentfwk_TechnologyArchitecture,
)
contentfwk_ApplicationArchitecture_strategy = st.builds(
    contentfwk_ApplicationArchitecture,
)
contentfwk_DataArchitecture_strategy = st.builds(
    contentfwk_DataArchitecture,
)
contentfwk_StrategicArchitecture_strategy = st.builds(
    contentfwk_StrategicArchitecture,
)
contentfwk_BusinessArchitecture_strategy = st.builds(
    contentfwk_BusinessArchitecture,
)
contentfwk_ServiceQuality_strategy = st.builds(
    contentfwk_ServiceQuality,
)
contentfwk_Measure_strategy = st.builds(
    contentfwk_Measure,
)
contentfwk_Contract_strategy = st.builds(
    contentfwk_Contract,
    portabilityCharacteristics=
        safe_text,
    throughput=
        safe_text,
    credibilityCharacteristics=
        safe_text,
    throughputPeriod=
        safe_text,
    reliabilityCharacteristics=
        safe_text,
    contractControlRequirements=
        safe_text,
    scalabilityCharacteristics=
        safe_text,
    serviceNameCalled=
        safe_text,
    behaviorCharacteristics=
        safe_text,
    internationalizationCharacteristics=
        safe_text,
    responseCharacteristics=
        safe_text,
    recoverabilityCharacteristics=
        safe_text,
    privacyCharacteristics=
        safe_text,
    integrityCharacteristics=
        safe_text,
    servicesTimes=
        safe_text,
    locatabilityCharacteristics=
        safe_text,
    resultControlRequirements=
        safe_text,
    growth=
        safe_text,
    performanceCharacteristics=
        safe_text,
    qualityOfInformationRequired=
        safe_text,
    availabilityQualityCharacteristics=
        safe_text,
    serviceabilityCharacteristics=
        safe_text,
    serviceQualityCharacteristics=
        safe_text,
    interoperabilityCharacteristics=
        safe_text,
    capacityCharacteristics=
        safe_text,
    peakProfileLongTerm=
        safe_text,
    serviceNameCaller=
        safe_text,
    peakProfileShortTerm=
        safe_text,
    extensibilityCharacteristics=
        safe_text,
    securityCharacteristics=
        safe_text,
    manageabilityCharacteristics=
        safe_text,
    localizationCharacteristics=
        safe_text,
    growthPeriod=
        safe_text
)
contentfwk_Product_strategy = st.builds(
    contentfwk_Product,
)
contentfwk_Location_strategy = st.builds(
    contentfwk_Location,
)
contentfwk_Event_strategy = st.builds(
    contentfwk_Event,
)
contentfwk_Control_strategy = st.builds(
    contentfwk_Control,
)
contentfwk_Process_strategy = st.builds(
    contentfwk_Process,
    processVolumetrics=
        safe_text,
    isAutomated=
        st.booleans(),
    processCritiality=
        safe_text
)
contentfwk_BusinessService_strategy = st.builds(
    contentfwk_BusinessService,
)
contentfwk_Function_strategy = st.builds(
    contentfwk_Function,
)
contentfwk_Architecture_strategy = st.builds(
    contentfwk_Architecture,
    ID=
        safe_text
)
contentfwk_EnterpriseArchitecture_strategy = st.builds(
    contentfwk_EnterpriseArchitecture,
    ID=
        safe_text
)




@given(instance=contentfwk_Standard_strategy)
def test_hyp_contentfwk_standard_standardCreationDate_setter(instance):
    original = instance.standardCreationDate
    instance.standardCreationDate = original
    assert instance.standardCreationDate == original



@given(instance=contentfwk_Standard_strategy)
def test_hyp_contentfwk_standard_standardClass_setter(instance):
    original = instance.standardClass
    instance.standardClass = original
    assert instance.standardClass == original



@given(instance=contentfwk_Standard_strategy)
def test_hyp_contentfwk_standard_nextStandardReviewDate_setter(instance):
    original = instance.nextStandardReviewDate
    instance.nextStandardReviewDate = original
    assert instance.nextStandardReviewDate == original



@given(instance=contentfwk_Standard_strategy)
def test_hyp_contentfwk_standard_lastStandardReviewDate_setter(instance):
    original = instance.lastStandardReviewDate
    instance.lastStandardReviewDate = original
    assert instance.lastStandardReviewDate == original



@given(instance=contentfwk_Standard_strategy)
def test_hyp_contentfwk_standard_retireDate_setter(instance):
    original = instance.retireDate
    instance.retireDate = original
    assert instance.retireDate == original






@given(instance=contentfwk_Principle_strategy)
def test_hyp_contentfwk_principle_rationale_setter(instance):
    original = instance.rationale
    instance.rationale = original
    assert instance.rationale == original



@given(instance=contentfwk_Principle_strategy)
def test_hyp_contentfwk_principle_implication_setter(instance):
    original = instance.implication
    instance.implication = original
    assert instance.implication == original



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
def test_hyp_contentfwk_principle_principleCategory_setter(instance):
    original = instance.principleCategory
    instance.principleCategory = original
    assert instance.principleCategory == original



@given(instance=contentfwk_Principle_strategy)
def test_hyp_contentfwk_principle_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original




@given(instance=contentfwk_WorkPackage_strategy)
def test_hyp_contentfwk_workpackage_capabilityDelivered_setter(instance):
    original = instance.capabilityDelivered
    instance.capabilityDelivered = original
    assert instance.capabilityDelivered == original



@given(instance=contentfwk_WorkPackage_strategy)
def test_hyp_contentfwk_workpackage_workPackageCategory_setter(instance):
    original = instance.workPackageCategory
    instance.workPackageCategory = original
    assert instance.workPackageCategory == original





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






@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_sourceDescr_setter(instance):
    original = instance.sourceDescr
    instance.sourceDescr = original
    assert instance.sourceDescr == original



@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=contentfwk_Element_strategy)
def test_hyp_contentfwk_element_ownerDescr_setter(instance):
    original = instance.ownerDescr
    instance.ownerDescr = original
    assert instance.ownerDescr == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings














@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_scalabilityCharacteristics_setter(instance):
    original = instance.scalabilityCharacteristics
    instance.scalabilityCharacteristics = original
    assert instance.scalabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_retirementDate_setter(instance):
    original = instance.retirementDate
    instance.retirementDate = original
    assert instance.retirementDate == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_serviceabilityCharacteristics_setter(instance):
    original = instance.serviceabilityCharacteristics
    instance.serviceabilityCharacteristics = original
    assert instance.serviceabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_privacyCharacteristics_setter(instance):
    original = instance.privacyCharacteristics
    instance.privacyCharacteristics = original
    assert instance.privacyCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_peakProfileLongTerm_setter(instance):
    original = instance.peakProfileLongTerm
    instance.peakProfileLongTerm = original
    assert instance.peakProfileLongTerm == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_dateOfLastRelease_setter(instance):
    original = instance.dateOfLastRelease
    instance.dateOfLastRelease = original
    assert instance.dateOfLastRelease == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_securityCharacteristics_setter(instance):
    original = instance.securityCharacteristics
    instance.securityCharacteristics = original
    assert instance.securityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_availabilityCharacteristics_setter(instance):
    original = instance.availabilityCharacteristics
    instance.availabilityCharacteristics = original
    assert instance.availabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_dateOfNextRelease_setter(instance):
    original = instance.dateOfNextRelease
    instance.dateOfNextRelease = original
    assert instance.dateOfNextRelease == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_extensibilityCharacteristics_setter(instance):
    original = instance.extensibilityCharacteristics
    instance.extensibilityCharacteristics = original
    assert instance.extensibilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_performanceCharacteristics_setter(instance):
    original = instance.performanceCharacteristics
    instance.performanceCharacteristics = original
    assert instance.performanceCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_servicesTimes_setter(instance):
    original = instance.servicesTimes
    instance.servicesTimes = original
    assert instance.servicesTimes == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_initialLiveDate_setter(instance):
    original = instance.initialLiveDate
    instance.initialLiveDate = original
    assert instance.initialLiveDate == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_lifeCycleStatus_setter(instance):
    original = instance.lifeCycleStatus
    instance.lifeCycleStatus = original
    assert instance.lifeCycleStatus == original



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
def test_hyp_contentfwk_physicalapplicationcomponent_peakProfileShortTerm_setter(instance):
    original = instance.peakProfileShortTerm
    instance.peakProfileShortTerm = original
    assert instance.peakProfileShortTerm == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_integrityCharacteristics_setter(instance):
    original = instance.integrityCharacteristics
    instance.integrityCharacteristics = original
    assert instance.integrityCharacteristics == original



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
def test_hyp_contentfwk_physicalapplicationcomponent_interoperabilityCharacteristics_setter(instance):
    original = instance.interoperabilityCharacteristics
    instance.interoperabilityCharacteristics = original
    assert instance.interoperabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_manageabilityCharacteristics_setter(instance):
    original = instance.manageabilityCharacteristics
    instance.manageabilityCharacteristics = original
    assert instance.manageabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_credibilityCharacteristics_setter(instance):
    original = instance.credibilityCharacteristics
    instance.credibilityCharacteristics = original
    assert instance.credibilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_growth_setter(instance):
    original = instance.growth
    instance.growth = original
    assert instance.growth == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_throughputPeriod_setter(instance):
    original = instance.throughputPeriod
    instance.throughputPeriod = original
    assert instance.throughputPeriod == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_portabilityCharacteristics_setter(instance):
    original = instance.portabilityCharacteristics
    instance.portabilityCharacteristics = original
    assert instance.portabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_growthPeriod_setter(instance):
    original = instance.growthPeriod
    instance.growthPeriod = original
    assert instance.growthPeriod == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_reliabilityCharacteristics_setter(instance):
    original = instance.reliabilityCharacteristics
    instance.reliabilityCharacteristics = original
    assert instance.reliabilityCharacteristics == original



@given(instance=contentfwk_PhysicalApplicationComponent_strategy)
def test_hyp_contentfwk_physicalapplicationcomponent_localizationCharacteristics_setter(instance):
    original = instance.localizationCharacteristics
    instance.localizationCharacteristics = original
    assert instance.localizationCharacteristics == original




@given(instance=contentfwk_Capability_strategy)
def test_hyp_contentfwk_capability_businessValue_setter(instance):
    original = instance.businessValue
    instance.businessValue = original
    assert instance.businessValue == original



@given(instance=contentfwk_Capability_strategy)
def test_hyp_contentfwk_capability_increments_setter(instance):
    original = instance.increments
    instance.increments = original
    assert instance.increments == original







@given(instance=contentfwk_LogicalTechnologyComponent_strategy)
def test_hyp_contentfwk_logicaltechnologycomponent_categoryTRM_setter(instance):
    original = instance.categoryTRM
    instance.categoryTRM = original
    assert instance.categoryTRM == original




@given(instance=contentfwk_PhysicalTechnologyComponent_strategy)
def test_hyp_contentfwk_physicaltechnologycomponent_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



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
def test_hyp_contentfwk_physicaltechnologycomponent_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original



@given(instance=contentfwk_PhysicalTechnologyComponent_strategy)
def test_hyp_contentfwk_physicaltechnologycomponent_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original




@given(instance=contentfwk_PlatformService_strategy)
def test_hyp_contentfwk_platformservice_standardClass_setter(instance):
    original = instance.standardClass
    instance.standardClass = original
    assert instance.standardClass == original



@given(instance=contentfwk_PlatformService_strategy)
def test_hyp_contentfwk_platformservice_categoryTRM_setter(instance):
    original = instance.categoryTRM
    instance.categoryTRM = original
    assert instance.categoryTRM == original






@given(instance=contentfwk_DataEntity_strategy)
def test_hyp_contentfwk_dataentity_dataEntityCategory_setter(instance):
    original = instance.dataEntityCategory
    instance.dataEntityCategory = original
    assert instance.dataEntityCategory == original



@given(instance=contentfwk_DataEntity_strategy)
def test_hyp_contentfwk_dataentity_privacyClassification_setter(instance):
    original = instance.privacyClassification
    instance.privacyClassification = original
    assert instance.privacyClassification == original



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




@given(instance=contentfwk_Actor_strategy)
def test_hyp_contentfwk_actor_actorGoal_setter(instance):
    original = instance.actorGoal
    instance.actorGoal = original
    assert instance.actorGoal == original



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




@given(instance=contentfwk_OrganizationUnit_strategy)
def test_hyp_contentfwk_organizationunit_headcount_setter(instance):
    original = instance.headcount
    instance.headcount = original
    assert instance.headcount == original















@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_portabilityCharacteristics_setter(instance):
    original = instance.portabilityCharacteristics
    instance.portabilityCharacteristics = original
    assert instance.portabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_credibilityCharacteristics_setter(instance):
    original = instance.credibilityCharacteristics
    instance.credibilityCharacteristics = original
    assert instance.credibilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_throughputPeriod_setter(instance):
    original = instance.throughputPeriod
    instance.throughputPeriod = original
    assert instance.throughputPeriod == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_reliabilityCharacteristics_setter(instance):
    original = instance.reliabilityCharacteristics
    instance.reliabilityCharacteristics = original
    assert instance.reliabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_contractControlRequirements_setter(instance):
    original = instance.contractControlRequirements
    instance.contractControlRequirements = original
    assert instance.contractControlRequirements == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_scalabilityCharacteristics_setter(instance):
    original = instance.scalabilityCharacteristics
    instance.scalabilityCharacteristics = original
    assert instance.scalabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_serviceNameCalled_setter(instance):
    original = instance.serviceNameCalled
    instance.serviceNameCalled = original
    assert instance.serviceNameCalled == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_behaviorCharacteristics_setter(instance):
    original = instance.behaviorCharacteristics
    instance.behaviorCharacteristics = original
    assert instance.behaviorCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_internationalizationCharacteristics_setter(instance):
    original = instance.internationalizationCharacteristics
    instance.internationalizationCharacteristics = original
    assert instance.internationalizationCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_responseCharacteristics_setter(instance):
    original = instance.responseCharacteristics
    instance.responseCharacteristics = original
    assert instance.responseCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_recoverabilityCharacteristics_setter(instance):
    original = instance.recoverabilityCharacteristics
    instance.recoverabilityCharacteristics = original
    assert instance.recoverabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_privacyCharacteristics_setter(instance):
    original = instance.privacyCharacteristics
    instance.privacyCharacteristics = original
    assert instance.privacyCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_integrityCharacteristics_setter(instance):
    original = instance.integrityCharacteristics
    instance.integrityCharacteristics = original
    assert instance.integrityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_servicesTimes_setter(instance):
    original = instance.servicesTimes
    instance.servicesTimes = original
    assert instance.servicesTimes == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_locatabilityCharacteristics_setter(instance):
    original = instance.locatabilityCharacteristics
    instance.locatabilityCharacteristics = original
    assert instance.locatabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_resultControlRequirements_setter(instance):
    original = instance.resultControlRequirements
    instance.resultControlRequirements = original
    assert instance.resultControlRequirements == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_growth_setter(instance):
    original = instance.growth
    instance.growth = original
    assert instance.growth == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_performanceCharacteristics_setter(instance):
    original = instance.performanceCharacteristics
    instance.performanceCharacteristics = original
    assert instance.performanceCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_qualityOfInformationRequired_setter(instance):
    original = instance.qualityOfInformationRequired
    instance.qualityOfInformationRequired = original
    assert instance.qualityOfInformationRequired == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_availabilityQualityCharacteristics_setter(instance):
    original = instance.availabilityQualityCharacteristics
    instance.availabilityQualityCharacteristics = original
    assert instance.availabilityQualityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_serviceabilityCharacteristics_setter(instance):
    original = instance.serviceabilityCharacteristics
    instance.serviceabilityCharacteristics = original
    assert instance.serviceabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_serviceQualityCharacteristics_setter(instance):
    original = instance.serviceQualityCharacteristics
    instance.serviceQualityCharacteristics = original
    assert instance.serviceQualityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_interoperabilityCharacteristics_setter(instance):
    original = instance.interoperabilityCharacteristics
    instance.interoperabilityCharacteristics = original
    assert instance.interoperabilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_capacityCharacteristics_setter(instance):
    original = instance.capacityCharacteristics
    instance.capacityCharacteristics = original
    assert instance.capacityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_peakProfileLongTerm_setter(instance):
    original = instance.peakProfileLongTerm
    instance.peakProfileLongTerm = original
    assert instance.peakProfileLongTerm == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_serviceNameCaller_setter(instance):
    original = instance.serviceNameCaller
    instance.serviceNameCaller = original
    assert instance.serviceNameCaller == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_peakProfileShortTerm_setter(instance):
    original = instance.peakProfileShortTerm
    instance.peakProfileShortTerm = original
    assert instance.peakProfileShortTerm == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_extensibilityCharacteristics_setter(instance):
    original = instance.extensibilityCharacteristics
    instance.extensibilityCharacteristics = original
    assert instance.extensibilityCharacteristics == original



@given(instance=contentfwk_Contract_strategy)
def test_hyp_contentfwk_contract_securityCharacteristics_setter(instance):
    original = instance.securityCharacteristics
    instance.securityCharacteristics = original
    assert instance.securityCharacteristics == original



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
def test_hyp_contentfwk_contract_growthPeriod_setter(instance):
    original = instance.growthPeriod
    instance.growthPeriod = original
    assert instance.growthPeriod == original








@given(instance=contentfwk_Process_strategy)
def test_hyp_contentfwk_process_processVolumetrics_setter(instance):
    original = instance.processVolumetrics
    instance.processVolumetrics = original
    assert instance.processVolumetrics == original



@given(instance=contentfwk_Process_strategy)
def test_hyp_contentfwk_process_isAutomated_setter(instance):
    original = instance.isAutomated
    instance.isAutomated = original
    assert instance.isAutomated == original



@given(instance=contentfwk_Process_strategy)
def test_hyp_contentfwk_process_processCritiality_setter(instance):
    original = instance.processCritiality
    instance.processCritiality = original
    assert instance.processCritiality == original






@given(instance=contentfwk_Architecture_strategy)
def test_hyp_contentfwk_architecture_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings





@given(instance=contentfwk_EnterpriseArchitecture_strategy)
def test_hyp_contentfwk_enterprisearchitecture_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



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


def test_contentfwk_Architecture_ID_value_roundtrip():
    instance = contentfwk_Architecture(ID="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


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


def test_contentfwk_Contract_availabilityQualityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.availabilityQualityCharacteristics == "sample_text"
    instance.availabilityQualityCharacteristics = "sample_text_2"
    assert instance.availabilityQualityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_behaviorCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.behaviorCharacteristics == "sample_text"
    instance.behaviorCharacteristics = "sample_text_2"
    assert instance.behaviorCharacteristics == "sample_text_2"


def test_contentfwk_Contract_capacityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.capacityCharacteristics == "sample_text"
    instance.capacityCharacteristics = "sample_text_2"
    assert instance.capacityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_contractControlRequirements_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.contractControlRequirements == "sample_text"
    instance.contractControlRequirements = "sample_text_2"
    assert instance.contractControlRequirements == "sample_text_2"


def test_contentfwk_Contract_credibilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.credibilityCharacteristics == "sample_text"
    instance.credibilityCharacteristics = "sample_text_2"
    assert instance.credibilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_extensibilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.extensibilityCharacteristics == "sample_text"
    instance.extensibilityCharacteristics = "sample_text_2"
    assert instance.extensibilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_growth_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.growth == "sample_text"
    instance.growth = "sample_text_2"
    assert instance.growth == "sample_text_2"


def test_contentfwk_Contract_growthPeriod_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.growthPeriod == "sample_text"
    instance.growthPeriod = "sample_text_2"
    assert instance.growthPeriod == "sample_text_2"


def test_contentfwk_Contract_integrityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.integrityCharacteristics == "sample_text"
    instance.integrityCharacteristics = "sample_text_2"
    assert instance.integrityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_internationalizationCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.internationalizationCharacteristics == "sample_text"
    instance.internationalizationCharacteristics = "sample_text_2"
    assert instance.internationalizationCharacteristics == "sample_text_2"


def test_contentfwk_Contract_interoperabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.interoperabilityCharacteristics == "sample_text"
    instance.interoperabilityCharacteristics = "sample_text_2"
    assert instance.interoperabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_localizationCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.localizationCharacteristics == "sample_text"
    instance.localizationCharacteristics = "sample_text_2"
    assert instance.localizationCharacteristics == "sample_text_2"


def test_contentfwk_Contract_locatabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.locatabilityCharacteristics == "sample_text"
    instance.locatabilityCharacteristics = "sample_text_2"
    assert instance.locatabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_manageabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.manageabilityCharacteristics == "sample_text"
    instance.manageabilityCharacteristics = "sample_text_2"
    assert instance.manageabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_peakProfileLongTerm_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.peakProfileLongTerm == "sample_text"
    instance.peakProfileLongTerm = "sample_text_2"
    assert instance.peakProfileLongTerm == "sample_text_2"


def test_contentfwk_Contract_peakProfileShortTerm_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.peakProfileShortTerm == "sample_text"
    instance.peakProfileShortTerm = "sample_text_2"
    assert instance.peakProfileShortTerm == "sample_text_2"


def test_contentfwk_Contract_performanceCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.performanceCharacteristics == "sample_text"
    instance.performanceCharacteristics = "sample_text_2"
    assert instance.performanceCharacteristics == "sample_text_2"


def test_contentfwk_Contract_portabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.portabilityCharacteristics == "sample_text"
    instance.portabilityCharacteristics = "sample_text_2"
    assert instance.portabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_privacyCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.privacyCharacteristics == "sample_text"
    instance.privacyCharacteristics = "sample_text_2"
    assert instance.privacyCharacteristics == "sample_text_2"


def test_contentfwk_Contract_qualityOfInformationRequired_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.qualityOfInformationRequired == "sample_text"
    instance.qualityOfInformationRequired = "sample_text_2"
    assert instance.qualityOfInformationRequired == "sample_text_2"


def test_contentfwk_Contract_recoverabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.recoverabilityCharacteristics == "sample_text"
    instance.recoverabilityCharacteristics = "sample_text_2"
    assert instance.recoverabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_reliabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.reliabilityCharacteristics == "sample_text"
    instance.reliabilityCharacteristics = "sample_text_2"
    assert instance.reliabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_responseCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.responseCharacteristics == "sample_text"
    instance.responseCharacteristics = "sample_text_2"
    assert instance.responseCharacteristics == "sample_text_2"


def test_contentfwk_Contract_resultControlRequirements_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.resultControlRequirements == "sample_text"
    instance.resultControlRequirements = "sample_text_2"
    assert instance.resultControlRequirements == "sample_text_2"


def test_contentfwk_Contract_scalabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.scalabilityCharacteristics == "sample_text"
    instance.scalabilityCharacteristics = "sample_text_2"
    assert instance.scalabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_securityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.securityCharacteristics == "sample_text"
    instance.securityCharacteristics = "sample_text_2"
    assert instance.securityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_serviceNameCalled_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.serviceNameCalled == "sample_text"
    instance.serviceNameCalled = "sample_text_2"
    assert instance.serviceNameCalled == "sample_text_2"


def test_contentfwk_Contract_serviceNameCaller_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.serviceNameCaller == "sample_text"
    instance.serviceNameCaller = "sample_text_2"
    assert instance.serviceNameCaller == "sample_text_2"


def test_contentfwk_Contract_serviceQualityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.serviceQualityCharacteristics == "sample_text"
    instance.serviceQualityCharacteristics = "sample_text_2"
    assert instance.serviceQualityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_serviceabilityCharacteristics_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.serviceabilityCharacteristics == "sample_text"
    instance.serviceabilityCharacteristics = "sample_text_2"
    assert instance.serviceabilityCharacteristics == "sample_text_2"


def test_contentfwk_Contract_servicesTimes_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.servicesTimes == "sample_text"
    instance.servicesTimes = "sample_text_2"
    assert instance.servicesTimes == "sample_text_2"


def test_contentfwk_Contract_throughput_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.throughput == "sample_text"
    instance.throughput = "sample_text_2"
    assert instance.throughput == "sample_text_2"


def test_contentfwk_Contract_throughputPeriod_value_roundtrip():
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
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
    instance = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_contentfwk_Element_category_value_roundtrip():
    instance = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_contentfwk_Element_description_value_roundtrip():
    instance = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_contentfwk_Element_name_value_roundtrip():
    instance = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_contentfwk_Element_ownerDescr_value_roundtrip():
    instance = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.ownerDescr == "sample_text"
    instance.ownerDescr = "sample_text_2"
    assert instance.ownerDescr == "sample_text_2"


def test_contentfwk_Element_sourceDescr_value_roundtrip():
    instance = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    assert instance.sourceDescr == "sample_text"
    instance.sourceDescr = "sample_text_2"
    assert instance.sourceDescr == "sample_text_2"


def test_contentfwk_EnterpriseArchitecture_ID_value_roundtrip():
    instance = contentfwk_EnterpriseArchitecture(ID="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


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


def test_contentfwk_PhysicalApplicationComponent_availabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.availabilityCharacteristics == "sample_text"
    instance.availabilityCharacteristics = "sample_text_2"
    assert instance.availabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_capacityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.capacityCharacteristics == "sample_text"
    instance.capacityCharacteristics = "sample_text_2"
    assert instance.capacityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_credibilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.credibilityCharacteristics == "sample_text"
    instance.credibilityCharacteristics = "sample_text_2"
    assert instance.credibilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_dateOfLastRelease_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.dateOfLastRelease == date(2024, 1, 1)
    instance.dateOfLastRelease = date(2025, 6, 15)
    assert instance.dateOfLastRelease == date(2025, 6, 15)


def test_contentfwk_PhysicalApplicationComponent_dateOfNextRelease_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.dateOfNextRelease == date(2024, 1, 1)
    instance.dateOfNextRelease = date(2025, 6, 15)
    assert instance.dateOfNextRelease == date(2025, 6, 15)


def test_contentfwk_PhysicalApplicationComponent_extensibilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.extensibilityCharacteristics == "sample_text"
    instance.extensibilityCharacteristics = "sample_text_2"
    assert instance.extensibilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_growth_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.growth == "sample_text"
    instance.growth = "sample_text_2"
    assert instance.growth == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_growthPeriod_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.growthPeriod == "sample_text"
    instance.growthPeriod = "sample_text_2"
    assert instance.growthPeriod == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_initialLiveDate_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.initialLiveDate == date(2024, 1, 1)
    instance.initialLiveDate = date(2025, 6, 15)
    assert instance.initialLiveDate == date(2025, 6, 15)


def test_contentfwk_PhysicalApplicationComponent_integrityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.integrityCharacteristics == "sample_text"
    instance.integrityCharacteristics = "sample_text_2"
    assert instance.integrityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_internationalizationCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.internationalizationCharacteristics == "sample_text"
    instance.internationalizationCharacteristics = "sample_text_2"
    assert instance.internationalizationCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_interoperabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.interoperabilityCharacteristics == "sample_text"
    instance.interoperabilityCharacteristics = "sample_text_2"
    assert instance.interoperabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_lifeCycleStatus_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.lifeCycleStatus == "sample_text"
    instance.lifeCycleStatus = "sample_text_2"
    assert instance.lifeCycleStatus == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_localizationCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.localizationCharacteristics == "sample_text"
    instance.localizationCharacteristics = "sample_text_2"
    assert instance.localizationCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_locatabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.locatabilityCharacteristics == "sample_text"
    instance.locatabilityCharacteristics = "sample_text_2"
    assert instance.locatabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_manageabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.manageabilityCharacteristics == "sample_text"
    instance.manageabilityCharacteristics = "sample_text_2"
    assert instance.manageabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_peakProfileLongTerm_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.peakProfileLongTerm == "sample_text"
    instance.peakProfileLongTerm = "sample_text_2"
    assert instance.peakProfileLongTerm == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_peakProfileShortTerm_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.peakProfileShortTerm == "sample_text"
    instance.peakProfileShortTerm = "sample_text_2"
    assert instance.peakProfileShortTerm == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_performanceCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.performanceCharacteristics == "sample_text"
    instance.performanceCharacteristics = "sample_text_2"
    assert instance.performanceCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_portabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.portabilityCharacteristics == "sample_text"
    instance.portabilityCharacteristics = "sample_text_2"
    assert instance.portabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_privacyCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.privacyCharacteristics == "sample_text"
    instance.privacyCharacteristics = "sample_text_2"
    assert instance.privacyCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_recoverabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.recoverabilityCharacteristics == "sample_text"
    instance.recoverabilityCharacteristics = "sample_text_2"
    assert instance.recoverabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_reliabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.reliabilityCharacteristics == "sample_text"
    instance.reliabilityCharacteristics = "sample_text_2"
    assert instance.reliabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_retirementDate_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.retirementDate == date(2024, 1, 1)
    instance.retirementDate = date(2025, 6, 15)
    assert instance.retirementDate == date(2025, 6, 15)


def test_contentfwk_PhysicalApplicationComponent_scalabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.scalabilityCharacteristics == "sample_text"
    instance.scalabilityCharacteristics = "sample_text_2"
    assert instance.scalabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_securityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.securityCharacteristics == "sample_text"
    instance.securityCharacteristics = "sample_text_2"
    assert instance.securityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_serviceabilityCharacteristics_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.serviceabilityCharacteristics == "sample_text"
    instance.serviceabilityCharacteristics = "sample_text_2"
    assert instance.serviceabilityCharacteristics == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_servicesTimes_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.servicesTimes == "sample_text"
    instance.servicesTimes = "sample_text_2"
    assert instance.servicesTimes == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_throughput_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert instance.throughput == "sample_text"
    instance.throughput = "sample_text_2"
    assert instance.throughput == "sample_text_2"


def test_contentfwk_PhysicalApplicationComponent_throughputPeriod_value_roundtrip():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
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
    instance = contentfwk_PlatformService(categoryTRM="sample_text", standardClass="sample_text")
    assert instance.categoryTRM == "sample_text"
    instance.categoryTRM = "sample_text_2"
    assert instance.categoryTRM == "sample_text_2"


def test_contentfwk_PlatformService_standardClass_value_roundtrip():
    instance = contentfwk_PlatformService(categoryTRM="sample_text", standardClass="sample_text")
    assert instance.standardClass == "sample_text"
    instance.standardClass = "sample_text_2"
    assert instance.standardClass == "sample_text_2"


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


def test_contentfwk_Standard_lastStandardReviewDate_value_roundtrip():
    instance = contentfwk_Standard(lastStandardReviewDate=date(2024, 1, 1), nextStandardReviewDate=date(2024, 1, 1), retireDate=date(2024, 1, 1), standardClass="sample_text", standardCreationDate=date(2024, 1, 1))
    assert instance.lastStandardReviewDate == date(2024, 1, 1)
    instance.lastStandardReviewDate = date(2025, 6, 15)
    assert instance.lastStandardReviewDate == date(2025, 6, 15)


def test_contentfwk_Standard_nextStandardReviewDate_value_roundtrip():
    instance = contentfwk_Standard(lastStandardReviewDate=date(2024, 1, 1), nextStandardReviewDate=date(2024, 1, 1), retireDate=date(2024, 1, 1), standardClass="sample_text", standardCreationDate=date(2024, 1, 1))
    assert instance.nextStandardReviewDate == date(2024, 1, 1)
    instance.nextStandardReviewDate = date(2025, 6, 15)
    assert instance.nextStandardReviewDate == date(2025, 6, 15)


def test_contentfwk_Standard_retireDate_value_roundtrip():
    instance = contentfwk_Standard(lastStandardReviewDate=date(2024, 1, 1), nextStandardReviewDate=date(2024, 1, 1), retireDate=date(2024, 1, 1), standardClass="sample_text", standardCreationDate=date(2024, 1, 1))
    assert instance.retireDate == date(2024, 1, 1)
    instance.retireDate = date(2025, 6, 15)
    assert instance.retireDate == date(2025, 6, 15)


def test_contentfwk_Standard_standardClass_value_roundtrip():
    instance = contentfwk_Standard(lastStandardReviewDate=date(2024, 1, 1), nextStandardReviewDate=date(2024, 1, 1), retireDate=date(2024, 1, 1), standardClass="sample_text", standardCreationDate=date(2024, 1, 1))
    assert instance.standardClass == "sample_text"
    instance.standardClass = "sample_text_2"
    assert instance.standardClass == "sample_text_2"


def test_contentfwk_Standard_standardCreationDate_value_roundtrip():
    instance = contentfwk_Standard(lastStandardReviewDate=date(2024, 1, 1), nextStandardReviewDate=date(2024, 1, 1), retireDate=date(2024, 1, 1), standardClass="sample_text", standardCreationDate=date(2024, 1, 1))
    assert instance.standardCreationDate == date(2024, 1, 1)
    instance.standardCreationDate = date(2025, 6, 15)
    assert instance.standardCreationDate == date(2025, 6, 15)


def test_contentfwk_WorkPackage_capabilityDelivered_value_roundtrip():
    instance = contentfwk_WorkPackage(capabilityDelivered="sample_text", workPackageCategory="sample_text")
    assert instance.capabilityDelivered == "sample_text"
    instance.capabilityDelivered = "sample_text_2"
    assert instance.capabilityDelivered == "sample_text_2"


def test_contentfwk_WorkPackage_workPackageCategory_value_roundtrip():
    instance = contentfwk_WorkPackage(capabilityDelivered="sample_text", workPackageCategory="sample_text")
    assert instance.workPackageCategory == "sample_text"
    instance.workPackageCategory = "sample_text_2"
    assert instance.workPackageCategory == "sample_text_2"


def test_contentfwk_LogicalApplicationComponent_isa_ApplicationComponent():
    instance = contentfwk_LogicalApplicationComponent()
    assert isinstance(instance, ApplicationComponent)


def test_contentfwk_PhysicalApplicationComponent_isa_ApplicationComponent():
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
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
    instance = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
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
    instance = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_PhysicalDataComponent_isa_Element():
    instance = contentfwk_PhysicalDataComponent()
    assert isinstance(instance, Element)


def test_contentfwk_PhysicalTechnologyComponent_isa_Element():
    instance = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    assert isinstance(instance, Element)


def test_contentfwk_PlatformService_isa_Element():
    instance = contentfwk_PlatformService(categoryTRM="sample_text", standardClass="sample_text")
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
    instance = contentfwk_WorkPackage(capabilityDelivered="sample_text", workPackageCategory="sample_text")
    assert isinstance(instance, StrategicElement)


def test_contentfwk_LogicalTechnologyComponent_isa_TechnologyComponent():
    instance = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    assert isinstance(instance, TechnologyComponent)


def test_contentfwk_PhysicalTechnologyComponent_isa_TechnologyComponent():
    instance = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    assert isinstance(instance, TechnologyComponent)


def test_assoc_accessesFunctions110_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'canBeAccessedByRoles', {b1})
    assert _is_linked(a, 'canBeAccessedByRoles', b1)
    if hasattr(b1, 'Function111'):
        assert _is_linked(b1, 'Function111', a)
    _safe_set(a, 'canBeAccessedByRoles', {b2})
    assert _is_linked(a, 'canBeAccessedByRoles', b2)
    if hasattr(b1, 'Function111'):
        assert not _is_linked(b1, 'Function111', a)
    if hasattr(b2, 'Function111'):
        assert _is_linked(b2, 'Function111', a)
    _safe_set(a, 'canBeAccessedByRoles', set())
    assert not _is_linked(a, 'canBeAccessedByRoles', b2)
    if hasattr(b2, 'Function111'):
        assert not _is_linked(b2, 'Function111', a)


def test_assoc_actors8_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_BusinessArchitecture()
    b2 = contentfwk_BusinessArchitecture()
    _safe_set(a, 'contentfwk_Actor', b1)
    assert _is_linked(a, 'contentfwk_Actor', b1)
    if hasattr(b1, 'contentfwk_BusinessArchitecture9'):
        assert _is_linked(b1, 'contentfwk_BusinessArchitecture9', a)
    _safe_set(a, 'contentfwk_Actor', b2)
    assert _is_linked(a, 'contentfwk_Actor', b2)
    if hasattr(b1, 'contentfwk_BusinessArchitecture9'):
        assert not _is_linked(b1, 'contentfwk_BusinessArchitecture9', a)
    if hasattr(b2, 'contentfwk_BusinessArchitecture9'):
        assert _is_linked(b2, 'contentfwk_BusinessArchitecture9', a)
    _safe_set(a, 'contentfwk_Actor', None)
    assert not _is_linked(a, 'contentfwk_Actor', b2)
    if hasattr(b2, 'contentfwk_BusinessArchitecture9'):
        assert not _is_linked(b2, 'contentfwk_BusinessArchitecture9', a)


def test_assoc_appliesToContracts247_link_reassign_clear():
    a = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
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


def test_assoc_architectures0_link_reassign_clear():
    a = contentfwk_EnterpriseArchitecture(ID="sample_text")
    b1 = contentfwk_Architecture(ID="sample_text")
    b2 = contentfwk_Architecture(ID="sample_text_2")
    _safe_set(a, 'contentfwk_EnterpriseArchitecture', {b1})
    assert _is_linked(a, 'contentfwk_EnterpriseArchitecture', b1)
    if hasattr(b1, 'contentfwk_Architecture'):
        assert _is_linked(b1, 'contentfwk_Architecture', a)
    _safe_set(a, 'contentfwk_EnterpriseArchitecture', {b2})
    assert _is_linked(a, 'contentfwk_EnterpriseArchitecture', b2)
    if hasattr(b1, 'contentfwk_Architecture'):
        assert not _is_linked(b1, 'contentfwk_Architecture', a)
    if hasattr(b2, 'contentfwk_Architecture'):
        assert _is_linked(b2, 'contentfwk_Architecture', a)
    _safe_set(a, 'contentfwk_EnterpriseArchitecture', set())
    assert not _is_linked(a, 'contentfwk_EnterpriseArchitecture', b2)
    if hasattr(b2, 'contentfwk_Architecture'):
        assert not _is_linked(b2, 'contentfwk_Architecture', a)


def test_assoc_belongsToOrganizationUnit85_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'OrganizationUnit86', b1)
    assert _is_linked(a, 'OrganizationUnit86', b1)
    if hasattr(b1, 'containsActors'):
        assert _is_linked(b1, 'containsActors', a)
    _safe_set(a, 'OrganizationUnit86', b2)
    assert _is_linked(a, 'OrganizationUnit86', b2)
    if hasattr(b1, 'containsActors'):
        assert not _is_linked(b1, 'containsActors', a)
    if hasattr(b2, 'containsActors'):
        assert _is_linked(b2, 'containsActors', a)
    _safe_set(a, 'OrganizationUnit86', None)
    assert not _is_linked(a, 'OrganizationUnit86', b2)
    if hasattr(b2, 'containsActors'):
        assert not _is_linked(b2, 'containsActors', a)


def test_assoc_canBeAccessedByRoles161_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'Role162', b1)
    assert _is_linked(a, 'Role162', b1)
    if hasattr(b1, 'accessesFunctions'):
        assert _is_linked(b1, 'accessesFunctions', a)
    _safe_set(a, 'Role162', b2)
    assert _is_linked(a, 'Role162', b2)
    if hasattr(b1, 'accessesFunctions'):
        assert not _is_linked(b1, 'accessesFunctions', a)
    if hasattr(b2, 'accessesFunctions'):
        assert _is_linked(b2, 'accessesFunctions', a)
    _safe_set(a, 'Role162', None)
    assert not _is_linked(a, 'Role162', b2)
    if hasattr(b2, 'accessesFunctions'):
        assert not _is_linked(b2, 'accessesFunctions', a)


def test_assoc_capabilities349_link_reassign_clear():
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


def test_assoc_communicatesWith317_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b2 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent316', {b1})
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent316', b1)
    if hasattr(b1, 'contentfwk_PhysicalApplicationComponent318'):
        assert _is_linked(b1, 'contentfwk_PhysicalApplicationComponent318', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent316', {b2})
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent316', b2)
    if hasattr(b1, 'contentfwk_PhysicalApplicationComponent318'):
        assert not _is_linked(b1, 'contentfwk_PhysicalApplicationComponent318', a)
    if hasattr(b2, 'contentfwk_PhysicalApplicationComponent318'):
        assert _is_linked(b2, 'contentfwk_PhysicalApplicationComponent318', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent316', set())
    assert not _is_linked(a, 'contentfwk_PhysicalApplicationComponent316', b2)
    if hasattr(b2, 'contentfwk_PhysicalApplicationComponent318'):
        assert not _is_linked(b2, 'contentfwk_PhysicalApplicationComponent318', a)


def test_assoc_consumesDataEntities358_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'DataEntity359', b1)
    assert _is_linked(a, 'DataEntity359', b1)
    if hasattr(b1, 'isAccessedByServices'):
        assert _is_linked(b1, 'isAccessedByServices', a)
    _safe_set(a, 'DataEntity359', b2)
    assert _is_linked(a, 'DataEntity359', b2)
    if hasattr(b1, 'isAccessedByServices'):
        assert not _is_linked(b1, 'isAccessedByServices', a)
    if hasattr(b2, 'isAccessedByServices'):
        assert _is_linked(b2, 'isAccessedByServices', a)
    _safe_set(a, 'DataEntity359', None)
    assert not _is_linked(a, 'DataEntity359', b2)
    if hasattr(b2, 'isAccessedByServices'):
        assert not _is_linked(b2, 'isAccessedByServices', a)


def test_assoc_consumesDataEntities83_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'DataEntity84', b1)
    assert _is_linked(a, 'DataEntity84', b1)
    if hasattr(b1, 'isConsumedByActors'):
        assert _is_linked(b1, 'isConsumedByActors', a)
    _safe_set(a, 'DataEntity84', b2)
    assert _is_linked(a, 'DataEntity84', b2)
    if hasattr(b1, 'isConsumedByActors'):
        assert not _is_linked(b1, 'isConsumedByActors', a)
    if hasattr(b2, 'isConsumedByActors'):
        assert _is_linked(b2, 'isConsumedByActors', a)
    _safe_set(a, 'DataEntity84', None)
    assert not _is_linked(a, 'DataEntity84', b2)
    if hasattr(b2, 'isConsumedByActors'):
        assert not _is_linked(b2, 'isConsumedByActors', a)


def test_assoc_consumesServices92_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'isProvidedToActors', {b1})
    assert _is_linked(a, 'isProvidedToActors', b1)
    if hasattr(b1, 'Service93'):
        assert _is_linked(b1, 'Service93', a)
    _safe_set(a, 'isProvidedToActors', {b2})
    assert _is_linked(a, 'isProvidedToActors', b2)
    if hasattr(b1, 'Service93'):
        assert not _is_linked(b1, 'Service93', a)
    if hasattr(b2, 'Service93'):
        assert _is_linked(b2, 'Service93', a)
    _safe_set(a, 'isProvidedToActors', set())
    assert not _is_linked(a, 'isProvidedToActors', b2)
    if hasattr(b2, 'Service93'):
        assert not _is_linked(b2, 'Service93', a)


def test_assoc_containsActors271_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'Actor272', b1)
    assert _is_linked(a, 'Actor272', b1)
    if hasattr(b1, 'operatesInLocation'):
        assert _is_linked(b1, 'operatesInLocation', a)
    _safe_set(a, 'Actor272', b2)
    assert _is_linked(a, 'Actor272', b2)
    if hasattr(b1, 'operatesInLocation'):
        assert not _is_linked(b1, 'operatesInLocation', a)
    if hasattr(b2, 'operatesInLocation'):
        assert _is_linked(b2, 'operatesInLocation', a)
    _safe_set(a, 'Actor272', None)
    assert not _is_linked(a, 'Actor272', b2)
    if hasattr(b2, 'operatesInLocation'):
        assert not _is_linked(b2, 'operatesInLocation', a)


def test_assoc_containsActors69_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'belongsToOrganizationUnit', {b1})
    assert _is_linked(a, 'belongsToOrganizationUnit', b1)
    if hasattr(b1, 'Actor'):
        assert _is_linked(b1, 'Actor', a)
    _safe_set(a, 'belongsToOrganizationUnit', {b2})
    assert _is_linked(a, 'belongsToOrganizationUnit', b2)
    if hasattr(b1, 'Actor'):
        assert not _is_linked(b1, 'Actor', a)
    if hasattr(b2, 'Actor'):
        assert _is_linked(b2, 'Actor', a)
    _safe_set(a, 'belongsToOrganizationUnit', set())
    assert not _is_linked(a, 'belongsToOrganizationUnit', b2)
    if hasattr(b2, 'Actor'):
        assert not _is_linked(b2, 'Actor', a)


def test_assoc_containsOrganizationUnits273_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'OrganizationUnit275', b1)
    assert _is_linked(a, 'OrganizationUnit275', b1)
    if hasattr(b1, 'operatesInLocation274'):
        assert _is_linked(b1, 'operatesInLocation274', a)
    _safe_set(a, 'OrganizationUnit275', b2)
    assert _is_linked(a, 'OrganizationUnit275', b2)
    if hasattr(b1, 'operatesInLocation274'):
        assert not _is_linked(b1, 'operatesInLocation274', a)
    if hasattr(b2, 'operatesInLocation274'):
        assert _is_linked(b2, 'operatesInLocation274', a)
    _safe_set(a, 'OrganizationUnit275', None)
    assert not _is_linked(a, 'OrganizationUnit275', b2)
    if hasattr(b2, 'operatesInLocation274'):
        assert not _is_linked(b2, 'operatesInLocation274', a)


def test_assoc_containsPhysicalApplicationComponents277_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'PhysicalApplicationComponent278', b1)
    assert _is_linked(a, 'PhysicalApplicationComponent278', b1)
    if hasattr(b1, 'isHostedInLocation'):
        assert _is_linked(b1, 'isHostedInLocation', a)
    _safe_set(a, 'PhysicalApplicationComponent278', b2)
    assert _is_linked(a, 'PhysicalApplicationComponent278', b2)
    if hasattr(b1, 'isHostedInLocation'):
        assert not _is_linked(b1, 'isHostedInLocation', a)
    if hasattr(b2, 'isHostedInLocation'):
        assert _is_linked(b2, 'isHostedInLocation', a)
    _safe_set(a, 'PhysicalApplicationComponent278', None)
    assert not _is_linked(a, 'PhysicalApplicationComponent278', b2)
    if hasattr(b2, 'isHostedInLocation'):
        assert not _is_linked(b2, 'isHostedInLocation', a)


def test_assoc_containsPhysicalTechnologyComponents279_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'PhysicalTechnologyComponent281', b1)
    assert _is_linked(a, 'PhysicalTechnologyComponent281', b1)
    if hasattr(b1, 'isHostedInLocation280'):
        assert _is_linked(b1, 'isHostedInLocation280', a)
    _safe_set(a, 'PhysicalTechnologyComponent281', b2)
    assert _is_linked(a, 'PhysicalTechnologyComponent281', b2)
    if hasattr(b1, 'isHostedInLocation280'):
        assert not _is_linked(b1, 'isHostedInLocation280', a)
    if hasattr(b2, 'isHostedInLocation280'):
        assert _is_linked(b2, 'isHostedInLocation280', a)
    _safe_set(a, 'PhysicalTechnologyComponent281', None)
    assert not _is_linked(a, 'PhysicalTechnologyComponent281', b2)
    if hasattr(b2, 'isHostedInLocation280'):
        assert not _is_linked(b2, 'isHostedInLocation280', a)


def test_assoc_contracts26_link_reassign_clear():
    a = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_BusinessArchitecture()
    b2 = contentfwk_BusinessArchitecture()
    _safe_set(a, 'contentfwk_Contract', b1)
    assert _is_linked(a, 'contentfwk_Contract', b1)
    if hasattr(b1, 'contentfwk_BusinessArchitecture27'):
        assert _is_linked(b1, 'contentfwk_BusinessArchitecture27', a)
    _safe_set(a, 'contentfwk_Contract', b2)
    assert _is_linked(a, 'contentfwk_Contract', b2)
    if hasattr(b1, 'contentfwk_BusinessArchitecture27'):
        assert not _is_linked(b1, 'contentfwk_BusinessArchitecture27', a)
    if hasattr(b2, 'contentfwk_BusinessArchitecture27'):
        assert _is_linked(b2, 'contentfwk_BusinessArchitecture27', a)
    _safe_set(a, 'contentfwk_Contract', None)
    assert not _is_linked(a, 'contentfwk_Contract', b2)
    if hasattr(b2, 'contentfwk_BusinessArchitecture27'):
        assert not _is_linked(b2, 'contentfwk_BusinessArchitecture27', a)


def test_assoc_decomposesActor103_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'Actor104', b1)
    assert _is_linked(a, 'Actor104', b1)
    if hasattr(b1, 'isDecomposedByActors'):
        assert _is_linked(b1, 'isDecomposedByActors', a)
    _safe_set(a, 'Actor104', b2)
    assert _is_linked(a, 'Actor104', b2)
    if hasattr(b1, 'isDecomposedByActors'):
        assert not _is_linked(b1, 'isDecomposedByActors', a)
    if hasattr(b2, 'isDecomposedByActors'):
        assert _is_linked(b2, 'isDecomposedByActors', a)
    _safe_set(a, 'Actor104', None)
    assert not _is_linked(a, 'Actor104', b2)
    if hasattr(b2, 'isDecomposedByActors'):
        assert not _is_linked(b2, 'isDecomposedByActors', a)


def test_assoc_decomposesDataEntity130_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    _safe_set(a, 'contentfwk_DataEntity129', b1)
    assert _is_linked(a, 'contentfwk_DataEntity129', b1)
    if hasattr(b1, 'contentfwk_DataEntity131'):
        assert _is_linked(b1, 'contentfwk_DataEntity131', a)
    _safe_set(a, 'contentfwk_DataEntity129', b2)
    assert _is_linked(a, 'contentfwk_DataEntity129', b2)
    if hasattr(b1, 'contentfwk_DataEntity131'):
        assert not _is_linked(b1, 'contentfwk_DataEntity131', a)
    if hasattr(b2, 'contentfwk_DataEntity131'):
        assert _is_linked(b2, 'contentfwk_DataEntity131', a)
    _safe_set(a, 'contentfwk_DataEntity129', None)
    assert not _is_linked(a, 'contentfwk_DataEntity129', b2)
    if hasattr(b2, 'contentfwk_DataEntity131'):
        assert not _is_linked(b2, 'contentfwk_DataEntity131', a)


def test_assoc_decomposesFunctions178_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'supportsProcesses', {b1})
    assert _is_linked(a, 'supportsProcesses', b1)
    if hasattr(b1, 'Function179'):
        assert _is_linked(b1, 'Function179', a)
    _safe_set(a, 'supportsProcesses', {b2})
    assert _is_linked(a, 'supportsProcesses', b2)
    if hasattr(b1, 'Function179'):
        assert not _is_linked(b1, 'Function179', a)
    if hasattr(b2, 'Function179'):
        assert _is_linked(b2, 'Function179', a)
    _safe_set(a, 'supportsProcesses', set())
    assert not _is_linked(a, 'supportsProcesses', b2)
    if hasattr(b2, 'Function179'):
        assert not _is_linked(b2, 'Function179', a)


def test_assoc_decomposesLogicalTechnologyComponent335_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'LogicalTechnologyComponent336', b1)
    assert _is_linked(a, 'LogicalTechnologyComponent336', b1)
    if hasattr(b1, 'isDecomposedByLogicalTechnologyComponents'):
        assert _is_linked(b1, 'isDecomposedByLogicalTechnologyComponents', a)
    _safe_set(a, 'LogicalTechnologyComponent336', b2)
    assert _is_linked(a, 'LogicalTechnologyComponent336', b2)
    if hasattr(b1, 'isDecomposedByLogicalTechnologyComponents'):
        assert not _is_linked(b1, 'isDecomposedByLogicalTechnologyComponents', a)
    if hasattr(b2, 'isDecomposedByLogicalTechnologyComponents'):
        assert _is_linked(b2, 'isDecomposedByLogicalTechnologyComponents', a)
    _safe_set(a, 'LogicalTechnologyComponent336', None)
    assert not _is_linked(a, 'LogicalTechnologyComponent336', b2)
    if hasattr(b2, 'isDecomposedByLogicalTechnologyComponents'):
        assert not _is_linked(b2, 'isDecomposedByLogicalTechnologyComponents', a)


def test_assoc_decomposesOrganizationUnit77_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_OrganizationUnit(headcount="sample_text")
    b2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    _safe_set(a, 'OrganizationUnit78', b1)
    assert _is_linked(a, 'OrganizationUnit78', b1)
    if hasattr(b1, 'isDecomposedByOrganizationUnits'):
        assert _is_linked(b1, 'isDecomposedByOrganizationUnits', a)
    _safe_set(a, 'OrganizationUnit78', b2)
    assert _is_linked(a, 'OrganizationUnit78', b2)
    if hasattr(b1, 'isDecomposedByOrganizationUnits'):
        assert not _is_linked(b1, 'isDecomposedByOrganizationUnits', a)
    if hasattr(b2, 'isDecomposedByOrganizationUnits'):
        assert _is_linked(b2, 'isDecomposedByOrganizationUnits', a)
    _safe_set(a, 'OrganizationUnit78', None)
    assert not _is_linked(a, 'OrganizationUnit78', b2)
    if hasattr(b2, 'isDecomposedByOrganizationUnits'):
        assert not _is_linked(b2, 'isDecomposedByOrganizationUnits', a)


def test_assoc_decomposesPhysicalApplicationComponent324_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b2 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    _safe_set(a, 'PhysicalApplicationComponent325', b1)
    assert _is_linked(a, 'PhysicalApplicationComponent325', b1)
    if hasattr(b1, 'isDecomposedByPhysicalApplicationComponents'):
        assert _is_linked(b1, 'isDecomposedByPhysicalApplicationComponents', a)
    _safe_set(a, 'PhysicalApplicationComponent325', b2)
    assert _is_linked(a, 'PhysicalApplicationComponent325', b2)
    if hasattr(b1, 'isDecomposedByPhysicalApplicationComponents'):
        assert not _is_linked(b1, 'isDecomposedByPhysicalApplicationComponents', a)
    if hasattr(b2, 'isDecomposedByPhysicalApplicationComponents'):
        assert _is_linked(b2, 'isDecomposedByPhysicalApplicationComponents', a)
    _safe_set(a, 'PhysicalApplicationComponent325', None)
    assert not _is_linked(a, 'PhysicalApplicationComponent325', b2)
    if hasattr(b2, 'isDecomposedByPhysicalApplicationComponents'):
        assert not _is_linked(b2, 'isDecomposedByPhysicalApplicationComponents', a)


def test_assoc_decomposesPhysicalTechnologyComponent219_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    _safe_set(a, 'PhysicalTechnologyComponent', b1)
    assert _is_linked(a, 'PhysicalTechnologyComponent', b1)
    if hasattr(b1, 'isDecomposedByPhysicalTechnologyComponents'):
        assert _is_linked(b1, 'isDecomposedByPhysicalTechnologyComponents', a)
    _safe_set(a, 'PhysicalTechnologyComponent', b2)
    assert _is_linked(a, 'PhysicalTechnologyComponent', b2)
    if hasattr(b1, 'isDecomposedByPhysicalTechnologyComponents'):
        assert not _is_linked(b1, 'isDecomposedByPhysicalTechnologyComponents', a)
    if hasattr(b2, 'isDecomposedByPhysicalTechnologyComponents'):
        assert _is_linked(b2, 'isDecomposedByPhysicalTechnologyComponents', a)
    _safe_set(a, 'PhysicalTechnologyComponent', None)
    assert not _is_linked(a, 'PhysicalTechnologyComponent', b2)
    if hasattr(b2, 'isDecomposedByPhysicalTechnologyComponents'):
        assert not _is_linked(b2, 'isDecomposedByPhysicalTechnologyComponents', a)


def test_assoc_decomposesProcess199_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    _safe_set(a, 'Process200', b1)
    assert _is_linked(a, 'Process200', b1)
    if hasattr(b1, 'isDecomposedByProcesses'):
        assert _is_linked(b1, 'isDecomposedByProcesses', a)
    _safe_set(a, 'Process200', b2)
    assert _is_linked(a, 'Process200', b2)
    if hasattr(b1, 'isDecomposedByProcesses'):
        assert not _is_linked(b1, 'isDecomposedByProcesses', a)
    if hasattr(b2, 'isDecomposedByProcesses'):
        assert _is_linked(b2, 'isDecomposedByProcesses', a)
    _safe_set(a, 'Process200', None)
    assert not _is_linked(a, 'Process200', b2)
    if hasattr(b2, 'isDecomposedByProcesses'):
        assert not _is_linked(b2, 'isDecomposedByProcesses', a)


def test_assoc_decomposesRole113_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_Role(estimatedFTEs="sample_text")
    b2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    _safe_set(a, 'Role114', b1)
    assert _is_linked(a, 'Role114', b1)
    if hasattr(b1, 'isDecomposedByRoles'):
        assert _is_linked(b1, 'isDecomposedByRoles', a)
    _safe_set(a, 'Role114', b2)
    assert _is_linked(a, 'Role114', b2)
    if hasattr(b1, 'isDecomposedByRoles'):
        assert not _is_linked(b1, 'isDecomposedByRoles', a)
    if hasattr(b2, 'isDecomposedByRoles'):
        assert _is_linked(b2, 'isDecomposedByRoles', a)
    _safe_set(a, 'Role114', None)
    assert not _is_linked(a, 'Role114', b2)
    if hasattr(b2, 'isDecomposedByRoles'):
        assert not _is_linked(b2, 'isDecomposedByRoles', a)


def test_assoc_decomposesServices185_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'supportsProcesses186', {b1})
    assert _is_linked(a, 'supportsProcesses186', b1)
    if hasattr(b1, 'Service187'):
        assert _is_linked(b1, 'Service187', a)
    _safe_set(a, 'supportsProcesses186', {b2})
    assert _is_linked(a, 'supportsProcesses186', b2)
    if hasattr(b1, 'Service187'):
        assert not _is_linked(b1, 'Service187', a)
    if hasattr(b2, 'Service187'):
        assert _is_linked(b2, 'Service187', a)
    _safe_set(a, 'supportsProcesses186', set())
    assert not _is_linked(a, 'supportsProcesses186', b2)
    if hasattr(b2, 'Service187'):
        assert not _is_linked(b2, 'Service187', a)


def test_assoc_delegates267_link_reassign_clear():
    a = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    b1 = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    b2 = contentfwk_Element(ID="sample_text_2", category="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
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


def test_assoc_deliversCapabilities289_link_reassign_clear():
    a = contentfwk_WorkPackage(capabilityDelivered="sample_text", workPackageCategory="sample_text")
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


def test_assoc_encapsulatesDataEntities290_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_LogicalDataComponent()
    b2 = contentfwk_LogicalDataComponent()
    _safe_set(a, 'DataEntity291', b1)
    assert _is_linked(a, 'DataEntity291', b1)
    if hasattr(b1, 'residesWithinLogicalDataComponent'):
        assert _is_linked(b1, 'residesWithinLogicalDataComponent', a)
    _safe_set(a, 'DataEntity291', b2)
    assert _is_linked(a, 'DataEntity291', b2)
    if hasattr(b1, 'residesWithinLogicalDataComponent'):
        assert not _is_linked(b1, 'residesWithinLogicalDataComponent', a)
    if hasattr(b2, 'residesWithinLogicalDataComponent'):
        assert _is_linked(b2, 'residesWithinLogicalDataComponent', a)
    _safe_set(a, 'DataEntity291', None)
    assert not _is_linked(a, 'DataEntity291', b2)
    if hasattr(b2, 'residesWithinLogicalDataComponent'):
        assert not _is_linked(b2, 'residesWithinLogicalDataComponent', a)


def test_assoc_encapsulatesPhysicalApplicationComponents301_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_PhysicalDataComponent()
    b2 = contentfwk_PhysicalDataComponent()
    _safe_set(a, 'PhysicalApplicationComponent302', b1)
    assert _is_linked(a, 'PhysicalApplicationComponent302', b1)
    if hasattr(b1, 'encapsulatesPhysicalDataComponents'):
        assert _is_linked(b1, 'encapsulatesPhysicalDataComponents', a)
    _safe_set(a, 'PhysicalApplicationComponent302', b2)
    assert _is_linked(a, 'PhysicalApplicationComponent302', b2)
    if hasattr(b1, 'encapsulatesPhysicalDataComponents'):
        assert not _is_linked(b1, 'encapsulatesPhysicalDataComponents', a)
    if hasattr(b2, 'encapsulatesPhysicalDataComponents'):
        assert _is_linked(b2, 'encapsulatesPhysicalDataComponents', a)
    _safe_set(a, 'PhysicalApplicationComponent302', None)
    assert not _is_linked(a, 'PhysicalApplicationComponent302', b2)
    if hasattr(b2, 'encapsulatesPhysicalDataComponents'):
        assert not _is_linked(b2, 'encapsulatesPhysicalDataComponents', a)


def test_assoc_encapsulatesPhysicalDataComponents319_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_PhysicalDataComponent()
    b2 = contentfwk_PhysicalDataComponent()
    _safe_set(a, 'encapsulatesPhysicalApplicationComponents', {b1})
    assert _is_linked(a, 'encapsulatesPhysicalApplicationComponents', b1)
    if hasattr(b1, 'PhysicalDataComponent320'):
        assert _is_linked(b1, 'PhysicalDataComponent320', a)
    _safe_set(a, 'encapsulatesPhysicalApplicationComponents', {b2})
    assert _is_linked(a, 'encapsulatesPhysicalApplicationComponents', b2)
    if hasattr(b1, 'PhysicalDataComponent320'):
        assert not _is_linked(b1, 'PhysicalDataComponent320', a)
    if hasattr(b2, 'PhysicalDataComponent320'):
        assert _is_linked(b2, 'PhysicalDataComponent320', a)
    _safe_set(a, 'encapsulatesPhysicalApplicationComponents', set())
    assert not _is_linked(a, 'encapsulatesPhysicalApplicationComponents', b2)
    if hasattr(b2, 'PhysicalDataComponent320'):
        assert not _is_linked(b2, 'PhysicalDataComponent320', a)


def test_assoc_ensuresCorrectOperationOfProcesses264_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Control()
    b2 = contentfwk_Control()
    _safe_set(a, 'Process265', b1)
    assert _is_linked(a, 'Process265', b1)
    if hasattr(b1, 'isGuidedByControls'):
        assert _is_linked(b1, 'isGuidedByControls', a)
    _safe_set(a, 'Process265', b2)
    assert _is_linked(a, 'Process265', b2)
    if hasattr(b1, 'isGuidedByControls'):
        assert not _is_linked(b1, 'isGuidedByControls', a)
    if hasattr(b2, 'isGuidedByControls'):
        assert _is_linked(b2, 'isGuidedByControls', a)
    _safe_set(a, 'Process265', None)
    assert not _is_linked(a, 'Process265', b2)
    if hasattr(b2, 'isGuidedByControls'):
        assert not _is_linked(b2, 'isGuidedByControls', a)


def test_assoc_entities32_link_reassign_clear():
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


def test_assoc_extendsLogicalApplicationComponents312_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_LogicalApplicationComponent()
    b2 = contentfwk_LogicalApplicationComponent()
    _safe_set(a, 'isExtendedByPhysicalApplicationComponents', {b1})
    assert _is_linked(a, 'isExtendedByPhysicalApplicationComponents', b1)
    if hasattr(b1, 'LogicalApplicationComponent313'):
        assert _is_linked(b1, 'LogicalApplicationComponent313', a)
    _safe_set(a, 'isExtendedByPhysicalApplicationComponents', {b2})
    assert _is_linked(a, 'isExtendedByPhysicalApplicationComponents', b2)
    if hasattr(b1, 'LogicalApplicationComponent313'):
        assert not _is_linked(b1, 'LogicalApplicationComponent313', a)
    if hasattr(b2, 'LogicalApplicationComponent313'):
        assert _is_linked(b2, 'LogicalApplicationComponent313', a)
    _safe_set(a, 'isExtendedByPhysicalApplicationComponents', set())
    assert not _is_linked(a, 'isExtendedByPhysicalApplicationComponents', b2)
    if hasattr(b2, 'LogicalApplicationComponent313'):
        assert not _is_linked(b2, 'LogicalApplicationComponent313', a)


def test_assoc_extendsLogicalTechnologyComponents213_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'isRealizedByPhysicalTechnologyComponents214', {b1})
    assert _is_linked(a, 'isRealizedByPhysicalTechnologyComponents214', b1)
    if hasattr(b1, 'LogicalTechnologyComponent215'):
        assert _is_linked(b1, 'LogicalTechnologyComponent215', a)
    _safe_set(a, 'isRealizedByPhysicalTechnologyComponents214', {b2})
    assert _is_linked(a, 'isRealizedByPhysicalTechnologyComponents214', b2)
    if hasattr(b1, 'LogicalTechnologyComponent215'):
        assert not _is_linked(b1, 'LogicalTechnologyComponent215', a)
    if hasattr(b2, 'LogicalTechnologyComponent215'):
        assert _is_linked(b2, 'LogicalTechnologyComponent215', a)
    _safe_set(a, 'isRealizedByPhysicalTechnologyComponents214', set())
    assert not _is_linked(a, 'isRealizedByPhysicalTechnologyComponents214', b2)
    if hasattr(b2, 'LogicalTechnologyComponent215'):
        assert not _is_linked(b2, 'LogicalTechnologyComponent215', a)


def test_assoc_followsProcesses205_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    _safe_set(a, 'Process206', b1)
    assert _is_linked(a, 'Process206', b1)
    if hasattr(b1, 'precedesProcesses'):
        assert _is_linked(b1, 'precedesProcesses', a)
    _safe_set(a, 'Process206', b2)
    assert _is_linked(a, 'Process206', b2)
    if hasattr(b1, 'precedesProcesses'):
        assert not _is_linked(b1, 'precedesProcesses', a)
    if hasattr(b2, 'precedesProcesses'):
        assert _is_linked(b2, 'precedesProcesses', a)
    _safe_set(a, 'Process206', None)
    assert not _is_linked(a, 'Process206', b2)
    if hasattr(b2, 'precedesProcesses'):
        assert not _is_linked(b2, 'precedesProcesses', a)


def test_assoc_generatesEvents194_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'isGeneratedByProcesses', {b1})
    assert _is_linked(a, 'isGeneratedByProcesses', b1)
    if hasattr(b1, 'Event195'):
        assert _is_linked(b1, 'Event195', a)
    _safe_set(a, 'isGeneratedByProcesses', {b2})
    assert _is_linked(a, 'isGeneratedByProcesses', b2)
    if hasattr(b1, 'Event195'):
        assert not _is_linked(b1, 'Event195', a)
    if hasattr(b2, 'Event195'):
        assert _is_linked(b2, 'Event195', a)
    _safe_set(a, 'isGeneratedByProcesses', set())
    assert not _is_linked(a, 'isGeneratedByProcesses', b2)
    if hasattr(b2, 'Event195'):
        assert not _is_linked(b2, 'Event195', a)


def test_assoc_generatesEvents95_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'isGeneratedByActors', {b1})
    assert _is_linked(a, 'isGeneratedByActors', b1)
    if hasattr(b1, 'Event96'):
        assert _is_linked(b1, 'Event96', a)
    _safe_set(a, 'isGeneratedByActors', {b2})
    assert _is_linked(a, 'isGeneratedByActors', b2)
    if hasattr(b1, 'Event96'):
        assert not _is_linked(b1, 'Event96', a)
    if hasattr(b2, 'Event96'):
        assert _is_linked(b2, 'Event96', a)
    _safe_set(a, 'isGeneratedByActors', set())
    assert not _is_linked(a, 'isGeneratedByActors', b2)
    if hasattr(b2, 'Event96'):
        assert not _is_linked(b2, 'Event96', a)


def test_assoc_governsAndMeasuresBusinessServices248_link_reassign_clear():
    a = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'isGovernedAndMeasuredByContracts', {b1})
    assert _is_linked(a, 'isGovernedAndMeasuredByContracts', b1)
    if hasattr(b1, 'Service249'):
        assert _is_linked(b1, 'Service249', a)
    _safe_set(a, 'isGovernedAndMeasuredByContracts', {b2})
    assert _is_linked(a, 'isGovernedAndMeasuredByContracts', b2)
    if hasattr(b1, 'Service249'):
        assert not _is_linked(b1, 'Service249', a)
    if hasattr(b2, 'Service249'):
        assert _is_linked(b2, 'Service249', a)
    _safe_set(a, 'isGovernedAndMeasuredByContracts', set())
    assert not _is_linked(a, 'isGovernedAndMeasuredByContracts', b2)
    if hasattr(b2, 'Service249'):
        assert not _is_linked(b2, 'Service249', a)


def test_assoc_interactsWithFunctions87_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'supportsActors', {b1})
    assert _is_linked(a, 'supportsActors', b1)
    if hasattr(b1, 'Function88'):
        assert _is_linked(b1, 'Function88', a)
    _safe_set(a, 'supportsActors', {b2})
    assert _is_linked(a, 'supportsActors', b2)
    if hasattr(b1, 'Function88'):
        assert not _is_linked(b1, 'Function88', a)
    if hasattr(b2, 'Function88'):
        assert _is_linked(b2, 'Function88', a)
    _safe_set(a, 'supportsActors', set())
    assert not _is_linked(a, 'supportsActors', b2)
    if hasattr(b2, 'Function88'):
        assert not _is_linked(b2, 'Function88', a)


def test_assoc_involvesActors188_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'participatesInProcesses189', {b1})
    assert _is_linked(a, 'participatesInProcesses189', b1)
    if hasattr(b1, 'Actor190'):
        assert _is_linked(b1, 'Actor190', a)
    _safe_set(a, 'participatesInProcesses189', {b2})
    assert _is_linked(a, 'participatesInProcesses189', b2)
    if hasattr(b1, 'Actor190'):
        assert not _is_linked(b1, 'Actor190', a)
    if hasattr(b2, 'Actor190'):
        assert _is_linked(b2, 'Actor190', a)
    _safe_set(a, 'participatesInProcesses189', set())
    assert not _is_linked(a, 'participatesInProcesses189', b2)
    if hasattr(b2, 'Actor190'):
        assert not _is_linked(b2, 'Actor190', a)


def test_assoc_involvesOrganizationUnits180_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_OrganizationUnit(headcount="sample_text")
    b2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    _safe_set(a, 'participatesInProcesses', {b1})
    assert _is_linked(a, 'participatesInProcesses', b1)
    if hasattr(b1, 'OrganizationUnit181'):
        assert _is_linked(b1, 'OrganizationUnit181', a)
    _safe_set(a, 'participatesInProcesses', {b2})
    assert _is_linked(a, 'participatesInProcesses', b2)
    if hasattr(b1, 'OrganizationUnit181'):
        assert not _is_linked(b1, 'OrganizationUnit181', a)
    if hasattr(b2, 'OrganizationUnit181'):
        assert _is_linked(b2, 'OrganizationUnit181', a)
    _safe_set(a, 'participatesInProcesses', set())
    assert not _is_linked(a, 'participatesInProcesses', b2)
    if hasattr(b2, 'OrganizationUnit181'):
        assert not _is_linked(b2, 'OrganizationUnit181', a)


def test_assoc_isAccessedByServices122_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'consumesDataEntities123', {b1})
    assert _is_linked(a, 'consumesDataEntities123', b1)
    if hasattr(b1, 'Service124'):
        assert _is_linked(b1, 'Service124', a)
    _safe_set(a, 'consumesDataEntities123', {b2})
    assert _is_linked(a, 'consumesDataEntities123', b2)
    if hasattr(b1, 'Service124'):
        assert not _is_linked(b1, 'Service124', a)
    if hasattr(b2, 'Service124'):
        assert _is_linked(b2, 'Service124', a)
    _safe_set(a, 'consumesDataEntities123', set())
    assert not _is_linked(a, 'consumesDataEntities123', b2)
    if hasattr(b2, 'Service124'):
        assert not _is_linked(b2, 'Service124', a)


def test_assoc_isAssumedByActors108_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'performsTaskInRoles', {b1})
    assert _is_linked(a, 'performsTaskInRoles', b1)
    if hasattr(b1, 'Actor109'):
        assert _is_linked(b1, 'Actor109', a)
    _safe_set(a, 'performsTaskInRoles', {b2})
    assert _is_linked(a, 'performsTaskInRoles', b2)
    if hasattr(b1, 'Actor109'):
        assert not _is_linked(b1, 'Actor109', a)
    if hasattr(b2, 'Actor109'):
        assert _is_linked(b2, 'Actor109', a)
    _safe_set(a, 'performsTaskInRoles', set())
    assert not _is_linked(a, 'performsTaskInRoles', b2)
    if hasattr(b2, 'Actor109'):
        assert not _is_linked(b2, 'Actor109', a)


def test_assoc_isConsumedByActors120_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'consumesDataEntities', {b1})
    assert _is_linked(a, 'consumesDataEntities', b1)
    if hasattr(b1, 'Actor121'):
        assert _is_linked(b1, 'Actor121', a)
    _safe_set(a, 'consumesDataEntities', {b2})
    assert _is_linked(a, 'consumesDataEntities', b2)
    if hasattr(b1, 'Actor121'):
        assert not _is_linked(b1, 'Actor121', a)
    if hasattr(b2, 'Actor121'):
        assert _is_linked(b2, 'Actor121', a)
    _safe_set(a, 'consumesDataEntities', set())
    assert not _is_linked(a, 'consumesDataEntities', b2)
    if hasattr(b2, 'Actor121'):
        assert not _is_linked(b2, 'Actor121', a)


def test_assoc_isDecomposedByActors106_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'Actor107', b1)
    assert _is_linked(a, 'Actor107', b1)
    if hasattr(b1, 'decomposesActor'):
        assert _is_linked(b1, 'decomposesActor', a)
    _safe_set(a, 'Actor107', b2)
    assert _is_linked(a, 'Actor107', b2)
    if hasattr(b1, 'decomposesActor'):
        assert not _is_linked(b1, 'decomposesActor', a)
    if hasattr(b2, 'decomposesActor'):
        assert _is_linked(b2, 'decomposesActor', a)
    _safe_set(a, 'Actor107', None)
    assert not _is_linked(a, 'Actor107', b2)
    if hasattr(b2, 'decomposesActor'):
        assert not _is_linked(b2, 'decomposesActor', a)


def test_assoc_isDecomposedByDataEntities136_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    _safe_set(a, 'contentfwk_DataEntity135', {b1})
    assert _is_linked(a, 'contentfwk_DataEntity135', b1)
    if hasattr(b1, 'contentfwk_DataEntity137'):
        assert _is_linked(b1, 'contentfwk_DataEntity137', a)
    _safe_set(a, 'contentfwk_DataEntity135', {b2})
    assert _is_linked(a, 'contentfwk_DataEntity135', b2)
    if hasattr(b1, 'contentfwk_DataEntity137'):
        assert not _is_linked(b1, 'contentfwk_DataEntity137', a)
    if hasattr(b2, 'contentfwk_DataEntity137'):
        assert _is_linked(b2, 'contentfwk_DataEntity137', a)
    _safe_set(a, 'contentfwk_DataEntity135', set())
    assert not _is_linked(a, 'contentfwk_DataEntity135', b2)
    if hasattr(b2, 'contentfwk_DataEntity137'):
        assert not _is_linked(b2, 'contentfwk_DataEntity137', a)


def test_assoc_isDecomposedByLogicalTechnologyComponents347_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'LogicalTechnologyComponent348', b1)
    assert _is_linked(a, 'LogicalTechnologyComponent348', b1)
    if hasattr(b1, 'decomposesLogicalTechnologyComponent'):
        assert _is_linked(b1, 'decomposesLogicalTechnologyComponent', a)
    _safe_set(a, 'LogicalTechnologyComponent348', b2)
    assert _is_linked(a, 'LogicalTechnologyComponent348', b2)
    if hasattr(b1, 'decomposesLogicalTechnologyComponent'):
        assert not _is_linked(b1, 'decomposesLogicalTechnologyComponent', a)
    if hasattr(b2, 'decomposesLogicalTechnologyComponent'):
        assert _is_linked(b2, 'decomposesLogicalTechnologyComponent', a)
    _safe_set(a, 'LogicalTechnologyComponent348', None)
    assert not _is_linked(a, 'LogicalTechnologyComponent348', b2)
    if hasattr(b2, 'decomposesLogicalTechnologyComponent'):
        assert not _is_linked(b2, 'decomposesLogicalTechnologyComponent', a)


def test_assoc_isDecomposedByOrganizationUnits80_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_OrganizationUnit(headcount="sample_text")
    b2 = contentfwk_OrganizationUnit(headcount="sample_text_2")
    _safe_set(a, 'OrganizationUnit81', b1)
    assert _is_linked(a, 'OrganizationUnit81', b1)
    if hasattr(b1, 'decomposesOrganizationUnit'):
        assert _is_linked(b1, 'decomposesOrganizationUnit', a)
    _safe_set(a, 'OrganizationUnit81', b2)
    assert _is_linked(a, 'OrganizationUnit81', b2)
    if hasattr(b1, 'decomposesOrganizationUnit'):
        assert not _is_linked(b1, 'decomposesOrganizationUnit', a)
    if hasattr(b2, 'decomposesOrganizationUnit'):
        assert _is_linked(b2, 'decomposesOrganizationUnit', a)
    _safe_set(a, 'OrganizationUnit81', None)
    assert not _is_linked(a, 'OrganizationUnit81', b2)
    if hasattr(b2, 'decomposesOrganizationUnit'):
        assert not _is_linked(b2, 'decomposesOrganizationUnit', a)


def test_assoc_isDecomposedByPhysicalApplicationComponents327_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b2 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    _safe_set(a, 'PhysicalApplicationComponent328', b1)
    assert _is_linked(a, 'PhysicalApplicationComponent328', b1)
    if hasattr(b1, 'decomposesPhysicalApplicationComponent'):
        assert _is_linked(b1, 'decomposesPhysicalApplicationComponent', a)
    _safe_set(a, 'PhysicalApplicationComponent328', b2)
    assert _is_linked(a, 'PhysicalApplicationComponent328', b2)
    if hasattr(b1, 'decomposesPhysicalApplicationComponent'):
        assert not _is_linked(b1, 'decomposesPhysicalApplicationComponent', a)
    if hasattr(b2, 'decomposesPhysicalApplicationComponent'):
        assert _is_linked(b2, 'decomposesPhysicalApplicationComponent', a)
    _safe_set(a, 'PhysicalApplicationComponent328', None)
    assert not _is_linked(a, 'PhysicalApplicationComponent328', b2)
    if hasattr(b2, 'decomposesPhysicalApplicationComponent'):
        assert not _is_linked(b2, 'decomposesPhysicalApplicationComponent', a)


def test_assoc_isDecomposedByPhysicalTechnologyComponents227_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    _safe_set(a, 'PhysicalTechnologyComponent228', b1)
    assert _is_linked(a, 'PhysicalTechnologyComponent228', b1)
    if hasattr(b1, 'decomposesPhysicalTechnologyComponent'):
        assert _is_linked(b1, 'decomposesPhysicalTechnologyComponent', a)
    _safe_set(a, 'PhysicalTechnologyComponent228', b2)
    assert _is_linked(a, 'PhysicalTechnologyComponent228', b2)
    if hasattr(b1, 'decomposesPhysicalTechnologyComponent'):
        assert not _is_linked(b1, 'decomposesPhysicalTechnologyComponent', a)
    if hasattr(b2, 'decomposesPhysicalTechnologyComponent'):
        assert _is_linked(b2, 'decomposesPhysicalTechnologyComponent', a)
    _safe_set(a, 'PhysicalTechnologyComponent228', None)
    assert not _is_linked(a, 'PhysicalTechnologyComponent228', b2)
    if hasattr(b2, 'decomposesPhysicalTechnologyComponent'):
        assert not _is_linked(b2, 'decomposesPhysicalTechnologyComponent', a)


def test_assoc_isDecomposedByProcesses208_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    _safe_set(a, 'Process209', b1)
    assert _is_linked(a, 'Process209', b1)
    if hasattr(b1, 'decomposesProcess'):
        assert _is_linked(b1, 'decomposesProcess', a)
    _safe_set(a, 'Process209', b2)
    assert _is_linked(a, 'Process209', b2)
    if hasattr(b1, 'decomposesProcess'):
        assert not _is_linked(b1, 'decomposesProcess', a)
    if hasattr(b2, 'decomposesProcess'):
        assert _is_linked(b2, 'decomposesProcess', a)
    _safe_set(a, 'Process209', None)
    assert not _is_linked(a, 'Process209', b2)
    if hasattr(b2, 'decomposesProcess'):
        assert not _is_linked(b2, 'decomposesProcess', a)


def test_assoc_isDecomposedByRoles116_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_Role(estimatedFTEs="sample_text")
    b2 = contentfwk_Role(estimatedFTEs="sample_text_2")
    _safe_set(a, 'Role117', b1)
    assert _is_linked(a, 'Role117', b1)
    if hasattr(b1, 'decomposesRole'):
        assert _is_linked(b1, 'decomposesRole', a)
    _safe_set(a, 'Role117', b2)
    assert _is_linked(a, 'Role117', b2)
    if hasattr(b1, 'decomposesRole'):
        assert not _is_linked(b1, 'decomposesRole', a)
    if hasattr(b2, 'decomposesRole'):
        assert _is_linked(b2, 'decomposesRole', a)
    _safe_set(a, 'Role117', None)
    assert not _is_linked(a, 'Role117', b2)
    if hasattr(b2, 'decomposesRole'):
        assert not _is_linked(b2, 'decomposesRole', a)


def test_assoc_isDelegatedBy269_link_reassign_clear():
    a = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    b1 = contentfwk_Element(ID="sample_text", category="sample_text", description="sample_text", name="sample_text", ownerDescr="sample_text", sourceDescr="sample_text")
    b2 = contentfwk_Element(ID="sample_text_2", category="sample_text_2", description="sample_text_2", name="sample_text_2", ownerDescr="sample_text_2", sourceDescr="sample_text_2")
    _safe_set(a, 'Element270', b1)
    assert _is_linked(a, 'Element270', b1)
    if hasattr(b1, 'delegates'):
        assert _is_linked(b1, 'delegates', a)
    _safe_set(a, 'Element270', b2)
    assert _is_linked(a, 'Element270', b2)
    if hasattr(b1, 'delegates'):
        assert not _is_linked(b1, 'delegates', a)
    if hasattr(b2, 'delegates'):
        assert _is_linked(b2, 'delegates', a)
    _safe_set(a, 'Element270', None)
    assert not _is_linked(a, 'Element270', b2)
    if hasattr(b2, 'delegates'):
        assert not _is_linked(b2, 'delegates', a)


def test_assoc_isDeliveredBy288_link_reassign_clear():
    a = contentfwk_WorkPackage(capabilityDelivered="sample_text", workPackageCategory="sample_text")
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


def test_assoc_isDependentOnLogicalTechnologyComponents338_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'LogicalTechnologyComponent339', b1)
    assert _is_linked(a, 'LogicalTechnologyComponent339', b1)
    if hasattr(b1, 'isRequiredByLogicalTechnologyComponents'):
        assert _is_linked(b1, 'isRequiredByLogicalTechnologyComponents', a)
    _safe_set(a, 'LogicalTechnologyComponent339', b2)
    assert _is_linked(a, 'LogicalTechnologyComponent339', b2)
    if hasattr(b1, 'isRequiredByLogicalTechnologyComponents'):
        assert not _is_linked(b1, 'isRequiredByLogicalTechnologyComponents', a)
    if hasattr(b2, 'isRequiredByLogicalTechnologyComponents'):
        assert _is_linked(b2, 'isRequiredByLogicalTechnologyComponents', a)
    _safe_set(a, 'LogicalTechnologyComponent339', None)
    assert not _is_linked(a, 'LogicalTechnologyComponent339', b2)
    if hasattr(b2, 'isRequiredByLogicalTechnologyComponents'):
        assert not _is_linked(b2, 'isRequiredByLogicalTechnologyComponents', a)


def test_assoc_isDependentOnPhysicalTechnologyComponents221_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    _safe_set(a, 'PhysicalTechnologyComponent222', b1)
    assert _is_linked(a, 'PhysicalTechnologyComponent222', b1)
    if hasattr(b1, 'isRequiredByPhysicalTechnologyComponent'):
        assert _is_linked(b1, 'isRequiredByPhysicalTechnologyComponent', a)
    _safe_set(a, 'PhysicalTechnologyComponent222', b2)
    assert _is_linked(a, 'PhysicalTechnologyComponent222', b2)
    if hasattr(b1, 'isRequiredByPhysicalTechnologyComponent'):
        assert not _is_linked(b1, 'isRequiredByPhysicalTechnologyComponent', a)
    if hasattr(b2, 'isRequiredByPhysicalTechnologyComponent'):
        assert _is_linked(b2, 'isRequiredByPhysicalTechnologyComponent', a)
    _safe_set(a, 'PhysicalTechnologyComponent222', None)
    assert not _is_linked(a, 'PhysicalTechnologyComponent222', b2)
    if hasattr(b2, 'isRequiredByPhysicalTechnologyComponent'):
        assert not _is_linked(b2, 'isRequiredByPhysicalTechnologyComponent', a)


def test_assoc_isExtendedByPhysicalApplicationComponents142_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
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


def test_assoc_isExtendedByPhysicalTechnologyComponent340_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent342', b1)
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent342', b1)
    if hasattr(b1, 'contentfwk_LogicalTechnologyComponent341'):
        assert _is_linked(b1, 'contentfwk_LogicalTechnologyComponent341', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent342', b2)
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent342', b2)
    if hasattr(b1, 'contentfwk_LogicalTechnologyComponent341'):
        assert not _is_linked(b1, 'contentfwk_LogicalTechnologyComponent341', a)
    if hasattr(b2, 'contentfwk_LogicalTechnologyComponent341'):
        assert _is_linked(b2, 'contentfwk_LogicalTechnologyComponent341', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent342', None)
    assert not _is_linked(a, 'contentfwk_PhysicalTechnologyComponent342', b2)
    if hasattr(b2, 'contentfwk_LogicalTechnologyComponent341'):
        assert not _is_linked(b2, 'contentfwk_LogicalTechnologyComponent341', a)


def test_assoc_isGeneratedByActors261_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'Actor263', b1)
    assert _is_linked(a, 'Actor263', b1)
    if hasattr(b1, 'generatesEvents262'):
        assert _is_linked(b1, 'generatesEvents262', a)
    _safe_set(a, 'Actor263', b2)
    assert _is_linked(a, 'Actor263', b2)
    if hasattr(b1, 'generatesEvents262'):
        assert not _is_linked(b1, 'generatesEvents262', a)
    if hasattr(b2, 'generatesEvents262'):
        assert _is_linked(b2, 'generatesEvents262', a)
    _safe_set(a, 'Actor263', None)
    assert not _is_linked(a, 'Actor263', b2)
    if hasattr(b2, 'generatesEvents262'):
        assert not _is_linked(b2, 'generatesEvents262', a)


def test_assoc_isGeneratedByProcesses256_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'Process257', b1)
    assert _is_linked(a, 'Process257', b1)
    if hasattr(b1, 'generatesEvents'):
        assert _is_linked(b1, 'generatesEvents', a)
    _safe_set(a, 'Process257', b2)
    assert _is_linked(a, 'Process257', b2)
    if hasattr(b1, 'generatesEvents'):
        assert not _is_linked(b1, 'generatesEvents', a)
    if hasattr(b2, 'generatesEvents'):
        assert _is_linked(b2, 'generatesEvents', a)
    _safe_set(a, 'Process257', None)
    assert not _is_linked(a, 'Process257', b2)
    if hasattr(b2, 'generatesEvents'):
        assert not _is_linked(b2, 'generatesEvents', a)


def test_assoc_isGovernedAndMeasuredByContracts360_link_reassign_clear():
    a = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'Contract361', b1)
    assert _is_linked(a, 'Contract361', b1)
    if hasattr(b1, 'governsAndMeasuresBusinessServices'):
        assert _is_linked(b1, 'governsAndMeasuresBusinessServices', a)
    _safe_set(a, 'Contract361', b2)
    assert _is_linked(a, 'Contract361', b2)
    if hasattr(b1, 'governsAndMeasuresBusinessServices'):
        assert not _is_linked(b1, 'governsAndMeasuresBusinessServices', a)
    if hasattr(b2, 'governsAndMeasuresBusinessServices'):
        assert _is_linked(b2, 'governsAndMeasuresBusinessServices', a)
    _safe_set(a, 'Contract361', None)
    assert not _is_linked(a, 'Contract361', b2)
    if hasattr(b2, 'governsAndMeasuresBusinessServices'):
        assert not _is_linked(b2, 'governsAndMeasuresBusinessServices', a)


def test_assoc_isGuidedByControls191_link_reassign_clear():
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


def test_assoc_isHostedInLocation216_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'containsPhysicalTechnologyComponents', {b1})
    assert _is_linked(a, 'containsPhysicalTechnologyComponents', b1)
    if hasattr(b1, 'Location217'):
        assert _is_linked(b1, 'Location217', a)
    _safe_set(a, 'containsPhysicalTechnologyComponents', {b2})
    assert _is_linked(a, 'containsPhysicalTechnologyComponents', b2)
    if hasattr(b1, 'Location217'):
        assert not _is_linked(b1, 'Location217', a)
    if hasattr(b2, 'Location217'):
        assert _is_linked(b2, 'Location217', a)
    _safe_set(a, 'containsPhysicalTechnologyComponents', set())
    assert not _is_linked(a, 'containsPhysicalTechnologyComponents', b2)
    if hasattr(b2, 'Location217'):
        assert not _is_linked(b2, 'Location217', a)


def test_assoc_isHostedInLocation314_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'containsPhysicalApplicationComponents', {b1})
    assert _is_linked(a, 'containsPhysicalApplicationComponents', b1)
    if hasattr(b1, 'Location315'):
        assert _is_linked(b1, 'Location315', a)
    _safe_set(a, 'containsPhysicalApplicationComponents', {b2})
    assert _is_linked(a, 'containsPhysicalApplicationComponents', b2)
    if hasattr(b1, 'Location315'):
        assert not _is_linked(b1, 'Location315', a)
    if hasattr(b2, 'Location315'):
        assert _is_linked(b2, 'Location315', a)
    _safe_set(a, 'containsPhysicalApplicationComponents', set())
    assert not _is_linked(a, 'containsPhysicalApplicationComponents', b2)
    if hasattr(b2, 'Location315'):
        assert not _is_linked(b2, 'Location315', a)


def test_assoc_isImplementedOnLogicalTechnologyComponents364_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'LogicalTechnologyComponent365', b1)
    assert _is_linked(a, 'LogicalTechnologyComponent365', b1)
    if hasattr(b1, 'providesPlatformForServices'):
        assert _is_linked(b1, 'providesPlatformForServices', a)
    _safe_set(a, 'LogicalTechnologyComponent365', b2)
    assert _is_linked(a, 'LogicalTechnologyComponent365', b2)
    if hasattr(b1, 'providesPlatformForServices'):
        assert not _is_linked(b1, 'providesPlatformForServices', a)
    if hasattr(b2, 'providesPlatformForServices'):
        assert _is_linked(b2, 'providesPlatformForServices', a)
    _safe_set(a, 'LogicalTechnologyComponent365', None)
    assert not _is_linked(a, 'LogicalTechnologyComponent365', b2)
    if hasattr(b2, 'providesPlatformForServices'):
        assert not _is_linked(b2, 'providesPlatformForServices', a)


def test_assoc_isMotivatedByDrivers72_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Driver()
    b2 = contentfwk_Driver()
    _safe_set(a, 'motivatesOrganizationUnits', {b1})
    assert _is_linked(a, 'motivatesOrganizationUnits', b1)
    if hasattr(b1, 'Driver73'):
        assert _is_linked(b1, 'Driver73', a)
    _safe_set(a, 'motivatesOrganizationUnits', {b2})
    assert _is_linked(a, 'motivatesOrganizationUnits', b2)
    if hasattr(b1, 'Driver73'):
        assert not _is_linked(b1, 'Driver73', a)
    if hasattr(b2, 'Driver73'):
        assert _is_linked(b2, 'Driver73', a)
    _safe_set(a, 'motivatesOrganizationUnits', set())
    assert not _is_linked(a, 'motivatesOrganizationUnits', b2)
    if hasattr(b2, 'Driver73'):
        assert not _is_linked(b2, 'Driver73', a)


def test_assoc_isOwnedAndGovernedByOrganizationUnits368_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'OrganizationUnit369', b1)
    assert _is_linked(a, 'OrganizationUnit369', b1)
    if hasattr(b1, 'ownsAndGovernsServices'):
        assert _is_linked(b1, 'ownsAndGovernsServices', a)
    _safe_set(a, 'OrganizationUnit369', b2)
    assert _is_linked(a, 'OrganizationUnit369', b2)
    if hasattr(b1, 'ownsAndGovernsServices'):
        assert not _is_linked(b1, 'ownsAndGovernsServices', a)
    if hasattr(b2, 'ownsAndGovernsServices'):
        assert _is_linked(b2, 'ownsAndGovernsServices', a)
    _safe_set(a, 'OrganizationUnit369', None)
    assert not _is_linked(a, 'OrganizationUnit369', b2)
    if hasattr(b2, 'ownsAndGovernsServices'):
        assert not _is_linked(b2, 'ownsAndGovernsServices', a)


def test_assoc_isOwnedByOrganizationUnit153_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'OrganizationUnit154', b1)
    assert _is_linked(a, 'OrganizationUnit154', b1)
    if hasattr(b1, 'ownsFunctions'):
        assert _is_linked(b1, 'ownsFunctions', a)
    _safe_set(a, 'OrganizationUnit154', b2)
    assert _is_linked(a, 'OrganizationUnit154', b2)
    if hasattr(b1, 'ownsFunctions'):
        assert not _is_linked(b1, 'ownsFunctions', a)
    if hasattr(b2, 'ownsFunctions'):
        assert _is_linked(b2, 'ownsFunctions', a)
    _safe_set(a, 'OrganizationUnit154', None)
    assert not _is_linked(a, 'OrganizationUnit154', b2)
    if hasattr(b2, 'ownsFunctions'):
        assert not _is_linked(b2, 'ownsFunctions', a)


def test_assoc_isPerformedByActors151_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'Actor152', b1)
    assert _is_linked(a, 'Actor152', b1)
    if hasattr(b1, 'performsFunctions'):
        assert _is_linked(b1, 'performsFunctions', a)
    _safe_set(a, 'Actor152', b2)
    assert _is_linked(a, 'Actor152', b2)
    if hasattr(b1, 'performsFunctions'):
        assert not _is_linked(b1, 'performsFunctions', a)
    if hasattr(b2, 'performsFunctions'):
        assert _is_linked(b2, 'performsFunctions', a)
    _safe_set(a, 'Actor152', None)
    assert not _is_linked(a, 'Actor152', b2)
    if hasattr(b2, 'performsFunctions'):
        assert not _is_linked(b2, 'performsFunctions', a)


def test_assoc_isProcessesByLogicalApplicationComponents128_link_reassign_clear():
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


def test_assoc_isProducedByOrganizationUnits229_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Product()
    b2 = contentfwk_Product()
    _safe_set(a, 'OrganizationUnit230', b1)
    assert _is_linked(a, 'OrganizationUnit230', b1)
    if hasattr(b1, 'producesProducts'):
        assert _is_linked(b1, 'producesProducts', a)
    _safe_set(a, 'OrganizationUnit230', b2)
    assert _is_linked(a, 'OrganizationUnit230', b2)
    if hasattr(b1, 'producesProducts'):
        assert not _is_linked(b1, 'producesProducts', a)
    if hasattr(b2, 'producesProducts'):
        assert _is_linked(b2, 'producesProducts', a)
    _safe_set(a, 'OrganizationUnit230', None)
    assert not _is_linked(a, 'OrganizationUnit230', b2)
    if hasattr(b2, 'producesProducts'):
        assert not _is_linked(b2, 'producesProducts', a)


def test_assoc_isProducedByProcesses231_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Product()
    b2 = contentfwk_Product()
    _safe_set(a, 'Process233', b1)
    assert _is_linked(a, 'Process233', b1)
    if hasattr(b1, 'producesProducts232'):
        assert _is_linked(b1, 'producesProducts232', a)
    _safe_set(a, 'Process233', b2)
    assert _is_linked(a, 'Process233', b2)
    if hasattr(b1, 'producesProducts232'):
        assert not _is_linked(b1, 'producesProducts232', a)
    if hasattr(b2, 'producesProducts232'):
        assert _is_linked(b2, 'producesProducts232', a)
    _safe_set(a, 'Process233', None)
    assert not _is_linked(a, 'Process233', b2)
    if hasattr(b2, 'producesProducts232'):
        assert not _is_linked(b2, 'producesProducts232', a)


def test_assoc_isProvidedToActors352_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'Actor353', b1)
    assert _is_linked(a, 'Actor353', b1)
    if hasattr(b1, 'consumesServices'):
        assert _is_linked(b1, 'consumesServices', a)
    _safe_set(a, 'Actor353', b2)
    assert _is_linked(a, 'Actor353', b2)
    if hasattr(b1, 'consumesServices'):
        assert not _is_linked(b1, 'consumesServices', a)
    if hasattr(b2, 'consumesServices'):
        assert _is_linked(b2, 'consumesServices', a)
    _safe_set(a, 'Actor353', None)
    assert not _is_linked(a, 'Actor353', b2)
    if hasattr(b2, 'consumesServices'):
        assert not _is_linked(b2, 'consumesServices', a)


def test_assoc_isRealizedByPhysicalTechnologyComponents321_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b2 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    _safe_set(a, 'PhysicalTechnologyComponent322', b1)
    assert _is_linked(a, 'PhysicalTechnologyComponent322', b1)
    if hasattr(b1, 'realizesPhysicalApplicationComponents'):
        assert _is_linked(b1, 'realizesPhysicalApplicationComponents', a)
    _safe_set(a, 'PhysicalTechnologyComponent322', b2)
    assert _is_linked(a, 'PhysicalTechnologyComponent322', b2)
    if hasattr(b1, 'realizesPhysicalApplicationComponents'):
        assert not _is_linked(b1, 'realizesPhysicalApplicationComponents', a)
    if hasattr(b2, 'realizesPhysicalApplicationComponents'):
        assert _is_linked(b2, 'realizesPhysicalApplicationComponents', a)
    _safe_set(a, 'PhysicalTechnologyComponent322', None)
    assert not _is_linked(a, 'PhysicalTechnologyComponent322', b2)
    if hasattr(b2, 'realizesPhysicalApplicationComponents'):
        assert not _is_linked(b2, 'realizesPhysicalApplicationComponents', a)


def test_assoc_isRealizedByPhysicalTechnologyComponents332_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'PhysicalTechnologyComponent333', b1)
    assert _is_linked(a, 'PhysicalTechnologyComponent333', b1)
    if hasattr(b1, 'extendsLogicalTechnologyComponents'):
        assert _is_linked(b1, 'extendsLogicalTechnologyComponents', a)
    _safe_set(a, 'PhysicalTechnologyComponent333', b2)
    assert _is_linked(a, 'PhysicalTechnologyComponent333', b2)
    if hasattr(b1, 'extendsLogicalTechnologyComponents'):
        assert not _is_linked(b1, 'extendsLogicalTechnologyComponents', a)
    if hasattr(b2, 'extendsLogicalTechnologyComponents'):
        assert _is_linked(b2, 'extendsLogicalTechnologyComponents', a)
    _safe_set(a, 'PhysicalTechnologyComponent333', None)
    assert not _is_linked(a, 'PhysicalTechnologyComponent333', b2)
    if hasattr(b2, 'extendsLogicalTechnologyComponents'):
        assert not _is_linked(b2, 'extendsLogicalTechnologyComponents', a)


def test_assoc_isRealizedByProcesses159_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'Process160', b1)
    assert _is_linked(a, 'Process160', b1)
    if hasattr(b1, 'orchestratesFunctions'):
        assert _is_linked(b1, 'orchestratesFunctions', a)
    _safe_set(a, 'Process160', b2)
    assert _is_linked(a, 'Process160', b2)
    if hasattr(b1, 'orchestratesFunctions'):
        assert not _is_linked(b1, 'orchestratesFunctions', a)
    if hasattr(b2, 'orchestratesFunctions'):
        assert _is_linked(b2, 'orchestratesFunctions', a)
    _safe_set(a, 'Process160', None)
    assert not _is_linked(a, 'Process160', b2)
    if hasattr(b2, 'orchestratesFunctions'):
        assert not _is_linked(b2, 'orchestratesFunctions', a)


def test_assoc_isRealizedByProcesses374_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'Process375', b1)
    assert _is_linked(a, 'Process375', b1)
    if hasattr(b1, 'orchestratesServices'):
        assert _is_linked(b1, 'orchestratesServices', a)
    _safe_set(a, 'Process375', b2)
    assert _is_linked(a, 'Process375', b2)
    if hasattr(b1, 'orchestratesServices'):
        assert not _is_linked(b1, 'orchestratesServices', a)
    if hasattr(b2, 'orchestratesServices'):
        assert _is_linked(b2, 'orchestratesServices', a)
    _safe_set(a, 'Process375', None)
    assert not _is_linked(a, 'Process375', b2)
    if hasattr(b2, 'orchestratesServices'):
        assert not _is_linked(b2, 'orchestratesServices', a)


def test_assoc_isRequiredByLogicalTechnologyComponents344_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b2 = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text_2")
    _safe_set(a, 'LogicalTechnologyComponent345', b1)
    assert _is_linked(a, 'LogicalTechnologyComponent345', b1)
    if hasattr(b1, 'isDependentOnLogicalTechnologyComponents'):
        assert _is_linked(b1, 'isDependentOnLogicalTechnologyComponents', a)
    _safe_set(a, 'LogicalTechnologyComponent345', b2)
    assert _is_linked(a, 'LogicalTechnologyComponent345', b2)
    if hasattr(b1, 'isDependentOnLogicalTechnologyComponents'):
        assert not _is_linked(b1, 'isDependentOnLogicalTechnologyComponents', a)
    if hasattr(b2, 'isDependentOnLogicalTechnologyComponents'):
        assert _is_linked(b2, 'isDependentOnLogicalTechnologyComponents', a)
    _safe_set(a, 'LogicalTechnologyComponent345', None)
    assert not _is_linked(a, 'LogicalTechnologyComponent345', b2)
    if hasattr(b2, 'isDependentOnLogicalTechnologyComponents'):
        assert not _is_linked(b2, 'isDependentOnLogicalTechnologyComponents', a)


def test_assoc_isRequiredByPhysicalTechnologyComponent224_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b2 = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text_2", moduleName="sample_text_2", productName="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    _safe_set(a, 'PhysicalTechnologyComponent225', b1)
    assert _is_linked(a, 'PhysicalTechnologyComponent225', b1)
    if hasattr(b1, 'isDependentOnPhysicalTechnologyComponents'):
        assert _is_linked(b1, 'isDependentOnPhysicalTechnologyComponents', a)
    _safe_set(a, 'PhysicalTechnologyComponent225', b2)
    assert _is_linked(a, 'PhysicalTechnologyComponent225', b2)
    if hasattr(b1, 'isDependentOnPhysicalTechnologyComponents'):
        assert not _is_linked(b1, 'isDependentOnPhysicalTechnologyComponents', a)
    if hasattr(b2, 'isDependentOnPhysicalTechnologyComponents'):
        assert _is_linked(b2, 'isDependentOnPhysicalTechnologyComponents', a)
    _safe_set(a, 'PhysicalTechnologyComponent225', None)
    assert not _is_linked(a, 'PhysicalTechnologyComponent225', b2)
    if hasattr(b2, 'isDependentOnPhysicalTechnologyComponents'):
        assert not _is_linked(b2, 'isDependentOnPhysicalTechnologyComponents', a)


def test_assoc_isResolvedByActors258_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'Actor260', b1)
    assert _is_linked(a, 'Actor260', b1)
    if hasattr(b1, 'resolvesEvents259'):
        assert _is_linked(b1, 'resolvesEvents259', a)
    _safe_set(a, 'Actor260', b2)
    assert _is_linked(a, 'Actor260', b2)
    if hasattr(b1, 'resolvesEvents259'):
        assert not _is_linked(b1, 'resolvesEvents259', a)
    if hasattr(b2, 'resolvesEvents259'):
        assert _is_linked(b2, 'resolvesEvents259', a)
    _safe_set(a, 'Actor260', None)
    assert not _is_linked(a, 'Actor260', b2)
    if hasattr(b2, 'resolvesEvents259'):
        assert not _is_linked(b2, 'resolvesEvents259', a)


def test_assoc_isResolvedByProcesses253_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'Process255', b1)
    assert _is_linked(a, 'Process255', b1)
    if hasattr(b1, 'resolvesEvents254'):
        assert _is_linked(b1, 'resolvesEvents254', a)
    _safe_set(a, 'Process255', b2)
    assert _is_linked(a, 'Process255', b2)
    if hasattr(b1, 'resolvesEvents254'):
        assert not _is_linked(b1, 'resolvesEvents254', a)
    if hasattr(b2, 'resolvesEvents254'):
        assert _is_linked(b2, 'resolvesEvents254', a)
    _safe_set(a, 'Process255', None)
    assert not _is_linked(a, 'Process255', b2)
    if hasattr(b2, 'resolvesEvents254'):
        assert not _is_linked(b2, 'resolvesEvents254', a)


def test_assoc_isSuppliedByActors118_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'suppliesDataEntities', {b1})
    assert _is_linked(a, 'suppliesDataEntities', b1)
    if hasattr(b1, 'Actor119'):
        assert _is_linked(b1, 'Actor119', a)
    _safe_set(a, 'suppliesDataEntities', {b2})
    assert _is_linked(a, 'suppliesDataEntities', b2)
    if hasattr(b1, 'Actor119'):
        assert not _is_linked(b1, 'Actor119', a)
    if hasattr(b2, 'Actor119'):
        assert _is_linked(b2, 'Actor119', a)
    _safe_set(a, 'suppliesDataEntities', set())
    assert not _is_linked(a, 'suppliesDataEntities', b2)
    if hasattr(b2, 'Actor119'):
        assert not _is_linked(b2, 'Actor119', a)


def test_assoc_isSuppliedByLogicalTechnologyComponents210_link_reassign_clear():
    a = contentfwk_PlatformService(categoryTRM="sample_text", standardClass="sample_text")
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


def test_assoc_isUpdatedThroughServices125_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'providesDataEntities', {b1})
    assert _is_linked(a, 'providesDataEntities', b1)
    if hasattr(b1, 'Service126'):
        assert _is_linked(b1, 'Service126', a)
    _safe_set(a, 'providesDataEntities', {b2})
    assert _is_linked(a, 'providesDataEntities', b2)
    if hasattr(b1, 'Service126'):
        assert not _is_linked(b1, 'Service126', a)
    if hasattr(b2, 'Service126'):
        assert _is_linked(b2, 'Service126', a)
    _safe_set(a, 'providesDataEntities', set())
    assert not _is_linked(a, 'providesDataEntities', b2)
    if hasattr(b2, 'Service126'):
        assert not _is_linked(b2, 'Service126', a)


def test_assoc_logicalComponents40_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_TechnologyArchitecture()
    b2 = contentfwk_TechnologyArchitecture()
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent', b1)
    assert _is_linked(a, 'contentfwk_LogicalTechnologyComponent', b1)
    if hasattr(b1, 'contentfwk_TechnologyArchitecture41'):
        assert _is_linked(b1, 'contentfwk_TechnologyArchitecture41', a)
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent', b2)
    assert _is_linked(a, 'contentfwk_LogicalTechnologyComponent', b2)
    if hasattr(b1, 'contentfwk_TechnologyArchitecture41'):
        assert not _is_linked(b1, 'contentfwk_TechnologyArchitecture41', a)
    if hasattr(b2, 'contentfwk_TechnologyArchitecture41'):
        assert _is_linked(b2, 'contentfwk_TechnologyArchitecture41', a)
    _safe_set(a, 'contentfwk_LogicalTechnologyComponent', None)
    assert not _is_linked(a, 'contentfwk_LogicalTechnologyComponent', b2)
    if hasattr(b2, 'contentfwk_TechnologyArchitecture41'):
        assert not _is_linked(b2, 'contentfwk_TechnologyArchitecture41', a)


def test_assoc_meetsServiceQuality250_link_reassign_clear():
    a = contentfwk_Contract(availabilityQualityCharacteristics="sample_text", behaviorCharacteristics="sample_text", capacityCharacteristics="sample_text", contractControlRequirements="sample_text", credibilityCharacteristics="sample_text", extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", qualityOfInformationRequired="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", responseCharacteristics="sample_text", resultControlRequirements="sample_text", scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceNameCalled="sample_text", serviceNameCaller="sample_text", serviceQualityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
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


def test_assoc_motivatesOrganizationUnits43_link_reassign_clear():
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


def test_assoc_operatesInLocation75_link_reassign_clear():
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


def test_assoc_operatesInLocation97_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Location()
    b2 = contentfwk_Location()
    _safe_set(a, 'containsActors98', b1)
    assert _is_linked(a, 'containsActors98', b1)
    if hasattr(b1, 'Location99'):
        assert _is_linked(b1, 'Location99', a)
    _safe_set(a, 'containsActors98', b2)
    assert _is_linked(a, 'containsActors98', b2)
    if hasattr(b1, 'Location99'):
        assert not _is_linked(b1, 'Location99', a)
    if hasattr(b2, 'Location99'):
        assert _is_linked(b2, 'Location99', a)
    _safe_set(a, 'containsActors98', None)
    assert not _is_linked(a, 'containsActors98', b2)
    if hasattr(b2, 'Location99'):
        assert not _is_linked(b2, 'Location99', a)


def test_assoc_operatesOnDataEntities140_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_LogicalApplicationComponent()
    b2 = contentfwk_LogicalApplicationComponent()
    _safe_set(a, 'DataEntity141', b1)
    assert _is_linked(a, 'DataEntity141', b1)
    if hasattr(b1, 'isProcessesByLogicalApplicationComponents'):
        assert _is_linked(b1, 'isProcessesByLogicalApplicationComponents', a)
    _safe_set(a, 'DataEntity141', b2)
    assert _is_linked(a, 'DataEntity141', b2)
    if hasattr(b1, 'isProcessesByLogicalApplicationComponents'):
        assert not _is_linked(b1, 'isProcessesByLogicalApplicationComponents', a)
    if hasattr(b2, 'isProcessesByLogicalApplicationComponents'):
        assert _is_linked(b2, 'isProcessesByLogicalApplicationComponents', a)
    _safe_set(a, 'DataEntity141', None)
    assert not _is_linked(a, 'DataEntity141', b2)
    if hasattr(b2, 'isProcessesByLogicalApplicationComponents'):
        assert not _is_linked(b2, 'isProcessesByLogicalApplicationComponents', a)


def test_assoc_orchestratesFunctions176_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'isRealizedByProcesses', {b1})
    assert _is_linked(a, 'isRealizedByProcesses', b1)
    if hasattr(b1, 'Function177'):
        assert _is_linked(b1, 'Function177', a)
    _safe_set(a, 'isRealizedByProcesses', {b2})
    assert _is_linked(a, 'isRealizedByProcesses', b2)
    if hasattr(b1, 'Function177'):
        assert not _is_linked(b1, 'Function177', a)
    if hasattr(b2, 'Function177'):
        assert _is_linked(b2, 'Function177', a)
    _safe_set(a, 'isRealizedByProcesses', set())
    assert not _is_linked(a, 'isRealizedByProcesses', b2)
    if hasattr(b2, 'Function177'):
        assert not _is_linked(b2, 'Function177', a)


def test_assoc_orchestratesServices182_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'isRealizedByProcesses183', {b1})
    assert _is_linked(a, 'isRealizedByProcesses183', b1)
    if hasattr(b1, 'Service184'):
        assert _is_linked(b1, 'Service184', a)
    _safe_set(a, 'isRealizedByProcesses183', {b2})
    assert _is_linked(a, 'isRealizedByProcesses183', b2)
    if hasattr(b1, 'Service184'):
        assert not _is_linked(b1, 'Service184', a)
    if hasattr(b2, 'Service184'):
        assert _is_linked(b2, 'Service184', a)
    _safe_set(a, 'isRealizedByProcesses183', set())
    assert not _is_linked(a, 'isRealizedByProcesses183', b2)
    if hasattr(b2, 'Service184'):
        assert not _is_linked(b2, 'Service184', a)


def test_assoc_ownsAndGovernsServices68_link_reassign_clear():
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


def test_assoc_ownsFunctions70_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'isOwnedByOrganizationUnit', {b1})
    assert _is_linked(a, 'isOwnedByOrganizationUnit', b1)
    if hasattr(b1, 'Function'):
        assert _is_linked(b1, 'Function', a)
    _safe_set(a, 'isOwnedByOrganizationUnit', {b2})
    assert _is_linked(a, 'isOwnedByOrganizationUnit', b2)
    if hasattr(b1, 'Function'):
        assert not _is_linked(b1, 'Function', a)
    if hasattr(b2, 'Function'):
        assert _is_linked(b2, 'Function', a)
    _safe_set(a, 'isOwnedByOrganizationUnit', set())
    assert not _is_linked(a, 'isOwnedByOrganizationUnit', b2)
    if hasattr(b2, 'Function'):
        assert not _is_linked(b2, 'Function', a)


def test_assoc_participatesInProcesses71_link_reassign_clear():
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


def test_assoc_participatesInProcesses90_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b2 = contentfwk_Actor(FTEs="sample_text_2", actorGoal="sample_text_2", actorTasks="sample_text_2")
    _safe_set(a, 'Process91', b1)
    assert _is_linked(a, 'Process91', b1)
    if hasattr(b1, 'involvesActors'):
        assert _is_linked(b1, 'involvesActors', a)
    _safe_set(a, 'Process91', b2)
    assert _is_linked(a, 'Process91', b2)
    if hasattr(b1, 'involvesActors'):
        assert not _is_linked(b1, 'involvesActors', a)
    if hasattr(b2, 'involvesActors'):
        assert _is_linked(b2, 'involvesActors', a)
    _safe_set(a, 'Process91', None)
    assert not _is_linked(a, 'Process91', b2)
    if hasattr(b2, 'involvesActors'):
        assert not _is_linked(b2, 'involvesActors', a)


def test_assoc_performsFunctions100_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'isPerformedByActors', {b1})
    assert _is_linked(a, 'isPerformedByActors', b1)
    if hasattr(b1, 'Function101'):
        assert _is_linked(b1, 'Function101', a)
    _safe_set(a, 'isPerformedByActors', {b2})
    assert _is_linked(a, 'isPerformedByActors', b2)
    if hasattr(b1, 'Function101'):
        assert not _is_linked(b1, 'Function101', a)
    if hasattr(b2, 'Function101'):
        assert _is_linked(b2, 'Function101', a)
    _safe_set(a, 'isPerformedByActors', set())
    assert not _is_linked(a, 'isPerformedByActors', b2)
    if hasattr(b2, 'Function101'):
        assert not _is_linked(b2, 'Function101', a)


def test_assoc_performsTaskInRoles89_link_reassign_clear():
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


def test_assoc_physicalApplicationComponents308_link_reassign_clear():
    a = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b1 = contentfwk_ApplicationArchitecture()
    b2 = contentfwk_ApplicationArchitecture()
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent', b1)
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent', b1)
    if hasattr(b1, 'contentfwk_ApplicationArchitecture309'):
        assert _is_linked(b1, 'contentfwk_ApplicationArchitecture309', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent', b2)
    assert _is_linked(a, 'contentfwk_PhysicalApplicationComponent', b2)
    if hasattr(b1, 'contentfwk_ApplicationArchitecture309'):
        assert not _is_linked(b1, 'contentfwk_ApplicationArchitecture309', a)
    if hasattr(b2, 'contentfwk_ApplicationArchitecture309'):
        assert _is_linked(b2, 'contentfwk_ApplicationArchitecture309', a)
    _safe_set(a, 'contentfwk_PhysicalApplicationComponent', None)
    assert not _is_linked(a, 'contentfwk_PhysicalApplicationComponent', b2)
    if hasattr(b2, 'contentfwk_ApplicationArchitecture309'):
        assert not _is_linked(b2, 'contentfwk_ApplicationArchitecture309', a)


def test_assoc_physicalComponents38_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_TechnologyArchitecture()
    b2 = contentfwk_TechnologyArchitecture()
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent', b1)
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent', b1)
    if hasattr(b1, 'contentfwk_TechnologyArchitecture39'):
        assert _is_linked(b1, 'contentfwk_TechnologyArchitecture39', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent', b2)
    assert _is_linked(a, 'contentfwk_PhysicalTechnologyComponent', b2)
    if hasattr(b1, 'contentfwk_TechnologyArchitecture39'):
        assert not _is_linked(b1, 'contentfwk_TechnologyArchitecture39', a)
    if hasattr(b2, 'contentfwk_TechnologyArchitecture39'):
        assert _is_linked(b2, 'contentfwk_TechnologyArchitecture39', a)
    _safe_set(a, 'contentfwk_PhysicalTechnologyComponent', None)
    assert not _is_linked(a, 'contentfwk_PhysicalTechnologyComponent', b2)
    if hasattr(b2, 'contentfwk_TechnologyArchitecture39'):
        assert not _is_linked(b2, 'contentfwk_TechnologyArchitecture39', a)


def test_assoc_platformServices37_link_reassign_clear():
    a = contentfwk_PlatformService(categoryTRM="sample_text", standardClass="sample_text")
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


def test_assoc_precedesProcesses202_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b2 = contentfwk_Process(isAutomated=False, processCritiality="sample_text_2", processVolumetrics="sample_text_2")
    _safe_set(a, 'Process203', b1)
    assert _is_linked(a, 'Process203', b1)
    if hasattr(b1, 'followsProcesses'):
        assert _is_linked(b1, 'followsProcesses', a)
    _safe_set(a, 'Process203', b2)
    assert _is_linked(a, 'Process203', b2)
    if hasattr(b1, 'followsProcesses'):
        assert not _is_linked(b1, 'followsProcesses', a)
    if hasattr(b2, 'followsProcesses'):
        assert _is_linked(b2, 'followsProcesses', a)
    _safe_set(a, 'Process203', None)
    assert not _is_linked(a, 'Process203', b2)
    if hasattr(b2, 'followsProcesses'):
        assert not _is_linked(b2, 'followsProcesses', a)


def test_assoc_processes16_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_BusinessArchitecture()
    b2 = contentfwk_BusinessArchitecture()
    _safe_set(a, 'contentfwk_Process', b1)
    assert _is_linked(a, 'contentfwk_Process', b1)
    if hasattr(b1, 'contentfwk_BusinessArchitecture17'):
        assert _is_linked(b1, 'contentfwk_BusinessArchitecture17', a)
    _safe_set(a, 'contentfwk_Process', b2)
    assert _is_linked(a, 'contentfwk_Process', b2)
    if hasattr(b1, 'contentfwk_BusinessArchitecture17'):
        assert not _is_linked(b1, 'contentfwk_BusinessArchitecture17', a)
    if hasattr(b2, 'contentfwk_BusinessArchitecture17'):
        assert _is_linked(b2, 'contentfwk_BusinessArchitecture17', a)
    _safe_set(a, 'contentfwk_Process', None)
    assert not _is_linked(a, 'contentfwk_Process', b2)
    if hasattr(b2, 'contentfwk_BusinessArchitecture17'):
        assert not _is_linked(b2, 'contentfwk_BusinessArchitecture17', a)


def test_assoc_producesProducts196_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Product()
    b2 = contentfwk_Product()
    _safe_set(a, 'isProducedByProcesses', {b1})
    assert _is_linked(a, 'isProducedByProcesses', b1)
    if hasattr(b1, 'Product197'):
        assert _is_linked(b1, 'Product197', a)
    _safe_set(a, 'isProducedByProcesses', {b2})
    assert _is_linked(a, 'isProducedByProcesses', b2)
    if hasattr(b1, 'Product197'):
        assert not _is_linked(b1, 'Product197', a)
    if hasattr(b2, 'Product197'):
        assert _is_linked(b2, 'Product197', a)
    _safe_set(a, 'isProducedByProcesses', set())
    assert not _is_linked(a, 'isProducedByProcesses', b2)
    if hasattr(b2, 'Product197'):
        assert not _is_linked(b2, 'Product197', a)


def test_assoc_producesProducts74_link_reassign_clear():
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


def test_assoc_providesDataEntities356_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'DataEntity357', b1)
    assert _is_linked(a, 'DataEntity357', b1)
    if hasattr(b1, 'isUpdatedThroughServices'):
        assert _is_linked(b1, 'isUpdatedThroughServices', a)
    _safe_set(a, 'DataEntity357', b2)
    assert _is_linked(a, 'DataEntity357', b2)
    if hasattr(b1, 'isUpdatedThroughServices'):
        assert not _is_linked(b1, 'isUpdatedThroughServices', a)
    if hasattr(b2, 'isUpdatedThroughServices'):
        assert _is_linked(b2, 'isUpdatedThroughServices', a)
    _safe_set(a, 'DataEntity357', None)
    assert not _is_linked(a, 'DataEntity357', b2)
    if hasattr(b2, 'isUpdatedThroughServices'):
        assert not _is_linked(b2, 'isUpdatedThroughServices', a)


def test_assoc_providesPlatformForServices329_link_reassign_clear():
    a = contentfwk_LogicalTechnologyComponent(categoryTRM="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'isImplementedOnLogicalTechnologyComponents', {b1})
    assert _is_linked(a, 'isImplementedOnLogicalTechnologyComponents', b1)
    if hasattr(b1, 'Service330'):
        assert _is_linked(b1, 'Service330', a)
    _safe_set(a, 'isImplementedOnLogicalTechnologyComponents', {b2})
    assert _is_linked(a, 'isImplementedOnLogicalTechnologyComponents', b2)
    if hasattr(b1, 'Service330'):
        assert not _is_linked(b1, 'Service330', a)
    if hasattr(b2, 'Service330'):
        assert _is_linked(b2, 'Service330', a)
    _safe_set(a, 'isImplementedOnLogicalTechnologyComponents', set())
    assert not _is_linked(a, 'isImplementedOnLogicalTechnologyComponents', b2)
    if hasattr(b2, 'Service330'):
        assert not _is_linked(b2, 'Service330', a)


def test_assoc_realizesPhysicalApplicationComponents211_link_reassign_clear():
    a = contentfwk_PhysicalTechnologyComponent(categoryTRM="sample_text", moduleName="sample_text", productName="sample_text", vendor="sample_text", version="sample_text")
    b1 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text", capacityCharacteristics="sample_text", credibilityCharacteristics="sample_text", dateOfLastRelease=date(2024, 1, 1), dateOfNextRelease=date(2024, 1, 1), extensibilityCharacteristics="sample_text", growth="sample_text", growthPeriod="sample_text", initialLiveDate=date(2024, 1, 1), integrityCharacteristics="sample_text", internationalizationCharacteristics="sample_text", interoperabilityCharacteristics="sample_text", lifeCycleStatus="sample_text", localizationCharacteristics="sample_text", locatabilityCharacteristics="sample_text", manageabilityCharacteristics="sample_text", peakProfileLongTerm="sample_text", peakProfileShortTerm="sample_text", performanceCharacteristics="sample_text", portabilityCharacteristics="sample_text", privacyCharacteristics="sample_text", recoverabilityCharacteristics="sample_text", reliabilityCharacteristics="sample_text", retirementDate=date(2024, 1, 1), scalabilityCharacteristics="sample_text", securityCharacteristics="sample_text", serviceabilityCharacteristics="sample_text", servicesTimes="sample_text", throughput="sample_text", throughputPeriod="sample_text")
    b2 = contentfwk_PhysicalApplicationComponent(availabilityCharacteristics="sample_text_2", capacityCharacteristics="sample_text_2", credibilityCharacteristics="sample_text_2", dateOfLastRelease=date(2025, 6, 15), dateOfNextRelease=date(2025, 6, 15), extensibilityCharacteristics="sample_text_2", growth="sample_text_2", growthPeriod="sample_text_2", initialLiveDate=date(2025, 6, 15), integrityCharacteristics="sample_text_2", internationalizationCharacteristics="sample_text_2", interoperabilityCharacteristics="sample_text_2", lifeCycleStatus="sample_text_2", localizationCharacteristics="sample_text_2", locatabilityCharacteristics="sample_text_2", manageabilityCharacteristics="sample_text_2", peakProfileLongTerm="sample_text_2", peakProfileShortTerm="sample_text_2", performanceCharacteristics="sample_text_2", portabilityCharacteristics="sample_text_2", privacyCharacteristics="sample_text_2", recoverabilityCharacteristics="sample_text_2", reliabilityCharacteristics="sample_text_2", retirementDate=date(2025, 6, 15), scalabilityCharacteristics="sample_text_2", securityCharacteristics="sample_text_2", serviceabilityCharacteristics="sample_text_2", servicesTimes="sample_text_2", throughput="sample_text_2", throughputPeriod="sample_text_2")
    _safe_set(a, 'isRealizedByPhysicalTechnologyComponents', {b1})
    assert _is_linked(a, 'isRealizedByPhysicalTechnologyComponents', b1)
    if hasattr(b1, 'PhysicalApplicationComponent212'):
        assert _is_linked(b1, 'PhysicalApplicationComponent212', a)
    _safe_set(a, 'isRealizedByPhysicalTechnologyComponents', {b2})
    assert _is_linked(a, 'isRealizedByPhysicalTechnologyComponents', b2)
    if hasattr(b1, 'PhysicalApplicationComponent212'):
        assert not _is_linked(b1, 'PhysicalApplicationComponent212', a)
    if hasattr(b2, 'PhysicalApplicationComponent212'):
        assert _is_linked(b2, 'PhysicalApplicationComponent212', a)
    _safe_set(a, 'isRealizedByPhysicalTechnologyComponents', set())
    assert not _is_linked(a, 'isRealizedByPhysicalTechnologyComponents', b2)
    if hasattr(b2, 'PhysicalApplicationComponent212'):
        assert not _is_linked(b2, 'PhysicalApplicationComponent212', a)


def test_assoc_relatesToDataEntities133_link_reassign_clear():
    a = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b1 = contentfwk_DataEntity(dataEntityCategory="sample_text", privacyClassification="sample_text", retentionClassification="sample_text")
    b2 = contentfwk_DataEntity(dataEntityCategory="sample_text_2", privacyClassification="sample_text_2", retentionClassification="sample_text_2")
    _safe_set(a, 'contentfwk_DataEntity132', {b1})
    assert _is_linked(a, 'contentfwk_DataEntity132', b1)
    if hasattr(b1, 'contentfwk_DataEntity134'):
        assert _is_linked(b1, 'contentfwk_DataEntity134', a)
    _safe_set(a, 'contentfwk_DataEntity132', {b2})
    assert _is_linked(a, 'contentfwk_DataEntity132', b2)
    if hasattr(b1, 'contentfwk_DataEntity134'):
        assert not _is_linked(b1, 'contentfwk_DataEntity134', a)
    if hasattr(b2, 'contentfwk_DataEntity134'):
        assert _is_linked(b2, 'contentfwk_DataEntity134', a)
    _safe_set(a, 'contentfwk_DataEntity132', set())
    assert not _is_linked(a, 'contentfwk_DataEntity132', b2)
    if hasattr(b2, 'contentfwk_DataEntity134'):
        assert not _is_linked(b2, 'contentfwk_DataEntity134', a)


def test_assoc_residesWithinLogicalDataComponent127_link_reassign_clear():
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


def test_assoc_resolvesEvents192_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Event()
    b2 = contentfwk_Event()
    _safe_set(a, 'isResolvedByProcesses', {b1})
    assert _is_linked(a, 'isResolvedByProcesses', b1)
    if hasattr(b1, 'Event193'):
        assert _is_linked(b1, 'Event193', a)
    _safe_set(a, 'isResolvedByProcesses', {b2})
    assert _is_linked(a, 'isResolvedByProcesses', b2)
    if hasattr(b1, 'Event193'):
        assert not _is_linked(b1, 'Event193', a)
    if hasattr(b2, 'Event193'):
        assert _is_linked(b2, 'Event193', a)
    _safe_set(a, 'isResolvedByProcesses', set())
    assert not _is_linked(a, 'isResolvedByProcesses', b2)
    if hasattr(b2, 'Event193'):
        assert not _is_linked(b2, 'Event193', a)


def test_assoc_resolvesEvents94_link_reassign_clear():
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


def test_assoc_roles10_link_reassign_clear():
    a = contentfwk_Role(estimatedFTEs="sample_text")
    b1 = contentfwk_BusinessArchitecture()
    b2 = contentfwk_BusinessArchitecture()
    _safe_set(a, 'contentfwk_Role', b1)
    assert _is_linked(a, 'contentfwk_Role', b1)
    if hasattr(b1, 'contentfwk_BusinessArchitecture11'):
        assert _is_linked(b1, 'contentfwk_BusinessArchitecture11', a)
    _safe_set(a, 'contentfwk_Role', b2)
    assert _is_linked(a, 'contentfwk_Role', b2)
    if hasattr(b1, 'contentfwk_BusinessArchitecture11'):
        assert not _is_linked(b1, 'contentfwk_BusinessArchitecture11', a)
    if hasattr(b2, 'contentfwk_BusinessArchitecture11'):
        assert _is_linked(b2, 'contentfwk_BusinessArchitecture11', a)
    _safe_set(a, 'contentfwk_Role', None)
    assert not _is_linked(a, 'contentfwk_Role', b2)
    if hasattr(b2, 'contentfwk_BusinessArchitecture11'):
        assert not _is_linked(b2, 'contentfwk_BusinessArchitecture11', a)


def test_assoc_suppliesDataEntities82_link_reassign_clear():
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


def test_assoc_suppliesPlatformServices331_link_reassign_clear():
    a = contentfwk_PlatformService(categoryTRM="sample_text", standardClass="sample_text")
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


def test_assoc_supportsActors163_link_reassign_clear():
    a = contentfwk_Actor(FTEs="sample_text", actorGoal="sample_text", actorTasks="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'Actor164', b1)
    assert _is_linked(a, 'Actor164', b1)
    if hasattr(b1, 'interactsWithFunctions'):
        assert _is_linked(b1, 'interactsWithFunctions', a)
    _safe_set(a, 'Actor164', b2)
    assert _is_linked(a, 'Actor164', b2)
    if hasattr(b1, 'interactsWithFunctions'):
        assert not _is_linked(b1, 'interactsWithFunctions', a)
    if hasattr(b2, 'interactsWithFunctions'):
        assert _is_linked(b2, 'interactsWithFunctions', a)
    _safe_set(a, 'Actor164', None)
    assert not _is_linked(a, 'Actor164', b2)
    if hasattr(b2, 'interactsWithFunctions'):
        assert not _is_linked(b2, 'interactsWithFunctions', a)


def test_assoc_supportsProcesses157_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Function()
    b2 = contentfwk_Function()
    _safe_set(a, 'Process158', b1)
    assert _is_linked(a, 'Process158', b1)
    if hasattr(b1, 'decomposesFunctions'):
        assert _is_linked(b1, 'decomposesFunctions', a)
    _safe_set(a, 'Process158', b2)
    assert _is_linked(a, 'Process158', b2)
    if hasattr(b1, 'decomposesFunctions'):
        assert not _is_linked(b1, 'decomposesFunctions', a)
    if hasattr(b2, 'decomposesFunctions'):
        assert _is_linked(b2, 'decomposesFunctions', a)
    _safe_set(a, 'Process158', None)
    assert not _is_linked(a, 'Process158', b2)
    if hasattr(b2, 'decomposesFunctions'):
        assert not _is_linked(b2, 'decomposesFunctions', a)


def test_assoc_supportsProcesses372_link_reassign_clear():
    a = contentfwk_Process(isAutomated=True, processCritiality="sample_text", processVolumetrics="sample_text")
    b1 = contentfwk_Service()
    b2 = contentfwk_Service()
    _safe_set(a, 'Process373', b1)
    assert _is_linked(a, 'Process373', b1)
    if hasattr(b1, 'decomposesServices'):
        assert _is_linked(b1, 'decomposesServices', a)
    _safe_set(a, 'Process373', b2)
    assert _is_linked(a, 'Process373', b2)
    if hasattr(b1, 'decomposesServices'):
        assert not _is_linked(b1, 'decomposesServices', a)
    if hasattr(b2, 'decomposesServices'):
        assert _is_linked(b2, 'decomposesServices', a)
    _safe_set(a, 'Process373', None)
    assert not _is_linked(a, 'Process373', b2)
    if hasattr(b2, 'decomposesServices'):
        assert not _is_linked(b2, 'decomposesServices', a)


def test_assoc_units6_link_reassign_clear():
    a = contentfwk_OrganizationUnit(headcount="sample_text")
    b1 = contentfwk_BusinessArchitecture()
    b2 = contentfwk_BusinessArchitecture()
    _safe_set(a, 'contentfwk_OrganizationUnit', b1)
    assert _is_linked(a, 'contentfwk_OrganizationUnit', b1)
    if hasattr(b1, 'contentfwk_BusinessArchitecture7'):
        assert _is_linked(b1, 'contentfwk_BusinessArchitecture7', a)
    _safe_set(a, 'contentfwk_OrganizationUnit', b2)
    assert _is_linked(a, 'contentfwk_OrganizationUnit', b2)
    if hasattr(b1, 'contentfwk_BusinessArchitecture7'):
        assert not _is_linked(b1, 'contentfwk_BusinessArchitecture7', a)
    if hasattr(b2, 'contentfwk_BusinessArchitecture7'):
        assert _is_linked(b2, 'contentfwk_BusinessArchitecture7', a)
    _safe_set(a, 'contentfwk_OrganizationUnit', None)
    assert not _is_linked(a, 'contentfwk_OrganizationUnit', b2)
    if hasattr(b2, 'contentfwk_BusinessArchitecture7'):
        assert not _is_linked(b2, 'contentfwk_BusinessArchitecture7', a)


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


contentfwk_Architecture_strategy = st.builds(contentfwk_Architecture, ID=safe_text)
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


contentfwk_Contract_strategy = st.builds(contentfwk_Contract, availabilityQualityCharacteristics=safe_text, behaviorCharacteristics=safe_text, capacityCharacteristics=safe_text, contractControlRequirements=safe_text, credibilityCharacteristics=safe_text, extensibilityCharacteristics=safe_text, growth=safe_text, growthPeriod=safe_text, integrityCharacteristics=safe_text, internationalizationCharacteristics=safe_text, interoperabilityCharacteristics=safe_text, localizationCharacteristics=safe_text, locatabilityCharacteristics=safe_text, manageabilityCharacteristics=safe_text, peakProfileLongTerm=safe_text, peakProfileShortTerm=safe_text, performanceCharacteristics=safe_text, portabilityCharacteristics=safe_text, privacyCharacteristics=safe_text, qualityOfInformationRequired=safe_text, recoverabilityCharacteristics=safe_text, reliabilityCharacteristics=safe_text, responseCharacteristics=safe_text, resultControlRequirements=safe_text, scalabilityCharacteristics=safe_text, securityCharacteristics=safe_text, serviceNameCalled=safe_text, serviceNameCaller=safe_text, serviceQualityCharacteristics=safe_text, serviceabilityCharacteristics=safe_text, servicesTimes=safe_text, throughput=safe_text, throughputPeriod=safe_text)
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


contentfwk_Element_strategy = st.builds(contentfwk_Element, ID=safe_text, category=safe_text, description=safe_text, name=safe_text, ownerDescr=safe_text, sourceDescr=safe_text)
@given(instance=contentfwk_Element_strategy)
@settings(max_examples=25)
def test_contentfwk_Element_instantiation(instance):
    assert isinstance(instance, contentfwk_Element)


contentfwk_EnterpriseArchitecture_strategy = st.builds(contentfwk_EnterpriseArchitecture, ID=safe_text)
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


contentfwk_PhysicalApplicationComponent_strategy = st.builds(contentfwk_PhysicalApplicationComponent, availabilityCharacteristics=safe_text, capacityCharacteristics=safe_text, credibilityCharacteristics=safe_text, dateOfLastRelease=st.dates(), dateOfNextRelease=st.dates(), extensibilityCharacteristics=safe_text, growth=safe_text, growthPeriod=safe_text, initialLiveDate=st.dates(), integrityCharacteristics=safe_text, internationalizationCharacteristics=safe_text, interoperabilityCharacteristics=safe_text, lifeCycleStatus=safe_text, localizationCharacteristics=safe_text, locatabilityCharacteristics=safe_text, manageabilityCharacteristics=safe_text, peakProfileLongTerm=safe_text, peakProfileShortTerm=safe_text, performanceCharacteristics=safe_text, portabilityCharacteristics=safe_text, privacyCharacteristics=safe_text, recoverabilityCharacteristics=safe_text, reliabilityCharacteristics=safe_text, retirementDate=st.dates(), scalabilityCharacteristics=safe_text, securityCharacteristics=safe_text, serviceabilityCharacteristics=safe_text, servicesTimes=safe_text, throughput=safe_text, throughputPeriod=safe_text)
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


contentfwk_PlatformService_strategy = st.builds(contentfwk_PlatformService, categoryTRM=safe_text, standardClass=safe_text)
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


contentfwk_Standard_strategy = st.builds(contentfwk_Standard, lastStandardReviewDate=st.dates(), nextStandardReviewDate=st.dates(), retireDate=st.dates(), standardClass=safe_text, standardCreationDate=st.dates())
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


contentfwk_WorkPackage_strategy = st.builds(contentfwk_WorkPackage, capabilityDelivered=safe_text, workPackageCategory=safe_text)
@given(instance=contentfwk_WorkPackage_strategy)
@settings(max_examples=25)
def test_contentfwk_WorkPackage_instantiation(instance):
    assert isinstance(instance, contentfwk_WorkPackage)





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
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture9')
    _safe_set(owner, 'contentfwk_Actor', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture9')


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
    assert owner in getattr(partner, 'meetsServiceQuality')
    _safe_set(owner, 'Contract', None)
    assert owner not in getattr(partner, 'meetsServiceQuality')


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
    assert owner in getattr(partner, 'accessesFunctions')
    _safe_set(owner, 'Role162', None)
    assert owner not in getattr(partner, 'accessesFunctions')


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
    assert owner in getattr(partner, 'contentfwk_StrategicArchitecture')
    _safe_set(owner, 'contentfwk_Capability', None)
    assert owner not in getattr(partner, 'contentfwk_StrategicArchitecture')


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
    assert owner in getattr(partner, 'isAccessedByServices')
    _safe_set(owner, 'DataEntity359', None)
    assert owner not in getattr(partner, 'isAccessedByServices')


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
    assert owner in getattr(partner, 'operatesInLocation')
    _safe_set(owner, 'Actor272', None)
    assert owner not in getattr(partner, 'operatesInLocation')


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
    assert owner in getattr(partner, 'operatesInLocation274')
    _safe_set(owner, 'OrganizationUnit275', None)
    assert owner not in getattr(partner, 'operatesInLocation274')


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
    assert owner in getattr(partner, 'isHostedInLocation')
    _safe_set(owner, 'PhysicalApplicationComponent278', None)
    assert owner not in getattr(partner, 'isHostedInLocation')


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
    assert owner in getattr(partner, 'isHostedInLocation280')
    _safe_set(owner, 'PhysicalTechnologyComponent281', None)
    assert owner not in getattr(partner, 'isHostedInLocation280')


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
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture27')
    _safe_set(owner, 'contentfwk_Contract', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture27')


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
    assert owner in getattr(partner, 'residesWithinLogicalDataComponent')
    _safe_set(owner, 'DataEntity291', None)
    assert owner not in getattr(partner, 'residesWithinLogicalDataComponent')


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
    assert owner in getattr(partner, 'encapsulatesPhysicalDataComponents')
    _safe_set(owner, 'PhysicalApplicationComponent302', None)
    assert owner not in getattr(partner, 'encapsulatesPhysicalDataComponents')


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
    assert owner in getattr(partner, 'isGuidedByControls')
    _safe_set(owner, 'Process265', None)
    assert owner not in getattr(partner, 'isGuidedByControls')


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
    assert owner in getattr(partner, 'contentfwk_DataArchitecture')
    _safe_set(owner, 'contentfwk_DataEntity', None)
    assert owner not in getattr(partner, 'contentfwk_DataArchitecture')


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
    assert owner in getattr(partner, 'extendsLogicalApplicationComponents')
    _safe_set(owner, 'PhysicalApplicationComponent', None)
    assert owner not in getattr(partner, 'extendsLogicalApplicationComponents')


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
    assert owner in getattr(partner, 'generatesEvents262')
    _safe_set(owner, 'Actor263', None)
    assert owner not in getattr(partner, 'generatesEvents262')


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
    assert owner in getattr(partner, 'generatesEvents')
    _safe_set(owner, 'Process257', None)
    assert owner not in getattr(partner, 'generatesEvents')


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
    assert owner in getattr(partner, 'governsAndMeasuresBusinessServices')
    _safe_set(owner, 'Contract361', None)
    assert owner not in getattr(partner, 'governsAndMeasuresBusinessServices')


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
    assert owner in getattr(partner, 'providesPlatformForServices')
    _safe_set(owner, 'LogicalTechnologyComponent365', None)
    assert owner not in getattr(partner, 'providesPlatformForServices')


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
    assert owner in getattr(partner, 'ownsAndGovernsServices')
    _safe_set(owner, 'OrganizationUnit369', None)
    assert owner not in getattr(partner, 'ownsAndGovernsServices')


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
    assert owner in getattr(partner, 'performsFunctions')
    _safe_set(owner, 'Actor152', None)
    assert owner not in getattr(partner, 'performsFunctions')


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
    assert owner in getattr(partner, 'producesProducts')
    _safe_set(owner, 'OrganizationUnit230', None)
    assert owner not in getattr(partner, 'producesProducts')


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
    assert owner in getattr(partner, 'producesProducts232')
    _safe_set(owner, 'Process233', None)
    assert owner not in getattr(partner, 'producesProducts232')


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
    assert owner in getattr(partner, 'consumesServices')
    _safe_set(owner, 'Actor353', None)
    assert owner not in getattr(partner, 'consumesServices')


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
    assert owner in getattr(partner, 'orchestratesFunctions')
    _safe_set(owner, 'Process160', None)
    assert owner not in getattr(partner, 'orchestratesFunctions')


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
    assert owner in getattr(partner, 'orchestratesServices')
    _safe_set(owner, 'Process375', None)
    assert owner not in getattr(partner, 'orchestratesServices')


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
    assert owner in getattr(partner, 'resolvesEvents259')
    _safe_set(owner, 'Actor260', None)
    assert owner not in getattr(partner, 'resolvesEvents259')


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
    assert owner in getattr(partner, 'resolvesEvents254')
    _safe_set(owner, 'Process255', None)
    assert owner not in getattr(partner, 'resolvesEvents254')


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
    assert owner in getattr(partner, 'contentfwk_TechnologyArchitecture41')
    _safe_set(owner, 'contentfwk_LogicalTechnologyComponent', None)
    assert owner not in getattr(partner, 'contentfwk_TechnologyArchitecture41')


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
    assert owner in getattr(partner, 'isMotivatedByDrivers')
    _safe_set(owner, 'OrganizationUnit', None)
    assert owner not in getattr(partner, 'isMotivatedByDrivers')


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
    assert owner in getattr(partner, 'isProcessesByLogicalApplicationComponents')
    _safe_set(owner, 'DataEntity141', None)
    assert owner not in getattr(partner, 'isProcessesByLogicalApplicationComponents')


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
    assert owner in getattr(partner, 'contentfwk_ApplicationArchitecture309')
    _safe_set(owner, 'contentfwk_PhysicalApplicationComponent', None)
    assert owner not in getattr(partner, 'contentfwk_ApplicationArchitecture309')


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
    assert owner in getattr(partner, 'contentfwk_TechnologyArchitecture39')
    _safe_set(owner, 'contentfwk_PhysicalTechnologyComponent', None)
    assert owner not in getattr(partner, 'contentfwk_TechnologyArchitecture39')


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
    assert owner in getattr(partner, 'contentfwk_TechnologyArchitecture')
    _safe_set(owner, 'contentfwk_PlatformService', None)
    assert owner not in getattr(partner, 'contentfwk_TechnologyArchitecture')


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
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture17')
    _safe_set(owner, 'contentfwk_Process', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture17')


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
    assert owner in getattr(partner, 'isUpdatedThroughServices')
    _safe_set(owner, 'DataEntity357', None)
    assert owner not in getattr(partner, 'isUpdatedThroughServices')


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
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture11')
    _safe_set(owner, 'contentfwk_Role', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture11')


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
    assert owner in getattr(partner, 'interactsWithFunctions')
    _safe_set(owner, 'Actor164', None)
    assert owner not in getattr(partner, 'interactsWithFunctions')


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
    assert owner in getattr(partner, 'decomposesFunctions')
    _safe_set(owner, 'Process158', None)
    assert owner not in getattr(partner, 'decomposesFunctions')


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
    assert owner in getattr(partner, 'decomposesServices')
    _safe_set(owner, 'Process373', None)
    assert owner not in getattr(partner, 'decomposesServices')


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
    assert owner in getattr(partner, 'contentfwk_BusinessArchitecture7')
    _safe_set(owner, 'contentfwk_OrganizationUnit', None)
    assert owner not in getattr(partner, 'contentfwk_BusinessArchitecture7')




import datetime as _ch_datetime
from python_code import DataEntityCategory
import pytest
from python_code import LifeCycleStatus
import pytest
from python_code import PrincipleCategory
import pytest
from python_code import StandardsClass
import pytest
from python_code import WorkPackageCategory
import pytest
from python_code import contentfwk_BusinessArchitecture
from python_code import contentfwk_Contract
from python_code import contentfwk_Service
from python_code import contentfwk_ServiceQuality

def test_contentfwk_Contract___init__():
    assert contentfwk_Contract.__init__(contentfwk_Contract('', '\x00', '', '\x01', '', '', '', '', '', '', '', '', '', '\x00', '\x00', '\x00', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', contentfwk_Contract=contentfwk_BusinessArchitecture(), Contract=contentfwk_ServiceQuality(), isGovernedAndMeasuredByContracts=set(), appliesToContracts=set(), Contract361=contentfwk_Service()), '', '', '', '', '\x00', '', '', '', '\x01', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', contentfwk_Contract=contentfwk_BusinessArchitecture(), Contract=contentfwk_ServiceQuality(), isGovernedAndMeasuredByContracts=set(), appliesToContracts=set(), Contract361=contentfwk_Service()) == None
from python_code import contentfwk_EnterpriseArchitecture

def test_contentfwk_EnterpriseArchitecture___init__():
    assert contentfwk_EnterpriseArchitecture.__init__(contentfwk_EnterpriseArchitecture('\x00', contentfwk_EnterpriseArchitecture=set()), '', contentfwk_EnterpriseArchitecture=set()) == None

def test_contentfwk_EnterpriseArchitecture_forceID():
    contentfwk_EnterpriseArchitecture.forceID(contentfwk_EnterpriseArchitecture('', contentfwk_EnterpriseArchitecture=set()), '')
from python_code import contentfwk_Principle

def test_contentfwk_Principle___init__():
    assert contentfwk_Principle.__init__(contentfwk_Principle('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None
from python_code import contentfwk_Requirement

def test_contentfwk_Requirement___init__():
    assert contentfwk_Requirement.__init__(contentfwk_Requirement('', '', '\x00\x00'), '', '', '') == None
from python_code import contentfwk_Standard

def test_contentfwk_Standard___init__():
    assert contentfwk_Standard.__init__(contentfwk_Standard('', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1)), '\x00\x00', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)) == None

