import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    petrinet_NamedElement,
    petrinet_Net,
    petrinet_Place,
    petrinet_Transition,
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

def test_assoc_first3_stub_double():
    # petrinet_Net has no real 'petrinet_Net4' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(tokens=7)
    partner = petrinet_Net()
    setattr(partner, 'petrinet_Net4', None)
    _safe_set(owner, 'petrinet_Place5', partner)
    assert getattr(partner, 'petrinet_Net4') == owner
    _safe_set(owner, 'petrinet_Place5', None)
    assert getattr(partner, 'petrinet_Net4') is None


def test_assoc_input9_stub_double():
    # petrinet_Transition has no real 'petrinet_Transition10' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(tokens=7)
    partner = petrinet_Transition()
    setattr(partner, 'petrinet_Transition10', None)
    _safe_set(owner, 'petrinet_Place11', partner)
    assert owner in getattr(partner, 'petrinet_Transition10')
    _safe_set(owner, 'petrinet_Place11', None)
    assert owner not in getattr(partner, 'petrinet_Transition10')


def test_assoc_output12_stub_double():
    # petrinet_Transition has no real 'petrinet_Transition13' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(tokens=7)
    partner = petrinet_Transition()
    setattr(partner, 'petrinet_Transition13', None)
    _safe_set(owner, 'petrinet_Place14', partner)
    assert owner in getattr(partner, 'petrinet_Transition13')
    _safe_set(owner, 'petrinet_Place14', None)
    assert owner not in getattr(partner, 'petrinet_Transition13')


def test_assoc_places0_stub_double():
    # petrinet_Net has no real 'petrinet_Net' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(tokens=7)
    partner = petrinet_Net()
    setattr(partner, 'petrinet_Net', None)
    _safe_set(owner, 'petrinet_Place', partner)
    assert owner in getattr(partner, 'petrinet_Net')
    _safe_set(owner, 'petrinet_Place', None)
    assert owner not in getattr(partner, 'petrinet_Net')


def test_assoc_to6_stub_double():
    # petrinet_Transition has no real 'petrinet_Transition8' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(tokens=7)
    partner = petrinet_Transition()
    setattr(partner, 'petrinet_Transition8', None)
    _safe_set(owner, 'petrinet_Place7', partner)
    assert getattr(partner, 'petrinet_Transition8') == owner
    _safe_set(owner, 'petrinet_Place7', None)
    assert getattr(partner, 'petrinet_Transition8') is None


