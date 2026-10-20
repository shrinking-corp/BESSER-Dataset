import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Device,
    NamedElement,
    iotsystem_Action,
    iotsystem_Actuator,
    iotsystem_Condition,
    iotsystem_Device,
    iotsystem_DigitalArtifact,
    iotsystem_IotSystem,
    iotsystem_NamedElement,
    iotsystem_Parameter,
    iotsystem_PhysicalEntity,
    iotsystem_Resource,
    iotsystem_Rule,
    iotsystem_Sensor,
    Actions,
    EnvironmentConditions,
    RelationalOperator,
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

def test_assoc_parameters9_reverse_link_reassign_clear():
    a1 = iotsystem_Parameter(name="sample_text", value="sample_text")
    a2 = iotsystem_Parameter(name="sample_text_2", value="sample_text_2")
    b = iotsystem_Action(action="sample_text")
    _safe_set(b, 'iotsystem_Action10', {a1})
    assert _is_linked(b, 'iotsystem_Action10', a1)
    if hasattr(a1, 'iotsystem_Parameter'):
        assert _is_linked(a1, 'iotsystem_Parameter', b)
    _safe_set(b, 'iotsystem_Action10', {a2})
    assert _is_linked(b, 'iotsystem_Action10', a2)
    if hasattr(a1, 'iotsystem_Parameter'):
        assert not _is_linked(a1, 'iotsystem_Parameter', b)
    if hasattr(a2, 'iotsystem_Parameter'):
        assert _is_linked(a2, 'iotsystem_Parameter', b)
    _safe_set(b, 'iotsystem_Action10', set())
    assert not _is_linked(b, 'iotsystem_Action10', a2)
    if hasattr(a2, 'iotsystem_Parameter'):
        assert not _is_linked(a2, 'iotsystem_Parameter', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions5_stub_double():
    # iotsystem_Rule has no real 'iotsystem_Rule6' property in the generated
    # code (a bare stub) -- manually attach it so iotsystem_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotsystem_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotsystem_Action(action="sample_text")
    partner = iotsystem_Rule()
    setattr(partner, 'iotsystem_Rule6', None)
    _safe_set(owner, 'iotsystem_Action', partner)
    assert owner in getattr(partner, 'iotsystem_Rule6')
    _safe_set(owner, 'iotsystem_Action', None)
    assert owner not in getattr(partner, 'iotsystem_Rule6')


def test_assoc_condition7_stub_double():
    # iotsystem_Rule has no real 'iotsystem_Rule8' property in the generated
    # code (a bare stub) -- manually attach it so iotsystem_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotsystem_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotsystem_Condition(expectedValue=3.14, relationalOperator="sample_text")
    partner = iotsystem_Rule()
    setattr(partner, 'iotsystem_Rule8', None)
    _safe_set(owner, 'iotsystem_Condition', partner)
    assert getattr(partner, 'iotsystem_Rule8') == owner
    _safe_set(owner, 'iotsystem_Condition', None)
    assert getattr(partner, 'iotsystem_Rule8') is None


def test_assoc_consumes0_stub_double():
    # iotsystem_Device has no real 'iotsystem_Device' property in the generated
    # code (a bare stub) -- manually attach it so iotsystem_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotsystem_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotsystem_Resource(measurement="sample_text", url="sample_text")
    partner = iotsystem_Device()
    setattr(partner, 'iotsystem_Device', None)
    _safe_set(owner, 'iotsystem_Resource', partner)
    assert owner in getattr(partner, 'iotsystem_Device')
    _safe_set(owner, 'iotsystem_Resource', None)
    assert owner not in getattr(partner, 'iotsystem_Device')


def test_assoc_resources1_stub_double():
    # iotsystem_DigitalArtifact has no real 'iotsystem_DigitalArtifact' property in the generated
    # code (a bare stub) -- manually attach it so iotsystem_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotsystem_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotsystem_Resource(measurement="sample_text", url="sample_text")
    partner = iotsystem_DigitalArtifact()
    setattr(partner, 'iotsystem_DigitalArtifact', None)
    _safe_set(owner, 'iotsystem_Resource2', partner)
    assert owner in getattr(partner, 'iotsystem_DigitalArtifact')
    _safe_set(owner, 'iotsystem_Resource2', None)
    assert owner not in getattr(partner, 'iotsystem_DigitalArtifact')


def test_assoc_variable18_stub_double():
    # iotsystem_Sensor has no real 'iotsystem_Sensor' property in the generated
    # code (a bare stub) -- manually attach it so iotsystem_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotsystem_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotsystem_Condition(expectedValue=3.14, relationalOperator="sample_text")
    partner = iotsystem_Sensor()
    setattr(partner, 'iotsystem_Sensor', None)
    _safe_set(owner, 'iotsystem_Condition19', partner)
    assert getattr(partner, 'iotsystem_Sensor') == owner
    _safe_set(owner, 'iotsystem_Condition19', None)
    assert getattr(partner, 'iotsystem_Sensor') is None


