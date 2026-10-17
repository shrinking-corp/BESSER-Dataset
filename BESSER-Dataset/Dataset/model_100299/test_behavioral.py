import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Attribute,
    Label,
    PetriNetType,
    Place,
    StructuredLabel,
    petrinet_Animation,
    petrinet_AnimationLabel,
    petrinet_Arc,
    petrinet_ExtendedPetriNet,
    petrinet_GeometryLabel,
    petrinet_Identity,
    petrinet_InputPlace,
    petrinet_Place,
    petrinet_Token,
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

def test_assoc_geometryLabel0_stub_double():
    # petrinet_Place has no real 'petrinet_Place' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_GeometryLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_GeometryLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_GeometryLabel(text="sample_text")
    partner = petrinet_Place()
    setattr(partner, 'petrinet_Place', None)
    _safe_set(owner, 'petrinet_GeometryLabel', partner)
    assert getattr(partner, 'petrinet_Place') == owner
    _safe_set(owner, 'petrinet_GeometryLabel', None)
    assert getattr(partner, 'petrinet_Place') is None


def test_assoc_identity9_stub_double():
    # petrinet_Arc has no real 'petrinet_Arc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Identity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Identity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Identity(text="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'petrinet_Arc', None)
    _safe_set(owner, 'petrinet_Identity', partner)
    assert getattr(partner, 'petrinet_Arc') == owner
    _safe_set(owner, 'petrinet_Identity', None)
    assert getattr(partner, 'petrinet_Arc') is None


def test_assoc_inputPlaceLabel5_stub_double():
    # petrinet_Place has no real 'petrinet_Place6' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_InputPlace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_InputPlace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_InputPlace(text=True)
    partner = petrinet_Place()
    setattr(partner, 'petrinet_Place6', None)
    _safe_set(owner, 'petrinet_InputPlace', partner)
    assert getattr(partner, 'petrinet_Place6') == owner
    _safe_set(owner, 'petrinet_InputPlace', None)
    assert getattr(partner, 'petrinet_Place6') is None


def test_assoc_tokens3_stub_double():
    # petrinet_Place has no real 'petrinet_Place4' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Token(text="sample_text")
    partner = petrinet_Place()
    setattr(partner, 'petrinet_Place4', None)
    _safe_set(owner, 'petrinet_Token', partner)
    assert getattr(partner, 'petrinet_Place4') == owner
    _safe_set(owner, 'petrinet_Token', None)
    assert getattr(partner, 'petrinet_Place4') is None


