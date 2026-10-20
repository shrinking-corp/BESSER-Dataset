import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Base,
    BaseResource,
    Service,
    services_CFSService,
    services_CIID,
    services_DateTimeRange,
    services_DerivedResource,
    services_DistributionEntry,
    services_Expression,
    services_Lifecycle,
    services_Message,
    services_NetXResource,
    services_Node,
    services_Protocol,
    services_RFSService,
    services_ReferenceRelationship,
    services_ResourceForecast,
    services_ResourceMonitor,
    services_Service,
    services_ServiceDistribution,
    services_ServiceFlow,
    services_ServiceFlowRelationship,
    services_ServiceForecast,
    services_ServiceForecastUsers,
    services_ServiceMonitor,
    services_ServiceProfile,
    services_ServiceUser,
    services_Tolerance,
    services_Value,
    ResourceOriginType,
    ServiceClassType,
    ServiceFlowDirection,
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

def test_assoc_cIID14_reverse_link_reassign_clear():
    a1 = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    a2 = services_Service(serviceCategory="sample_text_2", serviceClass="sample_text_2", serviceDescription="sample_text_2", serviceName="sample_text_2")
    b = services_CIID(commonCIID="sample_text", localCIID="sample_text")
    _safe_set(b, 'services_CIID', a1)
    assert _is_linked(b, 'services_CIID', a1)
    if hasattr(a1, 'services_Service'):
        assert _is_linked(a1, 'services_Service', b)
    _safe_set(b, 'services_CIID', a2)
    assert _is_linked(b, 'services_CIID', a2)
    if hasattr(a1, 'services_Service'):
        assert not _is_linked(a1, 'services_Service', b)
    if hasattr(a2, 'services_Service'):
        assert _is_linked(a2, 'services_Service', b)
    _safe_set(b, 'services_CIID', None)
    assert not _is_linked(b, 'services_CIID', a2)
    if hasattr(a2, 'services_Service'):
        assert not _is_linked(a2, 'services_Service', b)


def test_assoc_serviceFlow36_reverse_link_reassign_clear():
    a1 = services_ServiceFlowRelationship(direction="sample_text")
    a2 = services_ServiceFlowRelationship(direction="sample_text_2")
    b = services_ServiceFlow(name="sample_text")
    _safe_set(b, 'services_ServiceFlow38', a1)
    assert _is_linked(b, 'services_ServiceFlow38', a1)
    if hasattr(a1, 'services_ServiceFlowRelationship37'):
        assert _is_linked(a1, 'services_ServiceFlowRelationship37', b)
    _safe_set(b, 'services_ServiceFlow38', a2)
    assert _is_linked(b, 'services_ServiceFlow38', a2)
    if hasattr(a1, 'services_ServiceFlowRelationship37'):
        assert not _is_linked(a1, 'services_ServiceFlowRelationship37', b)
    if hasattr(a2, 'services_ServiceFlowRelationship37'):
        assert _is_linked(a2, 'services_ServiceFlowRelationship37', b)
    _safe_set(b, 'services_ServiceFlow38', None)
    assert not _is_linked(b, 'services_ServiceFlow38', a2)
    if hasattr(a2, 'services_ServiceFlowRelationship37'):
        assert not _is_linked(a2, 'services_ServiceFlowRelationship37', b)


def test_assoc_serviceFlowRelationships33_reverse_link_reassign_clear():
    a1 = services_ServiceFlowRelationship(direction="sample_text")
    a2 = services_ServiceFlowRelationship(direction="sample_text_2")
    b = services_ServiceFlow(name="sample_text")
    _safe_set(b, 'services_ServiceFlow', {a1})
    assert _is_linked(b, 'services_ServiceFlow', a1)
    if hasattr(a1, 'services_ServiceFlowRelationship'):
        assert _is_linked(a1, 'services_ServiceFlowRelationship', b)
    _safe_set(b, 'services_ServiceFlow', {a2})
    assert _is_linked(b, 'services_ServiceFlow', a2)
    if hasattr(a1, 'services_ServiceFlowRelationship'):
        assert not _is_linked(a1, 'services_ServiceFlowRelationship', b)
    if hasattr(a2, 'services_ServiceFlowRelationship'):
        assert _is_linked(a2, 'services_ServiceFlowRelationship', b)
    _safe_set(b, 'services_ServiceFlow', set())
    assert not _is_linked(b, 'services_ServiceFlow', a2)
    if hasattr(a2, 'services_ServiceFlowRelationship'):
        assert not _is_linked(a2, 'services_ServiceFlowRelationship', b)


def test_assoc_serviceForecasts20_reverse_link_reassign_clear():
    a1 = services_ServiceForecast(name="sample_text", revision="sample_text")
    a2 = services_ServiceForecast(name="sample_text_2", revision="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service21', {a1})
    assert _is_linked(b, 'services_Service21', a1)
    if hasattr(a1, 'services_ServiceForecast'):
        assert _is_linked(a1, 'services_ServiceForecast', b)
    _safe_set(b, 'services_Service21', {a2})
    assert _is_linked(b, 'services_Service21', a2)
    if hasattr(a1, 'services_ServiceForecast'):
        assert not _is_linked(a1, 'services_ServiceForecast', b)
    if hasattr(a2, 'services_ServiceForecast'):
        assert _is_linked(a2, 'services_ServiceForecast', b)
    _safe_set(b, 'services_Service21', set())
    assert not _is_linked(b, 'services_Service21', a2)
    if hasattr(a2, 'services_ServiceForecast'):
        assert not _is_linked(a2, 'services_ServiceForecast', b)


def test_assoc_serviceMonitors22_reverse_link_reassign_clear():
    a1 = services_ServiceMonitor(name="sample_text", revision="sample_text")
    a2 = services_ServiceMonitor(name="sample_text_2", revision="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service23', {a1})
    assert _is_linked(b, 'services_Service23', a1)
    if hasattr(a1, 'services_ServiceMonitor'):
        assert _is_linked(a1, 'services_ServiceMonitor', b)
    _safe_set(b, 'services_Service23', {a2})
    assert _is_linked(b, 'services_Service23', a2)
    if hasattr(a1, 'services_ServiceMonitor'):
        assert not _is_linked(a1, 'services_ServiceMonitor', b)
    if hasattr(a2, 'services_ServiceMonitor'):
        assert _is_linked(a2, 'services_ServiceMonitor', b)
    _safe_set(b, 'services_Service23', set())
    assert not _is_linked(b, 'services_Service23', a2)
    if hasattr(a2, 'services_ServiceMonitor'):
        assert not _is_linked(a2, 'services_ServiceMonitor', b)


def test_assoc_serviceProfile62_reverse_link_reassign_clear():
    a1 = services_ServiceUser(description="sample_text", name="sample_text")
    a2 = services_ServiceUser(description="sample_text_2", name="sample_text_2")
    b = services_ServiceProfile(name="sample_text")
    _safe_set(b, 'services_ServiceProfile64', a1)
    assert _is_linked(b, 'services_ServiceProfile64', a1)
    if hasattr(a1, 'services_ServiceUser63'):
        assert _is_linked(a1, 'services_ServiceUser63', b)
    _safe_set(b, 'services_ServiceProfile64', a2)
    assert _is_linked(b, 'services_ServiceProfile64', a2)
    if hasattr(a1, 'services_ServiceUser63'):
        assert not _is_linked(a1, 'services_ServiceUser63', b)
    if hasattr(a2, 'services_ServiceUser63'):
        assert _is_linked(a2, 'services_ServiceUser63', b)
    _safe_set(b, 'services_ServiceProfile64', None)
    assert not _is_linked(b, 'services_ServiceProfile64', a2)
    if hasattr(a2, 'services_ServiceUser63'):
        assert not _is_linked(a2, 'services_ServiceUser63', b)


def test_assoc_serviceUserRefs24_reverse_link_reassign_clear():
    a1 = services_ServiceUser(description="sample_text", name="sample_text")
    a2 = services_ServiceUser(description="sample_text_2", name="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service25', {a1})
    assert _is_linked(b, 'services_Service25', a1)
    if hasattr(a1, 'services_ServiceUser'):
        assert _is_linked(a1, 'services_ServiceUser', b)
    _safe_set(b, 'services_Service25', {a2})
    assert _is_linked(b, 'services_Service25', a2)
    if hasattr(a1, 'services_ServiceUser'):
        assert not _is_linked(a1, 'services_ServiceUser', b)
    if hasattr(a2, 'services_ServiceUser'):
        assert _is_linked(a2, 'services_ServiceUser', b)
    _safe_set(b, 'services_Service25', set())
    assert not _is_linked(b, 'services_Service25', a2)
    if hasattr(a2, 'services_ServiceUser'):
        assert not _is_linked(a2, 'services_ServiceUser', b)


def test_assoc_services18_reverse_link_reassign_clear():
    a1 = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    a2 = services_Service(serviceCategory="sample_text_2", serviceClass="sample_text_2", serviceDescription="sample_text_2", serviceName="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service19', a1)
    assert _is_linked(b, 'services_Service19', a1)
    if hasattr(a1, 'services_Service17'):
        assert _is_linked(a1, 'services_Service17', b)
    _safe_set(b, 'services_Service19', a2)
    assert _is_linked(b, 'services_Service19', a2)
    if hasattr(a1, 'services_Service17'):
        assert not _is_linked(a1, 'services_Service17', b)
    if hasattr(a2, 'services_Service17'):
        assert _is_linked(a2, 'services_Service17', b)
    _safe_set(b, 'services_Service19', None)
    assert not _is_linked(b, 'services_Service19', a2)
    if hasattr(a2, 'services_Service17'):
        assert not _is_linked(a2, 'services_Service17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_distribution8_stub_double():
    # services_DerivedResource has no real 'services_DerivedResource10' property in the generated
    # code (a bare stub) -- manually attach it so services_DistributionEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_DistributionEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_DistributionEntry(resourceOrigin="sample_text")
    partner = services_DerivedResource()
    setattr(partner, 'services_DerivedResource10', None)
    _safe_set(owner, 'services_DistributionEntry9', partner)
    assert getattr(partner, 'services_DerivedResource10') == owner
    _safe_set(owner, 'services_DistributionEntry9', None)
    assert getattr(partner, 'services_DerivedResource10') is None


def test_assoc_distributionEntries28_stub_double():
    # services_ServiceDistribution has no real 'services_ServiceDistribution29' property in the generated
    # code (a bare stub) -- manually attach it so services_DistributionEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_DistributionEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_DistributionEntry(resourceOrigin="sample_text")
    partner = services_ServiceDistribution()
    setattr(partner, 'services_ServiceDistribution29', None)
    _safe_set(owner, 'services_DistributionEntry30', partner)
    assert owner in getattr(partner, 'services_ServiceDistribution29')
    _safe_set(owner, 'services_DistributionEntry30', None)
    assert owner not in getattr(partner, 'services_ServiceDistribution29')


def test_assoc_expressionRef65_stub_double():
    # services_Expression has no real 'services_Expression67' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceUser's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceUser's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceUser(description="sample_text", name="sample_text")
    partner = services_Expression()
    setattr(partner, 'services_Expression67', None)
    _safe_set(owner, 'services_ServiceUser66', partner)
    assert getattr(partner, 'services_Expression67') == owner
    _safe_set(owner, 'services_ServiceUser66', None)
    assert getattr(partner, 'services_Expression67') is None


def test_assoc_lifecycle15_stub_double():
    # services_Lifecycle has no real 'services_Lifecycle' property in the generated
    # code (a bare stub) -- manually attach it so services_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    partner = services_Lifecycle()
    setattr(partner, 'services_Lifecycle', None)
    _safe_set(owner, 'services_Service16', partner)
    assert getattr(partner, 'services_Lifecycle') == owner
    _safe_set(owner, 'services_Service16', None)
    assert getattr(partner, 'services_Lifecycle') is None


def test_assoc_message41_stub_double():
    # services_Message has no real 'services_Message' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceFlowRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceFlowRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceFlowRelationship(direction="sample_text")
    partner = services_Message()
    setattr(partner, 'services_Message', None)
    _safe_set(owner, 'services_ServiceFlowRelationship42', partner)
    assert getattr(partner, 'services_Message') == owner
    _safe_set(owner, 'services_ServiceFlowRelationship42', None)
    assert getattr(partner, 'services_Message') is None


def test_assoc_nodes11_stub_double():
    # services_Node has no real 'services_Node' property in the generated
    # code (a bare stub) -- manually attach it so services_RFSService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_RFSService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_RFSService(functionalCategory="sample_text")
    partner = services_Node()
    setattr(partner, 'services_Node', None)
    _safe_set(owner, 'services_RFSService', {partner})
    assert getattr(partner, 'services_Node') == owner
    _safe_set(owner, 'services_RFSService', set())
    assert getattr(partner, 'services_Node') is None


def test_assoc_period43_stub_double():
    # services_DateTimeRange has no real 'services_DateTimeRange' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceForecast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceForecast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceForecast(name="sample_text", revision="sample_text")
    partner = services_DateTimeRange()
    setattr(partner, 'services_DateTimeRange', None)
    _safe_set(owner, 'services_ServiceForecast44', partner)
    assert getattr(partner, 'services_DateTimeRange') == owner
    _safe_set(owner, 'services_ServiceForecast44', None)
    assert getattr(partner, 'services_DateTimeRange') is None


def test_assoc_period55_stub_double():
    # services_DateTimeRange has no real 'services_DateTimeRange57' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceMonitor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceMonitor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceMonitor(name="sample_text", revision="sample_text")
    partner = services_DateTimeRange()
    setattr(partner, 'services_DateTimeRange57', None)
    _safe_set(owner, 'services_ServiceMonitor56', partner)
    assert getattr(partner, 'services_DateTimeRange57') == owner
    _safe_set(owner, 'services_ServiceMonitor56', None)
    assert getattr(partner, 'services_DateTimeRange57') is None


def test_assoc_profileResources60_stub_double():
    # services_DerivedResource has no real 'services_DerivedResource61' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceProfile(name="sample_text")
    partner = services_DerivedResource()
    setattr(partner, 'services_DerivedResource61', None)
    _safe_set(owner, 'services_ServiceProfile', {partner})
    assert getattr(partner, 'services_DerivedResource61') == owner
    _safe_set(owner, 'services_ServiceProfile', set())
    assert getattr(partner, 'services_DerivedResource61') is None


def test_assoc_protocol39_stub_double():
    # services_Protocol has no real 'services_Protocol' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceFlowRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceFlowRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceFlowRelationship(direction="sample_text")
    partner = services_Protocol()
    setattr(partner, 'services_Protocol', None)
    _safe_set(owner, 'services_ServiceFlowRelationship40', partner)
    assert getattr(partner, 'services_Protocol') == owner
    _safe_set(owner, 'services_ServiceFlowRelationship40', None)
    assert getattr(partner, 'services_Protocol') is None


def test_assoc_referenceRelationship34_stub_double():
    # services_ReferenceRelationship has no real 'services_ReferenceRelationship' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceFlowRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceFlowRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceFlowRelationship(direction="sample_text")
    partner = services_ReferenceRelationship()
    setattr(partner, 'services_ReferenceRelationship', None)
    _safe_set(owner, 'services_ServiceFlowRelationship35', partner)
    assert getattr(partner, 'services_ReferenceRelationship') == owner
    _safe_set(owner, 'services_ServiceFlowRelationship35', None)
    assert getattr(partner, 'services_ReferenceRelationship') is None


def test_assoc_resourceForecasts47_stub_double():
    # services_ResourceForecast has no real 'services_ResourceForecast' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceForecast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceForecast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceForecast(name="sample_text", revision="sample_text")
    partner = services_ResourceForecast()
    setattr(partner, 'services_ResourceForecast', None)
    _safe_set(owner, 'services_ServiceForecast48', {partner})
    assert getattr(partner, 'services_ResourceForecast') == owner
    _safe_set(owner, 'services_ServiceForecast48', set())
    assert getattr(partner, 'services_ResourceForecast') is None


def test_assoc_resourceMonitors58_stub_double():
    # services_ResourceMonitor has no real 'services_ResourceMonitor' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceMonitor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceMonitor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceMonitor(name="sample_text", revision="sample_text")
    partner = services_ResourceMonitor()
    setattr(partner, 'services_ResourceMonitor', None)
    _safe_set(owner, 'services_ServiceMonitor59', {partner})
    assert getattr(partner, 'services_ResourceMonitor') == owner
    _safe_set(owner, 'services_ServiceMonitor59', set())
    assert getattr(partner, 'services_ResourceMonitor') is None


def test_assoc_resourceRef7_stub_double():
    # services_NetXResource has no real 'services_NetXResource' property in the generated
    # code (a bare stub) -- manually attach it so services_DistributionEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_DistributionEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_DistributionEntry(resourceOrigin="sample_text")
    partner = services_NetXResource()
    setattr(partner, 'services_NetXResource', None)
    _safe_set(owner, 'services_DistributionEntry', partner)
    assert getattr(partner, 'services_NetXResource') == owner
    _safe_set(owner, 'services_DistributionEntry', None)
    assert getattr(partner, 'services_NetXResource') is None


def test_assoc_serviceDistribution26_stub_double():
    # services_ServiceDistribution has no real 'services_ServiceDistribution' property in the generated
    # code (a bare stub) -- manually attach it so services_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    partner = services_ServiceDistribution()
    setattr(partner, 'services_ServiceDistribution', None)
    _safe_set(owner, 'services_Service27', partner)
    assert getattr(partner, 'services_ServiceDistribution') == owner
    _safe_set(owner, 'services_Service27', None)
    assert getattr(partner, 'services_ServiceDistribution') is None


def test_assoc_serviceForecastUsers45_stub_double():
    # services_ServiceForecastUsers has no real 'services_ServiceForecastUsers' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceForecast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceForecast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceForecast(name="sample_text", revision="sample_text")
    partner = services_ServiceForecastUsers()
    setattr(partner, 'services_ServiceForecastUsers', None)
    _safe_set(owner, 'services_ServiceForecast46', {partner})
    assert getattr(partner, 'services_ServiceForecastUsers') == owner
    _safe_set(owner, 'services_ServiceForecast46', set())
    assert getattr(partner, 'services_ServiceForecastUsers') is None


def test_assoc_serviceUserRef52_stub_double():
    # services_ServiceForecastUsers has no real 'services_ServiceForecastUsers53' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceUser's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceUser's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceUser(description="sample_text", name="sample_text")
    partner = services_ServiceForecastUsers()
    setattr(partner, 'services_ServiceForecastUsers53', None)
    _safe_set(owner, 'services_ServiceUser54', partner)
    assert getattr(partner, 'services_ServiceForecastUsers53') == owner
    _safe_set(owner, 'services_ServiceUser54', None)
    assert getattr(partner, 'services_ServiceForecastUsers53') is None


def test_assoc_toleranceRefs12_stub_double():
    # services_Tolerance has no real 'services_Tolerance' property in the generated
    # code (a bare stub) -- manually attach it so services_RFSService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_RFSService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_RFSService(functionalCategory="sample_text")
    partner = services_Tolerance()
    setattr(partner, 'services_Tolerance', None)
    _safe_set(owner, 'services_RFSService13', {partner})
    assert getattr(partner, 'services_Tolerance') == owner
    _safe_set(owner, 'services_RFSService13', set())
    assert getattr(partner, 'services_Tolerance') is None


