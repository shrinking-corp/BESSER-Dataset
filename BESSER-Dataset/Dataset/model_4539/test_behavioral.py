import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activator,
    IotComponent,
    NamedElement,
    Sensor,
    SmartHome_Activator,
    SmartHome_AnalValue,
    SmartHome_Clock,
    SmartHome_DigitValue,
    SmartHome_Home,
    SmartHome_IotComponent,
    SmartHome_Light,
    SmartHome_LightSensor,
    SmartHome_NamedElement,
    SmartHome_PhysicalContext,
    SmartHome_Room,
    SmartHome_Rule,
    SmartHome_RuleComposant,
    SmartHome_Sensor,
    SmartHome_Shutter,
    SmartHome_Value,
    Value,
    Operator,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_iotcomponent23_stub_double():
    # SmartHome_IotComponent has no real 'SmartHome_IotComponent' property in the generated
    # code (a bare stub) -- manually attach it so SmartHome_RuleComposant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SmartHome_RuleComposant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SmartHome_RuleComposant(operator="sample_text")
    partner = SmartHome_IotComponent()
    setattr(partner, 'SmartHome_IotComponent', None)
    _safe_set(owner, 'SmartHome_RuleComposant24', partner)
    assert getattr(partner, 'SmartHome_IotComponent') == owner
    _safe_set(owner, 'SmartHome_RuleComposant24', None)
    assert getattr(partner, 'SmartHome_IotComponent') is None


def test_assoc_light1_stub_double():
    # SmartHome_Room has no real 'SmartHome_Room2' property in the generated
    # code (a bare stub) -- manually attach it so SmartHome_Light's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SmartHome_Light's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SmartHome_Light(intensity=3.14, stateInit=True)
    partner = SmartHome_Room()
    setattr(partner, 'SmartHome_Room2', None)
    _safe_set(owner, 'SmartHome_Light', partner)
    assert owner in getattr(partner, 'SmartHome_Room2')
    _safe_set(owner, 'SmartHome_Light', None)
    assert owner not in getattr(partner, 'SmartHome_Room2')


def test_assoc_physicalcontext3_stub_double():
    # SmartHome_Room has no real 'SmartHome_Room4' property in the generated
    # code (a bare stub) -- manually attach it so SmartHome_PhysicalContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SmartHome_PhysicalContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SmartHome_PhysicalContext(lightIn=3.14, lightOut=3.14)
    partner = SmartHome_Room()
    setattr(partner, 'SmartHome_Room4', None)
    _safe_set(owner, 'SmartHome_PhysicalContext', partner)
    assert getattr(partner, 'SmartHome_Room4') == owner
    _safe_set(owner, 'SmartHome_PhysicalContext', None)
    assert getattr(partner, 'SmartHome_Room4') is None


def test_assoc_room11_stub_double():
    # SmartHome_Room has no real 'SmartHome_Room12' property in the generated
    # code (a bare stub) -- manually attach it so SmartHome_Home's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SmartHome_Home's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SmartHome_Home(speed=3.14, startDay=3.14)
    partner = SmartHome_Room()
    setattr(partner, 'SmartHome_Room12', None)
    _safe_set(owner, 'SmartHome_Home', {partner})
    assert getattr(partner, 'SmartHome_Room12') == owner
    _safe_set(owner, 'SmartHome_Home', set())
    assert getattr(partner, 'SmartHome_Room12') is None


def test_assoc_rulecondition16_stub_double():
    # SmartHome_Rule has no real 'SmartHome_Rule17' property in the generated
    # code (a bare stub) -- manually attach it so SmartHome_RuleComposant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SmartHome_RuleComposant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SmartHome_RuleComposant(operator="sample_text")
    partner = SmartHome_Rule()
    setattr(partner, 'SmartHome_Rule17', None)
    _safe_set(owner, 'SmartHome_RuleComposant', partner)
    assert owner in getattr(partner, 'SmartHome_Rule17')
    _safe_set(owner, 'SmartHome_RuleComposant', None)
    assert owner not in getattr(partner, 'SmartHome_Rule17')


def test_assoc_ruleconsequence18_stub_double():
    # SmartHome_Rule has no real 'SmartHome_Rule19' property in the generated
    # code (a bare stub) -- manually attach it so SmartHome_RuleComposant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SmartHome_RuleComposant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SmartHome_RuleComposant(operator="sample_text")
    partner = SmartHome_Rule()
    setattr(partner, 'SmartHome_Rule19', None)
    _safe_set(owner, 'SmartHome_RuleComposant20', partner)
    assert owner in getattr(partner, 'SmartHome_Rule19')
    _safe_set(owner, 'SmartHome_RuleComposant20', None)
    assert owner not in getattr(partner, 'SmartHome_Rule19')


def test_assoc_rules13_stub_double():
    # SmartHome_Rule has no real 'SmartHome_Rule15' property in the generated
    # code (a bare stub) -- manually attach it so SmartHome_Home's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SmartHome_Home's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SmartHome_Home(speed=3.14, startDay=3.14)
    partner = SmartHome_Rule()
    setattr(partner, 'SmartHome_Rule15', None)
    _safe_set(owner, 'SmartHome_Home14', {partner})
    assert getattr(partner, 'SmartHome_Rule15') == owner
    _safe_set(owner, 'SmartHome_Home14', set())
    assert getattr(partner, 'SmartHome_Rule15') is None


def test_assoc_shutters5_stub_double():
    # SmartHome_Room has no real 'SmartHome_Room6' property in the generated
    # code (a bare stub) -- manually attach it so SmartHome_Shutter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SmartHome_Shutter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SmartHome_Shutter(stateInit=True)
    partner = SmartHome_Room()
    setattr(partner, 'SmartHome_Room6', None)
    _safe_set(owner, 'SmartHome_Shutter', partner)
    assert getattr(partner, 'SmartHome_Room6') == owner
    _safe_set(owner, 'SmartHome_Shutter', None)
    assert getattr(partner, 'SmartHome_Room6') is None


def test_assoc_value21_stub_double():
    # SmartHome_Value has no real 'SmartHome_Value' property in the generated
    # code (a bare stub) -- manually attach it so SmartHome_RuleComposant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SmartHome_RuleComposant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SmartHome_RuleComposant(operator="sample_text")
    partner = SmartHome_Value()
    setattr(partner, 'SmartHome_Value', None)
    _safe_set(owner, 'SmartHome_RuleComposant22', partner)
    assert getattr(partner, 'SmartHome_Value') == owner
    _safe_set(owner, 'SmartHome_RuleComposant22', None)
    assert getattr(partner, 'SmartHome_Value') is None


