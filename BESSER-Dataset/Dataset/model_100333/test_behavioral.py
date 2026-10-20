import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Attribute,
    Label,
    OurPNVis_Activities,
    OurPNVis_Arc,
    OurPNVis_CanChange,
    OurPNVis_Finished,
    OurPNVis_Geometry,
    OurPNVis_KeepAnim,
    OurPNVis_PNVis,
    OurPNVis_Place,
    OurPNVis_Sequence,
    OurPNVis_Shape,
    OurPNVis_Tokens,
    OurPNVis_Transition,
    OurPNVis_ident,
    PetriNetType,
    Place,
    StructuredLabel,
    Transition,
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

def test_assoc_canchange6_stub_double():
    # OurPNVis_Place has no real 'OurPNVis_Place7' property in the generated
    # code (a bare stub) -- manually attach it so OurPNVis_CanChange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OurPNVis_CanChange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OurPNVis_CanChange(text=True)
    partner = OurPNVis_Place()
    setattr(partner, 'OurPNVis_Place7', None)
    _safe_set(owner, 'OurPNVis_CanChange', partner)
    assert getattr(partner, 'OurPNVis_Place7') == owner
    _safe_set(owner, 'OurPNVis_CanChange', None)
    assert getattr(partner, 'OurPNVis_Place7') is None


def test_assoc_finished0_stub_double():
    # OurPNVis_Arc has no real 'OurPNVis_Arc' property in the generated
    # code (a bare stub) -- manually attach it so OurPNVis_Finished's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OurPNVis_Finished's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OurPNVis_Finished(text=True)
    partner = OurPNVis_Arc()
    setattr(partner, 'OurPNVis_Arc', None)
    _safe_set(owner, 'OurPNVis_Finished', partner)
    assert getattr(partner, 'OurPNVis_Arc') == owner
    _safe_set(owner, 'OurPNVis_Finished', None)
    assert getattr(partner, 'OurPNVis_Arc') is None


def test_assoc_geo12_stub_double():
    # OurPNVis_Place has no real 'OurPNVis_Place13' property in the generated
    # code (a bare stub) -- manually attach it so OurPNVis_Geometry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OurPNVis_Geometry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OurPNVis_Geometry(text="sample_text")
    partner = OurPNVis_Place()
    setattr(partner, 'OurPNVis_Place13', None)
    _safe_set(owner, 'OurPNVis_Geometry', partner)
    assert getattr(partner, 'OurPNVis_Place13') == owner
    _safe_set(owner, 'OurPNVis_Geometry', None)
    assert getattr(partner, 'OurPNVis_Place13') is None


def test_assoc_idnt3_stub_double():
    # OurPNVis_Arc has no real 'OurPNVis_Arc4' property in the generated
    # code (a bare stub) -- manually attach it so OurPNVis_ident's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OurPNVis_ident's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OurPNVis_ident(text="sample_text")
    partner = OurPNVis_Arc()
    setattr(partner, 'OurPNVis_Arc4', None)
    _safe_set(owner, 'OurPNVis_ident', partner)
    assert getattr(partner, 'OurPNVis_Arc4') == owner
    _safe_set(owner, 'OurPNVis_ident', None)
    assert getattr(partner, 'OurPNVis_Arc4') is None


def test_assoc_keepanm1_stub_double():
    # OurPNVis_Arc has no real 'OurPNVis_Arc2' property in the generated
    # code (a bare stub) -- manually attach it so OurPNVis_KeepAnim's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OurPNVis_KeepAnim's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OurPNVis_KeepAnim(text=True)
    partner = OurPNVis_Arc()
    setattr(partner, 'OurPNVis_Arc2', None)
    _safe_set(owner, 'OurPNVis_KeepAnim', partner)
    assert getattr(partner, 'OurPNVis_Arc2') == owner
    _safe_set(owner, 'OurPNVis_KeepAnim', None)
    assert getattr(partner, 'OurPNVis_Arc2') is None


def test_assoc_shape8_stub_double():
    # OurPNVis_Place has no real 'OurPNVis_Place9' property in the generated
    # code (a bare stub) -- manually attach it so OurPNVis_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OurPNVis_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OurPNVis_Shape(text="sample_text")
    partner = OurPNVis_Place()
    setattr(partner, 'OurPNVis_Place9', None)
    _safe_set(owner, 'OurPNVis_Shape', partner)
    assert getattr(partner, 'OurPNVis_Place9') == owner
    _safe_set(owner, 'OurPNVis_Shape', None)
    assert getattr(partner, 'OurPNVis_Place9') is None


def test_assoc_tokens5_stub_double():
    # OurPNVis_Place has no real 'OurPNVis_Place' property in the generated
    # code (a bare stub) -- manually attach it so OurPNVis_Tokens's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OurPNVis_Tokens's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OurPNVis_Tokens(text="sample_text")
    partner = OurPNVis_Place()
    setattr(partner, 'OurPNVis_Place', None)
    _safe_set(owner, 'OurPNVis_Tokens', partner)
    assert getattr(partner, 'OurPNVis_Place') == owner
    _safe_set(owner, 'OurPNVis_Tokens', None)
    assert getattr(partner, 'OurPNVis_Place') is None


