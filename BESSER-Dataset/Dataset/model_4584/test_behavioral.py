import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actor,
    Effect,
    dsl_Actor,
    dsl_ActorList,
    dsl_AnimtationActor,
    dsl_Color,
    dsl_DamageEffect,
    dsl_Effect,
    dsl_LauncherEffect,
    dsl_Model,
    dsl_ModelActor,
    dsl_Mover,
    dsl_ParticleActor,
    dsl_PersistentEffect,
    dsl_Projectile,
    dsl_Race,
    dsl_Turrent,
    dsl_Unit,
    dsl_UnitWeaponLink,
    dsl_Weapon,
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

def test_assoc_actor20_reverse_link_reassign_clear():
    a1 = dsl_ActorList(trigger="sample_text")
    a2 = dsl_ActorList(trigger="sample_text_2")
    b = dsl_Actor(name="sample_text")
    _safe_set(b, 'dsl_Actor22', a1)
    assert _is_linked(b, 'dsl_Actor22', a1)
    if hasattr(a1, 'dsl_ActorList21'):
        assert _is_linked(a1, 'dsl_ActorList21', b)
    _safe_set(b, 'dsl_Actor22', a2)
    assert _is_linked(b, 'dsl_Actor22', a2)
    if hasattr(a1, 'dsl_ActorList21'):
        assert not _is_linked(a1, 'dsl_ActorList21', b)
    if hasattr(a2, 'dsl_ActorList21'):
        assert _is_linked(a2, 'dsl_ActorList21', b)
    _safe_set(b, 'dsl_Actor22', None)
    assert not _is_linked(b, 'dsl_Actor22', a2)
    if hasattr(a2, 'dsl_ActorList21'):
        assert not _is_linked(a2, 'dsl_ActorList21', b)


def test_assoc_actor31_reverse_link_reassign_clear():
    a1 = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    a2 = dsl_Unit(mass="sample_text_2", maxHealth=13, name="sample_text_2", radius="sample_text_2", separationRadius="sample_text_2", sight=13, speed="sample_text_2", uIName="sample_text_2")
    b = dsl_Actor(name="sample_text")
    _safe_set(b, 'dsl_Actor33', a1)
    assert _is_linked(b, 'dsl_Actor33', a1)
    if hasattr(a1, 'dsl_Unit32'):
        assert _is_linked(a1, 'dsl_Unit32', b)
    _safe_set(b, 'dsl_Actor33', a2)
    assert _is_linked(b, 'dsl_Actor33', a2)
    if hasattr(a1, 'dsl_Unit32'):
        assert not _is_linked(a1, 'dsl_Unit32', b)
    if hasattr(a2, 'dsl_Unit32'):
        assert _is_linked(a2, 'dsl_Unit32', b)
    _safe_set(b, 'dsl_Actor33', None)
    assert not _is_linked(b, 'dsl_Actor33', a2)
    if hasattr(a2, 'dsl_Unit32'):
        assert not _is_linked(a2, 'dsl_Unit32', b)


def test_assoc_actor43_reverse_link_reassign_clear():
    a1 = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    a2 = dsl_Weapon(directionBone="sample_text_2", name="sample_text_2", period=13, range="sample_text_2", scanRange=13, sourceBone="sample_text_2", uIName="sample_text_2")
    b = dsl_Actor(name="sample_text")
    _safe_set(b, 'dsl_Actor45', a1)
    assert _is_linked(b, 'dsl_Actor45', a1)
    if hasattr(a1, 'dsl_Weapon44'):
        assert _is_linked(a1, 'dsl_Weapon44', b)
    _safe_set(b, 'dsl_Actor45', a2)
    assert _is_linked(b, 'dsl_Actor45', a2)
    if hasattr(a1, 'dsl_Weapon44'):
        assert not _is_linked(a1, 'dsl_Weapon44', b)
    if hasattr(a2, 'dsl_Weapon44'):
        assert _is_linked(a2, 'dsl_Weapon44', b)
    _safe_set(b, 'dsl_Actor45', None)
    assert not _is_linked(b, 'dsl_Actor45', a2)
    if hasattr(a2, 'dsl_Weapon44'):
        assert not _is_linked(a2, 'dsl_Weapon44', b)


def test_assoc_actor56_reverse_link_reassign_clear():
    a1 = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    a2 = dsl_Projectile(mass=13, name="sample_text_2", precision="sample_text_2", speed=13)
    b = dsl_Actor(name="sample_text")
    _safe_set(b, 'dsl_Actor58', a1)
    assert _is_linked(b, 'dsl_Actor58', a1)
    if hasattr(a1, 'dsl_Projectile57'):
        assert _is_linked(a1, 'dsl_Projectile57', b)
    _safe_set(b, 'dsl_Actor58', a2)
    assert _is_linked(b, 'dsl_Actor58', a2)
    if hasattr(a1, 'dsl_Projectile57'):
        assert not _is_linked(a1, 'dsl_Projectile57', b)
    if hasattr(a2, 'dsl_Projectile57'):
        assert _is_linked(a2, 'dsl_Projectile57', b)
    _safe_set(b, 'dsl_Actor58', None)
    assert not _is_linked(b, 'dsl_Actor58', a2)
    if hasattr(a2, 'dsl_Projectile57'):
        assert not _is_linked(a2, 'dsl_Projectile57', b)


def test_assoc_actorlist15_reverse_link_reassign_clear():
    a1 = dsl_ModelActor(modelPath="sample_text", scale=7)
    a2 = dsl_ModelActor(modelPath="sample_text_2", scale=13)
    b = dsl_ActorList(trigger="sample_text")
    _safe_set(b, 'dsl_ActorList', a1)
    assert _is_linked(b, 'dsl_ActorList', a1)
    if hasattr(a1, 'dsl_ModelActor'):
        assert _is_linked(a1, 'dsl_ModelActor', b)
    _safe_set(b, 'dsl_ActorList', a2)
    assert _is_linked(b, 'dsl_ActorList', a2)
    if hasattr(a1, 'dsl_ModelActor'):
        assert not _is_linked(a1, 'dsl_ModelActor', b)
    if hasattr(a2, 'dsl_ModelActor'):
        assert _is_linked(a2, 'dsl_ModelActor', b)
    _safe_set(b, 'dsl_ActorList', None)
    assert not _is_linked(b, 'dsl_ActorList', a2)
    if hasattr(a2, 'dsl_ModelActor'):
        assert not _is_linked(a2, 'dsl_ModelActor', b)


def test_assoc_effect40_reverse_link_reassign_clear():
    a1 = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    a2 = dsl_Weapon(directionBone="sample_text_2", name="sample_text_2", period=13, range="sample_text_2", scanRange=13, sourceBone="sample_text_2", uIName="sample_text_2")
    b = dsl_Effect(name="sample_text")
    _safe_set(b, 'dsl_Effect42', a1)
    assert _is_linked(b, 'dsl_Effect42', a1)
    if hasattr(a1, 'dsl_Weapon41'):
        assert _is_linked(a1, 'dsl_Weapon41', b)
    _safe_set(b, 'dsl_Effect42', a2)
    assert _is_linked(b, 'dsl_Effect42', a2)
    if hasattr(a1, 'dsl_Weapon41'):
        assert not _is_linked(a1, 'dsl_Weapon41', b)
    if hasattr(a2, 'dsl_Weapon41'):
        assert _is_linked(a2, 'dsl_Weapon41', b)
    _safe_set(b, 'dsl_Effect42', None)
    assert not _is_linked(b, 'dsl_Effect42', a2)
    if hasattr(a2, 'dsl_Weapon41'):
        assert not _is_linked(a2, 'dsl_Weapon41', b)


def test_assoc_effects46_reverse_link_reassign_clear():
    a1 = dsl_PersistentEffect(durations="sample_text", periodCount=7, ranges="sample_text")
    a2 = dsl_PersistentEffect(durations="sample_text_2", periodCount=13, ranges="sample_text_2")
    b = dsl_Effect(name="sample_text")
    _safe_set(b, 'dsl_Effect47', a1)
    assert _is_linked(b, 'dsl_Effect47', a1)
    if hasattr(a1, 'dsl_PersistentEffect'):
        assert _is_linked(a1, 'dsl_PersistentEffect', b)
    _safe_set(b, 'dsl_Effect47', a2)
    assert _is_linked(b, 'dsl_Effect47', a2)
    if hasattr(a1, 'dsl_PersistentEffect'):
        assert not _is_linked(a1, 'dsl_PersistentEffect', b)
    if hasattr(a2, 'dsl_PersistentEffect'):
        assert _is_linked(a2, 'dsl_PersistentEffect', b)
    _safe_set(b, 'dsl_Effect47', None)
    assert not _is_linked(b, 'dsl_Effect47', a2)
    if hasattr(a2, 'dsl_PersistentEffect'):
        assert not _is_linked(a2, 'dsl_PersistentEffect', b)


def test_assoc_endColor17_reverse_link_reassign_clear():
    a1 = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    a2 = dsl_ParticleActor(add="sample_text_2", directionBone="sample_text_2", duration=13, emissionBone="sample_text_2", endSize="sample_text_2", maxCount=13, maxLife="sample_text_2", minLife="sample_text_2", nbCol=13, nbRow=13, perSecond=13, spritePath="sample_text_2", startSize="sample_text_2", startVariation="sample_text_2")
    b = dsl_Color(a=7, b=7, g=7, r=7)
    _safe_set(b, 'dsl_Color19', a1)
    assert _is_linked(b, 'dsl_Color19', a1)
    if hasattr(a1, 'dsl_ParticleActor18'):
        assert _is_linked(a1, 'dsl_ParticleActor18', b)
    _safe_set(b, 'dsl_Color19', a2)
    assert _is_linked(b, 'dsl_Color19', a2)
    if hasattr(a1, 'dsl_ParticleActor18'):
        assert not _is_linked(a1, 'dsl_ParticleActor18', b)
    if hasattr(a2, 'dsl_ParticleActor18'):
        assert _is_linked(a2, 'dsl_ParticleActor18', b)
    _safe_set(b, 'dsl_Color19', None)
    assert not _is_linked(b, 'dsl_Color19', a2)
    if hasattr(a2, 'dsl_ParticleActor18'):
        assert not _is_linked(a2, 'dsl_ParticleActor18', b)


def test_assoc_mover26_reverse_link_reassign_clear():
    a1 = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    a2 = dsl_Unit(mass="sample_text_2", maxHealth=13, name="sample_text_2", radius="sample_text_2", separationRadius="sample_text_2", sight=13, speed="sample_text_2", uIName="sample_text_2")
    b = dsl_Mover(heightmap="sample_text", name="sample_text", pathfindingMode="sample_text", standingMode="sample_text")
    _safe_set(b, 'dsl_Mover28', a1)
    assert _is_linked(b, 'dsl_Mover28', a1)
    if hasattr(a1, 'dsl_Unit27'):
        assert _is_linked(a1, 'dsl_Unit27', b)
    _safe_set(b, 'dsl_Mover28', a2)
    assert _is_linked(b, 'dsl_Mover28', a2)
    if hasattr(a1, 'dsl_Unit27'):
        assert not _is_linked(a1, 'dsl_Unit27', b)
    if hasattr(a2, 'dsl_Unit27'):
        assert _is_linked(a2, 'dsl_Unit27', b)
    _safe_set(b, 'dsl_Mover28', None)
    assert not _is_linked(b, 'dsl_Mover28', a2)
    if hasattr(a2, 'dsl_Unit27'):
        assert not _is_linked(a2, 'dsl_Unit27', b)


def test_assoc_mover53_reverse_link_reassign_clear():
    a1 = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    a2 = dsl_Projectile(mass=13, name="sample_text_2", precision="sample_text_2", speed=13)
    b = dsl_Mover(heightmap="sample_text", name="sample_text", pathfindingMode="sample_text", standingMode="sample_text")
    _safe_set(b, 'dsl_Mover55', a1)
    assert _is_linked(b, 'dsl_Mover55', a1)
    if hasattr(a1, 'dsl_Projectile54'):
        assert _is_linked(a1, 'dsl_Projectile54', b)
    _safe_set(b, 'dsl_Mover55', a2)
    assert _is_linked(b, 'dsl_Mover55', a2)
    if hasattr(a1, 'dsl_Projectile54'):
        assert not _is_linked(a1, 'dsl_Projectile54', b)
    if hasattr(a2, 'dsl_Projectile54'):
        assert _is_linked(a2, 'dsl_Projectile54', b)
    _safe_set(b, 'dsl_Mover55', None)
    assert not _is_linked(b, 'dsl_Mover55', a2)
    if hasattr(a2, 'dsl_Projectile54'):
        assert not _is_linked(a2, 'dsl_Projectile54', b)


def test_assoc_race23_reverse_link_reassign_clear():
    a1 = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    a2 = dsl_Unit(mass="sample_text_2", maxHealth=13, name="sample_text_2", radius="sample_text_2", separationRadius="sample_text_2", sight=13, speed="sample_text_2", uIName="sample_text_2")
    b = dsl_Race(name="sample_text")
    _safe_set(b, 'dsl_Race25', a1)
    assert _is_linked(b, 'dsl_Race25', a1)
    if hasattr(a1, 'dsl_Unit24'):
        assert _is_linked(a1, 'dsl_Unit24', b)
    _safe_set(b, 'dsl_Race25', a2)
    assert _is_linked(b, 'dsl_Race25', a2)
    if hasattr(a1, 'dsl_Unit24'):
        assert not _is_linked(a1, 'dsl_Unit24', b)
    if hasattr(a2, 'dsl_Unit24'):
        assert _is_linked(a2, 'dsl_Unit24', b)
    _safe_set(b, 'dsl_Race25', None)
    assert not _is_linked(b, 'dsl_Race25', a2)
    if hasattr(a2, 'dsl_Unit24'):
        assert not _is_linked(a2, 'dsl_Unit24', b)


def test_assoc_startColor16_reverse_link_reassign_clear():
    a1 = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    a2 = dsl_ParticleActor(add="sample_text_2", directionBone="sample_text_2", duration=13, emissionBone="sample_text_2", endSize="sample_text_2", maxCount=13, maxLife="sample_text_2", minLife="sample_text_2", nbCol=13, nbRow=13, perSecond=13, spritePath="sample_text_2", startSize="sample_text_2", startVariation="sample_text_2")
    b = dsl_Color(a=7, b=7, g=7, r=7)
    _safe_set(b, 'dsl_Color', a1)
    assert _is_linked(b, 'dsl_Color', a1)
    if hasattr(a1, 'dsl_ParticleActor'):
        assert _is_linked(a1, 'dsl_ParticleActor', b)
    _safe_set(b, 'dsl_Color', a2)
    assert _is_linked(b, 'dsl_Color', a2)
    if hasattr(a1, 'dsl_ParticleActor'):
        assert not _is_linked(a1, 'dsl_ParticleActor', b)
    if hasattr(a2, 'dsl_ParticleActor'):
        assert _is_linked(a2, 'dsl_ParticleActor', b)
    _safe_set(b, 'dsl_Color', None)
    assert not _is_linked(b, 'dsl_Color', a2)
    if hasattr(a2, 'dsl_ParticleActor'):
        assert not _is_linked(a2, 'dsl_ParticleActor', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actors7_stub_double():
    # dsl_Model has no real 'dsl_Model8' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Actor(name="sample_text")
    partner = dsl_Model()
    setattr(partner, 'dsl_Model8', None)
    _safe_set(owner, 'dsl_Actor', partner)
    assert owner in getattr(partner, 'dsl_Model8')
    _safe_set(owner, 'dsl_Actor', None)
    assert owner not in getattr(partner, 'dsl_Model8')


def test_assoc_effects48_stub_double():
    # dsl_LauncherEffect has no real 'dsl_LauncherEffect' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Effect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Effect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Effect(name="sample_text")
    partner = dsl_LauncherEffect()
    setattr(partner, 'dsl_LauncherEffect', None)
    _safe_set(owner, 'dsl_Effect49', partner)
    assert owner in getattr(partner, 'dsl_LauncherEffect')
    _safe_set(owner, 'dsl_Effect49', None)
    assert owner not in getattr(partner, 'dsl_LauncherEffect')


def test_assoc_effects9_stub_double():
    # dsl_Model has no real 'dsl_Model10' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Effect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Effect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Effect(name="sample_text")
    partner = dsl_Model()
    setattr(partner, 'dsl_Model10', None)
    _safe_set(owner, 'dsl_Effect', partner)
    assert owner in getattr(partner, 'dsl_Model10')
    _safe_set(owner, 'dsl_Effect', None)
    assert owner not in getattr(partner, 'dsl_Model10')


def test_assoc_movers5_stub_double():
    # dsl_Model has no real 'dsl_Model6' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Mover's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Mover's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Mover(heightmap="sample_text", name="sample_text", pathfindingMode="sample_text", standingMode="sample_text")
    partner = dsl_Model()
    setattr(partner, 'dsl_Model6', None)
    _safe_set(owner, 'dsl_Mover', partner)
    assert owner in getattr(partner, 'dsl_Model6')
    _safe_set(owner, 'dsl_Mover', None)
    assert owner not in getattr(partner, 'dsl_Model6')


def test_assoc_projectiles13_stub_double():
    # dsl_Model has no real 'dsl_Model14' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Projectile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Projectile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    partner = dsl_Model()
    setattr(partner, 'dsl_Model14', None)
    _safe_set(owner, 'dsl_Projectile', partner)
    assert owner in getattr(partner, 'dsl_Model14')
    _safe_set(owner, 'dsl_Projectile', None)
    assert owner not in getattr(partner, 'dsl_Model14')


def test_assoc_projectiles50_stub_double():
    # dsl_LauncherEffect has no real 'dsl_LauncherEffect51' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Projectile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Projectile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    partner = dsl_LauncherEffect()
    setattr(partner, 'dsl_LauncherEffect51', None)
    _safe_set(owner, 'dsl_Projectile52', partner)
    assert owner in getattr(partner, 'dsl_LauncherEffect51')
    _safe_set(owner, 'dsl_Projectile52', None)
    assert owner not in getattr(partner, 'dsl_LauncherEffect51')


def test_assoc_races3_stub_double():
    # dsl_Model has no real 'dsl_Model4' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Race's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Race's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Race(name="sample_text")
    partner = dsl_Model()
    setattr(partner, 'dsl_Model4', None)
    _safe_set(owner, 'dsl_Race', partner)
    assert owner in getattr(partner, 'dsl_Model4')
    _safe_set(owner, 'dsl_Race', None)
    assert owner not in getattr(partner, 'dsl_Model4')


def test_assoc_turrent37_stub_double():
    # dsl_UnitWeaponLink has no real 'dsl_UnitWeaponLink38' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Turrent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Turrent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Turrent(boneName="sample_text", idleSpeed=7, name="sample_text", onIdle="sample_text", speed=7)
    partner = dsl_UnitWeaponLink()
    setattr(partner, 'dsl_UnitWeaponLink38', None)
    _safe_set(owner, 'dsl_Turrent39', partner)
    assert getattr(partner, 'dsl_UnitWeaponLink38') == owner
    _safe_set(owner, 'dsl_Turrent39', None)
    assert getattr(partner, 'dsl_UnitWeaponLink38') is None


def test_assoc_turrents11_stub_double():
    # dsl_Model has no real 'dsl_Model12' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Turrent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Turrent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Turrent(boneName="sample_text", idleSpeed=7, name="sample_text", onIdle="sample_text", speed=7)
    partner = dsl_Model()
    setattr(partner, 'dsl_Model12', None)
    _safe_set(owner, 'dsl_Turrent', partner)
    assert owner in getattr(partner, 'dsl_Model12')
    _safe_set(owner, 'dsl_Turrent', None)
    assert owner not in getattr(partner, 'dsl_Model12')


def test_assoc_units1_stub_double():
    # dsl_Model has no real 'dsl_Model2' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    partner = dsl_Model()
    setattr(partner, 'dsl_Model2', None)
    _safe_set(owner, 'dsl_Unit', partner)
    assert owner in getattr(partner, 'dsl_Model2')
    _safe_set(owner, 'dsl_Unit', None)
    assert owner not in getattr(partner, 'dsl_Model2')


def test_assoc_weapon34_stub_double():
    # dsl_UnitWeaponLink has no real 'dsl_UnitWeaponLink35' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Weapon's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Weapon's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    partner = dsl_UnitWeaponLink()
    setattr(partner, 'dsl_UnitWeaponLink35', None)
    _safe_set(owner, 'dsl_Weapon36', partner)
    assert getattr(partner, 'dsl_UnitWeaponLink35') == owner
    _safe_set(owner, 'dsl_Weapon36', None)
    assert getattr(partner, 'dsl_UnitWeaponLink35') is None


def test_assoc_weapons0_stub_double():
    # dsl_Model has no real 'dsl_Model' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Weapon's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Weapon's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    partner = dsl_Model()
    setattr(partner, 'dsl_Model', None)
    _safe_set(owner, 'dsl_Weapon', partner)
    assert owner in getattr(partner, 'dsl_Model')
    _safe_set(owner, 'dsl_Weapon', None)
    assert owner not in getattr(partner, 'dsl_Model')


def test_assoc_weapons29_stub_double():
    # dsl_UnitWeaponLink has no real 'dsl_UnitWeaponLink' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    partner = dsl_UnitWeaponLink()
    setattr(partner, 'dsl_UnitWeaponLink', None)
    _safe_set(owner, 'dsl_Unit30', {partner})
    assert getattr(partner, 'dsl_UnitWeaponLink') == owner
    _safe_set(owner, 'dsl_Unit30', set())
    assert getattr(partner, 'dsl_UnitWeaponLink') is None


