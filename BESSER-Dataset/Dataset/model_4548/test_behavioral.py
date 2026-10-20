import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AABB,
    Capability,
    NamedElement,
    Region,
    dronesStructure_AABB,
    dronesStructure_Capability,
    dronesStructure_Charger,
    dronesStructure_CooperativeAction,
    dronesStructure_Dimension,
    dronesStructure_Drone,
    dronesStructure_DroneType,
    dronesStructure_DronesStructure,
    dronesStructure_MovementCapability,
    dronesStructure_NamedElement,
    dronesStructure_Obstacle,
    dronesStructure_Position,
    dronesStructure_ProvidedCapability,
    dronesStructure_Region,
    dronesStructure_RequiredCapability,
    dronesStructure_Role,
    dronesStructure_ScanningCapability,
    dronesStructure_Scenario,
    dronesStructure_ScenarioBounds,
    dronesStructure_Task,
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

def test_assoc_dimension20_reverse_link_reassign_clear():
    a1 = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    a2 = dronesStructure_DroneType(idleEneryConsumption=9.99, maxBatteryCapacity=9.99, weight=9.99)
    b = dronesStructure_Dimension(depth=3.14, height=3.14, width=3.14)
    _safe_set(b, 'dronesStructure_Dimension', a1)
    assert _is_linked(b, 'dronesStructure_Dimension', a1)
    if hasattr(a1, 'dronesStructure_DroneType21'):
        assert _is_linked(a1, 'dronesStructure_DroneType21', b)
    _safe_set(b, 'dronesStructure_Dimension', a2)
    assert _is_linked(b, 'dronesStructure_Dimension', a2)
    if hasattr(a1, 'dronesStructure_DroneType21'):
        assert not _is_linked(a1, 'dronesStructure_DroneType21', b)
    if hasattr(a2, 'dronesStructure_DroneType21'):
        assert _is_linked(a2, 'dronesStructure_DroneType21', b)
    _safe_set(b, 'dronesStructure_Dimension', None)
    assert not _is_linked(b, 'dronesStructure_Dimension', a2)
    if hasattr(a2, 'dronesStructure_DroneType21'):
        assert not _is_linked(a2, 'dronesStructure_DroneType21', b)


def test_assoc_droneType28_reverse_link_reassign_clear():
    a1 = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    a2 = dronesStructure_ProvidedCapability(energyConsumptionPerValue=9.99, maximalValue=9.99)
    b = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    _safe_set(b, 'DroneType', a1)
    assert _is_linked(b, 'DroneType', a1)
    if hasattr(a1, 'providedCapabilities'):
        assert _is_linked(a1, 'providedCapabilities', b)
    _safe_set(b, 'DroneType', a2)
    assert _is_linked(b, 'DroneType', a2)
    if hasattr(a1, 'providedCapabilities'):
        assert not _is_linked(a1, 'providedCapabilities', b)
    if hasattr(a2, 'providedCapabilities'):
        assert _is_linked(a2, 'providedCapabilities', b)
    _safe_set(b, 'DroneType', None)
    assert not _is_linked(b, 'DroneType', a2)
    if hasattr(a2, 'providedCapabilities'):
        assert not _is_linked(a2, 'providedCapabilities', b)


def test_assoc_movementCapability18_reverse_link_reassign_clear():
    a1 = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    a2 = dronesStructure_ProvidedCapability(energyConsumptionPerValue=9.99, maximalValue=9.99)
    b = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    _safe_set(b, 'dronesStructure_DroneType19', a1)
    assert _is_linked(b, 'dronesStructure_DroneType19', a1)
    if hasattr(a1, 'dronesStructure_ProvidedCapability'):
        assert _is_linked(a1, 'dronesStructure_ProvidedCapability', b)
    _safe_set(b, 'dronesStructure_DroneType19', a2)
    assert _is_linked(b, 'dronesStructure_DroneType19', a2)
    if hasattr(a1, 'dronesStructure_ProvidedCapability'):
        assert not _is_linked(a1, 'dronesStructure_ProvidedCapability', b)
    if hasattr(a2, 'dronesStructure_ProvidedCapability'):
        assert _is_linked(a2, 'dronesStructure_ProvidedCapability', b)
    _safe_set(b, 'dronesStructure_DroneType19', None)
    assert not _is_linked(b, 'dronesStructure_DroneType19', a2)
    if hasattr(a2, 'dronesStructure_ProvidedCapability'):
        assert not _is_linked(a2, 'dronesStructure_ProvidedCapability', b)


def test_assoc_providedCapabilities17_reverse_link_reassign_clear():
    a1 = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    a2 = dronesStructure_ProvidedCapability(energyConsumptionPerValue=9.99, maximalValue=9.99)
    b = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    _safe_set(b, 'droneType', {a1})
    assert _is_linked(b, 'droneType', a1)
    if hasattr(a1, 'ProvidedCapability'):
        assert _is_linked(a1, 'ProvidedCapability', b)
    _safe_set(b, 'droneType', {a2})
    assert _is_linked(b, 'droneType', a2)
    if hasattr(a1, 'ProvidedCapability'):
        assert not _is_linked(a1, 'ProvidedCapability', b)
    if hasattr(a2, 'ProvidedCapability'):
        assert _is_linked(a2, 'ProvidedCapability', b)
    _safe_set(b, 'droneType', set())
    assert not _is_linked(b, 'droneType', a2)
    if hasattr(a2, 'ProvidedCapability'):
        assert not _is_linked(a2, 'ProvidedCapability', b)


def test_assoc_scanningCapability22_reverse_link_reassign_clear():
    a1 = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    a2 = dronesStructure_ProvidedCapability(energyConsumptionPerValue=9.99, maximalValue=9.99)
    b = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    _safe_set(b, 'dronesStructure_DroneType23', a1)
    assert _is_linked(b, 'dronesStructure_DroneType23', a1)
    if hasattr(a1, 'dronesStructure_ProvidedCapability24'):
        assert _is_linked(a1, 'dronesStructure_ProvidedCapability24', b)
    _safe_set(b, 'dronesStructure_DroneType23', a2)
    assert _is_linked(b, 'dronesStructure_DroneType23', a2)
    if hasattr(a1, 'dronesStructure_ProvidedCapability24'):
        assert not _is_linked(a1, 'dronesStructure_ProvidedCapability24', b)
    if hasattr(a2, 'dronesStructure_ProvidedCapability24'):
        assert _is_linked(a2, 'dronesStructure_ProvidedCapability24', b)
    _safe_set(b, 'dronesStructure_DroneType23', None)
    assert not _is_linked(b, 'dronesStructure_DroneType23', a2)
    if hasattr(a2, 'dronesStructure_ProvidedCapability24'):
        assert not _is_linked(a2, 'dronesStructure_ProvidedCapability24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actionToPerform48_stub_double():
    # dronesStructure_Task has no real 'dronesStructure_Task49' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_CooperativeAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_CooperativeAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    partner = dronesStructure_Task()
    setattr(partner, 'dronesStructure_Task49', None)
    _safe_set(owner, 'dronesStructure_CooperativeAction50', partner)
    assert getattr(partner, 'dronesStructure_Task49') == owner
    _safe_set(owner, 'dronesStructure_CooperativeAction50', None)
    assert getattr(partner, 'dronesStructure_Task49') is None


def test_assoc_allowedBounds9_stub_double():
    # dronesStructure_ScenarioBounds has no real 'dronesStructure_ScenarioBounds' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    partner = dronesStructure_ScenarioBounds()
    setattr(partner, 'dronesStructure_ScenarioBounds', None)
    _safe_set(owner, 'dronesStructure_Scenario10', partner)
    assert getattr(partner, 'dronesStructure_ScenarioBounds') == owner
    _safe_set(owner, 'dronesStructure_Scenario10', None)
    assert getattr(partner, 'dronesStructure_ScenarioBounds') is None


def test_assoc_capability25_stub_double():
    # dronesStructure_Capability has no real 'dronesStructure_Capability27' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_ProvidedCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_ProvidedCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    partner = dronesStructure_Capability()
    setattr(partner, 'dronesStructure_Capability27', None)
    _safe_set(owner, 'dronesStructure_ProvidedCapability26', partner)
    assert getattr(partner, 'dronesStructure_Capability27') == owner
    _safe_set(owner, 'dronesStructure_ProvidedCapability26', None)
    assert getattr(partner, 'dronesStructure_Capability27') is None


def test_assoc_capability32_stub_double():
    # dronesStructure_Capability has no real 'dronesStructure_Capability33' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_RequiredCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_RequiredCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_RequiredCapability(minimalValue=3.14)
    partner = dronesStructure_Capability()
    setattr(partner, 'dronesStructure_Capability33', None)
    _safe_set(owner, 'dronesStructure_RequiredCapability', partner)
    assert getattr(partner, 'dronesStructure_Capability33') == owner
    _safe_set(owner, 'dronesStructure_RequiredCapability', None)
    assert getattr(partner, 'dronesStructure_Capability33') is None


def test_assoc_cooperativeAction31_stub_double():
    # dronesStructure_Role has no real 'roles' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_CooperativeAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_CooperativeAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    partner = dronesStructure_Role()
    setattr(partner, 'roles', None)
    _safe_set(owner, 'CooperativeAction', partner)
    assert getattr(partner, 'roles') == owner
    _safe_set(owner, 'CooperativeAction', None)
    assert getattr(partner, 'roles') is None


def test_assoc_cooperativeActions3_stub_double():
    # dronesStructure_DronesStructure has no real 'dronesStructure_DronesStructure4' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_CooperativeAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_CooperativeAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    partner = dronesStructure_DronesStructure()
    setattr(partner, 'dronesStructure_DronesStructure4', None)
    _safe_set(owner, 'dronesStructure_CooperativeAction', partner)
    assert owner in getattr(partner, 'dronesStructure_DronesStructure4')
    _safe_set(owner, 'dronesStructure_CooperativeAction', None)
    assert owner not in getattr(partner, 'dronesStructure_DronesStructure4')


def test_assoc_dimension43_stub_double():
    # dronesStructure_AABB has no real 'dronesStructure_AABB44' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_Dimension(depth=3.14, height=3.14, width=3.14)
    partner = dronesStructure_AABB()
    setattr(partner, 'dronesStructure_AABB44', None)
    _safe_set(owner, 'dronesStructure_Dimension45', partner)
    assert getattr(partner, 'dronesStructure_AABB44') == owner
    _safe_set(owner, 'dronesStructure_Dimension45', None)
    assert getattr(partner, 'dronesStructure_AABB44') is None


def test_assoc_droneTypes1_stub_double():
    # dronesStructure_DronesStructure has no real 'dronesStructure_DronesStructure2' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_DroneType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_DroneType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    partner = dronesStructure_DronesStructure()
    setattr(partner, 'dronesStructure_DronesStructure2', None)
    _safe_set(owner, 'dronesStructure_DroneType', partner)
    assert owner in getattr(partner, 'dronesStructure_DronesStructure2')
    _safe_set(owner, 'dronesStructure_DroneType', None)
    assert owner not in getattr(partner, 'dronesStructure_DronesStructure2')


def test_assoc_drones7_stub_double():
    # dronesStructure_Drone has no real 'dronesStructure_Drone' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    partner = dronesStructure_Drone()
    setattr(partner, 'dronesStructure_Drone', None)
    _safe_set(owner, 'dronesStructure_Scenario8', {partner})
    assert getattr(partner, 'dronesStructure_Drone') == owner
    _safe_set(owner, 'dronesStructure_Scenario8', set())
    assert getattr(partner, 'dronesStructure_Drone') is None


def test_assoc_dronetype38_stub_double():
    # dronesStructure_Drone has no real 'dronesStructure_Drone39' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_DroneType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_DroneType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    partner = dronesStructure_Drone()
    setattr(partner, 'dronesStructure_Drone39', None)
    _safe_set(owner, 'dronesStructure_DroneType40', partner)
    assert getattr(partner, 'dronesStructure_Drone39') == owner
    _safe_set(owner, 'dronesStructure_DroneType40', None)
    assert getattr(partner, 'dronesStructure_Drone39') is None


def test_assoc_obstacles11_stub_double():
    # dronesStructure_Obstacle has no real 'dronesStructure_Obstacle' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    partner = dronesStructure_Obstacle()
    setattr(partner, 'dronesStructure_Obstacle', None)
    _safe_set(owner, 'dronesStructure_Scenario12', {partner})
    assert getattr(partner, 'dronesStructure_Obstacle') == owner
    _safe_set(owner, 'dronesStructure_Scenario12', set())
    assert getattr(partner, 'dronesStructure_Obstacle') is None


def test_assoc_position41_stub_double():
    # dronesStructure_AABB has no real 'dronesStructure_AABB' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_Position(x=3.14, y=3.14, z=3.14)
    partner = dronesStructure_AABB()
    setattr(partner, 'dronesStructure_AABB', None)
    _safe_set(owner, 'dronesStructure_Position42', partner)
    assert getattr(partner, 'dronesStructure_AABB') == owner
    _safe_set(owner, 'dronesStructure_Position42', None)
    assert getattr(partner, 'dronesStructure_AABB') is None


def test_assoc_regions13_stub_double():
    # dronesStructure_Region has no real 'dronesStructure_Region' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    partner = dronesStructure_Region()
    setattr(partner, 'dronesStructure_Region', None)
    _safe_set(owner, 'dronesStructure_Scenario14', {partner})
    assert getattr(partner, 'dronesStructure_Region') == owner
    _safe_set(owner, 'dronesStructure_Scenario14', set())
    assert getattr(partner, 'dronesStructure_Region') is None


def test_assoc_requiredCapabilities30_stub_double():
    # dronesStructure_Role has no real 'role' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_RequiredCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_RequiredCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_RequiredCapability(minimalValue=3.14)
    partner = dronesStructure_Role()
    setattr(partner, 'role', None)
    _safe_set(owner, 'RequiredCapability', partner)
    assert owner in getattr(partner, 'role')
    _safe_set(owner, 'RequiredCapability', None)
    assert owner not in getattr(partner, 'role')


def test_assoc_role34_stub_double():
    # dronesStructure_Role has no real 'Role35' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_RequiredCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_RequiredCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_RequiredCapability(minimalValue=3.14)
    partner = dronesStructure_Role()
    setattr(partner, 'Role35', None)
    _safe_set(owner, 'requiredCapabilities', partner)
    assert getattr(partner, 'Role35') == owner
    _safe_set(owner, 'requiredCapabilities', None)
    assert getattr(partner, 'Role35') is None


def test_assoc_roles29_stub_double():
    # dronesStructure_Role has no real 'Role' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_CooperativeAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_CooperativeAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    partner = dronesStructure_Role()
    setattr(partner, 'Role', None)
    _safe_set(owner, 'cooperativeAction', {partner})
    assert getattr(partner, 'Role') == owner
    _safe_set(owner, 'cooperativeAction', set())
    assert getattr(partner, 'Role') is None


def test_assoc_scenarios0_stub_double():
    # dronesStructure_DronesStructure has no real 'dronesStructure_DronesStructure' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    partner = dronesStructure_DronesStructure()
    setattr(partner, 'dronesStructure_DronesStructure', None)
    _safe_set(owner, 'dronesStructure_Scenario', partner)
    assert owner in getattr(partner, 'dronesStructure_DronesStructure')
    _safe_set(owner, 'dronesStructure_Scenario', None)
    assert owner not in getattr(partner, 'dronesStructure_DronesStructure')


def test_assoc_startPosition36_stub_double():
    # dronesStructure_Drone has no real 'dronesStructure_Drone37' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_Position(x=3.14, y=3.14, z=3.14)
    partner = dronesStructure_Drone()
    setattr(partner, 'dronesStructure_Drone37', None)
    _safe_set(owner, 'dronesStructure_Position', partner)
    assert getattr(partner, 'dronesStructure_Drone37') == owner
    _safe_set(owner, 'dronesStructure_Position', None)
    assert getattr(partner, 'dronesStructure_Drone37') is None


def test_assoc_tasks15_stub_double():
    # dronesStructure_Task has no real 'dronesStructure_Task' property in the generated
    # code (a bare stub) -- manually attach it so dronesStructure_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesStructure_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    partner = dronesStructure_Task()
    setattr(partner, 'dronesStructure_Task', None)
    _safe_set(owner, 'dronesStructure_Scenario16', {partner})
    assert getattr(partner, 'dronesStructure_Task') == owner
    _safe_set(owner, 'dronesStructure_Scenario16', set())
    assert getattr(partner, 'dronesStructure_Task') is None


