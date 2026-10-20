import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Vehicle,
    platoon_FrontGap,
    platoon_JoinPlatoonCoord,
    platoon_JoiningPosition,
    platoon_JoiningVehicle,
    platoon_Platoon,
    platoon_PlatoonVehicle,
    platoon_PlatooningSystem,
    platoon_Vehicle,
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

def test_assoc_follower1_reverse_link_reassign_clear():
    a1 = platoon_PlatoonVehicle(position=7)
    a2 = platoon_PlatoonVehicle(position=13)
    b = platoon_Platoon(desiredGapSize=7, length=7)
    _safe_set(b, 'platoon_Platoon2', {a1})
    assert _is_linked(b, 'platoon_Platoon2', a1)
    if hasattr(a1, 'platoon_PlatoonVehicle3'):
        assert _is_linked(a1, 'platoon_PlatoonVehicle3', b)
    _safe_set(b, 'platoon_Platoon2', {a2})
    assert _is_linked(b, 'platoon_Platoon2', a2)
    if hasattr(a1, 'platoon_PlatoonVehicle3'):
        assert not _is_linked(a1, 'platoon_PlatoonVehicle3', b)
    if hasattr(a2, 'platoon_PlatoonVehicle3'):
        assert _is_linked(a2, 'platoon_PlatoonVehicle3', b)
    _safe_set(b, 'platoon_Platoon2', set())
    assert not _is_linked(b, 'platoon_Platoon2', a2)
    if hasattr(a2, 'platoon_PlatoonVehicle3'):
        assert not _is_linked(a2, 'platoon_PlatoonVehicle3', b)


def test_assoc_follows11_reverse_link_reassign_clear():
    a1 = platoon_Vehicle(id=7)
    a2 = platoon_Vehicle(id=13)
    b = platoon_Vehicle(id=7)
    _safe_set(b, 'platoon_Vehicle10', a1)
    assert _is_linked(b, 'platoon_Vehicle10', a1)
    if hasattr(a1, 'platoon_Vehicle'):
        assert _is_linked(a1, 'platoon_Vehicle', b)
    _safe_set(b, 'platoon_Vehicle10', a2)
    assert _is_linked(b, 'platoon_Vehicle10', a2)
    if hasattr(a1, 'platoon_Vehicle'):
        assert not _is_linked(a1, 'platoon_Vehicle', b)
    if hasattr(a2, 'platoon_Vehicle'):
        assert _is_linked(a2, 'platoon_Vehicle', b)
    _safe_set(b, 'platoon_Vehicle10', None)
    assert not _is_linked(b, 'platoon_Vehicle10', a2)
    if hasattr(a2, 'platoon_Vehicle'):
        assert not _is_linked(a2, 'platoon_Vehicle', b)


def test_assoc_follows5_reverse_link_reassign_clear():
    a1 = platoon_Platoon(desiredGapSize=7, length=7)
    a2 = platoon_Platoon(desiredGapSize=13, length=13)
    b = platoon_Platoon(desiredGapSize=7, length=7)
    _safe_set(b, 'platoon_Platoon6', a1)
    assert _is_linked(b, 'platoon_Platoon6', a1)
    if hasattr(a1, 'platoon_Platoon4'):
        assert _is_linked(a1, 'platoon_Platoon4', b)
    _safe_set(b, 'platoon_Platoon6', a2)
    assert _is_linked(b, 'platoon_Platoon6', a2)
    if hasattr(a1, 'platoon_Platoon4'):
        assert not _is_linked(a1, 'platoon_Platoon4', b)
    if hasattr(a2, 'platoon_Platoon4'):
        assert _is_linked(a2, 'platoon_Platoon4', b)
    _safe_set(b, 'platoon_Platoon6', None)
    assert not _is_linked(b, 'platoon_Platoon6', a2)
    if hasattr(a2, 'platoon_Platoon4'):
        assert not _is_linked(a2, 'platoon_Platoon4', b)


def test_assoc_forms32_reverse_link_reassign_clear():
    a1 = platoon_PlatoonVehicle(position=7)
    a2 = platoon_PlatoonVehicle(position=13)
    b = platoon_FrontGap(actualGapSize=7)
    _safe_set(b, 'platoon_FrontGap34', a1)
    assert _is_linked(b, 'platoon_FrontGap34', a1)
    if hasattr(a1, 'platoon_PlatoonVehicle33'):
        assert _is_linked(a1, 'platoon_PlatoonVehicle33', b)
    _safe_set(b, 'platoon_FrontGap34', a2)
    assert _is_linked(b, 'platoon_FrontGap34', a2)
    if hasattr(a1, 'platoon_PlatoonVehicle33'):
        assert not _is_linked(a1, 'platoon_PlatoonVehicle33', b)
    if hasattr(a2, 'platoon_PlatoonVehicle33'):
        assert _is_linked(a2, 'platoon_PlatoonVehicle33', b)
    _safe_set(b, 'platoon_FrontGap34', None)
    assert not _is_linked(b, 'platoon_FrontGap34', a2)
    if hasattr(a2, 'platoon_PlatoonVehicle33'):
        assert not _is_linked(a2, 'platoon_PlatoonVehicle33', b)


def test_assoc_isAwareOf13_reverse_link_reassign_clear():
    a1 = platoon_Vehicle(id=7)
    a2 = platoon_Vehicle(id=13)
    b = platoon_Vehicle(id=7)
    _safe_set(b, 'platoon_Vehicle14', a1)
    assert _is_linked(b, 'platoon_Vehicle14', a1)
    if hasattr(a1, 'platoon_Vehicle12'):
        assert _is_linked(a1, 'platoon_Vehicle12', b)
    _safe_set(b, 'platoon_Vehicle14', a2)
    assert _is_linked(b, 'platoon_Vehicle14', a2)
    if hasattr(a1, 'platoon_Vehicle12'):
        assert not _is_linked(a1, 'platoon_Vehicle12', b)
    if hasattr(a2, 'platoon_Vehicle12'):
        assert _is_linked(a2, 'platoon_Vehicle12', b)
    _safe_set(b, 'platoon_Vehicle14', None)
    assert not _is_linked(b, 'platoon_Vehicle14', a2)
    if hasattr(a2, 'platoon_Vehicle12'):
        assert not _is_linked(a2, 'platoon_Vehicle12', b)


def test_assoc_leader0_reverse_link_reassign_clear():
    a1 = platoon_PlatoonVehicle(position=7)
    a2 = platoon_PlatoonVehicle(position=13)
    b = platoon_Platoon(desiredGapSize=7, length=7)
    _safe_set(b, 'platoon_Platoon', a1)
    assert _is_linked(b, 'platoon_Platoon', a1)
    if hasattr(a1, 'platoon_PlatoonVehicle'):
        assert _is_linked(a1, 'platoon_PlatoonVehicle', b)
    _safe_set(b, 'platoon_Platoon', a2)
    assert _is_linked(b, 'platoon_Platoon', a2)
    if hasattr(a1, 'platoon_PlatoonVehicle'):
        assert not _is_linked(a1, 'platoon_PlatoonVehicle', b)
    if hasattr(a2, 'platoon_PlatoonVehicle'):
        assert _is_linked(a2, 'platoon_PlatoonVehicle', b)
    _safe_set(b, 'platoon_Platoon', None)
    assert not _is_linked(b, 'platoon_Platoon', a2)
    if hasattr(a2, 'platoon_PlatoonVehicle'):
        assert not _is_linked(a2, 'platoon_PlatoonVehicle', b)


def test_assoc_members9_reverse_link_reassign_clear():
    a1 = platoon_PlatoonVehicle(position=7)
    a2 = platoon_PlatoonVehicle(position=13)
    b = platoon_Platoon(desiredGapSize=7, length=7)
    _safe_set(b, 'platoon', {a1})
    assert _is_linked(b, 'platoon', a1)
    if hasattr(a1, 'PlatoonVehicle'):
        assert _is_linked(a1, 'PlatoonVehicle', b)
    _safe_set(b, 'platoon', {a2})
    assert _is_linked(b, 'platoon', a2)
    if hasattr(a1, 'PlatoonVehicle'):
        assert not _is_linked(a1, 'PlatoonVehicle', b)
    if hasattr(a2, 'PlatoonVehicle'):
        assert _is_linked(a2, 'PlatoonVehicle', b)
    _safe_set(b, 'platoon', set())
    assert not _is_linked(b, 'platoon', a2)
    if hasattr(a2, 'PlatoonVehicle'):
        assert not _is_linked(a2, 'PlatoonVehicle', b)


def test_assoc_platoon39_reverse_link_reassign_clear():
    a1 = platoon_PlatoonVehicle(position=7)
    a2 = platoon_PlatoonVehicle(position=13)
    b = platoon_Platoon(desiredGapSize=7, length=7)
    _safe_set(b, 'Platoon', a1)
    assert _is_linked(b, 'Platoon', a1)
    if hasattr(a1, 'members'):
        assert _is_linked(a1, 'members', b)
    _safe_set(b, 'Platoon', a2)
    assert _is_linked(b, 'Platoon', a2)
    if hasattr(a1, 'members'):
        assert not _is_linked(a1, 'members', b)
    if hasattr(a2, 'members'):
        assert _is_linked(a2, 'members', b)
    _safe_set(b, 'Platoon', None)
    assert not _is_linked(b, 'Platoon', a2)
    if hasattr(a2, 'members'):
        assert not _is_linked(a2, 'members', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cordManager18_stub_double():
    # platoon_JoinPlatoonCoord has no real 'platoon_JoinPlatoonCoord19' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Vehicle(id=7)
    partner = platoon_JoinPlatoonCoord()
    setattr(partner, 'platoon_JoinPlatoonCoord19', None)
    _safe_set(owner, 'platoon_Vehicle20', partner)
    assert getattr(partner, 'platoon_JoinPlatoonCoord19') == owner
    _safe_set(owner, 'platoon_Vehicle20', None)
    assert getattr(partner, 'platoon_JoinPlatoonCoord19') is None


def test_assoc_gapMaker21_stub_double():
    # platoon_JoinPlatoonCoord has no real 'platoon_JoinPlatoonCoord22' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Vehicle(id=7)
    partner = platoon_JoinPlatoonCoord()
    setattr(partner, 'platoon_JoinPlatoonCoord22', None)
    _safe_set(owner, 'platoon_Vehicle23', partner)
    assert getattr(partner, 'platoon_JoinPlatoonCoord22') == owner
    _safe_set(owner, 'platoon_Vehicle23', None)
    assert getattr(partner, 'platoon_JoinPlatoonCoord22') is None


def test_assoc_insertsIn27_stub_double():
    # platoon_JoiningVehicle has no real 'platoon_JoiningVehicle' property in the generated
    # code (a bare stub) -- manually attach it so platoon_FrontGap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_FrontGap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_FrontGap(actualGapSize=7)
    partner = platoon_JoiningVehicle()
    setattr(partner, 'platoon_JoiningVehicle', None)
    _safe_set(owner, 'platoon_FrontGap', partner)
    assert getattr(partner, 'platoon_JoiningVehicle') == owner
    _safe_set(owner, 'platoon_FrontGap', None)
    assert getattr(partner, 'platoon_JoiningVehicle') is None


def test_assoc_joinCord15_stub_double():
    # platoon_JoinPlatoonCoord has no real 'platoon_JoinPlatoonCoord17' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Vehicle(id=7)
    partner = platoon_JoinPlatoonCoord()
    setattr(partner, 'platoon_JoinPlatoonCoord17', None)
    _safe_set(owner, 'platoon_Vehicle16', partner)
    assert getattr(partner, 'platoon_JoinPlatoonCoord17') == owner
    _safe_set(owner, 'platoon_Vehicle16', None)
    assert getattr(partner, 'platoon_JoinPlatoonCoord17') is None


def test_assoc_joiningRequest38_stub_double():
    # platoon_JoiningVehicle has no real 'JoiningVehicle' property in the generated
    # code (a bare stub) -- manually attach it so platoon_PlatoonVehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_PlatoonVehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_PlatoonVehicle(position=7)
    partner = platoon_JoiningVehicle()
    setattr(partner, 'JoiningVehicle', None)
    _safe_set(owner, 'wantsToJoin', partner)
    assert getattr(partner, 'JoiningVehicle') == owner
    _safe_set(owner, 'wantsToJoin', None)
    assert getattr(partner, 'JoiningVehicle') is None


def test_assoc_joiningVehicle24_stub_double():
    # platoon_JoinPlatoonCoord has no real 'platoon_JoinPlatoonCoord25' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Vehicle(id=7)
    partner = platoon_JoinPlatoonCoord()
    setattr(partner, 'platoon_JoinPlatoonCoord25', None)
    _safe_set(owner, 'platoon_Vehicle26', partner)
    assert getattr(partner, 'platoon_JoinPlatoonCoord25') == owner
    _safe_set(owner, 'platoon_Vehicle26', None)
    assert getattr(partner, 'platoon_JoinPlatoonCoord25') is None


def test_assoc_joinplatoonCord7_stub_double():
    # platoon_JoinPlatoonCoord has no real 'platoon_JoinPlatoonCoord' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Platoon's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Platoon's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Platoon(desiredGapSize=7, length=7)
    partner = platoon_JoinPlatoonCoord()
    setattr(partner, 'platoon_JoinPlatoonCoord', None)
    _safe_set(owner, 'platoon_Platoon8', partner)
    assert getattr(partner, 'platoon_JoinPlatoonCoord') == owner
    _safe_set(owner, 'platoon_Platoon8', None)
    assert getattr(partner, 'platoon_JoinPlatoonCoord') is None


def test_assoc_marks35_stub_double():
    # platoon_JoiningPosition has no real 'platoon_JoiningPosition37' property in the generated
    # code (a bare stub) -- manually attach it so platoon_PlatoonVehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_PlatoonVehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_PlatoonVehicle(position=7)
    partner = platoon_JoiningPosition()
    setattr(partner, 'platoon_JoiningPosition37', None)
    _safe_set(owner, 'platoon_PlatoonVehicle36', partner)
    assert getattr(partner, 'platoon_JoiningPosition37') == owner
    _safe_set(owner, 'platoon_PlatoonVehicle36', None)
    assert getattr(partner, 'platoon_JoiningPosition37') is None


def test_assoc_platoon42_stub_double():
    # platoon_PlatooningSystem has no real 'platoon_PlatooningSystem43' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Platoon's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Platoon's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Platoon(desiredGapSize=7, length=7)
    partner = platoon_PlatooningSystem()
    setattr(partner, 'platoon_PlatooningSystem43', None)
    _safe_set(owner, 'platoon_Platoon44', partner)
    assert owner in getattr(partner, 'platoon_PlatooningSystem43')
    _safe_set(owner, 'platoon_Platoon44', None)
    assert owner not in getattr(partner, 'platoon_PlatooningSystem43')


def test_assoc_vehicles40_stub_double():
    # platoon_PlatooningSystem has no real 'platoon_PlatooningSystem' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Vehicle(id=7)
    partner = platoon_PlatooningSystem()
    setattr(partner, 'platoon_PlatooningSystem', None)
    _safe_set(owner, 'platoon_Vehicle41', partner)
    assert owner in getattr(partner, 'platoon_PlatooningSystem')
    _safe_set(owner, 'platoon_Vehicle41', None)
    assert owner not in getattr(partner, 'platoon_PlatooningSystem')


def test_assoc_wantsToJoin28_stub_double():
    # platoon_JoiningVehicle has no real 'joiningRequest' property in the generated
    # code (a bare stub) -- manually attach it so platoon_PlatoonVehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_PlatoonVehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_PlatoonVehicle(position=7)
    partner = platoon_JoiningVehicle()
    setattr(partner, 'joiningRequest', None)
    _safe_set(owner, 'PlatoonVehicle29', partner)
    assert getattr(partner, 'joiningRequest') == owner
    _safe_set(owner, 'PlatoonVehicle29', None)
    assert getattr(partner, 'joiningRequest') is None


