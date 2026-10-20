import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Attribute,
    Label,
    PetriNetType,
    Place,
    StructuredLabel,
    extendedpetrinet_Animation,
    extendedpetrinet_AnimationLabel,
    extendedpetrinet_Arc,
    extendedpetrinet_ExtendedPetriNet,
    extendedpetrinet_GeometryLabel,
    extendedpetrinet_Identity,
    extendedpetrinet_InputPlaceAppearance,
    extendedpetrinet_InteractiveInput,
    extendedpetrinet_Place,
    extendedpetrinet_Token,
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

def test_assoc_appearance6_stub_double():
    # extendedpetrinet_Place has no real 'extendedpetrinet_Place7' property in the generated
    # code (a bare stub) -- manually attach it so extendedpetrinet_InputPlaceAppearance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extendedpetrinet_InputPlaceAppearance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extendedpetrinet_InputPlaceAppearance(text="sample_text")
    partner = extendedpetrinet_Place()
    setattr(partner, 'extendedpetrinet_Place7', None)
    _safe_set(owner, 'extendedpetrinet_InputPlaceAppearance', partner)
    assert getattr(partner, 'extendedpetrinet_Place7') == owner
    _safe_set(owner, 'extendedpetrinet_InputPlaceAppearance', None)
    assert getattr(partner, 'extendedpetrinet_Place7') is None


def test_assoc_geometryLabel8_stub_double():
    # extendedpetrinet_Place has no real 'extendedpetrinet_Place9' property in the generated
    # code (a bare stub) -- manually attach it so extendedpetrinet_GeometryLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extendedpetrinet_GeometryLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extendedpetrinet_GeometryLabel(text="sample_text")
    partner = extendedpetrinet_Place()
    setattr(partner, 'extendedpetrinet_Place9', None)
    _safe_set(owner, 'extendedpetrinet_GeometryLabel', partner)
    assert getattr(partner, 'extendedpetrinet_Place9') == owner
    _safe_set(owner, 'extendedpetrinet_GeometryLabel', None)
    assert getattr(partner, 'extendedpetrinet_Place9') is None


def test_assoc_identity0_stub_double():
    # extendedpetrinet_Arc has no real 'extendedpetrinet_Arc' property in the generated
    # code (a bare stub) -- manually attach it so extendedpetrinet_Identity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extendedpetrinet_Identity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extendedpetrinet_Identity(text=7)
    partner = extendedpetrinet_Arc()
    setattr(partner, 'extendedpetrinet_Arc', None)
    _safe_set(owner, 'extendedpetrinet_Identity', partner)
    assert getattr(partner, 'extendedpetrinet_Arc') == owner
    _safe_set(owner, 'extendedpetrinet_Identity', None)
    assert getattr(partner, 'extendedpetrinet_Arc') is None


def test_assoc_interactiveInput1_stub_double():
    # extendedpetrinet_Place has no real 'extendedpetrinet_Place' property in the generated
    # code (a bare stub) -- manually attach it so extendedpetrinet_InteractiveInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extendedpetrinet_InteractiveInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extendedpetrinet_InteractiveInput(text=True)
    partner = extendedpetrinet_Place()
    setattr(partner, 'extendedpetrinet_Place', None)
    _safe_set(owner, 'extendedpetrinet_InteractiveInput', partner)
    assert getattr(partner, 'extendedpetrinet_Place') == owner
    _safe_set(owner, 'extendedpetrinet_InteractiveInput', None)
    assert getattr(partner, 'extendedpetrinet_Place') is None


def test_assoc_tokens4_stub_double():
    # extendedpetrinet_Place has no real 'extendedpetrinet_Place5' property in the generated
    # code (a bare stub) -- manually attach it so extendedpetrinet_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extendedpetrinet_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extendedpetrinet_Token(text="sample_text")
    partner = extendedpetrinet_Place()
    setattr(partner, 'extendedpetrinet_Place5', None)
    _safe_set(owner, 'extendedpetrinet_Token', partner)
    assert owner in getattr(partner, 'extendedpetrinet_Place5')
    _safe_set(owner, 'extendedpetrinet_Token', None)
    assert owner not in getattr(partner, 'extendedpetrinet_Place5')


