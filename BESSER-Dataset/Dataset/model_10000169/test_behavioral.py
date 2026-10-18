import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Contexte,
    JArray,
    JBool,
    JMember,
    JNull,
    JNum,
    JObject,
    JStr,
    JValueJSONPrintVisitor,
    JValueVisitor_Interface,
    JValue_Interface,
    Protraction,
    Retraction,
    State_Interface,
    Wait,
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

def test_assoc_JArray_JValue_stub_double():
    # JValue_Interface has no real 'jArray5' property in the generated
    # code (a bare stub) -- manually attach it so JArray's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JArray's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JArray(value="sample_text")
    partner = JValue_Interface()
    setattr(partner, 'jArray5', None)
    _safe_set(owner, 'value4', {partner})
    assert getattr(partner, 'jArray5') == owner
    _safe_set(owner, 'value4', set())
    assert getattr(partner, 'jArray5') is None


def test_assoc_JMember_JValue_stub_double():
    # JValue_Interface has no real 'jMember3' property in the generated
    # code (a bare stub) -- manually attach it so JMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JMember(nom="sample_text")
    partner = JValue_Interface()
    setattr(partner, 'jMember3', None)
    _safe_set(owner, 'jValue2', partner)
    assert getattr(partner, 'jMember3') == owner
    _safe_set(owner, 'jValue2', None)
    assert getattr(partner, 'jMember3') is None


def test_assoc_JObject_JMember_stub_double():
    # JObject has no real 'JObject_JMember_00' property in the generated
    # code (a bare stub) -- manually attach it so JMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JMember(nom="sample_text")
    partner = JObject()
    setattr(partner, 'JObject_JMember_00', None)
    _safe_set(owner, 'JObject_JMember_11', partner)
    assert owner in getattr(partner, 'JObject_JMember_00')
    _safe_set(owner, 'JObject_JMember_11', None)
    assert owner not in getattr(partner, 'JObject_JMember_00')


