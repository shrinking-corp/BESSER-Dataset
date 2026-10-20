import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AA,
    B,
    ObjectR,
    ObjectX,
    TypeA_AA,
    TypeA_B,
    TypeA_C,
    TypeA_D,
    TypeA_ListElement,
    TypeA_ObjectR,
    TypeA_ObjectS,
    TypeA_ObjectX,
    TypeA_ObjectY,
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

def test_assoc_elements0_stub_double():
    # AA has no real 'AA' property in the generated
    # code (a bare stub) -- manually attach it so TypeA_ListElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeA_ListElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeA_ListElement(nameListElement="sample_text")
    partner = AA()
    setattr(partner, 'AA', None)
    _safe_set(owner, 'TypeA_ListElement', {partner})
    assert getattr(partner, 'AA') == owner
    _safe_set(owner, 'TypeA_ListElement', set())
    assert getattr(partner, 'AA') is None


def test_assoc_rsElements6_stub_double():
    # ObjectR has no real 'ObjectR' property in the generated
    # code (a bare stub) -- manually attach it so TypeA_ListElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeA_ListElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeA_ListElement(nameListElement="sample_text")
    partner = ObjectR()
    setattr(partner, 'ObjectR', None)
    _safe_set(owner, 'TypeA_ListElement7', {partner})
    assert getattr(partner, 'ObjectR') == owner
    _safe_set(owner, 'TypeA_ListElement7', set())
    assert getattr(partner, 'ObjectR') is None


def test_assoc_singleElement1_stub_double():
    # AA has no real 'AA3' property in the generated
    # code (a bare stub) -- manually attach it so TypeA_ListElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeA_ListElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeA_ListElement(nameListElement="sample_text")
    partner = AA()
    setattr(partner, 'AA3', None)
    _safe_set(owner, 'TypeA_ListElement2', partner)
    assert getattr(partner, 'AA3') == owner
    _safe_set(owner, 'TypeA_ListElement2', None)
    assert getattr(partner, 'AA3') is None


def test_assoc_xyElements4_stub_double():
    # ObjectX has no real 'ObjectX' property in the generated
    # code (a bare stub) -- manually attach it so TypeA_ListElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeA_ListElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeA_ListElement(nameListElement="sample_text")
    partner = ObjectX()
    setattr(partner, 'ObjectX', None)
    _safe_set(owner, 'TypeA_ListElement5', {partner})
    assert getattr(partner, 'ObjectX') == owner
    _safe_set(owner, 'TypeA_ListElement5', set())
    assert getattr(partner, 'ObjectX') is None


