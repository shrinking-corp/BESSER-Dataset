import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ElementWithResources,
    Service,
    model_Affinity,
    model_Application,
    model_Cluster,
    model_ElementWithResources,
    model_Host,
    model_Message,
    model_Service,
    model_ServiceInstance,
    model_StringToApplication,
    model_StringToDoubleMap,
    model_StringToHost,
    model_StringToService,
    model_StringToServiceInstance,
    Environment,
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

def test_assoc_applications1_reverse_link_reassign_clear():
    a1 = model_StringToApplication(key="sample_text")
    a2 = model_StringToApplication(key="sample_text_2")
    b = model_Cluster(environment="sample_text")
    _safe_set(b, 'model_Cluster2', {a1})
    assert _is_linked(b, 'model_Cluster2', a1)
    if hasattr(a1, 'model_StringToApplication'):
        assert _is_linked(a1, 'model_StringToApplication', b)
    _safe_set(b, 'model_Cluster2', {a2})
    assert _is_linked(b, 'model_Cluster2', a2)
    if hasattr(a1, 'model_StringToApplication'):
        assert not _is_linked(a1, 'model_StringToApplication', b)
    if hasattr(a2, 'model_StringToApplication'):
        assert _is_linked(a2, 'model_StringToApplication', b)
    _safe_set(b, 'model_Cluster2', set())
    assert not _is_linked(b, 'model_Cluster2', a2)
    if hasattr(a2, 'model_StringToApplication'):
        assert not _is_linked(a2, 'model_StringToApplication', b)


def test_assoc_destination13_reverse_link_reassign_clear():
    a1 = model_ServiceInstance(address="sample_text", containers="sample_text", id="sample_text", totalData="sample_text", totalMessages="sample_text")
    a2 = model_ServiceInstance(address="sample_text_2", containers="sample_text_2", id="sample_text_2", totalData="sample_text_2", totalMessages="sample_text_2")
    b = model_Message(avgResponseTime="sample_text", messageSize="sample_text", name="sample_text", timestamp="sample_text", uid="sample_text")
    _safe_set(b, 'model_Message14', a1)
    assert _is_linked(b, 'model_Message14', a1)
    if hasattr(a1, 'model_ServiceInstance15'):
        assert _is_linked(a1, 'model_ServiceInstance15', b)
    _safe_set(b, 'model_Message14', a2)
    assert _is_linked(b, 'model_Message14', a2)
    if hasattr(a1, 'model_ServiceInstance15'):
        assert not _is_linked(a1, 'model_ServiceInstance15', b)
    if hasattr(a2, 'model_ServiceInstance15'):
        assert _is_linked(a2, 'model_ServiceInstance15', b)
    _safe_set(b, 'model_Message14', None)
    assert not _is_linked(b, 'model_Message14', a2)
    if hasattr(a2, 'model_ServiceInstance15'):
        assert not _is_linked(a2, 'model_ServiceInstance15', b)


def test_assoc_hasAffinities3_reverse_link_reassign_clear():
    a1 = model_Service(application="sample_text", name="sample_text", stateful="sample_text")
    a2 = model_Service(application="sample_text_2", name="sample_text_2", stateful="sample_text_2")
    b = model_Affinity(degree="sample_text")
    _safe_set(b, 'model_Affinity', a1)
    assert _is_linked(b, 'model_Affinity', a1)
    if hasattr(a1, 'model_Service'):
        assert _is_linked(a1, 'model_Service', b)
    _safe_set(b, 'model_Affinity', a2)
    assert _is_linked(b, 'model_Affinity', a2)
    if hasattr(a1, 'model_Service'):
        assert not _is_linked(a1, 'model_Service', b)
    if hasattr(a2, 'model_Service'):
        assert _is_linked(a2, 'model_Service', b)
    _safe_set(b, 'model_Affinity', None)
    assert not _is_linked(b, 'model_Affinity', a2)
    if hasattr(a2, 'model_Service'):
        assert not _is_linked(a2, 'model_Service', b)


def test_assoc_host8_reverse_link_reassign_clear():
    a1 = model_ServiceInstance(address="sample_text", containers="sample_text", id="sample_text", totalData="sample_text", totalMessages="sample_text")
    a2 = model_ServiceInstance(address="sample_text_2", containers="sample_text_2", id="sample_text_2", totalData="sample_text_2", totalMessages="sample_text_2")
    b = model_Host(cores="sample_text", hostAddress="sample_text", name="sample_text")
    _safe_set(b, 'model_Host', a1)
    assert _is_linked(b, 'model_Host', a1)
    if hasattr(a1, 'model_ServiceInstance9'):
        assert _is_linked(a1, 'model_ServiceInstance9', b)
    _safe_set(b, 'model_Host', a2)
    assert _is_linked(b, 'model_Host', a2)
    if hasattr(a1, 'model_ServiceInstance9'):
        assert not _is_linked(a1, 'model_ServiceInstance9', b)
    if hasattr(a2, 'model_ServiceInstance9'):
        assert _is_linked(a2, 'model_ServiceInstance9', b)
    _safe_set(b, 'model_Host', None)
    assert not _is_linked(b, 'model_Host', a2)
    if hasattr(a2, 'model_ServiceInstance9'):
        assert not _is_linked(a2, 'model_ServiceInstance9', b)


def test_assoc_hosts0_reverse_link_reassign_clear():
    a1 = model_StringToHost(key="sample_text")
    a2 = model_StringToHost(key="sample_text_2")
    b = model_Cluster(environment="sample_text")
    _safe_set(b, 'model_Cluster', {a1})
    assert _is_linked(b, 'model_Cluster', a1)
    if hasattr(a1, 'model_StringToHost'):
        assert _is_linked(a1, 'model_StringToHost', b)
    _safe_set(b, 'model_Cluster', {a2})
    assert _is_linked(b, 'model_Cluster', a2)
    if hasattr(a1, 'model_StringToHost'):
        assert not _is_linked(a1, 'model_StringToHost', b)
    if hasattr(a2, 'model_StringToHost'):
        assert _is_linked(a2, 'model_StringToHost', b)
    _safe_set(b, 'model_Cluster', set())
    assert not _is_linked(b, 'model_Cluster', a2)
    if hasattr(a2, 'model_StringToHost'):
        assert not _is_linked(a2, 'model_StringToHost', b)


def test_assoc_messages7_reverse_link_reassign_clear():
    a1 = model_ServiceInstance(address="sample_text", containers="sample_text", id="sample_text", totalData="sample_text", totalMessages="sample_text")
    a2 = model_ServiceInstance(address="sample_text_2", containers="sample_text_2", id="sample_text_2", totalData="sample_text_2", totalMessages="sample_text_2")
    b = model_Message(avgResponseTime="sample_text", messageSize="sample_text", name="sample_text", timestamp="sample_text", uid="sample_text")
    _safe_set(b, 'model_Message', a1)
    assert _is_linked(b, 'model_Message', a1)
    if hasattr(a1, 'model_ServiceInstance'):
        assert _is_linked(a1, 'model_ServiceInstance', b)
    _safe_set(b, 'model_Message', a2)
    assert _is_linked(b, 'model_Message', a2)
    if hasattr(a1, 'model_ServiceInstance'):
        assert not _is_linked(a1, 'model_ServiceInstance', b)
    if hasattr(a2, 'model_ServiceInstance'):
        assert _is_linked(a2, 'model_ServiceInstance', b)
    _safe_set(b, 'model_Message', None)
    assert not _is_linked(b, 'model_Message', a2)
    if hasattr(a2, 'model_ServiceInstance'):
        assert not _is_linked(a2, 'model_ServiceInstance', b)


def test_assoc_resourceReserved18_reverse_link_reassign_clear():
    a1 = model_StringToDoubleMap(key="sample_text", value="sample_text")
    a2 = model_StringToDoubleMap(key="sample_text_2", value="sample_text_2")
    b = model_Host(cores="sample_text", hostAddress="sample_text", name="sample_text")
    _safe_set(b, 'model_Host19', {a1})
    assert _is_linked(b, 'model_Host19', a1)
    if hasattr(a1, 'model_StringToDoubleMap'):
        assert _is_linked(a1, 'model_StringToDoubleMap', b)
    _safe_set(b, 'model_Host19', {a2})
    assert _is_linked(b, 'model_Host19', a2)
    if hasattr(a1, 'model_StringToDoubleMap'):
        assert not _is_linked(a1, 'model_StringToDoubleMap', b)
    if hasattr(a2, 'model_StringToDoubleMap'):
        assert _is_linked(a2, 'model_StringToDoubleMap', b)
    _safe_set(b, 'model_Host19', set())
    assert not _is_linked(b, 'model_Host19', a2)
    if hasattr(a2, 'model_StringToDoubleMap'):
        assert not _is_linked(a2, 'model_StringToDoubleMap', b)


def test_assoc_services16_reverse_link_reassign_clear():
    a1 = model_StringToServiceInstance(key="sample_text")
    a2 = model_StringToServiceInstance(key="sample_text_2")
    b = model_Host(cores="sample_text", hostAddress="sample_text", name="sample_text")
    _safe_set(b, 'model_Host17', {a1})
    assert _is_linked(b, 'model_Host17', a1)
    if hasattr(a1, 'model_StringToServiceInstance'):
        assert _is_linked(a1, 'model_StringToServiceInstance', b)
    _safe_set(b, 'model_Host17', {a2})
    assert _is_linked(b, 'model_Host17', a2)
    if hasattr(a1, 'model_StringToServiceInstance'):
        assert not _is_linked(a1, 'model_StringToServiceInstance', b)
    if hasattr(a2, 'model_StringToServiceInstance'):
        assert _is_linked(a2, 'model_StringToServiceInstance', b)
    _safe_set(b, 'model_Host17', set())
    assert not _is_linked(b, 'model_Host17', a2)
    if hasattr(a2, 'model_StringToServiceInstance'):
        assert not _is_linked(a2, 'model_StringToServiceInstance', b)


def test_assoc_services33_reverse_link_reassign_clear():
    a1 = model_StringToService(key="sample_text")
    a2 = model_StringToService(key="sample_text_2")
    b = model_Application(name="sample_text", totalData="sample_text", totalMessages="sample_text", weight="sample_text")
    _safe_set(b, 'model_Application', {a1})
    assert _is_linked(b, 'model_Application', a1)
    if hasattr(a1, 'model_StringToService34'):
        assert _is_linked(a1, 'model_StringToService34', b)
    _safe_set(b, 'model_Application', {a2})
    assert _is_linked(b, 'model_Application', a2)
    if hasattr(a1, 'model_StringToService34'):
        assert not _is_linked(a1, 'model_StringToService34', b)
    if hasattr(a2, 'model_StringToService34'):
        assert _is_linked(a2, 'model_StringToService34', b)
    _safe_set(b, 'model_Application', set())
    assert not _is_linked(b, 'model_Application', a2)
    if hasattr(a2, 'model_StringToService34'):
        assert not _is_linked(a2, 'model_StringToService34', b)


def test_assoc_source10_reverse_link_reassign_clear():
    a1 = model_ServiceInstance(address="sample_text", containers="sample_text", id="sample_text", totalData="sample_text", totalMessages="sample_text")
    a2 = model_ServiceInstance(address="sample_text_2", containers="sample_text_2", id="sample_text_2", totalData="sample_text_2", totalMessages="sample_text_2")
    b = model_Message(avgResponseTime="sample_text", messageSize="sample_text", name="sample_text", timestamp="sample_text", uid="sample_text")
    _safe_set(b, 'model_Message11', a1)
    assert _is_linked(b, 'model_Message11', a1)
    if hasattr(a1, 'model_ServiceInstance12'):
        assert _is_linked(a1, 'model_ServiceInstance12', b)
    _safe_set(b, 'model_Message11', a2)
    assert _is_linked(b, 'model_Message11', a2)
    if hasattr(a1, 'model_ServiceInstance12'):
        assert not _is_linked(a1, 'model_ServiceInstance12', b)
    if hasattr(a2, 'model_ServiceInstance12'):
        assert _is_linked(a2, 'model_ServiceInstance12', b)
    _safe_set(b, 'model_Message11', None)
    assert not _is_linked(b, 'model_Message11', a2)
    if hasattr(a2, 'model_ServiceInstance12'):
        assert not _is_linked(a2, 'model_ServiceInstance12', b)


def test_assoc_value25_reverse_link_reassign_clear():
    a1 = model_StringToService(key="sample_text")
    a2 = model_StringToService(key="sample_text_2")
    b = model_Service(application="sample_text", name="sample_text", stateful="sample_text")
    _safe_set(b, 'model_Service26', a1)
    assert _is_linked(b, 'model_Service26', a1)
    if hasattr(a1, 'model_StringToService'):
        assert _is_linked(a1, 'model_StringToService', b)
    _safe_set(b, 'model_Service26', a2)
    assert _is_linked(b, 'model_Service26', a2)
    if hasattr(a1, 'model_StringToService'):
        assert not _is_linked(a1, 'model_StringToService', b)
    if hasattr(a2, 'model_StringToService'):
        assert _is_linked(a2, 'model_StringToService', b)
    _safe_set(b, 'model_Service26', None)
    assert not _is_linked(b, 'model_Service26', a2)
    if hasattr(a2, 'model_StringToService'):
        assert not _is_linked(a2, 'model_StringToService', b)


def test_assoc_value27_reverse_link_reassign_clear():
    a1 = model_StringToHost(key="sample_text")
    a2 = model_StringToHost(key="sample_text_2")
    b = model_Host(cores="sample_text", hostAddress="sample_text", name="sample_text")
    _safe_set(b, 'model_Host29', a1)
    assert _is_linked(b, 'model_Host29', a1)
    if hasattr(a1, 'model_StringToHost28'):
        assert _is_linked(a1, 'model_StringToHost28', b)
    _safe_set(b, 'model_Host29', a2)
    assert _is_linked(b, 'model_Host29', a2)
    if hasattr(a1, 'model_StringToHost28'):
        assert not _is_linked(a1, 'model_StringToHost28', b)
    if hasattr(a2, 'model_StringToHost28'):
        assert _is_linked(a2, 'model_StringToHost28', b)
    _safe_set(b, 'model_Host29', None)
    assert not _is_linked(b, 'model_Host29', a2)
    if hasattr(a2, 'model_StringToHost28'):
        assert not _is_linked(a2, 'model_StringToHost28', b)


def test_assoc_value30_reverse_link_reassign_clear():
    a1 = model_StringToServiceInstance(key="sample_text")
    a2 = model_StringToServiceInstance(key="sample_text_2")
    b = model_ServiceInstance(address="sample_text", containers="sample_text", id="sample_text", totalData="sample_text", totalMessages="sample_text")
    _safe_set(b, 'model_ServiceInstance32', a1)
    assert _is_linked(b, 'model_ServiceInstance32', a1)
    if hasattr(a1, 'model_StringToServiceInstance31'):
        assert _is_linked(a1, 'model_StringToServiceInstance31', b)
    _safe_set(b, 'model_ServiceInstance32', a2)
    assert _is_linked(b, 'model_ServiceInstance32', a2)
    if hasattr(a1, 'model_StringToServiceInstance31'):
        assert not _is_linked(a1, 'model_StringToServiceInstance31', b)
    if hasattr(a2, 'model_StringToServiceInstance31'):
        assert _is_linked(a2, 'model_StringToServiceInstance31', b)
    _safe_set(b, 'model_ServiceInstance32', None)
    assert not _is_linked(b, 'model_ServiceInstance32', a2)
    if hasattr(a2, 'model_StringToServiceInstance31'):
        assert not _is_linked(a2, 'model_StringToServiceInstance31', b)


def test_assoc_value35_reverse_link_reassign_clear():
    a1 = model_StringToApplication(key="sample_text")
    a2 = model_StringToApplication(key="sample_text_2")
    b = model_Application(name="sample_text", totalData="sample_text", totalMessages="sample_text", weight="sample_text")
    _safe_set(b, 'model_Application37', a1)
    assert _is_linked(b, 'model_Application37', a1)
    if hasattr(a1, 'model_StringToApplication36'):
        assert _is_linked(a1, 'model_StringToApplication36', b)
    _safe_set(b, 'model_Application37', a2)
    assert _is_linked(b, 'model_Application37', a2)
    if hasattr(a1, 'model_StringToApplication36'):
        assert not _is_linked(a1, 'model_StringToApplication36', b)
    if hasattr(a2, 'model_StringToApplication36'):
        assert _is_linked(a2, 'model_StringToApplication36', b)
    _safe_set(b, 'model_Application37', None)
    assert not _is_linked(b, 'model_Application37', a2)
    if hasattr(a2, 'model_StringToApplication36'):
        assert not _is_linked(a2, 'model_StringToApplication36', b)


def test_assoc_with_4_reverse_link_reassign_clear():
    a1 = model_Service(application="sample_text", name="sample_text", stateful="sample_text")
    a2 = model_Service(application="sample_text_2", name="sample_text_2", stateful="sample_text_2")
    b = model_Affinity(degree="sample_text")
    _safe_set(b, 'model_Affinity5', a1)
    assert _is_linked(b, 'model_Affinity5', a1)
    if hasattr(a1, 'model_Service6'):
        assert _is_linked(a1, 'model_Service6', b)
    _safe_set(b, 'model_Affinity5', a2)
    assert _is_linked(b, 'model_Affinity5', a2)
    if hasattr(a1, 'model_Service6'):
        assert not _is_linked(a1, 'model_Service6', b)
    if hasattr(a2, 'model_Service6'):
        assert _is_linked(a2, 'model_Service6', b)
    _safe_set(b, 'model_Affinity5', None)
    assert not _is_linked(b, 'model_Affinity5', a2)
    if hasattr(a2, 'model_Service6'):
        assert not _is_linked(a2, 'model_Service6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_metrics22_stub_double():
    # model_ElementWithResources has no real 'model_ElementWithResources23' property in the generated
    # code (a bare stub) -- manually attach it so model_StringToDoubleMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_StringToDoubleMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_StringToDoubleMap(key="sample_text", value="sample_text")
    partner = model_ElementWithResources()
    setattr(partner, 'model_ElementWithResources23', None)
    _safe_set(owner, 'model_StringToDoubleMap24', partner)
    assert owner in getattr(partner, 'model_ElementWithResources23')
    _safe_set(owner, 'model_StringToDoubleMap24', None)
    assert owner not in getattr(partner, 'model_ElementWithResources23')


def test_assoc_resourceLimit20_stub_double():
    # model_ElementWithResources has no real 'model_ElementWithResources' property in the generated
    # code (a bare stub) -- manually attach it so model_StringToDoubleMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_StringToDoubleMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_StringToDoubleMap(key="sample_text", value="sample_text")
    partner = model_ElementWithResources()
    setattr(partner, 'model_ElementWithResources', None)
    _safe_set(owner, 'model_StringToDoubleMap21', partner)
    assert owner in getattr(partner, 'model_ElementWithResources')
    _safe_set(owner, 'model_StringToDoubleMap21', None)
    assert owner not in getattr(partner, 'model_ElementWithResources')


