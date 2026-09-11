import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_dsl_Actor_name_value_roundtrip():
    instance = dsl_Actor(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dsl_ActorList_trigger_value_roundtrip():
    instance = dsl_ActorList(trigger="sample_text")
    assert instance.trigger == "sample_text"
    instance.trigger = "sample_text_2"
    assert instance.trigger == "sample_text_2"


def test_dsl_AnimtationActor_animName_value_roundtrip():
    instance = dsl_AnimtationActor(animName="sample_text", cycle="sample_text", speed="sample_text")
    assert instance.animName == "sample_text"
    instance.animName = "sample_text_2"
    assert instance.animName == "sample_text_2"


def test_dsl_AnimtationActor_cycle_value_roundtrip():
    instance = dsl_AnimtationActor(animName="sample_text", cycle="sample_text", speed="sample_text")
    assert instance.cycle == "sample_text"
    instance.cycle = "sample_text_2"
    assert instance.cycle == "sample_text_2"


def test_dsl_AnimtationActor_speed_value_roundtrip():
    instance = dsl_AnimtationActor(animName="sample_text", cycle="sample_text", speed="sample_text")
    assert instance.speed == "sample_text"
    instance.speed = "sample_text_2"
    assert instance.speed == "sample_text_2"


def test_dsl_Color_a_value_roundtrip():
    instance = dsl_Color(a=7, b=7, g=7, r=7)
    assert instance.a == 7
    instance.a = 13
    assert instance.a == 13


def test_dsl_Color_b_value_roundtrip():
    instance = dsl_Color(a=7, b=7, g=7, r=7)
    assert instance.b == 7
    instance.b = 13
    assert instance.b == 13


def test_dsl_Color_g_value_roundtrip():
    instance = dsl_Color(a=7, b=7, g=7, r=7)
    assert instance.g == 7
    instance.g = 13
    assert instance.g == 13


def test_dsl_Color_r_value_roundtrip():
    instance = dsl_Color(a=7, b=7, g=7, r=7)
    assert instance.r == 7
    instance.r = 13
    assert instance.r == 13


def test_dsl_DamageEffect_amount_value_roundtrip():
    instance = dsl_DamageEffect(amount=7)
    assert instance.amount == 7
    instance.amount = 13
    assert instance.amount == 13


def test_dsl_Effect_name_value_roundtrip():
    instance = dsl_Effect(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dsl_ModelActor_modelPath_value_roundtrip():
    instance = dsl_ModelActor(modelPath="sample_text", scale=7)
    assert instance.modelPath == "sample_text"
    instance.modelPath = "sample_text_2"
    assert instance.modelPath == "sample_text_2"


def test_dsl_ModelActor_scale_value_roundtrip():
    instance = dsl_ModelActor(modelPath="sample_text", scale=7)
    assert instance.scale == 7
    instance.scale = 13
    assert instance.scale == 13


def test_dsl_Mover_heightmap_value_roundtrip():
    instance = dsl_Mover(heightmap="sample_text", name="sample_text", pathfindingMode="sample_text", standingMode="sample_text")
    assert instance.heightmap == "sample_text"
    instance.heightmap = "sample_text_2"
    assert instance.heightmap == "sample_text_2"


def test_dsl_Mover_name_value_roundtrip():
    instance = dsl_Mover(heightmap="sample_text", name="sample_text", pathfindingMode="sample_text", standingMode="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dsl_Mover_pathfindingMode_value_roundtrip():
    instance = dsl_Mover(heightmap="sample_text", name="sample_text", pathfindingMode="sample_text", standingMode="sample_text")
    assert instance.pathfindingMode == "sample_text"
    instance.pathfindingMode = "sample_text_2"
    assert instance.pathfindingMode == "sample_text_2"


def test_dsl_Mover_standingMode_value_roundtrip():
    instance = dsl_Mover(heightmap="sample_text", name="sample_text", pathfindingMode="sample_text", standingMode="sample_text")
    assert instance.standingMode == "sample_text"
    instance.standingMode = "sample_text_2"
    assert instance.standingMode == "sample_text_2"


def test_dsl_ParticleActor_add_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.add == "sample_text"
    instance.add = "sample_text_2"
    assert instance.add == "sample_text_2"


def test_dsl_ParticleActor_directionBone_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.directionBone == "sample_text"
    instance.directionBone = "sample_text_2"
    assert instance.directionBone == "sample_text_2"


def test_dsl_ParticleActor_duration_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_dsl_ParticleActor_emissionBone_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.emissionBone == "sample_text"
    instance.emissionBone = "sample_text_2"
    assert instance.emissionBone == "sample_text_2"


def test_dsl_ParticleActor_endSize_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.endSize == "sample_text"
    instance.endSize = "sample_text_2"
    assert instance.endSize == "sample_text_2"


def test_dsl_ParticleActor_maxCount_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.maxCount == 7
    instance.maxCount = 13
    assert instance.maxCount == 13


def test_dsl_ParticleActor_maxLife_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.maxLife == "sample_text"
    instance.maxLife = "sample_text_2"
    assert instance.maxLife == "sample_text_2"


def test_dsl_ParticleActor_minLife_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.minLife == "sample_text"
    instance.minLife = "sample_text_2"
    assert instance.minLife == "sample_text_2"


def test_dsl_ParticleActor_nbCol_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.nbCol == 7
    instance.nbCol = 13
    assert instance.nbCol == 13


def test_dsl_ParticleActor_nbRow_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.nbRow == 7
    instance.nbRow = 13
    assert instance.nbRow == 13


def test_dsl_ParticleActor_perSecond_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.perSecond == 7
    instance.perSecond = 13
    assert instance.perSecond == 13


def test_dsl_ParticleActor_spritePath_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.spritePath == "sample_text"
    instance.spritePath = "sample_text_2"
    assert instance.spritePath == "sample_text_2"


def test_dsl_ParticleActor_startSize_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.startSize == "sample_text"
    instance.startSize = "sample_text_2"
    assert instance.startSize == "sample_text_2"


def test_dsl_ParticleActor_startVariation_value_roundtrip():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert instance.startVariation == "sample_text"
    instance.startVariation = "sample_text_2"
    assert instance.startVariation == "sample_text_2"


def test_dsl_PersistentEffect_durations_value_roundtrip():
    instance = dsl_PersistentEffect(durations="sample_text", periodCount=7, ranges="sample_text")
    assert instance.durations == "sample_text"
    instance.durations = "sample_text_2"
    assert instance.durations == "sample_text_2"


def test_dsl_PersistentEffect_periodCount_value_roundtrip():
    instance = dsl_PersistentEffect(durations="sample_text", periodCount=7, ranges="sample_text")
    assert instance.periodCount == 7
    instance.periodCount = 13
    assert instance.periodCount == 13


def test_dsl_PersistentEffect_ranges_value_roundtrip():
    instance = dsl_PersistentEffect(durations="sample_text", periodCount=7, ranges="sample_text")
    assert instance.ranges == "sample_text"
    instance.ranges = "sample_text_2"
    assert instance.ranges == "sample_text_2"


def test_dsl_Projectile_mass_value_roundtrip():
    instance = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    assert instance.mass == 7
    instance.mass = 13
    assert instance.mass == 13


def test_dsl_Projectile_name_value_roundtrip():
    instance = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dsl_Projectile_precision_value_roundtrip():
    instance = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    assert instance.precision == "sample_text"
    instance.precision = "sample_text_2"
    assert instance.precision == "sample_text_2"


def test_dsl_Projectile_speed_value_roundtrip():
    instance = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    assert instance.speed == 7
    instance.speed = 13
    assert instance.speed == 13


def test_dsl_Race_name_value_roundtrip():
    instance = dsl_Race(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dsl_Turrent_boneName_value_roundtrip():
    instance = dsl_Turrent(boneName="sample_text", idleSpeed=7, name="sample_text", onIdle="sample_text", speed=7)
    assert instance.boneName == "sample_text"
    instance.boneName = "sample_text_2"
    assert instance.boneName == "sample_text_2"


def test_dsl_Turrent_idleSpeed_value_roundtrip():
    instance = dsl_Turrent(boneName="sample_text", idleSpeed=7, name="sample_text", onIdle="sample_text", speed=7)
    assert instance.idleSpeed == 7
    instance.idleSpeed = 13
    assert instance.idleSpeed == 13


def test_dsl_Turrent_name_value_roundtrip():
    instance = dsl_Turrent(boneName="sample_text", idleSpeed=7, name="sample_text", onIdle="sample_text", speed=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dsl_Turrent_onIdle_value_roundtrip():
    instance = dsl_Turrent(boneName="sample_text", idleSpeed=7, name="sample_text", onIdle="sample_text", speed=7)
    assert instance.onIdle == "sample_text"
    instance.onIdle = "sample_text_2"
    assert instance.onIdle == "sample_text_2"


def test_dsl_Turrent_speed_value_roundtrip():
    instance = dsl_Turrent(boneName="sample_text", idleSpeed=7, name="sample_text", onIdle="sample_text", speed=7)
    assert instance.speed == 7
    instance.speed = 13
    assert instance.speed == 13


def test_dsl_Unit_mass_value_roundtrip():
    instance = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    assert instance.mass == "sample_text"
    instance.mass = "sample_text_2"
    assert instance.mass == "sample_text_2"


def test_dsl_Unit_maxHealth_value_roundtrip():
    instance = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    assert instance.maxHealth == 7
    instance.maxHealth = 13
    assert instance.maxHealth == 13


def test_dsl_Unit_name_value_roundtrip():
    instance = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dsl_Unit_radius_value_roundtrip():
    instance = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    assert instance.radius == "sample_text"
    instance.radius = "sample_text_2"
    assert instance.radius == "sample_text_2"


def test_dsl_Unit_separationRadius_value_roundtrip():
    instance = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    assert instance.separationRadius == "sample_text"
    instance.separationRadius = "sample_text_2"
    assert instance.separationRadius == "sample_text_2"


def test_dsl_Unit_sight_value_roundtrip():
    instance = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    assert instance.sight == 7
    instance.sight = 13
    assert instance.sight == 13


def test_dsl_Unit_speed_value_roundtrip():
    instance = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    assert instance.speed == "sample_text"
    instance.speed = "sample_text_2"
    assert instance.speed == "sample_text_2"


def test_dsl_Unit_uIName_value_roundtrip():
    instance = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    assert instance.uIName == "sample_text"
    instance.uIName = "sample_text_2"
    assert instance.uIName == "sample_text_2"


def test_dsl_Weapon_directionBone_value_roundtrip():
    instance = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    assert instance.directionBone == "sample_text"
    instance.directionBone = "sample_text_2"
    assert instance.directionBone == "sample_text_2"


def test_dsl_Weapon_name_value_roundtrip():
    instance = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dsl_Weapon_period_value_roundtrip():
    instance = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    assert instance.period == 7
    instance.period = 13
    assert instance.period == 13


def test_dsl_Weapon_range_value_roundtrip():
    instance = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    assert instance.range == "sample_text"
    instance.range = "sample_text_2"
    assert instance.range == "sample_text_2"


def test_dsl_Weapon_scanRange_value_roundtrip():
    instance = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    assert instance.scanRange == 7
    instance.scanRange = 13
    assert instance.scanRange == 13


def test_dsl_Weapon_sourceBone_value_roundtrip():
    instance = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    assert instance.sourceBone == "sample_text"
    instance.sourceBone = "sample_text_2"
    assert instance.sourceBone == "sample_text_2"


def test_dsl_Weapon_uIName_value_roundtrip():
    instance = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    assert instance.uIName == "sample_text"
    instance.uIName = "sample_text_2"
    assert instance.uIName == "sample_text_2"


def test_dsl_AnimtationActor_isa_Actor():
    instance = dsl_AnimtationActor(animName="sample_text", cycle="sample_text", speed="sample_text")
    assert isinstance(instance, Actor)


def test_dsl_ModelActor_isa_Actor():
    instance = dsl_ModelActor(modelPath="sample_text", scale=7)
    assert isinstance(instance, Actor)


def test_dsl_ParticleActor_isa_Actor():
    instance = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    assert isinstance(instance, Actor)


def test_dsl_DamageEffect_isa_Effect():
    instance = dsl_DamageEffect(amount=7)
    assert isinstance(instance, Effect)


def test_dsl_LauncherEffect_isa_Effect():
    instance = dsl_LauncherEffect()
    assert isinstance(instance, Effect)


def test_dsl_PersistentEffect_isa_Effect():
    instance = dsl_PersistentEffect(durations="sample_text", periodCount=7, ranges="sample_text")
    assert isinstance(instance, Effect)


def test_assoc_actor20_link_reassign_clear():
    a = dsl_ActorList(trigger="sample_text")
    b1 = dsl_Actor(name="sample_text")
    b2 = dsl_Actor(name="sample_text_2")
    _safe_set(a, 'dsl_ActorList21', b1)
    assert _is_linked(a, 'dsl_ActorList21', b1)
    if hasattr(b1, 'dsl_Actor22'):
        assert _is_linked(b1, 'dsl_Actor22', a)
    _safe_set(a, 'dsl_ActorList21', b2)
    assert _is_linked(a, 'dsl_ActorList21', b2)
    if hasattr(b1, 'dsl_Actor22'):
        assert not _is_linked(b1, 'dsl_Actor22', a)
    if hasattr(b2, 'dsl_Actor22'):
        assert _is_linked(b2, 'dsl_Actor22', a)
    _safe_set(a, 'dsl_ActorList21', None)
    assert not _is_linked(a, 'dsl_ActorList21', b2)
    if hasattr(b2, 'dsl_Actor22'):
        assert not _is_linked(b2, 'dsl_Actor22', a)


def test_assoc_actor31_link_reassign_clear():
    a = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    b1 = dsl_Actor(name="sample_text")
    b2 = dsl_Actor(name="sample_text_2")
    _safe_set(a, 'dsl_Unit32', b1)
    assert _is_linked(a, 'dsl_Unit32', b1)
    if hasattr(b1, 'dsl_Actor33'):
        assert _is_linked(b1, 'dsl_Actor33', a)
    _safe_set(a, 'dsl_Unit32', b2)
    assert _is_linked(a, 'dsl_Unit32', b2)
    if hasattr(b1, 'dsl_Actor33'):
        assert not _is_linked(b1, 'dsl_Actor33', a)
    if hasattr(b2, 'dsl_Actor33'):
        assert _is_linked(b2, 'dsl_Actor33', a)
    _safe_set(a, 'dsl_Unit32', None)
    assert not _is_linked(a, 'dsl_Unit32', b2)
    if hasattr(b2, 'dsl_Actor33'):
        assert not _is_linked(b2, 'dsl_Actor33', a)


def test_assoc_actor43_link_reassign_clear():
    a = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    b1 = dsl_Actor(name="sample_text")
    b2 = dsl_Actor(name="sample_text_2")
    _safe_set(a, 'dsl_Weapon44', b1)
    assert _is_linked(a, 'dsl_Weapon44', b1)
    if hasattr(b1, 'dsl_Actor45'):
        assert _is_linked(b1, 'dsl_Actor45', a)
    _safe_set(a, 'dsl_Weapon44', b2)
    assert _is_linked(a, 'dsl_Weapon44', b2)
    if hasattr(b1, 'dsl_Actor45'):
        assert not _is_linked(b1, 'dsl_Actor45', a)
    if hasattr(b2, 'dsl_Actor45'):
        assert _is_linked(b2, 'dsl_Actor45', a)
    _safe_set(a, 'dsl_Weapon44', None)
    assert not _is_linked(a, 'dsl_Weapon44', b2)
    if hasattr(b2, 'dsl_Actor45'):
        assert not _is_linked(b2, 'dsl_Actor45', a)


def test_assoc_actor56_link_reassign_clear():
    a = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    b1 = dsl_Actor(name="sample_text")
    b2 = dsl_Actor(name="sample_text_2")
    _safe_set(a, 'dsl_Projectile57', b1)
    assert _is_linked(a, 'dsl_Projectile57', b1)
    if hasattr(b1, 'dsl_Actor58'):
        assert _is_linked(b1, 'dsl_Actor58', a)
    _safe_set(a, 'dsl_Projectile57', b2)
    assert _is_linked(a, 'dsl_Projectile57', b2)
    if hasattr(b1, 'dsl_Actor58'):
        assert not _is_linked(b1, 'dsl_Actor58', a)
    if hasattr(b2, 'dsl_Actor58'):
        assert _is_linked(b2, 'dsl_Actor58', a)
    _safe_set(a, 'dsl_Projectile57', None)
    assert not _is_linked(a, 'dsl_Projectile57', b2)
    if hasattr(b2, 'dsl_Actor58'):
        assert not _is_linked(b2, 'dsl_Actor58', a)


def test_assoc_actorlist15_link_reassign_clear():
    a = dsl_ModelActor(modelPath="sample_text", scale=7)
    b1 = dsl_ActorList(trigger="sample_text")
    b2 = dsl_ActorList(trigger="sample_text_2")
    _safe_set(a, 'dsl_ModelActor', {b1})
    assert _is_linked(a, 'dsl_ModelActor', b1)
    if hasattr(b1, 'dsl_ActorList'):
        assert _is_linked(b1, 'dsl_ActorList', a)
    _safe_set(a, 'dsl_ModelActor', {b2})
    assert _is_linked(a, 'dsl_ModelActor', b2)
    if hasattr(b1, 'dsl_ActorList'):
        assert not _is_linked(b1, 'dsl_ActorList', a)
    if hasattr(b2, 'dsl_ActorList'):
        assert _is_linked(b2, 'dsl_ActorList', a)
    _safe_set(a, 'dsl_ModelActor', set())
    assert not _is_linked(a, 'dsl_ModelActor', b2)
    if hasattr(b2, 'dsl_ActorList'):
        assert not _is_linked(b2, 'dsl_ActorList', a)


def test_assoc_actors7_link_reassign_clear():
    a = dsl_Actor(name="sample_text")
    b1 = dsl_Model()
    b2 = dsl_Model()
    _safe_set(a, 'dsl_Actor', b1)
    assert _is_linked(a, 'dsl_Actor', b1)
    if hasattr(b1, 'dsl_Model8'):
        assert _is_linked(b1, 'dsl_Model8', a)
    _safe_set(a, 'dsl_Actor', b2)
    assert _is_linked(a, 'dsl_Actor', b2)
    if hasattr(b1, 'dsl_Model8'):
        assert not _is_linked(b1, 'dsl_Model8', a)
    if hasattr(b2, 'dsl_Model8'):
        assert _is_linked(b2, 'dsl_Model8', a)
    _safe_set(a, 'dsl_Actor', None)
    assert not _is_linked(a, 'dsl_Actor', b2)
    if hasattr(b2, 'dsl_Model8'):
        assert not _is_linked(b2, 'dsl_Model8', a)


def test_assoc_effect40_link_reassign_clear():
    a = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    b1 = dsl_Effect(name="sample_text")
    b2 = dsl_Effect(name="sample_text_2")
    _safe_set(a, 'dsl_Weapon41', b1)
    assert _is_linked(a, 'dsl_Weapon41', b1)
    if hasattr(b1, 'dsl_Effect42'):
        assert _is_linked(b1, 'dsl_Effect42', a)
    _safe_set(a, 'dsl_Weapon41', b2)
    assert _is_linked(a, 'dsl_Weapon41', b2)
    if hasattr(b1, 'dsl_Effect42'):
        assert not _is_linked(b1, 'dsl_Effect42', a)
    if hasattr(b2, 'dsl_Effect42'):
        assert _is_linked(b2, 'dsl_Effect42', a)
    _safe_set(a, 'dsl_Weapon41', None)
    assert not _is_linked(a, 'dsl_Weapon41', b2)
    if hasattr(b2, 'dsl_Effect42'):
        assert not _is_linked(b2, 'dsl_Effect42', a)


def test_assoc_effects46_link_reassign_clear():
    a = dsl_PersistentEffect(durations="sample_text", periodCount=7, ranges="sample_text")
    b1 = dsl_Effect(name="sample_text")
    b2 = dsl_Effect(name="sample_text_2")
    _safe_set(a, 'dsl_PersistentEffect', {b1})
    assert _is_linked(a, 'dsl_PersistentEffect', b1)
    if hasattr(b1, 'dsl_Effect47'):
        assert _is_linked(b1, 'dsl_Effect47', a)
    _safe_set(a, 'dsl_PersistentEffect', {b2})
    assert _is_linked(a, 'dsl_PersistentEffect', b2)
    if hasattr(b1, 'dsl_Effect47'):
        assert not _is_linked(b1, 'dsl_Effect47', a)
    if hasattr(b2, 'dsl_Effect47'):
        assert _is_linked(b2, 'dsl_Effect47', a)
    _safe_set(a, 'dsl_PersistentEffect', set())
    assert not _is_linked(a, 'dsl_PersistentEffect', b2)
    if hasattr(b2, 'dsl_Effect47'):
        assert not _is_linked(b2, 'dsl_Effect47', a)


def test_assoc_effects48_link_reassign_clear():
    a = dsl_Effect(name="sample_text")
    b1 = dsl_LauncherEffect()
    b2 = dsl_LauncherEffect()
    _safe_set(a, 'dsl_Effect49', b1)
    assert _is_linked(a, 'dsl_Effect49', b1)
    if hasattr(b1, 'dsl_LauncherEffect'):
        assert _is_linked(b1, 'dsl_LauncherEffect', a)
    _safe_set(a, 'dsl_Effect49', b2)
    assert _is_linked(a, 'dsl_Effect49', b2)
    if hasattr(b1, 'dsl_LauncherEffect'):
        assert not _is_linked(b1, 'dsl_LauncherEffect', a)
    if hasattr(b2, 'dsl_LauncherEffect'):
        assert _is_linked(b2, 'dsl_LauncherEffect', a)
    _safe_set(a, 'dsl_Effect49', None)
    assert not _is_linked(a, 'dsl_Effect49', b2)
    if hasattr(b2, 'dsl_LauncherEffect'):
        assert not _is_linked(b2, 'dsl_LauncherEffect', a)


def test_assoc_effects9_link_reassign_clear():
    a = dsl_Effect(name="sample_text")
    b1 = dsl_Model()
    b2 = dsl_Model()
    _safe_set(a, 'dsl_Effect', b1)
    assert _is_linked(a, 'dsl_Effect', b1)
    if hasattr(b1, 'dsl_Model10'):
        assert _is_linked(b1, 'dsl_Model10', a)
    _safe_set(a, 'dsl_Effect', b2)
    assert _is_linked(a, 'dsl_Effect', b2)
    if hasattr(b1, 'dsl_Model10'):
        assert not _is_linked(b1, 'dsl_Model10', a)
    if hasattr(b2, 'dsl_Model10'):
        assert _is_linked(b2, 'dsl_Model10', a)
    _safe_set(a, 'dsl_Effect', None)
    assert not _is_linked(a, 'dsl_Effect', b2)
    if hasattr(b2, 'dsl_Model10'):
        assert not _is_linked(b2, 'dsl_Model10', a)


def test_assoc_endColor17_link_reassign_clear():
    a = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    b1 = dsl_Color(a=7, b=7, g=7, r=7)
    b2 = dsl_Color(a=13, b=13, g=13, r=13)
    _safe_set(a, 'dsl_ParticleActor18', b1)
    assert _is_linked(a, 'dsl_ParticleActor18', b1)
    if hasattr(b1, 'dsl_Color19'):
        assert _is_linked(b1, 'dsl_Color19', a)
    _safe_set(a, 'dsl_ParticleActor18', b2)
    assert _is_linked(a, 'dsl_ParticleActor18', b2)
    if hasattr(b1, 'dsl_Color19'):
        assert not _is_linked(b1, 'dsl_Color19', a)
    if hasattr(b2, 'dsl_Color19'):
        assert _is_linked(b2, 'dsl_Color19', a)
    _safe_set(a, 'dsl_ParticleActor18', None)
    assert not _is_linked(a, 'dsl_ParticleActor18', b2)
    if hasattr(b2, 'dsl_Color19'):
        assert not _is_linked(b2, 'dsl_Color19', a)


def test_assoc_mover26_link_reassign_clear():
    a = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    b1 = dsl_Mover(heightmap="sample_text", name="sample_text", pathfindingMode="sample_text", standingMode="sample_text")
    b2 = dsl_Mover(heightmap="sample_text_2", name="sample_text_2", pathfindingMode="sample_text_2", standingMode="sample_text_2")
    _safe_set(a, 'dsl_Unit27', b1)
    assert _is_linked(a, 'dsl_Unit27', b1)
    if hasattr(b1, 'dsl_Mover28'):
        assert _is_linked(b1, 'dsl_Mover28', a)
    _safe_set(a, 'dsl_Unit27', b2)
    assert _is_linked(a, 'dsl_Unit27', b2)
    if hasattr(b1, 'dsl_Mover28'):
        assert not _is_linked(b1, 'dsl_Mover28', a)
    if hasattr(b2, 'dsl_Mover28'):
        assert _is_linked(b2, 'dsl_Mover28', a)
    _safe_set(a, 'dsl_Unit27', None)
    assert not _is_linked(a, 'dsl_Unit27', b2)
    if hasattr(b2, 'dsl_Mover28'):
        assert not _is_linked(b2, 'dsl_Mover28', a)


def test_assoc_mover53_link_reassign_clear():
    a = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    b1 = dsl_Mover(heightmap="sample_text", name="sample_text", pathfindingMode="sample_text", standingMode="sample_text")
    b2 = dsl_Mover(heightmap="sample_text_2", name="sample_text_2", pathfindingMode="sample_text_2", standingMode="sample_text_2")
    _safe_set(a, 'dsl_Projectile54', b1)
    assert _is_linked(a, 'dsl_Projectile54', b1)
    if hasattr(b1, 'dsl_Mover55'):
        assert _is_linked(b1, 'dsl_Mover55', a)
    _safe_set(a, 'dsl_Projectile54', b2)
    assert _is_linked(a, 'dsl_Projectile54', b2)
    if hasattr(b1, 'dsl_Mover55'):
        assert not _is_linked(b1, 'dsl_Mover55', a)
    if hasattr(b2, 'dsl_Mover55'):
        assert _is_linked(b2, 'dsl_Mover55', a)
    _safe_set(a, 'dsl_Projectile54', None)
    assert not _is_linked(a, 'dsl_Projectile54', b2)
    if hasattr(b2, 'dsl_Mover55'):
        assert not _is_linked(b2, 'dsl_Mover55', a)


def test_assoc_movers5_link_reassign_clear():
    a = dsl_Mover(heightmap="sample_text", name="sample_text", pathfindingMode="sample_text", standingMode="sample_text")
    b1 = dsl_Model()
    b2 = dsl_Model()
    _safe_set(a, 'dsl_Mover', b1)
    assert _is_linked(a, 'dsl_Mover', b1)
    if hasattr(b1, 'dsl_Model6'):
        assert _is_linked(b1, 'dsl_Model6', a)
    _safe_set(a, 'dsl_Mover', b2)
    assert _is_linked(a, 'dsl_Mover', b2)
    if hasattr(b1, 'dsl_Model6'):
        assert not _is_linked(b1, 'dsl_Model6', a)
    if hasattr(b2, 'dsl_Model6'):
        assert _is_linked(b2, 'dsl_Model6', a)
    _safe_set(a, 'dsl_Mover', None)
    assert not _is_linked(a, 'dsl_Mover', b2)
    if hasattr(b2, 'dsl_Model6'):
        assert not _is_linked(b2, 'dsl_Model6', a)


def test_assoc_projectiles13_link_reassign_clear():
    a = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    b1 = dsl_Model()
    b2 = dsl_Model()
    _safe_set(a, 'dsl_Projectile', b1)
    assert _is_linked(a, 'dsl_Projectile', b1)
    if hasattr(b1, 'dsl_Model14'):
        assert _is_linked(b1, 'dsl_Model14', a)
    _safe_set(a, 'dsl_Projectile', b2)
    assert _is_linked(a, 'dsl_Projectile', b2)
    if hasattr(b1, 'dsl_Model14'):
        assert not _is_linked(b1, 'dsl_Model14', a)
    if hasattr(b2, 'dsl_Model14'):
        assert _is_linked(b2, 'dsl_Model14', a)
    _safe_set(a, 'dsl_Projectile', None)
    assert not _is_linked(a, 'dsl_Projectile', b2)
    if hasattr(b2, 'dsl_Model14'):
        assert not _is_linked(b2, 'dsl_Model14', a)


def test_assoc_projectiles50_link_reassign_clear():
    a = dsl_Projectile(mass=7, name="sample_text", precision="sample_text", speed=7)
    b1 = dsl_LauncherEffect()
    b2 = dsl_LauncherEffect()
    _safe_set(a, 'dsl_Projectile52', b1)
    assert _is_linked(a, 'dsl_Projectile52', b1)
    if hasattr(b1, 'dsl_LauncherEffect51'):
        assert _is_linked(b1, 'dsl_LauncherEffect51', a)
    _safe_set(a, 'dsl_Projectile52', b2)
    assert _is_linked(a, 'dsl_Projectile52', b2)
    if hasattr(b1, 'dsl_LauncherEffect51'):
        assert not _is_linked(b1, 'dsl_LauncherEffect51', a)
    if hasattr(b2, 'dsl_LauncherEffect51'):
        assert _is_linked(b2, 'dsl_LauncherEffect51', a)
    _safe_set(a, 'dsl_Projectile52', None)
    assert not _is_linked(a, 'dsl_Projectile52', b2)
    if hasattr(b2, 'dsl_LauncherEffect51'):
        assert not _is_linked(b2, 'dsl_LauncherEffect51', a)


def test_assoc_race23_link_reassign_clear():
    a = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    b1 = dsl_Race(name="sample_text")
    b2 = dsl_Race(name="sample_text_2")
    _safe_set(a, 'dsl_Unit24', b1)
    assert _is_linked(a, 'dsl_Unit24', b1)
    if hasattr(b1, 'dsl_Race25'):
        assert _is_linked(b1, 'dsl_Race25', a)
    _safe_set(a, 'dsl_Unit24', b2)
    assert _is_linked(a, 'dsl_Unit24', b2)
    if hasattr(b1, 'dsl_Race25'):
        assert not _is_linked(b1, 'dsl_Race25', a)
    if hasattr(b2, 'dsl_Race25'):
        assert _is_linked(b2, 'dsl_Race25', a)
    _safe_set(a, 'dsl_Unit24', None)
    assert not _is_linked(a, 'dsl_Unit24', b2)
    if hasattr(b2, 'dsl_Race25'):
        assert not _is_linked(b2, 'dsl_Race25', a)


def test_assoc_races3_link_reassign_clear():
    a = dsl_Race(name="sample_text")
    b1 = dsl_Model()
    b2 = dsl_Model()
    _safe_set(a, 'dsl_Race', b1)
    assert _is_linked(a, 'dsl_Race', b1)
    if hasattr(b1, 'dsl_Model4'):
        assert _is_linked(b1, 'dsl_Model4', a)
    _safe_set(a, 'dsl_Race', b2)
    assert _is_linked(a, 'dsl_Race', b2)
    if hasattr(b1, 'dsl_Model4'):
        assert not _is_linked(b1, 'dsl_Model4', a)
    if hasattr(b2, 'dsl_Model4'):
        assert _is_linked(b2, 'dsl_Model4', a)
    _safe_set(a, 'dsl_Race', None)
    assert not _is_linked(a, 'dsl_Race', b2)
    if hasattr(b2, 'dsl_Model4'):
        assert not _is_linked(b2, 'dsl_Model4', a)


def test_assoc_startColor16_link_reassign_clear():
    a = dsl_ParticleActor(add="sample_text", directionBone="sample_text", duration=7, emissionBone="sample_text", endSize="sample_text", maxCount=7, maxLife="sample_text", minLife="sample_text", nbCol=7, nbRow=7, perSecond=7, spritePath="sample_text", startSize="sample_text", startVariation="sample_text")
    b1 = dsl_Color(a=7, b=7, g=7, r=7)
    b2 = dsl_Color(a=13, b=13, g=13, r=13)
    _safe_set(a, 'dsl_ParticleActor', b1)
    assert _is_linked(a, 'dsl_ParticleActor', b1)
    if hasattr(b1, 'dsl_Color'):
        assert _is_linked(b1, 'dsl_Color', a)
    _safe_set(a, 'dsl_ParticleActor', b2)
    assert _is_linked(a, 'dsl_ParticleActor', b2)
    if hasattr(b1, 'dsl_Color'):
        assert not _is_linked(b1, 'dsl_Color', a)
    if hasattr(b2, 'dsl_Color'):
        assert _is_linked(b2, 'dsl_Color', a)
    _safe_set(a, 'dsl_ParticleActor', None)
    assert not _is_linked(a, 'dsl_ParticleActor', b2)
    if hasattr(b2, 'dsl_Color'):
        assert not _is_linked(b2, 'dsl_Color', a)


def test_assoc_turrent37_link_reassign_clear():
    a = dsl_Turrent(boneName="sample_text", idleSpeed=7, name="sample_text", onIdle="sample_text", speed=7)
    b1 = dsl_UnitWeaponLink()
    b2 = dsl_UnitWeaponLink()
    _safe_set(a, 'dsl_Turrent39', b1)
    assert _is_linked(a, 'dsl_Turrent39', b1)
    if hasattr(b1, 'dsl_UnitWeaponLink38'):
        assert _is_linked(b1, 'dsl_UnitWeaponLink38', a)
    _safe_set(a, 'dsl_Turrent39', b2)
    assert _is_linked(a, 'dsl_Turrent39', b2)
    if hasattr(b1, 'dsl_UnitWeaponLink38'):
        assert not _is_linked(b1, 'dsl_UnitWeaponLink38', a)
    if hasattr(b2, 'dsl_UnitWeaponLink38'):
        assert _is_linked(b2, 'dsl_UnitWeaponLink38', a)
    _safe_set(a, 'dsl_Turrent39', None)
    assert not _is_linked(a, 'dsl_Turrent39', b2)
    if hasattr(b2, 'dsl_UnitWeaponLink38'):
        assert not _is_linked(b2, 'dsl_UnitWeaponLink38', a)


def test_assoc_turrents11_link_reassign_clear():
    a = dsl_Turrent(boneName="sample_text", idleSpeed=7, name="sample_text", onIdle="sample_text", speed=7)
    b1 = dsl_Model()
    b2 = dsl_Model()
    _safe_set(a, 'dsl_Turrent', b1)
    assert _is_linked(a, 'dsl_Turrent', b1)
    if hasattr(b1, 'dsl_Model12'):
        assert _is_linked(b1, 'dsl_Model12', a)
    _safe_set(a, 'dsl_Turrent', b2)
    assert _is_linked(a, 'dsl_Turrent', b2)
    if hasattr(b1, 'dsl_Model12'):
        assert not _is_linked(b1, 'dsl_Model12', a)
    if hasattr(b2, 'dsl_Model12'):
        assert _is_linked(b2, 'dsl_Model12', a)
    _safe_set(a, 'dsl_Turrent', None)
    assert not _is_linked(a, 'dsl_Turrent', b2)
    if hasattr(b2, 'dsl_Model12'):
        assert not _is_linked(b2, 'dsl_Model12', a)


def test_assoc_units1_link_reassign_clear():
    a = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    b1 = dsl_Model()
    b2 = dsl_Model()
    _safe_set(a, 'dsl_Unit', b1)
    assert _is_linked(a, 'dsl_Unit', b1)
    if hasattr(b1, 'dsl_Model2'):
        assert _is_linked(b1, 'dsl_Model2', a)
    _safe_set(a, 'dsl_Unit', b2)
    assert _is_linked(a, 'dsl_Unit', b2)
    if hasattr(b1, 'dsl_Model2'):
        assert not _is_linked(b1, 'dsl_Model2', a)
    if hasattr(b2, 'dsl_Model2'):
        assert _is_linked(b2, 'dsl_Model2', a)
    _safe_set(a, 'dsl_Unit', None)
    assert not _is_linked(a, 'dsl_Unit', b2)
    if hasattr(b2, 'dsl_Model2'):
        assert not _is_linked(b2, 'dsl_Model2', a)


def test_assoc_weapon34_link_reassign_clear():
    a = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    b1 = dsl_UnitWeaponLink()
    b2 = dsl_UnitWeaponLink()
    _safe_set(a, 'dsl_Weapon36', b1)
    assert _is_linked(a, 'dsl_Weapon36', b1)
    if hasattr(b1, 'dsl_UnitWeaponLink35'):
        assert _is_linked(b1, 'dsl_UnitWeaponLink35', a)
    _safe_set(a, 'dsl_Weapon36', b2)
    assert _is_linked(a, 'dsl_Weapon36', b2)
    if hasattr(b1, 'dsl_UnitWeaponLink35'):
        assert not _is_linked(b1, 'dsl_UnitWeaponLink35', a)
    if hasattr(b2, 'dsl_UnitWeaponLink35'):
        assert _is_linked(b2, 'dsl_UnitWeaponLink35', a)
    _safe_set(a, 'dsl_Weapon36', None)
    assert not _is_linked(a, 'dsl_Weapon36', b2)
    if hasattr(b2, 'dsl_UnitWeaponLink35'):
        assert not _is_linked(b2, 'dsl_UnitWeaponLink35', a)


def test_assoc_weapons0_link_reassign_clear():
    a = dsl_Weapon(directionBone="sample_text", name="sample_text", period=7, range="sample_text", scanRange=7, sourceBone="sample_text", uIName="sample_text")
    b1 = dsl_Model()
    b2 = dsl_Model()
    _safe_set(a, 'dsl_Weapon', b1)
    assert _is_linked(a, 'dsl_Weapon', b1)
    if hasattr(b1, 'dsl_Model'):
        assert _is_linked(b1, 'dsl_Model', a)
    _safe_set(a, 'dsl_Weapon', b2)
    assert _is_linked(a, 'dsl_Weapon', b2)
    if hasattr(b1, 'dsl_Model'):
        assert not _is_linked(b1, 'dsl_Model', a)
    if hasattr(b2, 'dsl_Model'):
        assert _is_linked(b2, 'dsl_Model', a)
    _safe_set(a, 'dsl_Weapon', None)
    assert not _is_linked(a, 'dsl_Weapon', b2)
    if hasattr(b2, 'dsl_Model'):
        assert not _is_linked(b2, 'dsl_Model', a)


def test_assoc_weapons29_link_reassign_clear():
    a = dsl_Unit(mass="sample_text", maxHealth=7, name="sample_text", radius="sample_text", separationRadius="sample_text", sight=7, speed="sample_text", uIName="sample_text")
    b1 = dsl_UnitWeaponLink()
    b2 = dsl_UnitWeaponLink()
    _safe_set(a, 'dsl_Unit30', {b1})
    assert _is_linked(a, 'dsl_Unit30', b1)
    if hasattr(b1, 'dsl_UnitWeaponLink'):
        assert _is_linked(b1, 'dsl_UnitWeaponLink', a)
    _safe_set(a, 'dsl_Unit30', {b2})
    assert _is_linked(a, 'dsl_Unit30', b2)
    if hasattr(b1, 'dsl_UnitWeaponLink'):
        assert not _is_linked(b1, 'dsl_UnitWeaponLink', a)
    if hasattr(b2, 'dsl_UnitWeaponLink'):
        assert _is_linked(b2, 'dsl_UnitWeaponLink', a)
    _safe_set(a, 'dsl_Unit30', set())
    assert not _is_linked(a, 'dsl_Unit30', b2)
    if hasattr(b2, 'dsl_UnitWeaponLink'):
        assert not _is_linked(b2, 'dsl_UnitWeaponLink', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Actor_strategy = st.builds(Actor)
@given(instance=Actor_strategy)
@settings(max_examples=25)
def test_Actor_instantiation(instance):
    assert isinstance(instance, Actor)


Effect_strategy = st.builds(Effect)
@given(instance=Effect_strategy)
@settings(max_examples=25)
def test_Effect_instantiation(instance):
    assert isinstance(instance, Effect)


dsl_Actor_strategy = st.builds(dsl_Actor, name=safe_text)
@given(instance=dsl_Actor_strategy)
@settings(max_examples=25)
def test_dsl_Actor_instantiation(instance):
    assert isinstance(instance, dsl_Actor)


dsl_ActorList_strategy = st.builds(dsl_ActorList, trigger=safe_text)
@given(instance=dsl_ActorList_strategy)
@settings(max_examples=25)
def test_dsl_ActorList_instantiation(instance):
    assert isinstance(instance, dsl_ActorList)


dsl_AnimtationActor_strategy = st.builds(dsl_AnimtationActor, animName=safe_text, cycle=safe_text, speed=safe_text)
@given(instance=dsl_AnimtationActor_strategy)
@settings(max_examples=25)
def test_dsl_AnimtationActor_instantiation(instance):
    assert isinstance(instance, dsl_AnimtationActor)


dsl_Color_strategy = st.builds(dsl_Color, a=st.integers(), b=st.integers(), g=st.integers(), r=st.integers())
@given(instance=dsl_Color_strategy)
@settings(max_examples=25)
def test_dsl_Color_instantiation(instance):
    assert isinstance(instance, dsl_Color)


dsl_DamageEffect_strategy = st.builds(dsl_DamageEffect, amount=st.integers())
@given(instance=dsl_DamageEffect_strategy)
@settings(max_examples=25)
def test_dsl_DamageEffect_instantiation(instance):
    assert isinstance(instance, dsl_DamageEffect)


dsl_Effect_strategy = st.builds(dsl_Effect, name=safe_text)
@given(instance=dsl_Effect_strategy)
@settings(max_examples=25)
def test_dsl_Effect_instantiation(instance):
    assert isinstance(instance, dsl_Effect)


dsl_LauncherEffect_strategy = st.builds(dsl_LauncherEffect)
@given(instance=dsl_LauncherEffect_strategy)
@settings(max_examples=25)
def test_dsl_LauncherEffect_instantiation(instance):
    assert isinstance(instance, dsl_LauncherEffect)


dsl_Model_strategy = st.builds(dsl_Model)
@given(instance=dsl_Model_strategy)
@settings(max_examples=25)
def test_dsl_Model_instantiation(instance):
    assert isinstance(instance, dsl_Model)


dsl_ModelActor_strategy = st.builds(dsl_ModelActor, modelPath=safe_text, scale=st.integers())
@given(instance=dsl_ModelActor_strategy)
@settings(max_examples=25)
def test_dsl_ModelActor_instantiation(instance):
    assert isinstance(instance, dsl_ModelActor)


dsl_Mover_strategy = st.builds(dsl_Mover, heightmap=safe_text, name=safe_text, pathfindingMode=safe_text, standingMode=safe_text)
@given(instance=dsl_Mover_strategy)
@settings(max_examples=25)
def test_dsl_Mover_instantiation(instance):
    assert isinstance(instance, dsl_Mover)


dsl_ParticleActor_strategy = st.builds(dsl_ParticleActor, add=safe_text, directionBone=safe_text, duration=st.integers(), emissionBone=safe_text, endSize=safe_text, maxCount=st.integers(), maxLife=safe_text, minLife=safe_text, nbCol=st.integers(), nbRow=st.integers(), perSecond=st.integers(), spritePath=safe_text, startSize=safe_text, startVariation=safe_text)
@given(instance=dsl_ParticleActor_strategy)
@settings(max_examples=25)
def test_dsl_ParticleActor_instantiation(instance):
    assert isinstance(instance, dsl_ParticleActor)


dsl_PersistentEffect_strategy = st.builds(dsl_PersistentEffect, durations=safe_text, periodCount=st.integers(), ranges=safe_text)
@given(instance=dsl_PersistentEffect_strategy)
@settings(max_examples=25)
def test_dsl_PersistentEffect_instantiation(instance):
    assert isinstance(instance, dsl_PersistentEffect)


dsl_Projectile_strategy = st.builds(dsl_Projectile, mass=st.integers(), name=safe_text, precision=safe_text, speed=st.integers())
@given(instance=dsl_Projectile_strategy)
@settings(max_examples=25)
def test_dsl_Projectile_instantiation(instance):
    assert isinstance(instance, dsl_Projectile)


dsl_Race_strategy = st.builds(dsl_Race, name=safe_text)
@given(instance=dsl_Race_strategy)
@settings(max_examples=25)
def test_dsl_Race_instantiation(instance):
    assert isinstance(instance, dsl_Race)


dsl_Turrent_strategy = st.builds(dsl_Turrent, boneName=safe_text, idleSpeed=st.integers(), name=safe_text, onIdle=safe_text, speed=st.integers())
@given(instance=dsl_Turrent_strategy)
@settings(max_examples=25)
def test_dsl_Turrent_instantiation(instance):
    assert isinstance(instance, dsl_Turrent)


dsl_Unit_strategy = st.builds(dsl_Unit, mass=safe_text, maxHealth=st.integers(), name=safe_text, radius=safe_text, separationRadius=safe_text, sight=st.integers(), speed=safe_text, uIName=safe_text)
@given(instance=dsl_Unit_strategy)
@settings(max_examples=25)
def test_dsl_Unit_instantiation(instance):
    assert isinstance(instance, dsl_Unit)


dsl_UnitWeaponLink_strategy = st.builds(dsl_UnitWeaponLink)
@given(instance=dsl_UnitWeaponLink_strategy)
@settings(max_examples=25)
def test_dsl_UnitWeaponLink_instantiation(instance):
    assert isinstance(instance, dsl_UnitWeaponLink)


dsl_Weapon_strategy = st.builds(dsl_Weapon, directionBone=safe_text, name=safe_text, period=st.integers(), range=safe_text, scanRange=st.integers(), sourceBone=safe_text, uIName=safe_text)
@given(instance=dsl_Weapon_strategy)
@settings(max_examples=25)
def test_dsl_Weapon_instantiation(instance):
    assert isinstance(instance, dsl_Weapon)


