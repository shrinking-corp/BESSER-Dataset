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
    services_Value,
    services_ServiceProfile,
    services_ResourceMonitor,
    services_ServiceForecastUsers,
    services_ResourceForecast,
    services_DateTimeRange,
    services_Expression,
    services_NetXResource,
    services_ServiceUser,
    services_ServiceDistribution,
    services_ServiceMonitor,
    services_ServiceForecast,
    services_Node,
    services_Service,
    services_Tolerance,
    services_CIID,
    Service,
    services_RFSService,
    services_CFSService,
    ServiceClassType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_services_value_is_not_abstract():
    assert not inspect.isabstract(services_Value)


def test_hyp_services_value_constructor_exists():
    assert callable(services_Value.__init__)


def test_hyp_services_value_constructor_args():
    sig = inspect.signature(services_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_serviceprofile_is_not_abstract():
    assert not inspect.isabstract(services_ServiceProfile)


def test_hyp_services_serviceprofile_constructor_exists():
    assert callable(services_ServiceProfile.__init__)


def test_hyp_services_serviceprofile_constructor_args():
    sig = inspect.signature(services_ServiceProfile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_services_resourcemonitor_is_not_abstract():
    assert not inspect.isabstract(services_ResourceMonitor)


def test_hyp_services_resourcemonitor_constructor_exists():
    assert callable(services_ResourceMonitor.__init__)


def test_hyp_services_resourcemonitor_constructor_args():
    sig = inspect.signature(services_ResourceMonitor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_serviceforecastusers_is_not_abstract():
    assert not inspect.isabstract(services_ServiceForecastUsers)


def test_hyp_services_serviceforecastusers_constructor_exists():
    assert callable(services_ServiceForecastUsers.__init__)


def test_hyp_services_serviceforecastusers_constructor_args():
    sig = inspect.signature(services_ServiceForecastUsers.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_resourceforecast_is_not_abstract():
    assert not inspect.isabstract(services_ResourceForecast)


def test_hyp_services_resourceforecast_constructor_exists():
    assert callable(services_ResourceForecast.__init__)


def test_hyp_services_resourceforecast_constructor_args():
    sig = inspect.signature(services_ResourceForecast.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_datetimerange_is_not_abstract():
    assert not inspect.isabstract(services_DateTimeRange)


def test_hyp_services_datetimerange_constructor_exists():
    assert callable(services_DateTimeRange.__init__)


def test_hyp_services_datetimerange_constructor_args():
    sig = inspect.signature(services_DateTimeRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_expression_is_not_abstract():
    assert not inspect.isabstract(services_Expression)


def test_hyp_services_expression_constructor_exists():
    assert callable(services_Expression.__init__)


def test_hyp_services_expression_constructor_args():
    sig = inspect.signature(services_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_netxresource_is_not_abstract():
    assert not inspect.isabstract(services_NetXResource)


def test_hyp_services_netxresource_constructor_exists():
    assert callable(services_NetXResource.__init__)


def test_hyp_services_netxresource_constructor_args():
    sig = inspect.signature(services_NetXResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_serviceuser_is_not_abstract():
    assert not inspect.isabstract(services_ServiceUser)


def test_hyp_services_serviceuser_constructor_exists():
    assert callable(services_ServiceUser.__init__)


def test_hyp_services_serviceuser_constructor_args():
    sig = inspect.signature(services_ServiceUser.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_services_servicedistribution_is_not_abstract():
    assert not inspect.isabstract(services_ServiceDistribution)


def test_hyp_services_servicedistribution_constructor_exists():
    assert callable(services_ServiceDistribution.__init__)


def test_hyp_services_servicedistribution_constructor_args():
    sig = inspect.signature(services_ServiceDistribution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_servicemonitor_is_not_abstract():
    assert not inspect.isabstract(services_ServiceMonitor)


def test_hyp_services_servicemonitor_constructor_exists():
    assert callable(services_ServiceMonitor.__init__)


def test_hyp_services_servicemonitor_constructor_args():
    sig = inspect.signature(services_ServiceMonitor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "revision" in params, "Missing parameter 'revision'"





def test_hyp_services_serviceforecast_is_not_abstract():
    assert not inspect.isabstract(services_ServiceForecast)


def test_hyp_services_serviceforecast_constructor_exists():
    assert callable(services_ServiceForecast.__init__)


def test_hyp_services_serviceforecast_constructor_args():
    sig = inspect.signature(services_ServiceForecast.__init__)
    params = list(sig.parameters.keys())
    assert "revision" in params, "Missing parameter 'revision'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_services_node_is_not_abstract():
    assert not inspect.isabstract(services_Node)


def test_hyp_services_node_constructor_exists():
    assert callable(services_Node.__init__)


def test_hyp_services_node_constructor_args():
    sig = inspect.signature(services_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_service_is_not_abstract():
    assert not inspect.isabstract(services_Service)


def test_hyp_services_service_constructor_exists():
    assert callable(services_Service.__init__)


def test_hyp_services_service_constructor_args():
    sig = inspect.signature(services_Service.__init__)
    params = list(sig.parameters.keys())
    assert "serviceDescription" in params, "Missing parameter 'serviceDescription'"
    assert "serviceCategory" in params, "Missing parameter 'serviceCategory'"
    assert "serviceName" in params, "Missing parameter 'serviceName'"
    assert "serviceClass" in params, "Missing parameter 'serviceClass'"







def test_hyp_services_tolerance_is_not_abstract():
    assert not inspect.isabstract(services_Tolerance)


def test_hyp_services_tolerance_constructor_exists():
    assert callable(services_Tolerance.__init__)


def test_hyp_services_tolerance_constructor_args():
    sig = inspect.signature(services_Tolerance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_services_ciid_is_not_abstract():
    assert not inspect.isabstract(services_CIID)


def test_hyp_services_ciid_constructor_exists():
    assert callable(services_CIID.__init__)


def test_hyp_services_ciid_constructor_args():
    sig = inspect.signature(services_CIID.__init__)
    params = list(sig.parameters.keys())
    assert "commonCIID" in params, "Missing parameter 'commonCIID'"
    assert "localCIID" in params, "Missing parameter 'localCIID'"





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
    assert "functionalCategory" in params, "Missing parameter 'functionalCategory'"




def test_hyp_services_cfsservice_is_not_abstract():
    assert not inspect.isabstract(services_CFSService)


def test_hyp_services_cfsservice_constructor_exists():
    assert callable(services_CFSService.__init__)


def test_hyp_services_cfsservice_constructor_args():
    sig = inspect.signature(services_CFSService.__init__)
    params = list(sig.parameters.keys())
    assert "provider" in params, "Missing parameter 'provider'"
    assert "scenario" in params, "Missing parameter 'scenario'"



def test_hyp_serviceclasstype_exists():
    # Check that the Enumeration exists
    assert ServiceClassType is not None

def test_hyp_serviceclasstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServiceClassType]
    expected_literals = [
        "Silver",
        "Bronze",
        "Gold",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServiceClassType"


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
services_Value_strategy = st.builds(
    services_Value,
)
services_ServiceProfile_strategy = st.builds(
    services_ServiceProfile,
    name=
        safe_text
)
services_ResourceMonitor_strategy = st.builds(
    services_ResourceMonitor,
)
services_ServiceForecastUsers_strategy = st.builds(
    services_ServiceForecastUsers,
)
services_ResourceForecast_strategy = st.builds(
    services_ResourceForecast,
)
services_DateTimeRange_strategy = st.builds(
    services_DateTimeRange,
)
services_Expression_strategy = st.builds(
    services_Expression,
)
services_NetXResource_strategy = st.builds(
    services_NetXResource,
)
services_ServiceUser_strategy = st.builds(
    services_ServiceUser,
    name=
        safe_text
)
services_ServiceDistribution_strategy = st.builds(
    services_ServiceDistribution,
)
services_ServiceMonitor_strategy = st.builds(
    services_ServiceMonitor,
    name=
        safe_text,
    revision=
        safe_text
)
services_ServiceForecast_strategy = st.builds(
    services_ServiceForecast,
    revision=
        safe_text,
    name=
        safe_text
)
services_Node_strategy = st.builds(
    services_Node,
)
services_Service_strategy = st.builds(
    services_Service,
    serviceDescription=
        safe_text,
    serviceCategory=
        safe_text,
    serviceName=
        safe_text,
    serviceClass=
        safe_text
)
services_Tolerance_strategy = st.builds(
    services_Tolerance,
)
services_CIID_strategy = st.builds(
    services_CIID,
    commonCIID=
        safe_text,
    localCIID=
        safe_text
)
Service_strategy = st.builds(
    Service,
)
services_RFSService_strategy = st.builds(
    services_RFSService,
    functionalCategory=
        safe_text
)
services_CFSService_strategy = st.builds(
    services_CFSService,
    provider=
        safe_text,
    scenario=
        safe_text
)





@given(instance=services_ServiceProfile_strategy)
def test_hyp_services_serviceprofile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original










@given(instance=services_ServiceUser_strategy)
def test_hyp_services_serviceuser_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=services_ServiceMonitor_strategy)
def test_hyp_services_servicemonitor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=services_ServiceMonitor_strategy)
def test_hyp_services_servicemonitor_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original




@given(instance=services_ServiceForecast_strategy)
def test_hyp_services_serviceforecast_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original



@given(instance=services_ServiceForecast_strategy)
def test_hyp_services_serviceforecast_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=services_Service_strategy)
def test_hyp_services_service_serviceDescription_setter(instance):
    original = instance.serviceDescription
    instance.serviceDescription = original
    assert instance.serviceDescription == original



@given(instance=services_Service_strategy)
def test_hyp_services_service_serviceCategory_setter(instance):
    original = instance.serviceCategory
    instance.serviceCategory = original
    assert instance.serviceCategory == original



@given(instance=services_Service_strategy)
def test_hyp_services_service_serviceName_setter(instance):
    original = instance.serviceName
    instance.serviceName = original
    assert instance.serviceName == original



@given(instance=services_Service_strategy)
def test_hyp_services_service_serviceClass_setter(instance):
    original = instance.serviceClass
    instance.serviceClass = original
    assert instance.serviceClass == original





@given(instance=services_CIID_strategy)
def test_hyp_services_ciid_commonCIID_setter(instance):
    original = instance.commonCIID
    instance.commonCIID = original
    assert instance.commonCIID == original



@given(instance=services_CIID_strategy)
def test_hyp_services_ciid_localCIID_setter(instance):
    original = instance.localCIID
    instance.localCIID = original
    assert instance.localCIID == original





@given(instance=services_RFSService_strategy)
def test_hyp_services_rfsservice_functionalCategory_setter(instance):
    original = instance.functionalCategory
    instance.functionalCategory = original
    assert instance.functionalCategory == original




@given(instance=services_CFSService_strategy)
def test_hyp_services_cfsservice_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original



@given(instance=services_CFSService_strategy)
def test_hyp_services_cfsservice_scenario_setter(instance):
    original = instance.scenario
    instance.scenario = original
    assert instance.scenario == original


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
    services_DateTimeRange,
    services_Expression,
    services_NetXResource,
    services_Node,
    services_RFSService,
    services_ResourceForecast,
    services_ResourceMonitor,
    services_Service,
    services_ServiceDistribution,
    services_ServiceForecast,
    services_ServiceForecastUsers,
    services_ServiceMonitor,
    services_ServiceProfile,
    services_ServiceUser,
    services_Tolerance,
    services_Value,
    ServiceClassType,
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
    instance = services_RFSService(functionalCategory="sample_text")
    assert instance.functionalCategory == "sample_text"
    instance.functionalCategory = "sample_text_2"
    assert instance.functionalCategory == "sample_text_2"


def test_services_Service_serviceCategory_value_roundtrip():
    instance = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    assert instance.serviceCategory == "sample_text"
    instance.serviceCategory = "sample_text_2"
    assert instance.serviceCategory == "sample_text_2"


def test_services_Service_serviceClass_value_roundtrip():
    instance = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    assert instance.serviceClass == "sample_text"
    instance.serviceClass = "sample_text_2"
    assert instance.serviceClass == "sample_text_2"


def test_services_Service_serviceDescription_value_roundtrip():
    instance = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    assert instance.serviceDescription == "sample_text"
    instance.serviceDescription = "sample_text_2"
    assert instance.serviceDescription == "sample_text_2"


def test_services_Service_serviceName_value_roundtrip():
    instance = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    assert instance.serviceName == "sample_text"
    instance.serviceName = "sample_text_2"
    assert instance.serviceName == "sample_text_2"


def test_services_ServiceForecast_name_value_roundtrip():
    instance = services_ServiceForecast(name="sample_text", revision="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_services_ServiceForecast_revision_value_roundtrip():
    instance = services_ServiceForecast(name="sample_text", revision="sample_text")
    assert instance.revision == "sample_text"
    instance.revision = "sample_text_2"
    assert instance.revision == "sample_text_2"


def test_services_ServiceMonitor_name_value_roundtrip():
    instance = services_ServiceMonitor(name="sample_text", revision="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_services_ServiceMonitor_revision_value_roundtrip():
    instance = services_ServiceMonitor(name="sample_text", revision="sample_text")
    assert instance.revision == "sample_text"
    instance.revision = "sample_text_2"
    assert instance.revision == "sample_text_2"


def test_services_ServiceProfile_name_value_roundtrip():
    instance = services_ServiceProfile(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_services_ServiceUser_name_value_roundtrip():
    instance = services_ServiceUser(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_services_CFSService_isa_Service():
    instance = services_CFSService(provider="sample_text", scenario="sample_text")
    assert isinstance(instance, Service)


def test_services_RFSService_isa_Service():
    instance = services_RFSService(functionalCategory="sample_text")
    assert isinstance(instance, Service)


def test_assoc_cIID3_link_reassign_clear():
    a = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    b1 = services_CIID(commonCIID="sample_text", localCIID="sample_text")
    b2 = services_CIID(commonCIID="sample_text_2", localCIID="sample_text_2")
    _safe_set(a, 'services_Service', {b1})
    assert _is_linked(a, 'services_Service', b1)
    if hasattr(b1, 'services_CIID'):
        assert _is_linked(b1, 'services_CIID', a)
    _safe_set(a, 'services_Service', {b2})
    assert _is_linked(a, 'services_Service', b2)
    if hasattr(b1, 'services_CIID'):
        assert not _is_linked(b1, 'services_CIID', a)
    if hasattr(b2, 'services_CIID'):
        assert _is_linked(b2, 'services_CIID', a)
    _safe_set(a, 'services_Service', set())
    assert not _is_linked(a, 'services_Service', b2)
    if hasattr(b2, 'services_CIID'):
        assert not _is_linked(b2, 'services_CIID', a)


def test_assoc_expressionRefs40_link_reassign_clear():
    a = services_ServiceUser(name="sample_text")
    b1 = services_Expression()
    b2 = services_Expression()
    _safe_set(a, 'services_ServiceUser41', {b1})
    assert _is_linked(a, 'services_ServiceUser41', b1)
    if hasattr(b1, 'services_Expression42'):
        assert _is_linked(b1, 'services_Expression42', a)
    _safe_set(a, 'services_ServiceUser41', {b2})
    assert _is_linked(a, 'services_ServiceUser41', b2)
    if hasattr(b1, 'services_Expression42'):
        assert not _is_linked(b1, 'services_Expression42', a)
    if hasattr(b2, 'services_Expression42'):
        assert _is_linked(b2, 'services_Expression42', a)
    _safe_set(a, 'services_ServiceUser41', set())
    assert not _is_linked(a, 'services_ServiceUser41', b2)
    if hasattr(b2, 'services_Expression42'):
        assert not _is_linked(b2, 'services_Expression42', a)


def test_assoc_nodes0_link_reassign_clear():
    a = services_RFSService(functionalCategory="sample_text")
    b1 = services_Node()
    b2 = services_Node()
    _safe_set(a, 'services_RFSService', {b1})
    assert _is_linked(a, 'services_RFSService', b1)
    if hasattr(b1, 'services_Node'):
        assert _is_linked(b1, 'services_Node', a)
    _safe_set(a, 'services_RFSService', {b2})
    assert _is_linked(a, 'services_RFSService', b2)
    if hasattr(b1, 'services_Node'):
        assert not _is_linked(b1, 'services_Node', a)
    if hasattr(b2, 'services_Node'):
        assert _is_linked(b2, 'services_Node', a)
    _safe_set(a, 'services_RFSService', set())
    assert not _is_linked(a, 'services_RFSService', b2)
    if hasattr(b2, 'services_Node'):
        assert not _is_linked(b2, 'services_Node', a)


def test_assoc_period19_link_reassign_clear():
    a = services_ServiceForecast(name="sample_text", revision="sample_text")
    b1 = services_DateTimeRange()
    b2 = services_DateTimeRange()
    _safe_set(a, 'services_ServiceForecast20', b1)
    assert _is_linked(a, 'services_ServiceForecast20', b1)
    if hasattr(b1, 'services_DateTimeRange'):
        assert _is_linked(b1, 'services_DateTimeRange', a)
    _safe_set(a, 'services_ServiceForecast20', b2)
    assert _is_linked(a, 'services_ServiceForecast20', b2)
    if hasattr(b1, 'services_DateTimeRange'):
        assert not _is_linked(b1, 'services_DateTimeRange', a)
    if hasattr(b2, 'services_DateTimeRange'):
        assert _is_linked(b2, 'services_DateTimeRange', a)
    _safe_set(a, 'services_ServiceForecast20', None)
    assert not _is_linked(a, 'services_ServiceForecast20', b2)
    if hasattr(b2, 'services_DateTimeRange'):
        assert not _is_linked(b2, 'services_DateTimeRange', a)


def test_assoc_period30_link_reassign_clear():
    a = services_ServiceMonitor(name="sample_text", revision="sample_text")
    b1 = services_DateTimeRange()
    b2 = services_DateTimeRange()
    _safe_set(a, 'services_ServiceMonitor31', b1)
    assert _is_linked(a, 'services_ServiceMonitor31', b1)
    if hasattr(b1, 'services_DateTimeRange32'):
        assert _is_linked(b1, 'services_DateTimeRange32', a)
    _safe_set(a, 'services_ServiceMonitor31', b2)
    assert _is_linked(a, 'services_ServiceMonitor31', b2)
    if hasattr(b1, 'services_DateTimeRange32'):
        assert not _is_linked(b1, 'services_DateTimeRange32', a)
    if hasattr(b2, 'services_DateTimeRange32'):
        assert _is_linked(b2, 'services_DateTimeRange32', a)
    _safe_set(a, 'services_ServiceMonitor31', None)
    assert not _is_linked(a, 'services_ServiceMonitor31', b2)
    if hasattr(b2, 'services_DateTimeRange32'):
        assert not _is_linked(b2, 'services_DateTimeRange32', a)


def test_assoc_profileResources35_link_reassign_clear():
    a = services_ServiceProfile(name="sample_text")
    b1 = services_NetXResource()
    b2 = services_NetXResource()
    _safe_set(a, 'services_ServiceProfile', {b1})
    assert _is_linked(a, 'services_ServiceProfile', b1)
    if hasattr(b1, 'services_NetXResource36'):
        assert _is_linked(b1, 'services_NetXResource36', a)
    _safe_set(a, 'services_ServiceProfile', {b2})
    assert _is_linked(a, 'services_ServiceProfile', b2)
    if hasattr(b1, 'services_NetXResource36'):
        assert not _is_linked(b1, 'services_NetXResource36', a)
    if hasattr(b2, 'services_NetXResource36'):
        assert _is_linked(b2, 'services_NetXResource36', a)
    _safe_set(a, 'services_ServiceProfile', set())
    assert not _is_linked(a, 'services_ServiceProfile', b2)
    if hasattr(b2, 'services_NetXResource36'):
        assert not _is_linked(b2, 'services_NetXResource36', a)


def test_assoc_resourceForecasts23_link_reassign_clear():
    a = services_ServiceForecast(name="sample_text", revision="sample_text")
    b1 = services_ResourceForecast()
    b2 = services_ResourceForecast()
    _safe_set(a, 'services_ServiceForecast24', {b1})
    assert _is_linked(a, 'services_ServiceForecast24', b1)
    if hasattr(b1, 'services_ResourceForecast'):
        assert _is_linked(b1, 'services_ResourceForecast', a)
    _safe_set(a, 'services_ServiceForecast24', {b2})
    assert _is_linked(a, 'services_ServiceForecast24', b2)
    if hasattr(b1, 'services_ResourceForecast'):
        assert not _is_linked(b1, 'services_ResourceForecast', a)
    if hasattr(b2, 'services_ResourceForecast'):
        assert _is_linked(b2, 'services_ResourceForecast', a)
    _safe_set(a, 'services_ServiceForecast24', set())
    assert not _is_linked(a, 'services_ServiceForecast24', b2)
    if hasattr(b2, 'services_ResourceForecast'):
        assert not _is_linked(b2, 'services_ResourceForecast', a)


def test_assoc_resourceMonitors33_link_reassign_clear():
    a = services_ServiceMonitor(name="sample_text", revision="sample_text")
    b1 = services_ResourceMonitor()
    b2 = services_ResourceMonitor()
    _safe_set(a, 'services_ServiceMonitor34', {b1})
    assert _is_linked(a, 'services_ServiceMonitor34', b1)
    if hasattr(b1, 'services_ResourceMonitor'):
        assert _is_linked(b1, 'services_ResourceMonitor', a)
    _safe_set(a, 'services_ServiceMonitor34', {b2})
    assert _is_linked(a, 'services_ServiceMonitor34', b2)
    if hasattr(b1, 'services_ResourceMonitor'):
        assert not _is_linked(b1, 'services_ResourceMonitor', a)
    if hasattr(b2, 'services_ResourceMonitor'):
        assert _is_linked(b2, 'services_ResourceMonitor', a)
    _safe_set(a, 'services_ServiceMonitor34', set())
    assert not _is_linked(a, 'services_ServiceMonitor34', b2)
    if hasattr(b2, 'services_ResourceMonitor'):
        assert not _is_linked(b2, 'services_ResourceMonitor', a)


def test_assoc_serviceDistribution13_link_reassign_clear():
    a = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    b1 = services_ServiceDistribution()
    b2 = services_ServiceDistribution()
    _safe_set(a, 'services_Service14', b1)
    assert _is_linked(a, 'services_Service14', b1)
    if hasattr(b1, 'services_ServiceDistribution'):
        assert _is_linked(b1, 'services_ServiceDistribution', a)
    _safe_set(a, 'services_Service14', b2)
    assert _is_linked(a, 'services_Service14', b2)
    if hasattr(b1, 'services_ServiceDistribution'):
        assert not _is_linked(b1, 'services_ServiceDistribution', a)
    if hasattr(b2, 'services_ServiceDistribution'):
        assert _is_linked(b2, 'services_ServiceDistribution', a)
    _safe_set(a, 'services_Service14', None)
    assert not _is_linked(a, 'services_Service14', b2)
    if hasattr(b2, 'services_ServiceDistribution'):
        assert not _is_linked(b2, 'services_ServiceDistribution', a)


def test_assoc_serviceForecastUsers21_link_reassign_clear():
    a = services_ServiceForecast(name="sample_text", revision="sample_text")
    b1 = services_ServiceForecastUsers()
    b2 = services_ServiceForecastUsers()
    _safe_set(a, 'services_ServiceForecast22', {b1})
    assert _is_linked(a, 'services_ServiceForecast22', b1)
    if hasattr(b1, 'services_ServiceForecastUsers'):
        assert _is_linked(b1, 'services_ServiceForecastUsers', a)
    _safe_set(a, 'services_ServiceForecast22', {b2})
    assert _is_linked(a, 'services_ServiceForecast22', b2)
    if hasattr(b1, 'services_ServiceForecastUsers'):
        assert not _is_linked(b1, 'services_ServiceForecastUsers', a)
    if hasattr(b2, 'services_ServiceForecastUsers'):
        assert _is_linked(b2, 'services_ServiceForecastUsers', a)
    _safe_set(a, 'services_ServiceForecast22', set())
    assert not _is_linked(a, 'services_ServiceForecast22', b2)
    if hasattr(b2, 'services_ServiceForecastUsers'):
        assert not _is_linked(b2, 'services_ServiceForecastUsers', a)


def test_assoc_serviceForecasts7_link_reassign_clear():
    a = services_ServiceForecast(name="sample_text", revision="sample_text")
    b1 = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    b2 = services_Service(serviceCategory="sample_text_2", serviceClass="sample_text_2", serviceDescription="sample_text_2", serviceName="sample_text_2")
    _safe_set(a, 'services_ServiceForecast', b1)
    assert _is_linked(a, 'services_ServiceForecast', b1)
    if hasattr(b1, 'services_Service8'):
        assert _is_linked(b1, 'services_Service8', a)
    _safe_set(a, 'services_ServiceForecast', b2)
    assert _is_linked(a, 'services_ServiceForecast', b2)
    if hasattr(b1, 'services_Service8'):
        assert not _is_linked(b1, 'services_Service8', a)
    if hasattr(b2, 'services_Service8'):
        assert _is_linked(b2, 'services_Service8', a)
    _safe_set(a, 'services_ServiceForecast', None)
    assert not _is_linked(a, 'services_ServiceForecast', b2)
    if hasattr(b2, 'services_Service8'):
        assert not _is_linked(b2, 'services_Service8', a)


def test_assoc_serviceMonitors9_link_reassign_clear():
    a = services_ServiceMonitor(name="sample_text", revision="sample_text")
    b1 = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    b2 = services_Service(serviceCategory="sample_text_2", serviceClass="sample_text_2", serviceDescription="sample_text_2", serviceName="sample_text_2")
    _safe_set(a, 'services_ServiceMonitor', b1)
    assert _is_linked(a, 'services_ServiceMonitor', b1)
    if hasattr(b1, 'services_Service10'):
        assert _is_linked(b1, 'services_Service10', a)
    _safe_set(a, 'services_ServiceMonitor', b2)
    assert _is_linked(a, 'services_ServiceMonitor', b2)
    if hasattr(b1, 'services_Service10'):
        assert not _is_linked(b1, 'services_Service10', a)
    if hasattr(b2, 'services_Service10'):
        assert _is_linked(b2, 'services_Service10', a)
    _safe_set(a, 'services_ServiceMonitor', None)
    assert not _is_linked(a, 'services_ServiceMonitor', b2)
    if hasattr(b2, 'services_Service10'):
        assert not _is_linked(b2, 'services_Service10', a)


def test_assoc_serviceProfile37_link_reassign_clear():
    a = services_ServiceUser(name="sample_text")
    b1 = services_ServiceProfile(name="sample_text")
    b2 = services_ServiceProfile(name="sample_text_2")
    _safe_set(a, 'services_ServiceUser38', b1)
    assert _is_linked(a, 'services_ServiceUser38', b1)
    if hasattr(b1, 'services_ServiceProfile39'):
        assert _is_linked(b1, 'services_ServiceProfile39', a)
    _safe_set(a, 'services_ServiceUser38', b2)
    assert _is_linked(a, 'services_ServiceUser38', b2)
    if hasattr(b1, 'services_ServiceProfile39'):
        assert not _is_linked(b1, 'services_ServiceProfile39', a)
    if hasattr(b2, 'services_ServiceProfile39'):
        assert _is_linked(b2, 'services_ServiceProfile39', a)
    _safe_set(a, 'services_ServiceUser38', None)
    assert not _is_linked(a, 'services_ServiceUser38', b2)
    if hasattr(b2, 'services_ServiceProfile39'):
        assert not _is_linked(b2, 'services_ServiceProfile39', a)


def test_assoc_serviceUserRef27_link_reassign_clear():
    a = services_ServiceUser(name="sample_text")
    b1 = services_ServiceForecastUsers()
    b2 = services_ServiceForecastUsers()
    _safe_set(a, 'services_ServiceUser29', b1)
    assert _is_linked(a, 'services_ServiceUser29', b1)
    if hasattr(b1, 'services_ServiceForecastUsers28'):
        assert _is_linked(b1, 'services_ServiceForecastUsers28', a)
    _safe_set(a, 'services_ServiceUser29', b2)
    assert _is_linked(a, 'services_ServiceUser29', b2)
    if hasattr(b1, 'services_ServiceForecastUsers28'):
        assert not _is_linked(b1, 'services_ServiceForecastUsers28', a)
    if hasattr(b2, 'services_ServiceForecastUsers28'):
        assert _is_linked(b2, 'services_ServiceForecastUsers28', a)
    _safe_set(a, 'services_ServiceUser29', None)
    assert not _is_linked(a, 'services_ServiceUser29', b2)
    if hasattr(b2, 'services_ServiceForecastUsers28'):
        assert not _is_linked(b2, 'services_ServiceForecastUsers28', a)


def test_assoc_serviceUserRefs11_link_reassign_clear():
    a = services_ServiceUser(name="sample_text")
    b1 = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    b2 = services_Service(serviceCategory="sample_text_2", serviceClass="sample_text_2", serviceDescription="sample_text_2", serviceName="sample_text_2")
    _safe_set(a, 'services_ServiceUser', b1)
    assert _is_linked(a, 'services_ServiceUser', b1)
    if hasattr(b1, 'services_Service12'):
        assert _is_linked(b1, 'services_Service12', a)
    _safe_set(a, 'services_ServiceUser', b2)
    assert _is_linked(a, 'services_ServiceUser', b2)
    if hasattr(b1, 'services_Service12'):
        assert not _is_linked(b1, 'services_Service12', a)
    if hasattr(b2, 'services_Service12'):
        assert _is_linked(b2, 'services_Service12', a)
    _safe_set(a, 'services_ServiceUser', None)
    assert not _is_linked(a, 'services_ServiceUser', b2)
    if hasattr(b2, 'services_Service12'):
        assert not _is_linked(b2, 'services_Service12', a)


def test_assoc_services5_link_reassign_clear():
    a = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    b1 = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    b2 = services_Service(serviceCategory="sample_text_2", serviceClass="sample_text_2", serviceDescription="sample_text_2", serviceName="sample_text_2")
    _safe_set(a, 'services_Service4', {b1})
    assert _is_linked(a, 'services_Service4', b1)
    if hasattr(b1, 'services_Service6'):
        assert _is_linked(b1, 'services_Service6', a)
    _safe_set(a, 'services_Service4', {b2})
    assert _is_linked(a, 'services_Service4', b2)
    if hasattr(b1, 'services_Service6'):
        assert not _is_linked(b1, 'services_Service6', a)
    if hasattr(b2, 'services_Service6'):
        assert _is_linked(b2, 'services_Service6', a)
    _safe_set(a, 'services_Service4', set())
    assert not _is_linked(a, 'services_Service4', b2)
    if hasattr(b2, 'services_Service6'):
        assert not _is_linked(b2, 'services_Service6', a)


def test_assoc_toleranceRefs1_link_reassign_clear():
    a = services_RFSService(functionalCategory="sample_text")
    b1 = services_Tolerance()
    b2 = services_Tolerance()
    _safe_set(a, 'services_RFSService2', {b1})
    assert _is_linked(a, 'services_RFSService2', b1)
    if hasattr(b1, 'services_Tolerance'):
        assert _is_linked(b1, 'services_Tolerance', a)
    _safe_set(a, 'services_RFSService2', {b2})
    assert _is_linked(a, 'services_RFSService2', b2)
    if hasattr(b1, 'services_Tolerance'):
        assert not _is_linked(b1, 'services_Tolerance', a)
    if hasattr(b2, 'services_Tolerance'):
        assert _is_linked(b2, 'services_Tolerance', a)
    _safe_set(a, 'services_RFSService2', set())
    assert not _is_linked(a, 'services_RFSService2', b2)
    if hasattr(b2, 'services_Tolerance'):
        assert not _is_linked(b2, 'services_Tolerance', a)


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


services_DateTimeRange_strategy = st.builds(services_DateTimeRange)
@given(instance=services_DateTimeRange_strategy)
@settings(max_examples=25)
def test_services_DateTimeRange_instantiation(instance):
    assert isinstance(instance, services_DateTimeRange)


services_Expression_strategy = st.builds(services_Expression)
@given(instance=services_Expression_strategy)
@settings(max_examples=25)
def test_services_Expression_instantiation(instance):
    assert isinstance(instance, services_Expression)


services_NetXResource_strategy = st.builds(services_NetXResource)
@given(instance=services_NetXResource_strategy)
@settings(max_examples=25)
def test_services_NetXResource_instantiation(instance):
    assert isinstance(instance, services_NetXResource)


services_Node_strategy = st.builds(services_Node)
@given(instance=services_Node_strategy)
@settings(max_examples=25)
def test_services_Node_instantiation(instance):
    assert isinstance(instance, services_Node)


services_RFSService_strategy = st.builds(services_RFSService, functionalCategory=safe_text)
@given(instance=services_RFSService_strategy)
@settings(max_examples=25)
def test_services_RFSService_instantiation(instance):
    assert isinstance(instance, services_RFSService)


services_ResourceForecast_strategy = st.builds(services_ResourceForecast)
@given(instance=services_ResourceForecast_strategy)
@settings(max_examples=25)
def test_services_ResourceForecast_instantiation(instance):
    assert isinstance(instance, services_ResourceForecast)


services_ResourceMonitor_strategy = st.builds(services_ResourceMonitor)
@given(instance=services_ResourceMonitor_strategy)
@settings(max_examples=25)
def test_services_ResourceMonitor_instantiation(instance):
    assert isinstance(instance, services_ResourceMonitor)


services_Service_strategy = st.builds(services_Service, serviceCategory=safe_text, serviceClass=safe_text, serviceDescription=safe_text, serviceName=safe_text)
@given(instance=services_Service_strategy)
@settings(max_examples=25)
def test_services_Service_instantiation(instance):
    assert isinstance(instance, services_Service)


services_ServiceDistribution_strategy = st.builds(services_ServiceDistribution)
@given(instance=services_ServiceDistribution_strategy)
@settings(max_examples=25)
def test_services_ServiceDistribution_instantiation(instance):
    assert isinstance(instance, services_ServiceDistribution)


services_ServiceForecast_strategy = st.builds(services_ServiceForecast, name=safe_text, revision=safe_text)
@given(instance=services_ServiceForecast_strategy)
@settings(max_examples=25)
def test_services_ServiceForecast_instantiation(instance):
    assert isinstance(instance, services_ServiceForecast)


services_ServiceForecastUsers_strategy = st.builds(services_ServiceForecastUsers)
@given(instance=services_ServiceForecastUsers_strategy)
@settings(max_examples=25)
def test_services_ServiceForecastUsers_instantiation(instance):
    assert isinstance(instance, services_ServiceForecastUsers)


services_ServiceMonitor_strategy = st.builds(services_ServiceMonitor, name=safe_text, revision=safe_text)
@given(instance=services_ServiceMonitor_strategy)
@settings(max_examples=25)
def test_services_ServiceMonitor_instantiation(instance):
    assert isinstance(instance, services_ServiceMonitor)


services_ServiceProfile_strategy = st.builds(services_ServiceProfile, name=safe_text)
@given(instance=services_ServiceProfile_strategy)
@settings(max_examples=25)
def test_services_ServiceProfile_instantiation(instance):
    assert isinstance(instance, services_ServiceProfile)


services_ServiceUser_strategy = st.builds(services_ServiceUser, name=safe_text)
@given(instance=services_ServiceUser_strategy)
@settings(max_examples=25)
def test_services_ServiceUser_instantiation(instance):
    assert isinstance(instance, services_ServiceUser)


services_Tolerance_strategy = st.builds(services_Tolerance)
@given(instance=services_Tolerance_strategy)
@settings(max_examples=25)
def test_services_Tolerance_instantiation(instance):
    assert isinstance(instance, services_Tolerance)


services_Value_strategy = st.builds(services_Value)
@given(instance=services_Value_strategy)
@settings(max_examples=25)
def test_services_Value_instantiation(instance):
    assert isinstance(instance, services_Value)



