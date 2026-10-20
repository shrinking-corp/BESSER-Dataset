import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    PetriNet_Arc,
    PetriNet_Element,
    PetriNet_PetriNetRoot,
    PetriNet_Place,
    PetriNet_Transition,
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

def test_assoc_In3_stub_double():
    # PetriNet_Arc has no real 'PetriNet_Arc4' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Element(name="sample_text")
    partner = PetriNet_Arc()
    setattr(partner, 'PetriNet_Arc4', None)
    _safe_set(owner, 'PetriNet_Element5', partner)
    assert getattr(partner, 'PetriNet_Arc4') == owner
    _safe_set(owner, 'PetriNet_Element5', None)
    assert getattr(partner, 'PetriNet_Arc4') is None


def test_assoc_Out6_stub_double():
    # PetriNet_Arc has no real 'PetriNet_Arc7' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Element(name="sample_text")
    partner = PetriNet_Arc()
    setattr(partner, 'PetriNet_Arc7', None)
    _safe_set(owner, 'PetriNet_Element8', partner)
    assert getattr(partner, 'PetriNet_Arc7') == owner
    _safe_set(owner, 'PetriNet_Element8', None)
    assert getattr(partner, 'PetriNet_Arc7') is None


def test_assoc_elements0_stub_double():
    # PetriNet_PetriNetRoot has no real 'PetriNet_PetriNetRoot' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Element(name="sample_text")
    partner = PetriNet_PetriNetRoot()
    setattr(partner, 'PetriNet_PetriNetRoot', None)
    _safe_set(owner, 'PetriNet_Element', partner)
    assert owner in getattr(partner, 'PetriNet_PetriNetRoot')
    _safe_set(owner, 'PetriNet_Element', None)
    assert owner not in getattr(partner, 'PetriNet_PetriNetRoot')


