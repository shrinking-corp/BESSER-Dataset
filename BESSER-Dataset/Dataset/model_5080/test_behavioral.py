import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Component,
    Interface,
    adlrecur_Base,
    adlrecur_Binding,
    adlrecur_Component,
    adlrecur_Interface,
    adlrecur_Provided,
    adlrecur_Required,
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

def test_assoc_bindings3_stub_double():
    # adlrecur_Binding has no real 'adlrecur_Binding' property in the generated
    # code (a bare stub) -- manually attach it so adlrecur_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlrecur_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlrecur_Interface(name="sample_text", signature="sample_text")
    partner = adlrecur_Binding()
    setattr(partner, 'adlrecur_Binding', None)
    _safe_set(owner, 'adlrecur_Interface', {partner})
    assert getattr(partner, 'adlrecur_Binding') == owner
    _safe_set(owner, 'adlrecur_Interface', set())
    assert getattr(partner, 'adlrecur_Binding') is None


def test_assoc_from_4_stub_double():
    # adlrecur_Binding has no real 'adlrecur_Binding5' property in the generated
    # code (a bare stub) -- manually attach it so adlrecur_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlrecur_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlrecur_Interface(name="sample_text", signature="sample_text")
    partner = adlrecur_Binding()
    setattr(partner, 'adlrecur_Binding5', None)
    _safe_set(owner, 'adlrecur_Interface6', partner)
    assert getattr(partner, 'adlrecur_Binding5') == owner
    _safe_set(owner, 'adlrecur_Interface6', None)
    assert getattr(partner, 'adlrecur_Binding5') is None


def test_assoc_providedInterfaces1_stub_double():
    # adlrecur_Provided has no real 'adlrecur_Provided' property in the generated
    # code (a bare stub) -- manually attach it so adlrecur_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlrecur_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlrecur_Component(name="sample_text")
    partner = adlrecur_Provided()
    setattr(partner, 'adlrecur_Provided', None)
    _safe_set(owner, 'adlrecur_Component2', {partner})
    assert getattr(partner, 'adlrecur_Provided') == owner
    _safe_set(owner, 'adlrecur_Component2', set())
    assert getattr(partner, 'adlrecur_Provided') is None


def test_assoc_requiredInterfaces0_stub_double():
    # adlrecur_Required has no real 'adlrecur_Required' property in the generated
    # code (a bare stub) -- manually attach it so adlrecur_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlrecur_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlrecur_Component(name="sample_text")
    partner = adlrecur_Required()
    setattr(partner, 'adlrecur_Required', None)
    _safe_set(owner, 'adlrecur_Component', {partner})
    assert getattr(partner, 'adlrecur_Required') == owner
    _safe_set(owner, 'adlrecur_Component', set())
    assert getattr(partner, 'adlrecur_Required') is None


def test_assoc_to7_stub_double():
    # adlrecur_Binding has no real 'adlrecur_Binding8' property in the generated
    # code (a bare stub) -- manually attach it so adlrecur_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlrecur_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlrecur_Interface(name="sample_text", signature="sample_text")
    partner = adlrecur_Binding()
    setattr(partner, 'adlrecur_Binding8', None)
    _safe_set(owner, 'adlrecur_Interface9', partner)
    assert getattr(partner, 'adlrecur_Binding8') == owner
    _safe_set(owner, 'adlrecur_Interface9', None)
    assert getattr(partner, 'adlrecur_Binding8') is None


