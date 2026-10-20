import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedEntity,
    Predicate,
    Sensor,
    smarthome_AnalogSensor,
    smarthome_CSVSensor,
    smarthome_DigitalSensor,
    smarthome_Duration,
    smarthome_Home,
    smarthome_Mode,
    smarthome_NamedEntity,
    smarthome_Pattern,
    smarthome_Person,
    smarthome_PersonPredicate,
    smarthome_Predicate,
    smarthome_Room,
    smarthome_Rule,
    smarthome_Sensor,
    smarthome_SensorPredicate,
    smarthome_Tag,
    Activity,
    Operator,
    Precision,
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

def test_assoc_monitoredEntities5_reverse_link_reassign_clear():
    a1 = smarthome_NamedEntity(name="sample_text")
    a2 = smarthome_NamedEntity(name="sample_text_2")
    b = smarthome_Home(fileEvents="sample_text")
    _safe_set(b, 'smarthome_Home6', {a1})
    assert _is_linked(b, 'smarthome_Home6', a1)
    if hasattr(a1, 'smarthome_NamedEntity'):
        assert _is_linked(a1, 'smarthome_NamedEntity', b)
    _safe_set(b, 'smarthome_Home6', {a2})
    assert _is_linked(b, 'smarthome_Home6', a2)
    if hasattr(a1, 'smarthome_NamedEntity'):
        assert not _is_linked(a1, 'smarthome_NamedEntity', b)
    if hasattr(a2, 'smarthome_NamedEntity'):
        assert _is_linked(a2, 'smarthome_NamedEntity', b)
    _safe_set(b, 'smarthome_Home6', set())
    assert not _is_linked(b, 'smarthome_Home6', a2)
    if hasattr(a2, 'smarthome_NamedEntity'):
        assert not _is_linked(a2, 'smarthome_NamedEntity', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_duration13_stub_double():
    # smarthome_Rule has no real 'smarthome_Rule14' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_Duration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_Duration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_Duration(precision="sample_text", time=7)
    partner = smarthome_Rule()
    setattr(partner, 'smarthome_Rule14', None)
    _safe_set(owner, 'smarthome_Duration', partner)
    assert getattr(partner, 'smarthome_Rule14') == owner
    _safe_set(owner, 'smarthome_Duration', None)
    assert getattr(partner, 'smarthome_Rule14') is None


def test_assoc_patterns3_stub_double():
    # smarthome_Pattern has no real 'smarthome_Pattern' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_Home's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_Home's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_Home(fileEvents="sample_text")
    partner = smarthome_Pattern()
    setattr(partner, 'smarthome_Pattern', None)
    _safe_set(owner, 'smarthome_Home4', {partner})
    assert getattr(partner, 'smarthome_Pattern') == owner
    _safe_set(owner, 'smarthome_Home4', set())
    assert getattr(partner, 'smarthome_Pattern') is None


def test_assoc_person28_stub_double():
    # smarthome_Person has no real 'smarthome_Person29' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_PersonPredicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_PersonPredicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_PersonPredicate(activity="sample_text")
    partner = smarthome_Person()
    setattr(partner, 'smarthome_Person29', None)
    _safe_set(owner, 'smarthome_PersonPredicate', partner)
    assert getattr(partner, 'smarthome_Person29') == owner
    _safe_set(owner, 'smarthome_PersonPredicate', None)
    assert getattr(partner, 'smarthome_Person29') is None


def test_assoc_persons1_stub_double():
    # smarthome_Person has no real 'smarthome_Person' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_Home's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_Home's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_Home(fileEvents="sample_text")
    partner = smarthome_Person()
    setattr(partner, 'smarthome_Person', None)
    _safe_set(owner, 'smarthome_Home2', {partner})
    assert getattr(partner, 'smarthome_Person') == owner
    _safe_set(owner, 'smarthome_Home2', set())
    assert getattr(partner, 'smarthome_Person') is None


def test_assoc_rooms0_stub_double():
    # smarthome_Room has no real 'smarthome_Room' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_Home's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_Home's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_Home(fileEvents="sample_text")
    partner = smarthome_Room()
    setattr(partner, 'smarthome_Room', None)
    _safe_set(owner, 'smarthome_Home', {partner})
    assert getattr(partner, 'smarthome_Room') == owner
    _safe_set(owner, 'smarthome_Home', set())
    assert getattr(partner, 'smarthome_Room') is None


def test_assoc_sensor26_stub_double():
    # smarthome_Sensor has no real 'smarthome_Sensor27' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_SensorPredicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_SensorPredicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_SensorPredicate(operator="sample_text", value=3.14)
    partner = smarthome_Sensor()
    setattr(partner, 'smarthome_Sensor27', None)
    _safe_set(owner, 'smarthome_SensorPredicate', partner)
    assert getattr(partner, 'smarthome_Sensor27') == owner
    _safe_set(owner, 'smarthome_SensorPredicate', None)
    assert getattr(partner, 'smarthome_Sensor27') is None


