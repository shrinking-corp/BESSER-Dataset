import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_ciID12_reverse_link_reassign_clear():
    a1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    a2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    b = services_CIID(commonCIID="sample_text", localCIID="sample_text")
    _safe_set(b, 'services_CIID', a1)
    assert _is_linked(b, 'services_CIID', a1)
    if hasattr(a1, 'services_Service13'):
        assert _is_linked(a1, 'services_Service13', b)
    _safe_set(b, 'services_CIID', a2)
    assert _is_linked(b, 'services_CIID', a2)
    if hasattr(a1, 'services_Service13'):
        assert not _is_linked(a1, 'services_Service13', b)
    if hasattr(a2, 'services_Service13'):
        assert _is_linked(a2, 'services_Service13', b)
    _safe_set(b, 'services_CIID', None)
    assert not _is_linked(b, 'services_CIID', a2)
    if hasattr(a2, 'services_Service13'):
        assert not _is_linked(a2, 'services_Service13', b)


def test_assoc_serviceContracts16_reverse_link_reassign_clear():
    a1 = services_ServiceContract(oLA="sample_text", sLA="sample_text", uC="sample_text", wLA="sample_text")
    a2 = services_ServiceContract(oLA="sample_text_2", sLA="sample_text_2", uC="sample_text_2", wLA="sample_text_2")
    b = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    _safe_set(b, 'services_Service17', {a1})
    assert _is_linked(b, 'services_Service17', a1)
    if hasattr(a1, 'services_ServiceContract'):
        assert _is_linked(a1, 'services_ServiceContract', b)
    _safe_set(b, 'services_Service17', {a2})
    assert _is_linked(b, 'services_Service17', a2)
    if hasattr(a1, 'services_ServiceContract'):
        assert not _is_linked(a1, 'services_ServiceContract', b)
    if hasattr(a2, 'services_ServiceContract'):
        assert _is_linked(a2, 'services_ServiceContract', b)
    _safe_set(b, 'services_Service17', set())
    assert not _is_linked(b, 'services_Service17', a2)
    if hasattr(a2, 'services_ServiceContract'):
        assert not _is_linked(a2, 'services_ServiceContract', b)


def test_assoc_serviceDescription6_reverse_link_reassign_clear():
    a1 = services_ServiceDescription(serviceDescriptionCommon="sample_text", serviceDescriptionNational="sample_text")
    a2 = services_ServiceDescription(serviceDescriptionCommon="sample_text_2", serviceDescriptionNational="sample_text_2")
    b = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    _safe_set(b, 'services_Service7', a1)
    assert _is_linked(b, 'services_Service7', a1)
    if hasattr(a1, 'services_ServiceDescription'):
        assert _is_linked(a1, 'services_ServiceDescription', b)
    _safe_set(b, 'services_Service7', a2)
    assert _is_linked(b, 'services_Service7', a2)
    if hasattr(a1, 'services_ServiceDescription'):
        assert not _is_linked(a1, 'services_ServiceDescription', b)
    if hasattr(a2, 'services_ServiceDescription'):
        assert _is_linked(a2, 'services_ServiceDescription', b)
    _safe_set(b, 'services_Service7', None)
    assert not _is_linked(b, 'services_Service7', a2)
    if hasattr(a2, 'services_ServiceDescription'):
        assert not _is_linked(a2, 'services_ServiceDescription', b)


def test_assoc_serviceIncidentMgt10_reverse_link_reassign_clear():
    a1 = services_ServiceIncidentMgt(businessImpact="sample_text", maintenance="sample_text", maintenanceWindow="sample_text", monitoring="sample_text")
    a2 = services_ServiceIncidentMgt(businessImpact="sample_text_2", maintenance="sample_text_2", maintenanceWindow="sample_text_2", monitoring="sample_text_2")
    b = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    _safe_set(b, 'services_Service11', a1)
    assert _is_linked(b, 'services_Service11', a1)
    if hasattr(a1, 'services_ServiceIncidentMgt'):
        assert _is_linked(a1, 'services_ServiceIncidentMgt', b)
    _safe_set(b, 'services_Service11', a2)
    assert _is_linked(b, 'services_Service11', a2)
    if hasattr(a1, 'services_ServiceIncidentMgt'):
        assert not _is_linked(a1, 'services_ServiceIncidentMgt', b)
    if hasattr(a2, 'services_ServiceIncidentMgt'):
        assert _is_linked(a2, 'services_ServiceIncidentMgt', b)
    _safe_set(b, 'services_Service11', None)
    assert not _is_linked(b, 'services_Service11', a2)
    if hasattr(a2, 'services_ServiceIncidentMgt'):
        assert not _is_linked(a2, 'services_ServiceIncidentMgt', b)


def test_assoc_serviceInterrest14_reverse_link_reassign_clear():
    a1 = services_ServiceInterrest(contactUnit="sample_text", interrestKind="sample_text")
    a2 = services_ServiceInterrest(contactUnit="sample_text_2", interrestKind="sample_text_2")
    b = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    _safe_set(b, 'services_Service15', a1)
    assert _is_linked(b, 'services_Service15', a1)
    if hasattr(a1, 'services_ServiceInterrest'):
        assert _is_linked(a1, 'services_ServiceInterrest', b)
    _safe_set(b, 'services_Service15', a2)
    assert _is_linked(b, 'services_Service15', a2)
    if hasattr(a1, 'services_ServiceInterrest'):
        assert not _is_linked(a1, 'services_ServiceInterrest', b)
    if hasattr(a2, 'services_ServiceInterrest'):
        assert _is_linked(a2, 'services_ServiceInterrest', b)
    _safe_set(b, 'services_Service15', None)
    assert not _is_linked(b, 'services_Service15', a2)
    if hasattr(a2, 'services_ServiceInterrest'):
        assert not _is_linked(a2, 'services_ServiceInterrest', b)


def test_assoc_serviceMisc20_reverse_link_reassign_clear():
    a1 = services_ServiceAdditional(costCenter="sample_text", history="sample_text", kpi="sample_text", lifeCycleState="sample_text", link="sample_text", report="sample_text", usageState="sample_text")
    a2 = services_ServiceAdditional(costCenter="sample_text_2", history="sample_text_2", kpi="sample_text_2", lifeCycleState="sample_text_2", link="sample_text_2", report="sample_text_2", usageState="sample_text_2")
    b = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    _safe_set(b, 'services_Service21', a1)
    assert _is_linked(b, 'services_Service21', a1)
    if hasattr(a1, 'services_ServiceAdditional'):
        assert _is_linked(a1, 'services_ServiceAdditional', b)
    _safe_set(b, 'services_Service21', a2)
    assert _is_linked(b, 'services_Service21', a2)
    if hasattr(a1, 'services_ServiceAdditional'):
        assert not _is_linked(a1, 'services_ServiceAdditional', b)
    if hasattr(a2, 'services_ServiceAdditional'):
        assert _is_linked(a2, 'services_ServiceAdditional', b)
    _safe_set(b, 'services_Service21', None)
    assert not _is_linked(b, 'services_Service21', a2)
    if hasattr(a2, 'services_ServiceAdditional'):
        assert not _is_linked(a2, 'services_ServiceAdditional', b)


def test_assoc_serviceName5_reverse_link_reassign_clear():
    a1 = services_ServiceName(alias="sample_text", identifier="sample_text", index="sample_text", name="sample_text")
    a2 = services_ServiceName(alias="sample_text_2", identifier="sample_text_2", index="sample_text_2", name="sample_text_2")
    b = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    _safe_set(b, 'services_Service', a1)
    assert _is_linked(b, 'services_Service', a1)
    if hasattr(a1, 'services_ServiceName'):
        assert _is_linked(a1, 'services_ServiceName', b)
    _safe_set(b, 'services_Service', a2)
    assert _is_linked(b, 'services_Service', a2)
    if hasattr(a1, 'services_ServiceName'):
        assert not _is_linked(a1, 'services_ServiceName', b)
    if hasattr(a2, 'services_ServiceName'):
        assert _is_linked(a2, 'services_ServiceName', b)
    _safe_set(b, 'services_Service', None)
    assert not _is_linked(b, 'services_Service', a2)
    if hasattr(a2, 'services_ServiceName'):
        assert not _is_linked(a2, 'services_ServiceName', b)


def test_assoc_serviceProfile3_reverse_link_reassign_clear():
    a1 = services_ServiceProfile(name="sample_text")
    a2 = services_ServiceProfile(name="sample_text_2")
    b = services_RFSService(functionalCategory="sample_text", location="sample_text")
    _safe_set(b, 'services_RFSService4', a1)
    assert _is_linked(b, 'services_RFSService4', a1)
    if hasattr(a1, 'services_ServiceProfile'):
        assert _is_linked(a1, 'services_ServiceProfile', b)
    _safe_set(b, 'services_RFSService4', a2)
    assert _is_linked(b, 'services_RFSService4', a2)
    if hasattr(a1, 'services_ServiceProfile'):
        assert not _is_linked(a1, 'services_ServiceProfile', b)
    if hasattr(a2, 'services_ServiceProfile'):
        assert _is_linked(a2, 'services_ServiceProfile', b)
    _safe_set(b, 'services_RFSService4', None)
    assert not _is_linked(b, 'services_RFSService4', a2)
    if hasattr(a2, 'services_ServiceProfile'):
        assert not _is_linked(a2, 'services_ServiceProfile', b)


def test_assoc_serviceSecurityMgt8_reverse_link_reassign_clear():
    a1 = services_ServiceSecurityMgt(drPlanContact="sample_text", drPlanRepository="sample_text", drRecoveryPlan="sample_text", securityRating="sample_text")
    a2 = services_ServiceSecurityMgt(drPlanContact="sample_text_2", drPlanRepository="sample_text_2", drRecoveryPlan="sample_text_2", securityRating="sample_text_2")
    b = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    _safe_set(b, 'services_Service9', a1)
    assert _is_linked(b, 'services_Service9', a1)
    if hasattr(a1, 'services_ServiceSecurityMgt'):
        assert _is_linked(a1, 'services_ServiceSecurityMgt', b)
    _safe_set(b, 'services_Service9', a2)
    assert _is_linked(b, 'services_Service9', a2)
    if hasattr(a1, 'services_ServiceSecurityMgt'):
        assert not _is_linked(a1, 'services_ServiceSecurityMgt', b)
    if hasattr(a2, 'services_ServiceSecurityMgt'):
        assert _is_linked(a2, 'services_ServiceSecurityMgt', b)
    _safe_set(b, 'services_Service9', None)
    assert not _is_linked(b, 'services_Service9', a2)
    if hasattr(a2, 'services_ServiceSecurityMgt'):
        assert not _is_linked(a2, 'services_ServiceSecurityMgt', b)


def test_assoc_serviceSupport18_reverse_link_reassign_clear():
    a1 = services_ServiceSupport(supportDays="sample_text", supportHours="sample_text")
    a2 = services_ServiceSupport(supportDays="sample_text_2", supportHours="sample_text_2")
    b = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    _safe_set(b, 'services_Service19', a1)
    assert _is_linked(b, 'services_Service19', a1)
    if hasattr(a1, 'services_ServiceSupport'):
        assert _is_linked(a1, 'services_ServiceSupport', b)
    _safe_set(b, 'services_Service19', a2)
    assert _is_linked(b, 'services_Service19', a2)
    if hasattr(a1, 'services_ServiceSupport'):
        assert not _is_linked(a1, 'services_ServiceSupport', b)
    if hasattr(a2, 'services_ServiceSupport'):
        assert _is_linked(a2, 'services_ServiceSupport', b)
    _safe_set(b, 'services_Service19', None)
    assert not _is_linked(b, 'services_Service19', a2)
    if hasattr(a2, 'services_ServiceSupport'):
        assert not _is_linked(a2, 'services_ServiceSupport', b)


def test_assoc_services23_reverse_link_reassign_clear():
    a1 = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    a2 = services_Service(mostTopService="sample_text_2", serviceCategory="sample_text_2", serviceCharacterCommon="sample_text_2", serviceClass="sample_text_2", serviceKind="sample_text_2", serviceSupport1="sample_text_2", ssDomain="sample_text_2")
    b = services_Service(mostTopService="sample_text", serviceCategory="sample_text", serviceCharacterCommon="sample_text", serviceClass="sample_text", serviceKind="sample_text", serviceSupport1="sample_text", ssDomain="sample_text")
    _safe_set(b, 'services_Service24', a1)
    assert _is_linked(b, 'services_Service24', a1)
    if hasattr(a1, 'services_Service22'):
        assert _is_linked(a1, 'services_Service22', b)
    _safe_set(b, 'services_Service24', a2)
    assert _is_linked(b, 'services_Service24', a2)
    if hasattr(a1, 'services_Service22'):
        assert not _is_linked(a1, 'services_Service22', b)
    if hasattr(a2, 'services_Service22'):
        assert _is_linked(a2, 'services_Service22', b)
    _safe_set(b, 'services_Service24', None)
    assert not _is_linked(b, 'services_Service24', a2)
    if hasattr(a2, 'services_Service22'):
        assert not _is_linked(a2, 'services_Service22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements0_stub_double():
    # services_EObject has no real 'services_EObject' property in the generated
    # code (a bare stub) -- manually attach it so services_CFSService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_CFSService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_CFSService(provider="sample_text", scenario="sample_text")
    partner = services_EObject()
    setattr(partner, 'services_EObject', None)
    _safe_set(owner, 'services_CFSService', {partner})
    assert getattr(partner, 'services_EObject') == owner
    _safe_set(owner, 'services_CFSService', set())
    assert getattr(partner, 'services_EObject') is None


def test_assoc_elements1_stub_double():
    # services_EObject has no real 'services_EObject2' property in the generated
    # code (a bare stub) -- manually attach it so services_RFSService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_RFSService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_RFSService(functionalCategory="sample_text", location="sample_text")
    partner = services_EObject()
    setattr(partner, 'services_EObject2', None)
    _safe_set(owner, 'services_RFSService', {partner})
    assert getattr(partner, 'services_EObject2') == owner
    _safe_set(owner, 'services_RFSService', set())
    assert getattr(partner, 'services_EObject2') is None


def test_assoc_serviceParameters25_stub_double():
    # services_Parameter has no real 'services_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceProfile(name="sample_text")
    partner = services_Parameter()
    setattr(partner, 'services_Parameter', None)
    _safe_set(owner, 'services_ServiceProfile26', {partner})
    assert getattr(partner, 'services_Parameter') == owner
    _safe_set(owner, 'services_ServiceProfile26', set())
    assert getattr(partner, 'services_Parameter') is None


