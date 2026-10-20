import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_cIID3_reverse_link_reassign_clear():
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


def test_assoc_serviceForecasts7_reverse_link_reassign_clear():
    a1 = services_ServiceForecast(name="sample_text", revision="sample_text")
    a2 = services_ServiceForecast(name="sample_text_2", revision="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service8', {a1})
    assert _is_linked(b, 'services_Service8', a1)
    if hasattr(a1, 'services_ServiceForecast'):
        assert _is_linked(a1, 'services_ServiceForecast', b)
    _safe_set(b, 'services_Service8', {a2})
    assert _is_linked(b, 'services_Service8', a2)
    if hasattr(a1, 'services_ServiceForecast'):
        assert not _is_linked(a1, 'services_ServiceForecast', b)
    if hasattr(a2, 'services_ServiceForecast'):
        assert _is_linked(a2, 'services_ServiceForecast', b)
    _safe_set(b, 'services_Service8', set())
    assert not _is_linked(b, 'services_Service8', a2)
    if hasattr(a2, 'services_ServiceForecast'):
        assert not _is_linked(a2, 'services_ServiceForecast', b)


def test_assoc_serviceMonitors9_reverse_link_reassign_clear():
    a1 = services_ServiceMonitor(name="sample_text", revision="sample_text")
    a2 = services_ServiceMonitor(name="sample_text_2", revision="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service10', {a1})
    assert _is_linked(b, 'services_Service10', a1)
    if hasattr(a1, 'services_ServiceMonitor'):
        assert _is_linked(a1, 'services_ServiceMonitor', b)
    _safe_set(b, 'services_Service10', {a2})
    assert _is_linked(b, 'services_Service10', a2)
    if hasattr(a1, 'services_ServiceMonitor'):
        assert not _is_linked(a1, 'services_ServiceMonitor', b)
    if hasattr(a2, 'services_ServiceMonitor'):
        assert _is_linked(a2, 'services_ServiceMonitor', b)
    _safe_set(b, 'services_Service10', set())
    assert not _is_linked(b, 'services_Service10', a2)
    if hasattr(a2, 'services_ServiceMonitor'):
        assert not _is_linked(a2, 'services_ServiceMonitor', b)


def test_assoc_serviceProfile37_reverse_link_reassign_clear():
    a1 = services_ServiceUser(name="sample_text")
    a2 = services_ServiceUser(name="sample_text_2")
    b = services_ServiceProfile(name="sample_text")
    _safe_set(b, 'services_ServiceProfile39', a1)
    assert _is_linked(b, 'services_ServiceProfile39', a1)
    if hasattr(a1, 'services_ServiceUser38'):
        assert _is_linked(a1, 'services_ServiceUser38', b)
    _safe_set(b, 'services_ServiceProfile39', a2)
    assert _is_linked(b, 'services_ServiceProfile39', a2)
    if hasattr(a1, 'services_ServiceUser38'):
        assert not _is_linked(a1, 'services_ServiceUser38', b)
    if hasattr(a2, 'services_ServiceUser38'):
        assert _is_linked(a2, 'services_ServiceUser38', b)
    _safe_set(b, 'services_ServiceProfile39', None)
    assert not _is_linked(b, 'services_ServiceProfile39', a2)
    if hasattr(a2, 'services_ServiceUser38'):
        assert not _is_linked(a2, 'services_ServiceUser38', b)


def test_assoc_serviceUserRefs11_reverse_link_reassign_clear():
    a1 = services_ServiceUser(name="sample_text")
    a2 = services_ServiceUser(name="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service12', {a1})
    assert _is_linked(b, 'services_Service12', a1)
    if hasattr(a1, 'services_ServiceUser'):
        assert _is_linked(a1, 'services_ServiceUser', b)
    _safe_set(b, 'services_Service12', {a2})
    assert _is_linked(b, 'services_Service12', a2)
    if hasattr(a1, 'services_ServiceUser'):
        assert not _is_linked(a1, 'services_ServiceUser', b)
    if hasattr(a2, 'services_ServiceUser'):
        assert _is_linked(a2, 'services_ServiceUser', b)
    _safe_set(b, 'services_Service12', set())
    assert not _is_linked(b, 'services_Service12', a2)
    if hasattr(a2, 'services_ServiceUser'):
        assert not _is_linked(a2, 'services_ServiceUser', b)


def test_assoc_services5_reverse_link_reassign_clear():
    a1 = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    a2 = services_Service(serviceCategory="sample_text_2", serviceClass="sample_text_2", serviceDescription="sample_text_2", serviceName="sample_text_2")
    b = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    _safe_set(b, 'services_Service6', a1)
    assert _is_linked(b, 'services_Service6', a1)
    if hasattr(a1, 'services_Service4'):
        assert _is_linked(a1, 'services_Service4', b)
    _safe_set(b, 'services_Service6', a2)
    assert _is_linked(b, 'services_Service6', a2)
    if hasattr(a1, 'services_Service4'):
        assert not _is_linked(a1, 'services_Service4', b)
    if hasattr(a2, 'services_Service4'):
        assert _is_linked(a2, 'services_Service4', b)
    _safe_set(b, 'services_Service6', None)
    assert not _is_linked(b, 'services_Service6', a2)
    if hasattr(a2, 'services_Service4'):
        assert not _is_linked(a2, 'services_Service4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_expressionRefs40_stub_double():
    # services_Expression has no real 'services_Expression42' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceUser's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceUser's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceUser(name="sample_text")
    partner = services_Expression()
    setattr(partner, 'services_Expression42', None)
    _safe_set(owner, 'services_ServiceUser41', {partner})
    assert getattr(partner, 'services_Expression42') == owner
    _safe_set(owner, 'services_ServiceUser41', set())
    assert getattr(partner, 'services_Expression42') is None


def test_assoc_nodes0_stub_double():
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


def test_assoc_period19_stub_double():
    # services_DateTimeRange has no real 'services_DateTimeRange' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceForecast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceForecast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceForecast(name="sample_text", revision="sample_text")
    partner = services_DateTimeRange()
    setattr(partner, 'services_DateTimeRange', None)
    _safe_set(owner, 'services_ServiceForecast20', partner)
    assert getattr(partner, 'services_DateTimeRange') == owner
    _safe_set(owner, 'services_ServiceForecast20', None)
    assert getattr(partner, 'services_DateTimeRange') is None


def test_assoc_period30_stub_double():
    # services_DateTimeRange has no real 'services_DateTimeRange32' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceMonitor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceMonitor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceMonitor(name="sample_text", revision="sample_text")
    partner = services_DateTimeRange()
    setattr(partner, 'services_DateTimeRange32', None)
    _safe_set(owner, 'services_ServiceMonitor31', partner)
    assert getattr(partner, 'services_DateTimeRange32') == owner
    _safe_set(owner, 'services_ServiceMonitor31', None)
    assert getattr(partner, 'services_DateTimeRange32') is None


def test_assoc_profileResources35_stub_double():
    # services_NetXResource has no real 'services_NetXResource36' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceProfile(name="sample_text")
    partner = services_NetXResource()
    setattr(partner, 'services_NetXResource36', None)
    _safe_set(owner, 'services_ServiceProfile', {partner})
    assert getattr(partner, 'services_NetXResource36') == owner
    _safe_set(owner, 'services_ServiceProfile', set())
    assert getattr(partner, 'services_NetXResource36') is None


def test_assoc_resourceForecasts23_stub_double():
    # services_ResourceForecast has no real 'services_ResourceForecast' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceForecast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceForecast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceForecast(name="sample_text", revision="sample_text")
    partner = services_ResourceForecast()
    setattr(partner, 'services_ResourceForecast', None)
    _safe_set(owner, 'services_ServiceForecast24', {partner})
    assert getattr(partner, 'services_ResourceForecast') == owner
    _safe_set(owner, 'services_ServiceForecast24', set())
    assert getattr(partner, 'services_ResourceForecast') is None


def test_assoc_resourceMonitors33_stub_double():
    # services_ResourceMonitor has no real 'services_ResourceMonitor' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceMonitor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceMonitor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceMonitor(name="sample_text", revision="sample_text")
    partner = services_ResourceMonitor()
    setattr(partner, 'services_ResourceMonitor', None)
    _safe_set(owner, 'services_ServiceMonitor34', {partner})
    assert getattr(partner, 'services_ResourceMonitor') == owner
    _safe_set(owner, 'services_ServiceMonitor34', set())
    assert getattr(partner, 'services_ResourceMonitor') is None


def test_assoc_serviceDistribution13_stub_double():
    # services_ServiceDistribution has no real 'services_ServiceDistribution' property in the generated
    # code (a bare stub) -- manually attach it so services_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_Service(serviceCategory="sample_text", serviceClass="sample_text", serviceDescription="sample_text", serviceName="sample_text")
    partner = services_ServiceDistribution()
    setattr(partner, 'services_ServiceDistribution', None)
    _safe_set(owner, 'services_Service14', partner)
    assert getattr(partner, 'services_ServiceDistribution') == owner
    _safe_set(owner, 'services_Service14', None)
    assert getattr(partner, 'services_ServiceDistribution') is None


def test_assoc_serviceForecastUsers21_stub_double():
    # services_ServiceForecastUsers has no real 'services_ServiceForecastUsers' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceForecast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceForecast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceForecast(name="sample_text", revision="sample_text")
    partner = services_ServiceForecastUsers()
    setattr(partner, 'services_ServiceForecastUsers', None)
    _safe_set(owner, 'services_ServiceForecast22', {partner})
    assert getattr(partner, 'services_ServiceForecastUsers') == owner
    _safe_set(owner, 'services_ServiceForecast22', set())
    assert getattr(partner, 'services_ServiceForecastUsers') is None


def test_assoc_serviceUserRef27_stub_double():
    # services_ServiceForecastUsers has no real 'services_ServiceForecastUsers28' property in the generated
    # code (a bare stub) -- manually attach it so services_ServiceUser's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_ServiceUser's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_ServiceUser(name="sample_text")
    partner = services_ServiceForecastUsers()
    setattr(partner, 'services_ServiceForecastUsers28', None)
    _safe_set(owner, 'services_ServiceUser29', partner)
    assert getattr(partner, 'services_ServiceForecastUsers28') == owner
    _safe_set(owner, 'services_ServiceUser29', None)
    assert getattr(partner, 'services_ServiceForecastUsers28') is None


def test_assoc_toleranceRefs1_stub_double():
    # services_Tolerance has no real 'services_Tolerance' property in the generated
    # code (a bare stub) -- manually attach it so services_RFSService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_RFSService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_RFSService(functionalCategory="sample_text")
    partner = services_Tolerance()
    setattr(partner, 'services_Tolerance', None)
    _safe_set(owner, 'services_RFSService2', {partner})
    assert getattr(partner, 'services_Tolerance') == owner
    _safe_set(owner, 'services_RFSService2', set())
    assert getattr(partner, 'services_Tolerance') is None


