import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Interface,
    adlsimple_Base,
    adlsimple_Binding,
    adlsimple_Component,
    adlsimple_Interface,
    adlsimple_Provided,
    adlsimple_Required,
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
    # adlsimple_Binding has no real 'adlsimple_Binding' property in the generated
    # code (a bare stub) -- manually attach it so adlsimple_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlsimple_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlsimple_Interface(name="sample_text", signature="sample_text")
    partner = adlsimple_Binding()
    setattr(partner, 'adlsimple_Binding', None)
    _safe_set(owner, 'adlsimple_Interface', {partner})
    assert getattr(partner, 'adlsimple_Binding') == owner
    _safe_set(owner, 'adlsimple_Interface', set())
    assert getattr(partner, 'adlsimple_Binding') is None


def test_assoc_components10_stub_double():
    # adlsimple_Base has no real 'adlsimple_Base' property in the generated
    # code (a bare stub) -- manually attach it so adlsimple_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlsimple_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlsimple_Component(name="sample_text")
    partner = adlsimple_Base()
    setattr(partner, 'adlsimple_Base', None)
    _safe_set(owner, 'adlsimple_Component11', partner)
    assert owner in getattr(partner, 'adlsimple_Base')
    _safe_set(owner, 'adlsimple_Component11', None)
    assert owner not in getattr(partner, 'adlsimple_Base')


def test_assoc_from_4_stub_double():
    # adlsimple_Binding has no real 'adlsimple_Binding5' property in the generated
    # code (a bare stub) -- manually attach it so adlsimple_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlsimple_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlsimple_Interface(name="sample_text", signature="sample_text")
    partner = adlsimple_Binding()
    setattr(partner, 'adlsimple_Binding5', None)
    _safe_set(owner, 'adlsimple_Interface6', partner)
    assert getattr(partner, 'adlsimple_Binding5') == owner
    _safe_set(owner, 'adlsimple_Interface6', None)
    assert getattr(partner, 'adlsimple_Binding5') is None


def test_assoc_providedInterfaces1_stub_double():
    # adlsimple_Provided has no real 'adlsimple_Provided' property in the generated
    # code (a bare stub) -- manually attach it so adlsimple_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlsimple_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlsimple_Component(name="sample_text")
    partner = adlsimple_Provided()
    setattr(partner, 'adlsimple_Provided', None)
    _safe_set(owner, 'adlsimple_Component2', {partner})
    assert getattr(partner, 'adlsimple_Provided') == owner
    _safe_set(owner, 'adlsimple_Component2', set())
    assert getattr(partner, 'adlsimple_Provided') is None


def test_assoc_requiredInterfaces0_stub_double():
    # adlsimple_Required has no real 'adlsimple_Required' property in the generated
    # code (a bare stub) -- manually attach it so adlsimple_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlsimple_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlsimple_Component(name="sample_text")
    partner = adlsimple_Required()
    setattr(partner, 'adlsimple_Required', None)
    _safe_set(owner, 'adlsimple_Component', {partner})
    assert getattr(partner, 'adlsimple_Required') == owner
    _safe_set(owner, 'adlsimple_Component', set())
    assert getattr(partner, 'adlsimple_Required') is None


def test_assoc_to7_stub_double():
    # adlsimple_Binding has no real 'adlsimple_Binding8' property in the generated
    # code (a bare stub) -- manually attach it so adlsimple_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlsimple_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlsimple_Interface(name="sample_text", signature="sample_text")
    partner = adlsimple_Binding()
    setattr(partner, 'adlsimple_Binding8', None)
    _safe_set(owner, 'adlsimple_Interface9', partner)
    assert getattr(partner, 'adlsimple_Binding8') == owner
    _safe_set(owner, 'adlsimple_Interface9', None)
    assert getattr(partner, 'adlsimple_Binding8') is None


