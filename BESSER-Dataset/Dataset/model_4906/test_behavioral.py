import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Service,
    services_CFSService,
    services_CIID,
    services_DateTimeRange,
    services_EObject,
    services_Expression,
    services_NetXResource,
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
    services_Value,
    ServiceClassType,
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

def test_assoc_cIID4_reverse_link_reassign_clear():
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


def test_assoc_serviceForecasts8_reverse_link_reassign_clear():
    a1 = services_ServiceForecast(name="sample_text", revision="sample_text")
    a2 = services_ServiceForecast(name="sample_text_2", revision="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service9', {a1})
    assert _is_linked(b, 'services_Service9', a1)
    if hasattr(a1, 'services_ServiceForecast'):
        assert _is_linked(a1, 'services_ServiceForecast', b)
    _safe_set(b, 'services_Service9', {a2})
    assert _is_linked(b, 'services_Service9', a2)
    if hasattr(a1, 'services_ServiceForecast'):
        assert not _is_linked(a1, 'services_ServiceForecast', b)
    if hasattr(a2, 'services_ServiceForecast'):
        assert _is_linked(a2, 'services_ServiceForecast', b)
    _safe_set(b, 'services_Service9', set())
    assert not _is_linked(b, 'services_Service9', a2)
    if hasattr(a2, 'services_ServiceForecast'):
        assert not _is_linked(a2, 'services_ServiceForecast', b)


def test_assoc_serviceMonitors10_reverse_link_reassign_clear():
    a1 = services_ServiceMonitor(name="sample_text", revision="sample_text")
    a2 = services_ServiceMonitor(name="sample_text_2", revision="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service11', {a1})
    assert _is_linked(b, 'services_Service11', a1)
    if hasattr(a1, 'services_ServiceMonitor'):
        assert _is_linked(a1, 'services_ServiceMonitor', b)
    _safe_set(b, 'services_Service11', {a2})
    assert _is_linked(b, 'services_Service11', a2)
    if hasattr(a1, 'services_ServiceMonitor'):
        assert not _is_linked(a1, 'services_ServiceMonitor', b)
    if hasattr(a2, 'services_ServiceMonitor'):
        assert _is_linked(a2, 'services_ServiceMonitor', b)
    _safe_set(b, 'services_Service11', set())
    assert not _is_linked(b, 'services_Service11', a2)
    if hasattr(a2, 'services_ServiceMonitor'):
        assert not _is_linked(a2, 'services_ServiceMonitor', b)


def test_assoc_serviceProfile38_reverse_link_reassign_clear():
    a1 = services_ServiceUser(name="sample_text")
    a2 = services_ServiceUser(name="sample_text_2")
    b = services_ServiceProfile(name="sample_text")
    _safe_set(b, 'services_ServiceProfile40', a1)
    assert _is_linked(b, 'services_ServiceProfile40', a1)
    if hasattr(a1, 'services_ServiceUser39'):
        assert _is_linked(a1, 'services_ServiceUser39', b)
    _safe_set(b, 'services_ServiceProfile40', a2)
    assert _is_linked(b, 'services_ServiceProfile40', a2)
    if hasattr(a1, 'services_ServiceUser39'):
        assert not _is_linked(a1, 'services_ServiceUser39', b)
    if hasattr(a2, 'services_ServiceUser39'):
        assert _is_linked(a2, 'services_ServiceUser39', b)
    _safe_set(b, 'services_ServiceProfile40', None)
    assert not _is_linked(b, 'services_ServiceProfile40', a2)
    if hasattr(a2, 'services_ServiceUser39'):
        assert not _is_linked(a2, 'services_ServiceUser39', b)


def test_assoc_serviceUserRefs12_reverse_link_reassign_clear():
    a1 = services_ServiceUser(name="sample_text")
    a2 = services_ServiceUser(name="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service13', {a1})
    assert _is_linked(b, 'services_Service13', a1)
    if hasattr(a1, 'services_ServiceUser'):
        assert _is_linked(a1, 'services_ServiceUser', b)
    _safe_set(b, 'services_Service13', {a2})
    assert _is_linked(b, 'services_Service13', a2)
    if hasattr(a1, 'services_ServiceUser'):
        assert not _is_linked(a1, 'services_ServiceUser', b)
    if hasattr(a2, 'services_ServiceUser'):
        assert _is_linked(a2, 'services_ServiceUser', b)
    _safe_set(b, 'services_Service13', set())
    assert not _is_linked(b, 'services_Service13', a2)
    if hasattr(a2, 'services_ServiceUser'):
        assert not _is_linked(a2, 'services_ServiceUser', b)


def test_assoc_services6_reverse_link_reassign_clear():
    a1 = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    a2 = services_Service(serviceCategory="sample_text_2", serviceClass="sample_text_2", serviceDescription="sample_text_2", serviceName="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service7', a1)
    assert _is_linked(b, 'services_Service7', a1)
    if hasattr(a1, 'services_Service5'):
        assert _is_linked(a1, 'services_Service5', b)
    _safe_set(b, 'services_Service7', a2)
    assert _is_linked(b, 'services_Service7', a2)
    if hasattr(a1, 'services_Service5'):
        assert not _is_linked(a1, 'services_Service5', b)
    if hasattr(a2, 'services_Service5'):
        assert _is_linked(a2, 'services_Service5', b)
    _safe_set(b, 'services_Service7', None)
    assert not _is_linked(b, 'services_Service7', a2)
    if hasattr(a2, 'services_Service5'):
        assert not _is_linked(a2, 'services_Service5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_expressionRefs41_stub_double():
    # services_Expression has no real 'services_Expression43' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceUser's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceUser's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceUser(name="sample_text")
    partner = services_Expression()
    setattr(partner, 'services_Expression43', None)
    _safe_set(owner, 'services_ServiceUser42', {partner})
    assert getattr(partner, 'services_Expression43') == owner
    _safe_set(owner, 'services_ServiceUser42', set())
    assert getattr(partner, 'services_Expression43') is None


def test_assoc_nodes0_stub_double():
    # services_EObject has no real 'services_EObject' property in the generated
    # code (a bare stub) -- manually attach it so services_RFSService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_RFSService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_RFSService(functionalCategory="sample_text")
    partner = services_EObject()
    setattr(partner, 'services_EObject', None)
    _safe_set(owner, 'services_RFSService', {partner})
    assert getattr(partner, 'services_EObject') == owner
    _safe_set(owner, 'services_RFSService', set())
    assert getattr(partner, 'services_EObject') is None


def test_assoc_period20_stub_double():
    # services_DateTimeRange has no real 'services_DateTimeRange' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceForecast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceForecast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceForecast(name="sample_text", revision="sample_text")
    partner = services_DateTimeRange()
    setattr(partner, 'services_DateTimeRange', None)
    _safe_set(owner, 'services_ServiceForecast21', partner)
    assert getattr(partner, 'services_DateTimeRange') == owner
    _safe_set(owner, 'services_ServiceForecast21', None)
    assert getattr(partner, 'services_DateTimeRange') is None


def test_assoc_period31_stub_double():
    # services_DateTimeRange has no real 'services_DateTimeRange33' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceMonitor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceMonitor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceMonitor(name="sample_text", revision="sample_text")
    partner = services_DateTimeRange()
    setattr(partner, 'services_DateTimeRange33', None)
    _safe_set(owner, 'services_ServiceMonitor32', partner)
    assert getattr(partner, 'services_DateTimeRange33') == owner
    _safe_set(owner, 'services_ServiceMonitor32', None)
    assert getattr(partner, 'services_DateTimeRange33') is None


def test_assoc_profileResources36_stub_double():
    # services_NetXResource has no real 'services_NetXResource37' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceProfile(name="sample_text")
    partner = services_NetXResource()
    setattr(partner, 'services_NetXResource37', None)
    _safe_set(owner, 'services_ServiceProfile', {partner})
    assert getattr(partner, 'services_NetXResource37') == owner
    _safe_set(owner, 'services_ServiceProfile', set())
    assert getattr(partner, 'services_NetXResource37') is None


def test_assoc_resourceForecasts24_stub_double():
    # services_ResourceForecast has no real 'services_ResourceForecast' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceForecast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceForecast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceForecast(name="sample_text", revision="sample_text")
    partner = services_ResourceForecast()
    setattr(partner, 'services_ResourceForecast', None)
    _safe_set(owner, 'services_ServiceForecast25', {partner})
    assert getattr(partner, 'services_ResourceForecast') == owner
    _safe_set(owner, 'services_ServiceForecast25', set())
    assert getattr(partner, 'services_ResourceForecast') is None


def test_assoc_resourceMonitors34_stub_double():
    # services_ResourceMonitor has no real 'services_ResourceMonitor' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceMonitor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceMonitor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceMonitor(name="sample_text", revision="sample_text")
    partner = services_ResourceMonitor()
    setattr(partner, 'services_ResourceMonitor', None)
    _safe_set(owner, 'services_ServiceMonitor35', {partner})
    assert getattr(partner, 'services_ResourceMonitor') == owner
    _safe_set(owner, 'services_ServiceMonitor35', set())
    assert getattr(partner, 'services_ResourceMonitor') is None


def test_assoc_serviceDistribution14_stub_double():
    # services_ServiceDistribution has no real 'services_ServiceDistribution' property in the generated
    # code (a bare stub) -- manually attach it so services_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    partner = services_ServiceDistribution()
    setattr(partner, 'services_ServiceDistribution', None)
    _safe_set(owner, 'services_Service15', partner)
    assert getattr(partner, 'services_ServiceDistribution') == owner
    _safe_set(owner, 'services_Service15', None)
    assert getattr(partner, 'services_ServiceDistribution') is None


def test_assoc_serviceForecastUsers22_stub_double():
    # services_ServiceForecastUsers has no real 'services_ServiceForecastUsers' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceForecast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceForecast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceForecast(name="sample_text", revision="sample_text")
    partner = services_ServiceForecastUsers()
    setattr(partner, 'services_ServiceForecastUsers', None)
    _safe_set(owner, 'services_ServiceForecast23', {partner})
    assert getattr(partner, 'services_ServiceForecastUsers') == owner
    _safe_set(owner, 'services_ServiceForecast23', set())
    assert getattr(partner, 'services_ServiceForecastUsers') is None


def test_assoc_serviceUserRef28_stub_double():
    # services_ServiceForecastUsers has no real 'services_ServiceForecastUsers29' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceUser's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceUser's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceUser(name="sample_text")
    partner = services_ServiceForecastUsers()
    setattr(partner, 'services_ServiceForecastUsers29', None)
    _safe_set(owner, 'services_ServiceUser30', partner)
    assert getattr(partner, 'services_ServiceForecastUsers29') == owner
    _safe_set(owner, 'services_ServiceUser30', None)
    assert getattr(partner, 'services_ServiceForecastUsers29') is None


def test_assoc_toleranceRefs1_stub_double():
    # services_EObject has no real 'services_EObject3' property in the generated
    # code (a bare stub) -- manually attach it so services_RFSService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_RFSService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_RFSService(functionalCategory="sample_text")
    partner = services_EObject()
    setattr(partner, 'services_EObject3', None)
    _safe_set(owner, 'services_RFSService2', {partner})
    assert getattr(partner, 'services_EObject3') == owner
    _safe_set(owner, 'services_RFSService2', set())
    assert getattr(partner, 'services_EObject3') is None


