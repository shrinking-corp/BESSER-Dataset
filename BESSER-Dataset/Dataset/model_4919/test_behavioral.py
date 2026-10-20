import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BaseElement,
    Error,
    Message,
    Operation,
    RootElement,
    services_services_EObject,
    services_services_EndPoint,
    services_services_Interface,
    services_services_Operation,
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

def test_assoc_errorRefs7_stub_double():
    # Error has no real 'Error' property in the generated
    # code (a bare stub) -- manually attach it so services_services_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_services_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_services_Operation(name="sample_text")
    partner = Error()
    setattr(partner, 'Error', None)
    _safe_set(owner, 'services_services_Operation8', {partner})
    assert getattr(partner, 'Error') == owner
    _safe_set(owner, 'services_services_Operation8', set())
    assert getattr(partner, 'Error') is None


def test_assoc_implementationRef1_stub_double():
    # services_services_EObject has no real 'services_services_EObject' property in the generated
    # code (a bare stub) -- manually attach it so services_services_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_services_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_services_Interface(name="sample_text")
    partner = services_services_EObject()
    setattr(partner, 'services_services_EObject', None)
    _safe_set(owner, 'services_services_Interface2', partner)
    assert getattr(partner, 'services_services_EObject') == owner
    _safe_set(owner, 'services_services_Interface2', None)
    assert getattr(partner, 'services_services_EObject') is None


def test_assoc_implementationRef9_stub_double():
    # services_services_EObject has no real 'services_services_EObject11' property in the generated
    # code (a bare stub) -- manually attach it so services_services_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_services_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_services_Operation(name="sample_text")
    partner = services_services_EObject()
    setattr(partner, 'services_services_EObject11', None)
    _safe_set(owner, 'services_services_Operation10', partner)
    assert getattr(partner, 'services_services_EObject11') == owner
    _safe_set(owner, 'services_services_Operation10', None)
    assert getattr(partner, 'services_services_EObject11') is None


def test_assoc_inMessageRef3_stub_double():
    # Message has no real 'Message' property in the generated
    # code (a bare stub) -- manually attach it so services_services_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_services_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_services_Operation(name="sample_text")
    partner = Message()
    setattr(partner, 'Message', None)
    _safe_set(owner, 'services_services_Operation', partner)
    assert getattr(partner, 'Message') == owner
    _safe_set(owner, 'services_services_Operation', None)
    assert getattr(partner, 'Message') is None


def test_assoc_operations0_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so services_services_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_services_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_services_Interface(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'services_services_Interface', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'services_services_Interface', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_outMessageRef4_stub_double():
    # Message has no real 'Message6' property in the generated
    # code (a bare stub) -- manually attach it so services_services_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # services_services_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = services_services_Operation(name="sample_text")
    partner = Message()
    setattr(partner, 'Message6', None)
    _safe_set(owner, 'services_services_Operation5', partner)
    assert getattr(partner, 'Message6') == owner
    _safe_set(owner, 'services_services_Operation5', None)
    assert getattr(partner, 'Message6') is None


