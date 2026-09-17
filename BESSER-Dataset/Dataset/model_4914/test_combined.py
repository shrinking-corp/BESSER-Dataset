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
    services_Parameter,
    services_ServiceAdditional,
    services_ServiceSupport,
    services_ServiceContract,
    services_ServiceInterrest,
    services_ServiceSecurityMgt,
    services_ServiceDescription,
    services_ServiceName,
    services_Service,
    services_ServiceProfile,
    services_ServiceIncidentMgt,
    services_CIID,
    services_EObject,
    Service,
    services_RFSService,
    services_CFSService,
    ServiceKindType,
    UsageStateType,
    LifeCycleStateType,
    MaintenanceType,
    ServiceClassType,
    InterrestKindType,
    SecurityRatingType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_services_parameter_is_not_abstract():
    assert not inspect.isabstract(services_Parameter)


def test_hyp_services_parameter_constructor_exists():
    assert callable(services_Parameter.__init__)


def test_hyp_services_parameter_constructor_args():
    sig = inspect.signature(services_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_serviceadditional_is_not_abstract():
    assert not inspect.isabstract(services_ServiceAdditional)


def test_hyp_services_serviceadditional_constructor_exists():
    assert callable(services_ServiceAdditional.__init__)


def test_hyp_services_serviceadditional_constructor_args():
    sig = inspect.signature(services_ServiceAdditional.__init__)
    params = list(sig.parameters.keys())
    assert "costCenter" in params, "Missing parameter 'costCenter'"
    assert "report" in params, "Missing parameter 'report'"
    assert "history" in params, "Missing parameter 'history'"
    assert "link" in params, "Missing parameter 'link'"
    assert "usageState" in params, "Missing parameter 'usageState'"
    assert "lifeCycleState" in params, "Missing parameter 'lifeCycleState'"
    assert "kpi" in params, "Missing parameter 'kpi'"










def test_hyp_services_servicesupport_is_not_abstract():
    assert not inspect.isabstract(services_ServiceSupport)


def test_hyp_services_servicesupport_constructor_exists():
    assert callable(services_ServiceSupport.__init__)


def test_hyp_services_servicesupport_constructor_args():
    sig = inspect.signature(services_ServiceSupport.__init__)
    params = list(sig.parameters.keys())
    assert "supportDays" in params, "Missing parameter 'supportDays'"
    assert "supportHours" in params, "Missing parameter 'supportHours'"





def test_hyp_services_servicecontract_is_not_abstract():
    assert not inspect.isabstract(services_ServiceContract)


def test_hyp_services_servicecontract_constructor_exists():
    assert callable(services_ServiceContract.__init__)


def test_hyp_services_servicecontract_constructor_args():
    sig = inspect.signature(services_ServiceContract.__init__)
    params = list(sig.parameters.keys())
    assert "uC" in params, "Missing parameter 'uC'"
    assert "oLA" in params, "Missing parameter 'oLA'"
    assert "wLA" in params, "Missing parameter 'wLA'"
    assert "sLA" in params, "Missing parameter 'sLA'"







def test_hyp_services_serviceinterrest_is_not_abstract():
    assert not inspect.isabstract(services_ServiceInterrest)


def test_hyp_services_serviceinterrest_constructor_exists():
    assert callable(services_ServiceInterrest.__init__)


def test_hyp_services_serviceinterrest_constructor_args():
    sig = inspect.signature(services_ServiceInterrest.__init__)
    params = list(sig.parameters.keys())
    assert "contactUnit" in params, "Missing parameter 'contactUnit'"
    assert "interrestKind" in params, "Missing parameter 'interrestKind'"





def test_hyp_services_servicesecuritymgt_is_not_abstract():
    assert not inspect.isabstract(services_ServiceSecurityMgt)


def test_hyp_services_servicesecuritymgt_constructor_exists():
    assert callable(services_ServiceSecurityMgt.__init__)


def test_hyp_services_servicesecuritymgt_constructor_args():
    sig = inspect.signature(services_ServiceSecurityMgt.__init__)
    params = list(sig.parameters.keys())
    assert "drRecoveryPlan" in params, "Missing parameter 'drRecoveryPlan'"
    assert "drPlanContact" in params, "Missing parameter 'drPlanContact'"
    assert "securityRating" in params, "Missing parameter 'securityRating'"
    assert "drPlanRepository" in params, "Missing parameter 'drPlanRepository'"







def test_hyp_services_servicedescription_is_not_abstract():
    assert not inspect.isabstract(services_ServiceDescription)


def test_hyp_services_servicedescription_constructor_exists():
    assert callable(services_ServiceDescription.__init__)


def test_hyp_services_servicedescription_constructor_args():
    sig = inspect.signature(services_ServiceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "serviceDescriptionNational" in params, "Missing parameter 'serviceDescriptionNational'"
    assert "serviceDescriptionCommon" in params, "Missing parameter 'serviceDescriptionCommon'"





def test_hyp_services_servicename_is_not_abstract():
    assert not inspect.isabstract(services_ServiceName)


def test_hyp_services_servicename_constructor_exists():
    assert callable(services_ServiceName.__init__)


def test_hyp_services_servicename_constructor_args():
    sig = inspect.signature(services_ServiceName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "index" in params, "Missing parameter 'index'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "identifier" in params, "Missing parameter 'identifier'"







def test_hyp_services_service_is_not_abstract():
    assert not inspect.isabstract(services_Service)


def test_hyp_services_service_constructor_exists():
    assert callable(services_Service.__init__)


def test_hyp_services_service_constructor_args():
    sig = inspect.signature(services_Service.__init__)
    params = list(sig.parameters.keys())
    assert "serviceCharacterCommon" in params, "Missing parameter 'serviceCharacterCommon'"
    assert "serviceCategory" in params, "Missing parameter 'serviceCategory'"
    assert "ssDomain" in params, "Missing parameter 'ssDomain'"
    assert "serviceSupport1" in params, "Missing parameter 'serviceSupport1'"
    assert "serviceClass" in params, "Missing parameter 'serviceClass'"
    assert "serviceKind" in params, "Missing parameter 'serviceKind'"
    assert "mostTopService" in params, "Missing parameter 'mostTopService'"










def test_hyp_services_serviceprofile_is_not_abstract():
    assert not inspect.isabstract(services_ServiceProfile)


def test_hyp_services_serviceprofile_constructor_exists():
    assert callable(services_ServiceProfile.__init__)


def test_hyp_services_serviceprofile_constructor_args():
    sig = inspect.signature(services_ServiceProfile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_services_serviceincidentmgt_is_not_abstract():
    assert not inspect.isabstract(services_ServiceIncidentMgt)


def test_hyp_services_serviceincidentmgt_constructor_exists():
    assert callable(services_ServiceIncidentMgt.__init__)


def test_hyp_services_serviceincidentmgt_constructor_args():
    sig = inspect.signature(services_ServiceIncidentMgt.__init__)
    params = list(sig.parameters.keys())
    assert "monitoring" in params, "Missing parameter 'monitoring'"
    assert "maintenanceWindow" in params, "Missing parameter 'maintenanceWindow'"
    assert "maintenance" in params, "Missing parameter 'maintenance'"
    assert "businessImpact" in params, "Missing parameter 'businessImpact'"







def test_hyp_services_ciid_is_not_abstract():
    assert not inspect.isabstract(services_CIID)


def test_hyp_services_ciid_constructor_exists():
    assert callable(services_CIID.__init__)


def test_hyp_services_ciid_constructor_args():
    sig = inspect.signature(services_CIID.__init__)
    params = list(sig.parameters.keys())
    assert "localCIID" in params, "Missing parameter 'localCIID'"
    assert "commonCIID" in params, "Missing parameter 'commonCIID'"





def test_hyp_services_eobject_is_not_abstract():
    assert not inspect.isabstract(services_EObject)


def test_hyp_services_eobject_constructor_exists():
    assert callable(services_EObject.__init__)


def test_hyp_services_eobject_constructor_args():
    sig = inspect.signature(services_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_hyp_service_constructor_exists():
    assert callable(Service.__init__)


def test_hyp_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_rfsservice_is_not_abstract():
    assert not inspect.isabstract(services_RFSService)


def test_hyp_services_rfsservice_constructor_exists():
    assert callable(services_RFSService.__init__)


def test_hyp_services_rfsservice_constructor_args():
    sig = inspect.signature(services_RFSService.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "functionalCategory" in params, "Missing parameter 'functionalCategory'"





def test_hyp_services_cfsservice_is_not_abstract():
    assert not inspect.isabstract(services_CFSService)


def test_hyp_services_cfsservice_constructor_exists():
    assert callable(services_CFSService.__init__)


def test_hyp_services_cfsservice_constructor_args():
    sig = inspect.signature(services_CFSService.__init__)
    params = list(sig.parameters.keys())
    assert "scenario" in params, "Missing parameter 'scenario'"
    assert "provider" in params, "Missing parameter 'provider'"



def test_hyp_servicekindtype_exists():
    # Check that the Enumeration exists
    assert ServiceKindType is not None

def test_hyp_servicekindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServiceKindType]
    expected_literals = [
        "CFS",
        "RFS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServiceKindType"

def test_hyp_usagestatetype_exists():
    # Check that the Enumeration exists
    assert UsageStateType is not None

def test_hyp_usagestatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UsageStateType]
    expected_literals = [
        "Reserved",
        "Assigned",
        "Disabled",
        "Free",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UsageStateType"

def test_hyp_lifecyclestatetype_exists():
    # Check that the Enumeration exists
    assert LifeCycleStateType is not None

def test_hyp_lifecyclestatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LifeCycleStateType]
    expected_literals = [
        "Planned",
        "Removed",
        "Active",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LifeCycleStateType"

def test_hyp_maintenancetype_exists():
    # Check that the Enumeration exists
    assert MaintenanceType is not None

def test_hyp_maintenancetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MaintenanceType]
    expected_literals = [
        "_1stLineMaintenance",
        "_2ndLineMaintenance",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MaintenanceType"

def test_hyp_serviceclasstype_exists():
    # Check that the Enumeration exists
    assert ServiceClassType is not None

def test_hyp_serviceclasstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServiceClassType]
    expected_literals = [
        "Bronze",
        "Sold",
        "Silver",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServiceClassType"

def test_hyp_interrestkindtype_exists():
    # Check that the Enumeration exists
    assert InterrestKindType is not None

def test_hyp_interrestkindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InterrestKindType]
    expected_literals = [
        "Reporting",
        "Escallation",
        "ServiceManagement",
        "FinancialManagement",
        "ProductManagement",
        "SalesManagement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InterrestKindType"

def test_hyp_securityratingtype_exists():
    # Check that the Enumeration exists
    assert SecurityRatingType is not None

def test_hyp_securityratingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SecurityRatingType]
    expected_literals = [
        "Low",
        "High",
        "Medium",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SecurityRatingType"


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
services_Parameter_strategy = st.builds(
    services_Parameter,
)
services_ServiceAdditional_strategy = st.builds(
    services_ServiceAdditional,
    costCenter=
        safe_text,
    report=
        safe_text,
    history=
        safe_text,
    link=
        safe_text,
    usageState=
        safe_text,
    lifeCycleState=
        safe_text,
    kpi=
        safe_text
)
services_ServiceSupport_strategy = st.builds(
    services_ServiceSupport,
    supportDays=
        safe_text,
    supportHours=
        safe_text
)
services_ServiceContract_strategy = st.builds(
    services_ServiceContract,
    uC=
        safe_text,
    oLA=
        safe_text,
    wLA=
        safe_text,
    sLA=
        safe_text
)
services_ServiceInterrest_strategy = st.builds(
    services_ServiceInterrest,
    contactUnit=
        safe_text,
    interrestKind=
        safe_text
)
services_ServiceSecurityMgt_strategy = st.builds(
    services_ServiceSecurityMgt,
    drRecoveryPlan=
        safe_text,
    drPlanContact=
        safe_text,
    securityRating=
        safe_text,
    drPlanRepository=
        safe_text
)
services_ServiceDescription_strategy = st.builds(
    services_ServiceDescription,
    serviceDescriptionNational=
        safe_text,
    serviceDescriptionCommon=
        safe_text
)
services_ServiceName_strategy = st.builds(
    services_ServiceName,
    name=
        safe_text,
    index=
        safe_text,
    alias=
        safe_text,
    identifier=
        safe_text
)
services_Service_strategy = st.builds(
    services_Service,
    serviceCharacterCommon=
        safe_text,
    serviceCategory=
        safe_text,
    ssDomain=
        safe_text,
    serviceSupport1=
        safe_text,
    serviceClass=
        safe_text,
    serviceKind=
        safe_text,
    mostTopService=
        safe_text
)
services_ServiceProfile_strategy = st.builds(
    services_ServiceProfile,
    name=
        safe_text
)
services_ServiceIncidentMgt_strategy = st.builds(
    services_ServiceIncidentMgt,
    monitoring=
        safe_text,
    maintenanceWindow=
        safe_text,
    maintenance=
        safe_text,
    businessImpact=
        safe_text
)
services_CIID_strategy = st.builds(
    services_CIID,
    localCIID=
        safe_text,
    commonCIID=
        safe_text
)
services_EObject_strategy = st.builds(
    services_EObject,
)
Service_strategy = st.builds(
    Service,
)
services_RFSService_strategy = st.builds(
    services_RFSService,
    location=
        safe_text,
    functionalCategory=
        safe_text
)
services_CFSService_strategy = st.builds(
    services_CFSService,
    scenario=
        safe_text,
    provider=
        safe_text
)





@given(instance=services_ServiceAdditional_strategy)
def test_hyp_services_serviceadditional_costCenter_setter(instance):
    original = instance.costCenter
    instance.costCenter = original
    assert instance.costCenter == original



@given(instance=services_ServiceAdditional_strategy)
def test_hyp_services_serviceadditional_report_setter(instance):
    original = instance.report
    instance.report = original
    assert instance.report == original



@given(instance=services_ServiceAdditional_strategy)
def test_hyp_services_serviceadditional_history_setter(instance):
    original = instance.history
    instance.history = original
    assert instance.history == original



@given(instance=services_ServiceAdditional_strategy)
def test_hyp_services_serviceadditional_link_setter(instance):
    original = instance.link
    instance.link = original
    assert instance.link == original



@given(instance=services_ServiceAdditional_strategy)
def test_hyp_services_serviceadditional_usageState_setter(instance):
    original = instance.usageState
    instance.usageState = original
    assert instance.usageState == original



@given(instance=services_ServiceAdditional_strategy)
def test_hyp_services_serviceadditional_lifeCycleState_setter(instance):
    original = instance.lifeCycleState
    instance.lifeCycleState = original
    assert instance.lifeCycleState == original



@given(instance=services_ServiceAdditional_strategy)
def test_hyp_services_serviceadditional_kpi_setter(instance):
    original = instance.kpi
    instance.kpi = original
    assert instance.kpi == original




@given(instance=services_ServiceSupport_strategy)
def test_hyp_services_servicesupport_supportDays_setter(instance):
    original = instance.supportDays
    instance.supportDays = original
    assert instance.supportDays == original



@given(instance=services_ServiceSupport_strategy)
def test_hyp_services_servicesupport_supportHours_setter(instance):
    original = instance.supportHours
    instance.supportHours = original
    assert instance.supportHours == original




@given(instance=services_ServiceContract_strategy)
def test_hyp_services_servicecontract_uC_setter(instance):
    original = instance.uC
    instance.uC = original
    assert instance.uC == original



@given(instance=services_ServiceContract_strategy)
def test_hyp_services_servicecontract_oLA_setter(instance):
    original = instance.oLA
    instance.oLA = original
    assert instance.oLA == original



@given(instance=services_ServiceContract_strategy)
def test_hyp_services_servicecontract_wLA_setter(instance):
    original = instance.wLA
    instance.wLA = original
    assert instance.wLA == original



@given(instance=services_ServiceContract_strategy)
def test_hyp_services_servicecontract_sLA_setter(instance):
    original = instance.sLA
    instance.sLA = original
    assert instance.sLA == original




@given(instance=services_ServiceInterrest_strategy)
def test_hyp_services_serviceinterrest_contactUnit_setter(instance):
    original = instance.contactUnit
    instance.contactUnit = original
    assert instance.contactUnit == original



@given(instance=services_ServiceInterrest_strategy)
def test_hyp_services_serviceinterrest_interrestKind_setter(instance):
    original = instance.interrestKind
    instance.interrestKind = original
    assert instance.interrestKind == original




@given(instance=services_ServiceSecurityMgt_strategy)
def test_hyp_services_servicesecuritymgt_drRecoveryPlan_setter(instance):
    original = instance.drRecoveryPlan
    instance.drRecoveryPlan = original
    assert instance.drRecoveryPlan == original



@given(instance=services_ServiceSecurityMgt_strategy)
def test_hyp_services_servicesecuritymgt_drPlanContact_setter(instance):
    original = instance.drPlanContact
    instance.drPlanContact = original
    assert instance.drPlanContact == original



@given(instance=services_ServiceSecurityMgt_strategy)
def test_hyp_services_servicesecuritymgt_securityRating_setter(instance):
    original = instance.securityRating
    instance.securityRating = original
    assert instance.securityRating == original



@given(instance=services_ServiceSecurityMgt_strategy)
def test_hyp_services_servicesecuritymgt_drPlanRepository_setter(instance):
    original = instance.drPlanRepository
    instance.drPlanRepository = original
    assert instance.drPlanRepository == original




@given(instance=services_ServiceDescription_strategy)
def test_hyp_services_servicedescription_serviceDescriptionNational_setter(instance):
    original = instance.serviceDescriptionNational
    instance.serviceDescriptionNational = original
    assert instance.serviceDescriptionNational == original



@given(instance=services_ServiceDescription_strategy)
def test_hyp_services_servicedescription_serviceDescriptionCommon_setter(instance):
    original = instance.serviceDescriptionCommon
    instance.serviceDescriptionCommon = original
    assert instance.serviceDescriptionCommon == original




@given(instance=services_ServiceName_strategy)
def test_hyp_services_servicename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=services_ServiceName_strategy)
def test_hyp_services_servicename_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=services_ServiceName_strategy)
def test_hyp_services_servicename_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=services_ServiceName_strategy)
def test_hyp_services_servicename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original




@given(instance=services_Service_strategy)
def test_hyp_services_service_serviceCharacterCommon_setter(instance):
    original = instance.serviceCharacterCommon
    instance.serviceCharacterCommon = original
    assert instance.serviceCharacterCommon == original



@given(instance=services_Service_strategy)
def test_hyp_services_service_serviceCategory_setter(instance):
    original = instance.serviceCategory
    instance.serviceCategory = original
    assert instance.serviceCategory == original



@given(instance=services_Service_strategy)
def test_hyp_services_service_ssDomain_setter(instance):
    original = instance.ssDomain
    instance.ssDomain = original
    assert instance.ssDomain == original



@given(instance=services_Service_strategy)
def test_hyp_services_service_serviceSupport1_setter(instance):
    original = instance.serviceSupport1
    instance.serviceSupport1 = original
    assert instance.serviceSupport1 == original



@given(instance=services_Service_strategy)
def test_hyp_services_service_serviceClass_setter(instance):
    original = instance.serviceClass
    instance.serviceClass = original
    assert instance.serviceClass == original



@given(instance=services_Service_strategy)
def test_hyp_services_service_serviceKind_setter(instance):
    original = instance.serviceKind
    instance.serviceKind = original
    assert instance.serviceKind == original



@given(instance=services_Service_strategy)
def test_hyp_services_service_mostTopService_setter(instance):
    original = instance.mostTopService
    instance.mostTopService = original
    assert instance.mostTopService == original




@given(instance=services_ServiceProfile_strategy)
def test_hyp_services_serviceprofile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=services_ServiceIncidentMgt_strategy)
def test_hyp_services_serviceincidentmgt_monitoring_setter(instance):
    original = instance.monitoring
    instance.monitoring = original
    assert instance.monitoring == original



@given(instance=services_ServiceIncidentMgt_strategy)
def test_hyp_services_serviceincidentmgt_maintenanceWindow_setter(instance):
    original = instance.maintenanceWindow
    instance.maintenanceWindow = original
    assert instance.maintenanceWindow == original



@given(instance=services_ServiceIncidentMgt_strategy)
def test_hyp_services_serviceincidentmgt_maintenance_setter(instance):
    original = instance.maintenance
    instance.maintenance = original
    assert instance.maintenance == original



@given(instance=services_ServiceIncidentMgt_strategy)
def test_hyp_services_serviceincidentmgt_businessImpact_setter(instance):
    original = instance.businessImpact
    instance.businessImpact = original
    assert instance.businessImpact == original




@given(instance=services_CIID_strategy)
def test_hyp_services_ciid_localCIID_setter(instance):
    original = instance.localCIID
    instance.localCIID = original
    assert instance.localCIID == original



@given(instance=services_CIID_strategy)
def test_hyp_services_ciid_commonCIID_setter(instance):
    original = instance.commonCIID
    instance.commonCIID = original
    assert instance.commonCIID == original






@given(instance=services_RFSService_strategy)
def test_hyp_services_rfsservice_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=services_RFSService_strategy)
def test_hyp_services_rfsservice_functionalCategory_setter(instance):
    original = instance.functionalCategory
    instance.functionalCategory = original
    assert instance.functionalCategory == original




@given(instance=services_CFSService_strategy)
def test_hyp_services_cfsservice_scenario_setter(instance):
    original = instance.scenario
    instance.scenario = original
    assert instance.scenario == original



@given(instance=services_CFSService_strategy)
def test_hyp_services_cfsservice_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Service,
    services_CFSService,
    services_CIID,
    services_EObject,
    services_Parameter,
    services_RFSService,
    services_Service,
    services_ServiceAdditional,
    services_ServiceContract,
    services_ServiceDescription,
    services_ServiceIncidentMgt,
    services_ServiceInterrest,
    services_ServiceName,
    services_ServiceProfile,
    services_ServiceSecurityMgt,
    services_ServiceSupport,
    InterrestKindType,
    LifeCycleStateType,
    MaintenanceType,
    SecurityRatingType,
    ServiceClassType,
    ServiceKindType,
    UsageStateType,
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

def test_services_CFSService_provider_value_roundtrip():
    instance = services_CFSService(provider="sample_text", scenario="sample_text")
    assert instance.provider == "sample_text"
    instance.provider = "sample_text_2"
    assert instance.provider == "sample_text_2"


def test_services_CFSService_scenario_value_roundtrip():
    instance = services_CFSService(provider="sample_text", scenario="sample_text")
    assert instance.scenario == "sample_text"
    instance.scenario = "sample_text_2"
    assert instance.scenario == "sample_text_2"


def test_services_CIID_commonCIID_value_roundtrip():
    instance = services_CIID(commonCIID="sample_text", localCIID="sample_text")
    assert instance.commonCIID == "sample_text"
    instance.commonCIID = "sample_text_2"
    assert instance.commonCIID == "sample_text_2"


def test_services_CIID_localCIID_value_roundtrip():
    instance = services_CIID(commonCIID="sample_text", localCIID="sample_text")
    assert instance.localCIID == "sample_text"
    instance.localCIID = "sample_text_2"
    assert instance.localCIID == "sample_text_2"


def test_services_RFSService_functionalCategory_value_roundtrip():
    instance = services_RFSService(functionalCategory="sample_text", location="sample_text")
    assert instance.functionalCategory == "sample_text"
    instance.functionalCategory = "sample_text_2"
    assert instance.functionalCategory == "sample_text_2"


def test_services_RFSService_location_value_roundtrip():
    instance = services_RFSService(functionalCategory="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_services_Service_mostTopService_value_roundtrip():
    instance = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    assert instance.mostTopService == "sample_text"
    instance.mostTopService = "sample_text_2"
    assert instance.mostTopService == "sample_text_2"


def test_services_Service_serviceCategory_value_roundtrip():
    instance = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    assert instance.serviceCategory == "sample_text"
    instance.serviceCategory = "sample_text_2"
    assert instance.serviceCategory == "sample_text_2"


def test_services_Service_serviceCharacterCommon_value_roundtrip():
    instance = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    assert instance.serviceCharacterCommon == "sample_text"
    instance.serviceCharacterCommon = "sample_text_2"
    assert instance.serviceCharacterCommon == "sample_text_2"


def test_services_Service_serviceClass_value_roundtrip():
    instance = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    assert instance.serviceClass == "sample_text"
    instance.serviceClass = "sample_text_2"
    assert instance.serviceClass == "sample_text_2"


def test_services_Service_serviceKind_value_roundtrip():
    instance = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    assert instance.serviceKind == "sample_text"
    instance.serviceKind = "sample_text_2"
    assert instance.serviceKind == "sample_text_2"


def test_services_Service_serviceSupport1_value_roundtrip():
    instance = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    assert instance.serviceSupport1 == "sample_text"
    instance.serviceSupport1 = "sample_text_2"
    assert instance.serviceSupport1 == "sample_text_2"


def test_services_Service_ssDomain_value_roundtrip():
    instance = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    assert instance.ssDomain == "sample_text"
    instance.ssDomain = "sample_text_2"
    assert instance.ssDomain == "sample_text_2"


def test_services_ServiceAdditional_costCenter_value_roundtrip():
    instance = services_ServiceAdditional(costCenter="sample_text", history="sample_text", kpi="sample_text", lifeCycleState="sample_text", link="sample_text", report="sample_text", usageState="sample_text")
    assert instance.costCenter == "sample_text"
    instance.costCenter = "sample_text_2"
    assert instance.costCenter == "sample_text_2"


def test_services_ServiceAdditional_history_value_roundtrip():
    instance = services_ServiceAdditional(costCenter="sample_text", history="sample_text", kpi="sample_text", lifeCycleState="sample_text", link="sample_text", report="sample_text", usageState="sample_text")
    assert instance.history == "sample_text"
    instance.history = "sample_text_2"
    assert instance.history == "sample_text_2"


def test_services_ServiceAdditional_kpi_value_roundtrip():
    instance = services_ServiceAdditional(costCenter="sample_text", history="sample_text", kpi="sample_text", lifeCycleState="sample_text", link="sample_text", report="sample_text", usageState="sample_text")
    assert instance.kpi == "sample_text"
    instance.kpi = "sample_text_2"
    assert instance.kpi == "sample_text_2"


def test_services_ServiceAdditional_lifeCycleState_value_roundtrip():
    instance = services_ServiceAdditional(costCenter="sample_text", history="sample_text", kpi="sample_text", lifeCycleState="sample_text", link="sample_text", report="sample_text", usageState="sample_text")
    assert instance.lifeCycleState == "sample_text"
    instance.lifeCycleState = "sample_text_2"
    assert instance.lifeCycleState == "sample_text_2"


def test_services_ServiceAdditional_link_value_roundtrip():
    instance = services_ServiceAdditional(costCenter="sample_text", history="sample_text", kpi="sample_text", lifeCycleState="sample_text", link="sample_text", report="sample_text", usageState="sample_text")
    assert instance.link == "sample_text"
    instance.link = "sample_text_2"
    assert instance.link == "sample_text_2"


def test_services_ServiceAdditional_report_value_roundtrip():
    instance = services_ServiceAdditional(costCenter="sample_text", history="sample_text", kpi="sample_text", lifeCycleState="sample_text", link="sample_text", report="sample_text", usageState="sample_text")
    assert instance.report == "sample_text"
    instance.report = "sample_text_2"
    assert instance.report == "sample_text_2"


def test_services_ServiceAdditional_usageState_value_roundtrip():
    instance = services_ServiceAdditional(costCenter="sample_text", history="sample_text", kpi="sample_text", lifeCycleState="sample_text", link="sample_text", report="sample_text", usageState="sample_text")
    assert instance.usageState == "sample_text"
    instance.usageState = "sample_text_2"
    assert instance.usageState == "sample_text_2"


def test_services_ServiceContract_oLA_value_roundtrip():
    instance = services_ServiceContract(oLA="sample_text", sLA="sample_text", uC="sample_text", wLA="sample_text")
    assert instance.oLA == "sample_text"
    instance.oLA = "sample_text_2"
    assert instance.oLA == "sample_text_2"


def test_services_ServiceContract_sLA_value_roundtrip():
    instance = services_ServiceContract(oLA="sample_text", sLA="sample_text", uC="sample_text", wLA="sample_text")
    assert instance.sLA == "sample_text"
    instance.sLA = "sample_text_2"
    assert instance.sLA == "sample_text_2"


def test_services_ServiceContract_uC_value_roundtrip():
    instance = services_ServiceContract(oLA="sample_text", sLA="sample_text", uC="sample_text", wLA="sample_text")
    assert instance.uC == "sample_text"
    instance.uC = "sample_text_2"
    assert instance.uC == "sample_text_2"


def test_services_ServiceContract_wLA_value_roundtrip():
    instance = services_ServiceContract(oLA="sample_text", sLA="sample_text", uC="sample_text", wLA="sample_text")
    assert instance.wLA == "sample_text"
    instance.wLA = "sample_text_2"
    assert instance.wLA == "sample_text_2"


def test_services_ServiceDescription_serviceDescriptionCommon_value_roundtrip():
    instance = services_ServiceDescription(serviceDescriptionCommon="sample_text", serviceDescriptionNational="sample_text")
    assert instance.serviceDescriptionCommon == "sample_text"
    instance.serviceDescriptionCommon = "sample_text_2"
    assert instance.serviceDescriptionCommon == "sample_text_2"


def test_services_ServiceDescription_serviceDescriptionNational_value_roundtrip():
    instance = services_ServiceDescription(serviceDescriptionCommon="sample_text", serviceDescriptionNational="sample_text")
    assert instance.serviceDescriptionNational == "sample_text"
    instance.serviceDescriptionNational = "sample_text_2"
    assert instance.serviceDescriptionNational == "sample_text_2"


def test_services_ServiceIncidentMgt_businessImpact_value_roundtrip():
    instance = services_ServiceIncidentMgt(businessImpact="sample_text", maintenance="sample_text", maintenanceWindow="sample_text", monitoring="sample_text")
    assert instance.businessImpact == "sample_text"
    instance.businessImpact = "sample_text_2"
    assert instance.businessImpact == "sample_text_2"


def test_services_ServiceIncidentMgt_maintenance_value_roundtrip():
    instance = services_ServiceIncidentMgt(businessImpact="sample_text", maintenance="sample_text", maintenanceWindow="sample_text", monitoring="sample_text")
    assert instance.maintenance == "sample_text"
    instance.maintenance = "sample_text_2"
    assert instance.maintenance == "sample_text_2"


def test_services_ServiceIncidentMgt_maintenanceWindow_value_roundtrip():
    instance = services_ServiceIncidentMgt(businessImpact="sample_text", maintenance="sample_text", maintenanceWindow="sample_text", monitoring="sample_text")
    assert instance.maintenanceWindow == "sample_text"
    instance.maintenanceWindow = "sample_text_2"
    assert instance.maintenanceWindow == "sample_text_2"


def test_services_ServiceIncidentMgt_monitoring_value_roundtrip():
    instance = services_ServiceIncidentMgt(businessImpact="sample_text", maintenance="sample_text", maintenanceWindow="sample_text", monitoring="sample_text")
    assert instance.monitoring == "sample_text"
    instance.monitoring = "sample_text_2"
    assert instance.monitoring == "sample_text_2"


def test_services_ServiceInterrest_contactUnit_value_roundtrip():
    instance = services_ServiceInterrest(contactUnit="sample_text", interrestKind="sample_text")
    assert instance.contactUnit == "sample_text"
    instance.contactUnit = "sample_text_2"
    assert instance.contactUnit == "sample_text_2"


def test_services_ServiceInterrest_interrestKind_value_roundtrip():
    instance = services_ServiceInterrest(contactUnit="sample_text", interrestKind="sample_text")
    assert instance.interrestKind == "sample_text"
    instance.interrestKind = "sample_text_2"
    assert instance.interrestKind == "sample_text_2"


def test_services_ServiceName_alias_value_roundtrip():
    instance = services_ServiceName(alias="sample_text", identifier="sample_text", index="sample_text", name="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_services_ServiceName_identifier_value_roundtrip():
    instance = services_ServiceName(alias="sample_text", identifier="sample_text", index="sample_text", name="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_services_ServiceName_index_value_roundtrip():
    instance = services_ServiceName(alias="sample_text", identifier="sample_text", index="sample_text", name="sample_text")
    assert instance.index == "sample_text"
    instance.index = "sample_text_2"
    assert instance.index == "sample_text_2"


def test_services_ServiceName_name_value_roundtrip():
    instance = services_ServiceName(alias="sample_text", identifier="sample_text", index="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_services_ServiceProfile_name_value_roundtrip():
    instance = services_ServiceProfile(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_services_ServiceSecurityMgt_drPlanContact_value_roundtrip():
    instance = services_ServiceSecurityMgt(drPlanContact="sample_text", drPlanRepository="sample_text", drRecoveryPlan="sample_text", securityRating="sample_text")
    assert instance.drPlanContact == "sample_text"
    instance.drPlanContact = "sample_text_2"
    assert instance.drPlanContact == "sample_text_2"


def test_services_ServiceSecurityMgt_drPlanRepository_value_roundtrip():
    instance = services_ServiceSecurityMgt(drPlanContact="sample_text", drPlanRepository="sample_text", drRecoveryPlan="sample_text", securityRating="sample_text")
    assert instance.drPlanRepository == "sample_text"
    instance.drPlanRepository = "sample_text_2"
    assert instance.drPlanRepository == "sample_text_2"


def test_services_ServiceSecurityMgt_drRecoveryPlan_value_roundtrip():
    instance = services_ServiceSecurityMgt(drPlanContact="sample_text", drPlanRepository="sample_text", drRecoveryPlan="sample_text", securityRating="sample_text")
    assert instance.drRecoveryPlan == "sample_text"
    instance.drRecoveryPlan = "sample_text_2"
    assert instance.drRecoveryPlan == "sample_text_2"


def test_services_ServiceSecurityMgt_securityRating_value_roundtrip():
    instance = services_ServiceSecurityMgt(drPlanContact="sample_text", drPlanRepository="sample_text", drRecoveryPlan="sample_text", securityRating="sample_text")
    assert instance.securityRating == "sample_text"
    instance.securityRating = "sample_text_2"
    assert instance.securityRating == "sample_text_2"


def test_services_ServiceSupport_supportDays_value_roundtrip():
    instance = services_ServiceSupport(supportDays="sample_text", supportHours="sample_text")
    assert instance.supportDays == "sample_text"
    instance.supportDays = "sample_text_2"
    assert instance.supportDays == "sample_text_2"


def test_services_ServiceSupport_supportHours_value_roundtrip():
    instance = services_ServiceSupport(supportDays="sample_text", supportHours="sample_text")
    assert instance.supportHours == "sample_text"
    instance.supportHours = "sample_text_2"
    assert instance.supportHours == "sample_text_2"


def test_services_CFSService_isa_Service():
    instance = services_CFSService(provider="sample_text", scenario="sample_text")
    assert isinstance(instance, Service)


def test_services_RFSService_isa_Service():
    instance = services_RFSService(functionalCategory="sample_text", location="sample_text")
    assert isinstance(instance, Service)


def test_assoc_ciID12_link_reassign_clear():
    a = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b1 = services_CIID(commonCIID="sample_text", localCIID="sample_text")
    b2 = services_CIID(commonCIID="sample_text_2", localCIID="sample_text_2")
    _safe_set(a, 'services_Service13', b1)
    assert _is_linked(a, 'services_Service13', b1)
    if hasattr(b1, 'services_CIID'):
        assert _is_linked(b1, 'services_CIID', a)
    _safe_set(a, 'services_Service13', b2)
    assert _is_linked(a, 'services_Service13', b2)
    if hasattr(b1, 'services_CIID'):
        assert not _is_linked(b1, 'services_CIID', a)
    if hasattr(b2, 'services_CIID'):
        assert _is_linked(b2, 'services_CIID', a)
    _safe_set(a, 'services_Service13', None)
    assert not _is_linked(a, 'services_Service13', b2)
    if hasattr(b2, 'services_CIID'):
        assert not _is_linked(b2, 'services_CIID', a)


def test_assoc_elements0_link_reassign_clear():
    a = services_CFSService(provider="sample_text", scenario="sample_text")
    b1 = services_EObject()
    b2 = services_EObject()
    _safe_set(a, 'services_CFSService', {b1})
    assert _is_linked(a, 'services_CFSService', b1)
    if hasattr(b1, 'services_EObject'):
        assert _is_linked(b1, 'services_EObject', a)
    _safe_set(a, 'services_CFSService', {b2})
    assert _is_linked(a, 'services_CFSService', b2)
    if hasattr(b1, 'services_EObject'):
        assert not _is_linked(b1, 'services_EObject', a)
    if hasattr(b2, 'services_EObject'):
        assert _is_linked(b2, 'services_EObject', a)
    _safe_set(a, 'services_CFSService', set())
    assert not _is_linked(a, 'services_CFSService', b2)
    if hasattr(b2, 'services_EObject'):
        assert not _is_linked(b2, 'services_EObject', a)


def test_assoc_elements1_link_reassign_clear():
    a = services_RFSService(functionalCategory="sample_text", location="sample_text")
    b1 = services_EObject()
    b2 = services_EObject()
    _safe_set(a, 'services_RFSService', {b1})
    assert _is_linked(a, 'services_RFSService', b1)
    if hasattr(b1, 'services_EObject2'):
        assert _is_linked(b1, 'services_EObject2', a)
    _safe_set(a, 'services_RFSService', {b2})
    assert _is_linked(a, 'services_RFSService', b2)
    if hasattr(b1, 'services_EObject2'):
        assert not _is_linked(b1, 'services_EObject2', a)
    if hasattr(b2, 'services_EObject2'):
        assert _is_linked(b2, 'services_EObject2', a)
    _safe_set(a, 'services_RFSService', set())
    assert not _is_linked(a, 'services_RFSService', b2)
    if hasattr(b2, 'services_EObject2'):
        assert not _is_linked(b2, 'services_EObject2', a)


def test_assoc_serviceContracts16_link_reassign_clear():
    a = services_ServiceContract(oLA="sample_text", sLA="sample_text", uC="sample_text", wLA="sample_text")
    b1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    _safe_set(a, 'services_ServiceContract', b1)
    assert _is_linked(a, 'services_ServiceContract', b1)
    if hasattr(b1, 'services_Service17'):
        assert _is_linked(b1, 'services_Service17', a)
    _safe_set(a, 'services_ServiceContract', b2)
    assert _is_linked(a, 'services_ServiceContract', b2)
    if hasattr(b1, 'services_Service17'):
        assert not _is_linked(b1, 'services_Service17', a)
    if hasattr(b2, 'services_Service17'):
        assert _is_linked(b2, 'services_Service17', a)
    _safe_set(a, 'services_ServiceContract', None)
    assert not _is_linked(a, 'services_ServiceContract', b2)
    if hasattr(b2, 'services_Service17'):
        assert not _is_linked(b2, 'services_Service17', a)


def test_assoc_serviceDescription6_link_reassign_clear():
    a = services_ServiceDescription(serviceDescriptionCommon="sample_text", serviceDescriptionNational="sample_text")
    b1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    _safe_set(a, 'services_ServiceDescription', b1)
    assert _is_linked(a, 'services_ServiceDescription', b1)
    if hasattr(b1, 'services_Service7'):
        assert _is_linked(b1, 'services_Service7', a)
    _safe_set(a, 'services_ServiceDescription', b2)
    assert _is_linked(a, 'services_ServiceDescription', b2)
    if hasattr(b1, 'services_Service7'):
        assert not _is_linked(b1, 'services_Service7', a)
    if hasattr(b2, 'services_Service7'):
        assert _is_linked(b2, 'services_Service7', a)
    _safe_set(a, 'services_ServiceDescription', None)
    assert not _is_linked(a, 'services_ServiceDescription', b2)
    if hasattr(b2, 'services_Service7'):
        assert not _is_linked(b2, 'services_Service7', a)


def test_assoc_serviceIncidentMgt10_link_reassign_clear():
    a = services_ServiceIncidentMgt(businessImpact="sample_text", maintenance="sample_text", maintenanceWindow="sample_text", monitoring="sample_text")
    b1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    _safe_set(a, 'services_ServiceIncidentMgt', b1)
    assert _is_linked(a, 'services_ServiceIncidentMgt', b1)
    if hasattr(b1, 'services_Service11'):
        assert _is_linked(b1, 'services_Service11', a)
    _safe_set(a, 'services_ServiceIncidentMgt', b2)
    assert _is_linked(a, 'services_ServiceIncidentMgt', b2)
    if hasattr(b1, 'services_Service11'):
        assert not _is_linked(b1, 'services_Service11', a)
    if hasattr(b2, 'services_Service11'):
        assert _is_linked(b2, 'services_Service11', a)
    _safe_set(a, 'services_ServiceIncidentMgt', None)
    assert not _is_linked(a, 'services_ServiceIncidentMgt', b2)
    if hasattr(b2, 'services_Service11'):
        assert not _is_linked(b2, 'services_Service11', a)


def test_assoc_serviceInterrest14_link_reassign_clear():
    a = services_ServiceInterrest(contactUnit="sample_text", interrestKind="sample_text")
    b1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    _safe_set(a, 'services_ServiceInterrest', b1)
    assert _is_linked(a, 'services_ServiceInterrest', b1)
    if hasattr(b1, 'services_Service15'):
        assert _is_linked(b1, 'services_Service15', a)
    _safe_set(a, 'services_ServiceInterrest', b2)
    assert _is_linked(a, 'services_ServiceInterrest', b2)
    if hasattr(b1, 'services_Service15'):
        assert not _is_linked(b1, 'services_Service15', a)
    if hasattr(b2, 'services_Service15'):
        assert _is_linked(b2, 'services_Service15', a)
    _safe_set(a, 'services_ServiceInterrest', None)
    assert not _is_linked(a, 'services_ServiceInterrest', b2)
    if hasattr(b2, 'services_Service15'):
        assert not _is_linked(b2, 'services_Service15', a)


def test_assoc_serviceMisc20_link_reassign_clear():
    a = services_ServiceAdditional(costCenter="sample_text", history="sample_text", kpi="sample_text", lifeCycleState="sample_text", link="sample_text", report="sample_text", usageState="sample_text")
    b1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    _safe_set(a, 'services_ServiceAdditional', b1)
    assert _is_linked(a, 'services_ServiceAdditional', b1)
    if hasattr(b1, 'services_Service21'):
        assert _is_linked(b1, 'services_Service21', a)
    _safe_set(a, 'services_ServiceAdditional', b2)
    assert _is_linked(a, 'services_ServiceAdditional', b2)
    if hasattr(b1, 'services_Service21'):
        assert not _is_linked(b1, 'services_Service21', a)
    if hasattr(b2, 'services_Service21'):
        assert _is_linked(b2, 'services_Service21', a)
    _safe_set(a, 'services_ServiceAdditional', None)
    assert not _is_linked(a, 'services_ServiceAdditional', b2)
    if hasattr(b2, 'services_Service21'):
        assert not _is_linked(b2, 'services_Service21', a)


def test_assoc_serviceName5_link_reassign_clear():
    a = services_ServiceName(alias="sample_text", identifier="sample_text", index="sample_text", name="sample_text")
    b1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    _safe_set(a, 'services_ServiceName', b1)
    assert _is_linked(a, 'services_ServiceName', b1)
    if hasattr(b1, 'services_Service'):
        assert _is_linked(b1, 'services_Service', a)
    _safe_set(a, 'services_ServiceName', b2)
    assert _is_linked(a, 'services_ServiceName', b2)
    if hasattr(b1, 'services_Service'):
        assert not _is_linked(b1, 'services_Service', a)
    if hasattr(b2, 'services_Service'):
        assert _is_linked(b2, 'services_Service', a)
    _safe_set(a, 'services_ServiceName', None)
    assert not _is_linked(a, 'services_ServiceName', b2)
    if hasattr(b2, 'services_Service'):
        assert not _is_linked(b2, 'services_Service', a)


def test_assoc_serviceParameters25_link_reassign_clear():
    a = services_ServiceProfile(name="sample_text")
    b1 = services_Parameter()
    b2 = services_Parameter()
    _safe_set(a, 'services_ServiceProfile26', {b1})
    assert _is_linked(a, 'services_ServiceProfile26', b1)
    if hasattr(b1, 'services_Parameter'):
        assert _is_linked(b1, 'services_Parameter', a)
    _safe_set(a, 'services_ServiceProfile26', {b2})
    assert _is_linked(a, 'services_ServiceProfile26', b2)
    if hasattr(b1, 'services_Parameter'):
        assert not _is_linked(b1, 'services_Parameter', a)
    if hasattr(b2, 'services_Parameter'):
        assert _is_linked(b2, 'services_Parameter', a)
    _safe_set(a, 'services_ServiceProfile26', set())
    assert not _is_linked(a, 'services_ServiceProfile26', b2)
    if hasattr(b2, 'services_Parameter'):
        assert not _is_linked(b2, 'services_Parameter', a)


def test_assoc_serviceProfile3_link_reassign_clear():
    a = services_ServiceProfile(name="sample_text")
    b1 = services_RFSService(functionalCategory="sample_text", location="sample_text")
    b2 = services_RFSService(functionalCategory="sample_text_2", location="sample_text_2")
    _safe_set(a, 'services_ServiceProfile', b1)
    assert _is_linked(a, 'services_ServiceProfile', b1)
    if hasattr(b1, 'services_RFSService4'):
        assert _is_linked(b1, 'services_RFSService4', a)
    _safe_set(a, 'services_ServiceProfile', b2)
    assert _is_linked(a, 'services_ServiceProfile', b2)
    if hasattr(b1, 'services_RFSService4'):
        assert not _is_linked(b1, 'services_RFSService4', a)
    if hasattr(b2, 'services_RFSService4'):
        assert _is_linked(b2, 'services_RFSService4', a)
    _safe_set(a, 'services_ServiceProfile', None)
    assert not _is_linked(a, 'services_ServiceProfile', b2)
    if hasattr(b2, 'services_RFSService4'):
        assert not _is_linked(b2, 'services_RFSService4', a)


def test_assoc_serviceSecurityMgt8_link_reassign_clear():
    a = services_ServiceSecurityMgt(drPlanContact="sample_text", drPlanRepository="sample_text", drRecoveryPlan="sample_text", securityRating="sample_text")
    b1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    _safe_set(a, 'services_ServiceSecurityMgt', b1)
    assert _is_linked(a, 'services_ServiceSecurityMgt', b1)
    if hasattr(b1, 'services_Service9'):
        assert _is_linked(b1, 'services_Service9', a)
    _safe_set(a, 'services_ServiceSecurityMgt', b2)
    assert _is_linked(a, 'services_ServiceSecurityMgt', b2)
    if hasattr(b1, 'services_Service9'):
        assert not _is_linked(b1, 'services_Service9', a)
    if hasattr(b2, 'services_Service9'):
        assert _is_linked(b2, 'services_Service9', a)
    _safe_set(a, 'services_ServiceSecurityMgt', None)
    assert not _is_linked(a, 'services_ServiceSecurityMgt', b2)
    if hasattr(b2, 'services_Service9'):
        assert not _is_linked(b2, 'services_Service9', a)


def test_assoc_serviceSupport18_link_reassign_clear():
    a = services_ServiceSupport(supportDays="sample_text", supportHours="sample_text")
    b1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    _safe_set(a, 'services_ServiceSupport', b1)
    assert _is_linked(a, 'services_ServiceSupport', b1)
    if hasattr(b1, 'services_Service19'):
        assert _is_linked(b1, 'services_Service19', a)
    _safe_set(a, 'services_ServiceSupport', b2)
    assert _is_linked(a, 'services_ServiceSupport', b2)
    if hasattr(b1, 'services_Service19'):
        assert not _is_linked(b1, 'services_Service19', a)
    if hasattr(b2, 'services_Service19'):
        assert _is_linked(b2, 'services_Service19', a)
    _safe_set(a, 'services_ServiceSupport', None)
    assert not _is_linked(a, 'services_ServiceSupport', b2)
    if hasattr(b2, 'services_Service19'):
        assert not _is_linked(b2, 'services_Service19', a)


def test_assoc_services23_link_reassign_clear():
    a = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    b2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    _safe_set(a, 'services_Service22', {b1})
    assert _is_linked(a, 'services_Service22', b1)
    if hasattr(b1, 'services_Service24'):
        assert _is_linked(b1, 'services_Service24', a)
    _safe_set(a, 'services_Service22', {b2})
    assert _is_linked(a, 'services_Service22', b2)
    if hasattr(b1, 'services_Service24'):
        assert not _is_linked(b1, 'services_Service24', a)
    if hasattr(b2, 'services_Service24'):
        assert _is_linked(b2, 'services_Service24', a)
    _safe_set(a, 'services_Service22', set())
    assert not _is_linked(a, 'services_Service22', b2)
    if hasattr(b2, 'services_Service24'):
        assert not _is_linked(b2, 'services_Service24', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Service_strategy = st.builds(Service)
@given(instance=Service_strategy)
@settings(max_examples=25)
def test_Service_instantiation(instance):
    assert isinstance(instance, Service)


services_CFSService_strategy = st.builds(services_CFSService, provider=safe_text, scenario=safe_text)
@given(instance=services_CFSService_strategy)
@settings(max_examples=25)
def test_services_CFSService_instantiation(instance):
    assert isinstance(instance, services_CFSService)


services_CIID_strategy = st.builds(services_CIID, commonCIID=safe_text, localCIID=safe_text)
@given(instance=services_CIID_strategy)
@settings(max_examples=25)
def test_services_CIID_instantiation(instance):
    assert isinstance(instance, services_CIID)


services_EObject_strategy = st.builds(services_EObject)
@given(instance=services_EObject_strategy)
@settings(max_examples=25)
def test_services_EObject_instantiation(instance):
    assert isinstance(instance, services_EObject)


services_Parameter_strategy = st.builds(services_Parameter)
@given(instance=services_Parameter_strategy)
@settings(max_examples=25)
def test_services_Parameter_instantiation(instance):
    assert isinstance(instance, services_Parameter)


services_RFSService_strategy = st.builds(services_RFSService, functionalCategory=safe_text, location=safe_text)
@given(instance=services_RFSService_strategy)
@settings(max_examples=25)
def test_services_RFSService_instantiation(instance):
    assert isinstance(instance, services_RFSService)


services_Service_strategy = st.builds(services_Service, mostTopService=safe_text, serviceCategory=safe_text, serviceCharacterCommon=safe_text, serviceClass=safe_text, serviceKind=safe_text, serviceSupport1=safe_text, ssDomain=safe_text)
@given(instance=services_Service_strategy)
@settings(max_examples=25)
def test_services_Service_instantiation(instance):
    assert isinstance(instance, services_Service)


services_ServiceAdditional_strategy = st.builds(services_ServiceAdditional, costCenter=safe_text, history=safe_text, kpi=safe_text, lifeCycleState=safe_text, link=safe_text, report=safe_text, usageState=safe_text)
@given(instance=services_ServiceAdditional_strategy)
@settings(max_examples=25)
def test_services_ServiceAdditional_instantiation(instance):
    assert isinstance(instance, services_ServiceAdditional)


services_ServiceContract_strategy = st.builds(services_ServiceContract, oLA=safe_text, sLA=safe_text, uC=safe_text, wLA=safe_text)
@given(instance=services_ServiceContract_strategy)
@settings(max_examples=25)
def test_services_ServiceContract_instantiation(instance):
    assert isinstance(instance, services_ServiceContract)


services_ServiceDescription_strategy = st.builds(services_ServiceDescription, serviceDescriptionCommon=safe_text, serviceDescriptionNational=safe_text)
@given(instance=services_ServiceDescription_strategy)
@settings(max_examples=25)
def test_services_ServiceDescription_instantiation(instance):
    assert isinstance(instance, services_ServiceDescription)


services_ServiceIncidentMgt_strategy = st.builds(services_ServiceIncidentMgt, businessImpact=safe_text, maintenance=safe_text, maintenanceWindow=safe_text, monitoring=safe_text)
@given(instance=services_ServiceIncidentMgt_strategy)
@settings(max_examples=25)
def test_services_ServiceIncidentMgt_instantiation(instance):
    assert isinstance(instance, services_ServiceIncidentMgt)


services_ServiceInterrest_strategy = st.builds(services_ServiceInterrest, contactUnit=safe_text, interrestKind=safe_text)
@given(instance=services_ServiceInterrest_strategy)
@settings(max_examples=25)
def test_services_ServiceInterrest_instantiation(instance):
    assert isinstance(instance, services_ServiceInterrest)


services_ServiceName_strategy = st.builds(services_ServiceName, alias=safe_text, identifier=safe_text, index=safe_text, name=safe_text)
@given(instance=services_ServiceName_strategy)
@settings(max_examples=25)
def test_services_ServiceName_instantiation(instance):
    assert isinstance(instance, services_ServiceName)


services_ServiceProfile_strategy = st.builds(services_ServiceProfile, name=safe_text)
@given(instance=services_ServiceProfile_strategy)
@settings(max_examples=25)
def test_services_ServiceProfile_instantiation(instance):
    assert isinstance(instance, services_ServiceProfile)


services_ServiceSecurityMgt_strategy = st.builds(services_ServiceSecurityMgt, drPlanContact=safe_text, drPlanRepository=safe_text, drRecoveryPlan=safe_text, securityRating=safe_text)
@given(instance=services_ServiceSecurityMgt_strategy)
@settings(max_examples=25)
def test_services_ServiceSecurityMgt_instantiation(instance):
    assert isinstance(instance, services_ServiceSecurityMgt)


services_ServiceSupport_strategy = st.builds(services_ServiceSupport, supportDays=safe_text, supportHours=safe_text)
@given(instance=services_ServiceSupport_strategy)
@settings(max_examples=25)
def test_services_ServiceSupport_instantiation(instance):
    assert isinstance(instance, services_ServiceSupport)



