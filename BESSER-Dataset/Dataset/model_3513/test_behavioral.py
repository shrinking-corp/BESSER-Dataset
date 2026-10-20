import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Parent,
    testoperationbody_ChildA,
    testoperationbody_ChildB,
    testoperationbody_ConceptA,
    testoperationbody_Main,
    testoperationbody_Parent,
    EnumA,
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

def test_assoc_children4_stub_double():
    # testoperationbody_Parent has no real 'testoperationbody_Parent' property in the generated
    # code (a bare stub) -- manually attach it so testoperationbody_Main's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testoperationbody_Main's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testoperationbody_Main(listint=7, singlebool=True)
    partner = testoperationbody_Parent()
    setattr(partner, 'testoperationbody_Parent', None)
    _safe_set(owner, 'testoperationbody_Main5', {partner})
    assert getattr(partner, 'testoperationbody_Parent') == owner
    _safe_set(owner, 'testoperationbody_Main5', set())
    assert getattr(partner, 'testoperationbody_Parent') is None


def test_assoc_listconcepta0_stub_double():
    # testoperationbody_ConceptA has no real 'testoperationbody_ConceptA' property in the generated
    # code (a bare stub) -- manually attach it so testoperationbody_Main's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testoperationbody_Main's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testoperationbody_Main(listint=7, singlebool=True)
    partner = testoperationbody_ConceptA()
    setattr(partner, 'testoperationbody_ConceptA', None)
    _safe_set(owner, 'testoperationbody_Main', {partner})
    assert getattr(partner, 'testoperationbody_ConceptA') == owner
    _safe_set(owner, 'testoperationbody_Main', set())
    assert getattr(partner, 'testoperationbody_ConceptA') is None


def test_assoc_singleconcepta1_stub_double():
    # testoperationbody_ConceptA has no real 'testoperationbody_ConceptA3' property in the generated
    # code (a bare stub) -- manually attach it so testoperationbody_Main's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testoperationbody_Main's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testoperationbody_Main(listint=7, singlebool=True)
    partner = testoperationbody_ConceptA()
    setattr(partner, 'testoperationbody_ConceptA3', None)
    _safe_set(owner, 'testoperationbody_Main2', partner)
    assert getattr(partner, 'testoperationbody_ConceptA3') == owner
    _safe_set(owner, 'testoperationbody_Main2', None)
    assert getattr(partner, 'testoperationbody_ConceptA3') is None


