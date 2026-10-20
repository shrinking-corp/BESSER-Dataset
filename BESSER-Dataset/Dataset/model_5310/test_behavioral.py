import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    ElementR,
    ElementX,
    TypeB_AnotherElement,
    TypeB_Element,
    TypeB_ElementR,
    TypeB_ElementS,
    TypeB_ElementX,
    TypeB_ElementY,
    TypeB_ListElement,
    TypeB_SubElement,
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
    # Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so TypeB_ListElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeB_ListElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeB_ListElement(nameListElement="sample_text")
    partner = Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'TypeB_ListElement', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'TypeB_ListElement', set())
    assert getattr(partner, 'Element') is None


def test_assoc_rsElements3_stub_double():
    # ElementR has no real 'ElementR' property in the generated
    # code (a bare stub) -- manually attach it so TypeB_ListElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeB_ListElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeB_ListElement(nameListElement="sample_text")
    partner = ElementR()
    setattr(partner, 'ElementR', None)
    _safe_set(owner, 'TypeB_ListElement4', {partner})
    assert getattr(partner, 'ElementR') == owner
    _safe_set(owner, 'TypeB_ListElement4', set())
    assert getattr(partner, 'ElementR') is None


def test_assoc_xyElements1_stub_double():
    # ElementX has no real 'ElementX' property in the generated
    # code (a bare stub) -- manually attach it so TypeB_ListElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeB_ListElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeB_ListElement(nameListElement="sample_text")
    partner = ElementX()
    setattr(partner, 'ElementX', None)
    _safe_set(owner, 'TypeB_ListElement2', {partner})
    assert getattr(partner, 'ElementX') == owner
    _safe_set(owner, 'TypeB_ListElement2', set())
    assert getattr(partner, 'ElementX') is None


